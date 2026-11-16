# Handoff to the reviewer of correction 1

You are a fresh reviewer: you did not make the change and did not write any earlier review of it.
Ask the human nothing; a question goes to the orchestrator in your report as `questions`.

## What you review

- The worktree (read-only for you): `the root of the task's worktree`.
- Method: `task-cycle/review/SKILL.md` (`review-change`), variant "the review of a correction for the
  human's remarks": read `task-cycle/review/fix.md` as the method says; the remarks stand in place of a
  findings file.
- The range: base `428cc4553042992c6a9813e7dd0a9ef11f0e2ea1` (the code the earlier reviews judged) to head
  `b3bd8f4` (`git rev-parse b3bd8f4` gives the full identifier). The two commits between them only add and
  remove the record's copy; the diff to review is `git diff 428cc45 b3bd8f4`.
- The remarks, word for word (they bind):
  `docs/task-cycles/audit-answers-contradiction-after-code/reports/correction-1-remarks.md`. The part you
  judge in code and instruction texts is items 1 and 4: the fix of the finding I-2 and of the Minor
  finding N-1, both written in `docs/task-cycles/audit-answers-contradiction-after-code/reports/review-fix-report.md`
  (read it whole).
- The author's report (claims to verify, not evidence):
  `docs/task-cycles/audit-answers-contradiction-after-code/reports/author-correction-report.md`.
- The frozen task: `docs/task-cycles/audit-answers-contradiction-after-code/task.md` (for *To do* 3 and 6 and
  question 5, which I-2 broke).
- Your report: `docs/task-cycles/audit-answers-contradiction-after-code/reports/review-correction-report.md`.
  Your directory for working copies: `.runs/review-correction/`.

## Two things to judge

1. **The correction (items 1 and 4).** Does it close I-2 and N-1 as the finding says, with no new wrong
   `yes` or `no` and no old right answer lost? The two records of the finding: a plain first attempt under
   an empty item beside a second entry (must not give `no`); the one-attempt text with its details as a list
   (gave `yes` at `ab2c8c8`). The author chose the second of the reviewer's two ways (read the whole item as
   one attempt where plain lines stand beside the entries); judge that choice. Crafted input at the trust
   boundary `process-audit/record_items.py` — an item with plain lines mixed among entries, deeper and
   shallower indents, fenced lines, tabs, a very long or very many lines, control characters — must give no
   wrong `yes`/`no`, no hang, no crash. The earlier tests that held WAY-404 and *To do* 3 must still stand.
2. **Item 3 of the remarks: the unread decisions.** The earlier reviewer of the whole change named as
   unread, though they bear on the route of the narrowing of WAY-344, these three: WAY-14 ("Who accepts a
   decision?"), WAY-314 ("Which act of the human consents to a change of a decision that refinement
   shows?") and WAY-315 ("From when does a decision of the foundation bind the work on a task?"). **Read the
   three whole** in `foundations/decisions.md`, with WAY-30 and WAY-114, which the route rests on. Then judge
   and state in your report: does the route by which the narrowing of WAY-344 is carried hold — the narrowing
   written by the cycle on the task branch under WAY-30, marked `the cycle's` (WAY-114), put before the
   human in the request, accepted by the human's merge — or does it go beyond what the task document's
   accepted *Settlements to record* and the human's acts allow? The narrowing is the new sentence of WAY-344,
   its *Verification* clause and its *Rationale* sentence, in commit `428cc45`
   (`git show 428cc45 -- foundations/decisions.md`); the human's answer to the request accepts it unless your
   reading shows the route does not hold. If it does not hold, that is a finding (Important), with the
   reason, and the orchestrator will leave the narrowing for the human.

Your **Unread material** names exactly which of the three you read whole.

## Checks

Focused checks only (`python -B gate/run_tests.py process-audit`, `... task-cycle`,
`python -B elements/common/foundation_check.py`, in a worktree of the head in your directory); **do not run
the product's full gate**. Report each check with command and exit code.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed.

## The report

First line `PASS <sha>` or `FAIL <sha>` (or `questions`); graded findings with places in the code; the
judgment of item 3 in a section of its own; checks with commands and exit codes; **Unread material**;
**Searches not found or unclear**; the line on your working copies. Return the first line, a one-line check
result and the path.
