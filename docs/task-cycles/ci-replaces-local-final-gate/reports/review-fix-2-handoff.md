# Handoff — review of the fix of the first CI run's Windows failures

You are the reviewer of the whole change, resumed (`the-way-stage`, model `opus`). You review this fix range once.

- Worktree: `the task's worktree`, branch `task/ci-replaces-local-final-gate`.
- Method: `task-cycle/review/SKILL.md`, variant the review of a fix (`task-cycle/review/fix.md`).
- Range: from `33426d58864cdfa78630d5da2bf4a21540f7e9a7` to `c6452215e40a32da2a9b65d79412e9fb2ec4e4b6` (one commit, `c645221`: four test files; the code is otherwise the code you reviewed). Compute the diff yourself.
- Findings file the fix was given: `reports/ci-windows-findings.md` (full path `docs/task-cycles/ci-replaces-local-final-gate/reports/ci-windows-findings.md`): F-1, F-2, F-3 from the first CI run of the Windows check, with the orchestrator's rulings that bind the fix. Those are no findings of yours; judge whether the fix answers them and breaks nothing. The log of the run: `.runs/ci-logs/windows-run-1.log` (paths of the runner inside; do not copy them into your report).
- The author's fix report: `docs/task-cycles/ci-replaces-local-final-gate/reports/author-fix-2-report.md` (claims to verify). Points to judge: that the tests, not the scripts, were wrong; the use of `os.path.realpath` and `.resolve()` against what each script prints; that the skip of the bar-in-a-name test on Windows keeps its check on POSIX and names its cause; that no assertion was weakened; what its reproduction of the short temporary name showed and what stays unchecked until the next CI run.
- Guidelines: `guidelines/testing.md` whole (the changes are in tests); `guidelines/coding.md`.
- Do not run the full gate. `python -B gate/run_tests.py task-cycle` and `python -B gate/run_tests.py project-level` are yours to run, with command and exit code.
- Report: `docs/task-cycles/ci-replaces-local-final-gate/reports/review-fix-2-report.md`, first line `PASS <sha>` or `FAIL <sha>` (head `c6452215e40a32da2a9b65d79412e9fb2ec4e4b6`), with the checks you ran, **Unread material**, **Searches not found or unclear**, the working copies line. Only a new Critical or Important finding fails this review.
- Your directory for working copies: `.runs/review-fix-2/`.

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
