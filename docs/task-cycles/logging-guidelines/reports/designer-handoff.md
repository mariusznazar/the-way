# Handoff — designer of the spec

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/logging-guidelines`
- This is the-way working on itself, at the checkout above; there is no `.the-way`, and the-way's
  files are read from this worktree, never from another checkout. Skills named below are this
  repository's files, listed here by path.
- Target branch `foundations`, base `ea4694e`, task branch `task/logging-guidelines`. You make no
  commit and change no file of the repository. You write two files only, both ignored by Git:
  - the spec: `.runs/task-cycles/logging-guidelines/spec.md`
  - your report: `.runs/task-cycles/logging-guidelines/reports/designer.md`
- The full test run of the base is running in this worktree in the background: touch no tracked
  file.

## Your method and stage

Read `task-cycle/spec/SKILL.md` whole and follow it as the **designer**. Read each file it names
when the step that names it comes. Your boundary: you return with `questions`, `done` or
`reserved`, before any plan or code; you start no later stage.

## The task

Frozen task, read it whole: `.runs/task-cycles/logging-guidelines/task.md`. It was copied from the
author's private notes on 2026-11-01, accepted there with `Status: ready for cycle`,
`Project relation: independent`. Its citations stand at `foundations` `ea4694e`, the base.

The task's *To do*, its answers to questions 1–12, read with the marks of which answer replaces
which, and its eight rows of *Settlements to record* are settled. They bind you; your spec does not
reopen them.

**One restriction stands in the task's Context and binds you:** apart from that document, read no
note of the author and no repository of any product. A later step measures whether the process
reaches its conclusions on a product's logs by itself, and a change that knows them voids the
measure. Stay in this worktree's tracked files and the cycle's directory.

## Answers of step 4

- Trust boundary: no at the start. Where your design changes a file the part map names as one, say
  so in the spec, by file.
- Operation that cannot be undone: no.
- Open design choice: yes, the choices below.

## The choices this spec settles

1. **The product's decision.** The task's first carried question: is the product's decision on
   this part a part of the decision adopting the coding template
   (`product-guidelines/coding/settle.md:21-22`), or an entry of its own, given one to three binding
   sentences (`elements/decisions/template.md`, section "Binding sentences")? To do 3 asks that
   decision to adopt or depart, settle the principle of scope, give what the agent adds alone and
   what needs the human's consent, and name the form of a line. Settle it, say what a product's log
   ends up holding, in the case of a product with no guidelines and of one adding the part, and
   whether a product departing from the part still needs what remains.
2. **The English words.** The task's second carried question: which word the template uses for
   "przepływ", given the glossary's narrower `critical flow`, and for "część", given that `part` is
   a part of the map. Apply the test of `elements/glossary/` to say whether either word needs an
   entry, and to which reader. Say also how the word for the part reads in the skill's question to
   the human, who hears it in plain words (`product-guidelines/coding/SKILL.md`, "How to show").
3. **The form of the part in the template.** To do 1 gives five rules, and To do 3 names a "reguła
   zakresu" carrying the list of today. Settle whether that is one of the five or a sixth, whether
   identifiers and events stand together, and the heading of each rule. Settle where the required
   rules stand in the required form, whose text today gives the three standing checks first and "the
   product's further rules" after them, and what each rule's *Decision*, *Invariant*, *Good* and
   *Bad* hold, a list of today included. Settle how a product's file looks that departs from the
   whole part, and from one rule (WAY-171). A rule holds no reasons (Context).

## What the design has to fit, for you to check, not a design

Each of these is a place where the settled rows meet the existing text. Where one calls for a
design decision, make it in the spec; where it follows with no way open, name it under
*Foundation entries* or *Left to the maker*.

- Rows 1–8 become entries of the decision log, each row whole, unless the search of the foundation
  finds it stated (WAY-134). Name the entries and say which row each carries, and where a row's
  meaning needs more than one to three binding sentences, how it splits without losing it.
- Row 6 prevails over row 2 where they meet: WAY-25 asks for `narrows` and a sentence stating the
  area. Rows 2 and 3 and WAY-268 and WAY-270 name the step of technology: check the agreement.
- Row 3 and WAY-100: what is adopted, where and why, against WAY-27, since the source cannot be
  pointed to as a place a reader reaches. The task's Context holds the wording left outside the
  template, and row 3 names the source. Say how the entry carries it.
- Row 7 and WAY-268, `product-guidelines/coding/new_tools.md`,
  `project-level/technology/reserved_choices.md`: a library that writes a line is put to the human by
  which step, and when the step of technology runs instead.
- Row 8 and question 2: `product-guidelines/coding/recognize.md`, `starting_set.md`, `research.md`,
  `trial_run.md`, `kinds.md`. What a refresh that finds the part missing does, in which file; what
  an extension whose only subject is this part researches, given that it has no tool (WAY-211,
  WAY-251). To do 2 names setting up, refreshing and extending.
- To do 3: `settle.md`, `task_document.md`, `hand_back.md`. Whether the task is ready without the
  product's decision on the part, as for a standing check (WAY-202), given that the part is no
  fourth standing check. The weak points of questions 1, 3, 5, 8 and 9 go in `settle.md`.
- The file start of a program, where the last place usually stands, is outside the audit of named
  kinds (Context): say whether anything has to reach it, or that it stays as the task says.
- To do 5: the two lines of `task-cycle/review/SKILL.md`, section 2 "Review", name no part. Check
  `task-cycle/review/whole_change.md`, and how a reviewer of a change gets the guidelines (WAY-213).
- Whether a test of this repository reads any of these files: `installation/test_coding_guidelines_installation.py`
  names the skill's path. A skill's *description* changing would call for
  `agent-instructions/skill_entry_points.py --write` (root `AGENTS.md`).
- `README.md` of this repository, `installation/README.md` and anything else that says what coding
  guidelines hold: search once.

## What to read

Of the foundation, each whole, from `foundations/decisions.md`: WAY-05, WAY-22, WAY-25, WAY-27,
WAY-30, WAY-33, WAY-86, WAY-100, WAY-134, WAY-135, WAY-161, WAY-165, WAY-167, WAY-168, WAY-169,
WAY-170, WAY-171, WAY-172, WAY-173, WAY-174, WAY-198, WAY-201, WAY-202, WAY-203, WAY-207, WAY-208,
WAY-209, WAY-210, WAY-211, WAY-213, WAY-221, WAY-225, WAY-251, WAY-268, WAY-270; each opens at its
heading `### WAY-<n> — `. The log is large: read by those ranges, not whole. From
`foundations/part_map.md`, the entries `product-guidelines`, `task-cycle` and `decisions`. From
`foundations/glossary.md`, `critical flow`, `part`, `guidelines`, `standing check`, `exemplar`,
`open design choice`. From `foundations/invariants.md`, those whose *Part* names `product-guidelines`
or `task-cycle` or `every`, as far as the work reaches them.

Files, whole: `product-guidelines/template.md`, `product-guidelines/reading.md`, every file of
`product-guidelines/coding/`, `product-guidelines/testing/template.md`, `task-cycle/review/SKILL.md`,
`task-cycle/review/whole_change.md`, `elements/decisions/template.md`,
`project-level/technology/reserved_choices.md`.

The-way has no `guidelines/` directory of its own, so no guideline file applies.

## Your return

Write the report as `task-cycle/spec/design.md` gives, with **Searches not found or unclear**, and
return only: your status, a one-line result and the report's path.
