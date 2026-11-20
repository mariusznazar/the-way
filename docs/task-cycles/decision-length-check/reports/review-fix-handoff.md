# Handoff — the review of the fix of your findings

You are the reviewer of the whole change, resumed to review once the fix of your findings (WAY-162).
The person who requested this cycle delegated intermediate choices to the orchestrator; no answer
here is that person's approval.

- Worktree and branch: the task's worktree, `task/decision-length-check`.
  Read-only. Range of the fix: from the reviewed head `e8b76178` to `9c7f9b71`
  (`git diff e8b76178..9c7f9b71`, `git log e8b76178..9c7f9b71`); confirm `git rev-parse HEAD`
  is `9c7f9b71`.
- Your method: `task-cycle/review/SKILL.md`, and `task-cycle/review/fix.md` for a review of a fix, as
  your method gives.
- The findings the fix answers: `.runs/task-cycles/decision-length-check/reports/review-whole-fix-findings.md`
  (the blocking finding 1 and the Minor findings 2–5 within the task, cut from your report; finding 6
  was outside the task and is not fixed). The author's report of the fix:
  `.runs/task-cycles/decision-length-check/reports/author-fix-report.md`; its claims are to be
  verified, not taken as evidence.
- The frozen task, for what the fix must not break: `.runs/task-cycles/decision-length-check/task.md`.
- Your directory for working copies: `.runs/review-fix/`; remove it before you return.
- Your report: `.runs/task-cycles/decision-length-check/reports/review-fix-report.md`, its first line
  `PASS <sha>` or `FAIL <sha>`, with the checks you ran each with command and exit code, **Unread
  material**, **Searches not found or unclear** and your working copies. Only a new Critical or
  Important finding in the fix fails this review; a Minor finding that remains or is new does not block.
- Do not run the product's full gate.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed, except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md` says, to the place the product's foundation settles for screenshots, and into the agent's directory only where no such place is settled. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed. It removes a copy, as any directory, by its path written out in full in the command, never through a shell variable: an empty variable turns the removal on the directory the shell stands in.
