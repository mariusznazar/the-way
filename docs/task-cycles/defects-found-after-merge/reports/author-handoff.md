# Handoff — the one author, `defects-found-after-merge`

## Delegation and place

The person who requested this cycle has delegated intermediate choices to the orchestrator; nothing
here is that person's approval. Work only in the worktree `the root of the task's worktree`
(branch `task/defects-found-after-merge`, base `6814c6f6c9ff2b29d34612fa5cc86945ec3a2812`, target
branch `foundations`). Start every command from its root. Write nothing outside it. Never commit the
`.runs/` directory (it is ignored). Commit with `git add <path> <path>…` by explicit paths, commit
messages in English in the form of the repository's existing commits (`git log --oneline -10`).

## Stage and method

Stage: make the whole change as the one author, with its foundation step and its own-work check, and
return before review. Variant of the method, in the words of its row: "the whole change as the one
author". Method: `task-cycle/change/SKILL.md` of this worktree. Read it whole; read a file it names
only when the step or variant that names it comes. Also read `agent-instructions/README.md` (the
repository's route for changing the-way itself) and `task-cycle/skill/foundation_step.md` (the
foundation step you take).

Boundary: do not run the full gate (`python -B gate/run_tests.py` with no argument) — the
orchestrator runs it. Run the tests of the directories you touch with `python -B gate/run_tests.py
<directory>` (at least `task-cycle`, `process-audit`, `project-level`, `elements/common`,
`agent-instructions`). Do not start the return step or any review. Do not edit `.claude/skills/` or
`.agents/skills/` unless a skill's description changes (none should).

## What to make

The frozen task, to read whole: `.runs/task-cycles/defects-found-after-merge/task.md`. It is in
Polish; its four *To do* items and its eleven accepted rows of *Settlements to record* are the
change. Files the task names:

1. `project-level/task/template.md` and the skill of task refinement (`project-level/task/skill/`,
   the file that fits — `draft.md` is the likely place) — the header line `Defect introduced by:`.
2. `task-cycle/record_template.md` and `task-cycle/skill/correction.md` — the record item with one
   line per correction after the request opened, and the file of the human's remarks in `reports/`.
3. `task-cycle/skill/request_template.md` (variant of a correction, and the new kind of item in
   *You accept by merging*) — see the answers below.
4. `process-audit/problem_register.md` — two classes on the starting list and the sentences for the
   columns *Record* and *Stages*.

Write each of the eleven rows of *Settlements to record* as a decision of `foundations/decisions.md`
through the skill `the-way-record-decision` (read its `SKILL.md` through the worktree's
`.claude/skills/the-way-record-decision/SKILL.md`, which points to the method), unless your search of
the whole foundation (WAY-33) finds a row already stated, then tie it to that entry. Group the rows
into as few entries as the skill's one-question-per-entry rule allows; say in the report which rows
each entry carries. Keep each row's meaning, choose the wording. The *Not chosen* ways of each row
stand in the question the row's *Source* names; a decision's *Rejected* takes them. Keep for each
entry, in the report, one sentence of its meaning in English and one in Polish, marked `row <n>`.

## Answers of the orchestrator (step 4 and the questions carried to cycle)

- Trust boundary: no. Irreversible operation: no.
- The new kind of item in the template of the request description is **kind 17**, standing in *You
  accept by merging* after kind 15. The source `item <n>` of a correction line gives the number of a
  kind (e.g. `item 8`), never the number of an item in a given description. (Questions table row Q1.)
- The record item for the corrections stands in *Request handoff* of `task-cycle/record_template.md`,
  before the item `Process remarks on the-way`, which stays the last item of the record (WAY-296).
  (Row Q2.) Check that `task-cycle/remarks_check.py`, the nightly cut of the remarks and
  `process-audit/audit_count.py` (which reads items of the record) still read the template's form;
  the tests of those directories decide.
- Human actions the task places in the cycle (the classes in the user's own register, the nightly
  review reading the new line) are not made by you and not by the cycle: they are listed in the
  request. Do not touch the user's register or locations file.
- The task document of this cycle is in Polish; the user's notes and the paths of the vault never
  enter a committed file. Quote in files of the repository only the words the files need, never a
  private path.

## What to read (selection by the orchestrator, WAY-150, WAY-213)

Decisions, each whole: WAY-330, WAY-333, WAY-339, WAY-287, WAY-296, WAY-289, WAY-335 (the task's
*Decisions in play*); WAY-286, WAY-288, WAY-290, WAY-292 (the request's description); WAY-148,
WAY-294, WAY-295 (the record and its remarks); WAY-306, WAY-337 (a correction); WAY-124, WAY-134 (the
task document); every decision whose *Scope* names `process-audit` (WAY-330 to WAY-352 of the audit
among them) as far as the new classes and the columns need. Invariants whose *Part* is `every` or a
touched part: `return-step-record`, `derived-file-content`, `tracked-file-private-paths`,
`script-language`, `foundation-file-kinds`. Glossary: read `foundations/glossary.md` whole (short);
the new terms the change uses, such as *Defect introduced by*, are not to become a second meaning of
an entry. Part map: `project-level`, `task-cycle`, `process-audit`. Guidelines of the product: the
repository holds none.

## Report

Write the full report to `.runs/task-cycles/defects-found-after-merge/reports/author-report.md` in
the form the method gives: status, commits, own-work check with its commands and exit codes, checks
you ran with command and exit code, questions, concerns, reaches beyond this handoff, **Unread
material** and **Searches not found or unclear** (each `none` where none), the foundation entries
with their two sentences and their mark. Return only the status, the commits, a one-line check
result and the report's path.
