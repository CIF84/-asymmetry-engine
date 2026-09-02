# Spec 017 — Behavioral Signal → Asymmetry Discovery

## Status

Research-only discovery-method pressure test. No production implementation.

## Context

Specs 013–016 exposed a weakness in the current commercial translation loop.

The Engine has mostly worked forward:

```text
observed domain evidence
→ candidate asymmetry
→ proposed resolution
→ commercialization hypothesis
→ distribution channel
→ market experiment
```

This is valid, but it can become solution-first: the Engine may infer an asymmetry and resolution before knowing whether economically meaningful behavior is observable at sufficient scale.

Spec 016 produced a useful counterexample. The proposed Czech appliance repair-versus-replace decision had nominally relevant search demand, but the strongest observed behavior was not explicit `repair or replace` demand. It was closer to:

```text
"How much should this repair cost?"
```

That behavior suggests a potentially different uncertainty:

```text
consumer knows appliance / fault / quote
→ repairer knows repair economics better
→ consumer cannot easily judge whether quote is fair
→ possible quote-benchmark / second-opinion asymmetry
```

The experiment therefore generated a new opportunity hypothesis rather than merely validating or rejecting the original one.

This suggests a reverse discovery path:

```text
BEHAVIORAL SIGNAL
→ REPEATED ECONOMIC UNCERTAINTY
→ DECISION FRICTION
→ INFORMATION ASYMMETRY
→ POSSIBLE RESOLUTION
→ EXPERIMENTABLE OPPORTUNITY
```

This spec tests whether that path is a useful, repeatable RADAR discovery mechanism.

Do not modify architecture or declare this the new canonical discovery model yet. First determine whether it works across unrelated signal classes and domains.

## Objective

Determine whether starting from **observable economically meaningful behavior** produces commercially useful asymmetry hypotheses that are:

- more grounded in demonstrated friction;
- closer to observable market behavior;
- easier to falsify;
- less dependent on speculative solution design;
- and at least as economically interesting as asymmetry-first discovery.

The central question is:

> Can behavioral exhaust from unresolved economic decisions be systematically translated into credible, commercially testable information-asymmetry hypotheses?

## Core hypothesis

Economic uncertainty leaves observable traces.

Examples may include:

- searches;
- complaints;
- questions;
- reviews;
- price comparisons or dispersion;
- marketplace behavior;
- tender behavior;
- regulatory disputes;
- repair/service requests;
- job postings;
- other public or cheaply accessible behavioral exhaust.

These signals are not themselves asymmetries.

The reasoning chain must remain explicit:

```text
OBSERVED BEHAVIOR
→ what decision is the actor trying to make?
→ what uncertainty or friction is visible?
→ what information would reduce that uncertainty?
→ who possesses, controls, fragments, obscures, or can derive that information?
→ why has the market not already resolved the problem sufficiently?
→ what resolution could reduce the uncertainty?
→ what behavior could cheaply reveal whether that resolution has economic value?
```

A signal must not be promoted to an opportunity merely because it is frequent.

## Research design

Use **5–7 materially different behavioral signal classes**.

At minimum include:

1. **search intent** — queries expressing economic uncertainty or decision friction;
2. **complaints / disputes** — repeated evidence of economic harm, confusion, failed expectations, or recourse seeking;
3. **questions / forums** — repeated requests for decision-relevant information;
4. **reviews** — recurring decision friction, hidden attributes, expectation gaps, or post-purchase surprises;
5. **market / price behavior** — dispersion, repeated comparison, quote opacity, listing behavior, or other transaction-adjacent evidence.

Add at most two other signal classes only if they provide genuinely orthogonal evidence, for example tenders, regulatory decisions, job postings, returns, or service requests.

Do not manufacture diversity by splitting one source into multiple nominal classes.

## Sources

Prefer sources already available to the project where they are suitable, but do not constrain the exercise to existing connectors.

Existing source families may include:

- Stack Exchange;
- CFPB;
- TED;
- Eurostat / Comext;
- Azure Retail Prices;
- OpenAlex;
- DataForSEO.

Public web research may be used to inspect other signal classes.

Paid data is allowed only where expected information value clearly exceeds acquisition cost. This spec should normally require little or no paid access.

Do not add a source connector.

Do not spend money merely to make signal classes symmetrical.

## Sampling rule

