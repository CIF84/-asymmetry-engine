# FROZEN PACKAGE ARTIFACT — TREATMENT / WORK PACKAGE A

## Package identity

- **Experiment:** Asymmetry Engine Experiment 041
- **Arm:** TREATMENT
- **Role:** PACKAGE-A AGENT
- **Package:** Work Package A — Implemented Software Truth
- **Baseline:** `6360064ea874e7350de2121e9cc569b9045fd1e0`
- **UTC start:** `2026-09-04T12:00:07Z`
- **UTC end:** `2026-09-04T12:01:09Z`
- **Measured internal interval:** 62 seconds
- **Repository mutation:** None
- **External interaction:** None
- **Human interventions/clarifications:** 0
- **Retries:** 0
- **Context restarts:** 0
- **Compute/model cost:** UNKNOWN
- **External spend:** €0
- **Test execution:** Not performed; the instruction required read-only operation, while the test suite uses temporary SQLite files. Findings are based on static inspection of code and tests.
- **Artifact persistence:** Returned as this frozen response; not written to `experiments/041/treatment-A.md` because the instruction explicitly prohibited modifying anything.

## Evidence read

Primary implementation evidence:

- [pyproject.toml](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/pyproject.toml:1)
- [src/asymmetry_engine/__main__.py](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/__main__.py:1)
- [src/asymmetry_engine/cli.py](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/cli.py:1)
- [src/asymmetry_engine/models.py](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/models.py:1)
- [src/asymmetry_engine/pipeline.py](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/pipeline.py:1)
- [src/asymmetry_engine/db.py](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:1)
- [src/asymmetry_engine/reasoning.py](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/reasoning.py:1)
- All modules under `src/asymmetry_engine/sources/`

Primary test evidence:

- All ten files under `tests/`, comprising 80 test functions
- Persistence/revision details: [tests/test_pipeline.py](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_pipeline.py:45)
- Domain reasoning: [tests/test_reasoning.py](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_reasoning.py:80)

Permitted documentation cross-checks:

- [specs/041-parallel-work-package-agentic-test.md](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/specs/041-parallel-work-package-agentic-test.md:1), read completely
- [experiments/041/preregistration.md](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/experiments/041/preregistration.md:1), read completely
- [ARCHITECTURE.md](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/ARCHITECTURE.md:1), read completely

No Package B, control-arm, other treatment-arm output, or live Experiment 030/035 state was read.

## Structured findings

### 1. Implemented modules and current entry points

The implementation is a Python 3.11+ modular monolith with no runtime dependencies outside the standard library; pytest is optional for testing. Its installed console entry point is `asymmetry-engine = asymmetry_engine.cli:main` ([pyproject.toml:5](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/pyproject.toml:5), [pyproject.toml:15](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/pyproject.toml:15)). `python -m asymmetry_engine` invokes the same function ([__main__.py:1](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/__main__.py:1)).

Implemented modules:

- `models.py`: UTC serialization and frozen `SignalSource`/`SourceObservation` domain inputs ([models.py:8](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/models.py:8), [models.py:18](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/models.py:18)).
- `db.py`: SQLite schema, legacy migration, run accounting, revision capture, latest reads.
- `pipeline.py`: collector protocol, run result, and one-collector execution pipeline ([pipeline.py:12](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/pipeline.py:12), [pipeline.py:28](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/pipeline.py:28)).
- `reasoning.py`: one fixed Czech CN75 trade reasoner.
- `cli.py`: eight general collection commands, one specialized CN75 collection command, and `reason-cn75` ([cli.py:19](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/cli.py:19), [cli.py:48](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/cli.py:48)).
- Source adapters: Stack Exchange, CFPB, DataForSEO, TED, Eurostat SBS, Azure Retail Prices, Eurostat Comext—including a specialized CN75 collector—and OpenAlex.

The CLI creates the database parent directory, constructs one collector, runs it, prints run counts, and returns exit status 0 only for success ([cli.py:81](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/cli.py:81)).

### 2. Source-adapter boundary and responsibilities

Every collector satisfies the structural `Collector` protocol: it exposes a `SignalSource` and returns a list of normalized `SourceObservation` objects ([pipeline.py:12](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/pipeline.py:12)). No source module imports `Repository`, `sqlite3`, or `run_collection`.

Adapters own:

- Bounded, source-specific request construction and authentication.
- Response parsing and structural validation.
- Stable source-native logical identity.
- Conversion into common observation fields.
- Timestamp interpretation.
- Preservation of source-native facts in metadata.
- Access method, terms, commercial-use considerations, and selection-bias caveats.
- Source-specific failures, generally without automatic retry.

Examples include Stack Exchange pagination bounds/backoff ([stackexchange.py:122](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/sources/stackexchange.py:122)), DataForSEO credential/task handling ([dataforseo.py:122](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/sources/dataforseo.py:122)), fixed TED query/field selection ([ted.py:14](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/sources/ted.py:14)), JSON-stat decoding for Eurostat ([eurostat.py:91](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/sources/eurostat.py:91)), explicit refusal to follow Azure pagination ([azure_prices.py:177](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/sources/azure_prices.py:177)), and exact topic-set validation in OpenAlex ([openalex.py:175](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/sources/openalex.py:175)).

