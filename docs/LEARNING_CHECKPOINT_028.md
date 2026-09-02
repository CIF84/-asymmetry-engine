# Learning Checkpoint 028 — Accessible Decision Surface Discovery

## Outcome

Spec 028 returned **A — ACCESSIBLE-SURFACE FORGE CANDIDATE**.

Starting from observable pre-decision behavior produced one bounded candidate that survived recoverability, economic consequence, accessible intervention, and exact-resolution competition: the customized-CRM stay / upgrade / negotiate / migrate decision.

This is the first candidate discovered specifically through an **accessible decision surface** rather than by discovering an asymmetry first and attempting to locate distribution afterward.

## What was tested

The central question was:

> Can economically consequential opportunities be discovered by starting with public behavior that exposes an actor before a decision, rather than finding an asymmetry first and searching for distribution afterward?

Exactly four surface families were inspected:

1. public Q&A and forum behavior;
2. comparison and configuration workflows;
3. public procurement and request feeds;
4. software/app migration and review surfaces.

Ten signal-native hypotheses were generated. Seven died shallowly, three were deepened, and one survived.

## Core result

The surviving topology is:

```text
ACTOR SELF-IDENTIFIES
        ↓
LIVE DECISION EXPOSED
        ↓
STRUCTURED FACTS PROVIDED
        ↓
ECONOMIC CONSEQUENCE
        ↓
INFORMATION RECOVERABLE
        ↓
RESIDUAL RESOLUTION GAP
        ↓
SAME-SURFACE INTERVENTION
```

This directly addresses the failure exposed by Specs 026–027, where a valid Canadian counter-tariff resolution lacked a low-friction accessible decision surface.

## Surviving candidate

### Customized CRM stay / upgrade / negotiate / migrate

Observed public behavior exposed a small business with a customized Salesforce environment and a still-changeable decision among staying, negotiating, upgrading, migrating to alternatives, adding external tooling, or building internally.

The actor publicly supplied enough structure to make the decision economically and operationally legible, including:

- current and expected seat count;
- current recurring spend and edition constraints;
- required automation/API capabilities;
- custom objects and workflows;
- integrations;
- migration disruption concerns;
- candidate alternatives;
- growth expectations.

The consequence is material: recurring subscription expense, potentially five-figure migration cost, months of implementation effort, workflow rebuilds, training/productivity loss, contractual lock-in, and operational risk.

Recoverability is **MEDIUM–HIGH**. Vendor pricing, editions, documented capabilities, integrations, migration documentation, and standard cost categories are public or authoritative. Business-specific workflow importance, internal effort, quotes, and operational constraints are user-controlled inputs.

Exact implementation effort remains uncertain and must be represented rather than guessed.

## Residual resolution gap

Generic CRM TCO calculators exist. Vendor migration assessments and consultancy processes also exist.

The observed residual gap is narrower:

> An independent pre-commitment resolution that joins the SME's actual workflow dependencies, platform/tier requirements, migration rebuilds, public vendor facts, multi-year economics, and explicit uncertainty into a bounded stay / upgrade / negotiate / migrate decision.

The candidate survives only at this bounded level. It must not silently expand into CRM implementation, migration services, a marketplace, generic software recommendation, or a recommendation engine.

## Important distinction: resolution versus recommendation

The likely value hypothesis is not:

> We know which CRM you should buy.

A more defensible hypothesis is:

> We can turn an opaque platform decision into a smaller set of explicit trade-offs and identify exactly what must be verified before commitment.

Therefore the first FORGE artifact should not force a single recommendation unless the evidence clearly dominates.

It should expose options, economics, workflow risk, reversibility, uncertainty, and next validation actions.

## Evidence classes required

CRM decisions are materially fuzzier than the tariff case. Future resolution work must explicitly separate:

```text
KNOWN
user-supplied current-state facts

PUBLIC FACTS
authoritative vendor pricing, editions, capabilities, documentation

ESTIMATED
migration effort, training cost, rebuild effort, administrative burden

UNKNOWN / VERIFY
workflow parity, edge cases, integration behavior, negotiated price,
implementation duration, other decision-sensitive facts
```

Do not allow modeled assumptions to masquerade as observed facts.

