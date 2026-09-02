# Spec 028 — Accessible Decision Surface Discovery

## Status

RADAR discovery experiment.

Research-only. Do not build software, contact prospects, run ads, create landing pages, or execute behavioral experiments.

## Context

Specs 023–027 completed a full opportunity branch for the Canadian September 8 counter-tariff case:

```text
credible asymmetry                  ✓
recoverable information             ✓
economic consequence                ✓
exact resolution gap                ✓
live competitor gap                 ✓
resolution producible               ✓
resolution correct                  ✓
resolution decision-ready           ✓
accessible decision surface         ✗
```

The opportunity was PARKED because the relevant importer decision lived primarily inside trusted broker, association, and authenticated customs workflows. The asymmetry was real; the resolution worked; intervention experimentability was poor.

This suggests a new candidate-generation prior:

> **Prefer asymmetries whose affected actors reveal themselves at an accessible pre-decision surface.**

Spec 028 tests that prior directly.

## Objective

Answer one question:

> **Can RADAR discover economically consequential opportunity hypotheses by starting from observable pre-decision surfaces where affected actors self-identify through their behavior, rather than discovering an asymmetry first and searching for distribution afterward?**

The experiment tests whether accessible decision surfaces are a productive discovery origin.

It does not assume that visibility, traffic, questions, or search volume imply an opportunity.

## Core discovery reversal

Previous common flow:

```text
ASYMMETRY
→ ACTOR
→ RESOLUTION
→ WHERE CAN WE REACH THEM?
```

Spec 028 begins with:

```text
ACCESSIBLE PRE-DECISION BEHAVIOR
→ ACTOR
→ DECISION
→ UNCERTAINTY
→ ECONOMIC CONSEQUENCE
→ ASYMMETRY
→ RECOVERABILITY
→ EXACT RESOLUTION GAP
```

The surface is the starting evidence, not the opportunity thesis.

## Accessible decision surface definition

For this experiment, a surface is potentially interesting when it provides public or legitimately accessible evidence of all or most of the following:

1. **Self-identifying actor** — the actor reveals enough context to know who is making the decision.
2. **Pre-decision timing** — the decision is still open; the economic consequence has not fully occurred.
3. **Decision specificity** — the behavior reveals a concrete choice, comparison, configuration, purchase, switch, application, pricing, repair, compliance, booking, selection, or similar decision.
4. **Decision-linked uncertainty** — the actor lacks information required to decide confidently.
5. **Potential structured inputs** — the uncertainty can plausibly be described using recoverable facts rather than private institutional state alone.
6. **Accessible intervention path** — a future bounded resolution could plausibly be delivered through, adjacent to, or discovered from the same surface without bespoke relationship-building.
7. **Observable response** — a future experiment could plausibly observe engagement, decision change, next action, conversion, or another meaningful response.

A surface does not need to satisfy every condition before inspection. These conditions determine whether it deserves deepening.

## What does NOT count

Do not treat the following as sufficient discovery origins:

- post-purchase complaints with no remaining decision;
- generic news consumption;
- broad discussion detached from action;
- passive social commentary;
- support requests where all meaningful facts are private to an institution;
- high-volume keywords that do not reveal a bounded decision;
- professional chatter with no end-user decision context;
- communities where actors are visible but intervention requires individual relationship-building every time;
- marketplace/category demand where the uncertainty has already been adequately resolved by existing filters/tools.

## Surface families

Inspect exactly **4 distinct surface families**.

The families must differ in how decision behavior becomes observable. Candidate families may include:

- search/query behavior;
- public Q&A or forum behavior;
- comparison/configuration workflows;
- marketplace or listing behavior;
- public application/eligibility workflows;
- public procurement/request feeds;
- public calculators/checkers with visible unresolved adjacent questions;
- software/app ecosystem reviews or migration questions where a decision is still open;
- booking/travel/selection workflows;
- repair/replace or buy/switch decisions;
- other surface types discovered during research.

Do not choose four versions of the same surface merely to satisfy the count.

At least **2 families must not be generic web search or Reddit/forum discussion**.

## Signal-before-hypothesis rule

For every candidate, preserve this order:

```text
RAW SURFACE SIGNAL
→ OBSERVED BEHAVIOR
→ ACTOR
→ LIVE DECISION
→ MISSING / UNCERTAIN INFORMATION
→ ECONOMIC CONSEQUENCE
→ RECOVERABILITY
→ HYPOTHESIZED ASYMMETRY
```

Do not begin with a familiar business idea and search backward for supporting examples.

If the hypothesis clearly existed before the signal, mark it as non-signal-native and do not count it toward the required candidate set.

## Candidate generation target

Generate **8–12 signal-native opportunity hypotheses** across the 4 surface families.

Each candidate must contain:

- raw evidence/surface;
- actor;
- live decision;
- uncertainty;
- economic consequence;
- why the actor is visible before the consequence;
- what information might resolve the decision;
- recoverability assessment;
- plausible bounded resolution;
- how the same or adjacent surface could support future intervention;
- exact-resolution competition status.

Do not generate candidates solely to hit the quota. If a surface family is unproductive, record that honestly.

## Early kill sequence

Evaluate candidates in this order:

```text
PRE-DECISION? 
→ ECONOMICALLY CONSEQUENTIAL?
→ ACTOR SELF-IDENTIFYING?
→ INFORMATION RECOVERABLE?
→ ACCESSIBLE INTERVENTION PATH?
→ EXACT RESOLUTION GAP?
```

Kill cheaply when any upstream property clearly fails.

Do not perform deep market research on a candidate that already fails pre-decision timing or recoverability.

## Pre-decision test

Ask:

> **What decision is still changeable at the moment this behavior is observed?**

If no concrete action can still be changed, the signal is post-decision and should normally die.

Examples of still-open decisions may include:

- buy A vs B;
- repair vs replace;
- switch vs stay;
- apply vs do not apply;
- submit now vs later;
- choose configuration X vs Y;
- accept quote vs challenge;
- book vs wait;
- import vs substitute;
- choose provider/product/tariff/plan;
- escalate vs proceed.

The list is illustrative, not exhaustive.

## Economic-consequence test

The uncertainty must plausibly affect something economically material such as:

- money spent or lost;
- recurring cost;
- avoided error;
- time-to-decision;
- switching cost;
- margin;
- eligibility/benefit value;
- failure/rework risk;
- utilization;
- contractual lock-in;
- asset lifetime;
- opportunity cost.

Do not advance candidates whose consequence is merely curiosity or convenience unless evidence suggests substantial aggregate value.

## Recoverability test

Classify as HIGH / MEDIUM / LOW.

### HIGH

The necessary decision facts are public, user-supplied, derivable, or available from stable authoritative sources.

### MEDIUM

Most facts are recoverable, but one bounded variable requires user confirmation, manual interpretation, or imperfect evidence.

### LOW

The decisive variable depends mainly on private institutional records, inaccessible internal state, case-specific legal judgment, or post-event evidence.

LOW normally dies unless a credible alternate resolution exists that does not require the hidden variable.

## Accessible intervention-path test

This is the new gate.

Ask:

> **If we later created a disposable resolution, could we put it in front of multiple relevant actors through this surface or an adjacent surface without bespoke relationship-building each time?**

Evidence may include:

- exact-intent search surface;
- repeated public questions in a structured category;
- an open comparison/configuration workflow;
- marketplace/listing context where the decision is visible;
- open public feed;
- self-service form or calculator context;
- repeated app/software migration decision surface;
- other public or legitimately accessible repeated behavior.

Do not count a channel that theoretically has many users but requires gatekeeper permission or one-to-one introductions for every exposure.

## Observable-effect test

For serious candidates, state one plausible future behavioral signal that could show whether a resolution helped.

Examples:

- selected option changes;
- user proceeds instead of escalates;
- quote challenged;
- purchase deferred;
- repair/replacement choice changes;
- configuration changes;
- application completed;
- user requests deeper evidence;
- click-through to action;
- repeat use;
- conversion to next step.

This is not yet the experiment design. It tests whether value could become observable.

## Exact-resolution competition gate

For each candidate that survives the upstream gates, search for functional competitors using:

```text
ACTOR × DECISION × INPUTS × RESOLUTION × OUTPUT × TIMING
```

Do not stop at category-level competitors.

A candidate dies when an existing accessible resolution already performs the bounded job adequately at the relevant decision moment.

A residual gap survives only when supported by specific evidence.

## Same-surface advantage

Record whether the surface that revealed the uncertainty could also plausibly become the future intervention surface.

Classify:

- **SAME** — discovery and intervention can plausibly occur on the same surface;
- **ADJACENT** — intervention requires a nearby but low-friction surface transition;
- **SEPARATE** — discovery is public but intervention requires a materially different acquisition channel.

SAME and ADJACENT are preferred but not automatic winners.

This classification is qualitative and must not become a mechanical score.

## Deepening limit

Deepen at most **3 candidates**.

A candidate deserves deepening only if it survives:

- pre-decision timing;
- economic consequence;
- actor visibility;
- recoverability;
- accessible intervention path;
- initial exact-resolution search.

For deepened candidates, inspect enough evidence to characterize:

- repeatedness of the behavior;
- decision timing;
- likely structured inputs;
- exact functional competition;
- plausible disposable resolution;
- future exposure mechanics;
- observable effect;
- likely value-creation mechanism.

Do not design durable products.

## Candidate quality over novelty

Novelty is informative but not a success criterion.

A familiar domain can survive if the specific unresolved decision gap and accessible surface are strong.

A surprising hypothesis still dies if the exact resolution exists or the actor is not accessible pre-decision.

