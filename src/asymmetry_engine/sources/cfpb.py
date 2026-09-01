from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen

from ..models import SignalSource, SourceObservation, utc_now

API_URL = "https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/"
DETAIL_URL = "https://www.consumerfinance.gov/data-research/consumer-complaints/search/detail"
SOURCE_ID = "cfpb:consumer-complaints"


class CFPBError(RuntimeError):
    pass


def cfpb_source() -> SignalSource:
    return SignalSource(
        source_id=SOURCE_ID,
        name="CFPB Consumer Complaint Database",
        access_method="Official CFPB Consumer Complaint Database search API v1",
        terms_reference="https://www.consumerfinance.gov/data-research/consumer-complaints/",
        commercial_use_considerations=(
            "Published complaint data is provided under CC0 and CFPB states it is freely "
            "available to use, analyze, and build on. Allegations are not verified facts."
        ),
        selection_biases=(
            "Not a statistical sample of consumer experience. Complaints are self-selected, "
            "not necessarily representative of all consumers, products, or companies, and "
            "counts require context such as company size, market share, usage, and population. "
            "CFPB does not verify every allegation; some complaints referred to other regulators "
            "are excluded. The data is primarily US-specific, shaped by the CFPB process, and "
            "recent records may be incomplete because publication can follow response or delay."
        ),
        metadata={
            "api_base": API_URL,
            "geographic_scope": "United States",
            "institutional_scope": "Complaints published through the CFPB complaint process",
            "license": "CC0",
            "narrative_policy": "Narratives are optional and collection does not depend on them.",
        },
    )


def _parse_source_date(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def normalize_complaint(
    item: dict[str, Any], observed_at: datetime
) -> SourceObservation:
    complaint_id = str(item["complaint_id"])
    occurred_at = _parse_source_date(item["date_received"])
    content_fields = (
        ("Product", "product"),
        ("Sub-product", "sub_product"),
        ("Issue", "issue"),
        ("Sub-issue", "sub_issue"),
        ("Company", "company"),
        ("Company response", "company_response"),
    )
    content = "\n".join(
        f"{label}: {item[key]}" for label, key in content_fields if item.get(key)
    )
    metadata_fields = (
        "product",
        "sub_product",
        "issue",
        "sub_issue",
        "company",
        "company_public_response",
        "company_response",
        "timely",
        "state",
        "zip_code",
        "tags",
        "submitted_via",
        "date_sent_to_company",
        "complaint_what_happened",
        "has_narrative",
    )
    metadata = {key: item[key] for key in metadata_fields if key in item}
    return SourceObservation(
        source_id=SOURCE_ID,
        external_id=f"cfpb:complaint:{complaint_id}",
        observed_at=observed_at,
        occurred_at=occurred_at,
        item_kind="complaint",
        content=content,
        canonical_url=f"{DETAIL_URL}/{complaint_id}",
        metadata=metadata,
    )


class CFPBCollector:
    def __init__(
        self,
        sample_size: int = 25,
        opener: Callable[..., Any] = urlopen,
        clock: Callable[[], datetime] = utc_now,
    ) -> None:
        if not 1 <= sample_size <= 100:
            raise ValueError("sample_size must be between 1 and 100")
        self.sample_size = sample_size
        self.opener = opener
        self.clock = clock
        self.source = cfpb_source()

    def collect(self) -> list[SourceObservation]:
        query = urlencode(
            {
                "size": self.sample_size,
                "sort": "created_date_desc",
                "no_aggs": "true",
            }
        )
        try:
            with self.opener(f"{API_URL}?{query}", timeout=30) as response:
                payload = json.load(response)
        except (HTTPError, URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
            raise CFPBError(f"CFPB request failed: {exc}") from exc

        if payload.get("timed_out") is True:
            raise CFPBError("CFPB API search timed out")
        observed_at = self.clock()
        try:
            hits = payload["hits"]["hits"]
            return [normalize_complaint(hit["_source"], observed_at) for hit in hits]
        except (KeyError, TypeError, ValueError) as exc:
            raise CFPBError(f"Invalid CFPB response: {exc}") from exc
