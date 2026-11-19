# Handoff — executor-10 (stage: make-change, a slice, or the retry of a slice)

## Delegation

The person who requested this cycle has delegated every intermediate choice to the orchestrator.
You never ask the human; a question goes back to the orchestrator in your report, with the ways open and
what each costs. Never label an answer as the human's approval. The cycle's own rule on a test that
contradicts the requirement binds you (`task-cycle/change/SKILL.md`, section 2).

## Where you work

- The worktree: `the worktree's root` (branch
  `task/code-order-formatter-linter-size`). Work from its root. The-way is the repository itself.
- Your slice's base: `0ccdc807dd43b0459589d895d691aed28788edd5` (written in the record before this dispatch). Your range runs from there.
- Your directory for working copies: `.runs/executor-10/` of the worktree.
- Your report: `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-10-report.md`.
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

## Current ranges of the decisions and invariants the slice reads

- `foundations/decisions.md:2327-2367` WAY-95
- `foundations/decisions.md:1760-1805` WAY-03
- `foundations/decisions.md:2566-2595` WAY-48
- `foundations/invariants.md:538-547` gate-times-refuses-impossible-entry

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

Your directory is `.runs/executor-10/`.

## Your return

Return: status (`done`, `done with concerns`, `questions`, `returned`, `reserved` or `blocked`), your
commits, a one-line check result naming what failed or did not run, and the report's path. The report holds
each check with its command and exit code, the own-work check `make-change` gives (WAY-164), the weakest
point you checked, your **Unread material** (what this handoff names that stayed unread or was read in
part, or `none`), **Searches not found or unclear** (or `none`), reaches beyond this handoff, and your
working copies with their removal.
