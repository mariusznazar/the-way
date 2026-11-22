# Handoff — the one author, `make-change`, the whole change

You are the one author (type `the-way-author`) of a task cycle of the-way. Work from the root of
the worktree `the worktree root` (branch
`task/poprawki-z-przegladu-cykli-22-11`, base `2a2f4106c216c0fef4e68b7ed8bd5728ae2660ae`, the
branch `foundations` of the-way). The-way is the product itself: no `.the-way` submodule, no pin;
every path below is relative to that worktree root, and the process files you read are the ones of
that worktree.

## Delegation

The person who requested this cycle has delegated every intermediate choice of the cycle to its
orchestrator, who answers your questions from the task, its sources, the foundation and the code.
Nothing the orchestrator says is that person's approval; the person reviews the finished pull
request, not the steps before it. You never ask the person anything and never start the next stage
of the cycle.

## Method and variant

Read `task-cycle/change/SKILL.md` whole — `make-change`, its variant "the whole change as the one
author" — and a file it names (one beside it included) only when the step or variant that names
that file comes. Do not read every file it names at the start.

Also read, whole, `task-cycle/skill/foundation_step.md` (the foundation step: you write the entries
the task carries, as its first paragraph gives, with your code), and, where you write a foundation
entry of an element, the `SKILL.md` of that element at the path that file gives (the decisions
`elements/decisions/skill/SKILL.md` for a decision; `elements/common/way_of_working.md` is the
shared way of working those skills read). You select the foundation entries you read for that
writing as step 1 of "Reading the foundation" in `elements/common/way_of_working.md` gives it. The
return step is not your task now: the orchestrator resumes you for it later.

## The stage and its boundary

Make the whole change the task requires: all 13 points of its *To do*, the four rows of its
*Settlements to record* (rows 1–3 go to a sentence of WAY-255, WAY-25 and WAY-136, row 4 to a new
decision) and the foundation entries those rows carry, as the foundation step gives, with the code
and its tests. Commit by path (`git add <path>…`, never `git add -A` or `git add .` or
`git commit -a`); commit messages in English. Return before review; do not run the product's gate
(`python -B gate/run_tests.py` with no argument): its run is the orchestrator's or CI's. Run the
focused checks of your own work, as `make-change` gives them.

The route is one author without a plan; the orchestrator judged that the change fits one agent. If
it proves too large, or you meet an open design choice the task, the foundation and its settled
questions leave open, return `returned` with a report and no code, as `make-change` gives it.

## The frozen task

`.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/task.md` — the frozen copy of the task document
(written in Polish; its quoted wordings are in English and are accepted by the human word for word).
Read it whole. It is the one source of what the change requires; its *To do* names the places by a
heading or a quotation, and the line numbers it gives are hints that hold at `foundations`
@ `2a2f4106`, the base. No spec and no plan exist.

The task's *Decisions in play* quotes WAY-25, WAY-255, WAY-136, WAY-229, WAY-160, WAY-12, WAY-148,
WAY-339, WAY-390, WAY-18 and WAY-225; read those entries whole in `foundations/decisions.md`
(find each by its heading), with the *Rejected* of the three the change edits. For the new decision
(row 4) and for the others the change touches, select by "Reading the foundation" as above; the
index script `elements/common/decision_index.py` is also a script this change edits (point 10), so
read its description and code before you write its index for your own reading, and write the
index into `.runs/author/` as that method gives.

## Answers of the orchestrator's start (WAY-13, WAY-48)

- Trust boundary: **yes**. `task-cycle/gate_times.py` (point 11.1) and
  `instruction-files/check_instructions.py` (point 5) are trust-boundary files in the part map.
  Every code review of the cycle is told so and tries crafted input at them; think of what a
  crafted command line, path or output could do to those two files after your change, and test it.
- Irreversible operation: **no**.
- Open design choice at start: none. Reserved choice: none.

## What you read (selected by the orchestrator, WAY-150, WAY-213)

