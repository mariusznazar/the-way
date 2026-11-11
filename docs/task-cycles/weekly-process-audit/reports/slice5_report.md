# Slice 5 report: problems and issues from the register

**Status:** done with concerns

**Commit:** `c2a0169` (Count the problems of the register against the cycles), on `task/weekly-process-audit`, base `9cf2633`.

The first session was lost in a crash after the code was written but before the tests ran, the report was written, or anything was committed. The work was resumed from the uncommitted tree; the saved copy matched what the session had reached.

**Files changed** (`git show --numstat c2a0169`):

| File | Added | Removed |
|---|---|---|
| `process-audit/audit_count.py` | 514 | 17 |
| `process-audit/test_audit_count.py` | 262 | 1 |

## What was done

- `audit_count.py` reads the register at the entry `problem_register` under `the-way`, in the four tables of `process-audit/problem_register.md` (*Classes*, *Weights*, *Issues*, *Problems*), found by heading and header row.
- Per cycle: problems by class and weight, a problem counted once by its row (WAY-333). A cycle copied again after a correction is one cycle. Result section `## Problems by cycle`.
- Per fixed issue: problems in cycles whose *Process pin* holds the fix, apart from those whose pin lacks it, never by date (WAY-334). Section `## Fixed issues`.
- Per open issue: the cycles it came back in, the problems, the problems whose cycle is not read, and the days waited. Section `## Open issues`. Issues are listed in register order, never ranked (WAY-335).
- Dropped issues counted apart, with no waiting. Section `## Dropped issues`.
- Refused rows and tables, and values with no cycle, are `unknown` with a reason in `## Unknown values`.
- New option `--today YYYY-MM-DD`; default today in UTC.
- Git additionally runs `merge-base --is-ancestor` and `rev-parse` (`--disambiguate`, `--verify`) in the-way checkout; the docstring says so.

**Which repository answers whether a pin holds a fix:** the checkout of the-way, which is the entry `repository` under `the-way`, or this script's own checkout where that entry is missing (`the_way_checkout`). Git answers with `merge-base --is-ancestor <fix> <pin>` there.

**From what date the days of waiting count:** from the commit date (UTC, `YYYY-MM-DD`) of the earliest cycle the issue's problems stand in, to the `--today` day. The commit date is the *Committed* column of that cycle, the first commit that adds its record.

## Checks

