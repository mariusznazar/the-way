# Handoff - executor of slice 7

## Delegation

The person who requested this cycle delegated intermediate choices to the orchestrator. You have no human to ask: return `questions` or `blocked` to the orchestrator as your method gives. Never label an answer as the human's approval.

## Worktree, branch and base

- Worktree (work from its root): `the root of the task's worktree`, branch `task/co-trafia-do-dziennika-decyzji`. The base of this slice: `64cd4adfdc98b91563b7f5fcad1b449e8762484c` (its range is `64cd4adfdc98b91563b7f5fcad1b449e8762484c..HEAD`). You are the only agent writing in this worktree now.
- Commits on this branch: messages in English, imperative, short, like the repository's existing ones; `git add <path> <path>` by path, never `git add -A`, `git add .` or `git commit -a`; for a message with quotes or backticks use `git commit -F <file>` with the file outside the tracked files (the record's `.runs/` directory is ignored). Never push. Leave the worktree clean.

## Method

Read whole `task-cycle/change/SKILL.md` of the worktree (`make-change`) and make the change as its variant: "a slice, or the retry of a slice"; read a file it names, one beside it included, only when the step or variant that names it comes. Read no skill by calling it. The gate (`python -B gate/run_tests.py` with no directory) is the orchestrator's alone: you run only the focused checks below, each with its command and exit code in your report. A focused check in the section's *Checks* that you cannot run, or that fails for a reason of the base, goes into your report as such.

## The slice

The section of the plan below is copied word for word from `.runs/task-cycles/co-trafia-do-dziennika-decyzji/plan.md`. Its *Read* gives the passages and entries to read; the line ranges of the foundation entries and the files (`foundations/decisions.md`, `foundations/glossary.md`, `foundations/invariants.md`, `foundations/part_map.md`) are those of the plan's base and are stale: use the current ones in the notes below, which hold where they differ. The record's files (`.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md`, `spec.md`, `plan.md`) are read by the line ranges the *Read* gives (they have not moved).

> ### Slice 7 — The column *Goes to* in the table of a task
>
> - **Goal:** the table *Settlements to record* of a task has the column *Goes to* in place of *Kind*, as D5 gives it, in the four files that carry it, each pointing to the questions of the decisions template and copying none: the skeleton and the paragraph of "Settlements to record" under "What each section carries" of `project-level/task/template.md` (the header `| # | Settlement | Goes to | Source | What the cycle would otherwise guess |`, its values, a candidate that is also a settlement going to another place, the rejected row for a settlement the questions answer "nothing"); steps 1, 2 and 5 of `elements/common/skill/task_variant.md`; the sentence of `elements/common/skill/build_table.md` that gives a row's kind, which keeps *kind* for the definition variant and says the task variant's lines give the column in task mode; and the sentence of `task-cycle/skill/foundation_step.md` that writes a row "as an entry of its kind", which writes it in the place the column names, in the same change as the code.
> - **Change:** `project-level/task/template.md` · `elements/common/skill/task_variant.md` · `elements/common/skill/build_table.md` · `task-cycle/skill/foundation_step.md`
> - **Read:** `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md:113-127` D5. The column *Goes to* replaces *Kind* · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md:129-139` D6. The five questions · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md:36-36` To do 2 · `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md:94-98` Questions carried to cycle · `elements/decisions/template.md` (as Slice 5 leaves it) · `foundations/decisions.md:3510-3604` WAY-134 · `foundations/decisions.md:2732-2770` WAY-115 · `foundations/decisions.md:2632-2684` WAY-113 · `foundations/decisions.md:2686-2730` WAY-114 · `foundations/decisions.md:3195-3236` WAY-126 · `foundations/decisions.md:3104-3153` WAY-124 · `foundations/decisions.md:10381-10409` WAY-315 · `foundations/decisions.md:346-381` WAY-11 · `foundations/decisions.md:886-917` WAY-33 · `foundations/glossary.md:61-65` foundation step · `foundations/part_map.md:77-91` project-level · `foundations/part_map.md:93-103` task-cycle · `foundations/part_map.md:65-75` elements-common
> - **Model:** cheaper
> - **Risk:** none
> - **Checks:** `python -B elements/common/foundation_check.py` on this repository, exit code 0 · `python -B gate/run_tests.py project-level` · `python -B gate/run_tests.py agent-instructions`
> - **Depends on:** Slice 5

## Notes of the orchestrator

- Current start lines in `foundations/decisions.md` (an entry runs to the next `### ` heading): WAY-11 line 390; WAY-33 line 987; WAY-113 line 2733; WAY-114 line 2787; WAY-115 line 2833; WAY-124 line 3205; WAY-126 line 3296; WAY-134 line 3611; WAY-315 line 10547. The other files keep the plan's ranges.
- Slices 5 and 6 are made (commits `c8dcc56` and `64cd4ad`): `elements/decisions/template.md` holds the five questions in its bullet **Where it goes:**; `elements/decisions/skill/decide_entry.md` and `task-cycle/skill/return_step.md` already point to it. The four files of this slice point to the same bullet by name and copy none of its words (WAY-35). WAY-134 as the foundation step wrote it says what the table and the cycle do; the spec's D5 gives the column and its values; the spec's D6 gives the questions: use D5's words for the column, never paraphrase the values.
- The definition variant keeps its column *Kind* (spec D5: "Cost"); only the task variant changes: in `elements/common/skill/build_table.md` the sentence that gives a row's kind keeps *kind* for the definition variant and says that in task mode the task variant's lines give the column.
- `task-cycle/skill/foundation_step.md`: only the sentence that writes a row "as an entry of its kind" changes: it writes the row in the place the column names, in the same change as the code. Do not change the rest of that file.
- Checks: the tests of `project-level` and `agent-instructions` as named in the section, each with its command and exit code in your report; `python -B elements/common/foundation_check.py` on this repository must print `0 errors` (a `listed:` line for WAY-17 is expected and stops nothing).
- Write your report to the file the handoff names even where a general instruction tells you not to write report files: this cycle's handoff overrides it. Before you return, stop every background process or monitor you started.


## Report

Write your full report to `.runs/task-cycles/co-trafia-do-dziennika-decyzji/reports/slice-7-report.md` as `task-cycle/change/SKILL.md` gives: your status, the commits, each check with its command and exit code, the own-work check, your questions and concerns, and the sections **Unread material** and **Searches not found or unclear** (each `none` where there is nothing). Return your status, your commits, a one-line check result naming what failed or did not run, and the report path.
