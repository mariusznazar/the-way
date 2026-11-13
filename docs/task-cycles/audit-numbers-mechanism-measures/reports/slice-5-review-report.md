PASS 0e75a4b4c7a23e0200a4d5762543b8701f2bbb9b

# Review of slice 5 (range `8a8f636..0e75a4b`, one commit)

`git rev-parse HEAD` is `0e75a4b4c7a23e0200a4d5762543b8701f2bbb9b`, the head given. Nothing in the reviewed worktree was
changed (`git status --short` empty before and after).

Changed files (from `git diff --stat 8a8f636..0e75a4b`):
- `process-audit/audit_count.py`: +236 −46 by `git diff --numstat`
- `process-audit/test_audit_count.py`: +324 −9 by `git diff --numstat`

## Findings

### Critical
none

### Important
none

### Minor
1. `process-audit/audit_count.py:197-199` — the docstring line `result and in an `Error:` line on stderr; 2 with `Error: <message>` on stderr and nothing written, when an argument is wrong, the`
   is 129 characters; the rewrite of the exit-code paragraph left the next line unwrapped. Three other new lines run to 101 to
   104 characters (`audit_count.py:126`, `:273`, `:1188`), where the file otherwise keeps to about 100. Effect: polish only.
2. `process-audit/audit_count.py:2420-2426` (`main`, the loop over `lacking`) with the test
   `test_a_file_with_neither_the_section_nor_the_table_misses_both` — a file with neither the heading nor a `Model` table gives
   two `Error:` lines, one per field. The slice says in one place "the `Error:` line names both" and in another "one `Error:`
   ... `<field>`" per missing field; WAY-344 asks for "a line `Error:` that names the file and the field". Both readings are
   defensible; the per-field one keeps one format for every field and is tested. Not blocking; if one line naming both was
   meant, it is a small change in `main` and in that test.
3. Unknown-values rows: every missing field of a table puts the same reason twice (once for `Cost`, once for `Fix rounds share`)
   (`audit_count.py:1218-1225`). A file missing three columns of the older table gives six rows. Longer table only; the list is
   capped at 500 rows elsewhere. Fine as is.

### Outside the task's scope
- `process-audit/SKILL.md:143-145` still says a `stages.md` without the section gives no cost (and the working-time lines
  give no times). Stale after this slice; the handoff says slice 8 carries it. Not a finding of this range.

## What I checked against the task and the foundation

- Newer form read as before: `section_table` keeps the earlier checks (header exactly `STAGE_COLUMNS` or plus `Files named`,
  cell counts, token counts). `priced` now calls the new `cost_at`, the same formula. A diff read confirms no change of
  arithmetic.
- Older form: `older_table` finds the table whose header row's first cell is `Model`, outside fences, not directly under another
  table row, exactly once; twice gives the reason `holds the table of tokens by model more than once` with no field missing
  (no `Error:`). Header must equal the five columns in order; the rows are priced by `priced_older`: a model `unknown`, cached
  above input, no price (a `None` price counts as none) and a non-number count (also in `Total tokens`) give unknown with a
  reason. Share is `unknown` with the reason `OLDER_NO_TURNS`; the number of rounds is still read from the record
  (`add_cost`, the `if table.older: return` after `cycle.rounds`). WAY-352 verification: cost known, share unknown with the
  reason, never `0.0%`, same price list: met.
- Missing fields (WAY-344 and settlement 6): newer form's eight columns and the table itself under a heading; `Files named`
  never missing; older form's `Input`, `Cached input`, `Output`; neither sign gives both the section and the table; one time
  line without the other gives the other; neither time line is the earlier form with no error; other order or another column
  beside them misses none and is refused with a reason. The field names are constants of the script, so no text of the file
  reaches the `Error:` line except the key and the folder, which `main` cuts to `TEXT_CAP` and passes through `display`
  (control characters escaped); the result's own cells go through `cell` (bars to `\x7c`). Exit code 1 added to the `main` return
  after the result is written. Missing `stages.md` file, a file that is no regular file, too large or not UTF-8 are not
  "fields" and stay unknown with exit 0: consistent with WAY-344's wording (a field is "a named thing the script looks for
  in the file") and with the slice, but see Declined to judge.
- The reading of `stages.md` is reworked, so every field is under the check: the only readings of `stages.md` in the module are
  `stages_time` (two lines) and `stage_table` (two forms); the other stage-based reading (`fix_rounds_share`) looks at cells of
  rows, not at a named field.
- Series: `git diff 2292f334… HEAD -- process-audit/audit_count.py` has no line that mentions `TREE_PATHS`; `git diff --quiet
  … -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` exits 0. The new
  `ProcessVersions` test puts a change of `task-cycle/cycle_measures.py` and then of `task-cycle/gate_times.py` between v1 to
  v3 (one series, older form) and a change of `task-cycle/cycle_stages.py` before v4 (new series): it would fail if either
  script were added to `TREE_PATHS` (the executor's mutation claim is plausible from the structure; I did not run the
  mutation).
