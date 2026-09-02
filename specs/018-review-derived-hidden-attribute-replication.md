# Spec 018 — Review-Derived Hidden Attribute Replication

## Status

Research-only replication test. No production implementation.

## Context

Spec 017 found behavioral-first discovery to be **PARTIALLY SUPPORTED** and identified reviews as the most productive signal class in that bounded pass.

The useful pattern was not simply that reviews contain complaints. It was that some reviews reveal **decision-relevant attributes that were not sufficiently visible before purchase**.

Examples from Spec 017 included:

```text
cabin luggage
seller claim: airline compatible
experienced reality: wheels / handles cause sizer failure

small-team SaaS
advertised price: per-seat price
experienced reality: minimum-seat floor changes effective team cost
```

These examples suggest a potentially reusable discovery mechanism:

```text
POST-PURCHASE EXPECTATION FAILURE
→ identify hidden / conditional attribute
→ ask whether buyer could have benefited from knowing it before purchase
→ ask whether attribute is recoverable before purchase
→ ask whether market already exposes it adequately
→ infer residual information asymmetry
→ derive smallest resolution
```

The risk is obvious: a review miner can easily become a sophisticated complaint collector. Many negative reviews concern stochastic quality failures, poor service, emotional disappointment, or facts that cannot be known before purchase.

This spec therefore tests a stricter proposition:

> Can review evidence repeatedly reveal commercially meaningful attributes that buyers could have benefited from knowing before purchase, that are recoverable before purchase, and that existing market information does not already expose well?

Do not promote reviews into a permanent RADAR source class yet.

## Objective

Test whether review-derived hidden-attribute discovery generalizes across unrelated product categories.

The method should succeed only when it finds attributes that are all of the following:

- hidden, omitted, conditional, inconsistently measured, or poorly surfaced before purchase;
- materially relevant to a purchase decision or economic outcome;
- observable or inferable before purchase with a credible data-acquisition path;
- insufficiently exposed by existing seller, marketplace, comparison, or specialist information;
- repeated enough to be more than an isolated anecdote;
- potentially resolvable through an information product, comparison, verification layer, benchmark, or decision aid.

The goal is to test the **discovery mechanism**, not to select a startup idea by force.

## Core distinction

Preserve this separation:

```text
NEGATIVE REVIEW
≠ HIDDEN ATTRIBUTE

HIDDEN ATTRIBUTE
≠ DECISION-RELEVANT ATTRIBUTE

DECISION-RELEVANT ATTRIBUTE
≠ PRE-PURCHASE RECOVERABLE ATTRIBUTE

RECOVERABLE ATTRIBUTE
≠ RESIDUAL COMMERCIAL ASYMMETRY
```

A review is only the starting observation.

## Research design

Select exactly **three unrelated product or plan categories**.

The categories should be economically meaningful and should differ materially in how attributes are represented. Avoid choosing three near-identical consumer-goods categories.

Good category diversity may include combinations such as:

- physical durable / travel product;
- subscription software / digital service;
- household / mobility / financial / utility product;
- other categories where reviews describe expectation failures.

Do not select a category solely because Spec 017 already identified an attractive solution.

At most one of the three categories may reuse a Spec 017 example as a calibration case.

## Sample size

Inspect a maximum of **15 recent negative or mixed reviews per category**.

Maximum total sample:

```text
3 categories × 15 reviews = 45 reviews
```

Use actual review text or sufficiently detailed public excerpts.

Prefer recent reviews where possible.

Do not collect reviewer personal information.

Do not contact reviewers.

Do not scrape at scale or add ingestion tooling.

Manual public research is sufficient.

## Sampling discipline

The sample is not statistically representative of the entire market.

Do not estimate prevalence from the share of sampled negative reviews.

The sample exists to discover whether the same **decision-relevant hidden variable** appears independently more than once.

Treat repeated appearances as hypothesis-strengthening evidence, not market-frequency estimates.

Avoid cherry-picking multiple reviews that clearly repeat the same syndicated complaint or copied text.

## Review coding

For every inspected review, classify the primary issue into one of these categories:

- **HIDDEN / OMITTED ATTRIBUTE** — a relevant property was not disclosed or was difficult to discover before purchase;
- **CONDITIONAL ATTRIBUTE** — the property depends on buyer context, configuration, geography, usage, team size, compatibility, etc.;
- **INCONSISTENT MEASUREMENT / DEFINITION** — seller and buyer interpret a measurement, price, capacity, size, performance claim, or category differently;
- **POST-PURCHASE REVEAL** — an economically material condition appears only after signup, checkout, activation, installation, or use;
- **SERVICE / PROCESS FAILURE** — support, delivery, refund, billing administration, or execution problem rather than information asymmetry;
- **STOCHASTIC QUALITY / DURABILITY** — failure that could not reasonably be known for the exact purchased unit before purchase;
- **PREFERENCE / EXPECTATION** — subjective disappointment without a recoverable hidden fact;
- **OTHER / UNCLEAR**.

