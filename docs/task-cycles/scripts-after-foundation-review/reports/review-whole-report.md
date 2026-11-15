PASS 84d062b817e2f8ba1cf141c0f9140cd5f178f61c

# Review of the whole change — task `scripts-after-foundation-review`

Range reviewed: base `7f5c5a56f67d9ff40554240594ca0bde59773cb3` to head `84d062b817e2f8ba1cf141c0f9140cd5f178f61c` (`git rev-parse HEAD` confirmed the head; 26 commits, 41 files, +2840 lines). Worktree `the root of the task's worktree`. Method: `task-cycle/review/SKILL.md` and `task-cycle/review/whole_change.md`.

Counts: blocking 0; Minor within the task 8 (M1-M8); Minor / observations marked outside the task's scope 4 (O1-O4).

## Blocking findings

None. No slice is named, because nothing blocks.

## What I checked against the task

Every item of *To do* 1-20, every row of *Settlements to record* 1-8, every answer of *Questions to settle* 1-9 and source fidelity. Result per item, each judged on the code, not on the executor's report.

| Item | Result | Evidence |
|---|---|---|
| 1 (level missing in *Weights* / *Costs of an occurrence*) | met | `process-audit/audit_count.py` `level_faults`, `check_levels` (about l. 2026-2054): the `Error:` line names each missing or doubled level, the result is still written, the table's values are `unknown`; tests at `process-audit/test_audit_count.py:3024-3028` (*Weights*) and `:3071-3075` (*Costs of an occurrence*), each with the level named. WAY-344 carries the exception (checked below). |
| 2 (agent type copies, exit 2) | met | `agent-instructions/agent_type_copies.py` `MissingFieldError`, `missing_field`, `main`; docstring names both exit codes; two tests (without `name:`, without `description:`) assert code 2, message and no file written; other errors stay exit 1. |
| 3 (`repository` entry) | met | WAY-344 sentence; `the_way_checkout` left as it is; test `test_the_way_with_no_repository_entry_is_the_checkout_the_script_lies_in` pins it. |
| 4 (Windows trace, no turn) | met | `task-cycle/cycle_stages.py` `read_codex_session` takes `default=None`, `codex_subagent_paths` has no floor for `None`; test `test_an_orchestrator_with_no_turn_finds_its_subagents_where_the_epoch_is_refused`. |
| 5 (two kinds of series) | met | `cost_boundary`, `count_boundary`, `split_series`, `versions_lines`; `Versions.cost` and `Versions.count`; tests that no row of one kind holds a figure of the other. WAY-339 says it in place with *Verification*, *Rationale* (the price is named: "after a change of the reviewer's instructions the audit cannot tell ...") and *Rejected* a and b of question 2. |
| 6 (`the-way-stage.md`) | met | `COUNT_PATHS` holds `task-cycle/agent-types/the-way-stage.md`; module description, `process-audit/SKILL.md` and the result text say so; test `test_a_change_of_the_reviewers_type_of_agent_starts_a_series_of_the_count_alone`. |
| 7 (cache writes priced by lifetime, price list) | met | route of the spec: two columns after *Files named* written by `cycle_stages.py` (`Usage.write_5m/write_1h`, report header), read by `section_table` (three forms), priced by `cost_at` per lifetime, a `—` write price gives `unknown` only for a row that holds that lifetime; Codex rows `0`/`0`; `process-audit/price_list.md` has *Cache write (1 hour)* in both tables, list date 2026-11-15, and no sentence "Cache writes ... are not priced". The 1-hour prices are 2x the input and the 5-minute prices 1.25x the input for all four Anthropic models, as the page's multipliers; I did not re-read the page (the orchestrator did, through an agent). Test across the two scripts: `CacheWritesAcrossScriptsTest`. |
| 8 (changed measuring tool gives `unknown`) | met | `TOOL_GROUPS`, `note_changed_tools`, `withdraw_values`; tests for the cost script, the measures script, the gate tools, "all three", unresolved pin, product cycle. See M1 for a sentence the foundation lacks. |
| 9 (comment at `MEASURES_FILE`) | met | the comment now reads "A copy that holds neither is of an earlier cycle or of one whose script failed", the module description's sentence. |
| 10 (*Unknown values* by field and reason) | met, and reaches further than the task's words | `unknown_rows`: one row for each pair, with count and first three examples; real run 1605 values in 106 rows. The task words say "wartości rejestru"; the rework (slice 18) groups every unknown value, the cycles' too, so the full list of a cycle's values now lies in git history only. The module description, the result's intro and `process-audit/SKILL.md` say so (after the fix of slice 18). I judge it within the intent of question 5 ("zalew") and name the cost in O3. |
| 11 (real runs) | met by the slices; the request must say what they gave | Slice 17: Codex cycle with 5 subagents, one defect found and fixed (`names_log` for a doubled-backslash path of a Codex custom tool call, 4 of 767 reads missed), test red first. Slice 18: count on the real register, exit 0, 0 `Error:` lines, 106 rows of *Unknown values* for 1605 values. Facts for the request's text: (a) the Codex cache measures stay `unknown` by design (the record's `cache_write_input_tokens` is a constant 0, no lifetime split); (b) a nested Claude Code helper in a Codex cycle was found in no rollout on the disk, so its measures were not tested on real data; (c) the register's repositories hold no Codex cycle. See M4 for a sentence of the description. |
| 12 (`todo_item`) | met | `re.split(r"[·,\n]", masked)`; bare `TODO` after a comma or a line break is an error; a described one gives "joins its items by ` · `". The plan's error text was not in the code; the executor followed the task's wording, which is right. |
| 13 (`decision:` line) | met | `elements/common/test_foundation_check.py:1500` now cites `WAY-03 "The check of the foundation lists an invariant whose method"`, the sentence the test checks (the citation is accepted by `foundation_check.py`, 0 errors). |
| 14 (`compile`) | met | `Resolver.runs` / `run_results`; `exec(compile(...))`, `code = compile(...); exec(code)` and `exec(codes[0])` (reported as code the check cannot read) still fail; a `compile` nothing runs passes; 40 tests of the file pass. A compiled object run by another route (`types.FunctionType(code, {})()`) passes now; the task's item narrows the check to `exec` and `eval` (O4). |
| 15 (dead-pointer test) | met | `product-guidelines/test_skill_references.py`. I ran its reader on the tree before the 16 corrections (`ef0a5ae`): it reports exactly 16 dead pointers (the 16 corrected ones); on the head it reports none. It reads only `product-guidelines/` and `project-level/`, passes product paths, names no path it opens (a lookup in a list of files). It imports only the standard library, so it adds no reach to a part the part map does not allow. No `description:` line of any skill changed in the range (`git diff` of every `SKILL.md`, grep of `^[-+]description:`: nothing). |
| 16 (remarks label under a list item) | met | `opens_paragraph` takes `MARKER`; description names the case; tests for `-`, `*`, `1.`, label with text on its line, label under a paragraph (opens nothing). |
| 17 (`a drive path in address form`) | met | `WINDOWS_DRIVE` second alternative; `https://host/C:/x`, `task/C:/x`, `//C:/x` and the others of the pin test stay unlisted; the escape-sequence rule keeps its meaning for the address form. |
| 18 (suffixes) | met | `MARKDOWN_SUFFIXES = (".md", ".markdown", ".mdx", ".mdc")`, `lower().endswith`; description, README and glossary say the same; test with four suffixes and one upper-case. |
| 19 (README, UTF-16 BOM) | met | the README sentence agrees with `private_paths_check.check_file` (`utf16 = data.startswith((BOM_UTF16_LE, BOM_UTF16_BE))` before the NUL test). |
| 20 (two installation tests) | met | both clone `SOURCE` into the test's temporary directory and install from the clone, as the four sibling tests do; the installer under test is copied in as in the siblings. Both ran: 4 tests OK. |

