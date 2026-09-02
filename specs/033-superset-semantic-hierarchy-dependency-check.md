# Spec 033 — Superset Semantic-Hierarchy Dependency Check

## Status

Bounded RADAR discriminator.

Research-only. Do not contact actors, post publicly, modify Superset issues/PRs, build software, open pull requests, test code, or modify Spec 030.

---

## Context

Spec 032 identified Apache Superset SIP-225 as the strongest actor-observable candidate. It passed the actor, live-decision, consequence, recoverability, intervention-path, exposure-observability, effect-observability, and control-feasibility topology, but stopped one bounded uncertainty short of FORGE.

SIP-225 proposes author-configured hierarchical drill-down using chart-local `form_data`:

```text
drilldown_hierarchy: string[]
```

The proposal explicitly frames the sequencing question as:

```text
SHIP CHART-LOCAL NOW
vs
WAIT FOR DATASET / SEMANTIC-LAYER HIERARCHY SUPPORT
```

The live discussion already establishes a plausible migration model:

```text
chart-local hierarchy now
        ↓
dataset-level named hierarchy later
        ↓
semantic layer hydrates that interface
```

The remaining uncertainty is therefore not generic architecture design.

It is whether currently public Superset evidence makes that migration path concrete enough to materially resolve the sequencing decision.

---

## Primary question

> **Does currently public Superset architecture, code, issue, proposal, or roadmap evidence establish a concrete dataset/semantic-layer hierarchy interface or landing path sufficient to determine whether SIP-225 should ship chart-local now, ship with an explicit migration boundary, or wait?**

This is a discriminator, not an opportunity-discovery run.

---

## Decision model

The bounded decision has three possible resolution states:

### S1 — Ship chart-local unchanged

Appropriate if no concrete hierarchy dependency exists and the proposed `string[]` form-data representation is sufficiently isolated that future migration is low-risk.

### S2 — Ship now with explicit migration boundary

Appropriate if future dataset/semantic-layer hierarchy direction is concrete enough to anticipate, but not mature enough to justify waiting; the current design should preserve a deliberate adapter/reference boundary.

### S3 — Wait for dependency

Appropriate if a concrete hierarchy interface, issue/PR, or imminent landing sequence already exists and chart-local implementation would create avoidable short-lived rework or incompatible state.

Do not invent a fourth product strategy.

---

## Evidence scope

Inspect only public, authoritative or repository-native Superset evidence relevant to the dependency, including where useful:

- SIP-225 and its comments;
- SIP-182 or other semantic-layer proposals;
- open/closed Superset issues relating to semantic-layer metadata, dataset metadata, hierarchy, dimensions, metrics, semantic models, or reusable dataset-level concepts;
- linked pull requests;
- current Superset repository code where it reveals actual public interfaces or model shape;
- official Superset documentation;
- project roadmaps/discussions if repository-native and current.

Search may locate sources, but conclusions should prefer primary repository/docs evidence.

Do not broaden into general BI hierarchy research, competitor analysis, customer demand research, or market sizing.

---

## Exact dependency to resolve

Determine whether public evidence establishes any of the following:

1. a named hierarchy concept at dataset/semantic-model level;
2. an ordered reusable dimension path or equivalent abstraction;
3. a stable identifier/reference mechanism charts could point to instead of embedding raw column names;
4. a semantic-layer import/sync mechanism capable of supplying such hierarchy metadata;
5. a concrete issue/PR/implementation branch for hierarchy support;
6. an explicit landing sequence or release horizon;
7. an architectural contract that would make SIP-225's migration assumptions materially more or less credible.

Do not treat vague phrases such as "semantic-layer extensions are landing" as concrete dependency evidence unless linked to an identifiable interface, issue, PR, implementation, or committed sequence.

---

## Evidence classes

Classify each material finding as:

- **KNOWN CURRENT** — present in current code/docs;
- **CONCRETE IN FLIGHT** — issue/PR/proposal with identifiable interface and credible implementation path;
- **DIRECTIONAL** — architectural intent exists but interface/timing is unresolved;
- **SPECULATIVE** — inferred future design without project-native support;
- **ABSENT** — no relevant public evidence found after bounded search.

Do not collapse DIRECTIONAL into CONCRETE IN FLIGHT.

---

## Compatibility test

If a future hierarchy representation is found, compare it directly with SIP-225's current representation:

```text
CURRENT
chart form_data
→ drilldown_hierarchy: string[]
→ raw ordered column names

FUTURE
?<dataset / semantic hierarchy representation>
```

Evaluate only the migration-relevant dimensions:

- ownership location;
- identifier shape;
- ordered level representation;
- column/dimension reference semantics;
- rename/change behavior;
- reuse across charts;
- upstream semantic-layer hydration;
- whether chart interaction logic can remain independent of hierarchy source;
- whether saved chart state would require destructive migration;
- whether an adapter/reference layer could isolate the change.