The last four classes should normally **not** produce an asymmetry candidate unless a separate recoverable attribute emerges.

## Pattern extraction

Within each category, group reviews only when they reveal the same underlying decision variable.

Examples:

```text
"wheels make bag too large"
"55 cm stated size excludes handles"
"bag fails airline sizer despite listed dimensions"

may group into:
EXTERNAL DIMENSION DEFINITION / PROJECTION INCLUSION
```

But:

```text
"zipper broke"
"wheel broke"
"fabric tore"
```

should not be grouped into a generic `quality` hidden attribute unless a credible pre-purchase measurable variable exists.

## Replication gate

Do **not** use a mechanical `3 reviews = pass` rule.

A pattern may advance to causal reconstruction when:

1. it appears in **multiple independent reviews** in the bounded sample; and
2. the attribute plausibly changes purchase choice, total cost, compatibility, return risk, or other meaningful economic outcome.

Strengthen confidence when there are three or more independent examples, but frequency alone is insufficient.

A two-review pattern may remain credible if the economic consequence and causal mechanism are strong.

A five-review pattern should still fail if it concerns a trivial annoyance or non-recoverable stochastic outcome.

## Required hidden-attribute test

For each pattern that survives the replication gate, answer all of the following.

### 1. What is the hidden variable?

Name the actual variable, not the complaint topic.

Bad:

```text
bad luggage sizing
```

Better:

```text
whether listed external dimensions include wheels and handles
```

### 2. Why does it matter economically?

Identify the decision consequence:

- purchase / no purchase;
- product choice;
- plan choice;
- total cost;
- compatibility;
- return/refund risk;
- switching cost;
- downtime;
- penalty / fee;
- other material consequence.

### 3. Could the buyer benefit from knowing it before purchase?

If not, stop.

### 4. Is it recoverable before purchase?

This is the central discriminator.

Classify recoverability as:

- **DIRECTLY RECOVERABLE** — seller/manufacturer/source data already exists but is poorly exposed or normalized;
- **DERIVABLE** — can be inferred by combining public or obtainable inputs;
- **MEASURABLE** — could be established through repeatable physical / technical / transactional measurement;
- **CROWDSOURCABLE** — could plausibly be established from structured user evidence;
- **NOT PRACTICALLY RECOVERABLE** — only knowable after stochastic use or private future events.

Reject `NOT PRACTICALLY RECOVERABLE` patterns from commercial-asymmetry promotion.

### 5. Who currently knows more?

Identify whether the advantage belongs to:

- seller;
- manufacturer;
- platform;
- specialist/intermediary;
- experienced users collectively;
- data aggregator;
- no one reliably.

If no actor or derivation process can plausibly know more, information-asymmetry framing may be wrong.

### 6. How is the market solving it today?

Inspect exact substitutes:

- seller pages;
- marketplace filters;
- comparison engines;
- specialist tools;
- forums;
- browser extensions;
- regulators;
- professional services;
- structured reviews;
- simple search.

### 7. What residual gap remains?

State why the information is still hard to obtain at the point of decision.

If the answer is merely `users do not bother looking`, do not assume a commercial asymmetry.

### 8. What is the data-acquisition path?

Specify how the attribute could be obtained repeatedly without heroic manual work.

Examples:

- manufacturer specifications;
- structured marketplace data;
- seller terms;
- public tariff/pricing data;
- user-submitted measurements;
- verified purchase evidence;
- APIs;
- public datasets;
- bounded manual enrichment followed by reusable structure.

If no credible path exists, record the candidate as **DATA-COLD-START / NON-SCALABLE**.

### 9. What is the smallest resolution?

Examples:

- verified attribute card;
- effective-cost calculator;
- compatibility checker;
- normalized comparison;
- warning / alert;
- claim verifier;
- benchmark;
- structured evidence layer.

Do not design a full product.

### 10. What behavior would reveal value cheaply?

Examples:

- exact-SKU lookup;
- comparison completion;
- alternative-product click;
- warning acknowledgement;
- save/share;
- affiliate redirect;
- priced intent.

Keep the evidence ladder explicit.

## Exact-solution pressure test

Only for patterns that survive the hidden-attribute test, perform a bounded exact-solution competition check.

Ask:

> Can a buyer already verify this exact attribute easily at the point of intent?

Do not reject a candidate merely because broad comparison sites exist.

Reject or materially weaken it when an existing free or dominant solution already exposes the **same hidden variable** with similar or better data coverage.

Distinguish:

```text
generic category comparison
vs
exact hidden-attribute verification
```

## Commercial evaluation

For surviving candidates, assess qualitatively:

```text
ATTRIBUTE CONSEQUENCE
× RECOVERABILITY
× RESIDUAL INFORMATION GAP
× DATA ACQUISITION FEASIBILITY
× DISTRIBUTABILITY
× EXPERIMENTABILITY
× COMMERCIAL VALUE
× OPERATOR FIT
```

Do not create a weighted scoring engine.

Do not let operator fit redefine underlying opportunity quality.

## Decision rule

At the end choose exactly one verdict:

### A — REPLICATED

Use only if review evidence across multiple categories repeatedly reveals pre-purchase-recoverable, economically meaningful hidden attributes, and at least one survives exact-solution and data-feasibility pressure.

Implication: review-derived hidden-attribute discovery deserves another bounded step, potentially testing one candidate behaviorally.

### B — PARTIALLY REPLICATED

Use if the mechanism works in one or more categories but is inconsistent, heavily category-dependent, or usually blocked by recoverability / competition / data acquisition.

Implication: preserve the method as a complementary research heuristic but do not promote reviews into dedicated infrastructure.

### C — NOT REPLICATED

Use if most review patterns are service failures, stochastic quality problems, preferences, already-solved attributes, or non-recoverable facts.

Implication: do not deepen review-first discovery now.

### D — BLOCKED

Use only if public review evidence cannot be inspected within the bounded scope.

Do not substitute invented review examples.

## Required synthesis

Answer these explicitly.

### Q1 — Does the hidden-attribute pattern replicate across unrelated categories?

State where it worked and where it failed.

### Q2 — Which filter removed the most false opportunities?

Choose from:

- decision relevance;
- pre-purchase usefulness;
- recoverability;
- exact-solution competition;
- data-acquisition feasibility;
- economic consequence;
- other.

### Q3 — Are reviews discovering asymmetries, or merely describing dissatisfaction?

Give a bounded answer from this sample.

### Q4 — Did any candidate survive all filters?

If yes, identify at most **one leading candidate** and explain why.

Do not authorize implementation automatically.

### Q5 — What single next action has the highest expected information value?

Choose at most one:

- behavioral test of one surviving candidate;
- deeper data-feasibility check for one candidate;
- replication in another signal class;
- preserve method and return to broader RADAR selection;
- stop review-first exploration.

## Required completion report

Return:

1. three categories selected and why they are sufficiently unrelated;
2. review sources and exact review counts;
3. coded review table or concise per-review coding summary;
4. repeated hidden-attribute patterns found;
5. rejected patterns and rejection reason;
6. hidden-attribute causal reconstruction for every surviving pattern;
7. recoverability classification;
8. exact-solution competition findings;
9. data-acquisition feasibility;
10. qualitative commercial evaluation;
11. verdict A/B/C/D;
12. answers to Q1–Q5;
13. exactly one recommended next action;
14. architecture implications separated into:
   - evidence worth preserving;
   - hypotheses too early to institutionalize.

## Budget

- Cash: **€0**.
- Research time: **4 hours maximum**.
- Reviews: **45 maximum**.
- Categories: **exactly 3**.
- No software implementation.
- No outreach.
- No advertising.

If the method cannot demonstrate value within these bounds, treat that as evidence against further deepening rather than expanding scope.

## Non-goals

Do not:

- build a review collector;
- scrape reviews at scale;
- add a sentiment model;
- add connectors;
- modify production code;
- create a behavioral ontology;
- create an attribute ontology;
- create an opportunity scoring framework;
- build a product;
- buy ads;
- contact reviewers or vendors;
- collect personal information;
- infer population prevalence from the negative-review sample;
- treat complaint frequency as willingness to pay;
- force all three categories to produce candidates;
- revisit the appliance paid-search forecast;
- rewrite architecture documents.

## Governing principles

> Reviews are post-purchase evidence. Their commercial value lies only in what they can reveal about preventable pre-purchase uncertainty.

> Frequency strengthens a hypothesis; economic consequence and recoverability determine whether it matters.

> A hidden attribute is useful only if it can be surfaced before the decision it would change.

> Data acquisition is part of the opportunity, not an implementation detail to postpone.

> Exact-solution pressure must test the hidden variable itself, not merely whether broad competitors exist.

> Let the method fail when the evidence says it should.
