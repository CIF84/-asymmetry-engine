# Learning Checkpoint — Specs 001–019

**Checkpoint date:** 2 September 2026  
**Scope:** Specs 001–019  
**Purpose:** Compress accumulated empirical learning into better project decision policy without rewriting the historical README, architecture, roadmap, or completed specifications.

---

## 1. Why this document exists

Asymmetry Engine is itself a learning system. Its documentation should therefore distinguish between:

```text
SPECIFICATIONS
what we decided to test
        ↓
RESULTS
what reality showed us
        ↓
CHECKPOINTS
what accumulated evidence currently means
        ↓
PRINCIPLES / ARCHITECTURE
only sufficiently reinforced learning should graduate here
```

This checkpoint is not a replacement for `README.md`, `ARCHITECTURE.md`, `ROADMAP.md`, or the individual specs.

It records how the project changed through empirical contact with reality, which ideas survived, which were weakened, which new concepts emerged, and which important assumptions remain unproven.

The goal is to prevent two opposite failures:

1. forgetting what experiments already taught us;
2. turning recent observations into permanent doctrine too quickly.

---

## 2. Starting thesis and current thesis

The project began approximately as:

```text
PUBLIC DATA
    ↓
detect unusual patterns
    ↓
identify information asymmetry
    ↓
score opportunity
    ↓
build resolution
    ↓
monetize
```

This remains directionally useful, but Specs 001–019 showed that valuable opportunity discovery is less mechanical.

The current working model is closer to:

```text
              ECONOMIC REALITY
                     │
          ┌──────────┴──────────┐
          │                     │
   structural signals     behavioral exhaust
          │                     │
          └──────────┬──────────┘
                     ↓
             DECISION FRICTION
                     ↓
          INFORMATION ASYMMETRY
                     ↓
              RECOVERABILITY
                     ↓
          POSSIBLE RESOLUTION
                     ↓
      ┌──────────────┴──────────────┐
      │                             │
economic consequence        existing solutions
      │                             │
      └──────────────┬──────────────┘
                     ↓
               RESIDUAL VALUE
                     ↓
              DISTRIBUTABILITY
                     +
              EXPERIMENTABILITY
                     +
               OPERATOR FIT
                     ↓
               EXPERIMENT
                     ↓
             ECONOMIC EVIDENCE
                     ↓
                  LEARN
                     │
                     └──────────────↺
```

A better current description of the Engine is therefore:

> **Find economically consequential uncertainty that can be resolved better than the market currently resolves it, then discover the cheapest reliable path to economic evidence.**

The Engine is becoming less an "asymmetry detector" and more an **economic hypothesis discovery and falsification system**.

This is a working interpretation, not a final ontology.

---

## 3. Evolution through Specs 001–019

### 3.1 Specs 001–009 — learning to observe heterogeneous reality

The early vertical slices tested whether the system could legitimately and consistently observe heterogeneous public signals.

Sources included Stack Exchange, CFPB, DataForSEO, TED, Eurostat SBS, Azure Retail Prices, and Comext.

The architectural spine that survived is deliberately simple:

```text
SOURCE
  ↓
OBSERVATION
  ↓
NORMALIZATION
  ↓
PERSISTENCE
  ↓
PROVENANCE
```

The most important learning was not merely that multiple sources could be ingested.

It was that **more observable data does not automatically create economic understanding**.

The source-independent observation model survived substantial variation in source semantics. That is evidence in favor of the modular observation architecture.

### 3.2 Specs 010–012 — observation became economic reasoning

Hierarchical Comext work demonstrated that an apparently interesting aggregate can weaken or disappear when decomposed.

This reinforced:

> **Observation is not explanation.**

It also showed that hierarchy can reduce uncertainty without itself supplying semantics.

OpenAlex then added semantic resolution and temporal/velocity considerations while exposing model-time leakage risk.

Spec 012 tested whether persisted evidence could support a structured economic argument:

```text
observations
    ↓
measurements
    ↓
entity
    ↓
relationships
    ↓
disequilibrium
    ↓
structured explanation
```

That reasoning chain worked for the tested case.

However, the experiment also exposed the danger of institutionalizing one successful reasoning pattern too early. A generic survival threshold and broader ontology were not empirically earned.

This reinforced a core architecture principle:

