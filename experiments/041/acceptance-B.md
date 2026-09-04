# Acceptance Packet B

## Package A — Implemented Software Truth

1. The software is a Python package containing models, SQLite persistence, a single-collector pipeline, CLI, one domain-specific reasoner, and eight source adapters. The installed command is `asymmetry-engine = asymmetry_engine.cli:main`; commands cover Stack Exchange, CFPB, DataForSEO keyword demand, TED, Eurostat, Azure prices, generic Comext, CN75 Comext, OpenAlex, and CN75 reasoning ([pyproject.toml:15](../../pyproject.toml:15), [cli.py:19](../../src/asymmetry_engine/cli.py:19)).

2. A collector exposes `SignalSource` and returns normalized `SourceObservation` values. Adapters own source-specific access, validation, identity, normalization, metadata, and caveats; the pipeline and repository own run lifecycle and generic persistence ([pipeline.py:12](../../src/asymmetry_engine/pipeline.py:12), [models.py:18](../../src/asymmetry_engine/models.py:18), [ARCHITECTURE.md:54](../../ARCHITECTURE.md:54)).

3. Storage has exactly `signal_sources`, `pipeline_runs`, and `source_observations`. Observation uniqueness is `(source_id, external_id, capture_sequence)`, with foreign keys to source and run records ([db.py:11](../../src/asymmetry_engine/db.py:11), [db.py:35](../../src/asymmetry_engine/db.py:35)). Run creation commits before collection. Successful completion inserts the full observation batch and updates its run in one transaction. Constraint failure rolls back that batch; failure status is then recorded separately ([db.py:142](../../src/asymmetry_engine/db.py:142), [db.py:150](../../src/asymmetry_engine/db.py:150), [pipeline.py:28](../../src/asymmetry_engine/pipeline.py:28)). Legacy conversion has explicit `BEGIN IMMEDIATE`, commit, and rollback boundaries ([db.py:91](../../src/asymmetry_engine/db.py:91)).

4. Logical identity is `(source_id, external_id)`. Comparison with the latest capture includes `occurred_at`, item kind, content, canonical URL, and canonicalized metadata. Material equality produces a duplicate; change appends the next sequence. `observed_at` and run identity alone do not create a revision. Reversion persists A→B→A ([db.py:162](../../src/asymmetry_engine/db.py:162), [test_pipeline.py:94](../../tests/test_pipeline.py:94), [test_pipeline.py:120](../../tests/test_pipeline.py:120), [test_pipeline.py:134](../../tests/test_pipeline.py:134)).

5. `latest_observations()` groups by logical identity, joins the maximum sequence, permits optional source filtering, and orders deterministically by source and external ID ([db.py:216](../../src/asymmetry_engine/db.py:216)). Tests specify one latest capture per item and confirm that revised, rather than historical, evidence drives reasoning ([test_pipeline.py:186](../../tests/test_pipeline.py:186), [test_reasoning.py:153](../../tests/test_reasoning.py:153)).

6. `build_cn75_argument()` is restricted to Czech Comext CN75/CN8 evidence for 2023–2024 and selected partners. It calculates value and mass growth, derived value-per-mass change, child and partner contributions, and supplier HHI. It retains exact observation lineage and separates supported interpretation, unsupported claims, alternative explanations, and next evidence ([reasoning.py:111](../../src/asymmetry_engine/reasoning.py:111), [reasoning.py:128](../../src/asymmetry_engine/reasoning.py:128), [reasoning.py:202](../../src/asymmetry_engine/reasoning.py:202)). It does not establish a commercial opportunity ([reasoning.py:237](../../src/asymmetry_engine/reasoning.py:237)).

7. Inspected tests cover bounded official requests, stable source-native identities, timestamps, missing-value preservation, metadata caveats, network/API failure, deduplication, atomic batch rollback, all material revision fields, A→B→A transitions, mixed-run accounting, deterministic latest reads, safe and idempotent legacy migration, migration rollback, deterministic reasoning, exact lineage, missing evidence, and unsupported inference ([test_pipeline.py:45](../../tests/test_pipeline.py:45), [test_pipeline.py:71](../../tests/test_pipeline.py:71), [test_pipeline.py:280](../../tests/test_pipeline.py:280), [test_reasoning.py:80](../../tests/test_reasoning.py:80)).

