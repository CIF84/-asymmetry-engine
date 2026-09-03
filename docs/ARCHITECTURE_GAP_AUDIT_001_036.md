# Architecture Gap Audit — Experiments 001–036

**Experiment:** 037  
**Baseline:** `c652e509960bf80e7dd8a23e6dc84b5ee168f453`  
**Verdict:** **B — MATERIAL ADAPTATION EARNED**  
**Prospective timer start:** `2026-09-03T02:29:47Z`  
**Prospective timer end:** `2026-09-03T02:35:46Z`  
**Active elapsed time:** `5 minutes 59 seconds` (359 seconds), derived from prospectively captured UTC epoch timestamps while work remained active; no observation-window wait occurred  
**Incremental spend:** `€0`

## 1. Executive verdict

The implemented system is healthy but much narrower than `ARCHITECTURE.md`, `README.md`, and `ROADMAP.md` imply. Actual code is a compact observation-ingestion substrate plus one bounded CN75 reasoning slice. That substrate still supports learned needs: it is source-separated, deterministic, inexpensive, testable, provenance-conscious, and explicit about unsupported inference.

One repeated need has crossed the implementation threshold. Stable source-item identity is currently also the uniqueness key for a single stored capture. A later collection of the same item is discarded even if its content, price, status, metadata, or effective-date facts changed. This contradicts the increasingly important freshness, revision, and reproducibility needs learned after the early implementation. A small additive revision-capture design is earned, but it should receive a bounded implementation spec before code.

No generic opportunity, scoring, policy, experiment, decision, telemetry, interaction, or ATLAS system is earned. Recent experiments operate successfully through repository-centered Markdown contracts and artifacts rather than the early pipeline, so architecture should not be expanded merely to mirror the conceptual operating model.

## 2. Scope and isolation

Inspected:

- all current files under `src/asymmetry_engine/`;
- all current tests under `tests/`;
- CLI entry points and `pyproject.toml`;
- the SQLite schema and transaction boundaries;
- source adapters, normalization, detection/reasoning, and actual persistence callers;
- `ARCHITECTURE.md`, `README.md`, `ROADMAP.md`, source/operating/reasoning documents, checkpoints, and non-live experiment artifacts needed to establish repeated operational needs;
- repository history sufficient to distinguish early implemented behavior from later documentary learning.

Isolation was preserved. No current Reddit or GitHub response/reaction/state evidence for Experiments 030 or 035 was inspected. Their artifacts were not modified. No external actor was contacted, no opportunity candidates were generated, and no code was changed. `docs/OPPORTUNITY_MODEL_001_035.md` and `docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md` were not modified.

## 3. Actual current-code map

| Component | Actual responsibility | Persisted state | Entry/callers | Tests | Current operational use |
|---|---|---|---|---|---|
| `models.py` | Frozen `SignalSource` and `SourceObservation` records; UTC formatting | None directly | All collectors and repository | Exercised through adapter/pipeline tests | Shared ingestion primitive |
| `sources/*.py` | Nine bounded, source-specific collectors/normalizers: Stack Exchange, CFPB, DataForSEO, TED, Eurostat, Azure prices, Comext broad/CN75, and OpenAlex | None directly | CLI or tests; collectors return `SourceObservation` lists | Source-faithfulness, request bounds, failure, caveat, and dedup tests | Repository evidence shows use in Specs 001–012; no later pipeline use is preserved |
| `pipeline.py` | Runs one collector, creates a run, persists a complete batch, records failure | `pipeline_runs` through repository | CLI and tests | Success, duplicate, failure, rollback | Generic early ingestion path |
| `db.py` | Creates SQLite schema; upserts source; records runs; inserts first-seen source items; exposes `get_run` | `signal_sources`, `pipeline_runs`, `source_observations` | Pipeline; direct SQL in reasoner/tests | Transaction, dedup, failure | Small persistence substrate, with no migration/version layer |
| `reasoning.py` | Builds one deterministic Czech CN75 disequilibrium argument with measurements, relationships, lineage, caveats, alternatives, and next evidence | None; reads observation rows | `reason-cn75` CLI | Seven reasoning tests | Domain-specific Spec 012 vertical slice, not a generic detector |
| `cli.py` / entry point | Nine collection commands and one CN75 reasoning command | User-selected SQLite file | `asymmetry-engine` / `python -m` | Indirect command test for reasoner | Thin manual interface; no scheduling or orchestration |
| `tests/` | Protects bounded requests, normalization, source caveats, identity, timestamps, rollback, dedup, lineage, and unsupported-claim discipline | Pytest cache only | `pytest` | 77 passing tests in this audit | Strong coverage of implemented early slices |

