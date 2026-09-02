# Spec 015 — Experimentability-First Opportunity Selection

## Status

Research and decision specification. No production implementation by default.

## Context

Specs 013–014 produced an important empirical correction to the commercial-validation strategy.

The cocoa-input case remained commercially plausible, but the planned 25-prospect outreach test exposed a measurement problem: for a small niche B2B population, cold-email response is a noisy and low-throughput sensor. A weak observed response may reflect deliverability, attention, channel fit, or insufficient sample size rather than absence of demand.

Therefore:

> Negative experimental evidence is meaningful only relative to the experiment's power to observe the behavior being tested.

And:

> Prefer opportunities whose commercial hypotheses can be falsified cheaply, quickly, and at sufficient sample size.

Cocoa is PARKED, not KILLED. Do not execute or redesign the cocoa proposition during this spec.

The project now needs to revisit opportunity selection with **experimentability** as an explicit first-class criterion.

This is not a mandate to choose B2C. B2C, prosumer, automated B2B, affiliate, lead-generation, or other models may qualify. The point is to let the economics of learning select the next experiment.

## Objective

Identify the opportunity class or concrete candidate that currently offers the highest expected **economic information gained per euro and per hour**, while remaining grounded in evidence available to or cheaply reachable by Asymmetry Engine.

The output should answer:

> Of the economic asymmetries we can currently observe — or can cheaply observe — which ones allow us to obtain the largest amount of real behavioral evidence at sufficient scale before committing meaningful time, money, operational burden, or legal/business infrastructure?

## Primary decision

Select at most **one** candidate for the next real-world experiment.

It is valid to select none.

The result must not be driven by a prior preference for B2C or B2B.

## Updated selection model

Evaluate candidates across five separate dimensions:

1. **Opportunity quality**
2. **Commercial potential**
3. **Experimentability**
4. **Distributability**
5. **Operator fit**

Do not collapse these dimensions prematurely.

### 1. Opportunity quality

Ask:

- Is there demonstrated decision friction?
- Is there a plausible information asymmetry rather than merely unusual data?
- Does resolving it change an economically meaningful decision?
- Is the resolution materially better than readily available substitutes?

### 2. Commercial potential

Ask:

- Who captures value?
- How often does the decision occur?
- What is the plausible value of a better decision?
- Is there a credible monetization mechanism?
- Could the economics support a repeatable asset rather than bespoke work?

### 3. Experimentability

Treat this as a first-class economic property.

Definition:

> Experimentability is the ability to obtain enough independent, behaviorally meaningful observations to reduce commercial uncertainty cheaply and quickly.

Assess:

- reachable population size;
- expected observations per euro;
- expected observations per hour;
- time to first observable behavior;
- ability to observe behavior rather than stated preference;
- ability to distinguish channel failure from proposition failure;
- sample-size / statistical-power limitations;
- attribution clarity;
- ability to run sequential tests;
- reversibility;
- legal and administrative friction before validation;
- whether validation requires company formation, contracts, regulated activity, enterprise procurement, domain credentials, or similar commitment;
- whether a failed test produces interpretable negative evidence.

Explicitly model the observation chain where relevant, for example:

```text
REAL DEMAND
→ reachable user
→ exposure delivered
→ exposure noticed
→ proposition understood
→ behavior possible
→ behavior observed
```

Identify where signal loss occurs.

Do **not** treat:

```text
no observed behavior = no demand
```

unless the experiment had reasonable power to observe the behavior.

### 4. Distributability

Assess separately from experimentability.

Ask:

- Can high-intent users be reached cheaply?
- Does existing search/social/community/marketplace traffic expose the problem?
- Can distribution eventually become repeatable or automated?
- Is acquisition dependent on relationships, outbound sales, trust-building, tenders, or enterprise procurement?
- Does an incumbent own the obvious high-intent distribution surface?

### 5. Operator fit

Keep opportunity quality separate from operator fit.

Current preferred operating characteristics:

- autonomous;
- low networking burden;
- low-touch support;
- scalable solo or very small operation;
- self-service where possible;
- automation-friendly;
- modest capital requirements;
- minimal regulatory/compliance burden;
- compatible with a portfolio of multiple assets rather than one all-consuming company.

A strong opportunity may still be PARKED because operator fit is poor.

## Strategic objective

The current objective is not simply maximum theoretical business value.

The objective is:

> **rapid accumulation of reliable economic learning that can lead toward repeatable independent revenue.**

Therefore, during this phase, experimentability may rationally outweigh a somewhat larger but much slower opportunity.

## Candidate universe

Start from existing Asymmetry Engine evidence and previously identified opportunity patterns. Do not restrict the search to the four Spec 013 cases.

At minimum revisit or consider:

