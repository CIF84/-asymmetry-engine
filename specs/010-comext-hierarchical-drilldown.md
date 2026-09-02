# Spec 010 — Comext hierarchical drill-down research pass

## Goal

Use the existing Spec 009 Comext capability to test whether **hierarchical decomposition converts broad trade anomalies into economically interpretable changes**.

This is a research pass, not a product feature and not a persistence-layer expansion.

The key empirical question is:

> When a broad CN2 category shows value/quantity divergence, does drilling into finer product and partner structure materially reduce uncertainty about what changed?

If yes, hierarchical evidence gathering becomes a candidate reasoning operation for Asymmetry Engine.

If no, Comext remains useful primarily as contextual / confirmation evidence rather than as a discovery surface.

## Context

Spec 009 established that Comext adds genuinely orthogonal evidence:

- trade value and physical quantity can move differently,
- value-only interpretation can be materially incomplete,
- broad CN2 categories create composition ambiguity,
- implied value per mass is a diagnostic, not a market price,
- product and partner aggregation can hide the actual economic mechanism.

The current implementation intentionally persists only source-native cells and does not store growth rates, implied unit values, anomalies, mappings, or opportunity interpretations.

Do not change that architecture in this pass.

## Cases to investigate

Investigate these five Czech import categories from the 2023 → 2024 Spec 009 run:

1. **CN84 — Machinery and mechanical appliances**
   - value: approximately +4.09%
   - mass: approximately −3.37%
   - purpose: opposite-direction value / quantity movement at very large economic scale

2. **CN28 — Inorganic chemicals**
   - value: approximately −14.72%
   - mass: approximately +14.85%
   - purpose: strong inverse divergence

3. **CN18 — Cocoa and cocoa preparations**
   - value: approximately +27.65%
   - mass: approximately +1.20%
   - purpose: value acceleration with almost flat physical quantity

4. **CN85 — Electrical machinery and equipment**
   - 2024 value approximately €47.62bn
   - value: approximately −1.38%
   - mass: approximately −6.79%
   - purpose: enormous economic scale with smaller but potentially meaningful divergence

5. **CN75 — Nickel and articles thereof**
   - value: approximately +26.74%
   - mass: approximately +47.60%
   - purpose: physical growth materially faster than value growth

Treat these values as orientation from the prior empirical run, not as hard-coded truth. Recalculate from live source data where practical.

## Research method

For each CN2 case, proceed in stages.

### Stage A — confirm broad anomaly

Using current official Eurostat Comext data, confirm the 2023 and 2024 Czech import value and populated physical-quantity measure for the CN2 chapter.

Record:

- 2023 value,
- 2024 value,
- percentage value change,
- 2023 physical quantity,
- 2024 physical quantity,
- percentage quantity change,
- implied value-per-quantity change as a diagnostic only.

Do not call the implied measure a price.

### Stage B — product decomposition

Drill from the CN2 chapter into the finest practical current product level available in `DS-045409`, preferably CN8.

For the products belonging to that CN2 chapter:

- retrieve 2023 and 2024 import value,
- retrieve the populated physical quantity measure where available,
- calculate absolute contribution to CN2 value change,
- calculate absolute contribution to CN2 quantity change where meaningful,
- identify the product rows explaining most of the aggregate movement.

Do not simply rank by percentage change because tiny baselines can dominate percentage rankings.

Prefer contribution analysis such as:

```text
subcategory contribution to aggregate Δvalue
= subcategory 2024 value − subcategory 2023 value
```

Report at least the largest positive and negative contributors and the cumulative share of aggregate change explained by the top contributors when meaningful.

Where CN8 classification changes, missing values, confidentiality, or discontinued codes make direct comparison unsafe, say so explicitly rather than forcing continuity.

### Stage C — partner decomposition

For the small number of CN8 products that explain the majority of each category's movement, inspect partner-country composition.

Retrieve enough partner-level data to answer:

- Is the movement geographically concentrated or broad?
- Which countries account for the largest absolute change?
- Did supplier concentration materially change?
- Does partner decomposition alter the interpretation produced by product decomposition?

Do not exhaustively download every partner × CN8 combination if a bounded query can answer the question.

Use expected information gain to control query volume.

### Stage D — interpretation

For each CN2 case, produce an evidence-based interpretation with this structure:

```text
BROAD SIGNAL
What changed at CN2 level?

DECOMPOSITION
Which CN8 products explain it?

GEOGRAPHY
Which partners explain the important CN8 movements?

WHAT THE DATA SUPPORTS
The strongest economically defensible interpretation.

WHAT THE DATA DOES NOT SUPPORT
Alternative explanations that remain unresolved.

NEXT BEST EVIDENCE
What source or measurement would most reduce remaining uncertainty?
```

Do not generate a business opportunity merely because a trade anomaly exists.

## Hypotheses to pressure-test

The research pass should explicitly assess these hypotheses.

### H1 — hierarchical decomposition is informative

A broad CN2 anomaly can often be explained by a small number of finer product movements.

### H2 — partner decomposition adds orthogonal information

Product decomposition alone is insufficient in some cases because supplier geography materially explains the change.

