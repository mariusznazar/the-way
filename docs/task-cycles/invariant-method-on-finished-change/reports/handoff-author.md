# Handoff — the one author, whole change

## Delegation

The person who requested this cycle delegated every intermediate choice to the orchestrator
(`implement-task`). Nothing below is that person's approval of a step; the human reviews only the
request. Do not ask the human anything; send questions to the orchestrator in your report.

## Where you work

- Worktree (your working directory, the process root): `the root of the task's worktree (the repository root)`
- Branch: `task/invariant-method-on-finished-change`, base commit `46bba355e51bc671a4af604e11757d91574949b6` (= `origin/foundations`)
- The repository is the-way itself (no `.the-way` submodule). Read the files of the worktree only,
  never a copy in another checkout.
- Commit by path (`git add <path> <path>`), never `git add -A`/`.`; commit messages in English,
  after the style of `git log` of the repository; do not push.

## Your stage and method

Stage: **the whole change as the one author** (variant of `make-change`, no plan, no spec).
Method: read `task-cycle/change/SKILL.md` in full and follow it; read each file it names only when
the step or variant that names it comes. Also read `agent-instructions/README.md` (how a change to
the-way itself is made; the product's gate is the orchestrator's alone, you do not run
`python -B gate/run_tests.py` in full — focused runs such as
`python -B gate/run_tests.py elements/common` are yours).

You also do the **foundation step** with your code: read `task-cycle/skill/foundation_step.md`
whole when the entries come; write each entry through the pinned skill of its element
(`.claude/skills/the-way-record-decision`, `the-way-record-invariant`; their `SKILL.md` point to
the real files).

## The task

The frozen task: `.runs/task-cycles/invariant-method-on-finished-change/task.md` (read it whole; it
is in Polish, the code and foundation entries are in English). Do all four *To do* items and write
the three rows of *Settlements to record* (rows 1–2 as decisions, row 3 as an invariant). The
questions 1–4 are settled in it; do not reopen them. Question 4 says three places stay unchanged.

Answers of the orchestrator to the points the task leaves to the author:

- The name of the switch of `foundation_check.py` that skips the new check is yours to choose; pick
  a plain, descriptive name, document it in the script's usage/help text and in
  `elements/common/way_of_working.md` step 4.3. Find every other place that runs `foundation_check.py`
  right after writing an entry (grep the skills and templates of the elements, not only
  `way_of_working.md`) and judge whether it should pass the switch; name each in your report.
- Row 1 leaves open whether the rejected way (a sentence in `task-cycle/plan/SKILL.md`) goes to
  *Rejected* of WAY-61. Decide by the decisions' template and `elements/common/rules.md`
  (*Rejected* takes the ways not chosen that the row's source keeps — the task's question 1 keeps
  it); record your choice as a row of your report.
- Row 2: whether the new check is a new decision or belongs in WAY-61 is yours, by the template:
  the task says row 2 is a decision of its own (check in every run, skipped only after writing an
  entry, with a switch). Keep the weak points the task names in the entry's wording where the
  template gives a place for them.
- Row 3: model the invariant on `map-reference-target` in `foundations/invariants.md`; the test that
  cites it is `test_the_way_foundation_passes` in `elements/common/test_foundation_check.py`
  (task *Context*). Add the line `invariant: <identifier>` there. Mind the sentence of WAY-61 you
  change: the new invariant's method reads `test` because that citation stands in the same change.
- The new check needs tests of its own in `elements/common/test_foundation_check.py` — at least a
  foundation with a `test` invariant and no citing line (reported), the same with a citing line in
  a tracked non-Markdown file (passes), the Markdown-only citation (still reported), and the switch
  (check skipped). Write the failing run first and record its command and exit code and the passing
  run in your report.
- The check must work in a repository where git tracks files: take the "tracked by git" definition
  the script already uses for the existing check of `invariant:` lines (`:473-483` at the base
  commit) — reuse, do not add a second way of listing files.

## What you read (selected by the orchestrator)

The parts touched: `decisions` (foundations/decisions.md), `invariants` (foundations/invariants.md,
elements/invariants/**), `elements-common` (elements/common/**), possibly `part-map`.

- Decisions, each whole from its heading to the next heading: WAY-61 (the task's main subject),
  WAY-16, WAY-65, WAY-63, WAY-160 (the task's *Decisions in play*), and WAY-08, WAY-54, WAY-71,
  WAY-35, WAY-33, WAY-37, WAY-134, WAY-30. Beyond these, search the decision log yourself for
  *Scope* lines naming `invariants`, `elements-common`, `decisions` where your wording needs them.
- Invariants, each whole: `map-reference-target` (the model for row 3), `script-language`,
  `script-imports`, `script-subprocesses`, `foundation-file-kinds`, `element-directory-contents`,
  `skill-rule-source`, `return-step-record`, `derived-file-content`, `cross-part-imports`,
  `tracked-file-private-paths`.
- Part map entries of `decisions`, `invariants`, `elements-common`, and the sections
  `foundation-check-command`, `test-runner-command` of the interface list.
- Glossary: read `foundations/glossary.md` for the terms you use (invariant, method, test, review).
- Files: `elements/invariants/template.md`, `elements/invariants/skill/SKILL.md`,
  `elements/decisions/template.md`, `elements/common/rules.md`, `elements/common/way_of_working.md`,
  `elements/common/foundation_check.py`, `elements/common/test_foundation_check.py`,
  `installation/README.md:71-74`.
- Guidelines: the-way has no `guidelines/` directory (question 3 of the task settles that the task
  does not wait for it). Follow the style of the neighbouring script and tests.

The task's line numbers refer to `foundations` @ a3206c1; the base is newer, so find places by their
text (the task quotes them).

## Checks already failing on the base

Run in a separate checkout of the base; the result is in the orchestrator's record. You are told if
any check fails on the base; at this handoff none is known to fail. The full gate is the
orchestrator's.

## Report

Write your full report to `.runs/task-cycles/invariant-method-on-finished-change/reports/author-report.md`
as `task-cycle/change/SKILL.md` gives it (own-work check, **Searches not found or unclear**, concerns,
reaches beyond this handoff, each check with its command and exit code, the sentences of meaning in
English and in Polish for each entry and its mark `row <n>` or `the cycle's`). Return its status,
your commits, a one-line check result and the report path.
