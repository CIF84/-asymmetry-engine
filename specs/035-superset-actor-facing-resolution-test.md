# Spec 035 — Superset Actor-Facing Resolution Test

## Status

INTERACT experiment.

This specification defines one controlled public interaction with the actor-visible decision surface identified in Specs 032–034.

**Creating this specification does not authorize the external interaction.**

Execution that posts any public GitHub comment requires explicit user authorization in the execution prompt after the repository has been synchronized and the final interaction text has been verified against this specification.

---

## Context

Specs 032–034 established the following chain:

```text
observable actor                ✓
live decision                   ✓
economic consequence            ✓
recoverable evidence             ✓
legitimate same-surface path     ✓
exposure observability           ✓
decision-effect observability    ✓
residual resolution gap          ✓
bounded discriminator            ✓
decision-ready resolution        ✓
```

The candidate is Apache Superset SIP-225:

`https://github.com/apache/superset/issues/43331`

The live sequencing decision is whether to:

- **S1** — ship the current chart-local hierarchy representation unchanged;
- **S2** — ship now while making hierarchy-source resolution an explicit narrow boundary;
- **S3** — wait for a future dataset/semantic-layer hierarchy contract.

Spec 034 produced a decision-ready resolution recommending **S2**, with a stop rule that falls back to S1 if the boundary requires broad refactoring or speculative architecture.

The remaining question is no longer whether the resolution can be constructed.

It is:

> **Does presenting the bounded S2 sequencing resolution to the actual SIP decision surface produce observable evidence that the resolution changes, sharpens, challenges, or closes the decision?**

---

## Primary question

> **When the disposable S2 resolution is presented once in the same GitHub issue where SIP-225 is being decided, does it produce a measurable decision-relevant effect?**

A useful result may be acceptance, rejection, refinement, or challenge.

Agreement is not required.

---

## Secondary question

This experiment also indirectly tests the Spec 032 research-policy change:

> **Did selecting a candidate for observable actor + live decision + legitimate intervention path + observable effect produce a more interpretable interaction than accessible-surface discovery alone?**

Do not overclaim from n=1.

---

## Experimental topology

```text
PUBLIC ACTOR-VISIBLE DECISION
            ↓
NATURAL BASELINE
            ↓
COMPRESSED DISPOSABLE RESOLUTION
            ↓
ONE AUTHORIZED SAME-SURFACE COMMENT
            ↓
ACTOR EXPOSURE EVIDENCE
            ↓
ACTOR / MAINTAINER RESPONSE
            ↓
DECISION-EFFECT CLASSIFICATION
```

---

## Fixed surface

Apache Superset GitHub issue:

`apache/superset#43331 — [SIP-225] Proposal for author-configured hierarchical drill-down on dashboard charts`

Use the issue discussion itself.

Do not post to PR #41907, another issue, Discourse, email, direct message, or any alternate channel.

---

## Fixed actors

The primary actor is the SIP-225 proposal author.

Relevant maintainers/core participants already active in the issue may also provide valid decision evidence because they participate directly in the same SIP decision.

Do not broaden to unrelated contributors or solicit responses from anyone.

---

## Natural baseline

Before posting, preserve a read-only baseline of the current issue state sufficient to reconstruct:

- issue title/state;
- current proposal text relevant to S1/S2/S3;
- existing comments relevant to hierarchy ownership, semantic-layer direction, feature flag, migration, or sequencing;
- current issue comment count;
- current PR #41907 state only insofar as already needed to confirm the decision is live;
- any explicit current disposition of ship-now versus wait.

Do not modify the issue while recording the baseline.

If the decision has already materially closed before execution, stop and classify the experiment invalid/not executed rather than posting into a resolved decision.

---

## Interaction content

Do **not** post the full Spec 034 actor-facing draft.

Compress it into one GitHub comment approximately **250–400 words**.

The final interaction must preserve only these components:

1. **Observation** — no concrete hierarchy contract, implementation, milestone, or reliable landing horizon currently justifies waiting.
2. **Decision** — current evidence favors shipping rather than waiting.
3. **Recommendation** — if small, make hierarchy-source resolution explicit before the existing ordered-level interaction.
4. **Boundary** — configured source → resolve once → ordered drillable dimensions → existing interaction.
5. **Scope limit** — this does not design the future hierarchy model and does not claim all future hierarchies reduce to `string[]`.
6. **Stop rule** — if making the boundary explicit requires broad refactoring, a new persistence/API/provider model, or speculative architecture, ship S1 instead.
7. **Challenge invitation** — explicitly ask for the concrete dependency, implementation constraint, or project knowledge that would make this sequencing wrong.

The comment must be original, factual, non-promotional, non-authoritative in tone, and framed as a bounded contribution to the existing decision.

---

## Prohibited interaction content

Do not:

- claim to represent Apache Superset or its maintainers;
- claim certainty about private roadmap work;
- claim that no hierarchy work exists anywhere;
- invent hierarchy IDs, models, APIs, persistence, migration rules, provider contracts, or timing;
- tell maintainers how to implement code beyond the minimal conceptual boundary;
- post code;
- request private information;
- mention Asymmetry Engine, experiments, market research, AI evaluation, monetization, or this specification;
- mention that the comment was generated by an AI system;
- conceal or misrepresent identity if GitHub independently requires disclosure;
- post promotional links;
- ask for stars, follows, contact, or off-platform discussion;
- tag additional people to force attention.

---

## Authorization gate

The external interaction is consequential.

Execution requires both:

```text
SPEC defines permitted action
+
USER explicitly authorizes posting
=
EXECUTION PERMITTED
```

Without explicit user authorization in the execution prompt, the executor may prepare and record the final draft but must not post it.

Authorization is specific to:

- exactly one public top-level comment;
- exactly this issue;
- exactly the bounded resolution described here.

It does not authorize follow-up comments.

---

## Pre-post control check

Immediately before posting, verify:

1. correct repository and issue;
2. issue remains open and decision remains live;
3. no material new evidence invalidates the Spec 034 recommendation;
4. platform permits normal issue participation;
5. final comment remains within this specification;
6. user authorization is explicit;
7. no private or sensitive information is included;
8. no code or implementation change is being proposed as completed work;
9. one-comment limit has not already been used.

If any check fails, do not post. Record the failure.

---

## Interaction limit

Exactly **one** public top-level comment may be posted.

No reactions are required.

No edits after posting unless a trivial formatting correction is necessary to preserve the intended text and can be performed immediately without changing substance. Prefer no edit.

No follow-up comment is authorized under Spec 035, even if the actor asks a question.

A follow-up would require separate user authorization and either an explicit extension or a new specification.

---

## Delivery evidence

After posting, record:

- exact posted text;
- comment permalink;
- timestamp;
- visible publication state;
- whether the comment appears under the intended GitHub identity;
- any immediate platform warning/error.

A permalink proves delivery, not actor exposure.

---

## Observation window

Default observation window: **72 hours from successful publication**.

Do not repeatedly poll manually.

One initialization read immediately after posting is permitted to verify delivery.

One final read-only observation at or after the 72-hour deadline is sufficient unless the user separately requests an earlier check.

If a substantive actor/maintainer response is independently surfaced before the deadline, it may be recorded, but do not respond under this spec.

---

## Measurement model

Measure the interaction on six dimensions.

### M1 — Exposure

Evidence the relevant actor or decision participant likely encountered the resolution.

Examples:

- direct reply;
- reaction from relevant actor/maintainer;
- quoted or referenced comment;
- issue-state change clearly tied to the comment;
- explicit acknowledgement.

Classify:

- HIGH
- MEDIUM
- LOW
- UNKNOWN

Publication alone = UNKNOWN exposure.

### M2 — Understanding / comprehension

Evidence the response engages with the actual sequencing claim rather than a peripheral point.

Examples:

- discusses S1/S2/S3;
- addresses source-resolution boundary;
- addresses future hierarchy dependency;
- invokes the stop rule/refactor cost;
- supplies contrary implementation facts.

Classify:

- OBSERVED
- PARTIAL
- NOT OBSERVED
- UNKNOWN

### M3 — Challenge / trust

Did the actor or maintainer test the resolution?

Useful outcomes include:

- supplies contrary evidence;
- rejects an assumption;
- confirms a project constraint;
- asks for clarification that exposes missing state;
- explicitly accepts the reasoning.

Classify:

- CHALLENGED WITH EVIDENCE
- ACCEPTED / ENDORSED
- ENGAGED WITHOUT DISCRIMINATING EVIDENCE
- NOT OBSERVED
- UNKNOWN

### M4 — Decision framing change

Did the issue's framing become more explicit or narrower?

Examples:

- ship-now versus wait explicitly closed;
- migration/source boundary becomes named;
- S1 becomes explicit fallback;
- future hierarchy dependency becomes concretely bounded;
- maintainer reframes the relevant architectural seam.

Classify:

- MATERIAL
- MINOR
- NONE
- UNKNOWN

### M5 — Next-action change

Did a concrete next action change or become more specific?

Examples:

- SIP text update;
- PR review request around source resolution;
- explicit decision to ship unchanged;
- explicit decision to isolate normalization;
- explicit decision to wait due to new dependency evidence;
- concrete requested test/check.

Classify:

- MATERIAL
- MINOR
- NONE
- UNKNOWN

### M6 — Resolution validity update

After the interaction, is the Spec 034 resolution:

- STRENGTHENED;
- REFINED;
- WEAKENED;
- FALSIFIED;
- UNCHANGED;
- UNTESTED.

Reality overrides the artifact.

---

## Material decision effect

A **material decision effect** is observed if at least one of these occurs and is plausibly connected to the interaction:

- S1/S2/S3 disposition changes or becomes explicit;
- SIP text changes materially around hierarchy source/ownership/sequencing;
- PR implementation/review direction changes around the boundary;
- a previously hidden project dependency is supplied and changes the recommendation;
- a concrete stop/progression test is adopted;
- the actor explicitly reports that the comment changed or clarified the decision.

A positive reaction or generic thanks alone is not a material effect.

---

## Interaction outcome classes

Classify the observed response primarily as one of:

### ACCEPTANCE

The decision participant substantively accepts the sequencing resolution or adopts its boundary/framing.

### REJECTION + EVIDENCE

The resolution is rejected with concrete project evidence that changes the decision model.

This is a high-value result.

### REFINEMENT

The response supplies missing state or a better distinction that materially improves the resolution without wholly rejecting it.

### ENGAGEMENT, EFFECT AMBIGUOUS

The actor engages substantively, but no material change in framing/action can yet be established.

### NO MATERIAL EFFECT OBSERVED

Exposure and comprehension are reasonably evidenced, but the decision state does not materially change.

### EXPOSURE / EFFECT UNKNOWN

Delivery is verified, but exposure or decision effect cannot be established.

---

## No-response interpretation

No response is not automatically evidence of no value.

At the final observation classify the strongest supported state:

- **DELIVERY VERIFIED / EXPOSURE UNKNOWN** — comment exists but actor exposure is not evidenced;
- **EXPOSURE OBSERVED / NO ENGAGEMENT** — relevant actor exposure is evidenced but no substantive response follows;
- **COMPREHENSION / TRUST UNKNOWN** — engagement is insufficient to tell whether the resolution was understood;
- **NO MATERIAL EFFECT OBSERVED** — only when exposure and comprehension are sufficiently evidenced and no decision effect follows.

Do not infer attention failure, comprehension failure, trust failure, or value failure without supporting evidence.

---

## Experiment verdicts

### A — MATERIAL DECISION EFFECT OBSERVED

A material decision effect occurs through acceptance, rejection with evidence, or refinement that changes the issue's decision state, framing, or next action.

### B — SUBSTANTIVE INTERACTION, EFFECT AMBIGUOUS

Actor/maintainer engagement demonstrates exposure and comprehension, but material decision effect cannot be established.

### C — EXPOSURE OBSERVED, NO MATERIAL EFFECT

Relevant actor exposure and comprehension are sufficiently evidenced, but the resolution produces no material decision change.

### D — EFFECT UNKNOWN

Delivery occurs, but exposure/comprehension/effect cannot be established within the observation window.

### E — INVALID / NOT EXECUTED

The interaction is not posted, the decision closes before posting, authorization is absent, controls fail, wrong surface is used, or another design violation prevents interpretation.