| Command | Exit code | Result |
|---|---|---|
| `python -B -m unittest test_audit_count.RegisterCount` (in `process-audit/`), before the code, after the `--today` option was missing | 1 | 11 of 12 failing; the failures stop at `unrecognized arguments: --today`, i.e. at the feature, not at a missing module |
| same, after the code | 1 | 2 failing: one assertion text in my test (`` `Issues` `` vs the message's `## Issues`), one unknown row copying an uncapped 200,000-character repository name; both fixed (the cap applied in `analyse`) |
| same, after the fixes | 0 | 12 tests OK |
| same, after a test for a class named in two rows was added | 0 | 13 tests OK |
| `python -B gate/run_tests.py process-audit` | 0 | 85 tests OK (368 s) |
| `python -B -m py_compile process-audit/audit_count.py process-audit/test_audit_count.py` | 0 | ok |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 | checked 279 files, 0 listed |
| `python -B elements/common/foundation_check.py --skip-test-citations` | 0 | 0 errors |
| run on this repository, stdin closed: `python -B process-audit/audit_count.py --locations <scratchpad>\run5\locations.json --today 2026-11-11 <&-` | 0 | `Wrote count-2026-11-11.md and count-latest.md: 71 cycles in 1 of 1 repositories.` Temporary register: one issue of each fate and one problem row of each kind, plus a row naming an unread key. Fixed issue `fixed-demo` (fix `b43558a`): 0 holding, 1 lacking; `git merge-base --is-ancestor b43558a c64a6071…` exits 1, as counted. Open issue `open-demo`: 34 days (cycle dated 2026-10-08). The unread row is `unknown`: "no named repository holds the cycle". |

Mutations, each made by hand in the worktree, run on its single test, and reverted (file compared byte for byte with the saved copy):

- ancestry arguments swapped: `test_a_fixed_issue_counts_apart...` exit 1.
- duplicate-name check disabled: `test_a_class_named_in_two_rows...` exit 1.
- open issues sorted by return count: `test_open_issues_are_listed_in_the_register_order...` exit 1.

## Own-work check (WAY-164)

- **Requirement most likely unmet:** a crafted register (malformed rows, a 200,000-character cell, a long run of blanks) makes the run abort, or puts an unchecked text into the result, or gives a count that looks measured when it is not.
- **Check:** the crafted tests `test_crafted_rows_of_the_register_are_refused_with_a_reason_and_the_rest_counted`, `test_a_long_run_of_blanks_in_a_class_name_does_not_stall_the_count` (60 s limit), `test_a_class_named_in_two_rows_refuses_both_and_its_problems_with_it`, `test_a_register_larger_than_the_cap_stops_the_run_with_nothing_written`, and the missing-table test; the stdin run above.
- **What it showed:** each refused row gives its value and reason, nothing aborts, control characters do not reach the output, text copied into the result is capped at 200 characters, the oversized register stops with exit 2 and nothing written. The fixed-issue and open-issue figures agree with git and with hand arithmetic.

## Choices made (the way rejected, and the cost if wrong)

1. **A missing table is an error of the register with exit 1** (result written, `Error:` on stderr). I read "exit 2 only where the register itself cannot be read at all" as covering only unreadable, oversized and non-UTF-8 files. Rejected: exit 2 with nothing written. Cost if wrong: one exit code changes.
2. **Days waiting is `unknown` where any of the issue's problems has a cycle no named repository holds**, because the earliest date would then be unknown. Rejected: the earliest known date. Cost if wrong: a figure that is too low is avoided, at the price of more `unknown`.
3. **An open issue with no problem yet shows `—`** for days, not `unknown`, and no unknown row. Cost if wrong: none seen.
4. **Fixed issues count problems, not cycles.** Cost: a cycle with two problems of one issue counts twice. The "Cycles" figure for open issues counts distinct cycles.
5. **A fix missing from the-way's history makes both holding columns `unknown`**; problems of cycles with a known pin are then counted under nothing else. Rejected: counting them as lacking. Cost if wrong: none.
6. **A shallow clone of the-way turns a "lacks" answer into `unknown`**, since the history may lack the commit. Cost: more `unknown` in a shallow checkout only.
7. **Withdrawn classes stay valid for problems**, as the template says earlier problems stay readable.
8. **The *Weights* table must name the four levels, each once**, else a register error. Rejected: no check of the table. Cost: none seen.
9. **The dated file name uses the `--today` day, which defaults to the UTC day**, where before it used the local `date.today()`. This is one changed behaviour outside the new code; it makes the file name and the days agree.
10. **The-way's checkout is resolved on every run**, so a wrong `repository` entry under `the-way` now stops the run with exit 2 even when that key is not named. Rejected: resolving it only when named (the ancestry check needs it on every run that has fixed issues).
11. **Test fixture:** `AuditCountCase.setUp` now writes the real template as the register (it was a placeholder line). Without this every existing test would hit the missing-table error.
12. **Short-hash resolution:** `rev-parse --disambiguate` lists every match; zero is "lacks", more than one is "ambiguous" (unknown), and the single match must be a commit (`^{commit}`). Rejected: `--verify` alone, which cannot tell ambiguity from absence.

## Questions

None blocking.

## Concerns

- **The ambiguous short-hash branch is not tested.** I could not construct a real 7-character collision cheaply. The code path returns `unknown` with its reason, but no test exercises it.
- **Columns of the result that depend on untested paths:** the "not read" column of *Open issues* and *Fixed issues* is covered only by the stdin run, not by a unit test with a missing repository other than the `ghost` key test.
- The full suite (WAY-160) was not run; the gate of `process-audit` was run instead, as the handoff's *Checks* name it.
- The stdin run's count (71 cycles) is higher than slice 3's 69, because the-way has more cycles now, not because of this slice.
- The `Process pin` of a product cycle must be a commit of the-way for the holding answer; a product pin that is a commit of the product, not of the-way, gives `unknown` ("the-way's history lacks commit"). Expected, but worth knowing when the first real product cycles are counted.

## Reaches beyond the handoff

- `remarks_check.py` functions used by the register reader (`split_lines`, `fenced_flags`, `display`) were used as already used by the price list; I did not read `task-cycle/remarks_check.py` whole in this session.
- `git` probes in the worktree: `rev-parse --disambiguate`, `merge-base --is-ancestor` exit codes (0, 1, and 128 for a missing commit), `rev-parse --is-shallow-repository`.
- The stdin run's register is a temporary copy of the template with demo rows, in the scratchpad (`run5`); nothing was written to the user's real places.

## Unread material

- `.runs/task-cycles/weekly-process-audit/plan.md`: not read, as the handoff says; the rows named by the slice are copied in the handoff.
- `task-cycle/remarks_check.py`: used through its names only (see Reaches).
- Everything else the handoff names was read: `task.md` passages, `foundations/decisions.md` WAY-38, 48, 89, 320, 329 to 336, `foundations/invariants.md` script-language, script-imports and script-subprocesses, `task-cycle/record_template.md` lines 1 to 15, the reports slice3, slice3_fix, slice4 and correction, `audit_count.py` and `test_audit_count.py` whole, and `task-cycle/change/SKILL.md` and `slice.md` whole.

## Searches not found or unclear

- Whether the-way's own cycles all carry a *Process pin* that is a commit of the-way: in the stdin run the-way cycles resolved, but I did not check each of the 71.
- How git reports a short hash that matches both a commit and a blob: `--disambiguate` lists both and the code returns `unknown`; not verified against a real repository.
