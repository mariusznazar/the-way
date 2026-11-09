# Working in the-way

When the-way is the top-level repository you are changing, read `agent-instructions/README.md`
before starting. It defines the current integration route while the-way has no `main` branch.
When this checkout is a product's `.the-way` submodule, follow the product's instructions instead.

## Skills

A session on this repository finds each skill of the-way as the project skill `the-way-<name>`,
in `.claude/skills/` for Claude Code and `.agents/skills/` for Codex, and each reads its skill, and
each file the skill names when the step that names it comes, from the checkout or worktree the
session works in. Use only these: a
personal skill of the same name without the prefix — `refine-task`, `critique` or another — is not
the-way's. A change that adds, renames or moves a skill, or changes its description, runs
`python -B agent-instructions/skill_entry_points.py --write` and commits what it writes; the gate's
tests report a skill a session would not see.

## Backlog

- Tasks: the entry `tasks` under `the-way` in the locations file `~/.the-way/locations.json`, which
  lies on the author's disk outside every repository. A task's description is a document in the
  `_zadania` folder beside the file the entry names, linked from the task's line. Both are in the
  author's private notes. Where the file or the entry is missing, or an agent cannot open them, it
  asks the human and offers to add the entry to the file.
- When a task document first reaches `Status: ready for cycle`, set the task's line to Ready,
  [/], and remove its date, as the author's rules for agent tasks in his notes give.
