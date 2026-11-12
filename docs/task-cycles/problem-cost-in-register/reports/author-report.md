# Report of the one author — problem-cost-in-register

**Status:** done with concerns (one concern: the exit code of a missing field against the task's wording, see "Choices" 1).

## Commits (branch `task/problem-cost-in-register`, base `55afa8e`)

- `f5e1d45` Count the problems of each issue on each level of the cost of an occurrence — code, tests, template, skill.
- `18b4a3f` Record the scale and the place of the cost of an occurrence, and the term — foundation step.

## Files changed (added / removed lines against the base)

| File | + / - |
|---|---|
| `process-audit/audit_count.py` | 128 total changed (see `git diff --stat 55afa8e HEAD`) |
| `process-audit/test_audit_count.py` | 179 total changed |
| `process-audit/problem_register.md` | 36 total changed |
| `process-audit/SKILL.md` | 32 total changed |
| `foundations/decisions.md` | 96 total changed (WAY-345, WAY-346 added; WAY-330 edited) |
| `foundations/glossary.md` | 6 added |

Whole diff: 6 files, 406 insertions, 71 deletions.

## What was made

- Template `process-audit/problem_register.md`: column `Cost of an occurrence` in *Problems* (after *Weight*, before *Issue*); new table `## Costs of an occurrence` (header `| Cost of an occurrence | Meaning |`) with the five levels `nothing`, `steps`, `stage`, `round`, `human` and meanings taken from the task; prose says the user adapts meanings, never levels.
- `process-audit/audit_count.py`: `COST_LEVELS`; `Problem.cost`; a row of *Problems* has 8 cells; a cost that is no level refuses the row ("the cost of an occurrence is not one of the five levels") exactly as an unknown weight does; the table of levels is checked as the table of *Weights* is (a level missing or doubled gives the register error and refuses the table, exit 1; an extra level refuses only its row); new result section `## Cost of an occurrence by issue` (columns Issue, Fate, nothing, steps, stage, round, human, Refused rows), one row per issue of the register in the register's order, for fixed, open and dropped alike.
- WAY-344 for the register: a heading, a table or a column the count needs and cannot find ends the run with exit code 2, nothing written, and one `Error: the register of problems lacks ...` line that names every missing field.
- `process-audit/SKILL.md`: the cost row is quoted beside each issue at steps 2 and 3, a rule "the cost of an occurrence is material, never a priority" (WAY-346, WAY-336), the exit codes updated.
- Foundation (rows 1-3): WAY-345 (row 1, the scale), WAY-346 (row 2, place in the result), glossary term `cost of an occurrence` (row 3), and WAY-330 edited in place (the register holds the cost, the audit gives none itself).

## Foundation entries (one sentence each, English and Polish; marked)

- `row 1` WAY-345 — The cost of an occurrence of a problem has five fixed levels, each dearer than the one before; a problem takes the highest level its cost reached; the user adapts only the meanings. / Koszt wystąpienia problemu ma pięć stałych poziomów, każdy droższy od poprzedniego; problem dostaje najwyższy poziom, do którego sięgnął jego koszt; użytkownik zmienia tylko znaczenia.
- `row 2` WAY-346 — The result of the count gives, for each issue fixed, open and dropped, how many of its problems stand on each level, and nothing by cycle. / Wynik liczenia podaje przy każdej sprawie poprawionej, otwartej i porzuconej, ile jej problemów stoi na każdym poziomie, a przy cyklach nic.
- `row 3` glossary `cost of an occurrence` — a level on the five-level scale, different from the cost of a cycle in money (WAY-337; kept in *Not* as `WAY-337`). / Poziom na skali pięciu poziomów, czym innym niż koszt cyklu w pieniądzach.
- `the cycle's` (an edit, not a row): WAY-330 — binding sentence, heading question, *Verification*, *Rationale*, *Rejected* now say class, weight and cost of an occurrence. The task's *Decisions in play* names this change to WAY-330 ("Zmiana, którą wprowadza zadanie"), so it is not beyond what the accepted task carries; the request should still list it.

*Rejected* of WAY-345 and WAY-346 holds only the ways the task's *Not chosen* keeps, each with its reason; *Based on* is `none` (no outside source); *Origin* `none`.

Choice: two new decisions plus an edit of WAY-330, not an edit of WAY-333. WAY-333 answers how weight and class are graded; cost is a third grade with its own scale, and the task says rows 1 and 2 are decisions. Rejected way: widening WAY-333 to carry both scales (one entry would then answer two questions). Cost if wrong: a reviewer folds the two entries into WAY-333 and WAY-336; only the log changes.

Search of the foundation (WAY-33): `git grep` for `occurrence`, `cost of a cycle`, `WAY-330`, `Weights` over tracked files; hits are in `process-audit/` and the decision log only. Part map entry `process-audit` still true (template, command, skill); no new part, so the *Scope* of WAY-328 and WAY-344 is unchanged. Invariants whose *Part* is `process-audit` or `every` (script-language, script-imports, script-subprocesses, tracked-file-private-paths, cross-part-imports, test-method-citation): the change adds no import and no subprocess, and `tracked_private_paths_check.py` lists 0.

## Checks (command and exit code)

| Check | Command | Exit |
|---|---|---|
| Red run, before the code (new and changed tests, the new template in place) | `python -B gate/run_tests.py process-audit` | 1 (127 of 129 failed; the failures of the new tests are assertions: exit code or missing section/row, e.g. `0 != 1 : ... header row the template gives`; the rest fail because the old code reads the new template's *Problems* header as a refused table) |
| Green run, after the code | `python -B gate/run_tests.py process-audit` | 0 (129 tests OK) |
| Foundation check, with and without test citations | `python -B elements/common/foundation_check.py --skip-test-citations`, `python -B elements/common/foundation_check.py` | 0, 0 (0 errors) |
| Tests of elements/common | `python -B gate/run_tests.py elements/common` | 0 (144 OK) |
| Tests of agent-instructions (skill entry points, instruction files) | `python -B gate/run_tests.py agent-instructions` | 0 (18 OK) |
| Private paths in tracked files | `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 (283 files, 0 listed) |
| Private paths in the three files I changed in prose | `python -B task-cycle/private_paths_check.py <file>` for `process-audit/SKILL.md`, `process-audit/problem_register.md`, `foundations/glossary.md` | 0, 0, 0 |
| Mutation: the cost check switched off (`elif False:`), then restored | `python -B -m unittest test_audit_count.RegisterCount.test_a_cost_that_is_no_level_refuses_its_row_and_reads_at_least_in_its_issue` (from `process-audit/`) | 1 with the mutation, 0 after restoring |

Not run: the whole gate `python -B gate/run_tests.py` (the handoff and `make-change` forbid it); `task-cycle` tests (nothing in `task-cycle/` changed); `request_check.py` (the orchestrator's step). The invariant tests of `every` were not rerun as separate runs beyond the checks above.

## Tests written (each: the break it catches)

All in `process-audit/test_audit_count.py`, class `RegisterCount`; helpers `PROBLEMS_HEADER` and `problem_row(..., cost=)` changed to the new column.

- `test_the_problems_of_each_issue_are_counted_on_each_level_of_the_cost_of_an_occurrence` — literals for 3 issues (open, fixed, dropped), a problem of an unread repository and a problem with no issue; weights deliberately differ from costs. Catches: cost read from the weight column, counting by cycle, wrong level order, a problem of an unread cycle dropped, an issue-less problem counted.
- `test_a_cost_that_is_no_level_refuses_its_row_and_reads_at_least_in_its_issue` — costs `Steps`, `free`, empty, `Minor` (a weight), `steps` + ESC, `st|eps` (a bar) and `steps` + line break; asserts refusal reasons, `at least n` in the issue's row, only printable output. Catches: the cost check removed (seen failing by mutation), case-insensitive reading, a bar or a control character reaching the result.
- `test_a_table_of_costs_that_lacks_a_level_is_treated_as_the_table_of_weights_is` — a level missing, a level written twice (exit 1, error naming the table, `Unknown values` row), an extra level (row refused, exit 0), the template as it stands (exit 0, empty stderr).
- `test_a_register_lacking_a_field_ends_the_run_with_an_error_naming_it` — WAY-344 test for the register's reading: a heading, the heading of the new table, a table, the new column in the old register form, the column under another name, the `Meaning` column of the new table; each: exit 2, `Error: the register of problems`, the field named, results directory empty.
- `test_every_field_missing_from_the_register_is_named_in_one_error` — two headings missing, both named in one error.
- `test_a_column_in_another_order_or_an_extra_one_is_refused_not_missing` — passes before and after; it keeps exit 1 and a refused table when no field is missing (guards against turning every header mismatch into exit 2).
- Replaced: `test_a_table_missing_from_the_register_is_an_error_of_the_register` (asserted exit 1 and a written result) — a deliberate change by WAY-344, now covered by the first two WAY-344 tests above. No invariant test changed; no assertion weakened.

Mutation in the head, not covered by a test: `COST_LEVELS` order is covered by the first test; the wording of the new section's paragraph is prose and untested on purpose; the `Fate` column is the raw register cell (covered by the first test's literals).

## Own-work check (section 3 of `make-change`)

- Requirement most likely unmet: WAY-344 "every field of that file" for the whole reading of the register, and the task's "a register without the new column is refused with an error that names it".
- Check 1: the new tests above for headings, tables, columns. Check 2, end to end: the old template from the base (`git show HEAD:process-audit/problem_register.md`) run through the command with a throwaway locations file in the scratchpad: `python -B process-audit/audit_count.py --locations <file> --today 2026-11-13` exit 2, stderr `Error: the register of problems lacks the heading `## Costs of an occurrence`, the column `Cost of an occurrence` of the table `Problems``, nothing newly written. Check 3: the new template with three problem rows (one in an unread repository) exit 0, and the section printed as designed (`a-matter` open: steps 1, round 1; `b-matter` dropped: human 1).
- What it showed: the requirement is met for the fields of headings, tables and columns. It is not met for row labels of the two level tables (see Choices 1).
- No check failed and passed on a rerun except the red-then-green run recorded above and one test of mine whose expectation I corrected before the green run (the `nothing` column reads `at least 0`, not `0`, when a refused row names the issue; my expectation was wrong, the code was right).

## Choices (each with the way rejected and the cost if wrong)

1. **Exit code of a missing field: 2 with nothing written, for the whole register reading.** WAY-344 says a changed script's reworked reading of a file brings every field of that file under the rule, with exit 2. The task's Context says "brak pola kończy się błędem, który je nazywa (WAY-344)". Before, a missing table gave exit 1 with a written result and the skill's step 2 and the docstring said so. Rejected: keeping exit 1 for the old tables and applying exit 2 only to the new table and column (two behaviours for one file; a reviewer reading WAY-344 would flag the old one). Cost if wrong: the nightly run writes no count at all for a register that lacks a heading, where it wrote a partial one before; a reviewer who reads "the way of reading is not reworked" can ask to restore exit 1 for the four old headings, which is a small revert of one `raise` and the two tests. **Concern, for the orchestrator:** the task text does not say the exit code, and the same text says a levels table lacking a level is treated as the weights table is today (exit 1, written). By WAY-344 a level is a "row label", a field, and a missing level would be exit 2; I followed the task's explicit words (exit 1) for the two level tables, for `Weights` too, and left a doubled heading as refusal (not a missing field). So row labels of the level tables are the one place where the reworked reading of the register is not under exit 2. The human may want to rule on it.
2. **Header word and names:** column and table header both `Cost of an occurrence` (the glossary term), heading `## Costs of an occurrence`, result section `## Cost of an occurrence by issue`. Rejected: `Cost` (collides with the existing result section `## Cost` and the word in tests' `rows("Cost")`). Cost if wrong: renaming in four files.
3. **Column order:** `... | Weight | Cost of an occurrence | Issue |` (cost beside weight, issue stays last). Rejected: appending after *Issue* (keeps old cells in place but separates the two grades).
4. **Layout of the output:** one new section with one row per issue and a `Fate` column, not five columns appended to each of *Fixed issues*, *Open issues* and *Dropped issues*. Rejected: it would add 15 columns, repeat the same five in three tables and rewrite about twelve whole-row assertions of existing tests. Cost if wrong: the skill quotes two tables per issue instead of one (it says so at steps 2 and 3).
5. **What counts per issue:** every valid row naming the issue, by its row, whether or not its cycle is read; refused rows of the issue make every level `at least n` and are shown in `Refused rows`, as the other issue tables do. Fixed issues are not split by whether the pin holds the fix (the task asks for how many problems stand on each level, not for the split).
6. **Layout of the template's levels table and the meanings:** meanings are the task's, in the order of the task; the table sits between *Weights* and *Issues*.
7. **Skill wording:** a rule that the cost is material and never a priority, with "add the levels into no score" (WAY-336's spirit); quoted rows beside issues at steps 2 and 3. Nothing about series or ordering beyond WAY-336.
8. **Foundation:** two decisions and an edit of WAY-330 (above); glossary *Not* names the money cost by `WAY-337` in backticks (the template allows an identifier as the carrier).

## Reaches beyond the dispatch (section 1 of `make-change`)

- `foundations/decisions.md` WAY-337 (read whole) and its neighbours WAY-331 to WAY-332, WAY-338, WAY-339 (read whole) — to avoid colliding with the cost of a cycle and with the series rule.
- `elements/decisions/template.md`, `elements/common/rules.md`, `elements/common/way_of_working.md`, `elements/decisions/skill/*.md`, `elements/glossary/template.md`, `elements/glossary/skill/*.md` (read whole) — the foundation step names the skills; I followed them in person (no subagent).
- `foundations/invariants.md` entries `script-language`, `script-imports`, `script-subprocesses`, `tracked-file-private-paths`, `test-method-citation`, `cross-part-imports` (read whole as entries) — the invariants of `every`.
- `task-cycle/remarks_check.py` (`display`, `split_lines`) read in part, to know how a line break and control characters are cut in a register.
- `the author's own rule files for scripts and for git` (the author's own rules) — for scripts and commits.

## Unread material

- `agent-instructions/README.md`: read whole. `task-cycle/change/SKILL.md`: read whole. `task.md`: read whole.
- The handoff's decision list: WAY-330, 333, 334, 335, 336, 337, 339, 344, 328, 38, 89 — all read whole. The rest of the glossary (read whole at the start; the entry texts above the new one) yes.
- `foundations/part_map.md`: I read the entry `process-audit` and its neighbours' header lines only (about 25 lines), not the whole file; the handoff asked for that entry only.
- `foundations/invariants.md`: I read only the entries named above and the headings/`Part` lines of all the others (the handoff names invariants of `process-audit` or `every`; none has *Part* `process-audit`).
- `process-audit/price_list.md`: not read (not changed, not touched by the new fields).
- `process-audit/test_audit_count.py`: I read lines 1-220 (helpers) and 1100-1599 (`RegisterCount`) before changing it, not the whole file. Unread: lines 220-1099 (the classes `CycleFound`, `ProcessPin`, `Remarks`, `Times`, `CraftedInput`, `Locations` and `Cost`) and 1600-end (`Run`, `ProcessVersions`, `PriceBoundary`). Those use the helpers `register_text`/`problem_row` only through `RegisterCount`-style tests in `Run` and `ProcessVersions` that I did not read; the full run of the file passed after the change, which is the only evidence they still hold.
- `ui_check.md`: not read, no screen changed.

## Searches not found or unclear

- The orchestrator's result of the base gate was not available to me (handoff said so); I ran focused checks only, so which tests failed on the base is unknown to me. `process-audit` had 129 tests OK after my change, and `elements/common` 144 and `agent-instructions` 18 OK.
- Unclear: whether WAY-339 wants a new series when a user adapts the meaning of a cost level (WAY-339 names classes, price list, stage report, reviewer instructions, not levels). Not asked; the count compares no cost level across time. Left as is.
- Unclear: the task's "Decisions in play" says WAY-330 changes; whether the human reads an edit of WAY-330's heading question as beyond the task. I edited the question (class, weight and cost of an occurrence) to match the binding sentence.
- The old test of a missing table asserted the table-level result for exit 1; no document I found says exit 1 was a decision rather than the earlier author's form (the skill and the docstring state it as description). Nothing in the foundation names that exit code for a missing table.

## Problems as observed

- The Bash tool of this session turned `\\n` in a heredoc Python script into a real newline (my first edit script failed its own assertion and changed nothing). I used the Edit tool and script files from then on. Cause: guessed (tool-side unescaping); not verified.
- A test run of `process-audit` takes 205-215 s, over the 120 s default timeout of the tool; I ran it in the background.
- Mariusz's own register (outside the repository, not touched) lacks the new column and the new table, so after this change the nightly count ends with exit 2 and the line above until the human action of the task (copy the column and the table into his register) is done. That is the intended effect; it is the human action the orchestrator lists in the request.