> **Let abstractions earn their existence empirically.**

### 3.3 Specs 013–016 — commercial reality became part of the model

Spec 013 pressure-tested whether structurally interesting asymmetries translated into commercially attractive opportunities.

Nickel was economically interesting but commercially distant. Chemicals contained strong asymmetry but poor operator fit and substantial trust/regulatory burden. Solar/battery comparison appeared crowded. Cocoa survived as the most plausible candidate for a cheap commercial test.

Spec 014 then exposed a different failure mode: a plausible proposition is not equivalent to an executable experiment. Public prospects could be identified, but legitimate authenticated outreach could not be executed within the available setup.

The resulting experiment was **invalid**, not negative.

Subsequent sample-size analysis exposed another important issue: zero responses from a small cold-outreach sample can be weak evidence because the measurement channel is lossy.

```text
REAL DEMAND
   ↓
reachable prospect
   ↓
delivered
   ↓
noticed
   ↓
understood
   ↓
motivated
   ↓
OBSERVED INTENT
```

This produced a durable principle:

> **Absence of observed demand is evidence only to the extent that the experiment had sufficient power to observe demand.**

Experimentability therefore became part of opportunity quality rather than a downstream implementation detail.

Spec 015 made this explicit.

Spec 016 then tested the appliance repair-vs-replace hypothesis against actual search behavior. The evidence did not strongly support the exact proposition. Adjacent repair-cost and appliance-lifespan intent was measurable, while explicit repair-vs-replace intent was weak.

Rather than inflate the hypothesis using adjacent demand, the opportunity was narrowed toward possible repair-quote fairness / repair economics uncertainty.

This reinforced:

> **Do not expand a weakly observed hypothesis by absorbing adjacent intent merely to make the market look larger.**

### 3.4 Specs 017–018 — behavioral signals became a discovery path

The appliance result suggested that market behavior can feed backward into opportunity discovery.

Instead of only:

```text
STRUCTURAL SIGNAL
      ↓
ASYMMETRY
      ↓
behavioral validation
```

RADAR can also use:

```text
OBSERVED BEHAVIOR
      ↓
repeated economic uncertainty
      ↓
decision friction
      ↓
inferred asymmetry
```

Spec 017 tested several behavioral signal classes. Reviews, search intent, complaints, questions/forums, market/price behavior, and tenders had different strengths and biases.

The result supported behavioral-first discovery as a **complementary path**, not a replacement for asymmetry-first discovery.

Spec 018 then tested whether reviews could reveal commercially interesting hidden decision variables across unrelated categories.

This produced an important discriminator:

```text
HIDDEN
  +
DECISION-RELEVANT
  +
PRE-DECISION RECOVERABLE
  +
INSUFFICIENTLY SURFACED
  +
ECONOMICALLY CONSEQUENTIAL
```

Many review complaints failed this test because they described stochastic quality, service failure, preference, or facts only knowable after purchase.

This made **recoverability** a first-class opportunity filter.

The EV smart-charging case survived because the missing answer appeared derivable before purchase from fragmented authoritative evidence.

### 3.5 Spec 019 — derived information asymmetry became concrete

The EV case exposed a form of asymmetry where no single actor necessarily possesses a hidden fact.

Instead:

```text
VEHICLE MAKER knows A
CHARGER MAKER knows B
ENERGY SUPPLIER knows C
HOUSEHOLD knows D

but the consumer needs

f(A, B, C, D)
```

The economically useful information is the **derived answer**.

Spec 019 tested exactly 10 representative UK configurations and reproducibly resolved 9 of 10 using authoritative public evidence.

The work demonstrated that configuration-level compatibility can often be reconstructed with provenance, while also exposing material maintenance costs:

- every compatible case contained material conditions;
- supplier documentation can be fragmented;
- live pages can contradict one another;
- pages can be undated;
- integrations change;
- household contexts create combinatorial complexity;
- broad coverage may require source monitoring and human exception handling.

The result therefore supported narrow evidence feasibility without proving broad product scalability.

This reinforced:

> **Behavioral evidence can discover the question. Authoritative evidence should answer it.**

and:

> **Do not validate the scalability of an unvalidated product.**

---

## 4. What has been reinforced

The following ideas have survived multiple forms of empirical pressure and should guide current work.

