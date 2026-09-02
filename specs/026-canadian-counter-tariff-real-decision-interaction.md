# Spec 026 — Canadian Counter-Tariff Real-Decision Interaction

**Status:** FORGE behavioral experiment  
**Depends on:** Specs 001–025 and learning checkpoints through 025  
**Primary objective:** Expose the decision-ready resolution produced in Spec 025 to one genuine bounded import decision and determine whether its causal effect on understanding, confidence, decision, or next action can be observed.

## 1. Central question

> **When a real Canadian importer facing a real bounded decision receives the FORGE resolution, can we observe whether and how it changes their understanding, confidence, decision, or next action?**

This is the first deliberate real-world interaction experiment for a FORGE artifact.

It is partly a value-creation test and partly calibration of the behavioral measurement instrument.

It is **not** market validation.

---

## 2. Why this experiment exists

Spec 024 demonstrated a material live resolution gap.

Spec 025 demonstrated that FORGE can produce a trustworthy, decision-ready resolution for the bounded known-HS problem.

Current evidence:

```text
RESOLUTION PRODUCED                 ✓
RESOLUTION CORRECT                  ✓
RESOLUTION DECISION-READY           ✓

REAL ACTOR EXPOSED                  ← NOW
RESOLUTION UNDERSTOOD
RESOLUTION TRUSTED
DECISION AFFECTED
ACTION TAKEN
VALUE CREATED
VALUE CAPTURED
TRANSACTION
REPEAT
```

The next uncertainty is no longer whether the answer can be produced.

It is whether the answer has observable effect when placed into a genuine economic decision.

---

## 3. Experimental unit

Use **one genuine Canadian SME importer/buyer decision** involving one real manifest or bounded set of order lines.

The actor must be facing, or have very recently faced, an actual decision involving the September 8, 2026 Canadian counter-tariff measure.

Examples of valid decisions:

- whether to place an order;
- whether to accept a supplier quote;
- whether to reprice goods;
- whether to substitute a supplier/product;
- whether to defer shipment;
- whether to confirm origin;
- whether to investigate remission;
- whether to escalate to a customs broker or specialist.

Do not use a purely hypothetical respondent who has no relevant economic decision.

Do not require a large company or formal procurement department.

---

## 4. Acquisition is a means, not the experiment

The experiment requires one qualifying actor, but do not turn Spec 026 into a broad outreach campaign.

Use the cheapest legitimate route available to obtain one real interaction.

Possible routes include:

- an existing personal/professional connection;
- a warm introduction;
- a relevant public business contact where a narrowly targeted approach is appropriate;
- another low-cost legitimate path to one qualifying Canadian importer/buyer.

Do not create a high-volume cold-email campaign.

Do not infer market demand from response or non-response to acquisition attempts.

If acquisition becomes the dominant bottleneck, stop and classify it explicitly rather than sending increasingly large outreach batches.

No message may misrepresent identity, affiliation, expertise, legal status, or commercial relationship.

Do not send external outreach unless explicitly authorized by the project owner/user.

---

## 5. Minimum real inputs

Collect only information necessary to produce the bounded resolution.

Required where applicable:

```text
supplied Canadian HS tariff item
origin
customs value
relevant entry / shipment date
already-in-transit fact
intended re-export fact
no-reasonably-substitutable-supply fact
```

Do not require unnecessary commercially sensitive data.

Supplier names, invoice numbers, customer names, bank information, contract documents, and unrelated commercial information are outside scope unless the actor independently determines a specific item is necessary and safe to share.

If identifying or sensitive information is supplied, minimize its reproduction in repository artifacts and completion reports.

---

## 6. Preserve the resolution boundary

Spec 026 does not provide customs classification.

The actor supplies the classification.

The resolution may identify that classification uncertainty matters and recommend specialist confirmation, but must not silently infer or replace the HS item.

Likewise, do not guarantee:

- legal origin;
- remission eligibility;
- all customs obligations;
- all taxes/duties/trade measures.

The September 8 counter-tariff decision remains the bounded job.

---

## 7. Freshness check before interaction

Immediately before producing the real-case resolution, re-check the authoritative Canadian sources necessary for the bounded decision.