The generic pipeline owns run lifecycle; persistence owns deduplication/revision behavior. Adapters do not decide whether an observation is new, duplicate, or revised.

### 3. SQLite tables and transaction boundary

Three application tables exist:

1. `signal_sources`: current source description, access/terms fields, caveats, and JSON metadata ([db.py:12](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:12)).
2. `pipeline_runs`: source, start/completion times, status, fetched/inserted/duplicate counts, and error ([db.py:21](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:21)).
3. `source_observations`: immutable captures with surrogate ID, logical identity, positive capture sequence, timestamps, normalized content, metadata, and observing run ([db.py:35](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:35)).

Foreign keys are enabled per connection ([db.py:60](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:60)). An index supports descending sequence lookup by logical identity ([db.py:54](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:54)).

Transaction boundaries are:

- `start_run`: source upsert and insertion of a `running` run commit together, before network collection ([db.py:142](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:142)).
- `complete_run`: all changed/first-seen observation inserts and the final successful run-accounting update occur in one connection transaction ([db.py:150](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:150)).
- If completion fails, that entire capture batch rolls back; `run_collection` then records failure in a separate transaction ([pipeline.py:35](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/pipeline.py:35), [db.py:234](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:234)).
- Legacy observation migration uses explicit `BEGIN IMMEDIATE` and explicit rollback/commit around table creation, copy, drop, rename, and index creation ([db.py:91](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:91)).

Thus a run’s initial `running` record is intentionally committed separately from either its eventual successful batch or failure update.

### 4. Revision-aware observation semantics

Logical identity is `(source_id, external_id)`. Capture identity adds `capture_sequence`; the database uniqueness constraint is `(source_id, external_id, capture_sequence)` ([db.py:35](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:35)).

For each incoming observation, persistence compares only the latest capture’s:

- `occurred_at`
- `item_kind`
- `content`
- `canonical_url`
- canonicalized `metadata_json`

([db.py:162](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:162)).

`observed_at` and `pipeline_run_id` are deliberately excluded from material equality. An unchanged recapture creates no new row and preserves the original capture timestamp and run linkage ([tests/test_pipeline.py:94](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_pipeline.py:94)). A material change appends sequence `N+1`; it does not update prior evidence ([db.py:186](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:186)).

Comparison is against the latest state, not all historical states. Therefore `A → B → A` stores sequences 1, 2, and 3 ([tests/test_pipeline.py:134](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_pipeline.py:134)).

Legacy databases lacking `capture_sequence` are migrated by assigning all old observations sequence 1 while preserving IDs and payloads ([db.py:91](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:91), [tests/test_pipeline.py:280](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_pipeline.py:280)).

### 5. Current/latest read semantics

`latest_observations()` groups by `(source_id, external_id)`, selects `MAX(capture_sequence)`, rejoins the complete row, optionally filters by source, and sorts deterministically by source and external ID ([db.py:216](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:216)).

“Current” therefore means highest persisted capture sequence—not greatest observation timestamp, greatest occurrence timestamp, or latest successful run. The tests verify one deterministic current row per logical item ([tests/test_pipeline.py:186](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_pipeline.py:186)).

Historical rows remain in `source_observations`, but there is no public repository method for:

- as-of-time reads,
- revision ranges,
- a logical item’s complete history,
- current source-policy history,
- interpretation version history.

The CN75 reasoner uses `latest_observations(SOURCE_ID)` and consequently does not double-count prior revisions ([reasoning.py:111](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/reasoning.py:111), [tests/test_reasoning.py:153](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_reasoning.py:153)).

### 6. Implemented domain-specific reasoning capability

The only implemented reasoner is `build_cn75_argument()`, fixed to Czech imports, Eurostat Comext dataset `DS-045409`, flow code `1`, years 2023/2024, parent CN2 `75`, child CN8 `75022000`, and selected partners France and Italy ([reasoning.py:8](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/reasoning.py:8), [reasoning.py:17](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/reasoning.py:17)).

It computes:

- parent trade-value and net-mass growth,
- derived value-per-mass change,
- child contribution to parent value and mass changes,
- France/Italy contribution to child changes,
- supplier-value HHI for each year and its change.

It emits explicit economic entities, measurements, `PART_OF`/`SUPPLIES` relationships, observation-ID lineage, detected/unusual/decomposition/geography sections, supported interpretation, unsupported claims, alternative explanations, and next-best evidence ([reasoning.py:27](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/reasoning.py:27), [reasoning.py:202](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/reasoning.py:202)).

Missing required cells and zero growth baselines raise `ReasoningError` ([reasoning.py:101](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/reasoning.py:101), [reasoning.py:135](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/reasoning.py:135)). This is deterministic arithmetic and templated interpretation for one case—not general inference or opportunity scoring.

