# Learning Checkpoint — Spec 023

**Checkpoint date:** 2 September 2026  
**Scope:** Spec 023  
**Relationship:** Continuation of learning checkpoints through 022.

## Outcome

Spec 023 returned **B — ONE BOUNDED TIMING UNCERTAINTY**.

Eight fresh change events produced eight opportunity hypotheses. Six were cheaply rejected, two received deeper examination, and one — Canadian September 8 counter-tariff exposure — retained exactly one decision-relevant uncertainty: whether rapidly emerging tools already provide a sufficiently complete product-level decision resolution.

This is the first recent RADAR run where the clean continuation is a bounded functional benchmark rather than another discovery pass.

## 1. Pre-consolidation sourcing improved survival

The progression is now:

```text
SPEC 021
familiar candidate set
→ strong evaluation
→ 0 survivors

SPEC 022
signal-native generation
→ less-obvious candidates
→ 0 survivors

SPEC 023
fresh changed decisions
→ signal-native generation + timing
→ 2 serious survivors
→ 1 bounded uncertainty
```

This does not prove fresh-change sourcing is generally superior. It does show that timing can materially affect candidate survival.

## 2. The opportunity clock begins with operational decision detail

A rule's proposal date is not necessarily the economically relevant start of an opportunity window.

The practical clock appears to begin when actors receive enough operational detail to make a changed decision.

```text
proposal / political announcement
        ↓
possibly too vague
        ↓
final operational detail
        ↓
DECISION UNCERTAINTY BECOMES ACTIONABLE
        ↓
early improvised resolution
        ↓
commercial response
        ↓
incumbent workflow absorption
        ↓
consolidation
```

The Canadian counter-tariff case is particularly sharp because the official product list, rates, effective date, and import decision are concrete while the commercial response market is changing over days.

## 3. Resolution-market latency is economically relevant

Spec 023 suggests that some resolution markets respond much faster than previously assumed.

```text
operational detail published
        ↓
DAYS
        ↓
calculators / scanners / consultants
        ↓
WEEKS
        ↓
incumbents absorb workflow
```

This introduces an important conceptual variable:

> **How much time remains before adequate resolution supply consolidates?**

Do not create a numeric opportunity-window score yet.

Conceptually, however:

```text
opportunity attractiveness
    depends partly on

ECONOMIC VALUE
× RESIDUAL RESOLUTION GAP
× TIME REMAINING BEFORE CONSOLIDATION
```

The Engine may eventually gain advantage not merely by discovering gaps, but by detecting and testing them faster than the market closes them.

## 4. P0 is unstable

A search finding no current resolver is weak evidence near a major implementation deadline.

A P0 state can become P1 or P2 within days.

Therefore:

- rule age alone is insufficient;
- absence of competition is insufficient;
- exact live output comparison becomes increasingly important near effective dates;
- resolution-market state must be treated as time-sensitive.

## 5. Existing distribution can collapse an apparent opportunity quickly

Freshness does not imply a greenfield market.

Training providers, payroll platforms, customs brokers, security platforms, advisers, and other incumbents can absorb changed rules through existing distribution without launching a conspicuous standalone product.

This means RADAR must inspect both:

```text
NEW RESOLUTION PRODUCTS
+
EXISTING ACTORS ABSORBING THE NEW DECISION
```

The second can eliminate an opportunity even when search results appear fragmented.

## 6. Strongest surviving hypothesis

The strongest candidate is deliberately narrow:

> **Canadian SME importer that already knows the relevant HS code → determine September 8 counter-tariff exposure, incremental landed cost, material origin/remission uncertainty, evidence, and next action before committing or repricing.**

The known-HS-code boundary is important.

It avoids pretending that a lightweight resolution can replace authoritative customs classification.

```text
KNOWN HS CLASSIFICATION
+
ORIGIN
+
CUSTOMS VALUE
+
ENTRY DATE
+
COUNTER-TARIFF RULES
+
REMISSION RULES
        ↓
DECISION INFORMATION
```

This is consistent with the Engine's recurring derived-information-asymmetry thesis: the underlying evidence may exist publicly while the economically useful answer still requires synthesis.

## 7. Remaining uncertainty is now unusually clean

The Canadian hypothesis does not currently need more broad demand research, source discovery, architecture work, or product design.

The remaining question is:

> **Has the live market already assembled the same complete decision answer?**

This should be answered by comparing outputs, not by counting competitors or reading marketing copy.

The next experiment should therefore benchmark credible live resolutions against an official truth baseline.

## 8. Core correctness vs resolution completeness

A mechanical feature-count threshold would create false precision.

The benchmark should distinguish:

### Core truth

- correct exposure;
- correct rate;
- correct effective-date treatment;
- correct incremental cost.

Material errors here mean the resolution is not adequate.

### Decision completeness

- origin/classification caveats;
- remission relevance;
- authoritative provenance;
- usable next action.

These determine whether a correct calculation actually resolves the importer's decision.

The central functional question is:

> **Will this order be hit, by how much, why, what remains uncertain, and what should the importer investigate next?**

## 9. Benchmark cases should maximize information gain

The planned 20-case benchmark is not intended to estimate population-level product accuracy.

Cases should therefore be deliberately varied and adversarial rather than statistically representative.

The set should expose different failure modes across:

- tariff rates;
- HS chapters/product families;
- straightforward and awkward tariff descriptions;
- entry dates around the effective-date boundary;
- US-origin and non-US-origin controls;
- classification/origin caveats;
- remission relevance;
- descriptions that are unsafe to resolve without known classification.

The benchmark is an information-gain instrument.

## 10. Spec 024 should terminate this RADAR branch

Spec 024 should answer the remaining market-maturity question.

Afterward:

```text
ADEQUATE EXISTING RESOLUTION?
          /            \
        YES             NO
         ↓               ↓
       PARK            FORGE
```

Do not add another RADAR validation study merely because uncertainty can always be reduced further.

If an adequate resolver exists, park the candidate and return to discovery.

If the benchmark demonstrates a material residual gap, stop researching the opportunity and hand it to FORGE for the smallest disposable experimental resolution.

This is the first deliberate terminal RADAR fork in the recent sequence.

## 11. What is supported vs unproven

**Supported:** fresh operational changes can produce candidates with stronger immediate commercial timing than the Spec 022 batch.

**Not established:** regulatory/change-event sourcing will reliably outperform other discovery paths.

**Supported:** commercial resolution supply can emerge within days or weeks.

**Not established:** RADAR can systematically exploit that latency before incumbents do.

**Supported:** the Canadian tariff candidate has a specific actor, immediate decision, material consequence, recoverable inputs, and plausible residual gap.

**Not established:** that residual gap actually exists in live resolver outputs.

**Supported:** live functional benchmarking is now the cheapest decision-changing action.

**Not established:** a demonstrated functional gap implies demand or value capture; those become FORGE questions if the candidate advances.

## 12. Next empirical question

> **Do current Canadian counter-tariff tools already resolve the importer's complete product-level decision accurately enough, or does a material functional gap remain?**

This motivates Spec 024 — Canadian Counter-Tariff Functional Benchmark.
