# Author report — installer-preview-ignores-line-endings

**Status:** done with concerns

Concern: the linter (pinned Ruff 0.17.1) reports 8 blocking rules on the installation part. None sits
on a line this change adds, all 8 predate it, and `foundations/invariants.md`, entry
`ruff-blocking-rules`, already records `Violated: yes`. Not fixed here; see the check section.

## Commits

- `b2c31cc2` on `task/installer-preview-ignores-line-endings` (not pushed):
  "Keep installer files whose text differs only in CRLF line endings"

## Files changed

| File | Added | Removed |
|---|---|---|
| `installation/install.py` | 4 | 1 |
| `installation/test_install.py` | 117 | 0 |
| `installation/README.md` | 4 | 1 |

The change (`file_action`, `installation/install.py:512`): the comparison is now
`path.read_bytes().replace(b"\r\n", b"\n") == content.encode("utf-8")`, with the foundations branch
unchanged. `run()` is untouched, so no move out of it was needed. `file_action` is now 9 lines,
far under the 80-line threshold.

## Choices made

1. **How a line ending is normalised.** Only the two-byte `\r\n` is folded to `\n`, the same as
   `agents_change` does with `text.replace("\r\n", "\n")`. Rejected: universal newlines or
   `splitlines()` before the comparison, which would also fold a lone `\r`, and stripping whitespace,
   which folds more than line endings. Cost if wrong: a file with a lone `\r` would be kept although
   its text differs.
2. **A lone `\r` is text.** A carriage return that no `\n` follows is not a line ending git's
   `core.autocrlf` ever writes from LF text, so the file is `REPLACE`d and rewritten with LF, which
   drops the stray `\r`. This is my judgement, pinned by a test.
3. **Mixed endings with the same text are `KEEP`.** The task says "differs only in line endings",
   and git stores both `\r\n` and `\n` as `\n`. Rejected: requiring all-CRLF, which would rewrite such
   a file to LF. Cost if wrong: a mixed file stays mixed in the product.
4. **A file missing its last line ending is `REPLACE`.** A missing ending is a text difference, not a
   CRLF for an LF. Cost: none beyond today's behaviour.
5. **Empty, non-UTF-8 and lone-`\r` files are `REPLACE`**, compared as raw bytes as before.
6. **A symlink or junction at an entry point's path** is refused by `plan()` before `file_action` runs
   (`owned()` and the foundations check, both unchanged). No new test for the symlink case at a skill
   path; the existing junction tests cover the path checks.
7. **Reach beyond the dispatch: `installation/README.md`.** Not named by the handoff. I read its
   lines 218–243 and the rows at 59–63 by grep. I added one sentence to the "Existing files" paragraph
   saying a CRLF file with the installer's text is kept and shows no difference, and a file with a real
   change is written with LF. Reason: the paragraph describes what the installer does with an existing
   entry point, and would be silent on the change. Cost if wrong: one sentence to revert.
8. **Test levels.** `FileActionTest` is a files test (temporary directory, no git, WAY-393), placed
   in `installation/test_install.py`, not a separate file. The three `InstallTest` methods are git
   tests on the existing fixture: `test_crlf_files_with_the_same_text_are_kept_and_not_rewritten`
   (the break named: raw-byte comparison returns), and
   `test_a_crlf_file_with_other_text_is_replaced_and_shows_only_the_real_change` (a guard, see below).
   Expected values are literals and the entry point's text comes from the `ENTRY_POINT` template the
   test already carries; no value is computed by `install.py`.
9. **Foundation step.** The task carries no *Settlements to record* and no projected entry, so no
   entry is written. The search of the foundation (see searches) found no entry that describes the
   preview's `KEEP` or `REPLACE`, or that says the installer compares bytes. No entry needed a
   correction. `invariants.md` `installation-claude-guidance` ("preserves the file byte for byte")
   is about `CLAUDE.md`, which this change does not touch.

## Tests written first, and the runs

Before the code change, with the new tests and the original `install.py`:

- Command: `python -B gate/run_tests.py installation`, exit 1, `Ran 73 tests`, `FAILED (failures=3)`:
  - `test_install.FileActionTest.test_the_same_text_with_crlf_endings_is_kept`: `AssertionError: 'REPLACE' != 'KEEP'`
  - `test_install.FileActionTest.test_the_same_text_with_mixed_endings_is_kept`: `AssertionError: 'REPLACE' != 'KEEP'`
  - `test_install.InstallTest.test_crlf_files_with_the_same_text_are_kept_and_not_rewritten`: the preview
    shows `REPLACE .claude/skills/the-way-record-decision/SKILL.md` and `REPLACE .claude/agents/the-way-stage.md`
    where `KEEP` is expected.
- The guard `test_a_crlf_file_with_other_text_is_replaced_and_shows_only_the_real_change` passed before
  the change too. It is a guard by design: it breaks only if CRLF files are kept whatever their text.

After the code change, the same command: exit 0, `Ran 73 tests`, `OK`.

