## ARM

TREATMENT — sole Integrator for Experiment 041. Two frozen, independently produced packages were integrated without delegation, Reviewer/Adversary roles, control-arm inspection, blind-mapping inspection, external research, or repository modification.

## BASELINE

`6360064ea874e7350de2121e9cc569b9045fd1e0`

`HEAD` matched the requested baseline.

## START/END TELEMETRY

- Package A wrapper: `2026-09-04T11:59:53Z–12:02:42Z`; 169s.
- Package B wrapper: `2026-09-04T11:59:55Z–12:02:34Z`; 159s.
- Parallel overlap: 159s.
- Package-phase union / critical path: 169s.
- Package overlap fraction: 159 / 169 = 94.1%.
- Integrator: `2026-09-04T12:03:42Z–12:04:06Z`; 24s.
- Gap between package-phase completion and Integrator start: 60s.
- Treatment successful path through captured Integrator end: 253s.
- Post-package overhead through captured end: 84s, comprising the 60s routing gap and 24s integration.
- Agent runs: 3 logical roles.
- Integrator retrieval retries: 1. The initial combined required-artifact retrieval was display-truncated; only the same authorized artifacts were re-read in bounded chunks.
- Failures: read-only macOS `xcrun` cache warnings; baseline resolution still succeeded.
- Human clarifications/interventions/escalations: 0.
- Context restarts: 0 observed.
- Broad re-research: No.
- Live Experiment 030/035 state: not inspected.
- External interaction/spend: none / €0.
- Compute/model cost: UNKNOWN; not exposed.
- Final output bytes/tokens: UNKNOWN; not exposed.

Package-internal timestamps differ from the supplied wrapper inputs: A reports `12:00:07Z–12:01:09Z` (62s), and B reports `12:00:11Z–12:01:18Z` (67s). The prospectively supplied wrapper intervals are retained as the package timing inputs; the difference is a telemetry-boundary ambiguity.

Direct repository reads beyond the required specification, preregistration, and frozen packages:

1. Git `HEAD` resolution — **CITATION VERIFICATION**: verified that the working repository resolved to the stated frozen baseline. No repository file content was read by the Integrator beyond the required artifacts.

## PACKAGE A SUMMARY

Implemented software is a Python 3.11+ modular monolith with console and `python -m` entry points. It contains:

- Source-specific adapters that handle bounded acquisition, validation, normalization, stable logical identity, timestamps, metadata, and source caveats without owning SQLite persistence.
- A generic one-collector pipeline governing run lifecycle.
- SQLite persistence with `signal_sources`, `pipeline_runs`, and `source_observations`.
- A deliberately split transaction model: the running record is committed before collection; a successful observation batch and its final accounting are atomic; failure is recorded separately.
- Revision-aware append semantics keyed by source, external identity, and capture sequence. Material comparison excludes collection time and run identity. Unchanged recaptures create no row; changed states append; `A → B → A` remains three captures.
- Current reads defined by maximum capture sequence, not timestamps or most recent run.
- One implemented domain-specific CN75 Czech trade reasoner with deterministic calculations, lineage, bounded interpretation, unsupported-claim controls, and missing-evidence failures.
- Static tests covering persistence, rollback, migration, latest-state selection, adapters, arithmetic, lineage, and inference limits.

No generic opportunity engine, exact-resolution comparator, FORGE engine, scheduler, orchestration service, authorization service, interaction/effect tracker, portfolio system, telemetry platform, or autonomous operating system is implemented.

Code and `ARCHITECTURE.md` have no material semantic contradiction. Bounded omissions concern a few tree entries, compressed CLI counting, lack of a public history API, and incomplete documentation of the split run transaction boundary.

## PACKAGE B SUMMARY

The empirical operating loop is:

`OBSERVE → RADAR → DISCRIMINATE → FORGE → INTERACT → MEASURE → LEARN`

It is a learned/manual operating practice, not a mandatory runtime pipeline. Candidates may skip stages or terminate when necessary conditions fail.

Opportunity discrimination uses interacting fatal constraints rather than compensatory additive scoring. A viable object requires an identifiable consequential decision, recoverable information, inadequate existing resolution, feasible improvement, legitimate actor access, and observable effect. Capture and repeatability are additional commercial requirements.

Exact-resolution analysis compares:

`ACTOR × DECISION × INPUTS × RESOLUTION × OUTPUT × TIMING`

It is empirically supported manual policy, not implemented generic automation.

FORGE has evidence as a bounded decision-compression artifact pattern. Generic reasoning capability, reliable actor value, and cross-domain generality remain unearned.

The governance boundary is:

`SPECIFICATION ≠ AUTHORIZATION ≠ CAPABILITY ≠ ACCESS`

Publication or delivery does not establish exposure, comprehension, decision effect, downstream action, value, or capture. UNKNOWN exposure/effect must remain UNKNOWN.

Telemetry policy is prospective, lightweight, artifact-local, and causally separated. It does not authorize inferred ROI, synthetic efficiency scores, dashboards, or retrospective token-cost reconstruction.

