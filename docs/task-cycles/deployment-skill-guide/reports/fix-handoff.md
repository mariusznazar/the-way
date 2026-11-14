# Handoff — the fix of the whole-change review's findings (task `deployment-skill-guide`)

You are the one author, resumed. Variant of `make-change`: "the fix of a review's findings". Worktree and branch as before
(`the task's worktree`, `task/deployment-skill-guide`); the reviewed head is
`a900916e8980eaf6d913e2c8bd0b6cbd212deb21`; the fix's range runs from it.

Findings file: `.runs/task-cycles/deployment-skill-guide/reports/review-whole-findings.md` (the reviewer's words: I1, I2
blocking; M1-M4 Minor within the task, all fixed in this one fix). The full review is
`.runs/task-cycles/deployment-skill-guide/reports/review-whole-report.md`; read it where a finding needs its evidence.

Notes of the orchestrator, no grading of any finding:
- I2: the reviewer asks that the whole sentence is quoted with the exception marked as loop2's. Fix as it directs; do not
  change WAY-140 or loop2.
- M2: keep the source order; where a fragment joins sentences from different places, name the section of the source or make it a
  separate fragment; correct the two inaccurate statements.
- A finding you hold wrong you answer with evidence in your report; you do not skip it silently.
- Keep your privacy search (no real game address, no sender mailbox domain) after the fix.

Run the affected checks again with command and exit code (`python -B elements/common/foundation_check.py`, the
`project-level` tests, the private-path checks of the changed files). Commit on the branch, do not push. Write the report to
`.runs/task-cycles/deployment-skill-guide/reports/author-fix-report.md` with the same sections as your first report
(**Unread material**, **Searches not found or unclear**, own-work check). Return status, commits, one-line check result, path.
