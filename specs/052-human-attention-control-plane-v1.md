# Spec 052 — Human Attention Control Plane V1

## Status
READY FOR EXECUTION

## Milestone
**Empirical Search Through Business Possibility Space — Control V1**

Representation V0 established that the operator can materially improve orientation by seeing what AE knows. Experiment 052 tests the next bounded question:

> **Can AE show what requires human attention, and what does not, without requiring the operator to reconstruct the system state?**

## Type
Bounded repository-only representation/UI experiment using Experiment 051's frozen opportunity evidence. No fresh RADAR, external research, actor interaction, production architecture, policy change, automation, or consequential action.

## Baseline
Execute from synchronized `main` at or after:
`a4e71855ef9fabc7d74b979d330381f1b77fbbc7`

Experiment 051 is CLOSED and its V0 viewer/fixtures are the frozen human-accepted baseline.

## Primary hypothesis
A control-oriented top layer can allow the human operator to determine within seconds:

- what requires attention;
- why;
- what is progressing safely without intervention;
- what is waiting;
- what is blocked;
- what needs a decision;
- what needs authorization;
- what happens if the operator does nothing;

while preserving evidence-backed drill-down auditability.

## What 052 is NOT testing
It is not testing:
- autonomous operation;
- automatic prioritization;
- opportunity ranking;
- economic-proximity policy;
- fresh opportunity selection;
- agent orchestration;
- production persistence;
- notification systems;
- whether AE can safely act without authorization.

## Human-control principle
The intended long-term direction is:

```text
human attention
→ ideation
→ human testing
→ consequential decisions
→ judgment-heavy exceptions

mechanical work
→ delegated where no new human judgment is required
```

052 tests only whether the interface can make that division legible.

## Preserve V0
Do not modify Experiment 051.

Copy/reuse its representational concepts in 052, but V0 must remain byte-for-byte historical evidence.

Must preserve in V1:
- opportunity-first representation;
- six independent dimensions:
  Resolution / Access / Adoption / Control / Regulatory / Economic;
- UNKNOWN distinct from FAR and BLOCKED;
- ACTIVE / DORMANT / REVIEW / TERMINAL distinction;
- Evidence/History trajectory;
- evidence provenance;
- explicit unproven claims;
- no numeric composite score;
- no automatic opportunity ranking.

Trajectory/auditability is a **MUST-HAVE** property.

## Two orthogonal states

### Opportunity state
Where the business possibility currently is:
- ACTIVE
- DORMANT
- REVIEW
- TERMINAL

### Operational/control state
What, if anything, is happening or required now.

052 may test a small vocabulary such as:
- NEEDS DECISION
- NEEDS AUTHORIZATION
- NEEDS REVIEW
- READY
- PROGRESSING
- WAITING
- BLOCKED / NO ACTION AVAILABLE
- NO ACTION

These labels are experimental. Simplify or adjust if implementation reveals semantic overlap.

Do not infer operational state from lifecycle mechanically when evidence does not support it.

## Historical truth versus control scenarios
The six Experiment 051 fixtures were not designed with complete operational-state telemetry.

Therefore:

1. Preserve historical opportunity evidence as historical truth.
2. Derive operational state only where repository evidence supports it.
3. If additional states are needed to test the control-plane interaction, create **clearly labeled synthetic control scenarios**.
4. Synthetic scenarios must never masquerade as historical AE evidence.
5. Synthetic control state must be visually distinguishable and excluded from claims about actual opportunity history.

This separation is mandatory.

## Control Plane V1 — required top layer
On opening V1, the operator should not need to open every opportunity.

The top layer must make these categories legible:

### NEEDS ATTENTION
Items requiring human judgment/action now, with:
- opportunity/scenario;
- attention type;
- concise reason;
- requested human action;
- consequence of doing nothing where supportable;
- link/drill-down to evidence.

### PROGRESSING / SAFE WITHOUT INTERVENTION
Items for which no current human action is required.

### WAITING
Items dependent on external evidence/time/process, distinct from a human-action requirement.

### BLOCKED / NO ACTION AVAILABLE
Items where progress cannot currently continue and human action is not presently useful.

### DORMANT
Contingently inactive opportunities with reactivation conditions.

Do not force an item into every category. Avoid duplicated cards unless the UI clearly communicates why.

