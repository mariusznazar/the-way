# Report of the fix of the Minor findings — script-invariants-by-test

**Status:** done

## Commits

- `540aed04` — "Fix the Minor findings of the review: narrow the kind .yml, drop wording from expected values, place the script tests in agent-instructions, name a missing .python-version" (from the reviewed head `4bc1667c`).

## Files changed

| File | Change |
|---|---|
| `elements/part-map/test_script_invariants.py` → `agent-instructions/test_script_invariants.py` | moved (`git mv`), then edited (M1, M2, M3, M4) |
| `elements/common/test_element_directory_contents.py` | edited (M2) |

No foundation file changed in this fix. `foundations/part_map.md` is untouched (M3 took the move, below).

## Findings, one by one

**M1 — fixed.** The kind `.yml` is no longer listed by its ending anywhere. `SUFFIXES` holds `.py` and `.md`; a new list `PLACES = ((".github/workflows/", ".yml"),)` lets a path pass that starts with the place and ends with the ending, and `possible_scripts` reads it. The comment at the entry gives the reason (CI configuration, whose commands `ci-checking-commands` keeps), and the reach now equals the reason. New test `ScriptLanguage.test_a_configuration_file_outside_the_place_of_its_kind_is_reported` (a root `tools_deploy.yml`, `docs/deploy.yml` and a `.sh` under the workflows directory are reported); the existing `test_a_python_file_a_text_and_a_file_of_the_listed_kinds_pass` still passes `.github/workflows/tests.yml`.
Check: the reviewer's case, a tracked root `tools_deploy.yml` holding an Ansible-style playbook (`git add`, removed from index and disk after): `python -B -m unittest discover -s agent-instructions -p test_script_invariants.py -k test_every_file_git_tracks` — exit 1, `AssertionError: Lists differ: [] != ['tools_deploy.yml']` (before the fix the same case gave exit 0). Passing run without it: exit 0.

