# Spec 051 — Opportunity Distance Representation Test

## Status
READY FOR EXECUTION

## Milestone
**Empirical Search Through Business Possibility Space — Representation V0**

North-star hypothesis:

> AE can be understood as an empirical search algorithm over business possibility space, progressively collapsing uncertainty between observed asymmetries and legitimate repeatable value capture.

This is a milestone hypothesis, not yet canonical architecture.

## Type
Bounded repository-only representation + static operator-UI experiment using historical evidence. No fresh RADAR, actor contact, monetization, policy change, autonomous scoring, or production architecture.

## Baseline
Execute from synchronized `main` at or after `0f72b7b94e40a5ad97087dc5b0ad4a8c707c2b54`.

## Why this experiment exists

After Experiment 050, AE has accumulated enough opportunity, interaction, economic-frontier, regulatory/control, and dormant-state concepts that linear Markdown alone may be becoming a cognitive bottleneck for the human operator.

The proposed UI is not decoration. It is a candidate representation of the observable state of AE's search process: **open AE and see what AE knows, what it does not know, what is blocked, and what observation could move an opportunity closer to legitimate value capture.**

The experiment tests the representation before it is allowed to influence fresh opportunity selection.

## Primary question

Can a small opportunity-first representation and static control-plane UI faithfully encode historical AE evidence while making the Engine's current business-search state materially easier for the operator to comprehend and navigate than experiment-centric Markdown alone?

## Secondary questions

1. Can opportunity identity remain stable while experiments become historical events attached to it?
2. Can six independent uncertainty dimensions represent distance to legitimate value capture without false precision?
3. Can `UNKNOWN`, `BLOCKED`, `DORMANT`, and terminal thesis failure remain visibly distinct?
4. Can regulatory feasibility be represented without treating “regulated” as “bad”?
5. Can reactivation conditions preserve opportunities that are right at the wrong time?
6. Does the representation expose the next discriminator without pretending to rank automatically?
7. Does a UI materially improve operator comprehension enough to justify a later search-space navigation milestone?

## Opportunity-first object

For this experiment, the UI's primary object is an **Opportunity**, not an Experiment.

Experiments remain immutable evidence/history:

```text
Opportunity
  ├── current evidence state
  ├── distance vector
  ├── blocker / next discriminator
  ├── status
  ├── reactivation condition if dormant
  └── experiment history → immutable artifacts
```

Do not rewrite historical experiments to fit the representation.

## Six-dimensional distance vector

Represent these independent dimensions:

### Resolution distance
Can AE construct a resolution that materially reduces the decision uncertainty?

Includes technical/data/reasoning feasibility where relevant.

### Access distance
Can AE legitimately reach the actor, buyer, required data/system, or distribution surface needed to validate/capture value?

Permission is not access; access is not exposure.

### Adoption distance
How much behavioral, organizational, technical, switching, integration, or workflow change separates the resolution from realized use/value?

### Control distance
Can AE legitimately test or execute the next step under authorization, platform, privacy, safety, operational, and project-control constraints?

### Regulatory distance
What legal/licensing/compliance/regulatory uncertainty or obligation separates the opportunity from a legitimate test/value-capture path?

Regulation may create asymmetry/value. `REGULATED` is not itself a negative state.

### Economic distance
What evidence layers remain before observable exchange/captured value: payer/buyer, budget/spend, exchange mechanism, economic effect, WTP behavior, transaction, repeatability, capture?

## No numeric scoring

Do NOT assign 0–100 scores, weighted totals, rankings, composite distance, or synthetic opportunity scores.

Each dimension must expose categorical evidence state plus uncertainty/evidence.

Use the smallest useful vocabulary. Candidate default:

- `NEAR`
- `MEDIUM`
- `FAR`
- `BLOCKED`
- `UNKNOWN`

If repository evidence proves this vocabulary misleading, adapt minimally and document why.

`UNKNOWN` must never silently become `FAR` or `BLOCKED`.

## Per-dimension fields

