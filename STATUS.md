# Asymmetry Engine Status

**Recorded:** 2026-10-07

**Branch:** `main`

**Operational state:** `READY_FOR_EXECUTION`

## Current project state

Asymmetry Engine is an experimental system for discovering economically consequential decisions under resolvable uncertainty and testing whether better resolution changes decisions and can eventually create and capture repeatable value. Current conceptual truth begins in `README.md`; authority and execution rules are in `AGENTS.md` and `docs/OPERATING_PROTOCOL.md`.

Bounded representation milestones:
- Experiment 051 — Representation V0: **What does AE know?**
- Experiment 052 — Control V1: **What needs the human operator?**
- Experiment 053 — Engine-State Semantics Audit: **whole-Engine counts require identity/evidence-contract repair first.**

## Active work

**Experiment 054 — Opportunity Identity and Evidence-Contract Repair**

- Specification: `specs/054-opportunity-identity-evidence-contract-repair.md`
- Type: bounded repository-only manual data-contract experiment.
- Cohort: exactly six historical chains — Cocoa, EV, Canadian tariff, CRM, Superset, realtime migration.
- Goal: test whether a minimal family/decision-instance identity and evidence contract can faithfully preserve history, lifecycle, evidence frontier, dormancy/reactivation, control state, provenance, and missingness without inventing evidence.
- Secondary goal: test whether the contract is sufficient for prospective truthful Engine accounting.
- No database/schema/UI/software implementation is authorized.
- No historical backfill beyond the six-case cohort is authorized.

## Authority now

Allowed under `Execute the active work packet.`:
- inspect repository evidence required by SPEC-054;
- execute the bounded six-case manual contract test;
- create only permitted Experiment 054 artifacts;
- mechanically update STATUS under the operating protocol;
- run tests/integrity checks;
- commit permitted work locally.

Not authorized:
- push Experiment 054;
- implement Engine UI/funnel;
- create production opportunity identity/persistence;
- backfill the full repository;
- modify 051/052/053;
- modify living or protocol docs;
- run fresh RADAR;
- use external research;
- perform consequential external action.

## Frozen and historical pointers

- Experiment 051 CLOSED and frozen.
- Experiment 052 CLOSED; V1 remains frozen.
- Experiment 053 CLOSED at published closure; verdict B — data-contract repair first.
- Experiment 054 has not yet executed.
- Historical evidence remains in `specs/` and `experiments/`; inspect only as required by SPEC-054.

## Next unresolved decision

Can one minimal manual opportunity identity/evidence contract survive the six historical cases and identity/counting stress tests strongly enough to support prospective Engine accounting without production software?

## Next operation

`Execute the active work packet.`

Publication is not authorized.
