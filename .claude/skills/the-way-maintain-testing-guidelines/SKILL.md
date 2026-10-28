---
name: the-way-maintain-testing-guidelines
description: Use when a product's tests need testing guidelines written before its first test, its existing tests audited for them, or its testing guidelines refreshed or extended — leading those matters of a testing-guidelines task's refinement with the human. Use this checkout's own the-way.
---

# the-way-maintain-testing-guidelines

This entry point serves a session that works on the-way itself. Stop following it, and use the product's own project skill `the-way-maintain-testing-guidelines`, if either check shows a product:

- `git -C <the directory that holds this file> rev-parse --show-superproject-working-tree` prints a path: this file lies in a product's `.the-way` submodule;
- `git ls-files --stage -- ':/.the-way'`, run in the session's working directory, prints a line: the session works in a product that pins the-way.

The process root is the checkout or worktree the session works in: the directory `git rev-parse --show-toplevel` prints when run in the session's working directory — the directory the session was started in, or the one it was last moved to (Claude Code's `/cd`) — not in the shell's current directory, which moves with `cd`. Read `product-guidelines/testing/SKILL.md` there in full and follow it, and read a file it names under the same root when the step or variant that names it comes, not all of them at the start, never a copy in another checkout or worktree. If `product-guidelines/testing/SKILL.md` is absent there, stop and say so. If the skill tells you to resolve a link to find the-way, skip that: the root is the one above. Do not substitute a global skill.

Where this skill or a file it reads names another the-way skill — `critique`, `find-foundation-entries`, `record-decision`, `record-environment-fact`, `record-glossary-term`, `record-invariant`, `update-part-map`, `maintain-instruction-files`, `maintain-coding-guidelines`, `maintain-styleguide`, `maintain-testing-guidelines`, `lead-project`, `plan-project`, `define-project`, `refine-task`, `settle-technology`, `make-change`, `plan-task`, `review-change`, `implement-task` or `write-spec` — use this repository's project skill of the same name with the `the-way-` prefix, never an unprefixed one.
