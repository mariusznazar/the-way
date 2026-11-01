# Handoff — the fix of a review's findings

The review of the return step returned `FAIL aee18e4`. Fix its blocking finding, on the same branch,
in the worktree `C:/Storage/repos/the-way/.runs/worktrees/guidelines-audit-report`, under
`task-cycle/change/SKILL.md`, variant "the fix of a review's findings".

- Findings file: `.runs/task-cycles/guidelines-audit-report/reports/return-review-findings.md`.
- Reviewed head: `aee18e4`; your fix's range runs from it.
- The full review, for its checks: `.runs/task-cycles/guidelines-audit-report/reports/return-review.md`.
  Its Minor findings are not fixed by this cycle. Answer with evidence a finding you hold wrong.

Commit by path, in English, leave a clean tree and do not push. Run the affected checks, with no
commit landing during a run: `python -B elements/common/foundation_check.py .` and any directory your
change bears on, each with its command and exit code. Do not run the full gate.

Write `.runs/task-cycles/guidelines-audit-report/reports/fix.md`, with **Searches not found or
unclear**. Return only your status, your commits, a one-line check result and the report's path.
