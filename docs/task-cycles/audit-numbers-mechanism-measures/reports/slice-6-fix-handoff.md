# Handoff — fix of the review's findings, slice 6

Delegation: the person who requested this cycle has delegated intermediate choices to the orchestrator; your questions go to the orchestrator, never to the human.

Worktree: `the task's worktree`, branch `task/audit-numbers-mechanism-measures`. Reviewed head: `0964b521610f2f7a73d19c6a99f9477e537e8dd9`; your fix range runs from it.

Method: `make-change`, variant "the fix of a review's findings". Read whole `task-cycle/change/SKILL.md` and, since the variant names it, `task-cycle/change/fix.md`.

Findings file: `reports/slice-6-fix-findings.md` (in `.runs/task-cycles/audit-numbers-mechanism-measures/reports/`) — one blocking finding, I1, in the reviewer's words. The reviewer's full report is `reports/slice-6-review-report.md`. Fix only what the file holds; the review's Minor findings are not yours.

The fix: the cap on runs counts every row that becomes a run, wrong-width rows included, so a file of such rows costs bounded work and bounded result rows; the cut says so in *Unknown values* as it does for well-formed rows. Add a test (written before the code, its failing run in your report) that gives a flood of wrong-width rows after a valid header, asserts the number of runs read is at most the cap and the reason names the cut. Then run the focused check `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Measures` and the whole `process-audit/test_audit_count.py` once at the end (about three minutes; run it in the background and wait for it before you commit — do not return before it ends), `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` after the commit, and confirm `git diff` shows no changed line in the assignment of `TREE_PATHS`. Commit by path. Write your report to `reports/slice-6-fix-report.md` with the Write tool: each finding fixed (how, with the check that shows it) or contested with evidence; **Unread material**, **Searches not found or unclear**, own-work check. Do not run the product's gate.
