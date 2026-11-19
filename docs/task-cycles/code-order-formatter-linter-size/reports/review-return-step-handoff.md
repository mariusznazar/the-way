# Handoff - reviewer of the return step (stage: review-change, the return step's commits)

## Delegation

The person who requested this cycle has delegated every intermediate choice to the orchestrator. You never ask the human. You did not make the change; you review it and change nothing (read-only). You alone grade and scope your findings.

## What you review

- Method: `task-cycle/review/SKILL.md` of the worktree (`review-change`), read whole; the return step's commits are reviewed as its section 2 gives, against the task and the foundation entries the return step writes or corrects.
- The worktree: `the worktree's root`. Range: `2e066ab4..d41712a6` (the return step made one commit; compute the diff yourself). The return step's report, a set of claims to verify, not evidence: `.runs/task-cycles/code-order-formatter-linter-size/reports/return-step-report.md`. Its handoff and method: `reports/return-step-handoff.md`, `task-cycle/skill/return_step.md`.
- The frozen task: `.runs/task-cycles/code-order-formatter-linter-size/task.md` (read whole). The change before this commit: base `d69fb20b` to `2e066ab4`, reviewed whole as `PASS 2e066ab4` (`reports/review-whole-fix-report.md`).
- Judge: that the commit changes no word of the `### Formatter` paragraph of `guidelines/coding.md` (only the wrapping of one sentence), and that the report's claims hold: that nothing else of the entries it names, of the part map of the touched parts (every part that holds Python code, `repository`, `decisions`, `invariants`) or of the guidelines no longer matches the code. Check the claims by your own searches (old phrases such as "80 lines", "1000 lines", "known violation", "expected failure", "none - WAY-382", "settings of the linter"; the part map's *Files* and *Depends on* lines against the files and imports of the new modules `process-audit/audit_shared.py`, `record_reading.py`, `problem_register.py`, `version_analysis.py`, `audit_report.py`, `task-cycle/stage_transcripts.py`), and run `python -B elements/common/foundation_check.py` (exit 0 expected).
- Your directory for working copies: `.runs/review-return-step/`. Your report: `.runs/task-cycles/code-order-formatter-linter-size/reports/review-return-step-report.md`; its first line is `PASS <sha>` or `FAIL <sha>`; then graded findings, checks with command and exit code, **Unread material**, **Searches not found or unclear**, reaches and working copies.
- `cycle.md` and other files of the record directory are not yours to read except those named here. Do not run the full gate; focused runs of one directory you may make; wait for your runs to finish.

## Working copies (word for word)

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

Your directory is `.runs/review-return-step/`.

## Your return

Return the report's first line, the changed files with line counts and the report path.
