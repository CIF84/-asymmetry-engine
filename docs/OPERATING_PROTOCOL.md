# Asymmetry Engine Operating Protocol

This protocol minimizes human operational work while preserving consequential authority, independent review, durable recovery, and evidence integrity.

## 1. Core rule

> **Human approval gates judgment and consequences, not repository bookkeeping.**

Routine Git publication inside the already-designated AE repository is mechanical project work when it:
- stays within the active contract;
- contains no secrets/customer data;
- preserves history;
- uses normal fast-forward/non-destructive operations;
- changes only permitted project files.

It does not require a fresh human approval merely because bytes leave the local checkout for the canonical project repository.

Consequential external action remains separately gated.

## 2. Roles

### Human
Owns:
- objectives and preferences;
- subjective/human testing;
- consequential economic/external authorization;
- acceptance of legal/commercial obligations;
- decisions where evidence supports multiple consequential paths.

The human is **not** the normal Git relay.

### ChatGPT
Owns:
- strategy/ideation;
- specifications;
- independent review;
- debrief interpretation;
- bounded protocol/living-truth proposals;
- direct GitHub writes when available and within repository authority.

### Codex
Owns:
- repository recovery;
- execution;
- tests/integrity;
- mechanical evidence capture;
- commits;
- routine review/canonical publication under this protocol;
- debrief transcription from approved evidence.

### Git/GitHub
Canonical durable shared memory.

## 3. Authority classes

### R — Repository-mechanical authority
Standing authority for Codex/ChatGPT to perform non-destructive repository operations in **this AE repository only** when required by an active contract/protocol:
- fetch;
- clean fast-forward;
- create/update bounded review refs;
- publish frozen review evidence;
- publish approved closure/canonical history;
- correct stale operational pointers;
- verify remote equality.

Conditions:
- no force-push/rebase/amend/history rewrite;
- no secrets/customer/private operational data;
- exact permitted-file scope;
- tests/integrity pass;
- stop on unexpected divergence/conflict;
- no expansion into external economic action.

**No fresh human approval is required for Class R.**

### H — Human judgment
Required when subjective evidence, product acceptance, strategic choice among consequential alternatives, or genuinely non-recoverable human preference is needed.

### C — Consequential external action
Fresh explicit human authorization required for the exact action, including:
- spending or financial exposure;
- accepting commercial/legal terms;
- account creation/enrollment where obligations arise;
- contacting actors/customers;
- publishing market-facing offers/content;
- transactions/trading;
- deployment that creates external obligations or irreversible effects.

Authentication/capability never implies C authority.

## 4. Recovery

Fresh agent reads the smallest sufficient path:

`README → AGENTS → STATUS → active spec/result → deeper evidence only as needed`.

If STATUS is stale but Git contains **unambiguous newer approved evidence**, the agent may reconcile STATUS mechanically under Class R and record the evidence pointer. Stop only when reconciliation requires judgment or competing histories exist.

This replaces the old rule that every STATUS contradiction requires human intervention.

## 5. Operational state

STATUS is a **derived operational pointer**, not the authority ledger or evidence source.

Keep it small:
- phase;
- active work ID;
- state;
- spec/result/review/debrief pointers;
- exact unresolved human/consequential decision, if any;
- next agent operation.

Historical publication narrative, hashes, timing, validation detail and authority prose belong in experiment artifacts/Git history, not STATUS.

States:
- `READY_FOR_EXECUTION`
- `IMPLEMENTING`
- `FROZEN`
- `HUMAN_DECISION_REQUIRED`
- `REVIEW_READY`
- `CLOSURE_READY`
- `CLOSED`
- `BLOCKED`

Use BLOCKED only for a real unresolved dependency/ambiguity, not because a routine repository push awaits redundant approval.

## 6. Normal experiment path

### No human review required
`READY → EXECUTE → FROZEN → REVIEW (if prescribed) → DEBRIEF/CLOSE → CLOSED`

Repository publication between these states is automatic Class R work.

### Human judgment required
`READY → EXECUTE → FROZEN → HUMAN_DECISION_REQUIRED → approved evidence → CLOSE → CLOSED`

One human interaction should normally contain the actual judgment, not Git instructions.

### Consequential economic experiment
`READY → design/freeze/review → HUMAN_DECISION_REQUIRED → explicit Class C authorization → external execution`

Human authorization occurs as close as practical to the consequential action.

## 7. Independent ChatGPT review

If ChatGPT can read the frozen state directly from canonical GitHub, Codex publishes the smallest review ref automatically under Class R.

Preferred:
- immutable experiment evidence on a bounded `codex/review-<id>` ref;
- ChatGPT records `review.md` there;
- Codex consumes that durable review.

A review-ref push does not authorize external action.

If direct canonical publication is safe and preserves review independence, a separate review branch is optional; use the smallest mechanism that gives the reviewer immutable recoverable evidence.

## 8. Closure

Once required human/reviewer evidence is durably present:

Codex may, without another human Git approval:
1. record/transcribe the approved debrief;
2. validate;
3. create closure commit;
4. publish approved history to canonical main by normal fast-forward;
5. set STATUS CLOSED;
6. verify local/remote synchronization.

Stop if:
- evidence is ambiguous;
- frozen artifacts would change;
- main cannot fast-forward cleanly;
- scope exceeds approved evidence;
- publication would expose secrets/private data.

## 9. Minimal handoffs

Normal commands:

- **`Execute the active work packet.`**
- **`Prepare the active work for review.`** — only when review/human testing is actually prescribed.
- **`Record the approved decision.`** — when human/reviewer evidence must be transcribed.
- **`Continue the protocol.`** — perform all remaining Class R mechanics until the next genuine H/C boundary or CLOSED.

The old separate “publish review,” “publish closure,” and STATUS-correction approvals are retired for this repository.

## 10. Human-attention target

Target per normal experiment:
- **0 human Git/publication operations**
- **0 human interactions** for fully mechanical/research work unless judgment is prescribed
- **1 human judgment** for subjective acceptance
- **1 consequential authorization** immediately before external economic action

Additional human interruptions are protocol exceptions and should record why they were necessary.

## 11. Evidence integrity

Always preserve:
- frozen artifacts;
- original executor verdicts;
- independent review separately;
- remediation separately;
- final approved disposition;
- UNKNOWN/NOT REACHED semantics;
- unrelated working-tree changes.

Never rewrite history to make the final answer appear to have been known earlier.

## 12. Protocol-performance audit

For each experiment debrief, record only when nonzero:
- human operational interruptions;
- human judgment events;
- consequential authorizations;
- protocol exception reason.

Do not create a new telemetry system.

## 13. Boundary

No hooks, CI, workflow engine, scheduler, queue, database or orchestration layer is earned.

Use Git, concise Markdown and agent capabilities. Revisit automation only if this simplified protocol still causes repeated measurable friction.