### 4.1 Friction, demand, asymmetry, and opportunity are distinct

```text
FRICTION
≠ DEMAND
≠ ASYMMETRY
≠ COMMERCIAL OPPORTUNITY
```

Each transition requires evidence.

### 4.2 Price dispersion is not automatically information asymmetry

Observed price differences may result from product differences, geography, timing, contract structure, taxes, quality, logistics, or other causes.

The Engine must reconstruct the economic mechanism rather than label dispersion as asymmetry.

### 4.3 Derived values are diagnostic until economically interpreted

For example, trade unit values can expose structure but are not automatically market prices.

### 4.4 Decomposition is useful when it reduces uncertainty

Hierarchical drilldown should be selective and driven by expected information gain rather than exhaustive traversal.

### 4.5 Behavioral evidence is powerful but biased

Searches, reviews, complaints, and questions expose real behavior, but each contains selection effects.

Visible behavior can overrepresent:

- complaints;
- post-purchase failure;
- search-visible problems;
- emotionally salient experiences;
- platform-specific populations;
- incumbent terminology;
- jurisdictions with accessible public evidence.

Behavioral-first discovery should complement structural/asymmetry-first discovery.

### 4.6 Recoverability matters

A hidden variable is commercially useful only if the missing information can plausibly be recovered before or during the economic decision.

### 4.7 Experimentability is part of opportunity quality

A theoretically valuable opportunity can be unattractive if commercial hypotheses require long, expensive, noisy, or legally difficult experiments.

Current opportunity reasoning therefore includes at least:

```text
ASYMMETRY QUALITY
+ RESOLUTION QUALITY
+ ECONOMIC CONSEQUENCE
+ COMPETITION
+ DATA FEASIBILITY
+ DISTRIBUTABILITY
+ EXPERIMENTABILITY
+ OPERATOR FIT
+ VALUE-CAPTURE PLAUSIBILITY
```

This is a conceptual checklist, **not authorization to build a generic scoring model**.

### 4.8 Provenance can be part of the resolution

When value comes from synthesizing fragmented authoritative information, the answer may be more useful because the system can explain why it believes the answer and show the supporting evidence.

### 4.9 Architecture should follow repeated empirical pressure

The modular monolith, generic observation primitive, SQLite persistence, source independence, provenance, and separation between immutable evidence and mutable interpretation have survived.

Generic ontologies, graph models, universal scoring engines, production compatibility databases, and broad automated reasoning abstractions have not yet earned implementation.

---

## 5. RADAR has changed

RADAR should no longer be interpreted merely as a ranking system for detected anomalies.

Its current working responsibility is closer to:

> **Transform heterogeneous evidence into falsifiable opportunity hypotheses.**

A RADAR output should therefore not be:

> Build an EV compatibility website.

It should resemble:

> There appears to be unresolved economic uncertainty around configuration-level EV smart-charging compatibility. The answer is consequential, pre-decision useful, derivable from authoritative evidence, incompletely surfaced by the market, and potentially observable through specific decision channels.

That is an **opportunity hypothesis**, not a product specification.

RADAR currently has two complementary discovery directions:

```text
ASYMMETRY-FIRST
structural economic evidence
→ possible gap
→ behavioral validation

BEHAVIORAL-FIRST
observed decision behavior
→ inferred uncertainty
→ asymmetry reconstruction
```

Neither has yet been shown universally superior.

---

## 6. Emerging interpretation of FORGE

The project originally risked treating FORGE as:

```text
RADAR
find opportunity
    ↓
FORGE
build product
    ↓
MARKET
money
```

Accumulated learning suggests a more useful early interpretation:

```text
RADAR
What uncertainty appears valuable?
        ↓
FORGE
What is the cheapest thing we can create
that tests whether resolving it creates value?
        ↓
REALITY
        ↓
BEHAVIORAL EVIDENCE
        ↓
RADAR learns ↔ FORGE learns
```

FORGE should initially manufacture **experimental resolutions**, not necessarily businesses.

Possible FORGE outputs include:

- manually generated answers;
- single-purpose webpages;
- calculators;
- comparison artifacts;
- reports;
- datasets;
- alerts;
- algorithms;
- simulated portfolios;
- trading rules;
- affiliate/referral paths;
- API endpoints;
- eventually software products.

