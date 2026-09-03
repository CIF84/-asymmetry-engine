import json
import sqlite3
from dataclasses import replace
from datetime import datetime, timedelta, timezone

import pytest

from asymmetry_engine.db import Repository
from asymmetry_engine.pipeline import run_collection
from asymmetry_engine.sources.stackexchange import normalize_question, source_for_site


NOW = datetime(2026, 9, 1, 12, tzinfo=timezone.utc)
LATER = NOW + timedelta(hours=1)


class FakeCollector:
    source = source_for_site("money")

    def __init__(self, observations=None, error=None):
        self.observations = observations or []
        self.error = error

    def collect(self):
        if self.error:
            raise self.error
        return self.observations


def observation(question_id=42):
    return normalize_question(
        {
            "question_id": question_id,
            "creation_date": 1_700_000_000,
            "title": f"Question {question_id}",
            "link": f"https://money.stackexchange.com/questions/{question_id}",
            "tags": ["saving"],
            "score": 1,
        },
        "money",
        NOW,
    )


def test_success_persists_source_run_and_deduplicates(tmp_path):
    repository = Repository(tmp_path / "test.db")
    first = run_collection(FakeCollector([observation()]), repository, lambda: NOW)
    second = run_collection(FakeCollector([observation()]), repository, lambda: NOW)
    assert (first.status, first.fetched_count, first.inserted_count, first.duplicate_count) == (
        "succeeded", 1, 1, 0
    )
    assert (second.inserted_count, second.duplicate_count) == (0, 1)
    assert repository.connection.execute("SELECT count(*) FROM source_observations").fetchone()[0] == 1
    source = repository.connection.execute("SELECT * FROM signal_sources").fetchone()
    assert "Self-selected" in source["selection_biases"]
    assert repository.get_run(first.run_id)["status"] == "succeeded"
    repository.close()


def test_collection_failure_is_recorded(tmp_path):
    repository = Repository(tmp_path / "test.db")
    result = run_collection(FakeCollector(error=RuntimeError("offline")), repository, lambda: NOW)
    row = repository.get_run(result.run_id)
    assert result.status == "failed"
    assert row["status"] == "failed"
    assert "offline" in row["error"]
    assert repository.connection.execute("SELECT count(*) FROM source_observations").fetchone()[0] == 0
    repository.close()


def test_non_deduplication_constraint_failure_rolls_back_entire_batch(tmp_path):
    repository = Repository(tmp_path / "test.db")
    invalid = replace(observation(2), content=None)
    result = run_collection(
        FakeCollector([observation(1), invalid]), repository, lambda: NOW
    )
    assert result.status == "failed"
    assert result.fetched_count == 2
    assert result.duplicate_count == 0
    assert "NOT NULL constraint failed" in result.error
    assert repository.get_run(result.run_id)["status"] == "failed"
    assert repository.connection.execute("SELECT count(*) FROM source_observations").fetchone()[0] == 0
    repository.close()


def captures(repository, question_id=42):
    return repository.connection.execute(
        """SELECT * FROM source_observations
           WHERE source_id=? AND external_id=? ORDER BY capture_sequence""",
        ("stackexchange:money", f"money:question:{question_id}"),
    ).fetchall()


def test_unchanged_recapture_preserves_original_capture_and_run(tmp_path):
    repository = Repository(tmp_path / "test.db")
    first = run_collection(FakeCollector([observation()]), repository, lambda: NOW)
    second_observation = replace(observation(), observed_at=LATER)
    second = run_collection(FakeCollector([second_observation]), repository, lambda: LATER)

    rows = captures(repository)
    assert (second.inserted_count, second.duplicate_count) == (0, 1)
    assert len(rows) == 1
    assert rows[0]["capture_sequence"] == 1
    assert rows[0]["observed_at"] == "2026-09-01T12:00:00Z"
    assert rows[0]["pipeline_run_id"] == first.run_id
    repository.close()


