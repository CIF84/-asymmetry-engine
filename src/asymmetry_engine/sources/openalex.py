from __future__ import annotations

import json
import os
from datetime import datetime
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from ..models import SignalSource, SourceObservation, utc_now

API_BASE = "https://api.openalex.org"
TOPICS_URL = f"{API_BASE}/topics"
WORKS_URL = f"{API_BASE}/works"
SOURCE_ID = "openalex:knowledge-topology"
YEARS = (2017, 2018, 2019)
TOPIC_IDS = (
    "T12072",  # Machine Learning and Algorithms
    "T10320",  # Neural Networks and Applications
    "T10181",  # Natural Language Processing Techniques
    "T10036",  # Advanced Neural Network Applications
    "T12549",  # Image and Object Detection Techniques
    "T10363",  # Low-power high-performance VLSI design
    "T11522",  # VLSI and FPGA Design Techniques
    "T10904",  # Embedded Systems Design Techniques
    "T10502",  # Advanced Memory and Neural Computing
)
MODEL_TIME_CAVEAT = (
    "OpenAlex topic assignments are model-generated. These current classifications "
    "are applied retrospectively to historical works and therefore introduce model-time "
    "leakage; they were not classifications available in 2019."
)


class OpenAlexError(RuntimeError):
    pass


def openalex_source() -> SignalSource:
    return SignalSource(
        source_id=SOURCE_ID,
        name="OpenAlex Knowledge Topology",
        access_method="Official OpenAlex API (anonymous casual access or optional API key)",
        terms_reference="https://openalex.org/OpenAlex_termsofservice.pdf",
        commercial_use_considerations=(
            "OpenAlex states that its data is released under CC0; API service access is "
            "also subject to the current OpenAlex terms and usage limits."
        ),
        selection_biases=(
            "Publication coverage varies by field, source, language, and year; counts can "
            "change as OpenAlex updates records; topic assignments are model-generated "
            "rather than author-provided ground truth; current classifications applied "
            "retrospectively create model-time leakage; publication volume is not "
            "commercial demand and count alone does not prove technological importance; "
            "some works lack topic classification."
        ),
        metadata={
            "api_base": API_BASE,
            "access": "keyless casual API access; OPENALEX_API_KEY supported as bearer token",
            "reuse": "OpenAlex data released under CC0; service subject to current terms",
            "evidence_semantics": (
                "scholarly/research activity plus source-native semantic classification"
            ),
            "geography": "global scholarly corpus",
            "topic_classification_caveat": MODEL_TIME_CAVEAT,
            "collection_method": "topic metadata batch lookup and grouped works counts",
        },
    )


def _short_id(value: Any, expected_prefix: str) -> str:
    if not isinstance(value, str):
        raise ValueError(f"missing {expected_prefix} ID")
    result = value.rstrip("/").rsplit("/", 1)[-1]
    if not result.startswith(expected_prefix):
        raise ValueError(f"invalid {expected_prefix} ID: {value}")
    return result


def _hierarchy_node(topic: dict[str, Any], name: str) -> dict[str, str]:
    node = topic[name]
    if not isinstance(node, dict) or not isinstance(node.get("display_name"), str):
        raise ValueError(f"topic is missing {name} hierarchy metadata")
    node_id = node.get("id")
    if not isinstance(node_id, str):
        raise ValueError(f"topic is missing {name} ID")
    short_id = node_id.rstrip("/").rsplit("/", 1)[-1]
    if not short_id.isdigit():
        raise ValueError(f"invalid {name} ID: {node_id}")
    return {"id": short_id, "display_name": node["display_name"]}


