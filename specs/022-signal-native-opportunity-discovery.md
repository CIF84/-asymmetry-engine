# Spec 022 — Signal-Native Opportunity Discovery

**Status:** Research-only discovery-policy test  
**Depends on:** Specs 001–021 and learning checkpoints through 021  
**Primary objective:** Test whether fresh public signals can generate specific, non-obvious opportunity hypotheses without beginning from brainstormed business/problem categories, while preserving the cheap rejection policy learned in Specs 020–021.

---

## 1. Why this spec exists

Spec 021 demonstrated that RADAR can cheaply evaluate and reject a fresh set of concrete opportunity hypotheses.

Eleven candidates were screened in approximately 20 minutes with €0 paid data. Most died at the early exact-resolution gate.

That is evidence that the **evaluation policy improved**.

It also exposed a new bottleneck:

```text
                 RADAR
                   │
          ┌────────┴────────┐
          │                 │
 CANDIDATE GENERATION    EVALUATION
          │                 │
         ???                ✓
```

Most Spec 021 candidates were recognizable economic problem categories. Their maturity made exact existing resolutions easy to find.

The next empirical question is therefore:

> **Can fresh public evidence generate specific opportunity hypotheses that were not first conceived as familiar problem categories, while preserving the cheap rejection policy learned in Specs 020–021?**

This spec tests candidate generation, not merely filtering.

---

## 2. Core constraint: signals before ideas

Do **not** begin by brainstorming businesses, products, industries, or familiar consumer problems.

The required sequence is:

```text
RAW PUBLIC SIGNAL
        ↓
OBSERVED PATTERN / CHANGE / FRICTION
        ↓
SPECIFIC ACTOR
        ↓
SPECIFIC ECONOMIC DECISION
        ↓
UNCERTAINTY / MISSING INFORMATION
        ↓
ECONOMIC CONSEQUENCE
        ↓
OPPORTUNITY HYPOTHESIS
        ↓
CHEAP RADAR EVALUATION
```

A candidate is invalid for this spec if its origin is effectively:

```text
"people probably struggle with X"
```

followed by searching for evidence.

Evidence must generate the hypothesis, not merely decorate it afterward.

---

## 3. Signal families

Use exactly **three distinct fresh signal families**.

Each family should begin from public evidence rather than a predetermined opportunity category.

Required families:

### A. Behavioral exhaust

Examples include:

- questions;
- complaints;
- reviews;
- dispute narratives;
- repeated troubleshooting;
- public user discussions;
- search suggestions/related queries if genuinely generative rather than fixed-seed confirmation.

The objective is to observe economically relevant behavior that implies a decision or unresolved uncertainty.

### B. Structural change

Examples include:

- new or changing regulation;
- eligibility-rule changes;
- product/service policy changes;
- subsidy/tax changes;
- standards transitions;
- platform rule changes;
- market-entry/exit changes;
- technology transitions that alter decisions.

The objective is to find situations where reality changed faster than decision support.

### C. Market friction / fragmented evidence

Examples include:

- price or fee structure changes;
- compatibility matrices;
- availability constraints;
- fragmented official specifications;
- public transactional/administrative evidence;
- contradictory authoritative claims;
- non-comparable pricing;
- changing product/service combinations.

The objective is to find evidence where a useful decision answer requires synthesis rather than simple lookup.

These families are experimental discovery surfaces, not permanent taxonomy.

---

## 4. Freshness and anti-recycling rules

Do not use as candidate hypotheses:

- any of the 11 Spec 021 candidates;
- EV smart-charging compatibility;
- cocoa input-cost intelligence;
- appliance repair-vs-replace / repair quote fairness;
- Spec 015 finalists unless a genuinely new raw signal independently produces a materially different decision problem.

Prior work may be used only as calibration for reasoning quality.

Do not deliberately search for previously discussed opportunities.

---

## 5. Observation collection

Spend the first phase observing each signal family **without committing to an opportunity**.

For each family, collect a small bounded set of concrete observations sufficient to identify repeated or structurally meaningful patterns.

Target approximately:

- **5–10 useful observations per signal family**;
- fewer if a decisive repeated pattern emerges early;
- more only if the source is noisy and one additional bounded batch is likely to clarify whether a pattern exists.

