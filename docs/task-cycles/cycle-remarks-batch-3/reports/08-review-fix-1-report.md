PASS c46a0c9666ed977304678a959e19f74c086510a2

# Review of the fix of finding 1, range 7841f0031df8f9dfa9db69efeab3f70efc2ddf97..c46a0c9

`git rev-parse HEAD` is `c46a0c9666ed977304678a959e19f74c086510a2`; `git log 7841f00..HEAD` shows the one commit. The fix changes only `foundations/decisions.md` (12 insertions, 9 deletions), WAY-298. The orchestrator chose that the entry follows the file and that step 4's sentence stays word for word; I judge the fix on that choice.

## Finding 1 (Important, blocking): fixed

- The defect was a difference between WAY-298 (restart without a condition for a correction) and `task-cycle/skill/correction.md:9` (restart "where something came in"). On the new head:
  - the correction sentence of WAY-298 reads "…merges the remote target branch into it, and, where something came in, starts again from the entry point" (`foundations/decisions.md:9035-9036`); the condition covers both ways of the correction (fast-forward in a copy, merge in the request's worktree), as `correction.md:8-10` has it ("In both cases, where something came in");
  - the Verification line "complies" says a correction restarts "where the merge brought something in" and one that "fetched and found nothing new goes on without starting again" (`:9049-9050`); the line "violates" names a correction that restarts when it found nothing new, "and so never ends" (`:9054-9056`);
  - the first sentence of the entry now follows step 4 (`task-cycle/skill/SKILL.md:116-120`): "it fetches and, where the checkout stands behind that branch, fast-forwards it …, and then starts again"; the restart there follows the fast-forward, which happens only where the checkout stands behind, so the ambiguity of step 4 is gone by structure and no longer in the entry.
- `grep -n "start again\|starts again" task-cycle/skill/*.md foundations/decisions.md`: `correction.md:9`, four places in WAY-298, `SKILL.md:116-120` (line break between "start" and "again") all say the restart follows something that came in. No place restarts unconditionally.
- The fix broke nothing: the diff touches the body and the Verification of the one entry; Scope, Based on, Relations, Origin, Rationale and Rejected are unchanged; the Rejected still holds the ways of the task's *Not chosen*. `foundation_check.py` is clean.

## Minor findings

- Minor — the entry's meaning now carries a condition that row 1 of the task's *Settlements to record* does not state (the row says the correction "zaczyna od nowa od punktu wejścia" without it). The fix report names it ("Adds a condition the task row does not state") and gives the reason (an unconditional restart never ends). The human accepts it at the merge (WAY-114), so the request's section for the human's decisions has to carry it; I have not seen that section.

## Declined to judge

- none new (those of report 04 stand).

## Checks I ran

- `git rev-parse HEAD` -> `c46a0c9666ed977304678a959e19f74c086510a2`; `git diff 7841f00..HEAD` read whole.
- `python -B elements/common/foundation_check.py` -> exit 0, `0 errors`.
- `python -B gate/run_tests.py elements/common` -> exit 0 (109 tests OK).
- `git status --short` -> empty; I changed no tracked file, index or branch.
- Not run: the full gate (the orchestrator's); `task-cycle` tests (the fix touches no file of that part; the author reports exit 0, 142 tests).

## Reaches beyond the dispatch

- `task-cycle/skill/correction.md:6-10` and `task-cycle/skill/SKILL.md:116-120` read again to compare the restart wording; `task-cycle/review/fix.md` as the method names it.

## Searches not found or unclear

- none
