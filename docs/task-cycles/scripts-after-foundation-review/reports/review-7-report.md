PASS f1d632396d25f47cddf7efee7d4659a2e7e47e7c

# Review of slice 7, task `scripts-after-foundation-review`

Range `4c03086723435b286e1a94c92c5b12e3028be12d..f1d632396d25f47cddf7efee7d4659a2e7e47e7c`, one commit (`f1d6323`), files `process-audit/audit_count.py` and `process-audit/test_audit_count.py`. `git rev-parse HEAD` is the head given.

Counts: blocking 0, Minor 1, out of scope 0.

## Findings

### Critical
none

### Important
none

### Minor

1. `process-audit/test_audit_count.py` (the added `def written_cost` in class `Cost`, right after `test_...disagree...`): the added methods follow two blank lines inside the class body (the diff shows `+    def written_cost` after an existing blank line that ended the previous method and another that the diff keeps), where the rest of the class uses one. Style only; no effect on behaviour or on any check. Evidence: the hunk at `@@ -1267,6 +1308,130 @@` and the end of the hunk, which adds two blank lines before `SECTION = ...`.

## What I verified against the task, spec and foundation

- **Form (D2, WAY-344).** `SECTION_FORMS` holds the three prefix forms; `section_table` reports a one-column header as a missing field naming the other column (also where *Files named* is absent or the writes stand before it), refuses any other header as "not of the form", and reads neither column as the earlier form with no `Error:`. The module description's WAY-344 paragraph says the pair is never missing when neither stands. Matches WAY-344's text ("neither column ... earlier form ... one of the two ... missing field").
- **Cost of a row.** `cost_at` prices plain input (`input - cached - write_5m - write_1h`) at *Input*, cached at *Cached input*, each lifetime at its own price, output at *Output*. `priced` checks `cached + write_5m + write_1h > input` before pricing and gives `unknown` with a reason; the older message for a cached input above its input is kept. `priced_older` uses the same `cost_at` with zero writes, so the older table and the earlier forms are priced as before (their rows hold 0 and 0). Codex rows with 0 and 0 and a model with `—` writes are priced.
- **`—` in a write column.** `read_prices` gives a model with `—` in *Input*, *Cached input* or *Output* the value `None` (no price at all) and a model with `—` only in a write column a `ModelPrice` whose lifetime is `None`; `cost_at` gives `unknown` with the reason only where the row holds writes of that lifetime and never takes another column's price. The two cases stay apart in the price table. A write cell that is neither a number nor `—` refuses the list (exit 2).
- **Price list boundary.** A table lacking a write column ends with exit 2 and an `Error:` naming `--prices` and only the missing column; the path is not in the message (tested). The price list of Slice 4 (`process-audit/price_list.md`) has both write columns in both tables, numbers or `—` in the cells, a `—` pair for the OpenAI table, and text that agrees with the audit's rule for `—`; I read it with the audit's own test (`python -B process-audit/audit_count.py --help` runs, and the whole file of tests, which runs the real list through the stage-report test, is green). The executor's one-off call on the real list is in its report; I did not repeat it. The price list was not changed by this slice, and needed no change.
- **Trust boundary (crafted input).** Write counts are read by `token_count` (ASCII digits, commas, at most 15 digits), so words, 16 digits, a negative, an empty cell and a float give cost `unknown`, exit 0 and no traceback (tested in `test_a_write_count_that_is_no_number_leaves_the_cost_unknown_and_no_traceback`); a model name in the new reason is cut by `TEXT_CAP`; a price cell must match `PRICE`; the `Error:` for the price list names the option and column only. Nothing of the input reaches a command or a write place. Row cell count is checked against the header before indexes 9 and 10 are read. No finding.
- **The task's text and the module description.** The description of the module, the paragraph of WAY-344 fields, the description of the price list and the text of the section *Cost* are changed as the slice gives; the sentence "priced as input: an approximation" now holds for the earlier forms and the older table only. The section *Cost* text states what the newer form does.
- **Tests.** The tests in the slice's list are all present: earlier form without the write columns (a pin, green on the base too, as the executor says and as the slice's wording makes unavoidable); one write column and not the other, each of the two (exit 1, result written, line naming `stages.md` and the column, cost `unknown`); the newer form with figures that tell 5 minutes (3) from 1 hour (5) (25000 against 23000 at one price); Codex-style row of 0 and 0 on a model with `—`; `—` with writes `unknown`; `—` without writes priced; cached input and writes above input `unknown` with a boundary test (exactly equal is priced); the price-list test (`Locations`, both columns, each naming the column and not the other nor the path). The expected values are worked by hand in the comments and are not computed by the code.
- **The orchestrator's information.** `Cost.test_the_stage_report_cycle_stages_writes_gives_the_share` is green. It was changed: the orchestrator's response now carries writes of 100 and 200, and the expected cost (`0.015550`) and share (`14.5%`) were recomputed by hand: 1000 plain at 2 + 100 at 3 + 200 at 5 + 100 at 10 = 4300, plus 3000 + 1500 + 6000 + 750 gives 15550; fix and review 2250 of 15550 is 14.47 %. I checked the arithmetic. It holds no `decision:` line and no invariant.
- **WAY-03.** No test with a line `decision:` and no invariant test is changed by this commit. None to name.
- **Reserved choice, guidelines, screenshots.** The slice settles no language, library, store, login or place to run; no product guideline files apply to this part (the-way's own script; WAY-328 departs from a product's guidelines), no screenshot in the range.
- **Size.** `section_table` and `read_prices` stay short; the added code is small. No finding on structure.

