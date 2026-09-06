# Experiment 035 — Superset Actor-Facing Resolution Test

## Initialization status

- **Experiment phase:** publication initialization
- **Execution state:** PUBLISHED; delivery verified; 72-hour observation window open
- **Provisional verdict:** D — EFFECT UNKNOWN at initialization; no behavioral verdict is inferred from delivery alone
- **Baseline captured:** 2026-09-03T01:49:17Z (2026-09-03T03:49:17+0200 CEST)
- **Published:** 2026-09-03T01:51:13Z (2026-09-03T03:51:13+0200 CEST)
- **Observation deadline:** 2026-09-06T01:51:13Z (2026-09-06T03:51:13+0200 CEST)
- **Target surface:** `apache/superset#43331`
- **Published public identity:** `CIF84`

## Natural pre-intervention baseline — immutable

This section records the natural state before the authorized comment. It must not be overwritten during later observation.

### Issue state

- Repository: `apache/superset`
- Issue: `#43331 — [SIP-225] Proposal for author-configured hierarchical drill-down on dashboard charts`
- URL: https://github.com/apache/superset/issues/43331
- State: **OPEN**
- Locked: **false**
- Active lock reason: none
- Labels: `sip`, `dashboard:drill-down`
- Milestone: none
- Created: 2026-08-19T10:02:53Z
- Last updated: 2026-09-01T17:39:10Z
- Top-level issue comment count: **7**

### Proposal state relevant to S1 / S2 / S3

The issue proposes an author-configured guided drill path stored in chart `form_data` as `drilldown_hierarchy: string[]`, an ordered list of plain column names. It says the list is additive, has no database migration, and may later be sourced from a dataset/semantic-layer hierarchy. The issue explicitly leaves open whether to ship the chart-local configuration now and migrate later or wait for a semantic-layer source.

The proposal contains no current dataset/semantic hierarchy contract, implementation, milestone, or landing horizon. The explicit sequencing question remains in the issue body; no later issue comment closes it.

### Existing issue comments relevant to the decision

1. **rusackas (MEMBER), 2026-08-19T17:41:46Z** — raises per-chart duplication, data-model breakage, dataset-level reuse, and external semantic-layer ownership; says feature-flag proliferation should be avoided and the feature could ship after SIP consensus. Permalink: https://github.com/apache/superset/issues/43331#issuecomment-5345841015
2. **tomerkl65 (proposal author), 2026-08-19T22:48:53Z** — confirms current chart-local raw-name storage and its tradeoffs; proposes future dataset-owned named hierarchies, chart references, and semantic-layer hydration; recommends shipping chart-local now and treating central ownership as a later SIP iteration; says the interaction/breadcrumb layer is intended to be source-agnostic. Permalink: https://github.com/apache/superset/issues/43331#issuecomment-5348927896
3. **shohamyamin, 2026-08-27T07:25:22Z** — generic support; no sequencing evidence. Permalink: https://github.com/apache/superset/issues/43331#issuecomment-5435731743
4. **ofekvs18, 2026-08-27T16:09:49Z** — supports starting chart-local while leaving room for reuse; supplies no dependency or timing evidence. Permalink: https://github.com/apache/superset/issues/43331#issuecomment-5441895899
5. **mkvyat, 2026-08-27T16:18:00Z** — generic support; no sequencing evidence. Permalink: https://github.com/apache/superset/issues/43331#issuecomment-5441991868
6. **W3r7y, 2026-08-27T16:54:40Z** — detailed value support for guided drilling; no hierarchy-dependency or timing evidence. Permalink: https://github.com/apache/superset/issues/43331#issuecomment-5442416728
7. **dpreuss, 2026-09-01T17:39:10Z** — reports an existing custom Pie implementation and willingness to replace it; no sequencing closure. Permalink: https://github.com/apache/superset/issues/43331#issuecomment-5497937421

No pre-intervention comment was authored by `CIF84`.

### Reference PR state needed to establish a live decision

