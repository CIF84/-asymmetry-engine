# Spec 002 — Targeted Deduplication Conflict

## Goal

Tighten the Spec 001 SQLite deduplication behavior so that only the intended duplicate identity conflict is ignored.

This is a small corrective specification discovered during review of the first empirical slice. It should remain a small change.

## Context

Spec 001 correctly enforces source-item identity with:

```text
UNIQUE(source_id, external_id)
```

However, observation insertion currently uses SQLite `INSERT OR IGNORE`.

That statement is broader than the domain rule. `OR IGNORE` can suppress constraint failures other than the intended duplicate source/external identity conflict. The pipeline then interprets any ignored insert as a duplicate.

The desired semantic is narrower:

> An already-observed `(source_id, external_id)` is a duplicate and may be ignored. Other persistence errors should fail loudly and cause the source run to fail according to the existing transactional behavior.

This change is about making persistence semantics match the domain rule exactly. It is not a redesign of the persistence layer.

## Scope

Change observation insertion so that conflict suppression targets only the uniqueness constraint representing stable source/external identity.

A suitable SQLite form is:

```sql
INSERT INTO source_observations (...)
VALUES (...)
ON CONFLICT(source_id, external_id) DO NOTHING
```

Equivalent implementation is acceptable if it has the same semantics.

Preserve the existing behavior that:

- first observation of a stable source/external identity is inserted
- subsequent insertion of that same identity is counted as a duplicate
- the duplicate does not create another observation row
- other persistence/constraint failures are not silently classified as duplicates
- persistence failure rolls back the observation batch
- the pipeline run is recorded as failed

## Tests

Retain the existing deduplication and rollback tests.

Add or adjust a focused test proving that a persistence constraint/error unrelated to `(source_id, external_id)` uniqueness is **not** swallowed as a duplicate.

The test should demonstrate the externally meaningful behavior rather than merely asserting the SQL string:

- run encounters a non-deduplication persistence failure
- run status becomes `failed`
- the failure is not counted as a duplicate
- no unintended partial observation batch remains committed

Use the smallest deterministic test mechanism that exercises the real persistence behavior.

## Explicitly out of scope

Do not use this corrective change to introduce:

- schema redesign
- migrations framework
- ORM
- observation version history
- monitoring
- mutable-source-state handling
- new collectors
- CFPB
- LLM extraction
- DecisionSignal
- DecisionProblem
- generic Evidence
- clustering
- scoring
- UI
- scheduling

Do not modify README.md, ARCHITECTURE.md, ROADMAP.md, or Spec 001 merely to make them reflect this correction. Spec 001 remains the historical implementation contract; this specification records the review-driven correction.

## Acceptance criteria

This specification is complete when:

1. Duplicate suppression applies only to the `(source_id, external_id)` uniqueness conflict.
2. Re-inserting an existing source/external identity still produces one persisted observation and the correct duplicate count.
3. A non-deduplication persistence failure is surfaced as a failure rather than counted as a duplicate.
4. Existing source-run transactional behavior remains intact: no unintended partial observation batch is committed on failure.
5. The pipeline run records the failure according to the existing Spec 001 semantics.
6. All tests pass.

## Requested completion report

When complete, Codex should report:

1. Commit SHA and commit message.
2. Files changed.
3. Exact persistence semantic changed.
4. Test added/changed to prove non-deduplication errors are not swallowed.
5. Test command and result/count.
6. Confirmation that no unrelated architecture or functionality was added.

Then stop. Do not proceed to CFPB or another roadmap phase. The next action is ChatGPT review and empirical interpretation of the Spec 001 observations.