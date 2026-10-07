# Spec 054 — Opportunity Identity and Evidence-Contract Repair

## Status
READY FOR EXECUTION

## Milestone
Empirical Search Through Business Possibility Space — Opportunity Identity V0

## Type
Bounded repository-only manual data-contract experiment on an explicitly limited historical cohort. No production schema, database, UI, automation, fresh RADAR, external research, actor interaction, or canonical-model modification.

## Baseline
Execute from synchronized canonical main at or after the published Experiment 053 closure (50452b8 short ref).

## Why this experiment exists
Experiment 053 found that AE can reconstruct useful historical opportunity trajectories but cannot truthfully present complete Engine-level counts because identity, admission, deduplication, dated state, and missingness semantics are incomplete.

The next step is not to build a database. Test whether one small manual contract can represent known opportunities faithfully enough to support future Engine accounting without inventing historical truth.

## Primary question
Can a bounded cohort of historically well-understood opportunities be represented under one stable identity/evidence contract that preserves family-versus-decision-instance distinction, evidence trajectory, lifecycle, dormancy/reactivation, control state, provenance, and missingness without rewriting history?

## Secondary question
Does the tested contract distinguish a rediscovered opportunity family, a new decision instance, and new evidence about an existing instance without double-counting signals or experiments?

## Cohort
Use exactly:
1. Cocoa 013→014
2. EV smart charging / compatibility 019→020
3. Canadian counter-tariff 023→027
4. Customized CRM 028→030
5. Superset hierarchy 032→035
6. Realtime migration 046→048

Do not add a seventh case.

## Evidence horizon
Repository evidence only through Experiment 053 and each chain's recorded historical horizon. Use Experiment 053 audit/review, Experiment 051 fixtures/result for bounded derived interpretations, original chain evidence where needed, and Experiment 050 for economic-frontier distinctions. Do not refresh external state.

## Core identity hypothesis
Test two levels:

### Opportunity Family
A recurring economic asymmetry / job / resolution thesis that may appear across multiple actors or decision events.

### Decision Instance
A scoped actor + decision object + decision horizon/event to which evidence and interventions can attach.

This is a hypothesis, not canonical ontology. Do not force both levels where evidence cannot support them.

## Non-equivalences
Preserve:
SIGNAL ≠ CANDIDATE ≠ OPPORTUNITY FAMILY ≠ DECISION INSTANCE ≠ EXPERIMENT
LIFECYCLE STATE ≠ EVIDENCE FRONTIER ≠ OPERATIONAL/CONTROL STATE
REACTIVATION ≠ NEW IDENTITY unless actor/decision/thesis semantics require a new instance.

## Required contract fields
Test the smallest manual contract capable of expressing where supported:

### Identity
- stable local referent
- family label/thesis
- decision-instance label
- actor/decision owner
- decision object
- decision horizon
- identity confidence/status
- same-as / new-instance / unresolved relationship

### Lineage
- originating signals
- candidate/run-local referents
- experiment history
- parent/related opportunity where supportable

### Admission
- whether/when admitted as an opportunity for this bounded cohort
- rationale/evidence/horizon
- UNKNOWN where historical admission was never recorded

### Evidence frontier
Independent states: signal observed; candidate formed; residual gap; decision-ready resolution; delivery; exposure; semantic/decision effect; downstream action; economic effect; WTP/exchange; transaction; repeatability; value capture. Do not force a linear pipeline.

### Lifecycle
ACTIVE / DORMANT / REVIEW / TERMINAL where supportable; effective evidence horizon; reason; RECORDED versus DERIVED.

### Control state
Only where historically supportable: action/attention requirement; authorization; waiting/blocking condition; NO CURRENT EVIDENCE where current control state cannot be known. Never import synthetic 052 scenarios as history.

### Blocker/reactivation
Blockers; structural/contingent/unresolved; reactivation condition; freshness checks; whether reactivation preserves instance or requires a new one.

### Roles/economics
Decision actor; beneficiary; buyer; payer; economic consequence; exchange path; preserve UNKNOWN.

### Provenance/missingness
Evidence links; horizon; RECORDED / DERIVED / ESTIMATED / UNKNOWN; known missing fields; ambiguity note.

## Identity stress tests
The contract must answer:
1. Another company faces customized CRM migration: same family, new instance?
2. Same actor receives new evidence before same decision closes: new opportunity or same instance evidence?
3. Old decision window closes and a new consultation/regulatory window opens: new instance?
4. Exact adequate resolver disappears/materially changes: can old terminal thesis be reconsidered without rewriting old verdict?
5. Dormant blocker clears: reactivate same instance or freshness/new-instance requirement?
6. RADAR rediscovers same family through another source: link signal without increasing unique-opportunity counts by default?
7. Identity undecidable: preserve UNRESOLVED without guessing?

## Counting stress test
For only the six-record cohort, test truthful counts of:
- represented families;
- represented decision instances;
- unresolved identity relationships;
- lifecycle distribution at explicit horizons;
- evidence-frontier distribution;
- terminal versus contingent blockers;
- dormant records with explicit reactivation conditions;
- records with identifiable buyer/payer versus UNKNOWN.

