# Handoff — the one author, `define-project` in the shape of WAY-256

## Delegation

Mariusz asked the orchestrator to take this task through its cycle. The orchestrator delegates the
intermediate choices to you where the task and the foundation leave them open; your answer is
never Mariusz's approval. You ask no human. Questions go back to the orchestrator in your report
(status `questions`).

## Where you work

- Worktree and process root: `.`
  (branch `task/define-project-skill-shape`, base `2754675`, the merge of PR #84 on `foundations`).
  Work from its root; read every file from it, never a copy in another checkout.
- Only you write in this worktree while you work. Do not touch `.runs/base-check` (a separate
  checkout where the orchestrator runs the base gate). Commit on this branch; add files by path,
  never `git add -A`. Commit messages in English. Do not push, do not open a request.
- Record directory (ignored by git, not part of any commit): `.runs/task-cycles/define-project-skill-shape/`.
  Write your artifacts that are not repository files under its `reports/`.

## Stage and variant

Your method: `task-cycle/change/SKILL.md`, read whole. Your variant, in the words of its row:
"the whole change as the one author". Read a file the method names only when the step or variant
that names it comes.

You also carry out the task's To do 1, which sends you to the skill of `maintain-instruction-files`:
its method is `instruction-files/SKILL.md` (read whole), in judging mode, with the file of kind
"skill" (`instruction-files/kind_skill.md`, and the other files that method names when their step
comes). Follow it for the assessment and for the rebuild.

## The task

The frozen task: `.runs/task-cycles/define-project-skill-shape/task.md` (status
`ready for cycle`, updated 2026-11-06; written in Polish). Read it whole; it is the whole of your
requirement. Its *Settlements to record* holds no row (`Candidates: 6 shown, 0 accepted`) and the
task carries no projected entry, so the foundation step has nothing to write: say so in your
report. No spec and no plan exist: the task leaves no open design choice and the change fits one
author.

Answers of the cycle's step 4: the change touches no trust boundary (the part `project-level`
names only three Python scripts as its boundary, none of which changes) and holds no operation
that cannot be undone.

The file you rebuild: `project-level/skill/SKILL.md`. Files you may add or change: only inside
`project-level/skill/` (task To do 3, question 1). `project-level/definition_template.md`,
`project-level/lead/**`, `elements/common/way_of_working.md`, every other file of the-way, the
skill's `description` and any Python stay as they are; so do the `the-way-*` entry points. If a
change would need any of them, return `questions`.

One figure to note: `wc -w project-level/skill/SKILL.md` on the base gives 1929, while the task
states 1937 (Need, first point). Count by `wc -w` as question 4 gives, state the counted figure,
and say in `word-counts.md` how it differs from the task's figure if you find what the 1937
counts.

Form already used in this part: `project-level/plan/skill/` (the `plan-project` skill, rebuilt by
an earlier task of the same series) holds a `SKILL.md` with files beside it per step and a
`delegated_mode.md` for its delegated variant. Read it for its form only, as an example of what
the series produced; it binds nothing, and the task and WAY-256/WAY-265 decide.

## What the request will need from you (task To do 4–6 and the acceptance criteria)

Write these into `.runs/task-cycles/define-project-skill-shape/reports/` (the orchestrator builds
the request from them):

1. `assessment.md` — the assessment table of the skill (To do 4): each fragment quoted literally
   with its line range on the base (`dfd50e5`; the file is identical at `2754675`), when it is
   needed, whether an agent recognises that moment, the verdict, and the place after the rebuild;
   every nonblank line of the base in exactly one row. After the table, the proposals (To do 6):
   the verdicts "remove" and "reword" that change the content of a rule are NOT applied in the
   files; they are listed as proposals, each with what happens if left and what the change costs.
   Among them the repetitions between the skill and `project-level/lead/skill/SKILL.md` (`:202–213`)
   and `project-level/definition_template.md` (question 1).
2. `word-counts.md` and a script `verify_counts.py` (in the same `reports/` directory) — words
   before (on the base) and after, on the five routes of question 4 (1, 2, 3a, 3b, 4, 5), each with
   its two sums (the skill's own text; the sum with the files read beside it as question 4 lists
   them), counted as `wc -w`; the counts are made after the last change to any counted file; the
   script compares with the files every number the request will state, in prose as well as in
   totals (last acceptance criterion), and is shown able to fail.
3. Per the acceptance criteria: for each changed conditional of a mode, variant or pointer, a
   comparison with the base that shows no route added and none lost, and for each new sentence
   what it switches off; the check that the delegated-mode file reaches step 7 (criterion 4); the
   fragments needed at several steps reaching each of them (criterion 5, with the cases it names).
   Put this in your report, not in a separate file.

## Foundation entries to read (by identifier; each whole, from the worktree)

- Decisions of the task's *Decisions in play*: WAY-256, WAY-257, WAY-265, WAY-106, WAY-112,
  WAY-118, WAY-156, WAY-120, WAY-113, WAY-111, WAY-127, WAY-259.
- Other decisions the skill cites, which its text carries and you must not change in meaning:
  WAY-30, WAY-114, WAY-121, WAY-142, WAY-150.
- Invariants (in `foundations/invariants.md`): `skill-rule-source`, `outbound-link-reach`,
  `project-definition-form`, `project-readiness-gate`, `skill-entry-points`, `derived-file-content`.
- Part map: the entry `project-level` of `foundations/part_map.md`.
- Glossary: `foundations/glossary.md`, whole.
- Reading the foundation for this work is by `elements/common/way_of_working.md`, section
  "Reading the foundation"; you read what is named here and no search of the whole foundation is
  asked of you before the return step.

Product guidelines: none — the-way has no `guidelines/` directory (task question 7).

Files that name the skill's steps by number (read-only; the numbers 0–7 and 7.1–7.5 must stay so
they still point right): `project-level/technology/start.md:8`, `project-level/lead/skill/SKILL.md:208`,
`project-level/plan/skill/existing_plan.md:9`. Files that name the skill otherwise:
`elements/common/projected_mode.md:4`, `:11`, `elements/common/skill/SKILL.md` (its line that names
`define-project`), `project-level/plan/skill/read.md:4`, `project-level/task/skill/read_sources.md:15`,
`project-level/technology/close.md:10–11`, `installation/install.py:31`, `installation/README.md:57`.
The delegated caller: `project-level/lead/skill/SKILL.md:202–219` and
`project-level/lead/conversation_template.md` — its words decide how a delegated agent recognises
its variant.

## Checks the move of a pin carried

None — no pin moves.

## Checks already failing on the base

The orchestrator runs the base gate separately and will give you the result in a later handoff if
it matters. You run only focused checks (`python -B gate/run_tests.py project-level`,
`python -B gate/run_tests.py installation`, `python -B gate/run_tests.py agent-instructions`,
`python -B elements/common/foundation_check.py` as its usage gives,
`python -B instruction-files/check_instructions.py` on the files you add, and
`python -B agent-instructions/skill_entry_points.py` in its check mode), each with its command and
exit code in the report. Do not run the whole gate; its run is the orchestrator's.

## Report

Write the full report to
`.runs/task-cycles/define-project-skill-shape/reports/author_report.md` as `task-cycle/change/SKILL.md`
gives it, with **Searches not found or unclear** (each item or `none`), your own-work check, the
weakest point of your work and the check you made on it. Return only: status, commits, a one-line
check result naming what failed or did not run, and the report path.