@pytest.mark.parametrize(
    "changed",
    [
        lambda item: replace(item, content="changed content"),
        lambda item: replace(item, metadata={**item.metadata, "score": 99}),
        lambda item: replace(item, occurred_at=item.occurred_at + timedelta(days=1)),
        lambda item: replace(item, canonical_url="https://example.invalid/changed"),
        lambda item: replace(item, item_kind="changed_kind"),
    ],
    ids=("content", "metadata", "occurred-at", "canonical-url", "item-kind"),
)
def test_material_change_creates_new_capture(tmp_path, changed):
    repository = Repository(tmp_path / "test.db")
    first = run_collection(FakeCollector([observation()]), repository, lambda: NOW)
    revised = replace(changed(observation()), observed_at=LATER)
    second = run_collection(FakeCollector([revised]), repository, lambda: LATER)

    rows = captures(repository)
    assert (first.inserted_count, first.duplicate_count) == (1, 0)
    assert (second.inserted_count, second.duplicate_count) == (1, 0)
    assert [row["capture_sequence"] for row in rows] == [1, 2]
    assert [row["pipeline_run_id"] for row in rows] == [first.run_id, second.run_id]
    repository.close()


def test_reversion_compares_with_latest_capture_and_stores_a_b_a(tmp_path):
    repository = Repository(tmp_path / "test.db")
    state_a = observation()
    state_b = replace(state_a, content="state B", observed_at=LATER)
    state_a_again = replace(state_a, observed_at=LATER + timedelta(hours=1))

    results = [
        run_collection(FakeCollector([state_a]), repository, lambda: NOW),
        run_collection(FakeCollector([state_b]), repository, lambda: LATER),
        run_collection(
            FakeCollector([state_a_again]),
            repository,
            lambda: LATER + timedelta(hours=1),
        ),
    ]

    assert [(result.inserted_count, result.duplicate_count) for result in results] == [
        (1, 0),
        (1, 0),
        (1, 0),
    ]
    assert [row["content"] for row in captures(repository)] == [
        state_a.content,
        "state B",
        state_a.content,
    ]
    repository.close()


def test_mixed_batch_counts_changed_unchanged_and_first_seen(tmp_path):
    repository = Repository(tmp_path / "test.db")
    run_collection(
        FakeCollector([observation(1), observation(2)]), repository, lambda: NOW
    )
    mixed = [
        replace(observation(1), content="changed", observed_at=LATER),
        replace(observation(2), observed_at=LATER),
        replace(observation(3), observed_at=LATER),
    ]
    result = run_collection(FakeCollector(mixed), repository, lambda: LATER)

    assert (result.fetched_count, result.inserted_count, result.duplicate_count) == (
        3,
        2,
        1,
    )
    assert len(captures(repository, 1)) == 2
    assert len(captures(repository, 2)) == 1
    assert len(captures(repository, 3)) == 1
    repository.close()


def test_latest_observations_returns_one_deterministic_current_capture_per_item(tmp_path):
    repository = Repository(tmp_path / "test.db")
    run_collection(
        FakeCollector([observation(2), observation(1)]), repository, lambda: NOW
    )
    run_collection(
        FakeCollector([replace(observation(1), content="latest", observed_at=LATER)]),
        repository,
        lambda: LATER,
    )

    rows = repository.latest_observations("stackexchange:money")
    assert [row["external_id"] for row in rows] == [
        "money:question:1",
        "money:question:2",
    ]
    assert [(row["capture_sequence"], row["content"]) for row in rows] == [
        (2, "latest"),
        (1, "Question 2"),
    ]
    repository.close()


