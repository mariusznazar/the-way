You are implementing Task 3: the generated entry points and their derived equality (steps 1–5 of the brief; step 6 belongs to the reviewer, not to you).

## Task Description

Read your task brief first — it is your requirements, with the exact values to use verbatim:
`C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\task-3-brief.md`.
Global constraints that bind it: `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\global-constraints.md`.

## Context

One task cycle of the-way (`implement-task`) on the-way itself. The foundation step is committed (47dcbe3): decision
WAY-127, invariant `skill-entry-points/1`, the part map's `agent-instructions` changes and the gate's flow test
`gate/test_skills_reach_the_way_sessions.py`. Task 2 committed the generator and its tests (a7f42aa). The flow test is
READ-ONLY for you (WAY-03) and you must not read it for guidance: the generator and the check come from different authors
(WAY-69). It, `elements/part-map`'s own-map test and the part-map guard are red until the entry points exist; this task
is expected to turn them green. If the gate still fails after you generate, do not change the check or bend the
generator to it: report the failing lines to the controller (status DONE_WITH_CONCERNS or BLOCKED). You generate the
entry points with the generator; never write or edit an entry point by hand. Mariusz delegated intermediate choices to
the orchestrator (the controller); questions go to the controller.

## Before You Begin

If you have questions about the requirements, the approach, dependencies or anything unclear, ask them now.

## Your Job

1. Implement exactly what the task specifies, test-first (Superpowers 6.4.1 `test-driven-development`:
   `C:\Users\Mariusz\.claude\plugins\cache\claude-plugins-official\superpowers\6.4.1\skills\test-driven-development\SKILL.md`).
2. Verify; commit by explicit paths with the brief's message; self-review your diff; report.

Work from: `C:\Storage\repos\the-way-skills-self` (branch `task/the-way-skills-in-the-way`). Run the checks of the brief's step 4 exactly; while
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

Write your full report to `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\task-3-report.md` — if the harness
refuses the write ("Subagents should return findings as text"), put the full report in your final message instead and the
controller saves it. The report holds: what you implemented; what you tested and results; TDD evidence (RED: command,
failing output, why expected; GREEN: command, passing output); files changed; self-review findings; issues or concerns.

Then report back with ONLY (under 15 lines unless the report file was refused): Status DONE | DONE_WITH_CONCERNS |
BLOCKED | NEEDS_CONTEXT; commits (short SHA + subject); one-line test summary; concerns; the report file path.