### H3 — broad implied unit-value divergence often collapses under decomposition

Some apparent CN2 value/quantity divergence is primarily product-mix composition rather than a coherent underlying price-like movement.

### H4 — some anomalies survive decomposition

At least some broad signals remain directionally coherent across finer product and/or partner levels and therefore deserve additional cross-source evidence.

### H5 — anomaly shape should determine next evidence acquisition

Different decomposed patterns should imply different follow-up evidence needs rather than one universal connector sequence.

Examples:

```text
quantity ↑↑ + value →/↓
→ investigate supply expansion, commodity pricing, domestic production

value ↑↑ + quantity →
→ investigate input prices, product mix, retail/producer prices

one partner dominates Δ
→ investigate supplier dependence / policy / capacity

many products and partners move together
→ investigate broad demand or macroeconomic change
```

These are hypotheses, not rules to encode in code.

## Source / access discipline

Use official Eurostat Comext API or official Eurostat Comext downloadable data only.

Do not use scraped mirrors as the evidentiary source.

Current first-party documentation confirms that Comext is Eurostat's detailed international-trade database and that DS-prefixed Comext datasets use the dedicated Comext dissemination endpoint and must be filtered because complete datasets are too large for unrestricted API download.

Useful references:

- https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-getting-started/comext-database
- https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines/prefixed-datasets
- https://ec.europa.eu/eurostat/web/international-trade-in-goods/database

Re-check current product and partner dimension behavior against live metadata rather than assuming query syntax beyond what Spec 009 already verified.

## Implementation constraint

**Do not modify production code unless the research cannot reasonably be completed with the existing collector, small one-off scripts, direct API queries, or temporary analysis code.**

Preferred outcome:

```text
0 production-code changes
0 schema changes
0 migrations
0 new dependencies
```

Temporary scripts or notebooks used only for analysis should not be committed unless they reveal a clearly reusable capability that this research proves is needed.

If a production-code change appears necessary, stop and explain why before making it. Do not silently broaden Spec 009's collector into a generic Comext client.

## No persistence changes

Do not add:

- anomaly tables,
- derived unit-value observations,
- CN hierarchy tables,
- partner-concentration tables,
- semantic mapping tables,
- reasoning graph tables,
- opportunity entities,
- scoring changes,
- revision history.

This pass is explicitly intended to learn what abstractions the data requires before implementing them.

## Required completion report

Return a completion report containing:

1. **Method**
   - exact live dataset / dimensions used,
   - number of API requests or downloaded slices,
   - whether any temporary analysis code was required,
   - confirmation that no production code changed unless explicitly justified.

2. **Broad confirmation table**
   - all five CN2 cases,
   - value change,
   - quantity change,
   - implied-value diagnostic.

3. **Per-case decomposition**
   For each of CN84, CN28, CN18, CN85 and CN75:
   - largest CN8 contributors to value change,
   - largest physical-quantity contributors where meaningful,
   - relevant partner-country contributors,
   - concentration observations,
   - concise interpretation,
   - unresolved alternatives.

4. **Hypothesis verdicts**
   - H1 through H5 as PASS / PARTIAL / FAIL / INCONCLUSIVE,
   - with evidence supporting each verdict.

5. **Cross-case learning**
   Specifically answer:

   > Did hierarchical drill-down materially reduce uncertainty compared with CN2-only evidence?

   > Did any anomaly survive decomposition strongly enough to justify cross-source investigation?

   > Did any apparent anomaly disappear once composition was resolved?

   > Does the Engine appear to need hierarchical reasoning as a first-class concept?

6. **Next-evidence recommendations**
   For the strongest surviving cases, identify the next evidence family with the highest expected information value. Examples may include:
   - Prodcom / domestic production,
   - producer or commodity prices,
   - policy / EUR-Lex,
   - procurement,
   - patents / research,
   - supplier concentration,
   - retail prices,
   - demand / search signals.

   Do not recommend a source merely because it exists. Explain what uncertainty it would resolve.

7. **Architecture pressure**
   Report whether the exercise creates empirical pressure for any of:
   - hierarchical economic entities,
   - parent/child product relationships,
   - explicit concept mapping,
   - evidence-directed research planning,
   - relationship provenance,
   - derived-measure lineage.

   Do not implement these in this spec.

8. **Repository status**
   - tests if any production code changed,
   - working-tree status,
   - any commit SHA only if a justified repository change was made.

## Success condition

Spec 010 succeeds if it lets us make a defensible decision between these outcomes:

```text
A — HIERARCHICAL DECOMPOSITION EARNS A PLACE IN THE REASONING MODEL

B — COMEXT IS USEFUL, BUT MAINLY AS BROAD CONTEXT / CONFIRMATION

C — FINER TRADE DETAIL IS TOO AMBIGUOUS OR EXPENSIVE TO JUSTIFY NEAR-TERM USE
```

The preferred result is not A. The preferred result is whichever conclusion the evidence supports.

## After this pass

Do not automatically implement another Comext feature.

Return the evidence to ChatGPT for review.

The likely next research comparison is OpenAlex / research topology, but the result of this drill-down should determine whether that remains the highest-value next move.
