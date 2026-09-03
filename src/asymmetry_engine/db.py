from __future__ import annotations

import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Iterable

from .models import SignalSource, SourceObservation, isoformat_utc

CORE_SCHEMA = """
CREATE TABLE IF NOT EXISTS signal_sources (
    source_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    access_method TEXT NOT NULL,
    terms_reference TEXT NOT NULL,
    commercial_use_considerations TEXT NOT NULL,
    selection_biases TEXT NOT NULL,
    metadata_json TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS pipeline_runs (
    run_id TEXT PRIMARY KEY,
    source_id TEXT NOT NULL,
    started_at TEXT NOT NULL,
    completed_at TEXT,
    status TEXT NOT NULL CHECK (status IN ('running', 'succeeded', 'failed')),
    fetched_count INTEGER NOT NULL DEFAULT 0,
    inserted_count INTEGER NOT NULL DEFAULT 0,
    duplicate_count INTEGER NOT NULL DEFAULT 0,
    error TEXT,
    FOREIGN KEY (source_id) REFERENCES signal_sources(source_id)
);
"""

OBSERVATION_TABLE = """
CREATE TABLE {table_name} (
    observation_id INTEGER PRIMARY KEY,
    source_id TEXT NOT NULL,
    external_id TEXT NOT NULL,
    capture_sequence INTEGER NOT NULL CHECK (capture_sequence > 0),
    observed_at TEXT NOT NULL,
    occurred_at TEXT,
    item_kind TEXT NOT NULL,
    content TEXT NOT NULL,
    canonical_url TEXT,
    metadata_json TEXT NOT NULL,
    pipeline_run_id TEXT NOT NULL,
    UNIQUE (source_id, external_id, capture_sequence),
    FOREIGN KEY (source_id) REFERENCES signal_sources(source_id),
    FOREIGN KEY (pipeline_run_id) REFERENCES pipeline_runs(run_id)
);
"""

LATEST_INDEX = """
CREATE INDEX IF NOT EXISTS source_observations_latest
ON source_observations (source_id, external_id, capture_sequence DESC)
"""


