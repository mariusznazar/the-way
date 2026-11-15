# Handoff — review of the fix of the Minor findings

You are the reviewer of the whole change, resumed, to review the fix of the findings you listed. You
review read-only: no file changed, no commit. The person who requested the cycle has delegated the
intermediate choices to the orchestrator; nothing you or the orchestrator say is that person's
approval.

- Worktree: `.`, branch
  `task/cycle-after-foundation-review`.
- Method: `task-cycle/review/SKILL.md`; for the review of a fix, read `fix.md` beside it and follow it
  (what you read and what bounds the review).
- The range reviewed: from your reviewed head `6727b67a34c54c9b6b6c7cae793c2e2681b9cdc9` to the head
  of the fix, `cfda61e` (one commit by the one author; compute the diff yourself).
- The findings file the fix was given: `.runs/task-cycles/cycle-after-foundation-review/reports/whole-findings.md`
  (your Minor findings 1 and 2, cut from your report in your words; the third Minor finding, marked
  outside the task's scope, was not given to the fix).
- The fix report: `.runs/task-cycles/cycle-after-foundation-review/reports/author-fix-report.md`
  (claims to verify, not evidence). The frozen task, as before:
  `.runs/task-cycles/cycle-after-foundation-review/task.md`.
- The fix is judged once. A new Critical or Important finding in it fails the review; a Minor finding
  that remains or is new does not block and goes to the request's list.
- Run only the checks the review needs; not the whole gate (the orchestrator's run).
- Agent directory for working copies: `.runs/review-whole/` (the report must say what stood there
  and that it was removed; your index of the earlier review may be removed now).
- Report path: `.runs/task-cycles/cycle-after-foundation-review/reports/review-whole-fix-report.md`.
  Its first line is `PASS <sha>` or `FAIL <sha>`.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed.
The files that a product's own tools and tests make by themselves are no working copy of the agent
and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a
worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside
its report what the report needs, and states in the report where each copy stood and that it was
removed. Where a removal fails, the agent finishes all the same and names in the report the
remainder, with its full path and the reason it stayed.

## What you return

First line `PASS <sha>` or `FAIL <sha>`; graded findings of the fix; the checks you ran with command
and exit code; **Unread material**; **Searches not found or unclear**; working copies.
