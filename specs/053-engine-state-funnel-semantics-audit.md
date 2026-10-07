# Spec 053 — Engine-State and Funnel Semantics Audit

## Status
READY FOR EXECUTION

## Milestone
**Empirical Search Through Business Possibility Space — Engine-State Semantics**

## Type
Repository-only semantic/evidence audit. No UI implementation, fresh RADAR, external research, actor interaction, policy modification, production architecture, persistence migration, or automation.

## Baseline
Execute from synchronized main at or after the Experiment 052 published closure. Experiment 052 is CLOSED and its implementation remains frozen.

## Why this experiment exists
Experiments 051 and 052 established two bounded representation layers:

- Representation V0: **What does AE know?**
- Control V1: **What needs the human operator?**

Human acceptance of V1 exposed a higher-level information gap:

> **How is AE itself performing?**

The operator wants a truthful system-level view of detected opportunity flow, lifecycle distribution, attention demand, dormant inventory, blockage, and systemic bottlenecks.

The six curated 051/052 fixtures are not the complete AE opportunity population. A funnel built directly from them would therefore create false operational truth.

Before any Engine-level funnel UI is built, AE must establish what its repository evidence can actually support.

## Primary question
> Can AE reconstruct a truthful, non-misleading Engine-level opportunity funnel from existing repository evidence—and, if so, what exactly are the identities, stages, transitions, distributions, and evidence limits that the Control Plane may legitimately display?

## Secondary question
Does the repository preserve enough sidelined/rejected opportunity history to support an **Opportunity Memory** in which contingent opportunities can later be re-evaluated when blockers change?

## Core semantic distinctions
The audit must not assume equivalence among:

- signal;
- raw signal;
- candidate;
- qualifying candidate;
- opportunity;
- resolution gap;
- resolution;
- experiment;
- interaction;
- transaction;
- lifecycle state;
- operational/control state.

One opportunity may produce multiple experiments.
Multiple signals may refer to one opportunity.
One experiment may examine multiple candidates.
A reactivated opportunity should not automatically become a new opportunity identity.
A terminal thesis invalidation differs from a contingent blocker.

## Evidence horizon
Use repository evidence through Experiment 052.

Start with:
- README.md
- ROADMAP.md
- docs/OPERATING_MODEL.md
- docs/OPPORTUNITY_MODEL_001_035.md
- docs/ECONOMIC_TELEMETRY_BASELINE_001_035.md
- Experiments 013–052 where relevant
- specifications where experiment artifacts are insufficient
- current SQLite/schema/source only to determine what structured operational data already exists, not to modify it

Prefer targeted reconstruction over exhaustive archaeology.

## Evidence discipline
For every material count or semantic claim label support as:
- RECORDED
- DERIVED
- ESTIMATED
- UNKNOWN

Do not create false precision.

A count is displayable as current Engine truth only when:
1. the population definition is explicit;
2. the evidence horizon is explicit;
3. identity/deduplication semantics are supportable;
4. state semantics are supportable;
5. known missingness does not make the number misleading.

Otherwise classify it as historical/sample/partial/UNKNOWN.

## Required identity audit
Determine whether AE currently has a durable concept of:

### Signal identity
What makes two observations the same/different signal?

### Candidate identity
When does a signal become a candidate, and can the same candidate recur?

### Opportunity identity
What stable logical object should survive multiple experiments, observations, blockers, and reactivation?

### Experiment identity
Preserve existing experiment identity as evidence history, not opportunity identity.

Assess whether current repository evidence supports a stable opportunity identity without implementing one.

## Required state audit
Distinguish at minimum:

### Evidence/progression state
What has actually been established:
- observed signal;
- candidate;
- qualified/survived;
- resolution gap;
- resolution-ready;
- actor/decision effect;
- economic effect;
- exchange/WTP;
- transaction;
- repeatability;
- value capture.

This need not be a mandatory linear pipeline.

### Opportunity lifecycle state
Use 051's experimental vocabulary as evidence:
- ACTIVE
- DORMANT
- REVIEW
- TERMINAL

Audit whether these states remain coherent at Engine level.

### Operational/control state
Use 052 only as representation evidence:
- attention;
- waiting;
- blocked/no action;
- progressing/no action;
- authorization/decision/review needs.

Do not collapse lifecycle and operational state.

## Terminal versus contingent disposition
Audit historical rejection/kill reasons and classify whether they are conceptually:

### Structural / terminal
The opportunity thesis or residual gap is invalidated in a way that should not normally reactivate without a materially new thesis.

