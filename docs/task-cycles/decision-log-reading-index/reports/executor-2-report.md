# Executor report: slice 2, "The comparison of a log's entries, and the check on a log with sections"

**Status:** `done`

**Commits** (branch `task/decision-log-reading-index`, from head `30c5b1b`):

| Commit | What |
|---|---|
| `394b7f0` | Add the failing test of the comparison of a log's entries (the test file and an empty script, so the test reaches its assertion) |
| `c85cb59` | Add the script that compares the entries of two copies of a decision log (the script, the rest of its tests) |
| `cea78e5` | Pin the foundation check on a log divided into sections and name the comparison in the part map |

**Files changed** (added / removed lines, against `30c5b1b`):

- `elements/common/compare_log_entries.py`: +189 / −0 (new)
- `elements/common/test_compare_log_entries.py`: +167 / −0 (new, 13 tests)
- `elements/common/test_foundation_check.py`: +17 / −0 (two tests, section "a log divided into topical sections")
- `foundations/part_map.md`: +3 / −2 (the `elements-common` sentence now names the script)
- `elements/common/foundation_check.py`: not changed. The sections test passed on the existing check.

**Check result:** all focused checks pass; nothing failed. The full product gate was not run (by the boundary).

## Checks run

1. First failing test, before the script existed (empty `compare_log_entries.py`):
   `python -B -m unittest discover -s elements/common -p test_compare_log_entries.py` gave exit 1, `AssertionError: 0 != 1`, on `test_entry_whose_text_differs_is_reported_with_its_first_line`. The script reported nothing and exited 0, so the assertion failed for the expected reason.
2. `python -B -m unittest discover -s elements/common -p test_compare_log_entries.py`: exit 0, 13 tests OK (after the script was written and after the report-count fix).
3. `python -B -m unittest discover -s elements/common -p test_foundation_check.py`: exit 0, 183 tests OK, run in background (about 197 s), including `test_log_divided_into_sections_passes_as_the_undivided_one_does` and `test_error_in_an_entry_of_the_second_section_is_reported_at_its_own_line`. Both passed on the existing `foundation_check.py`; no change to that file was needed.
4. Division check: `git show dae85e1:foundations/decisions.md` to a scratch `before.md`, `git show 104e126:foundations/decisions.md` to `after.md`, then `python -B elements/common/compare_log_entries.py before.md after.md`: exit 0, output `Compared 198 entries of ... with 198 of ...: all the same byte for byte.`
5. `python -B elements/common/foundation_check.py .` on the worktree after the part-map edit: exit 0, `0 errors`.
6. Mutation (own-work, heading left out of the block, in a scratch copy): tests `test_entry_whose_heading_differs_is_reported_at_its_heading` and `test_line_ending_is_a_byte_that_differs` failed (`FAILED (failures=2)`). Restored; the scratch copy was removed.

## Own-work check (section 3)

- Requirement: an entry is compared byte for byte, its heading included, and a changed entry is reported with its first differing line. Check: on the real log, I changed one word in WAY-05's body in a scratch copy and one row of the withdrawn block in another. Result: the script reported `WAY-05 differs: ... line 172 ... line 618` and `## Withdrawn identifiers differs: ... line 9100 ... line 9239`, both exit 1. The unchanged division comparison exits 0.
- Finding during this check: the count said "3 reports" for one difference, because the two indented lines were counted as reports. Fixed (each difference is one report now); the test asserts `1 report.`. This was a real bug, which I found by running the script, not by a failing test.
- Finding while writing the script: the first version left the heading out of each block, so a changed question in an entry heading was not compared. Fixed by including the heading as the block's first line. Caught by my own reading, then pinned by `test_entry_whose_heading_differs_is_reported_at_its_heading`, and confirmed by the mutation above.
- Requirement: the withdrawn block is compared the same way. Check: the mutated withdrawn copy above reports it.
- Test order: the first test was seen failing as the slice requires. The other twelve tests were written after the script, so they were not seen failing first. The mutation run is the evidence that they catch breaks.

## Reaches beyond the dispatch

- `foundations/decisions.md` was read whole-passage only where the dispatch named it: WAY-18, WAY-07, WAY-38, WAY-344 by line range, and the tasks' "To do" and question 3 passages. No reach beyond those.
- The sibling `elements/common/decision_index.py` was read whole, and `test_decision_index.py` lines 1–60, for house style.
- `foundation_check.py` and `migrate_foundation.py` were read in full, not just the named ranges, to satisfy "every file you change, whole" for `test_foundation_check.py`.
- `foundations/part_map.md` was read whole before the edit; `test_foundation_check.py` whole before the edit.

## Choices made

- The script treats only `### PREFIX-NN — ` headings as entries (the same prefix form `foundation_check.py` reads: uppercase prefix, digits, em dash). A `###` heading of another form (for example an earlier versioned form `### ABC-01/2 — `) is not an entry, and its block is not compared. Cost if wrong: an earlier-form heading in a copy would be silently skipped. The foundation check already reports that form as an error, so the gap is covered elsewhere.
- A heading is a line starting with 1–6 `#` followed by a space or end of line (Markdown); `foundation_check.py` uses `startswith("#")`. Cost: a line such as `#tag` is not a heading here but is one there. The log has none.
- Line endings are compared as bytes, so a CRLF copy differs from an LF copy in every line. This is what "byte for byte" says. Cost: a product whose two copies differ only in line endings gets exit 1; the test pins this.
- A copy with an entry-less body or only the withdrawn block exits 2 (WAY-344). The message names the file and the missing entry heading.
- The identifier listing puts the first copy's identifiers first, then those only in the second, so the order is stable.
- Output on success is one summary line; on failure, one report per entry, then `N report(s).`

## Working copies

- `.runs/executor-2/before.md` and `after.md` (git-show copies of `dae85e1` and `104e126`), plus two altered copies `after_mut_entry.md` and `after_mut_withdrawn.md`: removed by `rm -f`; the directory `.runs/executor-2/` is empty now.
- `.runs/executor-2/mut/` (heading mutation copy): removed.
- No git worktree was made. The tests' temporary directories are written by the tests themselves and are outside this rule.

## Unread material

- `.runs/task-cycles/decision-log-reading-index/task.md` lines 33–42 and 67–72: read as the dispatch copies them; I did not open the rest of the task file.
- `.runs/task-cycles/decision-log-reading-index/plan.md`: not opened. The slice text is copied in the handoff, which the method says is the source.
- `elements/common/test_decision_index.py` lines 61–324: not read (only the header for style).
- `foundations/decisions.md`: only the passages above; the other 9,000 lines were not read.
- `elements/common/migrate_foundation.py`: read in part only (lines 120–165 in the window I printed), as the dispatch's range 133–150 asks.

## Searches not found or unclear

- `git show` of `104e126` and `dae85e1`: `104e126`'s parent is `dae85e1`, as the foundation report says; the handoff's "commit before the division" was not stated explicitly, so I used the report's `dae85e1`.
- The handoff asks the executor to write the checks' output "for the request" in the report; the division output above is it.
- The plan's Read paths for `plan.md` were not checked against the handoff's slice copy (I used the handoff copy).

## Problems observed

- None in the repository's own checks. The foundation check test file takes about 197 s, which is slower than a focused check would be; this is the existing suite, not something this slice added.
