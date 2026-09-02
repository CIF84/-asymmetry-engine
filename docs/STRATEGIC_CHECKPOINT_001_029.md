# Strategic Checkpoint 001–029 — Pre-030 Model of the Engine

## Purpose

This document is a cross-experiment strategic synthesis, not another experiment result.

It records the current best interpretation of Asymmetry Engine after Specs 001–029 and **before Spec 030 introduces the first deliberately designed same-surface interaction evidence**.

The purpose is to preserve a pre-interaction epistemic snapshot so that later evidence can be compared against what we actually believed beforehand rather than allowing hindsight to rewrite the story.

This checkpoint is provisional. It should be challenged by future experiments.

---

## 1. Retrospective question

> **If we forgot the architecture and terminology invented along the way, but retained the empirical evidence from Specs 001–029, what system would we build now?**

The answer is not the same system we initially imagined.

That is evidence of learning, not failure.

---

## 2. Original model

The early conceptual model was approximately:

```text
PUBLIC DATA
    ↓
SIGNALS
    ↓
ASYMMETRIES
    ↓
SCORING
    ↓
OPPORTUNITIES
    ↓
PRODUCTS
    ↓
REVENUE
```

Embedded assumptions included:

1. asymmetries are discoverable properties of markets;
2. identifying an asymmetry moves meaningfully toward an opportunity;
3. opportunity quality can eventually be ranked sufficiently well by scoring;
4. FORGE is primarily downstream construction after RADAR selects a candidate;
5. distribution and monetization are largely downstream commercialization concerns.

Specs 001–012 were compatible with this worldview because they primarily established observation, normalization, persistence, provenance, source diversity, and reasoning feasibility.

Economic experiments from 013 onward progressively challenged it.

---

## 3. Central economic object: decision under resolvable uncertainty

The strongest current reinterpretation is that **asymmetry is not the central economic object**.

The more useful object is a **decision under potentially resolvable uncertainty**.

```text
ACTOR
  │
  ▼
DECISION ───────────────► ECONOMIC CONSEQUENCE
  │
  │ affected by
  ▼
UNCERTAINTY
  │
  │ potentially reducible using
  ▼
INFORMATION
  │
  │ transformed by
  ▼
RESOLUTION
  │
  │ potentially changes
  ▼
DECISION / ACTION
```

Information asymmetry can exist inside this system, but asymmetry alone is insufficient to establish opportunity.

Current provisional definition:

> **Asymmetry Engine is an experimental system for discovering economically consequential decisions under resolvable uncertainty, cheaply testing whether better information improves those decisions, and learning which resolution mechanisms can create and eventually capture repeatable value.**

This definition is provisional and should not yet trigger a wholesale architectural rewrite.

---

## 4. Opportunity quality behaves like interacting constraints

Experiments repeatedly demonstrated that a strong opportunity dimension does not necessarily compensate for a fatal weakness elsewhere.

Conceptually:

```text
OPPORTUNITY ≈
ECONOMIC CONSEQUENCE
× MEANINGFUL UNCERTAINTY
× RECOVERABILITY
× RESOLUTION GAP
× ACTOR ACCESSIBILITY
× RESOLUTION EFFECTIVENESS
× VALUE-CAPTURE POTENTIAL
```

This is **not an implementation formula** and should not be encoded as a numeric model yet.

Its purpose is to express a structural lesson:

> If a necessary term approaches zero, strength elsewhere may not rescue the opportunity.

Examples accumulated so far:

- plausible asymmetry + inaccessible actor can fail;
- consequential friction + unrecoverable decisive information can fail;
- recoverable uncertainty + exact existing resolver can fail;
- correct resolution + inaccessible decision surface can fail.

Therefore opportunity evaluation currently resembles **constraint satisfaction followed by ranking**, rather than weighted scoring from the beginning.

Provisional sequence:

```text
Consequential uncertainty?
        │
     no ┴── KILL
        │ yes
        ▼
Recoverable information?
        │
     no ┴── KILL
        │ yes
        ▼
Adequate existing resolution?
        │
    yes ┴── KILL
        │ no
        ▼
Resolution constructible?
        │
     no ┴── KILL
        │ yes
        ▼
Decision accessible?
        │
     no ┴── PARK / KILL
        │ yes
        ▼
FORGE
```

Ranking may become useful among candidates that survive necessary constraints.

---