Settlements 1-8: each one is in the place its row names (WAY-344, WAY-339, price list and `cost_at`, `unknown_rows`, the dead-pointer test, the glossary term `Markdown file`). Questions 1-9: each answer is carried out as given; question 9 (parallel change of `foundation_check.py` and the sentence of WAY-344) is no finding, as the handoff says.

Source fidelity: the 1-hour prices, the dates and the exit codes are taken from the task and the page the executor read, not invented; the prices are consistent with the page's multipliers. The foundation entries say what the code does, except M1 and M2 below.

## The foundation entries the change writes (WAY-263)

I read WAY-337, WAY-339 and WAY-344 whole (the entries from their headings to the next heading, *Rationale* and *Rejected* included) and compared each binding sentence with the code:

- WAY-339: two kinds of series (`cost_boundary` / `count_boundary`); the tools that measure (`COST_SCRIPTS`, `MEASURES_SCRIPT`, `GATE_SCRIPTS`) and the unknown measure of a changed tool (`TOOL_GROUPS`); the cache-write columns as an input of the cost counted by two scripts, neither taking figures from the other's file (`CacheWritesAcrossScriptsTest`). Agrees, but see M1 and M3.
- WAY-344: the three exceptions (levels, forms of `stages.md` with and without the two write columns, `repository` entry) agree with `check_levels`, `section_table` and `the_way_checkout`. The one place where the code does more than the sentence says is M1.
- WAY-337: unchanged, as the spec says.
- Glossary `Markdown file` and the five corrected uses: agree with the code behind each of them (`endswith(".md")` in `foundation_check.py`, `GUIDELINES` pattern, `POINTED_SUFFIXES`); see M2 for the uses that were left.

