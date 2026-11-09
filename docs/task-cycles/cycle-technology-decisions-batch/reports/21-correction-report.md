# Correction report: the human's remarks on the open request

**Status:** done
**Commit:** `d3f9eb4` on `task/cycle-technology-decisions-batch` (parent `58cb1f6`), two files, 32 added and 11 removed lines.
**Check:** all five focused checks exit 0; the before/after demonstration in a scratch copy behaves as the finding asks.

Worktree: `the task's worktree root`.

## Method read

- `task-cycle/change/SKILL.md` whole (the make-change skill; variant: a correction for the human's remarks).
- `agent-instructions/README.md` whole.
- Reached beyond the handoff, as the user's global rules require: `a document in the author's private notes` (before writing the scratch driver) and `a document in the author's private notes` (before the commit).
- Read `installation/test_install.py` whole, not only `setUp` and `install`; read `installation/install.py` tail and grepped for `__main__` and `def run`, to place a breaking edit correctly.

## Each remark as made, and how

1. **Item 1** (the no-strike rule also covers the place of the screenshots; a blocked draft is one extra line): accepted as it stands. **No change.**
2. **Item 2** (the two wording corrections of WAY-298 and WAY-322): accepted. **No change.**
3. **Item 3** (the merge before a request opens and WAY-298): decision left as it is. **No change.**
4. **Item 4** (fix the two other installer test files in this request): **done.**
   - `installation/test_coding_guidelines_installation.py`: `setUp` clones the-way into `self.source` in the temporary directory, reads `self.commit` from the clone, sets `self.installer` to the clone's `installation/install.py`, and copies the working tree's `INSTALL` over it. `install()` runs `self.installer` with `--url self.source`. The two other `cwd=SOURCE` reads (the committed-path `cat-file` check and the `git show` of the skill source in the preview test) now run against the clone. `SOURCE` remains only as the clone's source.
   - `installation/test_lead_installation.py`: the same pattern. `self.source = self.root / "source"`. The `cat-file`, `git show` and `rev-parse HEAD^` reads run against the clone; `install()` uses `self.installer` and `--url self.source`.
   - Each test keeps its own assertions. `installation/test_install.py` and `installation/install.py` are untouched.

## Changes

| File | Added | Removed |
|---|---|---|
| `installation/test_coding_guidelines_installation.py` | 16 | 5 |
| `installation/test_lead_installation.py` | 16 | 6 |

Commit `d3f9eb4` added both files by path, message in English.

## Own-work check (make-change section 3)

- **Requirement:** neither test file reads the live head, and neither installs from the live repository. A commit made between `setUp` and the install must fail a test of each file before the fix and pass after it. An uncommitted breaking edit of `install.py` must fail a test of each file after the fix.
- **Check:** scratch copy of the worktree at `a scratch file outside the repository`, outside the worktree. Driver `...\scratchpad\driver.py` runs one test class after its own `setUp`, and in mode `commit` makes an empty commit in the scratch repo at that point. Outputs are `...\scratchpad\out-*.txt`.
- **Result, before the fix** (HEAD test files restored in the scratch copy):
  - `commit` mode: `test_coding_guidelines_installation` FAILED (1 failure, `test_preview_apply_repeat_exposes_the_coding_guidelines_skill_and_preserves_product`); `test_lead_installation` FAILED (3 failures, including `test_preview_apply_repeat_exposes_lead_and_preserves_product`).
  - Plain run: both OK.
  - Breaking edit (`raise SystemExit(3)` inside `run()` in the scratch `install.py`, uncommitted): both FAILED, coding 9 failures, lead 5 failures in the first run — see the caveat below.
- **Result, after the fix** (fixed files copied into the scratch copy):
  - `commit` mode: both OK, exit 0.
  - Plain run: both OK.
  - Breaking edit: both FAILED, exit 1, coding 9 failures and lead 5 failures.
- **Check run in the worktree:** the same two files pass with the real commit as-is (see checks below).
- **Mismatch:** none in the checks. The test-first rule applies in the form that fits: the failing runs are the "before" `commit` runs above, each an assertion failing, not an import or path error.

Commands and exit codes of the key scratch runs (`python -I driver.py <module> <class> <mode>`, exit code captured directly):

| Module | Mode | Exit | Outcome |
|---|---|---|---|
| test_coding_guidelines_installation | commit (before fix) | 1 | FAILED, 1 failure |
| test_lead_installation | commit (before fix) | 1 | FAILED, 3 failures |
| test_coding_guidelines_installation | commit (after fix) | 0 | ok |
| test_lead_installation | commit (after fix) | 0 | ok |
| test_coding_guidelines_installation | breaking edit (after fix) | 1 | FAILED, 9 failures |
| test_lead_installation | breaking edit (after fix) | 1 | FAILED, 5 failures |

Caveat on the breaking-edit "before fix" run: it piped through `tail`, so its exit code is not recorded, but the failing test IDs were printed by the driver and listed above.

**My own error, recorded:** the first breaking-edit attempt appended `raise SystemExit(3)` after the `if __name__ == "__main__":` block, where it never runs. Both files then passed, which proved nothing. I redid it inside `run()`, at line 486 of the scratch copy, and the table above is from that run. The worktree's `installation/install.py` was never touched.

## Checks

Run from the worktree root. Each check with its command and exit code:

| Command | Exit | Result |
|---|---|---|
| `python -B -m unittest discover -s installation -p "test_coding_guidelines_installation.py"` | 0 | Ran 2 tests, OK |
| `python -B -m unittest discover -s installation -p "test_lead_installation.py"` | 0 | Ran 4 tests, OK |
| `python -B -m unittest discover -s installation -p "test_install.py"` | 0 | Ran 30 tests, OK (unchanged file, still passes) |
| `python -B elements/common/foundation_check.py --skip-test-citations` | 0 | 0 errors |
| `git diff --check` | 0 | clean |

No check was skipped.

## Searches not found or unclear

- I did not verify the reviewer's note that "the slice-5 executor reports the same pattern" in these files. I checked the current files directly: both read `self.commit` from the live head in `setUp` and install from the live repository, at the lines the finding names (32 in each). The note on the slice-5 executor itself I did not trace.
- The `task-cycle/change/SKILL.md` path in the handoff is the source; the `.claude/` and `.agents/` copies of `the-way-make-change` exist, and I read only the `task-cycle` source as the handoff names.

## Reaches beyond the handoff

- `a document in the author's private notes`: read before writing the scratch driver, as the user's rules require.
- `a document in the author's private notes`: read before the commit.
- `installation/test_install.py` read whole, and `installation/install.py` tail plus two greps, to place the breaking edit.
- Scratch files outside the worktree: `...\scratchpad\scratch-repo` (a clone of the worktree, with the test files and the breaking edit in it) and `...\scratchpad\driver.py`. Nothing was written to the-way's worktree except the two test files and this report.

## Problems observed

- None in the code under test. The fixed pattern does what the finding asks.
- The wider installer tests use the live `INSTALL` path for the installer file itself; that is intended, because the finding asks that an uncommitted edit of the installer stays under test.