## Attention is not priority
Do not equate:
- NEEDS ATTENTION with highest-value opportunity;
- urgency with economic significance;
- blocked with bad;
- dormant with dead;
- no-action with low value.

No numeric urgency score.

## Explain why
Every attention/control classification must expose a concise explanation.

The operator should be able to answer:

> Why is AE asking me to look at this?

without reconstructing the entire experiment chain.

Where useful show:

```text
CURRENT CONTROL STATE
        ↓
WHY
        ↓
REQUESTED HUMAN ACTION
        ↓
IF NO ACTION
        ↓
EVIDENCE / TRAJECTORY
```

Do not fabricate consequences of inaction. Use UNKNOWN where unsupported.

## Drill-down requirement
V1 must retain the ability to move from control summary to:
- current opportunity state;
- six-dimensional evidence;
- blocker/unknown;
- next discriminator;
- reactivation condition;
- Evidence/History trajectory;
- provenance;
- unproven claims.

The top layer compresses attention; it must not hide epistemic foundations.

## Information hierarchy
Experiment 051 found that lifecycle derivation was not immediately self-explanatory.

V1 should test a clearer detail hierarchy, approximately:
1. Current state
2. Why this state
3. Control/attention state
4. What could move it
5. Six-dimensional evidence
6. Evidence/provenance
7. Trajectory/history
8. What remains unproven

This is a hypothesis, not a mandatory pixel-level design.

## Visualization boundary
Do not add a radar/spider chart merely because it was discussed.

A pre-attentive six-dimensional visualization may be added only if it materially supports the primary control hypothesis and preserves categorical semantics.

Do not map NEAR/MEDIUM/FAR/BLOCKED/UNKNOWN onto fake numerical magnitudes.

## Behavioral acceptance test
The human operator must test the frozen V1 independently before Codex interprets the result.

Create an acceptance packet that measures whether the operator can answer from the top/control layer, preferably without opening every opportunity:

1. How many items require human attention now?
2. Which items require attention?
3. Why does each require attention?
4. What human action is requested?
5. What happens if no action is taken?
6. Which items are progressing safely without human intervention?
7. Which are waiting on external state rather than human action?
8. Which are blocked with no useful action currently available?
9. Which dormant opportunities have explicit reactivation conditions?
10. Can the operator trace an attention classification back to evidence/trajectory?
11. Did the operator need to inspect every opportunity to answer these?
12. What was confusing or required reconstruction?

## Timing
Measure human review separately from implementation.

The acceptance packet should instruct the operator to:
- start a timer immediately before opening V1;
- answer questions 1–9;
- stop the timer once those answers are formed;
- then perform auditability questions 10–12 without mixing that time into the primary control-comprehension measure.

If the operator does not provide timing, preserve UNKNOWN.

Do not impose an arbitrary PASS threshold before observing the result. Record seconds/minutes and qualitative reconstruction burden.

## Comparative baseline
Where feasible, create a bounded V0 comparison packet using the same control questions against frozen V0.

Do not require the human to repeat mechanical work if the comparison can be established without new judgment.

If a fair timed V0 comparison would require substantial operator burden, leave comparative timing UNKNOWN rather than manufacturing it.

## Success evidence
Strong evidence for V1 would include:
- operator identifies attention items without opening every opportunity;
- attention reason is understood correctly;
- waiting versus blocked versus human-action states are distinguishable;
- drill-down makes classifications auditable;
- operator reports lower reconstruction burden;
- no material loss of V0 knowledge visibility.

## Failure evidence
Material failure includes:
- attention layer merely restates lifecycle;
- operator must inspect all details anyway;
- control categories are ambiguous;
- UI hides why classifications exist;
- synthetic scenarios are confused with historical truth;
- attention implies ranking/value unsupported by evidence;
- trajectory/auditability is weakened;
- control compression creates false confidence.

## Required implementation scope
All new files must remain under:
`experiments/052/`

Prefer a dependency-free static HTML/CSS/JavaScript viewer.

Allowed artifacts:
- V1 fixtures/control scenarios;
- V1 static viewer;
- acceptance packet;
- experiment result record;
- screenshots if useful.

Do not modify Experiment 051.

