# Task 8 report

Status: DONE_WITH_CONCERNS. Commit 9b6e86f (only instruction-files/tool_loading.md).

## Measurement
Cursor CLI 2026.10.01-e373342, 2026-10-08. Full record: .runs/task-cycles/instruction-files-part/reports/cursor_measurement.md, cursor_V1..V5.txt, cursor_version.txt.
Command: `cursor-agent.cmd -p --trust --mode ask --output-format text "<P>"` in scratch fixtures (V1 root, V2 sub/, V3 enclosing git repo, V4 symlink above).
- V1-V4: exit 0; each listed MK-ROOT-7000, MK-OUTER-7001, "# Repository file", "# Outer file". Positive control present in all. Outer file loaded in all four, link followed.
- V5 (process root, no --trust): stopped on workspace trust, exit 1 -> not run. Negative control therefore not evaluated.
- Process root `git status --short --ignored`: before empty, after empty, identical.
- No cursor-agent process left (tasklist).
Deviations: `--sandbox enabled` errors on Windows ("requires macOS or Linux"), so it was dropped (mode ask is read-only; `agent sandbox disable` would change user config, not done). Without --trust V1-V4 stopped on trust; reran with --trust (scratch only).

## Task point 5
Met for a plain file and for a linked file (scratch setup). The real case (global file two directories above) is not established; the bullet says so.

## Checks
sources_check.py: 52 bullets, 0 without a source, exit 0. Local-path grep: exit 1 (none). Fact lines name only existing facts (9).

## Concerns
- Sandbox flag dropped; the file's method line says so.
- Codex source cited by main-branch file address, not a commit (commit unknown to me).
- project_doc_max_bytes: "each" wording is on the config-advanced page, "combined" on the AGENTS.md page; cited both.
- Claude "Project instructions" has a key: option instructionFiles under pluginConfigs -> cc-plugin-agents-md@builtin.
- Cursor staff-forum statement cited by thread address (from prototype notes, not reopened); skills/bugbot/hooks pages reopened.
- Statements about Claude Code hooks page fetched only first 100k chars; the InstructionsLoaded passage was found.

## Fix round 1
All 12 items applied to instruction-files/tool_loading.md: Codex check command now the documented `codex --ask-for-approval never ...` (Verify your setup); Codex source links pinned to 137f25f6 (raw files fetched at that SHA: `is_untrusted()` at agents_md.rs:64, "Do not carry skills across turns unless re-mentioned" in catalog_prompt.rs); `--trust` stated for V1-V4 and not given to V5; skill name/description moved under the build-skills address; the two "measured" skill-directory claims replaced by "not established" and removed from Measurements; Cursor session-start label dropped; `~/.claude/rules/` cited to User-level rules; catalog wording; shared V1/V2 fixture; evidence is the model's own marker list; only one directory above measured; trailing spaces removed, prose wrapped (only URL-bearing lines exceed 100 columns). Checks: sources 53 bullets / 0 missing, local grep none, 9 fact ids exist.
Note: the "User-level rules" section name was taken from the coordinator's finding, not reopened.
