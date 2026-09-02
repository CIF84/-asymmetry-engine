# Spec 019 — EV Configuration Evidence Feasibility

## Status

Research-only feasibility gate. No production implementation.

## Context

Spec 018 found one candidate that survived review-derived hidden-attribute replication, recoverability, exact-solution competition, and initial data-feasibility pressure:

> Configuration-aware home-EV charger, vehicle, and tariff compatibility verification.

The relevant decision is not whether an EV, charger, or tariff is individually compatible in isolation. The consumer's actual outcome may depend on the combination:

```text
vehicle model/version
× charger model
× energy tariff
× controlling component
× solar / battery / multiple-EV context
× software / integration limitations
→ actual smart-charging compatibility and economics
```

The candidate is interesting because much of the necessary information appears to exist publicly, while the decision answer exists at the intersection of multiple actors' information.

This is a candidate **derived information asymmetry**:

```text
vehicle maker knows vehicle capability
charger maker knows charger capability
energy supplier knows tariff eligibility / control rules
installer knows installation constraints
household knows local configuration

fragmented evidence
→ consumer must derive configuration truth
```

However, a theoretically derivable answer is commercially useless if authoritative evidence is too incomplete, contradictory, unstable, or expensive to maintain.

Spec 019 therefore tests the evidence system before any product or market experiment.

## Objective

Determine whether a useful EV smart-charging compatibility answer can be reconstructed **reproducibly from authoritative public evidence** for a small representative set of real UK configurations.

The central question is:

> Can we determine, explain, source, and maintain configuration-level compatibility cheaply enough that this asymmetry could plausibly be resolved by a self-service information product?

This spec is not a product validation and does not test willingness to pay.

## Governing distinction

> Behavioral evidence discovers the question. Authoritative evidence should answer it.

Reviews and forums were useful in Specs 017–018 for discovering the candidate. They must not be used as primary compatibility evidence in this feasibility test.

## Scope

Test **exactly 10 representative UK configurations**.

Each configuration should contain, where relevant:

- vehicle make/model and sufficiently precise variant or generation;
- charger make/model;
- energy tariff;
- controlling component or scheduling authority;
- relevant household context such as solar, battery, multiple EVs, or absence of these;
- any version/year/API distinction required by the authoritative sources.

Use a bounded set of common or commercially relevant combinations rather than obscure edge cases.

The sample should include enough variation to pressure-test the information model:

- more than one vehicle manufacturer;
- more than one charger manufacturer;
- more than one energy supplier/tariff family;
- at least one vehicle-controlled configuration;
- at least one charger-controlled configuration;
- at least two configurations with an additional household complication such as solar, battery, or multiple EVs;
- at least one deliberately plausible configuration expected to be incompatible or materially limited.

Do not expand beyond 10 configurations to improve the pass rate.

## Source hierarchy

Use authoritative sources in this order where available:

1. energy supplier tariff / eligibility / compatibility documentation;
2. charger manufacturer compatibility and product documentation;
3. vehicle manufacturer documentation;
4. official installation or integration documentation;
5. official regulatory or standards documentation where relevant.

Secondary comparison sites may be used only to identify what needs verification or to pressure-test coverage. They must not substitute for authoritative evidence when determining a configuration result.

Do not use Reddit, Trustpilot, forums, blogs, or anecdotal reports as evidence for a PASS compatibility determination.

If authoritative sources conflict, preserve the contradiction explicitly rather than resolving it by intuition.

## Required configuration reasoning

For each of the 10 configurations, reconstruct the evidence chain.

### 1. Configuration identity

Record the exact combination being tested.

### 2. User decision

State the practical decision the answer would support, for example:

- can I use this tariff with this existing EV and charger?
- should I buy this charger if I want this tariff?
- which component must control charging?
- will solar / battery / second-EV context change eligibility or expected behavior?

### 3. Controlling component

Determine whether charging is controlled primarily through:

- vehicle integration;
- charger integration;
- supplier hardware;
- another documented control path;
- or cannot be established.

Do not assume the charger controls charging merely because a charger is present.

### 4. Compatibility result

Choose exactly one:

- **COMPATIBLE** — authoritative evidence supports the complete tested configuration;
- **COMPATIBLE WITH MATERIAL CONDITIONS** — usable only if explicit conditions or configuration choices are satisfied;
- **INCOMPATIBLE** — authoritative evidence establishes that the combination does not qualify or function as required;
- **UNRESOLVED** — authoritative evidence is insufficient or contradictory.

### 5. Material conditions / caveats

Record conditions that could alter the consumer decision, such as:

- supported vehicle variants;
- charger firmware or connectivity;
- vehicle API support;
- tariff eligibility;
- control delegation;
- requirement to disable another schedule;
- multiple-EV restrictions;
- solar or home-battery interaction;
- installation constraints;
- supplier-specific hardware requirements;
- software/version limitations.

Do not record trivial technical detail that cannot change the decision.

### 6. Evidence provenance

For every material claim record:

- source organization;
- authoritative URL/page;
- page/document title where useful;
- retrieval date;
- what exact claim the source supports;
- whether the source is structured, semi-structured, or prose;
- whether the evidence appears versioned or dated.

The completion report may summarize repeated sources, but the underlying reasoning must remain traceable.

### 7. Contradictions

Record whether authoritative sources:

- agree;
- are incomplete but compatible;
- use different definitions;
- appear stale relative to one another;
- or directly contradict.

Do not hide contradiction inside an overall answer.

### 8. Reproducibility

Ask:

> Could another careful operator reach the same compatibility result from the cited evidence without relying on undocumented domain intuition?

Classify:

- **HIGH** — evidence chain is explicit and direct;
- **MEDIUM** — limited interpretation is required but reasoning is reproducible;
- **LOW** — substantial expert judgment or undocumented inference is required.

### 9. Maintenance burden

Assess what would cause this answer to become stale:

- tariff rule change;
- vehicle integration change;
- charger firmware/integration change;
- manufacturer page change;
- API/support change;
- regulatory change;
- other.

Then classify likely maintenance burden:

- **LOW** — stable source and simple change detection;
- **MEDIUM** — periodic verification or several sources required;
- **HIGH** — frequent manual archaeology, opaque state, or difficult version tracking.

### 10. Automation potential

Classify the evidence path:

- **STRUCTURED** — machine-readable or stable tabular/list source;
- **SEMI-STRUCTURED** — predictable page/document structure suitable for bounded extraction;
- **PROSE / MANUAL** — substantial interpretation required;
- **NOT PRACTICALLY AUTOMATABLE**.

This is an observation, not authorization to build extraction software.

## Feasibility dimensions

After resolving all 10 configurations, evaluate the candidate on four separate dimensions.

### A. Resolvability

Can configuration truth actually be determined?

Measure:

- number COMPATIBLE;
- number COMPATIBLE WITH MATERIAL CONDITIONS;
- number INCOMPATIBLE;
- number UNRESOLVED;
- number with HIGH/MEDIUM/LOW reproducibility.

A configuration counts as **resolved** if it is COMPATIBLE, COMPATIBLE WITH MATERIAL CONDITIONS, or INCOMPATIBLE with sufficient authoritative evidence.

### B. Provenance quality

Can the result be explained and defended?

Assess:

- authoritative source coverage;
- claim-level traceability;
- contradictions;
- date/version clarity;
- dependence on secondary sources.

A commercially useful compatibility product must be able to show users *why* a result exists, not merely output a label.

### C. Maintainability

Can the answer remain current without recurring manual archaeology?

Assess:

- number of distinct authoritative source families required;
- change frequency visible from source structure;
- whether pages expose dates/version information;
- whether source changes could plausibly be monitored;
- amount of manual interpretation required per update;
- whether a small number of source changes could invalidate many configurations simultaneously.

### D. Economic data feasibility

Estimate—not with false precision—the likely relationship between:

```text
coverage value
vs
initial evidence acquisition
+ ongoing monitoring
+ manual exception handling
```

Ask whether the evidence model could plausibly scale first to tens, then hundreds, of popular configurations without the operator becoming the permanent integration expert.

Do not estimate full business P&L or market size in this spec.

## Gate

