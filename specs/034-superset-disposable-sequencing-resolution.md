# Spec 034 — Superset Disposable Sequencing Resolution

## Status

FORGE resolution-construction experiment.

Research and synthesis only. Do not contact any actor, post to GitHub, react to issues, open or modify pull requests, write implementation code, or modify Spec 030.

---

## Context

Spec 032 produced one actor-observable candidate with one bounded unresolved dependency: Apache Superset SIP-225, proposing author-configured hierarchical drill-down.

Spec 033 resolved that dependency far enough to move the candidate from RADAR to FORGE:

- Superset has a concrete semantic-layer substrate.
- SIP-225 has a concrete chart-local implementation in PR #41907 using `drilldown_hierarchy: string[]`.
- Project-native discussion anticipates centrally owned named hierarchies and semantic-layer hydration.
- No current hierarchy contract, hierarchy-specific implementation, committed landing sequence, milestone, or release horizon was found.
- Therefore waiting for future hierarchy support is not evidence-supported today.
- Shipping chart-local without any migration seam is also weaker than necessary because the future ownership direction is already visible.

The current decision state is:

```text
S1 — ship chart-local representation unchanged
S2 — ship now with an explicit migration boundary
S3 — wait for dataset/semantic-layer hierarchy contract
```

Spec 033 concluded that **S2 is the strongest current resolution**, but did not define the minimal boundary needed to make that recommendation useful.

Spec 034 is the first FORGE step for this candidate.

---

## Primary question

> **Can the existing evidence be compressed into a defensible, decision-ready sequencing resolution that explains why S2 dominates S1/S3 and defines only the smallest migration boundary needed to preserve future hierarchy ownership?**

This is not an architecture-design exercise.

The objective is to produce the smallest resolution that could plausibly change or clarify the SIP author's decision.

---

## Hypothesis

A useful disposable resolution can be produced without inventing Superset's future semantic-layer contract if it separates:

```text
HIERARCHY SOURCE
      ↓
RESOLUTION TO ORDERED LEVELS
      ↓
DRILL INTERACTION
```

The current implementation may use chart-local `string[]` as one source, while a future dataset/semantic-layer reference can become another source without changing the interaction contract.

The hypothesis is specifically that **source ownership can remain replaceable while the interaction consumes a stable minimal resolved shape**.

Do not assume this hypothesis is correct. Attempt to falsify it.

---

## Decision owner and decision

Decision context:

- **Actor:** SIP-225 proposal author and Superset maintainers/community participating in SIP review.
- **Decision:** whether to ship the chart-local hierarchy implementation now, modify it before shipping, or wait for future hierarchy primitives.
- **Current candidate resolution:** S2 — ship now with a minimal migration/source boundary.

Do not broaden into whether hierarchical drill-down should exist at all unless current evidence directly invalidates the premise.

---

## Evidence baseline

Treat Spec 033 as the primary evidence baseline.

Use only enough fresh public source checking to verify claims required by the resolution.

Do not reopen broad repository discovery.

Key established evidence:

1. SIP-225's current representation is chart-local ordered raw column names.
2. The interaction layer is conceptually separable from hierarchy ownership.
3. Project discussion expects reusable dataset-level hierarchy ownership and possible semantic-layer hydration.
4. No stable future hierarchy contract currently exists.
5. No timing evidence justifies waiting.
6. Future identity, sync, precedence, validation, rename behavior, migration rules, provider representation, and ownership remain unknown.

Any contradiction found during Spec 034 overrides this baseline and must be reported.

---

## Required S1 / S2 / S3 comparison

Construct a compact decision table comparing exactly these three options.

### S1 — Ship chart-local unchanged

Assess:

- near-term implementation simplicity;
- duplication across charts;
- rename/change brittleness;
- future migration cost;
- coupling between interaction and storage/source representation;
- reversibility;
- evidence supporting or weakening this path.

### S2 — Ship now with explicit migration boundary

Assess:

- what additional conceptual seam is required now;
- whether that seam is smaller than speculative future architecture;
- compatibility with current `string[]` representation;
- compatibility with an unknown future hierarchy owner;
- migration/reversibility properties;
- implementation/review burden relative to S1;
- evidence supporting or weakening this path.

### S3 — Wait

Assess:

- concrete dependency evidence;
- timing evidence;
- opportunity cost of waiting;
- risk avoided by waiting;
- whether waiting produces a known architectural benefit or merely delays uncertainty;
- evidence supporting or weakening this path.

