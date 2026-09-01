import json
from datetime import datetime, timezone
from io import BytesIO
from urllib.error import URLError
from urllib.parse import parse_qs, urlparse

import pytest

from asymmetry_engine.db import Repository
from asymmetry_engine.pipeline import run_collection
from asymmetry_engine.sources.azure_prices import (
    API_URL,
    ARM_SKUS,
    CURRENCY,
    METER_NAMES,
    REGIONS,
    AzureRetailPriceCollector,
    AzureRetailPriceError,
    azure_price_source,
    normalize_price,
    odata_filter,
)


NOW = datetime(2026, 9, 3, 12, tzinfo=timezone.utc)
BASE_ITEM = {
    "currencyCode": "USD",
    "tierMinimumUnits": 0.0,
    "retailPrice": 0.115,
    "unitPrice": 0.115,
    "armRegionName": "westeurope",
    "location": "EU West",
    "effectiveStartDate": "2021-11-01T00:00:00Z",
    "meterId": "0561adcb-1c48-542e-9e0c-10dea22fc392",
    "meterName": "D2s v5",
    "productId": "DZH318Z08M9W",
    "skuId": "DZH318Z08M9W/0092",
    "productName": "Virtual Machines Dsv5 Series",
    "skuName": "Standard_D2s_v5",
    "serviceName": "Virtual Machines",
    "serviceId": "DZH313Z7MMC8",
    "serviceFamily": "Compute",
    "unitOfMeasure": "1 Hour",
    "type": "Consumption",
    "isPrimaryMeterRegion": True,
    "armSkuName": "Standard_D2s_v5",
}
WINDOWS_ITEM = {
    **BASE_ITEM,
    "retailPrice": 0.207,
    "unitPrice": 0.207,
    "meterId": "8aec24e5-8c37-581b-af93-3d8d785f272d",
    "productId": "DZH318Z08M9T",
    "skuId": "DZH318Z08M9T/005G",
    "productName": "Virtual Machines Dsv5 Series Windows",
}


class Response(BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def test_one_anonymous_official_filtered_get_request():
    requests = []

    def opener(request, timeout):
        requests.append((request, timeout))
        return Response(json.dumps({"Items": [BASE_ITEM], "NextPageLink": None}).encode())

    assert len(AzureRetailPriceCollector(opener=opener, clock=lambda: NOW).collect()) == 1
    assert len(requests) == 1
    request, timeout = requests[0]
    parsed = urlparse(request.full_url)
    query = parse_qs(parsed.query)
    assert parsed.scheme == "https"
    assert f"{parsed.scheme}://{parsed.netloc}{parsed.path}" == API_URL
    assert request.get_method() == "GET"
    assert timeout == 60
    assert request.get_header("Authorization") is None
    assert query["currencyCode"] == [repr(CURRENCY)]
    assert query["$filter"] == [odata_filter()]
    for value in (*ARM_SKUS, *METER_NAMES, *REGIONS):
        assert value in query["$filter"][0]
    assert "priceType eq 'Consumption'" in query["$filter"][0]
    assert "api-version" not in query


def test_identity_excludes_prices_dates_and_collection_time():
    first = normalize_price(BASE_ITEM, NOW)
    changed = normalize_price(
        {**BASE_ITEM, "retailPrice": 9.99, "unitPrice": 9.99,
         "effectiveStartDate": "2026-01-01T00:00:00Z"},
        NOW.replace(year=2027),
    )
    assert first.external_id == changed.external_id
    assert "0.115" not in first.external_id
    assert "2021" not in first.external_id


def test_regions_and_materially_distinct_products_do_not_collide():
    base = normalize_price(BASE_ITEM, NOW)
    other_region = normalize_price(
        {**BASE_ITEM, "armRegionName": "northeurope"}, NOW
    )
    windows = normalize_price(WINDOWS_ITEM, NOW)
    assert len({base.external_id, other_region.external_id, windows.external_id}) == 3


def test_effective_date_content_and_metadata_are_source_faithful():
    observation = normalize_price(BASE_ITEM, NOW)
    assert observation.item_kind == "retail_price"
    assert observation.observed_at == NOW
    assert observation.occurred_at.isoformat() == "2021-11-01T00:00:00+00:00"
    assert "Product: Virtual Machines Dsv5 Series" in observation.content
    assert "ARM SKU: Standard_D2s_v5" in observation.content
    assert "Retail price: 0.115" in observation.content
    assert "Currency: USD" in observation.content
    assert "Unit: 1 Hour" in observation.content
    assert observation.metadata["retailPrice"] == 0.115
    assert observation.metadata["unitPrice"] == 0.115
    assert observation.metadata["isPrimaryMeterRegion"] is True


def test_missing_or_unparseable_effective_date_is_not_invented():
    without_date = {key: value for key, value in BASE_ITEM.items() if key != "effectiveStartDate"}
    assert normalize_price(without_date, NOW).occurred_at is None
    assert normalize_price({**BASE_ITEM, "effectiveStartDate": "unknown"}, NOW).occurred_at is None


def test_multiple_product_variants_are_preserved_without_collapsing():
    def opener(request, timeout):
        return Response(
            json.dumps({"Items": [BASE_ITEM, WINDOWS_ITEM], "NextPageLink": None}).encode()
        )

    observations = AzureRetailPriceCollector(opener=opener, clock=lambda: NOW).collect()
    assert len(observations) == 2
    assert {item.metadata["productName"] for item in observations} == {
        "Virtual Machines Dsv5 Series",
        "Virtual Machines Dsv5 Series Windows",
    }


def test_next_page_is_reported_but_never_followed():
    calls = 0

    def opener(request, timeout):
        nonlocal calls
        calls += 1
        return Response(
            json.dumps({"Items": [BASE_ITEM], "NextPageLink": "https://next.invalid"}).encode()
        )

    collector = AzureRetailPriceCollector(opener=opener)
    with pytest.raises(AzureRetailPriceError, match="pagination is out of scope"):
        collector.collect()
    assert calls == 1
    assert collector.next_page_link == "https://next.invalid"


@pytest.mark.parametrize("payload", [b"not-json", b'{"Error":"bad filter"}'])
def test_malformed_or_api_error_fails_cleanly(payload):
    def opener(request, timeout):
        return Response(payload)

    with pytest.raises(AzureRetailPriceError):
        AzureRetailPriceCollector(opener=opener).collect()


def test_network_error_fails_without_retry():
    calls = 0

    def opener(request, timeout):
        nonlocal calls
        calls += 1
        raise URLError("offline")

    with pytest.raises(AzureRetailPriceError, match="request failed"):
        AzureRetailPriceCollector(opener=opener).collect()
    assert calls == 1


def test_source_metadata_records_price_caveats():
    source = azure_price_source()
    assert source.source_id == "azure:retail-prices"
    assert source.metadata["currency"] == "USD"
    assert "one supplier" in source.selection_biases
    assert "retail list price" in source.selection_biases
    assert "prices can change" in source.selection_biases


def test_identical_meter_price_is_deduplicated(tmp_path):
    class Collector:
        source = azure_price_source()

        def collect(self):
            return [normalize_price(BASE_ITEM, NOW)]

    repository = Repository(tmp_path / "test.db")
    first = run_collection(Collector(), repository, lambda: NOW)
    second = run_collection(Collector(), repository, lambda: NOW)
    assert (first.inserted_count, first.duplicate_count) == (1, 0)
    assert (second.inserted_count, second.duplicate_count) == (0, 1)
    repository.close()
