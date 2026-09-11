# Spec 048 — Bounded Realtime Migration Evidence Request

## Status

READY FOR REVIEW — NOT AUTHORIZED FOR EXECUTION

## Type

Actor-facing INTERACT preregistration only.

This specification defines one bounded public evidence request to the fixed actor/channel identified in Experiments 046–047. It does **not** authorize posting, replying, reacting, messaging, tagging, private contact, benchmarking, implementation, FORGE work, or any other external action.

## Baseline

Execute specification review from synchronized `main` at or after:

`047437673ca24e5d4dba29a44b66299f83207ece`

The evidence boundary is:

- Experiment 046: one fresh HOLD candidate survived RADAR.
- Experiment 047: constructibility classified **P2 — ACTOR-HELD BUT BOUNDED**.
- FORGE has not been earned.
- The missing discriminator is not publicly constructible without invention.
- The missing evidence is narrow, plausibly pre-existing, and safely expressible as an anonymized aggregate.

## Target public decision channel

Native public surface:

OpenAI Developer Community thread concerning a production migration from the deprecated `gpt-realtime-2025-08-28` snapshot to `gpt-realtime-2.1`.

Fixed actor/channel:

The production owner/account that authored the migration thread and described the completed fixed-corpus qualification.

Authority scope:

`DIRECT` for the actor's own production migration and qualification evidence.

This does **not** imply:

- verified natural-person authorship;
- authority to speak for OpenAI;
- authority over OpenAI roadmap, deprecation policy, or model behavior generally;
- organizational authority beyond the actor's own migration decision.

Authorship provenance at preregistration:

`UNKNOWN`.

## Decision object

The live decision is whether and how the actor should proceed with migration away from the deprecated realtime model snapshot when the reported fixed-corpus qualification shows a major regression on the replacement model.

Spec 048 does not attempt to solve that migration.

It tests whether one bounded actor-held evidence package can classify the residual uncertainty well enough to determine whether FORGE is justified.

## Primary experimental question

Can one bounded public request elicit the minimum anonymized aggregate evidence needed to distinguish whether the actor's reported regression is plausibly localized to configuration / prompting / tool-contract / evaluation-contract factors versus remaining broad enough that a useful resolution cannot yet be constructed?

## Experimental hypothesis

If the actor supplies the preregistered aggregate evidence from the already-completed qualification, the candidate may become sufficiently resolved to decide whether a bounded FORGE experiment is justified.

The hypothesis is **not** that the actor will respond, that the migration can be solved, or that the replacement model is better or worse generally.

## What this interaction may establish

A valid response may establish some or all of:

- exposure to the intervention;
- semantic engagement with the requested evidence package;
- actor-reported qualification structure;
- the paired outcome distribution needed to classify the failure more narrowly;
- a decision-state refinement or stated next test;
- whether FORGE is justified or the candidate should be killed.

It may **not**, without additional evidence, establish:

- verified human cognition;
- causal model failure;
- model equivalence/non-equivalence generally;
- vendor roadmap commitments;
- successful migration;
- observed downstream deployment;
- economic effect;
- value capture;
- repeatability.

## Minimum evidence package requested

The interaction may ask for **one anonymized aggregate table from the actor's already-completed qualification only**.

The requested table should contain, where already available:

1. intent class / test category;
2. paired case count / denominator for the same fixed corpus;
3. legacy model pass count;
4. `gpt-realtime-2.1` pass count;
5. success rubric / pass criterion;
6. pre-existing acceptance threshold;
7. whether a tool call was required for the intent class;
8. target tool-call outcome counts where relevant:
   - correct required tool;
   - wrong tool;
   - no tool when required;
   - other existing aggregate outcome if already tracked;
9. reasoning-effort setting used for `gpt-realtime-2.1`;
10. tool-choice mode / relevant function-calling mode;
11. retry policy used in the qualification;
12. confirmation that prompts/instructions, tools/tool schemas, voice configuration, language, application path, and fixed corpus were held constant except for the model, to the extent that this is accurate.

Conditional fields may be requested only if already part of the actor's acceptance criterion:

- latency summary;
- session/audio conditions;
- language consistency;
- short sanitized aggregate failure notes.

## Explicitly prohibited evidence requests

Do not request:

- raw prompts;
- system prompts;
- tool schemas;
- function definitions;
- raw logs;
- transcripts;
- audio;
- customer data;
- personal data;
- production secrets;
- API keys or credentials;
- confidential architecture;
- proprietary code;
- full test corpus;
- vendor correspondence;
- confidential roadmap information;
- screenshots containing sensitive information;
- a new benchmark campaign;
- new experiments beyond summarizing already-existing results.

The interaction must make clear that anonymized aggregate results are sufficient and that confidential material should not be shared.

## Exact intended ask — semantic content

The public interaction should:

1. acknowledge that the actor appears to have already run the decisive fixed-corpus comparison;
2. explain that public aggregate figures are insufficient to distinguish broad model-behavior regression from a narrower configuration/prompt/tool-contract/evaluation-contract issue;
3. request only the minimum anonymized aggregate table listed above;
4. state explicitly that raw prompts, schemas, logs, transcripts, customer data, and confidential implementation details are not needed;
5. explain what the table would discriminate;
6. avoid giving migration advice before the discriminator exists;
7. invite correction if the decision has already moved or the framing is wrong.

## Draft public reply

The final execution draft may be edited only for factual freshness, platform formatting, or brevity while preserving the semantic contract below.

> It looks like you may already have the one comparison that could make this migration question much more tractable: the fixed-corpus qualification you ran with the application, instructions, tools, voice setup and language held constant while changing the model.
>
> The public 100% vs ~25% aggregate is enough to show a reported regression, but not enough to tell whether the failures are broad across the workload or concentrated in a smaller class such as required-tool use, reasoning/tool-choice configuration, prompting, or the evaluation contract.
>
> If you already have the results in aggregate form, would you be willing to share one anonymized table with roughly:
>
> `intent/test class | case count | legacy passes | 2.1 passes | tool required? | correct/wrong/no-tool counts (if relevant)`
>
> plus the pass rubric/acceptance threshold, `gpt-realtime-2.1` reasoning-effort setting, tool-choice mode, retry policy, and confirmation of which controls were held constant?
>
> Raw prompts, tool schemas, logs, transcripts, customer data or confidential implementation details are not needed.
>
> That should be enough to distinguish whether there is a bounded adaptation hypothesis worth testing versus a broader capability/roadmap dependency where more migration advice would just be guesswork. If the decision has already moved or I have framed the comparison incorrectly, that would also be useful to know.

## Interaction placement

`SAME` — one public reply on the existing native thread.

No adjacent or private route is authorized or justified.

## Authorization boundary

This specification is **not authorization**.

Execution requires a separate explicit user authorization after review of:

- the final draft;
- current surface state;
- current platform/community rules;
- actor/thread availability;
- the one-comment limit;
- any material new evidence that would close or invalidate the decision.

The executor must stop without posting if explicit execution authorization is absent.

## Pre-post freshness and control check

If execution is later authorized, immediately before posting perform only the bounded checks necessary to establish:

1. correct native thread and fixed actor/channel;
2. thread remains available and permits a normal public reply;
3. decision has not visibly closed or moved enough to invalidate the request;
4. no new public actor post already supplies the discriminator;
5. no adequate exact resolution has appeared that makes the request redundant;
6. the final reply contains no request for confidential/raw materials;
7. platform/community rules do not prohibit the intended interaction;
8. explicit user authorization is present;
9. one-comment limit is unused by Spec 048.

If any material condition fails, do not post. Record the failed control and classify the experiment accordingly.

## Interaction limits

If separately authorized:

- exactly one public top-level or contextually appropriate same-thread reply;
- no follow-up reply under Spec 048;
- no private message;
- no email;
- no tagging additional people;
- no reactions used to seek attention;
- no duplicate posting;
- no alternate identity;
- no automated repeated outreach;
- no cross-posting;
- no request to move to private channels;
- no offer of paid service;
- no promotion;
- no pricing test;
- no code contribution;
- no benchmark execution.

## Observation window

