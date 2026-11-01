---
name: maintain-coding-guidelines
description: Use when a product's code needs coding guidelines written before its first code, its existing code audited for them, an exemplar settled for a kind of code, or its coding guidelines refreshed or extended — leading those matters of a coding-guidelines task's refinement with the human.
---

# Maintain coding guidelines

Leads the matters of coding guidelines in a task's refinement: it recognizes what the product's code
already has, gathers the starting set of standing checks or audits the code, and settles with the
human every standing check, exemplar and invariant the coding guidelines are to carry, and the
product's decision on the rules on failures and logs, so that the task's cycle can write them from
the task document alone. What every file of guidelines holds
stands in `product-guidelines/template.md`; what coding guidelines add, and how the cycle's author
writes their files, in `product-guidelines/coding/template.md`, each rule citing its decision; how
a skill asks stands in `elements/common/way_of_working.md`; the critique in
`elements/common/critique/SKILL.md`; how an entry is written in the skill of its element. This
skill holds the order of the work and restates none of them.

This skill lives in `product-guidelines/coding/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel` prints in
the session's working directory; in a product, it is the product's pinned `.the-way`. The files
named below lie there, and each skill named below is the project skill of that name with the
`the-way-` prefix. The files beside this `SKILL.md` hold what one step or one variant of the work
needs; each is read when the step or variant that names it comes, not at the start.

## Where the skill works

It runs inside the refinement of one task whose outcome is coding guidelines — written, refreshed
or extended — or the exemplar of a kind of code, a task the product's backlog holds or one opened
for it (WAY-107). `refine-task` opens or resumes the task through its steps 1 and 2; this skill
takes over at its step 3 for the matters of the coding guidelines and hands back to its step 4, or,
where its audit stops for the testing skill's, to its step 3, as `hand_back.md` gives.
Refinement and the task cycle find applicable and missing guidelines through
`product-guidelines/reading.md`; this skill owns settling their coding-guideline meanings. The
task writing the missing general file does not wait for its own output (WAY-215). One task may carry
the coding and the testing guidelines together, each skill leading its own matters in that
refinement (WAY-247). A product that pinned the-way before this skill existed reaches it once a task
moves the pin, as `installation/README.md` gives it.

| | This skill, in the refinement | The cycle's author, in `implement-task` |
|---|---|---|
| Writes | the task document, through `refine-task`'s steps, and the reports of the research and of the trial run under `.runs/coding/`, which the product's git ignores | the product's entries, through the skill of each element, in the foundation step; the files of the coding guidelines; each adopted tool, installed and configured; the one reformatting of the code where the task settles it; the test of each new invariant (WAY-08); the changes to the instruction files and to the part map |
| Never writes | the foundation, the coding guidelines, the product's code or any other file git tracks, which it leaves as it found them (WAY-01, WAY-28) | a meaning the task did not settle (WAY-172) |

A meaning reaches the code only through the task document: the human's acceptance of the whole
document before the cycle approves every new or changed meaning it carries, and a meaning the human
has not settled stays a question of the task, never a line the cycle could build on (WAY-172,
WAY-124). Using a meaning that a decision of the product's log already carries takes no approval.

## Rules that hold across the steps

- The cycle's author was not in the conversation and reads only the task document, so what the
  skill writes there is written for a reader who was not in it.
- **How to show.** Show each choice by its effect on the product in plain words — "a change that
  adds a library with a known security hole does not get in", "every new endpoint checks its input
  as the exemplar does" — never by the name of a linter's rule or a value of a tool's
  configuration, with the ways open, their cost and a recommendation. Put every choice to the
  human, a choice the skill recommends included, and after a choice that enters a binding part ask
  the one question "How a skill asks" gives. Ask for decisions, never for single rules: a set of
  rules is adopted whole, its split shown as "this many rules will block a change; these few
  flagged sound code here and stay as examples", each of the few shown by what it flagged. Before
  first speaking of a linter, a formatter or an audit of dependencies, say in plain words what it
  does for the product (WAY-174, WAY-113).
- Extend what exists: rules are added to the linter the product runs, never a second linter beside
  it, and a way of writing log lines the product or its language already gives raises no question.
  A new linter, formatter or audit of dependencies, or a library a chosen form of a log line needs,
  is a technology choice: record it as a question of the task, never settle it (WAY-210, WAY-121,
  WAY-277).
- A choice found in the product's files — a tool's configuration, a habit its files share — is a
  proposal, never a rule, until the human settles it. An existing choice the human keeps becomes a
  decision whose rationale is the human's words or `unknown`, never one the agent infers (WAY-29).
- Write each answer under its question in the task document before asking the next, as
  `refine-task` step 3 gives.
- **The route of one kind** (step 1's mode of one kind whose files the product already has).
  Steps 4 and 5 settle and check only what concerns that kind: its identifier, its exemplar, the
  status of its files and the rules a script checks of it with their invariants; the task's *To do*
  gains `guidelines/coding-<kind>.md` with its row in the index of `guidelines/coding.md`
  (WAY-216).

## Orchestrated mode

When `refine-task` runs in orchestrated mode — a coding-guidelines task of a project plan led by
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

At step 1, read `recognize.md` beside this skill. It gives the mode of the work.

## 2. Starting set

At step 2, which step 1 gives before the first code, for the product's code that has no coding
guidelines yet — no `guidelines/coding.md`; a kind of code without a file of its own is not that
case — and at every refresh or extension, read `product-guidelines/coding/template.md` in full and
`starting_set.md` beside this skill; the question of preferences is worded as "How to show" gives.
Where the human has no preference at the first coding guidelines, and at every extension,
`starting_set.md` sends you to `research.md`, also beside this skill (WAY-265).

## 3. Trial run and audit

At step 3, where the product has code and step 1 gave the trial run and the audit — code and no
coding guidelines, or coding guidelines refreshed or extended — read
`product-guidelines/coding/template.md` in full unless step 2 did, `trial_run.md` and `kinds.md`
beside this skill, and then `product-guidelines/audit_end.md`, which ends the audit. In that audit,
where the task carries the testing guidelines too (WAY-247), read also
`product-guidelines/testing/recognize.md`, that skill's step 1, before the audit ends:
`audit_end.md` says what it decides (WAY-265). Where step 1 gave the mode of one kind whose files
the product already has, and not the trial run and the audit, read the template in full unless an
earlier step did, and `kinds.md` alone, for that kind; there is no trial run on that route, and
that comparison, being no audit, has no such end.

- **A new kind.** Where the task creates the first file of a kind of code, that file is the kind's
  exemplar, and its file of guidelines comes into being with it (WAY-200, WAY-209): step 4 settles
  the kind's identifier, the path the file takes and the rules a script checks of it.

## 4. Settle with the human

At step 4, read `product-guidelines/template.md` in full, `product-guidelines/coding/template.md`
in full unless an earlier step did, and `settle.md` and `task_document.md` beside this skill, and,
where step 3's audit ran, `product-guidelines/audit_end.md` unless an earlier step did. For
each new tool or library left as a technology question of the task, `settle.md` sends you to
`new_tools.md`, also beside this skill (WAY-265). On the route of one kind, "The route of one kind"
above limits what these files settle.

## 5. Hand back

At step 5, read `hand_back.md` beside this skill, `task_document.md` unless step 4 did, and, where
step 3's audit ran, `product-guidelines/audit_end.md` unless an earlier step did. Where the human
answered yes to a backlog task for a deferred `grave` cause, read
`project-level/task/skill/guideline_findings.md` for its section "A deferred cause of an audit"
(WAY-265).