No generic DecisionSignal, opportunity/asymmetry registry, scoring, monitoring, experiment, outcome, authorization, telemetry, or ATLAS code exists. Those are documentary concepts, not partially implemented services.

## 4. Learned operating-model requirements

Repeated empirical needs through 036 are:

1. preserve evidence provenance, freshness, effective timing, uncertainty class, and unsupported claims;
2. distinguish immutable observations from mutable interpretation and current state;
3. use hard discriminators—live decision, consequence, recoverability, exact resolution, actor access, effect observability, and controls—before discretionary ranking;
4. keep semantic exact-resolution comparison and research-policy selection judgment-led while they remain unstable;
5. preserve Markdown experiment contracts, explicit authorization, budgets, stop rules, and result/learning separation;
6. separate delivery, exposure, response, decision effect, value creation, and value capture;
7. log lightweight prospective resource telemetry without building infrastructure;
8. keep GitHub documents as durable learned state until retrieval or coordination pain repeats enough to justify software.

Only requirement 2 exposes a repeated, mechanical mismatch in currently implemented code. Most other requirements apply to the manual experimental loop, not to a production software path that currently exists.

## 5. KEEP inventory

| Capability | Why it still fits | Primary classification |
|---|---|---|
| Modular monolith, standard-library runtime, SQLite, and CLI | Low cost, reversible, inspectable, and proportionate to actual use | KEEP |
| Frozen source/domain input records | Discourages in-memory mutation of captured evidence | KEEP |
| Collector protocol and persistence-agnostic adapters | Source acquisition returns a generic observation and has no database knowledge | KEEP |
| Stable source and external identities | Necessary logical identity for deduplication and future revision grouping | KEEP |
| Per-source run records and batch transaction | Success/failure and rollback are explicit; one source failure does not corrupt another run | KEEP |
| Source terms, commercial-use caveats, selection biases, timestamps, URLs, and metadata | Provides useful source-level provenance and semantic guardrails | KEEP |
| CN75 measurement/relationship lineage and `not_supported` output | Demonstrates inspectable reasoning without converting derived value into market price or opportunity | KEEP |
| Deterministic tests with injected openers/clocks | Keeps network behavior bounded and source normalization reproducible | KEEP |
| Repository-centered spec/result/checkpoint separation | Later experiments show Markdown is the current economical operating substrate | KEEP |

## 6. ADAPT inventory

| Capability | Required adaptation | Why not discard it | Primary classification |
|---|---|---|---|
| Source registry mutation | `SignalSource` is upserted in place, so terms, caveats, and source metadata have current state but no historical run snapshot. Future collection should distinguish current registry metadata from the policy context used by a run. | The source registry and its caveat fields remain valuable; the boundary, not the primitive, is wrong. | ADAPT |
| Architecture/README/Roadmap status | Their large fixed pipeline, additive scoring, registry-first roadmap, and aggressive discovery automation are historical direction, not current code or current learned policy. Mark the status clearly rather than implementing the diagrams. | They retain useful early principles and historical context. | ADAPT |
| Repository query boundary | `reasoning.py` and tests reach through `Repository.connection` to raw SQL. If a second reasoner appears, add narrow evidence-query methods rather than an ORM or repository framework. | One direct reader does not yet justify a new abstraction. | ADAPT |

