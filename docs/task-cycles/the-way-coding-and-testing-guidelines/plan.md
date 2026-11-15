# Plan — the way: coding and testing guidelines of the-way itself (end of the transitional state WAY-328)

- Task: `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md` (frozen; status `ready for cycle`, approved 2026-11-15, last commit of the note `a05edac6`)
- Spec: none
- Base: `2d593214e4ce11676880b1f3ac3aa75884e023ab`

How to read this plan. The task document is cited as its path and line range at the base; the line
numbers of its sections are those of the frozen copy. An entry written by the plan's *Foundation
entries* is named in a slice by its row (`E7`, and so on); the agent of those entries returns each
row's identifier in its report, and the orchestrator carries it into the handoffs. Where a slice
names `<ruff>`, it means `.runs/quality-venv/Scripts/ruff.exe` (on POSIX `.runs/quality-venv/bin/ruff`)
under the main checkout, the parent of the directory `git rev-parse --git-common-dir` prints.

## Foundation entries

Written first by one agent following `task-cycle/skill/foundation_step.md`, each by the `SKILL.md` of
its element, before slice 1; except `E39` and `E40`, which the slice named writes together with the
file it adds, because the check of the foundation reports a path pattern of the part map that matches
no tracked file (see *Choices*). The identifiers in the *Entry* column are the plan's proposals; the
writer takes the identifier the element's rules give. Tests that cite an invariant are written by the
slices named; the agent of the entries runs the check of the foundation with
`--skip-test-citations`.

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| E1 — the-way adopts the template of the coding discipline for its own code | decision | row 1 | Slices 18–21 (the *Decision* fields of the coding guidelines) |
| E2 — the linter: ruff 0.17.1, the default set of that version without preview, `target-version` py314, the parts it reads, the 18 rules kept as examples, a comment that turns a rule off has no effect, disabling a rule for the whole of the-way is a change of the decision | decision | row 3 | Slices 1, 16, 21 |
| E3 — the pin of the version: `required-version` in `ruff.toml`, `requirements-quality.in` and `.txt` with the SHA-256 of each wheel, the environment `.runs/quality-venv` installed by the README, CI gets an installation step only | decision | row 4 | Slices 1, 16, 21 |
| E4 — departure from the formatter, with the reason and the way back | decision | row 11 | Slice 21 |
| E5 — departure from the audit of dependencies, with the reason of row 12 | decision | row 12 | Slice 21 |
| E6 — departure from the six rules on failures and logs (way 4 of the template's "Departing from the rules on failures and logs") | decision | row 13 | Slice 21 |
| E7 — the rule of size: 80 lines a function with its nested functions, 1000 lines a file of a script, tests excluded, no exceptions, counted by a test over `ast` that runs apart from the linter | decision | row 14 | Slices 17, 21 |
| E8 — the six kinds of code and the exemplar of each (one decision a kind where the log's rules for an entry ask it) | decision | row 18 | Slices 12–15, 18–21 |
| E9 — the-way adopts the template of the testing discipline for its own tests | decision | row 2 | Slice 22 |
| E10 — the five levels of tests: unit, files, git, repository, e2e | decision | row 20 | Slice 22 |
| E11 — the sources of expected values of the-way's tests | decision | row 25 | Slices 2, 3, 22 |
| E12 — the fields of a recipe that bind, and the departure from *Time limit* | decision | row 26 | Slice 22 |
| E13 — the exemplar test of each level | decision | row 27 | Slice 22 |
| E14 — what the-way does not test on purpose: the behaviour of an agent that follows a skill | decision | row 28 | Slice 22 |
| E15 — departure from mutation testing, with its condition of return | decision | row 29 | Slice 22 |
| E16 — WAY-09 gains the directory `guidelines/` of the-way's own guidelines, which the part map gives to `agent-instructions` | change of a decision | row 31 | Slices 18, 23 |
| E17 — WAY-328 withdrawn | withdrawal of a decision | row 32 | Slices 21, 22, 23 |
| E18 — WAY-344: the sentence of its *Rationale* and the item of its *Rejected* that name WAY-328 | change of a decision | row 33 | Slice 21 |
| E19 — WAY-363: the example in its *Verification* that names a script of this repository with no coding guidelines | change of a decision | row 34 | none (a foundation edit that the withdrawal of E17 requires) |
| E20 — WAY-38 gains the sentence that the tests of the standing checks run the pinned tool from the environment the repository declares | change of a decision | row 9 | Slice 16 |
| E21 — `script-subprocesses` gains the same sentence | change of an invariant | row 10 | Slice 16 |
| E22 — invariant `ruff-blocking-rules`: no file of the parts named breaks a rule of the set that blocks; `Violated: yes`; rests on E37 | invariant, with its test `agent-instructions/test_linter_invariant.py` | row 6 | Slices 16, 21 |
| E23 — invariant `function-and-file-size`: no function and no file of a script of the parts named is longer than its threshold; `Violated: yes` | invariant, with its test `agent-instructions/test_size_invariant.py` | row 15 | Slices 17, 21 |
| E24 — invariant `generator-writes-only-with-write` | invariant, with its tests in Slice 12 | row 19 | Slices 12, 19 |
| E25 — invariant `repository-changer-acts-only-when-told` | invariant, with its tests in Slice 13 | row 19 | Slices 13, 20 |
| E26 — invariant `command-runner-passes-exit-code` | invariant, with its test in Slice 14 | row 19 | Slices 14, 20 |
| E27 — invariant `shared-module-import-runs-nothing` | invariant, with its test in Slice 15 | row 19 | Slices 15, 18 |
| E28 — invariant of the refusal of `project-level/readiness_check.py` (a file that is not UTF-8 is refused with exit 2) | invariant, derived from WAY-48 · WAY-235, citing an existing test | row 30 | Slices 2, 22 |
| E29 — invariant of the refusal of `task-cycle/cycle_stages.py` (crafted names neither split a row nor enter the column) | invariant, citing an existing test | row 30 | Slices 4, 22 |
| E30 — invariant of the refusal of `task-cycle/cycle_measures.py` (a line nested too deeply ends with exit 2 and nothing written) | invariant, citing an existing test | row 30 | Slices 5, 22 |
| E31 — invariant of the refusal of `task-cycle/gate_times.py` (a registry entry with a time that cannot be counts for nothing) | invariant, citing an existing test | row 30 | Slices 6, 22 |
| E32 — invariant of the refusal of `process-audit/audit_count.py` (a symbolic link leaving the record is not followed) | invariant, citing an existing test | row 30 | Slices 8, 22 |
| E33 — invariant of the refusal of `instruction-files/check_instructions.py` (a file link out of the repository is neither read nor listed) | invariant, citing an existing test | row 30 | Slices 11, 22 |
| E34 — the glossary term for the files level (`files`) | glossary | row 21 | Slice 22 |
| E35 — the glossary term for the git level (`git`) | glossary | row 22 | Slice 22 |
| E36 — the glossary term for the repository level (`repository`) | glossary | row 23 | Slice 22 |
| E37 — environment fact: the default set of ruff 0.17.1, 407 rules, from `DEFAULT_SELECTORS` at the tag | environment fact | row 7 | Slices 1, 16, 21 |
| E38 — environment fact: ruff with `required-version` ends with an error where the running version does not meet it | environment fact | row 8 | Slices 1, 16 |
| E39 — part map: `repository` lists `/ruff.toml`, `/requirements-quality.in`, `/requirements-quality.txt` | part-map line, written by Slice 1 | To do item 11, answer 23 | Slice 1 |
| E40 — part map: `agent-instructions` lists `guidelines/**` | part-map line, written by Slice 18 | To do item 11, answer 23, WAY-167 | Slice 18 |

## Slices

### Slice 1 — The linter's configuration and its installation

- **Goal:** ruff 0.17.1 is declared and installable, and CI installs it. The root holds `ruff.toml`
  with `required-version = "==0.17.1"`, `target-version = "py314"`, preview off, a `select` that
  lists exactly the 389 rules of E2 (the 407 rules of the default set of that version, which E37
  names the source of, less the 18 kept as examples), and an exclusion of what git ignores that a
  working copy may hold; the pinned `ruff` itself gives the 407 (its default selection) and the
  list is checked against the source E37 quotes. `requirements-quality.in` holds `ruff==0.17.1` and
  the option that allows wheels only; `requirements-quality.txt` holds the same option, a comment
  naming where the sums come from, and `ruff==0.17.1` with a `--hash=sha256:` line for every wheel
  that release publishes at `https://pypi.org/pypi/ruff/0.17.1/json`, no source distribution. The
  section "Running the tests" of `README.md` gives the installation (`python -m venv
  .runs/quality-venv`, then `pip install --require-hashes -r requirements-quality.txt` from that
  environment's own interpreter, for Windows and for POSIX, and the check `ruff --version`), says
  that the tests of the standing checks find that environment in the main checkout through the
  common directory of git (answer 25) and that one installation serves every working directory, and
  names no command of ruff to run beside the gate. The job `tests` of `.github/workflows/tests.yml`
  gets one step before `python -B gate/run_tests.py` that creates `.runs/quality-venv` and installs
  from the requirements file; the one checking command stays `python -B gate/run_tests.py` (WAY-16).
  Through `update-part-map`, the part `repository` of `foundations/part_map.md` lists the three
  files (E39). The slice needs the network (the sums; the install check); where it has none it
  returns `blocked` with that reason.
- **Change:** `ruff.toml` · `requirements-quality.in` · `requirements-quality.txt` · `README.md` · `.github/workflows/tests.yml` · `foundations/part_map.md`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:30-30` To do (item 4)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:72-86` Questions to settle (answers 1 to 3)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:197-202` Questions to settle (answer 25)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:229-229` Context (the fact of the default set)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:454-454` Human actions
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:516-518` Settlements to record (rows 3 to 5)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:520-521` Settlements to record (rows 7 and 8)
  · E2 · E3 · E37 · E38 · E39
  · `foundations/decisions.md:2597-2642` WAY-16
  · `foundations/decisions.md:8664-8724` WAY-203
  · `foundations/decisions.md:8726-8776` WAY-204
  · `foundations/invariants.md:66-74` ci-checking-commands
  · `elements/part-map/skill/SKILL.md` · `elements/part-map/template.md` · `elements/common/rules.md`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `<ruff> --version` prints `ruff 0.17.1`; `<ruff> check --config ruff.toml --show-settings
  agent-instructions/skill_entry_points.py` lists 389 enabled rules and none of the 18 of E2; `<ruff>
  check --config ruff.toml --no-cache --ignore-noqa --output-format concise` on the directories of
  the parts with Python (`agent-instructions`, `elements`, `gate`, `installation`,
  `instruction-files`, `process-audit`, `product-guidelines`, `project-level`, `relation-model`,
  `task-cycle`) runs with no error of configuration (it reports the places other slices clean or
  leave); an installation into a new environment in the agent's own directory under `.runs/` with
  `pip install --require-hashes -r requirements-quality.txt` ends with `ruff --version` giving
  0.17.1, and the environment is removed; `python -B elements/common/foundation_check.py
  --skip-test-citations` exits 0
- **Depends on:** Foundation entries E2 · E3 · E37 · E38

### Slice 2 — The sections of a definition written out in the readiness test, and the refusal invariant of `readiness_check.py`

- **Goal:** in `project-level/test_readiness_check.py` the list of the sections of a definition is
  written out in the test with its source in a comment (the headings of the form in
  `project-level/definition_template.md`), no longer taken from `readiness_check.SECTIONS`, so that a
  section dropped from the code's tuple no longer vanishes from the test data (cause 1; every place
  of the file that takes `readiness_check.SECTIONS` for an input or an expectation). The test
  `test_a_file_that_is_not_utf_8_exits_two` carries the line `# invariant: <identifier of E28>`
  (item 8). Both changes are shown to fail once: the sections test fails when a section is removed
  from the tuple for a moment, and the cited test fails when the refusal of a file that is not UTF-8
  is broken for a moment (item 9, WAY-08); each break is undone. The code it writes breaks no rule
  of `ruff.toml`.
- **Change:** `project-level/test_readiness_check.py`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:34-35` To do (items 8 and 9)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:38-38` To do (item 12)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:177-181` Questions to settle (answer 21)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:232-238` Context (cause 1)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:543-543` Settlements to record (row 30)
  · E28 · E11
  · `foundations/decisions.md:2492-2520` WAY-48
  · `foundations/decisions.md:9188-9242` WAY-235
  · `foundations/decisions.md:1746-1774` WAY-08
  · `foundations/decisions.md:9062-9100` WAY-232
  · `foundations/decisions.md:9102-9142` WAY-233
  · `foundations/invariants.md:166-174` test-method-citation
  · `foundations/part_map.md:80-99` project-level
  · `project-level/readiness_check.py:1-52` the description and the tuple of sections
  · `project-level/definition_template.md:39-75` the form of a definition
- **Model:** cheaper
- **Risk:** trust boundary — `project-level/readiness_check.py` (the slice adds the citation of the invariant of its refusal; the file itself is not changed)
- **Checks:** `python -B project-level/test_readiness_check.py` exits 0; the section test shown failing
  with `SECTIONS` changed for a moment and the cited test shown failing with the refusal broken for a
  moment, each with the command and its exit code, the changes undone (`git diff -- project-level/readiness_check.py`
  empty); `<ruff> check --config ruff.toml --no-cache --ignore-noqa project-level/test_readiness_check.py`
  reports nothing on a line the slice wrote; `python -B elements/common/foundation_check.py
  --skip-test-citations` exits 0
- **Depends on:** Foundation entries E28 · Slice 1

### Slice 3 — The expected block, the list of skills and the entry points written out in the installer test, and the form of `capture_output`

- **Goal:** in `installation/test_install.py` the expected block of `AGENTS.md`, the list of skills
  and the text of an entry point are written out in the test with their source in a comment (the
  README of the installation and the skills the installer carries), no longer taken from
  `install.SKILLS`, `install.agents_block()` and `install.skill_wrapper(...)`, so that the test no
  longer passes whatever the installer writes (cause 2: every place that takes its expectation from
  those three). The call at the head of the file that captures the output of a process with
  `stdout=PIPE, stderr=PIPE` uses `capture_output=True` (cause 27, the place of this file only).
  The test is shown to fail once: it fails when the installer's block or the text of an entry point
  is changed for a moment, undone after. `installation/install.py` is not changed. The code it
  writes breaks no rule of `ruff.toml`.
- **Change:** `installation/test_install.py`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:39-39` To do (item 13)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:46-46` To do (item 20)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:92-97` Questions to settle (answer 5)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:239-245` Context (cause 2)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:398-404` Context (cause 27)
  · E11
  · `foundations/decisions.md:9062-9100` WAY-232
  · `foundations/decisions.md:9102-9142` WAY-233
  · `foundations/decisions.md:8974-9023` WAY-228
  · `installation/README.md`
  · `installation/install.py:25-76` the skills the installer carries
  · `installation/install.py:118-216` the entry point, the guidance and the block
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B installation/test_install.py` exits 0; the test shown failing with the
  block and an entry point changed for a moment in `installation/install.py` (undone, `git diff --
  installation/install.py` empty); `<ruff> check --config ruff.toml --no-cache --ignore-noqa
  installation/test_install.py` reports nothing; `python -B elements/common/foundation_check.py
  --skip-test-citations` exits 0
- **Depends on:** Slice 1

### Slice 4 — A missing token count in a Codex session ends `cycle_stages.py` with exit 2, the zone of the date, and the refusal invariant of its crafted names

- **Goal:** the Claude Code half of cause 3 stands corrected at the base (the reading of a
  response's `usage` takes `required`, `required_count` and `MissingFieldError` and ends with exit
  code 2); the half that stays is Codex (item 14). In `task-cycle/cycle_stages.py`, where a record of
  tokens in a rollout of Codex (`token_usage_record`) lacks its `usage`, or `usage` lacks
  `input_tokens`, `cached_input_tokens` or `output_tokens`, the script ends with exit code 2 and a
  first line `Error:` on stderr that names the file, the line and the field, and writes no result,
  with the same helpers and the same wording as the Claude Code half; the description at the head of
  the script, which now says that the reading of a Codex rollout checks no field, says what it
  checks. The test comes first and is seen failing: in `task-cycle/test_cycle_stages.py`, one test
  for a record with no `usage` and one for each of the three counts, each the failing test that
  the change makes pass; the tests whose made-up Codex records lack a field now needed are given it.
  A key of a Codex record that the script's description and its test records do not show to be always
  present is named in the report, not made required. The read of a time takes the letter `Z` through
  `datetime.fromisoformat` with no replacement of `Z` (cause 30, the place of this file). The test
  `test_crafted_names_neither_break_a_row_nor_enter_the_column` carries `# invariant: <identifier of
  E29>` and is shown failing once with the escape of names broken for a moment, undone. The other
  fields of the reading of a Codex rollout stay as they are; the report names each one the changed
  function reads whose absence the script does not end with exit code 2, since WAY-344 binds the whole
  reading of a file whose way of reading a change reworks. The code it writes breaks no rule of
  `ruff.toml`.
- **Change:** `task-cycle/cycle_stages.py` · `task-cycle/test_cycle_stages.py`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:34-35` To do (items 8 and 9)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:40-40` To do (item 14)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:46-46` To do (item 20)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:92-97` Questions to settle (answer 5)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:177-181` Questions to settle (answer 21)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:246-252` Context (cause 3)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:417-422` Context (cause 30)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:543-543` Settlements to record (row 30)
  · E29
  · `foundations/decisions.md:2865-3010` WAY-344
  · `foundations/decisions.md:2492-2520` WAY-48
  · `foundations/decisions.md:9188-9242` WAY-235
  · `foundations/decisions.md:1746-1774` WAY-08
  · `foundations/decisions.md:9062-9100` WAY-232
  · `foundations/invariants.md:166-174` test-method-citation
  · `foundations/part_map.md:101-111` task-cycle
- **Model:** same — a change of behaviour in a trust boundary of 1130 lines, in a format whose records the script's own test makes up
- **Risk:** trust boundary — `task-cycle/cycle_stages.py`
- **Checks:** the new tests of the missing Codex fields fail on the base and pass after
  (`python -B task-cycle/test_cycle_stages.py` exits 0, with the failing run's command and exit code
  kept); the cited test shown failing with the escape of names broken for a moment, undone; `python -B
  process-audit/test_audit_count.py Cost.test_the_stage_report_cycle_stages_writes_gives_the_share`
  exits 0 (the test that runs this script as a step of a whole path); `<ruff> check --config
  ruff.toml --no-cache --ignore-noqa task-cycle/cycle_stages.py task-cycle/test_cycle_stages.py`
  reports nothing on a line the slice wrote or changed (the report of TRY004 at the base stays);
  `python -B elements/common/foundation_check.py --skip-test-citations` exits 0
- **Depends on:** Foundation entries E29 · Slice 1

### Slice 5 — The two places of the linter in `cycle_measures.py`, and the refusal invariant of its nested line

- **Goal:** in `task-cycle/cycle_measures.py` the read of a date takes the letter `Z` through
  `datetime.fromisoformat` with no replacement of `Z` (cause 30, the place of this file), and the
  loop over successive pairs uses `itertools.pairwise` (cause 33); behaviour does not change. The
  test `test_a_line_nested_too_deeply_ends_with_exit_2_naming_the_file_and_line` in
  `task-cycle/test_cycle_measures.py` carries `# invariant: <identifier of E30>` and is shown failing
  once with the refusal of a nested line broken for a moment, undone. The code it writes breaks no
  rule of `ruff.toml`.
- **Change:** `task-cycle/cycle_measures.py` · `task-cycle/test_cycle_measures.py`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:34-35` To do (items 8 and 9)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:46-46` To do (item 20)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:92-97` Questions to settle (answer 5)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:177-181` Questions to settle (answer 21)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:417-422` Context (cause 30)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:435-440` Context (cause 33)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:543-543` Settlements to record (row 30)
  · E30
  · `foundations/decisions.md:2492-2520` WAY-48
  · `foundations/decisions.md:9188-9242` WAY-235
  · `foundations/decisions.md:1746-1774` WAY-08
  · `foundations/invariants.md:166-174` test-method-citation
  · `foundations/part_map.md:101-111` task-cycle
- **Model:** cheaper
- **Risk:** trust boundary — `task-cycle/cycle_measures.py`
- **Checks:** `python -B task-cycle/test_cycle_measures.py` exits 0 before and after the change of
  the two places; the cited test shown failing with the refusal broken for a moment, undone;
  `<ruff> check --config ruff.toml --no-cache --ignore-noqa task-cycle/cycle_measures.py
  task-cycle/test_cycle_measures.py` reports nothing on a line the slice wrote or changed (the
  report of PYI034 in the test file at the base stays); `python -B elements/common/foundation_check.py
  --skip-test-citations` exits 0
- **Depends on:** Foundation entries E30 · Slice 1

### Slice 6 — The tests of `gate_times.py` take their time from a fixed value, and the refusal invariant of its registry

- **Goal:** the tests of `task-cycle/test_gate_times.py` no longer depend on the real clock or on
  constant sleeps (cause 4, the places of this file: the function `now_ms` of the test and every
  test that builds registry entries from it, and the test with `time.sleep(1)`): where a test needs
  the time of the run, it calls the script's `main` in the test's own process with the script's
  clock function replaced by a fixed value (the one double the testing rules allow, answer 17), and
  builds the registry entries from that value; no script is changed, and where that cannot be done
  the slice returns `blocked` with the reason. The test
  `test_entries_with_a_time_that_cannot_be_are_deleted_and_count_for_nothing` carries `# invariant:
  <identifier of E31>` and is shown failing once with the deletion of such an entry broken for a
  moment, undone. The code it writes breaks no rule of `ruff.toml`.
- **Change:** `task-cycle/test_gate_times.py`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:34-35` To do (items 8 and 9)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:41-41` To do (item 15)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:161-163` Questions to settle (answer 17)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:177-181` Questions to settle (answer 21)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:253-259` Context (cause 4)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:543-543` Settlements to record (row 30)
  · E31 · E11 · E12
  · `foundations/decisions.md:2492-2520` WAY-48
  · `foundations/decisions.md:9188-9242` WAY-235
  · `foundations/decisions.md:1746-1774` WAY-08
  · `foundations/decisions.md:9565-9594` WAY-243
  · `foundations/invariants.md:166-174` test-method-citation
  · `foundations/part_map.md:101-111` task-cycle
  · `task-cycle/gate_times.py:1-60` the description and the registry
  · `task-cycle/gate_times.py:110-135` the clock
  · `task-cycle/gate_times.py:280-329` the run
- **Model:** same — tests that depend on timing are reworked without a change of the script
- **Risk:** trust boundary — `task-cycle/gate_times.py` (the slice adds the citation of the invariant of its registry refusal; the script is not changed)
- **Checks:** `python -B task-cycle/test_gate_times.py` exits 0, run three times in a row; the cited
  test shown failing with the deletion broken for a moment, undone (`git diff --
  task-cycle/gate_times.py` empty); `grep -n "time.sleep\|time_ns\|time.time()" task-cycle/test_gate_times.py`
  names none that a test's expectation depends on, and the report names each one left with its
  reason; `<ruff> check --config ruff.toml --no-cache --ignore-noqa task-cycle/test_gate_times.py`
  reports nothing; `python -B elements/common/foundation_check.py --skip-test-citations` exits 0
- **Depends on:** Foundation entries E31 · Slice 1

### Slice 7 — The tests of the gate wait for events, not for constant pauses

- **Goal:** the tests of `gate/test_run_tests.py` named by cause 4 — the test of the order in which
  directories end (`pause=2.0`) and the test of the option `--slowest` (the pattern of a time the
  run itself gives) — no longer depend on a constant pause or on how fast the machine is: a module
  that must outlast another waits for the other's end by the event the helper `timed_module`
  already writes, with a limit, and an expectation about a time is stated so that a slow machine
  does not turn it red; no script is changed. The report names each pause or limit of the file it
  leaves and why.
- **Change:** `gate/test_run_tests.py`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:41-41` To do (item 15)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:161-163` Questions to settle (answer 17)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:253-259` Context (cause 4)
  · E12
  · `foundations/decisions.md:9565-9594` WAY-243
  · `foundations/decisions.md:9062-9100` WAY-232
  · `foundations/part_map.md:136-143` gate
  · `gate/run_tests.py:1-60` the description
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B gate/test_run_tests.py` exits 0, run three times in a row; `<ruff> check
  --config ruff.toml --no-cache --ignore-noqa gate/test_run_tests.py` reports nothing on a line the
  slice wrote; `python -B elements/common/foundation_check.py --skip-test-citations` exits 0
- **Depends on:** Slice 1

### Slice 8 — The tests of the audit count: fixed time, a repository built in a temporary directory, git without the user's configuration, no unused names, and the refusal invariant of a link

- **Goal:** in `process-audit/test_audit_count.py` — (a) cause 4, the places of this file: the two
  runs of the test `test_the_same_input_gives_the_same_bytes_in_both_files` are given `--today` with
  one fixed day, and the limit of wall time of the helper `run_count` and of the tests that pass it
  60 seconds no longer makes a test red on a slow machine where the limit is no oracle of the test
  (a limit that is the test's oracle, as in a test that a long line does not stall the count,
  stays and is named in the report); (b) cause 6: the test
  `test_the_way_without_a_repository_entry_is_this_checkout` runs on a repository built in a temporary
  directory that holds a copy of `process-audit/audit_count.py` (the script reads the checkout it
  lies in), not on this checkout; (c) cause 7, the place of this file: git runs with the user's
  global and system configuration shut out, `GIT_CONFIG_GLOBAL` and `GIT_CONFIG_NOSYSTEM` set as
  `project-level/test_plan_state_invariant.py` sets them, in the constant `GIT_ENV` and in the
  environment `run_count` gives the script; (d) cause 26: every unpacked name that is never read,
  in every place the linter reports in this file as RUF059 (13 at the task's commit, 14 at the
  base), is replaced by `_` or used, and the test whose name's reason the script rejects checks
  that reason; (e) the test `test_a_symbolic_link_leaving_the_record_is_not_followed` carries
  `# invariant: <identifier of E32>` and is shown failing once with the refusal broken for a moment,
  undone. The report names each place of the linter it leaves in the file (F541 at the base). The
  code it writes breaks no rule of `ruff.toml`.
- **Change:** `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:34-35` To do (items 8 and 9)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:41-44` To do (items 15 to 18)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:46-46` To do (item 20)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:92-97` Questions to settle (answer 5)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:161-168` Questions to settle (answers 17 and 18)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:177-181` Questions to settle (answer 21)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:253-259` Context (cause 4)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:267-279` Context (causes 6 and 7)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:391-397` Context (cause 26)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:543-543` Settlements to record (row 30)
  · E32 · E11 · E12
  · `foundations/decisions.md:2492-2520` WAY-48
  · `foundations/decisions.md:9188-9242` WAY-235
  · `foundations/decisions.md:1746-1774` WAY-08
  · `foundations/decisions.md:2865-3010` WAY-344
  · `foundations/decisions.md:9565-9594` WAY-243
  · `foundations/invariants.md:166-174` test-method-citation
  · `foundations/part_map.md:124-134` process-audit
  · `process-audit/audit_count.py:1-60` the description
  · `process-audit/audit_count.py:325-345` the checkout the script lies in
  · `process-audit/audit_count.py:3240-3310` the arguments
  · `project-level/test_plan_state_invariant.py:195-205` the environment of git of a test of the level git
- **Model:** same — four causes and a boundary citation in one file of 4195 lines
- **Risk:** trust boundary — `process-audit/audit_count.py` (the slice adds the citation of the invariant of its refusal; the script is not changed)
- **Checks:** `python -B process-audit/test_audit_count.py` exits 0 (the whole file; it is this
  slice's one file, not the gate); the cited test shown failing with the refusal of links broken for
  a moment, undone (`git diff -- process-audit/audit_count.py` empty); `<ruff> check --config
  ruff.toml --no-cache --ignore-noqa process-audit/test_audit_count.py` reports no RUF059 and nothing
  on a line the slice wrote; `python -B elements/common/foundation_check.py --skip-test-citations`
  exits 0
- **Depends on:** Foundation entries E32 · Slice 1

### Slice 9 — The test of the-way's foundation checks only the findings of its two invariants

- **Goal:** in `elements/common/test_foundation_check.py` the test `test_the_way_foundation_passes`
  no longer depends on which branch a clone calls the main one or on any error of the foundation
  that its two invariants (`map-reference-target` and `test-method-citation`) do not concern: it
  gives the check what does not depend on the base, or keeps from its findings only those the two
  invariants name, so that the same commit gives the same result in every clone (causes 5 and 23).
  The test is shown to still fail for its two invariants: with a reference to a part that the map
  lacks added for a moment, and with the citation of an invariant removed for a moment, each
  undone. No script is changed.
- **Change:** `elements/common/test_foundation_check.py`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:42-42` To do (item 16)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:260-266` Context (cause 5)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:373-378` Context (cause 23)
  · `foundations/invariants.md:156-174` map-reference-target and test-method-citation
  · `foundations/decisions.md:1746-1774` WAY-08
  · `foundations/part_map.md:65-78` elements-common
  · `elements/common/foundation_check.py:1-140` the description and the main branch it takes
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B elements/common/test_foundation_check.py` exits 0; the same test run in a
  clone with no `origin/HEAD`, `main` or `master` (a clone made in the agent's directory under
  `.runs/`, removed after) exits 0; the test shown failing for each of the two invariants, undone;
  `<ruff> check --config ruff.toml --no-cache --ignore-noqa elements/common/test_foundation_check.py`
  reports nothing on a line the slice wrote
- **Depends on:** Slice 1

### Slice 10 — A missing field of a skill ends `skill_entry_points.py` with exit 2

- **Goal:** `agent-instructions/skill_entry_points.py` ends with exit code 2 and a line `Error:` on
  stderr that names the file and the field, and writes nothing, where the frontmatter of a
  `SKILL.md` has no line `name:` or no line `description:`; every other error keeps exit code 1, and
  the description at the head of the script gives the exit codes (cause 17, the place
  `agent-instructions/skill_entry_points.py`, item 19). It does it as `agent-instructions/agent_type_copies.py`
  does for its definitions, so the two generators agree. The test comes first, in
  `agent-instructions/test_skill_entry_points.py`: one test for each of the two fields that gives
  the file without it and asserts exit code 2, the message and that nothing is written, seen failing
  on the base; the existing test that pins exit code 1 for a missing field is corrected. The code it
  writes breaks no rule of `ruff.toml`.
- **Change:** `agent-instructions/skill_entry_points.py` · `agent-instructions/test_skill_entry_points.py`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:45-45` To do (item 19)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:335-341` Context (cause 17)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:136-147` Questions to settle (answer 13)
  · E8
  · `foundations/decisions.md:2865-3010` WAY-344
  · `foundations/invariants.md:271-279` skill-entry-points
  · `foundations/invariants.md:56-64` derived-file-content
  · `foundations/part_map.md:155-173` agent-instructions
  · `agent-instructions/agent_type_copies.py` · `agent-instructions/test_agent_type_copies.py:166-205` the way the other generator does it
- **Model:** cheaper
- **Risk:** none
- **Checks:** the two new tests fail on the base and pass after (the failing run's command and exit
  code kept); `python -B agent-instructions/test_skill_entry_points.py` exits 0; `python -B
  agent-instructions/skill_entry_points.py` exits 0 and writes nothing (the entry points are current);
  `<ruff> check --config ruff.toml --no-cache --ignore-noqa agent-instructions/skill_entry_points.py
  agent-instructions/test_skill_entry_points.py` reports nothing on a line the slice wrote;
  `python -B elements/common/foundation_check.py --skip-test-citations` exits 0
- **Depends on:** Slice 1

### Slice 11 — The refusal invariant of `check_instructions.py` cited by its test of a link out of the repository

- **Goal:** the test `test_a_file_link_out_of_the_repository_is_neither_read_nor_listed` in
  `instruction-files/test_check_instructions.py` carries `# invariant: <identifier of E33>` (item 8)
  and is shown failing once with the refusal broken for a moment, undone (item 9). The test skips
  where links cannot be made; where the agent's machine cannot make them, the report says the test
  was skipped and the failing run is unchecked on this machine, with the reason, rather than
  claiming it.
- **Change:** `instruction-files/test_check_instructions.py`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:34-35` To do (items 8 and 9)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:177-181` Questions to settle (answer 21)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:543-543` Settlements to record (row 30)
  · E33
  · `foundations/decisions.md:2492-2520` WAY-48
  · `foundations/decisions.md:9188-9242` WAY-235
  · `foundations/decisions.md:1746-1774` WAY-08
  · `foundations/invariants.md:166-174` test-method-citation
  · `foundations/part_map.md:175-184` instruction-files
- **Model:** cheaper
- **Risk:** trust boundary — `instruction-files/check_instructions.py` (the slice adds the citation of the invariant of its refusal; the script is not changed)
- **Checks:** `python -B instruction-files/test_check_instructions.py` exits 0 and states whether
  the cited test ran or skipped; the cited test shown failing with the refusal broken for a moment,
  undone (`git diff -- instruction-files/check_instructions.py` empty), or the reason it could not
  be; `python -B elements/common/foundation_check.py --skip-test-citations` exits 0
- **Depends on:** Foundation entries E33

### Slice 12 — The tests of the rule of a generator

- **Goal:** for each file of the kind `generator` that Context lists — `agent-instructions/skill_entry_points.py`
  and `agent-instructions/agent_type_copies.py` — a test in the file of that script's tests
  (`agent-instructions/test_skill_entry_points.py`, `agent-instructions/test_agent_type_copies.py`)
  checks that without `--write` the run changes no file of the repository it runs in, including a
  run that finds what it would create, change or list as an orphan, and carries `# invariant:
  <identifier of E24>`. A test that already checks the rule in full is cited and strengthened where
  it checks only part of it; a test is written where none does. Each is shown failing once with the
  writing of a file without `--write` added for a moment, undone. The code it writes breaks no rule
  of `ruff.toml`.
- **Change:** `agent-instructions/test_skill_entry_points.py` · `agent-instructions/test_agent_type_copies.py`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:33-35` To do (items 7 to 9)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:136-147` Questions to settle (answer 13)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:532-532` Settlements to record (row 19)
  · E24 · E8
  · `foundations/decisions.md:1746-1774` WAY-08
  · `foundations/decisions.md:8560-8590` WAY-198
  · `foundations/invariants.md:166-174` test-method-citation
  · `foundations/part_map.md:155-173` agent-instructions
  · `agent-instructions/skill_entry_points.py` · `agent-instructions/agent_type_copies.py`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B agent-instructions/test_skill_entry_points.py` and `python -B
  agent-instructions/test_agent_type_copies.py` exit 0; each cited test shown failing with the
  writing added for a moment, undone (`git diff` of the two scripts empty); `<ruff> check --config
  ruff.toml --no-cache --ignore-noqa agent-instructions/test_skill_entry_points.py
  agent-instructions/test_agent_type_copies.py` reports nothing on a line the slice wrote; `python
  -B elements/common/foundation_check.py --skip-test-citations` exits 0
- **Depends on:** Slice 10 · Foundation entries E24

### Slice 13 — The tests of the rule of a repository changer

- **Goal:** for each file of the kind `repository-changer` that Context lists —
  `task-cycle/remove_merged_worktrees.py`, `elements/common/migrate_foundation.py` and
  `installation/install.py` — a test in the file of that script's tests
  (`task-cycle/test_remove_merged_worktrees.py`, `elements/common/test_migrate_foundation.py`,
  `installation/test_install.py`) checks that without `--apply`, or where the confirmation is
  declined, the run changes no file the repository tracks and no working directory, and carries `#
  invariant: <identifier of E25>`. A test that already checks the rule in full is cited and
  strengthened where it checks only part of it; a test is written where none does. Each is shown
  failing once with a change made without the act for a moment, undone. Where a script is found to
  change something without the act, the slice returns `blocked` with what it found, since the
  invariant would then be marked violated by a change a human accepts (WAY-51). The code it writes
  breaks no rule of `ruff.toml`.
- **Change:** `task-cycle/test_remove_merged_worktrees.py` · `elements/common/test_migrate_foundation.py` · `installation/test_install.py`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:33-35` To do (items 7 to 9)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:136-147` Questions to settle (answer 13)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:532-532` Settlements to record (row 19)
  · E25 · E8
  · `foundations/decisions.md:1746-1774` WAY-08
  · `foundations/decisions.md:1776-1820` WAY-51
  · `foundations/decisions.md:8560-8590` WAY-198
  · `foundations/invariants.md:166-174` test-method-citation
  · `foundations/part_map.md:65-78` elements-common
  · `foundations/part_map.md:101-111` task-cycle
  · `foundations/part_map.md:186-195` installation
  · `task-cycle/remove_merged_worktrees.py` · `elements/common/migrate_foundation.py:1-80` the description · `installation/install.py:564-693` the run
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B task-cycle/test_remove_merged_worktrees.py`, `python -B
  elements/common/test_migrate_foundation.py` and `python -B installation/test_install.py` exit 0;
  each cited test shown failing with the change made without the act for a moment, undone (`git
  diff` of the three scripts empty); `<ruff> check --config ruff.toml --no-cache --ignore-noqa` on
  the three test files reports nothing on a line the slice wrote; `python -B
  elements/common/foundation_check.py --skip-test-citations` exits 0
- **Depends on:** Slice 3 · Foundation entries E25

### Slice 14 — The test of the rule of a command runner

- **Goal:** a test in `task-cycle/test_gate_times.py` checks that the script, which wraps one
  command, ends with the exit code of that command unchanged, for a code of the command that is
  neither 0 nor 1 and for a code a signal gives (the existing `test_exit_code_of_the_command_is_passed_on`
  is cited and extended where it checks less), and carries `# invariant: <identifier of E26>`; it
  is shown failing once with the code changed for a moment, undone. `gate/run_tests.py` is a file of
  the kind that wraps no one command (it runs every directory and aggregates), so no test of it
  carries this invariant; the report states that. The code it writes breaks no rule of `ruff.toml`.
- **Change:** `task-cycle/test_gate_times.py`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:33-35` To do (items 7 to 9)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:136-147` Questions to settle (answer 13)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:532-532` Settlements to record (row 19)
  · E26 · E8
  · `foundations/decisions.md:1746-1774` WAY-08
  · `foundations/decisions.md:8560-8590` WAY-198
  · `foundations/invariants.md:166-174` test-method-citation
  · `foundations/part_map.md:101-111` task-cycle
  · `task-cycle/gate_times.py:1-60` the description
  · `task-cycle/gate_times.py:280-329` the run
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B task-cycle/test_gate_times.py` exits 0; the cited test shown failing with
  the code changed for a moment in `task-cycle/gate_times.py`, undone (`git diff --
  task-cycle/gate_times.py` empty); `<ruff> check --config ruff.toml --no-cache --ignore-noqa
  task-cycle/test_gate_times.py` reports nothing on a line the slice wrote; `python -B
  elements/common/foundation_check.py --skip-test-citations` exits 0
- **Depends on:** Slice 6 · Foundation entries E26

### Slice 15 — The test of the rule of a shared module

- **Goal:** a test in `relation-model/test_fingerprint.py` checks that importing
  `relation-model/fingerprint.py` runs nothing — in a new process of the interpreter that imports
  the module with its input closed, the import ends with exit code 0, writes nothing to either
  output and reads nothing from the input — and carries `# invariant: <identifier of E27>`; it is
  shown failing once with a statement that runs at import added to the module for a moment, undone.
  The code it writes breaks no rule of `ruff.toml`.
- **Change:** `relation-model/test_fingerprint.py`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:33-35` To do (items 7 to 9)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:136-147` Questions to settle (answer 13)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:532-532` Settlements to record (row 19)
  · E27 · E8
  · `foundations/decisions.md:1746-1774` WAY-08
  · `foundations/decisions.md:8560-8590` WAY-198
  · `foundations/invariants.md:166-174` test-method-citation
  · `foundations/part_map.md:27-34` relation-model
  · `relation-model/fingerprint.py`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B relation-model/test_fingerprint.py` exits 0; the new test shown failing with
  the statement added for a moment, undone (`git diff -- relation-model/fingerprint.py` empty);
  `<ruff> check --config ruff.toml --no-cache --ignore-noqa relation-model/test_fingerprint.py`
  reports nothing on a line the slice wrote; `python -B elements/common/foundation_check.py
  --skip-test-citations` exits 0
- **Depends on:** Foundation entries E27

### Slice 16 — The test of the linter's invariant, marked violated

- **Goal:** the new file `agent-instructions/test_linter_invariant.py` holds two tests and cites
  E22 in the second (`# invariant: <identifier of E22>`). The first, not marked, fails where the
  pinned ruff cannot be found or cannot run: it finds the environment `.runs/quality-venv` in the
  main checkout through `git rev-parse --git-common-dir` (answer 25), runs that ruff with
  `--config ruff.toml` on a clean file in a temporary directory, and makes no check of the version of
  its own (ruff itself refuses a version other than the one `required-version` names, E38). The
  second runs the same ruff with `--config ruff.toml --ignore-noqa` over every part with Python code
  — the directories `agent-instructions`, `elements`, `gate`, `installation`, `instruction-files`,
  `process-audit`, `product-guidelines`, `project-level`, `relation-model` and `task-cycle` — fails
  where ruff reports a break of a rule that blocks, and is marked as an expected failure (E22 is
  `Violated: yes`, WAY-51). Its failure stays separate from the first test's so that a missing ruff
  cannot pass as the expected failure and leave the gate green. Seen failing once (item 9): the
  second test unmarked fails with the reports of the places that remain (25 at the plan's base after
  the slices that clean 18 of the 43), and shown to pass on a clean file for a moment. Places the
  linter reports in the files of the parts that no slice of this plan cleans stay; the report lists
  them. The code it writes breaks no rule of `ruff.toml`, and the test imports no file of another
  part.
- **Change:** `agent-instructions/test_linter_invariant.py`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:31-31` To do (item 5)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:35-35` To do (item 9)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:77-97` Questions to settle (answers 2 to 5)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:197-202` Questions to settle (answer 25)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:516-523` Settlements to record (rows 3 to 10)
  · E22 · E20 · E21 · E2 · E3 · E37 · E38
  · `foundations/decisions.md:1746-1774` WAY-08
  · `foundations/decisions.md:1776-1820` WAY-51
  · `foundations/decisions.md:1862-1909` WAY-61
  · `foundations/decisions.md:2644-2668` WAY-38
  · `foundations/decisions.md:8664-8724` WAY-203
  · `foundations/decisions.md:8726-8776` WAY-204
  · `foundations/decisions.md:8778-8812` WAY-205
  · `foundations/invariants.md:126-144` script-imports and script-subprocesses
  · `foundations/invariants.md:166-174` test-method-citation
  · `foundations/invariants.md:348-356` cross-part-imports
  · `foundations/part_map.md:155-173` agent-instructions
  · ruff.toml, written by Slice 1 · `README.md:163-177` Running the tests
- **Model:** same — the environment lookup, the split between a test that must pass and the one marked as an expected failure, and the clean file are decisions of design inside the settled rules
- **Risk:** none
- **Checks:** `python -B agent-instructions/test_linter_invariant.py` exits 0 and reports one expected
  failure; the second test unmarked fails on the base of the slice with the reports named, command and
  exit code kept; the first test shown failing with the environment's path made wrong for a moment,
  undone; `<ruff> check --config ruff.toml --no-cache --ignore-noqa
  agent-instructions/test_linter_invariant.py` reports nothing; `python -B
  elements/common/foundation_check.py` exits 0
- **Depends on:** Slice 1 · Slice 3 · Slice 4 · Slice 5 · Slice 8 · Foundation entries E22 · E20 · E21

### Slice 17 — The test of the invariant of size, marked violated

- **Goal:** the new file `agent-instructions/test_size_invariant.py` holds two tests and cites E23 in
  the second (`# invariant: <identifier of E23>`). The first, not marked, checks the counting on
  made-up source text: the lines of a function with the functions nested in it, the lines of a file,
  a method counted as a function. The second reads every Python file of a script that git tracks in
  the parts with Python code (every `.py` file whose name does not begin `test_`, in `agent-instructions`,
  `elements`, `gate`, `installation`, `instruction-files`, `process-audit`, `product-guidelines`,
  `project-level`, `relation-model` and `task-cycle`) with the module `ast`, outside any run of the
  linter, and fails where a function has more than 80 lines or a file more than 1000, listing every
  function and every file over a threshold, each with its path, name or line, and its size; it has no
  exception (E7), and is marked as an expected failure (E23 is `Violated: yes`, WAY-51). Seen failing
  once (item 9): the second test unmarked fails and lists the functions and the files over, at the
  base of this slice. The code it writes breaks no rule of `ruff.toml`, and the test imports no file
  of another part.
- **Change:** `agent-instructions/test_size_invariant.py`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:32-32` To do (item 6)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:35-35` To do (item 9)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:108-129` Questions to settle (answers 8 to 11)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:527-528` Settlements to record (rows 14 and 15)
  · E23 · E7
  · `foundations/decisions.md:1746-1774` WAY-08
  · `foundations/decisions.md:1776-1820` WAY-51
  · `foundations/decisions.md:8876-8931` WAY-360
  · `foundations/decisions.md:8933-8972` WAY-361
  · `foundations/decisions.md:2597-2642` WAY-16
  · `foundations/invariants.md:126-144` script-imports and script-subprocesses
  · `foundations/invariants.md:166-174` test-method-citation
  · `foundations/invariants.md:348-356` cross-part-imports
  · `foundations/part_map.md:155-173` agent-instructions
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B agent-instructions/test_size_invariant.py` exits 0 and reports one expected
  failure; the second test unmarked fails and lists each function and each file over a threshold with
  its size, command and exit code kept; the first test shown failing with a nested function left out
  of the count for a moment, undone; `<ruff> check --config ruff.toml --no-cache --ignore-noqa
  agent-instructions/test_size_invariant.py` reports nothing; `python -B
  elements/common/foundation_check.py` exits 0
- **Depends on:** Foundation entries E23 · E7

### Slice 18 — The guidelines of the kinds `check` and `shared-module`, and the directory `guidelines/` in the part map

- **Goal:** the files `guidelines/coding-check.md` and `guidelines/coding-shared-module.md` stand in
  the form `product-guidelines/coding/template.md` gives a file of a kind (the form of
  `product-guidelines/template.md` with `## Files of this kind`), written from the settlements, E8
  and E27, never from memory: *Applies to* the parts the kind's files lie in; *When to read*
  before adding or changing a file of the kind; the table of the files of the kind with their
  statuses by the allocation of the task's Context (`task-cycle/tracked_private_paths_check.py` is
  the exemplar of `check`, with E8 in its *Decision* cell; a file whose places of `do not copy` are
  all corrected at the base or in this task is `copy`; `task-cycle/request_check.py` stays `do not
  copy`; `relation-model/fingerprint.py` is the exemplar of `shared-module`); for `shared-module`,
  the rule of E27 with that invariant and the rest of the exemplar as an example; for `check`, whose
  answer 13 gives no rule that a test checks, `## Rules` holds `none — <identifier of E8>` and the
  rest of the exemplar stands as an example (WAY-198). *Where in code* names the directories the files
  lie in. No value is copied from code or a decision. Through `update-part-map`, the part
  `agent-instructions` of `foundations/part_map.md` lists `guidelines/**` (E40), written with the
  first file this slice adds. A script of the repository added after the audit of the task (such as
  `elements/common/compare_log_entries.py` and `elements/common/decision_index.py`) takes no row, as
  the template says.
- **Change:** `guidelines/coding-check.md` · `guidelines/coding-shared-module.md` · `foundations/part_map.md`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:28-28` To do (item 2)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:130-147` Questions to settle (answers 12 and 13)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:218-224` Context (the allocation of the scripts to kinds)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:531-532` Settlements to record (rows 18 and 19)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:544-544` Settlements to record (row 31)
  · E8 · E27 · E16 · E40
  · `foundations/decisions.md:7880-7952` WAY-167
  · `foundations/decisions.md:7954-8013` WAY-168
  · `foundations/decisions.md:8015-8049` WAY-173
  · `foundations/decisions.md:8150-8211` WAY-312
  · `foundations/decisions.md:8560-8590` WAY-198
  · `foundations/decisions.md:8592-8626` WAY-199
  · `product-guidelines/template.md` · `product-guidelines/coding/template.md` · `product-guidelines/reading.md`
  · `task-cycle/tracked_private_paths_check.py` · `relation-model/fingerprint.py`
  · `elements/part-map/skill/SKILL.md` · `elements/part-map/template.md` · `elements/common/rules.md`
  · `foundations/invariants.md:86-94` tracked-file-private-paths
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py` exits 0 (every reference of the two files
  names an entry, every path pattern of the map matches a tracked file); `git ls-files guidelines`
  lists the two files; no path of the main checkout or of the user's disk, no link to a note, stands
  in either file (`python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths`)
- **Depends on:** Slice 1 · Slice 15 · Foundation entries E8 · E16 · E27

### Slice 19 — The guidelines of the kinds `measuring-report` and `generator`

- **Goal:** the files `guidelines/coding-measuring-report.md` and `guidelines/coding-generator.md`
  stand in the form of a file of a kind, written as Slice 18 gives: for `measuring-report` the
  exemplar `task-cycle/cycle_measures.py` (after its two places of the linter are cleaned) and
  `## Rules` that read `none — <identifier of E8>` with the rest of the exemplar as an example; for
  `generator` the exemplar `agent-instructions/skill_entry_points.py` (after a missing field ends it
  with exit code 2), the rule of E24 with that invariant, the rest as an example. The statuses follow
  the allocation of Context as the base holds the code: `task-cycle/cycle_stages.py` is `copy` (both
  its places of `do not copy` are corrected in this change), `task-cycle/slice_size.py` and
  `project-level/plan_state.py` stay `do not copy`, `agent-instructions/agent_type_copies.py` is `copy`
  (corrected before the base); the report checks each status against the code. No value is copied from
  code or a decision.
- **Change:** `guidelines/coding-measuring-report.md` · `guidelines/coding-generator.md`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:28-28` To do (item 2)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:130-147` Questions to settle (answers 12 and 13)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:218-224` Context (the allocation of the scripts to kinds)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:531-532` Settlements to record (rows 18 and 19)
  · E8 · E24
  · `foundations/decisions.md:7880-7952` WAY-167
  · `foundations/decisions.md:7954-8013` WAY-168
  · `foundations/decisions.md:8015-8049` WAY-173
  · `foundations/decisions.md:8150-8211` WAY-312
  · `foundations/decisions.md:8560-8590` WAY-198
  · `foundations/decisions.md:8592-8626` WAY-199
  · `foundations/decisions.md:2865-3010` WAY-344
  · `product-guidelines/template.md` · `product-guidelines/coding/template.md`
  · `task-cycle/cycle_measures.py` · `agent-instructions/skill_entry_points.py`
  · `foundations/invariants.md:86-94` tracked-file-private-paths
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py` exits 0; no path of the user's disk and
  no link to a note stands in either file (`python -B task-cycle/tracked_private_paths_check.py
  tracked-file-private-paths`); for each file the report states how it checked each status of the
  table against the code
- **Depends on:** Slice 4 · Slice 5 · Slice 10 · Slice 12 · Slice 18 · Foundation entries E8 · E24

### Slice 20 — The guidelines of the kinds `repository-changer` and `command-runner`

- **Goal:** the files `guidelines/coding-repository-changer.md` and `guidelines/coding-command-runner.md`
  stand in the form of a file of a kind, written as Slice 18 gives: for `repository-changer` the
  exemplar `task-cycle/remove_merged_worktrees.py`, the rule of E25 with that invariant, the rest as
  an example, `installation/install.py` stays `do not copy` and `elements/common/migrate_foundation.py`
  `copy`; for `command-runner` the exemplar `task-cycle/gate_times.py`, the rule of E26 with that
  invariant, `gate/run_tests.py` `copy`, the rest as an example. The report checks each status
  against the code. No value is copied from code or a decision.
- **Change:** `guidelines/coding-repository-changer.md` · `guidelines/coding-command-runner.md`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:28-28` To do (item 2)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:130-147` Questions to settle (answers 12 and 13)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:218-224` Context (the allocation of the scripts to kinds)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:531-532` Settlements to record (rows 18 and 19)
  · E8 · E25 · E26
  · `foundations/decisions.md:7880-7952` WAY-167
  · `foundations/decisions.md:7954-8013` WAY-168
  · `foundations/decisions.md:8015-8049` WAY-173
  · `foundations/decisions.md:8150-8211` WAY-312
  · `foundations/decisions.md:8560-8590` WAY-198
  · `foundations/decisions.md:8592-8626` WAY-199
  · `product-guidelines/template.md` · `product-guidelines/coding/template.md`
  · `task-cycle/remove_merged_worktrees.py` · `task-cycle/gate_times.py`
  · `foundations/invariants.md:86-94` tracked-file-private-paths
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py` exits 0; no path of the user's disk and
  no link to a note stands in either file (`python -B task-cycle/tracked_private_paths_check.py
  tracked-file-private-paths`); for each file the report states how it checked each status of the
  table against the code
- **Depends on:** Slice 13 · Slice 14 · Slice 18 · Foundation entries E8 · E25 · E26

### Slice 21 — The general coding guidelines `guidelines/coding.md`

- **Goal:** `guidelines/coding.md` stands in the form of the general file of
  `product-guidelines/coding/template.md`, written from the settlements and the entries, never from
  memory: *Applies to* every part with Python code (the ten the task names and `product-guidelines`,
  which holds a test file at the base — see the report of the plan); `## When to read` before any
  change of the code of the-way; `## Kinds of code` with its six rows (the file of each kind and
  when to read it); `### Linter` (E2, E3, E22, with the environment fact of its set), `### Formatter`
  and `### Dependency audit` reading `none — <identifier>` of E4 and E5, the six rules on failures and
  logs each reading `none — <identifier of E6>`, `### Size of a function and a file` (E7, E23), and
  the two further rules of the whole of the code — each script opens with a description of how it is
  run (`python -B …`) and what its exit codes mean and has one fixed place of start that returns the
  exit code; a field missing from a file a script reads is handled as WAY-344 gives, the rule naming
  WAY-344 and repeating none of it — each with *Invariant* `none`; `## Examples` holding the 18
  rules of ruff that stay examples, each named as the tool names it (`<ruff> rule <code>`); `##
  Where in code` naming `ruff.toml`, the two requirement files, the two tests of the standing checks
  and the directories of the kinds. No value is copied from a configuration file or a decision, and
  every reference names an entry the foundation holds (E17: WAY-328 is withdrawn, so no text names it).
- **Change:** `guidelines/coding.md`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:27-27` To do (item 1)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:59-61` Questions to settle (the tools of the standing checks)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:66-70` Questions to settle (the formatter)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:72-135` Questions to settle (answers 1 to 12)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:136-147` Questions to settle (answer 13)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:203-207` Questions to settle (answer 26)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:514-519` Settlements to record (rows 1 to 6)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:524-532` Settlements to record (rows 11 to 19)
  · E1 · E2 · E3 · E4 · E5 · E6 · E7 · E8 · E17 · E22 · E23 · E37
  · `foundations/decisions.md:2865-3010` WAY-344
  · `foundations/decisions.md:7880-7952` WAY-167
  · `foundations/decisions.md:7954-8013` WAY-168
  · `foundations/decisions.md:8015-8049` WAY-173
  · `foundations/decisions.md:8051-8092` WAY-212
  · `foundations/decisions.md:8150-8211` WAY-312
  · `foundations/decisions.md:8628-8662` WAY-202
  · `foundations/decisions.md:8664-8724` WAY-203
  · `foundations/decisions.md:8726-8776` WAY-204
  · `foundations/decisions.md:8778-8812` WAY-205
  · `foundations/decisions.md:8876-8931` WAY-360
  · `foundations/decisions.md:8933-8972` WAY-361
  · `product-guidelines/template.md` · `product-guidelines/coding/template.md` · `product-guidelines/reading.md`
  · ruff.toml and guidelines/coding-check.md, written by Slices 1 and 18 · `foundations/invariants.md:86-94` tracked-file-private-paths
- **Model:** same — a file of many rules, each tied to a decision and an invariant, written without a change of the settlements
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py` exits 0 (every decision, invariant and
  part it names is an entry; the invariants it names are cited by a test); `<ruff> rule <code>` for
  each of the 18 gives the name written in the file; `python -B task-cycle/tracked_private_paths_check.py
  tracked-file-private-paths` exits 0; `python -B instruction-files/check_instructions.py
  guidelines/coding.md` gives no finding the file's form causes
- **Depends on:** Slice 1 · Slice 16 · Slice 17 · Slice 18 · Slice 19 · Slice 20 · Foundation entries E1–E8 · E17 · E22 · E23

### Slice 22 — The testing guidelines `guidelines/testing.md`

- **Goal:** `guidelines/testing.md` stands in the form of `product-guidelines/testing/template.md`,
  written from the settlements and the entries, never from memory: *Applies to* every part the
  tests check or that holds test files; `## When to read` before writing or changing a test;
  `## Levels` with the table of the five levels (E10 in each *Decision* cell, E34–E36 named as the
  glossary terms of the three levels the glossary defines) and the table of parts with the sentence
  for each (the ten parts of answer 15; the table's row for `product-guidelines` follows the answer
  the orchestrator gives to the question of the plan's report, and a row whose answer is missing is
  left as a question, never filled); `## Rules` in the template's order, each required rule with its
  decisions and *Invariant* `none` but `### Trust boundaries`, which names the refusal invariant of
  each of the nine boundaries (E28–E33 and the three standing, `project-plan-form`,
  `project-plan-state-evidence` and `installation-paths-through-links`) and holds the table of
  authorization with its header and no row (the-way has no users or permissions); `### Where the
  expected value comes from` naming E11; `### Mutation testing` reading `none — <identifier of E15>`;
  `### AI in tests` with no decision of a tool (the-way's tests use no AI tool); `## Recipes` with one
  recipe per level, the fields in the template's order, the *Command* `python -B gate/run_tests.py
  <directory>`, the *Time limit* `none — <identifier of E12>`, the *Exemplar* of each level the test of
  answer 18 with E13; `## Not tested on purpose` naming E14; `## Examples`; `## Where in code`. No
  value is copied from code or a decision, no text names WAY-328 (E17), and every reference names an
  entry the foundation holds.
- **Change:** `guidelines/testing.md`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:29-29` To do (item 3)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:63-65` Questions to settle (preferences about tests)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:148-181` Questions to settle (answers 14 to 21)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:203-207` Questions to settle (answer 26)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:514-515` Settlements to record (rows 1 and 2)
  · `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:533-543` Settlements to record (rows 20 to 30)
  · E9 · E10 · E11 · E12 · E13 · E14 · E15 · E17 · E28 · E29 · E30 · E31 · E32 · E33 · E34 · E35 · E36
  · `foundations/decisions.md:9025-9060` WAY-231
  · `foundations/decisions.md:9188-9242` WAY-235
  · `foundations/decisions.md:9296-9349` WAY-237
  · `foundations/decisions.md:9423-9466` WAY-240
  · `foundations/decisions.md:9468-9514` WAY-241
  · `foundations/decisions.md:9516-9563` WAY-242
  · `foundations/decisions.md:9621-9662` WAY-252
  · `foundations/decisions.md:9664-9698` WAY-253
  · `foundations/decisions.md:9700-9730` WAY-254
  · `foundations/decisions.md:7880-7952` WAY-167
  · `foundations/decisions.md:7954-8013` WAY-168
  · `foundations/decisions.md:8015-8049` WAY-173
  · `foundations/decisions.md:8150-8211` WAY-312
  · `foundations/invariants.md:238-250` project-plan-form
  · `foundations/invariants.md:311-336` installation-paths-through-links and project-plan-state-evidence
  · `foundations/part_map.md:1-283` the part map of the-way
  · `product-guidelines/template.md` · `product-guidelines/testing/template.md` · `product-guidelines/reading.md`
  · `foundations/invariants.md:86-94` tracked-file-private-paths
- **Model:** same — a file of many rules and five recipes, written without a change of the settlements
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py` exits 0 (every decision, invariant and
  part it names is an entry); `python -B task-cycle/tracked_private_paths_check.py
  tracked-file-private-paths` exits 0; `python -B instruction-files/check_instructions.py
  guidelines/testing.md` gives no finding the file's form causes; each path in *Where in code* and
  *Exemplar* is a path `git ls-files` lists, and each exemplar test named exists
- **Depends on:** Slice 2 · Slice 4 · Slice 5 · Slice 6 · Slice 8 · Slice 11 · Foundation entries E9–E15 · E17 · E28–E36

### Slice 23 — The two pointers in `AGENTS.md`

- **Goal:** through `maintain-instruction-files` (`instruction-files/SKILL.md`), `AGENTS.md` of
  the-way gains two lines outside any block of the installer, each in the form of a pointer that skill
  gives: one naming `guidelines/coding.md` by its path in backticks with the condition of changing
  the-way's code, one naming `guidelines/testing.md` by its path in backticks with the condition of
  writing or changing a test; no line names a file `guidelines/coding-<kind>.md`, and no line holds
  a command (WAY-212, WAY-16). The files `guidelines/coding.md` and `guidelines/testing.md` are
  repository instruction files from then on and keep the checker quiet.
- **Change:** `AGENTS.md`
- **Read:** `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md:36-36` To do (item 10)
  · `AGENTS.md` · `instruction-files/SKILL.md`
  · `foundations/decisions.md:8051-8092` WAY-212
  · `foundations/decisions.md:2597-2642` WAY-16
  · `foundations/decisions.md:3017-3065` WAY-128
  · `foundations/decisions.md:3067-3088` WAY-129
  · `foundations/part_map.md:155-173` agent-instructions
  · `foundations/invariants.md:281-299` instruction-file-imports and root-claude-md-import
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B instruction-files/check_instructions.py AGENTS.md guidelines/coding.md
  guidelines/testing.md` reports no finding of level error; `python -B agent-instructions/test_instruction_files.py`
  exits 0; `python -B elements/common/foundation_check.py` exits 0
- **Depends on:** Slice 21 · Slice 22 · Foundation entries E17

## Coverage

| What the task requires | Slices or entries |
|---|---|
| To do 1 — `guidelines/coding.md` | Slice 21; E1–E8, E22, E23, E37 |
| To do 2 — the six `guidelines/coding-<kind>.md` | Slices 18, 19, 20; E8, E24–E27 |
| To do 3 — `guidelines/testing.md` | Slice 22; E9–E15, E28–E36 |
| To do 4 — ruff 0.17.1, `ruff.toml`, requirement files with sums, README, CI step | Slice 1; E2, E3, E37, E38, E39 |
| To do 5 — test of the linter invariant, marked violated | Slice 16; E22 |
| To do 6 — test of the invariant of size, marked violated | Slice 17; E23 |
| To do 7 — tests of the four rules of kinds | Slices 12, 13, 14, 15; E24–E27 |
| To do 8 — the six refusal tests cite their invariants | Slices 2, 4, 5, 6, 8, 11; E28–E33 |
| To do 9 — each test of items 5 to 8 seen failing once | Slices 2, 4, 5, 6, 8, 11, 12, 13, 14, 15, 16, 17 (each names its break) |
| To do 10 — two lines in `AGENTS.md` | Slice 23 |
| To do 11 — the part map | Slice 1 (E39), Slice 18 (E40) |
| To do 12 — cause 1 | Slice 2 |
| To do 13 — cause 2 | Slice 3 |
| To do 14 — cause 3, the half that stays: Codex (the Claude Code half is corrected at the base) | Slice 4 |
| To do 15 — cause 4 | Slices 6, 7, 8 |
| To do 16 — causes 5 and 23 | Slice 9 |
| To do 17 — cause 6 | Slice 8 |
| To do 18 — cause 7, the place of `test_audit_count.py` | Slice 8 |
| To do 19 — cause 17, the place of `skill_entry_points.py` | Slice 10 |
| To do 20 — causes 26, 27, 30 and 33 | Slice 8 (26), Slice 3 (27), Slices 4 and 5 (30), Slice 5 (33) |
| Cause 1 | Slice 2 |
| Cause 2 | Slice 3 |
| Cause 3 (the Codex half; the Claude Code half is corrected at the base) | Slice 4 |
| Cause 4 | Slices 6, 7, 8 |
| Cause 5 | Slice 9 |
| Cause 6 | Slice 8 |
| Cause 7 (the sliver of `process-audit/test_audit_count.py`) | Slice 8 |
| Cause 17 (the sliver of `agent-instructions/skill_entry_points.py`) | Slice 10 |
| Cause 23 | Slice 9 |
| Causes 26, 27, 30, 33 | Slice 8; Slice 3; Slices 4 and 5; Slice 5 |
| Row 1 | E1; Slice 21 |
| Row 2 | E9; Slice 22 |
| Row 3 | E2; Slices 1, 16, 21 |
| Row 4 | E3; Slice 1 |
| Row 5 | Slice 1 (README), Slice 16 (the test's lookup) |
| Row 6 | E22; Slice 16 |
| Row 7 | E37 |
| Row 8 | E38 |
| Row 9 | E20 |
| Row 10 | E21 |
| Row 11 | E4; Slice 21 |
| Row 12 | E5; Slice 21 |
| Row 13 | E6; Slice 21 |
| Row 14 | E7; Slices 17, 21 |
| Row 15 | E23; Slice 17 |
| Row 16 | Slice 21 (the rule of the description and the start of a script) |
| Row 17 | Slice 21 (the rule that points to WAY-344) |
| Row 18 | E8; Slices 18, 19, 20 |
| Row 19 | E24–E27; Slices 12, 13, 14, 15 |
| Row 20 | E10; Slice 22 |
| Rows 21, 22, 23 | E34, E35, E36; Slice 22 |
| Row 24 | Slice 22 (the table of parts) |
| Row 25 | E11; Slice 22 |
| Row 26 | E12; Slice 22 |
| Row 27 | E13; Slice 22 |
| Row 28 | E14; Slice 22 |
| Row 29 | E15; Slice 22 |
| Row 30 | E28–E33; Slices 2, 4, 5, 6, 8, 11, 22 |
| Row 31 | E16; Slice 18 |
| Row 32 | E17 |
| Row 33 | E18 |
| Row 34 | E19 |
| Human action (ruff 0.17.1 in `.runs/quality-venv` of the main checkout) | done before the cycle; Slices 1 and 16 rely on it and on the lookup of answer 25 |
| Gap, stated: the table of parts of `guidelines/testing.md` has no settled sentence for `product-guidelines` (answer 15 names ten parts; at the base an eleventh holds a test file) | the plan's report, question 1; Slice 22 leaves that row to the answer |

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| The part-map lines for the new files (E39, E40) are written by the slice that adds the first file the pattern matches (Slices 1 and 18), not in the step of the entries | writing them with the entries, as the table of the entries would otherwise have them | the check of the foundation reports a path pattern that matches no tracked file, and the step of the entries ends red |
| No slice moves code out ahead of a change to a function or a file over a size threshold (WAY-365): the guidelines of the-way hold no rule of size at the plan's base, and answer 11 says the rule binds after this task merges | a first slice that divides `cycle_stages.py` (1130 lines, `read_codex_agent` of about 140) before Slice 4 | Slice 4 adds to a function and a file that the rule of size will name; the first later task that changes them starts with a move |
| The tests of the standing checks (Slices 16 and 17) stand in `agent-instructions/`, each in a file of its own, with no change of that part's *Depends on* | `gate/` (which depends on no part); one file for both | a reviewer reads the test's reach into files of parts `agent-instructions` does not list (`relation-model`, `installation`) as a dependency; the existing tests that read every part (`elements/part-map/test_cross_part_imports.py`, `agent-instructions/test_instruction_files.py`) set the precedent |
| The test of the linter is two tests: one not marked that fails where the pinned ruff cannot be found or run, one marked as an expected failure for the rules | one test marked as an expected failure | a missing ruff passes as the expected failure and the gate stays green, against answer 24 |
| The test of size has a second test, not marked, on the counting of made-up source | the marked test alone | a counter that undercounts is hidden by the expected failure |
| The six refusal citations go into the slice that changes the same test file for another cause (Slices 2, 4, 5, 6, 8) and into Slice 11 alone | one slice for the six citations | the six test files are about 9100 lines, over the reading limit of a slice, and two slices would change one file with no dependence |
| A test that needs a time given from outside calls the script's `main` in its own process with the script's clock function replaced, and no script is changed (Slice 6); a pause is replaced by waiting for an event (Slice 7) | adding an option for the time to `gate_times.py` and `gate/run_tests.py` | a test that must run the script as a process for its exit code or its streams keeps a real clock; the report of the slice names it |
| The tests of the four rules of kinds are added to the test file of each script of the kind, where an existing test that checks the rule is cited and a missing one is written (Slices 12 to 15) | a new test file for each rule that runs every file of the kind | a test that runs files of several parts would reach across parts that do not depend on each other |
| The rule of the command runner is tested on `task-cycle/gate_times.py` alone; `gate/run_tests.py`, which wraps no one command, is listed as `copy` with no test of that rule | a test that gives `gate/run_tests.py` a child's exit code | the invariant's *Part* names a part for a file it does not check, and the first reviewer asks why |
| `## Rules` of the files of the kinds `check` and `measuring-report` reads `none — <identifier of E8>`, since answer 13 gives them no rule that a test checks (WAY-198) | rules drawn from the audit of the kinds that the task does not settle | the guidelines of those two kinds hold the exemplar as an example and no rule, so a new file of the kind has nothing but its model |
| The slice that changes the reading of the session files in `cycle_stages.py` makes only the token fields required and reports the other fields of the changed functions (Slice 4) | making every field of the two readings required at once, as the words of WAY-344 about the whole reading of a file could be read | the review of the change finds a field whose absence the script still reads as empty and grades it against WAY-344 |
| The places of the linter that appeared after the task's commit (F541 in `test_audit_count.py`, TRY004 in `cycle_stages.py`, PYI034 in `test_cycle_measures.py`, PIE810 in `product-guidelines/test_skill_references.py`) stay, with the places of the 37 that the task does not take, under the invariant marked violated; the one more RUF059 in `test_audit_count.py` is cleaned with the 13 of cause 26 | cleaning those four with the files the slices change anyway | the marked invariant stands with 25 reports at the base (43, of which the slices of this plan clean 18), and a reviewer who finds F541 in a file Slice 8 changed asks why it stayed |
| The linter and the size read the eleven parts with Python code, `product-guidelines` among them | the ten parts of answer 2, which leave a part with a Python file unread by the linter and the size test | a human who meant ten sees an eleventh part in `Applies to` and the invariants; the plan's report puts the question first |

## Orchestrator's additions to the plan's review (step 8; the go-ahead is provisional, never the human's)

Added to every slice's *Read*, by identifier, as the orchestrator's reading of the invariants that
the files of the slice reach (WAY-62), whole from `foundations/invariants.md`:

- every slice that adds or edits a Python file: `script-language`, `script-imports`,
  `script-subprocesses` (changed by E21), `cross-part-imports`, `test-method-citation`;
- Slices 1, 16, 17, 18, 19, 20, 21, 22 and 23, which add files at the root or under the new
  directory `guidelines/`: `repository-file-location`, `ci-checking-commands`,
  `tracked-file-private-paths`, `guidelines-file-place`, `python-version-declared` (Slice 1),
  `map-reference-target`, `derived-file-content`;
- Slice 23: `instruction-file-imports`, `root-claude-md-import`.

Decisions added to the *Read* of Slices 16 and 17: WAY-202, WAY-203, WAY-204, WAY-205 (Slice 16) and
WAY-360, WAY-361 (Slice 17), whole with *Rationale*; of Slices 21 and 22, the decisions of the
section whose `### Coding guidelines` or `### Rules of a product's tests` rules the file carries,
whole.

Answers to the planner's questions (recorded in the cycle record as autonomous choices Q2 to Q6):
the plan stands on the proposed answer of each. Where the human meant ten parts and not eleven, the
request says so and gives the removal the planner's question 1 describes.
