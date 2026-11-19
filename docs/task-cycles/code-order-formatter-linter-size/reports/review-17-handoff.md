# Handoff - reviewer of slice 17 (stage: review-change)

## Delegation

The person who requested this cycle has delegated every intermediate choice to the orchestrator. You never
ask the human. You did not make the change; you review it and change nothing (read-only). You alone grade
and scope your findings.

## What you review

- Method: `task-cycle/review/SKILL.md` of the worktree (`review-change`), read whole; read a file it names
  only when the step or variant that names it comes. This is the review of a planned slice (slice 17), not of the whole change.
- The worktree: `the worktree's root` (branch
  `task/code-order-formatter-linter-size`). Work from its root. Range to review: base `a30a04ff` to head `6c748289`;
  compute the diff yourself (`git diff a30a04ff..6c748289`, `git log a30a04ff..6c748289`).
- The executor's report, a set of claims to verify, not evidence:
  `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-17-report.md`.
- Your directory for working copies: `.runs/review-17/`. Your report:
  `.runs/task-cycles/code-order-formatter-linter-size/reports/review-17-report.md`; its first line is `PASS <sha>` or `FAIL <sha>`
  (the head you reviewed), then graded findings, the checks you ran (each with command and exit code) and the
  sections the method gives.
- `cycle.md` and other files of the record directory are not yours to read, except those named here.

## Answers of step 4 of the cycle (you are told so)

A trust boundary is touched by the change as a whole: the part map names these files as trust boundaries -
`task-cycle/cycle_stages.py`, `task-cycle/cycle_measures.py`, `task-cycle/gate_times.py`,
`process-audit/audit_count.py`, `process-audit/record_items.py`, `installation/install.py`,
`instruction-files/check_instructions.py`, `project-level/readiness_check.py`, `project-level/plan_check.py`,
`project-level/plan_state.py`. Check crafted input at the boundary files this range touches: the same input must
give the same verdict, exit code and message before and after. No operation that cannot be undone.
No full run of the gate: never `python -B gate/run_tests.py` without a directory argument; focused runs of one
directory you may make. `<ruff>` is `the Ruff of the quality environment of the main checkout`.

## The foundation entries written earlier

F1 = decision WAY-382; F2 = decision WAY-385; F3 = invariant `own-foundation-check-report`; F4 = invariant `formatter-layout`; F5 = decision WAY-379 (its Verification); F6 = decision WAY-145; F7 = decision WAY-350; F8 = invariant `gate-times-refuses-impossible-entry`; F9 = decision WAY-339 and invariant `audit-series-script-paths`. All nine were written by the commits `9c093516` and `00945f93` and stand in `foundations/`; words chosen for slice 10: "line" for the plan's log of changes, "file" for the registry of running gates.

## The slice the executor was given (copied word for word from `.runs/task-cycles/code-order-formatter-linter-size/plan.md`)

Judge the slice against the passages of the frozen task `.runs/task-cycles/code-order-formatter-linter-size/task.md` that its *Read* names by line address, and
against the entries and guideline files it names (read each whole); the current ranges of its decisions and
invariants are:

- `foundations/decisions.md:8400-8537` WAY-339
- `foundations/decisions.md:9935-9978` WAY-233
- `foundations/decisions.md:1760-1805` WAY-03
- `foundations/invariants.md:408-417` audit-series-script-paths

### Slice 17 — the tests import from the new modules, and the cost script spans two files

- **Goal:** `process-audit/test_audit_count.py` and `process-audit/test_audit_series_scripts.py`
  import each name they reached as `audit_count.<name>` from the module that now holds it.
  `COST_SCRIPTS` in `process-audit/version_analysis.py` names `task-cycle/stage_transcripts.py`
  beside `task-cycle/cycle_stages.py`, so that a change of either starts a series of the cost and
  marks a cycle that changes it as having changed the tool (F9, WAY-339); where the report names the
  script that measures the cost, it names both files. The expected values that follow from this —
  the tuple of `test_each_path_that_starts_a_series_is_a_path_git_tracks` and the set of the test of
  `audit-series-script-paths` where it holds the cost script — change with their cause in a comment:
  the script that measures the cost spans two files since Slice 13 (F9, WAY-233); the request names
  the invariant test it alters (WAY-03). No other expected value changes. The changed files are
  formatted as Slice 3 gives.
- **Change:** `process-audit/test_audit_count.py` · `process-audit/test_audit_series_scripts.py` ·
  `process-audit/version_analysis.py` · `process-audit/SKILL.md` (orchestrator's addition, from the
  report of the agent of the entries: line 54 names `task-cycle/cycle_stages.py` alone as the script
  that measures the cost; it names both files, as F9 does, and nothing else of the skill changes)
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:32-32` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:108-108` Questions carried to cycle ·
  F9 · `foundations/decisions.md:8399-8534` WAY-339 · `foundations/decisions.md:9933-9975` WAY-233 ·
  `foundations/decisions.md:1759-1803` WAY-03 ·
  `foundations/invariants.md:398-406` audit-series-script-paths · `guidelines/testing.md` ·
  `guidelines/coding.md` · `guidelines/coding-shared-module.md`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `<ruff>` as in Slice 1. `python -B gate/run_tests.py process-audit` passes; a search of
  the two test files finds no `audit_count.` before a name that moved;
  `<ruff> format --check --config ruff.toml` and `<ruff> check --config ruff.toml --ignore-noqa` on
  the three files exit 0; `python -B elements/common/foundation_check.py` exits 0 and lists no
  reworded invariant whose test was left as it was.
- **Depends on:** Slice 16 · Slice 13 · F9

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

Your directory is `.runs/review-17/`.

## Your return

Return the report's first line (`PASS <sha>` or `FAIL <sha>`), the changed files with their line counts, and the report path. The report holds
**Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found
or unclear** (or `none`), reaches beyond this handoff, and your working copies with their removal.
