# Acceptance Packet A

## Package A — Implemented Software Truth

Baseline: `6360064ea874e7350de2121e9cc569b9045fd1e0`; `HEAD` matched this baseline.

The implemented software is a Python 3.11+ modular monolith with console and `python -m` entry points. It includes:

- Source-specific adapters for bounded acquisition, validation, normalization, stable logical identity, timestamps, metadata, and source caveats. Adapters do not own SQLite persistence.
- A generic single-collector pipeline governing run lifecycle.
- SQLite tables: `signal_sources`, `pipeline_runs`, and `source_observations`.
- Split transaction semantics: the running record commits before collection; a successful observation batch and its final accounting are atomic; failure is recorded separately.
- Revision-aware append semantics keyed by source, external identity, and capture sequence. Material comparison excludes collection time and run identity. Unchanged recaptures add no row; changed states append; `A → B → A` remains three captures.
- Current-state reads selected by maximum capture sequence, not timestamps or latest run.
- One domain-specific CN75 Czech trade reasoner with deterministic calculations, lineage, bounded interpretation, unsupported-claim controls, and missing-evidence failures.
- Static tests covering persistence, rollback, migration, latest-state selection, adapters, arithmetic, lineage, and inference limits.

No generic opportunity engine, exact-resolution comparator, FORGE engine, scheduler, orchestration service, authorization service, interaction/effect tracker, portfolio system, telemetry platform, or autonomous operating system is implemented.

Code and `ARCHITECTURE.md` have no material semantic contradiction. Bounded omissions include several tree entries, compressed CLI counting, no public history API, and incomplete documentation of the split run transaction boundary.

## Package B — Empirical Operating and Governance Truth

The empirical operating loop is:

`OBSERVE → RADAR → DISCRIMINATE → FORGE → INTERACT → MEASURE → LEARN`

This is learned/manual operating practice, not a mandatory runtime pipeline. Candidates may skip stages or terminate when necessary conditions fail.

Opportunity discrimination uses interacting fatal constraints, not compensatory additive scoring. Viability requires:

- An identifiable consequential decision.
- Recoverable information.
- Inadequate existing resolution.
- Feasible improvement.
- Legitimate actor access.
- Observable effect.

Capture and repeatability are additional commercial requirements.

Exact-resolution analysis compares:

`ACTOR × DECISION × INPUTS × RESOLUTION × OUTPUT × TIMING`

It is empirically supported manual policy, not implemented generic automation.

FORGE has evidence as a bounded decision-compression artifact pattern. Generic reasoning capability, reliable actor value, and cross-domain generality remain unearned.

The governance boundary is:

`SPECIFICATION ≠ AUTHORIZATION ≠ CAPABILITY ≠ ACCESS`

Publication or delivery does not establish exposure, comprehension, decision effect, downstream action, value, or capture. UNKNOWN exposure or effect must remain UNKNOWN.

Telemetry policy is prospective, lightweight, artifact-local, and causally separated. It does not authorize inferred ROI, synthetic efficiency scores, dashboards, or retrospective token-cost reconstruction.

Automation is evidence-earned only for repeated, mechanically reusable, reversible work likely to improve experiment economics and subject to later measurement. Consequential authorization and semantic judgment remain human-governed.

Supported evidence includes fatal-gate discrimination, exact-resolution reasoning, bounded decision compression, controlled delivery, revision-aware persistence, and qualitative movement of uncertainty downstream.

Repeatable actor effect, value, payment, revenue, capture, scalable economics, economic compounding, and autonomous operation remain unproven or UNKNOWN.

## Cross-Boundary Reconciliation

The findings are complementary and materially consistent:

- Implemented software covers bounded source collection, normalization, SQLite run accounting, immutable revision capture, latest-state reads, and one fixed CN75 reasoner.
- Manual/documentary operating practice covers the broader empirical loop, experiment lifecycle, authorization controls, telemetry discipline, and human-governed progression decisions.
- Empirically learned but unimplemented policy covers fatal-gate opportunity discrimination, exact-resolution comparison, FORGE decision compression, evidence-earned automation criteria, and the delivery/exposure/effect evidence model.
- Unproven claims include reliable actor effect, commercial value, willingness to pay, repeatability, scale, autonomous operation, and general economic superiority from concurrent work.

The CN75 reasoner is a narrow instance of structured decision support. It does not implement generic FORGE, opportunity discrimination, exact-resolution comparison, or authorization policy. Revision-aware observation storage supports evidence preservation but does not constitute the complete empirical operating system.

## Material Reconstruction Ambiguities

- Current operating truth is distributed across top-level documents, dated models, checkpoints, audits, and experiment results.
- Documents cover different evidence horizons. Historical audits may describe drift later resolved by Experiment 039.
- Names such as ATLAS, RADAR, FORGE, PORTFOLIO, and FREEDOM can resemble software modules although they principally identify conceptual or manual layers.
- README and Operating Model express the loop at different abstraction levels. DISCRIMINATE is explicit in the newer summary but embedded in the older detailed lifecycle.
- Historical captures exist in SQLite, but no dedicated public full-history or as-of API is exposed.
- Source policy and caveat metadata represent mutable current state rather than versioned history.
- Migration applicability is inferred from schema shape rather than a schema-version table. Safety for noncanonical intermediate schemas is UNKNOWN.
- Concurrent-writer behavior, live external API behavior, and runtime test status are UNKNOWN.
- Supplied wrapper timings and package-internal timings use materially different boundaries.
- The static inspection reports 80 test functions, but the tests were not executed under the read-only constraint.

## What a New Operator Must Not Infer

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
- Current evidence proves revenue, willingness to pay, repeatability, scalable economics, compounding, or autonomous operation.
- This packet establishes a comparative speedup against another candidate.

## Confidence and Limitations

Confidence is **HIGH** for static software structure, persistence semantics, documented governance boundaries, and the distinction between implementation and learned practice.

Confidence is **MODERATE-HIGH** for operational behavior because tests were inspected but not run.

Confidence is **MEDIUM** for empirical generality.

Material UNKNOWNs include live external-source behavior, concurrent SQLite writers, noncanonical migration safety, exposure/effect in protected live observation windows, actor value, payment, repeatability, complete historical human-attention telemetry, and compute/model cost.

The underlying repository citations were not independently verified. No identified conflict justified additional repository reading. Runtime verification and external research were not performed.

## Candidate Verdict

**ADEQUATE WITH BOUNDED AMBIGUITIES**

A technically literate new operator can reconstruct the principal implemented-software truth and empirical operating/governance truth while preserving the critical distinction between software, manual practice, learned-but-unimplemented policy, and unproven claims.

Reconstruction is not STRONG because current truth remains distributed across differently dated artifacts, conceptual layer names can be mistaken for implementations, some software interfaces and telemetry boundaries are compressed, and several operational and empirical properties remain UNKNOWN.

## Human Review Form

- Accept/reject: ____________________
- Material corrections required: ____________________
- Additional evidence required: ____________________
- Clarity assessment: ____________________
- Confidence assessment: ____________________
- Human review minutes: ____________________
