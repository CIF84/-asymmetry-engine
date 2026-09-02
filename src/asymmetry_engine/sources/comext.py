from __future__ import annotations

import json
from datetime import datetime
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from ..models import SignalSource, SourceObservation, utc_now
from .eurostat import decode_cells

DATASET = "DS-045409"
API_URL = (
    "https://ec.europa.eu/eurostat/api/comext/dissemination/statistics/1.0/data/"
    f"{DATASET}"
)
SOURCE_ID = "eurostat:comext-physical-flow"
REPORTER = "CZ"
PARTNER = "WORLD"
FLOW = "1"
YEARS = ("2023", "2024")
INDICATORS = ("VALUE_IN_EUROS", "QUANTITY_IN_100KG")
PRODUCTS = tuple(f"{chapter:02d}" for chapter in range(1, 98) if chapter != 77) + (
    "99",
)
MEASURE_DETAILS = {
    "VALUE_IN_EUROS": ("Trade value", "EUR", "euro"),
    "QUANTITY_IN_100KG": ("Net mass", "100KG", "100 kilograms"),
}


class ComextError(RuntimeError):
    pass


def comext_source() -> SignalSource:
    return SignalSource(
        source_id=SOURCE_ID,
        name="Eurostat Comext Physical Flow",
        access_method="Official Eurostat Comext API",
        terms_reference="https://ec.europa.eu/eurostat/help/copyright-notice",
        commercial_use_considerations=(
            "Free public data reusable with Eurostat attribution subject to stated country "
            "and dataset exceptions. This slice uses Czechia as the declaring EU country and "
            "does not redistribute unrelated non-EU declarant data or Austrian CN8 data."
        ),
        selection_biases=(
            "Trade is not identical to final consumer demand. Gross value can move because of "
            "quantity, price, product mix, or exchange-rate effects, and net mass is not "
            "economically comparable across all product types. Broad CN2 categories can hide "
            "subcategory divergence; world partner hides origin concentration; goods trade "
            "does not cover pure software or services; revisions and classification changes "
            "can affect comparisons; and one cell is not one independent economic actor."
        ),
        metadata={
            "api_endpoint": API_URL,
            "access": "free public",
            "dataset": DATASET,
            "geography": "EU/European trade statistics; empirical slice scoped to Czechia",
            "commercial_use_status": (
                "Reusable with attribution subject to Eurostat copyright exceptions"
            ),
            "attribution": "Source: Eurostat Comext",
            "source_role": "structural / physical economic flow",
        },
    )


def query_parameters() -> list[tuple[str, str]]:
    parameters = [
        ("lang", "en"),
        ("freq", "A"),
        ("reporter", REPORTER),
        ("partner", PARTNER),
        ("flow", FLOW),
    ]
    parameters.extend(("product", product) for product in PRODUCTS)
    parameters.extend(("indicators", indicator) for indicator in INDICATORS)
    parameters.extend(("time", year) for year in YEARS)
    return parameters


def normalize_cell(
    cell: dict[str, Any], observed_at: datetime, request_url: str
) -> SourceObservation:
    dimensions = cell["dimensions"]
    labels = cell["labels"]
    reporter = dimensions["reporter"]
    partner = dimensions["partner"]
    product = dimensions["product"]
    flow = dimensions["flow"]
    indicator = dimensions["indicators"]
    period = dimensions["time"]
    measure_label, unit_code, unit_label = MEASURE_DETAILS[indicator]
    value = cell["value"]
    status = cell["status"]

    lines = [
        f"Dataset: Eurostat Comext ({DATASET})",
        f"Flow: {labels['reporter']} {labels['flow'].lower()}s ({reporter}, {flow})",
        f"Partner: {labels['partner']} ({partner})",
        f"Product: {product} — {labels['product']}",
        f"Measure: {measure_label} ({indicator})",
        f"Value: {value if value is not None else 'missing'}",
        f"Unit: {unit_label} ({unit_code})",
        f"Reference period: {period}",
    ]
    if status is not None:
        lines.append(f"Status: {status}")

    return SourceObservation(
        source_id=SOURCE_ID,
        external_id=(
            f"comext:{DATASET}:{reporter}:{flow}:{partner}:{product}:"
            f"{indicator}:{unit_code}:{period}"
        ),
        observed_at=observed_at,
        occurred_at=None,
        item_kind="trade_statistic",
        content="\n".join(lines),
        canonical_url=None,
        metadata={
            "dataset": DATASET,
            "frequency_code": dimensions["freq"],
            "frequency_label": labels["freq"],
            "reporter_code": reporter,
            "reporter_label": labels["reporter"],
            "partner_code": partner,
            "partner_label": labels["partner"],
            "product_classification": "Combined Nomenclature, broad 2-digit chapter",
            "product_code": product,
            "product_label": labels["product"],
            "flow_code": flow,
            "flow_label": labels["flow"],
            "measure_code": indicator,
            "measure_label": measure_label,
            "unit_code": unit_code,
            "unit_label": unit_label,
            "reference_period": period,
            "value": value,
            "status": status,
            "api_url": request_url,
        },
    )


class ComextCollector:
    def __init__(
        self,
        opener: Callable[..., Any] = urlopen,
        clock: Callable[[], datetime] = utc_now,
    ) -> None:
        self.opener = opener
        self.clock = clock
        self.source = comext_source()

    def collect(self) -> list[SourceObservation]:
        request_url = f"{API_URL}?{urlencode(query_parameters())}"
        request = Request(request_url, headers={"Accept": "application/json"})
        try:
            with self.opener(request, timeout=90) as response:
                payload = json.load(response)
        except (HTTPError, URLError, TimeoutError, OSError, json.JSONDecodeError):
            raise ComextError("Eurostat Comext API request failed") from None

        try:
            if payload.get("class") != "dataset":
                raise ValueError("response is not a JSON-stat dataset")
            cells = [
                cell
                for cell in decode_cells(payload)
                if cell["value"] is not None or cell["status"] is not None
            ]
            observed_at = self.clock()
            return [normalize_cell(cell, observed_at, request_url) for cell in cells]
        except (KeyError, TypeError, ValueError) as exc:
            raise ComextError(f"Invalid Comext JSON-stat response: {exc}") from exc