- consumer durable decision asymmetries;
- exact-model repair-versus-replace / ownership-cost decisions;
- price/specification/claim asymmetries;
- product comparison where seller information advantage is meaningful;
- regulation-driven consumer decisions where public data is fragmented;
- recurring household cost decisions;
- high-intent purchase decisions with affiliate or lead-generation paths;
- self-service prosumer decisions;
- automated B2B decisions with large reachable populations;
- existing evidence from Stack Exchange, CFPB, TED, Eurostat, Azure, Comext, OpenAlex, and prior manual research where commercially relevant.

Also allow new candidate discovery through bounded live web research if it materially improves selection.

Do not add a source connector merely to conduct this pass.

## B2C hypothesis to test — not assume

Spec 015 must explicitly test the following hypothesis:

> Consumer-facing decision problems may be superior early learning vehicles because large digitally reachable populations permit higher-throughput behavioral experiments with less dependence on interviews or cold outreach.

Potential validation advantages include:

- larger reachable populations;
- landing-page behavior;
- search behavior;
- recommendation interactions;
- affiliate redirects;
- wait-list or notification signups;
- price-sensitive CTA behavior;
- repeated experiments across variants;
- eventual transaction evidence.

But B2C must be penalized where:

- search acquisition is prohibitively competitive;
- the decision occurs too rarely;
- willingness to pay directly is weak;
- affiliate economics are poor;
- incumbents dominate comparison/discovery;
- product data is unavailable or expensive;
- consumer trust is costly to establish;
- traffic requirements make testing slower rather than faster.

The required conclusion is not "B2C wins." The required conclusion is whether the evidence supports that claim for the next experiment.

## Candidate generation

Generate a broad but bounded candidate set before ranking.

Target approximately **8–15 concrete candidates**, not vague sectors.

A candidate should be expressed as:

```text
ACTOR
→ DECISION
→ FRICTION / ASYMMETRY
→ RESOLUTION
→ MONETIZATION
→ DISTRIBUTION
→ CHEAPEST OBSERVABLE BEHAVIOR
```

Example shape only:

```text
consumer with broken appliance
→ repair or replace exact model
→ fragmented repair cost / expected life / energy / replacement data
→ exact-model ownership-cost decision aid
→ affiliate / lead generation
→ high-intent search
→ user completes comparison and clicks recommended action
```

Do not assume this example survives competition pressure.

## Minimum evidence per candidate

For each candidate establish enough evidence to answer:

1. What exact decision is being made?
2. Who makes it?
3. What makes the decision difficult or asymmetric?
4. What evidence suggests the friction actually exists?
5. What existing solutions/substitutes solve the same decision?
6. What resolution could Asymmetry Engine plausibly produce?
7. What monetization mechanism fits the resolution?
8. Where do users already reveal intent?
9. What observable behavior could test the proposition?
10. Roughly how many independent observations could be obtained in the first test?
11. What would that test cost in time and cash?
12. What would a negative result actually tell us?
13. What legal/administrative boundary would be crossed, if any?
14. What is the dominant uncertainty?

## Competition pressure test

Search for the **exact decision problem**, not merely category competitors.

For every finalist ask:

> If the user already has this problem today, what would they actually use instead?

Include:

- specialist tools;
- comparison sites;
- marketplaces;
- spreadsheets/calculators;
- forums/Reddit/community answers;
- retailers;
- search engines / AI assistants;
- brokers/advisers;
- doing nothing / intuition.

A crowded category does not automatically kill a candidate. But if the proposed resolution is already easily available at the point of intent, explain why another entrant has an information or distribution advantage.

## Experiment design pressure test

For the top candidates, design the **cheapest possible falsification experiment** without building the product.

Prefer observable behavior over opinion.

Possible evidence, from weaker to stronger depending on context:

```text
impression
→ click
→ interaction
→ completed analysis
→ recommendation click
→ email/wait-list signup
→ explicit priced intent
→ affiliate/lead redirect
→ transaction
→ repeat transaction
```

Do not assume this ladder is universal; explain what behavior is meaningful for each candidate.

For each proposed experiment specify:

- hypothesis;
- target population;
- channel;
- artifact/proposition;
- observable behavior;
- expected sample size or exposure range;
- expected cost;
- expected elapsed time;
- major measurement losses;
- what success means;
- what failure means;
- when failure would be uninterpretable;
- sequential stopping rule.

### Sequential testing

Avoid arbitrary tiny fixed samples where possible.

Prefer:

```text
WAVE 1
→ inspect signal quality
→ WAVE 2 if uncertainty remains
→ stop when evidence becomes decision-relevant
```

Do not fabricate statistical precision. Use ranges and sensitivity analysis where inputs are uncertain.

## Experimentability comparison

For finalists, compare at least:

| Dimension | Meaning |
|---|---|
| Reachable population | Plausible number of target users accessible to first test |
| Behavioral observability | How directly real behavior can be measured |
| Observation throughput | Meaningful observations per day/week |
| Cash per information unit | Approximate cash required to reduce uncertainty |
| Time per information unit | Approximate operator time required |
| Channel ambiguity | Risk that poor channel performance masks demand |
| Negative-evidence power | Whether failure would genuinely weaken the hypothesis |
| Legal/admin friction | Commitment required before meaningful validation |
| Reversibility | Cost of abandoning the experiment |
| Scale path | Whether successful validation can naturally become a scalable asset |

