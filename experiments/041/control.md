## ARM

CONTROL — one agent, sequential execution: Package A → Package B → reconciliation. No delegation, external research, live data, or architecture recommendations. No Experiment 041 treatment artifact was inspected.

## BASELINE

- Required and observed commit: `6360064ea874e7350de2121e9cc569b9045fd1e0`.
- Canonical repository content remained read-only.
- Initial and final status showed pre-existing untracked `experiments/041/`; it was not modified.
- `git diff --check` passed.
- Git emitted sandbox warnings because it could not create macOS toolchain cache files under `/tmp`; baseline resolution and read-only checks still completed.

## START/END TELEMETRY

| Interval | UTC start | UTC end | Elapsed |
|---|---:|---:|---:|
| Overall control run | 2026-09-04T12:00:02Z | 2026-09-04T12:01:35Z | 93 s |
| Package A | 2026-09-04T12:00:02Z | 2026-09-04T12:00:36Z | 34 s |
| Package B | 2026-09-04T12:00:47Z | 2026-09-04T12:01:13Z | 26 s |
| Reconciliation | 2026-09-04T12:01:28Z | 2026-09-04T12:01:35Z | 7 s |
| Unassigned transition/telemetry overhead | — | — | 26 s |

- Agent runs: 1.
- Retrieval retries: 2 targeted continuations after broad command output truncation.
- Test execution retries: 0; one attempted `pytest` invocation could not start because `pytest` was absent from `PATH`.
- Clarifications/interventions/escalations: 0.
- Context restarts: 0.
- Live external interactions: 0.
- External spend: €0, per preregistered boundary.
- Output bytes/tokens: UNKNOWN—not exposed before freeze.
- Compute/model cost: UNKNOWN—not exposed.

## PACKAGE A SUMMARY

1. **Implemented modules and entry points.** The software is one Python package containing models, SQLite persistence, a single-collector pipeline, CLI, one domain-specific reasoner, and eight source-adapter modules. The installed command is `asymmetry-engine = asymmetry_engine.cli:main`; CLI commands cover Stack Exchange, CFPB, DataForSEO keyword demand, TED, Eurostat, Azure prices, generic Comext, CN75 Comext, OpenAlex, and CN75 reasoning ([pyproject.toml:15](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/pyproject.toml:15), [cli.py:19](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/cli.py:19)).

2. **Source-adapter boundary.** A collector exposes a `SignalSource` and returns normalized `SourceObservation` values. Adapters own source-specific access, validation, identity, normalization, metadata, and caveats; the pipeline and repository own run lifecycle and generic persistence ([pipeline.py:12](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/pipeline.py:12), [models.py:18](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/models.py:18), [ARCHITECTURE.md:54](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/ARCHITECTURE.md:54)).

3. **SQLite schema and transaction boundary.** Current storage has exactly `signal_sources`, `pipeline_runs`, and `source_observations`. The last uses `(source_id, external_id, capture_sequence)` uniqueness and foreign keys to source and run records ([db.py:11](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:11), [db.py:35](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:35)). Run creation is committed before collection. Successful completion inserts the entire observation batch and updates its run within one connection transaction; constraint failure rolls that batch back, after which failure status is recorded separately ([db.py:142](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:142), [db.py:150](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:150), [pipeline.py:28](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/pipeline.py:28)). Legacy schema conversion has its own explicit `BEGIN IMMEDIATE`/commit/rollback boundary ([db.py:91](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:91)).

4. **Revision semantics.** Logical identity is `(source_id, external_id)`. Equality against the latest capture covers `occurred_at`, item kind, content, canonical URL, and canonicalized metadata. A materially equal recapture is a duplicate; a change appends the next sequence. `observed_at` and run identity alone do not create a revision. A reversion therefore persists A→B→A rather than collapsing against all history ([db.py:162](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:162), [test_pipeline.py:94](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_pipeline.py:94), [test_pipeline.py:120](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_pipeline.py:120), [test_pipeline.py:134](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_pipeline.py:134)).

5. **Current/latest reads.** `latest_observations()` groups by logical identity, joins the maximum sequence, permits optional source filtering, and orders deterministically by source and external ID ([db.py:216](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/db.py:216)). Tests specify one latest capture per item and confirm that revised evidence, rather than historical evidence, drives reasoning ([test_pipeline.py:186](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_pipeline.py:186), [test_reasoning.py:153](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_reasoning.py:153)).

