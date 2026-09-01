from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def isoformat_utc(value: datetime) -> str:
    if value.tzinfo is None:
        raise ValueError("timestamps must be timezone-aware")
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


@dataclass(frozen=True)
class SignalSource:
    source_id: str
    name: str
    access_method: str
    terms_reference: str
    commercial_use_considerations: str
    selection_biases: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class SourceObservation:
    source_id: str
    external_id: str
    observed_at: datetime
    occurred_at: datetime | None
    item_kind: str
    content: str
    canonical_url: str | None
    metadata: dict[str, Any]