8. Absent capabilities are: a generic opportunity detector or scorer, multi-source scheduler, monitoring or orchestration service, generic decision engine, actor interaction or effect measurement, permission system, experiment or portfolio database, UI, web service, provenance graph, event store, and temporal database ([ARCHITECTURE.md:112](../../ARCHITECTURE.md:112), [ARCHITECTURE.md:123](../../ARCHITECTURE.md:123), [ARCHITECTURE.md:227](../../ARCHITECTURE.md:227)).

9. No material discrepancy was found between current code/tests and `ARCHITECTURE.md`. Its inventory, adapter boundary, schema, transaction description, revision/latest semantics, CN75 scope, and explicit absences match implementation truth.

Package A confidence is high for static implementation semantics and medium-high overall because the suite could not be executed in this environment.

## Package B — Empirical Operating and Governance Truth

1. Current empirical practice is `OBSERVE → RADAR → DISCRIMINATE → FORGE → INTERACT → MEASURE → LEARN`. It is manual, may branch, revisit questions, skip stages, or terminate when a necessary condition fails; it is not a runtime pipeline ([README.md:33](../../README.md:33), [README.md:52](../../README.md:52)).

2. Opportunity discrimination is fatal-gate-first, not additive scoring. It tests an identifiable still-changeable actor decision, economic consequence, meaningful uncertainty, recoverability, inadequate exact resolution, feasible resolution, legitimate access, observable effect, and acceptable safeguards. One failed necessary condition can outweigh attractive heuristics ([ROADMAP.md:64](../../ROADMAP.md:64), [OPPORTUNITY_MODEL_001_035.md:315](../../docs/OPPORTUNITY_MODEL_001_035.md:315)). Research ordering follows the cheapest observation capable of changing the decision, not a numeric scheduler ([OPPORTUNITY_MODEL_001_035.md:357](../../docs/OPPORTUNITY_MODEL_001_035.md:357)).

3. Functional comparison uses `ACTOR × DECISION × INPUTS × RESOLUTION × OUTPUT × TIMING`. It rejects cases where information is difficult to find but the actor’s exact job is already adequately solved. This is a replicated manual principle, not a resolver service ([OPPORTUNITY_MODEL_001_035.md:149](../../docs/OPPORTUNITY_MODEL_001_035.md:149)).

4. FORGE has repeatedly converted unstructured uncertainty into structured uncertainty, options, dominant discriminators, a testable next question, and a decision-ready disposable resolution. This is the strongest candidate for reusable FORGE capability, but actor value remains unproven and the practice is not implemented as a generic engine ([OPPORTUNITY_MODEL_001_035.md:440](../../docs/OPPORTUNITY_MODEL_001_035.md:440), [README.md:69](../../README.md:69)).

5. The evidence chain must preserve: delivery ≠ actor exposure ≠ engagement/comprehension ≠ decision effect ≠ value creation ≠ value capture ≠ repeatability. Surface access, actor access, intervention permission, and exposure are distinct ([OPPORTUNITY_MODEL_001_035.md:183](../../docs/OPPORTUNITY_MODEL_001_035.md:183), [OPPORTUNITY_MODEL_001_035.md:489](../../docs/OPPORTUNITY_MODEL_001_035.md:489), [ROADMAP.md:129](../../ROADMAP.md:129)). Persisted initialization establishes delivery for Experiments 030/035; exposure, comprehension/engagement, effect, and value remain `UNKNOWN`, not negative ([ECONOMIC_TELEMETRY_BASELINE_001_035.md:65](../../docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md:65), [ECONOMIC_TELEMETRY_BASELINE_001_035.md:163](../../docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md:163)).

