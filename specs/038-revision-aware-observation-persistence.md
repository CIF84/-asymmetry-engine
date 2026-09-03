# Spec 038 — Revision-Aware Observation Persistence

## Status

Bounded implementation experiment.

This is the first code change proposed by the Architecture Gap Audit (`docs/ARCHITECTURE_GAP_AUDIT_001_036.md`). It is intentionally narrow and independent of the still-open 030/035 interaction outcomes.

The implementation is earned because the current persistence model conflates:

```text
LOGICAL SOURCE ITEM IDENTITY
(source_id, external_id)
```

with:

```text
ONE STORED CAPTURE
```

and therefore silently discards later materially changed observations of the same source item.

---

## Primary question

> **Can the Engine preserve materially changed recaptures of the same logical source item as append-only evidence, while continuing to suppress unchanged recaptures and preserving the current small SQLite/CLI architecture?**

---

## Why this is earned

The current table has:

```sql
UNIQUE (source_id, external_id)
```

and `complete_run()` uses:

```sql
ON CONFLICT(source_id, external_id) DO NOTHING
```

This means a later observation with the same stable source identity is discarded even when mutable evidence changed, including examples such as:

- content/body;
- score/activity/status;
- price;
- official statistics;
- procurement state;
- effective-date facts;
- metadata.

Later experiments increasingly rely on freshness, revision history, effective timing, reproducibility, and the principle:

```text
IMMUTABLE EVIDENCE
MUTABLE INTERPRETATION
```

The change is therefore about evidence preservation, not generic event sourcing or application versioning.

---

## Scope

Implement the smallest persistence change that separates:

```text
LOGICAL ITEM
    ↕ stable identity
(source_id, external_id)

CAPTURE / REVISION
    ↕ evidence observed at a particular point in collection history
material observation fields + run provenance
```

Required behavior:

1. first sighting of a logical source item is persisted;
2. later unchanged recapture is treated as a duplicate and does not create a redundant capture;
3. later materially changed recapture creates a new immutable capture;
4. if an item changes A → B → A, the final A is a new capture because it represents a real later state transition;
5. every stored capture remains associated with the pipeline run that observed it;
6. existing logical source identity remains stable;
7. existing callers and CLI behavior remain compatible where practical;
8. existing databases created by the current schema can be opened and upgraded without losing preserved observations.

---

## Material equality semantics

Do **not** use `observed_at` or `pipeline_run_id` to decide whether two captures are materially different. Those fields necessarily change across collection runs and would cause useless append-only duplication.

For this implementation, material equality must include the persisted observation payload:

```text
source_id
external_id
occurred_at
item_kind
content
canonical_url
metadata_json (canonicalized)
```

`source_id` and `external_id` establish the logical item group but should still be part of any deterministic capture fingerprint if one is used.

`metadata_json` must use deterministic canonical serialization consistent with the current repository (`sort_keys=True`).

The implementation may use direct field comparison or a deterministic content fingerprint/hash. Prefer the smallest clear implementation.

### Important transition rule

Duplicate suppression must compare a new observation to the **latest stored capture for that logical item**, not merely to any historical capture.

Therefore:

```text
A at t1 → store revision 1
A at t2 → duplicate; do not store
B at t3 → store revision 2
B at t4 → duplicate; do not store
A at t5 → store revision 3
```

The t5 capture must not be suppressed merely because revision 1 also contained A.

---

## Data-model requirements

Choose the smallest SQLite design that provides the required behavior.

Acceptable shapes include:

- a logical-item table plus append-only capture table;
- an append-only observation table with explicit logical grouping and a suitable latest-capture query;
- another comparably small normalized design.

The implementation must make these concepts unambiguous:

```text
logical identity
capture identity
capture sequence/order
run provenance
current/latest capture
```

### Required invariants

- `(source_id, external_id)` identifies one logical source item.
- A stored capture is immutable after insertion.
- One logical item may have multiple captures.
- Capture order is deterministic.
- The current/latest capture can be selected deterministically.
- No observation from the old schema is lost during upgrade.
- Foreign-key integrity remains enabled.
- A batch failure still rolls back atomically.

Do not introduce an ORM.

---

## Existing database compatibility

The repository currently initializes schema with `CREATE TABLE IF NOT EXISTS` and has no general migration framework.

A **single bounded compatibility migration** for this earned schema change is allowed.

Requirements:

1. detect the existing pre-038 schema safely;
2. migrate existing `source_observations` rows into the new representation without changing their evidence fields or run provenance;
3. preserve observation ordering deterministically;
4. leave an already-migrated database unchanged on subsequent opens;
5. perform migration transactionally;
6. add regression tests that start from a representative legacy schema/database and prove upgrade behavior.

Do not build a generic migration framework unless the smallest correct implementation genuinely requires a tiny version marker. If a schema-version marker is introduced, keep it minimal and scoped to this compatibility problem.

---

## Run accounting semantics

Preserve the current `complete_run()` contract where practical:

```python
(inserted, duplicates)
```

For Spec 038:

- `inserted` = number of new captures persisted during this run;
- `duplicates` = number of fetched observations whose material state is unchanged from the latest stored capture for that logical item.

`pipeline_runs.inserted_count` and `duplicate_count` must follow the same semantics.

A changed recapture is **inserted**, not a duplicate.

No new `changed_count` column is required unless implementation evidence shows it is necessary. It is acceptable that both first sightings and changed revisions count as inserted captures.

---

## Current-view behavior

Provide the smallest repository query needed to retrieve the latest/current capture for a logical source item or latest captures generally if current code needs it.

Do not create a large query abstraction layer.

Existing reasoning code should continue to operate on the intended current/latest evidence rather than accidentally consuming every historical revision as independent simultaneous evidence.

This requirement is important: append-only storage must not silently change the semantics of CN75 reasoning or other existing readers.

If `reasoning.py` currently accesses raw SQL directly, make only the minimum change necessary to preserve its current semantic behavior.

---

## Required regression cases

Tests must prove at least the following.

### Case 1 — first capture

```text
run 1: A
→ one logical item
→ one capture
→ inserted=1
→ duplicates=0
```

### Case 2 — unchanged recapture

```text
run 1: A
run 2: A
→ one logical item
→ one stored capture
→ run 2 inserted=0
→ run 2 duplicates=1
```

The original capture's `observed_at` and run provenance remain unchanged.

### Case 3 — changed content

```text
run 1: A
run 2: B
→ one logical item
→ two captures
→ run 2 inserted=1
→ run 2 duplicates=0
```

### Case 4 — changed metadata only

A metadata-only material change must create a new capture.

### Case 5 — changed `occurred_at` only

A changed effective/event timestamp must create a new capture.

### Case 6 — changed canonical URL or item kind

A material change to either persisted field must create a new capture.

### Case 7 — `observed_at` only changes

If all material fields are unchanged and only `observed_at` differs, no new capture is created.

### Case 8 — reversion A → B → A

Three captures must exist. The final A is not suppressed by historical equality with revision 1.

### Case 9 — multiple logical items in one run

Changed, unchanged, and first-seen items in one batch must produce correct inserted/duplicate counts.

### Case 10 — rollback

A non-duplicate database constraint/error during batch persistence must roll back all captures and run completion changes exactly as before.

### Case 11 — current/latest query

After multiple revisions, current-view retrieval returns the latest capture only and deterministically.

### Case 12 — legacy database migration

A database with the pre-038 schema and preserved observations opens successfully, migrates without data loss, and supports later changed recapture.

### Case 13 — migration idempotence

Opening an already migrated database again does not duplicate or alter captures.

### Case 14 — existing test suite

All pre-existing tests must continue to pass unless a test encoded the old incorrect changed-recapture behavior. Any such test must be updated explicitly rather than deleted silently.

---

## Source registry history — explicitly deferred

The Architecture Gap Audit also found that `signal_sources` is upserted in place, so source terms/caveats/metadata represent current state rather than historical run context.

That is a real provenance concern, but **it is not part of Spec 038 implementation scope**.

Do not add source-registry revision history in this change.

Record it as a follow-up architectural debt item only if the implementation touches related code.

Reason: observation-capture loss is the immediate proven defect. Combining source-policy history would broaden the migration and make the causal benefit harder to evaluate.

---

## Explicitly prohibited

Do not build:

- generic event sourcing;
- temporal database abstractions;
- generic version-control framework;
- generic migration framework;
- ORM;
- opportunity/scoring models;
- experiment database;
- telemetry database;
- source change-notification system;
- automatic semantic diffing;
- generic provenance graph;
- current-state/event architecture beyond what this persistence fix needs;
- actor interaction or 030/035 tooling.

