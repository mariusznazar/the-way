---
name: maintain-instruction-files
description: Use when an instruction file for coding agents — AGENTS.md, CLAUDE.md, .claude/rules, .cursor/rules/*.mdc, a user's global instruction file — has to be written, judged, split or cleaned up, or when a rule has to be placed in one, such as a rule settled in a review of agent sessions.
---

# Maintain instruction files

Writes, judges and cleans up the files from which coding agents take their rules, in Claude Code,
Codex and Cursor at once. The principles stand in `principles.md`, how each tool loads each file
stands in `tool_loading.md`, and the mechanical checks are `check_instructions.py` — all three in
this skill's component directory. This skill holds only the procedure.

This skill lives in `instruction-files/skill/` of the-way. Installed globally, its base directory
is a link, so resolve it first: `realpath <base>` in Bash, `(Get-Item <base>).Target` in
PowerShell. The component directory is the parent of the resolved one.

## 1. Read

- Read `principles.md` and `tool_loading.md` in full before anything else.
- Run `python -B <component>/check_instructions.py <repository>`; add `--file <path>` for the
  user's global file when it is under review. Read every file the checker lists — they load
  together, and a contradiction between them shows only when they are read together.
- Establish which of the three tools the repository is used with; ask when it is not stated.
  Section 4 of the principles depends on it.

## 2. Choose the mode

| Situation | Mode |
|---|---|
| the files exist and the request is to judge, split or clean them | judge |
| a judgement has been accepted | change |
| a single rule has to be placed | place |
| the repository has no instruction file | write |

## Judge

Output, in this order:

1. The checker's errors and warnings, each with what it means in each tool in use.
2. A table with one row per fragment of every file: the quoted fragment with `file:line`, the
   verdict — keep, move, remove or reword — and its reason: for keep, the three conditions of
   section 2; for move, the trigger and the target from section 3; for remove, the condition that
   fails or the defect of section 6; for reword, the new wording.
3. Contradictions between files that load together.

Every statement about when a tool loads a file comes from `tool_loading.md` or from a measurement
made in this session. The table is a batch of decisions; edit nothing until it is accepted.

## Change

Apply the accepted rows. A reworded rule replaces the sentence that stands. A moved rule gets its
target file and, where section 4 requires one, the pointing line. Run the checker again and show
the diff and the checker's output.

## Place

1. Name the mistake the rule removes and whether it applies with a human present or without one.
   A rule whose mistake cannot be named is not placed.
2. Find the rule's trigger (section 3). When it must happen every time, propose the mechanism
   first — a script, a git hook, a CI check, a Claude Code hook — and an instruction only for what
   the mechanism cannot do.
3. Search the instruction files for a rule on the same subject; when one stands, the new wording
   replaces it.
4. Word the rule by section 5, with the command or file that leaves its trace.
5. Show the place, the wording and what happens if it is left out, and write only after approval.

## Write

The rules of an instruction file cannot be derived from the repository; the repository gives at
most a check of what the human says.

1. From the repository take only what meets the three conditions of section 2 — typically a
   command the agent would not guess. Nothing the README, the configuration or the manifest
   already says.
2. Ask the human for the rest: the surroundings the agent cannot see, the rules that always
   apply, the activities whose way in the agent would not recognise. Leave `TODO` where there is
   no answer; do not fill it from the code.
3. Lay the files out by section 4 for the tools in use.
4. Name the file's sections in the words its readers use for the product, such as `Where things
   are`, `Before you release`, `Rules`, written in the language of the repository.
5. Show the files and write them only after approval.

## Mistakes this skill prevents

| Mistake | Instead |
|---|---|
| saying from memory when a tool loads a file | `tool_loading.md` or a measurement in this session |
| keeping a description of the repository or of what the product does | surroundings the agent cannot see, or nothing |
| repeating the README, the configuration or `package.json` | leave it to the file that holds it |
| placing a rule that must hold every time only as an instruction | a mechanism, and an instruction for the rest |
| copying the user's own global rules into a repository others share | ask; the global file is the user's |
| splitting a file by the number or length of its rules | split only when the trigger changes |
| using `@path` as a pointer | a path in backticks |
| headings and wording taken from the principles — surroundings, way in, route, trigger | the words the file's readers use for the product |
