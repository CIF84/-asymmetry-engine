from __future__ import annotations

import json
from datetime import datetime
from itertools import product
from typing import Any, Callable, Iterator
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from ..models import SignalSource, SourceObservation, utc_now

DATASET = "sbs_ovw_act"
API_URL = (
    "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/"
    f"{DATASET}"
)
SOURCE_ID = "eurostat:sbs-market-structure"
GEO = "CZ"
REFERENCE_YEAR = "2023"
NACE_SECTIONS = tuple("BCDEFGHIJKLMNPQR")
INDICATORS = ("ENT_NR", "EMP_NR", "NETTUR_MEUR", "AV_MEUR")
UNIT_BY_INDICATOR = {
    "ENT_NR": ("NR", "number"),
    "EMP_NR": ("NR", "number"),
    "NETTUR_MEUR": ("MEUR", "million euro"),
    "AV_MEUR": ("MEUR", "million euro"),
}


class EurostatError(RuntimeError):
    pass


def eurostat_source() -> SignalSource:
    return SignalSource(
        source_id=SOURCE_ID,
        name="Eurostat Structural Business Statistics",
        access_method="Official Eurostat Statistics API",
        terms_reference="https://ec.europa.eu/eurostat/help/copyright-notice",
        commercial_use_considerations=(
            "Free public API access; this slice preserves a filtered subset of official "
            "aggregate statistics and their source-native units and flags."
        ),
        selection_biases=(
            "Structural Business Statistics covers its defined business economy and market "
            "producers rather than every economic activity. Statistical definitions and NACE "
            "coverage matter; values can be revised, and confidentiality or suppression can "
            "create missing cells. Monetary variables use dataset-specific scales. A large "
            "sector is not evidence of an information asymmetry, and a statistical cell is "
            "not an independent person- or firm-level observation."
        ),
        metadata={
            "api_endpoint": API_URL,
            "access": "free public API",
            "dataset": DATASET,
            "geographic_scope": "European statistics; empirical slice scoped to Czechia",
            "evidence_semantics": (
                "Official aggregate market-structure measurement, not individual demand "
                "or friction"
            ),
        },
    )


def query_parameters() -> list[tuple[str, str]]:
    parameters = [("lang", "en"), ("geo", GEO), ("time", REFERENCE_YEAR)]
    parameters.extend(("nace_r2", section) for section in NACE_SECTIONS)
    parameters.extend(("indic_sbs", indicator) for indicator in INDICATORS)
    return parameters


def _position_map(index: Any) -> dict[int, str]:
    if isinstance(index, dict):
        return {int(position): str(code) for code, position in index.items()}
    if isinstance(index, list):
        return {position: str(code) for position, code in enumerate(index)}
    raise ValueError("dimension category index must be an object or array")


def _sparse_item(container: Any, position: int) -> Any:
    if isinstance(container, dict):
        return container.get(str(position))
    if isinstance(container, list):
        return container[position] if position < len(container) else None
    if container is None:
        return None
    raise ValueError("JSON-stat values and statuses must be objects or arrays")


def decode_cells(payload: dict[str, Any]) -> Iterator[dict[str, Any]]:
    dimensions = payload["id"]
    sizes = payload["size"]
    if not isinstance(dimensions, list) or not isinstance(sizes, list):
        raise ValueError("JSON-stat id and size must be arrays")
    if len(dimensions) != len(sizes) or any(not isinstance(size, int) for size in sizes):
        raise ValueError("JSON-stat dimensions and sizes do not align")

    codes_by_dimension: list[dict[int, str]] = []
    labels_by_dimension: list[dict[str, str]] = []
    for dimension, size in zip(dimensions, sizes):
        category = payload["dimension"][dimension]["category"]
        positions = _position_map(category["index"])
        if set(positions) != set(range(size)):
            raise ValueError(f"invalid category index for {dimension}")
        codes_by_dimension.append(positions)
        labels_by_dimension.append(category.get("label", {}))

    values = payload.get("value")
    statuses = payload.get("status")
    for flat_position, coordinates in enumerate(product(*(range(size) for size in sizes))):
        codes = {
            dimension: codes_by_dimension[offset][coordinate]
            for offset, (dimension, coordinate) in enumerate(zip(dimensions, coordinates))
        }
        labels = {
            dimension: labels_by_dimension[offset].get(code, code)
            for offset, (dimension, code) in enumerate(codes.items())
        }
        yield {
            "dimensions": codes,
            "labels": labels,
            "value": _sparse_item(values, flat_position),
            "status": _sparse_item(statuses, flat_position),
        }


def normalize_cell(
    cell: dict[str, Any], observed_at: datetime, request_url: str
) -> SourceObservation:
    dimensions = cell["dimensions"]
    labels = cell["labels"]
    geo = dimensions["geo"]
    nace = dimensions["nace_r2"]
    indicator = dimensions["indic_sbs"]
    year = dimensions["time"]
    unit_code, unit_label = UNIT_BY_INDICATOR[indicator]
    value = cell["value"]
    status = cell["status"]

    lines = [
        "Dataset: Eurostat Structural Business Statistics (sbs_ovw_act)",
        f"Geography: {labels['geo']} ({geo})",
        f"NACE activity: {labels['nace_r2']} ({nace})",
        f"Measure: {labels['indic_sbs']} ({indicator})",
        f"Value: {value if value is not None else 'missing'}",
        f"Unit: {unit_label} ({unit_code})",
        f"Reference year: {year}",
    ]
    if status is not None:
        lines.append(f"Status: {status}")

    return SourceObservation(
        source_id=SOURCE_ID,
        external_id=(
            f"eurostat:{DATASET}:{geo}:{nace}:{indicator}:{unit_code}:{year}"
        ),
        observed_at=observed_at,
        occurred_at=None,
        item_kind="market_statistic",
        content="\n".join(lines),
        canonical_url=None,
        metadata={
            "dataset": DATASET,
            "frequency_code": dimensions["freq"],
            "frequency_label": labels["freq"],
            "geo_code": geo,
            "geo_label": labels["geo"],
            "nace_code": nace,
            "nace_label": labels["nace_r2"],
            "indicator_code": indicator,
            "indicator_label": labels["indic_sbs"],
            "unit_code": unit_code,
            "unit_label": unit_label,
            "reference_year": year,
            "value": value,
            "status": status,
            "api_url": request_url,
        },
    )


class EurostatCollector:
    def __init__(
        self,
        opener: Callable[..., Any] = urlopen,
        clock: Callable[[], datetime] = utc_now,
    ) -> None:
        self.opener = opener
        self.clock = clock
        self.source = eurostat_source()

    def collect(self) -> list[SourceObservation]:
        request_url = f"{API_URL}?{urlencode(query_parameters())}"
        request = Request(request_url, headers={"Accept": "application/json"})
        try:
            with self.opener(request, timeout=60) as response:
                payload = json.load(response)
        except (HTTPError, URLError, TimeoutError, OSError, json.JSONDecodeError):
            raise EurostatError("Eurostat Statistics API request failed") from None

        try:
            if payload.get("class") != "dataset":
                raise ValueError("response is not a JSON-stat dataset")
            cells = list(decode_cells(payload))
            observed_at = self.clock()
            return [normalize_cell(cell, observed_at, request_url) for cell in cells]
        except (KeyError, TypeError, ValueError) as exc:
            raise EurostatError(f"Invalid Eurostat JSON-stat response: {exc}") from exc
