# Return step report — task `scripts-after-foundation-review`

**Status:** done

Worktree `the root of the task's worktree`, branch `task/scripts-after-foundation-review`, from head `c43062bdbce4a8dae7a00500aea30bd3ee7fb8c2`. Range compared: `7f5c5a56f67d9ff40554240594ca0bde59773cb3..c43062b`.

## Commit

- `8c6d668` — `foundations/decisions.md` (WAY-339 and WAY-344 *Verification* and the third sentence of WAY-344), `foundations/part_map.md` (`product-guidelines`), and comment lines `decision:` in `process-audit/test_audit_count.py`, `task-cycle/test_cycle_stages.py`, `agent-instructions/test_agent_type_copies.py` (49 added lines, all comments, no other change in the three files). Nothing under `.runs/` committed.

## Foundation compared with code

Compared, each against the code of the range: WAY-339, WAY-344, WAY-337 (read, untouched), WAY-321 and the uses it corrected, the glossary term *Markdown file* and the uses it moved (`test-method-citation`, `guidelines-file-place`, WAY-320, WAY-309 *Rationale*/*Rejected*, the part map entry `tracked-private-paths-command`, `repository instruction file`), WAY-03 (the lines `decision:` of `elements/common/test_foundation_check.py` quote sentences that stand in WAY-03; the check reads them with no error), WAY-294 (`remarks_check.py` reads the layout of the plan's report; the entry is not touched), WAY-309 (address form `a drive path in address form` is a path; the entry's "no letter for the start of a drive when a backslash stands before it" stays true), WAY-320, WAY-328, WAY-368, and WAY-33 (search of the whole foundation for `cycle_stages`, `agent_type_copies`, `price list`, `audit_count`, "stage report", "Markdown", "compile", `todo`: no sentence found that the code makes untrue beyond what is listed below). The entries and the code of the cache columns agree (settled point 3): the detailed section ends with *Cache write (5 minutes)* and *Cache write (1 hour)*, a Codex row reads 0 and 0, a header with neither column is the earlier form (cost priced as input, exit 0, no `Error:`), a header with one is a missing field (exit 1, `Error:` naming the column), the series of the cost splits at `task-cycle/cycle_stages.py` and at a new list, and the two scripts count the same tokens (test of both scripts in `task-cycle/test_cycle_stages.py`).

## Decisions written or changed

- WAY-344 (`the cycle's`: wording of entries the foundation step wrote, meaning unchanged). (a) The third sentence of the binding paragraph held three exceptions in one sentence; it is now three sentences (the levels of a table; the two cache write columns; the entry `repository`), so that a line `decision:` quotes the start of the sentence whose part a test holds. Words: "The same command, where …; where …; and where …" became "The command that counts the audit, where …. Where …, that command … Where …, no field is missing and that command takes …". (b) *Verification* now reads `tests: …` and keeps a pair only for what no test holds (point 1 of the handoff): removed from the pair — the count's missing field in the measures file, the gate file, a stage report or the register (unknown, result written, exit 1, `Error:`), the three earlier forms and the form without cache write columns, one time line or one write column alone as a missing field, the levels of the two tables, the entry `repository`; kept — the new JSON script, the reworked reading of section headings, the script that checks a form, the part map *Scope*, and the matching *violates* lines. The clause also names that a missing field in a transcript of Claude Code or in a definition of an agent type ends the script with exit 2, and that the file of a changed tool is not read.
- WAY-339 (`the cycle's`: same). *Verification* now reads `invariants: audit-series-script-paths. tests: …` and the pair keeps what no test holds: the comparison inside a series and not week against week, the place of a later measure of context and cache use, the bytes of the decision log, and the *violates* lines about a column of a measure of cache use, the script of the measures writing into the stage report, one script taking the tokens from the other's file. Removed from the pair: the series of the cost and the count of remarks, the series of the measures and of the gate times, the unknown measures of a changed tool, the cache write columns of the stage report. The old *complies*/*violates* lines about the cost script said "its cost and the share in fix rounds"; the clause says "the times, the cost and the share" as the code does (`STAGES_VALUES` in `process-audit/audit_count.py`).
- No decision written whole; no `row` of *Settlements to record* needed a second entry.

### Tests that now hold the sentences (lines `decision:` added; the request names them, WAY-03)

| Test (file) | Decision, sentence quoted |
|---|---|
| `process-audit/test_audit_count.py`: `test_a_measures_file_without_a_label_…`, `test_a_gate_file_without_a_column_…`, `test_a_gate_file_without_a_table_…`, `test_a_column_of_the_newer_table_…`, `test_a_heading_with_no_table_…`, `test_a_column_of_the_older_table_…`, `test_a_file_with_neither_the_section_nor_the_table_…`, `test_a_time_line_without_the_other_…`, `test_neither_time_line_is_the_earlier_form_…`, `test_the_column_files_named_is_never_a_missing_field`, `test_stages_md_without_the_section_…`, `test_a_field_missing_from_the_file_of_a_changed_tool_…` | WAY-344, "The rule binds a script that a change adds and, in a script" |
| same file: `test_a_table_with_neither_write_column_…`, `test_a_table_with_one_write_column_…`, `test_one_write_column_is_missing_…` | WAY-344, "Where a stage report has neither of the two columns" |
| same file: `test_a_table_of_costs_that_lacks_a_level_…`, `test_a_table_of_weights_that_lacks_a_level_…` | WAY-344, "The command that counts the audit, where a table of weights" |
| same file: `test_the_way_with_no_repository_entry_…`, `test_the_way_without_a_repository_entry_…` | WAY-344, "Where the locations file has no entry `repository` under `the-way`" |
| `task-cycle/test_cycle_stages.py`: `test_a_needed_field_that_is_missing_…` | WAY-344, the first sentence quoted above and "Each reading of a file that the rule covers has one test" |
| `agent-instructions/test_agent_type_copies.py`: the two `MissingField` tests | WAY-344, both of those |
| `process-audit/test_audit_count.py`: eight tests of the series of the cost and the count (class `ProcessVersions` and `test_a_new_price_list_starts_…`) | WAY-339, "A new series of the cost of cycles, the two numbers of WAY-337" |
| same file: four tests of the series of the measures (class `MeasureVersions`) | WAY-339, "The measures of how a cycle's agents use context and the prompt" |
| same file: seven tests of the unknown measures of a changed tool and of the two kinds of series | WAY-339, "The audit compares each measure only within a series" |
| `task-cycle/test_cycle_stages.py`: the four cache write column tests and the test across the two scripts | WAY-339, "The one exception is that this report holds" |

Also named by WAY-03 for the request: the check lists `guidelines-file-place` (its sentence now names the suffix `.md`; `elements/common/test_guidelines_place.py` left as it was). `test-method-citation` is no longer listed, because `elements/common/test_foundation_check.py` changed.

## Invariants

None written, none changed by me. The sentences of `test-method-citation` and `guidelines-file-place` agree with the code (`endswith(".md")`, `GUIDELINES = ^guidelines/[^/]+\.md$`). Settled point 2: the invariant `audit-series-script-paths` names the scripts of the series of the measures of context and cache use and of the gate times; `task-cycle/cycle_stages.py`, which now splits the series of the cost, is **not guarded by it**. The path is pinned today only by a test of `process-audit/test_audit_count.py` (`test_each_path_that_starts_a_series_is_a_path_git_tracks`, which also pins `COUNT_PATHS`), which cites no invariant. I did not extend the invariant; **the request proposes it** (a point for the human).

## Environment facts

None written. The change reads, from the transcripts of Claude Code, `usage.cache_creation.ephemeral_5m_input_tokens` and `ephemeral_1h_input_tokens`; a search found no official, versioned description of the local transcript format (only third-party parsers; Anthropic's documentation describes the API's `usage` object, not the transcript file), so no source exists that satisfies the form of a fact (address, passage word for word). The prices of the list are data of the dated file `process-audit/price_list.md` under WAY-337, no citation of a decision.

## Glossary terms

*Markdown file* (written by the foundation step, row 8): checked against `task-cycle/tracked_private_paths_check.py` (`name.lower().endswith(MARKDOWN_SUFFIXES)`, the four suffixes). **Point for the human (settled point 4):** the entry says "in any letter case", which row 8 of the task does not say; the words come from the description of the check and the plan. If the human wants the case to count, that clause is the one to change. The uses that mean `.md` alone were corrected by the foundation step and the fix of the whole change; a search of tracked files for "Markdown file" finds only uses true under the term (`installation/README.md`, `private_paths_check.py`, the two `help=` strings of `project-level` scripts for a document of any suffix, `elements/part-map/template.md`).

## Part map changes

- `product-guidelines`: one clause added — the part answers for the test that finds a dead pointer (a file, a step, a heading) in its skills and in those of `project-level` (new file `product-guidelines/test_skill_references.py`). The file is claimed by `product-guidelines/**`; no file is claimed by no part (the check of the foundation reports none).
- No new allowed dependency is needed (settled point 5): the new test imports only the standard library; it lists the files of the-way and reads the text of a target only for a step or a heading pointer, and I measured the targets it reads on the tree: files of `elements/`, `product-guidelines/` and `project-level/`, all parts `product-guidelines` may depend on. `test_cross_part_imports.py`, `test_skill_references.py`, `test_agent_type_copies.py`, `test_instruction_files.py` and the other new test files import nothing outside their allowed parts (the test `cross-part-imports` passed in the check of the foundation steps, not rerun by me).
- `task-cycle`, `process-audit`, `elements-common`, `part-map`, `installation`, `agent-instructions`, `instruction-files`, `gate`: compared, no change. The audit's series of the cost by `task-cycle/cycle_stages.py`, the stage report's new columns and the price list's new column are details of the code and of WAY-339, not of the map; `gate` has no changed file in the range.

## Projected entries

None (the task has no projected entries).

## Rows of *Settlements to record*

| # | Place |
|---|---|
| 1 | sentence of WAY-344: the second sentence of its third part, "The command that counts the audit, where a table of weights …" (tied to the foundation step's commit `da9d816`; now a sentence of its own); held by two tests (see table) |
| 2 | sentence of WAY-344: "Where the locations file has no entry `repository` under `the-way` …"; held by two tests |
| 3 | sentence of WAY-339: the first sentence ("A new series of the cost of cycles …"); *Rationale* names the price; held by tests |
| 4 | sentence of WAY-339: the third sentence of its first paragraph ("… the audit gives the measures of that tool … as unknown …"); held by tests |
| 5 | data and code, no entry: `process-audit/price_list.md` (column *Cache write (1 hour)*, new date) and the cost in `process-audit/audit_count.py` (each lifetime at its own price); tests in `process-audit/test_audit_count.py` |
| 6 | code, no entry: the section *Unknown values* and its description in `process-audit/audit_count.py` (one line for each pair of field and reason, three examples); tests in `process-audit/test_audit_count.py` |
| 7 | test, no entry: `product-guidelines/test_skill_references.py` (skills of `product-guidelines/` and `project-level/` only) |
| 8 | glossary term *Markdown file* in `foundations/glossary.md` |

## Checks (command and exit code)

- `python -B elements/common/foundation_check.py` (no `--skip-test-citations`), after the last edit of a foundation file: exit 0, "0 errors", one `listed:` (`guidelines-file-place`).
- `python -B -m unittest discover -s agent-instructions -p test_agent_type_copies.py`: exit 0 (9 tests).
- `python -B -m unittest discover -s task-cycle -p test_cycle_stages.py`: exit 0 (71 tests).
- `python -B -m unittest discover -s elements/common -p test_foundation_check.py`: exit 0 (190 tests).
- `python -B -m unittest discover -s process-audit -p test_audit_series_scripts.py`: exit 0 (3 tests).
- `python -B -m unittest discover -s process-audit -p test_audit_count.py -k StagesForms -k repository_entry -k lacks_a_level -k test_a_changed_tool_of_a_measure -k reviewers_type`: exit 0 (23 tests). The other tests of that file with a new comment line were not run one by one; the file parses (`ast.parse`, exit 0) and only comments changed. The whole file (231 tests, about 300 s) was not run; no run of the whole gate.
- A first call of the foundation check after the text edit, before the lines `decision:` stood, was green too; the lines were checked by the second run above (it reads their quotations).

## Own-work check

Requirement most likely unmet: a part of a pair removed that no test holds. For each removed line I named the test and its assertion in the listing above, and read the bodies of the tests of the stage forms (`StagesForms`, lines 1633-1760 of `test_audit_count.py`) and of the two level tests (3009-3085): each asserts the exit code and the line `Error:` or its absence the entry says. The gap found: the old *complies* line for a changed script that measures the cost named only the cost and the share, while the code also gives the working and waiting times as unknown; the clause now says so.

## Choices

- Split the third sentence of WAY-344 into three, and not quote its start for all three exceptions. Rejected: one sentence with one quotation for three tests (the clause would hold three parts under one quote). Cost if wrong: the sibling task's change to WAY-344 touches a nearby paragraph; the three sentences stand together at the end of the paragraph.
- Quote the start of the second sentence of WAY-344 for the tests of the audit's exceptions (they stand inside that long sentence, which cannot be quoted from the middle). Rejected: splitting that sentence, since the sibling task changes it and a merge conflict follows.
- A pair kept for the part no test holds instead of removing the pair whole.
- A clause in `product-guidelines` of the part map and not in `project-level`: the test lies in `product-guidelines` (task row 7).

## Points for the human and observations

- (4) "in any letter case" of *Markdown file*, above.
- (2) the invariant `audit-series-script-paths` does not guard `task-cycle/cycle_stages.py`, above.
- The code treats a level written twice in a table of weights or of the costs of an occurrence as a level missing (same exit code 1 and an `Error:` naming it, tests `test_a_table_of_weights_that_lacks_a_level_…` and the one for costs); WAY-344 names the lacking level only. I left the entry as it is: it is true of what it says.
- A transcript of Claude Code without the field `cache_creation` (an older log may hold only `cache_creation_input_tokens`, third-party sources say) now ends `cycle_stages.py` with exit 2, by the spec's decision (D4).
- "Stage report" still means two things in the foundation (the report of an agent of a stage; the file of the cycle's stages). The foundation step noticed it and left it; I changed nothing.

## Reaches beyond the handoff

- `elements/decisions/template.md` ("Verification", `tests:` clause, `decision:` lines) and `elements/common/foundation_check.py` (`check_decision_line`, `check_held`): to write the lines and the clause in the form the check reads.
- `foundations/part_map.md` and `elements/part-map/{SKILL.md,template.md,skill/write.md,skill/decide_entry.md}`: for the part map entry.
- `foundations/environment_facts.md`, `elements/environment-facts/{SKILL.md,template.md,skill/decide_entry.md}` and one web search for a source of the transcript format: for the decision not to write a fact.
- `product-guidelines/test_skill_references.py`, read whole: for the dependency of the part.

## Unread material

- `elements/glossary/skill/SKILL.md`, `elements/invariants/skill/SKILL.md` and their method files: not read, since I wrote no entry of those elements.
- `process-audit/audit_count.py`: read lines 1-630 and 2540-2630 only.
- `process-audit/test_audit_count.py`: read lines 1630-1765 and 3000-3085, and the names of all tests; the bodies of the other annotated tests were not read.
- `spec.md`: read whole; `plan.md`, the reports of the executors and reviews, `cycle.md`: not read. `fix-whole-report.md` and `foundation-report.md`: read whole.
- `task-cycle/cycle_stages.py`: read lines 1-140 and 985-1095. `task-cycle/test_cycle_stages.py` bodies: not read.
- `elements/decisions/skill/{read,decide_entry}.md`, `elements/common/{rules,way_of_working}.md`: not read.

## Searches not found or unclear

- No official description of the local transcript format of Claude Code (see *Environment facts*).
- The handoff says to settle that the part map's new test files need no new dependency; the method of "dependency of a part" (glossary: any reach, not only an import) is wider than what `cross-part-imports` holds, so I checked the reach by running the test's reads (above); the check of the foundation holds no test of that wider reach.
- The foundation step's report says the check lists two invariants for the request; it now lists one (see above).

## Working copies

One directory, `.runs/return-step/`, held three throw-away scripts (the edits of the two decisions, the insertion of the lines `decision:` and a measurement of the files the test of the pointers reads). It is removed. No worktree or clone made.
