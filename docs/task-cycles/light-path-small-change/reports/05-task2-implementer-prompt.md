You are implementing Task 2: `task-cycle/skill/SKILL.md` — the light cycle in the skill (spec §4), in one
the-way task cycle (Superpowers 6.4.1 `subagent-driven-development`, implementer role; template
`skills/subagent-driven-development/implementer-prompt.md` of that version, adapted below).

## Task Description
Read your task brief first: docs/task-cycles/light-path-small-change/reports/sdd/ (originally .superpowers/sdd/plan/) task-2-brief.md
It is your requirements, with the exact values to use verbatim.

## Context
- Worktree: C:/Storage/repos/the-way-light-path, branch `task/light-path-small-change`. Task 1 (the
  foundation step) is committed as b977e5f: WAY-13/1 and WAY-125/1 in `foundations/decisions.md` now
  allow the light cycle; your task cites them by number only.
- Global constraints (verbatim from the plan): edit only `task-cycle/skill/SKILL.md`; text is English
  and this file writes "behavior"; every new wording is copied from the brief — if you want a different
  word, stop and return the proposal; the file is LF (edit with the Edit tool); new and rewrapped lines
  are at most 100 characters except line 3 (front-matter `description`), which stays ONE line;
  rewrap only lines that hold a changed word; numbered-step continuation lines keep 3 spaces under
  steps 1–9 and 4 spaces under steps 10–14; commit with `git add task-cycle/skill/SKILL.md` only and
  `git commit -F <file>` (message file written with the Write tool in
  C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/f1c4ac63-3b4e-4e88-81d3-69c0173d41d5/scratchpad/);
  English message `type(scope): Sentence`; no push.
- Ruling C9 (orchestrator) removed one agent-written *Rejected* item from WAY-125; it does not touch
  your file.
- This is text only: TDD does not apply (ledger ruling). Your checks are those in the brief.
- Delegation: Mariusz delegated intermediate choices to the orchestrator. Questions go to the
  orchestrator: ask before starting, or stop with NEEDS_CONTEXT. Never seek human approval. Your
  boundary is the committed task with its checks run and your report written; do not invoke another
  Superpowers skill.

## You Do Not Dispatch Subagents
Do all of this task's work yourself; never spawn a subagent or a reviewer.

## Self-review, after-review findings and report
As in the template: self-review your diff; if resumed with findings, fix, re-run the covering checks and
append a fix report. Write your full report to
docs/task-cycles/light-path-small-change/reports/sdd/ (originally .superpowers/sdd/plan/) task-2-report.md
(what you implemented, checks and results, files changed, self-review findings, concerns). Then reply
with ONLY (under 15 lines): Status DONE | DONE_WITH_CONCERNS | BLOCKED | NEEDS_CONTEXT; commits (short
SHA + subject); one-line check summary; concerns; the report path.