- PR: `apache/superset#41907 — feat(explore): drill-down hierarchy for ECharts charts`
- URL: https://github.com/apache/superset/pull/41907
- State: **OPEN**, not draft, not merged
- Mergeable: true; mergeable state reported as `blocked`
- Base/head: `master` ← `tomerkl65:feat/echarts-drilldown-hierarchy`
- Created: 2026-07-09T13:23:47Z
- Last updated: 2026-08-28T22:53:45Z
- 33 commits; 45 changed files
- Human/member review remains discussion/review rather than a merged or closed disposition. The issue was opened because a maintainer placed the PR on hold pending SIP consensus. Later implementation review states the original functional blockers were addressed; no reviewed dataset/semantic hierarchy dependency or wait decision was found.

### Baseline sequencing disposition

- **S1:** available as the current chart-local implementation.
- **S2:** supported by Spec 034's bounded resolution but not explicitly adopted on the issue.
- **S3:** raised as an open alternative, with no concrete dependency or timing.
- **Decision status:** live and unresolved.

## Authorization record

The user explicitly authorized exactly one public top-level GitHub comment on `apache/superset#43331` using only the bounded actor-facing resolution permitted by Spec 035.

Authorization explicitly excludes follow-ups, comments on PR #41907 or other issues, attention-seeking reactions, tagging additional people, private messages, code/PR changes, and broader outreach. The user also instructed that no final 72-hour response check be performed during initialization.

## Material-evidence freshness check

Performed immediately before initialization using public read-only GitHub state:

- SIP-225 remains open, unlocked, without a milestone, and its explicit sequencing question remains in the body.
- Seven existing comments contain no decision closure or material contrary dependency.
- PR #41907 remains open and unmerged.
- Bounded repository searches for `drilldown_hierarchy` find the open PR and SIP issue; searches for a semantic hierarchy issue/PR reveal no replacement contract or implementation.
- No evidence invalidates Spec 034's narrow S2 recommendation.

## Pre-post control check

| # | Control | Result | Evidence |
|---|---|---|---|
| 1 | Correct repository and issue | PASS | `apache/superset#43331`, title and URL verified |
| 2 | Issue open and decision live | PASS | Open, unlocked, no milestone; explicit ship-now/wait question remains |
| 3 | No material new invalidating evidence | PASS | Issue/PR and bounded dependency searches checked |
| 4 | Platform permits normal participation | PASS | Issue unlocked; authenticated GitHub identity `CIF84` available |
| 5 | Final comment complies with Spec 035 | PASS | 291 words; all seven required components; no prohibited content |
| 6 | Explicit user authorization | PASS | Present in the execution prompt |
| 7 | No private or sensitive information | PASS | Public project facts only |
| 8 | No completed implementation claim | PASS | Conceptual sequencing recommendation only; no code posted |
| 9 | One-comment limit unused | PASS | No existing `CIF84` issue comment; no Spec 035 post yet |

**Overall pre-post control result: PASS.**

## Exact final pre-post draft

Word count: **291**.

> I think the current public evidence favors shipping rather than waiting, with one narrow boundary if it stays cheap.
>
> The reason is mostly sequencing: I couldn't find a concrete dataset/semantic-layer hierarchy contract, implementation, milestone, or reliable landing horizon that the chart-local version needs to wait for. At the same time, the discussion already points toward reusable dataset-owned hierarchies and possible semantic-layer hydration, so treating the inline `drilldown_hierarchy: string[]` as the permanent interaction contract seems unnecessarily binding.
>
> A minimal S2 could be:
>
> `configured hierarchy source → resolve once → ordered drillable dimensions → existing drill interaction`
>
> For the current version, the configured source remains the chart-local list. The click progression, query/filter updates, cross-filter emission, and breadcrumb behavior would consume only the resolved ordered sequence. A later compatible dataset or semantic-layer source could plug into the resolution step without requiring the interaction to understand where the hierarchy came from.
>
> This is intentionally not a proposal for the future hierarchy schema. It does not choose identifiers, persistence, sync, precedence, rename behavior, provider APIs, or migration mechanics. It also does not assume every future hierarchy reduces to `string[]`; parent-child or provider-native hierarchy semantics may need a different interaction contract.
>
> My recommendation would therefore be: ship now with this source/interaction boundary if making it explicit is a small concentration of the normalization already present. If it requires broad refactoring, a new persistence/API/provider model, or other speculative architecture, ship the current chart-local representation unchanged and revisit migration when a real contract exists.
>
> The strongest reason to wait would be concrete project knowledge that a near-term hierarchy interface is already being implemented and is incompatible with the current saved or query shape. Is there such a dependency or implementation constraint, or another reason this sequencing would be wrong?

