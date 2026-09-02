# Spec 021 — Reinforced RADAR Opportunity Search

**Status:** Research-only reinforcement test  
**Depends on:** Specs 001–020 and learning checkpoints 001–019 + 020  
**Primary objective:** Test whether RADAR can apply its accumulated learning to identify or reject the next opportunity set faster and more cheaply than the path that produced the EV conclusion.

---

## 1. Why this spec exists

Specs 001–020 materially changed RADAR's opportunity-discovery policy.

The EV sequence demonstrated both strengths and inefficiency:

- behavioral evidence revealed a real decision problem;
- recoverability filtered weak hidden attributes;
- authoritative evidence demonstrated technical resolvability;
- commercial research demonstrated pre-decision behavior;
- but an exact existing resolution was discovered only after substantial technical deepening.

Spec 020 therefore taught RADAR to test the **exact resolution gap earlier**.

This spec is not primarily another opportunity hunt.

It is a reinforcement test of RADAR itself.

The governing question is:

> **Can RADAR apply the lessons of Specs 001–020 and reach its next genuinely unresolved, FORGE-worthy hypothesis—or reject the candidate set—faster and with less research than it took to reach the EV conclusion?**

A run that rejects all candidates cheaply can be successful.

RADAR must not manufacture a winner to satisfy the spec.

---

## 2. Core research funnel

Use this as the working sequence, not as a generic software ontology:

```text
PUBLIC / CHEAP SIGNAL
        ↓
SPECIFIC ACTOR + DECISION
        ↓
ECONOMIC CONSEQUENCE
        ↓
OBSERVED UNCERTAINTY / FRICTION
        ↓
SPECIFIC MISSING INFORMATION
        ↓
PRE-DECISION RECOVERABILITY
        ↓
EXACT RESOLUTION SEARCH
        ↓
RESIDUAL RESOLUTION GAP?
      /             \
    NO               YES
    ↓                 ↓
  PARK         DISTRIBUTABILITY
                      +
                EXPERIMENTABILITY
                      +
                 OPERATOR FIT
                      +
             VALUE-CREATION PATH
                      ↓
             FORGE CANDIDATE?
```

The exact order may be changed locally when a later gate is dramatically cheaper to test, but explain why.

The intended policy is **cheap falsification first**.

---

## 3. Candidate requirements

Generate and inspect **8–12 concrete opportunity hypotheses**.

Do not simply recycle the finalists from Spec 015 unless fresh evidence independently makes one relevant. Previously parked or rejected candidates may be used only as calibration, not to fill the candidate quota.

Seek diversity across:

- consumer / prosumer / self-service SME decisions;
- structural and behavioral signal origins;
- different economic domains;
- different resolution types;
- different potential value-capture mechanisms.

Do not force category diversity if it lowers evidence quality.

Each candidate must be expressible as:

```text
ACTOR
→ DECISION
→ OBSERVED FRICTION / UNCERTAINTY
→ ECONOMIC CONSEQUENCE
→ SPECIFIC MISSING INFORMATION
→ RECOVERABILITY PATH
→ EXISTING RESOLUTION
→ RESIDUAL GAP
→ POSSIBLE RESOLUTION
→ DISTRIBUTION SURFACE
→ CHEAPEST OBSERVABLE BEHAVIOR
→ POSSIBLE VALUE CREATED
→ POSSIBLE VALUE CAPTURE
```

If the candidate cannot be expressed specifically enough to search for an exact existing resolution, it is not mature enough to advance.

---

## 4. Signal policy

Use inexpensive legitimate public evidence first.

Possible signal classes include:

- search behavior;
- reviews;
- complaints/disputes;
- questions/forums;
- pricing/market structure;
- public transaction or administrative data;
- regulatory changes;
- product/service compatibility constraints;
- fragmented official information;
- job/tender/business-process evidence where appropriate;
- other public behavioral exhaust.

Behavioral-first and asymmetry-first discovery are both allowed.

Do not assume one is superior.

For each serious candidate identify which discovery path produced it:

```text
ASYMMETRY-FIRST
or
BEHAVIORAL-FIRST
or
MIXED
```

---

## 5. Early exact-resolution gate

This is the primary policy change being tested.

Before substantial technical feasibility research, inspect whether an existing solution already performs substantially the same decision-resolution function.

Evaluate functional overlap across:

```text
ACTOR
× DECISION
× INPUTS
× RESOLUTION
× OUTPUT
× TIMING
```

Do not reject a candidate merely because competitors exist.

Classify existing resolution as one of:

```text
A — ADEQUATE EXACT RESOLUTION
The hypothesized uncertainty is already substantially resolved.

B — PARTIAL / FRAGMENTED RESOLUTION
Solutions exist but a specific decision-relevant residual gap remains.

C — ADJACENT COMPETITION
Products exist in the category but do not perform the same decision-resolution function.

D — NO CREDIBLE RESOLUTION FOUND
No materially equivalent resolution found in the bounded search.
```

