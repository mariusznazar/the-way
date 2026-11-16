# Handoff — the return step for correction 1 (the one author, resumed)

You are the one author, resumed, for the return step of correction 1. Nothing here is the human's approval.

- Worktree: `the task's worktree`, branch `task/ci-replaces-local-final-gate`, head `cdfcf480a4751a10fe57a198d9ed41b553fe67af`. The correction made one commit, `cdfcf48`, that changes `guidelines/coding-shared-module.md` (its *Applies to* line and its "Where in code" section). Do not push.
- Stage: the return step, repeated only for what the correction touches (the correction's rule). Read `task-cycle/skill/return_step.md` whole and follow it, with `task-cycle/skill/foundation_step.md`. Compare the foundation entries that bear on this file and its kind (the decisions that adopt the kind `shared-module`, the invariant `shared-module-import-runs-nothing`, the part map entries of `process-audit` and `relation-model`) with the files, and correct in the same change whatever no longer matches; a guidelines file is no foundation entry, so `none` is a likely answer.
- The remarks: `reports/correction-1-remarks.md`; your report of the correction: `reports/author-correction-report.md`.
- Do not run the full gate. `python -B elements/common/foundation_check.py` with its exit code.
- Report: `docs/task-cycles/ci-replaces-local-final-gate/reports/author-correction-return-step-report.md`, in the form `return_step.md` gives, with **Unread material**, **Searches not found or unclear** and the working copies line. Return status, commits (none if nothing was corrected), a one-line check result, report path.
- Your directory for working copies: `.runs/author-correction-return-step/`.

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
