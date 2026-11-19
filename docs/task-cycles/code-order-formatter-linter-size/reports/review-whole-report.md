PASS d0a861d9ca22cb2a1cb364d8224bc01f3cd65a44

# Review of the whole change — code-order-formatter-linter-size

- Reviewed: the whole change, base `d69fb20b` .. head `d0a861d9` (branch
  `task/code-order-formatter-linter-size`); `git rev-parse HEAD` in the worktree gave
  `d0a861d9ca22cb2a1cb364d8224bc01f3cd65a44`, the head of the handoff.
- Method: `task-cycle/review/SKILL.md` and `task-cycle/review/whole_change.md` of the worktree, read whole.
- Counts: blocking 0; Minor 11 (10 within the task, 1 outside it); out of scope 1 (the Minor outside
  the task); slice-review findings withdrawn 2, resolved 1.

## Findings

### Critical

none

### Important

none

### Minor — within the task

1. **A `yapf: disable` comment switches the formatter off and the gate stays green.**
   `agent-instructions/test_linter_invariant.py:49` (`FORMATTER_SWITCH`) and the class `Formatter` at
   `agent-instructions/test_linter_invariant.py:176-197`. Ruff 0.17.1 takes `# yapf: disable` and
   `# yapf: enable` as it takes `# fmt: off` and `# fmt: on`; the test's pattern finds only the three
   `fmt:` comments. A file can so stand outside the formatter's layout with both tests of
   `formatter-layout` passing — the consequence the task's answer "Czy komentarze wyłączające formater
   są zakazane? — tak (a)" names under its rejected way (b). Evidence: in
   `.runs/review-whole/yapf/` a file `X = 1` / `# yapf: disable` / `Y = [1,2]` / `# yapf: enable` /
   `Z = 1` gave `ruff format --check --config ruff.toml --no-cache` "1 file already formatted" (exit 0
   for that file), while the same file with `X = [1,2]` above the comment was reported; the pattern
   `\bfmt:\s*(?:off|on|skip)\b` does not match `yapf: disable`. Why Minor and not blocking: the code
   does what the settlement row 5, WAY-382 and `formatter-layout` say word for word — they name the
   three `fmt:` comments — and no file of the-way holds a `yapf:` comment today. The fix is the
   pattern widened to the two `yapf:` comments together with the words of WAY-382's second paragraph
   and of `formatter-layout` (both written by this change, F1 and F4), so it reaches a foundation
   entry and is the human's to accept; were it left, the request should name the gap.

