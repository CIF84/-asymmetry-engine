from __future__ import annotations

import json
import re
from datetime import datetime, timedelta, timezone
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from ..models import SignalSource, SourceObservation, utc_now

API_URL = "https://api.ted.europa.eu/v3/notices/search"
SOURCE_ID = "ted:public-procurement"
EXPERT_QUERY = (
    "place-of-performance = CZE AND publication-date = 20260902 "
    "SORT BY publication-number DESC"
)
REQUEST_FIELDS = (
    "publication-number",
    "publication-date",
    "notice-title",
    "buyer-name",
    "buyer-country",
    "place-of-performance",
    "form-type",
    "notice-type",
    "main-classification-proc",
    "procedure-type",
    "total-value",
    "total-value-cur",
    "deadline",
    "notice-version",
    "notice-identifier",
)


class TEDError(RuntimeError):
    pass


def ted_source() -> SignalSource:
    return SignalSource(
        source_id=SOURCE_ID,
        name="TED Public Procurement Notices",
        access_method="Official anonymous TED Search API v3",
        terms_reference="https://ted.europa.eu/en/legal-notice",
        commercial_use_considerations=(
            "Free anonymous access to published TED notices for analysis and reuse; this "
            "evidence slice retains selected indexed fields rather than full notice XML."
        ),
        selection_biases=(
            "Represents procurement published through TED; thresholds and legal publication "
            "obligations affect coverage. Publication is not a completed purchase, notice count "
            "is not independent demand count, and one procedure may produce multiple notices, "
            "lots, or updates. Values may be missing, estimated, changed, or recorded at "
            "different procedure or lot levels."
        ),
        metadata={
            "api_endpoint": API_URL,
            "access": "free anonymous",
            "geographic_scope": "EU and European public procurement",
            "empirical_scope": "Place of performance associated with Czechia",
            "evidence_semantics": "Institutional procurement demand, not consumer demand",
        },
    )


def _unique(values: Any) -> list[Any]:
    if values is None:
        return []
    source = values if isinstance(values, list) else [values]
    result = []
    for value in source:
        if value not in result:
            result.append(value)
    return result


def _i18n_text(value: Any) -> str | None:
    if isinstance(value, str):
        return value
    if not isinstance(value, dict):
        return None
    for language in ("eng", "ces", *sorted(value)):
        candidate = value.get(language)
        if isinstance(candidate, list) and candidate:
            return str(candidate[0])
        if isinstance(candidate, str) and candidate:
            return candidate
    return None


def _publication_datetime(value: str) -> datetime:
    match = re.fullmatch(r"(\d{4}-\d{2}-\d{2})([+-]\d{2}:\d{2})?", value)
    if not match:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    day = datetime.strptime(match.group(1), "%Y-%m-%d")
    offset = match.group(2)
    if offset:
        sign = 1 if offset[0] == "+" else -1
        hours, minutes = map(int, offset[1:].split(":"))
        zone = timezone(sign * timedelta(hours=hours, minutes=minutes))
    else:
        zone = timezone.utc
    return day.replace(tzinfo=zone).astimezone(timezone.utc)


def _canonical_url(item: dict[str, Any]) -> tuple[str | None, dict[str, str]]:
    links = item.get("links") or {}
    html_urls = links.get("html") if isinstance(links, dict) else None
    if not isinstance(html_urls, dict):
        return None, {}
    for language in ("ENG", "CES", *sorted(html_urls)):
        if html_urls.get(language):
            return str(html_urls[language]), html_urls
    return None, html_urls


def normalize_notice(item: dict[str, Any], observed_at: datetime) -> SourceObservation:
    publication_number = str(item["publication-number"])
    publication_date = str(item["publication-date"])
    title = _i18n_text(item.get("notice-title"))
    buyer = _i18n_text(item.get("buyer-name"))
    form_type = item.get("form-type")
    notice_type = item.get("notice-type")
    cpv = _unique(item.get("main-classification-proc"))
    place = _unique(item.get("place-of-performance"))
    value = item.get("total-value")
    currencies = _unique(item.get("total-value-cur"))
    deadlines = _unique(item.get("deadline"))
    canonical_url, html_urls = _canonical_url(item)

    content_values = (
        ("Title", title),
        ("Buyer", buyer),
        ("Form type", form_type),
        ("Notice type", notice_type),
        ("Main classification (CPV)", ", ".join(map(str, cpv)) if cpv else None),
        ("Place of performance", ", ".join(map(str, place)) if place else None),
        (
            "Value",
            f"{value} {currencies[0]}" if value is not None and currencies else value,
        ),
        ("Submission deadline", ", ".join(map(str, deadlines)) if deadlines else None),
    )
    content = "\n".join(
        f"{label}: {value}" for label, value in content_values if value not in (None, "")
    )
    metadata = {
        key: item[key]
        for key in REQUEST_FIELDS
        if key in item
    }
    metadata.update(
        {
            "selected_title": title,
            "selected_buyer": buyer,
            "canonical_url": canonical_url,
            "html_urls": html_urls,
        }
    )
    return SourceObservation(
        source_id=SOURCE_ID,
        external_id=f"ted:notice:{publication_number}",
        observed_at=observed_at,
        occurred_at=_publication_datetime(publication_date),
        item_kind="procurement_notice",
        content=content,
        canonical_url=canonical_url,
        metadata=metadata,
    )


class TEDCollector:
    def __init__(
        self,
        sample_size: int = 75,
        opener: Callable[..., Any] = urlopen,
        clock: Callable[[], datetime] = utc_now,
    ) -> None:
        if not 1 <= sample_size <= 75:
            raise ValueError("sample_size must be between 1 and 75")
        self.sample_size = sample_size
        self.opener = opener
        self.clock = clock
        self.source = ted_source()

    def collect(self) -> list[SourceObservation]:
        body = {
            "query": EXPERT_QUERY,
            "fields": list(REQUEST_FIELDS),
            "page": 1,
            "limit": self.sample_size,
            "scope": "ALL",
            "checkQuerySyntax": False,
            "paginationMode": "PAGE_NUMBER",
        }
        request = Request(
            API_URL,
            data=json.dumps(body).encode(),
            headers={"Content-Type": "application/json", "Accept": "application/json"},
            method="POST",
        )
        try:
            with self.opener(request, timeout=60) as response:
                payload = json.load(response)
        except (HTTPError, URLError, TimeoutError, OSError, json.JSONDecodeError):
            raise TEDError("TED Search API request failed") from None
        if payload.get("timedOut") is True:
            raise TEDError("TED Search API request timed out")
        try:
            observed_at = self.clock()
            return [normalize_notice(item, observed_at) for item in payload["notices"]]
        except (KeyError, TypeError, ValueError) as exc:
            raise TEDError(f"Invalid TED Search API response: {exc}") from exc
