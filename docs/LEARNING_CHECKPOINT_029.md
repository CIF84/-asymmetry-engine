# Learning Checkpoint 029 — Disposable CRM Decision Resolution

## Outcome

Spec 029 returned **A — DECISION-READY RESOLUTION PRODUCED**.

The experiment demonstrated that FORGE can produce a defensible decision aid for a messy, multidimensional CRM decision using only public case facts plus authoritative public evidence, without forcing false precision or pretending to know private implementation reality.

The result is materially stronger than simple information organization: the decision space was reduced.

## What was resolved

The fixed public case concerned a 12-person small business using a materially customized Salesforce environment and considering whether to:

- retain Salesforce Professional and add API access;
- upgrade to Salesforce Enterprise;
- migrate to HubSpot Enterprise;
- or defer commitment until decisive unknowns are verified.

Commercial negotiation was correctly treated as a layer on the Salesforce options rather than as an independent technical branch.

## Evidence discipline validated

Spec 029 successfully preserved four distinct evidence classes:

```text
KNOWN
actor-supplied case facts

PUBLIC FACT
authoritative vendor/product evidence

ESTIMATED
explicit modeled scenarios and bounded assumptions

UNKNOWN / VERIFY
decision-sensitive facts that cannot be inferred safely
```

This separation prevented the artifact from laundering assumptions into facts.

The experiment also corrected two material points during validation, including the distinction between Salesforce API enablement and API call capacity and the documented flow-limit detail.

## Decision-space reduction

The produced resolution did not merely summarize CRM facts.

It materially compressed the decision:

```text
BEFORE

"Salesforce is getting expensive.
Should I upgrade, migrate, build something,
or use another CRM?"

                 ↓ FORGE

AFTER

3 credible branches

Professional + API
Enterprise
HubSpot Enterprise

                 ↓

1 dominant technical discriminator
Can the critical workflow actually survive?

+

2 commercial discriminators
What will Salesforce actually quote?
What seat structure is actually required?
```

The experiment:

- eliminated staying unchanged;
- removed insufficiently evidenced build/workaround/alternative-vendor branches;
- reframed negotiation as a commercial layer;
- reduced a broad "which CRM?" problem into a small number of explicit option-specific checks.

## Structured uncertainty as value creation

A central learning is that useful resolution does not require eliminating uncertainty.

The artifact transformed unstructured uncertainty into testable uncertainty:

```text
UNSTRUCTURED UNCERTAINTY
"migration could be difficult"

            ↓

STRUCTURED UNCERTAINTY
"this particular workflow-parity question
can reverse the decision"

            ↓

TESTABLE QUESTION
run one representative workflow test
```

This may be more generalizable than CRM recommendation itself.

A decision aid can create value by identifying which unknowns matter, which do not, and what action reduces the highest-value uncertainty next.

## Economic treatment

The artifact used a three-year horizon only where defensible.

Visible recurring-price scenarios were calculated, while migration labor, duration, disruption, productivity loss, negotiated discounts, seat mix, add-ons, and other unavailable components remained explicit exclusions or unknowns.

No complete TCO was manufactured.

This supports the principle:

> **Uncertainty represented is more useful than false precision.**

## Dominant discriminator

The strongest technical discriminator is one executable acceptance scenario for the highest-value custom workflow, including:

- objects and relationships;
- trigger;
- expected state transitions;
- integration effects;
- exception paths;
- responsible owner;
- expected output.

However, FORGE should not fabricate this private workflow scenario itself.

The actor supplying or refining it can become observable behavioral evidence in the next experiment.

## Why the next step should be interaction, not more case resolution

Spec 029 has already established:

```text
RESOLUTION PRODUCED                    ✓
RESOLUTION DEFENSIBLE                  ✓
UNCERTAINTY REPRESENTED                ✓
DECISION SPACE REDUCED                 ✓
```

The next evidence boundary is:

```text
REAL ACTOR EXPOSED                     ?
RESOLUTION UNDERSTOOD                  ?
RESOLUTION CHALLENGED / TRUSTED        ?
DECISION FRAMING CHANGED               ?
NEXT ACTION CHANGED                    ?
VALUE CREATED                          ?
```

Therefore the next experiment should not merely request more facts privately or continue desk research.

The opportunity was selected specifically because discovery and intervention can plausibly occur on the same public surface.

That topology now needs to be tested.

## Natural baseline advantage

The original public post is unusually useful because it captures the actor's decision state **before** the Spec 029 resolution existed.

This creates a natural baseline without requiring a separate pre-intervention interview.

Potential observable changes include:

- narrower or changed shortlist;
- changed framing from "which CRM?" to "which workflow must survive?";
- acceptance or rejection of the proposed discriminator;
- request for a written quote;
- willingness to define the critical workflow;
- willingness to test a migration path;
- increased or decreased confidence with reasons;
- challenge to a material assumption;
- explicit statement that the resolution did or did not help.

## Important measurement caution

No response is not equivalent to no value.

A failed interaction must distinguish among:

```text
DELIVERY FAILURE
→ actor may never have seen the intervention

ATTENTION FAILURE
→ exposure occurred but was ignored

COMPREHENSION / TRUST FAILURE
→ actor saw it but did not accept/use it

VALUE FAILURE
→ actor understood it but it did not improve the decision
```

Negative experimental evidence is meaningful only relative to what the experiment was capable of observing.

## Current evidence ladder

```text
ACCESSIBLE PRE-DECISION SURFACE        ✓
ACTOR SELF-IDENTIFIES                  ✓
ECONOMICALLY CONSEQUENTIAL DECISION    ✓
RECOVERABLE INPUTS                     ✓
EXACT RESOLUTION GAP                   ✓
SAME-SURFACE INTERVENTION              ✓
RESOLUTION PRODUCED                    ✓
RESOLUTION DEFENSIBLE                  ✓
UNCERTAINTY REPRESENTED                ✓
DECISION SPACE REDUCED                 ✓
────────────────────────────────────────
REAL ACTOR EXPOSED                     ← NEXT
RESOLUTION UNDERSTOOD                  ?
RESOLUTION TRUSTED / CHALLENGED        ?
DECISION FRAMING CHANGED               ?
NEXT ACTION CHANGED                    ?
VALUE CREATED                          ?
VALUE CAPTURED                         ?
```

## What remains unproven

Spec 029 does not prove:

- actual workflow parity;
- implementation feasibility;
- migration cost or duration;
- actor comprehension;
- trust;
- decision or behavioral impact;
- willingness to pay;
- repeatability across actors;
- commercialization viability;
- whether public same-surface intervention is socially/platform acceptable in practice.

## Next uncertainty

The next question is:

> **When the existing decision resolution is presented to the actor in the same public surface where the decision was exposed, does it measurably change their understanding, framing, confidence, shortlist, or next action?**

This is a mechanism test, not market validation.

One positive interaction would not prove demand or market size. It would demonstrate a much more important intermediate capability:

```text
PUBLIC DECISION SIGNAL
→ RESOLUTION
→ SAME-SURFACE DELIVERY
→ OBSERVABLE DECISION EFFECT
```

That is the next FORGE boundary.
