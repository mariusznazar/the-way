# Handoff — the fix of a review's findings

You are the one author (agent type `the-way-author`), resumed for the fix. The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer here is that person's approval.

- Worktree: `the task's worktree`, branch `task/relations-todo-for-unwritten-decision`, reviewed head `452f123d65de88143c91fe37b5633ecd341d88ee`. The fix's range runs from that head.
- Method: `task-cycle/change/SKILL.md`, variant "the fix of a review's findings". Read the part of the method that names that variant and the files it names when their step comes.
- Findings file: `reports/review-whole-findings.md` (beside this handoff, in `.runs/task-cycles/relations-todo-for-unwritten-decision/reports/`), in the reviewer's words: one blocking finding (I1, Important) and three Minor findings within the task (M1, M2, M3). Fix all four. The review's report is `reports/review-whole-report.md`; read it where a finding points at it. M4 and M5 of that report are outside the task's scope: do not touch them.
- Answer with evidence a finding you hold wrong; do not change a finding's grade or scope.
- A fix for I1 and for the test it needs: write the test first, see it fail on the head, then fix; say so in the report. The tests for I1 are one for each form the finding names (a bare `TODO` behind a type, `derives from TODO`, `derives from WAY-01 · derives from TODO`, and a `TODO` with a description behind a type), and the message of each says what is wrong. For M2 add the one test the finding asks for.
- Where a fix changes a sentence that a test, WAY-71, `elements/common/rules.md`, `elements/decisions/template.md` or the docstring of `foundation_check.py` holds, change them together. Run the tests of the directories you change (`python -B gate/run_tests.py elements/common`, and `task-cycle` if you touch it) and `python -B elements/common/foundation_check.py`. You do not run the full gate (`python -B gate/run_tests.py` without a directory): that run is the orchestrator's alone (WAY-160).
- Report: `.runs/task-cycles/relations-todo-for-unwritten-decision/reports/author-fix-report.md`, in the report form of `task-cycle/change/SKILL.md`, with its own-work check, **Unread material**, **Searches not found or unclear** and working copies. Return its status, the fix commits, a one-line check result and the report path.
- Commit messages in English; `git add` by path, never `git add -A`/`.`/`commit -a`. Do not push.
- Your directory for working copies: `.runs/author/` (the same as before; remove your copy before you return).
