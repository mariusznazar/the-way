# Handoff — review of the fix of the whole-change review's findings

## Delegation

The person who requested this cycle delegated the intermediate choices of the cycle to the
orchestrator. Nothing here is that person's approval. Do not ask the human: return `questions`.

## What you review

- Worktree `the root of the task's worktree`, branch
  `task/part-map-dependencies-task-line`. Read-only. Range of the fix: base `af76148` (the head you
  reviewed) to head `1b5aba9` (confirm `git rev-parse HEAD`). One commit.
- Method: `task-cycle/review/SKILL.md` (`review-change`), the review of a fix; read `fix.md` beside
  it and follow it: what you read and what bounds the review.
- The findings the fix answers: `reports/whole-findings.md`
  (`docs/task-cycles/part-map-dependencies-task-line/reports/whole-findings.md`), cut from your own
  report `reports/review-whole-report.md`: I-1 (blocking), M-1, M-2, M-3 (Minor within the task).
- The fix report (claims to verify, not evidence):
  `docs/task-cycles/part-map-dependencies-task-line/reports/author-fix-report.md`.
- Evidence the author gives on M-3, which you grade and scope alone: the frozen task
  (`docs/task-cycles/part-map-dependencies-task-line/task.md`, *Decisions in play*) says WAY-225
  stays unchanged ("Bez zmiany"), so the author left the binding sentence of WAY-225 and the
  examples and prose of WAY-225 and WAY-51 as they were, and changed the bare word "dependency" in
  the part map, the part-map skill and the part-map template. The fix also split the invariant
  `blocked-request-line` into `blocked-request-wording` and `blocked-request-label` (M-2) and, because
  a skill's description changed, rewrote its two entry points with
  `agent-instructions/skill_entry_points.py --write`.
- Your own earlier selection stands; reach for more selectively and name each reach.
- A new Critical or Important finding in the fix counts as one that remains; a Minor finding that
  remains, or that you find new in the fix, does not block.
- Your directory for working copies: `.runs/review-whole-fix/`. Your report:
  `docs/task-cycles/part-map-dependencies-task-line/reports/review-whole-fix-report.md`, whose first
  line is `PASS <sha>` or `FAIL <sha>`. You do not run the whole gate.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.

## Report

First line, the checks you ran with commands and exit codes, **Unread material**, **Searches not
found or unclear**, working copies.