6. **Implemented reasoning.** `build_cn75_argument()` is restricted to Czech Comext CN75/CN8 evidence for 2023–2024 and selected partners. It calculates value/mass growth, derived value-per-mass change, child and partner contributions, and supplier HHI; it retains exact observation lineage and separates supported interpretation, unsupported claims, alternative explanations, and next evidence ([reasoning.py:111](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/reasoning.py:111), [reasoning.py:128](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/reasoning.py:128), [reasoning.py:202](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/reasoning.py:202)). It explicitly does not establish a commercial opportunity ([reasoning.py:237](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/src/asymmetry_engine/reasoning.py:237)).

7. **Protected invariants.** Inspected tests cover bounded official requests, stable source-native identities, timestamps, missing-value preservation, metadata caveats, network/API failure, deduplication, atomic batch rollback, all material revision fields, A→B→A transitions, mixed-run accounting, deterministic latest reads, safe/idempotent legacy migration, migration rollback, deterministic reasoning, exact lineage, missing evidence, and unsupported inference. Representative protections appear at [test_pipeline.py:45](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_pipeline.py:45), [test_pipeline.py:71](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_pipeline.py:71), [test_pipeline.py:280](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_pipeline.py:280), and [test_reasoning.py:80](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/tests/test_reasoning.py:80).

8. **Explicitly absent capabilities.** There is no generic opportunity detector/scorer, multi-source scheduler, monitoring/orchestration service, generic decision engine, actor interaction/effect measurement, permission system, experiment/portfolio database, UI, web service, provenance graph, event store, or temporal database ([ARCHITECTURE.md:112](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/ARCHITECTURE.md:112), [ARCHITECTURE.md:123](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/ARCHITECTURE.md:123), [ARCHITECTURE.md:227](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/ARCHITECTURE.md:227)).

9. **Architecture cross-check.** No material discrepancy was found between current code/tests and `ARCHITECTURE.md`. Its file inventory, adapter boundary, schema, transaction description, revision/latest semantics, CN75 scope, and explicit absences match implementation truth.

Package A confidence: high for static implementation semantics; medium-high overall because the suite could not be executed in this environment.

## PACKAGE B SUMMARY

1. **Operating loop.** Current empirical practice is `OBSERVE → RADAR → DISCRIMINATE → FORGE → INTERACT → MEASURE → LEARN`. It is manual, may branch, revisit questions, skip stages, or terminate on a failed necessary condition; it is not a runtime pipeline ([README.md:33](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/README.md:33), [README.md:52](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/README.md:52)).

2. **Opportunity discrimination.** Current policy is fatal-gate-first rather than additive scoring. It tests an identifiable still-changeable actor decision, economic consequence, meaningful uncertainty, recoverability, inadequate exact resolution, feasible resolution, legitimate access, observable effect, and acceptable controls. A failed necessary condition can dominate attractive heuristics ([ROADMAP.md:64](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/ROADMAP.md:64), [OPPORTUNITY_MODEL_001_035.md:315](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/docs/OPPORTUNITY_MODEL_001_035.md:315)). Research ordering follows the cheapest observation capable of changing the decision, not a numeric scheduler ([OPPORTUNITY_MODEL_001_035.md:357](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/docs/OPPORTUNITY_MODEL_001_035.md:357)).

3. **Exact resolution.** Functional comparison uses `ACTOR × DECISION × INPUTS × RESOLUTION × OUTPUT × TIMING`. Its role is to reject cases where information is difficult to find but the actor’s exact job is already adequately solved. It is a replicated manual principle, not a resolver service ([OPPORTUNITY_MODEL_001_035.md:149](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/docs/OPPORTUNITY_MODEL_001_035.md:149)).

4. **FORGE and decision compression.** FORGE has repeatedly transformed unstructured uncertainty into structured uncertainty, options, dominant discriminators, a testable next question, and a decision-ready disposable resolution. This is the strongest candidate for reusable FORGE capability, but actor value remains unproven and the practice is not implemented as a generic engine ([OPPORTUNITY_MODEL_001_035.md:440](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/docs/OPPORTUNITY_MODEL_001_035.md:440), [README.md:69](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/README.md:69)).

