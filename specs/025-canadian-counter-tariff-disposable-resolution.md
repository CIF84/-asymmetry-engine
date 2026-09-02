# Spec 025 — Canadian Counter-Tariff Disposable Resolution

**Status:** FORGE experiment  
**Phase:** First deliberate RADAR → FORGE handoff  
**Depends on:** Specs 001–024 and learning checkpoints through 024

## 1. Objective

Actually produce the smallest trustworthy, decision-ready resolution for the Canadian September 8 counter-tariff asymmetry demonstrated in Spec 024.

The question is:

> **Can FORGE transform the demonstrated asymmetry into a trustworthy, decision-ready Canadian counter-tariff exposure brief from already-classified inputs without building durable software?**

This is not another RADAR research spec.

Do not study whether the artifact could be produced.

**Produce it.**

---

## 2. Why this experiment exists

Spec 024 demonstrated a material live functional gap.

Current public tools provide components of the answer, but no tested resolver consistently joined:

```text
KNOWN CANADIAN HS TARIFF ITEM
+
ORIGIN
+
CUSTOMS VALUE
+
ENTRY / IN-TRANSIT DATE
+
CURRENT COUNTER-TARIFF SCHEDULE
+
EXCEPTION / REMISSION FACTS
        ↓
CASE-SPECIFIC EXPOSURE
+
RATE
+
INCREMENTAL COST
+
MATERIAL CAVEATS
+
AUTHORITATIVE EVIDENCE
+
NEXT ACTION
```

RADAR has ended for this candidate.

FORGE now tests the resolution itself.

---

## 3. Experimental principle

The first FORGE artifact must be **disposable before durable**.

Optimize for:

- correctness;
- speed;
- clarity;
- provenance;
- explicit uncertainty;
- decision usefulness;
- cheapness;
- reversibility.

Do not optimize for:

- scale;
- automation;
- maintainability;
- UI polish;
- generalized architecture;
- reuse across jurisdictions;
- monetization;
- customer acquisition.

Manual work is allowed and expected.

---

## 4. Actor and decision boundary

### Actor

Canadian SME importer or buyer evaluating already-classified goods.

### Decision

For each order line:

- proceed with identified exposure;
- reprice;
- renegotiate;
- substitute;
- defer;
- confirm origin;
- investigate remission/relief;
- escalate classification or another unresolved fact to a broker/customs specialist.

### Explicit boundary

The artifact does **not** provide customs classification.

The user supplies the Canadian HS tariff item.

If the supplied classification is uncertain, the resolution may flag that uncertainty but must not silently replace or infer the code from the commercial description.

---

## 5. Input manifest

Use a fixed experimental manifest of **no more than 20 lines**.

Do not require a real importer for Spec 025.

Construct the manifest from the authoritative, already-validated cases produced during Spec 024, selecting enough variation to exercise the resolution meaningfully.

Prefer approximately 10–15 lines unless additional lines materially improve the artifact test.

Each line should contain:

```text
line_id
product_description
supplied_hs_tariff_item
origin
customs_value_cad
entry_or_in_transit_date
already_in_transit_fact if relevant
intended_reexport_fact if relevant
no_reasonably_substitutable_supply_fact if relevant
```

Do not fabricate ambiguity merely to make the report sophisticated.

Use realistic fixed facts already defensible from Spec 024.

---

## 6. Authoritative evidence hierarchy

Use current authoritative Canadian sources as the resolution evidence.

Prefer:

1. Department of Finance current counter-tariff schedule and notices;
2. CBSA / Customs Tariff / CARM official material where necessary;
3. official remission, relief, drawback, or exception guidance;
4. other Canadian government material strictly necessary to resolve a line.

Commercial resolver outputs may be used as calibration only.

They must not determine the final answer when authoritative evidence is available.

Record the date each authoritative source was checked.

---

## 7. Required transformation

For each manifest line determine:

### Core truth

- exposure status;
- applicable incremental counter-tariff rate;
- effective-date treatment;
- incremental counter-tariff cost.

### Material uncertainty

- whether supplied classification must be independently confirmed;
- whether origin is sufficiently established;
- whether date/in-transit treatment requires additional evidence;
- whether remission/relief review is materially relevant;
- any other fact that prevents a clean YES or NO.

### Provenance

- authoritative source;
- relevant tariff item / rule;
- source-check date;
- short explanation of why the result follows.

### Action

Exactly one primary next action per line.

Examples:

```text
PROCEED / PRICE WITH IDENTIFIED EXPOSURE
NO SEPTEMBER 8 COUNTER-TARIFF IDENTIFIED
CONFIRM ORIGIN BEFORE COMMITTING
CONFIRM CLASSIFICATION WITH BROKER / CUSTOMS SPECIALIST
VERIFY IN-TRANSIT EVIDENCE
REVIEW EXCEPTIONAL REMISSION POSSIBILITY
REVIEW RE-EXPORT RELIEF / DRAWBACK ROUTE
DEFER DECISION — MATERIAL FACT UNRESOLVED
```

