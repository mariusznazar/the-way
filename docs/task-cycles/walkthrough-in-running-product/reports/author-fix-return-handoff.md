# Handoff to the one author — the fix of the return step's review finding

You are the one author, resumed. Variant of `task-cycle/change/SKILL.md`, in the words of its row:
**"the fix of a review's findings"** (`task-cycle/change/fix.md`, read whole).

- Worktree `the task's worktree`, branch
  `task/walkthrough-in-running-product`; the fix's range runs from the reviewed head `83aa64db`.
- Findings file: `.runs/task-cycles/walkthrough-in-running-product/reports/fix-return-findings.md` — one
  blocking finding with `Contradiction: yes` (the lower part of `request_template.md`, paragraph
  *Findings outside the task's scope*, still gives the walk's out-of-scope errors as the author's
  alone). Fix exactly it; correct to WAY-408 and row 3 of the task's *Settlements to record*. Where the
  same restatement stands in a second place that your fix would otherwise leave different, correct it too
  and name it (WAY-33); the reviewer's two Minor findings are not part of this fix (do not fix them unless
  the same sentence demands it, and say so).
- Run the affected checks again (`python -B elements/common/foundation_check.py`,
  `python -B task-cycle/private_paths_check.py task-cycle/skill/request_template.md`,
  `python -B gate/run_tests.py task-cycle`). No full gate. Commit by path, in English, nothing under `.runs/`.
- Working copies in `.runs/author-fix-return/`, removed before you return.
- Report: `.runs/task-cycles/walkthrough-in-running-product/reports/author-fix-return-report.md`, with what
  you did for the finding and its evidence, **Unread material**, **Searches not found or unclear**, your
  own-work check. Return status, commits, a one-line check result and the report path.