## 5. What the major economic experiments taught us

### Cocoa

Plausible information asymmetry and proposition were insufficient because the experiment could not legitimately expose the proposition to qualifying actors.

Lesson: failure to observe the target behavior is invalid evidence, not negative demand evidence.

### Appliance repair

Search evidence demonstrated adjacent repair-cost demand but not the exact repair-versus-replace denominator.

Lesson: do not expand weakly observed hypotheses by absorbing adjacent intent to make a market appear larger.

### EV configuration

Friction, consequence, recoverability, resolution feasibility, and pre-decision behavior all survived. Exact functional competition did not.

Lesson: exact-resolution search belongs early. A complex derived-information problem is not an opportunity when an adequate accessible resolver already exists.

### Canadian counter-tariffs

A material exact functional gap was demonstrated. A correct, decision-ready resolution was manually produced. The opportunity then failed because relevant decisions were embedded in broker, association, and authenticated customs relationships without a sufficiently low-friction independent decision surface.

Lesson: distribution/accessibility is part of opportunity structure, not merely a downstream commercialization problem.

### Customized CRM decision

Accessible pre-decision behavior exposed the actor, current state, alternatives, constraints, economic consequence, recoverable information, and communication surface. A disposable resolution successfully compressed the decision from a broad CRM-choice problem into three credible branches governed by a small number of decisive technical and commercial unknowns.

Lesson so far: same-surface discovery and intervention may improve experimentability, and decision-space reduction may itself be a meaningful form of value creation.

This remains based on one surviving case and must not be overgeneralized.

---

## 6. RADAR as sequential experimental search

RADAR increasingly appears less like an opportunity-scoring engine and more like a **sequential falsification and research-policy system**.

Its practical question is often:

> **What is the cheapest next observation capable of materially changing our belief about this hypothesis?**

This explains several high-yield runs in which many candidates were rejected quickly and cheaply.

A useful provisional objective is therefore not:

```text
maximize opportunities found
```

but closer to:

```text
minimize expected resources required
to discover economically relevant truth
while preserving genuine survivors
```

This must include the cost of false negatives. The Engine should not optimize only for rejecting hypotheses.

---

## 7. Burden of proof should change with evidence state

A persistent risk is building an intellectually elegant entrepreneurial immune system that rejects nearly everything.

Therefore the burden of proof should not remain constant.

Early-stage posture:

> **Why should we investigate this?**

After multiple inexpensive gates survive:

> **Why should we not run the cheapest real experiment?**

As evidence accumulates, experimentation should generally become easier rather than harder.

This is one reason Spec 030 is important: after 028 and 029 survived, another large research pass would likely have lower information value than one bounded interaction.

---

## 8. Discovery and intervention experimentability

Specs 026–028 earned a useful distinction.

### Discovery experimentability

> Can RADAR cheaply observe enough evidence to discover, discriminate, and reject opportunity hypotheses?

### Intervention experimentability

> Can FORGE cheaply place a resolution into enough real decisions to observe its effect?

An opportunity can perform strongly on one and poorly on the other.

Canadian counter-tariffs demonstrated this directly: discovery and resolution were strong, but intervention access was weak.

The CRM candidate currently appears stronger because discovery and potential intervention occur on the same public surface.

---

## 9. Accessible decision surfaces

The current promising topology is:

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
ACCESSIBLE INTERVENTION
```

Spec 028 introduced a useful surface relationship:

- **SAME** — discovery and intervention can occur on the same surface;
- **ADJACENT** — intervention requires a low-friction transition;
- **SEPARATE** — intervention requires a materially different acquisition path.

This is promising but not yet a universal Engine rule.

Do **not** infer from one survivor that:

- forums are the preferred source;
- Reddit is the preferred distribution channel;
- software migration is the preferred market;
- B2B SaaS is the preferred opportunity class.

The deeper provisional object is:

> **Observable pre-commitment economic decision state.**

Many surfaces may expose this, including search, marketplaces, configuration workflows, support communities, procurement feeds, regulatory processes, product reviews, public questions, job postings, GitHub issues, or sources not yet considered.

---

## 10. Public behavior can be both sensor and interface

Early project thinking treated public data primarily as input evidence.

Recent experiments suggest that some public behavior can simultaneously provide:

```text
SENSOR
+
ACTOR IDENTIFICATION
+
DECISION STATE
+
INPUTS
+
INTERVENTION SURFACE
```

This is unusually information-dense because it can reduce the cost of rediscovering the actor after resolution construction.

Whether this produces meaningful behavioral evidence remains untested before Spec 030.

---

## 11. FORGE is an epistemic instrument, not merely a product factory

The original pipeline implied:

```text
RADAR → FORGE
```

The observed process is more iterative:

```text
OBSERVE
   ↓