5. **Interaction, exposure, and effect.** The evidence chain must preserve: delivery ≠ actor exposure ≠ engagement/comprehension ≠ decision effect ≠ value creation ≠ value capture ≠ repeatability. Surface access, actor access, intervention permission, and exposure are also distinct ([OPPORTUNITY_MODEL_001_035.md:183](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/docs/OPPORTUNITY_MODEL_001_035.md:183), [OPPORTUNITY_MODEL_001_035.md:489](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/docs/OPPORTUNITY_MODEL_001_035.md:489), [ROADMAP.md:129](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/ROADMAP.md:129)). Persisted initialization establishes delivery for Experiments 030/035; exposure, comprehension/engagement, effect, and value remain UNKNOWN rather than negative ([ECONOMIC_TELEMETRY_BASELINE_001_035.md:65](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md:65), [ECONOMIC_TELEMETRY_BASELINE_001_035.md:163](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md:163)).

6. **Governance boundary.** `SPECIFICATION ≠ AUTHORIZATION ≠ CAPABILITY ≠ ACCESS`. A specification states intended work but never grants permission; external publication/contact, excess spending, commitments, payment, sensitive data use, and other consequential actions require explicit authority. Controls are proportional, human-governed, and retain `UNKNOWN` rather than silently converting it to `PASS` ([README.md:129](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/README.md:129), [OPERATING_MODEL.md:314](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/docs/OPERATING_MODEL.md:314), [OPERATING_MODEL.md:345](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/docs/OPERATING_MODEL.md:345)).

7. **Prospective telemetry.** Future experiment records should preserve actual/estimated active time, spend, human attention, control escalations, meaningful inputs/flow, bounded interaction counts, validity/verdict, before/after uncertainty, evidence yield, and policy change. Missing values remain `UNKNOWN`; phases and heterogeneous outputs must not share invented denominators ([ECONOMIC_TELEMETRY_BASELINE_001_035.md:166](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md:166), [ECONOMIC_TELEMETRY_BASELINE_001_035.md:186](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md:186)).

8. **Evidence-earned automation.** Automation requires repeated observed pain, mechanical reuse, likely improvement in experiment economics, and a small reversible implementation. It should multiply validated mechanisms, not compensate for weak opportunities or unresolved assumptions ([ROADMAP.md:36](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/ROADMAP.md:36), [OPERATING_MODEL.md:617](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/docs/OPERATING_MODEL.md:617), [README.md:151](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/README.md:151)).

9. **Supported boundary.** Supported: useful rejection policy; replicated fatal discriminators; exact-resolution checking; bounded decision compression and disposable resolutions; controlled publication/delivery; qualitative bottleneck migration; repeated near-zero incremental external spend; revision-aware source persistence. Unproven: repeatable actor decision effect, value creation/capture, willingness to pay, revenue, transactions, repeatability, quantitative efficiency improvement, scalable economics, economic compounding, and autonomous operation ([README.md:155](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/README.md:155), [ECONOMIC_TELEMETRY_BASELINE_001_035.md:102](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md:102)).

10. **Document consistency.** README and ROADMAP materially agree with the operating and checkpoint artifacts. Experiment 039 explicitly records that prior fixed-pipeline, additive-scoring, aggressive-automation, and premature commercial language was superseded, and reports no material contradiction after alignment ([documentation-truth-alignment.md:35](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/experiments/039/documentation-truth-alignment.md:35), [documentation-truth-alignment.md:82](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/experiments/039/documentation-truth-alignment.md:82)).

Package B confidence: high within the persisted evidence boundary.

## CROSS-BOUNDARY RECONCILIATION

- **What exists in software:** bounded source acquisition/normalization, source/run/revision-aware observation persistence, deterministic latest reads, and one CN75 reasoner.
- **What exists as manual/documentary practice:** RADAR, discrimination, exact-resolution comparison, FORGE, interaction design, effect measurement, authorization/control, telemetry, independent challenge, and learning consolidation.
- **What is empirically learned but not implemented:** fatal-gate opportunity policy; actor/effect-first topology; decision compression; separation of delivery/exposure/engagement/effect/value/capture/repeatability; evidence-earned automation.
- **What remains unproven:** actor effect and commercial/repeatability economics.
- The implementation does not contradict the operating model: it supplies bounded evidence primitives, while Git-hosted specifications, results, checkpoints, and human governance carry the broader loop. The lower operating loop is explicitly documentary/procedural rather than software ([ARCHITECTURE.md:167](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/ARCHITECTURE.md:167)).
- Pipeline-run timestamps/counts are ingestion telemetry and must not be interpreted as experiment economics ([ARCHITECTURE.md:221](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/ARCHITECTURE.md:221)).
- The CN75 reasoner’s “survives decomposition” condition is a domain calculation, not an opportunity-survival score or RADAR implementation.

