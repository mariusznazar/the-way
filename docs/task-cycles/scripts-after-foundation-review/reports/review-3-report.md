PASS 336ae16e1e5f8821a3fb800967da4e8c453b60c6

# Review of slice 3, task `scripts-after-foundation-review`

Range `40559b68ba26673de95e7c8d369c60230f219b4e..336ae16e1e5f8821a3fb800967da4e8c453b60c6`; `git rev-parse HEAD`
gave the head. One commit, three files: `task-cycle/cycle_stages.py`, `task-cycle/test_cycle_stages.py`,
`process-audit/test_audit_count.py`. Counts: 0 blocking, 1 Minor, 0 out of scope (the Minor lies within the task).

## Findings

### Critical
None.

### Important
None.

### Minor

**M1. The slice's own goal sentence, "after the slice the audit still reads the report", does not hold for
the report the changed script now writes (plan-mandated, not made by the executor).**
- Place: `process-audit/audit_count.py:953-975` (`section_table`), unchanged by this slice; the sentence is in
  the slice's Goal and its Checks line ("the audit still reads the report of the earlier forms").
- What: `section_table` accepts the header of the detailed table only if it equals the eight needed columns or
  those plus *Files named* (line 970-974). The report of `cycle_stages.py` now has eleven columns, so the audit
  answers "not of the form the stage report gives" and prices the cost, the count and the share `unknown`.
  The one test that runs the stage script and reads it with the audit,
  `process-audit/test_audit_count.py:865` (`test_the_stage_report_cycle_stages_writes_gives_the_share`), is red:
  `['0.014250', '1', '15.8%'] != ['unknown', 'unknown', 'unknown']`.
- Judgement of the orchestrator's question: the cause is exactly the refused header and nothing else. Evidence:
  I ran the subset (below); 50 of 51 pass, the one failure is that test with the three `unknown` values and
  no crash, no `Error:`; the code of `section_table` has no other path that gives "unknown" for this input
  (the eleven-cell rows would also fail the `len(cells) != columns` check, but the header check comes first).
  The fixture edit in `test_audit_count.py:836-838` (two zero lifetimes in `answered()`) is needed and
  sufficient: without it the script ends with exit 2 before the audit is reached.
- Why it matters, and why Minor: between this slice and Slice 7 a cycle run with the new script would lose its
  cost in the audit (with a reason, not silently), and the focused check the slice names is red. Slice 7's Goal
  makes the audit read the three forms of the header, which makes this test green again, and the plan's order
  (writer before reader) is a chosen one; the branch is not released between slices. It would be Important if
  Slice 7 were dropped or did not restore this test. The orchestrator should carry into Slice 7 that this test
  must be green at its end, and the spec's sentence in D4 "the audit still reads the report" is true only after
  Slice 7.

## Against the task and the spec (D1, D4, To do 7, WAY-337, WAY-339, WAY-344)

Verified by reading the diff and the code, not by the executor's report:
- Columns *Cache write (5 minutes)* and *Cache write (1 hour)* come after *Files named*, header and separator
  match (11 cells), each cell through `number()` like the other token cells; `Usage` gains `write_5m` and
  `write_1h`, summed in `add`; every place that sums (`row.by_model`, `row.subagent`, `row.orchestrator`,
  `totals`, `by_model` of the whole-cycle table) goes through `Usage.add`, so none drops the new counts.
- *Input* is built as before (input + writes + reads); the first table, the line "Tokens in all" and the whole-cycle
  table by model keep their columns and figures (the whole-cycle table is not given the new columns).
- Codex: `Usage` defaults give `0` and `0`; no warning and no `unknown` (`CodexCacheWriteColumnsTest` asserts empty
  stderr and `Warnings: none.`). A row with no token usage uses `Usage()`: zero cells, model `—`/`unknown` as before.
