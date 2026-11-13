# Handoff — the review of the whole change `friction-at-source`

## Delegation

You review, as an agent that did not make it, the whole change of one the-way task cycle. The orchestrator of the cycle, to whom you
return, has the person who requested the cycle's delegation for intermediate choices; no human answers during the cycle. You change nothing.

## Where

- Worktree (read from its root; read-only for you): `the worktree's root`
- Range to review: `6814c6f6c9ff2b29d34612fa5cc86945ec3a2812..e51d835` (three commits on the branch `task/friction-at-source`;
  target branch `foundations`). `git diff 6814c6f..e51d835` is the whole change, 10 files.
- Report path (write your full report there): `docs/task-cycles/friction-at-source/reports/review-whole-change-report.md`
  The first line of the report is `PASS e51d835`, `FAIL e51d835` or `questions`.

## Method

Read `task-cycle/review/SKILL.md` in the worktree whole and follow it in its variant "the whole change"; read a file it names (such as
`whole_change.md`) when the step that names it comes. Where it names another skill of the-way, use the project skill with the `the-way-` prefix.

## What is reviewed

- The frozen task: `docs/task-cycles/friction-at-source/task.md` (Polish; read whole).
  Judge coverage of each of its three points of *To do*, each accepted row of *Settlements to record* (rows 1 to 4), each *Decisions in play*
  entry it changes or touches, and its *Out of scope*.
- The author's report: `docs/task-cycles/friction-at-source/reports/author-report.md`.
  The author is one agent that made the whole change without a plan; there is no spec, no plan and no slice, so there is no slice with a review of its own:
  you judge the whole range.
- The author's own concerns, for you to judge, not to take as settled: (a) the steps for the human in the item of kind 4 meet WAY-286's rule that the top
  part of a description holds no file names — the author wrote that the steps carry no file name or entry identifier and that the item ends with its
  pointer to the lower part; (b) WAY-354's *Rationale* says an identifier an entry could name exists only for a task of a project plan, reading WAY-329
  (a reading, not a quotation); (c) the rule about the task document stands in `project-level/task/template.md`, `draft.md` and `final_review.md`;
  (d) the glossary entry `transitional state`; (e) three commits, each with its own decision.
- The change is the foundation entries the task carries (rows 1 to 4: WAY-353, WAY-354, WAY-327 edited in place, the glossary term), written in the same
  change as the files they bear on. Judge them by their element's template and skill (`elements/decisions/`, `elements/glossary/`) and
  `foundations/` rules, as `review-change` gives.

## Answers of the cycle's start (step 4)

- Trust boundary: no. The review is not aimed at a trust boundary. Irreversible operation: no. Open design choice: none. Reserved choice: none.
- Process pin: not applicable (the-way itself). The part map's parts touched: `task-cycle`, `project-level`, `foundation-review`, `decisions`, `glossary`.
- Product guidelines: the-way has none.

## Reading

You select your own foundation by the parts of the change, as "Reading the foundation" in `elements/common/way_of_working.md` gives for the reviewer of the
whole change; state in the report how many decisions you read whole and how many by title only. The decisions the task names under *Decisions in play* are
in its text: WAY-327, 286, 287, 289, 290, 24, 302, 305, 36, 37, 01 (that the author read them whole is no reason for you not to).

## Boundaries

- Read-only: change no file of the worktree; run only checks that write nothing outside your report (the focused checks the change calls for are
  `python -B elements/common/foundation_check.py`, `python -B gate/run_tests.py task-cycle`, `python -B gate/run_tests.py project-level`; the orchestrator runs
  the whole gate, do not run it). Give each check you ran with its command and exit code.
- Grade each finding as `review-change` gives, say for each blocking finding which part of the change it comes from, and mark findings outside the task's scope.
- Your report holds **Unread material** and **Searches not found or unclear** (each `none` where there is nothing).
- Return, as `review-change` gives: the first line, the checks, the path of the report. Do not fix anything.
