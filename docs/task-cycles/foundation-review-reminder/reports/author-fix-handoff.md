# Handoff — the fix of the review's findings

Stage: the fix of the Minor findings of the review of the whole change, by the author who made the change, resumed.

Variant of `make-change`: the fix of a review's findings. Read `task-cycle/change/fix.md` where the method names it.

## What you fix

The findings file: `reports/whole-findings.md` (in `docs/task-cycles/foundation-review-reminder/reports/`). It holds five Minor findings in the reviewer's words, all within the task, none marked outside its scope; the review's first line is `PASS b7ec371207ad67d6378f323433f643e1703335e5`, so no finding blocks, and the cycle fixes these Minor findings in one fix before the request opens. The reviewer's whole report is `reports/review-whole-report.md`; read the findings in the findings file, and the report only where a finding refers to a passage of it.

- Fix each finding, or answer with evidence in your report that one does not hold; the orchestrator moves no finding from one kind to another and neither do you.
- Your two additions (your choices 6 and 7) stay, as the reviewer found them and as finding 4 asks for a clause on the first; nothing else is added.
- The fix's range runs from the reviewed head `b7ec371`. Commit on the task branch only, each file by its path, messages in English, no push.
- Run the affected checks again: `python -B task-cycle/test_review_reminder.py` if the script or its test is touched, `python -B elements/common/foundation_check.py` for the log, and `python -B gate/run_tests.py task-cycle` for the files of `task-cycle`. No full gate (`python -B gate/run_tests.py` without a directory): the person who requested the cycle has asked that none run before a signal `start` of the day's advisor.
- Finding 3: the orchestrator kept your wording as an autonomous choice (record row Q4); the reviewer's finding says it is narrower than the task and fails for a product whose `## Backlog` section names no name. Choose the wording that follows the task's point 1 and question 3 and holds for such a product, name the choice in your report with the way rejected, and keep step 13, the template and WAY-300 saying the same.
- Finding 4: WAY-287 puts the steps skipped and the checks not run in the request's section for the human's decisions; one clause in step 13 is what the reviewer asks for.

## Where you work

Worktree `the task's worktree`, branch `task/foundation-review-reminder`; your directory for working copies is `.runs/author/`, as before, with the same rule for a working copy that your first handoff gave. Your report: `docs/task-cycles/foundation-review-reminder/reports/author-fix-report.md`, in the form of your earlier report: commits, checks with command and exit code, each finding with what you did or why it does not hold, your own-work check, reaches, **Unread material**, **Searches not found or unclear**, working copies.