## 7. MISSING BUT EARNED inventory

| Capability | Repeated evidence | Small reversible shape | Primary classification |
|---|---|---|---|
| Append-only capture revisions for stable source items | Specs/checkpoints 019–036 repeatedly depend on freshness, effective dates, revisions, and reproducible evidence. Current adapters deliberately keep stable IDs while mutable fields include Stack Exchange activity/score/body, Azure prices/effective dates, search metrics, procurement state, and official statistical revisions. `ON CONFLICT(source_id, external_id) DO NOTHING` loses every later capture and associates the logical item only with its first run. | Add an append-only capture/revision table keyed by capture identity/content hash and run, retain stable `(source_id, external_id)` as logical identity, and define an explicit current-view query. Do not reconstruct missing history. | MISSING BUT EARNED |

No other missing software capability passes all four governing filters today.

## 8. MISSING BUT UNEARNED inventory

| Capability | Why it remains unearned | Primary classification |
|---|---|---|
| Generic opportunity/asymmetry registry | Recent candidates and decisions are heterogeneous and handled effectively in artifacts; no repeated software bottleneck | MISSING BUT UNEARNED |
| Generic hard-gate or scoring engine | Gates are learned, but application remains semantic and context-dependent | MISSING BUT UNEARNED |
| Exact-resolution search automation | Repeated need exists, but functional equivalence remains judgment-heavy | MISSING BUT UNEARNED |
| Experiment database/schema | Markdown preregistration is reconstructable and flexible; no retrieval/consistency failure justifies migration | MISSING BUT UNEARNED |
| Authorization, permission, or regulatory service | Consequential actions are manual and sparse; rules are not stable enough for code | MISSING BUT UNEARNED |
| Telemetry database/dashboard/CLI | Experiment 036 explicitly found prospective Markdown warranted and implementation unearned; code inspection reveals no zero-complexity exception | MISSING BUT UNEARNED |
| Research-policy scheduler or autonomous critic | Choosing the next discriminator and independent challenge remain epistemic work | MISSING BUT UNEARNED |
| Generic FORGE decision engine | Four decision-compression examples do not establish stable cross-domain mechanics | MISSING BUT UNEARNED |
| Interaction/exposure/effect tracker | 030 and 035 remain open and the state model is not yet validated by completed outcomes | MISSING BUT UNEARNED |
| Knowledge graph, vector store, or ATLAS service | Current repository artifacts remain reconstructable; fragmentation has not produced repeated measured cost | MISSING BUT UNEARNED |

## 9. OBSOLETE / CONTRADICTED inventory

| Item | Contradiction and risk | Primary classification |
|---|---|---|
| Additive commercial scoring as the main selector in `ARCHITECTURE.md` and `ROADMAP.md` | Later evidence establishes fatal gates that must not be compensated by attractive dimensions. There is no scoring code, so this is docs-only steering risk. | OBSOLETE / CONTRADICTED |
| Fixed sequence from bulk collection through detection/registry/scoring before experiment | Later work used behavior-first, signal-native, accessible-surface-first, and direct discriminators. Treating the early roadmap as required order would recreate research overhead. | OBSOLETE / CONTRADICTED |
| README instruction to “automate discovery aggressively” | The learned policy says automate stable mechanics, not unresolved research policy or candidate volume. | OBSOLETE / CONTRADICTED |

There is no generic detector or scoring implementation to retire. These obsolete assumptions are documentary; the separate changed-capture persistence gap is classified only as MISSING BUT EARNED.

## 10. Architecture scar-tissue map

