---
name: define-project
description: Use when a project of a product that uses the-way has to be defined before it is broken into tasks — an idea, a concept or a note to turn into a project definition, a definition to resume from its status line, or a definition to take through the readiness gate.
---

# Define a project

Leads the first two steps of the project level: the definition, written with a human, and the
readiness gate; the settling of the project's technology, between them, it hands to
`settle-technology`. A definition records what is settled about the product before the project is
broken into tasks — as projected entries of the foundation — so that the breakdown and the tasks
guess as little as they can. The form of a definition and the rule of each section stand in
`definition_template.md`; how a skill asks stands in `elements/common/way_of_working.md`; this
skill holds the order of the work. The decisions that set its rules are cited below.

This skill lives in `project-level/skill/` of the-way. In the-way itself, the-way is the checkout
or worktree the session works in, the directory `git rev-parse --show-toplevel` prints in
the session's working directory; in a product, it is the product's pinned `.the-way`. The project
level's directory, `project-level/`, is there, and each skill named below is the project skill of
that name with the `the-way-` prefix.

The project level reads the product's foundation and writes nothing in it
(WAY-106).

## Delegated definition change and gate

When `lead-project` dispatches a definition edit or step 7 through a refinement conversation
path, read `delegated_mode.md` beside this skill first (WAY-156): it holds what that path changes
in the workflow below, and the file of step 7 points back to it.

## Rules that hold across the steps

- Speak the language the human opened in; the definition is written in it, as the template gives.
- What the files can answer, read yourself instead of asking
  (WAY-112).
- Once the definition is written (step 3), write each answer into it, with its status line, before
  the next question, so that a fresh agent reading only the file knows where the work stands
  (WAY-112).
- A change of the definition after the gate goes through the gate again
  (WAY-118).

## 0. Start or resume

- Read `definition_template.md` in full, and the section "How a skill asks" of
  `elements/common/way_of_working.md`.
- When the human names an existing definition — in a dispatched turn, the definition its
  conversation file names — read `existing_definition.md` beside this skill.
- Otherwise begin with step 1.

## 1. The idea

Read `idea.md` beside this skill.

## 2. Read the foundation for the idea

Read `read_foundation.md` beside this skill.

## 3. The first write

Read `first_write.md` beside this skill.

## 4. Rounds through the sections

Read `rounds.md` beside this skill.

## 5. Find the entries

Read `find_entries.md` beside this skill.

## 6. Settle the technology

Read `technology.md` beside this skill.

## 7. The readiness gate

Read `gate.md` beside this skill; in a turn dispatched through a refinement conversation path it
points to `delegated_mode.md` for what changes.