The common property is:

> **FORGE transforms an opportunity hypothesis into something capable of interacting with reality.**

This interpretation remains to be experimentally validated.

---

## 7. Separate resolution, value creation, and value capture

Specs 001–019 and the subsequent checkpoint discussion suggest that the following concepts should remain separate:

```text
OPPORTUNITY
    ↓
RESOLUTION
    ↓
VALUE CREATED
    ↓
VALUE CAPTURED
```

The actor experiencing the asymmetry does not necessarily need to be the payer.

Possible downstream value-capture mechanisms include:

- direct consumer payment;
- affiliate/referral economics;
- lead generation;
- advertising;
- SaaS;
- data/API access;
- licensing;
- proprietary datasets;
- sale of opportunities/intelligence;
- investing/trading using proprietary signals;
- mechanisms not yet discovered.

The Engine should not prematurely assume the correct branch.

A useful working principle is:

> **Reach repeatable evidence of value creation quickly, then determine the cheapest scalable mechanism for capturing some of that value.**

This does **not** weaken the requirement for eventual economic validation.

A free artifact that users like but that cannot contribute to sustainable economics is not sufficient long-term evidence.

---

## 8. Non-monetary reinforcement before monetization

Payment remains strong evidence, but it need not always be the first useful reinforcement signal.

The evidence ladder can be separated into three layers.

### Discovery evidence

```text
observation
→ repeated friction
→ credible asymmetry
```

### Resolution evidence

```text
resolution presented
→ engagement
→ decision affected
→ action taken
→ repeat use / referral
```

### Commercial evidence

```text
priced intent
→ transaction
→ repeat transaction
→ unit economics
```

This creates three distinct questions:

```text
RADAR
Is there something worth resolving?

FORGE
Does our resolution actually improve or affect the decision?

PORTFOLIO / VALUE CAPTURE
Can that improvement be captured economically?
```

The causal relationship between non-monetary resolution evidence and eventual economic value is **not yet proven**. It must itself become an empirical learning target.

---

## 9. FORGE velocity hypothesis

If RADAR eventually generates opportunity hypotheses quickly, FORGE cannot require conventional product-development cycles for every candidate.

Early FORGE may need to optimize for:

```text
speed
reversibility
observability
cheapness
specificity
disposability
```

rather than immediately optimizing for:

```text
durability
scalability
completeness
maintainability
production reliability
```

Working hypothesis:

> **Disposable before durable.**

The intended sequence is:

```text
opportunity hypothesis
        ↓
what must be true?
        ↓
what observable behavior distinguishes true from false?
        ↓
minimum resolution capable of producing that behavior
        ↓
BUILD / PRESENT
        ↓
MEASURE
        ↓
discard / modify / deepen
        ↓
only then consider durable asset engineering
```

This hypothesis should be tested rather than institutionalized prematurely.

---

## 10. The Engine's own learning loops

The project now appears to contain at least three reinforcement loops.

### Loop 1 — Economic learning

```text
Which asymmetries produce economic value?

opportunity
→ experiment
→ behavior/payment
→ outcome
```

### Loop 2 — Discovery learning

```text
Which signals reveal good opportunities?

source
→ pattern
→ opportunity hypothesis
→ downstream quality
```

### Loop 3 — Research-policy learning

```text
Which investigation most cheaply reduces
whatever uncertainty matters next?

question
→ research action
→ evidence
→ decision change
```

Loop 3 is newly explicit, although Specs 001–019 have already generated historical examples.

The Engine should eventually learn not only **which opportunities work**, but also **which research actions work**.

---

## 11. Research and compute are economic inputs

Specs 001–019 were completed at unusually high velocity, with substantial AI-assisted research and implementation effort.

At this checkpoint, the inference/compute burden appears to have produced substantial uncertainty reduction. It should therefore not be optimized away merely because usage was high.

However, compute is not free economically simply because its marginal cash cost may be hidden by a subscription or quota.

The relevant conceptual relationship is:

```text
                 DECISION-RELEVANT INFORMATION GAIN
RESEARCH VALUE ≈ ───────────────────────────────────
                 time + paid data + compute + effort
```

No generic numerical score is justified yet.

