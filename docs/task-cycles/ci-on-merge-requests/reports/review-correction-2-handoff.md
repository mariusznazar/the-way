# Handoff: review of correction 2 (the human's answer to the blocking item)

You are the reviewer of the merge `3eacbc1` and of its fix, resumed to review correction 2, once. You did not make the change. Read-only on the repository; your own working copy is `.runs/review-correction-2/` under the task's worktree `the worktree of the task`. No full gate (the orchestrator's); single directories one at a time.

## The range

`9a00830..2e83447`: one commit, `2e83447` "Allow installation to depend on instruction-files and drop the debt record", by the author of the corrections. The tree of `9a00830` equals the tree of `dcb1a19`, the fix you reviewed (`FAIL`, finding 2 remained). The author's report: `reports/author-correction-2-report.md`. Read from your own clone of `2e83447`, not from the worktree's working tree.

## What the correction had to do (the remarks it binds)

The human's answer is in `reports/correction-2-remarks.md`; the part that binds code, word for word:

> 1. (a) Allow the dependency: remove the debt record (the invariant `installation-instruction-files-dependency`) and add the instruction-file checker's part to the installer part's list of allowed dependencies in the part map, citing settlement 5 of the task. Then run what has not run on the final code: the comparison of the foundation with the code, a merge with the target branch if it moved, and the wait for the CI run.

The rest is the orchestrator's. `origin/foundations` has not moved from `7f5c5a5` since the merge `3eacbc1` you reviewed (the worktree is 21 commits ahead and 0 behind), so no merge is reviewed. The review of the whole change is replaced here by this review of the correction; the review of the fix's earlier part (finding 1) you accepted.

## What to judge

1. That the correction does what the answer asks and nothing else: the invariant `installation-instruction-files-dependency` is gone whole and no tracked file refers to it; `instruction-files` stands in the *Depends on* of `installation` in `foundations/part_map.md`, in the file's form; no other line of either file, and no file besides these two, changed (compare with `9a00830`).
2. The citation. The map's form has no field for one, so the author wrote the citation of settlement 5 in the commit message. Judge whether that satisfies "citing settlement 5 of the task" as far as the foundation's forms allow, or whether the foundation's form calls for the citation somewhere in the map or the entries.
3. Your finding 2 of the review of the merge: that this correction resolves it (the part map now allows the reach the task meant, and no recorded rule contradicts the task's settlement), and that nothing of the fix `dcb1a19` that you accepted (finding 1: the five places of the CI rule that defer to WAY-261) is changed.
4. The author's note that `instruction-files` already lists `installation` in its *Depends on*, so the two parts now allow each other. Judge whether the foundation (the part-map template and its skill, WAY-225, WAY-44, the glossary entry "dependency of a part", the checks) says anything against two parts allowing each other, and whether this creates a finding.
5. Your Minor finding 3 (two more reaches no *Depends on* allows) and the Minor finding of the review of the fix stand unfixed by design; do not count them against this correction.
6. The foundation check on the corrected tree (`python -B elements/common/foundation_check.py` without `--skip-test-citations`) and the tests of `elements/part-map` and `elements/common`, one directory at a time.

The author's gaps, carried to you: it did not read WAY-11 whole in this correction, and it did not use the decision index script for its selection; select your own foundation as your method gives.

## Your report

`reports/review-correction-2-report.md`, first line `PASS <sha>` or `FAIL <sha>` (the sha of `2e83447`); findings with grades and places (the reviewer alone grades and scopes); the checks with command and exit code; **Unread material**; **Searches not found or unclear**; working copies and their removal. No secrets or personal data.

## Working copies (word for word from the cycle's skill)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed, except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md` says, to the place the product's foundation settles for screenshots, and into the agent's directory only where no such place is settled. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed.
