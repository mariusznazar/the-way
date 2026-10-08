# How each tool loads instruction files

State checked on 2026-10-07 for Claude Code 2.1.293, Codex CLI 0.157.0 and Cursor CLI 2026.10.01.
"Measured" marks behaviour checked that day in fresh headless sessions, with a marker phrase in
each file under test and a positive control; the rest comes from the tools' documentation or, for
Cursor, from answers of Cursor's staff on its forum. Loading changes between versions without
notice: before a rule relies on it, check it in the version in use — the method is at the end.

## Claude Code

- **At session start:** `~/.claude/CLAUDE.md`, `~/.claude/rules/`, `CLAUDE.md` and
  `CLAUDE.local.md` from the working directory and the directories above it, rules in
  `.claude/rules/` without `paths`, files imported with `@`. `AGENTS.md` only when there is no
  `CLAUDE.md`, `.claude/CLAUDE.md` or `CLAUDE.local.md` (measured; since 2.1.277).
- **On access to a file:** a `CLAUDE.md` in a subdirectory and a rule with `paths` — on a read, on a
  write without an earlier read and on `cat` in Bash (measured). A subdirectory `AGENTS.md` loads on
  a read when that directory has no `CLAUDE.md`. After compaction they are summarised and come back
  on the next access; the main file is read again from disk.
- **`@path`** loads the whole file at the start of every session. It works only when a space or the
  end of the line follows the path — a full stop, comma, bracket or colon right after the path
  switches the loading off without a warning (measured). It does not work in backticks or code
  blocks. At most four levels deep; relative paths count from the importing file.
- **A `PreToolUse` hook** with an `if` field (for example `"Bash(git commit *)"`) injects text
  (`additionalContext`) at the moment a command is run.
- **Skills:** only `.claude/skills/` (measured: `.agents/skills/` is not read); the description in
  every session unless `disable-model-invocation: true`, the body once invoked; it stays in context
  until the session ends.
- **How to check what loaded:** the `InstructionsLoaded` hook records each loaded file with its
  reason (`session_start`, `nested_traversal`, `path_glob_match`, `include`); it does not record an
  `AGENTS.md` read directly.

## Codex

- **At session start:** `~/.codex/AGENTS.md` (or `AGENTS.override.md`) and the chain of `AGENTS.md`
  files from the repository root to the directory where the session started — at most one file per
  directory; the nearer one comes later and wins a conflict. A limit of 32 KiB
  (`project_doc_max_bytes`; the documentation contradicts itself on whether it is a total or per
  file). In an untrusted project only the global file.
- **A file in a subdirectory off that chain does not arrive:** an agent creating a file in such a
  subdirectory did not open its `AGENTS.md` in any of four sessions started at the root, and
  followed the same rule in both sessions started in that subdirectory (measured).
- **`@path`** is plain text. `CLAUDE.md` only when added to `project_doc_fallback_filenames`, and
  only in a directory without `AGENTS.md`.
- **Skills:** `.agents/skills` from the starting directory upwards and `~/.agents/skills`
  (measured: `.claude/skills/` is not read); the description in every session, the body once
  chosen; manual invocation only with `allow_implicit_invocation: false`. A skill does not carry
  over to the next turn unless it is named again (read in the source code).
- **How to check:** `codex exec "Summarize the current instructions."`.

## Cursor

- **At session start:** `AGENTS.md` and `CLAUDE.md` from the root, rules with
  `alwaysApply: true` (measured in the CLI). With a full `CLAUDE.md` beside `AGENTS.md`, both load.
- **On a read of a file:** a rule with `globs` and a subdirectory `AGENTS.md` — when the agent reads
  a matching file; not on a write without an earlier read (measured in the CLI), and not for a file
  that is only open in an editor tab.
- **A rule with only a description:** the agent sees the description and decides whether to load
  the rule.
- **`@file` in a rule** is not pasted in (measured) — the agent reads the file when it thinks it
  needs to.
- **A rule must be a `.mdc` file with a YAML header;** a `.md` file in `.cursor/rules/` is ignored,
  and so is `.claude/rules/` (measured). A rule added during a conversation works from the next
  chat.
- **Skills:** `.cursor/skills`, `.claude/skills`, `.codex/skills`, `.agents/skills`.
- **Bugbot** reads only `.cursor/BUGBOT.md`; project rules do not reach it.

## Method of checking

One fresh headless session per variant, each in its own directory: `claude -p`, `codex exec`,
`cursor-agent -p`. Each file under test holds a distinct marker phrase; the session lists the
markers it can see, after the tool action whose effect is under test (a read, a write without a
read, a command). One file in every variant must load — the positive control; without it an empty
list proves nothing. In Claude Code the `InstructionsLoaded` hook, passed with `--settings`, gives
evidence independent of the model's answer. Where loading cannot be listed, the behaviour is the
evidence: the rule asks for a visible trace, such as the first line of a file the agent creates.
