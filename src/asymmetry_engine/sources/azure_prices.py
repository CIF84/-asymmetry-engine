from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

from ..models import SignalSource, SourceObservation, utc_now

API_URL = "https://prices.azure.com/api/retail/prices"
SOURCE_ID = "azure:retail-prices"
CURRENCY = "USD"
ARM_SKUS = ("Standard_D2s_v5", "Standard_D4s_v5", "Standard_D8s_v5")
METER_NAMES = ("D2s v5", "D4s v5", "D8s v5")
REGIONS = (
    "westeurope",
    "northeurope",
    "germanywestcentral",
    "francecentral",
    "polandcentral",
)
METADATA_FIELDS = (
    "currencyCode",
    "tierMinimumUnits",
    "retailPrice",
    "unitPrice",
    "armRegionName",
    "location",
    "effectiveStartDate",
    "meterId",
    "meterName",
    "productId",
    "skuId",
    "productName",
    "skuName",
    "serviceName",
    "serviceId",
    "serviceFamily",
    "unitOfMeasure",
    "type",
    "isPrimaryMeterRegion",
    "armSkuName",
)


class AzureRetailPriceError(RuntimeError):
    pass


def azure_price_source() -> SignalSource:
    return SignalSource(
        source_id=SOURCE_ID,
        name="Microsoft Azure Retail Prices",
        access_method="Official unauthenticated Azure Retail Prices API",
        terms_reference="https://azure.microsoft.com/en-us/support/legal/",
        commercial_use_considerations=(
            "Free unauthenticated access to Microsoft-published retail rates; this bounded "
            "slice preserves selected source-native meter prices in USD."
        ),
        selection_biases=(
            "This is one supplier, not a whole market, and retail list price is not necessarily "
            "a realized customer price. Enterprise agreements, negotiated discounts, taxes, "
            "support, egress, and other charges are not represented by a single meter price. "
            "Regional differences may reflect costs, capacity, regulation, availability, or "
            "product differences rather than exploitable asymmetry. Apparently similar rows "
            "can differ by product, meter, or price type; prices can change while meter identity "
            "remains stable; and price dispersion alone does not establish information "
            "asymmetry or commercial opportunity."
        ),
        metadata={
            "api_endpoint": API_URL,
            "api_version": "documented unversioned endpoint",
            "access": "free unauthenticated",
            "source": "Microsoft Azure retail pricing",
            "empirical_scope": "Selected Dsv5 VM SKUs across selected European regions",
            "currency": CURRENCY,
            "evidence_semantics": (
                "Supplier-published retail price measurement, not observed transaction price"
            ),
        },
    )


def _or_filter(field: str, values: tuple[str, ...]) -> str:
    return "(" + " or ".join(f"{field} eq '{value}'" for value in values) + ")"


def odata_filter() -> str:
    return " and ".join(
        (
            "serviceName eq 'Virtual Machines'",
            "priceType eq 'Consumption'",
            _or_filter("armSkuName", ARM_SKUS),
            _or_filter("meterName", METER_NAMES),
            _or_filter("armRegionName", REGIONS),
        )
    )


def request_url() -> str:
    return f"{API_URL}?{urlencode({'currencyCode': repr(CURRENCY), '$filter': odata_filter()})}"


def _effective_datetime(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _identity_part(value: Any) -> str:
    return quote(str(value), safe="")


def normalize_price(item: dict[str, Any], observed_at: datetime) -> SourceObservation:
    meter_id = item["meterId"]
    product_id = item["productId"]
    sku_id = item["skuId"]
    region = item["armRegionName"]
    price_type = item["type"]
    tier = item.get("tierMinimumUnits", 0)
    unit = item["unitOfMeasure"]
    identity_values = (meter_id, product_id, sku_id, region, price_type, tier, unit)

    content_values = (
        ("Service", item.get("serviceName")),
        ("Product", item.get("productName")),
        ("ARM SKU", item.get("armSkuName")),
        ("SKU", item.get("skuName")),
        ("Meter", item.get("meterName")),
        ("Region", item.get("armRegionName")),
        ("Location", item.get("location")),
        ("Retail price", item.get("retailPrice")),
        ("Currency", item.get("currencyCode")),
        ("Unit", item.get("unitOfMeasure")),
        ("Price type", item.get("type")),
        ("Effective start", item.get("effectiveStartDate")),
        ("Tier minimum units", item.get("tierMinimumUnits")),
    )
    content = "\n".join(
        f"{label}: {value}"
        for label, value in content_values
        if value not in (None, "")
    )
    return SourceObservation(
        source_id=SOURCE_ID,
        external_id=(
            "azure:retail-price:" + ":".join(_identity_part(value) for value in identity_values)
        ),
        observed_at=observed_at,
        occurred_at=_effective_datetime(item.get("effectiveStartDate")),
        item_kind="retail_price",
        content=content,
        canonical_url=None,
        metadata={field: item[field] for field in METADATA_FIELDS if field in item},
    )


class AzureRetailPriceCollector:
    def __init__(
        self,
        opener: Callable[..., Any] = urlopen,
        clock: Callable[[], datetime] = utc_now,
    ) -> None:
        self.opener = opener
        self.clock = clock
        self.source = azure_price_source()
        self.next_page_link: str | None = None

    def collect(self) -> list[SourceObservation]:
        request = Request(request_url(), headers={"Accept": "application/json"})
        try:
            with self.opener(request, timeout=60) as response:
                payload = json.load(response)
        except (HTTPError, URLError, TimeoutError, OSError, json.JSONDecodeError):
            raise AzureRetailPriceError("Azure Retail Prices API request failed") from None

        try:
            items = payload["Items"]
            if not isinstance(items, list):
                raise TypeError("Items must be an array")
            self.next_page_link = payload.get("NextPageLink") or None
            if self.next_page_link is not None:
                raise AzureRetailPriceError(
                    "Filtered Azure response exceeded one page; pagination is out of scope"
                )
            observed_at = self.clock()
            return [normalize_price(item, observed_at) for item in items]
        except AzureRetailPriceError:
            raise
        except (KeyError, TypeError, ValueError) as exc:
            raise AzureRetailPriceError(f"Invalid Azure Retail Prices response: {exc}") from exc