HYPOTHESIZE
   ↓
TEST
   ↓
REVISE
   ↓
RESOLUTION
   ↓
TEST
   ↓
REVISE
   ↓
INTERACT
   ↓
LEARN
```

Constructing a resolution can change the understanding of the opportunity itself.

Spec 029 demonstrated this: the apparent question "Which CRM?" compressed into three credible branches plus a small number of decision-sensitive verification tasks.

Therefore FORGE should provisionally be understood as:

> **the layer that creates the cheapest intervention capable of generating the next economically relevant evidence.**

A product may eventually emerge from FORGE, but product construction is not its first obligation.

---

## 12. Disposable before durable

This principle has expanded beyond engineering.

It now means:

> **Use the cheapest representation capable of producing the next piece of economic evidence.**

Possible instruments include:

- search query;
- manual research;
- spreadsheet;
- Markdown brief;
- manual calculation;
- forum reply;
- mock page;
- script;
- calculator;
- API;
- web application.

Software is not inherently more advanced than a document. It is simply another experimental instrument whose cost must be justified by the evidence required.

---

## 13. Decision-space reduction as resolution quality

Spec 029 introduced a potentially important resolution-quality test:

> **Did the resolution reduce the decision space, or merely organize information?**

Possible evidence of reduction includes:

- eliminating a dominated option;
- narrowing the plausible option set;
- identifying a decisive threshold;
- converting broad uncertainty into one or two verifiable questions;
- exposing an incorrect decision framing;
- identifying a reversible next action that avoids premature commitment.

The CRM artifact succeeded under this test internally.

Whether an actor experiences this as useful value remains unproven before 030.

---

## 14. Explicit evidence classes

Spec 029 strengthened the distinction among:

```text
KNOWN
actor/case facts

PUBLIC FACT
authoritative external evidence

ESTIMATED
modeled quantities or bounded assumptions

UNKNOWN / VERIFY
decision-sensitive missing facts
```

This appears broadly reusable because many real decisions combine observed facts, public evidence, modeled uncertainty, and private unknown state.

The distinction should continue to be tested across domains before becoming a large generic abstraction.

---

## 15. Emerging learning policies

The Engine increasingly appears to accumulate at least four different kinds of intelligence.

### I. World model

```text
What kinds of economic uncertainty exist?
Where?
For whom?
Why?
```

### II. Experimental policy

```text
Given this hypothesis,
what is the cheapest observation
that could materially change our belief?
```

### III. Resolution policy

```text
Given a surviving decision,
what is the cheapest intervention
capable of reducing uncertainty?
```

### IV. Capture policy

```text
When value is created,
how can some of it be captured
with minimal operational burden?
```

Evidence for the first three is accumulating.

Capture policy remains largely untested and should not yet be architected as if understood.

---

## 16. Potential compounding asset

The long-term proprietary learning object may be richer than a database of asymmetries.

Conceptually:

```text
SIGNAL
× DECISION TYPE
× UNCERTAINTY STRUCTURE
× RESOLUTION TYPE
× INTERVENTION SURFACE
× EXPERIMENT RESULT
× ECONOMIC OUTCOME
```

Repeated experiments may eventually create priors such as:

- certain structural-change decisions often fail on distribution;
- certain highly structured comparison problems are likely to have exact incumbent resolvers;
- certain pre-decision migration questions may offer high resolution feasibility;
- certain evidence patterns predict unrecoverable private state.

These would be priors for entrepreneurial search, not merely startup ideas.

This potential moat remains hypothetical until repeated experiments demonstrate improved future performance.

---

## 17. Research framework and PORTFOLIO are not opposing objectives

A sophisticated research framework is not inherently incompatible with:

```text
ATLAS
  ↓
RADAR
  ↓
FORGE
  ↓
PORTFOLIO
  ↓