Automation is evidence-earned only for repeated, mechanically reusable, reversible work likely to improve experiment economics and subject to subsequent measurement. Consequential authorization and semantic judgment remain human-governed.

Supported evidence includes fatal-gate discrimination, exact-resolution reasoning, bounded decision compression, controlled delivery, revision-aware persistence, and qualitative movement of uncertainty downstream. Repeatable actor effect, value, payment, revenue, capture, scalable economics, economic compounding, autonomous operation, and general multi-agent superiority remain unproven or UNKNOWN.

## CROSS-BOUNDARY RECONCILIATION

The two packages are complementary and materially consistent:

- **Implemented software:** bounded source collection, normalization, SQLite run accounting, immutable revision capture, latest-state reads, and one fixed CN75 reasoner.
- **Manual/documentary operating practice:** the broader empirical loop, experiment lifecycle, authorization controls, telemetry discipline, and human-governed progression decisions.
- **Empirically learned but unimplemented policy:** fatal-gate opportunity discrimination, exact-resolution comparison, FORGE decision compression, evidence-earned automation criteria, and the delivery/exposure/effect evidence model.
- **Unproven claims:** reliable actor effect, commercial value, willingness to pay, repeatability, scale, autonomous operation, and general economic superiority from agent parallelism.

The implemented CN75 reasoner is a narrow instance of structured decision support; it does not implement generic FORGE, opportunity discrimination, exact-resolution comparison, or authorization policy. Likewise, revision-aware observation storage supports evidence preservation but does not constitute the full empirical operating system.

## MATERIAL RECONSTRUCTION AMBIGUITIES

- Current operating truth is distributed across top-level documents, dated models, checkpoints, audits, and experiment results.
- Documents cover different evidence horizons. Historical audits may describe drift later resolved by Experiment 039.
- Framework names such as ATLAS, RADAR, FORGE, PORTFOLIO, and FREEDOM can resemble software modules although they principally denote conceptual or manual layers.
- README and Operating Model express the loop at different abstraction levels; DISCRIMINATE is explicit in the newer summary but embedded in the older detailed lifecycle.
- Historical captures exist in SQLite, but the repository exposes no dedicated public full-history or as-of API.
- Source policy and caveat metadata represent mutable current state rather than versioned history.
- Migration applicability is inferred from schema shape rather than a schema-version table; noncanonical intermediate-schema safety is UNKNOWN.
- Concurrent-writer behavior, live external API behavior, and runtime test status are UNKNOWN.
- Package wrapper timings and package-internal timings use materially different boundaries.
- Package A reports 80 statically inspected test functions, but tests were not executed under the read-only constraint.

## WHAT A NEW OPERATOR MUST NOT INFER

A new operator must not infer that:

- The empirical operating loop or named framework layers are deployed software.
- The CN75 reasoner is a generic reasoning, FORGE, or opportunity engine.
- A specification grants authorization, capability grants authority, or surface access proves actor access.
- Delivery or publication proves exposure, response, comprehension, effect, value, or capture.
- UNKNOWN means failure, zero response, or negative evidence.
- Fatal constraints can be offset by an aggregate score.
- Signal volume, novelty, friction, public information, market size, or automation potential independently proves opportunity.
- Decision compression has proven actor or commercial value.
- Stored historical rows imply a supported history/as-of application interface.
- Static tests establish live-service compatibility, production reliability, concurrency safety, or scale.
- Zero incremental external spend proves low total cost or improving economics.
- Current evidence proves revenue, willingness to pay, repeatability, scalable economics, compounding, autonomous operation, or general multi-agent superiority.
- This packet evaluates the control arm or establishes a treatment speedup against it.

## CONFIDENCE / LIMITATIONS

Confidence is **HIGH** for static software structure, persistence semantics, documented governance boundaries, and the distinction between implementation and learned practice. Confidence is **MODERATE-HIGH** for operational behavior because tests were inspected but not run. Confidence is **MEDIUM** for empirical generality.

Material UNKNOWNs include live external-source behavior, concurrent SQLite writers, noncanonical migration safety, exposure/effect in the protected live observation windows, actor value, payment, repeatability, complete historical human-attention telemetry, and compute/model cost.

The Integrator relied on the frozen packages and did not independently verify their underlying citations. No package conflict justified additional repository reading, and no broad re-research or coordination failure occurred. The final treatment artifact could not be persisted because the user required read-only operation; this response is the frozen packet.

## FINAL VERDICT

**ADEQUATE WITH BOUNDED AMBIGUITIES**

A technically literate new operator can reconstruct the principal implemented software truth and empirical operating/governance truth from the repository, while preserving the critical distinction between software, manual practice, learned-but-unimplemented policy, and unproven claims. Reconstruction is not STRONG because current truth remains distributed across differently dated artifacts, conceptual layer names can be mistaken for implementations, some software interfaces and telemetry boundaries are compressed, and several operational and empirical properties remain UNKNOWN.