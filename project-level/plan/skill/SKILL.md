---
name: plan-project
description: Use when an approved project definition of a product that uses the-way has to be broken into tasks — the breakdown that writes the project plan, a plan to resume from its status line, or a plan to check again after its definition passed the readiness gate anew. Not for a task's plan of slices, and never refines a task.
---

# Plan a project

Leads the breakdown: the step after the readiness gate that turns an approved project definition
into its plan — the tasks, what each depends on, which tasks realize and write each projected
entry, and where each open question is resolved. The form of a plan and the rule of each part stand
in `project-level/plan/template.md`; how a skill asks stands in `elements/common/way_of_working.md`;
this skill holds the order of the work. The decisions that set its rules are cited below.

This skill lives in `project-level/plan/skill/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel` prints in
the session's working directory; in a product, it is the product's pinned `.the-way`. The project
level's directory, `project-level/`, is there, and each skill named below is the project skill of
that name with the `the-way-` prefix.

The breakdown reads the product's foundation and the definition and writes nothing in either
(WAY-106). It writes no task document; each task is refined later through `refine-task`.

## Delegated work while leading a plan

When `lead-project` dispatches you through a refinement conversation path, read
`delegated_mode.md` beside this skill first (WAY-156): it holds what that path changes in the
workflow below, and the files of steps 5, 6 and 7 point back to it.

## Rules that hold across the steps

The original definition and plan remain authoritative (WAY-151). Run every readiness, fingerprint
and plan check on those whole files at their original paths, never on selected excerpts or a
reduced copy. Selection is no reading cap; read a small file whole where useful.

A new complete breakdown processes every scope item, projected entry and exact question: batching
brings in context when needed and omits none of the project. Whole-plan checks run after a change.

## 0. Start or resume

- Read `project-level/plan/template.md` in full, and the section "How a skill asks" of
  `elements/common/way_of_working.md`.
- When an existing plan is named, by the human or in a dispatched turn by its conversation file,
  read `existing_plan.md` beside this skill, and `reading_definition_and_plan.md` beside it.
- Otherwise begin with step 1.

## 1. Read

Read `read.md` beside this skill, and `reading_definition_and_plan.md` beside it, each unless
step 0 had you read it.

## 2. Cut the tasks

Read `cut_tasks.md` beside this skill. Where the reading of the product's guidelines in step 1
found a styleguide, general coding file or testing guidelines missing or uncertain, or the
approved scope has a task create the first file of a kind of code, work on a kind that has files
but no entry in the guidelines index, make the first test of a level, or extend existing
guidelines, read `guideline_tasks.md` beside this skill too; `cut_tasks.md` points to it at the
same place.

## 3. Assign the projected entries

Read `assign_entries.md` beside this skill.

## 4. Place the open questions

Read `place_questions.md` beside this skill.

## 5. Write, check and ask

Read `write_and_check.md` beside this skill; in a turn dispatched through a refinement conversation
path it points to `delegated_mode.md` for what changes.

## 6. The critique

Read `critique_plan.md` beside this skill; in a turn dispatched through a refinement conversation
path it points to `delegated_mode.md` for what changes.

## 7. Hand over

Read `hand_over.md` beside this skill; in a turn dispatched through a refinement conversation
path it points to `delegated_mode.md` for what changes.
