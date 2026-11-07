# Handoff — the one author, `find-foundation-entries` in the shape of WAY-256

## Delegation

Mariusz asked the orchestrator to take this task through its cycle. The orchestrator delegates the
intermediate choices to you where the task and the foundation leave them open; your answer is
never Mariusz's approval. You ask no human. Questions go back to the orchestrator in your report
(status `questions`).

## Where you work

- Worktree and process root: `C:\Storage\repos\the-way\.runs\worktrees\find-foundation-entries-shape`
  (branch `task/find-foundation-entries-shape`, base `f447bb62ce4f8d4a4badb1b283a10f62651d65d7`).
  Work from its root; read every file from it, never a copy in another checkout.
- Only you write in this worktree while you work. Commit on this branch; add files by path, never
  `git add -A`. Commit messages in English. Do not push, do not open a request.
- Record directory (ignored by git, not part of any commit): `.runs/task-cycles/find-foundation-entries-shape/`.
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

The frozen task: `.runs/task-cycles/find-foundation-entries-shape/task.md` (status
`ready for cycle`, 2026-11-06). Read it whole; it is the whole of your requirement. Its
*Settlements to record* holds no row (`Candidates: 11 shown, 0 accepted`) and the task carries no
projected entry, so the foundation step has nothing to write: say so in your report. No spec and no
plan exist: the task leaves no open design choice and the change fits one author.

Answers of the cycle's step 4: the change touches no trust boundary (`elements-common`, trust
boundary none) and holds no operation that cannot be undone.

The file you rebuild: `elements/common/skill/SKILL.md` (1584 words on the base). Files you may
add or change: only inside `elements/common/skill/` (task To do 6). `elements/common/projected_mode.md`,
`elements/common/way_of_working.md`, the callers of the skill, the skill's `description` and any
Python stay as they are; so do the `the-way-*` entry points. If a change would need any of them,
return `questions`.

## What the request will need from you (task To do 3–5 and the acceptance criteria)

Write these into `.runs/task-cycles/find-foundation-entries-shape/reports/` (the orchestrator
builds the request from them):

1. `assessment.md` — the assessment table of the skill: each fragment quoted literally with its
   line range on the base `dfd50e5`/`f447bb6` (the file is identical), when it is needed, whether
   an agent recognises that moment, the verdict, and the place after the rebuild; every nonblank
   line of the base in exactly one row. After the table, the proposals: the verdicts "remove" and
   "reword" that change the content of a rule are NOT applied in the files; they are listed as
   proposals, each with what happens if left and what the change costs. Among them, reading in the
   task variant only the three sections of `elements/common/way_of_working.md` named in To do 5.
2. `word-counts.md` and a script `verify_counts.py` (in the same `reports/` directory) — words
   before (state on the base) and after, on the two routes of question 4, by the three sums it
   gives, counted as `wc -w`; the counts are made after the last change to any counted file; the
   script compares with the files every number the request will state, in prose as well as in
   totals.
3. Per the acceptance criteria: for each changed conditional or pointer, a comparison with the
   base that shows no route added and none lost, and for each new sentence what it switches off.
   Put this in `author.md` (your report), not in a separate file.

## Foundation entries to read (by identifier; each whole, from the worktree)

- Decisions of the task's *Decisions in play*: WAY-256, WAY-257, WAY-265, WAY-35, WAY-115,
  WAY-134, WAY-117, WAY-127, WAY-259.
- Other decisions whose *Scope* names `elements-common` that bear on this work: WAY-09, WAY-113,
  WAY-114, WAY-150.
- Invariants (in `foundations/invariants.md`): `element-directory-contents`, `skill-rule-source`,
  `outbound-link-reach`, `derived-file-content`, `foundation-file-kinds`.
- Part map: the entries `elements-common` and `agent-instructions` of `foundations/part_map.md`.
- Glossary: `foundations/glossary.md`, whole (it is short).
- Reading the foundation for this work is by `elements/common/way_of_working.md`, section
  "Reading the foundation"; you read what is named here and no search of the whole foundation is
  asked of you before the return step.

Product guidelines: none — the-way has no `guidelines/` directory.

Callers of the skill (read-only, they decide which words an agent uses to recognise its variant):
`project-level/skill/SKILL.md:129–131`, `project-level/task/skill/find_settlements.md:4–7`,
`project-level/task/skill/orchestrated_mode.md:17`, `product-guidelines/coding/hand_back.md:24`,
`product-guidelines/styleguide/hand_back.md:11`, `product-guidelines/testing/hand_back.md:16`.

## Checks the move of a pin carried

None — no pin moves.

## Checks already failing on the base

The orchestrator runs the base gate separately and will give you the result in the fix's or the
return step's handoff if it matters. You run only focused checks (`python -B gate/run_tests.py
elements/common`, `python -B elements/common/foundation_check.py` as its usage gives,
`python -B instruction-files/check_instructions.py` on the files you add, and
`python -B agent-instructions/skill_entry_points.py` in its check mode if it has one), each with its
command and exit code in the report. Do not run the whole gate; its run is the orchestrator's.

## Report

Write the full report to
`.runs/task-cycles/find-foundation-entries-shape/reports/author.md` as `task-cycle/change/SKILL.md`
gives it, with **Searches not found or unclear** (each item or `none`), your own-work check, the
weakest point of your work and the check you made on it. Return only: status, commits, a one-line
check result naming what failed or did not run, and the report path.