Do not use a numeric score unless naturally justified by evidence.

---

## Minimal-boundary constraint

The resolution must define the **smallest conceptual boundary** needed for S2.

It may describe something equivalent to:

```text
Chart configuration
      ↓
Hierarchy source / reference
      ↓
Resolve to ordered hierarchy levels
      ↓
Existing drill interaction
```

But it must not prescribe unnecessary classes, services, database schemas, APIs, persistence layers, or provider contracts.

The boundary must answer only:

1. What does the drill interaction need as input?
2. What part of the current chart config is source representation rather than interaction semantics?
3. What must remain replaceable later?
4. What invariants should survive a future source change?

If a simpler seam exists, prefer it.

---

## Required invariants

Identify the minimum invariants that should remain true across current and future hierarchy sources.

Candidate invariants to test rather than blindly adopt:

- the interaction receives an ordered sequence of drillable dimensions;
- the chart can resolve its hierarchy source before runtime interaction begins;
- absence or failure of a future reference must not silently corrupt existing inline charts;
- existing chart-local lists remain interpretable during any migration period;
- hierarchy ownership and drill-state behavior remain separate concerns;
- source migration should not require rewriting breadcrumb/click-state behavior;
- unknown future identifiers must not be hard-coded now.

Reject any invariant that current evidence does not support or that unnecessarily constrains future design.

---

## Explicit non-inventions

Do not define or assume:

- final hierarchy object schema;
- hierarchy UUID/name strategy;
- dataset database migrations;
- semantic-provider API shape;
- sync protocol;
- conflict/precedence rules;
- rename propagation behavior;
- deletion semantics;
- cache behavior;
- permission model;
- REST endpoints;
- upstream provider support;
- release timeline;
- exact migration implementation.

Where the resolution depends on one of these, mark it **UNKNOWN / FUTURE CONTRACT**.

The quality of the resolution depends partly on what it refuses to invent.

---

## Failure-mode analysis

Attempt to break S2 with at least these failure modes:

1. Future hierarchy semantics differ materially from a simple ordered list.
2. Hierarchies become provider-native and cannot be represented by raw Superset column names.
3. Chart-local inline config becomes difficult to migrate.
4. Multiple hierarchy sources introduce ambiguous precedence.
5. A source-resolution seam adds complexity without reducing migration risk.
6. The interaction actually depends on source-specific identity or metadata.
7. Waiting would avoid substantial rework because hierarchy implementation is more imminent than Spec 033 found.

For each failure mode state:

- whether evidence supports it;
- whether S2 survives;
- what minimal safeguard, if any, is justified now;
- whether the safeguard itself would be premature architecture.

---

## Counterargument requirement

Construct the strongest case **against S2**.

At minimum ask:

> Why not simply ship S1 and migrate later when the future contract is real?

and

> Why not wait under S3 to avoid two representations entirely?

The final recommendation must explicitly answer both.

Do not make S2 win by definition.

---

## Disposable-resolution format

Produce one concise decision artifact that could theoretically be shown to the SIP actor after separate authorization.

It should be useful without requiring the reader to understand Asymmetry Engine or Specs 032/033.

Target structure:

```text
Decision
Evidence
S1 / S2 / S3 trade-off
Recommendation
Minimal boundary
Why this is enough now
What remains deliberately unresolved
What evidence would reverse the recommendation
```

Prefer one page of dense useful reasoning over a long architecture memo.

---

## Decision-ready test

The artifact passes only if a reader can answer:

1. What should we do now?
2. Why is that preferable to the alternatives?
3. What exactly must change before shipping, if anything?
4. What should we deliberately not design yet?
5. What future evidence would cause us to reverse course?

If the resolution cannot answer these five questions, it is not decision-ready.

---

## Resolution-effect hypothesis

After constructing the artifact, state what observable decision effect it is intended to cause if later delivered.

Examples may include:

- SIP text changes from vague migration intent to an explicit source/interaction boundary;
- reference PR structure changes to isolate source resolution;
- maintainers accept S2 explicitly;
- maintainers reject S2 with evidence of a more concrete future dependency;
- the ship/wait question becomes closed.

Do not perform the interaction in Spec 034.

---

## Epistemic challenge

Before finalizing, perform an independent challenge of the draft resolution.

Ask:

