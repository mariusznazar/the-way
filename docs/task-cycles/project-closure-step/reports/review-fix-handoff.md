# Handoff — review of the fix of the review's findings (task `project-closure-step`)

You are the reviewer of the whole change, resumed to review the fix range once, with `review-change`
(`task-cycle/review/SKILL.md`), as `task-cycle/review/fix.md` gives it: read that file whole and follow
what it says you read and what bounds the review. Read-only: change and commit nothing.

- Worktree and branch: as before, `the task's worktree`, `task/project-closure-step`.
- Range of the fix: from the reviewed head `ee85f143fd43c01a94f46511680a8c2f3cb87db9` to the head
  `d4cfe710` (confirm `git rev-parse HEAD`; compute `git diff ee85f143..d4cfe710` and
  `git log ee85f143..d4cfe710` yourself): three commits `95d42e9a`, `836be8a0`, `d4cfe710`.
- The findings the fix answers, in your words: `.runs/task-cycles/project-closure-step/reports/review-whole-fix-findings.md`
  (the five blocking findings I1–I5 and the Minor findings 1–9 within the task; your Minor 10, outside
  the task, was not to be fixed and is not in it).
- The fix report: `.runs/task-cycles/project-closure-step/reports/author-report.md` (updated by the
  author; a set of claims to verify). Its checks, choices and quotation of the added passage of WAY-414
  are yours to test.
- Your report: `.runs/task-cycles/project-closure-step/reports/review-fix-report.md`, first line `PASS <sha>`
  or `FAIL <sha>`. Your directory for working copies: `.runs/review-whole/` (as before; the same
  rules for removal, and the same paragraph on working copies as in your first handoff holds).
- The frozen task, `.runs/task-cycles/project-closure-step/task.md`, and your earlier report are still
  yours to read; the other files of the record directory are not.

What to judge: whether each finding is fixed as you wrote it, and whether the fix introduced a new
Critical or Important finding (only such a finding fails this review; a Minor remaining or new goes to the
request's list). Two choices of the orchestrator that the fix carries out, to judge against the task and the
settlements rather than accept:

1. Q3 (your I2): a row `done — goal delivered in task <n>` whose task n is `dropped — approved by human`
   holds the closing as a row in another state does: it does not start, the agent tells the human which
   row and why, before any preview.
2. Q2 (your I5): the smallest reversible reading you named — for a withdrawn task made a task of its own
   whose `Document` cell already links a document, the closing makes no second document in silence; it shows
   the existing document in the preview, asks which document stands, and the new place refers to the old
   document.
3. Your I4: the added passage of WAY-414 (the question of the heading for a decision, the identifier or term
   for another entry, and the comparison of I3) is an addition to row 5, so `the cycle's`; check the
   passage against what the file `closure.md` does, in both directions.

The trust boundary answer stands (yes, `plan_check.py` and `plan_state.py`; the fix touched
`plan_state.py` (the help of an argument) and tests). Do not run the whole gate. You may run the tests of
one directory and the foundation check; report each with its command and exit code. Give your
**Unread material** and **Searches not found or unclear**, and your reaches beyond this handoff, as before.
Return the first line of your report, the changed files with line counts, your checks, and the path.
