# Handoff — the fix of the return step's review findings

You are the one author (agent type `the-way-author`), resumed for a second fix. The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer here is that person's approval.

- Worktree: `the task's worktree`, branch `task/relations-todo-for-unwritten-decision`, reviewed head `763af6951a65f6cca17b032a037c60c7b2d59e0a` (the return step's commit). The fix's range runs from that head.
- Method: `task-cycle/change/SKILL.md`, variant "the fix of a review's findings".
- Findings file: `reports/review-whole-findings.md` is the earlier file; this fix answers `reports/review-return-step-findings.md` (in `.runs/task-cycles/relations-todo-for-unwritten-decision/reports/`): one blocking finding, I1. The review's report is `reports/review-return-step-report.md`; read it where the finding points at it.
- Both ways the reviewer names are open to you; choose by the entry's rules (WAY-12, `elements/decisions/template.md` "Verification", `task-cycle/skill/return_step.md`): (a) add a line `decision:` at the two tests the finding names, quoting a sentence of WAY-71 that each test holds, and keep the clause as it stands; or (b) narrow the clause to the two held parts and restore the two removed examples to the pair. Say which you chose, why and what you rejected. After (a), run the foundation check to see the new lines are read, and alter a quotation once to see it rejected, then restore it.
- Answer with evidence a finding you hold wrong. Do not touch WAY-287, M4, M5, N1, N2 or m1: they go to the request's list.
- Run `python -B elements/common/foundation_check.py` and `python -B gate/run_tests.py elements/common`. You do not run the full gate (`python -B gate/run_tests.py` without a directory): that run is the orchestrator's (WAY-160).
- Report: `.runs/task-cycles/relations-todo-for-unwritten-decision/reports/author-fix-2-report.md`, in the report form of `task-cycle/change/SKILL.md`, with its own-work check, **Unread material**, **Searches not found or unclear** and working copies. Return its status, the fix commits, a one-line check result and the report path.
- Commit messages in English; `git add` by path, never `git add -A`/`.`/`commit -a`. Do not push.
- Your directory for working copies: `.runs/author/` (remove your copy before you return).