- What claim is weakest?
- What is being inferred from absence of evidence?
- Is the proposed seam actually necessary now?
- Is the resolution sneaking in speculative architecture?
- Could S1 be economically superior because migration later is cheaper than designing a seam now?
- Could the boundary make future migration harder by freezing the wrong abstraction?
- What single fact would most strongly overturn the recommendation?

Revise the artifact if the challenge exposes a material weakness.

Record the challenge separately from the final resolution.

---

## Evidence classes

Label important claims using:

- **KNOWN CURRENT** — verified current implementation/project state;
- **CONCRETE IN FLIGHT** — implemented in an active unmerged artifact;
- **DIRECTIONAL** — project-native stated intent without stable contract;
- **INFERRED** — reasoned consequence of evidence;
- **UNKNOWN / FUTURE CONTRACT** — deliberately unresolved;
- **CONTRADICTED** — evidence disproves the claim.

Do not silently upgrade DIRECTIONAL evidence into KNOWN CURRENT.

---

## Time and cost envelope

Target active time: **30 minutes**.

Hard ceiling: **45 minutes**.

Incremental spend: **€0**.

If the evidence is sufficient earlier, stop.

Do not use remaining time to broaden the architecture problem.

---

## Controls

Spec 034 authorizes only read-only research and local artifact creation.

Do not:

- comment on SIP-225;
- react to comments;
- contact the proposal author or maintainers;
- open or modify a Superset issue or PR;
- submit code;
- create branches in the Superset repository;
- clone or alter external repositories unless read-only local inspection is necessary and ordinary public access permits it;
- inspect private data;
- use alternate identities;
- perform outreach;
- modify Spec 030 response state.

Any future external interaction requires a separate spec and explicit user authorization.

---

## Verdicts

### A — DECISION-READY RESOLUTION

A concise defensible resolution is produced; S1/S2/S3 are discriminated; the minimal S2 boundary is explicit; speculative architecture is excluded; counterarguments are addressed; and the artifact is suitable for a future controlled actor interaction.

### B — USEFUL RESOLUTION, ONE MATERIAL UNCERTAINTY

The resolution substantially compresses the decision but one bounded uncertainty still prevents a defensible actor-facing recommendation.

Identify exactly one next discriminator.

### C — S2 DOES NOT SURVIVE CHALLENGE

Evidence or adversarial review shows that S1 or S3 dominates, or that the proposed migration boundary creates more cost/constraint than value.

State the revised decision and why.

### D — INVALID / INSUFFICIENT

The experiment could not construct a valid resolution within the evidence/control/time envelope.

State why.

---

## Required artifact

Create:

`experiments/034/superset-disposable-sequencing-resolution.md`

The artifact must contain both:

1. the internal evidence/challenge record; and
2. a clearly delimited actor-facing disposable resolution draft.

Do not post or send the actor-facing draft.

---

## Required completion report

Return exactly these sections:

1. Verdict
2. Decision being resolved
3. Evidence baseline used
4. S1 assessment
5. S2 assessment
6. S3 assessment
7. Recommended option
8. Minimal migration/source boundary
9. Required invariants
10. Explicit non-inventions
11. Failure-mode findings
12. Strongest case against recommendation
13. Evidence that would reverse recommendation
14. Epistemic challenge result
15. Decision-ready test result
16. Intended observable decision effect
17. Actor-facing resolution summary
18. Research time and spend
19. What FORGE learned
20. What remains unproven
21. Whether actor interaction is now justified
22. Exactly one recommended next action

---

## Non-goals

Do not:

- rediscover opportunities;
- compare BI products;
- conduct broad Superset architecture research;
- design a complete semantic layer;
- design a hierarchy data model;
- implement an adapter;
- write production code;
- modify Superset code;
- estimate market size;
- test willingness to pay;
- test commercialization;
- infer business opportunity from open-source contribution value;
- contact any actor;
- broaden into generic software-architecture advice;
- force S2 if evidence favors another option.

---

## Governing principles

> **FORGE should compress uncertainty into a decision, not expand the design space.**

> **A useful boundary protects what must remain replaceable without inventing what does not yet exist.**

> **Unknown future architecture is not a reason to wait unless waiting has concrete expected value.**

> **Reversibility is valuable only when its cost is lower than the uncertainty it protects against.**

> **The artifact should be disposable; the learning should compound.**

> **A resolution is not valuable because it is technically elegant. It is valuable if it makes the decision smaller, clearer, and more testable.**

> **Do not interact until the resolution itself survives adversarial review.**
