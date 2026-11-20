# Handoff — the one author, whole change

You are the one author of a change in a task cycle of the-way (agent type `the-way-author`). The
person who requested this cycle delegated intermediate choices to the orchestrator; no answer in
this handoff is that person's approval.

## Where you work

- Worktree (the only place you write): the task's worktree, branch
  `task/decision-length-check`, base commit `1b6fe1c1` (the head of `foundations`). Work from the
  worktree's root; the-way here is the worktree itself, there is no `.the-way`.
- Your directory for working copies: `.runs/author/` (directly under the ignored `.runs/` of the
  worktree).
- Your report goes to `.runs/task-cycles/decision-length-check/reports/author-report.md`. That file
  is the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it); its name starts with
  the role, which is the case the cycle's note on the refused `report…` name leaves open. Where the
  harness refuses the write all the same, return the report whole as your answer.
- The file `cycle.md` and the other files of `.runs/task-cycles/decision-length-check/` — other
  agents' handoffs, reports and findings — are not yours to read, except those this handoff names:
  `task.md` and `orch_index.md`.

## Your method and variant

Read `task-cycle/change/SKILL.md` whole. Your variant is the row **"the whole change as the one
author"**. Read a file it names, one beside it included, only when the step or variant that names it
comes. You do the foundation step with your code: read `task-cycle/skill/foundation_step.md` whole,
and, for the entry you write in `foundations/decisions.md`, the `SKILL.md` of the element at the path
that file gives. Return before review; the return step is another dispatch, to you resumed.

## The task

The frozen task: `.runs/task-cycles/decision-length-check/task.md`. Read it whole; it is the whole of
what you make. Its `Status: ready for cycle`, no human action is open. In short: the check of the
foundation, `elements/common/foundation_check.py`, reports as an error a decision that a change adds
or whose binding sentences it alters and whose binding paragraph has more than 3 sentences or more
than 300 words, lists any other decision over the limit with a line `listed:`, and the template, the
descriptions of the check and WAY-05 carry the new rule; points 1–6 of *To do*, the answers under
*Questions to settle* and *Settlements to record* rows 1–2 give the wording. Do not widen the task:
the 12 entries of the-way that stand over the limit today are shortened by another task and stay as
they are (*Out of scope*).

## Answers of the orchestrator

- Two questions at start: the change touches no trust boundary, and holds no operation that cannot be
  undone.
- No open design choice, no spec and no plan: you make the whole change.
- The question the task carries to the cycle — `elements/common/foundation_check.py` has 1141 lines
  against the 1200 of WAY-385 — is a choice of how to make what the task and WAY-385 settle, and is
  yours: where the new check fits the file within WAY-385 (a file of at most 1200 lines and a function
  of at most 110, on the code as the formatter of WAY-382 leaves it), put it in; where it does not,
  start by moving a coherent part of the script into a module of its own, under the guidelines named
  below, and name the choice in your report so that it enters the questions table of the record. A
  move of the names `elements/part-map/test_cross_part_imports.py` and
  `elements/common/decision_index.py` import from the script is a contract: keep them importable
  from `foundation_check` or change their importers in the same change, and say which.

## What you read

Foundation entries (by identifier, from `foundations/decisions.md`; the index of the orchestrator's
selection is `.runs/task-cycles/decision-length-check/orch_index.md`, whose entries you open whole
as you need):

- the task's *Decisions in play*: WAY-05 (changed; read whole, with its *Rejected*), WAY-12, WAY-02,
  WAY-22, WAY-385 (unchanged; the task quotes what binds);
- from the decisions and invariants of the parts you touch — `decisions`, `elements-common`,
  `agent-instructions`, `repository` (the root `README.md`) — select as "Reading the foundation" in
  `elements/common/way_of_working.md` gives, and read it with the templates and rules step 1 of that
  file names; you are the one who searches the whole foundation once the entry is settled (step 2
  there, WAY-33).

Guidelines of the-way's own code, each whole: `guidelines/coding.md`, `guidelines/coding-check.md`
(the kind of `elements/common/foundation_check.py`; its exemplar is settled by WAY-386),
`guidelines/testing.md`; and `guidelines/coding-shared-module.md` only if you split a module out.

The code and tests to change: `elements/common/foundation_check.py`,
`elements/common/test_foundation_check.py`, `elements/common/foundation_source.py` (the module it
imports), `elements/decisions/template.md` (whole, with `elements/decisions/examples.md` and the
`SKILL.md` of that element), `agent-instructions/README.md`, `README.md`, `foundations/decisions.md`
(WAY-05 and its neighbours WAY-12 and WAY-02 only).

## Checks

Run the focused checks of the directories you change: `python -B gate/run_tests.py <directory>`
(`elements/common`, `elements/decisions` and any other directory whose tests your change can reach,
such as `elements/part-map`, `agent-instructions`), `python -B elements/common/foundation_check.py`
(exit 0, `0 errors`), and the linter the guidelines name. **Do not run the product's
full gate (`python -B gate/run_tests.py` with no directory):** its run is the orchestrator's or CI's
(WAY-160). A new test file in a new directory runs only once it is added to git.

A test you write for the new check carries a line `decision:` with the start of the sentence of
WAY-05 it holds, as task point 6 and WAY-12 give; the sentence you quote is the one in the entry as
you leave it. Record, for a new test, its failing run (before the code) and its passing run, with
command and exit code each, as the record needs them.

## Commits

Commit on the task branch, explicitly by path (`git add <path> …`, never `git add -A` or `git add .`),
in English, in the form of the commits of this repository. Leave the worktree clean when you return.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by itself under its session's directory is moved into the agent's directory and the original removed, except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md` says, to the place the product's foundation settles for screenshots, and into the agent's directory only where no such place is settled. The files that a product's own tools and tests make by themselves are no working copy of the agent and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in the report where each copy stood and that it was removed. Where a removal fails, the agent finishes all the same and names in the report the remainder, with its full path and the reason it stayed. It removes a copy, as any directory, by its path written out in full in the command, never through a shell variable: an empty variable turns the removal on the directory the shell stands in.

## What the report holds

As `task-cycle/change/SKILL.md` gives it, with its status, your commits, your checks each with command
and exit code, your own-work check (the weakest point of the change and how you checked it), the
sections **Unread material** (what this handoff names that stayed unread or was read in part, or
`none`) and **Searches not found or unclear** (each thing you looked for and did not find or found
unclear, or `none`), and your working copies. Put every question to the orchestrator in the report
under status `questions`; seek no approval from the human.