## Explicit prohibitions
Do NOT:
- modify production source;
- modify database/schema;
- create production Opportunity/Control models;
- add backend/API/authentication;
- deploy;
- add external calls;
- add monitoring/notifications;
- automate state classification;
- implement agent actions;
- implement autonomous escalation;
- implement ranking/scoring;
- modify README/ROADMAP/ARCHITECTURE/OPERATING_MODEL;
- modify prior experiments/specs;
- run fresh RADAR;
- contact actors.

## Architecture boundary
V1 is a reversible experimental representation.

It may demonstrate what future production architecture needs to express, but it must not establish that architecture by implementation convenience.

## Human-operating-role test
Record whether the V1 control layer appears capable of reserving human attention for:
- decisions;
- authorization;
- exceptions;
- judgment;

while allowing mechanical status comprehension to be delegated to representation.

Do not infer autonomous-action permission.

## Adversarial checks
Before freezing V1 ask:
1. Are attention states evidence-backed or invented?
2. Does NEEDS ATTENTION merely mean ACTIVE?
3. Are synthetic scenarios unmistakably synthetic?
4. Is waiting distinct from blocked?
5. Is blocked distinct from dormant?
6. Is human authorization distinct from technical capability?
7. Is “no action” accidentally interpreted as “unimportant”?
8. Can every consequential classification be audited?
9. Has trajectory been weakened?
10. Has a hidden ranking system slipped in?
11. Can the operator understand the control plane without reading all details?
12. Would the interface still make sense with dozens of opportunities?

## Budget and stop conditions
Target active implementation/review work: 20–40 minutes.
Hard ceiling: 60 active minutes.
External spend: €0.

Stop when:
- V1 top/control layer is frozen;
- historical versus synthetic state is clearly separated;
- acceptance packet is ready;
- repository integrity passes.

Do not perform human acceptance on the operator's behalf.

## Verdicts

### A — CONTROL V1 EARNED
Implementation is faithful and human acceptance later demonstrates materially improved attention/control comprehension while preserving auditability.

### B — PROMISING BUT INCONCLUSIVE
Representation is coherent but human evidence is incomplete/mixed or control benefit is not yet established.

### C — CONTROL LAYER NOT USEFUL
Human acceptance shows little/no attention benefit or unacceptable reconstruction burden.

### D — CONTROL REPRESENTATION MISLEADING
The layer obscures evidence, confuses states, creates unsupported priority, or weakens auditability.

### E — INVALID
Scope, isolation, synthetic/historical separation, timing, or repository integrity was violated.

At implementation freeze before human acceptance, use a provisional implementation status rather than claiming final A–D.

## Required files
Create at minimum:
- `experiments/052/control-plane-v1-test.md`
- `experiments/052/acceptance-packet.md`
- `experiments/052/viewer/index.html`

Additional fixture/CSS/JS files under `experiments/052/` are allowed.

## Repository integrity
Before completion:
- all changes confined to `experiments/052/`;
- Experiment 051 unchanged;
- canonical docs unchanged;
- production source/tests/schema unchanged;
- no external action occurred;
- `git diff --check` passes;
- existing test suite passes if available.

Commit permitted 052 artifacts locally. Do not push.

## Required implementation-freeze report
Return exactly:

1. Provisional implementation status
2. Repository baseline
3. Active time and timing method
4. Spend
5. Isolation confirmation
6. V0 preservation result
7. Historical opportunities/scenarios represented
8. Synthetic-control-scenario result
9. Opportunity-state vocabulary
10. Operational/control-state vocabulary
11. Needs-attention implementation
12. Progressing/no-action implementation
13. Waiting implementation
14. Blocked/no-action implementation
15. Dormant/reactivation implementation
16. Why/explanation implementation
17. Consequence-of-inaction handling
18. Six-dimensional evidence preservation
19. Trajectory/auditability preservation
20. Information-hierarchy result
21. Ranking/scoring non-introduction
22. Historical/synthetic separation
23. Acceptance packet status
24. Behavioral timing design
25. Comparative V0 baseline status
26. Human-operating-role representation
27. Architecture boundary result
28. What implementation establishes
29. What remains unproven
30. Exactly one recommended next action

Append unnumbered:
- Viewer path
- Acceptance packet path
- Artifact path
- Integrity/test result
- Commit SHA

Do not push.
