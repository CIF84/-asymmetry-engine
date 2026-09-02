# Experiment 033 — Superset Semantic-Hierarchy Dependency Check

## 1. Verdict

**B — DIRECTION CONCRETE, SEQUENCING STILL UNRESOLVED.**

Superset has a current, implemented semantic-layer substrate and public project-native discussion describes plausible hierarchy shapes. However, no current hierarchy contract, hierarchy-specific implementation, stable chart-to-hierarchy reference, or reliable landing horizon was found. This supports shipping now with an explicit migration boundary rather than waiting, while leaving the final boundary design to a disposable sequencing resolution.

## 2. Primary question tested

Does current public Superset evidence establish a concrete dataset/semantic-layer hierarchy interface or landing path sufficient to choose among shipping SIP-225 chart-local unchanged (S1), shipping with an explicit migration boundary (S2), or waiting (S3)?

## 3. Sources inspected

All research was public and read-only. Sources were inspected on 2026-09-02.

- [SIP-225 issue and comments](https://github.com/apache/superset/issues/43331), including the [maintainer dependency questions](https://github.com/apache/superset/issues/43331#issuecomment-5345841015) and the [author's proposed dataset/semantic migration path](https://github.com/apache/superset/issues/43331#issuecomment-5348927896).
- [SIP-225 reference implementation PR #41907](https://github.com/apache/superset/pull/41907).
- [SIP-182 issue and comments](https://github.com/apache/superset/issues/35003), including the [roadmap statement](https://github.com/apache/superset/issues/35003#issuecomment-4260561398), [hierarchy pseudo-interface](https://github.com/apache/superset/issues/35003#issuecomment-4261624080), and [level-hierarchy note](https://github.com/apache/superset/issues/35003#issuecomment-4261638119).
- [Merged Explorable protocol PR #36245](https://github.com/apache/superset/pull/36245).
- [Merged semantic-layer extension PR #37815](https://github.com/apache/superset/pull/37815).
- [Merged optional metric/dimension metadata PR #43269](https://github.com/apache/superset/pull/43269).
- Current Superset `master` at [`e8540b7c49583a8ca89cfbcfd95a6a6e6a66a6ed`](https://github.com/apache/superset/commit/e8540b7c49583a8ca89cfbcfd95a6a6e6a66a6ed): [`semantic_layers/types.py`](https://github.com/apache/superset/blob/e8540b7c49583a8ca89cfbcfd95a6a6e6a66a6ed/superset-core/src/superset_core/semantic_layers/types.py), [`semantic_layers/view.py`](https://github.com/apache/superset/blob/e8540b7c49583a8ca89cfbcfd95a6a6e6a66a6ed/superset-core/src/superset_core/semantic_layers/view.py), [`superset/semantic_layers/models.py`](https://github.com/apache/superset/blob/e8540b7c49583a8ca89cfbcfd95a6a6e6a66a6ed/superset/semantic_layers/models.py), and [`superset/semantic_layers/schemas.py`](https://github.com/apache/superset/blob/e8540b7c49583a8ca89cfbcfd95a6a6e6a66a6ed/superset/semantic_layers/schemas.py).
- Bounded GitHub searches within `apache/superset` for hierarchy-related code, issues, and PRs, including `hierarchy_context`, `hierarchy-aware`, `drilldown_hierarchy`, and `class Hierarchy`.
- [Current Dataset API schema](https://superset.apache.org/developer-docs/api/schemas/dataset/).
- Historical [SIP-80 hierarchical drill-down proposal](https://github.com/apache/superset/issues/17927), closed without an implementation relationship.

## 4. Current SIP-225 dependency claim

SIP-225 proposes chart-local `form_data.drilldown_hierarchy: string[]`, containing ordered raw column names. It explicitly claims that the list can later be sourced from a dataset/semantic-layer hierarchy and asks whether chart-local configuration should ship now or wait. The issue is in pre-discussion, has no milestone, and shows no development relationship. Its reference implementation, PR #41907, remains open and unmerged.

The author later makes the migration idea more specific: add dataset `hierarchies` as a sibling to columns/metrics, represent each as a named ordered column list, let charts store a reference such as `hierarchy: "geo"`, and allow semantic layers to hydrate that dataset-level interface. This is a useful proposed boundary, but it is discussion—not a current contract or committed implementation.

## 5. Dataset-level hierarchy evidence

No named hierarchy concept, ordered reusable dimension-path object, or hierarchy reference is present in the inspected current Dataset API schema or semantic-layer models. Current datasets expose columns, metrics, IDs/UIDs, and generic extra/configuration fields. Generic extensibility does not establish hierarchy semantics.

The only concrete dataset-level shape found is the SIP-225 author's proposed future `hierarchies` sibling and chart reference. It has no linked issue, schema, PR, or implementation branch.

## 6. Semantic-layer hierarchy evidence

Current code implements `Dimension` and `Metric` objects with stable string `id` and `name` fields plus generic `metadata`; `SemanticView` exposes dimensions, metrics, compatibility filtering, values, and table/row-count queries. It does not expose hierarchy ownership, ordered levels, parent relationships, anchors, hierarchy context, or hierarchy-aware metric behavior.

SIP-182 discussion is more specific but still provisional. Its author said hierarchy would be added to the roadmap and sketched: a dimension `parent` field, metric hierarchy-awareness metadata, query `anchors`, result-row `has_children`, and `hierarchy_context.path`. The same comment labels the request/response structures pseudo-schema, says representation depends on the upstream semantic layer, and states uncertainty about provider support. No matching current code, issue, or PR was found.

## 7. Concrete issues / PRs / implementations found

- **Concrete current substrate:** PR #36245 (merged) introduced the datasource-agnostic `Explorable` protocol.
- **Concrete current substrate:** PR #37815 (merged) implemented semantic layers as extensions and semantic views as explorable sources.
- **Concrete current substrate:** PR #43269 (merged) added optional metadata to semantic-layer dimensions and metrics.
- **Concrete chart-local implementation:** PR #41907 is open and implements SIP-225's inline ordered column list and interaction layer.
- **No concrete hierarchy dependency:** no hierarchy-specific dataset/semantic-layer issue, PR, implementation branch, current code symbol, or committed landing sequence was found in the bounded searches.

## 8. Evidence classification table

| Finding | Classification | Why |
|---|---|---|
| `Dimension`/`Metric`, `SemanticView`, extension models, compatibility APIs | KNOWN CURRENT | Present on current `master` |
| Generic dimension/metric `metadata` | KNOWN CURRENT | Merged in PR #43269; no defined hierarchy semantics |
| Chart-local `drilldown_hierarchy: string[]` | CONCRETE IN FLIGHT | Implemented in open PR #41907, not on `master` |
| Dataset `hierarchies` plus chart `hierarchy: "geo"` reference | DIRECTIONAL | Detailed SIP-225 author comment only |
| Dimension `parent`, hierarchy-aware metrics, `anchors`, `has_children`, `hierarchy_context` | DIRECTIONAL | SIP-182 author's pseudo-schema/roadmap discussion only |
| Hierarchy-specific implementation or committed sequence | ABSENT | No matching current code, issue, PR, branch, milestone, or horizon found |
| Seamless/destructive-free migration from raw names to a future reference | SPECULATIVE | Plausible through an adapter, but no project contract defines it |

## 9. Current-versus-future representation comparison

| Dimension | Current SIP-225 | Future direction evidenced publicly |
|---|---|---|
| Ownership | Chart `form_data` | Dataset named hierarchy or upstream semantic layer |
| Identifier shape | Inline key plus raw column-name strings | Proposed named reference such as `"geo"`; semantic dimensions already have string IDs/names |
| Ordered levels | `string[]` | Proposed named ordered list; SIP-182's parent links imply order but do not define a level-list contract |
| Reference semantics | Raw column names | Proposed hierarchy reference; no stable contract exists |
| Rename/change behavior | Each saved chart can break independently | Proposed central repair at hierarchy owner; behavior undefined |
| Reuse | Re-entered per chart | Proposed reuse across charts |
| Upstream hydration | None | Proposed semantic-layer import/hydration; no sync contract found |
| Interaction coupling | Host consumes an ordered list | Author states click/breadcrumb logic is source-agnostic; PR is chart-local |
| Saved-state migration | Inline lists remain valid while columns remain named | Reference migration path and fallback rules are undefined |
| Adapter potential | High: resolve a source to an ordered list before interaction | Plausible, but not implemented or standardized |

## 10. Migration-risk findings

Raw column names create known rename/removal brittleness and duplicate hierarchy definitions across charts. The current interaction concept is nevertheless narrow: it consumes an ordered list and keeps runtime drill state browser-local. That makes a source-resolution boundary plausible without rewriting the interaction engine.

The largest avoidable risk is not shipping chart-local; it is allowing interaction code and saved-state interpretation to assume the inline list is the only possible hierarchy source. An explicit boundary should preserve inline lists as a fallback and isolate future reference resolution. Exact reference IDs, precedence, validation, import, and migration behavior remain unknown and must not be invented here.

## 11. Timing findings

**Hierarchy dependency timing: UNKNOWN.**

Semantic-layer foundations are current and continue to receive merged work, but hierarchy itself has only roadmap/proposal discussion. There is no hierarchy-specific PR, issue, milestone, release target, or landing sequence. Issue recency and surrounding semantic-layer activity do not justify an imminent classification.

PR #41907 makes chart-local delivery concrete now; it does not make the future hierarchy dependency imminent.

## 12. Exact-resolution assessment

Public evidence resolves one important point: there is no concrete hierarchy dependency that justifies waiting. It also establishes enough future direction—central ownership, reusable names/references, upstream hydration—to make an explicit migration boundary prudent.

Evidence does not fully resolve the adapter/reference contract. A disposable sequencing resolution still has value if it specifies the smallest boundary needed to keep S2 reversible without designing the future semantic architecture.

## 13. Decision state: S1 / S2 / S3

**S2 — Ship now with explicit migration boundary.**

S3 lacks a concrete or imminent dependency. S1 is less defensible because public project-native discussion consistently anticipates central ownership and the current raw-name representation has acknowledged duplication and rename risks.

## 14. Strongest evidence for waiting

The strongest case is the SIP-182 author's public commitment to add hierarchies to the roadmap, accompanied by a concrete pseudo-shape for parent/level metadata and hierarchy-aware queries. This shows that hierarchy support is not merely imagined. It does not establish implementation status or timing, so it is insufficient to justify waiting.

## 15. Strongest evidence for shipping now

No hierarchy contract or implementation exists on current `master`, no hierarchy-specific issue/PR or horizon was found, and PR #41907's interaction is already isolated around an ordered list with non-destructive browser state. The future source can plausibly be resolved before that interaction layer while preserving the inline representation.

## 16. What remains unknown

- Whether the project will model level-based and parent-child hierarchies through one interface.
- Whether hierarchy identity will use names, semantic dimension IDs, UUIDs, or provider-native identifiers.
- Whether metadata will live directly on dimensions, in named hierarchy objects, or both.
- How dataset hierarchies will sync/import from external semantic layers.
- Rename, deletion, precedence, fallback, validation, and saved-chart migration behavior.
- Any hierarchy implementation owner, milestone, release, or landing horizon.

## 17. Research time and spend

- Active research time: approximately 16 minutes.
- Hard ceiling: 30 minutes; not exceeded.
- Incremental spend: €0.
- External interactions: none; all activity was public and read-only.

## 18. What RADAR learned

The phrase “semantic-layer extensions now landing” is true for the general substrate but overstates the hierarchy dependency. Superset now has semantic-view abstractions and extensible metadata, while hierarchy semantics remain directional. The dependency is therefore credible enough to protect a boundary, not concrete enough to block chart-local delivery.

## 19. Whether candidate advances to FORGE

**Yes.** Verdict B permits advancement to a future disposable sequencing resolution. Spec 033 authorizes no FORGE interaction, and none was performed.

## 20. Exactly one recommended next action

Create one disposable, non-implementation sequencing resolution that compares S1/S2/S3 and defines only the minimal hierarchy-source adapter/reference boundary needed for S2, without inventing the future semantic-layer contract.
