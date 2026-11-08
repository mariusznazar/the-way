# Handoff — review of the whole change (`review-change`)

You are the reviewer of the whole change. You did not make it. You are read-only: you change no
file and make no commit. Work from the root of the worktree
`.`.

## Delegation

The human who requested this cycle delegated intermediate choices to the orchestrator; the cycle
has no human contact before the request. Ask the human nothing. A question for the orchestrator
is a question of section 4 of your method.

## Method

The project skill `review-change`: read
`task-cycle/review/SKILL.md` whole,
then `task-cycle/review/whole_change.md` whole, as the skill says for the review of the whole
change. Any other file the method names, only when the step that names it comes. You select your
own foundation entries and guidelines yourself (WAY-150, WAY-213). The repository has no
`guidelines/` of its own to read (the task, question 4).

## What is reviewed

- The whole change, on the one-author route (no plan, no slices, no spec).
- Range: base `05534d381b95a4e2692875263dd0d8875097b89d` to head
  `e66e8e790b370f1f04baf8cc73a6f9913cef2fe2` (`git diff 05534d3..e66e8e7`, `git log 05534d3..e66e8e7`;
  two commits, 21 files).
- Frozen task, read in full:
  `docs/task-cycles/guidelines-skills-batch/task.md`
  (20 items of *To do*, 4 answered questions, 5 rows of *Settlements to record*). Check every
  item and every settlement row against the change, and the source fidelity of the text the
  change adds: a rule, a case or a number that no item, decision or settled answer gives is an
  addition the task did not ask for. Line numbers in the task are of an older state; places are
  found by content.
- The author's report (claims to verify, not evidence):
  `docs/task-cycles/guidelines-skills-batch/reports/author-report.md`.
  It lists open details under *Searches not found or unclear*; judge each yourself, its grade and
  scope are yours.

## Answers of the orchestrator's step 4

- Trust boundary: no. Irreversible operation: no. The task did not move any pin (the repository
  is the-way itself). No reserved choice.
- Checks the author ran: `foundation_check.py`, `check_instructions.py`, and the focused tests of
  `instruction-files`, `agent-instructions`, `elements/common`, `project-level`, each with its
  command and exit code in the report. The base gate (`python -B gate/run_tests.py` on the base)
  passed: exit 0, 804 tests. The orchestrator runs the full gate on the reviewed change after
  your review; do not run it, and run only the checks you need for a finding.
- The five settlements are written as foundation entries (WAY-240, WAY-216, WAY-282 edited in
  place; WAY-310 and WAY-311 new). The return step comes after your review; you do not review it.

## Report

Write the full report to
`docs/task-cycles/guidelines-skills-batch/reports/review-whole-report.md`
as your method gives (first line `PASS <sha>` or `FAIL <sha>`, graded findings, Minor findings
that fall within the task listed apart from the out-of-scope ones, the checks you ran, each reach
beyond what you selected, and **Searches not found or unclear**, each item or `none`). Return only
the first line, the report path and a one-line result.
