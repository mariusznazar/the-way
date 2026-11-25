# Handoff — the fix of the findings of the review of the whole change, `make-change`

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer in this handoff is that person's approval. The cycle has one ordinary human contact, the request.

## Where you work

- The same worktree and branch as before: `the task's worktree` (branch `task/ai-review-fixes-from-24-11`). The reviewed head is `225bf1c5`; your fix range runs from it.
- Your directory for working copies: `.runs/author/` (as before).
- Your report: `.runs/task-cycles/ai-review-fixes-from-24-11/reports/author-fix-1-report.md`, with the same sections as your first report (**Unread material**, **Searches not found or unclear**, checks with command and exit code). The report file is the input of the cycle's scripts.

## Your stage and variant

"The fix of a review's findings", of `task-cycle/change/SKILL.md`. The findings file is `reports/review-whole-findings.md` in `.runs/task-cycles/ai-review-fixes-from-24-11/` (path: `.runs/task-cycles/ai-review-fixes-from-24-11/reports/review-whole-findings.md`); read it whole. It holds no blocking finding and one Minor finding within the task: two lines you re-wrapped, `README.md:94` (105 characters) and `agent-instructions/README.md:24` (126 characters), run past the 100 columns of their paragraphs. Re-wrap the two paragraphs so that every line of them is 100 characters or fewer, with the text unchanged word for word. Change nothing else. Run the affected checks again (the foundation check, `python -B gate/run_tests.py agent-instructions`, `python -B gate/run_tests.py elements/common`), and answer with evidence any finding you hold wrong. Commit by path (`git add <path> …`), message in English; return status, commits, one-line check result and the report path.

## Working copies

Make a working copy only in `.runs/author/`, remove it before you return, and say in the report where each stood and that it was removed; the removal by its full path, never through a shell variable.
