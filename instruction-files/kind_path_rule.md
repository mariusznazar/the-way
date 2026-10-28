# Files loaded with some files

An instruction file in a subdirectory, a rule pinned to paths in `.claude/rules/` and a Cursor rule
with `globs` hold the rules for one part of the code. They load when an agent works with the files
they cover and cost nothing elsewhere, but each tool reaches them its own way, so a rule meant for
every tool takes the shared carrier below.

## Its layout

| Layer | Shared carrier | Why it reaches every tool | Addition of a single tool |
|---|---|---|---|
| rules for parts of the code | `AGENTS.md` in a subdirectory and a line in the main file: "When working in `x/`, read `x/AGENTS.md`" | Claude Code and Cursor load it on access to a file there; Codex only when the session starts in that directory — the line in the main file closes this gap | a rule with `paths` (Claude Code), a rule with `globs` (Cursor) |
