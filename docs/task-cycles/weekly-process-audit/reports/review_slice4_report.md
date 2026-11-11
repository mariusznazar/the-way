FAIL 269d7be710ca9a391a57975fb9ee3a2c2f4f8aec

# Review of slice 4 — the cost of a cycle at constant prices

Range `116f319..269d7be` (one commit, `git rev-parse HEAD` = `269d7be710ca9a391a57975fb9ee3a2c2f4f8aec`, confirmed).
Worktree `the worktree of the task`, read only; `git status --short` stayed empty.
Counts: 2 blocking (Important), 4 Minor, 1 out of scope.

## Blocking findings

### 1. Important — the share of fix rounds can be silently wrong: the tie is by count of stage names that hold the word `fix`

Place: `process-audit/audit_count.py:663-719` (`stage_kind`, the tie in `add_cost`),
and the docstring at lines 55-64 and the report's claim "orchestrator stretches are in no fix round".

What is wrong. A stage counts as a fix stage when its name holds the word `fix` and not `review`, as a review of a fix when it holds
both. The record side is the number of report paths in *Events* with the words `fix` and `report`. The two sides are tied only
by equal counts. When the counts agree by coincidence, the share is given, and it is the share of whichever stages carry the word.
Two ways, both shown by a run:

- A cycle of a task whose own stages are named with the word (an author "Author: fix the login bug", a reviewer "Review the fix of the
  login bug"), while the real fix and the review of it are later turns of those same subagents (the form the archived cycles
  use: the fix is the author "resumed"). Names stripped of ` — turn n` collapse, so the whole author and the whole reviewer
  count as the fix round. Run: stages priced 0.786300 USD, fix rounds `1`, share `99.6%`. The fix turns themselves cost 0.000
  7 USD (turn 2 of the author, 400+40 tokens, and turn 2 of the reviewer, 300+30 tokens), so the true share is about 0.1%. Nothing is `unknown`.
