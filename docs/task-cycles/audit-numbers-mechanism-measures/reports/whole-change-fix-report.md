# Report — fix of the review's findings, the whole change

**Status:** done (M10 contested, with the reason the orchestrator ruled).

Worktree `the task's worktree`, branch `task/audit-numbers-mechanism-measures`, fix range from `1923ef446867b1b17a9ef749d9c811b1e2906c06`.

## Commits

1. `8bb47d5` — `foundations/decisions.md` (WAY-344 carve-out, WAY-350 registry sentence).
2. `91c5298` — `process-audit/SKILL.md`, `process-audit/price_list.md`, `process-audit/problem_register.md`, `task-cycle/skill/SKILL.md`, `task-cycle/record_template.md` (I1, M1, M5, M6).
3. `7380a5d` — `task-cycle/gate_times.py`, `task-cycle/test_gate_times.py` (M4).
4. `6f4982d` — `process-audit/audit_count.py`, `process-audit/test_audit_count.py` (M2, M7, M8, M11).
5. `1e2c028` — `task-cycle/cycle_measures.py`, `task-cycle/test_cycle_measures.py` (M9, M11, M12).

## Findings

- **I1** fixed. `process-audit/SKILL.md:197` now says the date "starts a new series of the cost and of no mechanism measure or gate time (WAY-339)". Wrapped to 100 columns. No test (prose).
- **I2** fixed. WAY-344 (`foundations/decisions.md`, binding paragraph, *Verification* complies and violates, *Rationale*) now says that a field an earlier form of a file never had is not missing where the file's other signs name that form, and that a file of the earlier form gives its values unknown with no `Error:` line and no change of the exit code. Edited in place; *Relations*, *Scope*, *Rejected* unchanged. Check: `python -B elements/common/foundation_check.py --skip-test-citations` exit 0 ("0 errors"). The existing test `test_neither_time_line_is_the_earlier_form_and_no_missing_field` pins the behaviour the entry now names.
- **M1** fixed. `process-audit/price_list.md` and `process-audit/problem_register.md` say "of the cost and of no mechanism measure or gate time".
- **M2** fixed. Module docstring of `process-audit/audit_count.py`: a paragraph on `mechanism_measures.md` and `gate_times.md` (fields, earlier form, limits, exit 1), the result description names the sections *Mechanism measures*, *Gate runs* and *Measure versions*, and the exit-code sentence names the three files. Prose, no test.
- **M3** fixed. One sentence in WAY-350: the registry of running gates is kept by the script in the user's own directory outside every repository, as an empty file for each run, made at its start and marked as ended at its end; a run not ended counts for at most six hours and an ended one is kept for a day. File names stay in the code.
- **M4** fixed. `task-cycle/gate_times.py`: `MAX_DIRECTORIES = 50` (the audit's number) and `DIRECTORY_CAP = 200` (the audit's `TEXT_CAP`). A run lists at most 50 blocks; a directory cell is cut at 200 characters ending in `…`; blocks after the fiftieth are not stored, and a last row of the run reads `… <n> more directories not listed` with `—` as seconds. A `Ran` line after a block not listed is not given to the last block listed (it would be a wrong time). Tests (`CapTest` in `task-cycle/test_gate_times.py`) failed first, then passed: flood of 2000 blocks gives 51 rows and a file under 10,000 bytes; exactly 50 blocks give no cut row; the time after a block not listed; a 5000-character line; a 200-character line kept whole. The flood of the finding (200,000 blocks, `--output`, `--registry`) now gives exit 0 and a 3,214-byte file; the audit's `read_gate` reads that file as 1 run, 50 directories, with its own reason "more than 50 directories: the rest are not listed", and nothing as zero. Mutation (remove the `or self.not_listed` guard) makes the time test fail.
- **M5** fixed. `task-cycle/skill/SKILL.md` step 4 says "a separate checkout of the base commit directly under the worktree's ignored `.runs/`"; the same step's lines are wrapped.
- **M6** fixed. `task-cycle/record_template.md` sentence wrapped.
- **M7** fixed. `GATE_CODE = [0-9]{1,10}` (a Windows code up to 4294967295). Tests `test_an_exit_code_above_255_is_read_as_written` (failed first) and `test_an_exit_code_that_is_not_a_whole_number_is_unknown` (`-1`).
- **M8** fixed, both parts. (a) A row after a line that ends the table (outside a code fence) is still not read, but *Unknown values* now says "`gate_times.md` holds a row after a line that is not a row of the table: the rows after it are not read"; text after the table with no row says nothing. (b) The two optional files are read through `guarded_optional`, each with its own `try`; a git failure on one gives its reason and leaves `cycle.md` and `stages.md` read. Tests (failed first): `test_a_row_after_a_line_that_ends_the_table_is_not_read_and_says_so`, `test_text_after_the_table_with_no_row_in_it_says_nothing`, `test_a_git_failure_on_the_gate_file_leaves_the_files_that_were_read` (calls `fill` with a `Git` that fails `cat-file` of the gate blob only).
- **M9** fixed. `task-cycle/cycle_measures.py` `codex_subagents` takes `since`, the time of the orchestrator's first call (None where it has none, so every rollout is read): a rollout last modified more than a second before it is not read, as `cycle_stages.py:443-452` does with the orchestrator's first turn. Every other rollout keeps the loud failure. A second rollout with an id already found is left out and a `Warning:` line on stderr names its file (exit stays 0). Tests `CodexSearchTest` (the two failing ones failed first): old unreadable rollout is skipped; a newer one with an unreadable first line gives exit 2 naming it; a duplicate gives a warning and one agent. The docstring says it.
- **M10** contested, as the orchestrator ruled: the two sentences of the plan are not a product file; both behaviours are tested as they are; the code is left as it is. Evidence: `process-audit/audit_count.py:2273-2285` area and `:1295-1315` unchanged by this fix.
- **M11** fixed: wrapped the lines of `audit_count.py` named by the finding (37-38, 143, 190, 216, 1412, the comment at the refused row, the `median_text` docstring); `read_time` docstring now says a naive time is taken as UTC and another offset is kept; `assert_error_names` takes no code; a test for the meta file nested too deeply (`RecursionError` branch); two blank lines before `class CodexTest`; the cache figures of `Call` are ints (0 for a Codex call) and "unknown" is held once, in `Agent.cache_known`.
- **M12** fixed with tests only (`InterleavedTest`): rewrites paired within an agent when an orchestrator and a subagent call in turn (8000 and 5000 by hand), and the orchestrator's first, middle and last call over two sessions of one tool by time (100, 300, 500 by hand). They pass on the code as it was; no code changed for them.

