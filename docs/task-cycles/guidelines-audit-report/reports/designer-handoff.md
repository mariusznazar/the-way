# Handoff — designer of the spec

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/guidelines-audit-report`
- This is the-way working on itself, at the checkout above; there is no `.the-way`, and the-way's
  files are read from this worktree, never from another checkout. Skills named below are this
  repository's files, listed here by path.
- Target branch `foundations`, base `2f51e6c`, task branch `task/guidelines-audit-report`. You make
  no commit and change no file of the repository. You write two files only, both ignored by Git:
  - the spec: `.runs/task-cycles/guidelines-audit-report/spec.md`
  - your report: `.runs/task-cycles/guidelines-audit-report/reports/designer.md`
- The full test run of the base is running in this worktree in the background: touch no tracked
  file.

## Your method and stage

Read `task-cycle/spec/SKILL.md` whole and follow it as the **designer**. Read each file it names
when the step that names it comes. Your boundary: you return with `questions`, `done` or
`reserved`, before any plan or code; you start no later stage.

## The task

Frozen task, read it whole: `.runs/task-cycles/guidelines-audit-report/task.md`. It was copied from
the author's private notes on 2026-11-01, accepted there with `Status: ready for cycle`,
`Project relation: independent`. Its citations stand at `foundations` `2f51e6c`, the base. It says
of itself that the scale and the order stand in it whole, so the cycle needs no skill of the course
it names: read none, and no note of the author beyond it.

The task's *To do*, its answers to questions 1–9 and its six rows of *Settlements to record* are
settled. They bind you; your spec does not reopen them.

## Answers of step 4

- Trust boundary: no at the start. Where your design changes a file the part map names as one, say
  so in the spec, by file.
- Operation that cannot be undone: no.
- Open design choice: yes, the choices below.

## The choices this spec settles

The first four are the task's *Questions carried to cycle*.

1. **The English words of the four grades** (question 2). They must differ from Critical, Important
   and Minor of the review of a change, so that no word has two meanings in the-way. Check them
   against the glossary too: `critical flow` already stands there. Say how a grade reads to the
   human, who hears it in plain words (WAY-174), in a product that writes in another language.
2. **How the audit shows the cost of a fix**, on which the order of To do 4 stands, so that the
   human sees where the order comes from. The task keeps the scale free of numbers (question 7,
   *Not chosen*).
3. **The English words for a finding of an audit and for a cause**, given that the review of a
   change uses `finding` and that the audits of screens and tests use `charge`. Apply the test of
   `elements/glossary/` to say whether any of them needs an entry, and say what happens to the word
   `charge` in the two audit files and the task documents.
4. **One decision or changes.** Whether rows 1–6 enter as one new decision shared by the three
   skills, which narrows WAY-187, WAY-201 and WAY-250, or as changes of those decisions, or as
   several entries, given that a decision holds one to three binding sentences
   (`elements/decisions/template.md:25`). Say which row each entry carries, how a row's meaning that
   needs more sentences splits without losing it, and what the three decisions read after the
   change, their *Rejected* included: the task's *Decisions in play* says the *Rejected* of WAY-250
   has to be rewritten with its change.
5. **One list across disciplines.** Rows 3 and 4 and question 7 give a task joining code and tests
   one list and one order, while WAY-247 has each skill lead its own discipline's matters. Settle
   who merges the two audits' causes, at which step, and where the verification of To do 5 and the
   top of the list then stand.
6. **Where each result stands in the task document.** To do 6 and 8 put the full list "lower in the
   document", and `task_document.md` of each skill today sends an audit's results to *Context*.
   Settle the section of each thing To do 8 names, against `project-level/task/template.md`, and
   the form of the list: what a line of it holds, so that the grade, the place in the order, the
   places in the code, the cost and the mark of verification each have a home, and a deferred cause
   its reason.

## What the design has to fit, for you to check, not a design

Each of these is a place where the settled rows meet the existing text. Where one calls for a
design decision, make it in the spec; where it follows with no way open, name it under
*Foundation entries* or *Left to the maker*.

- Rows 1–6 become entries of the decision log, each row whole, unless the search of the foundation
  finds it stated (WAY-134, `task-cycle/skill/foundation_step.md`). Each row's *Rejected* holds the
  ways its source keeps. Rows 1 and 2 of *Decisions in play* name how WAY-100 and WAY-27 bear on
  row 1: the entry names what is adopted, where and why, and describes it in its own words.
- The shared file the task requires for the scale (To do 1): its path and name beside the existing
  `product-guidelines/reading.md`, and how the three skills reach it, against WAY-256 and WAY-265.
  Say whether the merging, the order, the top of the list and the verification stand in it too or
  in each discipline's file, given that a skill keeps a step's text beside it and that the three
  audits must end alike. The three audit files today are `product-guidelines/coding/kinds.md` with
  `trial_run.md`, `product-guidelines/styleguide/audit.md` and `product-guidelines/testing/audit.md`.
- The audit runs at step 3 of each skill, the human decides at step 4 (`settle.md`), and each
  `SKILL.md` says how to show a choice to the human. Say in which step each of To do 4 to 7 happens.
  To do 5 comes before the human sees the top of the list. WAY-120's critique of a complete set of
  proposals stays after it: say how the two meet in each skill's order.
- To do 7: the route of a deferred critical cause into the backlog, through
  `project-level/task/skill/guideline_findings.md:12-17`, the answer `plan change` for a plan member,
  and orchestrated mode (`product-guidelines/*/orchestrated_mode.md`), where the skill ends the turn
  rather than asks. Say what a skill of guidelines does itself and what it returns to `refine-task`,
  and whether `hand_back.md` of each skill checks anything new.
- Row 2 and question 5: a trust boundary with no test of its refusal, and the linter's rules broken
  from one source, join the list; what they set off today stays (WAY-205, WAY-235, WAY-250). The
  linter's result comes from `trial_run.md`, a step run before the kinds in `coding/SKILL.md`, and
  WAY-201 names as a violation an audit that ends with reports by the names of their rules. A
  reformatting of the code is no finding.
- To do 2 has each finding belong to one cause, while question 1 keeps the `do not copy` list apart:
  say how a `do not copy` place relates to a cause, without a file standing twice in a way that
  misleads a reader, and without changing WAY-200.
- The route of one kind (WAY-216, `coding/kinds.md:6-9`) and the first test of a new level
  (`testing/SKILL.md:98`) are no audit and get no such end. A refresh and an extension run the audit
  as they do today (WAY-251).
- To do 3 keeps the four categories of WAY-187 at the cause.
- To do 5: what cannot be seen without the running product stays marked unchecked
  (`styleguide/audit.md:11-13`); a code audit and a test audit have their own forms of "checking the
  effect occurs" (question 6, the note after criticism). Say how the shared text reads for all three.
- What the scale binds: WAY-173. The scale binds the template and the skill, not a product's code.
- Whether any test of this repository reads these files, and whether the shared file needs anything
  from `installation/` (the three `installation/test_*_installation.py` name each skill's path). A
  skill's *description* changing would call for `agent-instructions/skill_entry_points.py --write`
  (root `AGENTS.md`).
- `README.md` of this repository, `installation/README.md`, `project-level/` and anything else that
  says how these audits end: search once.

## What to read

Of the foundation, each whole, from `foundations/decisions.md`: WAY-05, WAY-14, WAY-22, WAY-24,
WAY-25, WAY-26, WAY-27, WAY-29, WAY-30, WAY-33, WAY-36, WAY-100, WAY-114, WAY-120, WAY-134, WAY-135,
WAY-161, WAY-172, WAY-173, WAY-174, WAY-178, WAY-185, WAY-187, WAY-198, WAY-199, WAY-200, WAY-201,
WAY-204, WAY-205, WAY-207, WAY-216, WAY-235, WAY-247, WAY-250, WAY-251, WAY-256, WAY-265, WAY-266;
each opens at its heading `### WAY-<n> — `. The log is large: read by those ranges, not whole. From
`foundations/part_map.md`, the entries `product-guidelines`, `project-level` and `decisions`. From
`foundations/glossary.md`, `critical flow`, `exemplar`, `guidelines`, `part`, `standing check`,
`open design choice` and any entry on a grade or a blocking finding you find by search. From
`foundations/invariants.md`, those whose *Part* names `product-guidelines` or `every`, as far as the
work reaches them.

Files, whole: `product-guidelines/reading.md`, and of `product-guidelines/coding/`,
`product-guidelines/styleguide/` and `product-guidelines/testing/` each `SKILL.md`, `settle.md`,
`hand_back.md`, `task_document.md`, `orchestrated_mode.md`, `recognize.md`; `coding/kinds.md`,
`coding/trial_run.md`, `styleguide/audit.md`, `testing/audit.md`, `testing/new_level.md`;
`project-level/task/template.md`, `project-level/task/skill/guideline_findings.md`,
`task-cycle/review/SKILL.md` (for its grades only), `task-cycle/skill/foundation_step.md`,
`elements/decisions/template.md`, `elements/glossary/` as far as its test of a term goes.

The-way has no `guidelines/` directory of its own, so no guideline file applies.

## Your return

Write the report as `task-cycle/spec/design.md` gives, with **Searches not found or unclear**, and
return only: your status, a one-line result and the report's path.
