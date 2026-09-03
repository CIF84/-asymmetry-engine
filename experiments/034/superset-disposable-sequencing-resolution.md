# Experiment 034 — Superset Disposable Sequencing Resolution

## Experiment status

- **Verdict:** A — DECISION-READY RESOLUTION
- **Recommended decision:** S2 — ship now with an explicit migration/source boundary
- **Execution date:** 2026-09-03
- **External interaction:** none; the actor-facing draft below was not posted or sent
- **Incremental spend:** €0

---

# Part I — Internal evidence and challenge record

## 1. Decision being resolved

For [SIP-225](https://github.com/apache/superset/issues/43331) and its [reference implementation PR #41907](https://github.com/apache/superset/pull/41907), decide among:

- **S1:** ship chart-local `drilldown_hierarchy: string[]` unchanged;
- **S2:** ship now while making hierarchy-source resolution an explicit boundary;
- **S3:** wait for a dataset/semantic-layer hierarchy contract.

The decision is sequencing, not whether hierarchical drill-down should exist and not what the future hierarchy model should be.

## 2. Evidence baseline and freshness check

Experiment 033 is the primary evidence baseline. A bounded freshness check on 2026-09-03 found no contradiction:

- **KNOWN CURRENT:** Superset has merged `Explorable`, semantic-layer/view models, dimension and metric objects, compatibility APIs, and optional metadata. These provide a substrate but no hierarchy contract. Relevant sources: [PR #36245](https://github.com/apache/superset/pull/36245), [PR #37815](https://github.com/apache/superset/pull/37815), and [PR #43269](https://github.com/apache/superset/pull/43269).
- **CONCRETE IN FLIGHT:** PR #41907 remains open and unmerged. It has 33 commits and 45 changed files. The current implementation stores an inline ordered list, normalizes it inside `useDrillDownState`, and then uses the resulting `hierarchy: string[]` for interaction and query mutation.
- **DIRECTIONAL:** SIP-225 discussion proposes dataset-owned named hierarchies, chart references, and semantic-layer hydration. [The proposal author's comment](https://github.com/apache/superset/issues/43331#issuecomment-5348927896) says the interaction/breadcrumb layer should remain independent of the list's source.
- **DIRECTIONAL:** SIP-182 discussion sketches dimension parents, hierarchy-aware metrics, anchors, and hierarchy context, but labels the structures as pseudo-schema and supplies no implementation horizon. See the [roadmap statement](https://github.com/apache/superset/issues/35003#issuecomment-4260561398) and [hierarchy sketch](https://github.com/apache/superset/issues/35003#issuecomment-4261624080).
- **ABSENT:** no stable dataset/semantic hierarchy interface, hierarchy-specific implementation, milestone, release horizon, or committed landing sequence was established.
- **UNKNOWN / FUTURE CONTRACT:** hierarchy identity, sync, precedence, validation, rename behavior, deletion behavior, provider representation, and migration mechanics.

SIP-225 remains open with seven comments and no milestone. No fresh evidence makes waiting more valuable.

## 3. S1 / S2 / S3 decision table

| Decision factor | S1 — ship unchanged | S2 — ship with boundary | S3 — wait |
|---|---|---|---|
| Near-term simplicity | Strongest: no extra conceptual work | Slightly weaker: isolate and state one seam | Weakest: delivery blocked indefinitely |
| Current representation | Directly uses inline `string[]` | Preserves inline `string[]` as today's source | Avoids committing current representation |
| Duplication / rename brittleness | Accepted per chart | Not removed now, but isolated from interaction | Avoided only if a future central owner actually lands |
| Future source migration | Interaction and source may remain co-located | Future source can replace/extend resolution before interaction | One representation, if dependency arrives first |
| Unknown future semantics | Defers all work | Refuses to model them; protects only the source/interaction join | Also defers all work |
| Reversibility | Inline charts remain usable, but migration seam is implicit | Inline charts remain usable and seam is explicit | Reversible by ending the wait, but time is lost |
| Evidence supporting | Current feature works from raw names | Public direction favors central ownership; code already normalizes to an ordered list before using it | Future hierarchy intent exists |
| Evidence weakening | Known duplication/brittleness; stated future owner | Seam cost could exceed benefit; ordered list cannot cover all future semantics | No concrete contract or timing; waiting does not reduce known uncertainty |
| Overall | Viable fallback | **Dominant if boundary stays minimal** | Not evidence-supported |

## 4. Why S2 dominates without winning by definition

### Why not simply ship S1 and migrate later?

That is the strongest economic counterargument. If migration is remote or the current representation is cheap to replace, any seam added now may be waste.

S2 survives because the required boundary is not a future hierarchy abstraction. PR #41907 already has a concentrated normalization step that converts chart `form_data` into `hierarchy: string[]` before drill behavior consumes it. The incremental requirement is to treat that join explicitly as source resolution and prevent downstream interaction logic from independently reading source-specific fields. It does not require a database model, service, provider interface, or reference schema.

If review shows that enforcing this boundary requires broad refactoring rather than a small extraction/contract clarification, S1 becomes preferable. The recommendation is conditional on the seam remaining small.

### Why not wait under S3 to avoid two representations?

Waiting avoids two representations only if a replacement contract arrives within a decision-relevant horizon. Public evidence establishes neither a hierarchy implementation nor timing. Waiting therefore delays the current feature while preserving, rather than resolving, the same design unknowns. S3 becomes preferable only if a concrete hierarchy contract and credible near-term landing sequence appear before SIP-225 ships.

## 5. Minimal migration/source boundary

The smallest justified boundary is:

```text
chart configuration
  inline ordered levels today
  future reference/source unknown
            ↓
resolve the configured source
            ↓
ordered sequence of drillable dimensions
            ↓
existing level-based drill interaction
```

It answers only four questions:

1. **Interaction input:** an ordered sequence of dimensions that the current chart/query path can use.
2. **Source representation:** `drilldown_hierarchy` and any future reference identify or contain the source; they are not drill-state semantics.
3. **Replaceable part:** reading, validating, and resolving the configured source into the ordered sequence.
4. **Stable part:** click progression, accumulated filters, query refresh, cross-filter emission, breadcrumb state, and reset behavior for ordered-level drilling.

This boundary does **not** assert that every future hierarchy can resolve to raw column names or even to a fixed ordered list. Parent-child traversal or provider-native query semantics may require a different interaction contract. S2 protects the current level-based feature from source-ownership change; it does not pre-solve new hierarchy capabilities.

## 6. Required invariants

Only these invariants survive challenge:

1. The existing ordered-level interaction receives one resolved ordered sequence before drilling begins.
2. Interaction and breadcrumb state do not read or mutate hierarchy ownership/source representation.
3. Existing valid inline lists remain interpretable during any future migration period.
4. A future source failure must not cause an existing inline chart to be silently reinterpreted as a different hierarchy.
5. A change in the resolved sequence invalidates incompatible in-memory drill state, matching the current configuration-reset behavior.
6. No future identifier shape is hard-coded now.

Rejected as too broad:

- “All future hierarchies resolve to ordered raw column names.” Parent-child and provider-native semantics contradict that assumption.
- “A failed future reference must fall back to inline data.” Precedence and fallback are future-contract questions.
- “The chart must resolve every source client-side.” Resolution location is not established.
- “Source migration never changes interaction code.” This is defensible only for compatible ordered-level sources, not all future hierarchy types.

## 7. Explicit non-inventions

The resolution deliberately leaves these **UNKNOWN / FUTURE CONTRACT**:

- hierarchy object schema and identifier strategy;
- database persistence or migrations;
- semantic-provider APIs and sync protocol;
- source precedence, conflict, fallback, and deletion rules;
- rename propagation and validation UX;
- cache, permissions, and REST endpoints;
- provider support and release timing;
- migration mechanics from inline values to references;
- interaction contracts for parent-child or provider-native traversal.

## 8. Failure-mode analysis

| Failure mode | Evidence | Does S2 survive? | Minimal justified safeguard | Premature architecture avoided |
|---|---|---|---|---|
| Future semantics differ from a fixed ordered list | **DIRECTIONAL:** SIP-182 sketches parent-child traversal | Yes, after narrowing scope to current level-based drilling | State that the resolved-list boundary covers only compatible ordered-level sources | No universal hierarchy abstraction |
| Provider-native hierarchy cannot use raw Superset column names | **Plausible / UNKNOWN** | Yes | Keep raw names downstream only as today's resolved query tokens; do not define future IDs | No provider contract or mapping API |
| Inline config becomes hard to migrate | **INFERRED**, not demonstrated | Yes | Keep inline lists readable and isolate their interpretation | No migration script or dual-write design |
| Multiple sources create ambiguous precedence | **UNKNOWN / FUTURE CONTRACT** | Yes | Do not introduce multiple sources now; mark precedence unresolved | No precedence rules |
| Seam adds complexity without reducing risk | Strongest challenge; cost is not measured | Conditionally | Keep the seam to a single conceptual resolution point; choose S1 if review shows broad cost | No service/class hierarchy mandated |
| Interaction depends on source identity/metadata | **CONTRADICTED for current ordered-level implementation**; it consumes normalized names and filters | Yes for current capability | Preserve interaction's dependency on resolved levels only | No claim about future capabilities |
| Waiting avoids imminent rework | **Not supported:** no implementation or timing evidence | Yes | Reverse only on concrete near-term dependency evidence | No inferred roadmap date |

## 9. Strongest case against S2

S1 may be economically superior. The current code already has a local `useMemo` that normalizes `form_data` into a hierarchy list, so naming or extracting that seam could be ceremony. The future contract might never arrive, or might be so different that today's seam is discarded. Since source migration cost is unmeasured, S2's benefit is inferred rather than demonstrated.

S3 also has a coherent purity argument: one central representation avoids a later compatibility period. But it lacks expected-value support because neither the representation nor its arrival time is known.

The response is deliberately modest: S2 requires no future-facing type or persistence decision. Its value is simply to keep the current source read concentrated and the interaction contract explicit. If that cannot be achieved as a small reviewable change or SIP clarification, ship S1 rather than building speculative architecture.

## 10. Epistemic challenge record

### Weakest claim

That an explicit seam materially lowers future migration cost. Current code concentration makes this plausible, but no implementation estimate or migration test proves it.

### Absence inference

“No public hierarchy contract found” does not prove that none is being designed privately or imminently. It proves only that no public dependency can justify waiting now. Unknown private work cannot govern a public sequencing decision.

### Is the seam necessary now?

Not categorically. It is justified only if it remains the already-visible normalization boundary made explicit, rather than a new architecture layer.

### Is speculative architecture being smuggled in?

The first draft risked implying that every future hierarchy resolves to `string[]`. That claim was removed. The final resolution scopes the invariant to the current ordered-level interaction and marks parent-child/provider-native behavior as future contracts.

### Could S1 be cheaper?

Yes. The recommendation now contains a stop rule: if the boundary entails broad refactoring or new persistence/API concepts, choose S1.

### Could the boundary freeze the wrong abstraction?

Yes, if it names a universal hierarchy object or future identifier type. The revised boundary exposes only today's resolved interaction input and leaves source/identity types undefined.

### Single fact most likely to overturn S2

A concrete, reviewed dataset/semantic-layer hierarchy contract with an active implementation and credible near-term landing sequence that is incompatible with PR #41907's saved representation or query interaction.

### Challenge result

S2 survives, but only as a narrow sequencing rule for the current ordered-level feature. The challenge materially narrowed the claim and added a cost-based fallback to S1.

## 11. Decision-ready test

1. **What should happen now?** Ship the chart-local feature with one explicit source-resolution boundary.
2. **Why over alternatives?** It preserves current delivery, costs less than waiting, and protects the already-visible ownership seam without inventing a future model.
3. **What must change before shipping?** Make the single form-data-to-resolved-levels join explicit and ensure ordered-level interaction consumes only the resolved sequence.
4. **What should not be designed?** All future hierarchy identity, persistence, sync, provider, precedence, and migration contracts.
5. **What reverses the decision?** Concrete near-term dependency evidence, demonstrated broad seam cost, or proof that current interaction requires source-specific semantics.

**Result: PASS.**

## 12. Intended observable decision effect

If separately authorized and delivered later, the resolution is intended to cause one or more observable changes:

- SIP text replaces vague migration language with an explicit source-resolution/interaction boundary;
- PR review explicitly accepts S2 or rejects it with concrete dependency/cost evidence;
- hierarchy parsing/normalization remains concentrated before interaction behavior;
- the ship-now versus wait question becomes closed.

No interaction occurred in this experiment.

---

# Part II — Actor-facing disposable resolution draft

> **DELIMITED DRAFT — NOT POSTED OR SENT**

## Decision

Ship the chart-local ordered hierarchy now, but make one boundary explicit before shipping: drill interaction should consume a resolved ordered sequence of drillable dimensions, not own the representation from which that sequence came.

## Evidence

- PR #41907 already stores `drilldown_hierarchy: string[]`, normalizes it with the chart's primary dimension, and then uses the resulting ordered list for click progression, filters, queries, and breadcrumbs.
- Project discussion expects hierarchy ownership eventually to move toward reusable dataset-level definitions and possible semantic-layer hydration.
- Superset's semantic-layer substrate is real, but there is no current hierarchy contract, hierarchy implementation, milestone, or reliable landing horizon.

That combination argues against waiting and against designing the future hierarchy model now.

## S1 / S2 / S3 trade-off

| Option | Benefit | Cost / risk | Resolution |
|---|---|---|---|
| **S1 — ship unchanged** | Lowest immediate effort | Keeps source parsing and interaction implicitly coupled; duplicates raw names across charts | Acceptable fallback if the seam is not small |
| **S2 — ship with boundary** | Ships now and keeps source ownership replaceable | Small additional review/refactor burden; does not eliminate current rename brittleness | **Recommended** |
| **S3 — wait** | Might avoid a compatibility period | No concrete dependency or timing; delays value without reducing known uncertainty | Not supported by current evidence |

## Recommendation

Choose **S2** if it can remain a narrow boundary. Preserve `drilldown_hierarchy` as today's inline source. Resolve it once into the ordered levels the current interaction needs. Keep click state, filters, queries, cross-filtering, and breadcrumbs dependent only on that resolved sequence.

If making that separation requires a new model, endpoint, provider interface, persistence design, or broad refactor, do not build it speculatively—ship S1 instead.

## Minimal boundary

```text
inline chart hierarchy today / future source unknown
                         ↓
             resolve configured source
                         ↓
        ordered drillable dimensions
                         ↓
       existing level-based interaction
```

The boundary requires only these invariants:

- existing inline lists remain readable;
- interaction state stays separate from hierarchy ownership;
- changing the resolved levels clears incompatible drill state;
- a future source cannot silently reinterpret an existing inline chart;
- no future identifier shape is chosen now.

## Why this is enough now

The current PR already concentrates hierarchy normalization and exposes an ordered `hierarchy` list to the interaction. Making that join explicit protects the most likely ownership change while leaving the feature shippable. It does not need to solve future storage or semantic-provider integration.

## What remains deliberately unresolved

Hierarchy schema, IDs, persistence, sync, precedence, rename/deletion behavior, provider APIs, permissions, migration mechanics, and release timing remain future contracts.

This boundary also does not claim that parent-child or provider-native hierarchies reduce to a fixed list. Those may require different query and interaction semantics later; they should not constrain this ordered-level feature without concrete evidence.

## What evidence would reverse the recommendation

Reverse from S2 if either:

1. a reviewed dataset/semantic-layer hierarchy contract enters active implementation with a credible near-term landing sequence and is incompatible with the current saved/query shape; or
2. PR review demonstrates that the proposed boundary is not a small concentration of existing normalization but a broad speculative refactor.

Until then, waiting has no demonstrated architectural payoff, and shipping without acknowledging the source/interaction join leaves avoidable migration coupling.

> **END DELIMITED DRAFT**

---

## 13. Experiment conclusion

The resolution is concise enough for a future controlled actor interaction, discriminates S1/S2/S3, answers what must change and what must remain unknown, and survives adversarial review after narrowing its compatibility claim. It is disposable: if concrete hierarchy evidence arrives, the recommendation can be replaced without preserving this artifact as architecture.

## 14. Research time and controls

- Active research and synthesis: approximately 27 minutes.
- Target: 30 minutes; hard ceiling: 45 minutes; ceiling not exceeded.
- Incremental spend: €0.
- Public research: read-only and limited to the established Superset candidate.
- Actor contact or public interaction: none.
- GitHub comments, reactions, issue edits, or PR actions: none.
- Superset code or implementation work: none.
- New opportunity discovery: none.
- Spec 030 response state: not inspected or modified.

## 15. Exactly one recommended next action

Under a separate specification and explicit authorization, run one controlled actor-facing resolution test using only the delimited draft above and define exposure/response evidence before delivery.