Do not give generic advice when a more specific bounded action follows from the evidence.

---

## 8. Resolution statuses

Use only these primary statuses:

```text
YES
NO
REVIEW REQUIRED
```

### YES

The supplied facts and authoritative evidence support application of the bounded September 8 counter-tariff.

### NO

The supplied facts and authoritative evidence support no exposure to the bounded September 8 measure.

This does not mean no other customs duties, taxes, or trade measures apply.

### REVIEW REQUIRED

A material unresolved fact prevents a reliable YES/NO decision or an official relief/remission route is sufficiently relevant that the importer should investigate before acting.

Do not use REVIEW REQUIRED merely because all legal decisions contain uncertainty.

---

## 9. Required artifact

Create one human-readable disposable artifact in the repository under:

`experiments/025/`

The preferred primary format is Markdown unless another extremely simple format materially improves decision readability.

Suggested filename:

`experiments/025/canadian-counter-tariff-exposure-brief.md`

The artifact must stand on its own for a reader who has not read Specs 023–025.

It must contain at minimum:

### A. Decision summary

- manifest-level total identified incremental exposure;
- count of YES / NO / REVIEW REQUIRED lines;
- highest-value exposures;
- lines requiring action before commitment.

### B. Line-level decision table

For every line:

- description;
- supplied HS item;
- origin;
- customs value;
- relevant date;
- status;
- rate;
- incremental cost;
- primary next action.

### C. Why / evidence

For every line, or through a clearly mapped evidence section:

- short reasoning;
- authoritative evidence link/reference;
- source-check date;
- material caveat.

### D. Boundaries

State clearly that the brief:

- does not provide customs classification;
- does not guarantee legal origin determination;
- does not guarantee remission/relief eligibility;
- covers the bounded September 8 counter-tariff decision, not all duties/taxes/trade measures;
- reflects sources checked on the stated date and may become stale.

Do not bury these boundaries in generic boilerplate.

---

## 10. Decision-first design

The artifact is not a research memo.

The first screen/page/section should answer:

```text
WHAT IS MY EXPOSURE?
WHAT NEEDS ATTENTION?
WHAT SHOULD I DO NEXT?
```

Detailed evidence comes after the decision summary.

Avoid long regulatory exposition before the answer.

Use concise tables and short explanations.

---

## 11. Provenance is functional

For this experiment, provenance is part of the resolution itself.

Each material conclusion must be inspectable.

The artifact should make visible:

```text
ANSWER
+
WHY
+
SOURCE
+
SOURCE CHECK DATE
+
UNCERTAINTY
```

Do not cite commercial tools as authority for the final decision.

Do not hide source freshness.

---

## 12. Internal validation

After producing the artifact, independently validate every line against the authoritative baseline used in Spec 024 and current live authoritative sources.

Check:

### V1 — Core truth correctness

- exposure;
- rate;
- date treatment;
- arithmetic.

### V2 — Evidence fidelity

- source actually supports the conclusion;
- no stale or superseded schedule used;
- source date/check date recorded;
- removed items remain removed.

### V3 — Boundary discipline

- no unsupported customs classification;
- no unsupported legal-origin conclusion;
- no guaranteed remission eligibility;
- no claim that the report covers all import costs.

### V4 — Decision clarity

For each line, a reader can determine:

- current status;
- expected incremental cost;
- material uncertainty;
- exactly one primary next action.

Log validation failures and correct the artifact before final completion.

Do not silently leave known errors in the experimental artifact merely because it is disposable.

---

## 13. Resolution-quality verdict

At completion classify the experiment:

### A — DECISION-READY RESOLUTION PRODUCED

The artifact:

- is correct on all tested core-truth fields after validation;
- preserves the known-HS boundary;
- represents material uncertainty rather than hiding it;
- exposes authoritative provenance and freshness;
- gives clear line-level next actions;
- can reasonably be handed to a decision-maker for the bounded purpose.

**Next uncertainty:** interaction with a real decision-maker.

### B — RESOLUTION PRODUCED, ONE MATERIAL WEAKNESS

The artifact substantially works, but exactly one bounded weakness prevents calling it decision-ready.

Examples could include a specific unresolved official rule, confusing representation of a material uncertainty, or one evidence field that cannot yet be made inspectable.

Recommend exactly one repair.

### C — RESOLUTION NOT RELIABLY PRODUCIBLE

The transformation itself fails materially under the bounded conditions.

Examples:

- authoritative evidence cannot support reliable line-level conclusions;
- material exceptions dominate the supposedly simple job;
- core truth cannot be reproduced consistently;
- the known-HS boundary is insufficient to resolve the decision.

Do not retreat automatically into broad RADAR discovery. Identify the failure precisely.

### D — EXPERIMENT INVALID

The artifact was not actually produced/tested as specified, current policy changed so materially that the experiment no longer tests the Spec 024 gap, or another execution failure prevents interpretation.

---

## 14. Important distinction: 025 does not test behavior

Do not claim that Spec 025 proves:

- importer demand;
- trust;
- behavior change;
- economic value created;
- willingness to pay;
- value capture;
- repeatability.

025 tests only whether FORGE can produce a trustworthy decision-ready resolution.

If verdict A, the next experiment should expose the artifact to reality and observe behavior.

---

## 15. No real-importer acquisition requirement

Do not require a real importer, customer, partner, broker, or external participant for Spec 025.

This is deliberate.

A real-importer requirement would combine resolution production with acquisition and behavioral measurement.

Those are separate uncertainties.

Do not perform outreach in this spec.

---

## 16. No durable implementation

Do not build:

- a web app;
- a CLI;
- a database;
- an ingestion pipeline;
- an API;
- a scraper;
- an automated tariff matcher;
- a generic report generator;
- a reusable trade-compliance engine;
- accounts/authentication;
- monitoring infrastructure;
- payment infrastructure.

If a tiny throwaway local calculation is useful to prevent arithmetic mistakes, it may be used during execution, but do not turn it into production code or architecture.

The deliverable is the decision artifact, not software.

---

## 17. Time and spend envelope

### Target active execution time

**90 minutes.**

A bounded overrun is acceptable only to finish validation or correct a material artifact error already discovered.

Record the overrun and reason.

### Paid budget

**€0 preferred; €2 hard maximum.**

No new paid accounts or subscriptions.

---

## 18. Required completion report

Return these sections in order:

1. **Verdict** — A / B / C / D and one-sentence reason.
2. **Artifact created** — path, format, and concise description.
3. **Manifest used** — number of lines and why the selected cases exercise the resolution.
4. **Decision summary** — total identified exposure, YES/NO/REVIEW counts, material actions.
5. **Resolution transformation** — how inputs became outputs without durable software.
6. **Core truth validation** — exposure/rate/date/cost results and any corrections made.
7. **Evidence/provenance validation** — authoritative sources, freshness, stale-data controls.
8. **Boundary validation** — classification/origin/remission/all-cost boundaries.
9. **Decision-readiness review** — whether a bounded reader can understand exposure, uncertainty, and next action.
10. **Artifact weaknesses** — real weaknesses only; do not invent polish requirements.
11. **What FORGE learned about resolution construction**.
12. **What remains unproven**.
13. **Research/execution economics report**.
14. **Architecture implications** — preserve vs too early to institutionalize.
15. **Exactly one recommended next action**, constrained by verdict.

---

## 19. Execution economics report

Report observable inputs only.

### Effort

- elapsed active time;
- authoritative sources inspected;
- manifest lines resolved;
- manual calculations / validation checks;
- artifact files created;
- paid spend;
- visible Codex constraint if encountered.

### Uncertainty reduction

- entering uncertainty: can the resolution actually be produced?
- leaving uncertainty;
- whether artifact construction exposed new hidden complexity;
- whether the next uncertainty moves from resolution construction to real-world interaction.

### Evidence yield

Classify:

```text
HIGH YIELD
artifact construction clearly resolves the production question at modest cost

MEDIUM YIELD
artifact provides useful evidence but one material production uncertainty remains

LOW YIELD
substantial effort without a trustworthy interpretation
```

Do not infer hidden token/model costs.

---

## 20. Non-goals

Do **not**:

- return to opportunity discovery;
- repeat the competitor benchmark;
- perform another demand gate;
- perform keyword research;
- perform market sizing;
- contact importers;
- contact brokers;
- contact associations;
- run ads;
- test pricing;
- test willingness to pay;
- create a business entity;
- create payment infrastructure;
- build durable software;
- broaden into customs classification;
- broaden into general Canadian tariff compliance;
- broaden into US tariffs or other jurisdictions;
- optimize for future scalability;
- create architecture for hypothetical future requirements;
- treat disclaimers as a substitute for correct bounded reasoning.

---

## 21. Governing principles

> **FORGE makes something capable of interacting with reality.**

> **Disposable before durable.**

> **Resolve one decision before building a system.**

> **Correctness before convenience.**

> **Uncertainty should be represented, not hidden.**

> **Provenance and freshness are part of the answer.**

> **Do not expand the problem to rescue the experiment.**

> **Do not combine resolution production, acquisition, behavior change, and monetization into one test.**

> **A manually produced artifact can be a valid experimental resolution.**

---

## 22. Interpretation

Spec 024 ended RADAR for this candidate.

Spec 025 is the first deliberate FORGE experiment.

```text
RADAR
  ↓
material resolution gap demonstrated
  ↓
────────────────────────────
            FORGE
────────────────────────────
  ↓
produce disposable resolution
  ↓
validate core truth
  ↓
validate provenance + uncertainty
  ↓
validate decision clarity
  ↓
        ┌───────────────┐
        │               │
   DECISION-READY      FAILS
        │               │
        ↓               ↓
 expose to reality   diagnose exact
 in next experiment  resolution failure
```

Success in 025 does not mean the opportunity is commercially validated.

It means the Engine has successfully crossed from discovering an asymmetry to producing a trustworthy experimental resolution.