---

## Economic interpretation

This remains a mechanism experiment, not commercial validation.

It may establish evidence about:

- whether decision compression creates observable value;
- whether actor-observable topology improves experimentability;
- whether same-surface intervention can elicit discriminating evidence;
- whether FORGE resolutions survive contact with actual decision participants.

It cannot establish:

- willingness to pay;
- market size;
- repeatability;
- scalable acquisition;
- value capture;
- business viability;
- Superset as a market opportunity;
- generalization across domains.

---

## Operational telemetry

Record:

| Metric | Value |
|---|---|
| Preparation active time | |
| Post/publication time | |
| Final observation time | |
| Incremental spend | |
| External comments posted | |
| Follow-ups posted | must be 0 |
| Control escalations | |
| Human authorization events | |
| Delivery verified | yes/no |
| Exposure classification | |
| Substantive responses | |
| Material decision effect | yes/no/unknown |
| Evidence yield | LOW / MEDIUM / HIGH |

Target preparation + publication active time: **≤20 minutes**.

Final read-only observation should be brief.

Incremental spend: **€0**.

---

## Required artifact

Create:

`experiments/035/superset-actor-facing-resolution-test.md`

Initialize it at execution with:

- baseline;
- authorization record;
- control check;
- exact final pre-post draft;
- execution state.

If posted, immediately update with:

- exact published text;
- permalink;
- timestamp;
- delivery verification;
- observation-window deadline;
- initial M1–M6 state.

At final observation, append:

- actor/maintainer responses;
- M1–M6 final classification;
- material-effect assessment;
- outcome class;
- verdict;
- evidence yield;
- what FORGE/INTERACT learned;
- what remains unproven;
- exactly one recommended next action.

Do not overwrite the original baseline or published text.

---

## Required completion report after publication initialization

Return exactly these sections:

1. Execution state / provisional verdict
2. Authorization evidence
3. Pre-post control result
4. Surface and actors
5. Natural baseline
6. Final interaction text
7. Interaction executed: yes/no
8. Comment permalink
9. Publication timestamp
10. Observation-window deadline
11. Delivery verification
12. M1 exposure at initialization
13. M2 comprehension at initialization
14. M3 challenge/trust at initialization
15. M4 decision framing at initialization
16. M5 next action at initialization
17. M6 resolution validity at initialization
18. Integrity/control confirmation
19. Operational telemetry
20. What is now observable
21. What remains unproven
22. Artifact path
23. Commit SHA
24. Exactly one next action

If execution is not authorized or cannot proceed, use the same report structure and explain the stop.

---

## Final observation report

At or after the 72-hour deadline, update the artifact and report:

1. Final verdict
2. Delivery state
3. Exposure evidence
4. Actor/maintainer responses
5. M1 final
6. M2 final
7. M3 final
8. M4 final
9. M5 final
10. M6 final
11. Material decision effect
12. Interaction outcome class
13. No-response classification if applicable
14. Resolution changes required
15. What INTERACT learned
16. Spec 032 policy implication
17. What remains unproven
18. Operational telemetry
19. Artifact commit SHA
20. Exactly one recommended next action

---

## Non-goals

Do not:

- post without explicit user authorization;
- post more than one comment;
- reply to actor questions under this spec;
- tag additional participants;
- open or modify PRs;
- commit Superset code;
- propose implementation patches;
- contact anyone privately;
- use email or social media;
- perform outreach elsewhere;
- run pricing/WTP/payment tests;
- search for other opportunities;
- modify Spec 030 or its actor interaction;
- infer value from silence;
- treat agreement as the only successful result;
- treat disagreement as experiment failure.

---

## Governing principles

> **The purpose of interaction is not to be right. It is to let reality attack the resolution.**

> **Rejection with evidence can be more valuable than agreement without evidence.**

> **Delivery is not exposure. Exposure is not comprehension. Comprehension is not decision effect.**

> **A decision-ready artifact has not created value until something in the real decision changes.**

> **Same-surface access matters only when the actor and effect are observable.**

> **One bounded interaction is a mechanism test, not a market.**

> **Authorization and execution remain separate.**