Parts the change touches (by the part map's rules for assigning files): `task-cycle`
(`task-cycle/change/SKILL.md`, `task-cycle/review/SKILL.md`, `task-cycle/review/whole_change.md`,
`task-cycle/plan/SKILL.md`, `task-cycle/skill/SKILL.md`, `task-cycle/slice_size.py`,
`task-cycle/gate_times.py`), `decisions` (`elements/decisions/template.md`,
`elements/decisions/skill/SKILL.md`, `foundations/decisions.md`), `part-map`
(`elements/part-map/template.md`, `elements/part-map/skill/SKILL.md`), `environment-facts`
(`elements/environment-facts/template.md`, `elements/environment-facts/skill/draft.md`),
`elements-common` (`elements/common/decision_index.py`, `elements/common/way_of_working.md`),
`instruction-files` (`instruction-files/check_instructions.py`,
`instruction-files/SKILL.md`, `instruction-files/test_check_instructions.py`), `installation`
(`installation/README.md`) and `gate` (`gate/run_tests.py`). The part map is
`foundations/part_map.md`; read the entries of those parts whole.

Guidelines, each whole: `guidelines/coding.md` (with its index of kinds), `guidelines/testing.md`,
`guidelines/coding-check.md` (for `check_instructions.py` and `slice_size.py`) and
`guidelines/coding-command-runner.md` (for `gate_times.py` and `gate/run_tests.py`). For
`elements/common/decision_index.py`, read the kind file of the index `guidelines/coding.md` whose
*When to read* matches it. Where you reach a guideline file this selection did not name, read it
and name that reach in your report. The size rule (WAY-385, the invariant
`function-and-file-size`) bears on every script you add to: a change that adds to a function or a
file over its threshold begins with a move of a part of it out, with no change of behaviour.

The invariants the work reaches: those whose *Part* names a touched part or `every` in
`foundations/invariants.md`, found by that search, and each invariant a test you alter cites by its
`invariant:` line.

## Notes of the orchestrator for this change

- A new test file in a new directory runs only after `git add`; and many checks, the foundation
  check among them, list only the files git tracks. After `git add` of every file your change
  creates, run the checks again (the point 9 of the task is about exactly this).
- `python -B elements/common/foundation_check.py` is the foundation check; during the change, pass
  `--skip-test-citations` only as `elements/common/way_of_working.md` step 4.3 gives; run it without
  that switch on the finished change. A change to a binding sentence of a decision needs the
  decision held: by the invariants and tests it names or by a pair of examples (WAY-12).
- A sentence you add to a file of one part must not name a file of another part the part map does
  not allow it to depend on (the part map's *Depends on*; e.g. `task-cycle` does not depend on
  `instruction-files` — point 5.4's sentence in `task-cycle/review/whole_change.md` has to be worded
  accordingly, and the part-map entries of the parts you touch have to still match the files).
- A point whose wording the task quotes is written with that wording, word for word. Where a quoted
  wording meets a place whose current text it contradicts or duplicates, say so in your report
  instead of silently adapting it.
- Point 11 changes the measuring script and the test runner of the process; that starts a new series
  of gate times (WAY-339) — nothing for you to do about it beyond not hiding it.
- Tests: write them as `guidelines/testing.md` gives, with the `decision:` / `invariant:` lines it
  requires, and as point 9 of the task makes a rule for the tests that hold a sentence of a decision.

## Working copies

Your directory for working copies is `.runs/author/` of the worktree. The first paragraph of "Working
copies" of `task-cycle/skill/SKILL.md`, word for word:

> An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
> clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
> directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
> in the system's temporary directory, in the scratch directory of a session or in the main checkout
> of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
> itself under its session's directory is moved into the agent's directory and the original removed,
> except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
> says, to the place the product's foundation settles for screenshots, and into the agent's directory
> only where no such place is settled. The files that a product's own tools and tests make by
> themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
> each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
> `git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
> the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
> all the same and names in the report the remainder, with its full path and the reason it stayed. It
> removes a copy, as any directory, by its path written out in full in the command, never through a
> shell variable: an empty variable turns the removal on the directory the shell stands in.

## What you do not read

`cycle.md` and the other files of the cycle's record directory
(`.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/`) — other agents' handoffs, reports and
findings — are not yours to read, except the files this handoff names: the frozen task, and the
report path below, which you write. Do not read the transcripts of other sessions.

## Your report

Write the report to `.runs/task-cycles/poprawki-z-przegladu-cykli-22-11/reports/author-report.md`
(its name starts with the role, as Claude Code requires; that file is the input of the cycle's
scripts — `task-cycle/remarks_check.py` reads it — so the write is the case the note about subagents
leaves open: if the harness refuses the write, return the report whole as your answer). The report's
first line is yours; it follows `make-change` and holds, besides what that method gives: for each
foundation entry one sentence of its meaning in English and one in Polish, marked `row <n>`,
`projected` or `the cycle's`, a pair of examples you add word for word, each check you ran with its
command and exit code, your own-work check, **Unread material** (what this handoff names that stayed
unread or was read in part, or `none`), **Searches not found or unclear** (each thing you looked for
and did not find or found unclear, or `none`) and the line on your working copies. Return your
status, your commits, a one-line check result naming what failed or did not run, and the path of the
report.