Do not reward originality for its own sake.

## Distribution bias guardrail

Starting from visible surfaces can bias discovery toward:

- digitally literate actors;
- search-friendly problems;
- younger users;
- emotionally expressive problems;
- consumer rather than enterprise contexts;
- problems already served by content/SEO markets;
- platform-specific behavior;
- high-frequency but low-value uncertainty.

Record these biases explicitly.

Do not infer that inaccessible decisions are economically unimportant. The experiment asks whether accessible surfaces are a productive opportunity source for this Engine/operator profile.

## Operator-fit rule

Do not use operator fit to generate candidates.

Evaluate opportunity quality first.

For serious survivors, note whether the accessible intervention topology is compatible with a low-networking, self-service, automation-friendly operator model.

Do not kill a strong opportunity solely because it is personally inconvenient unless the inconvenience is structurally tied to the distribution mechanism.

## Value-capture boundary

Spec 028 is about opportunity discovery, not monetization design.

For serious survivors, state only whether a plausible value-capture mechanism exists in principle.

Do not perform pricing research, payment tests, detailed business-model design, or revenue forecasting.

## Time and cost envelope

Target active research time: **90 minutes**.

Preferred spend: **€0**.

Maximum paid research spend: **€2**, only when a single bounded paid data point has higher expected information value than available open evidence.

Do not spend merely to make the research appear more quantitative.

## Verdicts

### A — ACCESSIBLE-SURFACE FORGE CANDIDATE

At least one candidate survives all current RADAR gates with concrete evidence of:

- economically consequential live uncertainty;
- self-identifying actor;
- recoverable information;
- inadequate exact resolution;
- accessible intervention surface;
- observable future effect;
- plausible value creation.

Recommend exactly one candidate for a disposable FORGE resolution experiment.

### B — ONE BOUNDED UNCERTAINTY

One candidate is materially stronger than the rest but exactly one bounded uncertainty prevents a FORGE handoff.

Recommend exactly one cheap discriminator.

### C — NO SURVIVOR, SURFACE-FIRST DISCOVERY INFORMATIVE

No candidate survives, but the experiment provides meaningful evidence about which accessible surfaces are or are not productive discovery origins.

Recommend the next research-policy adjustment rather than forcing a product candidate.

### D — ACCESSIBLE-SURFACE DISCOVERY FAILURE

The experiment did not obtain adequate surface evidence or candidate generation was too weak to test the hypothesis.

State precisely why.

## Required research economics

Record:

- active time;
- searches/queries performed;
- surface families inspected;
- raw signals inspected;
- hypotheses generated;
- shallow kills;
- candidates deepened;
- paid spend;
- entering uncertainty;
- leaving uncertainty;
- which family produced the strongest candidates;
- which family produced the most false positives;
- whether same-surface/adjacent intervention improved experimentability;
- whether exact-resolution competition remained the dominant kill mechanism;
- evidence yield: HIGH / MEDIUM / LOW.

## Required completion report

Return exactly these sections:

1. Verdict
2. Discovery question tested
3. Surface families inspected
4. Raw signals observed
5. Signal-native hypotheses generated
6. Shallow kills
7. Deepened candidates
8. Pre-decision evidence
9. Economic-consequence evidence
10. Actor self-identification evidence
11. Recoverability
12. Accessible intervention paths
13. Same-surface / adjacent / separate classification
14. Exact-resolution competition
15. Observable future effects
16. Strongest candidate, if any
17. Surface-family productivity
18. Biases and blind spots observed
19. What RADAR learned about accessible decision surfaces
20. What remains unproven
21. Research economics report
22. Architecture/research-policy implications
23. Exactly one recommended next action

## Non-goals

Do not:

- build software;
- create a database or ingestion pipeline;
- add generic surface abstractions;
- contact users or companies;
- send outreach;
- post publicly;
- run ads;
- build landing pages;
- conduct interviews;
- test pricing or willingness to pay;
- accept payments;
- perform broad TAM/SAM/SOM exercises;
- use broad search volume as a substitute for decision specificity;
- generate opportunities from personal preferences first;
- force a survivor;
- reopen the Canadian counter-tariff opportunity unless a materially new distribution fact appears.

## Governing principles

> **Behavioral evidence discovers the question. Authoritative evidence should answer it.**

> **Prefer opportunities whose commercial hypotheses can be falsified cheaply, quickly, and at sufficient sample size.**

> **Experimentability includes the cost of reaching the decision context.**

> **Prefer asymmetries whose affected actors reveal themselves at an accessible pre-decision surface.**

> **Do not broaden a weakly observed hypothesis merely to make the market look larger.**

> **A visible actor is not enough; the decision must still be open.**

> **A surface is especially valuable when discovery and intervention can occur through the same or adjacent interface.**

> **Do not automate uncertainty. First prove that the uncertainty is worth resolving.**
