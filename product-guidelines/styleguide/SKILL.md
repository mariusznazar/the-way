---
name: maintain-styleguide
description: Use when a product's user interface — its screens, an admin panel added to a backend included — needs a styleguide created before its first screen, audited where screens exist, or refreshed or extended, leading those matters of a styleguide task's refinement with the human.
---

# Maintain a styleguide

Leads the styleguide matters of a styleguide task's refinement: it recognizes what the product's
user interface already has, gathers the starting rules or audits the screens, and settles with the
human every meaning, value and check the styleguide is to carry, so that the task's cycle can write
the styleguide from the task document alone. What every file of guidelines holds stands in
`product-guidelines/template.md`; what a styleguide adds, and how the cycle's author writes its
file, in `product-guidelines/styleguide/template.md`, each rule citing its decision; how a skill
asks stands in `elements/common/way_of_working.md`; the critique in
`elements/common/critique/SKILL.md`; how an entry is written in the skill of its element. This
skill holds the order of the work and restates none of them.

This skill lives in `product-guidelines/styleguide/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel` prints in
the session's working directory; in a product, it is the product's pinned `.the-way`. The files
named below lie there, and each skill named below is the project skill of that name with the
`the-way-` prefix. The files beside this `SKILL.md` hold what one step or one variant of the work
needs; each is read when the step or variant that names it comes, not at the start.

## Where the skill works

It runs inside the refinement of one task whose outcome is a styleguide, a task the product's
backlog holds or one opened for it (WAY-107). `refine-task` opens or resumes the task through its
steps 1 and 2; this skill takes over at its step 3 for the styleguide's matters and hands back to
its step 4. Refinement and the task cycle find applicable and missing guidelines through
`product-guidelines/reading.md`; this skill owns settling their styleguide meanings. The task
writing a missing styleguide does not wait for its own output (WAY-215).

| | This skill, in the refinement | The cycle's author, in `implement-task` |
|---|---|---|
| Writes | the task document, through `refine-task`'s steps, and the research reports under `.runs/styleguide/<part>/`, which the product's git ignores | the product's entries, through the skill of each element, in the foundation step; the styleguide's file; the values of design tokens with their sources; the page of every state; the test of each invariant (WAY-69); the changes to the instruction files and to the part map |
| Never writes | the foundation, the styleguide's file, the product's code (WAY-01, WAY-28) | a meaning the task did not settle (WAY-172) |

A meaning reaches the code only through the task document: the human's acceptance of the whole
document before the cycle approves every new or changed meaning it carries, and a meaning the human
has not settled stays a question of the task, never a line the cycle could build on (WAY-172,
WAY-124). Using a meaning that a decision of the product's log already carries takes no approval.

## Rules that hold at every step

- The cycle's author was not in the conversation and reads only the task document, so what the
  skill writes there is written for a reader who was not in it.
- **How to show.** Show each choice by what someone using the product sees — "the button that saves
  stands out; the one that deletes is red, and its text white" — never by the names or values of
  design tokens, with the ways open, their cost and a recommendation. Put every choice to the human,
  a choice the skill recommends included, and after a choice that enters a binding part ask the one
  question "How a skill asks" gives. Before first using a term of the field — contrast, focus, a
  state of a control — say in plain words what it means (WAY-174, WAY-113).
- Write each answer under its question in the task document before asking the next, as
  `refine-task` step 3 gives.

## Orchestrated mode

When `refine-task` runs in orchestrated mode — a project orchestrator dispatched it with a
conversation-file path, for a styleguide task of a project plan — read `orchestrated_mode.md`
beside this skill before step 1 and follow it at every step.

## 0. Read

Nothing is read at the start: each step below names the files it needs. What `refine-task` read at
its steps 1 and 2 — its own `project-level/task/skill/SKILL.md`, the task template
`project-level/task/template.md`, the section "How a skill asks" of
`elements/common/way_of_working.md`, and the product's foundation as it selected it — is not read
again.

## 1. Recognize

At step 1, read `recognize.md` beside this skill. A product with no user interface ends there.

## 2. Starting rules

At step 2, read `product-guidelines/styleguide/template.md` in full and `starting_rules.md`
beside this skill.

## 3. Audit

At step 3, where the user interface has screens — a first styleguide of a product with screens, or
an existing styleguide whose screens changed since it was written — read `audit.md` beside this
skill. Otherwise there is no step 3.

## 4. Settle with the human

At step 4, read `product-guidelines/template.md` in full, and `settle.md` and `task_document.md`
beside this skill.

## 5. Hand back

At step 5, read `hand_back.md` beside this skill.
