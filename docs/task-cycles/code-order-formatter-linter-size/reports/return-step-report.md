# Return step report - code-order-formatter-linter-size

**Status:** done with concerns (one concern outside the step's boundary, see Problems).

**Base:** `2e066ab4f6f7a0b30b29ed09bbafbaf61b6fea38`. **Commit:** `d41712a6` (one correction, below).

## Foundation compared with code

Entries and files compared: decisions WAY-382, WAY-385, WAY-379 (*Verification*), WAY-145, WAY-350, WAY-339,
WAY-09 (*Verification*), and the ones the task names (WAY-205, WAY-51, WAY-380, WAY-381, WAY-16, WAY-08, WAY-03,
WAY-233, WAY-95); invariants `formatter-layout`, `own-foundation-check-report`, `ruff-blocking-rules`,
`function-and-file-size`, `gate-times-refuses-impossible-entry`, `audit-series-script-paths`, and, because their
sentences name a place that moved, `cycle-stages-refuses-crafted-names` and `shared-module-import-runs-nothing`; the
part map (`repository`, `task-cycle`, `process-audit`, and every part that holds Python code, `decisions`,
`invariants`); `guidelines/coding.md`, `guidelines/coding-shared-module.md`, `guidelines/coding-measuring-report.md`,
`README.md`, `installation/README.md`, `ruff.toml`, `.git-blame-ignore-revs`, `process-audit/SKILL.md`,
`process-audit/price_list.md`, `project-level/lead/*.md`; and the code: `agent-instructions/test_linter_invariant.py`
(class `Formatter`), `agent-instructions/test_size_invariant.py`, `elements/common/test_foundation_check.py` (both
tests under "the-way's own foundation"), `process-audit/test_audit_series_scripts.py`, `task-cycle/gate_times.py`,
the new modules.

What matched (evidence):

- `.git-blame-ignore-revs` holds `015ce05c2a7209af7db05873775f561acdae408f`, which `git rev-parse 015ce05c` gives, the
  formatter-only commit; the part map lists the file under `repository`; every file of every *Files* line stands
  (`python -B gate/run_tests.py elements/part-map` exits 0, 40 tests, among them `cross-part-imports` and the file
  assignment).
- *Depends on* against the imports of the new modules: `audit_shared`, `record_reading`, `problem_register`,
  `version_analysis`, `audit_report` import only each other, `stage_pricing`, `record_items` (process-audit) and
  `remarks_check` (task-cycle); `process-audit` depends on `task-cycle`, so the line holds. `stage_transcripts.py`
  imports the standard library only. The trust-boundary lists name `stage_transcripts.py`, `problem_register.py`,
  `record_reading.py` and `audit_shared.py`, whose docstrings name untrusted input (WAY-48), and not
  `version_analysis.py` and `audit_report.py`, which the plan's choice 13 keeps off the list.
- Thresholds: `test_size_invariant.py` holds `FUNCTION_LIMIT = 110`, `FILE_LIMIT = 1200`, its `decision:` line quotes
  WAY-385's new opening; no `expectedFailure` stands in it or in `test_linter_invariant.py`; both invariants read
  `Violated: no`. `python -B gate/run_tests.py agent-instructions` exits 0 (52 tests, none skipped).
- `formatter-layout`'s sentence and the test agree: the tracked `.py` files of the ten directories (a search of
  `git ls-files '*.py'` finds no `.py` file outside them), `ruff format --check --config ruff.toml`, and a `tokenize`
  scan for `fmt:` and `yapf:` comments. `own-foundation-check-report`'s test runs the script with no switch and asserts
  exit code 0.
