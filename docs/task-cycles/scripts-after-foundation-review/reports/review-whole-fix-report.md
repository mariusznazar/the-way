PASS c43062bdbce4a8dae7a00500aea30bd3ee7fb8c2

# Review of the fix of the Minor findings of the whole change

Range: `84d062b817e2f8ba1cf141c0f9140cd5f178f61c..c43062bdbce4a8dae7a00500aea30bd3ee7fb8c2` (6 commits, 13 files, +194 -133); `git rev-parse HEAD` confirmed the head. Findings file: `reports/whole-findings.md` (M1-M7). Fix report: `reports/fix-whole-report.md`.

No new Critical or Important finding in the fix. Every finding is fixed. Three Minor findings of the fix itself (N1-N3), which block nothing.

## Each finding

- **M1 fixed.** WAY-339 (first paragraph) and WAY-344 (audit-exceptions sentence) each gain one clause saying that the file of a tool the cycle's own change changed is not read for that cycle, so none of its fields is missing and no `Error:` is given. It is what `withdraw_values` does (it clears `cycle.missing` and the missing-field pairs; confirmed in the code) and what the test `test_a_field_missing_from_the_file_of_a_changed_tool_is_not_read_and_ends_no_run` pins. The entries are edited in place, with no history or dating, and the binding meaning is unchanged apart from the stated case.
- **M2 fixed.** In `elements/common/foundation_check.py` only words changed: the module description, one comment, one docstring and the text of one printed message (`... holds a line `invariant: %s``); no statement, condition or test of the script changed (read the whole diff of the file; the 190 tests of `test_foundation_check.py` pass and no test asserts the message). `instruction-files/check_instructions.py`, `instruction-files/SKILL.md`, `agent-instructions/test_instruction_files.py` say "files whose name ends in `.md` or `.mdc`", which is what `POINTED_SUFFIXES` and the glossary entry *repository instruction file* say. See N2 for the one change that is more than words.
- **M3 fixed.** WAY-339 *Verification* gains a *complies* and a *violates* line for the script that measures the cost. See N1.
- **M4 fixed.** `task-cycle/cycle_measures.py` (module description and the docstring of `cache_sum`) now says Codex's record has no cache write by lifetime and a write field that is a constant 0, which measures nothing, so the figures are unknown.
- **M5 fixed, with a test that fails without the fix.** `task-cycle/cycle_stages.py` `required_count` refuses a count of 15 digits or more (`value >= 10 ** TOKEN_DIGITS`) with the same message and exit 2 as another count that is no whole number, so the sum can no longer reach 4300 digits; the module description names the bound. Tests: `test_a_count_of_more_than_fifteen_digits_is_no_whole_number_and_one_of_fifteen_is` (the four counts and the two lifetimes at 10^15 are refused; the four counts at 10^15-1 are read, exit 0) and `test_counts_of_thousands_of_digits_end_with_exit_code_2_and_no_stack_trace` (three counts of 9 x 10^4299: exit 2, no output file). The crafted input I used in the first review is the second test's input; the run ends with exit 2 and the line naming the field. The constant is repeated in the two scripts (neither imports the other), which the fix report names; nothing ties the two values.
- **M6 fixed.** The docstring of `Analysis` and the comment in `analyse` no longer say "in full"; the sentence the count writes in *Cost* names the change of `task-cycle/cycle_stages.py` as a start of a new series (a string in the result, asserted by no test: the 231 tests pass); the paragraph on exit codes says the `Error:` line names the level of a table of levels (the line numbers of the finding were off, the executor found the paragraph and edited it).
- **M7 fixed, one new long line.** The long lines named are rewrapped in `foundations/decisions.md`, `elements/decisions/template.md`, `process-audit/audit_count.py`, `task-cycle/cycle_measures.py`, `task-cycle/skill/SKILL.md`, `task-cycle/tracked_private_paths_check.py`; the extra blank line before `written_cost` is gone. The rewraps move words only (checked on the diffs of the decisions, the template and the skill). See N3.

## Minor findings of the fix (block nothing)

