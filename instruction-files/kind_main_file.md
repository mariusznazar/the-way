# The main file

The main file is the file the tool adds to every session: `CLAUDE.md`, `AGENTS.md`, a Cursor rule
with `alwaysApply: true`, the user's global file. Each of its lines costs context in every session
and — when it is a requirement — extra steps of the agent, because agents carry out instructions;
that is why each line meets the three conditions of the criterion. A file the main file points to
holds knowledge needed now and then.

## What it holds

The main file sketches the surroundings and points to the ways in. It holds three kinds of content:

- **Surroundings the agent cannot see.** Where things lie that are outside the repository or
  outside the obvious place (the backlog, documentation, related repositories), which source wins
  when two places speak of the same thing, unusual features of the environment. Not a description
  of the repository: directory structure, architecture and stack can be read from the code, and
  descriptions of a repository do not shorten the agent's way to the right files; overviews of a
  repository in such files have not helped agents, while the instructions in them are followed
  (fact `context-file-effect`).
- **Pointers to ways in.** "Before X, read `path`" or "X is done by the skill `name`" — for
  activities whose way in the agent will not recognise from the request alone, with the condition
  worded as the criterion asks.
- **Rules that always apply**, short and not derivable from the repository: a convention absent
  from the tools' configuration, a command the agent will not guess, a pitfall it trips on.

What the main file does not hold:

- repetitions of the README, configuration, the linter or the framework's documentation — a tool
  enforces them or the agent knows them without the file;
- multi-step procedures — they belong in a skill, and the main file at most points to its way in;
- rules for one part of the code — they belong in a rule pinned to paths or in a file in a
  subdirectory;
- content that changes often — the main file points to its source;
- the history of a rule: dates, the course of an incident, abandoned variants.

**The global file has the highest bar.** Its line costs context in every session in every
repository, so it keeps only what concerns work regardless of the repository. A rule true for one
repository or one kind of work goes into that repository's file or onto the route of that work.

## Its layout

| Layer | Shared carrier | Why it reaches every tool | Addition of a single tool |
|---|---|---|---|
| main file | `AGENTS.md` at the root | Codex and Cursor read it in a trusted project; Claude Code when the repository has no `CLAUDE.md` | `CLAUDE.md` only for additions meant for Claude Code alone; its first line is `@AGENTS.md` on its own (WAY-132) |
| global file | — (each tool has its own) | — | one copy per tool, kept in step by a check that reports drift between them |

Pitfalls:

- **`@path` only as `@AGENTS.md` alone on the first line of `CLAUDE.md`** (WAY-129, WAY-132).
  Nowhere else does it serve as a pointer: in Claude Code it loads the file into every session, and
  a punctuation mark right after it switches the loading off without a warning; in Codex it is
  plain text.
- **`CLAUDE.local.md` stops Claude Code from reading `AGENTS.md`.**
