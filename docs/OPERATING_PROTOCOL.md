# Asymmetry Engine Operating Protocol

This is the minimal repository-native protocol for recovering, executing, reviewing, and closing bounded work. It defines procedure, not conceptual project truth or software architecture.

## 1. Recovery

A fresh executor reads:

```text
README.md
→ AGENTS.md
→ STATUS.md
→ active specification and result
→ deeper history only as required
```

That sequence must answer:

- what AE is;
- the current project and active-work state;
- what is frozen;
- what work is allowed;
- what requires human judgment or fresh authorization;
- where historical evidence lives;
- the next unresolved decision.

If any answer is missing or repository state conflicts with `STATUS.md`, stop and surface the gap. Do not guess.

### Durable-handoff precondition

Before a minimal handoff is issued, every non-recoverable input required by the receiving role must already exist in Git or another explicitly referenced durable source. Conversation-only evidence is not recoverable project state. If a fresh executor could not complete the handoff from durable state alone, the upstream role must materialize the missing evidence/context before handing off.

A role that can see shared GitHub state must not bridge over unpublished local Codex history. Local-only commits must first be exposed through the appropriate bounded publication/review mechanism; publication authority remains separate from execution authority.

## 2. Authority boundary

```text
SPECIFICATION ≠ AUTHORIZATION
CAPABILITY ≠ AUTHORIZATION
IMPLEMENTATION ≠ HUMAN ACCEPTANCE
```

The human owns objectives, subjective testing, consequential decisions, explicit authorization, and required final judgment. ChatGPT owns reasoning, specifications, independent review, debrief interpretation, and living-truth alignment proposals. Codex owns bounded repository execution, implementation, validation, mechanical evidence capture, permitted Git operations, and transcription of approved evidence.

**Escalate judgment, not work.** Mechanical transcription, routine evidence capture, tests, Git inspection, and bookkeeping belong to Codex when they require no new human judgment.

## 3. Active-work lifecycle

`STATUS.md` carries exactly one current state:

| State | Meaning |
|---|---|
| `READY_FOR_EXECUTION` | Contract is complete; routine execution may begin. Any consequential action still needs fresh explicit authorization. |
| `IMPLEMENTING` | Bounded local execution is in progress. |
| `IMPLEMENTATION_FROZEN` | Implementation/evidence is frozen; no iteration is allowed before the prescribed review. |
| `HUMAN_REVIEW_REQUIRED` | Subjective testing or consequential human judgment is required; agents must not fabricate it. |
| `REVIEW_READY` | A bounded Git ref is available for required independent ChatGPT review. |
| `DEBRIEF_READY` | Approved human/reviewer evidence exists and may be transcribed and interpreted under the active contract. |
| `CLOSURE_READY` | Debrief, checks, and local closure commit are complete; publication is not yet authorized. |
| `CLOSED` | Approved closure is durably published and no work remains under that contract. |
| `BLOCKED` | A named missing dependency, authority, or contradiction prevents valid progress. |

Normal paths may skip inapplicable review states, but they may not skip required human evidence or authorization. `BLOCKED` records the exact blocker and the smallest condition that can clear it.

## 4. Handoff classes

### A — Routine repository execution

Local inspection, implementation, tests, validation, evidence capture, permitted commits, and safe Git operations within the active contract. No consequential external action.

### B — Human acceptance/testing

Codex freezes the test surface and prepares the acceptance packet. The human supplies subjective observations or decisions. Codex may later transcribe approved evidence exactly; it may not answer on the human's behalf.

### C — Consequential external action

Requires a complete specification **and fresh explicit authorization for the exact action**. Authentication, platform access, an earlier authorization, or technical ability is insufficient. Stop if any preregistered control fails.

### D — Independent ChatGPT review of local changes

When review requires actual local-only work, Codex prepares a bounded branch named `codex/review-<work-id>`, containing only review-permitted changes, and pushes that branch. ChatGPT reviews the actual GitHub state. Publishing a review branch authorizes neither merge nor a push to `main`; both require a later explicit handoff.

## 5. Minimal handoff commands

These commands derive their scope from `STATUS.md`, the active contract, and the handoff class. They never broaden authority.

### `Execute the active work packet.`

Verify repository state, move `READY_FOR_EXECUTION → IMPLEMENTING`, execute the bounded contract, validate, commit permitted work locally, and stop at its prescribed freeze/review state. Class C action requires fresh explicit authorization in the same bounded handoff.

### `Prepare the active work for review.`

Preserve the frozen output, prepare the smallest acceptance/review packet, run integrity checks, and set `HUMAN_REVIEW_REQUIRED` or `REVIEW_READY`. For Class D, publish only the bounded `codex/review-<work-id>` branch.

### `Record the approved debrief and close the active work.`

Use only already-approved human/reviewer evidence. Transcribe it without strengthening or weakening it, apply the contract's verdict rules, run checks, create the local closure commit, and set `CLOSURE_READY`. This command does not authorize push.

### `Publish the approved closure.`

Verify the exact closure commit, clean scope, and normal fast-forward path. With explicit publication authority, update the operational pointer to `CLOSED` as part of the bounded publication state, push only the approved history, and verify synchronization. Never force-push, rebase, amend, or resolve unexpected divergence automatically.

## 6. Durable truth and alignment

| Location | Role |
|---|---|
| `specs/` | Immutable work contracts: hypotheses, controls, budgets, stop rules, required evidence, verdicts. |
| `experiments/` | Durable execution evidence, results, acceptance records, and debrief history. |
| Living docs | Current conceptual truth, changed only through explicit alignment work. |
| `STATUS.md` | Current operational pointer, state, authority, frozen work, and next operation. |
| `AGENTS.md` | Permanent operating and authority contract. |

Experiment evidence must not silently rewrite living truth. A result may earn an alignment proposal; it does not apply that proposal automatically. Historical artifacts remain historical even when living truth changes.

## 7. Git discipline

- Preserve unrelated changes and frozen artifacts.
- Commit only files permitted by the active handoff.
- Prefer normal fast-forward operations; stop on unexpected divergence.
- Do not amend, rebase, force-push, or rewrite evidence history unless a separate explicit instruction authorizes the exact operation.
- A local commit is not publication. A review-branch push is not main-branch authority. A main-branch push is not consequential actor authorization.

## 8. Protocol boundary

This protocol earns no hooks, CI, workflow engine, scheduler, queue, orchestration layer, database, ADR system, template suite, monitoring, or automation. Use concise documents and Git until repeated operational evidence justifies a different mechanism.
