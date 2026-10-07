# Experiment 052 — Approved Debrief and Local Closure

**Recorded:** 2026-10-07

**Final experiment verdict:** A — CONTROL V1 EARNED, at the bounded experimental level.

**Operational endpoint:** CLOSURE_READY; local closure only, publication unauthorized.

## Contract and evidence

- Contract: [SPEC-052](../../specs/052-human-attention-control-plane-v1.md).
- Frozen implementation: `1ffb110bc2cd564ddeaf05f51dc2db5ebe33730c`.
- Frozen implementation report: [control-plane-v1-test.md](control-plane-v1-test.md). Its pending-acceptance statements remain historical freeze evidence, superseded for closure by this debrief.
- Approved source: [human-acceptance-evidence.md](human-acceptance-evidence.md), introduced by `20a4fac`; unchanged by closure.
- Transcribed observations and unsupported fields: [acceptance-packet.md](acceptance-packet.md).
- Reconciled execution baseline: `35c7b57`, retaining canonical protocol/evidence at `5adf331` and the original unpublished implementation commit.

## Human observations and timing

Attention requirements were clearly surfaced at the top and observable within seconds. Exact attention-identification seconds remain **UNKNOWN**. Full interface orientation took **approximately 3 minutes**, mostly understanding interface architecture/structure sufficiently to contextualize the attention information. This is not an exact measured completion time for all questions 1–9.

The operator then spent **approximately 7 additional minutes** exploring and tracing other opportunity states. This remains separate from primary orientation. Exact detail-view counts, question-by-question answers, and a comparative V0 timing baseline remain unsupported. No speedup ratio is claimed.

The approved human formulation is:

> Control Plane V1 materially improves human actionability and exposes attention requirements quickly while preserving auditability; full interface orientation still carries information-hierarchy friction, and the dominant newly exposed gap is truthful Engine-level funnel/state visibility.

The operator reported that the UI information model works really well and materially improves actionability/usability as a research tool. These observations establish bounded operator benefit; they do not establish external demand, production readiness, willingness to pay, or economic value.

## Applying the preregistered verdict rules

**A — CONTROL V1 EARNED** applies: the frozen implementation record establishes a faithful bounded representation, and the approved human evidence explicitly establishes materially improved attention/actionability while preserving auditability. The benefit is demonstrated for this operator and this static experimental surface.

**B — PROMISING BUT INCONCLUSIVE** does not best describe the approved overall finding: control benefit is established in the supplied bounded formulation. Incomplete individual answers limit the finding's scope; they are not filled from fixtures or treated as proof of exhaustive correctness.

**C — CONTROL LAYER NOT USEFUL** is unsupported: the human reported material improvement and quick attention visibility, despite orientation friction.

**D — CONTROL REPRESENTATION MISLEADING** is unsupported by the approved observations. Visual similarity creates hierarchy friction, but the source expressly treats this as an interface defect, not model failure. Untested semantic distinctions and synthetic/historical comprehension are not declared passed.

**E — INVALID** is not established. The implementation record reports compliant isolation and integrity, and closure preserves the frozen surface. Exact timing and procedural completion remain UNKNOWN where unsupported; descriptive approximate timing is retained without claiming full protocol execution or mixing phases. No timing ratio or arbitrary threshold is imposed.

## What the experiment earns

Control-oriented attention visibility materially improves the operator's actionability at this experimental level. Trajectory and auditability remain must-have properties. Full orientation still requires intellectual reconstruction of visually similar layers and objects.

Human use exposed a candidate ENGINE → CONTROL → POSSIBILITY SPACE → EVIDENCE hierarchy. This is an information-architecture hypothesis, not canonical architecture. The dominant new hypothesis is that truthful Engine-level funnel/distribution visibility could improve whole-system orientation and reveal accumulations, dormant inventory, and systemic bottlenecks.

The six curated historical fixtures are not the complete AE inventory. Neither those fixtures nor four synthetic control scenarios justify system-wide counts or funnel-efficiency claims.

## What remains unproven

Exact attention time; exact primary question-completion time; number and identity of details opened; individual control-question correctness; discrimination of every state pair; exhaustive six-dimensional and V0 preservation comprehension; synthetic/historical separation in human use; V0 comparative speed; external-user comprehension; scaling to dozens of opportunities; automatic classification; monitoring; autonomy safety; production architecture; demand; willingness to pay; and economic value remain unproven where not supported by the approved source.

The human-role finding reserves attention for ideation, testing, decisions, authorization, exceptions, and judgment while allowing mechanical work to be delegated without new judgment. It supplies no consequential-action authority.

## Integrity and closure boundary

- Existing deterministic suite: **89 passed** (`.venv/bin/pytest -q`).
- `git diff --check`: PASS before local commit.
- Experiment 051 and V1 viewer/fixtures: unchanged against frozen `1ffb110`.
- Frozen implementation report and approved human evidence: unchanged against reconciled `35c7b57`.
- Closure changes are confined to this debrief, the acceptance record, and `STATUS.md`; operational-state update is authorized by the current handoff and protocol.
- Specifications, living conceptual documents, production source, tests, and schema are unchanged.
- No human test rerun, external research, actor interaction, deployment, or push occurred. Experiment 053 has not started.

## Exactly one recommended next research action

Prepare a bounded repository-evidence audit to determine whether AE can truthfully support Engine-level funnel/lifecycle semantics and counts, including inventory completeness, counting units, evidence horizons, and synthetic exclusions, before any funnel implementation. This recommendation does not start Experiment 053 or authorize an implementation.

Publication remains a separate human-authorized operation. The closure commit is identified by Git history for this file; the original frozen artifacts remain inspectable at their immutable references.