Mutations in my head, and the test that catches each:
- no normalisation: the CRLF tests and the `InstallTest` CRLF test go red (seen above).
- fold every `\r`: `test_a_lone_carriage_return_is_text_and_is_replaced` goes red.
- keep every CRLF file: `test_crlf_endings_with_other_text_are_replaced` and the guard go red.
- normalise only the first line ending: `test_the_same_text_with_mixed_endings_is_kept` goes red.
- drop the foundations branch: `test_preview_apply_rerun_and_preserve_foundation` (its CRLF
  `decisions.md` must stay KEEP) goes red.

## Checks

| Check | Command | Exit | Result |
|---|---|---|---|
| Installation tests, before the change | `python -B gate/run_tests.py installation` | 1 | 3 failures, the new tests, as above |
| Installation tests, after the change | `python -B gate/run_tests.py installation` | 0 | 73 tests, OK |
| Linter on the installation part | `the pinned ruff binary of the main checkout's quality environment check --config ruff.toml --no-cache --output-format concise installation` | 1 | 8 reports, see below |
| Linter with noqa ignored (the invariant's flag) | same, plus `--ignore-noqa` | 1 | the same 8 reports |

Plain `ruff` is not on PATH. I used the pinned binary of the main checkout's `.runs/quality-venv`,
the one the invariant `ruff-blocking-rules` runs, at version 0.17.1 (`ruff --version` confirmed it).

The 8 reports, none in the lines I changed and none in `test_install.py`:
- `installation/install.py:83` UP022, `installation/install.py:467` PERF102 (both are on the base
  commit's same lines: `git show HEAD:installation/install.py` shows them unchanged);
- `installation/test_agent_types_installation.py:24`, `test_coding_guidelines_installation.py:20`,
  `test_installed_guidance.py:15`, `test_lead_installation.py:19`, `test_styleguide_installation.py:25`,
  `test_testing_guidelines_installation.py:20`, all UP022.

I did not fix them: they predate the change, six of them sit in files this change does not touch, and
the foundation records `ruff-blocking-rules` as `Violated: yes`. If the orchestrator wants the two in
`install.py` fixed in this task, that is a separate, behaviour-preserving edit.

Not run: the full gate (`python -B gate/run_tests.py` with no directory), as the handoff forbids.

## Own-work check (method section 3)

- Requirement most likely missed: a CRLF file with the installer's own text must be `KEEP`, must show no
  diff, must not be rewritten, and the rerun must answer "Already installed; no changes".
- Check: `InstallTest.test_crlf_files_with_the_same_text_are_kept_and_not_rewritten`, which converts
  every installed entry point and agent definition to CRLF, runs the preview (asserts `KEEP` for each,
  no `REPLACE`, no `---`/`+++` header), runs the apply (asserts `Already installed; no changes`), and
  asserts the product's bytes are unchanged. It showed the bug before the change and passes after it.
- Requirement: a CRLF file with a real change is `REPLACE` with a diff of only the real change, and the
  apply writes LF. Check: `test_a_crlf_file_with_other_text_is_replaced_and_shows_only_the_real_change`;
  it passes before and after, as a guard.
- Trust-boundary inputs of the handoff: CRLF, lone CR, mixed endings, non-UTF-8, empty and a file
  missing its last line ending are all pinned at `file_action`. A link is refused by `plan()` before
  this function, unchanged.

## Working copies

- I made no worktree, clone or prepared input. My directory `.runs/author/`
  held three files: `before_run.txt` and `after_run.txt` (the gate outputs of the two runs above) and
  `commit-message.txt` (the message I committed from). Their contents are recorded in this report, and
  I removed all three after writing it. The directory itself is kept as the handoff names it.

## Unread material

- `foundations/decisions.md`: only the entries the index lists, read through `.runs/orchestrator/index.md`.
  The whole log was not read, as the handoff selects.
- `foundations/part_map.md`: read at lines 190–235 (the `installation` and `installation-command`
  entries) only.
- `installation/README.md`: lines 218–243 read, and the rows at 59–63 by grep; the rest was not read.
- `gate/run_tests.py`: not read; I used it only as the command the handoff names.
- `task-cycle/agent-types/`: not read; the test uses the agent type names, which the installer carries.
- Read whole, as the handoff names: the three guidelines, `installation/install.py`,
  `installation/test_install.py`, `task.md`, `task-cycle/change/SKILL.md`,
  `task-cycle/skill/foundation_step.md`, `ruff.toml`, and the three invariants
  (`installation-claude-guidance`, `installation-paths-through-links`, `repository-changer-acts-only-when-told`)
  plus `ruff-blocking-rules`, which I read to check the lint finding.

## Searches not found or unclear

- `ruff` on PATH: not found; the pinned binary is in the main checkout's `.runs/quality-venv`
  (see checks). Unclear whether a worktree should use the main checkout's venv; I used it, as the
  invariant's test does.
- Foundation search for an entry describing the installer's `KEEP`, `REPLACE`, the preview, the byte
  comparison, or line endings: no entry matched, other than `invariants.md:303` (`CLAUDE.md` preserved
  byte for byte, unaffected) and `part_map.md:227` (the installer rewrites only its own files, unaffected).
  A broad first grep over `foundations/` and `installation/` produced output too large to read; I
  narrowed it and read the narrow results.
- No other searches came back unclear.
