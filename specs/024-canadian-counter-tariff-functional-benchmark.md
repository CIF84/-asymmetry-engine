# Spec 024 — Canadian Counter-Tariff Functional Benchmark

**Status:** Research-only terminal RADAR discriminator  
**Depends on:** Specs 001–023 and learning checkpoints through 023  
**Primary objective:** Determine whether current Canadian counter-tariff tools already resolve the importer's complete product-level decision accurately enough, or whether a material functional gap remains that warrants a FORGE handoff.

---

## 1. Why this spec exists

Spec 023 returned:

> **B — ONE BOUNDED TIMING UNCERTAINTY**

The strongest candidate was:

> **Canadian SME importer that already knows the relevant HS code → determine September 8 counter-tariff exposure, incremental landed cost, material origin/remission uncertainty, evidence, and next action before committing or repricing.**

The remaining uncertainty is narrow:

> **Has the live market already assembled the same complete decision answer?**

This spec answers that question by comparing actual functional outputs against an official truth baseline.

This is not another opportunity-discovery pass.

This is intended to terminate this RADAR branch.

```text
ADEQUATE EXISTING RESOLUTION?
          /            \
        YES             NO
         ↓               ↓
       PARK            FORGE
```

No additional RADAR validation study should follow unless this benchmark itself is invalid or impossible to execute.

---

## 2. Candidate boundary

Keep the candidate deliberately narrow.

### Actor

Canadian SME importer or buyer evaluating an order involving US-origin goods.

### Decision

Before committing, shipping, receiving, or repricing:

- import;
- renegotiate;
- substitute;
- defer;
- reprice;
- investigate remission or another exception.

### Required known inputs

The benchmark assumes the importer already knows or has obtained:

- HS classification;
- origin facts sufficient for the test case;
- customs value;
- relevant entry/import date.

Do **not** expand the opportunity into customs classification.

A tool may flag classification uncertainty, but the benchmark must not reward unsupported product-name → HS-code guessing as equivalent to authoritative classification.

---

## 3. Resolution job to be benchmarked

The complete decision job is:

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
REMISSION / EXCEPTION RULES
        ↓
