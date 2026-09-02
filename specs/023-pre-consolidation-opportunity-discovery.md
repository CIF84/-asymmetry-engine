# Spec 023 — Pre-Consolidation Opportunity Discovery

**Status:** Research-only timing-policy test  
**Depends on:** Specs 001–022 and learning checkpoints through 022  
**Primary objective:** Test whether RADAR can identify economically consequential decision gaps created by fresh public changes before adequate commercial resolution has consolidated.

---

## 1. Why this spec exists

Spec 021 showed that RADAR can cheaply reject weak candidates once a hypothesis exists.

Spec 022 showed that signal-native discovery can generate less obvious, more traceable hypotheses from fresh public evidence.

However, the strongest candidates still failed because commercial solutions had already emerged.

This suggests a new bottleneck:

```text
CANDIDATE GENERATION     strengthened
EVALUATION               strengthened
TIMING / PRE-CONSOLIDATION   ???
```

The governing question is:

> **Can RADAR identify economically consequential decision gaps shortly after a public rule, policy, platform, product, or market change—before adequate commercial resolution has consolidated?**

This spec tests opportunity timing, not merely novelty or problem existence.

---

## 2. Opportunity-window hypothesis

Use the following as a working research model only:

```text
CHANGE ANNOUNCED / PUBLISHED
          ↓
UNCERTAINTY CREATED
          ↓
AFFECTED ACTORS BEGIN MAKING DECISIONS
          ↓
EARLY WORKAROUNDS APPEAR
          ↓
COMMERCIAL RESOLUTION SUPPLY EMERGES
          ↓
MARKET CONSOLIDATES
```

The hypothesized opportunity window lies between:

```text
DECISION PROBLEM BECOMES CONCRETE
```

and:

```text
ADEQUATE RESOLUTION SUPPLY BECOMES MATURE
```

Freshness alone is not sufficient. A new rule may already have a mature response market.

---

## 3. Change-event scope

Inspect **6–9 fresh change events** across multiple domains and, where practical, multiple jurisdictions.

Eligible event types include:

- newly published regulation;
- recently enacted regulation before or shortly after effective date;
- tax / subsidy / eligibility changes;
- platform rule changes;
- product/service policy changes;
- standards transitions;
- new compatibility requirements;
- market-entry or market-exit events;
- newly introduced tariffs, fees, restrictions, or obligations;
- technology transitions that materially alter an economic decision.

The event should be recent enough that timing plausibly matters.

Prefer events where at least one of the following is true:

- effective date is in the future;
- effective date occurred within roughly the last 90 days;
- implementation guidance is still changing;
- affected actors are visibly asking new questions;
- products/services are still adjusting;
- provider support is incomplete or inconsistent.

This is guidance, not a rigid recency rule.

---

## 4. Anti-recycling rules

Do not use as candidate hypotheses:

- any Spec 021 candidate;
- any Spec 022 candidate;
- EV smart-charging compatibility;
- cocoa;
- appliance repair-vs-replace / quote fairness;
- previously parked opportunity families unless a genuinely new change event creates a materially different decision.

Prior work may be used only as calibration.

---

## 5. Signals before opportunities

For each change event, begin with the event itself and its first-order consequences.

Required sequence:

```text
FRESH CHANGE EVENT
      ↓
WHO IS AFFECTED?
      ↓
WHAT DECISION CHANGED?
      ↓
WHAT WAS PREVIOUSLY TRUE?
      ↓
WHAT IS NOW UNCERTAIN?
      ↓
WHEN MUST THE ACTOR DECIDE?
      ↓
WHAT IS THE ECONOMIC CONSEQUENCE?
      ↓
WHAT INFORMATION WOULD RESOLVE IT?
      ↓
IS THAT INFORMATION RECOVERABLE?
      ↓
HAS THE MARKET ALREADY RESOLVED IT?
```

Do not begin by brainstorming products for the event.

---

## 6. Change-to-decision reconstruction

For each event record:

- publication/announcement date;
- effective date or transition window if known;
- jurisdiction / market;
- affected actor(s);
- concrete economic decision created or changed;
- deadline or decision timing;
- economic consequence;
- missing information / uncertainty;
- why the change makes the uncertainty newly relevant;
- evidence that actors are already encountering the decision, if available.

Reject events that create only abstract compliance interest without a specific decision.

---

## 7. Pre-consolidation test

This is the central new gate.

For every candidate hypothesis, assess the state of the resolution market.

Classify:

```text
P0 — NO MATERIAL RESOLUTION SUPPLY FOUND
No credible decision-resolution product/service/tool found in bounded search.

P1 — EARLY / FRAGMENTED RESPONSE
Some guidance, consulting, spreadsheets, posts, or partial tools exist, but no adequate end-to-end decision resolution.

P2 — COMPETING RESOLUTIONS EMERGING
Several credible products/services address the decision, but coverage, distribution, or functional completeness appears unsettled.

P3 — CONSOLIDATED / ADEQUATELY SERVED
One or more mature solutions substantially resolve the same actor × decision × inputs × output × timing function.
```

