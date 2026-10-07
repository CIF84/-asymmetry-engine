# Spec 055 — Engine Control Plane V2

## Status
READY FOR EXECUTION

## Milestone
Empirical Search Through Business Possibility Space — Engine Visibility V2

## Type
Bounded repository-only representation/UI experiment. No fresh RADAR, external research, actor interaction, production persistence, automation, policy change, or canonical architecture change.

## Baseline
Execute from synchronized canonical main at or after published Experiment 054 closure (8aae719 short ref).

## Why
051 established opportunity-level knowledge visibility. 052 established attention/control visibility. 053 showed that a whole-Engine funnel built from curated history would be misleading. 054 validated a manual family/decision-instance evidence contract for prospective capture while preserving older history as partial.

The operator's remaining question is:
**How is AE itself performing?**

## Primary hypothesis
A truthful Engine-level top layer can let the operator quickly understand:
- what population is represented;
- what is historical/partial versus prospectively governed;
- where evidence has accumulated;
- where opportunity flow is blocked or unresolved;
- what the dominant known bottlenecks are;
- how much requires human attention;
while preserving Control, Possibility Space, Evidence, provenance and missingness underneath.

## Critical epistemic rule
The dashboard must communicate its own limits.

Do not present the six historical cohort records as the complete AE population.
Do not present mixed-horizon historical counts as current totals.
Do not present synthetic control scenarios as actual Engine state.
Do not infer prospective population counts that do not exist.

## Four-layer hypothesis
Test a coherent hierarchy:
1. ENGINE — how is AE performing?
2. CONTROL — what needs the human?
3. POSSIBILITY SPACE — what opportunities exist and what separates them from value capture?
4. EVIDENCE — why does AE believe this and how did the belief evolve?

This is a representation hypothesis, not canonical software architecture.

## Data populations
V2 must distinguish visually and semantically:

### A. Prospective governed population
Records captured under the 054 manual identity/evidence contract after it became available.
At experiment start this may legitimately be zero. Zero governed records is different from zero opportunities.

### B. Historical bounded cohort
The six 054 validation families, with three supported decision instances and three family-only unresolved-instance records. This is partial historical evidence, not a census.

### C. Historical run telemetry
Where useful, explicitly labeled run-local counts from earlier experiments (for example raw/candidate/disposition summaries validated by 053). These are heterogeneous historical run metrics, not unique opportunity counts.

### D. Synthetic UI/control scenarios
If reused to exercise Control, they must remain unmistakably synthetic and excluded from Engine counts.

## Engine top layer
On initial open, show a compact system overview that answers without drill-down:

### Population / coverage
- prospective governed population count;
- historical bounded cohort size;
- supported historical decision-instance count;
- unresolved family-only count;
- explicit completeness/horizon label.

### Evidence frontier
Represent where the bounded cohort has evidence without implying a mandatory linear funnel. Preserve independent states and UNKNOWN.

At minimum distinguish:
- signal/candidate evidence;
- residual gap / decision-ready resolution;
- delivery/exposure;
- decision-state effect;
- economic effect;
- WTP/exchange;
- transaction;
- repeatability/value capture.

A record may appear in multiple frontier states. Explain denominator and overlap.

### Lifecycle distribution
Show only for a named population/horizon.
Historical cohort lifecycle may be shown as historical/derived.
Prospective lifecycle may be shown only for governed records.

### Blocker/reactivation distribution
Show only supportable bounded-cohort categories and disclose derived/partial semantics.
Make contingent / structural-at-horizon / unresolved distinguishable.
Surface dormant/reactivation inventory without implying blockers have cleared.

### Human attention
Use real historical/control evidence only where supportable.
Do not use 052 synthetic attention cards to claim current actual attention load.
If current opportunity attention is unsupported, say so explicitly.
Repository active-work status may be shown separately as project-operation state, not opportunity attention.

## No fake funnel
Do not use one linear conversion funnel if it implies mutually exclusive stages or stable conversion rates.

Allowed visual grammars include:
- evidence-frontier distribution;
- state distribution;
- branching/flow summary;
- portfolio state map;
- clearly labeled historical run funnel snippets.

If a funnel-like shape is used, labels must prevent conversion-rate interpretation.

## System diagnostics
V2 should help the operator ask:
- Is evidence mostly accumulating upstream?
- Are many represented opportunities dormant?
- Which blocker types dominate this bounded population?
- Is the economic frontier still empty/unestablished?
- What is unknown because of missing data versus genuinely absent evidence?
- Is there any prospective governed population yet?

Do not create a composite Engine health score or efficiency score.

## Visual hierarchy
052 found that conceptually different layers looked like similar boxes.

V2 must deliberately test stronger visual hierarchy between:
- ENGINE;
- CONTROL;
- POSSIBILITY SPACE;
- EVIDENCE.

This is functional information architecture, not cosmetic polish.

Do not specify exact colors or ornamental styling. Use layout, typography, grouping, scale, spacing, labels and interaction hierarchy to make layers distinguishable.

## Preserve accepted lower layers
V2 must preserve the useful properties of 051/052:
- opportunity-first overview/detail;
- six dimensions: Resolution / Access / Adoption / Control / Regulatory / Economic;
- UNKNOWN distinct from FAR and BLOCKED;
- lifecycle semantics;
- control/attention semantics;
- trajectory/history as MUST-HAVE;
- evidence provenance;
- unproven claims;
- no numeric composite opportunity score;
- no automatic ranking.

Do not modify 051/052 artifacts.

## Identity/accounting
Use 054 semantics:
- family and decision instance are distinct;
- historical admission remains UNKNOWN;
- family-only unresolved instance records remain unresolved;
- signals/candidates/experiments do not inflate unique-opportunity counts;
- reactivation does not rewrite old verdicts;
- mixed historical horizons are disclosed.