2. **The reformatting made eleven files parse only on Python 3.14.**
   Ruff's formatter, run at `target-version = "py314"`, removed the brackets of fourteen `except (A,
   B):` clauses (PEP 758), for example `elements/common/foundation_source.py:48`,
   `elements/common/decision_index.py:75`, `elements/common/compare_log_entries.py:61`,
   `elements/common/migrate_foundation.py:863`, `instruction-files/check_instructions.py:516,766`,
   `process-audit/audit_count.py:520`, `process-audit/version_analysis.py:111`,
   `task-cycle/cycle_measures.py:496` and three test files. Every file of the base compiles on
   Python 3.12; at the head eleven do not (`SyntaxError: multiple exception types must be
   parenthesized`), and `python -B elements/common/foundation_check.py` and
   `elements/common/decision_index.py`, which ran on 3.12 at the base (`0 errors`, exit 0), stop with
   that `SyntaxError` at the head. Why Minor: the-way declares Python 3.14 for its scripts (WAY-89,
   `.python-version`) and tells a product to have it (`installation/README.md:14,165`), CI runs 3.14,
   and under 3.14 every file parses to the same tree, so no promise breaks. What it changes is that a
   product or a session on an older Python, which the base happened to serve, now gets a
   `SyntaxError` from the foundation check, the decision index, the instruction check and the audit.
   The fix is no code: a sentence in the request saying that the code now parses only on the Python
   it declares; a change of it (brackets kept) would take a setting of the formatter other than its
   default, a change of WAY-382.

3. **`README.md:106-107` still calls `ruff.toml` "the settings of the linter".** Since
   `6c13454c` the file also holds the formatter's width and its exclusion of Markdown (WAY-382), and
   the list of the repository's files there names neither the formatter nor `.git-blame-ignore-revs`.
   A name that stopped being true with this change; the agent of slice 3 saw it and left it as
   outside its section. Fix: "the settings of the linter and the formatter".

4. **`task-cycle/gate_times.py:213-216` and `:239-242` name the parsed name of a registry file
   `file`.** `file = parse_name(name)` holds a tuple (start, end, token), not a file or a path; the
   slice 10 renaming made `entry` into `file`, which reads as a path or an open handle beside the
   real file names of the same loops. Polish; a name such as `parsed` or `run` would say what it is.

5. **The test name `test_a_deeper_line_under_the_first_sub_item_is_no_sub_item_of_the_list`**
   (`process-audit/test_record_items.py`, renamed in `462add5d` from
   `test_a_sub_entry_under_the_first_entry_is_no_entry_of_the_list`). The record it reads holds a
   nested list item under the first sub-item; "a deeper line" drops that the line is itself a list
   item, which is what the test is about. Graded as the slice 10 review graded it: wording only.

6. **`guidelines/coding-shared-module.md:4` (*Applies to*) and `:38-41` (*Where in code*) do not name
   `task-cycle`, where `task-cycle/stage_transcripts.py`, a module of the kind `shared-module`, now
   stands.** The task carried to the cycle the question of the kind of the modules moved out
   ("Do jakiego rodzaju kodu należą moduły wydzielone przy podziale plików"), and the plan's *Choices*
   12 answered `shared-module` with no row in the kind's table; the table is not the gap — WAY-199
   asks a status only of the files a kind's guidelines list — but an agent changing
   `stage_transcripts.py` selects no guideline of its kind by `product-guidelines/reading.md`,
   since the file applies to `relation-model` and `process-audit` only. The slice 13 review graded
   this Minor and outside the task; I keep it Minor and within the task, since the task asked the
   question. The fix is an extension of the kind's guidelines (its *Applies to* and *Where in code*),
   made as `maintain-coding-guidelines` gives.

7. **The shared base of the audit's modules stands in the record reader.**
   `process-audit/record_reading.py` holds `AuditCountError`, `Git`, `GitError`, `table_cells`,
   `is_separator`, `THE_WAY` and `MAX_BYTES`, which `process-audit/problem_register.py:19`,
   `process-audit/version_analysis.py:35` and `process-audit/audit_report.py:19` import from it, so the
   register imports from the reader of records with which it shares only these. Below every threshold
   of WAY-385 (`record_reading.py` 1149 lines), so Minor by WAY-363, as the slice 15 review graded it.

8. **The sentence of `audit-series-script-paths` (`foundations/invariants.md`, rewritten by F9 in this
   change) and the first sentence of `process-audit/test_audit_series_scripts.py` still say the paths
   are those "whose history `process-audit/audit_count.py` reads".** Since `a30a04ff` the paths and
   the `git diff` that reads their history stand in `process-audit/version_analysis.py`, which the
   command imports; the docstring's second paragraph already says so. As a sentence of the command
   it stays true, so no departure from the entry (WAY-263) — a reader who looks for the reading in
   `audit_count.py` finds none. Graded as the slice 16 review graded it.

9. **`process-audit/audit_report.py` names the two files of the cost script by constants in one
   sentence and by literals in two others**: `:86` uses `COST_SCRIPT` and `COST_MODULE`, while
   `:150-152` and `:323-324` write `task-cycle/cycle_stages.py` and `task-cycle/stage_transcripts.py`
   out. A later move of either file would change one sentence of the report and leave two. Graded as
   the slice 17 review graded it.

10. **`process-audit/audit_count.py:76` and `process-audit/price_list.md:21` say that
    `task-cycle/cycle_stages.py` folds the cache writes into *Input*.** Since `1f09e4d6` the fold
    (`claude_usage`) stands in `task-cycle/stage_transcripts.py`, which `cycle_stages.py` imports. True
    of the command, as in finding 8; a name the change made less exact. The slice 17 review graded
    it outside the task; I grade it within, since the move that made it so is this task's
    (`whole_change.md`: a name that stopped being true). `audit_count.py:62` ("`stages.md` that
    `task-cycle/cycle_stages.py` writes") stays exact.

### Minor — outside the task

11. **`installation/install.py:448` `plan` stands at 109 lines against the threshold of 110** (the
    note of slice 19). The change did not grow it: it was 109 lines after the reformatting
    (`015ce05c`) and is 109 at the head. Any later addition to it must begin with a move out
    (WAY-365). Outside the task: no line of this change added to it; it goes to the request's list,
    not to the fix.

### Findings of the slice reviews, graded here

| Slice review | Finding | My grade |
|---|---|---|
| 10 | fixture text "entries none" at `process-audit/test_record_items.py:58,128` | withdrawn: the fixture is the text of an item *Discarded attempt*, which `task-cycle/record_template.md:38-40` fills with "changed files including foundation entries", so "entries" there means foundation entries, the glossary's meaning; not a use To do 8 replaces |
| 10 | the name `test_a_deeper_line_under_the_first_sub_item_is_no_sub_item_of_the_list` | Minor within the task (finding 5) |
| 13 | `stage_transcripts.py` in no table of `guidelines/coding-shared-module.md` | Minor within the task, restated (finding 6) |
| 15 | the shared base stands in `record_reading.py` | Minor within the task (finding 7) |
| 15 | `read_prices`, `fill` and `read_repository` stayed in `audit_count.py` | withdrawn: the plan moved them only "where the cut needs them"; `audit_count.py` stands at 868 lines with no function over 110, and the price list and the repository are inputs of the command itself; no consequence named or found |
| 16 | the comment over `__all__` of `audit_count.py` | resolved: `4e5f95fb` removed `__all__` and its comment; no `__all__` stands in `process-audit/*.py` (search) |
| 16 | `audit-series-script-paths` and the docstring of `test_audit_series_scripts.py` | Minor within the task (finding 8) |
| 17 | constants and literals in `audit_report.py` | Minor within the task (finding 9) |
| 17 | `price_list.md:21`, `audit_count.py:62,76` | Minor within the task for `:76` and `price_list.md:21` (finding 10); `:62` no finding |

### Known notes judged

- `README.md` around line 106: finding 3.
- `installation/install.py` `plan` at 109 lines: finding 11.
- The task's *To do* 1-8, both acceptance criteria and rows 1-5 of *Settlements to record*: met by
  the commits, as "Against the task" below gives; acceptance 1 (CI on Linux and Windows) is the
  orchestrator's run (WAY-160).
- `formatter-layout` (F4) and its tests (`5e8fa379`): the code meets the sentence; the test was seen
  failing both ways by the executor (reports `executor-3-break-*-failing-run.txt`); finding 1 is the
  gap of the wording.
- `own-foundation-check-report` (F3) and its test (`2620dcc3`): met; my own runs below.
- The entries marked `the cycle's`: F6 (`line` for the plan's log of changes — To do 8 names WAY-145
  and the phrase; the word is the one `project-level/plan/template.md` already uses), F7 and F8 (`file`
  for the registry — To do 8 names WAY-350 and `gate-times-refuses-impossible-entry`; WAY-350's own
  sentence calls the registry "an empty file for each run"), F9 (WAY-339 and
  `audit-series-script-paths` name both files — follows from To do 4: every part of `cycle_stages.py`
  measures the cost, so any division leaves the cost script in two files, and leaving the list as it
  was would let a change of the moved code start no series, against WAY-339's meaning), WAY-09's
  *Verification* gaining `own-foundation-check-report` (WAY-12: a decision names the invariants
  derived from it, and F3 derives from WAY-09), WAY-382's *Scope* gaining `repository` (`ruff.toml`
  stands in that part, as for WAY-380). Each follows from the task with no other way left open but the
  choice of a word, which To do 8 leaves to the cycle ("słowem, które pasuje w danym miejscu").
- The mismatches the orchestrator's mechanical check passed on: slice 3's line in
  `agent-instructions/test_script_invariants.py:65` (the test of the files that are no script failed
  on the new file and asks for its kind in `NAMES`; right); slice 17's widened *Change*
  (`process-audit/SKILL.md:54`, the docstring of `audit_count.py`, the text of `audit_report.py`;
  each now names both files); the cut of the modules (`committed_date` in fact stands in
  `version_analysis.py`, which `audit_count.py` imports; `fill`, `read_repository` and `read_prices`
  stay in `audit_count.py`; `count_rows`, `cost_rows` and `money` stand in `version_analysis.py` and
  `audit_report.py` imports `money` from it) — no consequence found; slice 4's comment above
  `OWN_FINDINGS` (drops the claim that the other findings depend on the clone's main branch, which
  the clone runs did not bear out); slice 9's use of `GIT_CONFIG_COUNT` (git 2.31 or later; on an
  older git the variables are ignored and the test is as flaky as before, nothing worse).

## Against the task

- **To do 1.** `ruff.toml` (`6c13454c`): `line-length = 100`, `[format] exclude = ["*.md"]`, comment
  naming WAY-382. `015ce05c` holds only formatter output: from a worktree of `6c13454c`, running the
  pinned Ruff's `format --config ruff.toml --no-cache` over the 79 tracked `.py` files of the parts
  ("78 files reformatted, 1 file left unchanged") gave a tree with no difference from `015ce05c`
  (`git diff 015ce05c` empty). `.git-blame-ignore-revs` holds its full hash, a comment line above it,
  and `foundations/part_map.md` gives the file to `repository`.
- **To do 2.** The test class `Formatter` with its two tests citing `formatter-layout`; the example of
  `installation/README.md:121-127` laid out as the formatter lays it out; `### Formatter` of
  `guidelines/coding.md:43-55` names WAY-382 · WAY-381 and `formatter-layout`, with *Good*, *Bad*
  and a paragraph that names no command (template `product-guidelines/coding/template.md:159-162,
  319-343`); `README.md` "Installing the linter" speaks of the formatter. Finding 1 for the `yapf:`
  comments.
- **To do 3.** `<ruff> check --ignore-noqa` over the parts passes at the head (the linter's invariant
  test passes unmarked); the fixes (`8fecce81`, `d6442f89`, `c41a772d`, `222c5a7b`) stand in the files
  that held the reports, with no rule turned off and no `noqa` added. TRY004 keeps exit code 2 and the
  message (`cycle_stages.py` `required_time` raises `MissingFieldError` with the same text before
  the `try`).
- **To do 4.** WAY-385 reads 110 and 1200 on the formatted code; the size test passes at the head
  (below).
- **To do 5.** Both expected failures removed (`222c5a7b`, `d0a861d9`); both invariants read
  `Violated: no`; no sentence on a known violation stands in the two test descriptions, in
  `guidelines/coding.md` or in WAY-380 and WAY-385 (search of `violated`, `expected failure`,
  `expectedFailure` at the head).
- **To do 6.** `test_the_way_foundation_check_reports_no_error` cites `own-foundation-check-report`;
  the narrow test stays with its two citations; `README.md:177-179` says the whole check runs in the
  gate. Acceptance 2: in a clone of the head whose only main branch is a local `main` at `f16616c0`
  and with no `origin`, the check gives `0 errors` (exit 0) and the test passes; with
  `Reference WAY-9999 here.` appended to `guidelines/testing.md` the new test fails with
  "guidelines/testing.md:271: `WAY-9999` names no decision of the log" and the narrow test passes.
- **To do 7.** `ENVIRONMENT` of `task-cycle/test_remove_merged_worktrees.py:31-47` sets
  `gc.auto=0` and `maintenance.auto=false` for every git process of the tests, `origin.git` and the
  script under test included (`env=ENVIRONMENT`); `state` and the assertions are unchanged; the cause
  stands in comments.
- **To do 8.** The six files hold no replaced use of `entr` (search at the head: only the invariant
  identifier, two uses meaning foundation entries in `project-level/lead/skill/SKILL.md:11,142`, and
  the fixture of the withdrawn slice-10 finding); WAY-145, WAY-350 and the invariant sentence
  reworded; no glossary entry added.
- **Settlements rows 1-5**: row 1 WAY-382 sentence 1; row 2 WAY-385; row 3 `own-foundation-check-report`;
  row 4 WAY-382 sentence 3 and `[format] exclude`; row 5 WAY-382 sentence 3, `formatter-layout` and the
  second test of `Formatter` (finding 1).
- **Nothing added that nobody asked for**, beyond the slice-3 line in `test_script_invariants.py`
  that the gate required.
- **Reserved choice**: none settled; Ruff's formatter is the tool WAY-381 already pins.

## The structure of the code the change leaves

- `python -B task-cycle/change_file_sizes.py d69fb20b d0a861d9` (reviewed worktree, exit 0): 95 files,
  55029 lines before, 64506 after (+9477). Largest scripts after: `elements/common/migrate_foundation.py`
  1162 (992 before), `process-audit/record_reading.py` 1149 (new), `elements/common/foundation_check.py`
  1141 (999), `process-audit/version_analysis.py` 1058 (new), `task-cycle/request_check.py` 768 (582),
  `process-audit/audit_count.py` 868 (3031), `task-cycle/cycle_stages.py` 582 (1183).
- The size test, in worktrees of my directory: at the base with its mark taken off (thresholds
  80/1000) it fails naming 11 functions and 2 files (the task's numbers); at the base with 110/1200 it
  names 5 functions and 1 file; at the head (110/1200, no mark) it passes. At the head with 80/1000 it
  would name 10 functions and 4 files — the reformatting's growth, which the new thresholds absorb.
  Nothing the head names is new against the base.
- Functions nearest the threshold at the head, each as it stood after the reformatting (my script over
  `git show` at `015ce05c` and `d0a861d9`): `installation/install.py:448` `plan` 109 (109),
  `task-cycle/cycle_stages.py:416` `report` 108 (108), `task-cycle/cycle_stages.py:229` `build_rows` 98
  (98), `process-audit/problem_register.py:266` `read_register` 93 (93 in `audit_count.py`),
  `task-cycle/stage_transcripts.py:618` `read_claude_agent` 91 (114, divided). No function grew past
  its post-reformatting size; the eleven over 110 were divided.
- Code left with no user: `__all__` and the imports kept for the tests are gone (`4e5f95fb`); the linter
  (F401 blocking) finds no unused import at the head. Names that stopped being true: findings 3, 8 and
  10.

## Declined to judge

- That `line-length = 100` stands at the top of `ruff.toml` and so also reaches the linter's rules
  that read a line length: WAY-380 fixes no width of the linter, the 24 reports stayed the same at
  slice 1 and the linter's invariant passes at the head; no behaviour of the task rests on it.
- That WAY-382 says "every other setting at its default" while `ruff.toml` sets `[format] exclude`:
  the next sentence of the same decision requires the formatter to cover `.py` files only, which the
  exclusion carries out, and the task's own wording has the same pair; no reader is misled.
- That no test of the suite holds `shared-module-import-runs-nothing` for the five new modules: the
  invariant names `relation-model/fingerprint.py` alone, as it did for `stage_pricing.py` and
  `record_items.py` before; widening it is a change of the foundation the task does not ask for.
- That a local `main` far behind the head can make the full foundation check report a decision
  "added and held by nothing": the plan's *Choices* 8 takes that cost on purpose, and a `main` at
  `f16616c0` gave no error.

## Changed invariant tests and tests holding a decision (WAY-03)

Changed by a commit other than the reformatting (every test file of the parts was also re-laid out
by `015ce05c`):
`agent-instructions/test_linter_invariant.py` (`ruff-blocking-rules` unmarked, `formatter-layout` new),
`agent-instructions/test_size_invariant.py` (`function-and-file-size` unmarked and thresholds; its
line `decision: WAY-385`), `elements/common/test_foundation_check.py` (`own-foundation-check-report`
new; the comment of the test of `map-reference-target` and `test-method-citation`),
`process-audit/test_audit_series_scripts.py` (`audit-series-script-paths`, expected set),
`process-audit/test_audit_count.py` (imports and expected tuple; lines `decision: WAY-339`, `WAY-344`
and others; `audit-count-refuses-record-links`), `task-cycle/test_gate_times.py`
(`gate-times-refuses-impossible-entry`, tests renamed), `task-cycle/test_cycle_stages.py` (imports;
`cycle-stages-refuses-crafted-names`, lines `decision: WAY-339`, `WAY-344`),
`task-cycle/test_remove_merged_worktrees.py` (`repository-changer-acts-only-when-told`),
`process-audit/test_record_items.py` (renamed tests holding lines `decision: WAY-405` and others),
`elements/common/test_migrate_foundation.py` (`repository-changer-acts-only-when-told`),
`agent-instructions/test_instruction_files.py`, `gate/test_skills_reach_the_way_sessions.py`,
`installation/test_agent_types_installation.py`, `installation/test_installed_guidance.py`,
`task-cycle/test_cycle_measures.py` (each a one-line fix of the linter in a file that cites an
invariant), `agent-instructions/test_script_invariants.py` (one name in `NAMES`). I read each change
against its sentence: none weakens an assertion (WAY-233); the one changed expected value
(`test_audit_series_scripts.py`, `test_audit_count.py`, the cost script in two files) gives its cause.

## Checks

| Check | Command or method | Result |
|---|---|---|
| Head | `git rev-parse HEAD` in the worktree | `d0a861d9…`, exit 0 |
| Sizes of the changed files | `python -B task-cycle/change_file_sizes.py d69fb20b d0a861d9` (worktree root) | exit 0, table above |
| Size test on the base, mark off | `python -B -m unittest agent-instructions/test_size_invariant.py` in `.runs/review-whole/base` (mark replaced by `pass`) | exit 1: 11 functions over 80, 2 files over 1000 |
| Size test on the base at 110/1200 | same, thresholds edited in the copy | exit 1: 5 functions, 1 file |
| Size test on the head | same in `.runs/review-whole/head` | exit 0, 4 tests OK |
| Size test on the head at 80/1000 | same, thresholds edited in the copy, then restored | exit 1: 10 functions, 4 files |
| The reformatting is formatter output only | in the base worktree checked out at `6c13454c`: `<ruff> format --config ruff.toml --no-cache` over the 79 tracked `.py` files of the parts, then `git diff --stat 015ce05c` | "78 files reformatted, 1 file left unchanged"; no difference from `015ce05c` |
| Blame file names the reformatting | `git log -1 --format='%H %s' 015ce05c` | the reformatting commit, the hash of `.git-blame-ignore-revs` |
| Focused gate `agent-instructions` | `python -B gate/run_tests.py agent-instructions` in the head worktree | exit 0, 52 tests OK (linter, formatter and size invariants, no expected failure) |
| Focused gate `process-audit` | `python -B gate/run_tests.py process-audit` | exit 0, 277 tests OK |
| Focused gate `task-cycle` | `python -B gate/run_tests.py task-cycle` | exit 0, 534 tests OK (skipped=2) |
| Focused gates `project-level`, `instruction-files`, `installation`, `elements/common`, `gate` | `python -B gate/run_tests.py <directory>` each, in the head worktree | each exit 0: project-level 281 OK; instruction-files 105 OK (skipped=5); installation 73 OK; elements/common 271 OK; gate 36 OK |
| Foundation check in a clone with an old local `main` | `.runs/review-whole/clone-main` (shared clone of the head, `main` at `f16616c0`, `origin` removed): `python -B elements/common/foundation_check.py .` | exit 0, `0 errors`, no listed line |
| Acceptance 2, passing and failing | in that clone: `python -B -m unittest elements.common.test_foundation_check.FoundationCheckTest.test_the_way_foundation_check_reports_no_error`; then with `WAY-9999` appended to `guidelines/testing.md`, both own-foundation tests | exit 0; then the new test fails naming the reference, the narrow test passes; file restored |
| `yapf:` comments | `<ruff> format --check --config ../../../ruff.toml --no-cache a.py b.py` in `.runs/review-whole/yapf` | exit 1 for `a.py` only: `b.py`, unformatted inside `# yapf: disable`, passes (finding 1) |
| Python 3.12 parse | `py -3.12 -B parse312.py base` / `head` (compiles each tracked `.py`) | base: 0 fail; head: 11 fail (finding 2) |
| Foundation check and index on 3.12 | `py -3.12 -B base/elements/common/foundation_check.py base`; same for head; `decision_index.py --sections` likewise | base exit 0 `0 errors` and index exit 0; head `SyntaxError` for both |
| Trust boundary `cycle_stages.py` | base and head `task-cycle/cycle_stages.py <transcript> --output …` on two real Claude Code transcripts of this machine (`4ae61def…`, `ed7e731d…`) | exit 0 both; report, stdout and stderr byte-identical |
| Trust boundary `check_instructions.py` | base and head on the head worktree, on `another repository of the author`, on a notes vault and on a crafted repository (dead path, missing `@` imports, `@../outside.md`, nested `AGENTS.md`) | exit codes and output identical in all four |
| `request_check.py` (slice 12, no review of its own) | `rc_diff.py`: base and head on `task-cycle/skill/request_template.md`, on each variant with one line dropped and on one with a second block, each with the Polish task and an English task | exit 0: 1156 runs, 0 differ in exit code, stdout or stderr |
| Unmoved lines of the moves | `unmoved.py` over `1f09e4d6`, `2dbccee8`, `a30a04ff`, `612146a2`, `72150951`, `679112e3`: the lines each adds that it removes nowhere, and the reverse | read: only imports, descriptions, the named divisions and test imports (the lists were removed with the directory) |
| Target branch | `git log --oneline d69fb20b..foundations` | empty: no second reformatting needed today |

Not run: the full gate (the orchestrator's or CI's, WAY-160); CI on Linux (acceptance 1), so the
stability of the worktree test on Linux is unverified here; `audit_count.py` end to end on a real
register (it writes into the user's places outside the repository) — the slice 15 and 16 reviews
compared its report bytes.

## Reaches beyond the handoff

- `a private rule file of the author` and `.ai/rules/git.md` — the user's
  instructions require them before a script and before `git worktree add` (a hook stopped the first
  call).
- `task-cycle/record_template.md:38-41` — to judge the slice-10 finding on "entries none".
- `process-audit/stage_pricing.py` description not read; `installation/README.md:1-20, 100-135`,
  `.github/workflows/tests.yml` (setup-python lines) — for finding 2.
- Two real Claude Code transcripts under `~/.claude/projects/C--Storage-repos-the-way/` — read only,
  as input of the differential run of `cycle_stages.py`; the reports made from them were removed with
  my directory.

## Working copies

All under `.runs/review-whole/`:
worktrees `base` (`d69fb20b`, at times `6c13454c`) and `head` (`d0a861d9`), the shared clone
`clone-main`, the directories `yapf` and `crafted`, the scripts `sizes.py`, `unmoved.py`,
`parse312.py`, `rc_diff.py`, the index `index.md` and `sections.md`, run outputs. Removed: both
worktrees by `git worktree remove --force`, then `git worktree prune`; then `rm -rf` of
`.runs/review-whole/` (the clone and every file with it). `git worktree list` names none of them and
`.runs/` holds only `orchestrator/` and `task-cycles/`; `git status` of the reviewed worktree is
clean. Nothing remains, and nothing was kept in `reports/` beyond this report: the results stand in
the table of checks.

## Unread material

25 decisions of the index of my selection read whole: WAY-03, WAY-08, WAY-12, WAY-16, WAY-48,
WAY-51, WAY-52, WAY-53, WAY-95, WAY-97, WAY-99, WAY-145, WAY-205, WAY-225, WAY-233, WAY-339,
WAY-350, WAY-365, WAY-379, WAY-380, WAY-381, WAY-382, WAY-383, WAY-384, WAY-385.

- Decisions that bear on the change and stayed unread whole: WAY-09 (its binding sentence in the
  index and the diff of its *Verification* only), WAY-61, WAY-62, WAY-89, WAY-38, WAY-321, WAY-344,
  WAY-360, WAY-361, WAY-363, WAY-391, WAY-392 (each its binding sentences in the index only).
- The rest of the 68 decisions listed in full in the index: binding sentences only; the 161 listed by
  heading: run through by question, and of them WAY-12, WAY-48, WAY-52, WAY-53, WAY-97, WAY-99,
  WAY-225 and WAY-365 opened.
- Invariants: those this change writes or rewords and those its altered tests cite, read whole
  (`formatter-layout`, `own-foundation-check-report`, `ruff-blocking-rules`,
  `function-and-file-size`, `audit-series-script-paths`, `gate-times-refuses-impossible-entry`,
  `map-reference-target`, `test-method-citation`, `repository-changer-acts-only-when-told`,
  `cycle-stages-refuses-crafted-names`, `audit-count-refuses-record-links`, `script-imports`,
  `cycle-measures-refuses-nested-line`, `check-instructions-refuses-outside-links`,
  `installation-paths-through-links`, `repository-file-location`, `shared-module-import-runs-nothing`,
  `cross-part-imports` (its sentence)); the other invariants whose *Part* names `every` or a touched
  part — most of `foundations/invariants.md` — not read.
- Part map: read whole. Glossary: `entry` only.
- Guidelines: `guidelines/coding.md` and `guidelines/coding-shared-module.md` read whole;
  `guidelines/testing.md`, `guidelines/coding-check.md`, `guidelines/coding-measuring-report.md`,
  `guidelines/coding-repository-changer.md`, `guidelines/coding-command-runner.md` and
  `guidelines/coding-generator.md` not read whole (their rules have no invariant the change reaches
  beyond those above; the slice executors and reviewers had them).
- `product-guidelines/coding/template.md`: lines 127-186 and 319-344 only.
- Diffs: every non-reformatting commit read in full, except the three moves (`1f09e4d6`, `2dbccee8`,
  `a30a04ff`) and `679112e3`, read as their unmoved lines (script above) and at the divided functions
  (`read_gate`, `waiting_days`, the `CodexScan` field `current`); `015ce05c` checked by reproduction,
  not read.
- Reports: the agent of the entries, executors 3, 4, 9, 19 read whole; executors 12 and 14 their
  own-work checks only; executors 1, 6, 7, 8 not read (their diffs were read in full); the slice
  reviews: the slice-10 report's two findings and the slice-13 compare output only.

## Searches not found or unclear

- `__all__` in `process-audit/*.py` at the head: not found (as expected after `4e5f95fb`).
- `yapf` in the decision log, the invariants and the coding guidelines: not found; the settlement's
  list of formatter-off comments omits it (finding 1).
- A statement that the reformatting may change which Python versions parse the code: not found in
  the task, the plan or WAY-382 (finding 2).
- Unclear: whether the handoff's "`committed_date` … stay in `audit_count.py`" is exact — the import
  list of `audit_count.py` takes `committed_date` from `version_analysis.py`.
