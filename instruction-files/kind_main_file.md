# The main file

The main file is the file the tool adds to every session. Each of its lines costs context in every
session and — when it is a requirement — extra steps of the agent, because agents carry out
instructions; that is why each line meets the three conditions of the criterion.

## What it holds

The main file sketches the surroundings and points to the ways in. It holds three kinds of content:

- **Surroundings the agent cannot see.** Where things lie that are outside the repository or
  outside the obvious place (the backlog, documentation, related repositories), which source wins
  when two places speak of the same thing, unusual features of the environment. Not a description
  of the repository: directory structure, architecture and stack can be read from the code, and
  descriptions of a repository do not shorten the agent's way to the right files; overviews of a
  repository in such files have not helped agents, while the instructions in them are followed
  (fact `context-file-effect`), and the agent reads the repository itself
  (https://code.claude.com/docs/en/best-practices § What you can stop doing).
- **Pointers to ways in**, where condition 1 of the criterion allows one, in the form of the
  shared layout or "X is done by the skill `name`", with the condition worded as the criterion asks;
  a concise main file references task-specific files
  (https://learn.chatgpt.com/guides/best-practices § Make guidance reusable with AGENTS.md).
- **Rules that always apply**, short: a convention absent from the tools' configuration, a command
  the agent will not guess, a pitfall it trips on.

Besides what the criterion places elsewhere, the main file does not hold:

- repetitions of the README, configuration, the linter or the framework's documentation — a tool
  enforces them or the agent knows them without the file;
- content that changes often — the main file points to its source.

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
