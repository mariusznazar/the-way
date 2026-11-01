---
name: maintain-testing-guidelines
description: Use when a product's tests need testing guidelines written before its first test, its existing tests audited for them, or its testing guidelines refreshed or extended — leading those matters of a testing-guidelines task's refinement with the human.
---

# Maintain testing guidelines

Leads the matters of testing guidelines in a task's refinement: it recognizes what the product's
tests already have, gathers the starting set of the guidelines or audits the tests, and settles with
the human every level, recipe, exemplar test, exclusion and invariant the testing guidelines are to
carry, so that the task's cycle can write them from the task document alone. What every file of
guidelines holds stands in `product-guidelines/template.md`; what testing guidelines add, and how
the cycle's author writes their file, in `product-guidelines/testing/template.md`, each rule citing
its decision; how a skill asks stands in `elements/common/way_of_working.md`; the critique in
`elements/common/critique/SKILL.md`; how an entry is written in the skill of its element. This
skill holds the order of the work and restates none of them.

This skill lives in `product-guidelines/testing/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel` prints in
the session's working directory; in a product, it is the product's pinned `.the-way`. The files
named below lie there, and each skill named below is the project skill of that name with the
`the-way-` prefix. The files beside this `SKILL.md` hold what one step or one variant of the work
needs; each is read when the step or variant that names it comes, not at the start.

## Where the skill works

It runs inside the refinement of one task whose outcome is testing guidelines — written, refreshed
or extended — or the exemplar test of a level, a task the product's backlog holds or one opened for
it (WAY-107). `refine-task` opens or resumes the task through its steps 1 and 2; this skill takes
over at its step 3 for the matters of the testing guidelines and hands back to its step 4, or, where
its audit stops for the coding skill's, to its step 3, as `hand_back.md` gives.
Refinement and the task cycle find applicable and missing guidelines through
`product-guidelines/reading.md`; this skill owns settling their testing-guideline meanings. The task
writing the missing file does not wait for its own output (WAY-215). One task may carry the coding
and the testing guidelines together, each skill leading its own matters in that refinement
(WAY-247). A product that pinned the-way before this skill existed reaches it once a task moves the
pin, as `installation/README.md` gives it.

| | This skill, in the refinement | The cycle's author, in `implement-task` |
|---|---|---|
| Writes | the task document, through `refine-task`'s steps, and the reports of the research under `.runs/testing/`, which the product's git ignores | the product's entries, through the skill of each element, in the foundation step; the file `guidelines/testing.md`; the test of each new invariant, seen failing once (WAY-08); the changes to the instruction files and to the part map |
| Never writes | the foundation, the testing guidelines, the product's tests, its code or any other file git tracks, which it leaves as it found them (WAY-01, WAY-28) | a meaning the task did not settle (WAY-172) |

A meaning reaches the code only through the task document: the human's acceptance of the whole
document before the cycle approves every new or changed meaning it carries, and a meaning the human
has not settled stays a question of the task, never a line the cycle could build on (WAY-172,
WAY-124). Using a meaning that a decision of the product's log already carries takes no approval.

## Rules that hold across the steps

- The cycle's author was not in the conversation and reads only the task document, so what the
  skill writes there is written for a reader who was not in it.
- **How to show.** Show each choice by its effect on the product in plain words — "the tests of the
  account server talk to a real database, so a broken query turns them red, at the price of a
  slower run", "a change that loosens what a test checks says what changed in the requirement, or
  the review reads it as hiding a fault" — never by the name of a technique or a tool, with the ways
  open, their cost and a recommendation. Put every choice to the human, a choice the skill
  recommends included, and after a choice that enters a binding part ask the one question "How a
  skill asks" gives. Before first using a term of the field — a level of tests, a double, a
  property test — say in plain words what it means (WAY-174, WAY-113).
- Extend what exists: the recipes are written for the test tool the product runs, never for a
  second tool beside it. A new test tool or a library of property tests is a technology choice:
  record it as a question of the task, never settle it (WAY-248, WAY-121).
- Write each answer under its question in the task document before asking the next, as
  `refine-task` step 3 gives.

## Orchestrated mode

When `refine-task` runs in orchestrated mode — a testing-guidelines task of a project plan led by
`lead-project` (WAY-154, WAY-155), which a project orchestrator dispatched with a
conversation-file path — read `orchestrated_mode.md` beside this skill before step 1 and follow it
at every step.

## 0. Read

Nothing is read at the start: each step below names the files it needs. What `refine-task` read at
its steps 1 and 2 — its own `project-level/task/skill/SKILL.md`, the task template
`project-level/task/template.md`, the section "How a skill asks" of
`elements/common/way_of_working.md`, the product's foundation as it selected it, and the guidelines
of the parts the task touches — is not read again. A session that has not read them in this
conversation — it opened this skill directly, or resumed the work in a new one — goes through
`refine-task` steps 1 and 2 first (WAY-266).

## 1. Recognize

At step 1, read `recognize.md` beside this skill.

## 2. Starting set

At step 2, which step 1 gives for tests with no testing guidelines yet and for a refresh or an
extension, read `product-guidelines/testing/template.md` in full and `starting_set.md` beside this
skill. Where the human has no preference at the first guidelines, and at every extension,
`starting_set.md` sends you to `research.md`, also beside this skill (WAY-265).

## 3. Audit

At step 3, where the product has tests and step 1 gave the audit — tests and no testing
guidelines, or guidelines refreshed or extended — read `audit.md` beside this skill and then
`product-guidelines/audit_end.md`, which ends the audit. In that audit, where the task carries the
coding guidelines too (WAY-247), read also `product-guidelines/coding/recognize.md`, that skill's
step 1, before the audit ends: `audit_end.md` says what it decides (WAY-265). Where the task's
required outcome is itself the first test of a level, read `new_level.md` beside this skill; a new
level is no audit and has no such end. For either, read `product-guidelines/testing/template.md` in
full unless step 2 did (WAY-256). Otherwise there is no step 3.

## 4. Settle with the human

At step 4, read `product-guidelines/template.md` in full, `product-guidelines/testing/template.md`
in full unless an earlier step did, and `settle.md` and `task_document.md` beside this skill, and,
where step 3's audit ran, `product-guidelines/audit_end.md` unless an earlier step did. For
each new tool or library left as a technology question of the task, `settle.md` sends you to
`new_tools.md`, also beside this skill (WAY-265).

## 5. Hand back

At step 5, read `hand_back.md` beside this skill, `task_document.md` unless step 4 did, and, where
step 3's audit ran, `product-guidelines/audit_end.md` unless an earlier step did. Where the human
answered yes to a backlog task for a deferred `grave` cause, read
`project-level/task/skill/guideline_findings.md` for its section "A deferred cause of an audit"
(WAY-265).
