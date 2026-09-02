# Spec 013 — Commercial Translation Pressure Test

## Status

Research specification. No production implementation is expected by default.

This spec deliberately shifts the project from architecture discovery toward **economic evidence**.

Spec 012 demonstrated that the Engine can construct an inspectable evidence-backed economic argument. The next uncertainty is no longer whether the reasoning layer can exist. It is whether any currently observed disequilibrium can be translated into a credible, reachable, monetizable information asymmetry.

## Objective

Take a small set of real evidence-backed cases already discovered by the project and test the chain:

```text
DISEQUILIBRIUM
    ↓
ECONOMIC CONSEQUENCE
    ↓
AFFECTED ACTOR
    ↓
DECISION / INFORMATION FRICTION
    ↓
ASYMMETRY
    ↓
POSSIBLE RESOLUTION
    ↓
VALUE-CAPTURE MECHANISM
    ↓
DISTRIBUTION PATH
    ↓
CHEAPEST COMMERCIAL TEST
```

The goal is not to invent business ideas around interesting data.

The goal is to determine whether any observed disequilibrium creates a **specific decision problem for a reachable actor** that can plausibly support a repeatable commercial mechanism.

## Why this slice now

The project has enough infrastructure for the moment:

- multiple orthogonal evidence families;
- hierarchical decomposition;
- semantic decomposition;
- an inspectable reasoning vertical slice;
- explicit lineage and supported/not-supported boundaries.

Adding more architecture or another connector before testing commercial translation would risk optimizing the Engine without evidence that its outputs can produce economic value.

Primary project metric remains:

> **TIME TO ECONOMIC EVIDENCE**

## Cases to pressure-test

Use these four evidence-backed cases from the completed research. Do not substitute unrelated trends merely because they appear more exciting.

### Case A — CN75 nickel alloys

Known evidence:

```text
Czech CN75 imports 2023→2024
value +26.74%
net mass +47.60%
derived value-per-mass -14.13%

CN8 75022000 unwrought nickel alloys
>100% of net CN75 value increase
~78% of net mass increase
France + Italy explain nearly all selected-child growth
supplier concentration increased
```

### Case B — CN18 cocoa and cocoa preparations

Known evidence:

```text
Czech imports 2023→2024
value +27.65%
mass +1.20%
derived value-per-mass +26.14%

value growth distributed across several cocoa inputs/preparations
some important products increased in value while physical mass fell
```

### Case C — CN85 batteries / photovoltaics versus consumer electronics

Known evidence:

```text
CN85 total value ~flat/slightly down
large opposing child movements

lithium-ion accumulators -€1.405bn
photovoltaic modules -€213.7m
smartphones +€702.3m
processor/controller ICs +€677.7m

supplier geography shifted materially
```

### Case D — CN28 bulk chemicals versus precious-metal compounds

Known evidence:

```text
CN28 total value -14.72%
mass +14.85%

high-value precious-metal compounds contracted sharply
bulk ammonia / sodium hydroxide / sulphuric acid mass expanded
strong supplier substitution visible in precious-metal compounds
```

## Research questions

For each case answer, in order:

1. **What exactly changed?**
   - Use only the evidence already established by Specs 010/012 as the starting point.
   - Do not reinterpret trade value-per-mass as market price.

2. **Who could economically care?**
   Identify concrete actor classes, for example:

```text
consumer
procurement manager
small manufacturer
importer / distributor
retailer
investor
supplier
service provider
policy/compliance actor
```

Do not assume an actor has a problem merely because the data is unusual.

3. **What decision could become harder, more valuable, or newly necessary because of the change?**

A valid answer must name a decision, not a theme.

Bad:

```text
battery market intelligence
```

Better:

```text
which supplier / substitute / purchase timing minimizes expected sourcing risk for a small Czech installer?
```

4. **What information asymmetry might exist?**

Distinguish:

```text
PUBLIC FACT
what anyone can observe

FRICTION
why the actor cannot easily turn the fact into a decision

ASYMMETRY
what useful synthesized / timely / comparative / predictive information is not cheaply available to that actor
```

5. **What would resolve the asymmetry?**

Possible resolution forms include:

```text
comparison
alert
benchmark
forecast
calculator
supplier map
price / availability tracker
decision assistant
report
dataset
lead-generation surface
```

6. **Can value be captured?**

For each plausible resolution identify the most realistic mechanisms:

```text
one-time digital purchase
subscription
affiliate
lead generation
advertising
sponsorship
API/data product
B2B seat
paid report
transaction fee
```

Do not equate monetization mechanism with willingness to pay.

7. **Can the actor be reached cheaply?**

Investigate realistic distribution channels. Prefer self-service / low-support channels where possible:

```text
search intent
organic content
comparison/search pages
marketplace traffic
communities
email alerts
browser / web utility
affiliate ecosystems
programmatic SEO
```

Record if the opportunity fundamentally requires outbound sales, procurement relationships, regulated advice, or high-touch enterprise selling.

8. **Does a solution already exist?**

Perform a live competition / substitute search for the exact decision problem, not merely the broad market.

Look for:

```text
specialist tools
comparison sites
consultancies
newsletters
market intelligence vendors
marketplaces
free government tools
industry associations
existing dashboards
search-result saturation
```

Competition can invalidate or narrow the hypothesis.

9. **What key uncertainty dominates now?**