For B–D, state the exact residual gap rather than using generic language such as "better UX," "AI-powered," "more personalized," or "more convenient."

A candidate with A should normally be PARKED immediately unless a separately evidenced distribution/value-capture asymmetry creates a materially different opportunity.

---

## 6. Recoverability gate

For each candidate that survives initial screening, ask whether the missing decision information is recoverable **before or during the decision**.

Classify:

```text
HIGH
authoritative or otherwise reliable evidence can plausibly reconstruct the answer cheaply

MEDIUM
answer is partially recoverable but material uncertainty, proprietary evidence, or maintenance remains

LOW
critical information is stochastic, private, subjective, only knowable after the decision, or prohibitively costly to recover
```

LOW candidates should normally be rejected.

Do not confuse repeated complaints with recoverable information asymmetry.

---

## 7. Experimentability gate

For survivors, reconstruct the measurement chain:

```text
REAL DECISION
→ reachable actor
→ exposure delivered
→ noticed
→ understood
→ behavior possible
→ behavior observed
```

Estimate qualitatively:

- reachable population;
- decision timing;
- likely qualification loss;
- cost per useful observation;
- time to useful evidence;
- behavioral versus stated signal;
- whether a small experiment could be sufficiently powered;
- legal/admin/platform constraints;
- whether the experiment tests the hypothesis or merely tests distribution noise.

Negative evidence is meaningful only relative to the experiment's power to observe behavior.

---

## 8. Operator fit

Operator fit remains separate from objective opportunity quality.

Record whether the likely operating model is compatible with:

- high automation potential;
- self-service delivery;
- low recurring support burden;
- limited relationship selling/networking;
- modest capital requirements;
- manageable compliance/liability;
- ability to operate remotely;
- eventual low-maintenance portfolio fit.

A strong opportunity with poor operator fit should be identified honestly rather than scored down invisibly.

It may still be valuable as intelligence, a sellable opportunity, a dataset, or another value-capture path.

---

## 9. Value creation before value capture

Do not require direct consumer payment as the only commercial path.

For each serious survivor separate:

```text
OPPORTUNITY
    ↓
RESOLUTION
    ↓
VALUE CREATED
    ↓
WHO BENEFITS?
    ↓
POSSIBLE VALUE CAPTURE
```

Possible mechanisms include direct payment, affiliate/referral, lead generation, ads, SaaS, data/API, licensing, proprietary datasets, sale of intelligence/opportunities, investing/trading, or unknown.

Do not join programs, contact partners, collect payment, or create a business vehicle in this spec.

---

## 10. Time and spend envelope

This is intentionally a fast RADAR test.

### Target research time

**90 minutes.**

This is a target, not permission to fabricate completeness.

If decisive evidence appears earlier, stop.

If the 90-minute target is exceeded, continue only when one clearly identified missing fact is likely to change the final decision. Record the overrun and reason.

### Paid research budget

**€2 maximum, preferably €0.**

Use existing legitimate access only.

DataForSEO may be used as a bounded Level 1 research instrument when expected decision value justifies the request. Do not integrate it into production code.

Do not repeat failed measurements unless the missing result can still change the decision.

---

## 11. Research depth policy

Start shallow across the full candidate set.

Deepen only candidates that survive cheap gates.

The intended shape is:

```text
8–12 candidates
      ↓
cheap screening
      ↓
rapid rejection
      ↓
2–4 serious survivors at most
      ↓
deeper evidence
      ↓
0–1 FORGE candidate
```

Do not perform equal-depth research on every candidate.

Do not spend substantial effort proving a candidate already killed by an earlier decisive gate.

---

## 12. Kill reasons

Every rejected candidate must have a primary kill reason selected from or clearly extending:

- weak/non-specific decision friction;
- low economic consequence;
- weak pre-decision recoverability;
- adequate exact existing resolution;
- residual gap too small or cosmetic;
- inaccessible or noisy distribution;
- underpowered cheap experiment;
- high trust/regulatory/liability burden;
- poor operator fit;
- weak value-creation path;
- weak plausible value capture;
- evidence too weak to justify deeper research.

Record the stage at which the candidate was killed.

The purpose is to learn **where RADAR rejects opportunities**.

---

## 13. Success conditions

Return exactly one verdict:

### A — FORGE CANDIDATE

One opportunity hypothesis survived strongly enough to justify a minimum experimental resolution.

Required:

- specific actor and decision;
- economically consequential uncertainty;
- credible recoverability;
- no adequate exact resolution found;
- explicit residual gap;
- reachable decision behavior;
- plausible sufficiently powered cheap experiment;
- plausible value creation;
- operator fit understood;
- no material unresolved uncertainty that should obviously be tested more cheaply before FORGE.

### B — PROMISING, ONE DOMINANT UNCERTAINTY

A candidate appears promising but exactly one bounded uncertainty dominates the decision.

Recommend exactly one discriminator.

Do not use B to avoid making a decision.

### C — NO SURVIVOR, RADAR WORKED

All candidates were rejected or parked for explicit evidence-based reasons within acceptable research economics.

