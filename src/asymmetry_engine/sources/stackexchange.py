from __future__ import annotations

import json
import time
from datetime import datetime, timezone
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen

from ..models import SignalSource, SourceObservation, utc_now

API_URL = "https://api.stackexchange.com/2.3/questions"


class StackExchangeError(RuntimeError):
    pass


def source_for_site(site: str) -> SignalSource:
    return SignalSource(
        source_id=f"stackexchange:{site}",
        name=f"Stack Exchange ({site})",
        access_method="Stack Exchange API v2.3 /questions",
        terms_reference="https://stackoverflow.com/legal/api-terms-of-use",
        commercial_use_considerations=(
            "API terms and the applicable Stack Exchange content licence must be reviewed "
            "before commercial reuse; attribution may be required."
        ),
        selection_biases=(
            "Self-selected Stack Exchange users; comparatively technical/prosumer-oriented "
            "and not representative of the general or global population."
        ),
        metadata={"site": site, "api_base": API_URL},
    )


def normalize_question(
    item: dict[str, Any], site: str, observed_at: datetime
) -> SourceObservation:
    question_id = int(item["question_id"])
    created = item.get("creation_date")
    occurred_at = (
        datetime.fromtimestamp(created, timezone.utc) if created is not None else None
    )
    metadata = {
        key: item[key]
        for key in (
            "tags",
            "score",
            "view_count",
            "answer_count",
            "is_answered",
            "accepted_answer_id",
            "last_activity_date",
            "content_license",
        )
        if key in item
    }
    return SourceObservation(
        source_id=f"stackexchange:{site}",
        external_id=f"{site}:question:{question_id}",
        observed_at=observed_at,
        occurred_at=occurred_at,
        item_kind="question",
        content=item.get("title", ""),
        canonical_url=item.get("link"),
        metadata=metadata,
    )


class StackExchangeCollector:
    def __init__(
        self,
        site: str = "money",
        sample_size: int = 25,
        opener: Callable[..., Any] = urlopen,
        sleeper: Callable[[float], None] = time.sleep,
        clock: Callable[[], datetime] = utc_now,
    ) -> None:
        if not 1 <= sample_size <= 100:
            raise ValueError("sample_size must be between 1 and 100")
        self.site = site
        self.sample_size = sample_size
        self.opener = opener
        self.sleeper = sleeper
        self.clock = clock
        self.source = source_for_site(site)

    def collect(self) -> list[SourceObservation]:
        query = urlencode(
            {
                "site": self.site,
                "pagesize": self.sample_size,
                "page": 1,
                "order": "desc",
                "sort": "creation",
            }
        )
        try:
            with self.opener(f"{API_URL}?{query}", timeout=30) as response:
                payload = json.load(response)
        except (HTTPError, URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
            raise StackExchangeError(f"Stack Exchange request failed: {exc}") from exc

        if "error_id" in payload:
            message = payload.get("error_message", "unknown API error")
            raise StackExchangeError(f"Stack Exchange API error: {message}")
        backoff = payload.get("backoff")
        if backoff is not None:
            self.sleeper(float(backoff))
        observed_at = self.clock()
        try:
            return [normalize_question(item, self.site, observed_at) for item in payload["items"]]
        except (KeyError, TypeError, ValueError) as exc:
            raise StackExchangeError(f"Invalid Stack Exchange response: {exc}") from exc
