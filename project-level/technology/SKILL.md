---
name: settle-technology
description: Use when a project definition of a product that uses the-way has to settle the technology and architecture choices its project needs before the readiness gate — a language, a framework, a library, a store of data, a way of logging in, a place to run — or to resume that step from the definition's Technology section. Also runs at a task document, with a note saying what for, for a choice no definition settles or one the human opens, and resumes from that document's Technology section.
---

# Settle technology

Leads the step of the project level that settles technology. It runs at a document: a project
definition, before the readiness gate (WAY-121) and after the step that finds the definition's
foundation entries, or a task document, with a note saying what the run is for (WAY-265). "The
document", here and in the files beside this skill, is the definition or, in a run at a task, the
task document with its note. The step lists the choices the document needs, finds the entry that
already settles each, and settles every other one with the human: at a definition as a projected
decision, at a task as a settled question of the task document. The human weighs consequences for
the product, not technologies
(WAY-123). The form and rules of the Technology section — which choices it lists, its markers, the
weighing and the tests of options — stand in `definition_template.md`, and the section's form in a
task document in `project-level/task/template.md`; how a skill asks stands in
`elements/common/way_of_working.md`; the critique stands in `elements/common/critique/SKILL.md`;
this skill holds the order of the work and the rules that hold across it, and a file beside it
holds the work of each step.

This skill lives in `project-level/technology/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel`
prints in the session's working directory; in a product, it is the product's pinned `.the-way`. The
project level's directory, `project-level/`, is there, and each skill named in this skill or in a
file beside it is the project skill of that name with the `the-way-` prefix.

The step writes only into the document, a definition or a task document, never into the product's
foundation (WAY-106).

The comparison of a choice is written to `.runs/technology/<choice>.md`, the choice's name in lower
case with hyphens for spaces, which the product's Git ignores.

## 0. Start or resume

Where a task document is named, read `task_run.md` beside this skill first: it holds what a run at
a task does in place of what the steps below and their files give. Where a note comes with no task
document, start `refine-task` with the note as the request: it creates the document and calls this
step from its step 3, the note passing to the run whether or not the choice is a reserved choice.

At a definition, read `start.md` beside this skill. Where the Technology section holds a list, read
`running_product.md` beside this skill too, and `list.md` beside this skill when the look it gives
adds an item to the list or the human adds or changes one.

## 1. List the choices

Where the Technology section reads `TODO`, read `list.md` beside this skill, and `running_product.md`
beside this skill where the project brings behaviour a user sees in the running product.

## 2. Settle the open choices

Where the list holds an open choice, read `settle.md` beside this skill. The research agent's work
stands in `research.md` beside this skill: you give its path to each research agent, as `settle.md`
says, and need not read it. Read `elements/common/critique/SKILL.md` when the first critique of a
comparison or of a table comes.

## 3. Close

Where the list holds no open choice, read `close.md` beside this skill.

A definition approved before this step changes in the sections its fingerprint covers, and goes
through the gate again
(WAY-118).
