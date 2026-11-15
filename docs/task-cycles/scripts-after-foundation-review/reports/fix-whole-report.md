# Report — the fix of the Minor findings of the review of the whole change (M1 to M7)

**Status:** done

Worktree `the root of the task's worktree`, branch `task/scripts-after-foundation-review`, from head `84d062b817e2f8ba1cf141c0f9140cd5f178f61c`. Nothing of `.runs/` is committed.

## Commits (oldest first)

| Commit | Concern |
|---|---|
| `34491dc` | M5: `required_count` refuses a count of more than 15 digits; tests first |
| `b8ef139` | M2: the uses of "Markdown file" that the glossary definition moves |
| `8a0c159` | M4 and the two lines of M7 in `cycle_measures.py` |
| `04c86d1` | M1 and M3 (WAY-339, WAY-344) and the long lines of M7 in `foundations/decisions.md` and `elements/decisions/template.md` |
| `297c610` | M6 and the long lines and the blank line of M7 in `process-audit/` |
| `c43062b` | M7: the long lines of `task-cycle/skill/SKILL.md` and `task-cycle/tracked_private_paths_check.py` |

## Each finding

**M1 — fixed.** `foundations/decisions.md`, WAY-339, first paragraph: after "...the reason that the cycle changed the tool that wrote them" the clause "(the file of that tool is not read for that cycle, so no field of it is missing and no line `Error:` is given for it)". WAY-344, the sentence of the audit's exceptions: after "...with no line `Error:` and no change of the exit code" the clause "; a file of a tool that the cycle's own change changed is not read for that cycle (WAY-339), so none of its fields is missing and it gives no line `Error:`". I put the clause in WAY-344 as well, though the remedy names WAY-339 only, because the finding's heading names both entries and WAY-344 names no exception for a changed tool (a reader of it expects the `Error:` line). Both are clauses inside an existing sentence, so the first paragraph of each keeps its number of sentences. The meaning does not change: the code (`withdraw_values`, `audit_count.py:2557-2577`: it clears `cycle.missing` and the missing-field pairs of the file) and `MechanismMeasures.test_a_field_missing_from_the_file_of_a_changed_tool_is_not_read_and_ends_no_run` already follow it; no `questions` needed. Check: `python -B elements/common/foundation_check.py --skip-test-citations` exit 0 ("0 errors"), after the last edit of the decisions; `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` exit 0.