| Observed problem | Evidence | Current code implication | Classification |
|---|---|---|---|
| Broad ignore hid non-duplicate constraint failures | Spec 002 and pipeline rollback test | Targeted uniqueness conflict and transaction are correct | KEEP |
| Same logical source item changes over time | Azure/Stack Exchange/DataForSEO adapter identities plus repeated freshness/revision needs in 019–036 | Later content is discarded under one uniqueness key | MISSING BUT EARNED |
| Derived unit value can be mistaken for price | Specs 009–012 and reasoning checkpoint | `not_supported` and test explicitly prevent that inference | KEEP |
| Source hierarchy can be mistaken for semantics | Specs 010–012 and Economic Reasoning Model | Relationships retain `source-native / structural` basis | KEEP |
| Adequate exact resolver kills attractive candidates | 020, 021, 031, and 032 | No mechanical exact-resolution code exists; keep semantic check manual | MISSING BUT UNEARNED |
| Correct resolution can lack reachable actor | 026–028 and 031–032 | Do not build generic detection/scoring that ignores access/effect gates | MISSING BUT UNEARNED |
| Delivery is not exposure or value | Frozen initialization evidence and 036 baseline | Do not create binary interaction-success state | MISSING BUT UNEARNED |
| Authorization differs from spec/capability/access | 026 and operating/control checkpoints | No external-action executor exists; procedural separation remains appropriate | KEEP |
| Telemetry is historically inconsistent | 036 | Preserve Markdown logging; do not build telemetry infrastructure | MISSING BUT UNEARNED |
| Conceptual architecture outpaced implemented behavior | Git history: implementation ends with Spec 012 while operating documents continue through 036 | Current audit must become the reality map; do not fill diagrams with speculative code | ADAPT |

## 11. Source/adapters assessment

Collectors are appropriately persistence-agnostic: each owns request construction, source-specific validation, normalization, clock, and failure semantics, then returns generic observations. Injected openers/clocks make tests deterministic. Source-specific fields stay in adapter metadata rather than becoming generic schema columns.

Identity is stable and usually source-native, but stable identity is incorrectly treated as capture identity. `observed_at` and optional `occurred_at` can represent capture and a single event/effective timestamp; they cannot express validity intervals, revision sequence, or multiple captures because persistence rejects them. Request/provenance detail is uneven: some observations have canonical URLs, some retain request URLs in metadata, and some have neither a canonical item URL nor a first-class retrieval reference. This is acceptable per source, provided revision capture is added before longitudinal reuse.

## 12. Evidence/provenance assessment

The strongest implemented primitives are source identity, observation timestamps, canonical URL, source metadata, normalized content, arbitrary metadata, and run association. CN75 reasoning adds explicit derivation strings and exact observation-ID lineage, and its tests protect unsupported-claim discipline.

The main gap is persistence of later evidence and derived interpretations. Derived measurements and arguments are rendered but not persisted or versioned. That is not yet a generic persistence requirement: only one domain reasoner exists, while later decision artifacts use transparent Markdown evidence classes successfully. A generic Evidence entity or provenance service would be premature. Append-only source captures are earned because they protect the evidence substrate regardless of future interpretation.

## 13. Persistence assessment

SQLite remains an appropriate choice. Run start/completion/failure is explicit; observation batch insertion is transactional; unrelated constraint failures roll back; and foreign keys are enabled. The model is inspectable and has no infrastructure burden.

Material limitations are:

- `UNIQUE(source_id, external_id)` plus `DO NOTHING` preserves first sighting but loses changed later captures;
- a logical item points only to the first successful `pipeline_run_id`, so later-run reproducibility is count-only;
- source metadata is overwritten without run-level policy history;
- schema creation is inline and unversioned, so an earned additive change needs an explicit compatibility/migration plan;
- failed collectors cannot preserve partial acquisition detail because collection returns a complete list or raises.

Only the first three belong in the next bounded persistence spec. A migration framework, ORM, event store, or partial-ingestion system is not earned.