## Execution record

- External comments posted: **1**
- Follow-ups posted: 0
- Publication state: **published successfully; visible delivery verified**
- Comment ID: `5519099440`
- Comment node ID: `IC_kwDOAlosUs8AAAABSPbGMA`
- Comment permalink: https://github.com/apache/superset/issues/43331#issuecomment-5519099440
- Publication timestamp: **2026-09-03T01:51:13Z** (2026-09-03T03:51:13+0200 CEST)
- Published identity: `CIF84` (`author_association: NONE`)
- Delivery verification: **yes** — a single permitted initialization GET returned the same comment ID, permalink, author, creation/update timestamp, and exact body
- Visible publication state: comment retrievable on the intended public issue
- Platform warning/error: none
- Edit performed: no

## Exact published text — immutable

The following is the exact text returned by GitHub after publication and by the permitted delivery-verification read. It matches the final pre-post draft.

> I think the current public evidence favors shipping rather than waiting, with one narrow boundary if it stays cheap.
>
> The reason is mostly sequencing: I couldn't find a concrete dataset/semantic-layer hierarchy contract, implementation, milestone, or reliable landing horizon that the chart-local version needs to wait for. At the same time, the discussion already points toward reusable dataset-owned hierarchies and possible semantic-layer hydration, so treating the inline `drilldown_hierarchy: string[]` as the permanent interaction contract seems unnecessarily binding.
>
> A minimal S2 could be:
>
> `configured hierarchy source → resolve once → ordered drillable dimensions → existing drill interaction`
>
> For the current version, the configured source remains the chart-local list. The click progression, query/filter updates, cross-filter emission, and breadcrumb behavior would consume only the resolved ordered sequence. A later compatible dataset or semantic-layer source could plug into the resolution step without requiring the interaction to understand where the hierarchy came from.
>
> This is intentionally not a proposal for the future hierarchy schema. It does not choose identifiers, persistence, sync, precedence, rename behavior, provider APIs, or migration mechanics. It also does not assume every future hierarchy reduces to `string[]`; parent-child or provider-native hierarchy semantics may need a different interaction contract.
>
> My recommendation would therefore be: ship now with this source/interaction boundary if making it explicit is a small concentration of the normalization already present. If it requires broad refactoring, a new persistence/API/provider model, or other speculative architecture, ship the current chart-local representation unchanged and revisit migration when a real contract exists.
>
> The strongest reason to wait would be concrete project knowledge that a near-term hierarchy interface is already being implemented and is incompatible with the current saved or query shape. Is there such a dependency or implementation constraint, or another reason this sequencing would be wrong?

## Observation window

- Publication timestamp: 2026-09-03T01:51:13Z
- 72-hour observation deadline: **2026-09-06T01:51:13Z** (2026-09-06T03:51:13+0200 CEST)
- Final observation performed: no
- Manual polling performed after delivery verification: no
- Next authorized observation under this spec: one brief read-only check at or after the deadline

## Initial M1–M6

These values apply immediately after verified delivery. Publication alone does not establish exposure.

| Measure | Initialization state |
|---|---|
| M1 — Exposure | UNKNOWN |
| M2 — Understanding / comprehension | UNKNOWN |
| M3 — Challenge / trust | UNKNOWN |
| M4 — Decision framing change | UNKNOWN |
| M5 — Next-action change | UNKNOWN |
| M6 — Resolution validity update | UNTESTED |

**Provisional experiment verdict:** D — EFFECT UNKNOWN. This is an initialization state, not a final verdict and not a negative behavioral result.

## Operational telemetry

