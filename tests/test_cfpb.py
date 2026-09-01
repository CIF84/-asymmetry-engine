import json
from datetime import datetime, timezone
from io import BytesIO
from urllib.error import URLError

from asymmetry_engine.db import Repository
from asymmetry_engine.pipeline import run_collection
from asymmetry_engine.sources.cfpb import (
    CFPBCollector,
    cfpb_source,
    normalize_complaint,
)


NOW = datetime(2026, 9, 2, 10, tzinfo=timezone.utc)
COMPLAINT = {
    "complaint_id": "12345",
    "date_received": "2026-08-30T14:15:16.000Z",
    "product": "Credit card",
    "sub_product": "General-purpose credit card",
    "issue": "Problem with a purchase shown on your statement",
    "sub_issue": "Card company isn't resolving a dispute",
    "company": "EXAMPLE BANK",
    "company_public_response": "Company believes it acted appropriately",
    "company_response": "Closed with explanation",
    "timely": "Yes",
    "state": "CA",
    "zip_code": "94105",
    "tags": ["Older American"],
    "submitted_via": "Web",
    "date_sent_to_company": "2026-08-31T09:00:00.000Z",
    "complaint_what_happened": "",
    "has_narrative": False,
}


class Response(BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def test_normalizes_structured_complaint_without_narrative():
    observation = normalize_complaint(COMPLAINT, NOW)
    assert observation.source_id == "cfpb:consumer-complaints"
    assert observation.external_id == "cfpb:complaint:12345"
    assert observation.item_kind == "complaint"
    assert observation.observed_at == NOW
    assert observation.occurred_at.isoformat() == "2026-08-30T14:15:16+00:00"
    assert observation.content == (
        "Product: Credit card\n"
        "Sub-product: General-purpose credit card\n"
        "Issue: Problem with a purchase shown on your statement\n"
        "Sub-issue: Card company isn't resolving a dispute\n"
        "Company: EXAMPLE BANK\n"
        "Company response: Closed with explanation"
    )
    assert observation.metadata["company_public_response"].startswith("Company")
    assert observation.metadata["complaint_what_happened"] == ""
    assert observation.metadata["has_narrative"] is False
    assert observation.canonical_url.endswith("/12345")


def test_missing_optional_fields_are_omitted_cleanly():
    minimal = {
        "complaint_id": 9,
        "date_received": "2026-08-30",
        "product": "Debt collection",
        "issue": "Written notification about debt",
        "company": "EXAMPLE COLLECTOR",
    }
    observation = normalize_complaint(minimal, NOW)
    assert "Sub-product:" not in observation.content
    assert "Sub-issue:" not in observation.content
    assert "complaint_what_happened" not in observation.metadata
    assert observation.occurred_at.tzinfo == timezone.utc


def test_collector_constructs_bounded_official_request():
    requested = []

    def opener(url, timeout):
        requested.append((url, timeout))
        payload = {"timed_out": False, "hits": {"hits": [{"_source": COMPLAINT}]}}
        return Response(json.dumps(payload).encode())

    observations = CFPBCollector(sample_size=75, opener=opener, clock=lambda: NOW).collect()
    assert len(observations) == 1
    url, timeout = requested[0]
    assert url.startswith("https://www.consumerfinance.gov/")
    assert "size=75" in url
    assert "sort=created_date_desc" in url
    assert "no_aggs=true" in url
    assert timeout == 30


def test_source_metadata_records_representativeness_limits():
    source = cfpb_source()
    assert source.source_id == "cfpb:consumer-complaints"
    assert "Not a statistical sample" in source.selection_biases
    assert "not necessarily representative" in source.selection_biases
    assert source.metadata["geographic_scope"] == "United States"
    assert source.metadata["license"] == "CC0"


def test_api_failure_is_recorded_by_pipeline(tmp_path):
    def opener(url, timeout):
        raise URLError("offline")

    repository = Repository(tmp_path / "test.db")
    result = run_collection(CFPBCollector(opener=opener), repository, lambda: NOW)
    assert result.status == "failed"
    assert result.duplicate_count == 0
    assert "CFPB request failed" in result.error
    assert repository.get_run(result.run_id)["status"] == "failed"
    repository.close()


def test_identical_cfpb_collection_is_deduplicated(tmp_path):
    class Collector:
        source = cfpb_source()

        def collect(self):
            return [normalize_complaint(COMPLAINT, NOW)]

    repository = Repository(tmp_path / "test.db")
    first = run_collection(Collector(), repository, lambda: NOW)
    second = run_collection(Collector(), repository, lambda: NOW)
    assert (first.inserted_count, first.duplicate_count) == (1, 0)
    assert (second.inserted_count, second.duplicate_count) == (0, 1)
    repository.close()
