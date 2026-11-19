# Handoff - reviewer of slice 2 (stage: review-change)

## Delegation

The person who requested this cycle has delegated every intermediate choice to the orchestrator. You never
ask the human. You did not make the change; you review it and change nothing (read-only). You alone grade
and scope your findings.

## What you review

- Method: `task-cycle/review/SKILL.md` of the worktree (`review-change`), read whole; read a file it names
  only when the step or variant that names it comes. This is the review of a planned slice (slice 2), not of the whole change.
- The worktree: `the worktree's root` (branch
  `task/code-order-formatter-linter-size`). Work from its root. Range to review: base `6c13454c` to head `015ce05c`;
  compute the diff yourself (`git diff 6c13454c..015ce05c`, `git log 6c13454c..015ce05c`).
- The executor's report, a set of claims to verify, not evidence:
  `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-2-report.md`.
- Your directory for working copies: `.runs/review-2/`. Your report:
  `.runs/task-cycles/code-order-formatter-linter-size/reports/review-2-report.md`; its first line is `PASS <sha>` or `FAIL <sha>`
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

- `foundations/decisions.md:9604-9639` WAY-205

### Slice 2 — the one reformatting

- **Goal:** one commit holds the output of `<ruff> format --config ruff.toml --no-cache`, run over
  the `.py` files git tracks in the parts WAY-379 names (`git ls-files` of `*.py`), and no other
  change; its subject says that it is the reformatting by `ruff format` and nothing else, so that
  Slice 3 and the orchestrator find its hash. The slice commits nothing else. No file is edited by
  hand, and no later slice changes this commit or makes a commit that mixes this reformatting with
  another change. Behaviour does not change: every changed file parses to the same syntax tree as
  before. Until Slice 4, run no test of `elements/common` (WAY-321: F3 and F4 have no citing test
  yet).
- **Change:** `agent-instructions/*.py` · `elements/**/*.py` · `gate/*.py` · `installation/*.py` ·
  `instruction-files/*.py` · `process-audit/*.py` · `product-guidelines/*.py` ·
  `project-level/*.py` · `relation-model/*.py` · `task-cycle/*.py`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:29-29` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:69-73` Questions to settle ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:93-93` Context ·
  `foundations/decisions.md:9602-9636` WAY-205 · F1 · F4 · `ruff.toml`
- **Model:** cheaper
- **Risk:** trust boundary — the layout of every trust-boundary file: `task-cycle/cycle_stages.py`,
  `task-cycle/cycle_measures.py`, `task-cycle/gate_times.py`, `process-audit/audit_count.py`,
  `process-audit/record_items.py`, `installation/install.py`,
  `instruction-files/check_instructions.py`, `project-level/readiness_check.py`,
  `project-level/plan_check.py`, `project-level/plan_state.py`
- **Checks:** `<ruff>` as in Slice 1. `<ruff> format --check --config ruff.toml --no-cache` over the
  `.py` files git tracks exits 0; `git show --stat --format= HEAD` lists only `.py` files; a script
  in the agent's working-copy directory finds that every file the commit changes parses with `ast`
  to the same tree as at the slice's base; `<ruff> check` as in Slice 1 reports the same 24 faults;
  `python -B gate/run_tests.py installation`, `… instruction-files`, `… process-audit`,
  `… project-level` and `… task-cycle` pass.
- **Depends on:** Slice 1

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

Your directory is `.runs/review-2/`.

## Your return

Return the report's first line (`PASS <sha>` or `FAIL <sha>`), the changed files with their line counts, and the report path. The report holds
**Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found
or unclear** (or `none`), reaches beyond this handoff, and your working copies with their removal.
