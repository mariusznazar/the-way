# Findings to fix — slice 6

The blocking finding of the review of slice 6 (`reports/slice-6-review-report.md`, head `0964b521610f2f7a73d19c6a99f9477e537e8dd9`), copied word for word from the reviewer's report. The review's Minor findings are not part of this fix.

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
