# Report — executor of slice 7, task `scripts-after-foundation-review`

**Status:** done

**Commit:** `f1d6323` "Price the cache writes of each lifetime at its own price in the audit count" (on `task/scripts-after-foundation-review`).

**Files changed:** `process-audit/audit_count.py` and `process-audit/test_audit_count.py` (about +363 / -59 together, per `git diff --stat`). No other file.

## What was made

- `audit_count.py`
  - The header of the detailed section has three forms (`SECTION_FORMS`), each a prefix of the next. The two write columns are a pair: with neither the table is the earlier form, with one the other is a missing field (`Error:` names `stages.md` and the column, cost `unknown`, result written, exit 1). Any other header is refused as before.
  - `StageTokens` gained `write_5m` and `write_1h` (zero for the earlier forms and the older table).
  - `ModelPrice` (input, cached, output, `write_5m`, `write_1h`): a model with `—` in *Input*, *Cached input* or *Output* is `None` (no price at all). A `—` in a write column is a `None` of that lifetime only.
  - `read_prices` reads both write columns. A table without one ends with exit 2, and the `Error:` names `--prices` and the missing column (only the missing ones, never the path).
  - `cost_at` is the one function for all rows (`priced` and `priced_older`). It prices the plain input, the cached input, each lifetime of writes and the output. A row with writes of a lifetime that has no price is `unknown` with a reason. `priced` checks `cached + writes > input` and gives `unknown`, keeping the old message for `cached > input`.
  - The module description and the text of the section *Cost* of the result are changed as the slice gives: the approximation holds for the earlier forms, the newer form prices each lifetime, the write columns are a pair under WAY-344, and the price list description gains the columns and the rule for `—`.
- `test_audit_count.py`
  - `TEST_PRICES` gained both write columns, and two models: `model-x` with `—` in both, `model-y` with 3 and `—`. The doubled-model row got the write cells.
  - New tests are listed under Checks below.
  - `test_the_stage_report_cycle_stages_writes_gives_the_share`: the orchestrator's response now carries cache writes of 100 (5 minutes) and 200 (1 hour). The expectation was recomputed by hand (15550 millionths, share 14.5 %), so the one test across the two scripts also checks the writes through the real stage script.
  - `StagesForms.newer` gained an optional `row` argument.

## Checks (command, exit code)

- Red on the base (new tests added to the test file only, `audit_count.py` as at the base): `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Cost -k StagesForms -k Locations -k PriceBoundary` — exit 1, `FAILED (failures=31)`, 85 tests. Output kept in `reports/executor-7-base-focused.txt`. The failures include `test_the_stage_report_cycle_stages_writes_gives_the_share`, the cost tests of the newest form, the one-write-column tests, the price-list test (both columns), the write-price `—` tests, the exceeding tests and the crafted-count tests. Four subtests of `test_a_wrong_price_list_refuses_the_run_with_nothing_written` fail on the base as a knock-on: the base accepted the list with a bad write price, and the later subtests then found a result written.
- Green after the code: the same command — exit 0, `Ran 84 tests ... OK` (`reports/executor-7-after-focused.txt`).
- `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` (whole file) — exit 0, `Ran 211 tests ... OK` (`reports/executor-7-whole.txt`). `Cost.test_the_stage_report_cycle_stages_writes_gives_the_share` is green.
- `python -B process-audit/audit_count.py --help` — exit 0.
- The real `process-audit/price_list.md` is read by `read_prices` (checked by a one-off call: date 2026-11-15, 8 models, Opus 5.5 writes 5 and 8, OpenAI writes `None`).
- Not run: the whole gate (WAY-160); no other check was left out.