Represent where supported:
- state;
- evidence summary;
- evidence class: `RECORDED / DERIVED / ESTIMATED / UNKNOWN`;
- next discriminator;
- discriminator active-cost estimate if supported;
- expected latency if supported;
- blocker;
- reactivation condition if contingent.

Do not fill absent fields with invention.

## Opportunity lifecycle state

Test a small lifecycle vocabulary separating structural failure from contingent blockage. Candidate default:

- `ACTIVE`
- `DORMANT`
- `TERMINAL`
- `REVIEW`

Definitions:
- `ACTIVE`: valid and currently progressable.
- `DORMANT`: currently blocked by a plausibly changeable external condition.
- `TERMINAL`: thesis materially invalidated under current evidence, not merely inconvenient.
- `REVIEW`: evidence insufficient to classify safely.

Do not convert all historical `KILL` dispositions to terminal. Preserve the original disposition and derive lifecycle state cautiously.

## Regulatory/control feasibility vocabulary

Where useful preserve:
- `CLEAR`
- `BOUNDED`
- `REVIEW REQUIRED`
- `BLOCKED`
- `ILLEGAL`
- `UNKNOWN`

Only use `ILLEGAL` when repository evidence explicitly establishes prohibition. Do not perform new legal research or infer illegality.

## Historical opportunity fixtures

Encode 4–6 historically well-understood opportunity chains, selected for representational diversity rather than favorable appearance.

Must include if evidence permits:
- CRM / 028→030;
- Superset / 032→035;
- Realtime migration / 046→048;
- Canadian tariff / 023→027;
- Cocoa / 013→014.

A sixth may be included only if it adds a materially different lifecycle/distance pattern.

Use repository evidence only.

## Representation fidelity requirement

For every fixture:
1. cite/source the experiment artifacts used;
2. preserve uncertainty;
3. distinguish historical state from current derived representation;
4. do not claim live-world freshness beyond the experiment horizon;
5. preserve decision actor vs buyer/payer distinction;
6. preserve decision effect vs economic effect vs value capture;
7. preserve authorization/access/exposure distinctions;
8. preserve regulatory UNKNOWN when not researched.

The UI must visibly communicate that it is rendering **repository-known state**, not omniscient current reality.

## Static Control Plane V0

Build the smallest local static viewer that makes the representation inspectable.

Required views:

### 1. Opportunity overview
Show all fixtures with at minimum:
- name;
- lifecycle state;
- significance/consequence summary;
- six-dimensional categorical vector;
- dominant current blocker/unknown;
- next discriminator if supported;
- last evidence horizon / experiment IDs.

### 2. Opportunity detail
For one selected opportunity show:
- thesis / decision;
- actor / beneficiary / buyer-payer distinctions;
- six dimensions with evidence and uncertainty;
- current blocker;
- next discriminator;
- reactivation condition where relevant;
- experiment history/timeline;
- explicit unproven claims.

### 3. Dormant / terminal distinction
The UI must make contingent dormancy visually/semantically distinct from terminal invalidation.

### 4. “What AE knows” framing
The page should make obvious:
- known evidence;
- unknowns;
- blockers;
- next observations;
- historical evidence provenance.

## UI constraints

- Local/static only.
- Prefer existing project language/runtime and minimal dependencies.
- No backend service unless absolutely required by existing architecture.
- No authentication.
- No deployment.
- No external APIs.
- No database migration.
- No new generic Opportunity Engine.
- No automatic scoring/ranking.
- No LLM inference at render time.
- No monitoring/notifications.
- No actor interaction.
- No monetization controls.
- No polished product-design detour.

The viewer may use fixture JSON/YAML/Markdown or another minimal structured representation. Choose the smallest reversible implementation.

## Operator-comprehension test

The implementation is not successful merely because it renders.

Produce a bounded comparison packet enabling the human operator to answer from the UI, without rereading full historical artifacts:

1. Which opportunity is currently closest to a legitimate economic discriminator, based on represented evidence only?
2. Which opportunity is blocked primarily by access?
3. Which opportunity reached actor decision-state effect but remains economically distant?
4. Which opportunities are dormant rather than terminal, and what would reactivate them?
5. For each opportunity, what is the largest UNKNOWN or blocker?
6. What experiment/evidence produced the current representation?

