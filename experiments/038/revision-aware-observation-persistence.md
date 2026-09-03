# Experiment 038 — Revision-Aware Observation Persistence

**Baseline commit:** `865f7d38082affc01a5f4534d72d095dd5caf6f0`  
**Verdict:** **A — REVISION-AWARE PERSISTENCE IMPLEMENTED**  
**Prospective timer start:** `2026-09-03T02:43:34Z`  
**Prospective timer end:** `2026-09-03T02:49:56Z`  
**Active time:** `6 minutes 22 seconds` (382 seconds), derived from prospectively captured UTC epoch timestamps through final implementation review  
**Incremental spend:** `€0`

## 1. Question and result

The experiment asked whether materially changed recaptures of one stable logical source item can be preserved as append-only evidence while unchanged recaptures remain suppressed and the small SQLite/CLI architecture stays intact.

The answer is yes. Logical identity remains `(source_id, external_id)`. Each persisted state has a positive per-item `capture_sequence`; equality is evaluated only against the latest capture; unchanged material state increments the run's duplicate count without inserting; changed state inserts the next immutable capture. The full suite passes.

## 2. Root cause

The pre-038 table enforced:

```sql
UNIQUE (source_id, external_id)
```

and insertion used targeted `DO NOTHING` on that conflict. This correctly protected stable source identity but also made one logical item synonymous with one permanent stored observation. Later changed content, metadata, status, price, URL, item kind, or event/effective time was silently counted as a duplicate and lost.

## 3. Schema before

```text
signal_sources
pipeline_runs
source_observations
  observation_id PRIMARY KEY
  source_id
  external_id
  observed_at
  occurred_at
  item_kind
  content
  canonical_url
  metadata_json
  pipeline_run_id
  UNIQUE(source_id, external_id)
```

One row represented both the logical item and its only stored capture.

## 4. Schema after

The existing table name and all evidence columns remain. One field and one index are added through a bounded table rebuild:

```text
source_observations
  observation_id PRIMARY KEY               # capture identity
  source_id
  external_id
  capture_sequence INTEGER NOT NULL > 0    # order within logical item
  observed_at
  occurred_at
  item_kind
  content
  canonical_url
  metadata_json
  pipeline_run_id
  UNIQUE(source_id, external_id,capture_sequence)

INDEX source_observations_latest
  (source_id,external_id,capture_sequence DESC)
```

`(source_id, external_id)` is the logical identity. `(source_id, external_id, capture_sequence)` identifies the ordered capture within that item; `observation_id` remains the database capture key. Stable source-adapter identities are unchanged.

## 5. Material equality and transition semantics

For an incoming observation, persistence first selects the latest stored capture for the same logical identity. It canonicalizes `metadata_json` with `json.dumps(..., sort_keys=True)` and compares:

```text
occurred_at
item_kind
content
canonical_url
metadata_json
```

`source_id` and `external_id` are included by selecting the logical group. `observed_at` and `pipeline_run_id` are deliberately excluded because they change on every collection run.

Comparison is latest-to-new, not any-history-to-new. Therefore:

```text
A → stored sequence 1
A → duplicate
B → stored sequence 2
B → duplicate
A → stored sequence 3
```

No semantic diffing or generic version system was introduced.

## 6. Run accounting

`complete_run()` still returns `(inserted, duplicates)`.

- `inserted` counts first sightings plus materially changed captures inserted in that run.
- `duplicates` counts fetched observations materially equal to the latest capture.
- `pipeline_runs.inserted_count` and `duplicate_count` use the same definitions.
- An unchanged recapture does not mutate the original capture's timestamp or run provenance.
- Every stored capture has the `pipeline_run_id` of the run that observed that stored state.

## 7. Current/latest reader

`Repository.latest_observations(source_id=None)` returns exactly one deterministic current row per logical item using maximum `capture_sequence`, ordered by source and external identity. The CN75 reasoning reader now uses this method rather than selecting every row directly.

This preserves prior reasoning semantics: historical revisions remain auditable in storage but cannot be consumed accidentally as simultaneous current evidence. A regression test revises one CN75 measurement, verifies that two captures exist, and proves reasoning uses only the revised current value.