Tests that pass on the base too (so they are pins, not red-first): `test_a_table_with_neither_write_column_is_the_earlier_form_and_misses_nothing` (the slice's "earlier form gives the cost it gave" test cannot be red on the base: the base already reads that form), and `test_the_two_write_columns_without_the_files_or_in_another_order_are_refused`.

## Own-work check (WAY-164)

- Requirement most likely unmet: an earlier-form copy, and the older table, are priced exactly as today, with no new `unknown` and the same exit code, while a one-column copy is a missing field and not the earlier form. Checks: the pin test of the earlier form (with and without *Files named*; cost `0.003000`, exit 0, no `Error:`, no `Unknown values` row naming `Cache write`), the existing older-table tests (green in the whole run), and the one-column test for each of the two columns (exit 1, one `Error:` line naming the column, cost `unknown`). All pass.
- Mutations run by hand on the code, each seen failing and the file restored (verified with `cmp`): the 5-minute write priced at the 1-hour price (`test_the_cache_writes_of_each_lifetime...` failed); `>` made `>=` in the check of cached input plus writes (`test_a_row_whose_cached_input_and_writes_make_exactly_its_input_is_priced` failed).
- Trust boundary: write counts and write prices are read by the same functions as the other counts (`token_count`: at most 15 ASCII digits) and the same price pattern; tested with words, 16 digits, a negative, empty and a float in a write count (no traceback, cost `unknown`, exit 0) and a non-number write price (exit 2). The model name in the new reason is cut by `TEXT_CAP` as in the other reasons, and it can only be a name the list holds.

## Choices

- `ModelPrice` as a frozen dataclass in place of the 3-tuple; the price table keeps "no price at all" (`None`) and "no price for one lifetime" (`None` in a field) apart. Rejected: a 5-tuple, which would leave the order of five numbers to the reader. Cost if wrong: only the internal shape; the tests that build a `Prices` give `{}`.
- A write column is a missing field also where the header lacks *Files named* or has the writes before it (one write column present): the missing one is named; the form check follows only when both or neither stand. Rejected: refusing such a header as "not of the form" with no field named, which would hide a column lost.
- The `Error:` for a price list without a write column names only the columns that are lacking (the old message listed all the columns). Cost if wrong: none; the test asserts the other column is not named.
- Reasons: "the cached input and the cache writes of stage `x` are above its input" (the old "cached input ... above its input" kept for a cached input above the input alone); "the price list gives no price of a cache write of 5 minutes|1 hour for model `m`".
- The test `test_the_stage_report_cycle_stages_writes_gives_the_share` was changed (writes added, expected cost and share recomputed). It holds no `decision:` line and no invariant; no test with a `decision:` line was changed (WAY-03: none to name).
- No move out of a function over the size rule was needed; the added code is small and the change did not call for one.

## Reaches beyond the handoff

- I read `process-audit/audit_count.py` and the test file by ranges and by search, not whole (the handoff allows it). Beyond the named ranges I read lines 1-200, 300-430, 780-1130 and 1275-1450 of `audit_count.py`, and the end of the renderer (the section *Cost* text, lines ~2960-2985), to change its text. I read lines 1025-1066 of `task-cycle/cycle_stages.py` (the table header it writes) to match the form. I did not change `cycle_stages.py`, `price_list.md` or the list of what starts a series.
- Tests in classes outside the named ones changed only through `TEST_PRICES`.

## Unread material

- `audit_count.py` and `test_audit_count.py`: read in the ranges above and by search; the parts for the register, the versions, the measures and the gate times were not read.
- `foundations/decisions.md` WAY-337 and WAY-344: read whole at the ranges given in the handoff.
- `spec.md` D2 and D5 and the task passages: read at the ranges named.
- `task-cycle/cycle_stages.py`: only the report function's header part, as above.

## Searches not found or unclear

- None. One note: the plan's wording "the test of the price list in class `Cost` or `Locations`": I put it in `Locations` (next to the other price-list refusal test); the handoff's `-k Locations` covers it.

## Problems observed

- A first whole-file run was started and I then changed the audit file for a mutation check while it ran; I stopped that run, discarded it, and made the whole-file run again with no edit meanwhile (the result above is that run).

## Working copies

- `.runs/executor-7/` of the worktree held the editing scripts, a copy of the good audit file for the mutation checks and the three test outputs. It was removed; the three outputs are kept as `reports/executor-7-base-focused.txt`, `reports/executor-7-after-focused.txt` and `reports/executor-7-whole.txt`. No remainder.
