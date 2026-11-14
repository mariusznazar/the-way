# Handoff — the review of the whole change (`review-change`)

You are a reviewer that did not make this change, a `the-way-stage` agent dispatched by the orchestrator of a task cycle of the-way. The requester has delegated intermediate choices to the orchestrator; you ask the human nothing. Questions go to the orchestrator in your report (first line `questions`).

## What you review

- Method: `task-cycle/review/SKILL.md` (`review-change`), variant "the whole change". Read that `SKILL.md` whole, and `task-cycle/review/whole_change.md` as it says; read each other file it names only when the step names it.
- Worktree (your working directory; start every command from its root): `the task's worktree`, branch `task/worktrees-removed-after-merge`.
- Range: base `835344fb183fce6dbd99be486df790f1212cacf6` to head `a8494082…` — take the head from `git rev-parse HEAD` (it is `a849408`). Three commits of one author: `9fe7f66` (the script and its test), `25daf50` (foundation entries: WAY-298 edited, WAY-375 and WAY-376 added), `a849408` (step 4 of the skill, the two templates).
- Route: one author without a plan, no spec; so there are no slices, no slice reviews and no plan. The whole change is yours to judge.
- The frozen task: `.runs/task-cycles/worktrees-removed-after-merge/task.md` — read it whole, it is the document you judge the change against (in Polish; the code and the foundation entries are in English). Judge every item of *To do* (1–9), every settlement row (1–6), every *Answer* under *Questions to settle*, and the places of `SKILL.md` that *Context* names.
- The author's report: `.runs/task-cycles/worktrees-removed-after-merge/reports/author-report.md` (its questions table lists the choices of how to make what the task settles; judge each).

## The orchestrator's answers of step 4

- Trust boundary: **no** (no file of the change is one the part map names; the script works on the product's own git state, WAY-48).
- Irreversible operation: **yes.** With `--apply` the script deletes directories. The cycle prepares it and never performs it; check that **the change only prepares it**: that nothing in the change, the tests included, runs the removal against a real worktree; that the script removes only what the task's rule allows (all of: tree clean, every commit on the remote, branch merged by the rule of item 3, directory belongs to a cycle) and nothing else; that it never removes a branch, the main checkout, the directory it runs in, a detached directory outside a cycle (`the-way-global`, `the-way-fullrun`, a session's scratchpad copy) or a path git does not list; and check the names that come from git (a branch name, a directory name, `..`, a symbolic link or junction, a registration git holds broken, a directory locked by another process) as crafted input.
- You may run read-only checks and the focused tests (`python -B gate/run_tests.py task-cycle`, `python -B -m unittest task-cycle.test_remove_merged_worktrees`). **Do not run the script with `--apply`** against any repository except a throwaway one you make in your own directory; a dry run of the script against the real repository from this worktree is allowed with `--no-fetch` and removes nothing. Do not run the product's full gate: the orchestrator does.

## Choices of the author that you are told of

The author's table of questions (report, section "Questions table") holds 15 choices. The orchestrator asks you to judge in particular: choice 4 (a nested checkout that is detached, clean and on the remote goes with its task directory whatever its name, where item 4 of the task names `base-check-*`; and item 5's "never detached directories outside the cycle"); choice 7 (two loose base copies stay because their names give no task branch); choice 9 (the option `--no-fetch` the task does not name); choice 13 (rows 2, 4, 5 as one decision, WAY-375); and the two wordings the author names as its own ("first-parent history" in WAY-375, the `.runs/` part of WAY-376). Decide each by the task and the foundation, not by the orchestrator's leaning.

## A gap the orchestrator carries to you

The author's handoff named `task-cycle/request_check.py` (and its test) as a file to read where it checks what the author writes, and the author's report says it did not read them. The author changed `task-cycle/skill/request_template.md` and `task-cycle/record_template.md`. Judge whether the change to the templates passes `task-cycle/request_check.py`'s expectations (read the script; you may run it on a description you make from the template's form), and whether the new record item *Directories of earlier tasks kept* and the lines under *Cost* and *Checks* hold together with WAY-373's route and with `task-cycle/remarks_check.py` and `private_paths_check.py`.

The author's report also names unread material (WAY-286, 287, 289, 290, 309 as entries; `elements/decisions/examples.md`; about 120 decisions of *Scope* `task-cycle` by title only). You select your own foundation by "Reading the foundation"; that selection is yours.

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

Your directory for working copies: `.runs/review-whole/`.

## Report

Write the full report to `.runs/task-cycles/worktrees-removed-after-merge/reports/review-whole-report.md`, its first line `PASS <sha>` or `FAIL <sha>` (or `questions`), as the method gives it, with graded findings (each with its place and expanded reasoning), the checks you ran with command and exit code, how many decisions you read whole and how many by title only, **Unread material**, **Searches not found or unclear** (each `none` or the items), the coverage of every task item and settlement row, and your working copies. Return the first line, the changed files with their line counts, a one-line check result and the report's path.
