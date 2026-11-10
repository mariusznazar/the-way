# Report 07 — the fix of the two blocking findings of the return step's review

**Status:** done. **Commit:** the one commit on top of `3057f16` named at the end.

## Findings as fixed

1. **Surface drops "in a Markdown file".** Right: the code lists note links only in a file whose
   name ends in `.md`. Fixed in `foundations/part_map.md` (`tracked-private-paths-command`): "for
   absolute paths, and for note links in Markdown files, and skips ...". The rest of the entry is
   unchanged.
2. **README restates the promise differently.** Right: the README said "name, argument and exit
   codes", the surface says path, argument, the meaning of the backticked texts and exit codes.
   Fixed in `installation/README.md`: "the command keeps its path, its argument, the meaning of the
   backticked texts of the sentence and its exit codes (the surface `tracked-private-paths-command`
   of the-way's part map), and its functions are not promised."

Making the accounts alike: I searched with `git grep -n "tracked_private_paths_check\|tracked-private-paths-command"`
(without the test files). Places found: the surface (fixed); the README section (fixed; its test
example names the path, which is now promised); `task-cycle/private_paths_check.py:35` and the
docstring of the command (both already say "a link only in a Markdown file", no promise restated);
WAY-324 (names no kind of hit, and its third sentence on backticked texts agrees with the surface);
the invariant (already "in a Markdown file"). One more place differed: the opening of the README
section said "a link to a private note" without the qualification; changed to "or, in a Markdown
file, a link to a private note". Only line wrapping was changed otherwise.

## Checks

| Command | Exit code |
|---|---|
| `python -B elements/common/foundation_check.py` | 0, 0 errors |
| `python -B gate/run_tests.py elements/part-map` | 0, OK |
| `python -B gate/run_tests.py installation` | 0, 44 tests OK |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` (the edited files are tracked) | 0, 275 files, 0 listed |
| whole gate | not run (the orchestrator runs it) |

## Own-work check

- Requirement most likely missed: that every account of the promise reads alike. Check: the grep
  above plus a read of the four accounts side by side (surface, README closing paragraph, WAY-324
  third sentence, invariant sentence): all give Markdown-only note links, and the surface and the
  README give the same four promised things. No further difference found.

## Reaches beyond the handoff

none

## Searches not found or unclear

none

The Minor finding of the review of the fix (the README, UTF-16 file) was not touched.