## 14. Detection/opportunity assessment

`DETECT` does not exist as a generic code layer. `reasoning.py` is one fixed CN75 argument builder; it constructs measurements and relationships, checks a decomposition condition, enumerates alternatives, and explicitly says the result does not establish a commercial opportunity. The local `survives` variable means the parent anomaly survives one child decomposition, not that an opportunity survives RADAR.

Therefore the code does not currently conflate signal, friction, anomaly, demand, asymmetry, or opportunity. The risk is documentary: early diagrams imply a generic deterministic progression from signals to detected asymmetries. No replacement opportunity engine should be built.

## 15. Scoring assessment

There is no scoring implementation, configuration, score table, or operational caller. Additive scoring exists only in early architecture/roadmap examples. Later hard constraints—no live decision, consequence, recoverability, exact resolver, actor access, observable effect, or control permission—cannot safely be compensated by a high value elsewhere.

Scoring may eventually rank candidates *after* fatal gates, but no stable comparable population or repeated ranking bottleneck exists. Do not implement or delete scoring code; instead mark the old documentary role as superseded.

## 16. Exact-resolution assessment

Exact functional resolution checking is a replicated discriminator from Experiment 020 onward. The reusable part is procedural: describe actor, decision, inputs, output, timing, and residual gap, then retain source evidence and the kill/advance result. The decisive comparison remains semantic and domain-specific.

Markdown already captures it at lower cost than software. Search automation, embeddings, competitor databases, or a generic resolver comparator would encode unstable judgment. Keep it manual until repeated cases expose a truly mechanical substep.

## 17. Experiment-contract assessment

Specs now function as proportional preregistration with questions, methods, evidence, boundaries, budgets, stops, authorization, and verdicts. Git provides immutable history and separates intended method from result and checkpoint interpretation. This mechanism is operationally used and reconstructable.

No database schema is earned. A linter could eventually check mechanical requirements, but no repeated contract-QA failure or stable cross-spec schema is preserved. Keep contract authoring and epistemic review in Markdown; defer executable validation.

## 18. Authorization/control assessment

The software has no actor-contact or publication executor, so it cannot currently autonomously blur specification, authorization, capability, and access. Collection commands can make external API calls, and DataForSEO can incur paid requests when credentials exist, but invocation is manual and no repository evidence shows repeated unsafe execution.

Procedural authorization and control checks remain sufficient. A permission service, standing authority model, or regulatory rules engine is unearned. If source collection becomes routine again, the smallest future control should be command-specific preflight and recorded run context, not autonomous authorization.

## 19. Telemetry assessment

Current `pipeline_runs` record timestamps and item counts, but not active work, money, paid tool use, human attention, control escalation, uncertainty, verdict, or evidence yield. Adding those experiment concepts to an ingestion-run table would conflate units.

Experiment 036's Markdown standard remains the correct implementation. Code inspection found no near-zero-complexity mechanism that changes that conclusion. A timer helper or telemetry CLI would add another workflow before the fields have been used prospectively often enough to stabilize.

## 20. Research-policy assessment

The learned policy has changed repeatedly: asymmetry-first, behavior-first, signal-native, pre-consolidation, accessible-surface-first, then actor/effect-observability first. That evolution is evidence against encoding it now. Current code contains none of these policies, which is preferable to a stale automated selector.

Keep next-uncertainty selection, gate interpretation, and independent challenge manual. Deterministic substeps may later be extracted only after repeated stable use and measured benefit.

## 21. FORGE/decision-compression assessment

Experiments 025, 029, 033, and 034 repeatedly move from unstructured uncertainty to options, discriminators, testable questions, and decision-ready resolutions. The reusable artifact pattern is real, but the reasoning spans tariffs, CRM, and software architecture and remains highly semantic.

A lightweight document template may be useful, but a generic decision engine, option ontology, recommendation engine, or reusable solver is not earned. Existing Markdown preserves evidence classes and challenge records more transparently.