class Repository:
    def __init__(self, path: str | Path) -> None:
        self.path = str(path)
        self.connection = sqlite3.connect(self.path)
        self.connection.row_factory = sqlite3.Row
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.connection.executescript(CORE_SCHEMA)
        self._ensure_observation_schema()

    def _ensure_observation_schema(self) -> None:
        exists = self.connection.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='source_observations'"
        ).fetchone()
        if exists is None:
            with self.connection:
                self.connection.execute(
                    OBSERVATION_TABLE.format(table_name="source_observations")
                )
                self.connection.execute(LATEST_INDEX)
            return

        columns = {
            row["name"]
            for row in self.connection.execute("PRAGMA table_info(source_observations)")
        }
        if "capture_sequence" not in columns:
            self._migrate_legacy_observations()
        else:
            with self.connection:
                self.connection.execute(LATEST_INDEX)

    def _migrate_legacy_observations(self) -> None:
        self.connection.execute("BEGIN IMMEDIATE")
        try:
            self.connection.execute(
                OBSERVATION_TABLE.format(table_name="source_observations_v038")
            )
            self.connection.execute(
                """INSERT INTO source_observations_v038
                   (observation_id, source_id, external_id, capture_sequence,
                    observed_at, occurred_at, item_kind, content, canonical_url,
                    metadata_json, pipeline_run_id)
                   SELECT observation_id, source_id, external_id, 1,
                          observed_at, occurred_at, item_kind, content, canonical_url,
                          metadata_json, pipeline_run_id
                   FROM source_observations
                   ORDER BY observation_id"""
            )
            self.connection.execute("DROP TABLE source_observations")
            self.connection.execute(
                "ALTER TABLE source_observations_v038 RENAME TO source_observations"
            )
            self.connection.execute(LATEST_INDEX)
        except Exception:
            self.connection.rollback()
            raise
        else:
            self.connection.commit()

    def close(self) -> None:
        self.connection.close()

    def _upsert_source(self, source: SignalSource) -> None:
        self.connection.execute(
            """INSERT INTO signal_sources VALUES (?, ?, ?, ?, ?, ?, ?)
               ON CONFLICT(source_id) DO UPDATE SET
                 name=excluded.name, access_method=excluded.access_method,
                 terms_reference=excluded.terms_reference,
                 commercial_use_considerations=excluded.commercial_use_considerations,
                 selection_biases=excluded.selection_biases,
                 metadata_json=excluded.metadata_json""",
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

    def start_run(self, run_id: str, source: SignalSource, started_at: datetime) -> None:
        with self.connection:
            self._upsert_source(source)
            self.connection.execute(
                "INSERT INTO pipeline_runs (run_id, source_id, started_at, status) VALUES (?, ?, ?, 'running')",
                (run_id, source.source_id, isoformat_utc(started_at)),
            )

    def complete_run(
        self,
        run_id: str,
        observations: Iterable[SourceObservation],
        completed_at: datetime,
    ) -> tuple[int, int]:
        items = list(observations)
        inserted = 0
        with self.connection:
            for item in items:
                occurred_at = isoformat_utc(item.occurred_at) if item.occurred_at else None
                metadata_json = json.dumps(item.metadata, sort_keys=True)
                latest = self.connection.execute(
                    """SELECT capture_sequence, occurred_at, item_kind, content,
                              canonical_url, metadata_json
                       FROM source_observations
                       WHERE source_id=? AND external_id=?
                       ORDER BY capture_sequence DESC LIMIT 1""",
                    (item.source_id, item.external_id),
                ).fetchone()
                material_payload = (
                    occurred_at,
                    item.item_kind,
                    item.content,
                    item.canonical_url,
                    metadata_json,
                )
                if latest is not None and material_payload == (
                    latest["occurred_at"],
                    latest["item_kind"],
                    latest["content"],
                    latest["canonical_url"],
                    latest["metadata_json"],
                ):
                    continue

                capture_sequence = (
                    int(latest["capture_sequence"]) + 1 if latest is not None else 1
                )
                self.connection.execute(
                    """INSERT INTO source_observations
                       (source_id, external_id, capture_sequence, observed_at, occurred_at,
                        item_kind, content, canonical_url, metadata_json, pipeline_run_id)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (
                        item.source_id,
                        item.external_id,
                        capture_sequence,
                        isoformat_utc(item.observed_at),
                        occurred_at,
                        item.item_kind,
                        item.content,
                        item.canonical_url,
                        metadata_json,
                        run_id,
                    ),
                )
                inserted += 1
            duplicates = len(items) - inserted
            self.connection.execute(
                """UPDATE pipeline_runs SET completed_at=?, status='succeeded',
                   fetched_count=?, inserted_count=?, duplicate_count=? WHERE run_id=?""",
                (isoformat_utc(completed_at), len(items), inserted, duplicates, run_id),
            )
        return inserted, duplicates

    def latest_observations(self, source_id: str | None = None) -> list[sqlite3.Row]:
        query = """SELECT observation.*
                   FROM source_observations AS observation
                   JOIN (
                       SELECT source_id, external_id, MAX(capture_sequence) AS capture_sequence
                       FROM source_observations
                       GROUP BY source_id, external_id
                   ) AS latest
                     ON latest.source_id = observation.source_id
                    AND latest.external_id = observation.external_id
                    AND latest.capture_sequence = observation.capture_sequence"""
        parameters: tuple[str, ...] = ()
        if source_id is not None:
            query += " WHERE observation.source_id=?"
            parameters = (source_id,)
        query += " ORDER BY observation.source_id, observation.external_id"
        return self.connection.execute(query, parameters).fetchall()

    def fail_run(
        self, run_id: str, completed_at: datetime, error: str, fetched_count: int = 0
    ) -> None:
        with self.connection:
            self.connection.execute(
                """UPDATE pipeline_runs SET completed_at=?, status='failed',
                   fetched_count=?, inserted_count=0, duplicate_count=0, error=?
                   WHERE run_id=?""",
                (isoformat_utc(completed_at), fetched_count, error, run_id),
            )

    def get_run(self, run_id: str) -> sqlite3.Row:
        row = self.connection.execute(
            "SELECT * FROM pipeline_runs WHERE run_id=?", (run_id,)
        ).fetchone()
        if row is None:
            raise KeyError(run_id)
        return row