Examples may include exact adequate resolution or non-material consequence, if evidence supports that interpretation.

### Contingent / dormant
The opportunity may remain valid but is currently blocked by changeable external state such as:
- actor access;
- regulation;
- platform capability;
- technology;
- data;
- price/cost;
- timing;
- control feasibility.

### Review / unresolved
Evidence is insufficient to classify terminal versus dormant.

Do not rewrite historical experiment verdicts. This is a semantic audit over them.

## Opportunity Memory audit
Determine whether historical experiments preserve enough information to reconstruct for sidelined opportunities:

- stable referent/name;
- original signal;
- opportunity thesis;
- disposition;
- disposition reason;
- evidence;
- blocker;
- whether blocker is contingent;
- reactivation condition;
- last evidence horizon;
- experiment history.

Classify repository recoverability of Opportunity Memory as:
- STRONG
- PARTIAL
- WEAK
- UNKNOWN

Identify what information was historically discarded or inconsistently recorded.

Do not build a database or memory system.

## Funnel semantics
Do not assume a conventional linear sales funnel.

Test whether AE is better represented as:
- funnel;
- state distribution;
- branching search tree;
- portfolio state machine;
- evidence frontier;
- combination of these.

The desired Engine layer must answer useful system questions without implying false conversion semantics.

At minimum evaluate whether it can truthfully answer:

- How many signals were observed in a defined horizon?
- How many candidates were generated?
- How many survived fatal gates?
- How many became material opportunities?
- How many are ACTIVE / DORMANT / REVIEW / TERMINAL?
- How many reached decision-ready resolution?
- How many reached actor/decision effect?
- How many reached economic effect?
- How many reached exchange/WTP?
- How many reached transaction?
- How many reached repeatability/value capture?
- How many currently need human attention?
- What blocker classes dominate?
- Where does evidence accumulate or terminate?

For each, classify:
- CURRENTLY DISPLAYABLE
- DISPLAYABLE WITH EXPLICIT PARTIAL/HISTORICAL LABEL
- NOT CURRENTLY SUPPORTABLE

## Counting rules
Explicitly test:
- whether counts should be unique opportunities, observations, candidates, or experiments;
- whether an opportunity appears in one stage or multiple evidence states;
- whether terminal/dormant are mutually exclusive with evidence frontier;
- whether reactivation changes historical counts;
- whether repeated RADAR discovery should deduplicate;
- whether curated UI fixtures can ever be used for system counts (presumptive answer: no);
- how evidence horizons should be shown.

Do not implement counting logic.

## Efficiency semantics
The human wants to know whether the funnel is working efficiently.

Audit which metrics are meaningful and which would be misleading.

Potentially meaningful descriptive metrics:
- stage/state distributions;
- disposition-reason distribution;
- blocker distribution;
- dormant inventory;
- reactivation candidates;
- evidence-frontier distribution;
- time in state where recorded;
- opportunity throughput over a defined horizon;
- attention load.

Potentially misleading without stronger semantics:
- generic conversion rate;
- one synthetic funnel percentage;
- aggregate opportunity score;
- “success rate” across heterogeneous experiment types.

Do not create a composite efficiency score.

## Historical reconstruction
Attempt a bounded reconstruction of the repository's opportunity inventory.

The goal is not perfect historical completeness. The goal is to determine what can be truthfully represented.

Produce:
1. a high-confidence inventory where opportunity identity is supportable;
2. a partial/ambiguous inventory where identity is uncertain;
3. known missingness.

Include the six 051/052 fixtures but do not privilege them as the full population.

## Regulatory/reactivation learning
Specifically inspect whether historical evidence supports the earlier hypothesis that opportunities blocked by regulatory or other contingent constraints should be preserved for future re-evaluation.

Determine whether any past opportunity has:
- contingent regulatory/control/access blocker;
- explicit or reconstructable reactivation condition;
- evidence worth preserving.

Do not perform current external regulatory checks.

## Discrimination-learning potential
Assess whether retained historical dispositions could eventually answer:
- which gates produce durable terminal rejections;
- which gates mostly produce contingent dormancy;
- which blocker classes later reopen;
- whether discrimination policy improves over time.

This is future learning potential only. Do not infer empirical gate accuracy without longitudinal evidence.

## Engine-layer information architecture
If evidence supports an Engine layer, define only its semantic contract, not UI.

It should potentially distinguish:

1. **ENGINE** — flow/distributions/systemic bottlenecks.
2. **CONTROL** — what needs human attention.
3. **POSSIBILITY SPACE** — opportunity lifecycle + distance to value capture.
4. **EVIDENCE** — provenance + trajectory.

Determine whether 053 supports, refines, or rejects this four-level hypothesis.

## Implementation gate
A later funnel/Engine-state UI experiment is earned only if:
1. at least a useful subset of system-level semantics is supportable;
2. population/evidence-horizon limits can be made explicit;
3. the representation would not imply false completeness;
4. lifecycle/evidence/control states can remain distinct;
5. the Engine layer would answer a real operator question exposed by 052.

If the repository cannot support truthful counts, the next step should be data-contract/evidence-capture repair rather than UI.

## Software gate
DO NOT BUILD in 053.

No:
- funnel UI;
- opportunity database;
- migrations;
- identity service;
- event store;
- dashboard;
- monitoring;
- reactivation automation;
- scheduler;
- scoring/ranking;
- autonomous portfolio management.

## Protocol observation
The recent operating-protocol test exposed one additional invariant:

**RECOVERY ≠ EXECUTION.**

A request to inspect, reconcile, recover, or report the next permitted operation does not authorize performing that operation.

Record this as protocol-alignment candidate only. Do not modify protocol files in 053.

## Explicit prohibitions
Do NOT:
- use live web research;
- contact actors;
- run RADAR;
- create fresh opportunities;
- modify prior experiments;
- modify 051/052 frozen artifacts;
- modify living docs;
- modify protocol docs;
- implement UI/software/schema;
- invent missing opportunity identities;
- infer current regulatory state from historical evidence.

## Budget
Target active work: 20–40 minutes.
Hard ceiling: 60 active minutes.
External spend: €0.
Use prospective timing.

Stop early when:
- identity semantics are clear enough for the audit;
- supportable versus unsupported Engine metrics are classified;
- Opportunity Memory recoverability is classified;
- the implementation gate is decisive;
- further archaeology is unlikely to change the conclusion.

## Verdicts

### A — ENGINE-STATE SEMANTICS SUFFICIENT; UI TEST EARNED
Repository evidence supports a bounded truthful Engine layer with explicit horizons/limits, and a later representation experiment is justified.

### B — PARTIAL SEMANTICS; DATA-CONTRACT REPAIR FIRST
The Engine-layer concept is valid, but current evidence cannot support key counts/identities without misleading completeness. Repair evidence capture/identity semantics before UI.

### C — ENGINE-LAYER HYPOTHESIS NOT YET USEFUL
System-level representation adds little beyond existing Control/Possibility/Evidence layers or cannot answer meaningful operator questions.

### D — EVIDENCE INSUFFICIENT
Historical repository evidence is too incomplete/ambiguous to distinguish the required semantics.

### E — INVALID
Scope, isolation, timing, evidence, or repository integrity violated.

## Required artifact
Create only:
- experiments/053/engine-state-funnel-semantics-audit.md

STATUS.md may be updated mechanically according to the operating protocol. No other file may change.

## Repository integrity
Before completion:
- prior experiments unchanged;
- 051/052 frozen artifacts unchanged;
- living/protocol docs unchanged;
- production source/tests/schema unchanged;
- no external action;
- git diff --check passes;
- existing tests pass if available.

Commit the 053 artifact and permitted STATUS transition locally. Do not push.

## Required completion report
Return exactly:

1. Verdict
2. Repository baseline
3. Active time and timing method
4. Spend
5. Isolation confirmation
6. Evidence horizon and reconstruction quality
7. Signal identity finding
8. Candidate identity finding
9. Opportunity identity finding
10. Experiment-versus-opportunity finding
11. Evidence/progression-state finding
12. Lifecycle-state finding
13. Operational/control-state finding
14. Terminal-versus-contingent disposition finding
15. Opportunity Memory recoverability
16. High-confidence opportunity inventory
17. Ambiguous/partial inventory
18. Known historical missingness
19. Funnel-versus-state-model finding
20. System-count supportability matrix
21. Blocker/disposition distribution finding
22. Dormant/reactivation finding
23. Regulatory-reactivation finding
24. Efficiency-metric finding
25. Discrimination-learning potential
26. Four-level information-architecture assessment
27. Engine-layer semantic contract
28. Data-contract gaps
29. Later UI experiment gate
30. Software/non-build disposition
31. Protocol-alignment candidate
32. What the audit establishes
33. What remains unproven
34. Exactly one recommended next action

Append unnumbered:
- Artifact path
- Integrity/test result
- Commit SHA

Do not push.
