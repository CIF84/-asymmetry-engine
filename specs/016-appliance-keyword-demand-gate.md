# Spec 016 — Appliance Keyword Demand Gate

## Status

Research-only distribution check. No production implementation by default.

## Context

Spec 015 selected the Czech exact-appliance repair-quote decision as the leading candidate, but only conditionally.

The dominant uncertainty is not whether the decision exists. It is whether a sufficiently large, sufficiently specific Czech intent surface exists to support a behaviorally meaningful experiment.

The candidate is:

```text
owner of failed washing machine / dishwasher / refrigerator
→ repair, second quote, or replace
→ fragmented quote / age / remaining life / energy / replacement-cost information
→ exact-appliance decision aid
→ repair lead and/or replacement affiliate later
→ high-intent search
→ completed assessment + recommended-action click
```

Spec 015 therefore returned verdict **B**: one bounded evidence check is required before any behavioral artifact is built.

This spec performs only that check.

## Objective

Determine whether Czech search demand around **repair-cost evaluation and repair-versus-replace decisions** is large and specific enough to justify a small behavioral experiment.

The question is:

> Can we plausibly acquire enough decision-specific Czech visitors to learn from user behavior without spending disproportionate time or cash?

## Evidence source

Use the existing DataForSEO Google Ads Search Volume Live capability if credentials are available.

Required scope:

- Czech Republic location;
- Czech language;
- Google Ads search-volume live endpoint already used by the project;
- one request maximum;
- approximately 20 manually selected seed phrases;
- no automatic keyword expansion;
- no new connector or adapter;
- no production code changes.

If credentials are unavailable, stop and report **BLOCKED — CREDENTIALS REQUIRED**. Do not substitute invented estimates, Google Trends, generic SEO articles, or broad web-result counts for the requested volume check.

## Seed design

Seeds must focus on the actual economic decision, not generic appliance shopping or DIY troubleshooting.

Include three appliance families:

- washing machine;
- dishwasher;
- refrigerator.

Include phrase families such as:

```text
vyplatí se opravit pračku
oprava pračky nebo nová
cena opravy pračky
kolik stojí oprava pračky
servis pračky cena
životnost pračky
opravit nebo koupit novou pračku

vyplatí se opravit myčku
oprava myčky cena
oprava myčky nebo nová
opravit nebo koupit novou myčku
životnost myčky

vyplatí se opravit lednici
oprava lednice cena
oprava lednice nebo nová
opravit nebo koupit novou lednici
životnost lednice
```

Add only a few exact-failure / quote-oriented variants if they materially sharpen intent.

Do not pad the request with broad terms such as:

```text
pračka
myčka
lednice
nejlepší pračka
nová pračka
oprava pračky
```

unless used only as clearly separated context and excluded from the decision-demand total.

## Required fields

For each seed capture, where returned:

- keyword;
- average monthly search volume;
- recent monthly search history if available;
- competition level/index;
- low/top-of-page CPC estimate;
- high/top-of-page CPC estimate;
- source timestamp / request date.

Preserve source wording and distinguish missing values from zero.

## Classification

Classify each phrase manually into one of:

- **DECISION-SPECIFIC** — explicitly evaluates repair economics, quote, repair vs replace, remaining life, or equivalent;
- **REPAIR-INTENT BUT AMBIGUOUS** — likely repair need but may simply seek service or troubleshooting;
- **GENERIC / EXCLUDE** — shopping, DIY, informational, or otherwise not attributable to the proposed proposition.

Do not let ambiguous or generic volume rescue a weak decision-specific result.

## Analysis

Produce:

1. total monthly volume for DECISION-SPECIFIC phrases;
2. total monthly volume for REPAIR-INTENT BUT AMBIGUOUS phrases;
3. appliance-family split;
4. concentration of volume among top phrases;
5. CPC range relevant to a small paid-search test;
6. rough number of visits obtainable under a €60 test budget using low/base/high CPC sensitivity;
7. whether seasonality or month volatility materially changes interpretation;
8. whether query phrasing suggests users hold an actual economic decision rather than merely seeking a repair provider.

Do not turn search volume into traffic or conversion certainty. Explicitly state the chain:

```text
search demand
→ ad eligibility / ranking
→ impression
→ click
→ qualified session
→ completed assessment
→ recommended-action click
```

## Gate

Use these thresholds as decision aids, not pseudo-precision.

### PASS

Proceed to a behavioral experiment if all are broadly true:

- at least three DECISION-SPECIFIC phrases have recurring measurable demand;
- combined DECISION-SPECIFIC demand is approximately **200+ searches/month**;
- demand is not almost entirely one misleading or generic phrase;
- CPC sensitivity suggests a €60 test could plausibly acquire enough qualified sessions to learn from behavior;
- search intent is reasonably aligned with repair-versus-replace / quote evaluation.

### FAIL

Return to candidate selection if either is broadly true:

- combined DECISION-SPECIFIC demand is approximately **below 50 searches/month**; or
- measurable volume is almost entirely generic repair/provider or replacement-shopping demand, making proposition attribution weak.

### AMBIGUOUS

If decision-specific demand is roughly **50–200 searches/month**, or CPC/intent quality creates uncertainty:

- inspect the few contributing SERPs manually;
- do not expand keyword research;
- return a bounded verdict on whether the channel is plausibly testable.

## Required verdict

Choose exactly one:

- **A — PASS: build the smallest behavioral experiment**
- **B — AMBIGUOUS: one tightly bounded discriminator remains**
- **C — FAIL: search is not a sufficiently powerful observation channel for this candidate**
- **D — BLOCKED: credentials or source access unavailable**

Do not force A.

## Required completion report

Return:

1. request scope and cost;
2. exact seed list;
3. raw returned metrics table;
4. manual intent classification;
5. decision-specific demand total;
6. ambiguous repair-intent total;
7. appliance-family split;
8. CPC / €60 traffic sensitivity;
9. measurement limitations;
10. verdict A/B/C/D;
11. exact implication for the next step.

If A, do **not** build the artifact in the same spec. State what Spec 017 should test.

If C, do not rescue the opportunity with another channel unless there is already concrete evidence that another channel offers materially better experimentability.

If D, report precisely which credential/environment variable is missing and stop.

## Non-goals

Do not:

- build a landing page or calculator;
- modify production code;
- add keyword-expansion logic;
- add a new source connector;
- buy ads;
- enroll in affiliate programs;
- collect personal data;
- contact repair businesses;
- create payment infrastructure;
- register a business;
- infer demand from broad appliance terms.

## Budget

- Cash: hard cap €5.
- Requests: one.
- Operator time: 90 minutes maximum.

## Governing principle

> Before testing the proposition, verify that the measurement channel itself has enough power to teach us something.
