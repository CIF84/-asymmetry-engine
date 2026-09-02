# Spec 014 — Cocoa Paid Pilot

## Status

Commercial experiment specification.

This spec deliberately stops architecture work and tests whether one evidence-backed disequilibrium can move toward a real transaction.

Do not build software unless the experiment itself requires a trivial artifact. The goal is not product development. The goal is economic evidence.

## Objective

Test whether small Czech chocolate and confectionery producers will pay for a lightweight weekly decision aid that translates cocoa-market and supplier information into purchasing and repricing signals.

The experiment should move the evidence ladder from:

```text
observation
→ repeated friction
```

toward:

```text
credible asymmetry
→ plausible resolution
→ commercial proposition
→ intent
→ transaction
```

The primary success criterion is not replies or interviews. It is explicit willingness to pay.

## Candidate

### Actor

Independent Czech chocolate / confectionery producer purchasing cocoa mass, cocoa butter, cocoa powder, or closely related cocoa inputs commercially.

### Decision

When and how much cocoa input to buy, and when input-cost changes justify repricing finished products.

### Observed friction

Existing evidence suggests that producers must reconcile:

- global cocoa benchmarks;
- supplier quotes;
- cocoa mass / butter / powder differences;
- CZK/EUR/USD movements;
- freight and minimum-order effects;
- recipe composition;
- current inventory;
- margin targets;
- retail pricing decisions.

Do not assume this friction creates willingness to pay. That is what the experiment tests.

## Core hypothesis

> At least 3 of 25 qualified Czech producers will explicitly commit to a four-week paid pilot at CZK 490 if shown a credible sample that converts cocoa-input movements into purchasing and repricing guidance.

## Commercial proposition

Working offer:

**Weekly Cocoa Cost & Repricing Brief — Czech SME edition**

Indicative contents:

1. cocoa mass / butter / powder benchmark movement;
2. available Czech/EU supplier quote comparison where publicly observable;
3. CZK conversion and explicit freight assumptions;
4. example input-cost change translated into recipe / SKU margin impact;
5. suggested purchasing or repricing trigger expressed as a decision aid, not financial advice;
6. data timestamp, confidence, and unresolved assumptions.

Pilot:

- duration: 4 weeks;
- delivery: manual email / PDF / spreadsheet as convenient;
- price: CZK 490 total for the pilot;
- no recurring billing infrastructure required;
- no software account required.

The pilot price is intentionally low enough to reduce purchase friction but high enough to distinguish payment intent from polite interest.

## Experiment design

### 1. Build the audience list

Identify 25 qualified Czech businesses that plausibly purchase cocoa inputs commercially.

Prefer:

- craft chocolate makers;
- bean-to-bar producers;
- small confectionery manufacturers;
- specialist pastry / chocolate producers with commercial production.

Exclude businesses that appear to be:

- hobby-only;
- pure retail resellers;
- cafes without meaningful production;
- large industrial manufacturers likely served by enterprise procurement systems;
- businesses with no discoverable decision-maker or legitimate business contact route.

For each candidate record only what is necessary:

```text
business name
website
contact person if public
role if public
business email or official contact channel
why qualified
```

Do not create a CRM system.

### 2. Build one sample brief

Create one manual sample using current public information available at execution time.

The sample must be useful enough that the recipient can judge the proposition.

At minimum show:

```text
CURRENT SIGNAL
- current / recent cocoa benchmark movement

SUPPLIER VIEW
- one or more visible Czech/EU supplier references where available
- quote timestamp and caveats

CZK VIEW
- explicit FX assumption

COST IMPACT
- one illustrative recipe or bill-of-materials example
- show how a cocoa-input movement changes unit cost and gross margin

DECISION TRIGGER
- example rule such as "if landed cocoa-butter input cost remains above X for Y weeks, a Z% SKU price increase would restore prior gross margin"

UNKNOWN
- freight, negotiated pricing, actual recipe, inventory, contract timing, etc.
```

Do not claim knowledge of the recipient's actual economics without their inputs.

### 3. Outreach

Send individually addressed Czech-language messages to 25 qualified businesses.

No bulk automation.

The message must be short and decision-specific. It should explain:

- what problem the sample attempts to solve;
- why the recipient was selected;
- that this is an early manual pilot;
- the price;
- the exact commitment requested.

Avoid asking for a generic "thoughts?" response.

Preferred CTA:

> If this would be useful for your purchasing / repricing decisions, reply `ANO` and I will send the details for the four-week pilot at CZK 490.

A secondary option may offer a short call only if they prefer to discuss the workflow first.

### 4. One follow-up

If there is no reply, send at most one concise follow-up after a reasonable interval.

Do not continue chasing non-responsive contacts.

## Measurement

Record for each qualified recipient:

```text
sent
delivered if knowable
reply
substantive decision-specific reply
interview accepted
explicit paid-pilot commitment
payment completed if practical within test window
rejection reason
```

Do not inflate evidence:

```text
reply ≠ intent
interview ≠ intent
"interesting" ≠ intent
"send me more information" ≠ payment intent
explicit willingness to purchase = intent
actual payment = transaction
```

## Success / narrow / kill rules

### PASS

At least 3 of 25 qualified recipients explicitly agree to purchase the four-week pilot at CZK 490.

If practical payment collection is possible without building infrastructure, actual payment is stronger evidence and should be recorded separately.

### NARROW

1–2 explicit paid-pilot commitments, or substantial repeated decision-specific pain from at least 5 recipients but no clear willingness to pay.

In this case do not build software. Determine whether the issue is proposition, audience, price, or workflow before deciding another test.

### KILL

0 explicit paid commitments AND fewer than 5 substantive decision-specific replies after:

- 25 qualified contacts;
- one follow-up maximum;
- the full experiment window.

Kill or park the cocoa proposition without trying to rescue it through product building.

## Budget

Maximum:

```text
2 person-days of active work
10 calendar days elapsed
€50 cash
```

Do not purchase paid datasets, advertising, software subscriptions, domains, design work, payment systems, or outreach tools unless unavoidable for the experiment and within the cash cap.

## Research discipline

Keep four states separate:

```text
KNOWN
OBSERVED IN THIS EXPERIMENT
INTERPRETED
UNKNOWN
```

Do not convert producer comments into generalized market claims without adequate evidence.

Record rejection reasons verbatim or near-verbatim where possible, but do not persist unnecessary personal information.

## What this experiment is NOT testing

It is not testing:

- whether cocoa is an attractive market in general;
- whether the Asymmetry Engine can automate cocoa analysis;
- whether a dashboard would be useful;
- whether supplier scraping is feasible;
- whether a SaaS product could eventually exist;
- whether the proposition can scale internationally.

It tests one narrow question:

> Will a small number of real Czech producers pay for this decision aid now?

## Explicit non-goals

Do not implement:

```text
new connector
new API integration
supplier scraper
web app
dashboard
payment integration
user accounts
database schema changes
opportunity scoring
LLM workflow
email automation
CRM
marketing site
SEO program
subscription system
```

## Required completion report

Return:

### 1. Experiment execution

- number of businesses screened;
- number qualified;
- number contacted;
- number followed up;
- elapsed time;
- cash spent.

### 2. Sample proposition

Include the actual sample brief structure and the exact outreach message used.

### 3. Funnel

```text
qualified
→ contacted
→ substantive replies
→ interviews
→ explicit paid-pilot commitments
→ payments
```

Report counts and percentages.

### 4. Evidence from replies

Summarize recurring decision friction, current substitutes, rejection reasons, price reactions, and any requested features.

Keep direct evidence separate from interpretation.

### 5. Economic verdict

Choose exactly one:

```text
A — PASS: enough payment intent to run the manual paid pilot.
B — NARROW: meaningful pain exists, but proposition / audience / price needs one more bounded test.
C — KILL: insufficient evidence of willingness to pay.
D — INVALID: experiment execution quality was insufficient to interpret.
```

### 6. Next action

If A:

Run the four-week pilot manually before automating anything.

If B:

Specify one and only one next uncertainty-reducing experiment.

If C:

Park or kill the cocoa proposition and return to the opportunity pool.

If D:

Explain exactly why the experiment was invalid and how to repair the test without changing the proposition opportunistically.

## Principle

> The Engine has earned the right to generate hypotheses. The market must now earn the right for us to build.