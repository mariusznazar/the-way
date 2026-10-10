# Task 2 report — product layout and pin movement

Status: DONE
Commit: d40e8cc92df4b876374644e3b9af333f06fb7b80 — docs(installation): Describe shared guidance through the root Claude import
Worktree: C:/Storage/repos/the-way-wt/installer-claude-md

## Changed wording

- installation/README.md: Claude Code receives root AGENTS.md through root CLAUDE.md; the file table describes the shared marked AGENTS.md guidance and generated sole-line @AGENTS.md import. Product commit paths include CLAUDE.md. Pin movement recreates 24 skill wrappers, preserves existing CLAUDE.md, and creates it only if absent. Old-rule removal applies only to products migrating from a pin that installed it. Existing skill conflict wording no longer calls a rule installer-owned. The warning section describes an ineffective or missing import, manual correction, and regular UTF-8 file refusal. The testing section describes four warning kinds and Claude-file/import coverage.
- instruction-files/SKILL.md: the installer exception names the root CLAUDE.md it creates instead of the old rule. The marked AGENTS.md block and both tools' skill entry points remain excluded from proposed edits. Frontmatter is unchanged; entry-point regeneration is not needed.

## Retained legacy-rule references

Ran: rg -n 'the-way\.md|CLAUDE\.md|AGENTS\.md' installation/README.md instruction-files/SKILL.md foundations/decisions.md

Exact README context:

> twenty-four wrappers for the new commit and leaves the foundation files as they are. Only when
> migrating from an older pin that installed `.claude/rules/the-way.md`, remove that old rule in the
> product task; the current installer neither writes nor deletes it. The installer creates root
> `CLAUDE.md` if absent and preserves it if present.

This is a conditional product migration instruction. It does not ask future pin moves to remove or recreate the file universally.

Exact decisions context, WAY-141/1:

> `CLAUDE.md` untouched. The installer writes no `.claude/rules/the-way.md`.

This prohibits current generation. WAY-132 verification examples now refer to the root CLAUDE.md and marked AGENTS.md block; no legacy-rule mention remains there or in instruction-files/SKILL.md. The invariant's matching prohibition was also read. Foundation files were not edited by this implementer.

## Checks

| Command | Exit | Result |
|---|---:|---|
| python -B gate/run_tests.py installation --record .runs/installation-tests.jsonl | 0 | 26 tests, OK, 84.169s |
| python -B gate/run_tests.py instruction-files | 0 | 104 tests, OK, 5 skipped, 2.659s |
| python -B gate/run_tests.py gate | 0 | 98 tests, OK, 14.144s |
| git diff --check | 0 | No whitespace errors |

Read .runs/installation-tests.jsonl: ten pass records for installation-claude-guidance/1, including the four independent tests; no failure or unchecked record. These are partial repository checks, not the full gate.

Read foundation-author-report.md and invariant-check-report.md in .runs/task-cycles/installer-claude-md/reports. Foundation guards reported 0 errors: decisions had 6 warnings and 5 unchecked (five overdue reviews, the pending request-link placeholder, and comparisons requiring base/merge commits); invariants had 3 unchecked; part map had 7 unchecked for coverage, promises, graph and base comparisons. The invariant report records its intentional pre-implementation four-test red result; the current installation run passes those four tests.

## Self-review and wording choices

Compared each brief requirement with the final diff and actual installation/install.py behavior. The generated route, preservation, warning-before-confirmation, shared block, migration-only cleanup, wrapper recreation and foundation preservation are described. No CLAUDE.local.md warning or loop2 change was introduced. Routine choices: replace the obsolete output row in place, use the actual twelve-per-tool wrapper count, describe effective imports briefly, and limit the skill exception to CLAUDE.md the installer creates. Only the two authorized files were staged and committed. Other agents' foundation changes and independent check remain uncommitted and untouched. No review was performed after the committed-slice boundary; no push was made.

Concerns: none affecting this slice. The known foundation warnings, unchecked checks and instruction-files skips remain visible above.
