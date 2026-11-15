# Handoff: the return step again on the final code (correction 2, after the answer to its question)

You are the author of the corrections, resumed for the return step again, on your class. The orchestrator's go-ahead is provisional, never the human's approval.

## Where and what

- Worktree `the worktree of the task`, branch `task/ci-on-merge-requests`, the-way itself, head `0e3cb2a` (your last commit, on the merge `cde07dd` of `origin/foundations` `9cbc6b2`). Reviews passed: the merge `cde07dd` (`PASS`), your commit `0e3cb2a` (`PASS`), correction 2 `2e83447` (`PASS`). Your directory for working copies: `.runs/return-step-correction-2b/`. Your report: `.runs/task-cycles/ci-on-merge-requests/reports/return-step-correction-2b-report.md`.
- Method: `task-cycle/skill/return_step.md` (read whole), with `task-cycle/skill/foundation_step.md` beside it (read whole), each by its path in the worktree.

## Scope

The same as in your report `return-step-correction-2-report.md` (range `b344595..`, the entries the task writes or changes and the part maps of the touched parts), now on the final code: your earlier return step stopped on one question, which the human has answered (the part `repository` is allowed for `agent-instructions`, which you added in `0e3cb2a`; the two mentions in `installation/README.md` are no dependency, no change). Run the step again: compare the entries and the part maps of the touched parts with the final code, which now holds the target's newer commits (`cde07dd`: among them new checks of private paths and of remarks, a test of dead pointers in skills, the glossary term "Markdown file", and WAY-321, WAY-339, WAY-344 rewritten). Where the map still differs from the code at a reach nobody has settled, return `blocked` with the question as before; where nothing needs a commit, say so and commit nothing. No entry is deferred or proposed for later. The Minor findings of the reviews are not yours to fix. Read WAY-11 whole if you did not in your earlier return step (your report said you would).

Never run the full gate (the orchestrator's; it waits for the day advisor's signal). The focused checks: `python -B elements/common/foundation_check.py` without `--skip-test-citations`, and `python -B gate/run_tests.py <directory>` for single directories you change.

## What your report holds

Status, commits, the place each settlement went to as the record's *Return step* gives it, checks with command and exit code, **Unread material**, **Searches not found or unclear**, and the working copies with their removal. No secrets or personal data.

## Working copies (word for word from the cycle's skill)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed, except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md` says, to the place the product's foundation settles for screenshots, and into the agent's directory only where no such place is settled. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.
