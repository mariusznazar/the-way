# Handoff — executor-5 (stage: make-change, a slice, or the retry of a slice)

## Delegation

The person who requested this cycle has delegated every intermediate choice to the orchestrator.
You never ask the human; a question goes back to the orchestrator in your report, with the ways open and
what each costs. Never label an answer as the human's approval. The cycle's own rule on a test that
contradicts the requirement binds you (`task-cycle/change/SKILL.md`, section 2).

## Where you work

- The worktree: `the worktree's root` (branch
  `task/code-order-formatter-linter-size`). Work from its root. The-way is the repository itself.
- Your slice's base: `2620dcc39afe19eacd781e1322718ad30762dcc8` (written in the record before this dispatch). Your range runs from there.
- Your directory for working copies: `.runs/executor-5/` of the worktree.
- Your report: `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-5-report.md`.
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

## Current ranges of the decisions and invariants the slice reads

- `foundations/decisions.md:10614-10655` WAY-380
- `foundations/decisions.md:2924-3093` WAY-344
- `foundations/decisions.md:2566-2595` WAY-48
- `foundations/invariants.md:438-447` ruff-blocking-rules
- `foundations/invariants.md:321-330` installation-paths-through-links
- `foundations/invariants.md:558-567` check-instructions-refuses-outside-links
- `foundations/invariants.md:548-557` audit-count-refuses-record-links
- `foundations/invariants.md:518-527` cycle-stages-refuses-crafted-names

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

Your directory is `.runs/executor-5/`.

## Your return

Return: status (`done`, `done with concerns`, `questions`, `returned`, `reserved` or `blocked`), your
commits, a one-line check result naming what failed or did not run, and the report's path. The report holds
each check with its command and exit code, the own-work check `make-change` gives (WAY-164), the weakest
point you checked, your **Unread material** (what this handoff names that stayed unread or was read in
part, or `none`), **Searches not found or unclear** (or `none`), reaches beyond this handoff, and your
working copies with their removal.
