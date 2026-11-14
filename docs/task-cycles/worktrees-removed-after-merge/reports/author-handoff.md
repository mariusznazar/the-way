# Handoff — the one author of the change (`make-change`)

You are the one author of this change, a `the-way-author` agent, dispatched by the orchestrator of a task cycle of the-way.

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. Do not ask the human anything and seek no approval; a question goes to the orchestrator in your report (status `questions`). The orchestrator's answers are never the human's approval.

## Where you work

- Worktree (your working directory; start every command from its root): `the task's worktree`
- Branch: `task/worktrees-removed-after-merge`, base commit `835344fb183fce6dbd99be486df790f1212cacf6` (`origin/foundations`). Commit on this branch only, by explicit paths (`git add <file> …`, never `git add -A`, `git add .` or `git commit -a`). Commit messages in English, like the history. Do not push, do not open a request, do not merge.
- This is the-way itself, not a product: there is no `.the-way` submodule. Every method and file of the process is read from this worktree by its path from the root.
- Your directory for working copies: `.runs/author/` (see below). Your report: `.runs/task-cycles/worktrees-removed-after-merge/reports/author-report.md`.

## Your stage and its boundary

- Method: `task-cycle/change/SKILL.md` (`make-change`), variant "the whole change as the one author". Read that `SKILL.md` whole; read a file it names only when the step or variant that names it comes.
- Make the whole change the task requires: the script and its test, the three places of `task-cycle/skill/SKILL.md` the task names, the matching change to `task-cycle/record_template.md` and `task-cycle/skill/request_template.md` where item 8 of *To do* needs them, and the foundation entries the task carries (rows 1–6 of its *Settlements to record*), by the foundation step: read `task-cycle/skill/foundation_step.md` whole and, when you write an entry of an element, that element's `SKILL.md` by the path `foundation_step.md` gives.
- Return before review. Do not run the product's full gate (`python -B gate/run_tests.py` without a directory): the orchestrator runs it. Focused checks of your own are yours: `python -B gate/run_tests.py task-cycle` and the directories your change touches, `python -B elements/common/foundation_check.py` for the foundation entries, and `python -B -m unittest` of the new test file. Each check you report carries its command and its exit code.
- The return step (comparing the foundation with the code after the change) is a later stage; do not take it now.
- Your own-work check is required by the method.

## The task

The frozen task: `.runs/task-cycles/worktrees-removed-after-merge/task.md`. Read it whole. It is in Polish; the code, its comments, its docstring, its messages and the foundation entries are in English, like the rest of the-way. The task's `Status` is `ready for cycle`; its *Human actions* are the one-off clean-up that Mariusz makes at the request, in the cycle — not yours.

Settled by the task and not to be reopened: every *Answer* under *Questions to settle*, *To do* items 1–9, *Settlements to record* rows 1–6, *Out of scope*.

## The orchestrator's answers of step 4

- Trust boundary: **no.** The files the change touches are none the part map names as a boundary, and the script works on the product's own git state (WAY-48).
- Irreversible operation: **yes.** With `--apply` the script deletes directories. The change prepares the operation and the cycle never performs it. Therefore:
  - run the script only against throwaway repositories and worktrees that you create under `.runs/author/`, never `--apply` against a worktree of this machine, the main checkout `<the main checkout>` and its ~90 worktrees included, and no test may touch anything outside its own temporary repository;
  - a read-only dry-run of the script against the real repository, from this worktree, is allowed and useful to see the output form; it must never remove or change anything;
  - take care that no code path removes a path outside the git-listed worktrees of the repository the script runs in, the directory the script runs from, the main checkout, or a detached directory that is no copy of the base under `.runs/`; take care with names that come from git (a branch name, a directory name, `..`, symbolic links and junctions, a registration of a worktree that git holds broken). The reviews check exactly this.
- Open design choice: **none.** The task's *Questions carried to cycle* — the name and place of the script, how a task branch is told from another (the prefix `task/` does not suffice), the order of removal of nested directories, a directory locked by another process on Windows, a broken registration, the exact rule of the name of a loose base copy (`base-check-*`, `base-fix-*`), the known caches the listing skips — are choices of how to make what the task settles: make each, name it in your report's table of questions with the option you rejected and what it costs if wrong, and test it. Where you meet an open design choice that needs a foundation entry the task and the foundation leave open, return `returned` with a report and no code.
- This cycle runs on the skill as it is now. The change you write adds the script's run to step 4 for the cycles after the merge; this cycle does not run it.

## What to read (selected by the orchestrator)

Foundation entries by identifier, each whole, in `foundations/decisions.md`: WAY-298 (the sentence you change), WAY-373, WAY-140, WAY-153, WAY-269, WAY-314, WAY-148, WAY-48, WAY-328 (the departure from the coding and testing guidelines: neither is missing for `task-cycle`; there are no guidelines files to read). Read the invariants of `foundations/invariants.md` whose *Part* is `task-cycle` or `every`, each whole — among them `script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`, `tracked-file-private-paths`, `map-reference-target`, `test-method-citation`, `skill-entry-points` — and the part map's entries for `task-cycle` and `repository` (`foundations/part_map.md`), the glossary entries of the terms you use (`foundations/glossary.md`). From the rest of the log, select by "Reading the foundation" in `elements/common/way_of_working.md` the decisions whose *Scope* names `task-cycle` that your change touches (the cycle's start, the working copies, the record, the request's description), and read each whole; the decision you write will also need the search of the whole foundation that the foundation step gives.

Files of the process you change, to read whole before editing them: `task-cycle/skill/SKILL.md`, `task-cycle/skill/request_template.md` (the places of working copies and *Cost*, *Checks*), `task-cycle/record_template.md`, and as the model of a script of this part `task-cycle/gate_times.py` with its test `task-cycle/test_gate_times.py`; `task-cycle/test_tracked_files_private_paths.py` and `task-cycle/request_check.py` where they check what you write.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed.
The files that a product's own tools and tests make by themselves are no working copy of the agent
and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a
worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside
its report what the report needs, and states in the report where each copy stood and that it was
removed. Where a removal fails, the agent finishes all the same and names in the report the
remainder, with its full path and the reason it stayed.

(The test of the script makes its throwaway repositories with Python's `tempfile`, as the other tests of the part do, or under `.runs/author/`; a test's own temporary files are the files "a product's own tools and tests make by themselves". The throwaway repositories you make by hand to try the script go under `.runs/author/`.)

## Report

Write the full report to the report path above, as `make-change` gives it, with **Unread material** and **Searches not found or unclear** (each `none` or the items), the own-work check, the checks with command and exit code, the questions table with every choice of the list above, and the working copies. Return: your status, your commits, a one-line check result naming what failed or did not run, and the report's path.
