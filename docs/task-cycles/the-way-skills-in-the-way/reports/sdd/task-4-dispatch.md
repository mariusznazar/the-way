You are implementing Task 4: where the-way lies, in each skill — nine paragraphs and one sentence of
`elements/common/way_of_working.md` (task points 2, 3). Prose only; no behaviour changes.

## Task Description

Read your task brief first — it is your requirements, with the exact values to use verbatim:
`C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\task-4-brief.md`.
Global constraints that bind it: `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\global-constraints.md`.

## Context

One task cycle of the-way (`implement-task`) on the-way itself. Done so far: the foundation step (WAY-127, invariant
`skill-entry-points/1`, part map, facts) and its correction for amendment R12 (972e9ad); the generator and the 22 generated
entry points (c61cebc). This task rewrites the paragraph each skill holds about where the-way lies. The brief already
carries amendment R12 ("the session works in", "the session's working directory"); use its text verbatim. You change no
skill's frontmatter, so the entry points stay current — the brief's check confirms it. Each element skill must keep naming
`elements/common/way_of_working.md` (invariant `skill-rule-source`). The gate's flow test is read-only; do not open it.
Mariusz delegated intermediate choices to the orchestrator (the controller); questions go to the controller.

## Before You Begin

If you have questions about the requirements or anything unclear, ask them now.

## Your Job

1. Make exactly the edits the brief specifies, replacing each paragraph whole with the Edit tool (old text = the
   paragraph as it stands in the file). Prose edits: no test-first cycle applies; the brief's step 6 checks are the
   verification.
2. Run the brief's step 6 checks exactly; commit as its step 7 says (explicit paths); self-review your diff; report.

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

Write your full report to `C:\Storage\repos\the-way-skills-self\.superpowers\sdd\plan\task-4-report.md` — if the harness
refuses the write, put the full report in your final message instead. It holds: what you changed (file by file), the
checks run with their output, files changed, self-review findings, concerns.

Then report back with ONLY (under 15 lines unless the report file was refused): Status DONE | DONE_WITH_CONCERNS |
BLOCKED | NEEDS_CONTEXT; commits (short SHA + subject); one-line check summary; concerns; the report file path.
