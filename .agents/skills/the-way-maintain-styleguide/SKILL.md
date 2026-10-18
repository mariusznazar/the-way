---
name: the-way-maintain-styleguide
description: Use when a product's user interface — its screens, an admin panel added to a backend included — needs a styleguide created before its first screen, audited where screens exist, or refreshed or extended, leading those matters of a styleguide task's refinement with the human. Use this checkout's own the-way.
---

# the-way-maintain-styleguide

This entry point serves a session that works on the-way itself. Stop following it, and use the product's own project skill `the-way-maintain-styleguide`, if either check shows a product:

- `git -C <the directory that holds this file> rev-parse --show-superproject-working-tree` prints a path: this file lies in a product's `.the-way` submodule;
- `git ls-files --stage -- ':/.the-way'`, run in the session's working directory, prints a line: the session works in a product that pins the-way.

The process root is the checkout or worktree the session works in: the directory `git rev-parse --show-toplevel` prints when run in the session's working directory — the directory the session was started in, or the one it was last moved to (Claude Code's `/cd`) — not in the shell's current directory, which moves with `cd`. Read `product-guidelines/styleguide/SKILL.md` there in full and follow it, and read the files it names under the same root, never a copy in another checkout or worktree. If `product-guidelines/styleguide/SKILL.md` is absent there, stop and say so. If the skill tells you to resolve a link to find the-way, skip that: the root is the one above. Do not substitute a global skill.

Where this skill or a file it reads names another the-way skill — `critique`, `find-foundation-entries`, `record-decision`, `record-environment-fact`, `record-glossary-term`, `record-invariant`, `update-part-map`, `maintain-instruction-files`, `maintain-styleguide`, `lead-project`, `plan-project`, `define-project`, `refine-task`, `settle-technology`, `plan-task` or `implement-task` — use this repository's project skill of the same name with the `the-way-` prefix, never an unprefixed one.
