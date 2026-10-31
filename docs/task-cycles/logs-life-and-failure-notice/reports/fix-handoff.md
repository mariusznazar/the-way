# Handoff — fix of the whole-change review's findings

You are the one author; your first handoff, `.runs/task-cycles/logs-life-and-failure-notice/reports/author-handoff.md`, still holds: its worktree, its restriction, its commit rules and its boundaries.

Your variant under `task-cycle/change/SKILL.md`: **the fix of a review's findings**. Read `task-cycle/change/fix.md` as its row gives.

- Findings file: `.runs/task-cycles/logs-life-and-failure-notice/reports/whole-review-findings.md`, four blocking findings of the review of `5d66387..4a3ee37`.
- Reviewed head: `4a3ee37`. Your fix is one or more new commits on it; do not amend.
- Fix each finding, or contest it with evidence. A review's *Fix in one line* is a suggestion; the finding binds. The review's Minor findings are not yours to fix (WAY-161).
- Finding 1: to name an alert in WAY-270 is a row's word and names no product; the step's files keep naming only the deliberate absence (spec D5).
- Finding 3: the list of WAY-139 and `resolve_gaps.md` then agree on seven items, five as today and two new. Check the sentences that count items.
- Finding 4: read the path of a new list as well as the path of a resumed one, and a run at a task (spec D6, its reading on what a run answers), before you call it fixed.

Run the affected checks again and report each with its command and exit code, not through a pipe: `python -B elements/common/foundation_check.py .`, `python -B gate/run_tests.py project-level`. The full gate stays mine. Say again, in the report, what your own-work check read, a new list included.

Write your report to `.runs/task-cycles/logs-life-and-failure-notice/reports/fix.md`, as `fix.md` gives, with **Searches not found or unclear**. Update the meaning sentence of any entry the fix changes. Return only your status, your commits, a one-line check result naming what failed or did not run, and the report's path.
