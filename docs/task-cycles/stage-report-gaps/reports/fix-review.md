PASS ac88e27e10cae51d6994cfab3a05e54ab360fbca

# Review of the fix

Range: `e95be3b912c09ce1e6f00be167880431a3a26301..ac88e27e10cae51d6994cfab3a05e54ab360fbca`.
Blocking findings: 0; Minor: 0; out of scope: 0.

## Original finding

**Fixed — “Preserve the rejected alternatives and their reasons from the accepted settlement.”**

At `foundations/decisions.md:7434`, WAY-260 now includes the alternative of adding the rule to the existing handoff decision, with the task's reason that it would add a second purpose and put the gap-collection reasoning in a decision chiefly about another matter. At line 7436 it retains the actual rejected condition for revisiting scope, with the cost of settling a measure and recording an obligation to check it. The unsupported temporary-reporting alternative and claim about lacking a steady basis are gone. The other alternatives are unchanged. Comparison against the two Questions to settle answers cited in the original finding confirms that the failure no longer exists.

The finding was not contested. Its original grade and scope remain appropriate; the fix resolves it.

## New findings caused by the fix

None. The whole fix changes only the Rejected paragraph, preserves the binding rule and relation to WAY-148, and introduces no private link, new requirement or unrelated edit.

## Declined to judge

None.

## Checks

- `git rev-parse HEAD` — exit 0, `ac88e27e10cae51d6994cfab3a05e54ab360fbca`, exactly the dispatched head.
- `git log --oneline e95be3b912c09ce1e6f00be167880431a3a26301..ac88e27e10cae51d6994cfab3a05e54ab360fbca` — exit 0, one fix commit, `Preserve accepted alternatives in WAY-260`.
- `git diff e95be3b912c09ce1e6f00be167880431a3a26301..ac88e27e10cae51d6994cfab3a05e54ab360fbca` — exit 0, whole fix inspected.
- `git diff --check e95be3b912c09ce1e6f00be167880431a3a26301..ac88e27e10cae51d6994cfab3a05e54ab360fbca` — exit 0.
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- Manual source-fidelity check: compare both replacement alternatives with the frozen task's fourth and fifth Questions to settle answers and the accepted row, using the original review's quoted evidence. Both are faithful; the disputed addition is removed. Command and exit code: not applicable.
- Author's own-work check: its requirement and comparison method directly target the prior failure; independent comparison confirms its claimed result.

Not run: full product gate, assigned to the orchestrator; unrelated Python tests and the earlier extraction scratch run, because the fix changes only the decision's Rejected prose and leaves reporting/extraction instructions untouched. No invariant test changed. No UI, trust boundary or irreversible operation is involved. No cycle record was read and no product file was edited.

## Reaches beyond the dispatch

None. Used the retained whole-change review context, the frozen task and decision-template rule already read there, plus the fix handoff, fix method and author report.

## Searches not found or unclear

none
