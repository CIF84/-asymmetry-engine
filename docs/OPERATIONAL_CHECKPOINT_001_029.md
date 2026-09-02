# Operational Checkpoint 001–029 — Pre-030 Operating Model Audit

## Purpose

This document freezes the operational interpretation of Asymmetry Engine after Specs 001–029 and **before Spec 030 introduces the first deliberately designed same-surface behavioral interaction**.

It is not the normative operating contract; that is recorded in `docs/OPERATING_MODEL.md`.

This checkpoint records **why the current operating model exists**, which operational patterns are supported by experience so far, which remain provisional, and what future experiments should be allowed to challenge.

Its purpose is to prevent hindsight from rewriting the operational history after new evidence arrives.

---

## 1. Audit question

> **If we reconstructed how Asymmetry Engine actually operated across Specs 001–029, which parts of the process created useful epistemic/economic value, which created accidental friction, and which repeated problems have earned codification or automation?**

The audit deliberately separated reconstruction from redesign.

Four dimensions were used:

```text
VALUE
Why does the step exist?

COST
What time, money, compute, attention, or latency does it consume?

CONTROL
What failure, risk, or authority boundary must be managed?

AUTOMATION
Should it remain manual, be simplified, codified, or automated?
```

A fifth discriminator was repeatedly useful:

> **What breaks if this step is removed?**

This helped distinguish protective friction from accidental friction.

---

## 2. The actual process contains three nested loops

The historical workflow is better described as three nested loops than as a single ChatGPT-to-Codex pipeline.

```text
┌────────────────────────────────────────────┐
│ STRATEGIC LOOP                             │
│ What are we learning about opportunities? │
│                                            │
│  ┌──────────────────────────────────────┐  │
│  │ EXPERIMENT LOOP                      │  │
│  │ What uncertainty matters next?       │  │
│  │                                      │  │
│  │  ┌────────────────────────────────┐  │  │
│  │  │ EXECUTION LOOP                 │  │  │
│  │  │ How do we obtain the evidence? │  │  │
│  │  └────────────────────────────────┘  │  │
│  └──────────────────────────────────────┘  │
└────────────────────────────────────────────┘
```

Observed role concentration before 030:

```text
STRATEGIC LOOP      human + ChatGPT
EXPERIMENT LOOP     ChatGPT + human
EXECUTION LOOP      Codex + tools + external world
PERSISTENCE         GitHub
AUTHORITY           human repository owner
```

This role separation emerged organically and has generally improved clarity.

---

## 3. ChatGPT / Codex / GitHub separation has been productive

The working division became:

```text
ChatGPT = THINK + SPECIFY + REVIEW
Codex   = EXECUTE
GitHub  = SHARED DURABLE STATE
```

This separation reduced implementation noise in strategic discussion and made experiment intent persistent outside the conversation.

No evidence through 029 demonstrates that collapsing ChatGPT and Codex into one continuous agent would improve economic or epistemic performance.

The separation may provide useful cognitive modularity by keeping experiment design/review partially independent from execution.

This is provisional rather than sacred. Future evidence may justify a different executor or orchestration mechanism.

---

## 4. Human role contains both valuable governance and accidental transport

Before 030, the human repository owner performs several distinct functions:

```text
PURPOSE
STRATEGIC CHALLENGE
AUTHORIZATION
GOVERNANCE
ROUTINE REVIEW
PROMPT TRANSPORT
COMPLETION NOTIFICATION
```

The audit found these should not be treated as one indivisible "human-in-the-loop" role.

### Currently high-value human functions

- defining the objective and meaning of FREEDOM;
- challenging strategic framing;
- deciding whether abstractions remain economically aligned;
- authorizing consequential external actions;
- resolving ambiguous objective/risk conflicts.

### Primarily mechanical human functions

- copying execution prompts;
- switching applications to initiate routine work;
- notifying ChatGPT that Codex finished;
- deterministic verification that software could eventually perform.

Provisional conclusion:

> **The target is not human removal. It is movement from routine operator toward governor.**

