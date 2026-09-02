# Spec 027 — Canadian Counter-Tariff Resolution Distribution Feasibility

## Status

FORGE experiment.

Research-only distribution feasibility test. Do not contact prospects, build a product, run ads, or execute the behavioral interaction yet.

## Context

Specs 023–024 demonstrated a bounded Canadian September 8 counter-tariff information asymmetry and a material functional gap in existing public self-service resolutions.

Spec 025 demonstrated that FORGE can manually produce a correct, source-linked, decision-ready exposure brief from already-classified inputs.

Spec 026 attempted to expose that resolution to a real Canadian SME importer/buyer and measure before/after decision effects. It stopped before execution because no qualifying actor was available and obtaining one required external contact.

This is not evidence against the resolution. It exposed a missing empirical layer between resolution construction and behavioral validation: **distribution feasibility**.

## Objective

Answer one question:

> **Is there a plausible, low-friction, repeatable way to expose the bounded Canadian counter-tariff resolution to Canadian importers at the moment they face the relevant decision?**

This experiment tests whether the opportunity has a viable observation/distribution interface. It does not test demand, behavior change, willingness to pay, or scalable customer acquisition.

## Why this question now

The project currently knows:

```text
credible asymmetry                  ✓
recoverable information             ✓
economic consequence                ✓
exact resolution gap                ✓
resolution producible               ✓
resolution correct                  ✓
resolution decision-ready           ✓
distribution path                   ?
real actor exposed                  ?
behavior/value effect               ?
```

Spec 026 showed that interaction cannot simply be assumed after producing a resolution.

Do not solve this by immediately searching for one person to contact. First determine whether the underlying path to relevant decision-makers is plausibly cheap and repeatable.

## Actor and decision boundary

Target actor remains:

**Canadian SME importer or buyer evaluating already-classified goods potentially affected by the September 8 Canadian counter-tariff measure.**

Relevant decision moments include:

- before placing or confirming an import order;
- before shipment/entry when timing matters;
- while evaluating incremental landed cost;
- while deciding whether to reprice, renegotiate, substitute, defer, confirm origin, investigate relief/remission, or escalate.

Do not broaden the actor to generic consumers, trade professionals, large-enterprise compliance teams, or US exporters merely to find easier distribution.

## What counts as a distribution path

A candidate path must plausibly connect:

```text
AFFECTED ACTOR
      ×
RELEVANT DECISION MOMENT
      ×
DISCOVERABLE / REACHABLE SURFACE
      ×
BOUNDED RESOLUTION
      →
INTERACTION OPPORTUNITY
```

Examples of surface classes may include, but are not limited to:

- high-intent search behavior;
- public questions or discussion surfaces;
- importer/procurement/accounting/trade communities;
- industry or SME association surfaces;
- customs/freight/accounting ecosystems;
- existing tariff-information workflows or adjacent tools;
- professional-role discovery surfaces;
- other public surfaces discovered during research.

These are hypotheses, not required channels.

## Distribution feasibility dimensions

For each serious candidate path assess qualitatively:

### D1 — Actor relevance

Does the surface contain the bounded target actor rather than merely adjacent professionals or general interest?

### D2 — Decision timing

Is the actor likely to encounter the surface while the import/repricing decision is still live enough for the resolution to matter?

### D3 — Intent strength

Does observed behavior indicate an active need to resolve exposure/cost/exception uncertainty, or only general awareness/news consumption?

### D4 — Reachability

Can the actor plausibly encounter or request the resolution without bespoke relationship-building, introductions, or repeated one-to-one persuasion?

### D5 — Throughput

Could the path plausibly generate enough independent interactions to learn from, rather than one rare contact at a time?

Do not impose an arbitrary numerical threshold. Assess whether throughput is sufficient for future evidence generation.

### D6 — Friction and dependency

What permissions, platform dependencies, gatekeepers, trust requirements, paid access, or manual effort stand between the resolution and the actor?

### D7 — Resolution fit

