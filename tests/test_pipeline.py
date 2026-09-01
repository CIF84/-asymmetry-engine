from dataclasses import replace
from datetime import datetime, timezone

from asymmetry_engine.db import Repository
from asymmetry_engine.pipeline import run_collection
from asymmetry_engine.sources.stackexchange import normalize_question, source_for_site


NOW = datetime(2026, 9, 1, 12, tzinfo=timezone.utc)


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
