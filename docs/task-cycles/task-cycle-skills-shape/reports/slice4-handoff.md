# Handoff — Slice 4, task `task-cycle-skills-shape`

You are the executor of one slice of a planned change in a the-way task cycle. The person who
requested this cycle has delegated intermediate choices to the orchestrator; send questions to the
orchestrator in your report, never to the human.

## Where you work

- Worktree, your working directory: `C:/Storage/repos/the-way-wt/task-cycle-skills-shape`, branch
  `task/task-cycle-skills-shape`.
- Slice 4's base: `8e5115ab0bb643784b37340d330627ea5e101738`. Class of model: `cheaper`.
- **Method:** `make-change`, read whole from the base copy of the-way,
  `.runs/the-way-base/task-cycle/change/SKILL.md`; every file of the process it names (the-way's
  skills, templates, `elements/common/way_of_working.md`, scripts) is read from
  `.runs/the-way-base/` as well. The task requires every agent of this cycle to read the methods of
  its stage from that copy at the base commit (its To do 7), because the task rebuilds them. The
  foundation (`foundations/`), the files you change and the tests are the worktree's.
- Your report: `.runs/task-cycles/task-cycle-skills-shape/reports/slice4-report.md`.

## Answers of the orchestrator's start

- Trust boundary: no. Irreversible operation: no. No spec was written; the route is planned
  slices. Guidelines: none — the-way has no `guidelines/` (the task settles it).
- The foundation entries of the plan (rows 1–3: changes of WAY-125, WAY-127 and WAY-256) are
  written in commit `40f0fd3`; read them in the worktree at the ranges below.

## Note from the orchestrator

Slice 2 (`61cc5ab`) changed the generator's sentence; write your paths with a one-off in-process
call of the generator's `produce(discover(ROOT))` (commit no script). The test
`test_the_tracked_entry_points_are_what_the_generator_produces` keeps failing on the paths of the
later batches until Slice 6 — the plan's expected state, not a failing check of your slice.

## Your section of the plan

Copied word for word from `.runs/task-cycles/task-cycle-skills-shape/plan.md`:

> ### Slice 4 — Entry points, second batch
>
> - **Goal:** the entry points of `maintain-testing-guidelines`, `make-change`, `plan-project`,
>   `plan-task` and `record-decision`, in both tools, are what the generator produces with Slice 2's
>   sentence, written from `produce(discover(ROOT))` of `agent-instructions/skill_entry_points.py`,
>   run in process for these ten paths only — never by hand and never by `--write`.
> - **Change:** `.claude/skills/the-way-maintain-testing-guidelines/SKILL.md` ·
>   `.agents/skills/the-way-maintain-testing-guidelines/SKILL.md` ·
>   `.claude/skills/the-way-make-change/SKILL.md` · `.agents/skills/the-way-make-change/SKILL.md` ·
>   `.claude/skills/the-way-plan-project/SKILL.md` · `.agents/skills/the-way-plan-project/SKILL.md` ·
>   `.claude/skills/the-way-plan-task/SKILL.md` · `.agents/skills/the-way-plan-task/SKILL.md` ·
>   `.claude/skills/the-way-record-decision/SKILL.md` ·
>   `.agents/skills/the-way-record-decision/SKILL.md`
> - **Read:** `agent-instructions/skill_entry_points.py` · Foundation entries row 2 (WAY-127 as the
>   foundation step changes it) · `foundations/invariants.md:241-250` skill-entry-points ·
>   `foundations/invariants.md:56-65` derived-file-content
> - **Model:** cheaper
> - **Risk:** none
> - **Checks:** each pair byte-identical and equal to what `produce` gives for its path;
>   `python -B agent-instructions/skill_entry_points.py` prints `would change` for exactly the 16
>   paths of Slices 5–6; `git diff --stat <base>..HEAD` names these ten paths alone.
> - **Depends on:** Slice 3

## Current ranges of the foundation entries your *Read* names

Where they differ from the plan's ranges, these hold (the foundation step moved them):

- `foundations/decisions.md:2918-2983` WAY-127
- `foundations/invariants.md:241-250` skill-entry-points
- `foundations/invariants.md:56-65` derived-file-content

## Passages your *Read* names, copied word for word

## Your boundary

Make your slice only, commit it on the task branch, keep the worktree clean, and return. Run your
slice's *Checks* and report each with its command and exit code. Do not run `gate/run_tests.py` as a
whole; that run is the orchestrator's (a directory argument is a focused check and allowed). Return
your status (`done`, `done with concerns`, `questions`, `returned` or `blocked`), your commits, a
one-line check result naming what failed or did not run, and your report's path.
