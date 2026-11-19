# Handoff - reviewer of slice 11 (stage: review-change)

## Delegation

The person who requested this cycle has delegated every intermediate choice to the orchestrator. You never
ask the human. You did not make the change; you review it and change nothing (read-only). You alone grade
and scope your findings.

## What you review

- Method: `task-cycle/review/SKILL.md` of the worktree (`review-change`), read whole; read a file it names
  only when the step or variant that names it comes. This is the review of a planned slice (slice 11), not of the whole change.
- The worktree: `the worktree's root` (branch
  `task/code-order-formatter-linter-size`). Work from its root. Range to review: base `462add5d` to head `679112e3`;
  compute the diff yourself (`git diff 462add5d..679112e3`, `git log 462add5d..679112e3`).
- The executor's report, a set of claims to verify, not evidence:
  `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-11-report.md`.
- Your directory for working copies: `.runs/review-11/`. Your report:
  `.runs/task-cycles/code-order-formatter-linter-size/reports/review-11-report.md`; its first line is `PASS <sha>` or `FAIL <sha>`
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
- `foundations/invariants.md:321-330` installation-paths-through-links
- `foundations/invariants.md:558-567` check-instructions-refuses-outside-links
- `foundations/invariants.md:248-261` project-plan-form
- `foundations/invariants.md:331-347` project-plan-state-evidence

### Slice 11 — four over-long functions at three parts' trust boundaries divided

- **Goal:** each of these functions stands at most 110 lines (F2), counted as the size test counts,
  by moving parts of it out into functions of the same file, each part with a name of its own
  (`guidelines/coding.md`, *Good* of the rule of size), with no change of behaviour, exit codes or
  messages: `run` of `installation/install.py` (149 lines after the reformatting),
  `check_file` of `instruction-files/check_instructions.py` (137), `check_header` of
  `project-level/plan_check.py` (123), and `provenance` (130) and `task_report` (140) of
  `project-level/plan_state.py`. The changed files are formatted as Slice 3 gives.
- **Change:** `installation/install.py` · `instruction-files/check_instructions.py` ·
  `project-level/plan_check.py` · `project-level/plan_state.py`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:32-32` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:62-68` Questions to settle · F2 ·
  `foundations/decisions.md:6615-6651` WAY-365 · `foundations/decisions.md:2565-2593` WAY-48 ·
  `foundations/invariants.md:438-446` function-and-file-size ·
  `foundations/invariants.md:311-319` installation-paths-through-links ·
  `foundations/invariants.md:538-546` check-instructions-refuses-outside-links ·
  `foundations/invariants.md:238-250` project-plan-form ·
  `foundations/invariants.md:321-336` project-plan-state-evidence ·
  `foundations/part_map.md:81-100` project-level · `foundations/part_map.md:183-203`
  instruction-files, installation · `guidelines/coding.md` · `guidelines/coding-check.md` ·
  `guidelines/coding-measuring-report.md` · `guidelines/coding-repository-changer.md` ·
  `agent-instructions/test_size_invariant.py`
- **Model:** same — four trust boundaries in three parts, each divided where its parts have a name
  of their own
- **Risk:** trust boundary — `installation/install.py`, `instruction-files/check_instructions.py`,
  `project-level/plan_check.py`, `project-level/plan_state.py`
- **Checks:** `<ruff>` as in Slice 1. The counting of `function_sizes` of
  `agent-instructions/test_size_invariant.py`, run on the four files, finds no function over 110
  lines; `python -B gate/run_tests.py installation`, `… instruction-files` and `… project-level`
  pass; `<ruff> format --check --config ruff.toml` and `<ruff> check --config ruff.toml --ignore-noqa`
  on the four files exit 0.
- **Depends on:** Slice 5 · F2

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

Your directory is `.runs/review-11/`.

## Your return

Return the report's first line (`PASS <sha>` or `FAIL <sha>`), the changed files with their line counts, and the report path. The report holds
**Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found
or unclear** (or `none`), reaches beyond this handoff, and your working copies with their removal.
