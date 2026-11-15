# Handoff: review of correction 2, second part

You are the reviewer of correction 2 (`PASS 2e83447`), resumed to review its second part, once. You did not make the change. Read-only on the repository; your working copy is `.runs/review-correction-2b/` under the task's worktree `the worktree of the task`. No full gate (the orchestrator's); single directories one at a time.

## The range

`cde07dd..0e3cb2a`: one commit, `0e3cb2a` "Allow agent-instructions to depend on repository", one line of `foundations/part_map.md`. `cde07dd` is the merge of `origin/foundations` (`9cbc6b2`) into `2e83447`, which another reviewer judges separately and you do not. The author's report: `reports/author-correction-2b-report.md`. Read from your own clone of `0e3cb2a`.

## What the correction had to do

The human's answer to the question of the return step of correction 2 (the file `reports/correction-2-remarks.md`, its second part, which holds the comment word for word):

> 1. Yes: allow the dependency. Add the part `repository` to the allowed dependencies of the part that holds the CI file (`.github/workflows/tests.yml` reads `/.python-version`), the same way as `instruction-files` for `installation`.
> 2. The two prose mentions in `installation/README.md` (the workflow file and `.the-way/.python-version`) are not a dependency: the code of `installation` does not read those files. No change.

## What to judge

1. That the correction adds exactly `repository` to the *Depends on* of the part that holds the CI file (`agent-instructions`, whose *Files* hold `.github/workflows/**`) in the file's form, and changes nothing else; and that item 2 of the answer is respected (`installation/README.md` and the part `installation` unchanged).
2. That the commit message cites the human's answer as far as the map's forms allow (the map has no field for a citation).
3. That the allowance causes no error of the map and no cycle (the part `repository`'s own *Depends on*, the part-map template and its skill, the checks), and that it is the whole of what the answer binds.
4. The foundation check on the corrected tree (`python -B elements/common/foundation_check.py` without `--skip-test-citations`) and the tests of `elements/part-map` and `elements/common`, one directory at a time.

The Minor findings of earlier reviews stand in the request's list and are not yours to re-judge.

## Your report

`reports/review-correction-2b-report.md`, first line `PASS <sha>` or `FAIL <sha>` (the sha of `0e3cb2a`); findings with grades and places; the checks with command and exit code; **Unread material**; **Searches not found or unclear**; working copies and their removal. No secrets or personal data.

## Working copies (word for word from the cycle's skill)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed, except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md` says, to the place the product's foundation settles for screenshots, and into the agent's directory only where no such place is settled. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.
