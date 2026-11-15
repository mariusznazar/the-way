# Executor report — slice 9 of `scripts-after-foundation-review`

**Status:** `done`

**Commit:** `b6f800c` on `task/scripts-after-foundation-review` — "Give the register's unknown values one line for each field and reason in the audit count" (author address `the author's e-mail address`, from the conditional git rule for the `mariusznazar` account; left as it is).

**Files changed:**
- `process-audit/audit_count.py` — removed the 500-value cap and its line; added the grouping of the register's unknown values into one row per (field, reason) pair; separate table for those rows under `## Unknown values`; docstring sentences about *Unknown values* updated; long lines wrapped to 100 columns.
- `process-audit/test_audit_count.py` — helpers changed (`rows` reads only the first table of *Unknown values*; new `pair_rows`); the register-value assertions moved to the pair table; one test replaced; one test added.

Diff totals for the commit: 148 insertions, 68 deletions across the two files.

## Check result

Focused checks (slice *Checks*) pass: 68 tests, exit 0; whole file `test_audit_count.py` passes: 227 tests, exit 0 (run on the final code, after the line-wrap edits).

## Own-work check (section 3)

- **Requirement:** the result gives one line for each pair of field and reason, with its count and first examples; the result is deterministic; crafted text reaches the result as before (cut, one line, no bar).
- **Checks:** the focused tests and the whole file; the existing same-bytes test (`Run.test_the_same_input_gives_the_same_bytes_in_both_files`) passes; the new `CraftedInput` test checks a crafted repository name with an escaped bar, a control character and text over the cut: the cell has no raw bar, the text is cut, the line is one line.
- **Mutations considered:** `EXAMPLES` at 0 or 4 is caught by the example assertions; dropping the row-number stripping is caught by the pair count assertions; dropping the grouping (one line per value) is caught by the 830-row test (it expects 2 pairs); a bar written raw is caught by the crafted test.
- **Failed and rerun:** none of the checks failed on the final code.

## Checks run

1. Before the change, on the base: `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Run -k RegisterCount -k CraftedInput` — exit 0, 67 tests (baseline green, not a red run).
2. Red run on the base: the new test file against the base `audit_count.py` (in a working copy under `.runs/executor-9/base-check/`, removed afterwards), same command — exit 1, 67 tests, **21 failures, 0 errors**. The failures are all register-value assertions (the pair table is absent on the base). `CraftedInput` cycle-level and `GateRunsMeasures` tests pass on the base as they should. Caveat: the `CraftedInput` crafted-text test was added after this run, so it has not been run on the base; its failure on the base follows from the code (no pair table, so `pair_rows()` is empty and `assertEqual(1, …)` fails), but that was not observed. The template test (`test_the_template_with_no_rows_counts_nothing_and_refuses_nothing`) passes on the base too: it is a guard, not a red test.
3. Final focused run: `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Run -k RegisterCount -k CraftedInput` — exit 0, 68 tests. Output saved as `reports/executor-9-focused-run.txt`. (Run before the line-wrap-only edits; the whole-file run below covers the final code.)
4. Whole file on the final code: `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` — exit 0, 227 tests. Output saved as `reports/executor-9-whole-run.txt`.
5. `python -B -m py_compile process-audit/audit_count.py process-audit/test_audit_count.py` — exit 0.

A whole-file run I started earlier was stopped (it ran on code I was still editing); it is not a check and its output was overwritten.

## Changed test that holds a decision or an invariant (WAY-03)

No test holds a `decision:` line or an invariant's test in this slice. Changed tests named anyway, because they assert on the cap or on register rows:
- `RegisterCount.test_a_register_far_larger_than_a_real_one_lists_its_unknown_rows_in_part` was replaced by `test_a_register_far_larger_than_a_real_one_gives_one_line_for_each_pair` (it asserted the 500-row cap and the "N more" line).
- The assertions on individual register rows (`row N of …`) in about 20 tests of `RegisterCount` now read the pair table; the helper `rows("Unknown values")` reads only the cycles' table.
- One test added: `CraftedInput.test_crafted_text_of_a_register_value_reaches_its_pair_as_one_cut_line_with_no_bar`.

## Choices made

