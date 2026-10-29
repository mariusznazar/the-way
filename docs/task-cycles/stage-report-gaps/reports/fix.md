# Review-fix report

Status: done

## Commit and changed files

Commit: `ac88e27e10cae51d6994cfab3a05e54ab360fbca` — `Preserve accepted alternatives in WAY-260`

| File | Added | Removed |
|---|---:|---:|
| `foundations/decisions.md` | 4 | 2 |

## Blocking finding

**Fixed — “Preserve the rejected alternatives and their reasons from the accepted settlement.”**
In WAY-260's *Rejected* paragraph, I added the task's alternative of adding the rule to the
existing handoff decision, with its recorded cost: that decision is already long, a second purpose
would be added, and the reason for collecting gaps would point to a decision chiefly about
something else. I replaced the unsupported “temporary or conditional” clause with the task's
alternative of a condition for revisiting the scope, and the source's stated cost: a measure must
be settled and the decision must carry an obligation to check it. The existing rejected options
and their reasons remain unchanged.

## Checks

- `python -B elements/common/foundation_check.py` — exit code 0; `0 errors`.
- `git diff --check` — exit code 0.
- Not run: the whole product gate, as assigned to the orchestrator.
- Not run: Python tests; the fix only corrects decision prose.

## Own-work check

Weakest requirement: the new decision's *Rejected* field must retain the human's considered
alternatives and their reasons from the accepted task settlement, without adding alternatives or
reasons inferred by the author. I compared the final paragraph with the accepted settlement and
its *Questions to settle* answers in the frozen task, including the two alternatives called out in
the finding. It now retains both with their source costs and no unsupported claim about steady
evidence or reducing process cost. `foundation_check.py` also passed.

## Searches not found or unclear

None.

## Reaches, choices and concerns

- No reach beyond the dispatch; the task, finding, review and decision template were named inputs.
- No new choices or concerns. No invariant test changed.
- The return step and review of the fix remain for later stages.