6. `SPECIFICATION ≠ AUTHORIZATION ≠ CAPABILITY ≠ ACCESS`. A specification states intended work but never grants permission. External publication or contact, excess spending, commitments, payment, sensitive-data use, and other consequential actions require explicit authority. Safeguards are proportional, human-governed, and retain `UNKNOWN` instead of silently converting it to `PASS` ([README.md:129](../../README.md:129), [OPERATING_MODEL.md:314](../../docs/OPERATING_MODEL.md:314), [OPERATING_MODEL.md:345](../../docs/OPERATING_MODEL.md:345)).

7. Future experiment records should preserve actual or estimated active time, spend, human attention, safeguard escalations, meaningful inputs and flow, bounded interaction counts, validity and verdict, before/after uncertainty, evidence yield, and policy change. Missing values remain `UNKNOWN`; phases and heterogeneous outputs must not share invented denominators ([ECONOMIC_TELEMETRY_BASELINE_001_035.md:166](../../docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md:166), [ECONOMIC_TELEMETRY_BASELINE_001_035.md:186](../../docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md:186)).

8. Automation requires repeated observed pain, mechanical reuse, likely improvement in experiment economics, and a small reversible implementation. It should multiply validated mechanisms, not compensate for weak opportunities or unresolved assumptions ([ROADMAP.md:36](../../ROADMAP.md:36), [OPERATING_MODEL.md:617](../../docs/OPERATING_MODEL.md:617), [README.md:151](../../README.md:151)).

9. Supported findings are useful rejection policy; replicated fatal discriminators; exact-resolution checking; bounded decision compression and disposable resolutions; governed publication and delivery; qualitative bottleneck migration; repeated near-zero incremental external spend; and revision-aware source persistence. Unproven findings are repeatable actor decision effect, value creation or capture, willingness to pay, revenue, transactions, repeatability, quantitative efficiency improvement, scalable economics, economic compounding, and autonomous operation ([README.md:155](../../README.md:155), [ECONOMIC_TELEMETRY_BASELINE_001_035.md:102](../../docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md:102)).

10. README and ROADMAP materially agree with the operating and checkpoint artifacts. Experiment 039 records that earlier fixed-pipeline, additive-scoring, aggressive-automation, and premature commercial language was superseded, with no material contradiction reported after alignment ([documentation-truth-alignment.md:35](../../experiments/039/documentation-truth-alignment.md:35), [documentation-truth-alignment.md:82](../../experiments/039/documentation-truth-alignment.md:82)).

Package B confidence is high within the persisted evidence boundary.

## Cross-Boundary Reconciliation

- Software provides bounded source acquisition and normalization, source/run/revision-aware observation persistence, deterministic latest reads, and one CN75 reasoner.
- Manual and documentary practice provides RADAR, discrimination, exact-resolution comparison, FORGE, interaction design, effect measurement, authorization and safeguards, measurement records, independent challenge, and learning consolidation.
- Empirically learned but unimplemented findings include fatal-gate opportunity policy, actor/effect-first structure, decision compression, separation of delivery/exposure/engagement/effect/value/capture/repeatability, and evidence-earned automation.
- Actor effect and commercial or repeatability economics remain unproven.
- The implementation does not contradict the operating model: it supplies bounded evidence primitives, while Git-hosted specifications, results, checkpoints, and human governance carry the broader loop. The lower operating loop is documentary and procedural, not software ([ARCHITECTURE.md:167](../../ARCHITECTURE.md:167)).
- Pipeline-run timestamps and counts concern ingestion and must not be interpreted as experiment economics ([ARCHITECTURE.md:221](../../ARCHITECTURE.md:221)).
- The CN75 reasoner’s “survives decomposition” condition is a domain calculation, not an opportunity-survival score or RADAR implementation.

## Material Reconstruction Ambiguities