## Checks run (from the worktree root; `-B`, so no `__pycache__` written beyond the ignored one)

- `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` (the whole file, including `Cost`, `StagesForms`, `Locations`, `PriceBoundary`): exit 0, `Ran 211 tests ... OK` (257 s). `Cost.test_the_stage_report_cycle_stages_writes_gives_the_share` is among them and green.
- `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"`: exit 0, `Ran 3 tests ... OK`.
- `python -B process-audit/audit_count.py --help`: exit 0.
- `git status --short` after the runs: empty (the worktree is unchanged).
- Not run: the focused `-k` selection separately (it is a subset of the whole file, which was green); the whole gate (WAY-160); a run of the base to see the new tests red (the executor's `reports/executor-7-base-focused.txt` records 31 failures on the base; I read the reasoning against the diff and did not repeat the run); a mutation of my own (the executor reports two mutations, which I did not repeat; the tests that pin them are present and I read their figures).

## Declined to judge

- The split of the series, the new list date and the change of `task-cycle/cycle_stages.py` (task To do 5 and 6, Slices 3 and 4): not this slice.
- Whether the price list's figures match the providers' pages: read by the cycle from the pages in Slice 4; outside this slice's change.

## Reaches beyond the dispatch

- `task-cycle/cycle_stages.py:1036-1066` (the function `report`, found by name), to check that its row writes `0` and `0` for rows with no usage and thousands separators in the counts, which `token_count` accepts. Asked for by the handoff ("the form of the stage report that Slice 3 wrote").
- `process-audit/audit_count.py` around `read_prices`, `priced`, `token_count` (whole functions), to check the boundary cases beyond the diff.

## Working copies

None made (`.runs/review-7/` not created). Nothing to remove.

## Unread material

none of the dispatch's named material: the handoff, method file, task passages (lines 30-36, 109-114, 145-148), spec D2 and D5, WAY-337 and WAY-344 and `process-audit/price_list.md` were read whole. Read in part: `audit_count.py` (the diff, plus the functions named in Reaches) and `test_audit_count.py` (the diff only; the unchanged tests I took from their green run); `executor-7-report.md` was read whole as claims. I did not read `whole_change.md` or `fix.md` (the variant says not to).

## Searches not found or unclear

none
