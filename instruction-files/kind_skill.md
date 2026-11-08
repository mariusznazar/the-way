# Skills

What is particular to skills — every skill, the skills of a process the repository works by
included.

## Where a fragment of a skill stands

For each fragment of a skill, ask whether every step of the skill needs it, or some steps but not
all, or only one variant of the skill or only one step (WAY-256). Whether a use of the skill comes
to a step is read from records of sessions a person can open — those of Claude Code and Codex, the
uses since the step stood in the skill — which the search before the table covers:

- **every step needs it** — it stays in `SKILL.md`, which keeps the picture of the whole, the rules
  of working that hold across the steps, and the pointers;
- **only one variant needs it, or only one step that the records show some uses pass by** — it
  stands in a file beside the skill, which that step tells the agent to read; the row that moves a
  step names the records in which a use passed it by;
- **only one step needs it, and the records show every use coming to that step, or show none** — it
  stays in `SKILL.md` in its step: a step every use comes to is in play in every use wherever it
  stands, so a file of its own spares no use anything and adds a pointer and an opening sentence to
  each; a skill with no record keeps every step in `SKILL.md`, a variant excepted;
- **some steps need it, not all** — a rule of working the agent has to keep during those steps stays
  in `SKILL.md`; text it reads or consults, such as a procedure, a list or a template, stands in a
  file beside the skill, each of those steps names that file, and a step after the first has it read
  unless an earlier step did (WAY-256).

The exception is a fragment of one step or one variant that is one instruction and would otherwise
stand in a file beside the skill: it stays in `SKILL.md`, where its pointer would stand, since the
pointer is an instruction too (WAY-256). Moving it out would leave the instructions in play as
many and add a file to keep. The exception reaches no further than one instruction against the one
pointer that would replace it: a fragment of several instructions does not stay because each of
them is short.

Where the repository's decisions place some rules of its skills elsewhere — as the-way places
every rule of an element's entries in the element's template and the way of working its skills
share in one common part (WAY-35) — those rules stand there, and the skill reads them from there.
The skill itself remains a sequence of steps.

## Its layout

| Layer | Shared carrier | Why it reaches every tool | Addition of a single tool |
|---|---|---|---|
| procedures of activities | a skill in `.claude/skills/`; for Codex, a pointer to its `SKILL.md` by path from `AGENTS.md`, or a copy in `.agents/skills/` | Claude Code and Cursor discover this directory themselves; Codex does not read it, so it gets there through the pointer, or reads the copy in `.agents/skills/` (fact `codex-repository-skills`) | — |
