---
name: find-foundation-entries
description: Use when a source has to be searched for what should become entries of a product's foundation — decisions, invariants, glossary terms, environment facts, changes to the part map — before any is written; for now, a project definition whose settlements are to be projected before the project is broken into tasks, or a task whose refinement's settlements are to be kept for its cycle.
---

# Find foundation entries

Finds in a source what should become entries of a product's foundation, puts it before the human as
a table of candidates, and hands every accepted one to the skill of its element, or, for a task,
keeps it as a row of the task document. It writes no entry itself. The rules of each entry stand in
its element's template; how a skill asks stands in `elements/common/way_of_working.md`. This skill
serves a project definition and the refinement of a task for now; the breakdown of a project, the
return step of a task (WAY-11) and the entry of the process into an existing product (WAY-28) will
call it too, each adding what it needs (WAY-115, WAY-134).

This skill lives in `elements/common/skill/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel`
prints in the session's working directory; in a product, it is the product's pinned `.the-way`.
`elements/common/` is there, and each skill named below or in the files beside this skill is the
project skill of that name with the `the-way-` prefix.

## What the caller gives

The caller gives the source, the next reader and the mode of the entries. Their values, and what
else changes with the caller at steps 1, 2, 4 and 5, stand in the file of your variant:

| The caller | Variant | File beside this skill |
|---|---|---|
| `define-project`, with a project definition as the source and projected entries into its section "Projected foundation changes" as the mode | project definition | `definition_variant.md` |
| `refine-task`, with a task document as the source and rows of its section "Settlements to record" as the mode — "task mode" to `refine-task` and to the skills of guidelines that hand back to it | task | `task_variant.md` |

Read the file of your variant in full once, at step 1; where you come to step 2, 4 or 5 without
having read it, read it first.

When the section already holds a working table, resume from the first row whose state is neither
`rejected` nor `written`, or, for a task, from the first row still `waiting`.

## 1. Read

Read the file of your variant in full — `definition_variant.md` for a project definition,
`task_variant.md` in task mode — then carry out `read.md` beside this skill, which has you carry
out that file's lines for step 1.

## 2. Build the table

Carry out `build_table.md` beside this skill, which has you carry out the lines for step 2 of
`definition_variant.md` for a project definition, of `task_variant.md` in task mode.

## 3. The human cuts

The human accepts or rejects rows, all at once or a few at a time. Write each state into the
working table as soon as it is given.

## 4. Row by row

For a project definition, carry out the lines for step 4 of `definition_variant.md`. In task mode
this step does not run; carry out in its place the lines for step 4 of `task_variant.md`.

## 5. Close

For a project definition, carry out the lines for step 5 of `definition_variant.md`; in task mode,
the lines for step 5 of `task_variant.md`.