Do not modify opportunity-model or telemetry checkpoint documents.

Do not inspect live 030/035 state.

---

## Implementation preference

Prefer additive, legible code over a large refactor.

The expected solution should remain understandable in one sitting by reading:

```text
models.py
→ db.py
→ pipeline.py
→ relevant tests
```

If implementation requires broad changes across source adapters, stop and reassess: stable adapter identity is intended to remain unchanged.

---

## Documentation

Update only documentation directly made stale by the persistence behavior change.

At minimum, make sure any claim that `source_observations` stores only first-seen items or deduplicates forever by `(source_id, external_id)` is corrected if present.

Do not rewrite the whole architecture documentation in this implementation spec.

---

## Validation

Run the complete test suite.

Report:

- total tests passed;
- new tests added;
- any modified existing tests and why;
- migration test result;
- unchanged/changed/reversion behavior;
- current-view behavior;
- any warnings.

No live external-source collection is required for acceptance. Unit/integration tests with deterministic observations are sufficient.

---

## Success criteria

Spec 038 succeeds only if all of the following are true:

```text
UNCHANGED RECAPTURE → NO REDUNDANT CAPTURE
CHANGED RECAPTURE   → NEW IMMUTABLE CAPTURE
REVERSION           → NEW CAPTURE
LATEST VIEW          → DETERMINISTIC CURRENT EVIDENCE
LEGACY DATABASE      → SAFE UPGRADE
RUN COUNTS           → CORRECT
BATCH FAILURE        → ATOMIC ROLLBACK
OLD TESTS            → STILL PASS / EXPLICITLY JUSTIFIED UPDATE
ARCHITECTURE         → REMAINS SMALL
```

---

## Verdicts

### A — REVISION-AWARE PERSISTENCE IMPLEMENTED

All required semantics, compatibility, current-view behavior, and regression tests pass with bounded architecture.

### B — CORE REVISION SEMANTICS IMPLEMENTED, COMPATIBILITY GAP REMAINS

New databases behave correctly but a material legacy/current-view/rollback issue remains.

### C — IMPLEMENTATION REQUIRES BROADER ARCHITECTURE THAN JUSTIFIED

The smallest correct solution appears materially larger or more coupled than the audit predicted. Stop rather than overbuild.

### D — REVISION MODEL INVALIDATES EXISTING SEMANTICS

The proposed revision behavior conflicts with source identity or reasoning semantics in a way not anticipated by the audit.

### E — INVALID / INCOMPLETE EXECUTION

Tests, isolation, or implementation evidence are insufficient.

---

## Resource budget

Target active time: **30–45 minutes**.

Hard ceiling: **60 minutes**.

Incremental spend: **€0**.

Use a prospective active-work timer from the beginning.

No external interaction.

---

## Stop conditions

Stop and report rather than broadening scope if:

- adapter identities need redesign across multiple sources;
- migration requires a general framework rather than one bounded compatibility path;
- current-view semantics cannot be preserved without redesigning reasoning;
- unexpected repository divergence is present;
- live 030/035 evidence would be needed;
- the 60-minute hard ceiling is reached.

---

## Required implementation artifact

Create:

`experiments/038/revision-aware-observation-persistence.md`

Record:

- baseline commit;
- schema before/after;
- equality semantics;
- migration approach;
- tests added/changed;
- final test result;
- implementation tradeoffs;
- deferred source-registry-history issue;
- active time/spend;
- verdict.

---

## Required completion report

Return exactly:

1. Verdict
2. Repository baseline
3. Active time and timing method
4. Spend
5. Isolation confirmation
6. Root cause confirmed yes/no
7. Schema before
8. Schema after
9. Logical identity semantics
10. Capture identity/order semantics
11. Material equality semantics
12. Latest-capture comparison behavior
13. First-capture result
14. Unchanged-recapture result
15. Changed-recapture result
16. Metadata-only-change result
17. Occurred-at-change result
18. Reversion result
19. Run-count semantics
20. Current/latest-view result
21. Legacy migration approach
22. Legacy migration result
23. Migration idempotence result
24. Rollback result
25. Existing-reader compatibility
26. Source-adapter changes
27. Existing tests modified and why
28. New tests added
29. Full test-suite result
30. Warnings
31. Files changed
32. Documentation changed
33. Explicitly deferred work
34. Architecture-size assessment
35. Artifact path
36. Commit SHA
37. Exactly one recommended next action
