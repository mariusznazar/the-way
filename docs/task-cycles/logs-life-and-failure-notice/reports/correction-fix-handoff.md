# Handoff — fix of the correction review's finding

You are the one author; your first handoff, `.runs/task-cycles/logs-life-and-failure-notice/reports/author-handoff.md`, still holds: its worktree, its restriction, its commit rules and its boundaries.

Your variant under `task-cycle/change/SKILL.md`: **the fix of a review's findings**. Read `task-cycle/change/fix.md` as its row gives.

- Findings file: `.runs/task-cycles/logs-life-and-failure-notice/reports/correction-review-findings.md`, one blocking finding of the review of `5eb89cf..94d20f3`.
- Reviewed head: `94d20f3`. Your fix is a new commit on it; do not amend and do not push.
- The human's decision still binds: a decision silent on part of a matter opens at a task only on the human's word, and WAY-267 stays as it is. So the file stands and the entry that departs from it is WAY-165, as the finding says. Fix the finding or contest it with evidence.
- A review's *Fix in one line* is a suggestion; the finding binds. Read every place of WAY-165 that the change depends on, its binding sentences and its *Verification* in both directions, its *Rationale* where it speaks of this, and keep to its three sentences (WAY-05). A definition's behaviour does not change.
- The review's Minor findings are not yours to fix.

Run the affected checks again and report each with its command and exit code, not through a pipe: `python -B elements/common/foundation_check.py .`, `python -B gate/run_tests.py project-level`. The full gate stays mine.

Write your report to `.runs/task-cycles/logs-life-and-failure-notice/reports/correction-fix.md`, as `fix.md` gives, with **Searches not found or unclear**. It holds the new meaning sentence of WAY-165, in Polish. Return only your status, your commit, a one-line check result naming what failed or did not run, and the report's path.
