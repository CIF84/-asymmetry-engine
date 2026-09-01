import base64
import json
from datetime import datetime, timezone
from io import BytesIO

import pytest

from asymmetry_engine.db import Repository
from asymmetry_engine.pipeline import run_collection
from asymmetry_engine.sources.dataforseo import (
    API_URL,
    DataForSEOError,
    DataForSEOKeywordCollector,
    dataforseo_source,
    keyword_external_id,
    normalize_keyword_measurement,
)
from asymmetry_engine.sources.dataforseo_seeds import KEYWORD_SEEDS


NOW = datetime(2026, 9, 2, 12, tzinfo=timezone.utc)
CONTEXT = {"location_code": 2840, "language_code": "en", "search_partners": False}
MEASUREMENT = {
    "keyword": "how much life insurance do i need",
    "spell": None,
    "location_code": 2840,
    "language_code": "en",
    "search_partners": False,
    "competition": "HIGH",
    "competition_index": 87,
    "search_volume": 5400,
    "low_top_of_page_bid": 2.35,
    "high_top_of_page_bid": 8.4,
    "cpc": 4.12,
    "monthly_searches": [{"year": 2026, "month": 7, "search_volume": 5100}],
}


class Response(BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def test_checked_in_seed_set_is_small_and_explicit():
    assert 20 <= len(KEYWORD_SEEDS) <= 30
    assert len(KEYWORD_SEEDS) == len(set(KEYWORD_SEEDS))


def api_payload(result=None, task_status=20000):
    return {
        "status_code": 20000,
        "tasks": [
            {
                "id": "task-id",
                "status_code": task_status,
                "cost": 0.05,
                "result": [MEASUREMENT] if result is None else result,
            }
        ],
    }


def test_one_authenticated_official_request_contains_all_keywords():
    requests = []

    def opener(request, timeout):
        requests.append((request, timeout))
        return Response(json.dumps(api_payload()).encode())

    collector = DataForSEOKeywordCollector(
        keywords=("first phrase", "second phrase"),
        login="fixture-login",
        password="fixture-password",
        opener=opener,
        clock=lambda: NOW,
    )
    assert len(collector.collect()) == 1
    assert len(requests) == 1
    request, timeout = requests[0]
    assert request.full_url == API_URL
    assert request.method == "POST"
    assert timeout == 60
    expected = base64.b64encode(b"fixture-login:fixture-password").decode()
    assert request.get_header("Authorization") == f"Basic {expected}"
    task = json.loads(request.data)[0]
    assert task == {
        "location_code": 2840,
        "language_code": "en",
        "search_partners": False,
        "keywords": ["first phrase", "second phrase"],
    }


def test_normalization_preserves_metrics_and_has_no_occurrence_timestamp():
    observation = normalize_keyword_measurement(MEASUREMENT, NOW, CONTEXT)
    assert observation.source_id == "dataforseo:google-ads-keyword-demand"
    assert observation.external_id.endswith(":2840:en")
    assert observation.observed_at == NOW
    assert observation.occurred_at is None
    assert observation.item_kind == "keyword_demand"
    assert "Search volume: 5400" in observation.content
    assert "CPC: 4.12 USD" in observation.content
    assert observation.metadata["monthly_searches"][0]["search_volume"] == 5100
    assert observation.metadata["competition_index"] == 87


def test_identity_is_normalized_and_distinguishes_market_context():
    first = keyword_external_id("  Life Insurance ", 2840, "en")
    assert first == keyword_external_id("life   insurance", 2840, "EN")
    assert first != keyword_external_id("life insurance", 2826, "en")
    assert first != keyword_external_id("life insurance", 2840, "es")


def test_null_metrics_are_omitted_cleanly():
    item = {
        "keyword": "no data phrase",
        "location_code": 2840,
        "language_code": "en",
        "search_volume": None,
        "cpc": None,
        "monthly_searches": None,
    }
    observation = normalize_keyword_measurement(item, NOW, CONTEXT)
    assert observation.content == "Keyword: no data phrase"
    assert observation.metadata["search_volume"] is None
    assert observation.metadata["monthly_searches"] is None


def test_missing_credentials_fail_clearly(monkeypatch):
    monkeypatch.delenv("DATAFORSEO_LOGIN", raising=False)
    monkeypatch.delenv("DATAFORSEO_PASSWORD", raising=False)
    with pytest.raises(DataForSEOError, match="DATAFORSEO_LOGIN"):
        DataForSEOKeywordCollector(keywords=("one",)).collect()


def test_task_error_is_recorded_by_pipeline(tmp_path):
    def opener(request, timeout):
        return Response(json.dumps(api_payload(task_status=40501)).encode())

    repository = Repository(tmp_path / "test.db")
    collector = DataForSEOKeywordCollector(
        keywords=("one",), login="fixture-login", password="fixture-password", opener=opener
    )
    result = run_collection(collector, repository, lambda: NOW)
    assert result.status == "failed"
    assert "task error 40501" in result.error
    assert repository.get_run(result.run_id)["status"] == "failed"
    repository.close()


def test_identical_keyword_measurement_is_deduplicated(tmp_path):
    class Collector:
        source = dataforseo_source()

        def collect(self):
            return [normalize_keyword_measurement(MEASUREMENT, NOW, CONTEXT)]

    repository = Repository(tmp_path / "test.db")
    first = run_collection(Collector(), repository, lambda: NOW)
    second = run_collection(Collector(), repository, lambda: NOW)
    assert (first.inserted_count, first.duplicate_count) == (1, 0)
    assert (second.inserted_count, second.duplicate_count) == (0, 1)
    repository.close()


def test_source_metadata_preserves_vendor_and_metric_caveats():
    source = dataforseo_source()
    assert "vendor dependency" in source.commercial_use_considerations
    assert "not unique people" in source.selection_biases
    assert "not evidence of product profitability" in source.selection_biases
