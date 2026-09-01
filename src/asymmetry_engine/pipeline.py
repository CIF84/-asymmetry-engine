from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import uuid4

from .db import Repository
from .models import SignalSource, SourceObservation, utc_now


class Collector(Protocol):
    source: SignalSource

    def collect(self) -> list[SourceObservation]: ...


@dataclass(frozen=True)
class RunResult:
    run_id: str
    status: str
    fetched_count: int
    inserted_count: int
    duplicate_count: int
    error: str | None = None


def run_collection(
    collector: Collector, repository: Repository, clock=utc_now
) -> RunResult:
    run_id = str(uuid4())
    started_at: datetime = clock()
    repository.start_run(run_id, collector.source, started_at)
    fetched_count = 0
    try:
        observations = collector.collect()
        fetched_count = len(observations)
        inserted, duplicates = repository.complete_run(run_id, observations, clock())
        return RunResult(run_id, "succeeded", fetched_count, inserted, duplicates)
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"
        repository.fail_run(run_id, clock(), error, fetched_count)
        return RunResult(run_id, "failed", fetched_count, 0, 0, error)