- **N1. The new example line of WAY-339 gives the cost script's unknown values as cost and share only.** `foundations/decisions.md`, WAY-339 *complies*: "a cycle whose own change changes the script that measures the cost gives its cost and the share of its cost in fix rounds as unknown ... and its other measures as they stand". `withdraw_values` also gives the two stage times (*Working time without waiting for tools*, *Waiting for tools*) as unknown for that tool (`STAGES_VALUES`), and the binding sentence says "the measures of that tool". The example is narrower than the code and "its other measures as they stand" would read the times as standing. No sentence of the binding paragraph is contradicted. Remedy: "its times, its cost and the share of its cost in fix rounds as unknown".
- **N2. The fix changed an invariant test, which the request must name (WAY-03).** `agent-instructions/test_instruction_files.py` (tests of the invariants `instruction-file-imports` and `root-claude-md-import`): `MARKDOWN_ENDINGS = (".md", ".markdown")` became `POINTED_ENDINGS = (".md", ".mdc")` and the fixture `docs/other.markdown` became `docs/other.mdc` in four places. The change is more than the words M2 asked for. It makes the test's population of repository instruction files equal to the glossary definition (`.md` or `.mdc`) and to `POINTED_SUFFIXES` in the check script, so I judge it right and no weakening against the invariants' sentences; it does narrow the population (a tracked `.markdown` file named by the root is no longer read), which is what the glossary entry says. The executor disclosed it with its reason; the 5 tests pass.
- **N3. One new line over 100 characters:** `task-cycle/cycle_stages.py`, module description, "message that names the transcript, the line and the field. Read with a fallback, and no error where absent: a line with no" (122 characters; the edit about the 15-digit bound left the paragraph unwrapped). Polish.

## Declined to judge

- Whether the number 15 should be shared by the two scripts (named by the executor; neither imports the other by design).
- The three lines over 100 characters in `process-audit/test_audit_count.py` that the executor left as outside the finding's list.

## Checks I ran (worktree `the root of the task's worktree`, head `c43062b`)

| Command | Exit |
|---|---|
| `git rev-parse HEAD` | 0, `c43062b...` |
| `python -B elements/common/foundation_check.py` | 0, `0 errors`, one `listed:` line (`guidelines-file-place`, as before) |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0, `checked: 310 files, 0 listed` |
| `python -B -m unittest test_cycle_stages` (in `task-cycle/`) | 0, 71 tests |
| `python -B -m unittest test_cycle_measures` | 0, 89 tests |
| `python -B -m unittest test_tracked_private_paths_check` | 0, 21 tests |
| `python -B -m unittest test_instruction_files` (in `agent-instructions/`) | 0, 5 tests |
| `python -B -m unittest test_check_instructions` (in `instruction-files/`) | 0, 104 tests (5 skipped) |
| `python -B -m unittest test_foundation_check` (in `elements/common/`) | 0, 190 tests |
| `python -B -m unittest test_audit_count` (in `process-audit/`) | 0, 231 tests |
| `git diff -U0 84d062b..HEAD`, added lines over 100 characters | one real (N3); one more is 101 bytes with a dash, 100 characters |
| `git grep -n Markdown` over `foundation_check.py`, `instruction-files/`, `agent-instructions/` | only `tool_loading.md:43` (the syntax of a code span, no file) |

No run of the whole gate.

## Unread material

- The fix's commits were read through the whole diff `84d062b..HEAD`, except the rewrapped paragraphs of `foundations/decisions.md` and `process-audit/audit_count.py`, which I compared only where a word changed (the diff shows the paragraphs moved, no word added or dropped outside the clauses named above).
- WAY-339 and WAY-344 are read whole from the first review; I did not re-read their *Rejected* after the rewrap beyond the diff.
- `reports/review-whole-report.md` and the task, spec and plan: not re-read.

## Searches not found or unclear

- A test that asserts the printed message of `foundation_check.py` for an uncited `test` invariant: none found (grep), so the changed words break none.
- A tie between the two copies of the 15-digit bound: none exists.

## Working copies

Only `.runs/review-whole/` of the worktree (test outputs); removed. `git status` is clean. No watcher or timer was started; the one test run I put in the background had ended before I wrote this report.