Use the following as decision aids rather than pseudo-precise scoring.

### PASS

Return PASS only if broadly all are true:

- at least **8 of 10** configurations are resolved reproducibly from authoritative evidence;
- material caveats can be surfaced rather than silently inferred;
- authoritative provenance is strong enough to explain the result;
- no more than a small minority depend on LOW-reproducibility reasoning;
- source structure suggests that change detection and updating are plausible;
- maintenance does not obviously require repeated manual rediscovery across every configuration;
- there is a credible path to expanding coverage without immediately building a large expert-maintained knowledge base.

### PARTIAL

Return PARTIAL if the 8/10 resolution threshold is reached but maintenance/provenance/automation creates a material unresolved question, or if 6–7 configurations resolve cleanly enough to justify exactly one narrower feasibility discriminator.

### FAIL

Return FAIL if broadly any are true:

- fewer than 6 configurations resolve reproducibly;
- authoritative sources routinely fail to expose material conditions;
- contradictions cannot be handled without anecdotal evidence;
- configuration answers depend heavily on undocumented expert judgment;
- source volatility or fragmentation makes maintenance visibly disproportionate;
- the data cold-start appears to require user reports or manual research at a scale incompatible with the intended self-service economics.

Do not rescue a FAIL by adding forums, more configurations, more countries, or implementation.

## Required verdict

Choose exactly one:

- **A — PASS: authoritative evidence appears sufficient and maintainable enough to justify the next commercial discriminator**
- **B — PARTIAL: evidence feasibility is promising but one bounded uncertainty remains**
- **C — FAIL: evidence acquisition / maintenance economics undermine the candidate**
- **D — BLOCKED: required authoritative evidence is inaccessible**

## Required completion report

Return:

1. exact 10 configurations tested;
2. rationale for sample composition;
3. authoritative source inventory;
4. per-configuration evidence table containing:
   - configuration;
   - user decision;
   - controlling component;
   - compatibility result;
   - material caveats;
   - key authoritative sources;
   - contradiction status;
   - reproducibility;
   - maintenance burden;
   - automation potential;
5. resolved/unresolved totals;
6. provenance-quality assessment;
7. contradiction analysis;
8. maintainability analysis;
9. automation-potential analysis;
10. economic data-feasibility assessment;
11. verdict A/B/C/D;
12. exact evidence that most strongly supports the verdict;
13. exactly one recommended next action;
14. architecture implications separated into:
   - evidence strong enough to preserve;
   - hypotheses too early to institutionalize.

## Next-action discipline

If **A — PASS**, do not build the product automatically.

Choose the single next action with the highest expected information value. It will likely test a commercial or distribution assumption now that data feasibility has survived, but the completion report must justify that choice from the evidence.

If **B — PARTIAL**, specify exactly one bounded discriminator. Do not broaden research.

If **C — FAIL**, park or kill the EV interoperability candidate. Do not search for a new EV subproblem in the same spec.

If **D — BLOCKED**, identify exactly what authoritative evidence could not be accessed and stop.

## Budget

- Cash: **€0**.
- Research/operator time: **4 hours maximum**.
- Configurations: exactly **10**.
- Geography: **UK only**.

If authoritative evidence cannot be reconstructed inside these bounds, that is evidence about the opportunity.

## Non-goals

Do not:

- build software;
- modify production code;
- create a compatibility database;
- create a graph or ontology;
- create scrapers or connectors;
- use reviews/forums as compatibility truth;
- contact manufacturers, suppliers, installers, or consumers;
- buy data;
- buy ads;
- build a landing page;
- test willingness to pay;
- estimate total addressable market;
- expand beyond the UK;
- expand beyond 10 configurations;
- rewrite architecture or reasoning-model documents;
- turn this into a general EV market report.

## Governing principles

> Behavioral evidence discovers the question. Authoritative evidence should answer it.

> Public information is not equivalent to usable decision information; value may exist in deriving the answer across fragmented sources.

> A correct answer today is insufficient if maintaining correctness requires permanent manual archaeology.

> Provenance is part of the product when the resolution depends on derived information.

> Data acquisition and maintenance economics are part of opportunity quality, not an implementation detail.