Do NOT answer these by automated ranking. The operator should infer them from the representation.

Create an acceptance packet with screenshots or a locally inspectable viewer path and a concise evidence-fidelity checklist. Human acceptance/rejection happens in a later turn; do not fabricate operator feedback.

## Architecture boundary

This experiment may create only the minimum representation/viewer needed for V0.

It does NOT earn or authorize:
- canonical Opportunity database;
- opportunity persistence architecture;
- automatic migration of historical experiments;
- automated distance inference;
- scoring engine;
- prioritization engine;
- reactivation monitor;
- event bus;
- scheduler;
- autonomous agents;
- customer-facing product UI.

If the representation is useful, later experiments decide what becomes durable architecture.

## Milestone interpretation

If successful, record that AE has earned the **Representation V0** step of the milestone:

> Empirical Search Through Business Possibility Space

Do not claim the milestone is complete. Later stages may include fresh distance-aware selection, search-space navigation, reactivation, and eventually automation.

## Explicit prohibitions

Do NOT:
- use live web research;
- update historical evidence from current reality;
- contact actors;
- run fresh RADAR;
- change opportunity-selection policy;
- change Operating Model/README/ROADMAP/ARCHITECTURE;
- modify prior experiments;
- invent buyer/payer/regulatory states;
- score/rank opportunities numerically;
- build production infrastructure.

## Budget

Target active work: 30–60 minutes. Hard ceiling: 90 minutes. Spend: €0. Use prospective timing.

Stop if the representation cannot be populated without material invention, if UI scope requires broad architecture, or when V0 + acceptance packet are complete.

## Verdicts

### A — REPRESENTATION V0 EARNED
Historical opportunities can be represented faithfully across the six dimensions and the static control plane is decision-usable enough to proceed to human acceptance.

### B — PARTIAL REPRESENTATION; ABSTRACTION NEEDS REFINEMENT
The UI is useful but one or more dimensions/lifecycle concepts materially distort evidence or fail to support operator reasoning.

### C — UI USEFUL, DATA MODEL NOT EARNED
The visual representation helps, but durable opportunity semantics remain too weak/ambiguous for structured adoption.

### D — REPRESENTATION NOT USEFUL
Markdown/history remains materially clearer or the abstraction adds complexity without decision benefit.

### E — INVALID
Scope, evidence, implementation, timing, or integrity controls were violated.

## Required files

Permitted changes only:
- minimal structured historical fixtures under `experiments/051/`;
- static viewer assets under `experiments/051/viewer/`;
- `experiments/051/opportunity-distance-representation-test.md`;
- `experiments/051/acceptance-packet.md`;
- screenshots under `experiments/051/` if generated.

Do not modify existing application/source architecture for this experiment unless SPEC-051 is first amended by a separate decision.

## Integrity

Run `git diff --check` and existing tests. Verify all changes are confined to `experiments/051/`. Commit locally. Do not push.

## Required completion report

Return exactly these 30 sections:
1. Verdict
2. Repository baseline
3. Active time and timing method
4. Spend
5. Isolation confirmation
6. Historical opportunities encoded
7. Fixture/representation format
8. Opportunity lifecycle vocabulary result
9. Six-dimensional vocabulary result
10. Resolution-distance findings
11. Access-distance findings
12. Adoption-distance findings
13. Control-distance findings
14. Regulatory-distance findings
15. Economic-distance findings
16. UNKNOWN preservation result
17. Dormant-versus-terminal result
18. Reactivation-condition result
19. Decision-actor versus buyer/payer result
20. Evidence-provenance result
21. Viewer implementation summary
22. Opportunity overview result
23. Opportunity detail result
24. “What AE knows” result
25. Operator-comprehension packet status
26. Architecture-boundary result
27. Milestone status
28. What remains unproven
29. Repository-integrity result
30. Exactly one recommended next action

After section 30 append unnumbered:
- Viewer path
- Acceptance packet path
- Artifact path
- Commit SHA

Do not push.