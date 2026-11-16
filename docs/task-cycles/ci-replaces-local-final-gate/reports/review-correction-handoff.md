# Handoff — review of correction 1

You are the reviewer of the whole change, resumed (`the-way-stage`, model `opus`). You review the correction once; the remarks stand in place of a findings file.

- Worktree: `the task's worktree`, branch `task/ci-replaces-local-final-gate`.
- Method: `task-cycle/review/SKILL.md`; the variant for a correction is read from `task-cycle/review/fix.md` (a correction for the human's remarks).
- Range: from `026308ff53ac44fe7ba43862974435d017f3891e` to `cdfcf480a4751a10fe57a198d9ed41b553fe67af` (one commit, `cdfcf48`, `guidelines/coding-shared-module.md`; the code is otherwise the code you reviewed). Compute the diff yourself.
- The human's remarks, word for word: `reports/correction-1-remarks.md` (full path `docs/task-cycles/ci-replaces-local-final-gate/reports/correction-1-remarks.md`). The bound of the review: remark 2 (fix N-3 only, the line that places `process-audit/stage_pricing.py` under the kind `shared-module`; the other seven Minor findings are let through, no task). Remark 1 and the acceptance of items 3 and 4 concern the description and the human action, not code.
- The author's report: `docs/task-cycles/ci-replaces-local-final-gate/reports/author-correction-report.md` (claims to verify). It added `process-audit/` to *Where in code* too, and no row to the table of files; judge both against the remark and the file's own conventions, and whether anything else (a test, a decision, an invariant, the kind index) now disagrees with the new *Applies to*.
- Do not run the full gate. `python -B elements/common/foundation_check.py` and single directories with `python -B gate/run_tests.py <directory>` are yours, with command and exit code.
- Report: `docs/task-cycles/ci-replaces-local-final-gate/reports/review-correction-report.md`, first line `PASS <sha>` or `FAIL <sha>` (head `cdfcf480a4751a10fe57a198d9ed41b553fe67af`), with the checks you ran, **Unread material**, **Searches not found or unclear**, the working copies line. Only a new Critical or Important finding fails this review.
- Your directory for working copies: `.runs/review-correction/`.

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