Do not redesign Superset.

---

## Timing test

The decision is sequencing-sensitive.

For any dependency found, classify timing evidence:

- **IMMINENT** — active implementation/PR or clearly committed near-term landing;
- **PLAUSIBLE BUT UNBOUNDED** — concrete direction exists but no reliable landing horizon;
- **DISTANT / EARLY** — proposal-stage or prerequisite work remains substantial;
- **UNKNOWN** — public evidence cannot support timing.

Do not infer release timing from issue recency alone.

---

## Cheapest-stop principle

Stop research as soon as one of these becomes well-supported:

```text
A. concrete dependency makes chart-local sequencing substantially resolved;
B. direction exists but timing/interface remain too weak to justify waiting;
C. no concrete dependency exists after bounded primary-source search;
D. evidence is internally conflicting or too incomplete to classify.
```

Do not continue gathering decorative evidence once the decision state is stable.

---

## Time and cost envelope

Target active research time: **20 minutes**.

Hard active-time ceiling: **30 minutes**.

Incremental spend: **€0**.

No paid tools are authorized.

---

## Controls

- Public read-only research only.
- No GitHub comments, reactions, issue edits, PRs, or code submissions.
- No actor contact.
- No private identity resolution.
- No use of Spec 030 response state.
- No Superset implementation work.
- No claims of maintainer intent beyond cited public evidence.
- Unknown timing must remain UNKNOWN.

---

## Verdicts

### A — DEPENDENCY CONCRETE; RESOLUTION GAP COLLAPSES

Public evidence establishes a concrete hierarchy interface/implementation path and sequencing sufficiently well that an additional decision-resolution artifact would add little value.

State whether evidence favors S2 or S3 and kill the candidate if the exact job is already effectively resolved.

### B — DIRECTION CONCRETE, SEQUENCING STILL UNRESOLVED

Public evidence establishes a credible future hierarchy direction but not enough timing/interface certainty to settle ship-now versus wait.

The candidate may advance to a disposable sequencing resolution comparing S1/S2/S3.

### C — NO CONCRETE DEPENDENCY FOUND

Bounded primary-source research finds only directional or absent hierarchy dependency evidence.

This materially favors S1 or S2 over waiting and may justify a disposable resolution explaining why.

### D — INVALID / INSUFFICIENT EVIDENCE

The bounded search cannot reliably determine dependency state because evidence is inaccessible, contradictory, stale, or too incomplete.

Do not force a conclusion.

---

## FORGE advancement rule

Only B or C may advance to a future disposable resolution.

A kills the candidate because the residual resolution gap has collapsed.

D returns the uncertainty to RADAR with no actor interaction.

Spec 033 itself authorizes no FORGE interaction.

---

## Required artifact

Create:

`experiments/033/superset-semantic-hierarchy-dependency-check.md`

The artifact must preserve enough evidence to reconstruct:

- sources inspected;
- dependency findings;
- evidence classification;
- current versus future representation comparison;
- timing classification;
- exact-resolution implications;
- verdict;
- next action.

---

## Required completion report

Return exactly these sections:

1. Verdict
2. Primary question tested
3. Sources inspected
4. Current SIP-225 dependency claim
5. Dataset-level hierarchy evidence
6. Semantic-layer hierarchy evidence
7. Concrete issues / PRs / implementations found
8. Evidence classification table
9. Current-versus-future representation comparison
10. Migration-risk findings
11. Timing findings
12. Exact-resolution assessment
13. Decision state: S1 / S2 / S3
14. Strongest evidence for waiting
15. Strongest evidence for shipping now
16. What remains unknown
17. Research time and spend
18. What RADAR learned
19. Whether candidate advances to FORGE
20. Exactly one recommended next action

---

## Non-goals

Do not:

- search for new opportunity candidates;
- compare Superset with Tableau, Power BI, Looker, or other BI tools;
- estimate market size;
- evaluate willingness to pay;
- evaluate user demand beyond what is already present in SIP-225 context;
- design a new semantic-layer architecture;
- implement hierarchy support;
- write production code;
- create a PR;
- comment on SIP-225;
- contact maintainers;
- inspect Spec 030 response state;
- turn this into a broad Superset research project.

---

## Governing principles

> **One bounded uncertainty should receive one bounded experiment.**

> **A vague roadmap claim is not a dependency.**

> **Exact resolution can collapse an otherwise attractive opportunity.**

> **Do not research architecture when the decision can be resolved by checking whether the dependency actually exists.**

> **Unknown timing remains unknown.**

> **Stop when the sequencing state is decision-ready, not when the subject is exhausted.**
