# Handoff: author, correction 2, second part (the human's answer to the question of the return step)

You are the author of the corrections, resumed, on your class. The orchestrator's go-ahead is provisional, never the human's approval.

## Where and what

- Worktree `the worktree of the task`, branch `task/ci-on-merge-requests`, head `cde07dd` (the merge of `origin/foundations`, `9cbc6b2`, into your correction 2 `2e83447`; no conflict; a reviewer reads that merge in its own clone while you work, so keep to the files named below). Your directory for working copies: `.runs/author-correction-2b/`. Your report: `.runs/task-cycles/ci-on-merge-requests/reports/author-correction-2b-report.md`.
- Method: `task-cycle/change/SKILL.md`, variant **"a correction for the human's remarks"**; `task-cycle/skill/foundation_step.md`.

## The remark you carry out, word for word

> 1. Yes: allow the dependency. Add the part `repository` to the allowed dependencies of the part that holds the CI file (`.github/workflows/tests.yml` reads `/.python-version`), the same way as `instruction-files` for `installation`.
> 2. The two prose mentions in `installation/README.md` (the workflow file and `.the-way/.python-version`) are not a dependency: the code of `installation` does not read those files. No change.
>
> Do it in correction 2, after merging `origin/foundations` (it moved to 9cbc6b2 with #132), then the return step on the final code, and before the full gate write that it is about to start and wait for the day advisor's signal.

The full answer is in `.runs/task-cycles/ci-on-merge-requests/reports/correction-2-remarks.md`. The merge is done; the return step comes to you separately later.

## What to do

1. Add `repository` to the *Depends on* of the part `agent-instructions` in `foundations/part_map.md` (the part that holds `.github/workflows/**`), as you did for `instruction-files`: the file's own form, one commit by explicit path, the human's answer cited in the commit message in English with its source (the comment URL of the answer and its date, 2026-11-15) since the map has no field for a citation.
2. Check that the allowance causes no error of the map: `python -B elements/common/foundation_check.py` without `--skip-test-citations`, and `python -B gate/run_tests.py elements/part-map` and `elements/common`, one directory at a time. Never the full gate (the orchestrator's; it waits for the day advisor's signal). Do not change `installation/README.md` or anything else: item 2 of the answer says no change.
3. Do not fix the Minor findings of the reviews; they stand in the request's list. Do not edit the request's description.

## Reading

WAY-225, the glossary entry "dependency of a part", `elements/part-map/template.md` ("Allowed dependencies"), and the map's own *Depends on* of `agent-instructions` and `repository`.

## Working copies (word for word from the cycle's skill)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed, except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md` says, to the place the product's foundation settles for screenshots, and into the agent's directory only where no such place is settled. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.

## Your report

Status, commits, what was changed, checks with command and exit code, the own-work check, reach beyond the handoff, **Unread material**, **Searches not found or unclear**, working copies and their removal. No secrets or personal data.