Beginning with Spec 020, completion reports should record observable research economics including elapsed time, approximate research activity, paid data cost, visible compute constraints, uncertainty entering/leaving the experiment, decision change, and qualitative evidence yield.

Preserve:

> **Compute and research effort are economic inputs. If increasingly expensive inference produces only tiny increments of evidence, that is itself an operating-cost signal.**

Current checkpoint assessment of Specs 001–019: **high evidence yield despite high activity**, because multiple major hypotheses, opportunity filters, research methods, and architectural assumptions changed materially in a short period.

This assessment should be revisited as evidence accumulates.

---

## 12. Clean continuation as project policy

The project generates many plausible adjacent opportunities. AI makes generating additional branches extremely cheap.

Therefore the scarce resource is not ideas. It is cumulative evidence.

A useful operating rule is:

> **The next spec should usually be the cleanest continuation of what reality just taught us, not the most interesting adjacent idea.**

In simplified form:

```text
Spec N
  ↓
reality teaches X
  ↓
Spec N+1 should maximize
useful information about X
```

Continue until the hypothesis either:

```text
strengthens enough → FORGE / deeper experiment
```

or:

```text
weakens enough → NARROW / PARK / KILL
```

This is intended to create depth without attachment and to resist research drift.

---

## 13. Revised project success ladder

The project's success criteria have become more precise.

### Phase I — OBSERVE

Can the Engine acquire and preserve legitimate heterogeneous evidence?

**Checkpoint status: achieved sufficiently for current work.**

### Phase II — REASON

Can observations support structured economic interpretation rather than merely anomaly detection?

**Checkpoint status: achieved sufficiently for current work.**

### Phase III — REJECT

Can the Engine falsify attractive but weak hypotheses without protecting them?

**Checkpoint status: repeatedly demonstrated.**

### Phase IV — DISCOVER

Can the Engine generate promising opportunity hypotheses from structural and behavioral evidence?

**Checkpoint status: increasingly supported, not yet proven repeatably.**

### Phase V — RESOLVE

Can the Engine/FORGE cheaply create a useful resolution to the uncertainty?

**Checkpoint status: entering this phase.**

### Phase VI — VALIDATE VALUE

Does the resolution change meaningful behavior?

**Checkpoint status: unproven.**

### Phase VII — CAPTURE VALUE

Can some of the created value be captured through a scalable mechanism?

**Checkpoint status: unproven.**

### Phase VIII — REPEAT

Can RADAR → FORGE → value capture work for materially different opportunities?

**Checkpoint status: unproven.**

### Phase IX — SELF-IMPROVE

Does accumulated evidence improve opportunity selection, experiment selection, research allocation, and eventual capital allocation?

**Checkpoint status: conceptual / early manual evidence only.**

---

## 14. Revised success criterion

A weak definition of success would be:

> Discover interesting information asymmetries.

A stronger current definition is:

> **Repeatedly convert inexpensive observations into economically validated opportunities faster and more cheaply than unaided entrepreneurial search, then compound successful resolutions into assets or other value-capture mechanisms.**

Evidence levels can be thought of as:

### Minimum proof

The Engine discovers an opportunity that eventually produces a real transaction or otherwise defensible captured economic value.

### Strong proof

It does so for at least two materially different opportunities.

### System proof

It repeatedly produces opportunities whose cumulative captured economic value exceeds the cost of:

```text
data
+ compute
+ experimentation
+ development
+ maintenance
+ operator time
```

### Portfolio proof

Outputs become assets or strategies that materially contribute to recurring cash flow, automation, diversification, accumulated knowledge, optionality, and ultimately greater freedom from external control.

The Engine itself does **not** necessarily need to become the business.

It may become the discovery, experimental-resolution, and eventually capital-allocation intelligence feeding FORGE and PORTFOLIO.

---

## 15. What we deliberately do not know yet

The following distinctions are important epistemic guardrails.

### Behavioral-first discovery

**Supported:** behavioral-first discovery can expose decision-proximate friction and useful asymmetry hypotheses.

**Not established:** behavioral-first discovery is superior overall to structural/asymmetry-first discovery.

### Derived information asymmetry

**Supported:** economically useful missing answers can be derived from fragmented public information even when no single hidden fact exists.

**Not established:** derived-information opportunities monetize better than other asymmetry classes.

### Recoverability