P3 candidates should normally be parked immediately.

P2 candidates may advance only if a specific residual gap is independently evidenced.

P0/P1 do **not** prove opportunity. They merely establish that adequate resolution supply has not yet been found.

---

## 8. Exact-resolution audit

As in Specs 020–022, compare functional overlap across:

```text
ACTOR
× DECISION
× INPUTS
× RESOLUTION
× OUTPUT
× TIMING
```

Search for the hypothesized output, not merely the market category.

Examples of output-oriented searches:

- "eligibility verdict";
- "SKU transition assessment";
- "which route applies";
- "deadline/action plan";
- "configuration checker";
- "cost exposure report";
- "claim-by-claim compliance review";
- other candidate-specific functional outputs.

Do not reject a candidate merely because consultants or generic software exist.

Reject when the same decision-resolution function is already adequately available.

---

## 9. Recoverability

Classify decision information:

```text
HIGH
credible evidence can reconstruct the answer before/during the decision at plausible cost

MEDIUM
partly recoverable but material expert interpretation, private data, or maintenance remains

LOW
critical state is private, stochastic, subjective, post-decision-only, or prohibitively costly
```

LOW candidates should normally die.

Special attention:

> **A public change can create public friction while the answer still depends on private institutional state.**

Do not confuse visibility with recoverability.

---

## 10. Timing evidence

For serious candidates estimate where the opportunity sits in the response cycle.

Record evidence for:

- actors only beginning to ask questions;
- official guidance incomplete or evolving;
- suppliers/platforms updating documentation;
- early manual workarounds;
- consulting articles appearing before tooling;
- first specialist products launching;
- search results still dominated by generic guidance rather than exact resolution;
- product pages with recent launch/update dates;
- rapidly changing terminology or policy interpretation.

Do not claim an opportunity is early merely because the rule is recent.

---

## 11. Candidate generation

Generate **6–9 opportunity hypotheses**, preferably one per event unless a single event clearly creates two materially distinct decisions.

Each must be traceable:

```text
CHANGE EVENT
→ affected actor
→ changed decision
→ uncertainty
→ economic consequence
→ recoverable information
→ current resolution-market state
→ candidate hypothesis
```

Avoid generic compliance software, newsletters, or advisory services unless the change evidence specifically points to a narrow unresolved decision function.

---

## 12. Cheap RADAR gates

After candidate generation apply:

```text
ECONOMIC CONSEQUENCE
        ↓
RECOVERABILITY
        ↓
PRE-CONSOLIDATION STATE
        ↓
EXACT RESOLUTION GAP
        ↓
DISTRIBUTABILITY
        ↓
EXPERIMENTABILITY
        ↓
OPERATOR FIT
        ↓
VALUE CREATION
        ↓
POSSIBLE VALUE CAPTURE
```

Start shallow. Deepen no more than **2–4 serious survivors**.

---

## 13. Experimentability

For serious survivors reconstruct:

```text
REAL CHANGED DECISION
→ reachable affected actor
→ exposure delivered
→ noticed
→ understood
→ behavior possible
→ behavior observed
```

Assess whether a small experiment can distinguish:

```text
"the change created a real unresolved decision"
```

from:

```text
"the rule is merely interesting or confusing"
```

Prefer pre-decision/during-decision behavior over retrospective complaints.

---

## 14. Operator fit and value creation

Keep objective opportunity quality separate from operator fit.

For serious survivors state:

```text
RESOLUTION
→ VALUE CREATED
→ WHO BENEFITS
→ POSSIBLE VALUE CAPTURE
```

Possible capture mechanisms remain open: direct payment, affiliate/referral, lead generation, SaaS, data/API, licensing, sellable intelligence, proprietary dataset, investing/trading, or unknown.

Do not join programs, contact partners, collect payment, or create a business vehicle.

---

## 15. Timing advantage hypothesis

For serious survivors answer explicitly:

> **What advantage would acting now provide that would probably decay if we waited 3–6 months?**

Possible answers might include:

- first useful structured dataset;
- early search visibility;
- first self-service resolver;
- lack of incumbent coverage;
- temporary information fragmentation;
- transition-specific demand;
- arbitrage before providers update rules;
- early evidence accumulation.

If no timing advantage exists, the candidate may still be good, but it does not validate this spec's pre-consolidation thesis.

---

## 16. Time and spend envelope

### Target active research time

**90 minutes.**

Stop early if decisive evidence appears.

Exceed the target only if one explicitly identified missing fact is likely to change the verdict; record why.

### Paid research budget

**€2 maximum, preferably €0.**

Use legitimate public/free evidence first.

Do not repair failed measurements unless the missing evidence can still change the decision.

---

## 17. Verdicts

Return exactly one:

### A — PRE-CONSOLIDATION FORGE CANDIDATE

At least one fresh-change hypothesis survives and appears to sit inside a real unresolved opportunity window.

Required:

- traceable fresh change event;
- specific actor and changed decision;
- meaningful economic consequence;
- recoverable information;
- P0/P1 or justified P2 resolution-market state;
- no adequate exact resolution;
- reachable pre/during-decision behavior;
- plausible cheap experiment;
- plausible value creation;
- operator fit understood;
- explicit reason timing matters now;
- no cheaper unresolved question should obviously precede FORGE.

### B — ONE BOUNDED TIMING UNCERTAINTY

A candidate appears strong but exactly one question about market maturity, actor behavior, recoverability, or timing dominates the FORGE decision.

Recommend exactly one discriminator.

### C — NO SURVIVOR, TIMING POLICY INFORMATIVE

No candidate reaches FORGE, but the run materially learns which fresh-change events produce early opportunities versus already-consolidated responses.

### D — PRE-CONSOLIDATION DISCOVERY FAILURE

The process cannot reliably distinguish fresh-but-solved changes from genuinely early unresolved decisions within the bounded research envelope, or most candidates are too vague/non-economic to evaluate.

---

## 18. Required completion report

Return these sections in order:

1. **Verdict** — A / B / C / D and one-sentence reason.
2. **Fresh-change event table** — 6–9 events, dates, jurisdiction/domain, affected actor, changed decision.
3. **Change-to-decision reconstruction** — why each event creates a new or changed economic uncertainty.
4. **Candidate derivation map** — event → actor → decision → uncertainty → consequence → recoverability → candidate.
5. **Candidate funnel** — all candidates and disposition.
6. **Pre-consolidation state table** — P0/P1/P2/P3 for every candidate, with evidence.
7. **Exact-resolution audit** — strongest functional solutions found.
8. **Early kills** — kill stage and primary reason.
9. **Serious survivors** — no more than 2–4 deeper reconstructions.
10. **Timing evidence** — where each serious survivor sits in the response cycle.
11. **Timing advantage** — what advantage exists now and why it might decay in 3–6 months.
12. **Strongest opportunity hypothesis** — if any.
13. **Minimum experimental resolution** — only for verdict A; describe, do not build.
14. **One bounded discriminator** — only for verdict B.
15. **Why timing policy was still informative** — only for verdict C.
16. **Pre-consolidation discovery failure analysis** — only for verdict D.
17. **Comparison with Spec 022** — did timing-focused sourcing improve commercial survival rather than merely novelty?
18. **Research economics report**.
19. **What RADAR learned about opportunity timing**.
20. **Architecture implications** — preserve vs too early to institutionalize.
21. **Exactly one recommended next action**.

---

## 19. Research economics report

Report observable inputs only.

### Effort

- elapsed active research time;
- approximate searches;
- approximate major source inspections;
- paid data/API spend;
- work mode;
- visible Codex usage constraint if encountered.

### Uncertainty reduction

- dominant uncertainty entering;
- dominant uncertainty leaving;
- which timing/source hypotheses moved up/down;
- whether evidence changed the next decision.

### Evidence yield

Classify overall:

```text
HIGH YIELD
substantial learning about opportunity timing and/or a strong surviving candidate at modest effort

MEDIUM YIELD
useful timing evidence but meaningful uncertainty remains

LOW YIELD
substantial effort with little decision-relevant learning
```

Do not infer hidden token counts or unavailable compute cost.

---

## 20. Non-goals

Do **not**:

- build regulatory monitoring infrastructure;
- implement software;
- create feeds or scrapers;
- build a change-event database;
- build an opportunity-window score;
- build a source ranking system;
- build a competitor database;
- build an ontology;
- perform outreach;
- run ads;
- contact partners;
- collect payment;
- interpret freshness as proof of opportunity;
- assume no competitor means demand;
- deepen P3 candidates without independently evidenced residual gap;
- rescue weak candidates through broader geography or generic demand;
- repeat prior candidate families merely because a new article mentions them;
- spend equal effort on every event;
- repair failed measurements that cannot change the decision.

---

## 21. Governing principles

> **Signals before ideas.**

> **Evidence must generate the hypothesis, not merely decorate it.**

> **Freshness ≠ opportunity.**

> **A new rule can generate both an information gap and a rapid incumbent response wave.**

> **Public evidence of a problem does not imply public recoverability of the answer.**

> **Competition should be evaluated by decision-resolution function, not category label.**

> **RADAR creates value by advancing strong opportunities and cheaply rejecting weak ones.**

> **The next research action should maximize expected decision-relevant uncertainty reduction.**

> **The next spec should usually be the cleanest continuation of what reality just taught us, not the most interesting adjacent idea.**

> **Do not automate a timing policy before repeated evidence shows that timing itself predicts opportunity quality.**

---

## 22. Interpretation

Specs 020–022 progressively improved:

```text
020 → evaluation sequence
021 → evaluation reinforcement
022 → candidate-generation quality
```

Spec 023 tests the next layer:

```text
WHEN does RADAR look?
```

The broader hypothesis is that AI-assisted research may create an advantage not merely by finding better problems, but by recognizing and testing decision gaps **faster than resolution markets consolidate**.

That hypothesis is now ready for a bounded empirical test.
