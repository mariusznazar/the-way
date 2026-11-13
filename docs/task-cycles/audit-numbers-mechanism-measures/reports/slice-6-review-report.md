FAIL 0964b521610f2f7a73d19c6a99f9477e537e8dd9

# Review of slice 6, range `0e75a4b..0964b52`

Head reviewed: `0964b521610f2f7a73d19c6a99f9477e537e8dd9` (`git rev-parse HEAD` confirmed). Method: `review-change`, a planned
slice. Trust boundary: yes, as the handoff says. Counts: 1 blocking, 4 Minor, 0 out of scope.

Changed files (`git diff --stat 0e75a4b..0964b52`):
- `process-audit/audit_count.py`: +242 / -6 lines (net 479 insertions in the two files together)
- `process-audit/test_audit_count.py`: +243 lines

File sizes at head: `audit_count.py` 2664 lines, `test_audit_count.py` 2702 lines.

## Verified claims of the executor and the handoff

- The writer `task-cycle/gate_times.py` repeats four run-level cells (Started, Exit code, Total, Other) in each row of a
  run (`rows()`, `gate_times.py:231-236`), not five; the plan's "first five cells" is a plan error and the reader's grouping by four
  cells (`audit_count.py:1485`) is right. Two runs merge only when consecutive and equal in start (to the millisecond), code,
  total and others: not practical.
- The labels in `MEASURE_LABELS` (`audit_count.py:333-343`) equal, word for word, the fifteen lines `cycle_measures.py:412-427`
  writes. The six columns in `GATE_COLUMNS` (`audit_count.py:347`) equal the writer's table header.
- The audit never imports or runs either script: the imports of `audit_count.py` (lines 208-225) are unchanged and the two
  script names occur only in comments and in result text. `git diff 2292f33 HEAD -- process-audit/audit_count.py` holds no changed line
  that mentions `TREE_PATHS`.
- A copy without either file gives unknown with the reason "the copy holds no `<file>`: an earlier form" and no `Error:`
  (`read_optional`, `audit_count.py:1376-1381`); a file over `MAX_BYTES`, a symbolic link or non-UTF-8 text goes through the
  existing `read_file`.
- A missing label, a missing column and a missing table each end with exit 1, the result written, every value of that file
  unknown and one `Error:` line naming file and field (`audit_count.py:1397-1413`, `1450-1465`, `2646-2660`); the tests
  `test_a_measures_file_without_a_label...`, `test_a_gate_file_without_a_column...` and `..._without_a_table...` assert the
  exact line.
- Values that reach cells are either validated by a full-match pattern before they are kept (measures, started, code, total,
  others, seconds) or pass `cell()` after a cut to `TEXT_CAP` (directory names); reasons are constants. I found no way to
  put a bar or a control character into a cell. Work on crafted 4 MiB files of the measures file (many labelled lines, one
  long line, many continuation lines, colons only) took under 3 s each, linear.
- The two sections sit after `## Cost` and before `## Process versions` (`audit_count.py:2494-2495`), each with a line before the table that names
  the writing script and says `unknown` is never zero.

## Findings

### Critical

none

### Important (blocking, within the task)

**I1. The run limit does not hold for rows of the wrong number of cells** — `process-audit/audit_count.py:1476-1480`.
In `read_gate`, the branch for a row whose cell count differs from the header's does `runs.append((None, []))` and
`continue` before the test `if len(runs) >= MAX_RUNS` at line 1484, which sits only in the branch of a row that has the right
cells. So a file of rows with the wrong cell count is read without limit: every such row becomes a run of its own, and
`cycle.gate_runs.append([UNKNOWN] * 5)` (line 1504) puts a row in the result for each of them. The slice's goal says "at most a
fixed number of runs per file ... are read, and the rest give unknown with that reason", and the test list asks for a crafted
file with "very many runs ... costing bounded work".
Evidence: I gave `read_gate` (imported from the worktree, no test fixture) a gate file of the maximum size the count reads
(4 MiB, `MAX_BYTES`) made of the line `| a | b |` after a valid header: it returned 419,412 runs (1.3 s). A cycle copy of that
size therefore writes about 420 thousand rows of seven cells to the result (tens of megabytes) from one 4 MiB file, and
nothing in *Unknown values* says that rows were cut. Distinct well-formed runs are cut at 500 as intended (60,000 distinct
rows gave 500 runs). `test_runs_beyond_the_limit_are_not_read_and_say_so` (test file near the new `GateRunsMeasures`) feeds only well-formed
rows, so it does not see this. The cap must count every run, malformed or not, and the crafted-file tests must include a flood of
wrong-width rows.
Why it matters: this is the trust-boundary requirement of the slice (untrusted history), and the check that the plan
names for it is the one that fails.

### Minor

**M1. An exit code of four or more digits is read as unknown with a wrong reason** — `process-audit/audit_count.py:350`
(`GATE_CODE = [0-9]{1,3}`) and `:1512`. The writer writes `str(code)` of the child's exit code
(`gate_times.py:232`); on Windows, the author's system, a crashed or interrupted gate ends with codes such as 3221225786
or 4294967295. I ran `read_gate` on both: the exit code cell became `unknown` and the reason says "an exit code is not a whole number",
which it is. The value is lost, not mis-stated, and slice 7 may not need it; still it contradicts "a value that is not what
its label gives" being the only way to unknown. Widen the pattern to the range a process can return, and no test gives
a code above 255.

