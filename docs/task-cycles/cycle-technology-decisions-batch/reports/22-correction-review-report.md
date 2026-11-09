PASS d3f9eb4cf1ffe5b9ae43b45001148d64b6ca4e51

# Review of the correction `58cb1f6..d3f9eb4`

Method read: `task-cycle/review/SKILL.md` and `task-cycle/review/fix.md`, whole. `git rev-parse HEAD` is `d3f9eb4cf1ffe5b9ae43b45001148d64b6ca4e51`; `git log 58cb1f6..d3f9eb4` is one commit (`d3f9eb4`); the diff, computed by me, touches two files only. `git status` is clean.

## Counts

Blocking: 0. Minor: 0. Out-of-scope: 1 (note below).

## Each remark as made or not

1. Item 1 (accepted, no change): no change in the range. Made.
2. Item 2 (accepted, no change): no change in the range. Made.
3. Item 3 (left as it is, no change): no change in the range. Made.
4. Item 4 (fix the two other installer test files): made.
   - `installation/test_coding_guidelines_installation.py:30-45`: `setUp` clones `SOURCE` into `Path(temporary.name)/"source"`, asserts the clone succeeded, reads `self.commit` from the clone, sets `self.installer` to the clone's `installation/install.py`, and copies the working tree's `INSTALL` over it (`shutil.copyfile`, line 42). `install()` (line 52-54) runs `self.installer` with `--url self.source`. The `cat-file` check (43) and the `git show` in the preview test (98) run in `self.source`.
   - `installation/test_lead_installation.py:30-43`: same, with `self.source = self.root / "source"`. `install()` (51-53) uses `self.installer` and `self.source`. The `cat-file` (43), the `git show` (128) and `rev-parse HEAD^` (154) run in `self.source`.
   - This is the pattern of `4515b4d` in `test_install.py`: clone in `setUp`, install from the clone, working tree's installer copied over the clone's, even the comment is the same two sentences. A commit during a run changes neither the installed nor the expected commit (both come from the clone); an uncommitted edit of `install.py` stays under test because it is copied in.
   - Each test keeps its own assertions: the diff changes no `assert*` line other than the `cwd` argument of the reads; no test was removed, renamed or weakened. Test counts are 2 and 4, as before.
   - Other reads of the live head in the two files: none. `grep` for `SOURCE`, `INSTALL`, `rev-parse` and `cwd=` in both files shows `SOURCE` only as the clone's source and the `INSTALL` copy source in `setUp`; every `git` call in a test body goes to `self.product`, `self.root`, a clone of the product, or `self.source`.
   - Growth beyond the finding: none. Only the `setUp`, `install()` and three/two `cwd` arguments change, plus the `import shutil`. `installation/test_install.py` and `installation/install.py` are unchanged in the range (`git diff --name-only` for them is empty).

The installer copied into the clone runs with `--url self.source`, and `install.py` pins `HEAD` of its own checkout (`install.py:496`, `cwd=SOURCE` where `SOURCE` is the installer's own parent directory), which is now the clone. So the pinned commit and the test's expected `self.commit` both come from the clone. Consistent.

## Findings

None.

## Out-of-scope note (does not block)

`installation/test_styleguide_installation.py:37-38` and `installation/test_testing_guidelines_installation.py:32-33, 87` read `self.commit` from the live head with `cwd=SOURCE` and install from the live repository: the same race as the finding. Neither file is in the request's range (`git log foundations..HEAD` shows only older, unrelated commits) and neither is among the two files the human's remark names ("the two other installer test files" being the files with the same defect that the whole-change review named). Left for the orchestrator to decide whether to say it to the human.

## Declined to judge

- The two files above with the same pattern (outside the finding and the remarks).
- Whether to keep the clone-based design at its cost (each `setUp` now clones the repository; the two files take about 13-15 s each) — the pattern is the one the human asked for.

## Checks run

| Command (from the worktree root) | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `d3f9eb4cf1ffe5b9ae43b45001148d64b6ca4e51` |
| `python -B -m unittest discover -s installation -p "test_coding_guidelines_installation.py"` | 0 | Ran 2 tests, OK |
| `python -B -m unittest discover -s installation -p "test_lead_installation.py"` | 0 | Ran 4 tests, OK |
| `python -B elements/common/foundation_check.py --skip-test-citations` | 0 | 0 errors |

Not run: a scratch run with a commit made between `setUp` and the install, and with an uncommitted breaking edit of `install.py`. I relied on reading the code against the `4515b4d` pattern; the correction report's own demonstration of both (before and after the fix) is its claim, not re-verified by me. The whole gate was not run, as instructed.

## Reaches beyond the dispatch

- `git show 4515b4d -- installation/test_install.py` and the first 40 lines of `installation/test_install.py`: the pattern the handoff names, read to compare.
- `grep` of `cwd=SOURCE` across `installation/*.py`: to find any other test file reading the live head (basis of the out-of-scope note).
- `git log foundations..HEAD -- <two files>`: to see whether the request touched the two other files.
- `.runs/.../reports/21-correction-report.md`: the report to verify, as named.

## Searches not found or unclear

- The text of the human's remarks: the handoff quotes items 1-4, and I read the correction against that quote, not the request description itself.
- Which two files "the two other installer test files" means is taken from the handoff (coding-guidelines and lead); the existence of two further files with the same race is why the question above is raised.
- Otherwise none.
