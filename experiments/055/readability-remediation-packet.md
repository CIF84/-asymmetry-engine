# Experiment 055 — V2.1 Human-Language Remediation Packet

## Purpose
Remove the human-language confounder found in acceptance attempt 1, without changing Experiment 055's underlying Engine semantics or adding product features.

## Primary remediation hypothesis
If AE presents the same precise state in plain operator language first, with technical precision available on demand, the human operator can validly evaluate the original Engine-visibility hypothesis with materially lower translation burden.

## Frozen baseline
The original V2 implementation commit is `412a56f6befe776c7de9232ab9e313bc9abfdb30`.

Preserve that baseline. V2.1 must be a separately identifiable iteration under `experiments/055/`; do not erase the failed-language baseline or its evidence.

## Required work
1. Read SPEC-055, the frozen V2 implementation/report, and `human-acceptance-attempt-1.md`.
2. Inventory every visible primary-interface string.
3. Rewrite primary UI copy for an intelligent business operator who has not read the AE research history.
4. Apply **Plain English first. Precision on demand.**
5. Keep exact technical terminology available in secondary detail where useful for auditability.
6. Make headings answer human questions rather than expose internal ontology wherever possible.
7. Preserve all numerical values, denominators, horizons, UNKNOWN semantics, historical/prospective distinctions and provenance.
8. Preserve the four-layer hierarchy and accepted lower-layer functionality.
9. Freeze V2.1 and prepare the same behavioral acceptance test for another human attempt.

## Copy quality checks
For every primary label ask:
- Would a business operator understand this without reading AE specs?
- Does the label explain why the information matters?
- Is a technical noun being used where a short sentence/question would be clearer?
- Can the exact research term move to secondary detail without losing precision?
- Does simplification accidentally strengthen the evidence claim?

Do not use marketing language, anthropomorphic certainty, or casual simplification that erases UNKNOWN/missingness.

## Scope
Allowed changes:
- Experiment 055 viewer copy/layout needed to support readability;
- Experiment 055 explanatory/help text;
- V2.1 snapshot/copy if needed to preserve original V2;
- Experiment 055 acceptance packet only if wording must be made human-readable without changing questions;
- Experiment 055 report append/update describing remediation;
- mechanical STATUS transition.

Do not modify other experiments, specs, living/protocol docs, production code/tests/schema.

## No semantic redesign
Do not change:
- family/instance counts;
- lifecycle assignments;
- blocker classifications;
- evidence-frontier assertions;
- historical/prospective populations;
- current-attention UNKNOWN;
- prospective zero-state;
- accounting rules;
- synthetic/historical boundaries.

If a phrase cannot be simplified without changing meaning, retain the precise term but explain it plainly.

## Acceptance
Do not perform human acceptance.

After V2.1 freeze, human repeats the original cold-use Engine comprehension test. Record the second attempt separately; do not overwrite attempt 1.

## Integrity
Run existing tests, browser checks, semantic-value comparison against frozen V2, and `git diff --check`.

Commit remediation locally only. Do not push to main.

## Completion report
Return:
1. Remediation status
2. Baseline preserved
3. Active time
4. Files changed
5. Visible-copy inventory result
6. Major language transformations
7. Precision-on-demand implementation
8. Semantic-equivalence verification
9. Population/count preservation
10. UNKNOWN/missingness preservation
11. Four-layer preservation
12. Lower-layer preservation
13. Acceptance packet status
14. Integrity/test result
15. Commit SHA
16. Exactly one recommended next action
