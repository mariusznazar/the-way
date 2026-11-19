# Plan — the way: porządek kodu Pythona — automatyczne formatowanie, błędy lintera, podział za dużych funkcji i plików, ostre testy obu reguł i pełne sprawdzenie fundamentu w bramce

- Task: .runs/task-cycles/code-order-formatter-linter-size/task.md
- Spec: none
- Base: d69fb20b

## Foundation entries

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| F1 — WAY-382, changed in place: the-way's code gets Ruff's formatter, in the version WAY-381 pins, with line width 100 and the other settings at their defaults, brought in by one reformatting of the whole code (WAY-205); the formatter and its invariant cover `.py` files only, never Python examples in Markdown files; a comment `fmt: off`, `fmt: on` or `fmt: skip` in a file the rule covers is forbidden and the test of the formatter fails on it; its *Verification* names F4 | decision (changed) | rows 1, 4, 5; To do 1–2 | Slices 1, 2, 3 |
| F2 — WAY-385, changed in place: a function of a script has at most 110 lines and a file of a script at most 1200, counted on the code after formatting, the same sharpness as 80/1000 on the code before the formatter | decision (changed) | row 2; To do 4 | Slices 11, 12, 13, 15, 16, 19 |
| F3 — new invariant: `elements/common/foundation_check.py` run on the-way's own repository reports no error; *Method* `test`; check: the full test of the-way's foundation in `elements/common/test_foundation_check.py`, written by Slice 4 | invariant (new) | row 3; To do 6 | Slice 4 |
| F4 — new invariant of the formatter: every `.py` file of the parts WAY-379 names stands as the formatter of the Ruff WAY-381 pins, run with `ruff.toml`, leaves it, and holds no comment `fmt: off`, `fmt: on` or `fmt: skip`; *Method* `test`; *Part* the parts of WAY-379's *Scope* and `repository` (the configuration stands there), as the template's rule *Formatter* and its paragraph on *Part* give; *Violated* `no` (WAY-205); check: the test of the formatter in `agent-instructions/test_linter_invariant.py`, written by Slice 3 | invariant (new) | To do 2; rows 1, 4, 5 | Slices 1, 2, 3 |
| F5 — WAY-379, corrected: its *Verification*, which gives as compliant "the rule of the formatter reads `none —` with the decision that departs from it", follows F1 | decision (corrected) | Decisions in play (WAY-379); To do 2 | Slice 3 |
| F6 — WAY-145, reworded: "entry" in the plan's log of changes, in its sentence and in its *Verification*, takes a word that fits there; meaning unchanged | decision (reworded) | To do 8 | Slice 10 |
| F7 — WAY-350, reworded: "entry" of the registry of running gates takes the word Slice 10 uses for it; meaning unchanged | decision (reworded) | To do 8 | Slice 10 |
| F8 — `gate-times-refuses-impossible-entry`, reworded: its sentence speaks of the registry's files without "entry"; the identifier stays (`elements/common/rules.md`, Identifiers) | invariant (reworded) | To do 8 | Slice 10 |
| F9 — WAY-339 and the invariant `audit-series-script-paths`, corrected: where they name the script that measures the cost as `task-cycle/cycle_stages.py`, they name it as `task-cycle/cycle_stages.py` with the module `task-cycle/stage_transcripts.py` that Slice 13 moves out of it, so that a change of either starts a series of the cost; meaning unchanged; marked `the cycle's` | decision and invariant (corrected) | the cycle's: follows from dividing `task-cycle/cycle_stages.py` (To do 4), with no other way open (see *Choices*) | Slices 13, 17 |

The agent of these entries also brings the line `decision: WAY-385 "…"` of
`agent-instructions/test_size_invariant.py` (line 58 at the base) to F2's new wording in the same
commit, since the check of the foundation reports a quotation that stands in no binding sentence
(WAY-12), and names that test for the request (WAY-03). It keeps the opening words of each sentence
of WAY-339 that a line `decision:` quotes (in `process-audit/test_audit_count.py` and
`task-cycle/test_cycle_stages.py`), such as "A new series of the cost of cycles, the two numbers of
WAY-337". It leaves the marks *Violated* of `ruff-blocking-rules` and `function-and-file-size` as
they stand: Slices 8 and 19 clear them in the slice in which their tests start to pass (WAY-51).
Its own check of the foundation runs with `--skip-test-citations`, since the tests of F3 and F4 come
in Slices 4 and 3 (WAY-61, WAY-321); until Slice 4 no slice runs `elements/common`'s tests.

## Slices

### Slice 1 — formatter configuration

- **Goal:** `ruff.toml` configures Ruff's formatter for the-way's code as F1 gives: line width 100,
  every other setting of the formatter at Ruff's default, and `ruff format` kept off Markdown files,
  so that a run from the root reformats no `.md` file; the comment that opens the file names the
  formatter and WAY-382 beside the linter. No Python file is reformatted in this slice, and the
  linter's reports stay the 24 of the base. Until Slice 4 the foundation holds two invariants that
  read `test` with no citing test yet (F3, F4): run no test of `elements/common` (WAY-321).