Examples:

```text
actor pain
frequency
willingness to pay
solution saturation
access to required data
distribution cost
regulatory burden
repeatability
```

10. **What is the cheapest test that could falsify the commercial hypothesis?**

Prefer tests such as:

```text
landing page
search-demand check
manual report sample
alert signup
calculator prototype
comparison page
small paid-search test
affiliate click test
preorder / payment intent
```

Do not build the full product.

## Commercial translation table

Return one comparable table with at least these fields:

| Field | Meaning |
|---|---|
| Case | Evidence-backed disequilibrium |
| Actor | Who may care |
| Decision | Exact decision to be improved |
| Friction | Why that decision is difficult today |
| Candidate asymmetry | Missing useful information / synthesis |
| Resolution | Cheapest plausible solution form |
| Monetization | Plausible value-capture mechanism |
| Distribution | Cheapest credible acquisition path |
| Existing alternatives | Main substitutes / competitors |
| Evidence gap | Dominant remaining uncertainty |
| Cheapest falsification test | Next experiment |
| Commercialization distance | Near / medium / far |
| Operator fit | High / medium / low, with reason |

## Scoring discipline

Do not produce a fake 0–100 ranking.

Use only coarse comparative judgments:

```text
asymmetry strength: weak / medium / strong
commercialization distance: near / medium / far
distribution plausibility: weak / medium / strong
operator fit: low / medium / high
confidence: low / medium / high
```

Every judgment must have a short reason.

Opportunity quality and operator fit must remain separate.

A commercially strong B2B industrial opportunity may still have low operator fit. Do not downgrade its objective quality merely because it would require sales or networking.

## Research discipline

### Evidence versus hypothesis

For every case maintain explicit sections:

```text
KNOWN FROM EXISTING EVIDENCE
NEW EXTERNAL EVIDENCE
INTERPRETATION
COMMERCIAL HYPOTHESIS
UNKNOWN / FALSIFIER
```

Do not blur them.

### Search narrowly enough to kill ideas

Search for the exact proposed resolution and decision problem.

Examples:

```text
not: cocoa prices
but: cocoa input cost alert for small confectionery manufacturers

not: battery market
but: battery sourcing / inventory / installation decision tool for Czech solar installers
```

The purpose is not to collect competitor names. It is to determine whether the information gap actually exists.

### No architecture work

Do not modify:

```text
reasoning.py
observation schema
source adapters
entity models
relationship models
CLI
```

Do not add a connector merely because a useful external source is discovered during research.

Temporary scripts and direct web/API research outside the repository are acceptable when needed.

## Selection decision

At the end, choose exactly one of:

```text
A — One case deserves an immediate commercial experiment.
B — One case is promising but one cheap evidence check is required before experimentation.
C — None of the four currently justify commercial experimentation; return to discovery.
D — A commercially strong opportunity exists but is structurally incompatible with the preferred operator model; park it explicitly.
```

If A or B, identify **one primary candidate** only.

The candidate must include:

```text
actor
exact decision problem
proposed resolution
monetization mechanism
distribution hypothesis
cheapest next test
success signal
kill signal
maximum time budget
maximum cash budget
```

The time and cash budgets should be deliberately small enough that failure is cheap.

## Economic-evidence ladder

State where the selected candidate currently sits:

```text
observation
→ repeated friction
→ credible asymmetry
→ plausible resolution
→ commercial proposition
→ visitor
→ intent
→ transaction
→ repeat transaction
```

Do not claim advancement beyond the evidence actually observed.

## Required completion report

Return:

### 1. Research scope

- sources/search surfaces used
- approximate number of live searches / API calls
- any cost incurred
- any access/licensing limitation encountered

### 2. Four-case translation table

Return the complete comparable table.

### 3. Per-case findings

For each case:

```text
KNOWN FROM EXISTING EVIDENCE
NEW EXTERNAL EVIDENCE
INTERPRETATION
COMMERCIAL HYPOTHESIS
COMPETITION / SUBSTITUTE PRESSURE
UNKNOWN / FALSIFIER
```

### 4. Candidate comparison

Compare:

```text
asymmetry strength
commercialization distance
distribution plausibility
operator fit
confidence
```

No precision scoring.

### 5. Selection verdict

Choose A/B/C/D and explain.

### 6. Cheapest next experiment

If A or B, specify exactly one experiment with:

```text
hypothesis
audience
artifact / offer
channel
call to action
measurement
success threshold
kill threshold
time budget
cash budget
```

### 7. Architecture implication

Answer only:

- Did commercial translation require any new software architecture?
- Which existing reasoning output was useful?
- Which existing reasoning output was irrelevant to commercialization?
- What information would the Engine eventually need to collect automatically if this experiment succeeds?

Do not implement those implications yet.

## Explicit non-goals

Do not implement:

```text
new connectors
persistent opportunity tables
opportunity dashboard
scoring engine
LLM agent
web UI
payment system
landing page
prototype product
cross-source ontology
knowledge graph
commercial automation
```

This is a **commercial hypothesis pressure test**, not a build phase.

## Decision after Spec 013

The next implementation should be determined by economic evidence.

If a candidate survives, the next spec should describe the cheapest real-world experiment that can move the candidate one rung further on the economic-evidence ladder.

If none survive, return to discovery with explicit knowledge about why the existing cases failed commercially.