---

## 5. Productive disagreement is an independent error signal

Several strategic improvements occurred because the human challenged an apparently coherent AI interpretation.

The operational lesson is not that disagreement is valuable because it is human.

The stronger abstraction is:

> **Independent challenge is a necessary property of the epistemic loop. Human disagreement is currently the primary implementation.**

The risk is a self-consistent loop in which the same reasoning system:

```text
generates hypothesis
      ↓
designs experiment
      ↓
interprets evidence
      ↓
updates principles
      ↓
generates future hypotheses
```

Internal agreement in such a loop is weak evidence of correctness.

Reality remains the strongest critic, but external outcomes still require interpretation. Therefore some form of adversarial/independent interpretation remains useful even as human review declines.

### Current autonomy principle

Human review should not be removed globally when the AI "seems good enough."

It should be reduced **per decision class** when repeated evidence shows that human intervention has low marginal information value.

Potential future observation:

```text
human challenge occurred?
      ↓
conclusion changed?
      ↓
experiment changed?
      ↓
later evidence suggests correction was useful?
```

No multi-agent architecture has yet been earned from this observation alone.

---

## 6. Candidate generation is itself an experimental policy

Candidate generation evolved across multiple approaches:

```text
ASYMMETRY-FIRST
      ↓
BEHAVIOR-FIRST
      ↓
SIGNAL-NATIVE
      ↓
PRE-CONSOLIDATION
      ↓
ACCESSIBLE-SURFACE-FIRST
```

This means the project is not only testing opportunity hypotheses. It is testing **ways of finding opportunity hypotheses**.

Specs 021–028 demonstrated that candidate originality alone is insufficient. Signal-native candidates can still fail on recoverability, existing resolution, or intervention access.

Operational implication:

> More candidate generation is not automatically better RADAR. Candidate quality and cheap rejection policy must improve together.

Do not automate candidate volume without corresponding rejection/research policy.

---

## 7. Choosing the next uncertainty is core experimental intelligence

A major high-value activity currently occurs largely in discussion rather than code:

```text
CURRENT BELIEF STATE
        ↓
WHAT COULD MOST CHEAPLY CHANGE OUR DECISION?
        ↓
NEXT EXPERIMENT
```

This decision implicitly considers:

- economic relevance;
- expected information gain;
- falsification potential;
- cost;
- reversibility;
- experimental power;
- evidence availability;
- control feasibility.

This appears to be one of the most important emerging Engine capabilities and should not be prematurely automated into a rigid scoring function.

The system should eventually learn research policy, but the abstraction is still developing.

---

## 8. Specifications function as preregistration

Specs proved valuable beyond executor instruction.

They protect against:

```text
experiment starts
      ↓
interesting evidence appears
      ↓
scope expands
      ↓
hypothesis changes
      ↓
denominator changes
      ↓
result becomes difficult to interpret
```

The appliance keyword experiment was an important example of why the original denominator should not be expanded merely because adjacent evidence looks attractive.

Therefore the specification contract should be preserved.

However, the audit also found no reason to assume every experiment requires identical specification overhead.

Provisional principle:

> **Specification effort should be proportional to consequence, ambiguity, and irreversibility while preserving preregistration of the question and verdict logic.**

No rigid tier schema has yet been earned.

---

## 9. GitHub became the correct shared-state boundary

Moving specifications and artifacts into GitHub materially improved the workflow.

The repository now preserves distinctions among:

```text
SPEC
what we intended to test

RESULT / ARTIFACT
what happened

CHECKPOINT
what accumulated evidence currently means
```

This separation protects against hindsight rewriting and enables later comparison of prediction versus result.

The strategic checkpoint created before Spec 030 extended this logic by freezing cross-experiment beliefs before interaction evidence.

The operational audit identified one remaining weakness:

> Some important current operating/research-policy knowledge still lives disproportionately in conversation rather than the repository.

`OPERATING_MODEL.md` is the first deliberate correction.

---

