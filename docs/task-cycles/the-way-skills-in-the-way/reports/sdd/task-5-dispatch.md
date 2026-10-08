You are implementing Task 5: `AGENTS.md` (two new sections, `## Skills` and `## Backlog`) and `README.md` (two places).
Prose only; no behaviour changes.

## Task Description

Read your task brief first — it is your requirements, with the exact values to use verbatim:
`C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\task-5-brief.md`.
Global constraints that bind it: `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\global-constraints.md`.

## Context

One task cycle of the-way (`implement-task`) on the-way itself. Done so far: the foundation step (WAY-127, invariant
`skill-entry-points/1`, part map, facts) and its correction for amendment R12 (972e9ad); the generator and the 22 generated
entry points (c61cebc). Task 4 rewrote each skill's paragraph on where the-way lies (dd25a36). This task adds the root instructions. The brief already
carries amendment R12; use its text verbatim. The `## Backlog` path is deliberate: the branch proposes an exception in WAY-27 and `outbound-link-reach/1` that admits exactly this place of tasks (Mariusz decides at the request). `## Skills` names the generator command, not a check command, and points to the gate tests; offer no other check command (WAY-16). The gate's flow test is read-only; do not open it.
Mariusz delegated intermediate choices to the orchestrator (the controller); questions go to the controller.

## Before You Begin

If you have questions about the requirements or anything unclear, ask them now.

## Your Job

1. Make exactly the edits the brief specifies, replacing each paragraph whole with the Edit tool (old text = the
   paragraph as it stands in the file). Prose edits: no test-first cycle applies; the brief's step 4 checks are the
   verification.
2. Run the brief's step 4 checks exactly; commit as its step 5 says (explicit paths); self-review your diff; report.

Work from: `C:\Storage\repos\the-way-skills-self` (branch `task/the-way-skills-in-the-way`). Write only the files the
brief names. Keep LF line endings and lines within 100 columns as the files have them.

## You Do Not Dispatch Subagents

Do all of this task's work yourself. Never spawn a subagent, and never a reviewer.

## When You're in Over Your Head

Report BLOCKED or NEEDS_CONTEXT with specifics — for example a paragraph that does not stand at the lines the brief names
or reads differently from the brief's "begins …" text.

## Before Reporting Back: Self-Review

Every listed file has its edit; nothing else changed; the text matches the brief word for word; checks pristine.

## Report Format

Write your full report to `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\task-5-report.md` — if the harness
refuses the write, put the full report in your final message instead. It holds: what you changed (file by file), the
checks run with their output, files changed, self-review findings, concerns.

Then report back with ONLY (under 15 lines unless the report file was refused): Status DONE | DONE_WITH_CONCERNS |
BLOCKED | NEEDS_CONTEXT; commits (short SHA + subject); one-line check summary; concerns; the report file path.