## 22. INTERACT/measurement assessment

There is no delivery/exposure/engagement/effect software. That absence is currently appropriate. The learned state model is valuable, but the two initialized interactions have not completed their observation windows within the evidence allowed here.

Do not implement binary response tracking, actor monitoring, notifications, profile inspection, or external-action automation. Completed outcomes must first show which states recur and which measurement burden is material.

## 23. ATLAS/durable-learning assessment

Git history, numbered specs, experiment artifacts, checkpoints, the frozen Opportunity Model, Operating Model, and Economic Telemetry Baseline let a fresh operator reconstruct the current policy. Knowledge is distributed, and the early top-level documents can mislead unless read beside later checkpoints, but this audit itself supplies a current code-to-model index.

No repeated measured retrieval failure supports a knowledge graph, vector store, learned-state database, or automatic indexer. Continue punctuated documentary consolidation.

## 24. Tests/developer-ergonomics assessment

Audit command: `.venv/bin/pytest -q`  
Result: **77 passed in 0.19 seconds**. Pytest emitted one environmental cache warning because the sandbox could not update `.pytest_cache`; no test failed and no tracked file changed.

Tests strongly cover bounded requests, source-native identities, timestamps, missing-value discipline, source caveats, network failures, duplicate behavior, transaction rollback, deterministic reasoning, lineage, and the derived-value/market-price boundary. Test doubles are simple and effective.

The important missing regression test is a second capture with the same stable external ID but changed content/metadata. Today it proves the wrong longitudinal behavior by being counted as a duplicate. That test belongs with the earned revision-capture implementation. Repository query ergonomics and CLI dispatch are repetitive but not painful enough to refactor.

## 25. Stale-assumption audit

| Assumption | Finding | Risk class |
|---|---|---|
| Additive opportunity scoring | Present in early docs; no code | DOCS-ONLY STALENESS |
| Generic asymmetry detection | Present as architecture/roadmap concept; no code | DOCS-ONLY STALENESS |
| Fixed opportunity taxonomy | Early DecisionSignal examples only; no implementation | DOCS-ONLY STALENESS |
| Friction implies demand | Explicit adapter/checkpoint caveats reject it | NOT PRESENT |
| Signal implies opportunity | CN75 output explicitly rejects commercial inference; early flow diagrams remain suggestive | DOCS-ONLY STALENESS |
| Source hierarchy is universal semantics | Reasoner labels relationships `source-native / structural`; Economic Reasoning Model warns against it | NOT PRESENT |
| Derived value is market price | Explicitly rejected and tested | NOT PRESENT |
| Generic survival threshold | CN75 `>50%` condition is a bounded decomposition diagnostic, not opportunity selection | HISTORICAL BUT HARMLESS |
| Automation before validation | README/Roadmap language is broader than later policy; no automation code exists | DOCS-ONLY STALENESS |
| External action without separate authorization | No external-action executor exists; manual collection commands are capability only | NOT PRESENT |
| Mutable evidence | Existing rows are not mutated, but later changed captures are discarded | CODE RISK |
| Current-state records without provenance/history | Source metadata overwrites and logical items retain only first-run capture | CODE RISK |

## 26. Ranked implementation candidates, maximum five

### 1. Revision-aware observation persistence — SPEC NEXT

- **Problem:** stable logical identity and immutable capture identity are conflated, so changed recaptures disappear.
- **Observed evidence:** mutable fields exist across several implemented adapters; freshness, effective dates, revisions, and reproducibility recur throughout later experiments and checkpoints.
- **Smallest useful change:** additive capture/revision storage associated with every run, a content hash or equivalent capture identity, and an explicit current-view query while retaining stable source/external identity.
- **Deliberately does not solve:** generic evidence ontology, interpretation versioning, monitoring, scheduling, scoring, experiment tracking, or actor measurement.
- **Expected benefit:** prevents evidence loss and makes later comparisons/reasoning reproducible if collection code is reused.
- **Main risk:** ambiguous migration/current-view semantics could create duplicate inflation or break existing first-seen behavior.
- **030/035 dependency:** none.
- **Implementation verdict:** **SPEC NEXT**; write a bounded persistence contract and tests before code.

