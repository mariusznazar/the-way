---
name: the-way-lead-project
description: Use to lead a handed-over project plan through human-confirmed rounds of task refinement and evidence-backed state upkeep, or resume that work from its files, and to close the project once every task is done, delivered in another task or dropped. Not for defining or breaking down a project, refining one task directly or running task cycles. Requires child agents. Use this checkout's own the-way.
disable-model-invocation: true
---

# the-way-lead-project

This entry point serves a session that works on the-way itself. Stop following it, and use the product's own project skill `the-way-lead-project`, if either check shows a product:

- `git -C <the directory that holds this file> rev-parse --show-superproject-working-tree` prints a path: this file lies in a product's `.the-way` submodule;
- `git ls-files --stage -- ':/.the-way'`, run in the session's working directory, prints a line: the session works in a product that pins the-way.

The process root is the checkout or worktree the session works in: the directory `git rev-parse --show-toplevel` prints when run in the session's working directory — the directory the session was started in, or the one it was last moved to (Claude Code's `/cd`) — not in the shell's current directory, which moves with `cd`. Read `project-level/lead/skill/SKILL.md` there in full and follow it, and read a file it names under the same root when the step or variant that names it comes, not all of them at the start, never a copy in another checkout or worktree. If `project-level/lead/skill/SKILL.md` is absent there, stop and say so. If the skill tells you to resolve a link to find the-way, skip that: the root is the one above. Do not substitute a global skill.

Where this skill or a file it reads names another the-way skill, do not call it, since Claude Code does not offer the entry points of the-way's skills to the model: read that skill's `SKILL.md` under the same root in full and follow it there, as above. The skills of the-way and their files:

- `critique`: `elements/common/critique/SKILL.md`
- `find-foundation-entries`: `elements/common/skill/SKILL.md`
- `record-decision`: `elements/decisions/skill/SKILL.md`
- `record-environment-fact`: `elements/environment-facts/skill/SKILL.md`
- `record-glossary-term`: `elements/glossary/skill/SKILL.md`
- `record-invariant`: `elements/invariants/skill/SKILL.md`
- `update-part-map`: `elements/part-map/skill/SKILL.md`
- `review-foundation`: `foundation-review/SKILL.md`
- `maintain-instruction-files`: `instruction-files/SKILL.md`
- `audit-process`: `process-audit/SKILL.md`
- `maintain-coding-guidelines`: `product-guidelines/coding/SKILL.md`
- `maintain-styleguide`: `product-guidelines/styleguide/SKILL.md`
- `maintain-testing-guidelines`: `product-guidelines/testing/SKILL.md`
- `lead-project`: `project-level/lead/skill/SKILL.md`
- `plan-project`: `project-level/plan/skill/SKILL.md`
- `define-project`: `project-level/skill/SKILL.md`
- `refine-task`: `project-level/task/skill/SKILL.md`
- `settle-technology`: `project-level/technology/SKILL.md`
- `make-change`: `task-cycle/change/SKILL.md`
- `plan-task`: `task-cycle/plan/SKILL.md`
- `review-change`: `task-cycle/review/SKILL.md`
- `implement-task`: `task-cycle/skill/SKILL.md`
- `write-spec`: `task-cycle/spec/SKILL.md`
