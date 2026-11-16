# Author report — the fix of the review of correction 1 (R-1)

**Status:** done

**Commit:** `47a47fe`, range `b3bd8f4..47a47fe`. Files (added / removed): `process-audit/record_items.py` 7/5,
`process-audit/test_record_items.py` 29/2. The worktree is clean. No entry of the foundation touched.

## R-1 — fixed

- **How:** in `discarded_entries` the predicate `alone` now also requires `lines[0][0] == base`, so the first
  line under the item must be an entry at the entries' indent. A first entry deeper than the ones after it is no
  longer passed over: the whole is read as the text of one attempt, which holds two markers and gives `unknown`.
  The docstring says why a first line deeper than the later entries is not a continuation (there is no entry
  before it to continue). The reason for that case is reworded, as the finding asks, to name both cases: "a line
  of the item `Discarded attempt` is no entry or stands at another indent than its entries: write each attempt as
  an entry, all at one indent, and nothing else beside them" (it replaces "a plain line stands beside the
  entries", which was false for a line that is an entry). I used the reviewer's one-condition fix; no other way
  was needed.
- **Tests** (`process-audit/test_record_items.py`, with a line `decision: WAY-404 "..."`):
  `test_an_entry_first_under_the_item_and_deeper_than_the_next_one_is_not_dropped` — the record of the finding
  (first entry `open design choice` at 6, the next `size` at 4), the same with a third entry
  `reserved choice`, with the marker order swapped, and with four entries: each gives `unknown` with the reason
  above, never `no`; the same entries at one indent give `yes`. `test_a_sub_entry_under_the_first_entry_is_no_entry_of_the_list`
  — a deeper entry after the first at `base` is dropped as before (`no`), which also keeps the reviewer's `deeper`
  test standing. The three assertions of the earlier tests on the reason of a plain line beside entries now
  assert the new reason (cause: the reason is reworded to be true for both cases; evidence: R-1).
- **Seen failing first:** with the file of `b3bd8f4` put back, `python -B -m unittest test_record_items` in
  `process-audit` — `FAILED (failures=8)`, among them the four subtests of the new test (a false `no`); with the
  fixed file, `OK`, 31 tests (the corrected file was restored and committed).

## Checks (command, exit code)

- `python -B gate/run_tests.py process-audit` — 0, 269 tests.
- `python -B gate/run_tests.py task-cycle` — 0, 534 tests, 1 skipped.
- `python -B elements/common/foundation_check.py` (without `--skip-test-citations`) — 0, `0 errors`.
- Ruff, the pinned executable of the main checkout's `quality-venv`, `check --config ruff.toml --no-cache
  --ignore-noqa --output-format concise process-audit`, to a file — exit 1, the same 4 reports on lines this fix
  did not write.
- Not run: the product's full gate (by the handoff).

## The own-work check

- **Requirement most likely unmet:** no shape of the item *Discarded attempt* gives a wrong `no` or `yes` — the
  finding's own demand, including crafted input with deeper and shallower indents.
- **Check:** the new tests with first entries deeper than the later ones (two, three, four entries, either marker
  order), the test of a sub-entry, the earlier tests of plain lines beside entries and of 100,000 entries, and the
  failing run on the old file.
- **What it showed:** every such record gives `unknown`, or the answer its entries give where they stand at one
  indent; no wrong `no` or `yes` found. A first entry shallower than the later ones gives `unknown` by the same
  condition (the first line is not at `base`), checked by reading the predicate, not by a test of its own.

## Reaches beyond the handoff

None.

## Working copies

`.runs/author-correction-fix/` held the check outputs and a copy of the fixed file; it stood at
`the root of the task's worktree\.runs\author-correction-fix\` and was removed before
this return.

## Unread material

none.

## Searches not found or unclear

none.