Every count states unit, cohort, horizon, derivation, and missingness. Never present these as Engine totals.

## Opportunity Memory test
For each case test whether the contract preserves enough to recognize it later, understand why it stopped/continued, see learning and unknowns, identify reactivation evidence, avoid rerunning settled research, and preserve old verdicts while accepting new evidence. Classify STRONG / PARTIAL / WEAK, then overall cohort result.

## Auditability requirement
Every material state traces to repository evidence or is explicitly DERIVED/UNKNOWN. Do not upgrade interpretation to fact.

## Minimality challenge
Keep a field only if it prevents double counting, preserves auditability, supports lifecycle/reactivation, supports truthful Engine accounting, distinguishes family/instance, or prevents material ambiguity in a cohort case. Do not design an enterprise data model.

## Prospective-use thought experiment
Without fresh RADAR, classify only the semantics of:
A. Same CRM family, new company/decision.
B. Same realtime actor, same migration decision, new actor-supplied matrix.
C. Canadian tariff family, new importer after historical decision horizon.
D. EV exact resolver materially disappears/changes.
E. Existing dormant opportunity receives a new signal but blocker remains.

For each: new family / new instance / new evidence / reactivation candidate / unresolved. Do not claim events occurred.

## Data-contract output
May create a manual Markdown/JSON/YAML fixture only under experiments/054/. Prefer simplest human-readable representation. No production schema.

## Engine-accounting readiness
Assess whether the contract prospectively supports truthful family counts, decision-instance counts, lifecycle distributions, evidence-frontier distributions, blocker/reactivation distributions, buyer/payer visibility, and trajectories. Classify READY FOR PROSPECTIVE CAPTURE / NEEDS FURTHER SEMANTIC WORK / NOT EARNED. Do not claim historical completeness.

## Historical backfill disposition
Decide among: backfill all now; backfill selected high-confidence chains; start prospectively and preserve old history as partial; defer backfill. Prefer smallest justified action.

## UI gate
No Engine UI implementation. A later Engine-state representation experiment is earned only if the contract survives all six cases without material invention; handles or safely preserves unresolved family/instance identity; produces truthful bounded counts; preserves provenance/missingness; supports prospective capture; and remains coherent without production software.

## Software gate
DO NOT BUILD. No database, schema migration, identity service, event store, dashboard/funnel, reactivation monitor, dedup engine, scoring, automation, or production Opportunity model.

## Protocol observation
Preserve the separately alignable finding: RECOVERY ≠ EXECUTION. Do not modify protocol files.

## Explicit prohibitions
No live web; RADAR; actor contact; fresh real opportunities; prior-experiment changes; 051/052/053 changes; living/protocol changes; production source/test/schema changes; invented timestamps/actors/payers/admissions/identities; DERIVED→RECORDED upgrades; or backfill beyond cohort.

## Budget
Target 20–40 active minutes; hard ceiling 60; external spend €0; prospective timing. Stop early when fields stabilize, all six cases are represented or decisively fail, identity/counting stress tests are decisive, and readiness/UI gate is decisive.

## Verdicts
A — MANUAL IDENTITY/EVIDENCE CONTRACT VALIDATED: faithfully represents all six, preserves uncertainty/provenance, survives identity/counting tests, sufficient for prospective Engine accounting; later Engine representation may be earned.
B — PARTIAL CONTRACT; ONE BOUNDED REPAIR NEEDED: directionally sound but one material semantic remains unresolved.
C — CONTRACT OVERCOMPLEX / NOT JUSTIFIED.
D — HISTORICAL EVIDENCE TOO WEAK.
E — INVALID.

## Required artifacts
Create only under experiments/054/:
- opportunity-identity-evidence-contract-test.md
- one manual cohort fixture if useful (.json, .yaml, or .md)

STATUS.md may be mechanically updated. No other files may change.

## Repository integrity
Prior experiments/frozen evidence/living/protocol docs/production source/tests/schema unchanged; no external action; git diff --check and existing tests pass. Commit permitted 054 artifacts and mechanical STATUS transition locally. Do not push.

## Required completion report
Return exactly:
1. Verdict
2. Repository baseline
3. Active time and timing method
4. Spend
5. Isolation confirmation
6. Contract format
7. Minimal field set
8. Opportunity-family semantic result
9. Decision-instance semantic result
10. Signal/candidate/opportunity/experiment separation
11. Admission semantic result
12. Evidence-frontier result
13. Lifecycle-state result
14. Control-state result
15. Blocker/reactivation result
16. Role/buyer/payer result
17. Provenance/missingness result
18. Cocoa representation result
19. EV representation result
20. Canadian representation result
21. CRM representation result
22. Superset representation result
23. Realtime representation result
24. Identity stress-test result
25. Counting stress-test result
26. Opportunity Memory result
27. Prospective-use thought experiment
28. Engine-accounting readiness
29. Historical-backfill disposition
30. UI gate
31. Software/non-build disposition
32. Protocol observation
33. What the experiment establishes
34. What remains unproven
35. Exactly one recommended next action

Append unnumbered: Artifact paths; Integrity/test result; Commit SHA.

Do not push.