- WAY-338, WAY-342, WAY-343, WAY-346, WAY-348 and WAY-352 (the withdrawn rows "its rule stands in
  `process-audit/audit_count.py` / `task-cycle/cycle_stages.py`"): the rules stand in the docstrings of those two
  files, which the division left in them, so the rows hold.
- No moved name stands in any `.md` file of the repository (a search of every function and class name of the six new
  modules, in `.md` files outside `.claude/` and `.agents/`, finds none); no `audit_count.<name>` or `cycle_stages.<name>`
  reference stands in a `.md` file.
- The nine `.md` places that name `task-cycle/cycle_stages.py`: where it is the script that measures the cost (WAY-339
  at line 8403, `audit-series-script-paths`, `process-audit/SKILL.md:54`, `process-audit/price_list.md:22`) they name
  `task-cycle/stage_transcripts.py` too; where it writes `stages.md` or the record's files
  (`task-cycle/skill/SKILL.md` lines 319, 483, 641, 650; `task-cycle/skill/blocked_finding.md:15`;
  `task-cycle/skill/reserved_return.md:55`) they are left, as the handoff gives. The remaining WAY-339 sentences that
  say "the script that measures the cost" without a path stand after the sentence that names both files.
  `guidelines/coding-measuring-report.md` lists `task-cycle/cycle_stages.py` as a file of its kind; the plan's choice 12
  keeps rows for `stage_transcripts.py` out, as for `stage_pricing.py`. `invariants.md:520` (`cycle-stages-refuses-crafted-names`)
  names the description of `cycle_stages.py`, which still holds the form of *Files named* (line 69).
- `process-audit/test_audit_series_scripts.py`'s description names `version_analysis.py` as the reader and both cost
  files, as `audit-series-script-paths` does; its two expected values hold `COST_SCRIPTS` and the two cost paths with
  the cause in a comment.
- Old phrases ("80 lines", "1000 lines", "known violation", "expected failure", "none - WAY-382", "settings of the
  linter", "no formatter", "80/1000"): the only hits are the general text of WAY-51, WAY-205, WAY-365, the templates
  and `README.md:82` (all about the mechanism, not about the-way's own state) and the historical measurements in the
  *Rationale* and *Rejected* of WAY-382 and WAY-385 (counted "before the formatter" there). `README.md`'s
  "Installing the linter" says the same Ruff formats and what the formatter covers, as the task gives.
- Word `entry` in the places the change renamed: WAY-145 and its *Verification* ("a line in the plan's log of changes",
  "no line in the log"), WAY-350 ("a file whose times cannot be"), `gate-times-refuses-impossible-entry` ("a file of its
  registry"), `project-level/lead/{SKILL,answering,conversation_template}.md`, `task-cycle/gate_times.py`,
  `task-cycle/test_gate_times.py`, `process-audit/test_record_items.py` carry the new word. `entry` in the remaining
  `.md` places of `task-cycle` and `process-audit` means an entry of the foundation. Uses that stay by the task (a
  tree entry of git, an entry point, a transcript entry, `entries none` as data of a record line) were left.
- The `decision:` lines that quote WAY-339 (`process-audit/test_audit_count.py`, `task-cycle/test_cycle_stages.py`)
  and WAY-385 (`agent-instructions/test_size_invariant.py:58`) still match a binding sentence: `python -B
  elements/common/foundation_check.py` exits 0 ("0 errors").

What no longer matched, and its correction:

1. `guidelines/coding.md`, `### Formatter`: the last sentence of the paragraph ran on to 150 characters beside a
   paragraph wrapped at 100, with "(WAY-16)." alone on the next line. Re-wrapped; no word changed. Committed as
   `d41712a6` (path `guidelines/coding.md` only). No test holds this sentence.

Nothing else no longer matched.

## Written or changed

- Decisions written or changed: none.
- Invariants written or changed: none.
- Environment facts: none written. Reason, as `elements/environment-facts/skill/SKILL.md` and the template's *Which
  facts are written* give: the change rests on Ruff's behaviour on `fmt:` and `yapf:` comments, on Markdown examples
  and on the `except` clauses of Python 3.14, but no sentence of WAY-382 or of `formatter-layout` would be called into
  question if that behaviour changed: the ban on the comments is a rule the human chose, and its test finds the
  comments itself with `tokenize` and not by what Ruff does with them; the layout is "as the formatter leaves it",
  whatever that is for `except`; the exclusion of Markdown stands in `ruff.toml` and in the test's own file list. A
  fact about what runs an invariant's test is no fact (WAY-73), and WAY-380's `--ignore-noqa` rests on no fact of its
  own either. A fact would need a quoted source and a read date, which this step could not take from memory
  (the source discipline). See the concern in Problems.
- Glossary terms: none (WAY-95: `entry` keeps its ordinary meaning and gets none).
- Part-map changes: none by this step (the change's own `repository`, `task-cycle` and `process-audit` edits matched
  the code).
- Projected entries written whole or in part: none (the task has none).
- Rows of *Settlements to record*: rows 1, 2, 4 and 5 stand as sentences of WAY-382 (rows 1, 4, 5) and WAY-385 (row 2),
  written by the foundation step; row 3 stands as the invariant `own-foundation-check-report`. This step wrote none and
  found none missing. A choice of the cycle that binds after the merge: none that the questions of the decisions
  template place in the log; the cycle's choices stay rows of the record.

## Own-work check (WAY-164)

- Requirement most likely not met: no sentence of the foundation or guidelines still states a number or state the
  change altered, and no moved place is still named in its old file.
- Check: searches of the old phrases and thresholds (above), a search of every moved function and class name in `.md`
  files, a read of each *Verification* and rationale that names a threshold, and the runs below.
- Showed: only the historical measurements remain; the one defect found was the wrapped line, fixed.

## Checks run

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (before and after the correction) | 0 ("0 errors") |
| `python -B gate/run_tests.py elements/part-map` | 0 (40 tests) |
| `python -B gate/run_tests.py agent-instructions` (before and after the correction) | 0 (52 tests) |

The full gate was not run (the handoff forbids it). The tests that hold a sentence this step reworded: none (the
reworded sentence is held by no test).

## Problems and concerns

1. **Outside this step's boundary (code), for the orchestrator.** Four test names in `process-audit/test_audit_count.py`
   still use `entry` for what the record template calls a sub-item of an item, as the renamed tests of
   `process-audit/test_record_items.py` did: line 545 `..._is_not_among_its_entries`, line 556
   `..._are_not_its_entries`, line 1428 `test_an_entry_of_review_rounds_without_its_findings_file_...`, line 4986
   `test_crafted_entries_of_review_rounds_...`. The task's list of the places (point 8) names `test_record_items.py` and
   not `test_audit_count.py`, so they may be among the uses the task leaves; the return step cannot rename a test, and
   the sub-item sense (WAY-337 quotes "a sub-item for a review") makes them the same case. Decide: rename in a fix
   round, or leave. No foundation entry depends on it.
2. **Unsourced claim in a binding sentence.** WAY-382, `formatter-layout` and `guidelines/coding.md` forbid
   `yapf: disable` and `yapf: enable` as well as `fmt:` comments, which the task's row 5 does not name; the *Rationale*
   gives no reason for the two, and the foundation holds no source that Ruff's formatter honours them (commit
   `3b3008b3` added them from the formatter's behaviour). If the orchestrator wants that behaviour sourced, the way is a
   fact for the formatter's documentation (address of the 0.17.1 documentation, passage word for word, read date) named
   in WAY-382's *Based on*; I did not write it because the sentence stands without it (see Environment facts). Cost if
   left: none for the gate; the ban stays a rule a reader cannot check against a source.
3. WAY-385's sentence now depends on WAY-382 ("counted on the code as the formatter of WAY-382 leaves it") while its
   *Relations* name WAY-379, WAY-360, WAY-361 only. The check does not require it; noted, not changed.

## Reaches beyond the handoff

- Read `elements/environment-facts/skill/decide_entry.md` and the head of `elements/environment-facts/template.md` to
  decide the environment fact (the handoff names `SKILL.md`, whose step 2 points there).
- Read `product-guidelines/coding/template.md` lines 42 and 159-162 (the rule *Formatter*) and
  `guidelines/coding-measuring-report.md`, `guidelines/coding-shared-module.md`, WAY-391 and WAY-338/342/343/346/348/352
  rows of *Withdrawn identifiers*, to compare what the division moved.
- `.runs/task-cycles/.../task.md` and `plan.md`: read the task whole; the plan's *Foundation entries*, *Coverage*,
  *Choices* and Slice 17, not the other slices.

## Unread material

- `plan.md`: slices 1-16, 18, 19 not read (the handoff names the *Foundation entries* section and the *Choices*).
- The decisions WAY-205, WAY-51, WAY-380, WAY-381, WAY-16, WAY-08, WAY-03, WAY-233, WAY-95: read only the passages the
  task quotes, WAY-205 whole except its *Rationale* tail, WAY-380 and WAY-381 in the parts shown; not whole.
- WAY-339 read at its first paragraph and by search of "the script that measures the cost", not whole.
- The new modules were read for imports and docstring heads only (`audit_shared.py` head), not whole.
- `elements/*/SKILL.md` of decisions, invariants, glossary and part-map were not read: no entry of those elements was
  written.

## Searches not found or unclear

- Whether the cycle's choice to forbid `yapf:` comments has a source: not found in the foundation, the task or the plan
  (concern 2).
- Whether the four `test_audit_count.py` names (concern 1) are among the uses of `entry` that PR 148's findings list
  keeps: the PR description is not in the task's reach; not established.
- No place named the old function names of the moved code; a search found none.

## Working copies

Stood in `.runs/return-step/` of the worktree: `names.txt`, `names_u.txt` (names of the new modules' functions, for a
search) and `agent_instructions_run.txt` (a run's output). No worktree, clone or screenshot was made. All removed before
return; nothing remains.