**M2 — fixed.**
- `ScriptImports.test_an_import_whose_name_cannot_be_worked_out_is_reported` no longer asserts the wording of the reader: it asserts one report whose text starts with `a.py:2:` (the file and the line of the call; the requirement is that the import is reported). The six-forms test asserts `yaml` in the report, not the backticked wording.
- `missing()` of `elements/common/test_element_directory_contents.py` now returns pairs `(directory, what)` with `what` one of `template`, `examples`, `skill`; the five tests that asserted its sentences assert the pairs, so rewording a message breaks none. The sentence moved into the failure message of the repository test, where it explains the failure and is asserted by nothing.
- *Data* sources named in comments: the listed kinds (the task's list and the four kinds the change added, each in a file git tracks), the patch release (the sentence of `python-version-declared` reads `3.14.3` as declaring 3.14, my choice 4 of the first report), the six forms (the reach of settlement row 3), the classes `Missing` (the three names the invariant and the directories of this repository give; the pointer form of `elements/environment-facts/template.md`) and `MergeOntoExists` (`elements/common/rules.md`, section `{fork-point}`, which defines {merge-onto}; `foundations` and `work` are made-up branch names).
Check: `python -B -m unittest discover -s elements/common -p test_element_directory_contents.py` — exit 0, 13 tests; `python -B -m unittest discover -s agent-instructions -p test_script_invariants.py` — exit 0, 13 tests; the file has 13 tests, the 11 of before and the two added below. I did not repeat the breaks of the first report on `element-directory-contents` after the rewrite of `missing()`; the unit tests of `Missing` assert the same facts (which directory lacks which thing).

Not changed in M2: `PythonVersionDeclared`'s assertion messages and the literal `3.14`, whose source is the sentence of the invariant (named at the constant).

**M3 — fixed by moving the file; the choice and the way rejected.** The three tests of `python-version-declared`, `script-language` and `script-imports` now stand in `agent-instructions/test_script_invariants.py` (the file moved whole, not split: the three share the version read and the helper that lists tracked files). Why this way:
- The map's sentence for `agent-instructions` covers the guidelines of the-way's own code and the instructions and configuration that direct agents, and the part already holds the tests of the-way's own code rules (`agent-instructions/test_linter_invariant.py`, `test_size_invariant.py`); WAY-38 and WAY-89 name `agent-instructions` in their *Scope*, so a later change to this file selects them with `--part agent-instructions`, which the review found missing in `part-map`.
- `agent-instructions` depends, by the map, on `part-map` and `repository`, so the import of `imports` from `elements/part-map/test_cross_part_imports.py` is one the map allows (`sys.path.insert(0, os.path.join(HERE, "..", "elements", "part-map"))`, which the reader of `cross-part-imports` works out; its test, in `elements/part-map`, passes on the moved file).
- The fewest changes: one `git mv` and the path lines of the file; no change to the part map, to WAY-44's *Scope* or to an entry of the foundation. The three tests keep their lines `invariant: python-version-declared`, `invariant: script-language` and `invariant: script-imports`, and `foundation_check.py` without the switch reports no uncited invariant.
Way rejected: widen the sentence of `part-map` in `foundations/part_map.md` to name these tests, through `elements/part-map/skill/SKILL.md`. Cost: a change of a map entry and of its derived places (the sentence says the part answers for the import test, so the `Scope` of the decisions that bear on the script rules would also have to name `part-map`, or the same gap stays), and `part-map` would then answer for script rules that no entry of it carries. The cost of the way taken, if wrong: the file moves once more and the citations stay; the test of `script-imports` imports a file of another part, which the map allows and the reader of `cross-part-imports` checks on every run.
Check: `python -B gate/run_tests.py elements/part-map` — exit 0 (40 tests: the 51 of before less the 11 of the moved file; the test of `cross-part-imports` on the real repository passes with the file in its new place); `python -B gate/run_tests.py agent-instructions` — see "Last runs".

**M4 — fixed.** `wrong_interpreter(declared, running)` takes `None` for a `.python-version` that is missing or holds no version and answers with a message that names the file and says it is missing or holds no version, with the version of the run. The test no longer turns the absence into the string `none`. New test `ScriptImports.test_a_missing_declaration_is_refused_by_naming_the_file`.
Check: `.python-version` moved away from the working tree for a moment (restored, `git status` shows no change to it): `python -B -m unittest discover -s agent-instructions -p test_script_invariants.py -k test_no_python_file_git_tracks` — exit 1, `AssertionError: .python-version is missing or holds no version, so the version of Python the tests have to run on is not declared (this run is on Python 3.14)`. Before the fix the message read "Python none".

## Tests changed or added, by name (WAY-03)

In `agent-instructions/test_script_invariants.py`: added `ScriptLanguage.test_a_configuration_file_outside_the_place_of_its_kind_is_reported`, `ScriptImports.test_a_missing_declaration_is_refused_by_naming_the_file`; changed (expected value from the wording of the code to the behaviour it carries, cause M2 of `fix-findings.md`) `ScriptImports.test_an_import_whose_name_cannot_be_worked_out_is_reported` and `ScriptImports.test_a_module_outside_the_standard_library_is_reported_in_each_form_of_import`; the three tests that cite the invariants (`PythonVersionDeclared.test_the_repository_declares_python_3_14_in_python_version`, `ScriptLanguage.test_every_file_git_tracks_is_a_python_file_or_of_a_kind_that_is_no_script`, `ScriptImports.test_no_python_file_git_tracks_imports_a_module_outside_the_standard_library`) moved with the file; the last of them changed in how it reads the declared version (M4) and the path it stands at (M3). In `elements/common/test_element_directory_contents.py`: the five `Missing` tests that asserted sentences now assert pairs (M2); the repository test `ElementDirectoryContents.test_every_element_directory_holds_a_template_examples_or_a_pointer_and_a_skill` has the sentence as its failure message. No assertion was weakened: each now asserts the same fact (which directory lacks which thing) without the words of the message; the evidence is the findings file, M2.

## Checks (command, exit code)

- `python -B -m unittest discover -s agent-instructions -p test_script_invariants.py` — exit 0 (13 tests); `... -p test_element_directory_contents.py` in `elements/common` — exit 0 (13 tests).
- `python -B gate/run_tests.py elements/part-map` — exit 0 (40 tests).
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`, after the commit.
- ``ruff.exe` of the quality environment `.runs/quality-venv` of the main checkout check --config ruff.toml --no-cache --ignore-noqa --output-format concise` on the two files — exit 0, `All checks passed!`.
- `python -B gate/run_tests.py agent-instructions` and `python -B gate/run_tests.py elements/common` on the committed tree — see "Last runs" below.
- Not run: the full gate (WAY-160).

## Last runs

- `python -B gate/run_tests.py agent-instructions` — exit 0 (50 tests, `OK (expected failures=2)`: the two expected failures are the tests of the invariants `ruff-blocking-rules` and `function-and-file-size`, which read `Violated: yes`; the file moved here is among the 50).
- `python -B gate/run_tests.py elements/common` — exit 0 (270 tests, OK).

## Reaches beyond the handoff

`foundations/part_map.md` lines for `agent-instructions` and `part-map` (read in the first report) were re-read for M3; `git grep` for the old path of the file (no match in a tracked file); `agent-instructions/test_linter_invariant.py` and `test_size_invariant.py` by name only, as the places the part keeps its code-rule tests.

## Working copies

`.runs/author/` of the worktree holds the outputs of the focused runs (`fix-part-map.txt`, `fix-agent-instructions.txt`, `fix-common.txt`, and the earlier `common.txt`, `part-map.txt`); ignored by git, kept as evidence. The temporary breaks (a tracked `tools_deploy.yml`, the moved `.python-version`) were undone in the worktree before the commit and `git status` is clean. No worktree or clone was made.

## Unread material

none — WAY-344 and WAY-395 were read whole for this fix (WAY-344 from its sentence to the end of its *Verification* complies/violates; WAY-395 whole), and `fix-findings.md` and the handoff whole. I did not read `review-whole-report.md`: each finding stood whole in the findings file.

## Searches not found or unclear

none

## Concerns

- The first report's note on the earlier test of `script-imports` seen red on Python 3.12 stands; the moved test was not run again on 3.12 (the unit test `test_an_interpreter_of_another_version_is_refused_with_both_versions` covers the message).