def create_legacy_database(path):
    source = source_for_site("money")
    item = observation()
    connection = sqlite3.connect(path)
    connection.executescript(
        """
        CREATE TABLE signal_sources (
            source_id TEXT PRIMARY KEY, name TEXT NOT NULL, access_method TEXT NOT NULL,
            terms_reference TEXT NOT NULL, commercial_use_considerations TEXT NOT NULL,
            selection_biases TEXT NOT NULL, metadata_json TEXT NOT NULL
        );
        CREATE TABLE pipeline_runs (
            run_id TEXT PRIMARY KEY, source_id TEXT NOT NULL, started_at TEXT NOT NULL,
            completed_at TEXT, status TEXT NOT NULL CHECK (status IN ('running', 'succeeded', 'failed')),
            fetched_count INTEGER NOT NULL DEFAULT 0, inserted_count INTEGER NOT NULL DEFAULT 0,
            duplicate_count INTEGER NOT NULL DEFAULT 0, error TEXT,
            FOREIGN KEY (source_id) REFERENCES signal_sources(source_id)
        );
        CREATE TABLE source_observations (
            observation_id INTEGER PRIMARY KEY, source_id TEXT NOT NULL, external_id TEXT NOT NULL,
            observed_at TEXT NOT NULL, occurred_at TEXT, item_kind TEXT NOT NULL,
            content TEXT NOT NULL, canonical_url TEXT, metadata_json TEXT NOT NULL,
            pipeline_run_id TEXT NOT NULL, UNIQUE (source_id, external_id),
            FOREIGN KEY (source_id) REFERENCES signal_sources(source_id),
            FOREIGN KEY (pipeline_run_id) REFERENCES pipeline_runs(run_id)
        );
        """
    )
    connection.execute(
        "INSERT INTO signal_sources VALUES (?, ?, ?, ?, ?, ?, ?)",
        (
            source.source_id,
            source.name,
            source.access_method,
            source.terms_reference,
            source.commercial_use_considerations,
            source.selection_biases,
            json.dumps(source.metadata, sort_keys=True),
        ),
    )
    connection.execute(
        """INSERT INTO pipeline_runs
           (run_id, source_id, started_at, completed_at, status,
            fetched_count, inserted_count, duplicate_count)
           VALUES ('legacy-run', ?, ?, ?, 'succeeded', 1, 1, 0)""",
        (
            source.source_id,
            NOW.isoformat().replace("+00:00", "Z"),
            NOW.isoformat().replace("+00:00", "Z"),
        ),
    )
    connection.execute(
        """INSERT INTO source_observations
           (observation_id, source_id, external_id, observed_at, occurred_at, item_kind,
            content, canonical_url, metadata_json, pipeline_run_id)
           VALUES (7, ?, ?, ?, ?, ?, ?, ?, ?, 'legacy-run')""",
        (
            item.source_id,
            item.external_id,
            item.observed_at.isoformat().replace("+00:00", "Z"),
            item.occurred_at.isoformat().replace("+00:00", "Z"),
            item.item_kind,
            item.content,
            item.canonical_url,
            json.dumps(item.metadata, sort_keys=True),
        ),
    )
    connection.commit()
    connection.close()


def test_legacy_database_migrates_idempotently_and_accepts_changed_recapture(tmp_path):
    path = tmp_path / "legacy.db"
    create_legacy_database(path)

    repository = Repository(path)
    migrated = captures(repository)
    assert len(migrated) == 1
    assert (migrated[0]["observation_id"], migrated[0]["capture_sequence"]) == (7, 1)
    original = observation()
    assert migrated[0]["source_id"] == original.source_id
    assert migrated[0]["external_id"] == original.external_id
    assert migrated[0]["observed_at"] == "2026-09-01T12:00:00Z"
    assert migrated[0]["occurred_at"] == "2023-11-14T22:13:20Z"
    assert migrated[0]["item_kind"] == original.item_kind
    assert migrated[0]["content"] == original.content
    assert migrated[0]["canonical_url"] == original.canonical_url
    assert json.loads(migrated[0]["metadata_json"]) == original.metadata
    assert migrated[0]["pipeline_run_id"] == "legacy-run"
    assert repository.connection.execute("PRAGMA foreign_key_check").fetchall() == []
    repository.close()

    reopened = Repository(path)
    assert [
        (row["observation_id"], row["capture_sequence"])
        for row in captures(reopened)
    ] == [(7, 1)]
    changed = replace(observation(), content="post-migration change", observed_at=LATER)
    result = run_collection(FakeCollector([changed]), reopened, lambda: LATER)
    assert (result.inserted_count, result.duplicate_count) == (1, 0)
    assert [row["capture_sequence"] for row in captures(reopened)] == [1, 2]
    reopened.close()


def test_legacy_migration_failure_rolls_back_schema_rebuild(tmp_path):
    path = tmp_path / "invalid-legacy.db"
    create_legacy_database(path)
    connection = sqlite3.connect(path)
    connection.execute("PRAGMA foreign_keys = OFF")
    connection.execute("DELETE FROM signal_sources")
    connection.commit()
    connection.close()

    with pytest.raises(sqlite3.IntegrityError, match="FOREIGN KEY constraint failed"):
        Repository(path)

    inspection = sqlite3.connect(path)
    columns = {
        row[1] for row in inspection.execute("PRAGMA table_info(source_observations)")
    }
    tables = {
        row[0]
        for row in inspection.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )
    }
    assert "capture_sequence" not in columns
    assert "source_observations_v038" not in tables
    assert inspection.execute("SELECT count(*) FROM source_observations").fetchone()[0] == 1
    inspection.close()
