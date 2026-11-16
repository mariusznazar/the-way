# Handoff - the fix of the review's findings (resumed author)

Same delegation, worktree, branch and rules as `reports/author-handoff.md`; your working-copies directory is `.runs/author-fix/` this time (remove it before you return). Method: `task-cycle/change/SKILL.md`, variant "the fix of a review's findings".

The findings file is `reports/review-whole-findings.md`: two blocking findings (I-1, I-2) and one Minor finding (M-1) of the review of the whole change, `FAIL 34db2685148207b901f8a19c2629b0e14af04c91`, whose full report is `reports/review-whole-report.md`. Fix all three in one fix round, on the branch, as a new commit on top of `34db2685` (never amend). Answer with evidence any finding you hold wrong.

Notes from the orchestrator:
- I-2 offers two ways out; choose one, state the choice and the rejected way with its cost in your report. Whichever you choose, the step that checks the pass (I-1) has to treat an earlier conversion row consistently with it.
- For I-1, the reviewer's suggested kind of check (a count of each reference before the pass under its old number against the count after it under its new one) is a suggestion; any check that holds when old and new ranges overlap and needs no search that a correct pass fails is acceptable. Keep the text short: it is a skill step, not a program.
- After the fix, extend your own-work check to what the reviewer found: run the new step-3 check as the text gives it on an overlapping map (for example 500..502 -> 502..504) and on the two-pass case of I-2, and keep the script beside your report in `reports/` (`author-fix-passcheck.py`).
- If the entry WAY-403 (its examples or its second paragraph) says something your fix changes, correct it in the same commit and run `python -B elements/common/foundation_check.py --skip-test-citations` and the focused tests of the directories you touch. Do not run the product's full gate.
- Report: `reports/author-fix-report.md`, with the same sections as before (status, commits, checks with command and exit code, own-work check, **Unread material**, **Searches not found or unclear**, working copies).
