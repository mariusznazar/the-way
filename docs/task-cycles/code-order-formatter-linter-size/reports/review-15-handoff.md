# Handoff - reviewer of slice 15 (stage: review-change)

## Delegation

The person who requested this cycle has delegated every intermediate choice to the orchestrator. You never
ask the human. You did not make the change; you review it and change nothing (read-only). You alone grade
and scope your findings.

## What you review

- Method: `task-cycle/review/SKILL.md` of the worktree (`review-change`), read whole; read a file it names
  only when the step or variant that names it comes. This is the review of a planned slice (slice 15), not of the whole change.
- The worktree: `the worktree's root` (branch
  `task/code-order-formatter-linter-size`). Work from its root. Range to review: base `efc2f090` to head `95316c25`;
  compute the diff yourself (`git diff efc2f090..95316c25`, `git log efc2f090..95316c25`).
- The executor's report, a set of claims to verify, not evidence:
  `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-15-report.md`.
- Your directory for working copies: `.runs/review-15/`. Your report:
  `.runs/task-cycles/code-order-formatter-linter-size/reports/review-15-report.md`; its first line is `PASS <sha>` or `FAIL <sha>`
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
- `foundations/invariants.md:458-467` function-and-file-size
- `foundations/invariants.md:548-557` audit-count-refuses-record-links
- `foundations/invariants.md:358-367` cross-part-imports

### Slice 15 — the register of problems and the reading of records moved out of the audit's command

- **Goal:** two parts of `process-audit/audit_count.py` move into new modules, with no change of
  behaviour, exit codes, messages or the bytes of the report: the register of problems — from
  `Problem` to `read_register` at the base, with what only it uses — into
  `process-audit/problem_register.py`, and the reading of a cycle's record and of its files from
  git — from `header_fields` to `read_gate` at the base, with the classes they fill and the
  constants only they use; `fill` and `read_repository` move too where the cut needs them — into
  `process-audit/record_reading.py`. On the way `read_gate` (153 lines) is divided to at most 110
  (F2), each part with a name of its own. A module never imports `audit_count.py`: what both need
  moves into a module, and `audit_count.py` imports what it uses. A name that
  `process-audit/test_audit_count.py` or `process-audit/test_audit_series_scripts.py` reaches as
  `audit_count.<name>` (`Git`, `GitError`, `Cycle`, `fill`, `Prices`, `Version`, `Ancestry`,
  `cost_boundary`, `count_boundary`, `Register`, `instrument_series`, `read_contradiction`,
  `remarks_check`, `COST_SCRIPT`, `COST_SCRIPTS`, `COUNT_PATHS`, `MEASURES_SCRIPT`, `GATE_SCRIPT`,
  `GATE_TEST_RUNNER`, `TOOL_GROUPS`) and that `audit_count.py` no longer uses itself stays
  importable from it until Slice 17, by an import that `__all__` of `audit_count.py` names, never
  by a `noqa`; Slice 18 removes it. The tests do not change. Each module's description says, as that
  of `process-audit/stage_pricing.py` does, what it holds, that it was moved out of
  `audit_count.py` and that it is imported, never run, and importing it runs nothing (the rule of
  the kind `shared-module`). The description of `audit_count.py` stays whole there.
  `foundations/part_map.md` names both modules among the *Trust boundary* files of `process-audit`,
  since they read the user's register and the records of cycles (WAY-48). The changed `.py` files
  are formatted as Slice 3 gives.
- **Change:** `process-audit/audit_count.py` · `process-audit/problem_register.py` ·
  `process-audit/record_reading.py` · `foundations/part_map.md`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:32-32` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:108-108` Questions carried to cycle ·
  F2 · `foundations/decisions.md:6615-6651` WAY-365 · `foundations/decisions.md:2565-2593` WAY-48 ·
  `foundations/invariants.md:438-446` function-and-file-size ·
  `foundations/invariants.md:528-536` audit-count-refuses-record-links ·
  `foundations/invariants.md:348-356` cross-part-imports · `foundations/invariants.md:126-134`
  script-imports · `foundations/part_map.md:125-136` process-audit ·
  `foundations/part_map.md:262-269` External context · `guidelines/coding.md` ·
  `guidelines/coding-measuring-report.md` · `guidelines/coding-shared-module.md` ·
  `process-audit/stage_pricing.py:1-7` · `process-audit/test_audit_series_scripts.py` ·
  `process-audit/test_audit_count.py:2345-2366` · `process-audit/test_audit_count.py:3536-3616` ·
  `process-audit/test_audit_count.py:3780-3800` · `process-audit/test_audit_count.py:4060-4140` ·
  `process-audit/test_audit_count.py:4340-4350` · `agent-instructions/test_size_invariant.py`
- **Model:** same — orchestrator's change to the planner's `cheaper`: the slice moves two parts of a 3600-line script at a trust boundary into modules and divides a 153-line function, with a transitional `__all__` that must be exact
- **Risk:** trust boundary — `process-audit/audit_count.py`, `process-audit/problem_register.py`,
  `process-audit/record_reading.py`
- **Checks:** `<ruff>` as in Slice 1. `python -B gate/run_tests.py process-audit` and
  `… elements/part-map` pass; the counting of `function_sizes` and `file_lines` of
  `agent-instructions/test_size_invariant.py`, run on the two modules, finds no function over 110
  lines and no file over 1200; a new interpreter that imports each module with its input empty ends
  with exit code 0 and writes nothing; `<ruff> format --check --config ruff.toml` and
  `<ruff> check --config ruff.toml --ignore-noqa` on the three `.py` files exit 0;
  `python -B elements/common/foundation_check.py` exits 0.
- **Depends on:** Slice 14 · Slice 13 · Slice 5 · F2

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

Your directory is `.runs/review-15/`.

## Your return

Return the report's first line (`PASS <sha>` or `FAIL <sha>`), the changed files with their line counts, and the report path. The report holds
**Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found
or unclear** (or `none`), reaches beyond this handoff, and your working copies with their removal.