- Warning: counted per chosen response (after the choice by the largest output among lines sharing an id), one note
  per agent naming the full transcript path, figures as read, exit 0. This reads the spec ("a `Warning:` line names
  the transcript") correctly.
- WAY-344: `message.usage.cache_creation` and both lifetimes are read with `required` / `required_count` after the four
  counts, so a missing or null field, a non-object `cache_creation`, a negative, text, fractional or boolean count
  give exit 2 with a message naming transcript, line and field. The executor's choice to check them after the four
  counts keeps the existing test of the list-shaped `usage` valid; fine. The module description lists the new fields in
  the *Needed* paragraph and the warning in the warnings paragraph; the paragraph above the section and the module
  token paragraph say that *Input* holds the writes and what the two columns are. The exit-code line is unchanged
  (that is Slice 2's).
- `task-cycle/cycle_measures.py` and `mechanism_measures.md` unchanged; no other script changed except the one fixture.
- Invariants (script-language: English identifiers and comments, no new import beyond the existing test sibling
  import; script-imports: `cycle_measures` imported in the test through the `sys.path` insert the file already has;
  script-subprocesses: none added): no departure found.

## Tests

- New tests fail on the base: I copied the base `cycle_stages.py` (`git show 40559b6:task-cycle/cycle_stages.py`) beside
  the new `test_cycle_stages.py` and `cycle_measures.py` in `.runs/review-3/base/` and ran it: 69 tests, `FAILED
  (failures=23)`. Green on the head: 69 tests OK.
- The tests do not compute their expectation from the code: the figures (30/70, 200/100, 250/170) are worked out by hand
  in comments from the transcript; the test across the two scripts sums the stage rows and compares with the
  `- Cache written, 5 minutes` / `1 hour` lines of `cycle_measures.py`, with a response written over two lines
  counted once in both. A swap of the lifetimes, a sum of them into one column, a dropped Codex default and a
  missing warning each change one of the asserted figures (the lifetimes are distinct in every fixture).
- The crafted-names test changed its cell count (10 to 12 bars) and its end-of-row check, which follows from two more
  cells and keeps its intent. No test here holds a `decision:` line or is an invariant's test; nothing to name under
  WAY-03. The `answer()` helper gained an optional `five` argument and writes `cache_creation` in every response, as the
  spec (D4, "existing fixtures gain the needed fields") says.

## Trust boundary (transcript read by `cycle_stages.py`)

Checked: a missing, null, list-shaped, negative, text, fractional and boolean `cache_creation` or lifetime gives
exit 2 with the field named (`ClaudeFieldsTest` new tests, green); a lifetime sum that differs from the response's
writes gives a warning and exit 0, not a crash; no command is run, nothing is written outside the output path; the new
cells are integers formatted by `number()`, so no transcript text reaches a result from them. The warning holds the
path of the transcript found on disk, as the other notes do (the report's Warnings list already holds such text; the
path is the file system's, not the transcript's contents). No finding.

## Declined to judge
- The line-length overshoot of lines the slice did not add (executor report names lines 49, 59, 66, 1049): not in the
  diff (my own check of the added lines found none over 100 columns).
- The effect of the red audit test on the gate: the cycle's own gate comes at the end, after Slice 7; outside this slice.

## Checks run (from the worktree root)
1. `python -B -m unittest discover -s task-cycle -p "test_cycle_stages.py"` on the head: exit 0, 69 tests OK.
2. `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"` on the head: exit 0, 87 tests OK.
3. `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Cost -k StagesForms` on the head: exit 1,
   51 tests, 1 failure: `test_the_stage_report_cycle_stages_writes_gives_the_share` (see M1).
4. Red on the base: `cd .runs/review-3/base && python -B -m unittest test_cycle_stages` (base `cycle_stages.py` + head
   tests): exit 1, 69 tests, `failures=23`.
5. Manual: `git diff` of the range read whole; line length of added lines (`awk length>101`): none over.
No check I could not run. The full gate and the full audit file were not run (WAY-160).

## Reaches beyond the dispatch
- `process-audit/audit_count.py:953-1010` (`section_table`, `older_table`): to establish the cause of the red share test
  (M1).
- `plan.md` Slice 3 and Slice 7 goals and the slice list around them: to see whether Slice 7 restores the share test.
- `task.md:30-36` for To do 7 (the task passage the dispatch cites).
- `task-cycle/cycle_stages.py` whole functions `read_claude_agent`, `required`, `required_count`, `warnings` builder
  (lines 905-920): to follow the new fields to every sum and to the warnings list.

## Working copies
- `.runs/review-3/base/` (the base `cycle_stages.py`, head `test_cycle_stages.py`, `cycle_measures.py`): made, run,
  and removed (with `.runs/review-3/` itself) before returning. No worktree was made; the reviewed worktree, its index and
  branch were not changed (`git status --short` clean).

## Unread material
none. (Read whole: the handoff, `task-cycle/review/SKILL.md`, the executor report, the whole diff of the range,
`spec.md:80-179` and `225-330`, `task.md:30-36`, the changed functions of `cycle_stages.py` and the lines of
`audit_count.py` named above. The foundation entries named by the handoff — WAY-337, WAY-339, WAY-344, the three
invariants and the `task-cycle` part-map entry — I did not open whole; I judged the slice against the spec and task
passages that restate them, and against the code of the invariants' reach. This is the gap to weigh: a sentence of
WAY-339/WAY-344 that the spec does not restate would have escaped me.)

## Searches not found or unclear
- The spec's "the paragraph above the section" has two candidates (the top paragraph and the paragraph under the section
  heading); the executor updated both, which is consistent with D4, so unclear but harmless.
- The reason text the audit gives for the refused header I took from the code (`section_table`, line ~972), not from a
  printed run; the share test's `unknown` values agree with it.
