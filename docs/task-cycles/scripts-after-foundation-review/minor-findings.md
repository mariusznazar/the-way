# Findings of slice reviews that no fix touches (for the request's lists)

## From review 1 (slice 1 and the foundation entries; report `reports/review-1-report.md`)

### Minor

1. **Out of scope, pre-existing: a crafted rollout beside the orchestrator's gives a stack trace.** `task-cycle/cycle_stages.py:455-456` (`codex_subagent_paths`) and `:277` (`codex_meta`). Where the orchestrator has no turn the search now has no lower bound, so every `rollout-*.jsonl` under `home/sessions` is read by `codex_meta`. I ran `cycle_stages.py <idle rollout> --codex-home <home>` at the head with one extra rollout in the home:
   - `session_meta` with `parent_thread_id` and no `id` -> exit 1, `KeyError: 'id'` (line 456);
   - first line a JSON array (`[1,2]`) -> exit 1, `AttributeError: 'list' object has no attribute 'get'` (line 277);
   - `session_meta` whose payload is an array -> exit 1, `AttributeError` (line 455);
   - an empty rollout and a non-JSON first line -> exit 1 with a clean `Error:` line (correct).
   The same four inputs crash the base too, and also with a lower bound whenever the stray file is newer than the floor, so the slice did not introduce them and the task's *To do* 4 (the epoch call) does not reach them; the cost of the slice is only that the unbounded search reads more files. No write outside the places the script writes, no command run, no input text reaching the table. Slice 2 reworks the reading of a transcript and is where the checks of a rollout's first line belong (WAY-344: the invariant of reading fields). Not blocking: the task asks for no tolerance of malformed rollouts.
2. **Minor, polish: lines over 100 characters in the foundation entries.** Added lines of `foundations/decisions.md` (WAY-321 line 1893, WAY-339 *Rationale* and *Rejected*, one line of WAY-344 *Rejected*), `foundations/invariants.md` (`test-method-citation`, `guidelines-file-place` are single-line entries, so these two are expected) and `elements/decisions/template.md:233` are 101-113 characters where the files wrap at 100. The foundation check passes (`0 errors`); no reader reads it wrongly. Only the lines in the decisions file that the commits re-wrapped partially are worth fixing at the next edit of those entries.
3. **Minor, coverage: the *Verification* of WAY-339 gives the unknown of a changed measuring tool only for the script that records the gate times.** `foundations/decisions.md`, WAY-339 *complies* and *violates*: the sentence of the rule names four tools (the cost script, the script of the measures of context and cache use, the script that records the gate times, the test runner), the example lines name one. A reader of the entry still finds the rule whole in the binding paragraph, so no sentence is read wrongly; a line for the cost script would match task row 4 (`cycle_stages.py`, `cycle_measures.py`, `gate_times.py`, `gate/run_tests.py`) as written. The tests of the audit are for the later slices.


## From review 2 (slice 2; report `reports/review-2-report.md`; the blocking finding 1 is fixed in the fix round)

### Minor

**2. A count of about 4300 digits passes the check as a whole number and then, summed over responses, ends the script with a stack trace.** `task-cycle/cycle_stages.py:517-521` (`required_count`) accepts any non-negative `int`; the sum goes into `number()`, which formats it with `f"{value:,}"`. Evidence: three responses of `output_tokens` = 9 * 10^4299 (4300 digits each, which `json.loads` accepts): exit 1 with `ValueError: Exceeds the limit (4300 digits) for integer string conversion`. A count of 10^400 alone, and of 3 * 10^4000, runs with exit 0. The executor named this as a residual. The spec sets no upper bound, and the contrivance (a transcript made for it, no real source) keeps it Minor; the cheapest remedy is to reject a count of more than a stated number of digits as "not a whole number" in `required_count`, or to name the residual as a decision.

**3. The shared line reader of the Codex reading changed.** `numbered_lines`/`read_lines` (`cycle_stages.py:251-270`) now also catch `UnicodeDecodeError`, `RecursionError`, `MemoryError` and any `ValueError`, and `read_session` refuses a first line that is no object, for the Codex rollout too (exit 1 with `Error:` instead of a trace). The slice says the reading of a Codex rollout "does not change". No field is checked and no Codex test changed, so it is no breach of WAY-344 (no new missing field is read for another file), but it is a change nobody asked for in a file the slice fences off; the executor disclosed it (choice 5). Harmless; named so the human sees it.

