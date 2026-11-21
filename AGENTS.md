# Working in the-way

When the-way is the top-level repository you are changing, read `agent-instructions/README.md`
before starting. It defines the current integration route while the-way has no `main` branch.
When this checkout is a product's `.the-way` submodule, follow the product's instructions instead.

## Skills

A human starts each skill of the-way in a session on this repository as the project skill
`the-way-<name>` — in Claude Code with the command `/the-way-<name>` — from its entry point in
`.claude/skills/` for Claude Code and `.agents/skills/` for Codex. The entry points carry
`disable-model-invocation: true`, so the model is not offered a skill of the-way and never calls
one: a skill hands work to another through that skill's `SKILL.md`, which the session reads from the
checkout or worktree it works in, as an entry point reads its skill and each file the skill names
when the step that names it comes. Start only these: a personal skill of the same name without the
prefix — `refine-task`, `critique` or another — is not the-way's. A change that adds, renames or
moves a skill, or changes its description, runs
`python -B agent-instructions/skill_entry_points.py --write` and commits what it writes; the gate's
tests report a skill a human could not start under its `the-way-` name. A change to a definition of
an agent type in `task-cycle/agent-types/` runs
`python -B agent-instructions/agent_type_copies.py --write` and commits what it writes; the gate's
tests report a copy in `.claude/agents/` that differs from its definition.

## Backlog

- Tasks: the key `tasks` under `the-way` in the locations file `~/.the-way/locations.json`, which
  lies on the author's disk outside every repository. A task's description is a document in the
  `_zadania` folder beside the file the key names, linked from the task's line. Both are in the
  author's private notes. Where the file or the key is missing, or an agent cannot open them, it
  asks the human and offers to add the key to the file.
- Task rules: the key `task-rules` under `the-way` in the same locations file. It names the
  author's rules for a task's line: its status when new, its move to ready, its dependencies. A
  missing key or file is handled as for the tasks.

## Guidelines

- Before you change the-way's code, read `guidelines/coding.md`.
- Before you write or change a test, read `guidelines/testing.md`.