Use coarse labels plus explanation. Avoid fake 0–100 scores.

## Information economics

For finalists explicitly estimate:

```text
EXPECTED INFORMATION VALUE
--------------------------
CASH COST + OPERATOR TIME + IRREVERSIBLE COMMITMENT
```

This is conceptual, not a requirement for a mathematically precise ratio.

The key question is:

> Which experiment is most likely to change our decision at the lowest total cost?

## Required output

### 1. Strategic update

Explain what Specs 013–014 taught about commercial validation and why experimentability now matters.

### 2. Candidate universe

Provide 8–15 concrete candidates with actor, decision, asymmetry, resolution, monetization, distribution, and cheapest observable behavior.

### 3. First-pass elimination

Eliminate weak candidates explicitly and state why.

Common valid reasons include:

- asymmetry not demonstrated;
- incumbent already resolves it;
- distribution too expensive;
- insufficient population;
- low behavioral observability;
- legal/admin burden before validation;
- monetization too distant;
- poor operator fit;
- weak economic consequence;
- data unavailable;
- negative experiment would be uninterpretable.

### 4. Finalist comparison

Compare approximately 3–5 finalists across all five selection dimensions and the experimentability table above.

### 5. B2C hypothesis verdict

Choose one:

- **SUPPORTED** — B2C/prosumer currently offers materially better learning economics;
- **PARTIALLY SUPPORTED** — some consumer candidates do, but channel/monetization constraints prevent a general conclusion;
- **NOT SUPPORTED** — another opportunity type offers better learning economics.

Explain why.

### 6. Selection verdict

Choose exactly one:

**A — one candidate clearly deserves the next real-world experiment**

**B — one candidate leads, but one bounded evidence check is required before experiment**

**C — several candidates remain tied; perform one cheap discriminator before selecting**

**D — no current candidate has adequate opportunity quality × experimentability; return to discovery with explicit failure knowledge**

Do not force A or B.

### 7. If A or B: primary candidate

State:

- actor;
- decision;
- asymmetry;
- resolution;
- monetization;
- distribution;
- experiment;
- observable behavior;
- expected exposure/sample range;
- time budget;
- cash budget;
- success signal;
- kill signal;
- uninterpretable-result condition;
- legal/admin boundary;
- next evidence-ladder rung.

### 8. If C: discriminator

Specify the single cheapest research or behavioral test that best separates the tied candidates.

### 9. If D: discovery implication

State exactly what kind of evidence or source is missing and why collecting it has higher expected information value than experimenting now.

### 10. Architecture implication

Answer:

- Did this pass require new production architecture?
- Did any existing reasoning output materially help selection?
- What information would eventually deserve persistence if repeated experiments force it?
- Did experimentability emerge as a durable reasoning concept or merely a temporary portfolio heuristic?

Do not implement architecture based on this answer.

## Evidence discipline

For each finalist separate:

```text
KNOWN FROM EXISTING EVIDENCE
NEW EXTERNAL EVIDENCE
INTERPRETATION
COMMERCIAL HYPOTHESIS
EXPERIMENTAL HYPOTHESIS
UNKNOWN / FALSIFIER
```

Do not blur search-volume estimates, competitor marketing claims, observed user behavior, and inferred willingness to pay.

## Legal and operational discipline

This spec is research and selection only.

Do not:

- create a company;
- register a trade;
- collect money;
- send commercial outreach;
- create contracts;
- purchase ads;
- open merchant accounts;
- create payment infrastructure.

Legal or administrative friction should be assessed as a property of the experiment, not crossed during this spec.

## Repository / implementation constraints

Research-only by default.

Do not modify:

- production source code;
- database schema;
- adapters;
- reasoning.py;
- CLI;
- domain models;
- tests unrelated to documentation/spec work.

Do not add:

- new source connectors;
- dashboards;
- web UI;
- opportunity scoring engine;
- generic experiment framework;
- CRM;
- email automation;
- payment integration;
- knowledge graph;
- ontology system;
- LLM orchestration layer.

Temporary scripts or external research are acceptable if they are not persisted as speculative production infrastructure.

## Budget

Research budget:

- Cash: target €0; hard cap €25 without explicit approval.
- Time: target one focused research pass; stop if additional research is merely adding candidates rather than changing selection.

## Completion rule

Spec 015 is complete when we know whether there is a candidate whose **learning economics** justify the next real-world experiment.

The goal is not to find the theoretically best business.

The goal is to choose the next experiment that maximizes useful economic learning while preserving optionality.

## Governing principles

> Constrain execution, not discovery.

> Automation should multiply validated asymmetries, not compensate for weak ones.

> Absence of observed demand is evidence only to the extent that the experiment had sufficient power to observe demand.

> Prefer opportunities whose commercial hypotheses can be falsified cheaply, quickly, and at sufficient sample size.

> The market must earn the right for us to build.