## 10. Custom Codex prompts are increasingly transport protocol

As specs became more complete, execution prompts increasingly reduced to:

```text
sync main
read spec NNN
execute exactly as written
respect boundaries
return completion report
```

This indicates that semantic intent is successfully migrating into the repository contract.

The remaining prompt transport is mostly accidental friction.

However, automation is not yet economically justified because the current human cost is tiny relative to the infrastructure required to orchestrate execution automatically.

Current verdict:

> **Accept the friction until throughput makes it material.**

---

## 11. Authorization must not collapse into the execution prompt

Spec 030 exposed a critical distinction.

```text
SPECIFICATION
what may/should be done

EXECUTION
who/what does it

AUTHORIZATION
whether a consequential external action is permitted
```

The existence of a spec must never imply authorization.

Even if current interfaces cause execution instructions and authorization to appear in the same prompt, they remain different control objects.

This is likely to become increasingly important as the Engine gains autonomy.

---

## 12. Execution separation currently works

Codex has performed bounded research and implementation effectively when given explicit contracts, stop rules, and prohibitions.

The strongest operational pattern is:

```text
QUESTION / DECISION
      ↓
SPECIFICATION
      ↓
EXECUTION
      ↓
RESULT
      ↓
INDEPENDENT REVIEW
```

No evidence currently justifies making the executor the sole judge of its own result.

Executor replacement should remain possible; Codex is a current execution environment, not a permanent architectural dependency.

---

## 13. Controls exist but are distributed

By Spec 029 the project already used many controls, but not as one coherent system.

Observed controls include:

```text
SOURCE CONTROL
public access?
programmatic access?
retention / derivation?
commercial reuse?

EXPERIMENT CONTROL
scope?
stop rule?
budget?
cases?

INTERACTION CONTROL
public/private?
authorized?
number of contacts?
promotion prohibited?

EVIDENCE CONTROL
authoritative?
fresh?
known / public / estimated / unknown?
provenance?

ECONOMIC CONTROL
can this evidence still change the decision?

LEGAL / REGULATORY CONTROL
when encountered
```

Operational conclusion:

> Controls are empirically necessary but currently scattered and inconsistently invoked.

This is sufficient evidence to codify a conceptual control plane, but not sufficient evidence to build a generic policy engine.

---

## 14. Regulatory checks should be recursive

The audit introduced a first-class regulatory/control concern.

Publicly visible information is not automatically legitimate for programmatic ingestion, retention, derivation, outreach, or commercial exploitation.

Regulatory relevance changes as the Engine moves from passive research toward interaction, monetization, automation, and cross-jurisdiction operation.

A one-time compliance conclusion therefore decays.

Material changes in:

```text
source
jurisdiction
data use
interaction
product
monetization
autonomy
regulation / platform terms
```

may require re-evaluation.

Provisional invariant:

> **UNKNOWN must never silently become PASS.**

Repeated compliance reasoning should be codified and automated only after the underlying rule has repeated enough to be understood and mechanically useful.

---

## 15. Regulatory experimentability joins discovery and intervention experimentability

Earlier work distinguished:

```text
DISCOVERY EXPERIMENTABILITY
Can RADAR cheaply observe the evidence?

INTERVENTION EXPERIMENTABILITY
Can FORGE cheaply place the resolution into a real decision and observe effect?
```

The operational audit adds a provisional third dimension:

```text
REGULATORY EXPERIMENTABILITY
Can the experiment legitimately be performed at acceptable compliance cost and risk?
```

This matters economically because legal review, record keeping, licensing, consent management, liability, and jurisdiction complexity can create ongoing operational burden incompatible with FREEDOM even when an opportunity is otherwise attractive.

This concept is currently documented, not encoded.

---

## 16. Execution QA and epistemic QA are different

### Execution QA

Asks whether the executor complied with the experiment contract.

Many checks are deterministic and eventually automatable:

- artifact exists;
- required cases present;
- tests pass;
- budget respected;
- forbidden actions absent;
- required evidence included.

### Epistemic QA

