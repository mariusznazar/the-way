# Handoff — the return step again, over the range of fix 2, `make-change`

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer in this handoff is that person's approval. The cycle has one ordinary human contact, the request.

## Where you work

- The same worktree and branch: `the task's worktree`. The head is `b87125b6` (your fix 2; the second review of the whole change `FAIL 2dca6873`, the review of its fix `PASS b87125b6`). Your directory for working copies: `.runs/author/`.
- Your report: `.runs/task-cycles/ai-review-fixes-from-24-11/reports/author-return-2-report.md`, with **Unread material**, **Searches not found or unclear**, each check with command and exit code, in the record's *Return step* form as before.

## Your stage

The return step, as `task-cycle/skill/return_step.md` gives it, which you read whole: the first return step (`reports/author-return-report.md`, no commit) ran before the second review of the whole change, and fix 2 (`2dca6873..b87125b6`) has since changed code (`check_linked` now keys decisions by the value of the number and skips an invariant of the earlier form with a version in its heading), two tests, the *Rejected* of WAY-12 and WAY-30 and one sentence of WAY-30. Compare that range's code and entries, and the entries and part map the first return step compared, with the files of the repository once more: the docstring of `foundation_check.py`, `agent-instructions/README.md`, the root `README.md`, the two templates' rows and the entries WAY-12 and WAY-30 against what the check now does, and correct in the same change whatever no longer matches. The reports to read for it: `reports/review-whole-2-report.md` and `reports/review-fix-2-report.md`. Where you find nothing to correct, commit nothing and say so. Do not run the full gate. Commit any correction by path, English message.

## Working copies

Only in `.runs/author/`; remove before you return by the full path, and say so in the report.
