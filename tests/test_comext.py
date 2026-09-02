import json
from datetime import datetime, timezone
from io import BytesIO
from urllib.error import URLError
from urllib.parse import parse_qs, urlparse

import pytest

from asymmetry_engine.db import Repository
from asymmetry_engine.pipeline import run_collection
from asymmetry_engine.sources.comext import (
    API_URL,
    DATASET,
    INDICATORS,
    PRODUCTS,
    YEARS,
    ComextCollector,
    ComextError,
    comext_source,
    normalize_cell,
)
from asymmetry_engine.sources.eurostat import decode_cells


NOW = datetime(2026, 9, 3, 15, tzinfo=timezone.utc)
PAYLOAD = {
    "version": "2.0",
    "class": "dataset",
    "id": ["freq", "reporter", "partner", "product", "flow", "indicators", "time"],
    "size": [1, 1, 1, 2, 1, 2, 2],
    "dimension": {
        "freq": {"category": {"index": {"A": 0}, "label": {"A": "Annual"}}},
        "reporter": {
            "category": {"index": {"CZ": 0}, "label": {"CZ": "Czechia"}}
        },
        "partner": {
            "category": {
                "index": {"WORLD": 0},
                "label": {"WORLD": "All countries of the world"},
            }
        },
        "product": {
            "category": {
                "index": {"84": 0, "85": 1},
                "label": {"84": "MACHINERY", "85": "ELECTRICAL MACHINERY"},
            }
        },
        "flow": {"category": {"index": {"1": 0}, "label": {"1": "IMPORT"}}},
        "indicators": {
            "category": {
                "index": {"VALUE_IN_EUROS": 0, "QUANTITY_IN_100KG": 1},
                "label": {
                    "VALUE_IN_EUROS": "VALUE_IN_EUROS",
                    "QUANTITY_IN_100KG": "QUANTITY_IN_100KG",
                },
            }
        },
        "time": {
            "category": {
                "index": {"2023": 0, "2024": 1},
                "label": {"2023": "2023", "2024": "2024"},
            }
        },
    },
    # Product is the outer varying dimension; time is the innermost.
    "value": {
        "0": 1000,
        "1": 1100,
        "2": 50,
        "3": 45,
        "4": 2000,
        "5": 2400,
        "6": 75,
    },
    "status": {"7": "c"},
}


class Response(BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def test_one_official_bounded_czech_world_import_request():
    requests = []

    def opener(request, timeout):
        requests.append((request, timeout))
        return Response(json.dumps(PAYLOAD).encode())

    observations = ComextCollector(opener=opener, clock=lambda: NOW).collect()
    assert len(observations) == 8
    assert len(requests) == 1
    request, timeout = requests[0]
    query = parse_qs(urlparse(request.full_url).query)
    assert request.full_url.startswith(API_URL)
    assert timeout == 90
    assert query["freq"] == ["A"]
    assert query["reporter"] == ["CZ"]
    assert query["partner"] == ["WORLD"]
    assert query["flow"] == ["1"]
    assert query["product"] == list(PRODUCTS)
    assert query["indicators"] == list(INDICATORS)
    assert query["time"] == list(YEARS)


def test_json_stat_dimensions_map_value_and_quantity_to_separate_cells():
    cells = list(decode_cells(PAYLOAD))
    assert cells[0]["dimensions"]["product"] == "84"
    assert cells[0]["dimensions"]["indicators"] == "VALUE_IN_EUROS"
    assert cells[0]["dimensions"]["time"] == "2023"
    assert cells[0]["value"] == 1000
    assert cells[2]["dimensions"]["indicators"] == "QUANTITY_IN_100KG"
    assert cells[2]["value"] == 50
    assert cells[4]["dimensions"]["product"] == "85"
    assert cells[4]["value"] == 2000


def test_identity_content_metadata_and_annual_timestamp_semantics():
    cell = list(decode_cells(PAYLOAD))[0]
    observation = normalize_cell(cell, NOW, "https://example.invalid/filtered")
    assert observation.external_id == (
        "comext:DS-045409:CZ:1:WORLD:84:VALUE_IN_EUROS:EUR:2023"
    )
    assert "1000" not in observation.external_id
    assert observation.item_kind == "trade_statistic"
    assert observation.occurred_at is None
    assert observation.observed_at == NOW
    assert "Flow: Czechia imports (CZ, 1)" in observation.content
    assert "Product: 84 — MACHINERY" in observation.content
    assert "Measure: Trade value (VALUE_IN_EUROS)" in observation.content
    assert "Unit: euro (EUR)" in observation.content
    assert "Reference period: 2023" in observation.content
    assert observation.metadata["value"] == 1000
    assert observation.metadata["api_url"].endswith("/filtered")


def test_flagged_missing_cell_is_preserved_without_fabricating_zero():
    cell = list(decode_cells(PAYLOAD))[7]
    observation = normalize_cell(cell, NOW, API_URL)
    assert observation.metadata["value"] is None
    assert observation.metadata["status"] == "c"
    assert "Value: missing" in observation.content
    assert "Status: c" in observation.content
    assert "Value: 0" not in observation.content


def test_truly_absent_sparse_cell_is_not_fabricated():
    payload = {**PAYLOAD, "status": {}}

    def opener(request, timeout):
        return Response(json.dumps(payload).encode())

    observations = ComextCollector(opener=opener, clock=lambda: NOW).collect()
    assert len(observations) == 7
    assert not any(
        item.metadata["product_code"] == "85"
        and item.metadata["measure_code"] == "QUANTITY_IN_100KG"
        and item.metadata["reference_period"] == "2024"
        for item in observations
    )


def test_source_metadata_records_reuse_and_interpretation_caveats():
    source = comext_source()
    assert source.source_id == "eurostat:comext-physical-flow"
    assert source.metadata["dataset"] == DATASET
    assert "Czechia as the declaring EU country" in source.commercial_use_considerations
    assert "net mass is not economically comparable" in source.selection_biases
    assert "world partner hides origin concentration" in source.selection_biases


@pytest.mark.parametrize("payload", [b"not-json", b'{"class":"error"}'])
def test_malformed_or_api_error_fails_cleanly(payload):
    def opener(request, timeout):
        return Response(payload)

    with pytest.raises(ComextError):
        ComextCollector(opener=opener).collect()


def test_network_error_fails_without_retry():
    calls = 0

    def opener(request, timeout):
        nonlocal calls
        calls += 1
        raise URLError("offline")

    with pytest.raises(ComextError, match="request failed"):
        ComextCollector(opener=opener).collect()
    assert calls == 1


def test_identical_trade_cell_is_persisted_then_deduplicated(tmp_path):
    class Collector:
        source = comext_source()

        def collect(self):
            return [normalize_cell(list(decode_cells(PAYLOAD))[0], NOW, API_URL)]

    repository = Repository(tmp_path / "test.db")
    first = run_collection(Collector(), repository, lambda: NOW)
    second = run_collection(Collector(), repository, lambda: NOW)
    assert (first.inserted_count, first.duplicate_count) == (1, 0)
    assert (second.inserted_count, second.duplicate_count) == (0, 1)
    repository.close()