The V2 fixtures may copy/transform 054 data for representation, but must cite provenance and remain under experiments/055/.

## Prospective zero-state
Explicitly test whether the UI remains useful when prospective governed population = 0.

The interface should make the meaning obvious:
- contract is ready for prospective capture;
- no governed prospective records have yet been captured;
- historical evidence remains available separately;
- zero does not mean RADAR found nothing.

## Drill-down
From any Engine aggregate, operator must be able to understand:
- population/denominator;
- evidence horizon;
- included records;
- missingness/UNKNOWN;
- derivation/provenance;
then reach opportunity/control/evidence detail.

No aggregate may become an unauditable decorative number.

## Behavioral human acceptance
Codex must freeze V2 before human acceptance. It must not answer for the operator.

Primary cold-use questions:
1. What population(s) am I looking at?
2. How much of this is historical partial evidence versus prospective governed state?
3. How many historical families and supported decision instances are represented?
4. Where has evidence accumulated?
5. What major frontier remains unestablished?
6. What lifecycle distribution is shown, and for what population/horizon?
7. What blockers appear dominant in the bounded historical cohort?
8. Do we know the actual current opportunity-attention load?
9. Is there any prospective governed population yet?
10. What does AE not know about itself?

Secondary questions:
11. Can an aggregate be traced to included opportunities/evidence?
12. Can the operator move naturally from ENGINE → CONTROL → POSSIBILITY SPACE → EVIDENCE?
13. Are the four layers visually/conceptually distinct?
14. Did the Engine layer reduce reconstruction burden?
15. What remains confusing or misleading?

## Timing
Human acceptance should separately record:
- time to answer primary questions 1–10 with confidence;
- subsequent exploration/audit time if voluntarily continued.

No arbitrary pass threshold. Preserve exact/approximate timing honestly.

## Success evidence
Strong evidence includes:
- correct population/horizon interpretation without prior explanation;
- no confusion between historical cohort and complete Engine;
- no confusion between zero prospective records and zero opportunities;
- operator identifies upstream/economic evidence pattern correctly;
- aggregates are auditable;
- stronger visual hierarchy materially improves orientation;
- lower-layer usability/auditability is retained.

## Failure evidence
Material failure includes:
- historical partial counts look current/complete;
- prospective zero-state looks like empty AE;
- evidence frontier reads as false conversion funnel;
- operator cannot identify denominator/horizon;
- layer hierarchy remains visually ambiguous;
- aggregates hide provenance;
- Control/Possibility/Evidence become harder to use;
- UI implies unsupported efficiency/ranking.

## Implementation scope
All new files under experiments/055/.

Create at minimum:
- experiments/055/engine-control-plane-v2-test.md
- experiments/055/acceptance-packet.md
- experiments/055/viewer/index.html
- bounded fixtures/data needed by viewer

Prefer dependency-free static HTML/CSS/JavaScript.

Screenshots are optional under experiments/055/.

## Architecture/software boundary
This is a reversible experimental representation only.

Do NOT:
- create production Opportunity model;
- create database/schema/migration;
- implement live prospective capture;
- implement RADAR ingestion;
- add APIs/backend/authentication;
- add monitoring/notifications;
- automate identity/dedup/lifecycle;
- implement ranking/scoring;
- deploy;
- modify production source/tests/schema;
- modify living/protocol docs;
- modify prior experiments/specs;
- use external research/contact.

## Human role
The human tests comprehension, usability, control and judgment. Do not require the human to transcribe acceptance forms; after natural feedback, approved evidence should be materialized durably by the upstream role before context-free closure handoff.

## Budget
Target implementation 20–40 active minutes; hard ceiling 60; external spend €0. Use prospective timing. Stop when V2 is frozen, population semantics are explicit, acceptance packet is ready, and integrity passes.

## Verdicts
A — ENGINE VISIBILITY V2 EARNED: implementation faithful and later human acceptance shows materially improved truthful whole-system comprehension while preserving lower-layer auditability.
B — PROMISING BUT INCONCLUSIVE: representation coherent but human evidence incomplete/mixed.
C — ENGINE LAYER NOT USEFUL: little comprehension benefit or unacceptable burden.
D — MISLEADING REPRESENTATION: false completeness, funnel semantics, population confusion or weakened auditability.
E — INVALID: scope/isolation/timing/integrity violation.

Before human acceptance use only a provisional implementation status.

## Required implementation-freeze report
Return exactly:
1. Provisional implementation status
2. Repository baseline
3. Active time and timing method
4. Spend
5. Isolation confirmation
6. V0/V1/054 preservation result
7. Populations represented
8. Prospective zero-state result
9. Historical bounded-cohort result
10. Historical run-telemetry result
11. Family/decision-instance accounting result
12. Evidence-frontier implementation
13. Lifecycle-distribution implementation
14. Blocker/reactivation implementation
15. Human-attention implementation
16. Missingness/UNKNOWN implementation
17. Engine diagnostics implementation
18. Four-layer hierarchy implementation
19. Visual-hierarchy result
20. Control-layer preservation
21. Possibility-space preservation
22. Evidence/trajectory preservation
23. Aggregate auditability result
24. False-funnel/completeness safeguards
25. Acceptance packet status
26. Behavioral timing design
27. Architecture boundary result
28. What implementation establishes
29. What remains unproven
30. Exactly one recommended next action

Append unnumbered: Viewer path; Acceptance packet path; Artifact path; Integrity/test result; Commit SHA.

## Repository integrity
All implementation changes under experiments/055/ plus mechanical STATUS transition only. Prior experiments/specs/living/protocol docs/production source/tests/schema unchanged. git diff --check and existing tests pass. Commit locally. Do not push.

Do not push.