**4. The edited line of step 12 in `task-cycle/skill/SKILL.md` is 122 characters long** (the paragraph around it is wrapped at about 100; the line starts "with exit code 2 and an `Error:` line, record the command, ..."). Rewrapping the paragraph would keep the file's form. No rule of an invariant is broken.

### Out of scope

**5. `agent-<id>.meta.json` that is valid JSON but no object (a list) still crashes at `meta.get`** (`cycle_stages.py`, `read_claude_session`). The task says the reading of that file does not change; the executor named it. Beyond the task, so not blocking.


## From review 3 (slice 3) (report `reports/review-3-report.md`)

### Minor

**M1. The slice's own goal sentence, "after the slice the audit still reads the report", does not hold for
the report the changed script now writes (plan-mandated, not made by the executor).**
- Place: `process-audit/audit_count.py:953-975` (`section_table`), unchanged by this slice; the sentence is in
  the slice's Goal and its Checks line ("the audit still reads the report of the earlier forms").
- What: `section_table` accepts the header of the detailed table only if it equals the eight needed columns or
  those plus *Files named* (line 970-974). The report of `cycle_stages.py` now has eleven columns, so the audit
  answers "not of the form the stage report gives" and prices the cost, the count and the share `unknown`.
  The one test that runs the stage script and reads it with the audit,
  `process-audit/test_audit_count.py:865` (`test_the_stage_report_cycle_stages_writes_gives_the_share`), is red:
  `['0.014250', '1', '15.8%'] != ['unknown', 'unknown', 'unknown']`.
- Judgement of the orchestrator's question: the cause is exactly the refused header and nothing else. Evidence:
  I ran the subset (below); 50 of 51 pass, the one failure is that test with the three `unknown` values and
  no crash, no `Error:`; the code of `section_table` has no other path that gives "unknown" for this input
  (the eleven-cell rows would also fail the `len(cells) != columns` check, but the header check comes first).
  The fixture edit in `test_audit_count.py:836-838` (two zero lifetimes in `answered()`) is needed and
  sufficient: without it the script ends with exit 2 before the audit is reached.
- Why it matters, and why Minor: between this slice and Slice 7 a cycle run with the new script would lose its
  cost in the audit (with a reason, not silently), and the focused check the slice names is red. Slice 7's Goal
  makes the audit read the three forms of the header, which makes this test green again, and the plan's order
  (writer before reader) is a chosen one; the branch is not released between slices. It would be Important if
  Slice 7 were dropped or did not restore this test. The orchestrator should carry into Slice 7 that this test
  must be green at its end, and the spec's sentence in D4 "the audit still reads the report" is true only after
  Slice 7.

## From review 5 (slice 5) (report `reports/review-5-report.md`)

### Minor

1. `process-audit/audit_count.py:248-256` (the paragraph on exit codes) — the goal of the slice says the module description says, beside its exit codes, that the `Error:` line names the level. The change says it in the paragraph on the register's tables (`audit_count.py:204-207`), a screen above; the paragraph on exit codes still says only "a table of the register refused as a whole". The description does say it, and no reader is led wrong, so the effect is a reader of the exit codes who does not learn that the line names the level. Evidence: `git diff` of the file touches only the lines near 205.

## From review 6 (slice 6) (report `reports/review-6-report.md`)

### Minor

1. `process-audit/audit_count.py:2908-2909` (section *Cost*): "a cost belongs to that series only, and a new list starts a new one (WAY-339)". After this slice a series of the cost also ends at a change of `task-cycle/cycle_stages.py`, so a price list is no longer the only thing a cost's series is told by (the module description at `audit_count.py:258`, "(the series the cost belongs to)", says the same). The sentence is not false (a new list does start a new series) but it reads as if the list were the whole rule. The section is not the *Process versions* section the slice rewrites, and Slice 7 reworks the cost, so the wording is better made right there. Evidence: the two sentences against `cost_boundary` (`audit_count.py:2404`).

## From review 7 (slice 7) (report `reports/review-7-report.md`)

### Minor

1. `process-audit/test_audit_count.py` (the added `def written_cost` in class `Cost`, right after `test_...disagree...`): the added methods follow two blank lines inside the class body (the diff shows `+    def written_cost` after an existing blank line that ended the previous method and another that the diff keeps), where the rest of the class uses one. Style only; no effect on behaviour or on any check. Evidence: the hunk at `@@ -1267,6 +1308,130 @@` and the end of the hunk, which adds two blank lines before `SECTION = ...`.

## From review 8 (slice 8) (report `reports/review-8-report.md`)

### Minor