FREEDOM
```

The real trade-off is between:

```text
LEARNING → FORMALIZATION
```

and

```text
LEARNING → MORE EMPIRICAL TESTING
```

at a particular evidence state.

Framework investment is valuable when it increases the expected economics of future experiments enough to justify its construction and the risk of premature abstraction.

The dangerous version is not "building a framework." It is encoding immature hypotheses into durable infrastructure before they have replicated.

---

## 18. Preferred development rhythm: punctuated formalization

Current evidence favors an alternating strategy:

```text
EMPIRICAL RUNS
      ↓
ACCUMULATED PRESSURE / REPEATED LESSONS
      ↓
CONSOLIDATION
      ↓
SELECTIVE FORMALIZATION
      ↓
MORE EMPIRICAL RUNS
```

This avoids both extremes:

- endless bespoke research with no accumulating capability;
- large speculative architecture built around unreplicated ideas.

The project has already evolved in this pattern organically.

---

## 19. Maturity ladder for framework investment

A useful provisional maturity ladder is:

```text
OBSERVATION
    ↓
REPEATED OBSERVATION
    ↓
PROVISIONAL PRINCIPLE
    ↓
REPLICATED PRINCIPLE
    ↓
FORMAL MODEL
    ↓
IMPLEMENTED CAPABILITY
    ↓
AUTOMATED CAPABILITY
```

Not every insight needs to climb the ladder.

Current decision rule:

### Formalize / encode when

- the principle has repeated empirical support;
- reuse value is high;
- implementation reduces future research/experiment cost;
- premature encoding risk is low.

### Document but do not encode when

- the principle appears important;
- evidence is promising but insufficiently replicated;
- reuse value may be high;
- abstraction could still change materially.

### Leave experimental when

- the concept itself remains poorly understood;
- evidence is sparse;
- implementation would mainly satisfy architectural neatness.

Examples before 030:

- provenance: strong candidate for durable capability;
- freshness: strong reusable concern;
- research economics: repeatedly useful, possible future formalization;
- exact-resolution gate: repeatedly useful, possible future formalization;
- recoverability: strong concept, still domain-sensitive;
- accessible decision surface: promising but insufficiently replicated;
- decision compression: promising, currently one strong case;
- value capture: insufficient empirical evidence.

These classifications are provisional, not numeric scores.

---

## 20. ATLAS → RADAR → FORGE → PORTFOLIO → FREEDOM as a flywheel

The framework should not be interpreted only as a one-way pipeline.

A more complete model is:

```text
            ┌──────────────────────────┐
            │                          │
            ▼                          │
ATLAS → RADAR → FORGE → PORTFOLIO → FREEDOM
  ▲        │       │         │
  │        │       │         │
  └────────┴───────┴─────────┘
           LEARNING
```

PORTFOLIO generates economic evidence that can improve ATLAS.

ATLAS improves RADAR.

RADAR supplies FORGE and learns from rejection.

FORGE improves resolution and experimental policy.

Successful FORGE experiments may enter PORTFOLIO.

Failed experiments can still improve the Engine if their evidence changes future priors or research policy.

Under this interpretation, the research framework can be the **compounding mechanism beneath the portfolio**, not an alternative to it.

---

## 21. FREEDOM remains the objective function

The ultimate target is not merely fastest possible revenue.

FREEDOM increases with:

- recurring cash flow;
- automation;
- portfolio diversification;
- reusable infrastructure;
- accumulated knowledge;
- optionality.

FREEDOM decreases with:

- maintenance burden;
- operational complexity;
- customer support;
- platform dependency;
- capital requirements;
- concentration risk.

Therefore reusable research capability and accumulated knowledge can be economically valuable even before direct monetization.

First revenue remains important as evidence that the system can cross into value capture, but it is not the terminal objective.

A better strategic test is:

> **Does investment in ATLAS / RADAR / FORGE increase our ability to create PORTFOLIO faster, more reliably, or with less operational burden?**

---

## 22. Is the Engine beginning to compound?

This is now a central strategic question.

The research framework earns continued investment if later experiments increasingly show some combination of:

- lower time to meaningful evidence;
- lower paid research cost;
- faster rejection of weak hypotheses;
- better candidate generation;
- fewer repeated mistakes;
- better selection of the next discriminator;
- more reliable resolution construction;
- cheaper access to behavioral evidence;
- reusable artifacts or infrastructure;
- better prediction of where opportunities will fail;
- faster movement from observation toward economic interaction.

Conceptually:

```text
MORE EXPERIMENTS
      ↓
