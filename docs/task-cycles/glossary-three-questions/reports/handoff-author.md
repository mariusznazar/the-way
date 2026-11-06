# Handoff — the one author (make-change), task `glossary-three-questions`

## Delegation

You make the whole change of one the-way task as the one author. The person who requested this
cycle has delegated intermediate choices to the orchestrator and, through it, to you; the human
reviews the pull request, not the steps. Do not seek human approval and do not start another stage.
Answers to your questions come from the orchestrator, from the task and the foundation.

## Where you work

- Worktree (work only here, from its root): `C:\Storage\repos\the-way\.runs\worktrees\glossary-three-questions`
- Branch: `task/glossary-three-questions`, base `61c72fb6347649a9bd61a71f0d2695f2e91e8b6a` (target branch `foundations`).
- This is the-way itself: the process root is this worktree. Read every file of the-way, including
  the methods named below, from this worktree, never from another checkout.
- Git: commit on this branch only; `git add <path> <path>` by explicit paths (never `-A`, `.` or
  `commit -a`); English commit messages in the style of `git log` (e.g. `docs: …`); do not commit
  anything under `.runs/`; never force-push, never push. Read `agent-instructions/README.md` first
  (how a change to the-way is made before `main` exists).

## Your method and variant

Method: `task-cycle/change/SKILL.md` in this worktree. Read it whole. Your variant, in the words of
its table row: **"the whole change as the one author"**. Read a file the method names (for example
`task-cycle/change/ui_check.md`) only when the step that names it comes; no part of this change is a
user interface.

The foundation step — writing the entries the task carries — is yours, together with the change:
read `task-cycle/skill/foundation_step.md` whole. Each entry is written through the pinned skill of
its element: decisions through `elements/decisions/skill/SKILL.md` (and `elements/decisions/template.md`,
`elements/decisions/examples.md`), glossary text through `elements/glossary/skill/SKILL.md`. Read the
skill of an element when you write an entry of that element, and select your foundation as that
skill's step 1 gives.

## Stage and boundary

Make the change and the foundation entries, commit them, and return. You do not take the return
step (the orchestrator resumes you for it later), run no review, and do not run the product's gate
(`python -B gate/run_tests.py` with no argument is the orchestrator's run, step 10). Focused
checks are yours: `python -B gate/run_tests.py <directory>` for the directories your change reaches
and the foundation check `elements/common/foundation_check.py` on this worktree's foundation. Report
each with its command and exit code.

Answers of the orchestrator's start (task cycle step 4): trust boundary — no; irreversible operation
— no; open design choice — none; reserved choice — none; route — one author without a plan; your
class — `same`.

## The task (frozen)

Read whole: `docs/task-cycles/glossary-three-questions/task.md`
(copy of `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\zadanie_the_way_slownik_trzy_pytania.md`,
accepted 2026-11-05; sha256 prefix `0c67bd3e963cca83`). Its *To do* items 1–5, *Questions to settle*
(the human's answers, with *Not chosen* ways — they are settled, do not reopen them) and *Settlements
to record* rows 1–5 are what you carry out. The row's meaning is the human's; the wording is yours
(WAY-134). *Out of scope*: fixing sentences in loop2 or any product — touch no product's foundation.
Nothing in the task is a question carried to the cycle, and no human action is placed in the cycle.

Where a row's meaning cannot hold, or an entry would change the meaning of an approved decision beyond
what the task carries (WAY-30), or a row collides with a current entry other than as the task commands,
return `blocked` with the question, as `foundation_step.md` gives.

## What to read (selected by the orchestrator)

Foundation entries by identifier, each whole (a decision from its heading to the next `###`), in
`foundations/decisions.md` of this worktree:

- the task's *Decisions in play*: WAY-95, WAY-97, WAY-99, WAY-104, WAY-161, WAY-263, WAY-226, WAY-72, WAY-171;
- the ones those link to or that the task's text names: WAY-94, WAY-96, WAY-114, WAY-134, WAY-33, WAY-07, WAY-11, WAY-71;
- then, as the decisions skill's step 1 gives, the decisions whose *Scope* names `decisions`, `glossary`
  or `task-cycle` that your entries touch, and the invariants whose *Part* names them or `every`.

Whole files: `foundations/glossary.md` (short), `foundations/part_map.md`, `elements/glossary/template.md`,
`task-cycle/review/SKILL.md`.

Guidelines: the-way keeps no `guidelines/` directory; none to read.

## What the change must reach (orientation — the task's text rules, quoting it word for word where it speaks)

The files the task names: `foundations/decisions.md` (WAY-95, WAY-97, WAY-99, WAY-104 edited in place,
WAY-07; a new decision in `task-cycle` scope), `elements/glossary/template.md` ("Which words take an
entry", "Two glossaries", and the `TODO — decision pending: which decision sets when two uses of a word
carry two meanings`), `task-cycle/review/SKILL.md` section 3. Your own search of the whole foundation
and repository (WAY-33) finds the rest that mentions the rules you change (for instance
`elements/common/way_of_working.md:98-100`, `foundations/decisions.md` lines near 1981–2008, 4958, 6858,
and any skill or template that restates the bare-word rule of WAY-104 or the two-meaning rule). Correct
each in this change; name in your report what the search found and what you changed.

Two placement choices are yours to make and report (record each as a choice with the option rejected):
(a) which decision carries the sentence test of question 1b — the orchestrator's reading is WAY-99,
which already speaks of a word that "carries two meanings"; use another or a new one only for a reason
you name; (b) the shape of the new `task-cycle` decision for questions 1a and 2 (the orchestrator's
reading: it narrows WAY-161 for exactly the case the task names, and WAY-263 stays as the task says).
The sentence in `task-cycle/review/SKILL.md` section 3 must fit the grading rules already there and
leave WAY-263's paragraph and the WAY-99 renaming finding as they are.

Language: the foundation, templates and skills are in English (WAY-72). In your report, give for each
entry one sentence of its meaning in English and one in Polish, and mark it `row <n>` (rows 1–5 of
*Settlements to record*), `projected` or `the cycle's`.

## Own-work check

Before you return, name the requirement of the task most likely to be unmet by your text (for example:
a rule that works in only one direction, an example the rule would not decide, a place that still states
the old rule) and a check that would catch it; run it and report what it showed.

## Report

Write the full report to:
`docs/task-cycles/glossary-three-questions/reports/author.md`
in the form `task-cycle/change/SKILL.md` gives, including **Searches not found or unclear**.
Return to the orchestrator only: status, commits, a one-line check result, and the report path.
