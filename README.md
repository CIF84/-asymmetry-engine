# Asymmetry Engine

> Observe economic decision friction, track information asymmetries, test ways to resolve them, and learn which resolutions generate durable cash flow.

## Mission

Asymmetry Engine is an evidence-driven system for discovering, monitoring, evaluating, and commercializing information asymmetries visible in public economic behaviour.

The core question is:

> Given observable human decision-making demand on the internet, where does a repeatable information asymmetry exist that can be cheaply collapsed into a useful outcome people will pay for?

The project is not a startup-idea generator.

Its purpose is to create a reusable system that:

1. observes real-world demand signals,
2. detects recurring decision friction,
3. identifies underlying information asymmetries,
4. tracks those asymmetries over time,
5. estimates their economic value and commercial potential,
6. tests multiple monetization models cheaply,
7. records real market outcomes,
8. compounds successful experiments into automated cash-flowing assets.

## Core Thesis

AI is rapidly reducing the cost of software development, research, analysis, content generation, automation, design, personalization, and distribution.

Implementation is becoming less scarce.

What remains valuable is increasingly concentrated around:

- identifying valuable problems,
- finding reliable signals,
- selecting decisions worth solving,
- understanding economic consequences,
- packaging useful outcomes,
- reaching users at the moment of decision,
- earning trust,
- learning from real payment behaviour.

Asymmetry Engine is designed around that shift.

It does **not** assume that every opportunity should become SaaS.

A detected asymmetry may become:

- a decision tool,
- a personalized report,
- a digital product,
- an alerting service,
- a dataset,
- a content engine,
- an affiliate property,
- a lead-generation workflow,
- a micro-SaaS product,
- an API,
- a marketplace,
- or another monetizable workflow.

The productive asset is often not the visible product. It is the **workflow behind the product**.

## System Loop

```text
Signals
   ↓
Observations
   ↓
Decision Demand
   ↓
Asymmetry Detection
   ↓
Asymmetry Registry
   ↓
Monitoring + Scoring
   ↓
Commercial Experiments
   ↓
Revenue Assets
   ↓
Outcomes
   ↺
```

The system is deliberately cyclical.

Experiments create new evidence. Revenue assets generate proprietary data. Failures alter future scoring. Old asymmetries can become newly attractive as markets change.

## What Is an Asymmetry?

An asymmetry exists when a decision has economic value but the information required to make it well is fragmented, difficult to compare, expensive to obtain, changing over time, hidden behind expertise, personalized, computationally tedious, poorly presented, or distorted by incentives.

Example:

```text
Decision:
Should I repair or replace this appliance?

Economic consequence:
€150–€1,000

Information friction:
Repair cost, expected remaining life, replacement cost,
energy use, failure probability, resale value, warranty.

Potential resolution:
A personalized repair-vs-replace recommendation.

Possible monetization:
€5 report, affiliate referral, lead fee, decision tool.
```

## Signal Sources

The system should combine independent sources rather than depend on one platform.

Preferred sources include:

- official APIs,
- public datasets,
- search-demand data,
- trend data,
- advertising-intent data,
- YouTube API data,
- Stack Exchange,
- Hacker News,
- government open data,
- complaint databases,
- open web corpora,
- public pricing and market data.

Scraping should not be a foundational dependency.

For every source, the system should know its access method, usage constraints, commercial-use status, retention requirements, rate limits, and reliability.

## The Asymmetry Registry

Detected asymmetries should persist as first-class objects rather than disappear after each run.

Example:

```text
ASYM-000184

Title:
Optimal smartphone replacement timing

Decision:
Buy now / wait / repair / replace

Domain:
Consumer electronics

Economic consequence:
€100–€500

Observed demand:
High

Transaction proximity:
0.89

Information fragmentation:
0.82

Automation feasibility:
0.91

First observed:
2026-09-01

Last observed:
2026-12-01

Trajectory:
Rising

Status:
WATCHING
```

The registry should retain longitudinal history so the system can distinguish structural asymmetries, emerging asymmetries, temporary asymmetries, accelerating or declining demand, regulatory shocks, technological disruption, and changes in competition or willingness to pay.

## Commercialization Philosophy

The system should not ask:

> What app should we build?

It should ask:

> What is the cheapest credible mechanism for converting this asymmetry into value and testing whether someone will pay for that value?

Possible experiment models include:

| Model | Example | Monetization |
|---|---|---|
| Digital product | guide, report, course | direct purchase |
| Decision tool | calculator, recommender | payment / subscription |
| Content engine | articles, video, newsletter | ads / affiliate |
| Lead engine | high-intent consumer matching | referral / lead fee |
| Intelligence product | data, alerts, rankings | subscription / licence |
| Micro-SaaS | interactive workflow | subscription |
| Marketplace | buyer-provider matching | commission |

One asymmetry may support several models. The system should test the **cheapest credible representation first**.

## Design Principles

### Observe before inventing

Prefer observable demand over speculative ideation.

### Automate discovery aggressively

High-volume signal acquisition, extraction, clustering, scoring, and monitoring should be automated wherever practical.

### Validate monetization cheaply

A payment is stronger evidence than a feature.

### Workflows over applications

Software is one interface to an economic workflow, not the default answer.

### Public signals, proprietary learning

Public data may reveal demand. The accumulating proprietary asset should become taxonomy, historical observations, scoring history, resolved entities, experiment outcomes, conversion data, payment behaviour, and monetization performance.

### Avoid single-platform dependency

No critical pipeline should require one external platform to survive.

### Prefer derived data

Store the economic signal needed for analysis rather than unnecessary archives of user-generated content.

### Fail cheaply

A failed experiment should produce structured learning.

### Revenue before elegance

Architecture is valuable only if it improves the path:

```text
signal → asymmetry → experiment → payment → learning
```

## Initial Scope

The first implementation milestone is intentionally narrow:

> Automatically discover, persist, monitor, and rank real economic information asymmetries from multiple legitimate public signal sources.

No UI is required.

The initial system may simply produce:

```text
opportunities.csv
```

and persist the underlying evidence in SQLite.

The next milestone is more important:

> Use one ranked asymmetry to launch a real monetization experiment.

## Success

The project succeeds when it can repeatedly move through:

```text
observe
  ↓
detect
  ↓
evaluate
  ↓
experiment
  ↓
payment
  ↓
learn
  ↺
```

The long-term objective is not one startup. It is a portfolio of low-maintenance, automated, economically useful assets supported by a continuously improving body of proprietary market intelligence.