Asks whether the experiment supports the conclusion.

This is where several major project lessons arose:

- zero responses do not establish zero demand when the experiment lacks power;
- a failed parser does not need repair when the missing measurement can no longer change the decision;
- a correct resolution does not establish opportunity when intervention access is weak.

Epistemic QA remains reasoning-heavy and should preserve independent challenge.

---

## 17. Checkpointing and punctuated formalization are operationally healthy

The project increasingly follows:

```text
RAW EVIDENCE
     ↓
EXPERIMENT RESULT
     ↓
LOCAL INTERPRETATION
     ↓
REPEATED PATTERN
     ↓
CHECKPOINT
     ↓
PRINCIPLE / ARCHITECTURE
```

Not every experiment needs a conceptual checkpoint.

The preferred rhythm is:

```text
EMPIRICAL RUNS
      ↓
ACCUMULATED PRESSURE
      ↓
CONSOLIDATION
      ↓
SELECTIVE FORMALIZATION
      ↓
MORE EMPIRICAL RUNS
```

This pattern protects against both endless bespoke research and premature infrastructure.

---

## 18. Operational telemetry is underdeveloped

Individual experiments increasingly record time, money, query counts, and qualitative yield, but not consistently enough to evaluate the operating system itself.

The audit concluded that lightweight documentation should begin now for:

- active research/execution time;
- elapsed time when relevant;
- money spent;
- paid tools used;
- candidate/case/source counts where meaningful;
- verdict;
- validity;
- yield;
- human authorization requirement;
- control escalation.

No telemetry database or dashboard is justified yet.

The eventual question is:

> **Is the Engine beginning to compound?**

Possible evidence includes lower time/cost to useful evidence, fewer repeated mistakes, better candidate/resolution quality, less routine human intervention, and more rapid movement toward behavioral/economic evidence.

---

## 19. Current classification of operational components

### Protect

- choosing the next important uncertainty;
- independent epistemic challenge;
- experiment preregistration;
- human governance;
- explicit consequential authorization.

### Keep

- GitHub shared durable state;
- spec/result/interpretation separation;
- ChatGPT/Codex separation while it continues to improve clarity and review independence.

### Simplify when evidence justifies it

- specification ceremony for cheap probes;
- repeated execution-prompt wording;
- checkpoint cadence.

### Future automation candidates

- deterministic execution QA;
- repeated exact-resolution functional comparison;
- repeated regulatory checks;
- mechanical notifications and handoffs;
- routine review for demonstrated-low-risk decision classes.

### Explicitly not earned yet

- orchestration engine;
- autonomous experiment scheduler;
- multi-agent critic architecture;
- regulatory rules database;
- generic policy engine;
- experiment database;
- opportunity scoring engine;
- governance UI;
- telemetry dashboard;
- agent permission service;
- autonomous outreach.

---

## 20. Target operating architecture

The audit converged on four layers:

```text
GOVERNANCE
why / objectives / authority / boundaries
        ↓
CONTROL PLANE
what may happen / what should be believed
        ↓
ECONOMIC PLANE
what should be tried / what happened
        ↓
WORLD
external evidence and consequences
        ↺
```

Research policy connects these layers by choosing the next observation based on current evidence, objectives, costs, and controls.

The economic plane should favor speed, experimentation, reversibility, and information gain.

The control plane should favor correctness, auditability, boundaries, independence, and escalation.

Governance remains external to the Engine even as AI increasingly assists it.

---

## 21. Desired human trajectory

The operational target is:

```text
TODAY
human = operator + reviewer + challenger + authorizer + governor

LATER
human = selective reviewer + challenger + authorizer + governor

TARGET
human = governor of objectives, boundaries, risk and exceptions
```

Routine disagreement should decline if the Engine learns.

Strategic disagreement may become less frequent but more consequential.

The mature system should not merely learn to agree with the human. It should learn to challenge its own hypotheses productively and expose disagreements to reality.

---

## 22. Pre-030 operational claims