| Metric | Value |
|---|---|
| Preparation + publication active time | approximately 18 minutes |
| Post/publication time | 2026-09-03T01:51:13Z; approximately 1 minute for publication and verification |
| Final observation time | not performed |
| Incremental spend | €0 |
| External comments posted | 1 |
| Follow-ups posted | 0 |
| Control escalations | 0 |
| Human authorization events | 1 explicit authorization in execution prompt |
| Delivery verified | yes |
| Exposure classification | UNKNOWN |
| Substantive responses | not checked after initialization; final window remains open |
| Material decision effect | unknown |
| Evidence yield | LOW at initialization: delivery evidence only |

## Integrity constraints for the open window

- Do not edit the baseline or exact published text.
- Do not post a follow-up under Spec 035.
- Publication proves delivery only, not exposure.
- Do not infer attention, comprehension, trust, or value failure from silence.
- Do not perform the final observation before the 72-hour deadline unless separately instructed to record independently surfaced evidence; never respond under this spec.

---

## Final observation — 2026-09-06

### Final observation status

- **Experiment phase:** final read-only observation
- **Final observation performed:** yes, at `2026-09-06T01:53:37Z`, after the predeclared `2026-09-06T01:51:13Z` deadline
- **Final verdict:** **A — MATERIAL DECISION EFFECT OBSERVED**
- **Interaction outcome class:** **REFINEMENT**
- **Delivery state:** verified; the original `CIF84` comment remains publicly retrievable with the same body and unchanged creation/update timestamp
- **Issue state at final observation:** OPEN; 9 top-level comments; last updated `2026-09-05T13:05:26Z`
- **Reactions on the intervention comment:** 0
- **Follow-ups by `CIF84`:** 0

### Actor response evidence

The fixed primary actor, SIP-225 proposal author **tomerkl65**, posted a substantive top-level response at `2026-09-05T13:05:26Z`, within the 72-hour window:

https://github.com/apache/superset/issues/43331#issuecomment-5552015432

The response is directly attributable to the intervention despite being top-level rather than threaded: it opens by agreeing with the sequencing, repeatedly references the proposed `configured source → resolve once → ordered drillable dimensions → existing drill interaction` seam, addresses the "narrow boundary if it stays cheap" stop rule, and answers the dependency question.

Material actor-supplied evidence:

- the interaction layer already has a single implicit resolution step that normalizes the configured chart-local source against the primary dimension and yields an ordered drillable sequence;
- downstream click progression, query/filter updates, cross-filter emission, and breadcrumb behavior already consume that resolved sequence rather than the raw `drilldown_hierarchy: string[]` directly;
- making the source/resolve seam explicit is therefore described by the proposal author as a small concentration of existing normalization rather than broad refactoring or a new persistence/API/provider model;
- the actor also reports no known concrete dataset/semantic-layer hierarchy contract, saved shape, or in-flight implementation that currently requires waiting, while preserving the caveat that someone closer to that work could still surface an incompatible interface;
- the actor refines the proposed contract: place the explicit boundary on the **source → resolve seam**, but do not permanently bind the output to bare `string[]`; describe it as an ordered sequence of drillable levels with the level kept minimally opaque enough to accommodate future parent-child or provider-native semantics;
- the actor's resulting disposition is to ship now and make the seam explicit because it is cheap in the current implementation.

No additional response, reaction, edit, or follow-up was required to interpret this evidence.

### Final M1–M6

| Measure | Final classification | Evidence |
|---|---|---|
| M1 — Exposure | **HIGH** | The fixed actor explicitly responds to the intervention's sequencing claim, seam, stop rule, and dependency question. |
| M2 — Understanding / comprehension | **OBSERVED** | The response engages the exact S2 sequencing claim and explains the current implementation structure behind the source-resolution boundary. |
| M3 — Challenge / trust | **ACCEPTED / ENDORSED** | The actor says they largely agree, strengthens the ship-now case, and accepts the explicit seam while supplying a bounded refinement. |
| M4 — Decision framing change | **MATERIAL** | The previously implicit architectural seam becomes explicit, and the relevant distinction shifts from raw `string[]` to a source-resolution contract with a more durable ordered-level abstraction. |
| M5 — Next-action change | **MATERIAL** | The actor states a concrete next action: ship now, make the source/resolve seam explicit, and phrase the contract around an ordered sequence of levels rather than bare strings, subject only to confirmation of any hidden incompatible near-term interface. |
| M6 — Resolution validity update | **REFINED** | The S2 sequencing survives contact with the actor and is strengthened by implementation evidence, while its output-contract wording is improved. |