Can the Spec 025 bounded input/output format reasonably be delivered through this path, or would the path require a fundamentally different product/problem boundary?

### D8 — Temporal durability

Is the path useful only during the short September 8 implementation window, or does it suggest a repeatable pattern for future tariff/regulatory changes?

Temporal durability is informative but is not itself a reason to broaden the experiment.

## Required research method

### Step 1 — Discover surfaces before judging them

Search for real public evidence of where affected Canadian importers encounter or express the relevant decision uncertainty.

Do not begin with a fixed preferred acquisition channel and then collect confirming evidence.

Look for actor behavior, questions, workflows, communities, search surfaces, adjacent tools, trade guidance surfaces, or other evidence that reveals how the decision is actually navigated.

### Step 2 — Identify candidate paths

Construct no more than **6 candidate distribution paths**.

Each path must state:

- target actor;
- decision moment;
- surface;
- observed evidence that the actor is present;
- how the bounded resolution could reach them;
- principal friction/dependency;
- likely learning throughput.

### Step 3 — Kill weak paths cheaply

Reject paths early when evidence shows:

- wrong actor;
- post-decision timing;
- passive news interest rather than decision intent;
- dependency on bespoke introductions or high-touch sales;
- negligible observable throughput;
- severe platform/permission friction;
- the required artifact would no longer solve the bounded problem.

Do not deepen every channel equally.

### Step 4 — Deepen at most 2 paths

For the strongest one or two paths, inspect enough real evidence to answer whether a future interaction experiment could plausibly obtain multiple relevant exposures without disproportionate effort.

Where useful, inspect current search results, communities, discussion activity, association/workflow surfaces, adjacent services/tools, or public role/activity evidence.

Do not contact anyone.

### Step 5 — Define the cheapest next interaction

Only if at least one path survives, define the smallest concrete interaction experiment that could expose the existing resolution to a relevant actor and observe a behavioral/decision effect.

Do not execute it under this spec.

## Search-intent rule

Search data may be used if it genuinely helps determine whether affected actors express the relevant decision at sufficient intent and reachability.

Do not repeat Spec 016's error of expanding the denominator with adjacent generic terms merely to make a channel appear larger.

Exact or closely decision-linked intent matters more than broad tariff/news volume.

Paid keyword data is not required. Use open evidence by default. A paid research request is allowed only if its expected information value clearly exceeds its cost and the open evidence cannot answer the discriminator.

## Community/public-discussion rule

Public discussion can demonstrate actor presence and decision timing, but do not equate discussion frequency with commercial demand.

Distinguish:

```text
NEWS / COMMENTARY
GENERAL INFORMATION SEEKING
ACTIVE DECISION UNCERTAINTY
REQUEST FOR CASE-SPECIFIC RESOLUTION
```

The latter two are substantially more relevant to distribution feasibility.

## Professional/intermediary rule

Customs brokers, freight forwarders, accountants, trade consultants, and similar professionals may reveal where the decision occurs, but they are not automatically the target actor.

A channel dominated by intermediaries can still be useful if it provides a credible route to the importer decision. State the dependency explicitly.

Do not silently change the customer or actor to the intermediary.

## No outreach boundary

Under Spec 027:

- do not email anyone;
- do not send LinkedIn messages;
- do not post in communities;
- do not submit contact forms;
- do not request introductions;
- do not create accounts solely to message people;
- do not run ads;
- do not publish the artifact or a landing page.

Publicly accessible research and passive inspection are allowed.

If a promising surface requires authentication merely to read evidence, use it only if already legitimately accessible. Do not bypass restrictions.

## Distribution-path evidence standard

A path survives only if there is concrete evidence supporting all of the following propositions:

1. relevant actors are present or reliably reachable;
2. the surface intersects the decision before it is resolved;
3. the uncertainty is close enough to the bounded counter-tariff exposure job;
4. the Spec 025 resolution can plausibly be introduced without fundamentally changing the problem;
5. future experiments could plausibly generate repeated independent observations at reasonable effort.

No single signal proves the path.

## Experimentability lens

For serious paths ask:

> **If we wanted five independent resolution exposures, what would actually have to happen?**

This is not a quota and no five exposures should be obtained now.

Use the question to expose hidden acquisition mechanics such as:

- finding individual companies;
- identifying the right employee;
- gaining permission;
- waiting for a live import decision;
- obtaining sensitive manifest data;
- repeated persuasion;
- platform posting limits;
- trust barriers;
- paid traffic requirements;
- low event frequency.

A path that theoretically reaches the actor but requires bespoke work for every observation is weak for the Engine's current experimental needs.

## FORGE/portfolio-fit interpretation

The goal is not to prove a permanent distribution moat.

The goal is to determine whether this resolution has a sufficiently observable interface with reality to justify another FORGE experiment.

A correct resolution can rationally be parked if its decision context is too difficult to reach.

This is not a failure of the asymmetry thesis. It is evidence about opportunity quality.

## Verdicts

### A — DISTRIBUTION PATH DEMONSTRATED

At least one path has concrete evidence of relevant actor presence, live decision timing, resolution fit, and plausible repeated exposure at reasonable effort.

Next experiment should execute the smallest real interaction through that path.

### B — ONE BOUNDED DISTRIBUTION UNCERTAINTY

One path appears plausible, but exactly one material uncertainty prevents confidence that repeated relevant exposures are obtainable.

Recommend exactly one cheap discriminator.

### C — DISTRIBUTION NOT FEASIBLE ENOUGH / PARK

No investigated path provides a sufficiently low-friction, repeatable interface to the relevant decision.

Recommend PARK for this opportunity despite the demonstrated asymmetry and working resolution.

Do not rescue it by broadening actor, geography, tariff problem, or product scope.

### D — EXPERIMENT INVALID

The required distribution research could not be executed or the evidence was insufficient to evaluate the paths.

State precisely what prevented execution.

## Time and cost envelope

Target active research time: **45–60 minutes**.

A bounded overrun is permitted only when one surviving path needs a small amount of additional evidence to distinguish A/B/C.

Preferred spend: **€0**.

Maximum paid research spend: **€2**, only when justified by expected information gain.

## Research economics report

Record:

- active research time;
- searches performed;
- surfaces inspected;
- candidate paths generated;
- paths killed shallowly;
- paths deepened;
- paid spend;
- entering uncertainty;
- leaving uncertainty;
- strongest evidence;
- weakest assumption;
- whether distribution, rather than resolution, is now the dominant bottleneck;
- evidence yield: HIGH / MEDIUM / LOW.

## Required completion report

Return exactly these sections:

1. Verdict
2. Distribution question tested
3. Public surfaces inspected
4. Candidate distribution paths
5. Shallow kills
6. Deepened paths
7. Actor relevance evidence
8. Decision-timing evidence
9. Intent evidence
10. Reachability and throughput
11. Friction and dependencies
12. Resolution-format fit
13. Five-exposure thought experiment
14. Temporal durability
15. Strongest surviving path, if any
16. What this says about experimentability
17. What remains unproven
18. Research economics report
19. Architecture/framework implications
20. Exactly one recommended next action

## Non-goals

Do not:

- contact prospects;
- acquire a participant;
- execute Spec 026 interaction;
- test comprehension or behavior change;
- test willingness to pay;
- test pricing;
- run ads;
- build a landing page;
- build software;
- create an importer database;
- scrape at scale;
- build acquisition automation;
- expand to general Canadian tariffs;
- expand to US exporters or other jurisdictions;
- perform broad market sizing;
- redesign the Spec 025 artifact unless a distribution incompatibility is directly observed;
- create generic distribution architecture.

## Governing principles

> **FORGE makes something capable of interacting with reality.**

> **Disposable before durable.**

> **An experiment that cannot observe its target behavior is invalid, not negative.**

> **Experimentability includes the cost of reaching the decision context.**

> **A real asymmetry with a working resolution can still be a poor opportunity if its interface with reality is too expensive.**

> **Do not broaden the problem to rescue the experiment.**
