# Handoff - reviewer of slice 5 (stage: review-change)

## Delegation

The person who requested this cycle has delegated every intermediate choice to the orchestrator. You never
ask the human. You did not make the change; you review it and change nothing (read-only). You alone grade
and scope your findings.

## What you review

- Method: `task-cycle/review/SKILL.md` of the worktree (`review-change`), read whole; read a file it names
  only when the step or variant that names it comes. This is the review of a planned slice (slice 5), not of the whole change.
- The worktree: `the worktree's root` (branch
  `task/code-order-formatter-linter-size`). Work from its root. Range to review: base `2620dcc3` to head `8fecce81`;
  compute the diff yourself (`git diff 2620dcc3..8fecce81`, `git log 2620dcc3..8fecce81`).
- The executor's report, a set of claims to verify, not evidence:
  `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-5-report.md`.
- Your directory for working copies: `.runs/review-5/`. Your report:
  `.runs/task-cycles/code-order-formatter-linter-size/reports/review-5-report.md`; its first line is `PASS <sha>` or `FAIL <sha>`
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

- `foundations/decisions.md:10614-10655` WAY-380
- `foundations/decisions.md:2924-3093` WAY-344
- `foundations/decisions.md:2566-2595` WAY-48
- `foundations/invariants.md:438-447` ruff-blocking-rules
- `foundations/invariants.md:321-330` installation-paths-through-links
- `foundations/invariants.md:558-567` check-instructions-refuses-outside-links
- `foundations/invariants.md:548-557` audit-count-refuses-record-links
- `foundations/invariants.md:518-527` cycle-stages-refuses-crafted-names

### Slice 5 — linter faults at four trust boundaries

- **Goal:** the blocking reports of the linter in four trust-boundary files are fixed in those
  files, with no rule turned off, no `noqa` and no change of behaviour: `installation/install.py`
  (PERF102, UP022), `instruction-files/check_instructions.py` (FURB188),
  `process-audit/audit_count.py` (UP037, three) and `task-cycle/cycle_stages.py` (TRY004). For
  TRY004, `required_time` keeps what it does: a timestamp that is not a text still ends the run
  with exit code 2 and the message that the field timestamp is not a time (WAY-344), never with a
  `TypeError` that escapes, and the rule stays on (WAY-380) — the type is refused outside the `try`
  that turns `ValueError` into a missing field, or in another way that keeps the exit code and the
  message. The changed files are formatted as Slice 3 gives.
- **Change:** `installation/install.py` · `instruction-files/check_instructions.py` ·
  `process-audit/audit_count.py` · `task-cycle/cycle_stages.py`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:31-31` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:98-98` Context ·
  `foundations/decisions.md:10611-10651` WAY-380 · `foundations/decisions.md:2923-3091` WAY-344 ·
  `foundations/decisions.md:2565-2593` WAY-48 · `foundations/invariants.md:428-436` ruff-blocking-rules ·
  `foundations/invariants.md:311-319` installation-paths-through-links ·
  `foundations/invariants.md:538-546` check-instructions-refuses-outside-links ·
  `foundations/invariants.md:528-536` audit-count-refuses-record-links ·
  `foundations/invariants.md:498-506` cycle-stages-refuses-crafted-names ·
  `foundations/part_map.md:102-136` task-cycle, foundation-review, process-audit ·
  `foundations/part_map.md:183-203` instruction-files, installation · `guidelines/coding.md` ·
  `guidelines/coding-check.md` · `guidelines/coding-measuring-report.md` ·
  `guidelines/coding-repository-changer.md`
- **Model:** same — fixes at four trust boundaries in four parts, one of which (TRY004) changes
  behaviour when made the usual way
- **Risk:** trust boundary — `installation/install.py`, `instruction-files/check_instructions.py`,
  `process-audit/audit_count.py`, `task-cycle/cycle_stages.py`
- **Checks:** `<ruff>` as in Slice 1.
  `<ruff> check --config ruff.toml --no-cache --ignore-noqa` and
  `<ruff> format --check --config ruff.toml` on the four files exit 0;
  `python -B gate/run_tests.py installation`, `… instruction-files`, `… process-audit` and
  `… task-cycle` pass; once, before and after the fix, `task-cycle/cycle_stages.py` given a
  transcript, prepared in the agent's working-copy directory, whose line holds a timestamp that is a
  number, ends with exit code 2 and the same message.
- **Depends on:** Slice 3

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

Your directory is `.runs/review-5/`.

## Your return

Return the report's first line (`PASS <sha>` or `FAIL <sha>`), the changed files with their line counts, and the report path. The report holds
**Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found
or unclear** (or `none`), reaches beyond this handoff, and your working copies with their removal.