### Material decision effect

**YES — observed.**

The evidence does not establish that the entire SIP has been formally accepted, merged, or closed. It does establish a material effect under Spec 035 because the proposal author directly adopts the intervention's source-resolution seam, supplies implementation facts showing the stop rule is satisfied cheaply, and refines the contract in a way that changes the decision framing and next action.

The causal connection is unusually strong for this experiment: the response explicitly discusses the intervention's exact seam, its cost condition, its future-hierarchy caveat, and its dependency question.

### Interaction outcome class

**REFINEMENT.**

The actor substantively accepts the S2 sequencing direction and adds missing implementation state plus a better abstraction boundary. This improves the resolution without rejecting it.

### No-response classification

Not applicable. Exposure and substantive comprehension are directly evidenced by the fixed actor's response.

### Resolution changes required

Spec 034's core recommendation remains **S2 — ship now with a narrow source-resolution boundary if cheap**. The actor response requires only a bounded refinement:

1. Treat the source/resolve seam as the durable boundary.
2. Phrase its output as an **ordered sequence of drillable levels**, not as permanently bare `string[]`.
3. Record the actor-supplied implementation fact that the seam already exists implicitly, so making it explicit is currently expected to be cheap.
4. Preserve the remaining stop condition: if concrete near-term semantic-layer work surfaces an incompatible saved/query/interface shape, re-evaluate before binding the seam.

This final observation does not modify Spec 034 or implementation artifacts; it records the evidence earned by Spec 035.

### What INTERACT learned

A bounded disposable resolution can survive contact with the actual decision participant and return more useful state than static reconstruction alone. In this case, the intervention produced direct evidence of exposure and comprehension, confirmed the sequencing direction, revealed that the proposed seam already exists implicitly, and improved the abstraction boundary.

The useful effect was not mere agreement. The interaction converted an architectural hypothesis into actor-supplied implementation evidence and a sharper contract.

### Spec 032 policy implication

This n=1 result supports the Spec 032 policy change toward candidates with an observable actor, live decision, legitimate same-surface intervention path, and observable effect. Here that topology produced a highly interpretable result: exposure was directly evidenced, the actor engaged the intended discriminator, and the response supplied decision-relevant state.

Do not generalize this result into a universal claim that same-surface public intervention will work across domains or projects.

### What remains unproven

- formal SIP consensus or maintainer adoption;
- whether the issue body or PR implementation will actually be changed to encode the explicit seam;
- whether PR #41907 will merge or ship;
- whether an incompatible semantic-layer hierarchy contract exists but has not surfaced publicly;
- end-user value from the shipped feature;
- willingness to pay, market size, repeatability, scalable acquisition, or value capture;
- Superset as a commercial opportunity;
- generalization of this interaction mechanism across domains.

### Final operational telemetry

| Metric | Final value |
|---|---|
| Preparation + publication active time | approximately 18 minutes |
| Post/publication time | approximately 1 minute for publication and verification |
| Final observation time | `2026-09-06T01:53:37Z`; brief bounded read-only check; exact active duration not prospectively instrumented and remains UNKNOWN |
| Incremental spend | €0 |
| External comments posted | 1 |
| Follow-ups posted | 0 |
| Control escalations | 0 |
| Human authorization events | 1 |
| Delivery verified | yes |
| Exposure classification | HIGH |
| Substantive responses | 1, from fixed primary actor tomerkl65 |
| Material decision effect | yes |
| Evidence yield | **HIGH** |

### Exactly one recommended next action

Close Experiment 035 and perform one bounded **030 × 035 interaction-topology comparison** before changing any canonical opportunity, experimentability, or operating-model policy.