## MATERIAL RECONSTRUCTION AMBIGUITIES

- `README.md` names `DISCRIMINATE` as a loop stage, while some older normative operating-model diagrams express the same work through research policy, lifecycle gates, and independent challenge without that explicit stage name. The behavior aligns, but the vocabulary is not perfectly normalized.
- The four-part `SPECIFICATION ≠ AUTHORIZATION ≠ CAPABILITY ≠ ACCESS` formulation is clearest in current top-level documents; the older operating model often uses the three objects specification/execution/authorization and discusses capability/access elsewhere.
- Interaction vocabulary varies slightly between “response,” “engagement,” “comprehension,” and “effect.” These must be treated as separate evidence levels or explicitly defined per experiment, not silently merged.
- `OPPORTUNITY_MODEL_001_035.md` is intentionally frozen through Experiment 035 and right-censored at interaction initialization. It is evidence history and a provisional model, not evidence of current live outcomes.
- Source registry rows are mutable current metadata; historical source-policy snapshots are absent. Observation revision history therefore must not be mistaken for complete historical policy provenance ([ARCHITECTURE.md:77](/Users/romanchristov/Documents/GitHub/-asymmetry-engine/ARCHITECTURE.md:77)).
- Tests were statically reconstructable but not executable because the available shell lacked `pytest`; runtime confirmation at this exact baseline is consequently UNKNOWN in this assessment.

## WHAT A NEW OPERATOR MUST NOT INFER

- The conceptual Engine, its named loops, or the long-term ATLAS/RADAR/FORGE/PORTFOLIO/FREEDOM direction are implemented services.
- A public signal, friction, novelty, dispersion, candidate count, or difficult-to-find fact is itself an opportunity.
- Fatal opportunity constraints can compensate for one another through an additive score.
- A bounded collector proves unrestricted permission to ingest, retain, reuse, contact, or commercialize source data.
- A specification, executable capability, accessible surface, or public visibility supplies authorization.
- Delivery proves exposure; exposure proves engagement or comprehension; engagement proves decision effect; effect proves value; value proves capture; or one capture proves repeatability.
- UNKNOWN exposure or effect means zero response, failure, or negative value evidence.
- The CN75 reasoner is a generic detector, market-price model, demand model, or commercial opportunity scorer.
- Revision-aware captures form a generic event store, temporal database, complete provenance graph, or historical source-policy registry.
- Ingestion run counts/timestamps establish economic efficiency.
- Zero recorded external spend means total compute, human-attention, or operational cost was zero.
- Documentation of potential automation authorizes or demonstrates autonomous operation.
- Persisted Experiment 030/035 initialization evidence reveals their current live state.

## CONFIDENCE / LIMITATIONS

Overall confidence is **high on repository-stated boundaries and static implementation semantics**, and **medium-high on executable implementation health**.

Limitations:

- No live external evidence was consulted.
- Experiment 030/035 current state remains deliberately UNKNOWN.
- Experiment 041 treatment artifacts were not inspected.
- The test suite could not be run because `pytest` was unavailable in `PATH`.
- Broad retrieval output was truncated twice; both cases were resolved through bounded, targeted reads.
- This is one static reconstruction at the stated baseline, not proof that an unaided operator would make every required semantic distinction.
- Compute/model cost and final output size were not exposed.

## FINAL VERDICT

**ADEQUATE WITH BOUNDED AMBIGUITIES**

A technically literate new operator can reconstruct the implemented software truth and the empirical operating/governance truth from the repository alone. The primary boundaries—software versus manual practice, learned policy versus automation, delivery versus downstream effects, and specification versus authorization—are explicit and materially consistent.

The remaining ambiguities are bounded: minor vocabulary drift across document generations, intentionally frozen/right-censored empirical artifacts, incomplete historical source-policy provenance, and the inability to execute the test suite in this environment. None prevents a defensible reconstruction, but together they preclude a `STRONG` verdict.