PASS 116f31921ab646dc827db191606c70814ef7763e

# Review of the fix of slice 3 (`9285a74..116f319`)

Method: `task-cycle/review/fix.md` with `task-cycle/review/SKILL.md` section 2. `git rev-parse HEAD` in
`the worktree of the task` is `116f31921ab646dc827db191606c70814ef7763e`, as given. The range holds one
commit (`116f319`), changing `process-audit/audit_count.py` (+46 −17) and `process-audit/test_audit_count.py` (+88 −7). The reviewed
worktree, its index and its branch were not changed (`git status --short` empty after all runs); every run was made in a separate
detached worktree of the head commit, removed at the end.

Counts: **0 blocking**, **1 Minor**, **0 out of scope**.

## The three blocking findings

### 1. Crafted header line and long continuation (`audit_count.py`) — fixed

The pattern `HEADER_FIELD` is gone. `header_field` (`audit_count.py`, new) cuts the line at the first colon with `str.partition`
and strips blanks: one pass, no backtracking. `header_fields` collects the continuation lines of a value in a list and joins once.
The semantics for lines the old pattern read are the same (marker `-` plus a blank, label up to the first colon, empty label
refused); the only difference is that blanks around the label are now dropped, which is more lenient and harmless.

Evidence on the new head, `process_pin` + `remarks_count` on a record of the 4 MiB limit, each shape run by my own harness:

| shape | time |
|---|---|
| `- ` + 4 MiB of blanks + `x` (the finding's case; was 13.6 s at 40 KB) | 0.04 s |
| `-` + blanks only | 0.04 s |
| `- Process pin: a` + 1.4 million lines ` x` (was 37 s at 400,000 lines) | 0.74 s |
| 600,000 header lines `- a: b` | 0.64 s |
| 4 MiB of colons after the label | 0.16 s |
| 2 million lines of one blank in a header continuation | 0.72 s |
| 4 MiB hex run with and without a digit; `moved to ` repeated 460,000 times | 0.08–0.14 s |
| remarks item with 700,000 entries; one 4 MiB entry line of blanks; a heading-like line of ` #` repeated | 0.01–0.67 s |

All are linear in the record. The two new tests (`test_a_header_line_of_blanks_does_not_stall_the_count`,
`test_a_long_continuation_of_a_header_line_does_not_stall_the_count`) fail by timeout on the old shape and pass; they assert the
real pin is still read after the crafted line.

### 2. Backslash before a bar breaks out of a cell (`cell`) — fixed

`cell` now writes each `|` as the text `\x7c` after `display`, so no cell holds a bar at all, whichever way a reader treats `\\|`. I
checked the choice rather than the test alone: five repositories whose folders (and keys) were `x\|none\|7777777\|99`, `ends\`,
`a||b|`, `\\|\\|`, `` `tick` <b>* `` and a name with U+2028, U+0085 and a bar, and a key `k0|\`, were counted by the command; every
row of *Repositories*, *Cycles* and *Unknown values* has the width of its header (3, 9, 4) both when split by a GFM-style
tokenizer that honours backslash escapes and when counted by bars (4, 10, 5), and no line of a section is outside the table. The
test `test_a_backslash_before_a_bar_stays_inside_its_cell` checks both counts on the finding's own folder; the helper `rows` now uses
`split_row`, which honours the escape, so the earlier hiding of the defect by `(?<!\\)\|` is gone. The cost the executor names (a
folder with a literal `\x7c` reads the same as one with a bar) is the cost `display` already has for control characters.

### 3. Out-of-range committer date aborts the run — fixed

The timestamp is kept as git's text and converted by `committed_date`, which catches `OSError`, `OverflowError` and `ValueError` and
returns `None`; the cycle then has *Committed* `unknown`, a row in *Unknown values*, and every other cycle and repository is read.
Evidence: a raw commit dated `18446744073709551615` (a value other than the finding's `99999999999999`) adding a record gives exit 0,
stdout `Wrote … 1 cycles in 1 of 1 repositories.`, the row with *Committed* `unknown` and the real pin, and the *Unknown values* row
"the commit's date lies outside the years the command can read". The test
`test_a_commit_dated_beyond_the_readable_years_leaves_its_date_unknown` uses `99999999999999`, a second ordinary repository and a
raw object written with `hash-object --literally`; the executor reports it failing on `9285a74` with a traceback, and the finding's own
reproduction is the same case. A non-numeric stamp takes the same path. The row sorts as the text `unknown` among the dates, which is
deterministic.

## What the fix itself changed (hostile input in the diff)

- `header_field` / `header_fields`: no pattern is left in the header cut; the remaining patterns on record text (`COMMIT`,
  `MOVED_PIN`, `REMARKS_OPENER`, and `HEADING`/`MARKER` of `remarks_check`) were measured above at the limit and are linear. The joined
  value is built once; its size is bounded by the file size, itself bounded by `MAX_BYTES`.
- `cell`: the only change is the bar; control characters, line breaks and Unicode line separators are still folded or escaped before
  it. No new characters reach the result beyond ASCII `\x7c`.
- `committed_date`: takes only the text git prints for `%ct`; no new subprocess, no new path, no new import (`script-subprocesses`,
  `script-imports` unaffected).
- The test helpers (`commit_dated`, `split_row`, `timeout` in `run_count`) run only on temporary repositories and directories. The
  `re` import was removed with its only use.
- No new Critical or Important finding in the diff.

## Minor findings

### M-new. The module docstring says each control character and each bar is written `\x..`, while a bar is written `\x7c`

`audit_count.py`, module docstring (new text in the sentence about the untrusted input): "with each control character and each bar
written as `\\x..`" — in the docstring's non-raw string this reads as `\x..`, which is accurate for the form but does not tell a
reader that a literal bar and the text `\x7c` come out the same. The executor names the ambiguity in the fix report; the file does not
say it. Polish, blocks nothing.

The three Minor findings of the first review (M1 a very large integer in the locations file, M2 inherited `GIT_*` environment and
`log.showSignature`, M3 the results guard not covering the-way's checkout) are untouched by the fix and still stand; they are not in
the findings file and block nothing.

## Declined to judge

none (nothing was set aside as outside the task in this review; the two lines of the first review stand as they were).

## Checks run

| Command | Exit code | Result |
|---|---|---|
| `git rev-parse HEAD` (reviewed worktree) | 0 | `116f31921ab646dc827db191606c70814ef7763e` |
| `python -B gate/run_tests.py process-audit` (detached worktree of `116f319`) | 0 | 47 tests OK in 32 s |
| `python -B gate/run_tests.py elements/part-map` | 0 | OK |
| `python -B elements/common/foundation_check.py` | 0 | no errors |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 | 278 files, 0 listed |
| the command on this repository, temporary locations file and results directory, stdin closed | 0 | `Wrote count-2026-11-11.md and count-latest.md: 69 cycles in 1 of 1 repositories.` |
| scratch probes in the session scratchpad (`probe6.py` timing at the limit; `probe7.py` cells of five hostile folders and keys through the command, and the `18446744073709551615` date) | 0 each | results above |

Not run: the full suite (the cycle's own run). Not re-run on the old head: the tests' failure on `9285a74`, which I take from the
fix report; my own reproductions of findings 1–3 on the old head stand in the first review's report.

## Reaches beyond the dispatch

none beyond the files the coordinator named, the method file `task-cycle/review/fix.md` and `task-cycle/review/SKILL.md` section 2.

## Unread material

- `.runs/task-cycles/weekly-process-audit/reports/review_slice3_findings.md`: read whole up to the end of finding 3; it holds nothing
  after it that I did not see.
- The slice's foundation entries were not re-read for this review: the fix does not touch the part map, the foundation or the
  trust-boundary pattern; they were read for the first review.

## Searches not found or unclear

none
