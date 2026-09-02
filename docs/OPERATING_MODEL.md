# Asymmetry Engine Operating Model

## Purpose

This document defines the current normative operating model for Asymmetry Engine.

It is deliberately lighter than a software architecture. It records how the project should be governed and operated based on lessons accumulated through Specs 001–029, immediately before Spec 030 introduces the first deliberately designed same-surface behavioral interaction.

The model is directional. It should guide current work without causing premature implementation of orchestration, policy engines, multi-agent systems, regulatory databases, dashboards, or other infrastructure that has not yet earned its cost.

The core principle is:

> **Increase autonomy in economic experimentation without granting unrestricted authority, and formalize operational capability only when repeated evidence justifies it.**

---

## 1. Operating objective

Asymmetry Engine exists inside the broader flywheel:

```text
ATLAS
  ↓
RADAR
  ↓
FORGE
  ↓
PORTFOLIO
  ↓
FREEDOM
  ↘
   learning feeds ATLAS
```

The operating system should therefore optimize not only for immediate revenue, but for the ability to create a portfolio faster, more reliably, and with lower ongoing burden.

FREEDOM is increased by:

- recurring cash flow;
- automation;
- portfolio diversification;
- reusable infrastructure;
- accumulated knowledge;
- optionality.

FREEDOM is reduced by:

- maintenance burden;
- operational complexity;
- customer support;
- platform dependency;
- capital requirements;
- concentration risk.

A process improvement is valuable when it improves the expected economics of future experiments or portfolio assets enough to justify its implementation and maintenance cost.

---

## 2. Four-layer operating architecture

```text
┌─────────────────────────────────────────────┐
│                  GOVERNANCE                 │
│                                             │
│ purpose • FREEDOM • risk appetite           │
│ authority • irreversible boundaries         │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│                CONTROL PLANE                │
│                                             │
│ evidence • regulatory • permissions         │
│ resources • authorization • escalation      │
│ independent epistemic challenge             │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│                ECONOMIC PLANE               │
│                                             │
│ OBSERVE → RADAR → FORGE → INTERACT          │
│                    ↓                        │
│                  MEASURE → LEARN            │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│                    WORLD                    │
│                                             │
│ sources • markets • actors • competitors    │
│ behavior • transactions • regulation        │
└─────────────────────┬───────────────────────┘
                      │
                      └──────── feedback ─────↺
```

The layers have different jobs.

### Governance

Defines why the Engine operates, what it optimizes, which risks are acceptable, which boundaries are non-negotiable, and where human authority remains required.

### Control plane

Determines how the Engine may act and how much confidence should be placed in its conclusions.

### Economic plane

Discovers, falsifies, resolves, interacts, measures, and learns.

### World

Provides evidence that can contradict the Engine. External behavior and transactions outrank internal agreement.

---

## 3. Current roles

### Repository owner / human governor

The human role should increasingly be **governance rather than routine operation**.

Current responsibilities include:

- defining purpose and portfolio objectives;
- challenging strategic framing when useful;
- setting risk appetite and boundaries;
- authorizing consequential external actions;
- resolving objective conflicts and ambiguous exceptions;
- deciding whether the system remains aligned with FREEDOM.

Mechanical transport, notification, deterministic checking, and repeated routine review are not desirable long-term human responsibilities.

### ChatGPT — think, specify, review

Primary responsibilities:

- framing questions and hypotheses;
- research and strategic reasoning;
- choosing or recommending the next decision-relevant uncertainty;
- experiment design;
- writing experiment specifications into the repository;
- independent review of execution and evidence;
- interpreting what reality taught us;
- checkpointing accumulated learning;
- identifying when repeated learning may have earned formalization.

ChatGPT should generally not become the implementation environment merely because it can reason about implementation.

### Codex — execute

Primary responsibilities:

- read the repository and experiment contract;
- execute bounded research or implementation;
- respect scope, budgets, stop rules, prohibitions, and authorization boundaries;
- test and debug implementation where relevant;
- persist artifacts/results and commits;
- report execution facts without expanding the experiment.

Codex is an execution adapter, not part of the economic ontology. Future executors may include scripts, APIs, browsers, specialized models, or other agents.

### GitHub — durable shared state

The repository is the authoritative shared memory for durable project state.

It should increasingly make the project reconstructible without dependence on a particular conversation.

```text
README
  → what is this?

ARCHITECTURE
  → how is the implemented system structured?

OPERATING_MODEL
  → how do we operate it?

ROADMAP
  → where are we going?

CHECKPOINTS
  → what have we learned?

SPECS
  → what did we decide to test?

EXPERIMENTS
  → what actually happened?
```

