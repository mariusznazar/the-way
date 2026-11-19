# Handoff - reviewer of slice 16 (stage: review-change)

## Delegation

The person who requested this cycle has delegated every intermediate choice to the orchestrator. You never
ask the human. You did not make the change; you review it and change nothing (read-only). You alone grade
and scope your findings.

## What you review

- Method: `task-cycle/review/SKILL.md` of the worktree (`review-change`), read whole; read a file it names
  only when the step or variant that names it comes. This is the review of a planned slice (slice 16), not of the whole change.
- The worktree: `the worktree's root` (branch
  `task/code-order-formatter-linter-size`). Work from its root. Range to review: base `95316c25` to head `a30a04ff`;
  compute the diff yourself (`git diff 95316c25..a30a04ff`, `git log 95316c25..a30a04ff`).
- The executor's report, a set of claims to verify, not evidence:
  `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-16-report.md`.
- Your directory for working copies: `.runs/review-16/`. Your report:
  `.runs/task-cycles/code-order-formatter-linter-size/reports/review-16-report.md`; its first line is `PASS <sha>` or `FAIL <sha>`
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

- `foundations/decisions.md:6616-6653` WAY-365
- `foundations/decisions.md:2566-2595` WAY-48
- `foundations/decisions.md:8400-8537` WAY-339
- `foundations/invariants.md:458-467` function-and-file-size
- `foundations/invariants.md:408-417` audit-series-script-paths
- `foundations/invariants.md:358-367` cross-part-imports

### Slice 16 — the analysis of versions and the report moved out of the audit's command

- **Goal:** two more parts of `process-audit/audit_count.py` move into new modules, with no change
  of behaviour, exit codes, messages or the bytes of the report: the analysis of the versions of the
  process — from `Ancestry` at the base through `analyse`, the versions, series and boundaries, to
  `process_versions`, with the constants of the series (`COST_SCRIPT`, `COST_SCRIPTS`,
  `COUNT_PATHS`, `MEASURES_SCRIPT`, the scripts of the gate times, `GATE_TEST_RUNNER`,
  `TOOL_GROUPS`) and their comments — into `process-audit/version_analysis.py`, and the writing of
  the report — from `count_rows` at the base to `render` and `write` — into
  `process-audit/audit_report.py`. On the way `analyse` (219 lines) and `render` (206) are divided to
  at most 110 lines each (F2), each part with a name of its own. After this slice
  `audit_count.py` and every module moved out of it stand at most 1200 lines and no function of them
  over 110. A module never imports `audit_count.py`. Names the tests reach as
  `audit_count.<name>`, as Slice 15 lists them, stay importable through `__all__` of
  `audit_count.py` until Slice 17, never by a `noqa`; the tests do not change. Each module's
  description says what it holds, that it was moved out of `audit_count.py` and that it is imported,
  never run, and importing it runs nothing. Neither module reads input from outside the product, so
  neither is a trust boundary (WAY-48) and the part map does not change. The changed `.py` files are
  formatted as Slice 3 gives.
- **Change:** `process-audit/audit_count.py` · `process-audit/version_analysis.py` ·
  `process-audit/audit_report.py`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:32-32` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:108-108` Questions carried to cycle ·
  F2 · `foundations/decisions.md:6615-6651` WAY-365 · `foundations/decisions.md:2565-2593` WAY-48 ·
  `foundations/decisions.md:8399-8534` WAY-339 ·
  `foundations/invariants.md:438-446` function-and-file-size ·
  `foundations/invariants.md:398-406` audit-series-script-paths ·
  `foundations/invariants.md:348-356` cross-part-imports · `foundations/part_map.md:125-136`
  process-audit · `foundations/part_map.md:262-269` External context · `guidelines/coding.md` ·
  `guidelines/coding-measuring-report.md` · `guidelines/coding-shared-module.md` ·
  `process-audit/stage_pricing.py:1-7` · `process-audit/test_audit_series_scripts.py` ·
  `agent-instructions/test_size_invariant.py`
- **Model:** same — orchestrator's change to the planner's `cheaper`: the slice divides two functions of 219 and 206 lines (the largest of the change) and moves the analysis of versions and the report into two modules
- **Risk:** trust boundary — `process-audit/audit_count.py`
- **Checks:** `<ruff>` as in Slice 1. `python -B gate/run_tests.py process-audit` and
  `… elements/part-map` pass; the counting of `function_sizes` and `file_lines` of
  `agent-instructions/test_size_invariant.py`, run on `audit_count.py` and on the four modules moved
  out of it, finds no function over 110 lines and no file over 1200; a new interpreter that imports
  each new module with its input empty ends with exit code 0 and writes nothing;
  `<ruff> format --check --config ruff.toml` and `<ruff> check --config ruff.toml --ignore-noqa` on
  the three `.py` files exit 0.
- **Depends on:** Slice 15 · F2

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

Your directory is `.runs/review-16/`.

## Your return

Return the report's first line (`PASS <sha>` or `FAIL <sha>`), the changed files with their line counts, and the report path. The report holds
**Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found
or unclear** (or `none`), reaches beyond this handoff, and your working copies with their removal.
