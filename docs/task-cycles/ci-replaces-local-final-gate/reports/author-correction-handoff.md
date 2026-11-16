# Handoff — correction 1 for the human's remarks (the one author, resumed)

You are the one author, resumed, for a correction after the human's remarks on the open request. The remarks bind. Nothing here is more than that.

- Worktree: `the task's worktree`, branch `task/ci-replaces-local-final-gate`, head `026308ff53ac44fe7ba43862974435d017f3891e` (the code is the code at `c6452215e40a32da2a9b65d79412e9fb2ec4e4b6`; the commits above it only add and remove the record). The remote target branch `foundations` stands at `8f0c1c3`, already in the branch: no merge. Do not push.
- Method: `task-cycle/change/SKILL.md`, variant "a correction for the human's remarks".
- The remarks, word for word: `reports/correction-1-remarks.md` (full path `docs/task-cycles/ci-replaces-local-final-gate/reports/correction-1-remarks.md`). Read it whole. What is yours: remark 2 — of the eight Minor findings, fix N-3 only: add the line in the guidelines that places `process-audit/stage_pricing.py` under the kind `shared-module` (its *Applies to* in `guidelines/coding-shared-module.md`, beside `relation-model`). The review's wording of N-3 is in `reports/review-fix-report.md`; the human's remark is the bound. Make the smallest change that places the file under the kind: the *Applies to* line, and, only where the file's own table of files of the kind or its section "Where in code" would otherwise contradict it, that line too; add no rule, no exemplar mark and no decision, and say in the report what you added and why each addition was needed. The other seven Minor findings are let through: change nothing for them. Remark 1 (the request's state and the human action) and the acceptance of items 3 and 4 are the orchestrator's, in the description; leave the environment fact `foundations-branch-ruleset` as it is.
- Read whole before you change it: `guidelines/coding-shared-module.md`; and `guidelines/coding.md` (the kind index) and `product-guidelines/reading.md` (how a guideline's *Applies to* is read). Search the repository once for what names this file's *Applies to* or the kind `shared-module` (tests of the guidelines' form, the invariant `shared-module-import-runs-nothing`, the decisions that adopt the kind) and report what the new *Applies to* changes for them.
- Checks: run the directories whose tests read the guidelines (`product-guidelines`, `agent-instructions`, `process-audit`, `elements/part-map`, and any the search names) with `python -B gate/run_tests.py <directory>`, and `python -B elements/common/foundation_check.py`; not the full gate (the orchestrator's alone). Commit the change by path; commit message in English.
- Report: `docs/task-cycles/ci-replaces-local-final-gate/reports/author-correction-report.md`: each remark answered, what the new *Applies to* does to the tests and entries the search found, the checks with command and exit code, **Unread material**, **Searches not found or unclear**, the own-work check, the working copies line. Return status, commits, a one-line check result, report path.
- Your directory for working copies: `.runs/author-correction/`.

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