If separately authorized and published, use a **72-hour observation window** beginning at the verified publication timestamp.

During the open window:

- do not manually poll repeatedly;
- do not follow up;
- do not rescue silence through another channel;
- do not infer failure from no immediate response.

One final read-only observation is permitted at or after the deadline, unless independently surfaced evidence is explicitly recorded under a separate instruction without interaction.

## Hypothesis-relevant interaction evidence ledger

Track only the following states for this experiment.

### Surface access

Evidence that the native thread is available and accepts a normal reply.

### Intervention permission

Evidence that platform/community rules and explicit user authorization permit exactly one bounded public reply.

### Delivery

Verified publication of the intended reply on the intended thread.

### Exposure

`UNKNOWN` from publication alone.

Exposure may become supported if the fixed authoritative actor posts a substantive response that is logically dependent on the request.

Silence does not establish exposure.

### Semantic engagement

Observed only if the actor response materially engages the requested discriminator or corrects the framing.

Generic thanks, generic model commentary, third-party discussion, views, likes, reactions, or unrelated replies are insufficient.

### Account/channel identity

Record whether a qualifying response comes from the fixed actor/account or another participant.

### Decision authority/accountability

`DIRECT` for the fixed actor's own production migration evidence unless new evidence weakens that classification.

Do not generalize this to OpenAI roadmap or organizational authority.

### Authorship provenance

Use only:

- `HUMAN VERIFIED`
- `AI-ASSISTED DISCLOSED`
- `DELEGATED AGENT DISCLOSED`
- `AUTOMATED DISCLOSED`
- `UNKNOWN`

Default remains `UNKNOWN` absent explicit evidence.

Do not infer authorship from style.

### Decision-state refinement

Observed if the fixed actor supplies the paired evidence, materially narrows the failure class, corrects the migration framing, or states that the decision has moved/closed.

### Stated next action

Record separately if the actor states a concrete next test or migration action.

Do not treat a stated action as completed action.

### Observed downstream action

Not required to validate Spec 048's primary question.

Remain `UNKNOWN` unless directly observable within the authorized evidence boundary.

### Economic effect

Not tested. Remain `UNKNOWN`.

### Value capture

Not tested. Remain `UNKNOWN`.

## Synthetic-evidence contamination check

A semantically plausible response counts only if it is attributable to the fixed authoritative actor/channel and materially engages the requested workload evidence or decision framing.

Unknown authorship does not invalidate authoritative-channel evidence when the claim is limited to reported decision-state refinement.

Unknown authorship **does** prohibit claims of verified human cognition.

Third-party, generic, or unverifiable semantic chatter must not be counted as actor evidence.

No bot detection, style inference, or hidden-authorship classification is authorized.

## Qualifying response classes

A response from the fixed actor may be classified as one of:

### R1 — DISCRIMINATOR SUPPLIED

The response provides enough of the preregistered anonymized aggregate evidence to classify the failure more narrowly without invention.

Potential consequence: FORGE may be earned, subject to a separate specification.

### R2 — PARTIAL DISCRIMINATOR / ONE BOUNDED GAP

The response supplies material evidence but leaves exactly one small missing field or ambiguity that determines whether FORGE is possible.

Potential consequence: HOLD; no follow-up under Spec 048.

### R3 — FRAME CORRECTION / DECISION MOVED

The actor corrects a material premise, states the decision has moved/closed, or supplies evidence making the requested discriminator irrelevant.

Potential consequence: candidate may be killed or reclassified based on the evidence.

### R4 — BROAD CAPABILITY / ROADMAP DEPENDENCY CONFIRMED

The actor's evidence shows the failures remain broad enough that no bounded adaptation resolution is constructible from current evidence.

Potential consequence: kill on recoverability/resolution value unless a distinct cheap public discriminator emerges.

### R5 — SEMANTIC RESPONSE BUT NON-DISCRIMINATING

The actor responds substantively but does not supply or correct evidence that changes the decision state.

Potential consequence: exposure/semantic engagement may be observed, but FORGE remains unearned.

### R6 — NO QUALIFYING RESPONSE

No qualifying fixed-actor response is observable by the final observation.

