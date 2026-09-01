import json
from datetime import datetime, timezone
from io import BytesIO

from asymmetry_engine.db import Repository
from asymmetry_engine.pipeline import run_collection
from asymmetry_engine.sources.ted import (
    API_URL,
    EXPERT_QUERY,
    REQUEST_FIELDS,
    TEDCollector,
    normalize_notice,
    ted_source,
)


NOW = datetime(2026, 9, 2, 12, tzinfo=timezone.utc)
NOTICE = {
    "publication-number": "603254-2026",
    "publication-date": "2026-09-02+02:00",
    "notice-identifier": "0d355422-7928-41c3-a081-a21a3b13a372",
    "notice-version": 1,
    "notice-title": {
        "ces": "Česko – Implementace programového vybavení",
        "eng": "Czechia – Software implementation services",
    },
    "buyer-name": {"ces": ["ČEPS, a.s."]},
    "buyer-country": ["CZE"],
    "place-of-performance": ["CZ010", "CZE", "CZ010"],
    "form-type": "result",
    "notice-type": "can-standard",
    "main-classification-proc": ["72263000"],
    "procedure-type": "open",
    "total-value": 78765450,
    "total-value-cur": ["CZK"],
    "deadline": ["2026-10-01+02:00"],
    "links": {
        "html": {
            "CES": "https://ted.europa.eu/cs/notice/-/detail/603254-2026",
            "ENG": "https://ted.europa.eu/en/notice/-/detail/603254-2026",
        },
        "xml": {"MUL": "https://ted.europa.eu/en/notice/603254-2026/xml"},
    },
}


class Response(BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def test_one_bounded_official_request_uses_czech_query_and_selected_fields():
    requests = []

    def opener(request, timeout):
        requests.append((request, timeout))
        return Response(json.dumps({"notices": [NOTICE], "timedOut": False}).encode())

    assert len(TEDCollector(opener=opener, clock=lambda: NOW).collect()) == 1
    assert len(requests) == 1
    request, timeout = requests[0]
    assert request.full_url == API_URL
    assert request.method == "POST"
    assert timeout == 60
    body = json.loads(request.data)
    assert body["query"] == EXPERT_QUERY
    assert body["limit"] == 75
    assert body["page"] == 1
    assert body["paginationMode"] == "PAGE_NUMBER"
    assert body["fields"] == list(REQUEST_FIELDS)
    assert "xml" not in body["fields"]


def test_normalizes_identity_timestamps_content_metadata_and_url():
    observation = normalize_notice(NOTICE, NOW)
    assert observation.source_id == "ted:public-procurement"
    assert observation.external_id == "ted:notice:603254-2026"
    assert observation.item_kind == "procurement_notice"
    assert observation.observed_at == NOW
    assert observation.occurred_at.isoformat() == "2026-09-01T22:00:00+00:00"
    assert "Title: Czechia – Software implementation services" in observation.content
    assert "Buyer: ČEPS, a.s." in observation.content
    assert "Main classification (CPV): 72263000" in observation.content
    assert "Value: 78765450 CZK" in observation.content
    assert observation.canonical_url.endswith("/603254-2026")
    assert observation.metadata["notice-identifier"].startswith("0d355")
    assert observation.metadata["notice-version"] == 1
    assert observation.metadata["html_urls"]["CES"].startswith("https://ted.europa.eu")


def test_missing_optional_values_are_omitted_cleanly():
    minimal = {
        "publication-number": "1-2026",
        "publication-date": "2026-09-02",
        "notice-title": {"ces": "Dodávka"},
    }
    observation = normalize_notice(minimal, NOW)
    assert observation.content == "Title: Dodávka"
    assert observation.canonical_url is None
    assert "Value:" not in observation.content


def test_source_metadata_records_procurement_caveats():
    source = ted_source()
    assert source.source_id == "ted:public-procurement"
    assert source.metadata["access"] == "free anonymous"
    assert "not a completed purchase" in source.selection_biases
    assert "multiple notices" in source.selection_biases
    assert "Place of performance" in source.metadata["empirical_scope"]


def test_api_timeout_is_recorded_by_pipeline(tmp_path):
    def opener(request, timeout):
        return Response(json.dumps({"timedOut": True, "notices": []}).encode())

    repository = Repository(tmp_path / "test.db")
    result = run_collection(TEDCollector(opener=opener), repository, lambda: NOW)
    assert result.status == "failed"
    assert "request timed out" in result.error
    assert repository.get_run(result.run_id)["status"] == "failed"
    repository.close()


def test_identical_ted_notice_is_deduplicated(tmp_path):
    class Collector:
        source = ted_source()

        def collect(self):
            return [normalize_notice(NOTICE, NOW)]

    repository = Repository(tmp_path / "test.db")
    first = run_collection(Collector(), repository, lambda: NOW)
    second = run_collection(Collector(), repository, lambda: NOW)
    assert (first.inserted_count, first.duplicate_count) == (1, 0)
    assert (second.inserted_count, second.duplicate_count) == (0, 1)
    repository.close()
