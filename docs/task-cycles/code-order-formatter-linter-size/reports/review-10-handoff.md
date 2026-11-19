# Handoff - reviewer of slice 10 (stage: review-change)

## Delegation

The person who requested this cycle has delegated every intermediate choice to the orchestrator. You never
ask the human. You did not make the change; you review it and change nothing (read-only). You alone grade
and scope your findings.

## What you review

- Method: `task-cycle/review/SKILL.md` of the worktree (`review-change`), read whole; read a file it names
  only when the step or variant that names it comes. This is the review of a planned slice (slice 10), not of the whole change.
- The worktree: `the worktree's root` (branch
  `task/code-order-formatter-linter-size`). Work from its root. Range to review: base `0ccdc807` to head `462add5d`;
  compute the diff yourself (`git diff 0ccdc807..462add5d`, `git log 0ccdc807..462add5d`).
- The executor's report, a set of claims to verify, not evidence:
  `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-10-report.md`.
- Your directory for working copies: `.runs/review-10/`. Your report:
  `.runs/task-cycles/code-order-formatter-linter-size/reports/review-10-report.md`; its first line is `PASS <sha>` or `FAIL <sha>`
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

- `foundations/decisions.md:2327-2367` WAY-95
- `foundations/decisions.md:1760-1805` WAY-03
- `foundations/decisions.md:2566-2595` WAY-48
- `foundations/invariants.md:538-547` gate-times-refuses-impossible-entry

### Slice 10 — "entry" kept for an entry of the foundation

- **Goal:** where the files below use "entry" for something other than an entry of the foundation,
  it gives way to a word that fits the place, and nothing else changes: the registry of running
  gates in `task-cycle/gate_times.py` (its description, comments, messages and names) and in
  `task-cycle/test_gate_times.py` (the names and comments of the tests of
  `gate-times-refuses-impossible-entry`, whose identifier stays), in the word F7 and F8 use; "their
  change-log entries" in `project-level/lead/skill/SKILL.md`, in the word F6 uses; the phrase
  "file/entry/section" in `project-level/lead/conversation_template.md` and
  `project-level/lead/answering.md`; and the names of about 24 tests and the comment "a doubled
  item, an entry in neither form, a findings file named twice" in
  `process-audit/test_record_items.py`, where "entry" is an item of a list under the record's items,
  a sub-item since the pull request #148. The uses Context of the task keeps stay: the output of
  `git worktree list`, git's trees, session transcripts, the entries of the decision log in the
  scripts that compare it, "entry point". No word gets a glossary entry (WAY-95). The behaviour of
  `gate_times.py` — its exit codes, the files of the registry and what it deletes — does not change.
  The description of the skill does not change, so no skill entry point is written. The changed
  `.py` files are formatted as Slice 3 gives.
- **Change:** `task-cycle/gate_times.py` · `task-cycle/test_gate_times.py` ·
  `project-level/lead/skill/SKILL.md` · `project-level/lead/conversation_template.md` ·
  `project-level/lead/answering.md` · `process-audit/test_record_items.py`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:36-36` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:96-96` Context · F6 · F7 · F8 ·
  `foundations/invariants.md:518-526` gate-times-refuses-impossible-entry ·
  `foundations/decisions.md:2326-2365` WAY-95 · `foundations/decisions.md:1759-1803` WAY-03 ·
  `foundations/decisions.md:2565-2593` WAY-48 · `foundations/glossary.md:49-53` entry ·
  `foundations/part_map.md:81-112` project-level, task-cycle · `foundations/part_map.md:125-136`
  process-audit · `guidelines/coding.md` · `guidelines/coding-command-runner.md` ·
  `guidelines/testing.md`
- **Model:** cheaper
- **Risk:** trust boundary — `task-cycle/gate_times.py`
- **Checks:** `<ruff>` as in Slice 1. `python -B gate/run_tests.py task-cycle`, `… process-audit` and
  `… project-level` pass; a search for `entr` in the six files finds none of the uses this slice
  replaces; `<ruff> format --check --config ruff.toml` and `<ruff> check --config ruff.toml --ignore-noqa`
  on the changed `.py` files exit 0; `python -B elements/common/foundation_check.py` exits 0.
- **Depends on:** Slice 3 · F6 · F7 · F8

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

Your directory is `.runs/review-10/`.

## Your return

Return the report's first line (`PASS <sha>` or `FAIL <sha>`), the changed files with their line counts, and the report path. The report holds
**Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found
or unclear** (or `none`), reaches beyond this handoff, and your working copies with their removal.