- The orchestrator's rows `orchestrator while in parallel: <names of the subagents running>` (written by `task-cycle/cycle_stages.py`
  `build_rows`, common in the archive: dozens of such rows) hold the names of the subagents. When one of those names holds
  `fix`, the row is itself taken for a fix stage and its tokens enter the numerator, against the docstring ("the orchestrator's own
  stretches are in no round") and the report. Run: no fix subagent at all, two parallel rows naming "Fix typos" and "Review the fix", record
  with one fix report and one review report: fix rounds `1`, share `49.7%`, nothing `unknown`.

Why it matters. The slice goal and the review brief ask that a share the command cannot tie to the rounds is `unknown`, and the
brief asks specifically whether a crafted record can make it silently wrong. It can, and ordinary naming does it without craft. The same
rule also makes the usual names fail loudly instead: in the archive the fix stages are named "Fix review findings", "Fix the
review's blocking findings" (hold `review`, so they count as a review of a fix; run D gives `unknown`) or are resumed turns of
the author (no `fix` in the name; the counts differ, `unknown`). So the share is mostly `unknown`, and where it is given it can be wrong in
either direction with no signal. The task (`task.md:30` and the settlement row 8) asks for the share of fix rounds as a measure the human weighs; a
number that is wrong without a sign is worse than `unknown`. The slice text also says the rounds are "as the record's *Review rounds* and *Events* name them";
only *Events* is read.

Evidence: scratch runs in `a scratch file outside the repository`
(scenarios B, C, D) and `...\scratchpad\scratch2.py` (the parallel rows scenario), run on temporary repositories through the tests' own helpers.
The existing tests have no case with a parallel row or with resumed turns, so the 55 tests pass.

Direction of a fix (the author's choice): exclude rows whose name starts with `orchestrator`; give the share only where each fix
and review stage can be tied by something stronger than a word count (e.g. the stage's name appearing in the record's *Events* row of the
fix), else `unknown`.

### 2. Important — a `stages.md` whose section holds no tokens gives a cost of `0.000000`, not `unknown`

Place: `process-audit/audit_count.py:628-648` (`priced`, the `NO_MODEL` branch)
and `:674-683` (`add_cost`: only the share is made `unknown` for a total of zero).

What is wrong. A row with the model `—` and zero tokens is priced as zero. A section whose every row is such a row
(`cycle_stages.py` writes `—` with zero counts for a stage it found no usage for, and lists that case in its Warnings, which the command does
not read) gives the cost `0.000000` in the *Cost* table, with the share `unknown` in the same row. Run A: one row `| 1 | orchestrator | ... | — | 0 | 0 | 0 |`
gives `Cost (USD)` = `0.000000`.

Why it matters. The slice goal and the task say "a `stages.md` without each stage's tokens by model and kind ... gives `unknown` with its reason, never a
cost of zero". A zero enters the series that slice 6 takes the median of and shows as a true figure. The command already treats the
zero total as not usable for the share; the cost beside it is inconsistent with that.

Evidence: scratch scenario A. No test covers it (the sixteen-digit, ceiling, model-lacking and earlier-form tests do not).

## Minor findings

### 3. Minor — untrusted names are copied whole into the *Unknown values* reasons, twice per cycle, with no cap

Place: `audit_count.py:640-646` (`priced` reasons carry `row.name` and `row.model`), rendered at `:930` through `cell()`.
A model name of 2,000,000 characters in `stages.md` (inside the 4 MiB read cap) produced a 4,001,839-byte result (scenario F): two rows of the reason.
Control characters, escape sequences, a right-to-left mark and a bar are neutralised correctly by `cell()` (scenario with `x\|y<ESC>[31m<U+202E>\`:
written as `x\\x7cy\x1b[31m\u202e\`), so this is a size matter, not an injection. A cap on the quoted name (say 80 characters, with a sign it was cut) keeps the
result readable.

### 4. Minor — a price cell that is not a number and not `—` means "no price" instead of refusing the list

Place: `audit_count.py:529-531` (`numbers = [Decimal(...) if PRICE.fullmatch(...) else None ...]`).
`1e9`, a full-width digit or a typo in the-way's own price list makes the model unpriced, and every cycle that used it is `unknown` with the reason
"the price list gives no price for model", pointing away from the list. Cells with the wrong number of cells and a bad date do refuse the run (scratch: exit 2),
so only the cell content is lenient. The list is a tracked file of the-way, so the effect is limited. A cell other than `—` that is no price should be an error naming the model.

### 5. Minor — the four narrowed `Times` tests no longer notice an unexpected unknown row of another value

Place: `process-audit/test_audit_count.py` (`Times.time_rows` and the four tests).
What they protect: that the two times are read or given as `unknown` with the right reason. That is kept: the assertions on the time rows are unchanged in
content, and the cost rows added for the same `stages.md` are the reason the old whole-table assertions fail. What is lost: `assertEqual([], unknown)` in
`test_the_times_of_stages_md` also asserted that *Process pin* and *Remarks* were not unknown for the record; now a stray unknown of those goes unseen by
this test (other tests cover the pin and the remarks). Asserting that every other row is one of `Cost` / `Fix rounds share` would keep that.
It does not weaken the time protection; graded Minor.

### 6. Minor — gaps in the tests of the trust boundary the handoff lists

The handoff says each lesson has a test. Present: a sixteen-digit count, the ceiling, cached above input, a model the list lacks, a doubled price model.
Absent: a stage or model name with a bar, a control character or an escape sequence in a reason; a very long run in the new table/fix-name parsing
(I ran 150,000 rows / 10 MB in 0.6 s, and `table_cells`, `stage_kind` and `TURN_SUFFIX` are linear by reading, so no defect, only no test);
a price list with a non-number cell, a doubled or invalid `List date`, an oversized list; a zero-token section (finding 2); a parallel
orchestrator row (finding 1); a `stages.md` or a record whose section appears twice. Also an `## Events` table with only its header gives `0` rounds and `0.0%` (scenario E),
indistinguishable from a cycle without fix rounds; it follows the form of the record and is noted, not graded further.

## Out of scope

### 7. Out of scope — `cycle_stages.py` writes `—` with zero counts for a stage with no usage found

Place: `task-cycle/cycle_stages.py:~775` (`or [("—", Usage())]`). A stage with no readable usage
and a stage with truly no tokens are the same row, so the audit cannot tell an under-count from a zero (it feeds finding 2 only in part: an all-`—`
section is fixable in the audit; a single `—` row among priced rows is a possible under-count that only the stage report can mark). Slice 2's file; named for the
orchestrator, not graded as a defect of this slice.

## Checks of the brief

- Trust boundary: `process-audit/audit_count.py` — hostile input checked: control characters/escapes/bar in names and models (neutralised by `cell()`; scenario with ESC, U+202E, backslash, bar),
  tokens with commas/unicode digits/negative/16 digits (all `unknown`, no abort), oversized price or section (caps hold; the price list has the 4 MiB cap, `stages.md` the copy cap),
  doubled section/price model (unknown/refused), malformed table rows (unknown with reason), backtracking (none: the new patterns are anchored and bounded, tables are cut by a linear
  scanner; 10 MB / 150,000 rows in 0.6 s), conversions (`int` on at most 15 ASCII digits, `Decimal` of a bounded pattern, ceiling 10^18 keeps `quantize` inside the precision),
  git (no new git call; the commit/blob ids are those of slice 3), what the command runs (no new subprocess; `decimal` only; invariants `script-language`, `script-imports`,
  `script-subprocesses` hold), a failure of one cycle (`add_cost` has no path that raises on the inputs tried; each case is `unknown` for that cycle).
- Price list: every figure of `process-audit/price_list.md` equals `.runs/task-cycles/weekly-process-audit/reports/prices_fetched.md` (8 models x input, cached input, output, and the four cache-write
  figures; page addresses and the date 2026-11-11 equal). No price in the list is absent from that file. I cannot check the providers' pages themselves.
- Decisions: WAY-334 (cost as an amount at one dated list and the share of fix rounds, no size divisor) — complied with in form; the share's reliability is finding 1.
  WAY-336 — the list's date is in each cost row (*Price list*); the command computes under one list per run.
  WAY-38 / WAY-48 / WAY-89 and the three invariants — comply. No invariant test is changed. No reserved choice taken (standard library `decimal`).
- Changed tests: finding 5.

## Declined to judge

- Whether the figures on the providers' pages are as the orchestrator read them (cannot reach the pages); whether the OpenAI `$` means USD (the list states the reading).
- The pricing of cache writes as input (the orchestrator's choice Q9, stated in the docstring and the list).
- Slice 5 and 6 use of the *Cost* section; the median over a series (slice 6).
- The short-context rows of the list when a call is longer than 100,000 / 272K tokens (the list states it).

## Checks run

| Command | Exit |
|---|---|
| `git rev-parse HEAD`; `git log 116f319..269d7be`; `git diff 116f319..269d7be` (read whole) | 0 |
| `python -B gate/run_tests.py process-audit` (worktree, bytecode off) | 0 — 55 tests OK, 40 s |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 — checked 279 files, 0 listed |
| `python -B process-audit/audit_count.py --help` | 0 |
| scratch scenarios A–H (`scratchpad\scratch_review4.py`, `scratch2.py`, outside the worktree, temporary repositories through the tests' helpers) | findings 1, 2, 3, scenario results as above; 150,000 rows in 0.6 s |
| `git status --short` after the checks | empty (worktree unchanged) |

Not run: the full suite (the cycle's own run); `elements/common/foundation_check.py` (the range touches no foundation file); a run on the real repository (the executor's; not repeated).

## Reaches beyond the dispatch

- `task-cycle/cycle_stages.py` (`build_rows`, `report`, lines ~500-590 and ~655-790) — to learn what rows and names `stages.md` holds (the parallel rows, the `—` row, the turn suffix).
- `task-cycle/record_template.md` (the *Review rounds* item and the *Events* table) — to see what the record names for rounds; named by the slice's *Read*, read in part.
- Archived `stages.md` and `cycle.md` of earlier cycles in history (`git show` of `guidelines-departure`, `request-decision-groups`, `unread-material`; names of all archived stage rows by `git log --all`) — only names and forms, to see how real fix rounds are named.
- `foundations/part_map.md` (grep of `audit_count`/`price_list`) — to check the boundary entry.

## Unread material

- `plan.md`: not read (the handoff gives the slice and the rows). `task.md`: read the passages named (`23-36`, `91-108` in the slice; I read `20-40` and `88-110`), not the whole file.
- `task-cycle/record_template.md` read in part (the *Review rounds* item and *Events*); `task-cycle/cycle_stages.py` read in the ranges above, not whole.
- `process-audit/audit_count.py` read whole in the changed ranges and the code they call (lines 100-720, 720-987); lines 1-100 (docstring) read as part of the diff.
- Foundation entries WAY-38, WAY-48, WAY-89, WAY-334, WAY-336 and the three invariants read whole at the current ranges. WAY-334 / 336 quoted above.
- The executor's slice 2 and slice 3 reports: not read.

## Searches not found or unclear

- No archived `stages.md` holds the per-model section with a fix round, so the naming of real fix stages could only be judged from the older form's stage names.
- Whether the orchestrator will name fix subagents with `fix` in future cycles is not settled anywhere I found; the method files were not searched for a naming rule.
- The brief says the record's *Review rounds* is read; the command reads only *Events* (finding 1).