At minimum verify:

- the current September 8 counter-tariff schedule;
- effective-date/in-transit treatment;
- relevant remission/relief guidance if applicable.

Record the source-check date/time.

As of Spec 026 creation on 2 September 2026, official Canadian material still states that the new countermeasures take effect at 12:01 a.m. on September 8, apply to qualifying U.S.-origin goods, exclude qualifying goods already in transit on commencement, and retain an exceptional-remission framework. Re-check rather than relying on this statement during execution.

If policy changes materially enough to invalidate the resolution premise, stop and classify the experiment accordingly.

---

## 8. Baseline must precede the resolution

Where practical, capture the actor's baseline **before** showing the FORGE answer.

Record concisely:

### B1 — Current understanding

What does the actor currently believe about exposure?

Examples:

```text
EXPOSED
NOT EXPOSED
UNSURE
MIXED / LINE-SPECIFIC
```

### B2 — Expected financial impact

What cost or range do they currently expect, if any?

`UNKNOWN` is valid.

### B3 — Current intended decision

What would they do if they had to decide now?

### B4 — Current next action

What would they do next without our resolution?

### B5 — Confidence

Ask for a simple self-reported confidence level using one fixed scale, for example 0–10.

The number is not a scientific measure of value. It is a before/after indicator for this interaction.

Do not coach the actor toward uncertainty or toward a particular answer.

---

## 9. Produce the real-case resolution

Using the Spec 025 method, produce a fresh bounded exposure brief for the actor's actual supplied facts.

The resolution should contain:

- YES / NO / REVIEW REQUIRED per line;
- applicable rate;
- incremental cost;
- material caveat;
- authoritative evidence;
- source-check date;
- exactly one primary next action per line;
- manifest-level summary where useful;
- explicit scope boundaries.

Keep it decision-first and concise.

Do not add speculative recommendations simply to make the artifact appear more valuable.

Store a sanitized experimental artifact under:

`experiments/026/`

Do not commit unnecessary identifying or confidential information.

---

## 10. Present the resolution without persuasion

The purpose is to test the resolution, not the operator's sales ability.

Present the artifact neutrally.

Do not:

- argue that it is useful;
- explain why the actor should trust it before they react;
- tell them that competitors are worse;
- prime them to change their decision;
- ask leading questions such as “wouldn't this save you money?”;
- mention future pricing before the behavioral observation is complete.

Answer factual clarification questions honestly.

Record material challenges or objections.

---

## 11. Post-resolution observation

After the actor has inspected the resolution, capture:

### P1 — Understanding

Can the actor correctly explain the key result in their own words?

Record the substance, not a transcript unless necessary.

### P2 — Trust / challenge

Classify:

```text
ACCEPTED
ACCEPTED WITH QUESTIONS
CHALLENGED — RESOLVED
CHALLENGED — UNRESOLVED
REJECTED
```

Record the material reason.

### P3 — Confidence

Use the same scale as baseline.

### P4 — Decision after resolution

What would the actor now do?

### P5 — Next action after resolution

What is their next concrete action?

### P6 — Why

Ask what, if anything, in the resolution caused the difference.

Do not force a positive answer.

---

## 12. Behavioral effect classification

Compare baseline and post-resolution states.

Classify the observed effect as one or more of:

```text
DECISION CHANGED
NEXT ACTION CHANGED
ESCALATION TARGET CHANGED
COST EXPECTATION CHANGED
CONFIDENCE MATERIALLY CHANGED
UNCERTAINTY NARROWED
NO OBSERVABLE EFFECT
NEGATIVE EFFECT / CONFUSION INCREASED
```

Examples of potentially useful effects:

- reprice order;
- change supplier;
- defer shipment;
- investigate remission;
- confirm origin;
- escalate to broker;
- proceed with greater justified confidence;
- avoid an unnecessary escalation;
- revise expected landed cost.

Do not define success as “the actor changed their decision.”

A confirmed decision can still represent value if the resolution materially reduces uncertainty or unnecessary work.

---

## 13. Action evidence

Where practical within the natural timing of the interaction, distinguish:

```text
STATED INTENT
vs
OBSERVED ACTION
```

