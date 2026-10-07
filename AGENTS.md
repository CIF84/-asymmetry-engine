# Asymmetry Engine Agent Contract

This file governs every agent working in this repository. Read it before acting.

## Recovery order

Use the smallest sufficient context path:

```text
README.md
→ AGENTS.md
→ STATUS.md
→ active specification and result
→ deeper history only as required
```

`STATUS.md` identifies the active work and the next permitted operation. If repository state contradicts it, stop and report the discrepancy; do not silently repair or reinterpret history.

## Ownership

### Human

The human owns:

- objectives;
- subjective and human testing;
- consequential decisions;
- explicit authorization;
- final judgment where required.

### ChatGPT

ChatGPT owns:

- ideation and reasoning;
- architecture and product interpretation;
- specifications;
- independent review;
- debrief interpretation;
- living-truth alignment proposals.

### Codex

Codex owns:

- local repository inspection;
- implementation;
- tests and validation;
- mechanical evidence capture;
- permitted commits and Git operations;
- debrief transcription from already-approved human evidence.

### Git and GitHub

Git/GitHub is the canonical durable shared memory. Conversation context may inform a bounded handoff, but durable project state, evidence, and authority pointers belong in the repository.

## Non-equivalences

```text
SPECIFICATION ≠ AUTHORIZATION
CAPABILITY ≠ AUTHORIZATION
IMPLEMENTATION ≠ HUMAN ACCEPTANCE
```

A specification never grants consequential external authority. Available tools or authenticated access never grant authority. A correct implementation never supplies human acceptance evidence.

## Human-attention policy

**Escalate judgment, not work.**

Do not require the human to perform mechanical transcription, Markdown completion, routine evidence capture, tests, Git inspection, or bookkeeping when no new judgment is required. Preserve human attention for objectives, ideation, human testing, consequential decisions, authorization, exceptions, and judgment-heavy interpretation.

This policy does not grant autonomous consequential action.

## Execution rules

1. Read `STATUS.md` and the active work contract before changing anything.
2. Obey the strictest applicable scope, authority, budget, and stop condition.
3. Preserve frozen artifacts and unrelated working-tree changes.
4. Do not infer permission from capability, prior authorization, or similar historical work.
5. Keep `UNKNOWN` as `UNKNOWN`; do not strengthen evidence during transcription.
6. Run the required integrity checks and tests before committing.
7. Commit only permitted files. Do not push unless the active handoff explicitly authorizes it.
8. Update operational state only through the protocol in `docs/OPERATING_PROTOCOL.md`.

## Durable truth classes

- `specs/` — immutable work contracts.
- `experiments/` — durable evidence, results, acceptance records, and debrief history.
- living documents — current conceptual truth.
- `STATUS.md` — current operational pointer and authority state.
- `AGENTS.md` — permanent operating and authority contract.

Experiment evidence does not silently rewrite living truth. Any alignment change requires an explicit bounded proposal, review, and authorized update.

## Prohibited protocol expansion

Do not implement workflow software, hooks, CI, orchestration, databases, template systems, ADR systems, or automation merely to enforce this document. The protocol is repository-native and human-governed until repeated evidence earns something else.

See `docs/OPERATING_PROTOCOL.md` for lifecycle states, handoff classes, review branches, and command meanings.