### 7. Tests and protected invariants

The repository contains 80 test functions across ten files.

Core persistence tests protect:

- source/run persistence and unchanged deduplication,
- failure recording without observations,
- complete-batch rollback on a constraint failure,
- exclusion of collection time from material equality,
- append-on-change for every material field,
- `A → B → A` revision behavior,
- mixed first/changed/duplicate accounting,
- deterministic latest reads,
- idempotent legacy migration,
- rollback of failed migration without leaving the temporary table.

See [tests/test_pipeline.py:45](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_pipeline.py:45) through [tests/test_pipeline.py:313](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_pipeline.py:313).

Adapter tests protect bounded requests, stable identities, timestamp rules, missing-value handling, response validation, error propagation, source caveats, and deduplication. Notable invariants include no invented zero for suppressed/missing statistical cells, no retry for several network failures, refusal of unexpected Azure pagination, exact OpenAlex topic coverage, and separation of changing measurements from stable logical identity.

Reasoning tests protect exact arithmetic, HHI, lineage, structural relationships, deterministic rendering, clear missing-evidence failure, use of latest captures, and the explicit refusal to infer that nickel market prices fell ([tests/test_reasoning.py:80](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_reasoning.py:80), [tests/test_reasoning.py:124](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_reasoning.py:124)).

UNKNOWN: runtime pass/fail status at the frozen baseline, because the tests were not executed.

### 8. Explicitly absent generic software capabilities

The code contains no implementation of:

- generic opportunity detection, clustering, registry, or scoring;
- generic decision extraction or exact-resolution comparison;
- generic FORGE/decision reasoning;
- scheduler, multi-source orchestration, or monitoring;
- web UI, API service, daemon, or microservices;
- experiment/outcome/asset/portfolio databases;
- interpretation versioning or historical source-policy snapshots;
- generic provenance graph, ontology, vector store, or ATLAS;
- experiment-economic telemetry infrastructure;
- interaction, outreach, exposure, response, attribution, or revenue tracking;
- permission, authorization, policy, regulatory, or autonomous-action services;
- event streaming or a general migration framework.

This matches the explicit absence statements in [ARCHITECTURE.md:227](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/ARCHITECTURE.md:227). The implemented program is collection, revision-aware storage, run accounting, latest reads, and one fixed reasoner.

### 9. Material discrepancies between code and `ARCHITECTURE.md`

No material semantic discrepancy was found.

The architecture’s principal claims are borne out by code:

- adapters normalize without SQLite knowledge;
- three SQLite tables exist;
- material comparison excludes collection time/run identity;
- revisions append;
- current reads select maximum sequence;
- successful batches are atomic;
- one CN75 reasoner exists;
- no scheduler/UI/service or generic opportunity engine exists.

Minor reconstructability discrepancies:

- The architecture’s repository tree omits the implemented `sources/dataforseo_seeds.py`, `__init__.py`, and `__main__.py` files ([ARCHITECTURE.md:29](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/ARCHITECTURE.md:29)).
- “The CLI exposes bounded source-collection commands” is accurate but compressed: there are eight named source families and nine collection commands because Comext has both broad and specialized CN75 collectors ([cli.py:22](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/cli.py:22)).
- The architecture describes historical captures as “available” ([ARCHITECTURE.md:110](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/ARCHITECTURE.md:110)); they are available through direct SQL, but the repository class exposes only the latest-read helper, not a dedicated history API.
- The architecture does not spell out that `start_run` commits before collection and that failure is recorded in a later transaction. Its statement about an atomic successful observation batch remains correct ([ARCHITECTURE.md:114](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/ARCHITECTURE.md:114)).

These are bounded documentation omissions or compression, not contradictions in implemented behavior.

### 10. Confidence and unknowns

**Overall confidence: HIGH for static implemented structure and semantics; MODERATE-HIGH for operational behavior.**

High-confidence findings are directly supported by current code plus focused tests: entry points, tables, transaction scopes, revision equality, latest selection, adapter separation, CN75 calculations, and explicitly absent modules.

Unknowns and limitations:

- Test-suite runtime status is UNKNOWN.
- Behavior against current live external APIs is UNKNOWN and was not inspected.
- SQLite behavior under concurrent writers is not specified or tested.
- There is no schema-version table; migration applicability is inferred solely from the presence of `capture_sequence`.
- Whether databases with noncanonical intermediate schemas migrate safely is UNKNOWN.
- Source metadata is mutable current state; historical policy/caveat snapshots are not recoverable from these tables.
- There is no public full-history/as-of API, although raw historical captures are retained.
- Domain reasoning outside the fixed CN75 case is absent, not merely unverified.
- Production deployment, sustained operation, scale, revenue, commercial value, and autonomous operation are not established by this software or its unit tests.

## Failures and diagnostic notes

- Git commands emitted macOS `xcrun` cache warnings because the read-only environment could not create temporary cache files under `/tmp`. Commit resolution and read-only status/diff inspection still completed.
- No retrieval retry was required.
- No repository file was changed.