def normalize_measurement(
    topic: dict[str, Any], year: int, count: int, observed_at: datetime, request_url: str
) -> SourceObservation:
    topic_id = _short_id(topic.get("id"), "T")
    label = topic.get("display_name")
    if not isinstance(label, str) or not label:
        raise ValueError("topic is missing display_name")
    if year not in YEARS or not isinstance(count, int) or isinstance(count, bool) or count < 0:
        raise ValueError("invalid annual topic measurement")
    subfield = _hierarchy_node(topic, "subfield")
    field = _hierarchy_node(topic, "field")
    domain = _hierarchy_node(topic, "domain")
    content = "\n".join(
        (
            "Source: OpenAlex",
            f"Topic: {label} ({topic_id})",
            f"Subfield: {subfield['display_name']} ({subfield['id']})",
            f"Field: {field['display_name']} ({field['id']})",
            f"Domain: {domain['display_name']} ({domain['id']})",
            f"Publication year: {year}",
            f"Works count: {count}",
        )
    )
    return SourceObservation(
        source_id=SOURCE_ID,
        external_id=f"openalex:{topic_id}:works_count:{year}",
        observed_at=observed_at,
        occurred_at=None,
        item_kind="research_statistic",
        content=content,
        canonical_url=f"https://openalex.org/{topic_id}",
        metadata={
            "topic_id": topic_id,
            "topic_display_name": label,
            "topic_description": topic.get("description"),
            "topic_keywords": topic.get("keywords", []),
            "subfield": subfield,
            "field": field,
            "domain": domain,
            "publication_year": year,
            "works_count": count,
            "measurement": "works_count",
            "api_url": request_url,
            "api_query": request_url.partition("?")[2],
            "collection_method": "OpenAlex Works API group_by=publication_year",
            "topic_classification_caveat": MODEL_TIME_CAVEAT,
        },
    )


class OpenAlexCollector:
    def __init__(
        self,
        opener: Callable[..., Any] = urlopen,
        clock: Callable[[], datetime] = utc_now,
        api_key: str | None = None,
    ) -> None:
        self.opener = opener
        self.clock = clock
        self.api_key = api_key if api_key is not None else os.getenv("OPENALEX_API_KEY")
        self.source = openalex_source()
        self.successful_request_count = 0
        self.response_bytes = 0

    def _get(self, url: str) -> dict[str, Any]:
        headers = {"Accept": "application/json", "User-Agent": "asymmetry-engine/0.1"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        request = Request(url, headers=headers)
        try:
            with self.opener(request, timeout=30) as response:
                raw = response.read()
            payload = json.loads(raw)
        except (HTTPError, URLError, TimeoutError, OSError, json.JSONDecodeError):
            raise OpenAlexError("OpenAlex API request failed") from None
        if not isinstance(payload, dict):
            raise OpenAlexError("Invalid OpenAlex response: expected an object")
        self.successful_request_count += 1
        self.response_bytes += len(raw)
        return payload

    def collect(self) -> list[SourceObservation]:
        self.successful_request_count = 0
        self.response_bytes = 0
        topic_url = f"{TOPICS_URL}?{urlencode({
            'filter': 'openalex:' + '|'.join(TOPIC_IDS),
            'per_page': len(TOPIC_IDS),
            'select': 'id,display_name,description,keywords,subfield,field,domain',
        })}"
        try:
            payload = self._get(topic_url)
            results = payload["results"]
            if not isinstance(results, list):
                raise ValueError("topic results must be a list")
            topics = {_short_id(item.get("id"), "T"): item for item in results}
            if set(topics) != set(TOPIC_IDS):
                raise ValueError("topic lookup did not return the exact selected topic set")

            observed_at = self.clock()
            observations: list[SourceObservation] = []
            for topic_id in TOPIC_IDS:
                count_url = f"{WORKS_URL}?{urlencode({
                    'filter': f'topics.id:{topic_id},publication_year:{YEARS[0]}-{YEARS[-1]}',
                    'group_by': 'publication_year',
                    'per_page': len(YEARS),
                })}"
                grouped = self._get(count_url).get("group_by")
                if not isinstance(grouped, list):
                    raise ValueError("works response is missing group_by")
                counts = {year: 0 for year in YEARS}
                for group in grouped:
                    year = int(group["key"])
                    count = group["count"]
                    if year not in counts or not isinstance(count, int) or isinstance(count, bool):
                        raise ValueError("invalid publication-year group")
                    counts[year] = count
                observations.extend(
                    normalize_measurement(topics[topic_id], year, counts[year], observed_at, count_url)
                    for year in YEARS
                )
            return observations
        except (KeyError, TypeError, ValueError) as exc:
            raise OpenAlexError(f"Invalid OpenAlex response: {exc}") from exc