For each signal class, identify a small number of concrete observations or repeated patterns sufficient to reason from actual behavior.

Do not perform exhaustive market research.

The purpose is to test the **discovery method**, not to find every possible opportunity.

Avoid selecting examples because a known product solution already comes to mind. Start from the behavior and reconstruct the decision problem.

## Required reasoning template

For every candidate derived from a behavioral signal, document:

### 1. Signal

What exactly is observable?

Distinguish direct behavior from interpretation.

### 2. Actor

Who is producing the behavior?

### 3. Decision

What economic decision is the actor plausibly trying to make?

If no meaningful decision can be identified, stop the chain.

### 4. Uncertainty / friction

What does the actor apparently not know, cannot compare, cannot verify, cannot predict, or cannot access cheaply?

### 5. Asymmetry hypothesis

Who has better information, or what information can be derived by combining fragmented evidence?

Explicitly distinguish:

- missing information;
- fragmented information;
- costly-to-interpret information;
- strategically withheld information;
- expertise asymmetry;
- genuine information asymmetry;
- ordinary inconvenience.

Do not label inconvenience as asymmetry without argument.

### 6. Existing resolution

How is the market currently solving the problem?

Look for incumbents, free tools, intermediaries, comparison sites, professional services, marketplaces, regulation, standardization, or simple heuristics.

### 7. Residual gap

Why might meaningful uncertainty remain despite existing solutions?

If no credible residual gap exists, stop the chain.

### 8. Candidate resolution

What is the smallest information product, decision aid, benchmark, alert, comparison, dataset, workflow, or other mechanism that could reduce the uncertainty?

Do not design a full product.

### 9. Commercialization hypothesis

Who might pay, refer, affiliate, advertise, subscribe, license, or otherwise create economic value if the resolution works?

### 10. Cheapest observable behavior

What is the cheapest behavioral signal that could move the hypothesis materially up or down the evidence ladder?

Prefer behavior over stated preference.

### 11. Experimentability

Assess qualitatively:

- reachable population;
- observation throughput;
- cost per independent observation;
- attribution quality;
- time to signal;
- behavioral vs stated signal;
- legal / administrative friction;
- likely statistical power of a small experiment.

### 12. Confidence

State what is observed, inferred, and still speculative.

## Candidate volume

Produce approximately **8–12 candidate chains total**, distributed across the signal classes.

Do not create a 50-item idea list.

Quality of causal reconstruction matters more than candidate count.

At least one signal class should produce **no viable opportunity** if the evidence does not support one. Do not force every source to succeed.

## Comparison with asymmetry-first discovery

After deriving the candidates, compare the method against the process used in Specs 013–016.

Evaluate whether behavioral-first discovery tends to improve:

- evidence of repeated friction;
- decision proximity;
- commercialization distance;
- distribution observability;
- experimentability;
- confidence in the causal story;
- resistance to solution-first reasoning.

Also identify its biases.

For example, behavioral-first discovery may over-select problems that are:

- easy to observe rather than economically valuable;
- search-visible;
- complaint-heavy;
- consumer-facing;
- already served by mature markets;
- emotionally salient but low willingness-to-pay.

Do not assume behavioral-first is superior.

## Opportunity evaluation

For candidates that survive the reasoning chain, assess qualitatively:

```text
ASYMMETRY QUALITY
× RESOLUTION QUALITY
× COMMERCIAL VALUE
× DISTRIBUTABILITY
× EXPERIMENTABILITY
× OPERATOR FIT
```

Do not create pseudo-precise weighted scores unless the evidence naturally supports them.

Opportunity quality and operator fit must remain separate concepts.

A commercially strong opportunity may be rejected for this portfolio because it requires high-touch enterprise sales, regulatory exposure, or other poor operator fit. Record that distinction rather than downgrading the underlying opportunity itself.

## Appliance case

Use the Spec 016 result as one calibration example, not as the focus of this spec.

Preserve the distinction:

```text
original hypothesis:
repair vs replace decision aid

observed search behavior:
repair-cost uncertainty / lifespan research

possible revised hypothesis:
repair quote benchmark / independent second opinion
```

Do not run the proposed seven-keyword paid-search forecast.

Do not build an appliance artifact.

The appliance opportunity family remains **PARKED / UNRESOLVED** while this discovery method is tested.

## Evidence discipline

Preserve these distinctions:

```text
FREQUENT SIGNAL ≠ ECONOMIC FRICTION
FRICTION ≠ INFORMATION ASYMMETRY
ASYMMETRY ≠ RESOLVABLE ASYMMETRY
RESOLUTION ≠ COMMERCIAL PROPOSITION
SEARCH / COMPLAINT / REVIEW VOLUME ≠ WILLINGNESS TO PAY
OBSERVABILITY ≠ MARKET SIZE
```

And preserve the evidence ladder:

```text
observation
→ repeated friction
→ credible asymmetry
→ plausible resolution
→ commercial proposition
→ visitor
→ intent
→ explicit priced intent
→ transaction
→ repeat transaction
```

Do not silently promote candidates beyond the evidence actually obtained.

## Source economics

Record whether each useful behavioral signal came from:

- open/free intelligence;
- existing paid access;
- incremental paid access;
- manual public research.

For any paid signal, record actual incremental cost.

Use the principle:

> Open intelligence by default. Paid intelligence when expected information value exceeds acquisition cost and dependency cost.

Specifically assess whether search-intent data appears to be an **orthogonal and repeatedly useful signal class**, rather than deciding whether DataForSEO itself should become permanent infrastructure.

DataForSEO currently remains:

```text
LEVEL 1 — research instrument
```

This spec must not promote it to an experiment instrument or permanent Engine signal source.

## Required synthesis

At the end, answer five questions explicitly.

### Q1 — Does behavioral-first discovery work?

Choose:

- **SUPPORTED** — repeatedly generated credible asymmetry hypotheses with better grounding / experimentability;
- **PARTIALLY SUPPORTED** — useful in some signal classes but materially biased or unreliable in others;
- **NOT SUPPORTED** — mostly produced obvious, weak, already-solved, or commercially distant problems.

### Q2 — What signal classes were most productive?

Rank only on observed usefulness in this exercise, not theoretical richness.

Explain why.

### Q3 — Did the method discover anything we were unlikely to generate asymmetry-first?

Identify the strongest examples, if any.

### Q4 — Should behavioral signals feed backward into RADAR discovery?

Choose:

- yes, as a first-class discovery path;
- yes, but only as a complementary path;
- not yet;
- no.

Do not modify architecture in this spec.

### Q5 — What single next action has the highest expected information value?

Choose at most **one**:

- test one newly discovered opportunity;
- deepen one signal class;
- compare one paid source against alternatives;
- revise the reasoning model;
- return to broader candidate selection;
- stop / rethink the behavioral-first hypothesis.

Do not authorize multiple parallel experiments.

## Required completion report

Return:

1. signal classes examined;
2. sources used and incremental cost;
3. 8–12 behavioral-signal candidate chains using the required template;
4. candidates rejected during causal reconstruction and why;
5. surviving candidates and qualitative opportunity evaluation;
6. comparison against asymmetry-first discovery;
7. observed biases / failure modes of behavioral-first discovery;
8. answer to Q1–Q5;
9. one recommended next action only;
10. architecture implications, explicitly separated into:
   - evidence strong enough to preserve;
   - hypotheses still too early to institutionalize.

## Budget

- Cash: **€5 maximum**, preferably €0.
- Operator / research time: **4 hours maximum**.
- No software implementation.
- No market outreach.
- No ads.
- No payment setup.

If useful evidence cannot be obtained inside these bounds, report that as evidence about the method rather than expanding the scope.

## Non-goals

Do not:

- build or modify production code;
- add connectors;
- create a generic behavioral ontology;
- create a scoring framework;
- rewrite `ARCHITECTURE.md`;
- rewrite `ECONOMIC_REASONING_MODEL.md`;
- build an opportunity database;
- run the appliance paid-search forecast;
- buy ads;
- contact prospects;
- enroll in affiliate programs;
- register a business;
- optimize SEO;
- select B2C by assumption;
- force all signal classes to yield opportunities;
- turn this into a broad market landscape report.

## Governing principles

> Start from what economic actors demonstrably do, then ask what uncertainty makes that behavior necessary.

> Behavioral exhaust is evidence of activity, not proof of asymmetry or willingness to pay.

> Let experiments revise the opportunity hypothesis, not merely accept or reject it.

> Prefer discovery mechanisms that make commercial hypotheses cheap to falsify.

> Automation should multiply validated asymmetries, not compensate for weak ones.
