import json
from datetime import datetime, timezone
from io import BytesIO

import pytest

from asymmetry_engine.sources.stackexchange import (
    StackExchangeCollector,
    StackExchangeError,
    normalize_question,
)


ITEM = {
    "question_id": 42,
    "creation_date": 1_700_000_000,
    "title": "Should I pay down my mortgage?",
    "link": "https://money.stackexchange.com/questions/42/example",
    "tags": ["mortgage", "debt"],
    "score": 7,
    "view_count": 120,
    "answer_count": 2,
    "is_answered": True,
}


def test_normalizes_identity_timestamp_and_metadata():
    seen = datetime(2026, 9, 1, 12, tzinfo=timezone.utc)
    observation = normalize_question(ITEM, "money", seen)
    assert observation.source_id == "stackexchange:money"
    assert observation.external_id == "money:question:42"
    assert observation.observed_at == seen
    assert observation.occurred_at.isoformat() == "2023-11-14T22:13:20+00:00"
    assert observation.content == ITEM["title"]
    assert observation.metadata["tags"] == ["mortgage", "debt"]
    assert observation.metadata["view_count"] == 120


class Response(BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def test_collector_uses_bounded_query_and_honors_backoff():
    requested = []
    slept = []

    def opener(url, timeout):
        requested.append((url, timeout))
        return Response(json.dumps({"items": [ITEM], "backoff": 2}).encode())

    collector = StackExchangeCollector(
        sample_size=3,
        opener=opener,
        sleeper=slept.append,
        clock=lambda: datetime(2026, 9, 1, tzinfo=timezone.utc),
    )
    assert len(collector.collect()) == 1
    assert "pagesize=3" in requested[0][0]
    assert "site=money" in requested[0][0]
    assert slept == [2.0]


def test_collector_reports_api_error():
    def opener(url, timeout):
        return Response(json.dumps({"error_id": 400, "error_message": "bad site"}).encode())

    with pytest.raises(StackExchangeError, match="bad site"):
        StackExchangeCollector(opener=opener).collect()
