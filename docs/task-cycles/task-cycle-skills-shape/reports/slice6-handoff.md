# Handoff — Slice 6, task `task-cycle-skills-shape`

You are the executor of one slice of a planned change in a the-way task cycle. The person who
requested this cycle has delegated intermediate choices to the orchestrator; send questions to the
orchestrator in your report, never to the human.

## Where you work

- Worktree, your working directory: `C:/Storage/repos/the-way-wt/task-cycle-skills-shape`, branch
  `task/task-cycle-skills-shape`.
- Slice 6's base: `df95b4d71ff087417bef57224ad0eefc689ffcc2`. Class of model: `cheaper`.
- **Method:** `make-change`, read whole from the base copy of the-way,
  `.runs/the-way-base/task-cycle/change/SKILL.md`; every file of the process it names (the-way's
  skills, templates, `elements/common/way_of_working.md`, scripts) is read from
  `.runs/the-way-base/` as well. The task requires every agent of this cycle to read the methods of
  its stage from that copy at the base commit (its To do 7), because the task rebuilds them. The
  foundation (`foundations/`), the files you change and the tests are the worktree's.
- Your report: `.runs/task-cycles/task-cycle-skills-shape/reports/slice6-report.md`.

## Answers of the orchestrator's start

- Trust boundary: no. Irreversible operation: no. No spec was written; the route is planned
  slices. Guidelines: none — the-way has no `guidelines/` (the task settles it).
- The foundation entries of the plan (rows 1–3: changes of WAY-125, WAY-127 and WAY-256) are
  written in commit `40f0fd3`; read them in the worktree at the ranges below.

## Note from the orchestrator

Slices 2–5 (`61cc5ab`..`df95b4d`) wrote 34 entry points; the generator's dry run now lists only your eight paths. Your slice runs `--write` as the plan gives.

## Your section of the plan

Copied word for word from `.runs/task-cycles/task-cycle-skills-shape/plan.md`:

> ### Slice 6 — Entry points, last batch, by the generator's command
>
> - **Goal:** the entry points of `review-change`, `settle-technology`, `update-part-map` and
>   `write-spec`, in both tools, are written by `python -B agent-instructions/skill_entry_points.py
>   --write` (task, *To do* 3), which by now changes these eight paths and no other; every entry point
>   of the-way is then what the generator produces.
> - **Change:** `.claude/skills/the-way-review-change/SKILL.md` ·
>   `.agents/skills/the-way-review-change/SKILL.md` ·
>   `.claude/skills/the-way-settle-technology/SKILL.md` ·
>   `.agents/skills/the-way-settle-technology/SKILL.md` ·
>   `.claude/skills/the-way-update-part-map/SKILL.md` ·
>   `.agents/skills/the-way-update-part-map/SKILL.md` · `.claude/skills/the-way-write-spec/SKILL.md` ·
>   `.agents/skills/the-way-write-spec/SKILL.md`
> - **Read:** `agent-instructions/skill_entry_points.py` · Foundation entries row 2 (WAY-127 as the
>   foundation step changes it) · `foundations/invariants.md:241-250` skill-entry-points ·
>   `foundations/invariants.md:56-65` derived-file-content
> - **Model:** cheaper
> - **Risk:** none
> - **Checks:** `python -B agent-instructions/skill_entry_points.py` prints `entry points are current`
>   and exits 0; `python -B gate/run_tests.py agent-instructions` exits 0;
>   `python -B gate/run_tests.py gate` exits 0; `git diff --stat <base>..HEAD` names these eight paths
>   alone.
> - **Depends on:** Slice 5

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