## Surface topology

Spec 028 classified serious candidates by the relationship between discovery and intervention surfaces:

- **SAME** — discovery and intervention can occur on the same surface;
- **ADJACENT** — intervention requires a low-friction transition;
- **SEPARATE** — intervention requires a materially different acquisition channel.

The CRM candidate is **SAME**.

This matters because the actor does not need to be rediscovered after the resolution is constructed. The same public migration context can expose the actor, inputs, clarification, resolution, and observable reaction.

## Discovery versus intervention experimentability

The Engine should preserve the distinction learned in Checkpoint 027:

```text
DISCOVERY EXPERIMENTABILITY
Can RADAR cheaply observe enough evidence
for opportunity discovery and rejection?

                +

INTERVENTION EXPERIMENTABILITY
Can FORGE cheaply place a resolution into
real decisions and observe its effect?
```

Accessible decision surfaces can improve both simultaneously.

## Surface-family learning

### Public Q&A/forums

Strong timing signals, but visible questions can still fail because the decisive variable is physically/private unrecoverable or because an exact resolver already exists.

### Comparison/configuration workflows

Produced many apparent opportunities but all were killed by existing resolution supply. Structured visible uncertainty often means someone has already built the calculator.

This is a useful negative prior, not a prohibition.

### Public procurement

Strong economic consequence and timing, but exact compliance tools and issuer-specific clarification dependencies reduced residual opportunity.

### Software/app migration

Produced the sole survivor. Migration decisions can expose current state, desired state, constraints, recurring cost, switching cost, workflow dependencies, and candidate alternatives before commitment.

Do not generalize from one experiment into a permanent preference for software migration.

## Dominant kill mechanism

**Exact-resolution competition** remained the dominant kill mechanism.

Accessible behavior is not enough. Highly visible structured uncertainty can attract strong incumbent resolution supply.

Therefore the ordered gates remain important:

```text
PRE-DECISION
→ ECONOMIC CONSEQUENCE
→ ACTOR VISIBILITY
→ RECOVERABILITY
→ INTERVENTION ACCESS
→ EXACT RESOLUTION COMPETITION
```

## Biases and blind spots

Accessible-surface discovery favors digitally articulate actors, structured public facts, English-language indexed communities, software/consumer decisions, and actors willing to reveal operational details.

It under-observes sensitive enterprise decisions, offline actors, non-English communities, and decisions contained entirely within trusted professional relationships.

These are discovery biases, not evidence that unobserved problems are economically weaker.

## Current evidence ladder

```text
ACCESSIBLE PRE-DECISION SURFACE        ✓
ACTOR SELF-IDENTIFIES                  ✓
ECONOMICALLY CONSEQUENTIAL DECISION    ✓
RECOVERABLE INPUTS                     ✓
EXACT RESOLUTION GAP                   ✓
SAME-SURFACE INTERVENTION              ✓
────────────────────────────────────────
RESOLUTION PRODUCED                    ← NEXT
RESOLUTION CORRECT / DEFENSIBLE        ?
UNCERTAINTY REPRESENTED                ?
DECISION SPACE REDUCED                 ?
REAL ACTOR EXPOSED                     ?
DECISION EFFECT                        ?
VALUE CREATED                          ?
VALUE CAPTURED                         ?
```

## What remains unproven

For the CRM candidate, Spec 028 does not prove:

- that the decision brief can be produced accurately;
- that public inputs are sufficient;
- that uncertainty can be bounded usefully;
- that the actor would understand or trust it;
- that public communities would welcome the intervention;
- that it changes a decision or next action;
- value creation;
- willingness to pay;
- value capture;
- repeatability;
- market size;
- sustainable maintenance of vendor facts.

## Next uncertainty

The next question is deliberately narrower than market validation:

> **Can FORGE transform the already-observed customized-Salesforce case into a defensible, evidence-linked stay / upgrade / negotiate / migrate decision brief using only the public case facts plus authoritative public evidence, while representing material uncertainty explicitly?**

The artifact should be disposable and manual. No outreach, posting, software, CRM market study, TAM analysis, pricing research, or automation is justified yet.

If the resolution itself cannot be produced defensibly, the candidate should not advance merely because its distribution topology is attractive.