- **Change:** `ruff.toml`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:29-30` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:56-61` Questions to settle ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:79-83` Questions to settle ·
  `foundations/decisions.md:10653-10684` WAY-381 · `foundations/decisions.md:10611-10651` WAY-380 ·
  F1 · F4 · `foundations/part_map.md:147-158` repository · `guidelines/coding.md`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `<ruff>` is the Ruff of `.runs/quality-venv` of the main checkout, which
  `ruff_program()` of `agent-instructions/test_linter_invariant.py` finds.
  `<ruff> format --check --config ruff.toml --no-cache .` from the root exits 1 naming only `.py`
  files (78 at the base) and no `.md` file;
  `<ruff> check --config ruff.toml --no-cache --ignore-noqa --output-format concise agent-instructions elements gate installation instruction-files process-audit product-guidelines project-level relation-model task-cycle`
  reports the same 24 faults, by file and rule, as at the slice's base;
  `python -B gate/run_tests.py agent-instructions` passes.
- **Depends on:** F1

### Slice 2 — the one reformatting

- **Goal:** one commit holds the output of `<ruff> format --config ruff.toml --no-cache`, run over
  the `.py` files git tracks in the parts WAY-379 names (`git ls-files` of `*.py`), and no other
  change; its subject says that it is the reformatting by `ruff format` and nothing else, so that
  Slice 3 and the orchestrator find its hash. The slice commits nothing else. No file is edited by
  hand, and no later slice changes this commit or makes a commit that mixes this reformatting with
  another change. Behaviour does not change: every changed file parses to the same syntax tree as
  before. Until Slice 4, run no test of `elements/common` (WAY-321: F3 and F4 have no citing test
  yet).
- **Change:** `agent-instructions/*.py` · `elements/**/*.py` · `gate/*.py` · `installation/*.py` ·
  `instruction-files/*.py` · `process-audit/*.py` · `product-guidelines/*.py` ·
  `project-level/*.py` · `relation-model/*.py` · `task-cycle/*.py`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:29-29` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:69-73` Questions to settle ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:93-93` Context ·
  `foundations/decisions.md:9602-9636` WAY-205 · F1 · F4 · `ruff.toml`
- **Model:** cheaper
- **Risk:** trust boundary — the layout of every trust-boundary file: `task-cycle/cycle_stages.py`,
  `task-cycle/cycle_measures.py`, `task-cycle/gate_times.py`, `process-audit/audit_count.py`,
  `process-audit/record_items.py`, `installation/install.py`,
  `instruction-files/check_instructions.py`, `project-level/readiness_check.py`,
  `project-level/plan_check.py`, `project-level/plan_state.py`
- **Checks:** `<ruff>` as in Slice 1. `<ruff> format --check --config ruff.toml --no-cache` over the
  `.py` files git tracks exits 0; `git show --stat --format= HEAD` lists only `.py` files; a script
  in the agent's working-copy directory finds that every file the commit changes parses with `ast`
  to the same tree as at the slice's base; `<ruff> check` as in Slice 1 reports the same 24 faults;
  `python -B gate/run_tests.py installation`, `… instruction-files`, `… process-audit`,
  `… project-level` and `… task-cycle` pass.
- **Depends on:** Slice 1

### Slice 3 — the formatter's test, rule and documents

- **Goal:** `agent-instructions/test_linter_invariant.py` holds the test of F4, in a class of its
  own beside the linter's tests and cited by a line `invariant: <F4's identifier>`: it runs the
  pinned Ruff's `format --check` with `ruff.toml` and no cache over the `.py` files git tracks in
  the parts of `PARTS`, passed as files so that no Markdown file enters, fails where Ruff reports a
  file or cannot run, and fails where such a file holds a comment `fmt: off`, `fmt: on` or
  `fmt: skip`, found among the file's comments (as `tokenize` gives them), so that the same words in
  a string, the test's own included, count for nothing; the module's description covers the
  formatter. The test is seen failing once each way (WAY-08): a file put out of the formatter's
  layout for a moment, and a comment `# fmt: skip` added for a moment. `### Formatter` of
  `guidelines/coding.md` stops reading `none — WAY-382` and carries *Decision* WAY-382 · WAY-381,
  *Invariant* F4, *Good*, *Bad* and its paragraph, as the template's rule *Formatter* and its
  section "The tools of the standing checks" give — no command of a tool beside the gate. In
  `README.md`, the section "Installing the linter" says that the same Ruff also formats the code and
  that a test checks it, tells how to format a file with the installed Ruff, and names
  `.git-blame-ignore-revs`. The Python example of `installation/README.md` (the block of
  `TrackedFilesTest`) stands laid out as the formatter lays it out at width 100, once, its text
  otherwise unchanged. `.git-blame-ignore-revs` at the root holds the full hash of Slice 2's commit,
  taken from `git log` (the commit whose subject says it is the reformatting and which changes only
  `.py` files), with a comment line saying what the file lists; `foundations/part_map.md` gives it to
  the part `repository` (`/.git-blame-ignore-revs` in its *Files*). From this slice on, every slice
  that changes a `.py` file formats the files it changes with `<ruff> format --config ruff.toml`
  before it commits: that is the layout of its own change, never a second reformatting.
- **Change:** `agent-instructions/test_linter_invariant.py` · `guidelines/coding.md` · `README.md` ·
  `installation/README.md` · `.git-blame-ignore-revs` · `foundations/part_map.md`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:29-30` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:51-61` Questions to settle ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:69-73` Questions to settle ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:79-88` Questions to settle ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:131-141` Settlements to record ·
  F1 · F4 · F5 · `foundations/decisions.md:9602-9636` WAY-205 ·
  `foundations/decisions.md:10653-10684` WAY-381 · `foundations/decisions.md:2670-2723` WAY-16 ·
  `foundations/decisions.md:1805-1833` WAY-08 · `foundations/decisions.md:1759-1803` WAY-03 ·
  `foundations/invariants.md:428-436` ruff-blocking-rules ·
  `foundations/invariants.md:166-174` test-method-citation ·
  `foundations/invariants.md:26-34` repository-file-location ·
  `foundations/part_map.md:147-181` repository, agent-instructions · `foundations/glossary.md:181-185` standing check ·
  `product-guidelines/coding/template.md:60-68` Required form ·
  `product-guidelines/coding/template.md:159-162` What each section carries ·
  `product-guidelines/coding/template.md:319-343` The tools of the standing checks ·
  `guidelines/testing.md` · `ruff.toml`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `<ruff>` as in Slice 1. `python -B gate/run_tests.py agent-instructions` passes, the new
  test among its passes, and fails once for each of the two breaks above (the report gives both
  failing runs); `<ruff> format --check --config ruff.toml` and
  `<ruff> check --config ruff.toml --ignore-noqa` on the changed `.py` file exit 0;
  `git log -1 --format=%H <the hash in .git-blame-ignore-revs>` names Slice 2's commit;
  `python -B elements/common/foundation_check.py --skip-test-citations` exits 0 (F3's test comes in
  Slice 4).
- **Depends on:** Slice 2 · F1 · F4 · F5

### Slice 4 — the full check of the foundation in the gate

- **Goal:** under the comment "the-way's own foundation" of
  `elements/common/test_foundation_check.py`, a new test runs `elements/common/foundation_check.py`
  on the-way's repository as it stands, with no switch and with the base the script finds in git as
  it does today, and passes only where the script ends with exit code 0; it cites F3 by a line
  `invariant:`. The existing narrow test stays, cited by `map-reference-target` and
  `test-method-citation` as now. The new test is seen failing once (WAY-08) with a reference to a
  decision the log does not hold, written into a tracked file for a moment. `foundation_check.py`
  does not change. The paragraph of `README.md` that opens "Two invariants of the foundation of
  the-way" says that the whole check runs in the gate under F3, beside the two invariants of the
  narrow test.
- **Change:** `elements/common/test_foundation_check.py` · `README.md`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:34-34` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:38-41` Acceptance criteria ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:74-78` Questions to settle ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:99-99` Context ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:105-105` Questions carried to cycle ·
  F3 · `foundations/decisions.md:1805-1833` WAY-08 · `foundations/decisions.md:1759-1803` WAY-03 ·
  `foundations/decisions.md:1935-1982` WAY-61 · `foundations/decisions.md:2035-2070` WAY-321 ·
  `foundations/invariants.md:156-174` map-reference-target, test-method-citation ·
  `foundations/part_map.md:65-79` elements-common ·
  `foundations/part_map.md:239-243` foundation-check-command ·
  `foundations/glossary.md:217-221` repository test · `elements/common/rules.md:80-89` {fork-point} ·
  `elements/common/foundation_check.py:1-125` · `guidelines/testing.md` · `guidelines/coding.md`
- **Model:** same — orchestrator's change to the planner's `cheaper`: the slice reads about 64 000 tokens and its checks need clones of the repository with other names of the main branch, a judgment of how a base is found in git
- **Risk:** none
- **Checks:** `python -B gate/run_tests.py elements/common` passes, and fails once with the reference
  to a missing decision in place; the same command passes in a local clone of the task branch, made
  under the agent's working-copy directory, whose only main branch is a local `main` and which has
  no `refs/remotes/origin/HEAD`, and in a shallow clone (`git clone --depth 1`), each removed
  afterwards; `python -B elements/common/foundation_check.py` exits 0; `<ruff>` as in Slice 1:
  `<ruff> format --check --config ruff.toml` and `<ruff> check --config ruff.toml --ignore-noqa` on
  the test file exit 0.
- **Depends on:** Slice 3 · F3

### Slice 5 — linter faults at four trust boundaries

- **Goal:** the blocking reports of the linter in four trust-boundary files are fixed in those
  files, with no rule turned off, no `noqa` and no change of behaviour: `installation/install.py`
  (PERF102, UP022), `instruction-files/check_instructions.py` (FURB188),
  `process-audit/audit_count.py` (UP037, three) and `task-cycle/cycle_stages.py` (TRY004). For
  TRY004, `required_time` keeps what it does: a timestamp that is not a text still ends the run
  with exit code 2 and the message that the field timestamp is not a time (WAY-344), never with a
  `TypeError` that escapes, and the rule stays on (WAY-380) — the type is refused outside the `try`
  that turns `ValueError` into a missing field, or in another way that keeps the exit code and the
  message. The changed files are formatted as Slice 3 gives.
- **Change:** `installation/install.py` · `instruction-files/check_instructions.py` ·
  `process-audit/audit_count.py` · `task-cycle/cycle_stages.py`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:31-31` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:98-98` Context ·
  `foundations/decisions.md:10611-10651` WAY-380 · `foundations/decisions.md:2923-3091` WAY-344 ·
  `foundations/decisions.md:2565-2593` WAY-48 · `foundations/invariants.md:428-436` ruff-blocking-rules ·
  `foundations/invariants.md:311-319` installation-paths-through-links ·
  `foundations/invariants.md:538-546` check-instructions-refuses-outside-links ·
  `foundations/invariants.md:528-536` audit-count-refuses-record-links ·
  `foundations/invariants.md:498-506` cycle-stages-refuses-crafted-names ·
  `foundations/part_map.md:102-136` task-cycle, foundation-review, process-audit ·
  `foundations/part_map.md:183-203` instruction-files, installation · `guidelines/coding.md` ·
  `guidelines/coding-check.md` · `guidelines/coding-measuring-report.md` ·
  `guidelines/coding-repository-changer.md`
- **Model:** same — fixes at four trust boundaries in four parts, one of which (TRY004) changes
  behaviour when made the usual way
- **Risk:** trust boundary — `installation/install.py`, `instruction-files/check_instructions.py`,
  `process-audit/audit_count.py`, `task-cycle/cycle_stages.py`
- **Checks:** `<ruff>` as in Slice 1.
  `<ruff> check --config ruff.toml --no-cache --ignore-noqa` and
  `<ruff> format --check --config ruff.toml` on the four files exit 0;
  `python -B gate/run_tests.py installation`, `… instruction-files`, `… process-audit` and
  `… task-cycle` pass; once, before and after the fix, `task-cycle/cycle_stages.py` given a
  transcript, prepared in the agent's working-copy directory, whose line holds a timestamp that is a
  number, ends with exit code 2 and the same message.
- **Depends on:** Slice 3

### Slice 6 — linter faults in nine test files

- **Goal:** the blocking reports of the linter in these test files are fixed in them, with no rule
  turned off, no `noqa` and no test weakened (WAY-233): UP022 in the six tests of `installation/`
  named below, FURB188 in `agent-instructions/test_instruction_files.py`, PIE810 in
  `gate/test_skills_reach_the_way_sessions.py` and in `product-guidelines/test_skill_references.py`.
  The changed files are formatted as Slice 3 gives.
- **Change:** `installation/test_agent_types_installation.py` ·
  `installation/test_coding_guidelines_installation.py` · `installation/test_installed_guidance.py` ·
  `installation/test_lead_installation.py` · `installation/test_styleguide_installation.py` ·
  `installation/test_testing_guidelines_installation.py` ·
  `agent-instructions/test_instruction_files.py` · `gate/test_skills_reach_the_way_sessions.py` ·
  `product-guidelines/test_skill_references.py`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:31-31` To do ·
  `foundations/decisions.md:10611-10651` WAY-380 · `foundations/decisions.md:9933-9975` WAY-233 ·
  `foundations/invariants.md:428-436` ruff-blocking-rules · `guidelines/testing.md` ·
  `guidelines/coding.md`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `<ruff>` as in Slice 1. `<ruff> check --config ruff.toml --no-cache --ignore-noqa` and
  `<ruff> format --check --config ruff.toml` on the nine files exit 0;
  `python -B gate/run_tests.py installation`, `… agent-instructions`, `… gate` and
  `… product-guidelines` pass.
- **Depends on:** Slice 3

### Slice 7 — linter faults in the check and migration of the foundation and three tests

- **Goal:** the blocking reports of the linter are fixed in the files that hold them, with no rule
  turned off, no `noqa`, no change of behaviour and no test weakened (WAY-233):
  `elements/common/foundation_check.py` (PERF102, two), `elements/common/migrate_foundation.py`
  (RUF059, two), `elements/common/test_migrate_foundation.py` (RUF059),
  `task-cycle/test_cycle_measures.py` (PYI034) and `task-cycle/test_remarks_check.py` (PLR1704).
  The changed files are formatted as Slice 3 gives.
- **Change:** `elements/common/foundation_check.py` · `elements/common/migrate_foundation.py` ·
  `elements/common/test_migrate_foundation.py` · `task-cycle/test_cycle_measures.py` ·
  `task-cycle/test_remarks_check.py`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:31-31` To do ·
  `foundations/decisions.md:10611-10651` WAY-380 · `foundations/decisions.md:9933-9975` WAY-233 ·
  `foundations/invariants.md:428-436` ruff-blocking-rules · `guidelines/coding.md` ·
  `guidelines/coding-check.md` · `guidelines/coding-repository-changer.md` · `guidelines/testing.md`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `<ruff>` as in Slice 1. `<ruff> check --config ruff.toml --no-cache --ignore-noqa` and
  `<ruff> format --check --config ruff.toml` on the five files exit 0;
  `python -B gate/run_tests.py elements/common` and `… task-cycle` pass;
  `python -B elements/common/foundation_check.py` exits 0.
- **Depends on:** Slice 4

### Slice 8 — the last linter fault and the linter's mark cleared

- **Goal:** the F541 report of `process-audit/test_audit_count.py` is fixed in that file with no
  test weakened, so that no file of the parts breaks a blocking rule; in the same commit the test
  `test_no_file_of_a_part_breaks_a_blocking_rule` of `agent-instructions/test_linter_invariant.py`
  loses its marking as an expected failure, the module's description loses its sentences about the
  invariant being violated and the expected failure, and `ruff-blocking-rules` in
  `foundations/invariants.md` reads `Violated: no` (WAY-51). The request names the cleared mark and
  the changed invariant test (WAY-51, WAY-03). The changed `.py` files are formatted as Slice 3
  gives.
- **Change:** `process-audit/test_audit_count.py` · `agent-instructions/test_linter_invariant.py` ·
  `foundations/invariants.md`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:31-33` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:38-41` Acceptance criteria ·
  `foundations/decisions.md:1835-1879` WAY-51 · `foundations/decisions.md:9602-9636` WAY-205 ·
  `foundations/decisions.md:10611-10651` WAY-380 · `foundations/decisions.md:1759-1803` WAY-03 ·
  `foundations/decisions.md:9933-9975` WAY-233 · `guidelines/testing.md` · `guidelines/coding.md`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `<ruff>` as in Slice 1.
  `<ruff> check --config ruff.toml --no-cache --ignore-noqa agent-instructions elements gate installation instruction-files process-audit product-guidelines project-level relation-model task-cycle`
  exits 0; `python -B gate/run_tests.py agent-instructions` passes with the linter's invariant test
  passing and no expected failure among the linter's tests; `python -B gate/run_tests.py process-audit`
  passes; `python -B elements/common/foundation_check.py` exits 0.
- **Depends on:** Slice 5 · Slice 6 · Slice 7

### Slice 9 — the worktree test no longer depends on git's background maintenance

- **Goal:** `ApplyTest.test_a_dry_run_removes_nothing_and_apply_removes_only_what_is_marked` of
  `task-cycle/test_remove_merged_worktrees.py` gives the same verdict on the same code every time:
  every git process of the test's repositories, the bare `origin.git` included and the git run by
  the script under test where it inherits the test's environment, runs with git's automatic
  maintenance and automatic collection of garbage off — through the test's `ENVIRONMENT`, by the
  settings git reads from the environment — so that no `maintenance.lock` appears or vanishes while
  the test takes its snapshot. The snapshot `state` and every assertion stay as they are (WAY-233);
  the test names its cause in a comment: the failure of the first CI run of the pull request #144
  on Linux, `FileNotFoundError` on `maintenance.lock`. The changed file is formatted as Slice 3
  gives.
- **Change:** `task-cycle/test_remove_merged_worktrees.py`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:35-35` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:95-95` Context ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:107-107` Questions carried to cycle ·
  `foundations/invariants.md:458-466` repository-changer-acts-only-when-told ·
  `foundations/decisions.md:9933-9975` WAY-233 · `foundations/glossary.md:211-215` git test ·
  `guidelines/testing.md` · `guidelines/coding.md`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `<ruff>` as in Slice 1. `python -B gate/run_tests.py task-cycle` passes; once, a git
  command run with the test's `ENVIRONMENT` reports the maintenance and the collection of garbage as
  off (`git config --get` of each setting); `<ruff> format --check --config ruff.toml` and
  `<ruff> check --config ruff.toml --ignore-noqa` on the file exit 0.
- **Depends on:** Slice 3

### Slice 10 — "entry" kept for an entry of the foundation

- **Goal:** where the files below use "entry" for something other than an entry of the foundation,
  it gives way to a word that fits the place, and nothing else changes: the registry of running
  gates in `task-cycle/gate_times.py` (its description, comments, messages and names) and in
  `task-cycle/test_gate_times.py` (the names and comments of the tests of
  `gate-times-refuses-impossible-entry`, whose identifier stays), in the word F7 and F8 use; "their
  change-log entries" in `project-level/lead/skill/SKILL.md`, in the word F6 uses; the phrase
  "file/entry/section" in `project-level/lead/conversation_template.md` and
  `project-level/lead/answering.md`; and the names of about 24 tests and the comment "a doubled
  item, an entry in neither form, a findings file named twice" in
  `process-audit/test_record_items.py`, where "entry" is an item of a list under the record's items,
  a sub-item since the pull request #148. The uses Context of the task keeps stay: the output of
  `git worktree list`, git's trees, session transcripts, the entries of the decision log in the
  scripts that compare it, "entry point". No word gets a glossary entry (WAY-95). The behaviour of
  `gate_times.py` — its exit codes, the files of the registry and what it deletes — does not change.
  The description of the skill does not change, so no skill entry point is written. The changed
  `.py` files are formatted as Slice 3 gives.
- **Change:** `task-cycle/gate_times.py` · `task-cycle/test_gate_times.py` ·
  `project-level/lead/skill/SKILL.md` · `project-level/lead/conversation_template.md` ·
  `project-level/lead/answering.md` · `process-audit/test_record_items.py`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:36-36` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:96-96` Context · F6 · F7 · F8 ·
  `foundations/invariants.md:518-526` gate-times-refuses-impossible-entry ·
  `foundations/decisions.md:2326-2365` WAY-95 · `foundations/decisions.md:1759-1803` WAY-03 ·
  `foundations/decisions.md:2565-2593` WAY-48 · `foundations/glossary.md:49-53` entry ·
  `foundations/part_map.md:81-112` project-level, task-cycle · `foundations/part_map.md:125-136`
  process-audit · `guidelines/coding.md` · `guidelines/coding-command-runner.md` ·
  `guidelines/testing.md`
- **Model:** cheaper
- **Risk:** trust boundary — `task-cycle/gate_times.py`
- **Checks:** `<ruff>` as in Slice 1. `python -B gate/run_tests.py task-cycle`, `… process-audit` and
  `… project-level` pass; a search for `entr` in the six files finds none of the uses this slice
  replaces; `<ruff> format --check --config ruff.toml` and `<ruff> check --config ruff.toml --ignore-noqa`
  on the changed `.py` files exit 0; `python -B elements/common/foundation_check.py` exits 0.
- **Depends on:** Slice 3 · F6 · F7 · F8

### Slice 11 — four over-long functions at three parts' trust boundaries divided

- **Goal:** each of these functions stands at most 110 lines (F2), counted as the size test counts,
  by moving parts of it out into functions of the same file, each part with a name of its own
  (`guidelines/coding.md`, *Good* of the rule of size), with no change of behaviour, exit codes or
  messages: `run` of `installation/install.py` (149 lines after the reformatting),
  `check_file` of `instruction-files/check_instructions.py` (137), `check_header` of
  `project-level/plan_check.py` (123), and `provenance` (130) and `task_report` (140) of
  `project-level/plan_state.py`. The changed files are formatted as Slice 3 gives.
- **Change:** `installation/install.py` · `instruction-files/check_instructions.py` ·
  `project-level/plan_check.py` · `project-level/plan_state.py`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:32-32` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:62-68` Questions to settle · F2 ·
  `foundations/decisions.md:6615-6651` WAY-365 · `foundations/decisions.md:2565-2593` WAY-48 ·
  `foundations/invariants.md:438-446` function-and-file-size ·
  `foundations/invariants.md:311-319` installation-paths-through-links ·
  `foundations/invariants.md:538-546` check-instructions-refuses-outside-links ·
  `foundations/invariants.md:238-250` project-plan-form ·
  `foundations/invariants.md:321-336` project-plan-state-evidence ·
  `foundations/part_map.md:81-100` project-level · `foundations/part_map.md:183-203`
  instruction-files, installation · `guidelines/coding.md` · `guidelines/coding-check.md` ·
  `guidelines/coding-measuring-report.md` · `guidelines/coding-repository-changer.md` ·
  `agent-instructions/test_size_invariant.py`
- **Model:** same — four trust boundaries in three parts, each divided where its parts have a name
  of their own
- **Risk:** trust boundary — `installation/install.py`, `instruction-files/check_instructions.py`,
  `project-level/plan_check.py`, `project-level/plan_state.py`
- **Checks:** `<ruff>` as in Slice 1. The counting of `function_sizes` of
  `agent-instructions/test_size_invariant.py`, run on the four files, finds no function over 110
  lines; `python -B gate/run_tests.py installation`, `… instruction-files` and `… project-level`
  pass; `<ruff> format --check --config ruff.toml` and `<ruff> check --config ruff.toml --ignore-noqa`
  on the four files exit 0.
- **Depends on:** Slice 5 · F2

### Slice 12 — the over-long check of a request's description divided

- **Goal:** `check` of `task-cycle/request_check.py` (195 lines after the reformatting) stands at
  most 110 lines (F2), counted as the size test counts, by moving parts of it out into functions of
  the same file, each with a name of its own, with no change of behaviour, exit codes or messages.
  The changed file is formatted as Slice 3 gives.
- **Change:** `task-cycle/request_check.py`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:32-32` To do · F2 ·
  `foundations/decisions.md:6615-6651` WAY-365 ·
  `foundations/invariants.md:438-446` function-and-file-size · `guidelines/coding.md` ·
  `guidelines/coding-check.md` · `agent-instructions/test_size_invariant.py`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `<ruff>` as in Slice 1. The counting of `function_sizes` of
  `agent-instructions/test_size_invariant.py`, run on the file, finds no function over 110 lines;
  `python -B gate/run_tests.py task-cycle` passes; `<ruff> format --check --config ruff.toml` and
  `<ruff> check --config ruff.toml --ignore-noqa` on the file exit 0.
- **Depends on:** Slice 3 · F2

### Slice 13 — the reading of the transcripts moved out of the report of the stages

- **Goal:** the reading of the transcripts of Codex and Claude Code sessions in
  `task-cycle/cycle_stages.py` — from `codex_meta` to `read_session` at the base, with the classes
  they fill and the constants only they use — moves into a new module
  `task-cycle/stage_transcripts.py`, so that `cycle_stages.py` stands at most 1200 lines; on the way
  `read_codex_agent` (131 lines) and `read_claude_agent` (114) are divided to at most 110 lines each
  (F2), each part with a name of its own. Behaviour, exit codes, messages and the bytes of the
  report do not change. The module holds what other scripts import, and importing it runs nothing
  (the rule of the kind `shared-module`); its description says, as that of
  `process-audit/stage_pricing.py` does, what it holds, that it was moved out of `cycle_stages.py`
  and that it is imported, never run; it never imports `cycle_stages.py`. The description of
  `cycle_stages.py`, to which `cycle-stages-refuses-crafted-names` points, stays whole there.
  `task-cycle/test_cycle_stages.py` imports the moved names from the module that now holds them;
  `cycle_stages.py` keeps no import made only for the tests. `foundations/part_map.md` names the
  module among the *Trust boundary* files of `task-cycle`, since it reads the transcripts (WAY-48).
  The list of the script that measures the cost in `process-audit/audit_count.py` changes in
  Slice 17, not here (F9). The changed `.py` files are formatted as Slice 3 gives.
- **Change:** `task-cycle/cycle_stages.py` · `task-cycle/stage_transcripts.py` ·
  `task-cycle/test_cycle_stages.py` · `foundations/part_map.md`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:32-32` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:108-108` Questions carried to cycle ·
  F2 · F9 · `foundations/decisions.md:6615-6651` WAY-365 · `foundations/decisions.md:2565-2593`
  WAY-48 · `foundations/decisions.md:8399-8534` WAY-339 ·
  `foundations/invariants.md:438-446` function-and-file-size ·
  `foundations/invariants.md:498-506` cycle-stages-refuses-crafted-names ·
  `foundations/invariants.md:398-406` audit-series-script-paths ·
  `foundations/invariants.md:348-356` cross-part-imports · `foundations/invariants.md:126-134`
  script-imports · `foundations/part_map.md:102-112` task-cycle · `guidelines/coding.md` ·
  `guidelines/coding-measuring-report.md` · `guidelines/coding-shared-module.md` ·
  `guidelines/testing.md` · `process-audit/stage_pricing.py:1-7` · `agent-instructions/test_size_invariant.py`
- **Model:** same — orchestrator's change to the planner's `cheaper`: the slice divides two functions of 114 and 131 lines and cuts a 1270-line script at a trust boundary into two modules, a design done by the executor
- **Risk:** trust boundary — `task-cycle/cycle_stages.py`, `task-cycle/stage_transcripts.py`
- **Checks:** `<ruff>` as in Slice 1. `python -B gate/run_tests.py task-cycle`, `… process-audit`
  (its tests run `cycle_stages.py` as a process) and `… elements/part-map` pass; the counting of
  `function_sizes` and `file_lines` of `agent-instructions/test_size_invariant.py`, run on both
  files, finds no function over 110 lines and no file over 1200; a new interpreter that imports
  `stage_transcripts` with its input empty ends with exit code 0 and writes nothing;
  `<ruff> format --check --config ruff.toml` and `<ruff> check --config ruff.toml --ignore-noqa` on
  the three `.py` files exit 0; `python -B elements/common/foundation_check.py` exits 0.
- **Depends on:** Slice 5 · Slice 3 · F2 · F9

### Slice 14 — the copy of the audit's command takes every module beside it

- **Goal:** `test_the_way_without_a_repository_key_is_this_checkout` of
  `process-audit/test_audit_count.py` copies into the checkout it builds, beside
  `process-audit/audit_count.py`, every Python file of `process-audit/` whose name does not begin
  with `test_`, found when the test runs, beside the other files it copies now, so that a module
  that a later slice moves out of `audit_count.py` is copied with no change of this test. Its
  assertions do not change (WAY-233). The changed file is formatted as Slice 3 gives.
- **Change:** `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:32-32` To do ·
  `foundations/decisions.md:9933-9975` WAY-233 · `guidelines/testing.md`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `<ruff>` as in Slice 1. `python -B gate/run_tests.py process-audit` passes; once, in the
  agent's working copy, a module made for a moment beside `audit_count.py` and imported by it is
  copied by the test, which passes, and then removed; `<ruff> format --check --config ruff.toml` and
  `<ruff> check --config ruff.toml --ignore-noqa` on the file exit 0.
- **Depends on:** Slice 8

### Slice 15 — the register of problems and the reading of records moved out of the audit's command

- **Goal:** two parts of `process-audit/audit_count.py` move into new modules, with no change of
  behaviour, exit codes, messages or the bytes of the report: the register of problems — from
  `Problem` to `read_register` at the base, with what only it uses — into
  `process-audit/problem_register.py`, and the reading of a cycle's record and of its files from
  git — from `header_fields` to `read_gate` at the base, with the classes they fill and the
  constants only they use; `fill` and `read_repository` move too where the cut needs them — into
  `process-audit/record_reading.py`. On the way `read_gate` (153 lines) is divided to at most 110
  (F2), each part with a name of its own. A module never imports `audit_count.py`: what both need
  moves into a module, and `audit_count.py` imports what it uses. A name that
  `process-audit/test_audit_count.py` or `process-audit/test_audit_series_scripts.py` reaches as
  `audit_count.<name>` (`Git`, `GitError`, `Cycle`, `fill`, `Prices`, `Version`, `Ancestry`,
  `cost_boundary`, `count_boundary`, `Register`, `instrument_series`, `read_contradiction`,
  `remarks_check`, `COST_SCRIPT`, `COST_SCRIPTS`, `COUNT_PATHS`, `MEASURES_SCRIPT`, `GATE_SCRIPT`,
  `GATE_TEST_RUNNER`, `TOOL_GROUPS`) and that `audit_count.py` no longer uses itself stays
  importable from it until Slice 17, by an import that `__all__` of `audit_count.py` names, never
  by a `noqa`; Slice 18 removes it. The tests do not change. Each module's description says, as that
  of `process-audit/stage_pricing.py` does, what it holds, that it was moved out of
  `audit_count.py` and that it is imported, never run, and importing it runs nothing (the rule of
  the kind `shared-module`). The description of `audit_count.py` stays whole there.
  `foundations/part_map.md` names both modules among the *Trust boundary* files of `process-audit`,
  since they read the user's register and the records of cycles (WAY-48). The changed `.py` files
  are formatted as Slice 3 gives.
- **Change:** `process-audit/audit_count.py` · `process-audit/problem_register.py` ·
  `process-audit/record_reading.py` · `foundations/part_map.md`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:32-32` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:108-108` Questions carried to cycle ·
  F2 · `foundations/decisions.md:6615-6651` WAY-365 · `foundations/decisions.md:2565-2593` WAY-48 ·
  `foundations/invariants.md:438-446` function-and-file-size ·
  `foundations/invariants.md:528-536` audit-count-refuses-record-links ·
  `foundations/invariants.md:348-356` cross-part-imports · `foundations/invariants.md:126-134`
  script-imports · `foundations/part_map.md:125-136` process-audit ·
  `foundations/part_map.md:262-269` External context · `guidelines/coding.md` ·
  `guidelines/coding-measuring-report.md` · `guidelines/coding-shared-module.md` ·
  `process-audit/stage_pricing.py:1-7` · `process-audit/test_audit_series_scripts.py` ·
  `process-audit/test_audit_count.py:2345-2366` · `process-audit/test_audit_count.py:3536-3616` ·
  `process-audit/test_audit_count.py:3780-3800` · `process-audit/test_audit_count.py:4060-4140` ·
  `process-audit/test_audit_count.py:4340-4350` · `agent-instructions/test_size_invariant.py`
- **Model:** same — orchestrator's change to the planner's `cheaper`: the slice moves two parts of a 3600-line script at a trust boundary into modules and divides a 153-line function, with a transitional `__all__` that must be exact
- **Risk:** trust boundary — `process-audit/audit_count.py`, `process-audit/problem_register.py`,
  `process-audit/record_reading.py`
- **Checks:** `<ruff>` as in Slice 1. `python -B gate/run_tests.py process-audit` and
  `… elements/part-map` pass; the counting of `function_sizes` and `file_lines` of
  `agent-instructions/test_size_invariant.py`, run on the two modules, finds no function over 110
  lines and no file over 1200; a new interpreter that imports each module with its input empty ends
  with exit code 0 and writes nothing; `<ruff> format --check --config ruff.toml` and
  `<ruff> check --config ruff.toml --ignore-noqa` on the three `.py` files exit 0;
  `python -B elements/common/foundation_check.py` exits 0.
- **Depends on:** Slice 14 · Slice 13 · Slice 5 · F2

### Slice 16 — the analysis of versions and the report moved out of the audit's command

- **Goal:** two more parts of `process-audit/audit_count.py` move into new modules, with no change
  of behaviour, exit codes, messages or the bytes of the report: the analysis of the versions of the
  process — from `Ancestry` at the base through `analyse`, the versions, series and boundaries, to
  `process_versions`, with the constants of the series (`COST_SCRIPT`, `COST_SCRIPTS`,
  `COUNT_PATHS`, `MEASURES_SCRIPT`, the scripts of the gate times, `GATE_TEST_RUNNER`,
  `TOOL_GROUPS`) and their comments — into `process-audit/version_analysis.py`, and the writing of
  the report — from `count_rows` at the base to `render` and `write` — into
  `process-audit/audit_report.py`. On the way `analyse` (219 lines) and `render` (206) are divided to
  at most 110 lines each (F2), each part with a name of its own. After this slice
  `audit_count.py` and every module moved out of it stand at most 1200 lines and no function of them
  over 110. A module never imports `audit_count.py`. Names the tests reach as
  `audit_count.<name>`, as Slice 15 lists them, stay importable through `__all__` of
  `audit_count.py` until Slice 17, never by a `noqa`; the tests do not change. Each module's
  description says what it holds, that it was moved out of `audit_count.py` and that it is imported,
  never run, and importing it runs nothing. Neither module reads input from outside the product, so
  neither is a trust boundary (WAY-48) and the part map does not change. The changed `.py` files are
  formatted as Slice 3 gives.
- **Change:** `process-audit/audit_count.py` · `process-audit/version_analysis.py` ·
  `process-audit/audit_report.py`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:32-32` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:108-108` Questions carried to cycle ·
  F2 · `foundations/decisions.md:6615-6651` WAY-365 · `foundations/decisions.md:2565-2593` WAY-48 ·
  `foundations/decisions.md:8399-8534` WAY-339 ·
  `foundations/invariants.md:438-446` function-and-file-size ·
  `foundations/invariants.md:398-406` audit-series-script-paths ·
  `foundations/invariants.md:348-356` cross-part-imports · `foundations/part_map.md:125-136`
  process-audit · `foundations/part_map.md:262-269` External context · `guidelines/coding.md` ·
  `guidelines/coding-measuring-report.md` · `guidelines/coding-shared-module.md` ·
  `process-audit/stage_pricing.py:1-7` · `process-audit/test_audit_series_scripts.py` ·
  `agent-instructions/test_size_invariant.py`
- **Model:** same — orchestrator's change to the planner's `cheaper`: the slice divides two functions of 219 and 206 lines (the largest of the change) and moves the analysis of versions and the report into two modules
- **Risk:** trust boundary — `process-audit/audit_count.py`
- **Checks:** `<ruff>` as in Slice 1. `python -B gate/run_tests.py process-audit` and
  `… elements/part-map` pass; the counting of `function_sizes` and `file_lines` of
  `agent-instructions/test_size_invariant.py`, run on `audit_count.py` and on the four modules moved
  out of it, finds no function over 110 lines and no file over 1200; a new interpreter that imports
  each new module with its input empty ends with exit code 0 and writes nothing;
  `<ruff> format --check --config ruff.toml` and `<ruff> check --config ruff.toml --ignore-noqa` on
  the three `.py` files exit 0.
- **Depends on:** Slice 15 · F2

### Slice 17 — the tests import from the new modules, and the cost script spans two files

- **Goal:** `process-audit/test_audit_count.py` and `process-audit/test_audit_series_scripts.py`
  import each name they reached as `audit_count.<name>` from the module that now holds it.
  `COST_SCRIPTS` in `process-audit/version_analysis.py` names `task-cycle/stage_transcripts.py`
  beside `task-cycle/cycle_stages.py`, so that a change of either starts a series of the cost and
  marks a cycle that changes it as having changed the tool (F9, WAY-339); where the report names the
  script that measures the cost, it names both files. The expected values that follow from this —
  the tuple of `test_each_path_that_starts_a_series_is_a_path_git_tracks` and the set of the test of
  `audit-series-script-paths` where it holds the cost script — change with their cause in a comment:
  the script that measures the cost spans two files since Slice 13 (F9, WAY-233); the request names
  the invariant test it alters (WAY-03). No other expected value changes. The changed files are
  formatted as Slice 3 gives.
- **Change:** `process-audit/test_audit_count.py` · `process-audit/test_audit_series_scripts.py` ·
  `process-audit/version_analysis.py` · `process-audit/SKILL.md` (orchestrator's addition, from the
  report of the agent of the entries: line 54 names `task-cycle/cycle_stages.py` alone as the script
  that measures the cost; it names both files, as F9 does, and nothing else of the skill changes)
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:32-32` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:108-108` Questions carried to cycle ·
  F9 · `foundations/decisions.md:8399-8534` WAY-339 · `foundations/decisions.md:9933-9975` WAY-233 ·
  `foundations/decisions.md:1759-1803` WAY-03 ·
  `foundations/invariants.md:398-406` audit-series-script-paths · `guidelines/testing.md` ·
  `guidelines/coding.md` · `guidelines/coding-shared-module.md`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `<ruff>` as in Slice 1. `python -B gate/run_tests.py process-audit` passes; a search of
  the two test files finds no `audit_count.` before a name that moved;
  `<ruff> format --check --config ruff.toml` and `<ruff> check --config ruff.toml --ignore-noqa` on
  the three files exit 0; `python -B elements/common/foundation_check.py` exits 0 and lists no
  reworded invariant whose test was left as it was.
- **Depends on:** Slice 16 · Slice 13 · F9

### Slice 18 — the transitional exports of the audit's command removed

- **Goal:** `process-audit/audit_count.py` loses its `__all__` and every import that stood only so
  that the tests could reach a moved name, and nothing else changes; behaviour, exit codes and
  messages stay. The changed file is formatted as Slice 3 gives.
- **Change:** `process-audit/audit_count.py`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:32-32` To do ·
  `foundations/invariants.md:428-436` ruff-blocking-rules · `guidelines/coding.md`
- **Model:** cheaper
- **Risk:** trust boundary — `process-audit/audit_count.py`
- **Checks:** `<ruff>` as in Slice 1. `<ruff> check --config ruff.toml --no-cache --ignore-noqa` and
  `<ruff> format --check --config ruff.toml` on the file exit 0; `python -B gate/run_tests.py process-audit`
  passes; the counting of `file_lines` of `agent-instructions/test_size_invariant.py` gives the file
  at most 1200 lines.
- **Depends on:** Slice 17

### Slice 19 — the size test turned strict and its mark cleared

- **Goal:** in `agent-instructions/test_size_invariant.py`, the thresholds are those of F2 (110 for
  a function, 1200 for a file), the test `test_no_function_or_file_of_a_script_is_over_its_threshold`
  loses its marking as an expected failure, and the module's description gives the new thresholds
  and loses its sentences about the invariant being violated and the expected failure;
  `function-and-file-size` in `foundations/invariants.md` reads `Violated: no` (WAY-51). The request
  names the cleared mark and the changed invariant test (WAY-51, WAY-03). The changed `.py` file is
  formatted as Slice 3 gives.
- **Change:** `agent-instructions/test_size_invariant.py` · `foundations/invariants.md`
- **Read:** `.runs/task-cycles/code-order-formatter-linter-size/task.md:32-33` To do ·
  `.runs/task-cycles/code-order-formatter-linter-size/task.md:38-41` Acceptance criteria · F2 ·
  `foundations/decisions.md:1835-1879` WAY-51 · `foundations/decisions.md:1759-1803` WAY-03 ·
  `foundations/decisions.md:9933-9975` WAY-233 · `guidelines/testing.md` · `guidelines/coding.md`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `<ruff>` as in Slice 1. `python -B gate/run_tests.py agent-instructions` passes with the
  size test passing and no expected failure left in `test_linter_invariant.py` or
  `test_size_invariant.py`; `python -B elements/common/foundation_check.py` exits 0;
  `<ruff> format --check --config ruff.toml` and `<ruff> check --config ruff.toml --ignore-noqa` on
  the file exit 0.
- **Depends on:** Slice 8 · Slice 11 · Slice 12 · Slice 18 · F2

## Coverage

| What the task requires | Slices or entries |
|---|---|
| To do 1 — Ruff's formatter at width 100, `.py` only, one reformatting in a commit of its own, its hash in `.git-blame-ignore-revs` given to `repository` | F1 · Slice 1 · Slice 2 · Slice 3 |
| To do 2 — the formatter's invariant and test beside the linter's, no `fmt:` comments; the example of `installation/README.md`; `### Formatter` with decision and invariant; "Installing the linter" | F4 · F5 · Slice 3 |
| To do 3 — the 24 linter faults fixed in their files, no rule turned off (TRY004 kept to exit code 2) | Slice 5 · Slice 6 · Slice 7 · Slice 8 |
| To do 4 — thresholds 110/1200 in WAY-385; every function and file over them divided after the reformatting | F2 · Slice 11 · Slice 12 · Slice 13 · Slice 14 · Slice 15 · Slice 16 · Slice 17 · Slice 18 · Slice 19 |
| To do 5 — both tests lose the expected failure, both invariants read `Violated: no`, sentences about the known faults removed from decisions, guidelines and test descriptions | Slice 8 (linter) · Slice 19 (size) · F2 (WAY-385's sentence on the mark) |
| To do 6 — the full check of the foundation in the gate, citing its own invariant, at any name of the main branch; the narrow test stays; the README paragraph | F3 · Slice 4 |
| To do 7 — the worktree test independent of git's background maintenance | Slice 9 |
| To do 8 — "entry" replaced where it is no entry of the foundation; no glossary entry | F6 · F7 · F8 · Slice 10 |
| Acceptance 1 — the gate green in CI on Linux and Windows with no expected failure in the two tests | Slice 8 · Slice 19; the gate on the finished change is the orchestrator's or CI's (WAY-160) |
| Acceptance 2 — the test of the-way's foundation passes in a clone whose main branch is `main` and fails on a reference to a missing decision | Slice 4 (its checks) |
| Row 1 — formatter at width 100, one reformatting | F1 |
| Row 2 — 110/1200 on formatted code | F2 |
| Row 3 — the check of the foundation reports no error, held by the full test | F3 · Slice 4 |
| Row 4 — `.py` only, no Markdown examples | F1 · F4 · Slice 1 · Slice 3 |
| Row 5 — `fmt:` comments forbidden, the test fails on them | F1 · F4 · Slice 3 |
| Questions carried to cycle | *Choices* rows 1, 7, 8, 9, 12, 13 |

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| 1. The linter faults are fixed after the reformatting commit (Slices 5–8), and the formatter's test stands right after that commit (Slice 3): F4 holds from that commit (WAY-205), so every later change, the fixes included, is held to the layout by a test, and the two new invariants go uncited only through Slices 1–3 (WAY-61, WAY-321); the linter's mark clears in the slice in which its test starts to pass (WAY-51) | the fixes before the reformatting — reviewed on the layout the task's line numbers point to, but the invariants F3 and F4 would stand uncited through four more slices, during which `elements/common`'s tests, which the fixes of `foundation_check.py` need, could not run | a fix at a trust boundary is read on the new layout, so its review compares behaviour, not lines; nothing to undo |
| 2. The formatter's configuration goes in a slice of its own before the reformatting, and the reformatting runs from the committed configuration | the configuration in the reformatting commit — that commit would hold another change; the reformatting run with command-line switches and the configuration after it — for a slice the configuration and the code would disagree | one more small slice |
| 3. The reformatting's *Change* names one pattern per part's directory, `elements/**/*.py` covering its two directories, ten patterns | one pattern per output directory — eleven, over the limit of ten files the size script sets, though the command is one | the mechanical check reads `elements/**/*.py` as covering `elements/common` and `elements/part-map`; nothing else |
| 4. Markdown is kept out twice: the configuration keeps `ruff format` off `.md` files, and the test passes only the `.py` files git tracks | only the test — a human or agent running `ruff format .` would reformat 249 Markdown files; only the configuration — the invariant would rest on a setting a change of `ruff.toml` can drop unseen | a later change of the configuration that lets Markdown in is caught by the run from the root, not by the test |
| 5. The test of the formatter stands in `agent-instructions/test_linter_invariant.py`, in a class of its own, beside the linter's test and with its way of finding Ruff | a new file — it would repeat the finding of Ruff in the main checkout or import it from another test file | the file's name speaks of the linter alone; its description covers both |
| 6. `fmt:` comments are found among the comments `tokenize` gives | a search of the text — it would flag the test's own pattern and words inside strings | a comment written in a form `tokenize` does not give as a comment would pass; none does |
| 7. F4 and F3 are written before slice 1 by the agent of the entries, and F1's *Verification* names F4 | F4 written by Slice 3 with its test (WAY-69) — WAY-382 could not name it, since no slice can change `foundations/decisions.md` within the reading limit of the size script | three slices run no test of `elements/common` |
| 8. The full test runs `foundation_check.py` unchanged, with the base it finds in git, and asserts exit code 0; a run on 2026-11-19 in a clone with no `origin/HEAD` and a local `main` at an old commit (`f16616c0`) gave 0 errors | a new argument that fixes the base — a change of `foundation-check-command`, which no row carries; the test filtering the findings that depend on the base — the narrowing the task undoes | where a clone gives a base that makes a decision look added and unheld, the test turns red on a real gap of that clone's comparison; the checks of Slice 4 run it in a clone with `main` and in a shallow clone |
| 9. A second reformatting, needed where `foundations` brings new unformatted code before the merge, is a commit of its own holding only the formatter's output, and its hash is added to `.git-blame-ignore-revs` in a later commit — by the orchestrator at that merge, as the answer "3a" gives for the first | the new code's layout folded into the merge commit — `git blame` names the merge for each reformatted line | one more line in the file |
| 10. Git's background maintenance and collection of garbage are turned off for every git process of the worktree test through its environment, and the snapshot stays whole | `origin.git` left out of the snapshot, as the description of `state` ("git's own directories left out") allows — it weakens the test of `repository-changer-acts-only-when-told` (WAY-233) where the script would write into the remote | another background writer of a future git brings the failure back, seen as before |
| 11. `task-cycle/test_gate_times.py` takes the same word as `gate_times.py` and F8, though the task lists only `gate_times.py` | left as it is — the tests of F8 would speak of entries while the sentence and the script do not | the request names one more invariant test (WAY-03) |
| 12. The modules moved out of `cycle_stages.py` and `audit_count.py` follow the rule of the kind `shared-module` (importing runs nothing) and the description of `stage_pricing.py`, and get no row in `guidelines/coding-shared-module.md`, as `stage_pricing.py` and `record_items.py` have none | rows in the table of the kind — a status (`copy`, `do not copy`) is a judgment of `maintain-coding-guidelines`, and the kind's *Applies to* lacks `task-cycle` | the table goes on not listing every module of the kind; named in the report as a guideline found uncertain |
| 13. A moved module is a trust boundary where it reads input from outside the product — the transcripts, the records, the user's register — and none where it only computes or writes the report from values already read (WAY-48), as `record_items.py` is one and `stage_pricing.py` none | every module moved out of a trust boundary named one — WAY-48 counts files that take in what the product does not control | a later change to `audit_report.py` gets no review aimed at crafted input, though it writes text a record carries into the report |
| 14. The tests import moved names from the module that now holds them; between Slices 15 and 17 `audit_count.py` keeps them importable through `__all__`, and Slice 18 removes that | `__all__` kept for good — names the command's code does not use stay in it for the tests; the tests changed in each move — a slice changing `test_audit_count.py` and `audit_count.py` exceeds the reading limit | two more small slices (17, 18) |
| 15. Slice 14 makes the copy test take every non-test Python file of `process-audit/` | each new module added to the test's list in its move slice — the same reading limit | the test copies files the command does not import; harmless |
| 16. The reading of the transcripts moves from `cycle_stages.py` to `task-cycle/stage_transcripts.py`, and the audit's list of the script that measures the cost (`COST_SCRIPTS`), WAY-339 and `audit-series-script-paths` name both files (F9) | the list left as it is — a later change of the moved code would start no series of the cost, against WAY-339; `cycle_stages.py` brought under 1200 lines without dividing it — a cut made only to stand under the threshold (`guidelines/coding.md`, *Bad*); every part of the file measures the cost, so no cut avoids the list | the request puts F9 before the human; were it refused, the division of `cycle_stages.py` would need a spec |
| 17. `audit_count.py` is cut into four modules — the register of problems, the reading of records, the analysis of versions, the writing of the report — in two slices | one module per slice — four reviews where two read the same kind of move | each of the two reviews reads a larger move |
| 18. The four over-long functions at the trust boundaries of installation, instruction-files and project-level are divided in one slice on the orchestrator's class | three slices on the cheaper class — three reviews of their own | a failure of one division sends the whole slice back |
| 19. Every division is a move into functions or modules of the same part, with no change of behaviour, checked by the directory's tests (WAY-365) | a rewrite of the divided functions | none beyond the time of the move |