## Changed tests named for the request (WAY-03)

- Invariant test changed: `cross-part-imports`, in `elements/part-map/test_cross_part_imports.py` (slice 13: the resolver reads `compile` only where `exec` or `eval` runs its result; the line `compile(open(...).read(), 'screen', mode='exec')` of `test_each_form_of_code_run_by_exec_eval_or_compile_is_read` was changed to `exec(compile(...))`, and a test that a standing `compile` is no dependency was added). The check is weaker by the task's item 14, on purpose.
- Test with a line `decision:` changed: `test_reworded_sentence_with_its_citing_file_changed_is_not_listed` in `elements/common/test_foundation_check.py:1500`: the cited sentence of WAY-03 changed from "A change whose check lists such an invariant" to "The check of the foundation lists an invariant whose method" (slice 12). No other `decision:` or `invariant:` line was added, changed or dropped in the range (grep of the diff).
- Sentences of invariants reworded while their tests stayed: `test-method-citation` and `guidelines-file-place` (the foundation entries: "Markdown" became "whose name ends in `.md`"). The check of the foundation at the head lists `guidelines-file-place` only (`test-method-citation` is no longer listed, since a file that cites it changed). The request names both in plain words.

## Minor findings within the task (the orchestrator has them fixed)

**M1. The sentence of WAY-339 and of WAY-344 does not say that a field missing from the file of a changed tool is dropped without an `Error:`.** Place: `process-audit/audit_count.py` `withdraw_values` (l. 2555-2575), which clears `cycle.missing` and the missing-field pairs of the file whose tool the cycle changed, and `note_changed_tools`, run before the `Error:` lines are built in `main`; the module description says it (`audit_count.py:222-223`), `foundations/decisions.md` WAY-339 (l. 7432-7459) and WAY-344 (l. 2741-2771) do not. Why it matters: WAY-344 says a missing field in a file of the record read from git history ends the run with exit 1 and an `Error:` line, and names no exception for a changed tool, so a reader of the entry expects the line the code does not give; the reading is reasoned (a file in the intermediate form of a tool the cycle itself changed would give the `Error:` in every later run, which WAY-344's rationale calls a signal-less exit code), and the values are `unknown` with the reason either way. Evidence: `MechanismMeasures.test_a_field_missing_from_the_file_of_a_changed_tool_is_not_read_and_ends_no_run`; grep of the two entries for the case finds nothing. Graded Minor and not Important: no figure is wrong, no sentence of the entries is contradicted by a sentence of the code, and the loss is one cycle. Remedy: one sentence in WAY-339 (the paragraph on a changed tool) saying that the file of that tool is not read for that cycle, so no field of it is missing and no `Error:` is given for it; this is the slice-8 review's Minor 1, which I confirm.

**M2. Uses of "Markdown file" that the new glossary definition moves were left in code, docstrings and one skill (WAY-97).** Places: `elements/common/foundation_check.py:35, 70, 72, 79, 92, 410, 750, 856` ("a file other than Markdown", "a Markdown file" for `endswith(".md")`; l. 856 is a message the check prints), `instruction-files/check_instructions.py:8, 569` and `instruction-files/SKILL.md:277` ("the Markdown files the root names", meaning `.md` and `.mdc`), `agent-instructions/test_instruction_files.py:4, 84` (`MARKDOWN_ENDINGS = (".md", ".markdown")`). The foundation step's report named them and left them to the slices and to this review; no slice changed them. Why it matters: WAY-97 has the author of a change to a definition rewrite, in the same change, each use whose meaning the new definition moves; a sentence "a file other than Markdown" reads under the new term as "not `.md`, `.markdown`, `.mdx` or `.mdc`", while the code treats `.mdc` and the rest as files that may hold a citing line. Why Minor: no behaviour follows, and the task's own source says neither the-way nor the product loop2 tracks such files today. Remedy: rewrite each as the foundation step did ("whose name does not end in `.md`", "ends in `.md` or `.mdc`"). The parallel task edits `foundation_check.py`; the cycle that merges second reconciles (task question 9).

**M3. The *Verification* of WAY-339 gives the unknown of a changed tool as an example for the gate-times script only.** `foundations/decisions.md`, WAY-339 *complies* and *violates* lines (about l. 7477-7490): the binding sentence names four tools, the example lines name one. Not wrong, so Minor (WAY-364); slice-1 review's Minor 3, confirmed. Remedy: a line for the script that measures the cost, which is the case the cycle itself is.

**M4. The module description of `task-cycle/cycle_measures.py` says "Codex's record gives no cache write" (l. 30, and the docstring at l. 588), which the real run shows is inexact.** Executor 17 found that the record has the field `cache_write_input_tokens`, which is 0 in all 6347 records, and has no lifetime split; the figures stay `unknown`, which is right (a zero that measures nothing), but the sentence gives a reason that is not the one. Task item 11 is about whether the measures of a real Codex cycle are full; the measure is empty on purpose and the sentence should say why. Remedy: reword to "Codex's record has no cache write by lifetime and its write field is a constant 0, so ...". Executor 17 named it and left it.

**M5. A count of about 4300 digits passes `required_count` and ends `cycle_stages.py` with a stack trace.** `task-cycle/cycle_stages.py:531-535` (`required_count`) accepts any non-negative `int`; `number()` formats the sum with `f"{value:,}"`. I ran three responses of `output_tokens` = 9 x 10^4299 through `cycle_stages.py`: exit 1 with `ValueError: Exceeds the limit (4300 digits)` and a trace (a count of 10^400 alone runs). At the trust boundary the task names, this is a crash with a stack trace, from a crafted transcript only; the audit's own reading of the same counts bounds them (`TOKEN_DIGITS = 15`). Slice-2 review's Minor 2, confirmed. Remedy: refuse a count longer than a stated number of digits as "not a whole number" in `required_count` (exit 2), with a test.

**M6. Comments and a docstring of `process-audit/audit_count.py` still say the unknown values are "given in full".** Lines 2279-2281 (docstring of `Analysis`: "each in full (`unknown`), and the values the register holds back ... (`held`)") and 2310-2311 ("every other unknown value is given in full"). After slice 18 every value goes through `unknown_rows`, so both are false, and the split into `unknown` and `held` is no longer a difference of treatment. Slice-18 review's M1, confirmed (not fixed by the fix round, which the findings file said). Also in the same file: `audit_count.py:3108` ("a cost belongs to that series only, and a new list starts a new one") reads as if the list were the whole rule of a series of the cost, which a change of `cycle_stages.py` now also ends (slice-6 review's Minor 1), and the paragraph on exit codes at `audit_count.py:248-256` does not say that the `Error:` line names the level (slice-5 review's Minor 1; the module description says it a screen above, at l. 204-207). Remedy: one edit each.

**M7. Style: unwrapped lines and two blank lines.** (a) Lines over 100 characters added by the change: `task-cycle/tracked_private_paths_check.py:16` (122 characters; the rewrap of the docstring left one long line), `task-cycle/skill/SKILL.md` step 12 (122 characters, the edited line), `task-cycle/cycle_measures.py:50-51` (101 and 111), `process-audit/audit_count.py` (about 8 lines of 101-106) and the lines of `foundations/decisions.md` (WAY-321 l. 1893, WAY-339 *Rationale* and *Rejected*, WAY-344 *Rejected*) and `elements/decisions/template.md:233` of 101-113, where the files wrap at 100 (slice-1 review's Minor 2 and slice-2's Minor 4). (b) `process-audit/test_audit_count.py`, class `Cost`: the added `written_cost` follows two blank lines where the class uses one (slice-7 review's Minor 1). No rule of an invariant is broken, and the foundation check passes (0 errors).

**M8. The goal sentence of slice 3 and the spec's D4, "after the slice the audit still reads the report", did not hold between slices 3 and 7 (slice-3 review's M1).** It holds at the head: `test_the_stage_report_cycle_stages_writes_gives_the_share` is green (the full file `process-audit/test_audit_count.py`, 231 tests, exit 0). Nothing to fix; named so that the list is complete.

## Minor findings and observations outside the task's scope (not fixed)

**O1. A crafted Codex rollout among the user's rollouts ends `cycle_stages.py` with a stack trace** (`task-cycle/cycle_stages.py` `codex_subagent_paths`, `codex_meta`: a `session_meta` with `parent_thread_id` and no `id` gives `KeyError`; a first line that is a JSON array gives `AttributeError`). Pre-existing: the base crashes on the same inputs; slice 1 only makes the search read every rollout where the orchestrator has no turn, which the base did on non-Windows systems. No write outside the places the script writes, no command run, no input text in the table. The task asks for no tolerance of malformed rollouts. Slice-1 review's Minor 1, confirmed.

**O2. `agent-<id>.meta.json` that is valid JSON but no object still crashes at `meta.get`** (`read_claude_session`). The task says the reading of that file does not change. Slice-2 review's out-of-scope finding 5, confirmed.

**O3. After slice 18 the full list of a *cycle's* unknown values lies only in the git history of the cycle's record; the result keeps the count and three examples.** The task's words are about "wartości rejestru" and say the full list stays in the register; the rework applies the same grouping to every value, because the real run gave 1605 rows on the first table. It is a choice of the orchestrator, written in the description, the result's intro and `process-audit/SKILL.md` (and held by `test_the_section_says_where_the_full_list_of_a_pair_stands_and_names_no_run_of_the_count`). It is no defect; named so that the request's *Human decisions* section shows the human that the listing of cycles' values was cut as well. The slice-9 review's Minor M1 (line count follows the number of issues) no longer holds: issue names are taken out of the field, and `test_a_register_far_larger_than_a_real_one_gives_one_line_for_each_pair` and `test_issues_that_differ_only_in_their_names_make_one_pair_for_each_kind_of_value` pin it.

**O4. Structure of the code the change leaves (WAY-363; the-way has no coding guidelines of its own, WAY-328, so no rule of size applies and each finding is Minor).** `python -B task-cycle/change_file_sizes.py <base> <head>`: `process-audit/audit_count.py` 2991 -> 3306 lines (+315), `process-audit/test_audit_count.py` 3185 -> 4158 (+973), `task-cycle/test_cycle_stages.py` 902 -> 1429 (+527), `task-cycle/cycle_stages.py` 1009 -> 1123 (+114). Functions of the changed files by `ast` on the base and on the head: `read_claude_agent` 81 -> 99 lines, `render` 156, `analyse` 154 (the two largest of `audit_count.py`; `analyse` grew little), `note_changed_tools` 23 and `withdraw_values` 21 new. No dead code that the change leaves, apart from `TURN_SUFFIX` in `audit_count.py:405`, which has no user and which the base already had unused (a constant the change did not touch); a name that stopped being true: none besides M6. The growth is what the items require; no action asked.

## Declined to judge

- `agent_type_copies.py` treats `Name:` (another case) as a line that is present and keeps exit 1; WAY-344 reads "stands under another name" and a stricter reading would give exit 2. The plan fixed this ("a line in another form is not claimed missing"); the message names the `name:` line and the file either way; effect nil.
- The shared reader of JSON lines (`numbered_lines`) now also catches `UnicodeDecodeError`, `RecursionError`, `MemoryError` and any `ValueError`, and `read_session` refuses a first line that is no object, for a Codex rollout too: a change in a reading the slice fenced off, disclosed by the executor, harmless (slice-2 review's Minor 3).
- A compiled object run by another route than `exec` and `eval` is no longer reported by the imports test (see item 14); the task narrows the check on purpose.
- Whether the price list should price the 30-minute and 12-hour cache writes that the OpenAI page now gives for some models: executor 4 named it; Codex rows hold no writes, so no cost depends on it. For the human.
- The prices themselves against the Anthropic and OpenAI pages: not re-read; checked only for consistency with the page's multipliers and with the orchestrator's check.
- The range's merge with the parallel task on `foundation_check.py` and the sentence of WAY-344 (task question 9).

## Slices that had no review of their own (4, 10, 11, 12, 13, 14, 15, 16)

I judged each as section 2 of the method gives, with its executor's own-work check (WAY-164):

- 4 (price list): the data and the description match the spec and `read_prices`; the four 1-hour prices follow the page's multiplier; the OpenAI cells are `—`; no `audit_count.py` change. The own-work check (compare every cell with the page) is the right one for the weakest requirement.
- 10 (prose of `process-audit/`): `process-audit/SKILL.md` and `problem_register.md` say what the code does (two kinds of series, the five forms of `stages.md` with their lacks, the date of a class starting the count-of-remarks series). Checked against `cost_boundary`, `count_boundary`, `section_table`; no sentence disagrees.
- 11: met; see item 2 and the Declined line on `Name:`. The own-work check ran the exit code and the unchanged-tree assertion.
- 12: met against the task's wording (the plan's error text was not in the code, the executor wrote the task's); the probe of 57 hostile values found two crashes and fixed them (`TODO,`, `TODO·TODO`: the match is now made against the full value); I re-ran the test file (190 tests OK).
- 13: met; see item 14; the own-work check named the right weakness (a `compile` whose result is run by `exec` or `eval` through a name) and the test pins it; I probed six indirect forms myself: direct, through a name, with a namespace, and through two names are reported, a list and a lambda are reported as unreadable, `types.FunctionType` passes (Declined).
- 14: the dead-pointer test is real (16 pointers found on the earlier tree, none on the head); its repair (sample drive path built in pieces) keeps `tracked_private_paths_check` at 0 listed (`checked: 310 files, 0 listed`, exit 0).
- 15: met; the new regular expressions are linear, tests pin the neighbours that must stay unlisted.
- 16: met; one long docstring line (M7), the rest as items 18-20.

## Checks I ran

All from the worktree root or from the directory of the test file, working copies only under `.runs/review-whole/` (removed).

| Check | Command | Exit |
|---|---|---|
| Head | `git rev-parse HEAD` | 0, `84d062b...` |
| Foundation | `python -B elements/common/foundation_check.py` | 0, `0 errors`, one `listed:` line (`guidelines-file-place`) |
| Private paths in tracked files | `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0, `checked: 310 files, 0 listed` |
| Index of decisions | `python -B elements/common/decision_index.py --output .runs/review-whole/index.md --section ... --part ... --decision ...` | 0 (58 in full, 139 by heading) |
| Remarks check tests | `python -B -m unittest test_remarks_check` (in `task-cycle/`) | 0, 64 tests |
| Private paths tests | `python -B -m unittest test_private_paths_check` | 0, 54 tests |
| Tracked private paths tests | `python -B -m unittest test_tracked_private_paths_check` | 0, 21 tests |
| Measures tests | `python -B -m unittest test_cycle_measures` | 0, 89 tests |
| Stages tests | `python -B -m unittest test_cycle_stages` | 0, 69 tests |
| Agent type copies tests | `python -B -m unittest test_agent_type_copies` (in `agent-instructions/`) | 0, 9 tests |
| Imports test | `python -B -m unittest test_cross_part_imports` (in `elements/part-map/`) | 0, 40 tests |
| Foundation check tests | `python -B -m unittest test_foundation_check` (in `elements/common/`) | 0, 190 tests |
| Dead-pointer test | `python -B -m unittest discover -s product-guidelines -p test_skill_references.py` | 0, 14 tests |
| Audit tests | `python -B -m unittest test_audit_count` (in `process-audit/`) | 0, 231 tests (308 s) |
| Installation tests | `python -B -m unittest test_styleguide_installation test_testing_guidelines_installation` (in `installation/`) | 0, 4 tests |
| Dead pointers on the earlier tree | `git archive ef0a5ae`, then `check_tree` of the new test on it | 16 problems, as the 16 corrections |
| Crafted counts at `cycle_stages.py` | three responses of 9 x 10^4299 output tokens | 1, trace (M5) |
| Indirect runs of a compiled object | six lines through `Code.run_from_core` | as described under item 14 |
| File sizes | `python -B task-cycle/change_file_sizes.py 7f5c5a5 84d062b` | 0 |

No run of the whole gate (WAY-160). The two tests that read the live repository (`test_skill_references`, the installation tests) ran against the worktree as it stands.

## Reaches beyond my selection (what, where, why)

- `elements/common/way_of_working.md` ("Reading the foundation") and `product-guidelines/reading.md`: the method of my selection; the-way holds no guidelines of its own (WAY-328), so I read none.
- `task-cycle/private_paths_check.py` `check_file` (l. 138-155), `task-cycle/remarks_check.py` `MARKER` and `opens_paragraph`, `agent-instructions/skill_entry_points.py` not at all: only to check items 16 and 19.
- `git grep` of "Markdown" in tracked English files, for M2; of `series`, for stale sentences; of `invariant:` and `decision:` in the diff, for WAY-03.
- The executor reports of slices 4, 11, 12, 17 and 18 and the slice reviews' findings in the handoff; the reports of slices 10, 13-16 only for the lines I name.

## Unread material

Decisions of the index read whole: **3** of 58 listed in full (WAY-337, WAY-339, WAY-344), plus WAY-03 read whole (4 in all). The other 54 I read by the binding sentences the index gives, without *Rationale*, *Rejected* or *Verification*: among them those that bear on the change and stayed unopened whole are WAY-07, WAY-12, WAY-97, WAY-99, WAY-161, WAY-263, WAY-294, WAY-297, WAY-309, WAY-320, WAY-328, WAY-363, WAY-364, WAY-368 (the task names several of them; none of my findings rests on a *Rationale* of them, and WAY-97 and WAY-99 are the ground of M2, read in their binding sentences). I did not run through the headings of the 139 decisions listed by heading alone; the sections I chose are in the report's selection (the index is kept beside this report as `review-whole-index.md`).
Guideline files: none selected (WAY-328: the-way holds none).
Invariants, part-map entries, glossary entries: the part map read whole; invariants read by the sentences of those the change reaches (`test-method-citation`, `guidelines-file-place`, `cross-part-imports`, `tracked-file-private-paths`, `audit-series-script-paths`, `script-language`, `script-imports`, `script-subprocesses` by name and the check of the foundation), not the whole file; the glossary entry `Markdown file` and the entries around it, not the whole glossary.
The plan (`plan.md`, 63 KB): read only the slice 11 and slice 87-127 lines I name; the reports of slices 1, 2, 3, 5-9, 15, 16 and the reviews of slices were not read beyond the handoff's findings. `executor-18-rework` and `-fix` reports were read whole.
`process-audit/audit_count.py` and `task-cycle/cycle_stages.py`: read through the diff of the range and the functions it reaches, not whole.

## Searches not found or unclear

- A sentence in WAY-339 or WAY-344 that says the file of a changed tool is not read for the cycle (so no `Error:` for its missing field): not found (M1).
- A user of `TURN_SUFFIX` in `process-audit/audit_count.py`: none (pre-existing).
- The plan's "error that says the items of the field are joined by ` · `": not in the code before the change (the executor's own search); now present.
- A nested Claude Code helper of a Codex cycle in the data on the disk: not found by executor 17, so the question of item 11 about its measures stays unanswered by real data.
- Whether "Markdown file" in `foundation_check.py` means `.md` alone on purpose: the foundation step said it reads `.md` alone; unclear whether the sibling task rewords the same lines.

## Working copies

All under `.runs/review-whole/` of the worktree: the index and its list of sections, the output of the test runs, a `git archive` of `ef0a5ae` (the tree before the 16 pointer corrections), two probe scripts (`probe_compile.py`, `fsize.py`) and a transcript probe directory. Removed before returning, apart from the index, which I copied to `.runs/task-cycles/scripts-after-foundation-review/reports/review-whole-index.md`. `git status` of the worktree is clean. No watcher or timer was started; four test runs I started in the background had all ended before I returned.
