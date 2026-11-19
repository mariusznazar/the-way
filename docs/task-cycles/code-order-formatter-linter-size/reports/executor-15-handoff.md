# Handoff — executor-15 (stage: make-change, a slice, or the retry of a slice)

## Delegation

The person who requested this cycle has delegated every intermediate choice to the orchestrator.
You never ask the human; a question goes back to the orchestrator in your report, with the ways open and
what each costs. Never label an answer as the human's approval. The cycle's own rule on a test that
contradicts the requirement binds you (`task-cycle/change/SKILL.md`, section 2).

## Where you work

- The worktree: `the worktree's root` (branch
  `task/code-order-formatter-linter-size`). Work from its root. The-way is the repository itself.
- Your slice's base: `efc2f0901eefd5e63df6132bd95d484b76a9fdc4` (written in the record before this dispatch). Your range runs from there.
- Your directory for working copies: `.runs/executor-15/` of the worktree.
- Your report: `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-15-report.md`.
- `cycle.md` and the other files of the record directory — other agents' handoffs, reports and
  findings — are not yours to read, except those this handoff names.

## Method and variant

- Method: `task-cycle/change/SKILL.md` of the worktree (`make-change`). Variant: "a slice, or the retry of a slice". Read the
  `SKILL.md` whole; read a file it names only when the step or variant that names it comes.
- Boundary: you make this one slice and nothing beyond its *Change*; you return before any review.
  Commit on the task branch, by path (`git add <path> ...`, never `git add -A`, `.` or `commit -a`), with
  English commit messages that say what the commit does.
- Do NOT run the full gate: never `python -B gate/run_tests.py` without a directory argument. Its run is
  the orchestrator's or CI's (WAY-160). The focused checks named in your slice, such as
  `python -B gate/run_tests.py <directory>`, you run, each with its command and exit code in your report.
- `<ruff>` of the slice's *Checks* is `the Ruff of the quality environment of the main checkout` (the main
  checkout's quality environment; `ruff.toml` pins its version).
- A file with a trust boundary (the part map names them: `task-cycle/cycle_stages.py`,
  `task-cycle/cycle_measures.py`, `task-cycle/gate_times.py`, `process-audit/audit_count.py`,
  `process-audit/record_items.py`, `installation/install.py`, `instruction-files/check_instructions.py`,
  `project-level/readiness_check.py`, `project-level/plan_check.py`, `project-level/plan_state.py`) must give the
  same verdict, exit code and message for the same input after your change as before it; where your slice
  touches one, compare crafted input before and after and report it.
- Where a `.py` file is changed by this slice after the reformatting commit (slice 2), its layout is
  the formatter's, made by `<ruff> format --config ruff.toml <file>` on the changed files only.

## The foundation entries written earlier

F1 = decision WAY-382; F2 = decision WAY-385; F3 = invariant `own-foundation-check-report`; F4 = invariant `formatter-layout`; F5 = decision WAY-379 (its Verification); F6 = decision WAY-145; F7 = decision WAY-350; F8 = invariant `gate-times-refuses-impossible-entry`; F9 = decision WAY-339 and invariant `audit-series-script-paths`. All nine were written by the commits `9c093516` and `00945f93` and stand in `foundations/`; words chosen for slice 10: "line" for the plan's log of changes, "file" for the registry of running gates.

## The slice (copied word for word from `.runs/task-cycles/code-order-formatter-linter-size/plan.md`)

The plan is `.runs/task-cycles/code-order-formatter-linter-size/plan.md`; read the passages its *Read* names from the frozen task
`.runs/task-cycles/code-order-formatter-linter-size/task.md` by their line addresses, and the foundation entries by the current ranges below
(the foundation step moved them; where the plan's ranges differ, these hold).

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

## Current ranges of the decisions and invariants the slice reads

- `foundations/decisions.md:6616-6653` WAY-365
- `foundations/decisions.md:2566-2595` WAY-48
- `foundations/invariants.md:458-467` function-and-file-size
- `foundations/invariants.md:548-557` audit-count-refuses-record-links
- `foundations/invariants.md:358-367` cross-part-imports

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

Your directory is `.runs/executor-15/`.

## Your return

Return: status (`done`, `done with concerns`, `questions`, `returned`, `reserved` or `blocked`), your
commits, a one-line check result naming what failed or did not run, and the report's path. The report holds
each check with its command and exit code, the own-work check `make-change` gives (WAY-164), the weakest
point you checked, your **Unread material** (what this handoff names that stayed unread or was read in
part, or `none`), **Searches not found or unclear** (or `none`), reaches beyond this handoff, and your
working copies with their removal.
