---
name: the-way-plan-task
description: Use when a ready the-way task's change has to be divided into slices before it is made — after the cycle selects planning from the frozen task or a reviewed spec, or a one-author change or planned slice proves too large. Not for a project's plan of tasks, and never writes code. Use this checkout's own the-way.
---

# the-way-plan-task

This entry point serves a session that works on the-way itself. Stop following it, and use the product's own project skill `the-way-plan-task`, if either check shows a product:

- `git -C <the directory that holds this file> rev-parse --show-superproject-working-tree` prints a path: this file lies in a product's `.the-way` submodule;
- `git ls-files --stage -- ':/.the-way'`, run in the session's working directory, prints a line: the session works in a product that pins the-way.

The process root is the checkout or worktree the session works in: the directory `git rev-parse --show-toplevel` prints when run in the session's working directory — the directory the session was started in, or the one it was last moved to (Claude Code's `/cd`) — not in the shell's current directory, which moves with `cd`. Read `task-cycle/plan/SKILL.md` there in full and follow it, and read the files it names under the same root, never a copy in another checkout or worktree. If `task-cycle/plan/SKILL.md` is absent there, stop and say so. If the skill tells you to resolve a link to find the-way, skip that: the root is the one above. Do not substitute a global skill.

Where this skill or a file it reads names another the-way skill — `critique`, `find-foundation-entries`, `record-decision`, `record-environment-fact`, `record-glossary-term`, `record-invariant`, `update-part-map`, `maintain-instruction-files`, `maintain-styleguide`, `lead-project`, `plan-project`, `define-project`, `refine-task`, `settle-technology`, `plan-task` or `implement-task` — use this repository's project skill of the same name with the `the-way-` prefix, never an unprefixed one.
