# Fix report — worktrees removed after merge

**Status:** done

Range of the fix: from the reviewed head `a849408fade7f5454a2a1535fc14ee364a0fa7bf`.

| Commit | What |
|---|---|
| `1f27200` | Script and tests: I1, M1, M2, M4, M5 |
| `b8a16cc` | WAY-375: M3 |

Files: `task-cycle/remove_merged_worktrees.py`, `task-cycle/test_remove_merged_worktrees.py`,
`foundations/decisions.md`.

## Findings, one by one

- **I1 (blocking), fixed.** `inspect_state` passes `--ignore-submodules=none` to `git status`, as git's own check in
  `git worktree remove` does. Docstring says so. The `--force` retry stays, now behind the stricter status.
  Test `test_a_change_in_a_submodule_that_the_configuration_hides_keeps_the_directory`: a product-like
  repository whose `.gitmodules` declares `ignore = all`, a populated submodule with a changed tracked file and
  a new file; it asserts that plain `git status --porcelain` is empty and the strict one is not, then that
  `--apply` keeps the directory ("uncommitted changes") and the new file survives.
- **M1, fixed.** The retry now looks for git's sentence `working trees containing submodules cannot be moved or
  removed` (constant `SUBMODULE_REFUSAL`), not the word "submodule". Test
  `RefusalTest.test_only_gits_sentence_about_submodules_makes_the_removal_forced`: git replaced by a made-up
  refusal for changed files whose path holds `submodule`; one call only, no `--force`.
- **M2, fixed.** The fetch is `git fetch --no-tags --no-prune <remote>`; docstring says no setting of
  `fetch.prune` can take away a ref. The test now sets `fetch.prune true` in the repository's configuration.
- **M3, fixed.** WAY-375's first paragraph now says: the tree is clean as git's own check for removing a
  checkout reads it; a cycle's directory stands on a branch whose name begins with `task/` or whose directory
  holds the record of a cycle, or is a detached copy of a base made for a check; and a detached checkout nested
  in a removed directory goes with it, whatever its name, only where it is clean and on the remote, else the
  holding directory stays. Still three sentences; the `decision:` quotations of the tests still match.
- **M4, fixed.** The reason is the fixed text `git cannot read its state`. Test
  `RefusalTest.test_a_reason_for_the_list_never_holds_what_git_says_of_a_path`: git replaced by a failing call
  whose message names a path; the reason holds none of it.
- **M5, fixed.** Added `test_a_listed_path_that_is_a_junction_is_kept` (a merged directory replaced by a junction
  made with `_winapi.CreateJunction`, a standard-library module; skipped with a reason where it is missing or
  the junction cannot be made; it ran here, not skipped) and the test of I1 above.

No finding held wrong.

## Checks (command, exit code)

| Command | Exit | Result |
|---|---|---|
| `python -B -m unittest task-cycle.test_remove_merged_worktrees` | 0 | 46 tests OK |
| `python -B gate/run_tests.py task-cycle` | 0 | 440 tests OK |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |

Not run: the full gate (the orchestrator's).

## Own-work check (WAY-164)

- **Requirement most likely unmet:** the reviewer's I1, that a removal never takes uncommitted work of a
  populated submodule, and that each new test fails on the break it names.
- **Check:** five mutations of the script, each applied alone with the named tests run, the script restored
  after (throwaway driver, removed): status without `--ignore-submodules=none`; the fetch without `--no-prune`;
  the retry on the word "submodule" anywhere; the git message put back in the reason; the junction not read in
  `is_link`.
- **Showed:** all five caught by the test written for them (exit non-zero each); the script is back to the
  committed text (`git diff` empty after). A read-only dry run on the real repository of the-way
  (`--no-fetch`, exit 0) still marks the same 88 directories `remove`; nothing was applied there.

## Reaches beyond the dispatch

None beyond the handoff's reading of `reports/fix-findings.md` and `reports/fix-handoff.md`; I did not open
`reports/review-whole-report.md` and its driver, since the findings gave the evidence.

## Unread material

- `reports/review-whole-report.md` and `reports/review-whole-submodule-check.py`: not read; the findings file
  holds the evidence and I wrote my own test of I1.

## Searches not found or unclear

- none

## Working copies

- `.runs/author/` of the worktree (the fix scripts, the mutation driver, the outputs of the checks): removed with
  `rm -rf` before the commit; `git worktree list` holds the same 96 entries as before. Remainder: none.
- The tests' temporary repositories live in the system's temporary directory and are removed by the tests.