Examples of observed action could include the actor actually:

- requesting origin confirmation;
- asking a broker a narrower question;
- revising an internal price;
- pausing an order;
- proceeding with an order;
- investigating remission.

Do not require access to confidential systems or documents merely to prove action.

If action cannot yet occur during the experiment window, report stated intent honestly and do not relabel it as behavior.

---

## 14. Value-creation interpretation

Spec 026 may produce early evidence of value creation, but must distinguish mechanism from magnitude.

Possible value mechanisms include:

```text
AVOIDED FALSE EXPOSURE
AVOIDED MARGIN SURPRISE
BETTER COST ESTIMATE
FASTER DECISION
NARROWER BROKER / SPECIALIST QUESTION
AVOIDED UNNECESSARY ESCALATION
BETTER SUPPLIER / TIMING DECISION
INCREASED JUSTIFIED CONFIDENCE
```

Do not fabricate a monetary value if the actor cannot support one.

Do not claim market-wide value from one case.

---

## 15. Verdicts

### A — CAUSAL MECHANISM OBSERVED

A genuine actor and real decision were used; baseline was captured; the resolution was understood sufficiently; and a defensible before/after difference was observed in understanding, confidence, decision, next action, escalation, or cost expectation that the actor attributes materially to the resolution.

This demonstrates the mechanism at least once.

It does **not** validate market demand.

### B — INTERACTION VALID, NO MATERIAL EFFECT

A genuine decision was tested correctly, but the resolution produced no meaningful observable difference.

This is valid negative evidence about this interaction.

Do not automatically kill the opportunity from `n = 1`.

Identify whether the reason appears to be prior knowledge, low relevance, insufficient resolution, timing, or another observed factor.

### C — ONE BOUNDED INTERACTION WEAKNESS

The interaction occurred, but exactly one bounded weakness prevents interpreting the causal effect—for example baseline was contaminated, one necessary input was missing, or the actor could not inspect the artifact sufficiently.

Recommend exactly one repair.

### D — INTERACTION INVALID / NOT OBTAINED

No qualifying real decision was obtained, policy changed materially, the actor did not have the necessary bounded inputs, or another problem prevents a valid interaction.

Do not interpret acquisition failure as absence of demand.

---

## 16. Sample-size discipline

This experiment is intentionally `n = 1`.

A verdict A means only:

> **The resolution's causal mechanism was observable in at least one genuine economic decision.**

It does not establish:

- population demand;
- conversion rate;
- average value;
- willingness to pay;
- trust rate;
- repeatability;
- market size;
- scalability.

A verdict B likewise does not establish that the mechanism never works.

The purpose is to calibrate real-world measurement before choosing a larger evidence design.

---

## 17. Acquisition stop rule

Do not let participant acquisition consume the project.

Target one qualifying interaction.

If a legitimate low-cost route does not produce a qualifying actor within a bounded effort envelope, stop.

Recommended acquisition envelope:

- **60 minutes active effort maximum** before reassessment;
- no paid acquisition;
- no high-volume outreach;
- no repeated follow-up pressure.

If no participant is obtained, return verdict D and report the acquisition bottleneck separately from opportunity quality.

---

## 18. Execution envelope

Once a participant is obtained:

- target **90 minutes active execution** for baseline, resolution production, presentation, post-observation, and recording;
- €0 preferred; €2 hard maximum for research/data only;
- no payment requested from the participant;
- no durable software;
- no automation required.

A bounded overrun is acceptable only to finish an already-started valid interaction or verify a material factual challenge raised by the actor.

---

## 19. Privacy and evidence handling

Store only what is necessary to interpret the experiment.

Prefer sanitized summaries over raw confidential documents.

Repository artifacts should avoid unnecessary:

- personal names;
- private email addresses;
- supplier/customer identities;
- invoice numbers;
- bank/payment information;
- confidential contract terms.

Use anonymous labels such as `Importer A` where identity is irrelevant.

Do not invent anonymity claims if identifying information is actually committed.

---

## 20. Required experiment record

Create a sanitized record under:

`experiments/026/`

Suggested files:

```text
experiments/026/interaction-record.md
experiments/026/exposure-brief.md
```

