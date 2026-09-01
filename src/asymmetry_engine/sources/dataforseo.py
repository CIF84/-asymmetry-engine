from __future__ import annotations

import base64
import json
import os
import unicodedata
from datetime import datetime
from typing import Any, Callable, Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

from ..models import SignalSource, SourceObservation, utc_now
from .dataforseo_seeds import KEYWORD_SEEDS

API_URL = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"
DOCS_URL = "https://docs.dataforseo.com/v3/keywords_data-google_ads-search-volume-live/"
SOURCE_ID = "dataforseo:google-ads-keyword-demand"
US_LOCATION_CODE = 2840
ENGLISH_LANGUAGE_CODE = "en"


class DataForSEOError(RuntimeError):
    pass


def dataforseo_source() -> SignalSource:
    return SignalSource(
        source_id=SOURCE_ID,
        name="DataForSEO Google Ads Keyword Demand",
        access_method="Paid DataForSEO v3 Google Ads Search Volume Live API",
        terms_reference="https://dataforseo.com/terms-of-service",
        commercial_use_considerations=(
            "Paid vendor-mediated data sold for programmatic analytics use. Terms and product "
            "policies can change and must be rechecked before large-scale dependence or raw-data "
            "redistribution. DataForSEO is a vendor dependency, not an open public source."
        ),
        selection_biases=(
            "Google Ads-derived search volume is approximate search activity, not unique people, "
            "customers, exact demand, or willingness to pay. Measurements depend on geography, "
            "language, provider processing, and keyword grouping. CPC, competition, and bids are "
            "paid-advertising market metrics, not evidence of product profitability."
        ),
        metadata={
            "api_endpoint": API_URL,
            "provider": "DataForSEO",
            "metric_origin": "Google Ads-derived",
            "access": "paid",
            "request_cost_applies": True,
        },
    )


def normalized_keyword(value: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


def keyword_external_id(keyword: str, location_code: int, language_code: str) -> str:
    encoded_keyword = quote(normalized_keyword(keyword), safe="")
    encoded_language = quote(language_code.casefold(), safe="")
    return f"dataforseo:keyword:{encoded_keyword}:{location_code}:{encoded_language}"


def normalize_keyword_measurement(
    item: dict[str, Any],
    observed_at: datetime,
    request_context: dict[str, Any],
    task_metadata: dict[str, Any] | None = None,
) -> SourceObservation:
    keyword = str(item["keyword"])
    location_code = item.get("location_code") or request_context["location_code"]
    language_code = item.get("language_code") or request_context["language_code"]
    display_fields = (
        ("Keyword", "keyword", None),
        ("Search volume", "search_volume", None),
        ("Competition", "competition", None),
        ("Competition index", "competition_index", None),
        ("CPC", "cpc", "USD"),
        ("Low top-of-page bid", "low_top_of_page_bid", "USD"),
        ("High top-of-page bid", "high_top_of_page_bid", "USD"),
    )
    lines = []
    for label, key, unit in display_fields:
        value = item.get(key)
        if value is not None:
            suffix = f" {unit}" if unit else ""
            lines.append(f"{label}: {value}{suffix}")

    result_fields = (
        "keyword",
        "spell",
        "location_code",
        "language_code",
        "search_partners",
        "competition",
        "competition_index",
        "search_volume",
        "low_top_of_page_bid",
        "high_top_of_page_bid",
        "cpc",
        "monthly_searches",
    )
    metadata = {key: item[key] for key in result_fields if key in item}
    metadata["request_location_code"] = request_context["location_code"]
    metadata["request_language_code"] = request_context["language_code"]
    metadata["request_search_partners"] = request_context["search_partners"]
    if task_metadata:
        metadata.update(task_metadata)

    return SourceObservation(
        source_id=SOURCE_ID,
        external_id=keyword_external_id(keyword, int(location_code), str(language_code)),
        observed_at=observed_at,
        occurred_at=None,
        item_kind="keyword_demand",
        content="\n".join(lines),
        canonical_url=DOCS_URL,
        metadata=metadata,
    )


class DataForSEOKeywordCollector:
    def __init__(
        self,
        keywords: Iterable[str] = KEYWORD_SEEDS,
        location_code: int = US_LOCATION_CODE,
        language_code: str = ENGLISH_LANGUAGE_CODE,
        login: str | None = None,
        password: str | None = None,
        opener: Callable[..., Any] = urlopen,
        clock: Callable[[], datetime] = utc_now,
    ) -> None:
        self.keywords = tuple(keywords)
        if not 1 <= len(self.keywords) <= 1000:
            raise ValueError("keywords must contain between 1 and 1000 phrases")
        self.location_code = location_code
        self.language_code = language_code
        self._login = login if login is not None else os.getenv("DATAFORSEO_LOGIN")
        self._password = password if password is not None else os.getenv("DATAFORSEO_PASSWORD")
        self.opener = opener
        self.clock = clock
        self.source = dataforseo_source()

    def collect(self) -> list[SourceObservation]:
        if not self._login or not self._password:
            raise DataForSEOError(
                "DataForSEO credentials are missing; set DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD"
            )
        context = {
            "location_code": self.location_code,
            "language_code": self.language_code,
            "search_partners": False,
        }
        body = json.dumps([{**context, "keywords": list(self.keywords)}]).encode()
        token = base64.b64encode(
            f"{self._login}:{self._password}".encode()
        ).decode("ascii")
        request = Request(
            API_URL,
            data=body,
            headers={
                "Authorization": f"Basic {token}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with self.opener(request, timeout=60) as response:
                payload = json.load(response)
        except (HTTPError, URLError, TimeoutError, OSError, json.JSONDecodeError):
            raise DataForSEOError("DataForSEO request failed") from None

        if payload.get("status_code") != 20000:
            raise DataForSEOError(
                f"DataForSEO API error {payload.get('status_code', 'unknown')}"
            )
        try:
            tasks = payload["tasks"]
            if len(tasks) != 1:
                raise DataForSEOError("DataForSEO returned an unexpected task count")
            task = tasks[0]
            if task.get("status_code") != 20000:
                raise DataForSEOError(
                    f"DataForSEO task error {task.get('status_code', 'unknown')}"
                )
            task_metadata = {
                "provider_task_id": task.get("id"),
                "provider_task_cost": task.get("cost"),
                "provider_task_status_code": task.get("status_code"),
            }
            observed_at = self.clock()
            return [
                normalize_keyword_measurement(item, observed_at, context, task_metadata)
                for item in (task.get("result") or [])
            ]
        except (KeyError, TypeError, ValueError) as exc:
            raise DataForSEOError("Invalid DataForSEO response") from exc
