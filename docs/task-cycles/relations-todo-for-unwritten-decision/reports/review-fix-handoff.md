# Handoff — review of the fix of the whole-change review's findings

You are the same reviewer (agent type `the-way-stage`), resumed to review the fix once. You did not make the change or the fix. You are read-only. The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer here is that person's approval.

- Worktree: `the task's worktree`, branch `task/relations-todo-for-unwritten-decision`. Work from its root.
- Method: `task-cycle/review/SKILL.md`, the review of the fix of earlier findings.
- Range of the fix: from the reviewed head `452f123d65de88143c91fe37b5633ecd341d88ee` to `68d8645` (one commit; files `elements/common/foundation_check.py`, `elements/common/test_foundation_check.py`, `elements/decisions/template.md`, `foundations/decisions.md`). Read the full diff of that range.
- Findings the fix answers: `reports/review-whole-findings.md` (in `.runs/task-cycles/relations-todo-for-unwritten-decision/reports/`): I1 (blocking), M1, M2, M3. The fix's report: `reports/author-fix-report.md`. Your own report of the whole change: `reports/review-whole-report.md`.
- Judge: whether each of the four findings is fixed; whether the fix is right against the frozen task (`.runs/task-cycles/relations-todo-for-unwritten-decision/task.md`, To do 1-6, *Questions to settle*, *Out of scope*); whether the fix introduces a new finding (a new Critical or Important finding counts as one that remains). The author says `foundation_check.py` now stands at 999 lines, under the 1000-line file threshold (WAY-385): check it. M4 and M5 are outside the task's scope and were not to be touched; say so if they were.
- Trust boundary: no; irreversible operation: no.
- You run no full gate (`python -B gate/run_tests.py` without a directory); you may run `python -B gate/run_tests.py elements/common` and `python -B elements/common/foundation_check.py`, and the size test and `change_file_sizes.py` as before. Where `ruff` is still absent, say so.
- Report: `.runs/task-cycles/relations-todo-for-unwritten-decision/reports/review-fix-report.md`, first line `PASS <sha>` or `FAIL <sha>`, by the report form of `task-cycle/review/SKILL.md`, with graded findings, checks with command and exit code, **Unread material**, **Searches not found or unclear**, working copies. Return the first line, the report path and one line of the checks.
- Your directory for working copies: `.runs/review-whole/` (the same as before; remove your copy before you return).
