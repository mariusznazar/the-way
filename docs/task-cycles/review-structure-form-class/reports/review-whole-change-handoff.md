# Handoff — the review of the whole change `review-structure-form-class`

## Delegation

You review, as an agent that did not make it, the whole change of one the-way task cycle. The orchestrator of the cycle, to whom you
return, has the person who requested the cycle's delegation for intermediate choices; no human answers during the cycle. You change nothing.

## Where

- Worktree (read from its root; read-only for you): `the worktree's root`
- Range to review: `65b6d7007ec4fffad998612e5c521eee93c7b8b5..5353268` (four commits on the branch `task/review-structure-form-class`;
  target branch `foundations`). `git diff 65b6d70..5353268` is the whole change, 14 files, 881 lines added, 15 removed.
- Report path (write your full report there): `docs/task-cycles/review-structure-form-class/reports/review-whole-change-report.md`
  The first line of the report is `PASS 5353268`, `FAIL 5353268` or `questions`.

## Method

Read `task-cycle/review/SKILL.md` in the worktree whole and follow it in its variant "the whole change"; read a file it names (such as
`whole_change.md`) when the step that names it comes. Where it names another skill of the-way, use the project skill with the `the-way-` prefix.
Note: the change itself edits `task-cycle/review/SKILL.md` and `whole_change.md`. Review with the version of the base (`git show 65b6d70:<path>`)
as your instructions, and judge the head's version as part of the change.

## What is reviewed

- The frozen task: `docs/task-cycles/review-structure-form-class/task.md` (Polish; read whole). Judge coverage of each of its eight items of
  *To do*, each accepted row of *Settlements to record* (rows 1 to 6), each entry of *Decisions in play* it changes or touches (WAY-229 and WAY-164
  are changed in place, binding sentences unchanged; the others are left unchanged), the answers of its *Questions to settle* (1–7) with their
  *Not chosen*, and its *Out of scope*.
- The author's report: `docs/task-cycles/review-structure-form-class/reports/author-report.md`. There is no spec, no plan and no slice, so no
  slice has a review of its own: you judge the whole range.
- The author's own concerns, for you to judge, not to take as settled: (a) rows 1–6 became six entries, WAY-355 to WAY-360, numbered in the order of
  the commits; (b) "the first commit" of the author without a plan is read as the first commit that changes the code (task item 5, question 6);
  (c) WAY-358 says "below the threshold" for every finding of structure, also one with no size (code with no user, a name no longer true), and says
  nothing for a product with no rule of size; (d) the paragraph the author added to `whole_change.md` that the reviewer takes the "violated" mark
  off the size test in its own separate worktree — not in the task; (e) five files of `product-guidelines/coding/` beyond `template.md` and `settle.md`
  changed so that a refresh and a hand back notice the rule; (f) WAY-359's *Scope*; (g) the new script's command line (`change_file_sizes.py BASE HEAD
  [--root DIR]`), its use of git with argument lists only, and whether its tests would fail if it broke (the author broke it six ways); (h) the numbers
  and conditions of WAY-229 and WAY-164 against item 7 and 8 of the task, word for word.
- The cycle's own choices (autonomous, recorded): the reviewer runs the new script (not the orchestrator); the author's class is `same`; the position of
  the rule in the template and the wording of its invariant were left to the author. Judge them as any other part of the change.
- The foundation entries the change writes are WAY-355 to WAY-360 and the edits of WAY-229 and WAY-164. Judge them by their element's template and
  skill (`elements/decisions/`) and `foundations/` rules, as `review-change` gives; WAY-263 and WAY-297 grade their mismatches.
- Where the change writes or changes a product's guidelines (`product-guidelines/coding/`), compare them with `product-guidelines/template.md`
  and `product-guidelines/coding/template.md` as section 2 of the skill says.

## Answers of the cycle's start (step 4)

- Trust boundary: no. The review is not aimed at a trust boundary; still try the new script with file names with a space and with non-ASCII letters,
  a renamed file, a binary file and a submodule, in a scratch repository outside the worktree. Irreversible operation: no.
  Open design choice: none. Reserved choice: none.
- Process pin: not applicable (the-way itself). The parts touched: `task-cycle`, `product-guidelines`, `decisions`.
- Product guidelines: the-way has none and departs from them (WAY-328).

## Reading

You select your own foundation by the parts of the change, as "Reading the foundation" in `elements/common/way_of_working.md` gives for the reviewer
of the whole change; state in the report how many decisions you read whole and how many by title only. Read each invariant of the parts touched, or
naming `every`, whole: the author read twelve of them by heading and part only (list in its report, **Unread material**), and `product-guidelines/reading.md`
beyond its first 60 lines — judge whether either bears on the change. The decisions of the task's *Decisions in play* are in its text.

## Boundaries

- Read-only: change no file of the worktree; run only checks that write nothing outside your report (in a separate worktree or a scratch directory for
  anything that needs files changed). The focused checks the change calls for are `python -B elements/common/foundation_check.py`,
  `python -B gate/run_tests.py task-cycle`, `python -B gate/run_tests.py instruction-files` and `python -B gate/run_tests.py agent-instructions`; the
  orchestrator runs the whole gate, do not run it. Give each check you ran with its command and exit code. Run the new script on this very range
  (`python -B task-cycle/change_file_sizes.py 65b6d70 5353268`) and compare its table with `git diff --stat`.
- Grade each finding as `review-change` gives, mark findings outside the task's scope, and list each Minor finding with its place and its own words.
  Say for each blocking finding which part of the change it comes from (here: the one author, so no slice).
- Your report holds **Unread material** (with the counts of decisions read whole and by title only) and **Searches not found or unclear**
  (each `none` where there is nothing).
- Return, as `review-change` gives: the first line, the counts of blocking, Minor and out-of-scope findings, a one-line check result and the path of
  the report. Do not fix anything.
