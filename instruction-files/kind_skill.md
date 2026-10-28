# Skills

A skill leads an activity along its route: its `SKILL.md` carries the procedure, and the files its
steps point to carry what a step needs — long rules of an area, checklists, patterns. This holds
for every skill, the skills of a process the repository works by included.

## Where a fragment of a skill stands

For each fragment of a skill, ask whether every use of the skill needs it, or only one step or one
variant of the skill (WAY-256):

- **every use needs it** — it stays in `SKILL.md`, which keeps the picture of the whole, the rules
  of working that hold across the steps, and the pointers;
- **only one step or one variant needs it** — it stands in a file beside the skill, which that
  step tells the agent to read.

What sets the place is whether a use of the skill needs the fragment at that step, never the count
of the skill's words or lines. Where the repository's decisions place some rules of its skills
elsewhere — as the-way places every rule of an element's entries in the element's template and the
way of working its skills share in one common part (WAY-35) — those rules stand there, and the
skill reads them from there. The skill itself remains a sequence of steps.

## Its layout

| Layer | Shared carrier | Why it reaches every tool | Addition of a single tool |
|---|---|---|---|
| procedures of activities | a skill in `.claude/skills/`; for Codex, a pointer to its `SKILL.md` by path from `AGENTS.md`, or a copy in `.agents/skills/` | Claude Code and Cursor discover this directory themselves; Codex does not read it, so it gets there through the pointer, or reads the copy in `.agents/skills/` (fact `codex-repository-skills`) | — |