Spec 030 and subsequent experiments may support, weaken, contradict, or leave untested the following operational claims.

### O1 — Repository-centered experiment contracts improve state continuity

Moving durable intent and results into GitHub reduces dependence on conversational memory and improves handoff clarity.

### O2 — Executor/reviewer separation improves epistemic quality

Independent review can detect validity and interpretation failures that executor self-assessment may miss.

### O3 — Explicit authorization should remain separate from experiment existence

A consequential external action should require explicit permission even when the experiment itself has already been specified.

### O4 — Same-surface interaction can reduce operational distribution friction

When discovery and intervention share a surface, the human/Engine may be able to obtain behavioral evidence with lower transport/acquisition overhead.

### O5 — Consequence-proportional specification can preserve preregistration without unnecessary ceremony

The value of experiment contracts does not imply identical documentation depth for every probe.

### O6 — Recursive controls are required as experiments move toward external interaction

Source/data/platform/regulatory/authorization assumptions can change as the experiment changes state and therefore should be re-evaluated when material conditions change.

### O7 — Human challenge currently has positive information value

Human disagreement has corrected or reframed important strategic interpretations, but this value should be measured rather than assumed permanent.

### O8 — The current manual handoff cost is below the threshold for orchestration investment

Copying a short execution instruction is inefficient but currently cheaper than building and maintaining orchestration infrastructure.

### O9 — Lightweight telemetry is sufficient for the current maturity level

Consistent experiment-level operational observations should provide enough evidence to decide later whether a formal telemetry capability is justified.

### O10 — The operating system can itself become a compounding capability

If later experiments reach economically relevant evidence faster, more cheaply, with fewer repeated errors and less routine human attention because of accumulated operating knowledge, the framework is functioning as productive infrastructure rather than research overhead.

---

## 23. What Spec 030 cannot establish operationally

One same-surface interaction cannot establish:

- that same-surface discovery/intervention generalizes across domains;
- that human review is no longer needed;
- that multi-agent challenge is useful;
- that the Engine should automate external interaction;
- that the control plane should become software;
- that regulatory checks can be safely automated;
- that GitHub contains all necessary durable project state;
- that the Engine is economically compounding;
- that CRM/software migration is the preferred opportunity class;
- that current role boundaries are permanent.

It can, however, reveal new operational friction at the transition from internal resolution to external interaction.

---

## 24. Post-030 back-check protocol

After Spec 030 reaches a valid result or a clearly invalid/unexecuted terminal state:

1. preserve the Spec 030 artifact/result without rewriting this checkpoint;
2. compare the result against operational claims O1–O10;
3. classify each relevant claim as `SUPPORTED`, `WEAKENED`, `CONTRADICTED`, or `STILL UNTESTED`;
4. identify unexpected operational friction or control requirements;
5. distinguish interaction/value failure from access/execution/control failure;
6. update the operating model only where new evidence warrants it;
7. decide the next highest-information action rather than automatically building infrastructure.

---

## 25. Pre-030 operational snapshot

The current preferred system is intentionally simple:

```text
PURPOSE / FREEDOM
       ↓
HUMAN GOVERNANCE
       ↓
CHATGPT REASONING
       ↓
BOUNDED EXPERIMENT SPEC
       ↓
CONTROL / AUTHORIZATION
       ↓
GITHUB SHARED STATE
       ↓
CODEX / EXECUTOR
       ↓
WORLD
       ↓
RESULT IN GITHUB
       ↓
INDEPENDENT REVIEW
       ↓
WHAT DID REALITY TEACH US?
       ↓
NEXT EXPERIMENT / LEARNING
       ↺
```

The directional target is not a larger software platform.

It is a **governed experimental economic system** in which routine operation becomes increasingly autonomous only as evidence demonstrates that the relevant reasoning, controls, and execution are mature enough to deserve automation.

---

## 26. Final pre-030 operating principle

> **Automate repeated work, codify repeated controls, preserve independent challenge, keep authority explicit, and let evidence determine when autonomy has been earned.**