**M2 — fixed.** No behaviour changed in `foundation_check.py`; only words:
- `elements/common/foundation_check.py` module description (the former l. 35, 70, 72, 79, 92), the comment of `self.cited` (l. 410), the docstring of `list_invariants` (l. 750) and the message printed for an uncited `test` invariant (l. 856): "a file other than Markdown" became "a file whose name does not end in `.md`", "a Markdown file" became "a file whose name ends in `.md`". The paragraphs around them were rewrapped to 100 characters where a longer phrase pushed a line over. The message of l. 856 is asserted by no test (grep of `*.py`, `*.md`, `*.sh` for its text found nothing).
- `instruction-files/check_instructions.py` (module description l. 8 and docstring of `pointed_files`, l. 569) and `instruction-files/SKILL.md:277`: "the Markdown files the root names" became "the files whose name ends in `.md` or `.mdc` that the root names" (the code's `POINTED_SUFFIXES = (".md", ".mdc")` and the glossary entry *repository instruction file* say exactly this).
- `agent-instructions/test_instruction_files.py`: the module description (l. 4) and the docstring of `population` (l. 84) likewise. **Choice beyond the words:** the test's own constant was `MARKDOWN_ENDINGS = (".md", ".markdown")`, which is neither the old nor the new meaning (the glossary says `.md` or `.mdc`), so the words could not be made true by rewriting alone. I changed it to `POINTED_ENDINGS = (".md", ".mdc")` (renamed, since "Markdown" under the new term would mislead) and changed the fixture file `docs/other.markdown` to `docs/other.mdc` in the four places the test names it (the root text l. 256, the files of the fixture l. 266, `IMPORT_POPULATION` l. 291, the expected problems l. 300). Rejected: words only, leaving `.markdown` in the test — the docstring would then say `.mdc` while the test reads `.markdown`, and the test would hold a population the glossary does not give. Cost if wrong: the test's fixture covers `.mdc` instead of `.markdown`; no other test reads that fixture. `python -B gate/run_tests.py agent-instructions` was red once after the constant changed (the fixture still held `.markdown`, `population` lists differed) and green after the four places changed.
- The parallel task edits `foundation_check.py`: my change there is the 7 places above; the cycle that merges second reconciles.

**M3 — fixed.** `foundations/decisions.md`, WAY-339 *Verification*: a *complies* line "a cycle whose own change changes the script that measures the cost gives its cost and the share of its cost in fix rounds as unknown, with the reason that the cycle changed the tool that wrote them, and its other measures as they stand under the version it ran on" and the matching *violates* line "a cycle whose own change changes the script that measures the cost gets its cost counted as measured, in a series of its own or in the series of the version it ran on". The finding names the example lines ("a line for the script that measures the cost"); I added the pair, since the entry pairs each *complies* with a *violates* for the gate-times script. Which values `cycle_stages.py` measures (the times, the cost, the share of the cost in fix rounds) I took from the module description of `audit_count.py` (the paragraph "A cycle of the-way whose own change changes a tool...").

**M4 — fixed.** `task-cycle/cycle_measures.py`, module description and the docstring of `cache_sum`: "Codex's record gives no cache write" became "Codex's record has no cache write by lifetime and its write field is a constant 0, which measures nothing, so the cache figures of a Codex agent are unknown, never zero" (and the docstring in the same words, shorter). I did not state the 6347 records of executor 17's run; that is a count of one run, not of the code. I did not re-read a Codex record: the finding and executor 17's report are the source of "a constant 0" (see *Unread material*).

**M5 — fixed, test first.**
- Tests, `task-cycle/test_cycle_stages.py`, class `ClaudeFieldsTest`: `test_a_count_of_more_than_fifteen_digits_is_no_whole_number_and_one_of_fifteen_is` (each of the four counts and each of the two lifetimes at `10**15` ends with exit 2 and "is not a whole number"; each of the four counts at `10**15 - 1` runs to exit 0) and `test_counts_of_thousands_of_digits_end_with_exit_code_2_and_no_stack_trace` (three counts of `9 * 10**4299` end with exit 2, not with a `ValueError`).
- Red on the head: `python -B -m unittest discover -s task-cycle -p "test_cycle_stages.py"` exit 1 (6 failures of the first test, 4 counts + 2 lifetimes, as `2 != 0`, and 1 error of the second, `ValueError: Exceeds the limit (4300 digits) for integer string conversion` out of `main`); the boundary part of the first test passed on the head, as it should.
- Fix, `task-cycle/cycle_stages.py`: constant `TOKEN_DIGITS = 15` with the comment that the audit bounds the same counts alike, and `required_count` refuses `value >= 10 ** TOKEN_DIGITS` with the message of "is not a whole number" (exit 2, as the other malformed counts). The module description names the bound ("of at most 15 digits"). Green: same command, exit 0 (71 tests).
- Choice: the constant is repeated in `cycle_stages.py` and not imported from `process-audit/audit_count.py`, since both scripts are standard-library-only scripts that do not import each other; the cost if one changes, the other does not follow, and nothing checks it (named here; no test ties the two).
- The Codex reading (`usage.get(..., 0)`, l. 479-481) checks no field and is not changed; the finding is about `required_count`.

**M6 — fixed.** `process-audit/audit_count.py`: (1) the docstring of `Analysis` no longer says "each in full"; it says both `unknown` and `held` go into the pairs of *Unknown values* alike; (2) the comment in `analyse` ("every other unknown value is given in full") now says every unknown value, the held ones included, is grouped by field and reason in `unknown_rows`; (3) the printed sentence of the section *Cost* (l. 3108, a string the audit writes into its result, not a comment): "a new list or a change of `task-cycle/cycle_stages.py` starts a new one (WAY-339)"; no test asserts that text (grep); (4) the paragraph on exit codes of the module description: the clause "which for a table of levels of the register names the level it lacks or writes twice" after "an `Error:` line on stderr". **Line numbers of the finding:** the finding gives `audit_count.py:248-256` for the exit-code paragraph and `204-207` for the sentence "a screen above"; in the head the exit-code paragraph stands at l. 300-307 and the sentence that says the `Error:` line names the level at l. 251-252, so I took the paragraph of exit codes as meant and put the clause there (the text of l. 251-252 already says it).

**M7 — fixed.**
(a) Lines over 100 characters that the change added (measured in characters, on the added lines of the diff from `7f5c5a5`; the finding's counts were in bytes in some places, so some lines it names — for instance in WAY-344 *Rejected* and the lines of 101 bytes with a dash — are 100 characters or fewer and were left): `task-cycle/tracked_private_paths_check.py:16`; `task-cycle/skill/SKILL.md` step 12 (and the lines the move carried); `task-cycle/cycle_measures.py` module description (the paragraph from "It is a read of the log" re-filled); `process-audit/audit_count.py` six lines (the bullet on the form of a stage report, "its other values as they stand", "count from the register ... A section *Cost*", the comment before `TOOL_GROUPS`, `changed = changed_paths(...)` as two lines, "lists the rest. The full list of a pair's values"); `foundations/decisions.md` WAY-321, the paragraph of WAY-344 that M1 edits, WAY-339 *Rationale* and *Rejected* (one line each); `elements/decisions/template.md:233`. A long line was cut at the last space within 100 and the rest carried to the start of the next line until a line fitted, so only lines from the long one to the end of its paragraph moved. After the edit no line added by the change over `7f5c5a5` in the files I touched is over 100 characters except those of `process-audit/test_audit_count.py` named below.
(b) `process-audit/test_audit_count.py`: one blank line before `written_cost` instead of two.
Not done: three lines over 100 characters that the change added to `process-audit/test_audit_count.py` (a long `assertIn` line, a table header and two test names of 103) — the finding names no such line and the slice-7 review's blank-line Minor was the only item for that file; I left them (out of the finding's list).

## Checks (command and exit code)

| Command | Exit |
|---|---|
| `python -B -m unittest discover -s task-cycle -p "test_cycle_stages.py"` (red on head, as above) | 1, then 0 (71 tests) |
| `python -B -m unittest discover -s task-cycle -p "test_cycle_stages.py"` after all edits | 0 |
| `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"` | 0 (89 tests) |
| `python -B -m unittest discover -s task-cycle -p "test_private_paths_check.py"` | 0 (54 tests) |
| `python -B -m unittest discover -s task-cycle -p "test_tracked_private_paths_check.py"` | 0 (21 tests) |
| `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` | 0 (231 tests, 306 s) |
| `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"` | 0 (3 tests) |
| `python -B gate/run_tests.py elements/common` | 0 (242 tests) |
| `python -B gate/run_tests.py instruction-files` | 0 (104 tests, 5 skipped) |
| `python -B gate/run_tests.py agent-instructions` (once red after the constant of the M2 test changed, before the fixture followed) | 1, then 0 (27 tests) |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 ("checked: 310 files, 0 listed") |
| `python -B elements/common/foundation_check.py --skip-test-citations` after the last edit of a foundation file | 0 ("0 errors"; one note about `guidelines-file-place`, present before) |

The whole gate was not run (WAY-160). Every run in the list above was made on the tree after the last edit of the files it covers, and before the three last commits were made (they only record that tree; no file changed between the runs and the commits).

## Own-work check

The requirement most likely unmet: M5's refusal "as the other malformed counts", exit 2, and that no true count is refused. The check is the first test above: the boundary at 15 digits both ways (`10**15` refused, `10**15 - 1` read, for each of the four counts) and the crafted 4300-digit input; it showed red on the head and green after. M1 "states the rule the code already follows": the check is the test `test_a_field_missing_from_the_file_of_a_changed_tool_is_not_read_and_ends_no_run`, which the run of `test_audit_count.py` passes (exit 0), and the reading of `withdraw_values` quoted above. For M2 the check was that no message or test depends on the changed wording (grep) and the three gates above; the `.markdown` to `.mdc` change was found by the first gate run, not by reading.

## Reaches beyond the dispatch

- `process-audit/audit_count.py` (module description, paragraph on changed tools; `withdraw_values`; the sentence of the section *Cost*) and the test names `MechanismMeasures.test_a_field_missing_...`: to confirm that M1 states what the code does, and which values `cycle_stages.py` measures (for M3).
- `foundations/glossary.md` (the entries *Markdown file* and *repository instruction file*): to read the definitions M2 follows; the dispatch named the finding only.
- `instruction-files/check_instructions.py` `POINTED_SUFFIXES`: to read what the check script counts (M2).
- `foundations/decisions.md` WAY-339 and WAY-344 read whole to the end of *Rejected* of WAY-339 (up to the line I rewrapped); the dispatch named them. WAY-321's entry was read to l. 1915.

## Working copies

None made. A directory `.runs/fix-whole/` held the logs of the checks; it and the two logs I wrote directly under `.runs/` (`m2-*.log`, three files) are removed.

## Unread material

- `reports/review-whole-report.md` (the review report with each finding's place and evidence): not read; the findings file was enough.
- `task.md`, `spec.md`, `plan.md` of the cycle: not read.
- Executor 17's record of Codex's `cache_write_input_tokens` (the "constant 0 in 6347 records"): not read; M4's sentence rests on the finding.
- `elements/common/rules.md` and `elements/common/way_of_working.md` (named by the template and the skill): not read whole; the template and the skill read whole, and the check run after the edit stood in for the rules.
- WAY-339 and WAY-344: read whole as to *Verification* and the binding sentences; *Rationale* and *Rejected* of WAY-344 read only in part (the lines around the edit).
- `task-cycle/change/slice.md`: not read (a fix, not a slice).

## Searches not found or unclear

- The finding's line numbers for the exit-code paragraph of `audit_count.py` (248-256, "a screen above" at 204-207) do not hold in the head; see M6 (4).
- The finding's "about 8 lines of 101-106" in `audit_count.py`: I found 6 added lines over 100 characters (the rest were 101 bytes or fewer than 100 characters).
- The finding names "WAY-344 *Rejected*" and "WAY-339 *Rationale* and *Rejected*" among the long lines; I found one long line each in WAY-339 *Rationale* and *Rejected* (110 and 113 characters) and none in WAY-344 *Rejected* in the head.
- The line "A cycle whose file stays missing stays missing" in `task-cycle/skill/SKILL.md` step 12 reads as a repeated phrase in the head; I kept its words as they were (outside the finding).
