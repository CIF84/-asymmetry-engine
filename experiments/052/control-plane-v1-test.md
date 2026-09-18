# Experiment 052 — Human Attention Control Plane V1

## Evidence status

**IMPLEMENTATION FROZEN / HUMAN ACCEPTANCE PENDING**

No final A–D verdict is assigned before the independent behavioral acceptance exercise. Verdict E is not supported at implementation freeze because scope and integrity checks are designed to be completed before commit.

## 1. Provisional implementation status

Control Plane V1 is implemented as a bounded, reversible, dependency-free static viewer. It is ready for independent human acceptance but has not yet established attention compression, comprehension speed, lower reconstruction burden, or human acceptance.

## 2. Repository baseline

Execution began from synchronized `main` at `edc6ffb00ea336b2f9b301de49aa7c0f270e67ff`, which contains complete SPEC-052 and has Experiment 051 closed at `a4e71855ef9fabc7d74b979d330381f1b77fbbc7`.

## 3. Active time and timing method

Prospective implementation timing began at `2026-09-18T09:32:14Z` and froze after implementation, adversarial review, integrity checks, and tests at `2026-09-18T09:43:55Z`: **11 minutes 41 seconds** active elapsed. Human acceptance time is explicitly separate and remains unmeasured.

## 4. Spend

External spend: **€0**. Compute/model credit cost: **UNKNOWN** because the environment does not expose it.

## 5. Isolation confirmation

The work is repository-only. No external platform was inspected, no actor was contacted, and no fresh research or consequential action occurred. All new files are confined to `experiments/052/`.

## 6. V0 preservation result

Experiment 051 remains byte-for-byte unchanged. V1 reads the frozen `experiments/051/opportunities.js` fixture directly and adds no mutation path. Pre-implementation SHA-256 hashes were recorded for all six Experiment 051 files and are rechecked at freeze.

## 7. Historical opportunities/scenarios represented

All six frozen V0 opportunities remain represented:

- Czech cocoa purchasing and repricing aid (`013→014`);
- UK EV smart-charging compatibility (`019→020`);
- Canadian counter-tariff exposure brief (`023→027`);
- customized CRM stay / upgrade / migrate decision (`028→030`);
- Superset hierarchy sequencing decision (`032→035`);
- production `gpt-realtime-2.1` migration (`046→048`).

Their opportunity state, six-dimensional evidence, actors, beneficiaries, buyer/payer uncertainty, blockers, next discriminators, reactivation conditions, trajectory, provenance, and unproven claims are loaded from frozen V0 rather than restated as new truth.

## 8. Synthetic-control-scenario result

Four synthetic scenarios exercise states the historical telemetry cannot honestly supply: NEEDS DECISION, NEEDS AUTHORIZATION, PROGRESSING, and WAITING. Each is visibly striped, labeled `SYNTHETIC SCENARIO`, separated in the drill-down selector, and states that it is not AE history, a live task, a running process, or an authorization request.

## 9. Opportunity-state vocabulary

V1 preserves ACTIVE / DORMANT / REVIEW / TERMINAL exactly as opportunity-state concepts. Historical values come from V0. Synthetic values are scenario-only. Opportunity state is never mechanically converted into a control state.

## 10. Operational/control-state vocabulary

The implemented bounded vocabulary is NEEDS DECISION, NEEDS AUTHORIZATION, PROGRESSING, WAITING, BLOCKED / NO ACTION AVAILABLE, NO ACTION, and DORMANT. NEEDS REVIEW and READY were omitted because the test does not need them to distinguish its target states and adding them would create avoidable semantic overlap.

## 11. Needs-attention implementation

The top layer presents two synthetic attention items, one needing a decision and one needing explicit authorization. Each shows the item, attention type, reason, requested human action, consequence of doing nothing, and an auditable drill-down. No historical opportunity is claimed to need current action because frozen repository evidence cannot support that live operational assertion.

## 12. Progressing/no-action implementation

The safe/no-action group contains one synthetic PROGRESSING scenario plus two historical NO ACTION states. The synthetic item explicitly says no process is actually running. Historical NO ACTION preserves closed evidence horizons for the terminal EV thesis and the completed Superset actor-decision test; it does not mean low value, low significance, or live-world completion.

## 13. Waiting implementation

WAITING is exercised by one synthetic predeclared observation-window scenario. It says that time or external evidence—not current human action—is the dependency, and explicitly prohibits polling or follow-up within the scenario. No actual observation window is asserted.

## 14. Blocked/no-action implementation

The historical realtime-migration case is shown as BLOCKED / NO ACTION AVAILABLE because Experiment 048 closed with delivery unknown and no valid present action. This demonstrates that operational state can differ from its DORMANT opportunity lifecycle. The interface neither recommends retrying nor converts delivery ambiguity into behavioral failure.

## 15. Dormant/reactivation implementation

Cocoa, Canadian counter-tariff, and CRM appear in the Dormant/reactivation group with evidence-backed reactivation conditions. Realtime migration remains lifecycle DORMANT in detail but appears only once in the top layer under BLOCKED, avoiding duplicate cards while demonstrating orthogonal state concepts.

## 16. Why/explanation implementation

Every card exposes `Why`, `Human action`, and `If no action` before drill-down. Detail follows current opportunity state → current control state and reason → what could move it → categorical evidence → trajectory/provenance. The operator should not need to reconstruct the full experiment chain merely to understand why attention is or is not requested.

## 17. Consequence-of-inaction handling

Consequences are bounded to repository-supported persistence of state or synthetic scenario rules. They do not invent lost revenue, urgency, actor behavior, or external outcomes. Where history cannot establish a live consequence, the interface preserves unresolved evidence rather than claiming harm.

