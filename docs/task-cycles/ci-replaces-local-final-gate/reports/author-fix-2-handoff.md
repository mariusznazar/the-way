# Handoff — the fix of the failures of the first CI run of the Windows check (the one author, resumed)

You are the one author, resumed. The first CI run of the new Windows check on the request failed in 31 tests that passed on the work machine; the red result is a failed gate, and you fix it. Nothing here is the human's approval.

- Worktree: `the task's worktree`, branch `task/ci-replaces-local-final-gate`, head `33426d58864cdfa78630d5da2bf4a21540f7e9a7` (the code is the same as at `e3842146a4ed24254eb16a302284f231f0dd1801`; the two commits above it only add and remove the record). Do not push.
- Method: `task-cycle/change/SKILL.md`, variant "the fix of a review's findings" (`fix.md`).
- Findings file: `reports/ci-windows-findings.md` (full path `docs/task-cycles/ci-replaces-local-final-gate/reports/ci-windows-findings.md`): F-1, F-2, F-3 and the orchestrator's rulings that bind the fix. The log of the run: `.runs/ci-logs/windows-run-1.log` of the worktree (absolute paths of the runner inside; never copy them into a report).
- Guidelines to read whole before you change a test: `guidelines/testing.md`, and `guidelines/coding.md` for the code you may change (`task-cycle/remove_merged_worktrees.py`, `project-level/plan_state.py` or the tests), plus `guidelines/coding-repository-changer.md` if you change `remove_merged_worktrees.py`.
- Run the affected checks: `python -B gate/run_tests.py task-cycle` and `python -B gate/run_tests.py project-level` with exit codes; not the full gate.
- Report: `docs/task-cycles/ci-replaces-local-final-gate/reports/author-fix-2-report.md`: each finding answered (fixed and how, whether the test or the code was wrong, commit; or held wrong with evidence), what you reproduced of the runner's short name spelling and what stayed unchecked, the checks with command and exit code, **Unread material**, **Searches not found or unclear**, the own-work check, the working copies line. Return status, commits, a one-line check result, report path.
- Your directory for working copies: `.runs/author-fix-2/`.

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