### 2. Exact-resolution comparison support — KEEP MANUAL

- **Problem:** exact functional competition checks recur.
- **Observed evidence:** repeated kills and narrowing from 020 onward.
- **Smallest useful change:** continue the actor/decision/input/output/timing/residual-gap Markdown record.
- **Deliberately does not solve:** semantic equivalence automatically.
- **Expected benefit:** auditability without false automation.
- **Main risk:** template ceremony.
- **030/035 dependency:** none.
- **Implementation verdict:** **KEEP MANUAL**.

### 3. Mechanical experiment-contract QA — DEFER

- **Problem:** required sections and controls are checked manually.
- **Observed evidence:** contracts recur, but no repeated execution-QA failure is recorded.
- **Smallest useful change:** eventually lint only stable required headings and protected paths.
- **Deliberately does not solve:** epistemic validity or authorization.
- **Expected benefit:** lower clerical error if throughput rises.
- **Main risk:** freezing a still-variable schema and confusing conformance with validity.
- **030/035 dependency:** completed interaction learning could change required fields.
- **Implementation verdict:** **DEFER**.

### 4. Operational telemetry helper — DEFER

- **Problem:** telemetry was historically inconsistent.
- **Observed evidence:** Experiment 036 established a prospective Markdown standard but explicitly found software unearned.
- **Smallest useful change:** none now; use the block manually.
- **Deliberately does not solve:** efficiency scoring, dashboards, or outcome valuation.
- **Expected benefit:** prospective comparability at zero implementation cost.
- **Main risk:** tooling before schema stability.
- **030/035 dependency:** none for logging, but interaction outcomes may refine fields.
- **Implementation verdict:** **DEFER**.

## 27. What must explicitly NOT be built now

Do not build an orchestration engine, autonomous scheduler, multi-agent critic system, regulatory database, generic policy engine, permission service, experiment database, opportunity scoring engine, governance UI, telemetry dashboard, knowledge graph, vector-store ATLAS, automated Codex launcher, autonomous outreach, generic decision engine, generic ontology/graph layer, monitoring platform, or interaction-response tracker.

Also do not implement the aspirational folders/tables/commands in the early architecture merely to make documentation appear complete. No current evidence warrants microservices, an ORM, a migration framework by itself, event streaming, a web UI, or production scheduling.

## 28. Architecture changes dependent on 030/035

Any software for exposure verification, response classification, decision-state change, attribution, observation deadlines, notification, follow-up eligibility, or interaction outcome aggregation depends on completed and independently interpreted 030/035 evidence. Their initialization proves bounded publication and delivery only.

No such change should be specified or built from this audit. Revision-aware source persistence is independent of those outcomes.

## 29. Overall code-health conclusion

The current code is small, coherent, deterministic, and fully passing. Its implemented boundaries are clearer and safer than the top-level conceptual diagrams suggest. There is little dead code because most aspirational architecture was never built. The CN75 reasoner is intentionally specific and demonstrates good lineage and inference discipline rather than a failed generic engine.

The material health risk is silent loss of longitudinal source evidence. This is bounded and repairable through an additive design, not a platform rewrite. Documentary staleness is the larger navigation risk: operators must distinguish early architectural aspiration from the repository-centered manual Engine learned through 036.

## 30. Exactly one recommended next action

Write a bounded implementation specification for append-only observation captures that preserves stable logical identity, associates every capture with its pipeline run, defines current-view semantics, and adds changed-recapture regression tests without introducing an ORM, migration framework, monitoring, scoring, or new domain layers.