---

## 4. Research policy

The Engine should not operate from a fixed task roadmap when evidence can determine the next experiment.

The central research-policy question is:

> **Given the current belief state, what is the cheapest next observation capable of materially changing what we should do?**

Conceptually:

```text
CURRENT BELIEF STATE
        ↓
UNRESOLVED UNCERTAINTIES
        ↓
POSSIBLE EXPERIMENTS
        ↓
consider:
- decision relevance
- information potential
- falsification power
- cost
- reversibility
- experimentability
- control feasibility
        ↓
INDEPENDENT CHALLENGE
        ↓
NEXT EXPERIMENT
```

Research policy is neither purely economic execution nor purely control. It connects current evidence, objectives, constraints, and the choice of the next observation.

The Engine should minimize the expected resources required to discover economically relevant truth while preserving genuine survivors. Optimizing only for rapid rejection would create false-negative risk.

---

## 5. Economic experiment lifecycle

The current preferred lifecycle is:

```text
OBSERVATION
    ↓
ACTOR
    ↓
CHANGEABLE DECISION
    ↓
ECONOMIC CONSEQUENCE
    ↓
MATERIAL UNCERTAINTY
    ↓
RECOVERABLE INFORMATION
    ↓
INADEQUATE EXISTING RESOLUTION
    ↓
DISPOSABLE RESOLUTION
    ↓
ACCESSIBLE INTERVENTION
    ↓
OBSERVED DECISION EFFECT
    ↓
VALUE CREATED
    ↓
VALUE CAPTURED
    ↓
REPEATABILITY
    ↓
LEARNING
```

Not every candidate will traverse every state. Cheap rejection is desirable when a necessary condition fails.

As evidence accumulates, however, the burden of proof should shift. Early candidates must justify investigation; survivors should increasingly be allowed the cheapest real experiment unless there is a specific reason not to run it.

---

## 6. Experiment contracts and proportional preregistration

A specification is not merely an instruction to an executor. It is an experimental preregistration mechanism that preserves the distinction between what was intended before evidence and what was concluded afterward.

Specification effort should be proportional to consequence, ambiguity, and irreversibility.

A cheap reversible probe may require only:

```text
QUESTION
METHOD
STOP
RESULT
```

A bounded experiment should normally make explicit:

```text
QUESTION
HYPOTHESIS
BOUNDARY
METHOD
EVIDENCE
STOP RULE
VERDICT LOGIC
```

A consequential external experiment should additionally make explicit:

```text
CONTROLS
AUTHORIZATION REQUIREMENTS
PROHIBITED ACTIONS
REGULATORY / PLATFORM CONSIDERATIONS
```

The exact schema should remain flexible until repeated use earns stronger formalization.

Once execution begins, a spec is a historical contract. Material changes should be recorded through a new spec or explicit revision rather than silently rewriting original intent.

---

## 7. Authorization is separate from execution

Three objects must remain conceptually distinct:

```text
SPECIFICATION
what should happen

EXECUTION
who or what performs it

AUTHORIZATION
whether a consequential action may happen
```

The existence of a specification never implies permission for consequential external action.

Explicit authorization is currently required for actions such as:

- contacting or messaging a real person where not already authorized;
- publishing or posting externally;
- spending beyond an agreed experiment budget;
- accepting contractual commitments;
- taking payment where commercial/legal status has not already been cleared;
- using sensitive or materially different data;
- other irreversible or materially consequential actions.

As the Engine matures, classes of low-risk actions may receive standing policy authorization. Expansion of autonomy should be earned per action/decision class, not granted globally because the system appears capable.

---

## 8. Control plane

Every material proposed action should be considered against relevant controls before execution.

```text
PROPOSED ACTION
       │
       ├── EVIDENCE CONTROL
       ├── SOURCE / DATA CONTROL
       ├── REGULATORY / LEGAL CONTROL
       ├── PLATFORM CONTROL
       ├── RESOURCE CONTROL
       ├── AUTHORITY CONTROL
       └── EPISTEMIC CONTROL
                ↓
          DISPOSITION

PASS
CONDITIONAL
REVIEW REQUIRED
BLOCK
```

Not every trivial internal action requires a ceremonial checklist. Controls should be applied proportionally to risk and consequence.

### Core invariant

> **UNKNOWN must never silently become PASS.**

Uncertainty can be accepted explicitly when immaterial, investigated when decision-sensitive, escalated when outside current competence, or used to block an action when necessary.

---

## 9. Evidence control

Important questions include:

- What is the source of this claim?
- Is the source authoritative enough for the consequence?
- How fresh is the evidence?
- What is observed versus inferred?
- Which evidence belongs to the actor/case versus a public external source?
- Which quantities are estimated?
- What remains unknown?
- Could missing information change the decision?

The current reusable evidence classes are:

```text
KNOWN
actor / case facts

PUBLIC FACT
authoritative external evidence

ESTIMATED
modeled range or explicit assumption

UNKNOWN / VERIFY
decision-sensitive missing information
```

Provenance and freshness should strengthen as consequence increases.

---

## 10. Regulatory and operational control

Public visibility does not imply unrestricted ingestion, retention, derivation, contact, or commercial exploitation.

Potential control dimensions include:

- legitimate source access;
- programmatic-access conditions;
- data retention and derivation rights;
- commercial reuse;
- privacy and personal data;
- intellectual property and licensing;
- platform terms and automation rules;
- communication and outreach rules;
- consumer protection and claims;
- regulated financial, legal, medical, or other advice;
- commercial operating status;
- tax/accounting obligations;
- jurisdiction;
- AI-specific obligations where applicable.

The Engine is not assumed competent to resolve novel legal ambiguity autonomously. Novel or material ambiguity should produce `REVIEW REQUIRED`, not a guessed compliance conclusion.

### Recursive regulatory check

A compliance/control conclusion is not permanent.

Material changes can invalidate it, including:

```text
source changed
jurisdiction changed
data use changed
interaction changed
product changed
monetization changed
autonomy changed
regulation / platform terms changed
```

When such a change could alter prior assumptions, the relevant control must be re-evaluated.

Repeated regulatory reasoning may later become structured policy or policy-as-code. Automation should follow repeated, sufficiently understood rules rather than imagined future requirements.

---

## 11. Resource control

Experiments consume more than money.

Relevant resources include:

```text
TIME
MONEY
COMPUTE / TOOL ALLOWANCE
HUMAN ATTENTION
OPPORTUNITY COST
```

Budgets and stop rules should be chosen according to the expected value of decision-relevant evidence.

A failed measurement should be repaired only when the missing evidence can still change the current decision.

The dominant economic objective remains **time to economically relevant evidence**, not research completeness.

---

## 12. Independent epistemic challenge

Internal consistency is not sufficient evidence of correctness.

A system that generates hypotheses, designs experiments, interprets evidence, and updates its own policies can become self-consistent while systematically wrong.

Therefore:

> **Independent challenge is a required property of the epistemic loop. Human disagreement is currently one implementation of it, not the permanent abstraction.**

The conceptual target is:

```text
HYPOTHESIS
    │
 ┌──┴───┐
 ▼      ▼
SUPPORT ATTACK
 │      │
 └──┬───┘
    ▼
WHAT OBSERVATION WOULD DISCRIMINATE?
    ↓
WORLD
    ↓
EVIDENCE
```

For now, executor output should receive independent review rather than relying only on executor self-assessment.

Do not build a multi-agent critic architecture merely because this requirement exists. First observe whether independent challenge repeatedly changes decisions and whether later evidence shows those corrections were useful.

Human review should eventually be reduced **per decision class** when its marginal information value becomes consistently low.

---

## 13. Execution QA versus epistemic QA

These are different activities.

### Execution QA

Checks whether the experiment contract was followed:

- required artifacts exist;
- required cases were evaluated;
- tests pass;
- budgets and stop rules were respected;
- prohibited actions were not taken;
- required sources or evidence classes are present.

Much of this may eventually be automated.

### Epistemic QA

Asks whether the evidence actually supports the conclusion:

- was the experiment capable of observing the target behavior?
- does the denominator match the hypothesis?
- are alternative explanations plausible?
- did scope drift change what was tested?
- does missing evidence still matter?
- what does the result establish and not establish?

Epistemic QA should preserve independent challenge even if execution QA becomes mechanical.

---

## 14. Result and learning separation

Maintain the distinction:

```text
SPEC
what we intended to test

RESULT / EXPERIMENT ARTIFACT
what happened

CHECKPOINT
what accumulated evidence currently means

PRINCIPLE / ARCHITECTURE
what repeated learning has earned promotion
```

This separation reduces hindsight rewriting and makes later back-checking possible.

The preferred rhythm is punctuated formalization:

```text
EMPIRICAL RUNS
      ↓
REPEATED PRESSURE
      ↓
CHECKPOINT / CONSOLIDATION
      ↓
SELECTIVE FORMALIZATION
      ↓
MORE EMPIRICAL RUNS
```

---

## 15. Operational telemetry

The Engine should begin recording lightweight operational telemetry consistently without building a telemetry system.

Where relevant, experiment completion reports should record:

- active research/execution time;
- elapsed time when materially different;
- money spent;
- paid tools used;
- cases/candidates/sources examined where useful;
- verdict;
- experiment validity;
- evidence/research yield (`LOW`, `MEDIUM`, `HIGH`) when meaningful;
- human authorization required (`YES` / `NO`);
- control escalation (`YES` / `NO`, with reason if yes).

The purpose is to make future comparison possible, not to optimize vanity metrics.

Evidence that the Engine is compounding would include trends such as:

```text
time to useful evidence ↓
cost to rejection ↓
repeated mistakes ↓
human intervention for routine decisions ↓
candidate quality ↑
resolution quality ↑
behavioral evidence ↑
economic evidence ↑
```

---

## 16. Automation maturity

Operational automation should follow the same maturity ladder as economic capability:

```text
OBSERVATION
    ↓
REPEATED OBSERVATION
    ↓
PROVISIONAL PRINCIPLE
    ↓
REPLICATED PRINCIPLE
    ↓
FORMAL MODEL
    ↓
IMPLEMENTED CAPABILITY
    ↓
AUTOMATED CAPABILITY
```

Before implementing a target capability, ask:

```text
Repeated observed problem?
        │
     NO ──→ DOCUMENT
        │ YES
        ▼
Mechanically reusable?
        │
     NO ──→ KEEP MANUAL
        │ YES
        ▼
Likely to improve future experiment economics?
        │
     NO ──→ DEFER
        │ YES
        ▼
Small reversible implementation?
        │
     NO ──→ WAIT
        │ YES
        ▼
IMPLEMENT
    ↓
MEASURE
```

---

## 17. Current automation posture

### Protect

- choosing the next important uncertainty;
- independent epistemic challenge;
- experiment preregistration;
- human governance and consequential authorization.

### Keep

- GitHub as shared durable state;
- separation of spec, result, and interpretation;
- ChatGPT/Codex cognitive separation while it continues to improve clarity and independence.

### Simplify when useful

- specification ceremony for low-consequence probes;
- repeated handoff wording;
- checkpoint cadence.

### Strong future automation candidates

- deterministic execution-contract QA;
- repeated exact-resolution/functional-competition checks once the abstraction stabilizes;
- repeated regulatory checks once rules are sufficiently understood;
- notifications and mechanical handoffs when throughput makes them material;
- routine review for decision classes where human correction value becomes demonstrably low.

### Do not build yet

- orchestration engine;
- autonomous experiment scheduler;
- multi-agent critic architecture;
- generic regulatory rules database;
- generic policy engine;
- experiment database;
- opportunity scoring engine;
- governance UI;
- telemetry dashboard;
- agent permission service;
- autonomous outreach.

These remain possible future capabilities, not current requirements.

---

## 18. Target human experience

The long-term objective is not to remove the human from the system. It is to remove the human from low-value operation.

Desired progression:

```text
TODAY
human performs transport + review + challenge + authorization + governance

LATER
Engine performs routine work + routine evaluation
human handles authorization + exceptions + strategic challenge

TARGET
Engine operates inside demonstrated policies
human governs objectives, boundaries, risk and exceptional decisions
```

Autonomy should expand by demonstrated competence and bounded policy, not by confidence or convenience.

The human should eventually be the Engine's governor rather than its message bus.

---

## 19. Reconstructability test

A useful operational invariant is:

> **Could a competent fresh reasoning/execution environment reconstruct how to operate Asymmetry Engine correctly from the repository?**

If not, important durable state is still trapped in conversations or operator memory.

The repository should be improved selectively when reconstruction failures reveal missing state. Do not duplicate every conversation merely to make the repository exhaustive.

---

## 20. Current operating loop

Until further evidence earns deeper automation, the preferred practical loop remains intentionally simple:

```text
QUESTION
    ↓
ChatGPT + human reasoning / research
    ↓
DECISION
    ↓
ChatGPT writes bounded spec to GitHub
    ↓
explicit human authorization if required
    ↓
Codex / appropriate executor executes
    ↓
result + artifact persisted to GitHub
    ↓
independent ChatGPT + human review
    ↓
WHAT DID REALITY TEACH US?
    ↓
CONTINUE / NARROW / PIVOT / PARK / KILL
    ↓
checkpoint / formalization only when earned
    ↓
NEXT DECISION
```

This manual loop is not considered a failure of automation. It is the current cheapest representation capable of producing high-quality economic evidence while the operating policy itself is still learning.

---

## 21. Current operating principle

> **Automate repeated work, codify repeated controls, preserve independent challenge, keep authority explicit, and let evidence determine when autonomy has been earned.**
