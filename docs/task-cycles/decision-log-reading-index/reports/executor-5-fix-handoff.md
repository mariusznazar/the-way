# Handoff: the fix of the review's findings for slice 5, task `decision-log-reading-index`

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer it
gives is the human's approval. You never ask the human. The cycle has one human contact, the request.

## What you do

- You are the executor of slice 5, resumed (same worktree `the task's worktree`,
  branch `task/decision-log-reading-index`, your directory `.runs/executor-5/`). The review of your slice returned
  `FAIL e1ab383eeb425a811a9f7a1a3663b027414a13f1`; its one blocking finding, I1, is in the findings file
  `reports/slice-5-findings.md` (path from `.runs/task-cycles/decision-log-reading-index/`), in the reviewer's words;
  its full report is `reports/review-5-report.md` beside it.
- Method: `task-cycle/change/SKILL.md`, the variant "the fix of a review's findings"; read `task-cycle/change/fix.md`.
- Boundary: fix I1 and nothing else. The Minor findings M1 (`MemoryError` of a huge line) and M2 (a subtest that never
  runs) are not yours to fix, and no other finding exists; touch only `task-cycle/cycle_measures.py` and
  `task-cycle/test_cycle_measures.py`. If you hold the finding wrong, answer with evidence instead of changing code.
  Run the affected checks again (the commands of the slice's checks), not the product's full gate. Commit by path;
  message in English, imperative, on top of the head `e1ab383`.
- Report: `.runs/task-cycles/decision-log-reading-index/reports/executor-5-fix-report.md`, written as a file at that
  exact path (its name begins with `executor`), as `fix.md` gives it, with the checks' commands and exit codes, the own-work
  check, **Unread material** and **Searches not found or unclear**, and the working copies line.

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

Your directory for working copies: `.runs/executor-5/`; remove the scripts you left there
(`mutate.py`, `real_codex.py`, `real_run.py`) and anything else you made, unless the report needs them, in which case
copy them into `reports/` first.
