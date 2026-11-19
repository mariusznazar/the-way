# Handoff — executor-12 (stage: make-change, a slice, or the retry of a slice)

## Delegation

The person who requested this cycle has delegated every intermediate choice to the orchestrator.
You never ask the human; a question goes back to the orchestrator in your report, with the ways open and
what each costs. Never label an answer as the human's approval. The cycle's own rule on a test that
contradicts the requirement binds you (`task-cycle/change/SKILL.md`, section 2).

## Where you work

- The worktree: `the worktree's root` (branch
  `task/code-order-formatter-linter-size`). Work from its root. The-way is the repository itself.
- Your slice's base: `679112e3bf1225559d129d949473e12ed6520546` (written in the record before this dispatch). Your range runs from there.
- Your directory for working copies: `.runs/executor-12/` of the worktree.
- Your report: `.runs/task-cycles/code-order-formatter-linter-size/reports/executor-12-report.md`.
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

### Slice 12 — the over-long check of a request's description divided

- **Goal:** `check` of `task-cycle/request_check.py` (195 lines after the reformatting) stands at
  most 110 lines (F2), counted as the size test counts, by moving parts of it out into functions of
  the same file, each with a name of its own, with no change of behaviour, exit codes or messages.
  The changed file is formatted as Slice 3 gives.
- **Change:** `task-cycle/request_check.py`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:32-32` To do · F2 ·
  `foundations/decisions.md:6615-6651` WAY-365 ·
  `foundations/invariants.md:438-446` function-and-file-size · `guidelines/coding.md` ·
  `guidelines/coding-check.md` · `agent-instructions/test_size_invariant.py`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `<ruff>` as in Slice 1. The counting of `function_sizes` of
  `agent-instructions/test_size_invariant.py`, run on the file, finds no function over 110 lines;
  `python -B gate/run_tests.py task-cycle` passes; `<ruff> format --check --config ruff.toml` and
  `<ruff> check --config ruff.toml --ignore-noqa` on the file exit 0.
- **Depends on:** Slice 3 · F2

## Current ranges of the decisions and invariants the slice reads

- `foundations/decisions.md:6616-6653` WAY-365
- `foundations/invariants.md:458-467` function-and-file-size

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

Your directory is `.runs/executor-12/`.

## Your return

Return: status (`done`, `done with concerns`, `questions`, `returned`, `reserved` or `blocked`), your
commits, a one-line check result naming what failed or did not run, and the report's path. The report holds
each check with its command and exit code, the own-work check `make-change` gives (WAY-164), the weakest
point you checked, your **Unread material** (what this handoff names that stayed unread or was read in
part, or `none`), **Searches not found or unclear** (or `none`), reaches beyond this handoff, and your
working copies with their removal.