**M2. The table of runs is read only to its first line that does not begin with `|`, and what follows is dropped without a
reason** — `process-audit/audit_count.py:1471-1472`. A run after a blank line or any other line (for instance a
hand-edited or merged file) is silently not counted: I confirmed that a second valid row after a blank line gives one run and no
row in *Unknown values*. The goal says a value that cannot be read is unknown "with a reason in *Unknown values*". One
reason row ("rows after line N are not read") would do.

**M3. The module docstring is stale** — `process-audit/audit_count.py:190-198`. The list of sections of the result does not
name `## Mechanism measures` and `## Gate runs`, and the exit-1 sentence still reads "a field missing in a `stages.md`",
while the code now also ends with exit 1 for the two new files. Slice 5's text brings the docstring to its own change; no
slice among 6, 7 and 8 as I read the plan names the docstring for these two sections, so this may stay unowned until
slice 7 or 8.

**M4. A git failure on an optional file blanks the whole copy** — `process-audit/audit_count.py:1531-1539`. The two new
`read_optional` calls stand in the same `try` as the reads of `cycle.md` and `stages.md`; if `git cat-file` fails on the
new files, the `except` sets `record = stages = None` although both were already read. Before the slice only a failure of a
required file did that. It is an unlikely event (`ls-tree` just listed the object), and the executor's reading is consistent
with the existing code; read the two optional files in their own `try` if the record and the stages are to survive.

### Tests (no separate grade; part of I1 and M1)

The 15 new tests assert values worked out by hand (`MEASURE_VALUES`, the runs of the first test), not values the code
computes. Each fails when the behaviour breaks as far as I read them; I did not mutate the code. The two cases
missing are named in I1 and M1.

## Declined to judge

- The writer `task-cycle/gate_times.py` and `task-cycle/cycle_measures.py` (slices 1 and 3): only what they write was read,
  to check the reader; their own behaviour, such as the exit codes they pass on, is not this slice's.
- Series, medians and comparison between versions: slice 7, as the handoff says.
- The plan's wording "first five cells": a plan error, recorded above; no change to the code is asked for.
- The separator `" · "` between directories inside the *Directories* cell can also occur in a directory name from the file; the
  cell is for reading by a human and the slice does not split it again, so I set it aside.

## Checks run

- `git rev-parse HEAD`: `0964b521610f2f7a73d19c6a99f9477e537e8dd9`, matches the dispatch.
- `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Measures`: exit 0, 15 tests OK in 11.7 s.
- `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"`: exit 0, 1 test OK.
- `git diff 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- process-audit/audit_count.py | grep -c TREE_PATHS`: 0 matches
  (the slice's check; the executor's claim holds).
- Scratch probes (read-only, in the session's scratchpad, importing `audit_count` from the worktree and calling `read_gate` and
  `read_measures` on crafted text; nothing written in the worktree): `a probe script (probe.py) in the session's scratchpad`
  and `...\probe2.py` in the same directory. They showed the numbers given in I1, M1, M2 and the bounds of the measures reading.
- Not run: the whole `test_audit_count.py` (several minutes; the executor reports 163 of 163 after the second commit; I
  take it as claimed, unverified by me) and the product's gate, as the handoff says. Not run either:
  `python -B -m unittest discover -s elements/part-map -p "test_cross_part_imports.py"` (not in this slice's list).

## Reaches beyond the handoff

- `task-cycle/gate_times.py:105-299` and `task-cycle/cycle_measures.py:405-430`: read to check what the writers write against the readers
  (labels, columns, the cells repeated per row, the exit code form); both exist in the worktree.
- `process-audit/audit_count.py` helpers `header_fields`, `table_cells`, `is_separator`, `read_file`, `cell`, `table`, `main`: read as the
  code the change leans on.
- `.runs/task-cycles/audit-numbers-mechanism-measures/plan.md:219-336` (slices 5 to 8) to see who owns the module docstring.
- `the author's rules file on scripts`: read before writing the probe scripts.

## Unread material

- `task-cycle/review/fix.md` and `whole_change.md`: not read; the variants that name them did not come.
- `foundations/decisions.md` WAY-338, WAY-343, WAY-328 and WAY-38: WAY-344 and WAY-348 read whole; WAY-338, WAY-343, WAY-328, WAY-38,
  `foundations/invariants.md` tracked-file-private-paths and `foundations/part_map.md` External context were not opened by me (the
  private-paths test and the part-map entry of process-audit, lines 115-124, were what I used). I found no behaviour that bears on them.
- The foundation entry WAY-349 and WAY-347 were read only where WAY-348 and the writers cite them (not whole).
- `process-audit/audit_count.py` and `process-audit/test_audit_count.py`: read the whole diff and the helpers above; not every line of
  the files.

## Searches not found or unclear

- The plan and handoff say each run's rows repeat "the first five cells"; the writer repeats four (explained above).
- The handoff's "a fixed number of runs per file and of directories per run": the numbers are not given; 500 and 50 are the
  executor's choice, reasonable, and the only gap is I1.