## 8. Legacy compatibility migration

Repository initialization checks whether `source_observations` exists and whether it contains `capture_sequence`.

- New database: create the revision-aware table and latest index directly.
- Legacy database: begin one explicit `BEGIN IMMEDIATE` transaction, create a temporary v038 table, copy every legacy row with its original `observation_id`, evidence fields, and `pipeline_run_id`, assign sequence 1, drop the legacy table, rename the new table, and create the index.
- Already migrated database: leave captures unchanged and ensure the index exists.

No general migration framework or schema-version service was added. Tests prove all legacy fields survive, foreign keys remain valid, reopening is idempotent, a changed post-migration recapture is accepted, and a deliberately invalid legacy database rolls the whole schema rebuild back without leaving the temporary table.

## 9. Regression behavior

| Case | Result |
|---|---|
| First A | One logical item, sequence 1, inserted 1, duplicates 0 |
| A then unchanged A | One capture; second run inserted 0, duplicates 1; original time/run retained |
| Content change | New sequence inserted |
| Metadata-only change | New sequence inserted |
| `occurred_at`-only change | New sequence inserted |
| Canonical-URL change | New sequence inserted |
| Item-kind change | New sequence inserted |
| `observed_at`-only change | Suppressed as unchanged |
| A → B → A | Sequences 1, 2, 3 stored |
| Mixed changed/unchanged/new batch | Inserted 2, duplicates 1 |
| Non-duplicate constraint failure | Entire capture batch rolls back; run becomes failed |
| Latest view | One highest-sequence row per logical item |
| Legacy upgrade | Original evidence/key/run preserved; changed recapture accepted |
| Second open | No duplicate or altered migrated capture |

## 10. Tests added or changed

Eight new test functions produce twelve collected regression cases:

1. unchanged recapture preserves original capture and run;
2. five parameterized material-change cases: content, metadata, occurred time, URL, and kind;
3. A → B → A reversion;
4. mixed changed/unchanged/first-seen accounting;
5. deterministic latest-view selection;
6. legacy migration, field preservation, idempotence, and post-upgrade change;
7. transactional rollback of a failed legacy rebuild;
8. current-only CN75 reasoning after a historical revision.

No existing test behavior or assertion was removed. Existing imports were extended and the tests were appended. The pre-existing batch rollback test continues to prove that a non-deduplication persistence failure rolls back inserted captures and records the run as failed.

## 11. Validation

Command:

```text
.venv/bin/pytest -q
```

Final result before artifact finalization:

```text
89 passed in 0.25s
1 warning
```

The warning is the existing sandbox-specific `PytestCacheWarning`: pytest could not update `.pytest_cache/v/cache/nodeids` because that cache path was not writable. It does not affect test execution, database behavior, or tracked files. No live source collection was performed.

## 12. Tradeoffs and bounded architecture

- Direct field comparison is clearer than a new fingerprint abstraction at this size.
- Per-item sequence provides deterministic transition order without event sourcing or temporal-query abstractions.
- The existing table name minimizes reader and CLI disruption.
- A bounded table rebuild is necessary to remove the old two-column uniqueness constraint; explicit transaction handling makes it atomic.
- The latest-view method is intentionally narrow and returns SQLite rows, matching the existing repository style rather than introducing models or an ORM.
- Changed and first-seen captures share `inserted_count`, as required; no redundant `changed_count` was added.
- Failed/partial collector capture beyond the existing batch contract remains out of scope.

Changed implementation is limited to `db.py` and the current CN75 reader. No source adapter changed.

## 13. Explicitly deferred

Source-registry history remains deferred: `signal_sources` still represents mutable current source terms/caveats/metadata and is not snapshotted per run. Also deferred are event sourcing, generic migrations, ORM, generic provenance or temporal models, notifications, telemetry, scoring, opportunity models, experiment persistence, interaction systems, and any 030/035-dependent capability.

No Opportunity Model, Economic Telemetry Baseline, live-interaction artifact, or external state was modified or consulted.