BETTER RESEARCH POLICY
      ↓
CHEAPER / BETTER EXPERIMENTS
      ↓
BETTER PRIORS
      ↓
BETTER CANDIDATES
      ↓
BETTER RESOLUTIONS
      ↓
MORE ECONOMIC EVIDENCE
      ↺
```

If this loop does not emerge, the framework risks becoming sophisticated overhead.

If it does emerge, the framework is part of the factory producing PORTFOLIO.

---

## 23. Architecture posture before 030

Do **not** perform a large architecture refactor based on this checkpoint.

The conceptual model has changed enough to document, but several important ideas remain under-replicated.

After 030 and subsequent experiments, explicitly ask:

> **Which findings have earned promotion from documentation into reusable Engine capability?**

Potential candidates should be evaluated by both empirical maturity and expected reuse value.

The goal is selective formalization, not architectural purity.

---

## 24. Claims Spec 030 can challenge

The following claims are intentionally recorded **before** the first same-surface interaction experiment.

After 030, classify each as:

- **SUPPORTED**
- **WEAKENED**
- **CONTRADICTED**
- **STILL UNTESTED**

### C1 — Same-surface access improves intervention experimentability

If the actor, live decision, resolution delivery, clarification, and response can remain on one surface, the cost of obtaining behavioral evidence should be lower than in separate-surface acquisition.

### C2 — A decision-ready resolution can create observable value without supplying a categorical recommendation

The actor may benefit from narrowed options, clearer trade-offs, or better verification actions even when the resolution does not say "choose X."

### C3 — Decision compression is a meaningful form of value creation

Reducing an opaque decision to fewer credible branches and a small number of decisive unknowns should be capable of changing understanding, confidence, or action.

### C4 — Public pre-decision behavior can function as both discovery sensor and intervention surface

A public decision question may expose enough actor state to discover the opportunity and provide a legitimate location for a bounded resolution.

### C5 — Once a candidate survives enough cheap gates, burden of proof should shift toward cheap experimentation

After 028 and 029, another broad research pass should have lower expected information value than one bounded real interaction.

### C6 — FORGE interaction produces information that improves the opportunity model itself

Actor reaction should reveal information not available from desk research alone and may alter the understanding of the problem, resolution, or future experiment design.

---

## 25. What Spec 030 cannot establish alone

Even a strong 030 result cannot prove:

- market size;
- repeatability across actors;
- willingness to pay;
- value capture;
- sustainable acquisition economics;
- that CRM is the right business;
- that software migration is a preferred opportunity family;
- that same-surface discovery generalizes across domains;
- that the Engine is already compounding economically.

One interaction can demonstrate or weaken a mechanism. It cannot validate a market.

---

## 26. Pre-030 strategic position

Current best interpretation:

```text
WORLD
  ↓
OBSERVATION
  ↓
ACTOR + LIVE DECISION
  ↓
ECONOMIC CONSEQUENCE
  ↓
UNCERTAINTY
  ↓
RECOVERABLE INFORMATION
  ↓
RESOLUTION GAP
  ↓
DISPOSABLE RESOLUTION
  ↓
ACCESSIBLE INTERVENTION
  ↓
DECISION EFFECT
  ↓
VALUE CREATED
  ↓
VALUE CAPTURED
  ↓
REPEATABILITY
  ↓
LEARNING
  └──────────────► improves future search and resolution
```

Evidence through 029 has reached **resolution production and internal decision-space reduction** for one accessible-surface candidate.

Spec 030 is intended to test the next boundary:

```text
WORLD
  ↓
ENGINE
  ↓
WORLD
```

The important question is not whether the CRM artifact is impressive.

It is whether placing a bounded resolution into a real decision produces observable information about value.

---

## 27. Back-check protocol after 030

After Spec 030 completes:

1. preserve its result without reinterpretation;
2. compare the result against Claims C1–C6 above;
3. classify each claim SUPPORTED / WEAKENED / CONTRADICTED / STILL UNTESTED;
4. identify surprises that this checkpoint failed to anticipate;
5. distinguish interaction failure from value failure;
6. update the evidence ladder;
7. decide whether another interaction, a replication, a candidate pivot, or selective framework formalization has the highest expected information value;
8. do not rewrite this checkpoint to make the prediction look better.

The checkpoint should remain historical evidence of the model held before interaction.
