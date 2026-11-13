# Author fix report — defects-found-after-merge

## Status

`done`

## Commits

- `6d3298b` — fixes findings 1, 2 and 3 (on top of `10c0f9e`); files and lines added/removed:
  `foundations/decisions.md` 1/1, `project-level/task/skill/draft.md` 1/1,
  `project-level/task/template.md` 3/2, `task-cycle/skill/correction.md` 1/1. Nothing else touched.

## Findings of `reports/whole-change-findings.md`

1. Fixed. `draft.md` now reads "a document the refinement does not reopen keeps no line, and its
   missing line means that it was not assessed"; `template.md` reads "A task document written before
   this line has no line, and a missing line means that the task was not assessed, never `none`";
   WAY-354's last sentence reads "A task document written before the line has no line, and a missing
   line means that the task was not assessed, never `none`." The meaning (missing line = not assessed,
   never `none`) is unchanged in each. Check: `python -B elements/common/foundation_check.py
   --skip-test-citations .` exit 0 ("0 errors").
2. Fixed. `correction.md` reads "as in item 8 below" (item 8 is named in the paragraph that follows).
3. Fixed. In `template.md` the sentence "`TODO` marks a missing answer; never use it to make an
   unfinished task look ready." is on its own line again, as before the change.

Contested: none.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py --skip-test-citations .` — exit 0.
- `python -B gate/run_tests.py task-cycle` — exit 0 (367 tests OK).
- `python -B gate/run_tests.py project-level` — exit 0 (275 tests OK).
- `python -B gate/run_tests.py elements/common` — exit 0 (144 tests OK).
- Not run: `process-audit` and `agent-instructions` (no file of them changed in this fix) and the full
  gate (the orchestrator's).

## Own-work check

Requirement most likely not met: "the meaning of the fixed sentences stays intact, and nothing besides
the three findings changes". Check: `git diff HEAD~1 HEAD` shows four one- to three-line changes, each
a wording of the finding's sentence, and `git grep -n "has no line\|keeps no line"` (exit 0) finds `draft.md:27` and `template.md:112`
(WAY-354's sentence wraps after "has", so I read it at `foundations/decisions.md:11738-11739`); the foundation check and the three test directories above exit 0. Showed: the diff holds only
the findings' lines.

## Reaches beyond the handoff

none. (Read `task-cycle/change/fix.md` and the findings file.)

## Unread material

none. (Findings file, `fix.md`, the four files each as far as the lines changed, and the earlier author
handoff and report: read.)

## Searches not found or unclear

none