- Tests: they assert values computed by hand (0.010650, 0.008000), stderr lines compared as whole strings, exit code, the
  `Unknown values` rows and the result written. Tests for the three readings the slice names (newer table, older table, time
  lines) each give the file without a field and assert exit 1. The changed fixtures of `Times` append an older table so the
  file is not missing the section; that choice is reasonable.
- Trust boundary, crafted input (probe in the scratchpad, `python -I`, imports of the module under review only):
  - 200,000-row older table: 1.6 s, priced; token counts capped at 15 digits (`token_count`); costs above the ceiling
    handled by the existing check; copy size capped by `MAX_BYTES` before reading.
  - 100,000 lines `| Model |` glued (one table start) and the same separated by blank lines (100,000 starts): 0.2 s each; the
    second gives "more than once" with no error, the first gives a missing-column result. No quadratic path.
  - A body row whose model is `Model`, an escaped bar in a model name, a bare `|` row, an empty-cell header, a heading with no
    table: all give a reason or a field, none raises.
  - Missing and renamed fields: tested (every column of the newer table, the three of the older table, the renamed `Start`).
  - Control characters and bars: the folder test (`x|`, 300 characters, `\x1b[2J`) asserts the stderr and the result hold
    only printable characters; model names in reasons are cut to `TEXT_CAP` before `cell` escapes them, as in the newer path.
  - Malformed JSON lines: not touched by this slice (no JSON read).
- The author's own-work check: the real-history run (75 cycles, 73 with a cost, no `Error:`) is the check that fits the
  weakest requirement. I did not repeat it; I ran the focused tests instead.

## Declined to judge
- A cycle whose `stages.md` is absent from the copy, is no regular file, is too large or is not UTF-8 gives unknown and exit
  0, no `Error:`: the task's text speaks of a field missing in a report; I take a missing file as not a field. Whether it
  should also end with exit 1 is a decision for WAY-344 / row 6, not for this slice.
- `process-audit/SKILL.md` (stale text): slice 8.
- The product repositories of the author were not read by the executor (real-history run was the-way only); I did not read
  them either. The task's context states every report in both repositories' history has the table once.

## Checks I ran
| Check | Command | Exit |
|---|---|---|
| Focused tests of the slice | `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Cost -k Times -k StagesForms -k ProcessVersions` | 0 (71 tests OK, 105 s) |
| No changed line mentions `TREE_PATHS` | `git diff 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- process-audit/audit_count.py \| grep -c TREE_PATHS` | the count is 0 (grep exit 1 by its own rule); `TREE_PATHS` at `audit_count.py:301-302` is unchanged text |
| Reviewed task-cycle files untouched | `git diff --quiet 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` | 0 |
| Crafted-input probe | `python -I <scratchpad>\probe.py` (calls `stage_table` on crafted text; reads only) | 0 |
| Line lengths | `awk 'length>100'` over both files | lists the long lines of Minor 1 |

Not run: the whole `test_audit_count.py` (the executor ran it: 148 tests, exit 0; I ran the focused classes the slice names),
`test_tracked_files_private_paths.py` (the executor's run, exit 0; I did not repeat it; it reads the tracked files and the
commit adds no path of a private kind that I saw in the diff), the product's gate (told not to). The new-tests-fail-on-the-base
check was not repeated; it needs the base's `audit_count.py` in a separate worktree and the executor's report gives 31
failures and 1 error there, with the error explained.

## Reaches beyond the handoff
- `foundations/decisions.md:11640-11710` read as the handoff's range for WAY-352 (the handoff lists it); no other reach.
- `task-cycle/remarks_check.py:90-92` (`display`), to confirm what it escapes; `process-audit/audit_count.py` lines around
  `fill`, `cell`, `token_count`, `table_cells` and `stages_time` (callers and contracts of the change).
- A probe script written in the scratchpad `a scratch script in the session's scratchpad`
  (outside every repository), and the focused test output in the same folder (`focused.txt`).

## Unread material
- `process-audit/test_audit_count.py`: I read the diff of the range whole, not the classes it did not touch.
- `process-audit/audit_count.py`: read the diff whole and the surrounding functions named above; not the 2,400 lines as a whole.
- Decision entries WAY-337, 338, 339, 343, 331, 328, 38; invariants `script-imports`, `cross-part-imports`,
  `tracked-file-private-paths`; part-map entries `process-audit` and *External context*; `task-cycle/cycle_stages.py:858-954`;
  `process-audit/price_list.md`: not read by me. I read WAY-344 and WAY-352 whole, the two entries that bear on this slice's
  behaviour, and judged the rest through the slice's text and the diff (no import was added; the module's imports are unchanged
  in the diff, so `script-imports` and `cross-part-imports` are not reached by what the diff shows).
- `task.md` and `plan.md`: not opened; the passages the handoff carries were used.

## Searches not found or unclear
- The slice's "the `Error:` line names both" against its "one `Error:` ... `<field>`" per missing field: unclear (Minor 2).
- None otherwise.