This does not automatically mean attention failure, comprehension failure, or value failure.

If exposure is unestablished, silence remains measurement-limited.

## Third-party response handling

A response from another participant may be recorded for context but does not satisfy the primary actor-held discriminator unless:

- that participant demonstrates direct authority over the same production qualification; and
- the evidence itself is sufficient and attributable.

Do not silently replace the fixed actor with a more responsive participant.

## Decision logic after final observation

### ADVANCE TO FORGE REVIEW

Only if the fixed authoritative actor supplies enough bounded evidence to make a defensible resolution constructible without guessing.

FORGE still requires a separate specification.

### HOLD

If meaningful evidence arrives but one bounded discriminator remains.

No follow-up under Spec 048.

### KILL — DECISION CLOSED / MOVED

If the actor establishes that the decision is no longer live.

### KILL — RECOVERABILITY / RESOLUTION VALUE

If the response establishes that decisive evidence is unavailable, too broad, or insufficient for a useful bounded resolution.

### MEASUREMENT-LIMITED / NO QUALIFYING RESPONSE

If no qualifying actor response is observed and exposure remains unknown.

Do not convert silence into value failure.

## Success criteria

Spec 048 succeeds as an INTERACT experiment if it produces interpretable evidence about the actor-held discriminator while respecting all interaction and evidence boundaries.

Success does **not** require a response or FORGE advancement.

A valid measurement-limited no-response result is still informative about experimentability.

## Verdict taxonomy

### A — DISCRIMINATOR ACQUIRED / FORGE REVIEW EARNED

Enough bounded actor-held evidence is supplied to justify a separately specified FORGE review.

### B — MATERIAL REFINEMENT / HOLD

Substantive actor evidence materially narrows the candidate but one bounded gap remains.

### C — CANDIDATE KILLED BY ACTOR EVIDENCE

The response closes/moves the decision or demonstrates that a useful bounded resolution is not constructible.

### D — MEASUREMENT-LIMITED / NO QUALIFYING RESPONSE

The interaction is validly delivered but no qualifying response establishes the target discriminator. Silence must be interpreted according to exposure evidence.

### E — INVALID / NOT EXECUTED

Pre-post control, authorization, platform, scope, integrity, or execution requirements fail.

## Execution economics

If execution is later authorized, record prospectively where practicable:

- preparation/freshness-check active minutes;
- posting time;
- incremental spend;
- external interactions count;
- observation window;
- final observation active minutes;
- human authorization events;
- control escalations;
- evidence yield.

Do not represent unknown compute/model cost as zero.

## Repository artifact if execution is later authorized

Create/update only:

`experiments/048/bounded-realtime-migration-evidence-request.md`

The artifact should preserve:

- natural pre-intervention baseline;
- authorization record;
- pre-post control check;
- exact final draft;
- exact published text;
- publication verification;
- observation deadline;
- evidence-ledger states;
- final response classification;
- verdict;
- what is established;
- what remains unproven;
- operational telemetry;
- exactly one next action.

Do not modify Experiments 046 or 047.

## Current stop condition

This specification is complete when the public ask, evidence contract, authorization boundary, observation rules, ledger, response classes, and verdict logic are preregistered.

**STOP HERE. Do not execute the interaction without a separate explicit user authorization.**

## Required review report before authorization

A review/executor preparing this spec for execution should return:

1. Specification status
2. Repository baseline
3. Target decision/channel
4. Actor authority scope
5. Authorship-provenance state
6. Primary experimental question
7. Minimum evidence package
8. Prohibited evidence requests
9. Exact draft word count
10. Interaction placement
11. Authorization state
12. Pre-post checks required
13. Interaction limits
14. Observation window
15. Delivery evidence
16. Exposure logic
17. Semantic-engagement logic
18. Authority/authorship logic
19. Decision-state-effect logic
20. Synthetic-contamination logic
21. Qualifying response classes
22. Silence/no-response logic
23. FORGE advancement rule
24. Kill rules
25. Control-feasibility assessment
26. What remains unproven
27. Repository artifact path if later executed
28. Exactly one recommended next action