**Supported:** pre-decision recoverability is a strong filter against many false opportunities.

**Not established:** recoverability alone predicts commercial attractiveness.

### Non-monetary reinforcement

**Supported:** behavioral interaction with a resolution can provide information before payment is tested.

**Not established:** non-monetary behavioral evidence reliably predicts willingness to pay or another durable value-capture mechanism.

### EV compatibility

**Supported:** narrow UK EV smart-charging configuration answers are frequently derivable from authoritative public evidence.

**Not established:** enough users need the answer; users will change behavior because of it; a viable acquisition surface exists; the information can be monetized; broad coverage is economically maintainable.

### FORGE

**Supported:** separating opportunity discovery from experimental resolution is conceptually useful.

**Not established:** the proposed fast/disposable FORGE operating model will generate reliable behavioral evidence at acceptable cost.

### AI-assisted velocity

**Supported:** AI assistance has enabled very rapid research and implementation across Specs 001–019.

**Not established:** the resulting information gain will continue to justify inference/compute burden as the Engine scales.

### Scoring

**Supported:** opportunity quality is multidimensional.

**Not established:** those dimensions should be combined into a stable generic score, weighting system, or ontology.

### Monetization

**Supported:** direct payment is only one possible value-capture mechanism.

**Not established:** which value-capture mechanism is best for the Engine's eventual opportunity portfolio.

---

## 16. Architectural implications at this checkpoint

### Strong enough to preserve

- modular monolith;
- source-independent observations;
- immutable evidence / mutable interpretation;
- provenance;
- source legitimacy and access constraints;
- SQLite for current experimental scale;
- small vertical slices;
- hypothesis → implementation/research → real evidence → review;
- structural-first and behavioral-first discovery as complementary research paths;
- experimentability as an opportunity-quality consideration;
- operator fit separated from objective opportunity quality;
- research economics as an observable project input;
- explicit PARK / NARROW / KILL decisions;
- specs as historical experimental contracts once execution begins.

### Too early to institutionalize

- generic asymmetry ontology;
- universal opportunity scoring engine;
- generic economic knowledge graph;
- production EV compatibility model;
- automated review-mining infrastructure;
- broad search-intent ingestion infrastructure;
- generic research-efficiency score;
- autonomous opportunity selection;
- autonomous capital allocation;
- universal FORGE artifact framework;
- assumption that direct consumer monetization is preferred;
- assumption that SaaS is preferred;
- assumption that non-monetary behavior predicts payment;
- assumption that EV is the first portfolio asset.

---

## 17. Immediate transition after this checkpoint

Spec 020 is intentionally a commercial-evidence gate rather than another EV technical/data study.

Its role is to determine whether configuration-specific EV compatibility uncertainty is sufficiently observable and reachable to justify a behavioral artifact.

If it passes, the likely significance is not:

> Build an EV business.

It is:

> **RADAR has produced a hypothesis strong enough to hand to FORGE for an experimental resolution.**

That would mark the first deliberate transition from discovery toward resolution-value validation.

If it fails, the correct response is to preserve the learning and return to RADAR rather than rescue the opportunity through scope expansion.

---

## 18. Checkpoint summary

Specs 001–019 substantially changed the project without invalidating its original thesis.

The project began by asking whether public signals could reveal monetizable information asymmetries.

It now asks a more disciplined question:

> **Where is economically consequential uncertainty already visible, can the missing decision information be recovered better than the market currently recovers it, can we test the resolution cheaply and with sufficient experimental power, and can successful resolutions eventually be converted into durable economic value?**

The central system is increasingly:

```text
OBSERVE REALITY
      ↓
FIND UNCERTAINTY
      ↓
DERIVE RESOLUTION
      ↓
FALSIFY CHEAPLY
      ↓
VALIDATE VALUE
      ↓
CAPTURE VALUE
      ↓
MEASURE OUTCOME
      ↓
LEARN WHAT WORKED
      ↓
IMPROVE OPPORTUNITY SELECTION
+ IMPROVE RESEARCH SELECTION
+ IMPROVE EXPERIMENT SELECTION
      ↓
REPEAT
```

The most important unresolved risk is now less about whether the Engine can observe or reason and more about whether its hypotheses can cross the boundary into **real behavioral and economic value**.

That is the next empirical frontier.
