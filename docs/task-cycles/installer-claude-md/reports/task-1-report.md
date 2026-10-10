# Task 1 report

Status: DONE

## Implementation

Only installation/install.py and installation/test_install.py are delivered in this slice.
The installer creates root CLAUDE.md with the exact bytes `@AGENTS.md\n` when absent.
An existing regular UTF-8 CLAUDE.md is KEEP, never appended to or rewritten. The plan warns
before confirmation when its prose lacks the root import. Detection excludes backtick code
spans and backtick/tilde fenced blocks, and does not mistake a suffix or adjacent punctuation
for the required import. The former generated .claude/rules/the-way.md is removed from the
write plan. The existing AGENTS.md product_guidance source remains the single guidance source.

CLAUDE.md uses the existing shared-file CREATE/KEEP path so preview diffs, ignored-file warnings,
exclusive creation, cancellation, and repeated runs follow existing installer behavior.
Malformed UTF-8, directories and symlinks at CLAUDE.md fail before any writes, using the
installer's existing regular UTF-8 text validation. No CLAUDE.local.md warning was added.

## TDD RED

Read Superpowers 6.4.1 test-driven-development/SKILL.md and writing-good-tests.md before tests.
The independent invariant check had already reached RED (see the dispatch's referenced report).
Wrote changed behavior integration tests before production changes, then ran:

`python -B gate/run_tests.py installation --record .runs/installation-tests.jsonl`

Exit 1; `Ran 24 tests in 59.408s`; `FAILED (failures=19, errors=1)`.
Expected failures included missing CREATE/KEEP CLAUDE.md, absent missing-import warnings,
continued writing of the old rule, and acceptance of a nonregular CLAUDE.md.
The error was a fixture cascade: the failing directory subtest left its directory in place
before the following byte fixture attempted to write the same path. This was corrected by
splitting the new CLAUDE directory and invalid UTF-8 checks into independent tests, without
weakening assertions. Before changing production code, ran:

`python -B -m unittest installation.test_install.InstallTest.test_rejects_claude_directory_before_writing installation.test_install.InstallTest.test_rejects_claude_invalid_utf8_before_writing`

Exit 1; `Ran 2 tests in 1.424s`; `FAILED (failures=2)`.
Both failed with `AssertionError: 0 == 0`: preview accepted invalid CLAUDE paths instead of
refusing them before writes. These are the intended missing-behavior failures.

## GREEN and verification

`python -B gate/run_tests.py installation --record .runs/installation-tests.jsonl`

Exit 0; `Ran 26 tests in 77.154s`; `OK`.

Inspected .runs/installation-tests.jsonl: all ten records cite
installation-claude-guidance/1 with verdict pass, including all four independently authored
invariant tests. No null, fail or skipped record. Symlinks were available and the symlink test
executed successfully on this host.

`python -B gate/run_tests.py gate`

Exit 0; `Ran 98 tests in 14.981s`; `OK`.

`git diff --check`: exit 0, no whitespace errors.

Tests cover real CLI preview/apply, exact new bytes, repeated installation, unchanged existing
bytes, warning ordering, ignored new CLAUDE.md, cancellation, misleading fenced and inline code,
imports followed by suffixes or punctuation, valid prose imports, malformed UTF-8, directories,
and a symlink whose external target stays unchanged. Existing installer cases continue passing.
The orchestrator confirmed installation and gate are the checks for this slice and will run
checks for all changed parts and foundation guards at the task boundary. This is not a full-gate
claim.

## Self-review and choices

Inspected the complete diff of the two delivered files. Existing product guidance and pin logic
are preserved; the old rule is no longer in the file plan. The new shared path is always CREATE
or KEEP and therefore cannot reach APPEND. Existing file reads do not normalize or write bytes.
The warning is printed by the existing warning loop before the confirmation prompt. Ignored
CLAUDE.md joins the existing ignored-path warning. Existing files are never replaced, including
nonregular inputs, and cancellation reaches no write loop. Original line endings were preserved
by reading and writing bytes during scripted edits. No blocking findings identified.

Routine choices: reject unreadable/nonregular CLAUDE.md consistently with AGENTS.md/.gitignore;
recognize the exact whitespace-delimited root import while excluding Markdown code spans and
fences, consistent with the binding fact and the measured adjacent-punctuation limitation in
instruction-files/tool_loading.md. This is a local import detector, not a full Markdown renderer
or Claude Code parser. No new dependency is introduced.

## Boundaries and concerns

No known blocking concerns. Foundation files and installation/test_installed_guidance.py were
read-only for this implementer and remain outside this commit. No push and no independent review
were performed; this is the committed-slice boundary requested by the dispatch.

## Fix round 1 ? complete opening backtick runs

Addressed independent review finding 1. Added the exact adversarial fixture
`b"``example ` @AGENTS.md `\n"` to the existing real CLI preview/cancelled-apply test.
The fixture expects a missing-import warning and unchanged CLAUDE.md bytes. It exposed the
regex starting at the second backtick of an unmatched two-backtick run and thereby removing
the wrong code span. Added a negative lookbehind at the opening delimiter so both opening
and closing delimiters must be complete equal-length backtick runs.

Changed files: installation/install.py and installation/test_install.py only.
Exact covering test files: installation/test_install.py and installation/test_installed_guidance.py
(the independent latter file remains read-only and outside the commit).

RED, before the production fix:
`python -B -m unittest installation.test_install.InstallTest.test_existing_claude_import_detection_and_cancel_preserve_bytes`

Exit 1; `Ran 1 test in 13.044s`; `FAILED (failures=1)`.
The new fixture failed because no WARNING appeared in preview, exactly the reported defect.
The command output was retained in .runs/task-1-fix-red.txt.

Focused GREEN, after the fix, same command:
Exit 0; `Ran 1 test in 11.441s`; `OK`.

Covering suite:
`python -B gate/run_tests.py installation --record .runs/installation-tests.jsonl`
Exit 0; `Ran 26 tests in 70.129s`; `OK`.
Inspected the JSONL: ten records, all pass for installation-claude-guidance/1; no skipped,
null or failing records.

Required critical-flow checks:
`python -B gate/run_tests.py gate`
Exit 0; `Ran 98 tests in 13.223s`; `OK`.

Self-review: read the complete two-line diff, confirmed opening and closing runs have both
boundary guards, confirmed the fixture exercises actual CLI warning ordering and preservation
rather than merely the helper return value. `git diff --check` passes. Existing files' line
endings were preserved using byte reads and writes. No new concern, subagent or push.

## Independent-assessment wording fix

Applied the accepted observation dispatched in assessment-code-fix-dispatch.md: changed only
"Claude Code will miss" to "Claude Code may miss" in the missing-import warning in
installation/install.py. Loading settings can read both files, so the warning must express
that consequence as a possibility. The missing-import condition, warning placement before
confirmation, and manual @AGENTS.md instruction remain intact. No foundation or independent
invariant-test file was read or edited for this fix.

Focused verification:
`python -B -m unittest installation.test_install.InstallTest.test_existing_claude_import_detection_and_cancel_preserve_bytes`
Exit 0; `Ran 1 test in 12.312s`; `OK`.

Covering installation checks:
`python -B gate/run_tests.py installation --record .runs/installation-tests.jsonl`
Exit 0; `Ran 26 tests in 78.647s`; `OK`.
The record has ten pass verdicts for installation-claude-guidance/1 and no failing or skipped
records. Covering test files are installation/test_install.py and installation/test_installed_guidance.py;
neither test file changed in this wording fix.

Critical-flow verification:
`python -B gate/run_tests.py gate`
Exit 0; `Ran 98 tests in 14.975s`; `OK`.

Self-review: read the complete one-line production diff. Only the modal verb changed; the
condition and actionable manual-edit guidance are unchanged. `git diff --check` passes.
Byte-based editing preserves existing line endings. No additional test was introduced for a
message-wording change. Only installation/install.py is staged for this commit. No concerns,
subagents, or push. The fix stops at the committed boundary before final whole-branch review.