EXPOSURE VERDICT
+
RATE
+
INCREMENTAL COST
+
MATERIAL CAVEATS
+
PROVENANCE
+
NEXT ACTION
```

In plain language:

> **Will this order be hit, by how much, why, what remains uncertain, and what should the importer investigate next?**

---

## 4. Benchmark philosophy

Use exactly **20 fixed test cases**.

The purpose is not to estimate population-level accuracy.

The purpose is to expose whether live resolutions are functionally complete and where they fail.

Therefore the cases should be **deliberately varied and adversarial**, while remaining realistic and grounded in authoritative rules.

Do not randomly sample products.

Do not choose twenty easy positive cases.

Do not tune cases to make competitors fail.

The set should maximize decision-relevant information gain.

---

## 5. Required case coverage

The 20 cases must collectively include meaningful variation across:

- multiple tariff rates present in the September 8 measures;
- multiple HS chapters / product families;
- clearly exposed products;
- non-exposed controls;
- US-origin cases;
- non-US-origin controls where relevant;
- entry dates immediately before the effective date;
- entry dates on/after the effective date;
- straightforward tariff-line descriptions;
- awkward or easily misread tariff descriptions;
- cases where classification caveats matter;
- cases where origin caveats matter;
- cases where remission or exception review is plausibly relevant;
- at least one case where a commercial description alone would be unsafe to resolve without the supplied HS code.

Record why each case was included.

If an intended category cannot be supported by authoritative evidence, do not fabricate it; replace it with another documented failure mode and explain the substitution.

---

## 6. Official truth baseline

Before testing commercial/self-service tools, establish the expected result for all 20 cases from authoritative Canadian sources.

Prefer, in order:

1. Government of Canada / Department of Finance counter-tariff list and official notices;
2. CBSA / CARM / Customs Tariff sources where applicable;
3. official remission orders, guidance, notices, or explanatory material;
4. other authoritative Canadian government sources necessary to interpret effective dates or treatment.

For each case record:

- case ID;
- realistic product description;
- supplied HS code;
- origin;
- customs value;
- entry date;
- expected exposure: YES / NO / CONDITIONAL;
- expected counter-tariff rate;
- expected incremental counter-tariff cost;
- material classification caveat;
- material origin caveat;
- remission/exception relevance: YES / NO / REVIEW REQUIRED;
- authoritative evidence URL(s);
- short reasoning trace.

If official evidence does not permit a defensible expected result, mark the case **UNRESOLVED BASELINE** and replace it before benchmarking tools.

All 20 benchmark cases must have defensible baselines.

---

## 7. Resolver discovery

Perform one fresh bounded search for credible publicly accessible/self-service resolutions available at execution time.

Include tools found in Spec 023 if still live, plus newly discovered credible resolvers.

Potential classes:

- official Canadian tools;
- tariff calculators;
- counter-tariff-specific checkers;
- catalog/manifest scanners;
- customs/broker self-service tools;
- other public tools that claim substantially the same product-level resolution.

Exclude pure articles, generic newsletters, or contact-us consulting pages from functional scoring unless they expose an actual self-service output.

Record tools that claim the function but cannot be tested publicly as **UNTESTABLE COMMERCIAL SUPPLY**. Discuss them separately; do not pretend their marketing claims prove functional adequacy.

Do not purchase subscriptions or services unless a free trial already available without new financial commitment is necessary and clearly within scope.

Paid budget remains €2 maximum, preferably €0.

---

## 8. Test the same cases against each resolver

Where technically and legally possible, test the same 20 cases against every credible accessible resolver.

If a resolver cannot accept the benchmark inputs or cannot process a case, record that as a functional limitation rather than silently excluding the case.

Do not use automation, scraping, or high-volume requests if prohibited or unnecessary.

Manual entry is acceptable.

Do not bypass access controls, rate limits, authentication requirements, or terms.

---

## 9. Core correctness

Evaluate these fields separately from all other features:

### C1 — Exposure

Does the resolver correctly determine whether the supplied case is subject to the relevant counter-tariff?

### C2 — Rate

Does it return the correct applicable counter-tariff rate?

### C3 — Effective-date treatment

Does it correctly distinguish the supplied before/after effective-date case?

### C4 — Incremental cost

Does it correctly calculate the incremental counter-tariff amount from the supplied customs value and applicable rate?

These are **core truth**.

A material error in core truth is more important than missing convenience features.

Do not collapse core correctness into a single feature count.

---

## 10. Decision completeness

Evaluate these separately:

### D1 — Classification caveat

Does the output appropriately preserve the supplied HS code and flag when classification remains material rather than silently treating product-name inference as authoritative?

### D2 — Origin caveat

Does it distinguish tariff-line exposure from the factual/legal origin condition required for the measure to apply?

### D3 — Remission / exception relevance

Does it identify when a remission, exception, or additional official review is materially relevant?

It does not need to provide legal advice or guarantee eligibility.

### D4 — Authoritative provenance

Does the output link or clearly trace the decision to authoritative Canadian evidence sufficiently for the importer to inspect why the answer was produced?

### D5 — Usable next action

Does the resolver convert the result into a useful action such as:

- no counter-tariff exposure identified;
- confirm origin;
- confirm classification with broker/customs specialist;
- investigate identified remission route;
- quantify repricing exposure;
- compare substitution;
- escalate unresolved case.

Do not reward generic marketing copy as a useful action.

---

## 11. Failure-mode logging

For every material failure, classify the failure where possible:

```text
WRONG EXPOSURE
WRONG RATE
WRONG DATE TREATMENT
WRONG COST
CLASSIFICATION OVERCLAIM
ORIGIN BLINDNESS
REMISSION BLINDNESS
NO PROVENANCE
NO ACTIONABLE OUTPUT
INPUT NOT SUPPORTED
OUTPUT UNRESOLVED
TOOL FAILURE
ACCESS / TESTABILITY LIMITATION
OTHER
```

Record examples.

The objective is to understand whether the market's residual gap is systematic rather than merely count missing fields.

---

## 12. Adequacy test

Do **not** use a mechanical `6 of 7 fields × 18 of 20 cases` threshold.

Judge adequacy using two distinct layers.

### Layer A — Core reliability

An existing resolver is **not adequate** if it exhibits material, non-edge-case errors in:

- exposure;
- rate;
- effective-date treatment;
- incremental cost.

A single genuinely pathological edge case does not automatically prove a market gap. Explain materiality and pattern.

### Layer B — Decision resolution

Among tools with reliable core truth, ask whether at least one accessible resolver substantially answers:

> **Will this order be hit, by how much, why, what remains uncertain, and what should the importer investigate next?**

A resolver can be adequate without beautiful UX or every optional feature.

A resolver is not inadequate merely because another product could be more convenient, more polished, AI-enabled, or personalized.

The residual gap must be economically meaningful.

---

## 13. Market-level interpretation

After individual tool testing, classify the market:

### P3 — ADEQUATELY RESOLVED

At least one credible accessible resolver provides reliable core truth and substantially complete decision resolution for the bounded job.

**Action: PARK.**

### P2 — MATERIAL FUNCTIONAL GAP DEMONSTRATED

Existing tools provide pieces of the answer, but benchmark evidence demonstrates a recurring economically meaningful gap in core reliability or decision completeness.

**Action: FORGE HANDOFF.**

### INVALID BENCHMARK

The official truth baseline cannot be established, credible tools cannot be tested sufficiently, the live measures differ materially from the Spec 023 premise, or another execution problem prevents a defensible market comparison.

Only this outcome permits another RADAR research spec.

Do not invent a P0/P1 conclusion from tool absence alone.

---

## 14. FORGE handoff if P2

If and only if the benchmark demonstrates P2, define the smallest disposable experimental resolution.

Do **not** build it.

The handoff must specify:

```text
ACTOR
→ INPUT
→ TRANSFORMATION
→ OUTPUT
→ DECISION IMPROVED
→ OBSERVABLE BEHAVIOR
→ VALUE CREATED
```

Keep the known-HS-code boundary unless benchmark evidence specifically proves that classification is both necessary and safely tractable.

The experimental resolution should optimize:

- speed;
- reversibility;
- observability;
- cheapness;
- specificity;
- disposability.

Not durability or scalability.

---

## 15. Terminal-branch rule

This spec is intended to terminate the Canadian counter-tariff RADAR branch.

### If P3

Park the candidate.

Return to broader RADAR discovery in a future spec.

Do not perform demand research, keyword research, interviews, maintenance studies, feature comparisons, or prototype work for this candidate.

### If P2

Stop RADAR research.

The next spec must be a FORGE experiment for the minimum disposable resolution.

Do not add another market study, demand gate, competitor audit, data-feasibility study, or architecture spec first.

### If INVALID BENCHMARK

Recommend exactly one action that repairs the benchmark's validity, and explain why it can change the decision.

---

## 16. Time and spend envelope

### Target active research time

**90 minutes.**

Because manual testing across 20 cases may be slower than prior research, a bounded overrun is acceptable only if completing one already-started resolver comparison will materially change the market verdict.

Record any overrun and why.

### Paid research budget

**€2 maximum, preferably €0.**

Do not create paid accounts or subscriptions merely to complete the benchmark.

---

## 17. Required completion report

Return these sections in order:

1. **Verdict** — P3 / P2 / INVALID BENCHMARK and one-sentence reason.
2. **Benchmark date and live-policy check** — confirm the relevant Canadian measure is still materially as assumed.
3. **20-case benchmark table** — inputs, expected official truth, inclusion rationale, authoritative provenance.
4. **Resolver set** — every credible live resolver tested or classified as untestable commercial supply.
5. **Core correctness results** — C1–C4 by resolver and case, with material error summary.
6. **Decision completeness results** — D1–D5 by resolver and case or applicable output pattern.
7. **Failure-mode table** — material failures and examples.
8. **Best existing resolver** — strongest functional incumbent and why.
9. **Functional gap analysis** — exactly what remains unresolved, if anything.
10. **Market-level interpretation** — why evidence supports P3, P2, or invalidity.
11. **Minimum disposable FORGE resolution** — only if P2; describe, do not build.
12. **Why PARK is correct** — only if P3.
13. **Benchmark validity problem** — only if INVALID BENCHMARK.
14. **Research economics report**.
15. **What RADAR learned about timing and live functional competition**.
16. **Architecture implications** — preserve vs too early to institutionalize.
17. **Exactly one next action**, constrained by the terminal-branch rule.

---

## 18. Research economics report

Report observable inputs only.

### Effort

- elapsed active research time;
- approximate searches;
- resolver tools tested;
- case executions;
- major authoritative source inspections;
- paid spend;
- visible Codex usage constraint if encountered.

### Uncertainty reduction

- entering uncertainty;
- leaving uncertainty;
- whether live output testing changed the candidate classification;
- whether the result terminates RADAR as intended.

### Evidence yield

Classify:

```text
HIGH YIELD
benchmark clearly changes or resolves the PARK/FORGE decision at modest cost