1. **A field missing from the file of a changed tool is dropped silently; the foundation does not say that.** `process-audit/audit_count.py` `withdraw_values` (about l. 2518-2538) clears `cycle.missing` and the `missing_in` pairs of the file whose tool changed, and `note_changed_tools` runs before the `Error:` lines are built in `main` (about l. 3248-3254). So a cycle that changes `task-cycle/cycle_measures.py` and writes a file that lacks a label gives the measures `unknown` with the reason, and the run ends with exit 0.
   - The orchestrator's note says the executor's reading is "as the foundation entries now say it". I read WAY-339 (`foundations/decisions.md:7432-7585`) and WAY-344 (`foundations/decisions.md:2741-2900`), and grep found no sentence in the foundation that says the file of a changed tool is not read. WAY-339 says only "the audit gives the measures of that tool for that cycle as unknown, with the reason that the cycle changed the tool that wrote them, and its other measures as they stand". WAY-344 says a missing field in a file of the record read from git history ends the run with exit 1 and a line `Error:`, and does not except a changed tool. Both readings fit the words, so this is a choice of the executor, not something the foundation settles.
   - Why Minor and not Important: the reading is reasoned (a file in the intermediate form of a tool that the cycle itself changed would give an `Error:` at every later run, and WAY-344's rationale calls an exit code that every run gives a signal-less one); the loss is limited to the one cycle that changed the tool, since the next cycle's file is read and its missing field shows; the values are `unknown` either way, so no figure is wrong; and one test pins it (`MechanismMeasures.test_a_field_missing_from_the_file_of_a_changed_tool_is_not_read_and_ends_no_run`), and the module description says it (`audit_count.py:222-223`, "The file of a changed tool is not read for the cycle, so no field of it is missing").
   - Price if left: the very cycle whose change may have broken a tool's output form gives no `Error:` for it. Price if reversed (keep the `Error:` for the missing field): such a cycle's `Error:` line stays in every later run, since a copy in git history cannot be mended.
   - Recommendation: the orchestrator confirms the reading and has it written in the sentence of WAY-339 (or the "complies" list of WAY-344) that the next foundation step touches, so the code and the entry say the same. Nothing for the executor to change.

## From review 9 (slice 9; report `reports/review-9-report.md`; the blocking finding is fixed in the fix round)

### Minor

**M1. The number of lines still follows the number of issues, because the field of an issue's value carries the issue's name.**
Place: `process-audit/audit_count.py` `register_unknown_rows` (the field is the value with only `row N of ` normalised), fed by `the fix of issue \`name\`` (about line 2371) and `waiting of issue \`name\`` (about lines 2398-2416).
What is wrong: each issue with an unknown fix or an unknown waiting is its own pair, so the section has one line for each such issue. I ran a scratch register with 3000 open issues each with a problem of an unread cycle: 3001 pair rows (result of 9117 lines); with 3000 fixed issues whose fix is not in the history: 3000 pair rows. The limit that bounded this (`MAX_LISTED`) is gone and nothing replaces it for these values. A real register has far fewer issues than problem rows, so the flood the task names (about 830 lines from problem rows) is gone, and the pair is read literally (field includes the name); the cost shows only with a large register of issues. Graded Minor because the task's line is "one line for each pair of a field and a reason" and the field of such a value is arguably the issue's.
Evidence: scratch test in `.runs/review-9/test_scratch.py` (removed with the directory, see Working copies): prints `pairs 3001` and `pairs 3000`. Resolving I1 by keeping those values in the first table would leave this as it was before the change.


## From review 17 (slice 17) (report `reports/review-17-report.md`)

(no Minor section found in the report)

## From review 18 (slice 18 rework; report `reports/review-18-report.md`)

### Minor

**M1. Two comments of the code still say the unknown values are "given in full".**
- `process-audit/audit_count.py:2279` (docstring of `Analysis`): "the values it leaves unknown as (repository, record, value, why), each in full (`unknown`), and the values the register holds back ... (`held`)".
- `process-audit/audit_count.py:2309-2310` (comment in `analyse`): "The values the register holds back ... are the ones grouped by field and reason; every other unknown value is given in full."
After the rework every value goes through `unknown_rows`, so both sentences are false; the first also keeps the two lists `unknown` and `held` described as two kinds of treatment. They are comments for the next author of the file, so not blocking by themselves; they are a sentence about where a full list stands that is not true. Fix with I1.

### Out of scope

None.


## From review 18 fix (slice 18) (report `reports/review-18-fix-report.md`)

## Minor (not blocking; not given to the fix, as the findings file said)

- M1 of the earlier review remains: `process-audit/audit_count.py:2279` (docstring of `Analysis`, "each in full (`unknown`)") and `process-audit/audit_count.py:2310` (comment "every other unknown value is given in full") are false after the rework. Minor findings of a slice review are not fixed; named so that the whole-change review sees it.

## From the review of the whole change (report `reports/review-whole-report.md`): the Minor findings within the task, M1-M7, were given to the fix round; those outside the task's scope are in the report's own section

## From the review of the whole-change fix (report `reports/review-whole-fix-report.md`; Minor findings of the fix itself: not fixed)

## Minor findings of the fix (block nothing)

- **N1. The new example line of WAY-339 gives the cost script's unknown values as cost and share only.** `foundations/decisions.md`, WAY-339 *complies*: "a cycle whose own change changes the script that measures the cost gives its cost and the share of its cost in fix rounds as unknown ... and its other measures as they stand". `withdraw_values` also gives the two stage times (*Working time without waiting for tools*, *Waiting for tools*) as unknown for that tool (`STAGES_VALUES`), and the binding sentence says "the measures of that tool". The example is narrower than the code and "its other measures as they stand" would read the times as standing. No sentence of the binding paragraph is contradicted. Remedy: "its times, its cost and the share of its cost in fix rounds as unknown".
- **N2. The fix changed an invariant test, which the request must name (WAY-03).** `agent-instructions/test_instruction_files.py` (tests of the invariants `instruction-file-imports` and `root-claude-md-import`): `MARKDOWN_ENDINGS = (".md", ".markdown")` became `POINTED_ENDINGS = (".md", ".mdc")` and the fixture `docs/other.markdown` became `docs/other.mdc` in four places. The change is more than the words M2 asked for. It makes the test's population of repository instruction files equal to the glossary definition (`.md` or `.mdc`) and to `POINTED_SUFFIXES` in the check script, so I judge it right and no weakening against the invariants' sentences; it does narrow the population (a tracked `.markdown` file named by the root is no longer read), which is what the glossary entry says. The executor disclosed it with its reason; the 5 tests pass.
- **N3. One new line over 100 characters:** `task-cycle/cycle_stages.py`, module description, "message that names the transcript, the line and the field. Read with a fallback, and no error where absent: a line with no" (122 characters; the edit about the 15-digit bound left the paragraph unwrapped). Polish.


## From the review of the return step (report `reports/review-return-step-report.md`; blocking finding fixed in the fix round)

### Minor

**2. WAY-339 clause drops the instructions of the reviewer from the changes that start a series of the count of remarks.**
Place: `foundations/decisions.md:7454-7456`: "a series of the count of remarks also at a date of the list of classes and a change of the files that give the form of a stage report or of the type of agent the reviewer receives its instructions as". The binding sentence (`:7423-7424`) says "a change of the form of a stage report, of the list of classes or of the instructions of the reviewer", and `COUNT_PATHS` (`audit_count.py:421`) holds `task-cycle/review` among the four method directories and the type `the-way-stage.md`. The old pair named "a change of the reviewer's instructions" outright. The clause now reads as if the directory `task-cycle/review` were not among the paths; the test `test_a_change_under_the_review_starts_a_series_of_the_count_and_none_of_the_cost` (decision line present) holds it. A reader who takes the clause for the full list would read the reviewer's instructions as outside it. Minor because the binding sentence is untouched and the test holds the case; one phrase ("or of the instructions of the reviewer") would close it.

**3. Two sentences of the old pairs lost their only statement.**
(a) WAY-339, the author's instructions: the binding sentence says "no change of the instructions of the cycle, the reviewer's and the author's included, starts one"; the old *violates* line named "a change of the reviewer's or the author's instructions divides the series of the gate times". The new clause says "none of these splits …", where "these" are the price list, the scripts, the list of classes and the files of the form and of the reviewer; a change of the author's instructions is in no clause and in no tagged test for the measures (the author's type of agent appears only in a test of the count and the cost, `test_audit_count.py:3354-3362`, and in the table at `:3429`, neither tagged for WAY-339's measures). (b) WAY-344, the entry `repository` "for that entry alone": the old *violates* line "reads any other missing entry of that file as having a value of its own" has no clause; the test `test_a_named_repository_the_file_lacks` (`test_audit_count.py:830-835`) holds it but carries no line `decision:`. Both are covered by code and by tests; the loss is in what an agent comparing a change reads. Minor.


## From return step fix review (report `reports/review-return-step-fix-report.md`)

(no Minor section found in the report)

## From review of correction 1 (the correction's Minor finding: not fixed) (report `reports/review-correction-1-report.md`)

(no Minor section found in the report)
