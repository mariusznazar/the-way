# Independent invariant check: installation Claude guidance

- Model: GPT-6, delegated check author.
- Worktree: `C:/Storage/repos/the-way-wt/installer-claude-md`.
- Deliverable: `installation/test_installed_guidance.py` (uncommitted). No installer, existing test, foundation sentence, or Method was changed by this check author.

## Inputs

- `C:/Storage/repos/the-way-wt/installer-claude-md/foundations/invariants.md`, `installation-claude-guidance/1` sentence and Method.
- `C:/Storage/repos/the-way-wt/installer-claude-md/foundations/decisions.md`, `WAY-141/1` binding text.
- `C:/Storage/repos/the-way-wt/installer-claude-md/foundations/part_map.md`, `installation` part and `installation-command` surface.
- `C:/Storage/The Brain/The Brain/Notes/Projects/(P) Proces pracy nad produktem/_zadania/instalator_claude_md_z_importem_agents_md.md`, frozen task.
- `C:/Storage/repos/the-way-wt/installer-claude-md/foundations/environment_facts.md`, `claude-code-imports/1` for fenced-code import interpretation.
- `C:/Storage/repos/the-way-wt/installer-claude-md/gate/run_tests.py`, citation and record rules.
- `C:/Storage/repos/the-way-wt/installer-claude-md/installation/test_install.py`, product repository fixture mechanics only.
- `Superpowers 6.4.1 test-driven-development/SKILL.md` and `writing-good-tests.md` in the same directory.

## Cases and production breaks caught

Each test creates a real temporary Git product repository and invokes the installer subprocess with `--apply`; no installer behavior is mocked. Each test method cites `# invariant: installation-claude-guidance/1`.

1. `test_creates_root_claude_import_when_missing`: catches omission of root `CLAUDE.md`, extra or different content, and writing the legacy rule path. It expects exactly `@AGENTS.md` plus the terminating newline.
2. `test_warns_before_confirmation_and_preserves_existing_file_without_import`: catches a missing or late plan warning, changed existing bytes, and writing the legacy rule path. The existing file uses CRLF to expose byte changes.
3. `test_code_fenced_import_mention_still_warns`: catches treating a fenced example as an effective import. The environment fact explicitly says Claude Code skips fenced code blocks.
4. `test_effective_import_needs_no_missing_import_warning_and_is_preserved`: catches a false warning, changed existing bytes, and writing the legacy rule path.

The warning assertions require a warning that identifies `CLAUDE.md` and `@AGENTS.md` before the confirmation prompt; they do not fix its prose. Existing guidance content is only a fixture whose bytes must be preserved.

## Red verification

Command: `python -B gate/run_tests.py installation --record .runs/installation-tests.jsonl`

Exit: `1`. Output: `Ran 21 tests in 51.886s`; `FAILED (failures=4)`. The pre-existing 17 installation tests passed. The four new tests failed for the expected old-installer behavior:

- `test_creates_root_claude_import_when_missing`: root `CLAUDE.md` was not created.
- `test_warns_before_confirmation_and_preserves_existing_file_without_import`: no missing-import warning appeared.
- `test_code_fenced_import_mention_still_warns`: no missing-import warning appeared.
- `test_effective_import_needs_no_missing_import_warning_and_is_preserved`: `.claude/rules/the-way.md` was written.

Record `C:/Storage/repos/the-way-wt/installer-claude-md/.runs/installation-tests.jsonl` contains four `fail` lines, all for `installation-claude-guidance/1`, one per new test. There are no null-citation failures or import/fixture errors. This is the intended red boundary before installer implementation.

## Uncertainty

None affecting this boundary. The test does not assert whether other import syntax beyond the plain active `@AGENTS.md` line is effective; the specified cases cover the import required by the invariant and the documented fenced-code exclusion.
