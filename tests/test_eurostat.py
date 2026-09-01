import json
from datetime import datetime, timezone
from io import BytesIO
from urllib.error import URLError
from urllib.parse import parse_qs, urlparse

import pytest

from asymmetry_engine.db import Repository
from asymmetry_engine.pipeline import run_collection
from asymmetry_engine.sources.eurostat import (
    API_URL,
    DATASET,
    GEO,
    INDICATORS,
    NACE_SECTIONS,
    REFERENCE_YEAR,
    EurostatCollector,
    EurostatError,
    decode_cells,
    eurostat_source,
    normalize_cell,
)


NOW = datetime(2026, 9, 3, 10, tzinfo=timezone.utc)
PAYLOAD = {
    "version": "2.0",
    "class": "dataset",
    "id": ["freq", "nace_r2", "indic_sbs", "geo", "time"],
    "size": [1, 2, 2, 1, 1],
    "dimension": {
        "freq": {"category": {"index": {"A": 0}, "label": {"A": "Annual"}}},
        "nace_r2": {
            "category": {
                "index": {"C": 0, "J": 1},
                "label": {"C": "Manufacturing", "J": "Information and communication"},
            }
        },
        "indic_sbs": {
            "category": {
                "index": {"ENT_NR": 0, "AV_MEUR": 1},
                "label": {
                    "ENT_NR": "Enterprises - number",
                    "AV_MEUR": "Value added - million euro",
                },
            }
        },
        "geo": {"category": {"index": {"CZ": 0}, "label": {"CZ": "Czechia"}}},
        "time": {"category": {"index": {"2023": 0}, "label": {"2023": "2023"}}},
    },
    "value": {"0": 189479, "1": 55597.37, "2": 65591},
    "status": {"1": "p", "3": "c"},
}


class Response(BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def test_official_filtered_request_uses_fixed_czech_slice_once():
    requests = []

    def opener(request, timeout):
        requests.append((request, timeout))
        return Response(json.dumps(PAYLOAD).encode())

    observations = EurostatCollector(opener=opener, clock=lambda: NOW).collect()
    assert len(observations) == 4
    assert len(requests) == 1
    request, timeout = requests[0]
    parsed = urlparse(request.full_url)
    query = parse_qs(parsed.query)
    assert request.full_url.startswith(API_URL)
    assert timeout == 60
    assert query["geo"] == [GEO]
    assert query["time"] == [REFERENCE_YEAR]
    assert query["nace_r2"] == list(NACE_SECTIONS)
    assert query["indic_sbs"] == list(INDICATORS)
    assert "sinceTimePeriod" not in query


def test_json_stat_dimension_indexes_control_multidimensional_mapping():
    cells = list(decode_cells(PAYLOAD))
    assert cells[0]["dimensions"] == {
        "freq": "A",
        "nace_r2": "C",
        "indic_sbs": "ENT_NR",
        "geo": "CZ",
        "time": "2023",
    }
    assert cells[0]["value"] == 189479
    assert cells[1]["dimensions"]["indic_sbs"] == "AV_MEUR"
    assert cells[1]["value"] == 55597.37
    assert cells[2]["dimensions"]["nace_r2"] == "J"
    assert cells[2]["value"] == 65591
    assert cells[3]["value"] is None
    assert cells[3]["status"] == "c"


def test_identity_content_units_metadata_and_year_timestamp_semantics():
    request_url = "https://example.invalid/filtered"
    cell = list(decode_cells(PAYLOAD))[1]
    observation = normalize_cell(cell, NOW, request_url)
    assert observation.external_id == "eurostat:sbs_ovw_act:CZ:C:AV_MEUR:MEUR:2023"
    assert "55597.37" not in observation.external_id
    assert observation.item_kind == "market_statistic"
    assert observation.occurred_at is None
    assert observation.observed_at == NOW
    assert "NACE activity: Manufacturing (C)" in observation.content
    assert "Value: 55597.37" in observation.content
    assert "Unit: million euro (MEUR)" in observation.content
    assert "Reference year: 2023" in observation.content
    assert "Status: p" in observation.content
    assert observation.metadata["value"] == 55597.37
    assert observation.metadata["status"] == "p"
    assert observation.metadata["api_url"] == request_url


def test_flagged_missing_cell_is_preserved_without_becoming_zero():
    cell = list(decode_cells(PAYLOAD))[3]
    observation = normalize_cell(cell, NOW, "https://example.invalid/filtered")
    assert observation.metadata["value"] is None
    assert observation.metadata["status"] == "c"
    assert "Value: missing" in observation.content
    assert "Value: 0" not in observation.content


def test_source_metadata_records_statistical_caveats():
    source = eurostat_source()
    assert source.source_id == "eurostat:sbs-market-structure"
    assert source.metadata["dataset"] == DATASET
    assert source.metadata["access"] == "free public API"
    assert "values can be revised" in source.selection_biases
    assert "not evidence of an information asymmetry" in source.selection_biases


@pytest.mark.parametrize(
    "response",
    [b"not-json", json.dumps({"class": "error"}).encode()],
)
def test_network_or_malformed_responses_fail_cleanly(response):
    def opener(request, timeout):
        return Response(response)

    with pytest.raises(EurostatError):
        EurostatCollector(opener=opener).collect()


def test_network_failure_is_reported_without_retry():
    calls = 0

    def opener(request, timeout):
        nonlocal calls
        calls += 1
        raise URLError("offline")

    with pytest.raises(EurostatError, match="request failed"):
        EurostatCollector(opener=opener).collect()
    assert calls == 1


def test_identical_statistical_cell_is_deduplicated(tmp_path):
    class Collector:
        source = eurostat_source()

        def collect(self):
            return [normalize_cell(list(decode_cells(PAYLOAD))[0], NOW, API_URL)]

    repository = Repository(tmp_path / "test.db")
    first = run_collection(Collector(), repository, lambda: NOW)
    second = run_collection(Collector(), repository, lambda: NOW)
    assert (first.inserted_count, first.duplicate_count) == (1, 0)
    assert (second.inserted_count, second.duplicate_count) == (0, 1)
    repository.close()