## 18. Six-dimensional evidence preservation

Historical drill-down renders Resolution / Access / Adoption / Control / Regulatory / Economic directly from frozen V0, with categorical labels and supporting evidence. UNKNOWN remains distinct from FAR and BLOCKED. No visual maps categories to invented numerical magnitudes. Synthetic scenarios make no six-dimensional historical claim.

## 19. Trajectory/auditability preservation

Every historical classification can drill down to immutable experiment history and linked provenance. The V0 trajectory is retained as a must-have layer rather than hidden by the control summary. Synthetic scenarios disclose that they have no historical trajectory.

## 20. Information-hierarchy result

The detail hierarchy is: current opportunity state; current control state and reason; what could move it/requested action/consequence; actor roles; six-dimensional evidence; known/unknown/blocker/next discriminator/reactivation/unproven claims; experiment trajectory; provenance. This is a testable hierarchy, not a production design claim.

## 21. Ranking/scoring non-introduction

No numeric score, urgency score, composite, automatic rank, or recommendation algorithm exists. Items are grouped by control requirement and retain stable fixture order. The viewer states explicitly that attention is not priority, NO ACTION is not low value, BLOCKED is not bad, and DORMANT is not dead.

## 22. Historical/synthetic separation

Historical and synthetic states use distinct badges, striped synthetic backgrounds, separate selector groups, explicit scenario warnings, and different detail content. Synthetic scenarios never inherit historical dimensions, provenance, actors, or experiment timelines and are excluded from claims about actual AE state.

## 23. Acceptance packet status

The packet is frozen and ready. All human answers remain `HUMAN ANSWER REQUIRED`; no acceptance result is fabricated. It tests top-layer comprehension first, then auditability, V0 preservation, synthetic/historical separation, and the intended human operating role.

## 24. Behavioral timing design

The operator starts a timer immediately before opening V1, answers questions 1–9, and stops once answers are formed. Detail views opened are counted. Questions 10–12 happen only afterward and do not contaminate primary timing. No arbitrary pass threshold is imposed; elapsed time and reconstruction burden are interpreted together.

## 25. Comparative V0 baseline status

Comparative timed V0 performance remains **UNKNOWN / NOT RUN**. Experiment 051 did not capture equivalent timing, and a fresh V0 retest would add operator burden and familiarity bias. No speedup or improvement ratio is claimed.

## 26. Human-operating-role representation

The top layer tries to delegate mechanical status reconstruction while exposing decisions, authorization, exceptions, and evidence-backed judgment. It does not grant autonomous consequential authority; the synthetic authorization case makes the human-authority boundary explicit.

## 27. Architecture boundary result

V1 is static HTML/CSS/JavaScript under the experiment directory. It has no backend, API, authentication, database, schema, monitoring, notification, agent, classifier, external call, deployment, persistence, or production model. Implementation convenience establishes no future architecture.

## 28. What implementation establishes

It establishes that the bounded control-plane concept can be represented without modifying V0, inventing live historical operational telemetry, scoring opportunities, weakening trajectory, or crossing the architecture boundary. It also establishes a testable behavioral acceptance surface.

## 29. What remains unproven

Human comprehension speed, correctness, reconstruction burden, auditability, synthetic/historical clarity, preservation of V0 knowledge visibility, and control benefit all remain unproven pending independent acceptance. Production scalability, automatic classification, monitoring, autonomy, architecture, economic value, and suitability for dozens of opportunities also remain unproven.

## 30. Exactly one recommended next action

Have the human operator complete the frozen acceptance packet once, measuring questions 1–9 separately from the auditability review, without changing V1 first.

Viewer path: `experiments/052/viewer/index.html`

Acceptance packet path: `experiments/052/acceptance-packet.md`

Artifact path: `experiments/052/control-plane-v1-test.md`

Integrity/test result: `PASS — git diff --check clean; 89 tests passed; all new files confined to experiments/052/; Experiment 051 SHA-256 hashes unchanged.`

Commit SHA: `PENDING LOCAL COMMIT`

## Adversarial review record

1. **Evidence-backed or invented?** Historical states are bounded to frozen repository evidence; invented coverage is synthetic and unmistakable.
2. **Does attention merely mean ACTIVE?** No. Both attention fixtures are synthetic ACTIVE scenarios, while the synthetic WAITING scenario is also ACTIVE and requests no human action. Historical REVIEW and TERMINAL items also request no current action.
3. **Are synthetic scenarios unmistakable?** Yes: stripes, badges, selector grouping, warning text, and absence of historical evidence panels.
4. **Waiting versus blocked?** Waiting has an expected external/time transition; blocked has no useful present action or guaranteed transition.
5. **Blocked versus dormant?** Blocked is an operational constraint; dormant is opportunity lifecycle. Realtime migration is lifecycle DORMANT and operationally BLOCKED.
6. **Authorization versus technical capability?** The authorization fixture asks for explicit authority only after hypothetical capability/control readiness; it states no real interaction exists.
7. **Does no action imply unimportant?** The interface explicitly denies that inference and retains significance in drill-down.
8. **Can consequential classifications be audited?** Historical states trace to dimensions, sources, and experiment events. Synthetic ones trace only to their disclosed scenario contract.
9. **Has trajectory weakened?** No. Full V0 experiment history and provenance remain available beneath the control layer.
10. **Hidden ranking?** None. Grouping reflects action requirement; within-group order is stable, not computed.
11. **Understandable without all details?** The top layer was designed for this, but only human acceptance can establish it.
12. **Dozens of opportunities?** Responsive card grids and grouped states suggest a plausible path, but scalability beyond these fixtures is untested.
