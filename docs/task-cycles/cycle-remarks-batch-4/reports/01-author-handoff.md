# Handoff — the one author, cycle `cycle-remarks-batch-4`

You are the one author of this task's change. The person who requested the cycle delegated its
intermediate choices to the orchestrator; nothing the orchestrator says below is that person's
approval. Answer nothing to a human: questions go back to the orchestrator as your report's status
`questions`.

## Where

- Worktree (work only here, from its root): `.runs/worktrees/cycle-remarks-batch-4`
  on branch `task/cycle-remarks-batch-4`; base commit `e3825a82386a61930a86f8517fc0c5f422fc2833` (`foundations`).
- This is the-way itself, with no `main` branch: the route of `agent-instructions/README.md` applies.
  Do not touch anything under `.runs/` except your report, do not push, do not open a request.
- Report: write it to `docs/task-cycles/cycle-remarks-batch-4/reports/02-author-report.md`.

## Method and variant

- Method: `task-cycle/change/SKILL.md` of this worktree. Read it whole, and a file it names only
  when the step or variant that names it comes.
- Your variant: **the whole change as the one author**.
- The foundation step (the entries the task carries): `task-cycle/skill/foundation_step.md`. Read it
  whole. The two decisions the task edits (WAY-160, WAY-71) are edited in place through the skill
  `record-decision`, `elements/decisions/skill/SKILL.md` of this worktree; read it whole and the
  files it names when its steps come, together with `elements/decisions/template.md`,
  `elements/common/rules.md` and `elements/common/way_of_working.md` that it names.
- You do the foundation step with your code and return before review. The return step is a separate
  stage, later; you do not take it.
- The orchestrator runs the product's gate (`python -B gate/run_tests.py` without argument). You do
  not. Run focused checks only: `python -B gate/run_tests.py task-cycle`,
  `python -B gate/run_tests.py elements/common`, `python -B elements/common/foundation_check.py .`
  (check its usage in its docstring) and whatever else your change makes affected. Another full gate
  is running in a separate checkout; do not start a full run.

## What the change is

The frozen task, whole: `docs/task-cycles/cycle-remarks-batch-4/task.md`.
Its *To do* items 1–7 give the wording to write; copy a quoted sentence exactly. Its *Questions to
settle* are settled (with sources); *Settlements to record* is `none`; *Out of scope* binds.

Answers of the orchestrator's start (step 4):

- Trust boundary: no. Irreversible operation: no.
- No open design choice, so no spec; one author without a plan.
- Item 7 (the request template) leaves open in which point of the description the cycle shows a
  descriptive `TODO` in *Rests on*: choose it from `task-cycle/skill/request_template.md` itself
  (where the unfixed findings and *For you to decide* items stand) and say which and why in your
  report as a choice of how to make what the task settles.
- Item 5/6 fit together: `foundation_check.py` must accept `TODO — <fact>` (also with a comma) and
  report a bare `TODO` in *Rests on*; `rules.md` and WAY-71 carry the sentence of item 6. Check the
  docstring of `foundation_check.py` and `elements/invariants/template.md` for statements that must
  follow. A bare `TODO` in the foundation of the-way itself, if any, is a finding for your report.

## Foundation entries to read

Whole, by identifier (selected by "Reading the foundation" in `elements/common/way_of_working.md`):

- decisions in play: WAY-160, WAY-71, WAY-27, WAY-17, WAY-163, WAY-294;
- also: WAY-05, WAY-07, WAY-11, WAY-29, WAY-33, WAY-35, WAY-37, WAY-148, WAY-159, WAY-260, WAY-295,
  WAY-296, WAY-286, WAY-287, WAY-289, WAY-290, WAY-298, WAY-300;
- invariants whose *Part* names `every`, `decisions`, `task-cycle` or `elements-common` (20 entries,
  found by that search of `foundations/invariants.md`), among them `skill-rule-source`,
  `element-directory-contents`, `record-copy-image-check`, `test-method-citation`;
- the part map entries `decisions`, `task-cycle`, `elements-common`;
- the glossary terms the work uses (`foundations/glossary.md`).

Product guidelines: the-way has no `guidelines/` directory (the question of its own guidelines is a
separate task, WAY-215 does not hold this one). Name any reach beyond this selection in your report.

## Report

Write it as `task-cycle/change/SKILL.md` gives, with the own-work check, each check with its command
and exit code, **Unread material** (what this handoff names that stayed unread or was read in part,
or `none`), **Searches not found or unclear** (or `none`), your choices (including the one named
above), and the weakest-point check of your own. Commit on the task branch with `git add <paths>`
(never `-A`), English messages. Return your status, commits, a one-line check result and the report path.
