# Findings of the review of slice 4 (`116f319..269d7be`, `FAIL 269d7be710ca9a391a57975fb9ee3a2c2f4f8aec`) — the reviewer's words

Full review: `.runs/task-cycles/weekly-process-audit/reports/review_slice4_report.md`

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