1. **Field and pair.** The field is the value with its row number taken out (`row 3 of \`Problems\`` becomes `row of \`Problems\``); the pair is (field, reason). Rejected: keeping a single table with count and example columns — the cycle rows would then carry empty cells, and the test helper that reads the first four columns would mis-read them. Cost if wrong: an extra table to read, nothing more.
2. **Two tables under `## Unknown values`.** The first keeps the cycles' values and the values of versions and measures as before; the second holds the register's pairs, with columns `Field of the register | Values | Why | First examples`. An intro paragraph says what each table is (the task asked that the headings say what the lines are). Cost: the first table is no longer the only one under the heading.
3. **Examples.** The first three values of each pair, each written as `repository record: value`, joined by `; `. Repository and record are cut to 200 characters as before, and the cell goes through the existing `cell()`.
4. **Scope of "register values".** The list grouped is `analysis.unknown`, which the old cap applied to. That list also contains values the ancestry check adds from the cycles' *Process pin* (reason `… ambiguous` or `… lacks commit`) and the fix of an issue. These are now also one line per pair, so their per-cycle detail shows only as examples. I kept them in the group because the old cap covered them too. This is a choice the orchestrator may want to revisit: the alternative is to keep those per-cycle values in the cycles' table.
5. **Versions and measures values** stay in the first table (not grouped). Their number is bounded by versions times measures, and the slice did not name them.
6. **Reasons unchanged.** The row-width reason (`the row has N cells, not 8`) keeps its count, so the number of pairs follows the number of distinct widths in a crafted register. That is bounded by the register's size, not by a constant. Rejected: removing the count from the reason; it would change wording the slice did not ask about.
7. **Line wrapping** of the lines I added to 100 columns.
8. **Helper change in the tests.** `rows()` now reads only the first table of *Unknown values*; `pair_rows()` is new. Tolerant of the base output (returns empty if the table is absent) so that the red run fails on assertions, not on exceptions.

## Problems as observed

- **Stale reference outside the slice.** `process-audit/SKILL.md` lines 161–162 say that a refused row's entry in *Unknown values* "names row `<n>` of *Problems*" and gives the reason. After this change the row sits in the pair table as `row of \`Problems\`` with its count and examples. The skill's reading step should follow the new shape. Not edited: the slice's *Change* list names only the two files. Flagged for the orchestrator or a later slice.
- **The "about 830 lines" of the slice.** The register template as shipped holds no problem rows, so the template alone gives no unknown lines (the existing template test confirms zero). I could not reproduce "about 830 lines" from the template; I used 830 problems of one pair on top of the template as the stand-in register size. The orchestrator may want to confirm this reading.

## Unread material

- The task `task.md` passages and foundation entries named in the *Read* were read at the ranges the handoff gives: task lines 37, 75–79, 114, 148; `foundations/decisions.md:7357-7390` (WAY-330); `foundations/invariants.md:116-145`; `foundations/part_map.md:124-135`. Read in full as the ranges name.
- `process-audit/audit_count.py` was read in part: lines 1–1107, 1900–2170, 2280–2470 (partly), 2960–3265, and the parts found by grep; not read whole.
- `process-audit/test_audit_count.py` was read in parts: lines 1–240, 563–593, 2228–2360, 2636–2660, 2921–2980, and the assertion lines found by grep and by reading their contexts.
- `process-audit/SKILL.md` was read only at the lines found by grep (127–199).
- `process-audit/problem_register.md` was read only by grep (no mention of the cap found there).
- The foundation files outside the named ranges were not read.

## Reaches beyond the handoff (what, where, why)

- `process-audit/SKILL.md` lines 127–199 and `problem_register.md` by grep — to find mentions of the cap and of the row shape of *Unknown values* (found the stale reference above).
- `process-audit/audit_count.py` `read_register` and `Register` (about lines 1900–2170) — to see which reasons the register refusals carry, for the grouping (reasons are fixed texts, except the row-width count).
- `task-cycle/change/SKILL.md` and `slice.md`, `.ai/rules/git.md` — the method and the git rule (read in full).

## Searches not found or unclear

- "about 830 lines" from the template: not found in the template; see *Problems as observed*.
- Whether the orchestrator wants the ancestry values (*Process pin*, fix of an issue) kept per cycle: unclear from the slice; see choice 4.

## Working copies

- `.runs/executor-9/base-check/` — a copy of `process-audit/` and `task-cycle/` with the base `audit_count.py`, for the red run. **Removed** with `rm -rf`; it was a directory copy, not a worktree.
- `.runs/executor-9/` (its check logs) — the two logs were copied into `reports/` (`executor-9-focused-run.txt`, `executor-9-whole-run.txt`), and the directory was **removed**.
- No worktree was created; the removal step with `git worktree remove` did not apply.