Do not build datasets, scrapers, or ingestion pipelines.

Record enough provenance to explain where the observation came from and why it matters.

---

## 6. Pattern extraction

Before generating candidates, summarize each signal family independently.

For each family identify up to **three observed patterns**.

A pattern should be grounded in the collected evidence and stated without a product idea.

Good form:

> Multiple actors making decision X repeatedly lack information Y because A and B publish incompatible or fragmented evidence.

Bad form:

> There should be an AI app for X.

For each pattern state:

- observed behavior/change/friction;
- actor;
- apparent decision;
- apparent economic consequence;
- uncertainty or missing information;
- whether the pattern appears pre-decision, during-decision, or post-decision;
- confidence that the pattern is real rather than anecdotal noise.

---

## 7. Candidate generation

Generate **6–9 opportunity hypotheses total** from the observed patterns.

Target roughly 2–3 candidates per signal family, but do not force equal counts if one family produces weak evidence.

Every candidate must preserve a traceable evidence chain:

```text
SOURCE OBSERVATIONS
        ↓
OBSERVED PATTERN
        ↓
ACTOR
        ↓
DECISION
        ↓
UNCERTAINTY / MISSING INFORMATION
        ↓
ECONOMIC CONSEQUENCE
        ↓
OPPORTUNITY HYPOTHESIS
```

For every candidate explicitly state which observations generated it.

If the chain requires inventing an unobserved problem to make the candidate interesting, reject it before RADAR evaluation.

---

## 8. Novelty / obviousness check

The objective is not novelty for its own sake.

However, this spec specifically tests whether signal-native discovery produces candidates less obvious than generic problem brainstorming.

Classify each generated candidate:

```text
OBVIOUS
A familiar, broadly recognized problem category that could easily have been brainstormed without the source observations.

INTERSECTIONAL
The opportunity emerges from a specific combination of actor, rule/configuration, evidence fragmentation, timing, or market structure.

SURPRISING
The evidence reveals a decision problem that was not reasonably apparent before observing the signal.
```

This classification is qualitative and must not influence the candidate's economic evaluation.

An obvious candidate may still be excellent. A surprising candidate may still be worthless.

---

## 9. Apply the reinforced RADAR gates

After signal-native candidates have been generated, apply the cheap evaluation policy from Specs 020–021.

For each candidate reconstruct:

```text
ACTOR
→ DECISION
→ ECONOMIC CONSEQUENCE
→ SPECIFIC MISSING INFORMATION
→ PRE-DECISION RECOVERABILITY
→ EXACT EXISTING RESOLUTION
→ RESIDUAL GAP
→ DISTRIBUTION SURFACE
→ CHEAPEST OBSERVABLE BEHAVIOR
→ EXPERIMENTABILITY
→ OPERATOR FIT
→ POSSIBLE VALUE CREATED
→ POSSIBLE VALUE CAPTURE
```

Start shallow and deepen only survivors.

---

## 10. Exact-resolution gate

As soon as actor, decision, inputs, and desired output are specific enough, search for functional existing resolutions.

Compare:

```text
ACTOR
× DECISION
× INPUTS
× RESOLUTION
× OUTPUT
× TIMING
```

Classify:

```text
A — ADEQUATE EXACT RESOLUTION
B — PARTIAL / FRAGMENTED RESOLUTION
C — ADJACENT COMPETITION
D — NO CREDIBLE RESOLUTION FOUND
```

Do not confuse category competition with exact resolution.

Do not infer opportunity from absence of competition.

A candidate with A should normally be parked immediately unless separately evidenced distribution or value-capture asymmetry creates a materially different opportunity.

---

## 11. Recoverability gate

Classify the missing information:

```text
HIGH
reconstructable before/during the decision from credible evidence at plausible cost

MEDIUM
partly reconstructable, with material uncertainty or maintenance burden

LOW
stochastic, private, subjective, post-decision-only, or prohibitively expensive to recover
```

LOW candidates should normally die.

Repeated complaints are not sufficient if the decision-relevant variable cannot be recovered.

---

## 12. Candidate-generation yield

This spec must evaluate not only candidates but also the **signal families that generated them**.

For each signal family report:

- observations inspected;
- meaningful patterns extracted;
- candidates generated;
- obvious vs intersectional vs surprising candidates;
- candidates surviving the first cheap RADAR gates;
- primary reasons candidates died;
- research effort;
- qualitative discovery yield.

Classify family yield:

```text
HIGH DISCOVERY YIELD
Produced at least one specific, economically meaningful candidate that survived cheap gates long enough to justify deeper evaluation.

MEDIUM DISCOVERY YIELD
Produced real and specific decision hypotheses, but they were cheaply killed by existing resolution, recoverability, economics, or experimentability.

LOW DISCOVERY YIELD
Mostly produced vague friction, post-purchase complaints, familiar solved problems, economically weak decisions, or hypotheses requiring invention beyond the evidence.
```

Do not create a numeric source score.

---

## 13. Experimentability and operator fit

For serious survivors only, reconstruct:

```text
REAL DECISION
→ reachable actor
→ exposure delivered
→ noticed
→ understood
→ behavior possible
→ observed behavior
```

Estimate whether a small experiment could produce enough independent observations to reduce uncertainty.

Keep operator fit separate from objective opportunity quality.

Prefer, but do not force:

- self-service;
- automation potential;
- low support burden;
- low relationship-selling dependence;
- modest capital;
- manageable compliance/liability;
- remote operation;
- eventual portfolio compatibility.

A strong opportunity with poor operator fit may still be valuable as intelligence, dataset, saleable opportunity, licensing input, investment signal, or another mechanism.

---

## 14. Value creation and value capture

For serious survivors separate:

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

Do not assume direct consumer payment.

Possible paths include direct payment, affiliate/referral, lead generation, advertising, SaaS, data/API, licensing, proprietary dataset, sale of intelligence/opportunity, investing/trading, or unknown.

Do not join programs, contact partners, collect money, or create a business vehicle.

---

## 15. Time and spend envelope

### Target research time

**90 minutes.**

If decisive evidence appears earlier, stop.

If the target is exceeded, continue only when one explicitly identified missing fact is likely to change the verdict. Record the reason.

### Paid research budget

**€2 maximum, preferably €0.**

Use legitimate public/free evidence first.

DataForSEO may be used only if it provides genuinely generative or decision-changing evidence and existing access suffices.

Do not repeat failed measurements unless the missing result can still change the decision.

---

## 16. Success conditions

Return exactly one verdict:

### A — SIGNAL-NATIVE FORGE CANDIDATE

At least one hypothesis generated from raw evidence survives strongly enough for a minimum experimental resolution.

Required:

- traceable observation → pattern → hypothesis chain;
- specific actor and decision;
- meaningful economic consequence;
- credible recoverability;
- no adequate exact resolution;
- explicit residual gap;
- reachable behavior;
- plausible sufficiently powered cheap experiment;
- plausible value creation;
- operator fit understood;
- no cheaper unresolved question should obviously precede FORGE.

### B — ONE BOUNDED UNCERTAINTY

At least one signal-native candidate is promising but exactly one uncertainty dominates the FORGE decision.

Recommend exactly one discriminator.

### C — NO SURVIVOR, DISCOVERY STILL INFORMATIVE

No candidate reaches FORGE, but at least one signal family generated specific, evidence-native hypotheses and the run learned useful information about which signals produce or fail to produce opportunities.

This can be a successful discovery-policy run.

### D — CANDIDATE-GENERATION FAILURE

The signal-native process mainly produced obvious solved problems, vague friction, post-decision complaints, economically weak hypotheses, or candidates requiring invention beyond the evidence.

Use D even if the evaluation filter efficiently rejected them.

The purpose is to distinguish **filter success** from **candidate-generation success**.

---

## 17. Required completion report

Return these sections in order:

1. **Verdict** — A / B / C / D and one-sentence reason.
2. **Signal-family summary** — behavioral exhaust, structural change, market friction/fragmented evidence.
3. **Raw observations** — bounded evidence collected per family with provenance.
4. **Observed patterns** — up to three per family, stated without product ideas.
5. **Candidate derivation map** — observation → pattern → actor → decision → missing information → consequence → hypothesis.
6. **Candidate funnel** — all 6–9 candidates and disposition.
7. **Novelty/obviousness classification** — obvious / intersectional / surprising, with one-line justification.
8. **Candidate evidence table** — recoverability, exact-resolution class, residual gap, experimentability, operator fit, disposition.
9. **Early kills** — kill stage and primary reason.
10. **Serious survivors** — no more than 2–4 deeper reconstructions.
11. **Exact-resolution audit** — strongest functional existing solutions for serious survivors.
12. **Strongest opportunity hypothesis** — if any.
13. **Minimum experimental resolution** — only for verdict A; describe, do not build.
14. **One bounded discriminator** — only for verdict B.
15. **Why discovery was still informative** — only for verdict C.
16. **Candidate-generation failure analysis** — only for verdict D.
17. **Signal-family discovery yield** — HIGH / MEDIUM / LOW per family and why.
18. **Comparison with Spec 021** — did signal-native generation produce less obvious or stronger candidates than familiar-problem generation?
19. **Research economics report**.
20. **What RADAR learned about candidate generation**.
21. **Architecture implications** — preserve vs too early to institutionalize.
22. **Exactly one recommended next action**.

---

## 18. Research economics report

Report observable inputs only.

### Effort

- elapsed research time;
- approximate searches;
- approximate major source inspections;
- paid data/API spend;
- work mode;
- visible Codex usage constraint if encountered.

### Uncertainty reduction

- dominant uncertainty entering;
- dominant uncertainty leaving;
- which discovery-family hypotheses moved up/down;
- whether the evidence changed the next decision.

### Evidence yield

Classify overall:

```text
HIGH YIELD
substantial learning about candidate generation and/or a strong surviving opportunity at modest effort

MEDIUM YIELD
useful signal-family learning but important uncertainty remains

LOW YIELD
substantial effort with little evidence about either opportunities or discovery policy
```

Do not infer hidden token counts or unavailable compute costs.

---

## 19. Non-goals

Do **not**:

- brainstorm a candidate list before observing signals;
- use evidence merely to justify preselected ideas;
- implement software;
- change production architecture;
- build source ingestion pipelines;
- build scrapers;
- build a candidate generator;
- build a scoring engine;
- build a source-yield model;
- build an opportunity registry;
- build a competitor database;
- build an ontology;
- run ads;
- perform outreach;
- contact partners;
- collect payment;
- revive prior candidates without genuinely independent fresh evidence;
- force equal candidate counts from weak signal families;
- confuse surprising with valuable;
- confuse obvious with worthless;
- rescue weak hypotheses with adjacent demand;
- deepen candidates already killed by exact resolution;
- repair failed measurements that cannot change the decision.

---

## 20. Governing principles

> **Signals before ideas.**

> **Evidence must generate the hypothesis, not merely decorate it.**

> **Friction ≠ demand ≠ asymmetry ≠ commercial opportunity.**

> **Behavioral evidence can discover the question. Authoritative evidence should answer it.**

> **Recoverability is a prerequisite for many information-resolution opportunities.**

> **Competition should be evaluated by decision-resolution function, not category label.**

> **Do not repair a failed measurement unless the missing evidence can still change the decision.**

> **RADAR creates value by advancing strong opportunities and cheaply rejecting weak ones.**

> **A strong filter cannot compensate indefinitely for weak candidate generation.**

> **The next research action should maximize expected decision-relevant uncertainty reduction.**

> **The next spec should usually be the cleanest continuation of what reality just taught us, not the most interesting adjacent idea.**

---

## 21. Interpretation

Spec 021 tested whether RADAR had learned to **evaluate** better.

Spec 022 tests whether RADAR can begin to learn to **discover** better.

The desired long-term loop is:

```text
REALITY
   ↓
SIGNAL SOURCES
   ↓
CANDIDATE GENERATION
   ↓
CHEAP EVALUATION
   ↓
FORGE-WORTHY HYPOTHESES
   ↓
REAL EXPERIMENTS
   ↓
OUTCOMES
   ↓
LEARN WHICH SIGNALS
AND WHICH RESEARCH ACTIONS
PRODUCE ECONOMIC VALUE
   ↓
REPEAT
```

Do not automate this loop until repeated evidence identifies stable components worth automating.
