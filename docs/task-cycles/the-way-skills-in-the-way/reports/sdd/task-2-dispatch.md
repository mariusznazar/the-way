You are implementing Task 2: the generator of the project skill entry points and its tests (`agent-instructions`).

## Task Description

Read your task brief first — it is your requirements, with the exact values to use verbatim:
`C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\task-2-brief.md`.
Global constraints that bind it: `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\global-constraints.md`.

## Context

One task cycle of the-way (`implement-task`) on the-way itself. The foundation step is committed (head 47dcbe3): decision
WAY-127, invariant `skill-entry-points/1`, the part map's `agent-instructions` changes and the gate's flow test
`gate/test_skills_reach_the_way_sessions.py`. That flow test is READ-ONLY for you (WAY-03) and you must not read it for
guidance: the generator and the check come from different authors (WAY-69). It stays red until Task 3 generates the entry
points — that is expected, not yours to fix. `elements/part-map`'s own-map test and the part-map guard are red for the
same reason. You generate no entry points in this task (Task 3 does). Mariusz delegated intermediate choices to the
orchestrator (the controller); questions go to the controller.

## Before You Begin

If you have questions about the requirements, the approach, dependencies or anything unclear, ask them now.

## Your Job

1. Implement exactly what the task specifies, test-first (Superpowers 6.4.1 `test-driven-development`:
   `C:\Users\Mariusz\.claude\plugins\cache\claude-plugins-official\superpowers\6.4.1\skills\test-driven-development\SKILL.md`).
2. Verify; commit by explicit paths with the brief's message; self-review your diff; report.

Work from: `C:\Storage\repos\the-way-skills-self` (branch `task/the-way-skills-in-the-way`). Run the focused tests while
iterating (`python -B gate/run_tests.py agent-instructions`), and once before committing also
`python -B gate/run_tests.py installation`. Write only the files the brief names.

## You Do Not Dispatch Subagents

Do all of this task's work yourself. Never spawn a subagent, and never a reviewer. Review is the controller's job.

## Code Organization

Follow the plan's file structure; one clear responsibility per file; follow the repository's patterns (standard library,
`git` as the only subprocess, `python -B`). If a file grows beyond the plan's intent, report DONE_WITH_CONCERNS.

## When You're in Over Your Head

Stop and report BLOCKED or NEEDS_CONTEXT with specifics: architectural choices with several valid approaches, code you
cannot understand, uncertainty about correctness.

## Before Reporting Back: Self-Review

Completeness, quality, discipline (YAGNI, only what was requested, existing patterns), testing (real behaviour, TDD
followed, output pristine). Fix what you find.

## Report Format

Write your full report to `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\task-2-report.md` — if the harness
refuses the write ("Subagents should return findings as text"), put the full report in your final message instead and the
controller saves it. The report holds: what you implemented; what you tested and results; TDD evidence (RED: command,
failing output, why expected; GREEN: command, passing output); files changed; self-review findings; issues or concerns.

Then report back with ONLY (under 15 lines unless the report file was refused): Status DONE | DONE_WITH_CONCERNS |
BLOCKED | NEEDS_CONTEXT; commits (short SHA + subject); one-line test summary; concerns; the report file path.
