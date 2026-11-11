PASS 2e7168c34f51a6123ffd1e1bff65934013aaa361

# Review of slice 6 — the measures of each process version, series kept apart (`7bb25c3..2e7168c`)

`git rev-parse HEAD` = `2e7168c34f51a6123ffd1e1bff65934013aaa361`, confirmed. Two commits: `260b650` (the main change) and `2e7168c` (a discarded attempt that opens with `none` reads `unknown`), both in
`process-audit/audit_count.py` and `process-audit/test_audit_count.py`. Worktree read only (`git status --short` empty after every check).
Read: `task-cycle/review/SKILL.md` whole, the review handoff, the executor's handoff (ranges, the slice, entries, binding choices 1-7), the executor's report (claims), WAY-336 (whole, `foundations/decisions.md:10995-11035`) and WAY-338 (whole, `:11056-11080`),
the template's items *Plan*, *Discarded attempt* and *Slices returned too large* and the glossary entries it names, and the whole diff.
Counts: 0 blocking, 4 Minor, 0 out of scope.

## Findings

No Critical or Important finding. The code does what WAY-336 and WAY-338 say as far as the slice reaches them (the cost is the median of the cycles' costs at the one dated list; versions are compared only inside a series, each series is its own table, no cell sets one series' number beside another's), and the trust-boundary lessons hold in the new code (details below).

### Minor 1 — the plan's count of slices is read from any one figure before the word `slices`, not from the figure that counts them

Place: `process-audit/audit_count.py` `read_plan` (`FIGURE.findall(text[:word.start()])`, exactly one figure required).
Scratch (`scratch8.py`): `- Plan: reviewed by 2 agents; slices: 8` gives *Plans read* `1 of 1` with the count 2 — a figure that is not the count, read as the count, and no `unknown`. The rule "exactly one standalone figure before the first `slices`" removes the executor's example (`3 rows, 11 slices` has two figures and reads `unknown`) but not a text with one unrelated figure
before the word. A tighter rule — the figure written immediately before `slices` (`[0-9]+ slices`) — reads `3 rows, 11 slices` as 11 and `2 agents; slices: 8` as `unknown`. Effect: Q2 can be `no`/`yes` on a wrong count in an atypical plan text; Minor, since the archive's forms (`11 slices`, `…, 8 slices`) read right.

### Minor 2 — Q1 reads a negated mention as `yes`, and an old-form `none` as `no` without the slices' rounds

Place: `read_contradiction`. (a) `DESIGN_CHOICE in text.casefold()` makes `yes` of any text holding the phrase: "reserved choice, not an open design choice" is `yes`. The fix `2e7168c` closes the one case the executor found (`none — no open design choice`), not the negations that do not open with `none`. No archived record has a discarded attempt other than `none` (the executor's survey, and mine: 4 of the archive's records read `none` for both *Discarded attempt* and *Review rounds*), so the case is a reading rule, not a seen form.
(b) Q1 is `no` where both items read `none`. In the old template a slice's review rounds stand in the *Slices* table, not in *Review rounds*; an old record with `none` in both and a slice review that blocked on a foundation entry would read `no`. I found no such record in the archive (the 4 records with both items `none` have no fix row in their *Slices* table), and the new template puts slice rounds in *Review rounds*. Minor on both; a negation guard and a note in the docstring would close (a).

### Minor 3 — Q2 is `no` or `yes` on the plans that read, with `k of m` as the only sign of the partial basis

Place: `too_large_of`. Binding choice 6 says the sums are "of the version's cycles" and `unknown` where no cycle's plan reads; the code sums the cycles whose plan and too-large count both read and writes `Plans read` as `k of m`, which is visible in the next column. The executor's question 4 asks whether the partial basis is sound. A `yes` on part of the plans is a lower bound and sound; a `no` on part (1 of 3 read) is not guaranteed by the plans that did not read, which the *Unknown values* rows
explain only per cycle. I read the reading as permitted by the binding choice and visible, so not a defect; a `no` that reads `no (1 of 3)` or `unknown` below a share of plans read would keep the table from looking measured. Minor.

### Minor 4 — the docstring's list of the git commands omits `diff`

Place: `audit_count.py:113-114`, "Git runs only to read: `rev-parse`, `log`, `diff-tree`, `ls-tree`, `cat-file` and `merge-base`". The new code also runs `git diff --quiet` (`Ancestry.changed`, line 1467, named in the series paragraph above) and `log -1 --format=%ct`. Invariant `script-subprocesses` (git only) is kept; the docstring list is incomplete. Minor.

## The executor's four questions

1. **The price-list boundary as a unit test of `series_boundary` (`PriceBoundary`) instead of a subprocess test — sound.** One run reads one price list (`--prices`), and `Version.price` is that list's date for every version, so the boundary cannot fire inside a run; every cost of a result is priced at the one list, so the results of two lists are two files, each its own series by its *Price list* column. WAY-338's case ("the cost of cycles priced by two lists is shown as two series")
   is therefore carried by the result per list; the unit test calls the function with two versions of different lists and checks the reason. Not a defect; the code path is dead in a run, and the docstring says "this never splits a run".
2. **20 series for 53 versions of the-way's history, Q3 `unknown` everywhere — the reading is sound; the outcome is a limit for the orchestrator and the human, not a defect of the code.** I ran the command on this worktree (temporary locations file, register and results; stdin closed): exit 0, 71 cycles, **20 series, 53 version rows**, 15 s; confirms the report. The rule is the binding choice 3(c) and the docstring states that it errs toward fewer comparisons. The consequence is that, while the reviewed paths change at nearly every merge (and the costs are known only for cycles of the new `stages.md` form), the question "does the cost fall" will rarely have an answer; a finer rule (the form of the report, not any change of the files) is a later decision.
3. **The planned-slices count as exactly one standalone figure before `slices` — sound as a guard, with the gap of Minor 1.** It is safer than "the first integer", which would read 3 in `3 rows, 11 slices`; a figure immediately before the word would be tighter still.
4. **Sums over the cycles whose plan reads, shown as `k of m` — permitted by the binding choice and visible; see Minor 3.**

## The brief's lessons, checked in the new code

- **Backtracking patterns.** `FIGURE = (?<![A-Za-z0-9])[0-9]{1,6}(?![A-Za-z0-9])` takes at most six steps per position and its lookbehind fails fast inside a digit run; `SLICES_WORD` is a literal; no nested repetition is added. The test with a 200,000-digit *Plan* figure passes (`1 of 2`, no stall).
- **Unguarded number and date conversions.** `int(figures[0])` is a figure of at most six digits; `Ancestry.stamp` converts `%ct` in `try` (`ValueError` is caught; a non-number gives "the date of the commit is not a number") and `committed_date` catches the out-of-range values. Scratch: a commit dated `99999999999999` gives "the commit's date lies outside the years the command can read", a commit dated `-5` gives "not a number"; both cycles go to *No version* with a reason and the run exits 0.
  The median uses `Decimal` over costs already below the ceiling of 10^18, `money()` quantizes inside the precision. A cost, a count or a date of the record is never converted without a guard.
- **Cells and copied text.** Version rows pass `table()` and so `cell()`; the series reason is one of four constant sentences; the unknown rows carry constants, a commit hash and a git reason that passes `cell()`. The text of *Discarded attempt* and *Plan* is only matched, never copied (scratch: a discarded attempt with ESC, `|` and a clear-screen sequence leaves the result without a non-printable character).
- **Size cap and work.** The record read stays under the 4 MiB cap. `item_texts` reads each item down to the next margin line, linear overall; a record with a doubled item is `unknown`. Versions are grouped by a dictionary; the work is linear in cycles and versions: 40 versions 9.7 s, 120 versions 29.6 s on temporary repositories (0.25 s per version, git calls only), no quadratic grouping. A register of 10,000 distinct pins would take about 40 minutes (git calls, as for reading each cycle), unbounded but linear.
- **One cycle or version aborting the run.** Each failure is `unknown` for that cycle or version (no version); `changed` returns `True` on a git failure; none raised in my runs.
- **A value given to git as an option.** `stamp` and `changed` receive full hashes returned by `rev-parse --disambiguate` after `--verify`, and fixed paths; `log` gets `--` after the hash, `diff` has `--` before the paths. No text of a record reaches git.
- **A refused or unreadable value shown as zero.** A median with no known cost is `unknown`; Q1 to Q3 are `yes`, `no` or `unknown` with a reason in *Unknown values* (the rows I looked at); a plan with no figure is left out of the sums with its reason. The only `no` with a partial basis is Minor 3.
- **Comparing numbers of two series.** Q3 compares a version only with the previous version of the same series (`previous` resets per series) and writes `unknown` when the previous median is unknown; each series is its own `### Series n` table; the *No version* cycles are in no table. The test `test_versions_compare_within_a_series_and_not_across_it` pins this (the third version's cost, lower than the second's, is not compared). I found no cell in which a number of one series stands beside a number of another.
- **Binding choices 1-7:** 1 (a version is the full commit the pin resolves to; unknown, unresolvable, ambiguous pins in no version): kept; 2 (ordered by committer date, ties by hash): kept; 3 (series by price list, class dates, tree of the five paths, `git diff --quiet`, failure counts as changed): kept, with the class-date rule inclusive of the version's day and a list of classes that does not read splitting at every pair (so one typo in the *Classes* table makes every version its own series and Q3 `unknown` — conservative, documented); 4: kept; 5 (median of known costs, even count mean, `Decimal`, the digits of *Cost*): kept; 6: kept except Minors 1-3; 7 (items read as slice 5 reads them, a doubled item `unknown`): kept.
- **The tests.** Mutations reported by the executor (the third, the class boundary, the median's middle, the tree check, the findings rule) each fail a test by its account; I read the tests and found them asserting values worked by hand in comments. The three tests that read *Unknown values* by position now select by value through `reasons_of`: each asserts the same text, so none is weakened (the value now selects its rows instead of taking the first row).

## Declined to judge

- The price list's figures, and the cost method (earlier slices).
- Slice 7's skill and its handling of the new section.
- Whether the series rule should be finer (a decision of the orchestrator and the human).
- The readings of an archive's *Review rounds* in prose (slice 4's rule, taken as given).

## Checks run

| Command | Exit |
|---|---|
| `git rev-parse HEAD`; `git log 7bb25c3..2e7168c`; `git diff 7bb25c3..2e7168c` (read whole) | 0 |
| `python -B gate/run_tests.py process-audit` (worktree, bytecode off) | 0 — 94 tests OK, 123 s |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 |
| `python -B process-audit/audit_count.py --locations <scratchpad>\run7\locations.json --today 2026-11-11 <&-` (temporary locations file naming this worktree as the-way's repository, a copy of the template as the register, a temporary results directory) | 0 — 71 cycles, 20 series, 53 version rows, 2 cycles in no version, 15 s |
| scratch `scratch8.py` (outside the worktree; temporary repositories through the tests' helpers): dates out of range, negated phrase, ESC and `\|` in an item, a plan with one unrelated figure, scaling to 40 and 120 versions | results as above |
| a scan of the archived records for both items `none` with fix rows in the slices table, `git show` | 4 records, 0 with a fix row |
| `git status --short` after the checks | empty |

Not run: the full suite; a run with 10,000 cycles (scaling shown to 120 versions, linear).

## Reaches beyond the handoff

- `task-cycle/record_template.md` lines 37-44 and 66-69 and `foundations/glossary.md` (open design choice, slice) — to judge the readings of the three items; both are named by the slice.
- The archive's `docs/task-cycles/*/cycle.md` by `git show` (names of items only).
- `task-cycle/cycle_stages.py`: not read; named only as a path in the series rule.

## Unread material

- `plan.md`; the reports of slices 4, 5 and the correction (shapes known from my earlier reviews of them).
- `audit_count.py` before the diff read as the diff and the code it calls; foundation entries WAY-38, WAY-48, WAY-332, WAY-334 and the three script invariants were read in the earlier reviews of this cycle and not again in full here; WAY-336 and WAY-338 whole.

## Searches not found or unclear

- A record with a *Discarded attempt* other than `none` or a *Slices returned too large* that lists entries: none in the archive (agrees with the executor); the `yes` and list readings are from the template and untested on real text.
- Whether the weekly configuration will always name the key `the-way` for the-way's own cycles (the executor's concern: under another key 37 cycles became *No version*): unclear, bears on slice 7.