## Checks

Each as command and exit code, run from the worktree root; the same results hold on the final head `1e2c028`.

| Command | Exit |
|---|---|
| `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"` (49 tests) | 0 |
| `python -B -m unittest discover -s task-cycle -p "test_gate_times.py"` (22 tests) | 0 |
| `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` (177 tests, 286 s, in the background, ended before the commits) | 0 |
| `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` (after the commits) | 0 |
| `python -B -m unittest discover -s elements/part-map -p "test_cross_part_imports.py"` (39 tests) | 0 |
| `python -B -m unittest discover -s task-cycle -p "test_remarks_check.py"` (59 tests) | 0 |
| `python -B -m unittest discover -s gate -p "test_skills_reach_the_way_sessions.py"` (2 tests) | 0 |
| `python -B instruction-files/check_instructions.py .` (0 errors, 0 warnings, 3 info) | 0 |
| `python -B elements/common/foundation_check.py --skip-test-citations` (0 errors) | 0 |
| `git diff --quiet 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` | 0 |

Tests written first and seen failing before the code: the five `CapTest` tests of the gate script (3 failed or errored), the M7 exit-code test, the M8 tests (row after the table, git failure) and the two M9 tests (older rollout, duplicate). The product's gate was not run. The check_instructions exit on the base was not measured separately; it is 0 on the head.

## Own-work check

Requirement most likely not met: M4's "nothing counted as zero", read through the audit. Check: wrote the flood of the finding with the script, then read the file with the audit's `read_gate`. Result: 1 run, 50 directories, the audit's reason, no zero.

