import json
from datetime import datetime, timezone
from io import BytesIO
from urllib.error import URLError
from urllib.parse import parse_qs, urlparse

import pytest

from asymmetry_engine.db import Repository
from asymmetry_engine.pipeline import run_collection
from asymmetry_engine.sources.openalex import (
    MODEL_TIME_CAVEAT,
    SOURCE_ID,
    TOPIC_IDS,
    TOPICS_URL,
    WORKS_URL,
    YEARS,
    OpenAlexCollector,
    OpenAlexError,
    normalize_measurement,
    openalex_source,
)

NOW = datetime(2026, 9, 3, 13, tzinfo=timezone.utc)


def topic(topic_id):
    return {
        "id": f"https://openalex.org/{topic_id}",
        "display_name": f"Topic {topic_id}",
        "description": "Source-native description",
        "keywords": ["one", "two"],
        "subfield": {"id": "https://openalex.org/subfields/1702", "display_name": "AI"},
        "field": {"id": "https://openalex.org/fields/17", "display_name": "Computer Science"},
        "domain": {"id": "https://openalex.org/domains/3", "display_name": "Physical Sciences"},
    }


class Response(BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def api_opener(request, timeout):
    parsed = urlparse(request.full_url)
    if parsed.path == "/topics":
        return Response(json.dumps({"results": [topic(i) for i in reversed(TOPIC_IDS)]}).encode())
    query = parse_qs(parsed.query)
    topic_id = query["filter"][0].split(":", 1)[1].split(",", 1)[0]
    offset = TOPIC_IDS.index(topic_id)
    return Response(
        json.dumps(
            {
                "results": [],
                "group_by": [
                    {"key": "2019", "key_display_name": "2019", "count": 30 + offset},
                    {"key": "2017", "key_display_name": "2017", "count": 10 + offset},
                    {"key": "2018", "key_display_name": "2018", "count": 20 + offset},
                ],
            }
        ).encode()
    )


def test_collector_makes_only_bounded_official_requests():
    requests = []

    def opener(request, timeout):
        requests.append((request, timeout))
        return api_opener(request, timeout)

    observations = OpenAlexCollector(opener=opener, clock=lambda: NOW, api_key="secret").collect()
    assert len(observations) == len(TOPIC_IDS) * len(YEARS)
    assert len(requests) == 1 + len(TOPIC_IDS) == 10
    assert urlparse(requests[0][0].full_url).path == "/topics"
    assert parse_qs(urlparse(requests[0][0].full_url).query)["filter"] == [
        "openalex:" + "|".join(TOPIC_IDS)
    ]
    for request, timeout in requests[1:]:
        assert request.full_url.startswith(WORKS_URL)
        assert timeout == 30
        query = parse_qs(urlparse(request.full_url).query)
        assert query["group_by"] == ["publication_year"]
        assert "publication_year:2017-2019" in query["filter"][0]
        assert "secret" not in request.full_url
        assert request.get_header("Authorization") == "Bearer secret"


def test_hierarchy_content_timestamp_and_metadata_are_source_faithful():
    observation = normalize_measurement(topic(TOPIC_IDS[0]), 2018, 42, NOW, "https://api/query")
    assert observation.source_id == SOURCE_ID
    assert observation.item_kind == "research_statistic"
    assert observation.observed_at == NOW
    assert observation.occurred_at is None
    assert "Subfield: AI (1702)" in observation.content
    assert "Field: Computer Science (17)" in observation.content
    assert "Domain: Physical Sciences (3)" in observation.content
    assert "Publication year: 2018" in observation.content
    assert "Works count: 42" in observation.content
    assert observation.metadata["subfield"] == {"id": "1702", "display_name": "AI"}
    assert observation.metadata["field"]["id"] == "17"
    assert observation.metadata["domain"]["id"] == "3"
    assert observation.metadata["topic_classification_caveat"] == MODEL_TIME_CAVEAT


def test_identity_excludes_count_and_collection_timestamp():
    first = normalize_measurement(topic(TOPIC_IDS[0]), 2017, 10, NOW, "https://api/query")
    changed = normalize_measurement(
        topic(TOPIC_IDS[0]), 2017, 999, NOW.replace(year=2027), "https://api/query"
    )
    assert first.external_id == changed.external_id == f"openalex:{TOPIC_IDS[0]}:works_count:2017"
    assert "999" not in changed.external_id
    assert "2026" not in first.external_id


def test_grouped_counts_map_to_correct_topic_and_year_despite_response_order():
    observations = OpenAlexCollector(opener=api_opener, clock=lambda: NOW, api_key="").collect()
    values = {(o.metadata["topic_id"], o.metadata["publication_year"]): o.metadata["works_count"] for o in observations}
    assert values[(TOPIC_IDS[0], 2017)] == 10
    assert values[(TOPIC_IDS[0], 2019)] == 30
    assert values[(TOPIC_IDS[-1], 2018)] == 20 + len(TOPIC_IDS) - 1


@pytest.mark.parametrize("payload", [b"not-json", b'[]', b'{"results":"wrong"}'])
def test_malformed_responses_fail_clearly(payload):
    def opener(request, timeout):
        return Response(payload)

    with pytest.raises(OpenAlexError):
        OpenAlexCollector(opener=opener, api_key="").collect()


def test_network_failure_fails_without_retry():
    calls = 0

    def opener(request, timeout):
        nonlocal calls
        calls += 1
        raise URLError("offline")

    with pytest.raises(OpenAlexError, match="request failed"):
        OpenAlexCollector(opener=opener, api_key="").collect()
    assert calls == 1


def test_source_metadata_retains_current_model_time_caveat():
    source = openalex_source()
    assert source.source_id == SOURCE_ID
    assert source.metadata["topic_classification_caveat"] == MODEL_TIME_CAVEAT
    assert "model-generated" in source.selection_biases
    assert "publication volume is not commercial demand" in source.selection_biases
    assert "lack topic classification" in source.selection_biases


def test_identical_collection_deduplicates(tmp_path):
    collector = OpenAlexCollector(opener=api_opener, clock=lambda: NOW, api_key="")
    repository = Repository(tmp_path / "test.db")
    first = run_collection(collector, repository, lambda: NOW)
    second = run_collection(collector, repository, lambda: NOW)
    expected = len(TOPIC_IDS) * len(YEARS)
    assert (first.inserted_count, first.duplicate_count) == (expected, 0)
    assert (second.inserted_count, second.duplicate_count) == (0, expected)
    repository.close()
