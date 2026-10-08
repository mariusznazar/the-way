You are implementing Task 6: one sentence of the installer's product skill wrapper and its test (`installation`, a trust
boundary).

## Task Description

Read your task brief first — it is your requirements, with the exact values to use verbatim:
`C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\task-6-brief.md`.
Global constraints that bind it: `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\global-constraints.md`.

## Context

One task cycle of the-way (`implement-task`) on the-way itself. Task 4 (dd25a36) replaced the "Installed globally …"
paragraph of every skill with one that names two cases, the-way itself and a product. A product's wrapper, which
`installation/install.py` `skill_wrapper` generates, still says "Its paragraph about resolving a global skill link applies
only to a global install" — a pointer to a paragraph that no longer exists. This task changes that one literal and adds
its test. `installation/install.py` is the installation part's trust boundary: change nothing but the literal (no new
input, path, argument or subprocess). The installer's tests install this checkout's committed `HEAD`, so commit-dependent
assertions see committed files only. Mariusz delegated intermediate choices to the orchestrator (the controller);
questions go to the controller.

## Your Job

1. Test-first (Superpowers 6.4.1 `test-driven-development`:
   `C:\Users\Mariusz\.claude\plugins\cache\claude-plugins-official\superpowers\6.4.1\skills\test-driven-development\SKILL.md`):
   add the brief's test, see it fail, change the literal, see it pass.
2. Run `python -B gate/run_tests.py installation` and `python -B gate/run_tests.py gate --record .runs/gate-tests.jsonl`;
   commit by explicit paths with the brief's message; self-review; report.

Work from: `C:\Storage\repos\the-way-skills-self` (branch `task/the-way-skills-in-the-way`). Write only the two files the
brief names.

## You Do Not Dispatch Subagents

## When You're in Over Your Head

Report BLOCKED or NEEDS_CONTEXT with specifics.

## Report Format

Write your full report to `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\task-6-report.md` — if the harness
refuses the write, put it in your final message. It holds: what you changed; TDD evidence (RED command and output, why
expected; GREEN command and output); files changed; self-review; concerns.

Then report back with ONLY (under 15 lines unless the report file was refused): Status; commits (short SHA + subject);
one-line test summary; concerns; the report file path.