## Reaches beyond the dispatch

- `process-audit/audit_count.py` `TEXT_CAP` (200) and `MAX_DIRECTORIES` (50), read to choose the writer's numbers.
- `task-cycle/cycle_stages.py:443-452`, read only (not touched).
- `foundations/decisions.md` WAY-140 read for M3 (the sentence went to WAY-350 as the ruling says).

## Entries' meaning sentences

- WAY-344, marked `the cycle's` (words an approved decision a little wider; for the human's list, WAY-114).
  - English: A field that an earlier form of a file never had is not missing where the file's other signs name that form, so the count of the audit gives the values that need it as unknown and ends with no `Error:` line.
  - Polish: Pole, którego wcześniejsza postać pliku nigdy nie miała, nie jest brakującym, gdy inne oznaki pliku wskazują tę postać — liczenie audytu podaje wtedy wartości, które go potrzebują, jako nieznane i nie kończy się linią `Error:`.
- WAY-350 (not a change of meaning: it states where the registry of running gates is kept and its limits as the script has them; no `the cycle's` mark).
  - English: The script keeps the record of running gates in the user's own directory outside every repository, one empty file for each run, and counts a run that has not ended for at most six hours and keeps an ended one for a day.
  - Polish: Skrypt trzyma rejestr działających bramek w katalogu użytkownika poza każdym repozytorium, jeden pusty plik na uruchomienie; uruchomienie, które się nie skończyło, liczy co najwyżej sześć godzin, a zakończone przechowuje przez dobę.

## Unread material

- `reports/whole-change-review-report.md` (named by the handoff, not read; the findings file holds its words).
- `task.md`, `plan.md` (named, not read; the handoff's rulings were enough).
- `elements/decisions/skill/read.md` and `decide_entry.md` were read; `elements/decisions/template.md` was read only in "Changing a decision" (grep), `elements/common/rules.md` and `way_of_working.md` only in part.

## Searches not found or unclear

- The handoff gives the report path under `.runs/task-cycles/...` of the worktree; the `.runs` directory of the main checkout (`.runs/task-cycles/...`) does not hold the cycle, only the worktree's does. Not a problem, noted.
- "Slice 2 Minor 3: `unknown` held twice in `Call` and in `Agent.cache_known`" was read as the double encoding of the unknown cache figures; fixed so. If the reviewer meant the literal `"unknown"` against the constant `UNKNOWN` in `mean`, `share` and `position`, that is not changed.
- WAY-263 text was not read; the grading words come from the findings file.

## Choices, with the way rejected and its cost if wrong

- M4 cut: 50 blocks plus a cut row (the row is the 51st, so the audit drops it and gives its own "more than 50 directories" reason). Rejected: 49 blocks plus the cut row (the audit would read the row as a directory with unknown seconds and a misleading reason; costs the 50th real directory). Cost if wrong: the cut row is invisible to the audit, visible only to a human reading the file.
- M8(a): a reason, not reading past the break. Rejected: reading every `|` line to the end (could take an unrelated later table for runs). Cost if wrong: runs after a blank line stay unread (flagged).
- M9 duplicate: a `Warning:` on stderr, not a line in the file. Rejected: a counted line in `mechanism_measures.md` (changes the file's form). Cost if wrong: the note does not survive in the record.
- M9 floor: the first call of the orchestrator, not its first turn (the script has calls, not turns); a subagent cannot exist before the orchestrator's first call, so the floor is never later than needed. Cost if wrong: a subagent rollout with an mtime before the orchestrator's first call (clock skew over a second) is skipped.
- M11 `Call`: ints with 0 for Codex, the knowledge held in `Agent.cache_known`. Rejected: `None` in `Call` and a derived `cache_known` (an agent with no calls would read as known and give 0). Cost if wrong: a future unguarded use of a Codex call's cache figure reads 0 silently.
- M7 pattern: 10 digits. Rejected: unbounded digits (a limit keeps the cell bounded). Cost if wrong: a code above 4294967295 reads as unknown with the "not a whole number" reason.
- WAY-344 words: edited the entry itself rather than WAY-352, as the ruling says; *Relations* not changed.