**This is a successful RADAR run.**

Do not manufacture a winner.

### D — RADAR PROCESS FAILURE

The process could not discriminate the candidate set within the available evidence/time/cost envelope, or research repeatedly expanded without materially reducing decision uncertainty.

This is the failure condition for the reinforcement test.

---

## 14. Compare with the EV path

The purpose is not fake numerical benchmarking, but evidence of improved research policy.

Report:

### Time

How long until candidates were rejected or advanced?

### Research depth

How much investigation was required per rejected candidate?

### Kill location

At which gates did candidates die?

### Exact-resolution timing

Did the process discover BecSpec-like killers before technical deepening?

### Decision quality

Can each important rejection/advancement be explained by concrete evidence?

### FORGE readiness

If a candidate survives, can the minimum experimental resolution be stated without another multi-spec conceptual excavation?

### Cost-to-rejection

Qualitatively assess whether weak candidates were eliminated cheaply.

Do not invent a monetary value for avoided work.

---

## 15. Research economics report

Report observable inputs only.

### Effort

- elapsed research time;
- approximate search count;
- approximate major source inspections;
- paid data/API spend;
- primarily web / code / implementation / mixed;
- visible Codex usage constraint if encountered.

### Uncertainty reduction

- dominant uncertainty entering;
- dominant uncertainty leaving;
- which hypotheses moved up/down;
- whether evidence changed the next decision.

### Evidence yield

Classify:

```text
HIGH YIELD
substantial decision-relevant uncertainty reduction at modest effort

MEDIUM YIELD
useful evidence but meaningful uncertainty remains

LOW YIELD
substantial effort with little decision-relevant information
```

Do not infer hidden token counts, hidden model cost, or unavailable compute metrics.

---

## 16. Required completion report

Return these sections in order:

1. **Verdict** — A / B / C / D and one-sentence reason.
2. **Candidate funnel** — all 8–12 candidates and final disposition.
3. **Candidate evidence table** — actor, decision, consequence, missing information, recoverability, exact-resolution class, residual gap, experimentability, operator fit, disposition.
4. **Early kills** — primary reason and kill stage for each rejected candidate.
5. **Serious survivors** — deeper reconstruction for no more than 2–4 candidates.
6. **Exact-resolution audit** — strongest existing functional solutions for serious survivors.
7. **Strongest opportunity hypothesis** — if any.
8. **Minimum experimental resolution** — only if verdict A; describe, do not build.
9. **One bounded discriminator** — only if verdict B.
10. **Why no survivor** — only if verdict C.
11. **RADAR process failure analysis** — only if verdict D.
12. **Comparison with EV path** — time, depth, kill location, exact-resolution timing, decision quality, FORGE readiness, qualitative cost-to-rejection.
13. **Research economics report**.
14. **What RADAR learned about its own search policy**.
15. **Architecture implications** — preserve vs too early to institutionalize.
16. **Exactly one recommended next action**.

---

## 17. Non-goals

Do **not**:

- implement software;
- modify production architecture;
- build a scoring engine;
- build an opportunity registry;
- build a generic competitor database;
- build a research-policy engine;
- create a generic ontology;
- create a UI;
- run ads;
- perform outreach;
- contact businesses or partners;
- join affiliate programs;
- collect payment;
- create a company/business vehicle;
- revive EV compatibility without independent new evidence;
- spend equal effort on every candidate;
- rescue weak hypotheses with adjacent demand;
- treat generic category competition as exact resolution;
- treat no competition as proof of opportunity;
- repeat failed measurement solely to complete the report;
- exceed the research budget without stopping.

---

## 18. Governing principles

Preserve throughout execution:

> **Friction ≠ demand ≠ asymmetry ≠ commercial opportunity.**

> **Absence of observed demand is evidence only to the extent that the experiment had sufficient power to observe demand.**

> **Do not expand a weakly observed hypothesis by absorbing adjacent intent merely to make the market look larger.**

> **Behavioral evidence can discover the question. Authoritative evidence should answer it.**

> **Do not validate the scalability of an unvalidated product.**

> **Do not repair a failed measurement unless the missing evidence can still change the decision.**

> **Competition should be evaluated by decision-resolution function, not category label.**

> **RADAR creates value by advancing strong opportunities and cheaply rejecting weak ones.**

> **The next research action should maximize expected decision-relevant uncertainty reduction.**

> **The next spec should usually be the cleanest continuation of what reality just taught us, not the most interesting adjacent idea.**

> **Disposable before durable — but only after a hypothesis earns the right to enter FORGE.**

---

## 19. Interpretation of a successful A verdict

An A verdict does **not** authorize a startup build.

It means RADAR has produced a hypothesis strong enough for the first deliberate RADAR → FORGE handoff.

The likely next question would be:

> **What is the smallest disposable resolution capable of interacting with reality strongly enough to tell us whether resolving this uncertainty creates meaningful value?**

That should be answered empirically rather than by designing FORGE architecture in advance.
