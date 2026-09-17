# Experiment 051 — Operator Acceptance Packet

## Purpose

This packet supports a later human acceptance test of **Static Control Plane V0**. It does not contain or imply operator answers. The test asks whether the opportunity-first UI makes repository-known state easier to comprehend than experiment-centric Markdown alone.

## Frozen evaluation surface

- Viewer: `experiments/051/viewer/index.html`
- Structured fixtures: `experiments/051/opportunities.js`
- Evidence horizon: historical repository evidence only, as stated per opportunity
- Ordering: chronological by first experiment, not ranked
- External data: none
- Automated inference, scoring, recommendation, or prioritization: none

Open the viewer directly in a local browser. It is self-contained and requires no server, authentication, network access, or build step.

## Evaluation protocol

1. Start a prospective timer.
2. Open only the viewer initially; do not reread the underlying historical artifacts yet.
3. Use the overview and detail surfaces to answer the six questions below.
4. Record confidence and any ambiguity.
5. Only after freezing the first-pass answers, use the evidence-provenance links to audit at least two answers against source artifacts.
6. Record material corrections, unsupported claims, or missing evidence.
7. Stop the timer and record total human review minutes.

The evaluator should not treat spatial order, color, `NEAR/MEDIUM/FAR`, or lifecycle as an automatic recommendation. Dimensions are independent; `UNKNOWN` is not `FAR`, and `BLOCKED` is not `TERMINAL`.

## Operator-comprehension questions

### 1. Economic discriminator

Which opportunity appears closest to a legitimate economic discriminator based on represented evidence?

- Answer:
- Evidence used:
- Confidence: Low / Medium / High
- Ambiguity or caveat:

### 2. Access blocker

Which opportunity is blocked primarily by access?

- Answer:
- Evidence used:
- Confidence: Low / Medium / High
- Ambiguity or caveat:

### 3. Decision effect versus economic distance

Which opportunity reached actor decision-state effect but remains economically distant?

- Answer:
- Evidence used:
- Confidence: Low / Medium / High
- Ambiguity or caveat:

### 4. Dormant versus terminal

Which opportunities are dormant rather than terminal, and what would reactivate each dormant opportunity?

- Answer:
- Evidence used:
- Confidence: Low / Medium / High
- Ambiguity or caveat:

### 5. Largest unknown or blocker

For each encoded opportunity, what is the largest `UNKNOWN` or blocker?

| Opportunity | Largest UNKNOWN or blocker | Confidence | Ambiguity |
|---|---|---|---|
| Cocoa |  |  |  |
| EV smart-charging |  |  |  |
| Canadian counter-tariff |  |  |  |
| Customized CRM |  |  |  |
| Superset hierarchy |  |  |  |
| Realtime migration |  |  |  |

### 6. Evidence provenance

Which experiments/evidence produced each current representation?

- Answer:
- Could provenance be reached from the UI without searching the repository? Yes / No
- Confidence: Low / Medium / High
- Missing or confusing link:

## Evidence-fidelity checklist

Mark each item after using the viewer.

- [ ] I could distinguish recorded historical disposition from derived current lifecycle.
- [ ] I could distinguish `DORMANT` contingent blockage from `TERMINAL` thesis invalidation.
- [ ] I could distinguish `UNKNOWN` from `FAR` and `BLOCKED`.
- [ ] I could see all six dimensions without a composite score or rank.
- [ ] I could distinguish decision actor, beneficiary, and buyer/payer.
- [ ] I could distinguish actor decision effect from downstream action, economic effect, and value capture.
- [ ] I could identify the next discriminator or understand why no continuation is claimed.
- [ ] I could identify the historical evidence horizon.
- [ ] I could navigate from each representation to its supporting repository artifacts.
- [ ] I did not read any fixture as a claim about current external reality.

## Acceptance record

- Accept / reject:
- Human review minutes:
- Material corrections required:
- Additional evidence required:
- Clarity assessment: Low / Medium / High
- Confidence assessment: Low / Medium / High
- Unsupported claim found:
- Lifecycle misclassification found:
- Dimension distortion found:
- Provenance defect found:
- Mobile readability: Pass / Fail / Not tested
- Desktop readability: Pass / Fail / Not tested
- Notes:

Human acceptance is intentionally not fabricated in Experiment 051. A later turn must supply the completed record.