- `README.md` names `DISCRIMINATE` as a loop stage, while some older normative operating-model diagrams express the same work through research policy, lifecycle gates, and independent challenge without that explicit name. Behavior aligns, but vocabulary is not fully normalized.
- The four-part `SPECIFICATION ≠ AUTHORIZATION ≠ CAPABILITY ≠ ACCESS` formulation is clearest in current top-level documents. The older operating model often uses specification/execution/authorization and discusses capability and access elsewhere.
- Interaction vocabulary varies among “response,” “engagement,” “comprehension,” and “effect.” These must remain separate evidence levels or be explicitly defined per experiment.
- `OPPORTUNITY_MODEL_001_035.md` is intentionally frozen through Experiment 035 and right-censored at interaction initialization. It is evidence history and a provisional model, not evidence of current live outcomes.
- Source-registry rows are mutable current metadata; historical source-policy snapshots are absent. Observation revision history is not complete historical policy provenance ([ARCHITECTURE.md:77](../../ARCHITECTURE.md:77)).
- Tests were statically reconstructable but not executable because the available shell lacked `pytest`; runtime confirmation at the stated baseline is therefore `UNKNOWN`.

## What a New Operator Must Not Infer

- The conceptual Engine, its named loops, or the long-term ATLAS/RADAR/FORGE/PORTFOLIO/FREEDOM direction are implemented services.
- A public signal, friction, novelty, dispersion, candidate count, or difficult-to-find fact is itself an opportunity.
- Fatal opportunity constraints can compensate for one another through an additive score.
- A bounded collector proves unrestricted permission to ingest, retain, reuse, contact, or commercialize source data.
- A specification, executable capability, accessible surface, or public visibility supplies authorization.
- Delivery proves exposure; exposure proves engagement or comprehension; engagement proves decision effect; effect proves value; value proves capture; or one capture proves repeatability.
- `UNKNOWN` exposure or effect means zero response, failure, or negative-value evidence.
- The CN75 reasoner is a generic detector, market-price model, demand model, or commercial-opportunity scorer.
- Revision-aware captures form a generic event store, temporal database, complete provenance graph, or historical source-policy registry.
- Ingestion-run counts or timestamps establish economic efficiency.
- Zero recorded external spend means total compute, human-attention, or operational cost was zero.
- Documentation of potential automation authorizes or demonstrates autonomous operation.
- Persisted Experiment 030/035 initialization evidence reveals their current live state.

## Confidence and Limitations

Overall confidence is **high on repository-stated boundaries and static implementation semantics**, and **medium-high on executable implementation health**.

- No live external evidence was consulted.
- Experiment 030/035 current state remains deliberately `UNKNOWN`.
- The test suite could not run because `pytest` was unavailable in `PATH`.
- Broad retrieval output was truncated twice; bounded targeted reads resolved both cases.
- This is one static reconstruction at commit `6360064ea874e7350de2121e9cc569b9045fd1e0`, not proof that an unaided operator would make every required semantic distinction.
- Canonical repository content remained read-only. Initial and final status showed pre-existing untracked `experiments/041/`; it was not modified. `git diff --check` passed.
- Git emitted sandbox warnings because it could not create macOS toolchain cache files under `/tmp`; baseline resolution and read-only checks still completed.
- Compute/model cost and final output size are `UNKNOWN`.

## Candidate Verdict

**ADEQUATE WITH BOUNDED AMBIGUITIES**

A technically literate new operator can reconstruct the implemented software truth and the empirical operating and governance truth from the repository alone. The primary boundaries—software versus manual practice, learned policy versus automation, delivery versus downstream effects, and specification versus authorization—are explicit and materially consistent.

Remaining ambiguities are bounded: minor vocabulary drift across document generations, intentionally frozen and right-censored empirical artifacts, incomplete historical source-policy provenance, and inability to execute the test suite in this environment. None prevents a defensible reconstruction, but together they preclude a `STRONG` verdict.

## Human Review Form

- Accept/reject: ____________________
- Material corrections required: ____________________
- Additional evidence required: ____________________
- Clarity assessment: ____________________
- Confidence assessment: ____________________
- Human review minutes: ____________________