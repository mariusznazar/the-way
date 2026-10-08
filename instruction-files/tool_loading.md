# How each tool loads instruction files

Each statement below carries its source: `fact <identifier>`, an environment fact of the-way whose
entry in `foundations/environment_facts.md` holds the passage it rests on; the address of the
documentation or the public source it was read at; or *measured*, with what was measured
described where it stands. A statement no source supports says "not established". Loading changes
between versions without notice: before a rule relies on it, check it in the version in use — the
method is at the end.

## Claude Code

- **At session start:** `~/.claude/CLAUDE.md`, and `CLAUDE.md` and
  `CLAUDE.local.md` from the working directory and every directory above it, concatenated from the
  filesystem root down to the working directory
  (https://code.claude.com/docs/en/memory § How CLAUDE.md files load).
- **User-level rules:** `~/.claude/rules/` loads at launch
  (https://code.claude.com/docs/en/memory § User-level rules).
- **Rules without `paths`:** a rule in `.claude/rules/` without `paths` frontmatter loads at launch
  with the same priority as `.claude/CLAUDE.md`
  (https://code.claude.com/docs/en/memory § Organize rules with .claude/rules/).
- **`AGENTS.md` at the start:** read as the project instructions, on v2.1.277 or later, only when
  no `CLAUDE.md`, `.claude/CLAUDE.md` or `CLAUDE.local.md` stands in the working directory or any
  directory above it (fact `claude-code-agents-md`).
- **`AGENTS.md` in a subdirectory:** read when Claude opens a file there with the Read tool and
  that subdirectory has none of the three `CLAUDE.md` files of its own
  (https://code.claude.com/docs/en/memory § When Claude Code reads AGENTS.md).
- **Not read:** `AGENTS.local.md`, `AGENTS.override.md`, or anything under a `.agents/` directory
  (https://code.claude.com/docs/en/memory § When Claude Code reads AGENTS.md).
- **On access to a file:** a `CLAUDE.md` or `CLAUDE.local.md` in a subdirectory loads when Claude
  uses the Read, Write or Edit tool on a file in that subdirectory
  (https://code.claude.com/docs/en/memory § How CLAUDE.md files load).
- **Path rules:** a rule whose frontmatter gives `paths` applies only when Claude works with files
  matching those patterns (fact `claude-code-path-rules`).
- **On a write without an earlier read, and on `cat` in Bash,** a subdirectory `CLAUDE.md` and a
  rule with `paths` loaded too (measured, see below).
- **After compaction:** the project-root `CLAUDE.md` is read again from disk; nested `CLAUDE.md`
  files and rules with `paths` load again on demand
  (https://code.claude.com/docs/en/memory § Instructions seem lost after /compact).
- **`@path`** expands the imported file and loads it into context at launch, alongside the
  `CLAUDE.md` that references it; Markdown code spans and fenced code blocks are skipped
  (fact `claude-code-imports`).
- **`@path` depth and paths:** imports may nest to a depth of four hops, and a relative path
  resolves from the file that holds the import
  (https://code.claude.com/docs/en/memory § Import additional files).
- **`@path` followed at once by a full stop, comma, bracket or colon** did not load, without a
  warning, while a space or the end of the line after it loaded (measured, see below).
- **A `PreToolUse` hook** with an `if` field (for example `"Bash(git commit *)"`) runs only when
  the tool call matches, and its `additionalContext` is inserted into the conversation next to the
  tool result (https://code.claude.com/docs/en/hooks).
- **Skills:** project skills load from `.claude/skills/` in the starting directory and every
  parent directory up to the repository root (fact `claude-code-project-skills`), and those below
  the starting directory when a file there is first read or edited
  (fact `claude-code-nested-skills`).
- **Skills in context:** the description is in context in every session unless
  `disable-model-invocation: true`; the body enters when the skill is invoked and stays across
  later turns (https://code.claude.com/docs/en/skills).
- **`.agents/skills/`:** whether Claude Code reads it is not established; its skills page and facts
  name `.claude/skills/` only.
- **How to check what loaded:** the `InstructionsLoaded` hook records each loaded file with its
  `load_reason` (`session_start`, `nested_traversal`, `path_glob_match`, `include`, `compact`); it
  does not fire when Claude reads `AGENTS.md` directly through the Project instructions setting
  (https://code.claude.com/docs/en/hooks § InstructionsLoaded).

### Settings that change loading

- **Project instructions** (`/config`): `claude-md-or-agents-md` by default, also
  `claude-md-and-agents-md`, `claude-md` and `managed-only`. In a settings file it is the option
  `instructionFiles` under `pluginConfigs` → `cc-plugin-agents-md@builtin`, read from
  `~/.claude/settings.json`, a `--settings` file or managed settings and ignored in project and
  local settings (https://code.claude.com/docs/en/memory § Choose which instruction files load).
- **`claudeMdExcludes`:** glob patterns, matched against absolute paths, of `CLAUDE.md` files to
  skip; configurable at any settings layer (https://code.claude.com/docs/en/memory § Exclude
  specific CLAUDE.md files).

## Codex

- **At session start:** the instruction chain is built once per run: `AGENTS.override.md`, or else
  `AGENTS.md`, of the Codex home directory, then, walking from the project root down to the
  current working directory, at most one file per directory; the search stops at the current
  directory (fact `codex-agents-md`).
- **Order and conflicts:** the files are concatenated root first, so the one nearer the working
  directory comes later and wins a conflict
  (https://learn.chatgpt.com/docs/agent-configuration/agents-md § Layer project instructions).
- **Size:** Codex stops adding files once their combined size reaches `project_doc_max_bytes`
  (32 KiB by default); another page of the documentation words the same key as the amount read
  from each `AGENTS.md` file
  (https://learn.chatgpt.com/docs/agent-configuration/agents-md § How Codex discovers guidance;
  https://learn.chatgpt.com/docs/config-file/config-advanced § Project instructions discovery).
- **A file in a subdirectory off that chain does not arrive:** an agent creating a file in such a
  subdirectory did not open its `AGENTS.md` in any of four sessions started at the root, and
  followed the same rule in both sessions started in that subdirectory (measured, see below).
- **In an untrusted project** only the global file loads
  (https://github.com/openai/codex/blob/137f25f6439ce8be758f15dbd1e1b297c6cd0c3b/codex-rs/core/src/agents_md.rs, the public
  source of Codex, `config.active_project.is_untrusted()`).
- **`@path`** is plain text; the page names no `@` syntax
  (https://learn.chatgpt.com/docs/agent-configuration/agents-md).
- **`CLAUDE.md`** is read only when added to `project_doc_fallback_filenames`, and then only in a
  directory without `AGENTS.md` (https://learn.chatgpt.com/docs/agent-configuration/agents-md §
  Customize fallback filenames).
- **Skills:** `.agents/skills` in every directory from the current working directory up to the
  repository root (fact `codex-repository-skills`), and `$HOME/.agents/skills`
  (https://learn.chatgpt.com/docs/build-skills).
- **Skills in context:** the initial list holds each skill's file path (fact `codex-skill-paths`)
  and each skill's name and description; the full `SKILL.md` is read when Codex chooses the skill, and a
  skill with `allow_implicit_invocation: false` is invoked only by an explicit `$skill`
  (https://learn.chatgpt.com/docs/build-skills).
- **Codex's skills prompt tells the model not to carry skills across turns unless re-mentioned**
  (https://github.com/openai/codex/blob/137f25f6439ce8be758f15dbd1e1b297c6cd0c3b/codex-rs/ext/skills/src/catalog_prompt.rs, the
  public source of Codex).
- **`.claude/skills/`:** whether Codex reads it is not established; its documentation names
  `.agents/skills` only.
- **How to check:** `codex --ask-for-approval never "Summarize the current instructions."` from a
  repository root
  (https://learn.chatgpt.com/docs/agent-configuration/agents-md § Verify your setup).

### Settings that change loading

- **`project_doc_max_bytes`:** 32 KiB by default; the AGENTS.md page says "combined" and the
  advanced-configuration page says "each"
  (https://learn.chatgpt.com/docs/agent-configuration/agents-md;
  https://learn.chatgpt.com/docs/config-file/config-advanced).
- **`project_doc_fallback_filenames`:** filenames tried in each directory after `AGENTS.override.md`
  and `AGENTS.md`; names not on the list are ignored
  (https://learn.chatgpt.com/docs/agent-configuration/agents-md § Customize fallback filenames).
- **`AGENTS.override.md`:** takes the place of `AGENTS.md` in the directory, or in the Codex home
  directory, where it stands (https://learn.chatgpt.com/docs/agent-configuration/agents-md).
- **`CODEX_HOME`:** the environment variable that moves the Codex home directory, `~/.codex` by
  default (https://learn.chatgpt.com/docs/agent-configuration/agents-md).

## Cursor

- `AGENTS.md` and `CLAUDE.md` at the project root, where present, are applied as rules alongside
  `.cursor/rules` (fact `cursor-agents-md`).
- **A rule with `alwaysApply: true`** is always included (https://cursor.com/docs/rules § Rule
  anatomy).
- **An `AGENTS.md` in a subdirectory** applies when the agent works with files in that directory
  or its children, combined with those of the parent directories (https://cursor.com/docs/rules §
  AGENTS.md).
- **On a read of a file:** a rule with `globs` and a subdirectory `AGENTS.md` loaded when the
  agent read a matching file, and a glob rule did not load on a write without an earlier read
  (measured, see below).
- **A file that is only open in an editor tab** does not trigger a glob rule — an answer of
  Cursor's staff, and a user's measurement, on its forum
  (https://forum.cursor.com/t/glob-scoped-rules-should-trigger-on-ai-file-access-not-just-editor-tabs-plus-mcp-cli-tool-triggers/156553).
- **A rule with only a description:** the agent reads the description and pulls the rule in when
  relevant (https://cursor.com/docs/rules § Rule anatomy).
- **`@file` in a rule:** the file's contents are not inlined into the prompt, in the editor, the
  CLI and Cloud Agents; the agent reads the file when it needs it (https://cursor.com/docs/rules §
  Referencing files from a rule).
- **A rule must be a `.mdc` file with a YAML header;** a plain `.md` file in `.cursor/rules` is
  ignored (https://cursor.com/docs/rules § Rule file structure).
- **`.claude/rules/`** was not loaded (measured, see below); the rules page does not name it
  (https://cursor.com/docs/rules).
- **Skills:** `.agents/skills/` and `.cursor/skills/`, and for compatibility `.claude/skills/`,
  `.codex/skills/` and their `~/` equivalents (https://cursor.com/docs/skills).
- **Bugbot** reads `.cursor/BUGBOT.md` files; project rules in `.cursor/rules` do not apply to its
  runs, and the page does not name `AGENTS.md` (https://cursor.com/docs/bugbot).
- **An `AGENTS.md` above the directory it works in:** loaded in a session started at a
  repository's root when it stands one directory above, outside git (Cursor CLI 2026.10.01,
  2026-10-08, 1 of 1 session), and in a session started in a subdirectory of that repository (1 of
  1); loaded when the directory above is itself a git repository (1 of 1); loaded when the file
  above is a symbolic link to a file elsewhere (1 of 1). Only one directory above was measured;
  how far up Cursor walks is not established. Whether the file two directories above, a link to a
  user's global file, reaches Cursor is not established: that session was started without
  `--trust`, stopped on workspace trust and was not run. Method: one fresh `cursor-agent -p
  --trust --mode ask` session per variant, in a scratch directory (`--trust` given to the four
  scratch variants, never to the last), a marker phrase per file, the repository's own `AGENTS.md`
  as the positive control (it appeared in every session). The evidence is the model's own list of
  markers: the text output records no tool calls, and the prompt forbade reading files. The
  sandbox flag is not available on Windows and was not used (measured).

### Settings that change loading

- No setting that changes which instruction files load is found in Cursor's documentation
  (https://cursor.com/docs/rules, https://cursor.com/docs/cli/using).

## Method of checking

One fresh headless session per variant, each in its own directory: `claude -p`, `codex exec`,
`cursor-agent -p`. Each file under test holds a distinct marker phrase; the session lists the
markers it can see, after the tool action whose effect is under test (a read, a write without a
read, a command). One file in every variant must load — the positive control; without it an empty
list proves nothing. In Claude Code the `InstructionsLoaded` hook, passed with `--settings`, gives
evidence independent of the model's answer
(https://code.claude.com/docs/en/hooks § InstructionsLoaded). Where loading cannot be listed, the
behaviour is the evidence: the rule asks for a visible trace, such as the first line of a file the
agent creates.

## Measurements

- **Claude Code 2.1.293 (`claude -p`), 2026-10-07:** one fresh headless session per variant in its
  own directory, a marker phrase in each file under test, a file that must load as the positive
  control, and the `InstructionsLoaded` hook's log. `@path` followed at once by `.`, `,`, `)` or
  `:` did not load, without a warning, while a space or the end of the line after it loaded; the
  same `@path` in backticks did not load; a subdirectory `CLAUDE.md` and a rule with `paths` did
  not load at the start and loaded on a read, on a write without an earlier read and on `cat` in
  Bash; a rule without `paths` loaded at the start; `AGENTS.md` alone, without `CLAUDE.md`, put
  its marker in the context (the hook does not record it, as the documentation says) (measured).
- **Codex CLI 0.157.0 (`codex exec`), 2026-10-07:** one fresh headless session per variant in a
  repository whose root `AGENTS.md` and `pkg/AGENTS.md` each held a rule; the task was to create
  `pkg/hello.js`. The root's rule held in 4 of 4 sessions started at the root; the rule in
  `pkg/AGENTS.md` was followed in 0 of 4 sessions started at the root and in 2 of 2 sessions
  started in `pkg/` (measured).
- **Cursor CLI 2026.10.01 (`cursor-agent -p`), 2026-10-07:** one fresh headless session per
  variant, a marker phrase in each file under test. At the start `AGENTS.md`, `CLAUDE.md` and a
  rule with `alwaysApply: true` loaded, while a file named with `@` in a rule, a rule with only a
  description, `.claude/rules/`, a subdirectory `AGENTS.md` and glob rules did not; on a read a
  subdirectory `AGENTS.md` and a glob rule loaded; on a write without a read the glob rule did not
  (measured, 1 session per variant).
- **Cursor CLI 2026.10.01 (`cursor-agent -p --trust --mode ask`), 2026-10-08:** four fresh
  sessions in scratch directories, each given `--trust`, a marker phrase in each file; the first
  and second share one fixture, the second starting in its `sub/`. The evidence is the model's own
  list of markers (the text output records no tool calls; the prompt forbade reading files). The
  repository's own `AGENTS.md` (the positive control) appeared in all four. The outer `AGENTS.md`,
  one directory above, also appeared when the session started at the repository's root with the
  file outside git, when it started in a subdirectory, when the directory above was itself a git
  repository, and when the file above was a symbolic link to a file elsewhere (measured, 1 session
  per variant). A fifth session, in a directory two levels below a link to a user's global file,
  was started without `--trust`, stopped on workspace trust and was not run, so the negative
  control was not needed.