MEDIUM YIELD
useful functional evidence but some material market uncertainty remains

LOW YIELD
substantial effort without a defensible market-level decision
```

Do not infer hidden model/token costs.

---

## 19. Non-goals

Do **not**:

- build the proposed product;
- implement software;
- change production architecture;
- build a tariff ingestion pipeline;
- build a scraper;
- automate the benchmark;
- broaden into customs classification;
- infer HS codes from descriptions and treat them as authoritative;
- perform outreach;
- run ads;
- perform keyword demand research;
- interview importers;
- contact brokers or associations;
- join affiliate or partner programs;
- create a company or payment mechanism;
- test willingness to pay;
- benchmark generic consulting services that expose no testable output;
- use feature counts as a substitute for economic adequacy;
- manufacture edge cases solely to make competitors fail;
- rescue the candidate by broadening into adjacent trade-compliance problems;
- add another RADAR validation step after a valid P2/P3 result.

---

## 20. Governing principles

> **Benchmark outputs, not marketing claims.**

> **Core truth and decision completeness are different things.**

> **A correct calculator is not necessarily a complete decision resolution.**

> **A complete resolution does not need every conceivable feature.**

> **Do not replace customs classification with unsupported product-name inference.**

> **The benchmark should maximize information gain, not simulate a population survey.**

> **Competition should be evaluated by actor × decision × inputs × resolution × output × timing.**

> **A fresh gap is valuable only while adequate resolution supply remains absent.**

> **Do not validate the scalability of an unvalidated product.**

> **Do not add another research step after the decision is already good enough to PARK or FORGE.**

> **Disposable before durable.**

---

## 21. Interpretation

Specs 021–023 progressively improved RADAR's evaluation, candidate generation, and timing awareness.

Spec 024 asks whether those improvements can now produce a terminal decision from live market evidence.

```text
RADAR
  ↓
fresh change detected
  ↓
specific decision gap reconstructed
  ↓
recoverability established
  ↓
possible pre-consolidation window
  ↓
LIVE FUNCTIONAL BENCHMARK
  ↓
        ┌───────────────┐
        │               │
       P3              P2
        │               │
      PARK            FORGE
```

A P3 result is not failure.

A P2 result is not permission to build a durable product.

The objective is to make the next decision with the smallest sufficient amount of evidence.
