# Learning Checkpoint — Spec 025

**Checkpoint date:** 2 September 2026  
**Scope:** Spec 025  
**Milestone:** First decision-ready FORGE resolution

## Outcome

Spec 025 returned **A — DECISION-READY RESOLUTION PRODUCED**.

A standalone 12-line Canadian counter-tariff exposure brief was produced and validated without durable software, paid data, outreach, or external participants.

All 12 lines passed core-truth, provenance, boundary, arithmetic, and decision-clarity validation.

The experiment took approximately 30 minutes and €0.

## 1. FORGE can resolve the demonstrated asymmetry

The central Spec 025 question was:

> **Can FORGE transform the demonstrated asymmetry into a trustworthy, decision-ready Canadian counter-tariff exposure brief from already-classified inputs without building durable software?**

For the bounded manifest, the answer is yes.

```text
KNOWN HS ITEM
+
ORIGIN
+
VALUE
+
DATE
+
BOUNDED EXCEPTION FACTS
+
CURRENT AUTHORITATIVE RULES
        ↓
DECISION-READY RESOLUTION
```

The artifact contained exposure status, rate, incremental cost, material uncertainty, authoritative provenance, freshness, and exactly one primary next action per line.

## 2. The first resolution was cheap once the problem was correctly bounded

A notable result is the asymmetry between discovery effort and resolution-construction effort.

Specs 021–024 progressively established:

- candidate quality;
- signal-native discovery;
- timing;
- recoverability;
- exact functional competition;
- the residual decision gap.

Once that problem was precisely specified, the first resolution required only about 30 minutes.

This supports a working hypothesis:

> **The expensive intellectual work may often be selecting and specifying the right resolution problem rather than constructing the first disposable resolution.**

This is not yet a universal claim. It is one empirical observation from the first FORGE handoff.

It strongly supports keeping early FORGE work disposable.

## 3. Current evidence ladder

```text
OBSERVATION                         ✓
REPEATED FRICTION                   ✓
CREDIBLE ASYMMETRY                 ✓
RECOVERABLE INFORMATION            ✓
ECONOMIC CONSEQUENCE               ✓
EXACT RESOLUTION GAP               ✓
LIVE COMPETITOR BENCHMARK          ✓
PLAUSIBLE RESOLUTION               ✓

─────────────────────────────────────
RADAR → FORGE
─────────────────────────────────────

RESOLUTION PRODUCED                 ✓
RESOLUTION CORRECT                  ✓
RESOLUTION DECISION-READY           ✓

REAL ACTOR EXPOSED                  ← NEXT
RESOLUTION UNDERSTOOD
RESOLUTION TRUSTED
DECISION AFFECTED
ACTION TAKEN
VALUE CREATED
VALUE CAPTURED
TRANSACTION
REPEAT
```

Do not skip directly from decision-ready resolution to commercial validation.

## 4. Construction exposed the recurring resolution primitives

The successful artifact preserved:

```text
ANSWER
+
WHY
+
AUTHORITATIVE SOURCE
+
SOURCE CHECK DATE
+
UNCERTAINTY
+
NEXT ACTION
```

These elements appear functionally important for this resolution class.

Do not yet create a generic architecture abstraction around them. Observe whether they recur across future FORGE experiments.

## 5. Boundaries enabled speed

The known-HS boundary remained critical.

The artifact did not attempt to solve:

- customs classification;
- guaranteed legal-origin determination;
- guaranteed remission eligibility;
- all duties/taxes/trade measures;
- future automatic freshness.

This allowed the resolution to answer one decision reliably rather than becoming a general trade-compliance product.

> **Resolution speed was enabled by disciplined exclusion as much as by available evidence.**

## 6. Freshness remains part of trust

The artifact is a dated snapshot.

That is acceptable for a disposable experiment, but freshness must remain visible because Spec 024 demonstrated that live tools can diverge materially from current authoritative schedules.

The next real-world interaction should not hide this property.

A user should be able to understand when the evidence was checked and that later policy changes may alter the answer.

## 7. Do not combine the next uncertainties

Spec 025 established production capability only.

Still unproven:

- whether a real actor understands the resolution;
- whether they trust it;
- whether it changes or confirms a decision;
- whether it changes a next action;
- whether that effect creates economic value;
- whether value can be captured;
- whether the mechanism repeats.

The next experiment should expose the resolution to a real economic decision, but should not simultaneously attempt to prove market-wide demand, pricing, repeatability, and scale.

## 8. The next experiment is partly instrument calibration

One real importer interaction is weak evidence about the population.

However, the first real interaction can answer a different and necessary question:

> **Can we observe the causal effect of the resolution on an actual decision at all?**

The initial real-world test should therefore calibrate the behavioral measurement instrument.

The useful chain is:

```text
REAL IMPORT DECISION
        ↓
ACTUAL ALREADY-CLASSIFIED INPUTS
        ↓
BASELINE
what would actor do without resolution?
        ↓
FORGE RESOLUTION
        ↓
UNDERSTOOD?
TRUSTED / CHALLENGED?
        ↓
DECISION AFTER
        ↓
SAME / CHANGED / ESCALATED
        ↓
OBSERVABLE NEXT ACTION
```

The experiment must record the baseline before presenting the resolution where practical. Otherwise confirmation and behavior change become difficult to distinguish.

## 9. Do not optimize for positive decision change

A resolution can create value without reversing a decision.

Potential useful outcomes include:

- reprice order;
- change supplier;
- defer shipment;
- confirm origin;
- investigate remission;
- escalate to broker;
- proceed with greater justified confidence;
- avoid unnecessary escalation.

Therefore success should not mean simply `decision changed = yes`.

The experiment should observe whether the resolution materially affects understanding, confidence, decision, or next action, and why.

## 10. Minimum real inputs

A real-world interaction does not require unnecessary commercially sensitive information.

The bounded resolution needs only the facts necessary to answer the decision, such as:

- already-supplied HS tariff item;
- origin;
- customs value;
- relevant entry/shipment timing;
- bounded exception facts where relevant.

Supplier names, invoice numbers, customer identities, and unrelated commercial information are not inherently required.

Collect no more information than necessary for the experiment.

## 11. Sample-size discipline

The first real interaction must not be interpreted as market validation.

`n = 1` can demonstrate that a causal mechanism is observable in at least one real case and can reveal flaws in the measurement design.

It cannot establish:

- population demand;
- conversion rate;
- willingness to pay;
- general trust;
- repeatability;
- market size.

If the first interaction is successful, later experiments can determine how much behavioral evidence is required before moving toward value capture.

## 12. Next empirical question

> **When a real importer facing a real bounded decision receives the FORGE resolution, can we observe whether and how it changes their understanding, confidence, decision, or next action?**

This motivates Spec 026 — Canadian Counter-Tariff Real-Decision Interaction.