The interaction record should include:

- actor qualification without unnecessary identity;
- decision context;
- bounded inputs;
- baseline B1–B5;
- source freshness check;
- post-resolution P1–P6;
- behavioral effect classification;
- stated intent vs observed action;
- value mechanism if evidenced;
- challenges/objections;
- experiment limitations.

Do not include verbatim private conversation unless necessary and authorized.

---

## 21. Required completion report

Return these sections in order:

1. **Verdict** — A / B / C / D and one-sentence reason.
2. **Actor qualification** — why this was a genuine bounded economic decision, without unnecessary identity.
3. **Acquisition route and effort** — how the interaction was obtained and whether acquisition became a bottleneck.
4. **Real decision context**.
5. **Inputs used** — sanitized.
6. **Baseline B1–B5**.
7. **Freshness check** — authoritative sources checked immediately before resolution.
8. **Resolution delivered** — artifact path and concise summary.
9. **Post-resolution P1–P6**.
10. **Before/after comparison**.
11. **Behavioral effect classification**.
12. **Stated intent vs observed action**.
13. **Value-creation evidence** — mechanism only where supported.
14. **Challenges and objections**.
15. **What FORGE learned about real-world interaction**.
16. **What remains unproven**.
17. **Execution economics report**.
18. **Architecture implications** — preserve vs too early to institutionalize.
19. **Exactly one recommended next action**, constrained by the evidence.

---

## 22. Execution economics report

Report observable inputs only.

### Acquisition

- active acquisition time;
- contacts/introductions attempted if any;
- qualifying interactions obtained;
- paid acquisition spend.

### Interaction

- active execution time;
- manifest lines resolved;
- authoritative sources inspected;
- material challenges requiring verification;
- files created;
- paid research spend;
- visible Codex constraint if encountered.

### Uncertainty reduction

- entering uncertainty: can the resolution's effect be observed in a genuine decision?
- leaving uncertainty;
- whether the behavioral instrument worked;
- whether acquisition or resolution quality became the next bottleneck.

### Evidence yield

Classify:

```text
HIGH YIELD
valid interaction clearly reveals whether/how the resolution affected the decision mechanism at modest cost

MEDIUM YIELD
valid interaction occurred but causal interpretation remains partly ambiguous

LOW YIELD
substantial effort without interpretable behavioral evidence
```

Do not infer hidden model/token costs.

---

## 23. Non-goals

Do **not**:

- infer market validation from one participant;
- perform a large outreach campaign;
- send external messages without explicit user authorization;
- test pricing;
- request payment;
- create a business entity;
- build payment infrastructure;
- build software;
- automate report generation;
- build a tariff database;
- broaden into customs classification;
- broaden into general trade compliance;
- collect unnecessary confidential information;
- optimize the artifact based on speculative preferences before observing the actor;
- lead the actor toward a positive response;
- call stated intent observed behavior;
- manufacture monetary value estimates;
- return to RADAR discovery merely because acquisition is inconvenient.

---

## 24. Governing principles

> **FORGE makes something capable of interacting with reality.**

> **Measure the actor before and after the resolution.**

> **Do not persuade when you are trying to observe.**

> **A changed decision is not the only form of value.**

> **Stated intent and observed action are different evidence.**

> **One case can demonstrate a mechanism; it cannot establish a market.**

> **Acquisition failure is not demand failure.**

> **Collect only the information required to resolve the bounded decision.**

> **Preserve provenance, freshness, and uncertainty when the artifact meets reality.**

---

## 25. Interpretation

The project has now moved through:

```text
RADAR
  ↓
find valuable uncertainty
  ↓
prove exact resolution gap
  ↓
────────────────────────────
FORGE
  ↓
produce resolution          ✓
validate resolution         ✓
  ↓
REAL-DECISION INTERACTION   ← SPEC 026
  ↓
understanding
trust / challenge
before vs after decision
next action
  ↓
VALUE-CREATION EVIDENCE
```

Spec 026 should tell us whether the resolution can create an observable causal effect in one genuine economic decision.

If that mechanism is observed, the next experiment should be chosen based on what the interaction teaches us—not automatically jump to monetization or software.
