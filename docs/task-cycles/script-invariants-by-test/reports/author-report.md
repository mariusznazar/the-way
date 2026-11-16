# Report of the one author — script-invariants-by-test

**Status:** done

## Commits

- `4bc1667c` — "Test the invariants python-version-declared, script-language, script-imports and element-directory-contents" (on `task/script-invariants-by-test`, base `604907c8`).

## Files changed

| File | Added / removed |
|---|---|
| `elements/part-map/test_script_invariants.py` (new) | +209 / 0 |
| `elements/common/test_element_directory_contents.py` (new) | +222 / 0 |
| `foundations/invariants.md` | +4 / -4 (`Method: review` to `Method: test` under the four headings, nothing else) |

No move of a function or file over the size threshold was needed (WAY-365): the change adds two new test files, and test files stand outside the rule of size (WAY-385).

## Tests written, by name (WAY-03)

`elements/part-map/test_script_invariants.py`:

- `PythonVersionDeclared.test_the_repository_declares_python_3_14_in_python_version` (cites `python-version-declared`)
- `ScriptLanguage.test_every_file_git_tracks_is_a_python_file_or_of_a_kind_that_is_no_script` (cites `script-language`)
- `ScriptLanguage.test_a_file_of_another_language_is_reported`
- `ScriptLanguage.test_a_python_file_a_text_and_a_file_of_the_listed_kinds_pass`
- `ScriptLanguage.test_a_file_named_like_a_listed_kind_in_its_ending_only_is_reported`
- `ScriptImports.test_no_python_file_git_tracks_imports_a_module_outside_the_standard_library` (cites `script-imports`)
- `ScriptImports.test_an_interpreter_of_another_version_is_refused_with_both_versions`
- `ScriptImports.test_the_declared_version_and_a_patch_release_of_it_are_accepted`
- `ScriptImports.test_a_module_outside_the_standard_library_is_reported_in_each_form_of_import`
- `ScriptImports.test_a_module_of_the_standard_library_and_a_tracked_file_are_no_failure`
- `ScriptImports.test_an_import_whose_name_cannot_be_worked_out_is_reported`

`elements/common/test_element_directory_contents.py`:

- `ElementDirectoryContents.test_every_element_directory_holds_a_template_examples_or_a_pointer_and_a_skill` (cites `element-directory-contents`)
- `Missing.*` (8 tests: complete directory; pointer in the template stands for examples; pointer to an untracked file; pointer outside the section `## Examples`; no skill; no template; a new directory with one file; `common` is no element directory)
- `MergeOntoExists.*` (4 tests: `main` branch; `origin/HEAD`; branches but no main branch; no commit)

No existing test was changed, weakened, skipped or deleted. These are new invariant tests, so the request names them (WAY-03).

## Where each test file stands, and why

- `elements/part-map/test_script_invariants.py` stands in part `part-map` (`elements/part-map/**`). The test of `script-imports` reuses `imports` of `elements/part-map/test_cross_part_imports.py`, the reader of the invariant `cross-part-imports`, which stands in the same part, so the import is no import between parts. `script-language` and `python-version-declared` need no import; they stand in the same file because the three invariants are the script rules of WAY-38 and WAY-89 and the test of `script-imports` reads the declared version too. `python-version-declared` names the part `repository`, which has no directory of its own (its files are root files), so no directory of that part can hold a test; `gate/` was rejected because `gate` depends on no part and so could not import the reader, and moving the reader out of `part-map` would be a change of another invariant's test. Cost if wrong: the file moves and the citations stay.
- `elements/common/test_element_directory_contents.py` stands in part `elements-common` (`elements/common/**`), beside the exemplar repository test `test_elements_pending_marker.py`, which tests an invariant about the same directories. It imports only `foundation_source.py` of its own directory.

## Checks (command, exit code)

- `python -B gate/run_tests.py elements/part-map` — exit 0 (51 tests, OK). Run on the committed tree.
- `python -B gate/run_tests.py elements/common` — exit 0 (270 tests, OK), run on the committed tree.
- `python -B elements/common/foundation_check.py` (no `--skip-test-citations`) — exit 0, `0 errors`, after the commit. Before the commit it listed 4 errors: the four invariants read `test` and the new files were not yet tracked, so no tracked file cited them; that is the report of WAY-321 working, and it vanished once the files were tracked.
- ``ruff.exe` of the quality environment `.runs/quality-venv` of the main checkout check --config ruff.toml --no-cache --ignore-noqa --output-format concise <the two new files>` — exit 0, `All checks passed!` (the linter's own test, `agent-instructions`, I did not run: the full set is the orchestrator's).
- `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` — exit 0, `checked: 331 files, 0 listed`; `python -B -m unittest discover -s task-cycle -p test_private_paths_check.py` — exit 0 (54 tests).
- Not run: the full gate (the orchestrator's alone, WAY-160); `agent-instructions`, `task-cycle` and the other directories in full.

## The failing run of each invariant test, and the passing run after (WAY-08)

Each break was made in the worktree for a moment and undone before the commit (`git status` clean of it). The command for the failing and the passing run of a class is the one shown; the passing run of the whole directory is `python -B gate/run_tests.py elements/part-map` (exit 0) and `elements/common`.

1. `python-version-declared` — break: `.python-version` written as `3.13`. Command: `python -B -m unittest discover -s elements/part-map -p test_script_invariants.py -k PythonVersionDeclared`, exit 1, line `AssertionError: False is not true : .python-version declares '3.13', not Python 3.14`. After `git checkout .python-version`: same command, exit 0, `OK`.
2. `script-language` — break: a tracked `build_tool.sh` (`git add`, removed from index and disk after). Command: same with `-k ScriptLanguage`, exit 1, `AssertionError: Lists differ: [] != ['build_tool.sh']`. After: exit 0, `OK` (4 tests).
3. `script-imports` — break (a): a tracked `elements/part-map/outside_import.py` holding `import yaml`; command `... -k test_no_python_file_git_tracks`, exit 1, line `'elements/part-map/outside_import.py:1: imports \`yaml\`, which is neither a module of the standard library nor a file the check sees'`. Break (b), the wrong version: the same command run by `py -3.12 -B -m unittest ...`, exit 1, line `AssertionError: 'the tests have to run on Python 3.14, the version .python-version declares, and this run is on Python 3.12: ...'` (seen first on an earlier form of the assertion, and again on the final form, `self.fail(<that message>)`, with the same exit 1 and the same message). Break (c), the dynamic reach, the own-work check below. After: `python -B -m unittest ... -k test_no_python_file_git_tracks` exit 0, `OK`.
4. `element-directory-contents` — break (a): `git mv elements/glossary/skill/SKILL.md ...`, command `python -B -m unittest discover -s elements/common -p test_element_directory_contents.py -k test_every_element`, exit 1, line `'elements/glossary has no skill/SKILL.md'`; break (b): the two mentions of `foundations/environment_facts.md` in `elements/environment-facts/template.md` replaced by plain words, exit 1, line `'elements/environment-facts has no examples.md and its template points to no file of foundations/ as its examples'`. After both were undone: exit 0, `OK`.

## Own-work check (WAY-164)

The requirement most likely not met: "the test of `script-imports` sees imports in the same reach as the test of `cross-part-imports`, and reports an import whose name cannot be worked out" (point 3 of the task, settlement row 3). The check: a tracked file `elements/part-map/dyn_break.py` holding `importlib.import_module("yaml")` and `importlib.import_module(os.environ["M"])`, run through the real test. It showed exit 1 with both lines reported: `dyn_break.py:2: imports \`yaml\`, which is neither a module of the standard library nor a file the check sees` and `dyn_break.py:3: imports a module the check cannot work out`. The file was removed from index and disk after. The fixture tests `test_a_module_outside_the_standard_library_is_reported_in_each_form_of_import` (six forms: `import`, `from ... import`, `import_module`, `__import__`, `-c`, `exec`) and `test_an_import_whose_name_cannot_be_worked_out_is_reported` keep the reach.

A second requirement I checked: the invariant `element-directory-contents` holds "where {merge-onto} exists"; the test skips with a reason where none does. `MergeOntoExists.*` shows the condition is not stuck at false (a test that always skipped would pass the gate quietly): repositories with `main`, with `origin/HEAD`, with other branches only, and with no commit give true, true, false, false.

## Walk through the running product

The change alters no behaviour a user sees in a running product: it adds tests and four words of foundation entries (`review` to `test`); no screen, API answer, command or data of a product changes. My judgment agrees with the orchestrator's.

## Settlements to record (where each is written)

- Row 1 (`script-language` recognises a script by a list of kinds that are no script; the author adds a kind with its reason): `SUFFIXES` and `NAMES` with a comment at each kind, and the docstring, in `elements/part-map/test_script_invariants.py`.
- Row 2 (`script-imports` on an interpreter other than the declared version fails with both versions): `wrong_interpreter` and its use in `ScriptImports.test_no_python_file_git_tracks_imports_a_module_outside_the_standard_library`, with the reason in the docstring of the file and in the comment of `test_an_interpreter_of_another_version_is_refused_with_both_versions`, same file.
- Row 3 (`script-imports` has the reach of `cross-part-imports`; an import whose name cannot be worked out is reported): `outside_imports`, which calls `imports` of `test_cross_part_imports`, same file; the docstring says so.

All three rows go to "data or code", so no foundation entry is written for them (foundation step: a row whose column names no element is written in its place, in the same change).

Entry meanings (foundation step, the four entries are `projected` of the task's point 5, each only a change of *Method*; the sentence of none changed):

- `python-version-declared` — EN: the repository declares Python 3.14 in `.python-version`, and a test checks it. PL: repozytorium deklaruje Pythona 3.14 w `.python-version`, a sprawdza to test.
- `script-language` — EN: every script git tracks is a Python file, and a test checks it by reporting each file that is neither Python nor of a listed kind that is no script. PL: każdy skrypt śledzony przez git jest plikiem Pythona; test zgłasza każdy plik, który nie jest Pythonem ani rodzajem z listy niebędących skryptami.
- `script-imports` — EN: no script imports a module outside the standard library of Python 3.14 or a tracked Python file, and a test checks it on Python 3.14 only. PL: żaden skrypt nie importuje modułu spoza biblioteki standardowej Pythona 3.14 ani śledzonego pliku Pythona; test sprawdza to tylko na Pythonie 3.14.
- `element-directory-contents` — EN: where {merge-onto} exists, every element directory holds a template, examples or a pointer, and a skill, and a test checks it. PL: tam, gdzie istnieje {merge-onto}, każdy katalog elementu ma szablon, przykłady albo odesłanie i skill, a sprawdza to test.

Marking: none of the four entries comes from a row of *Settlements to record*; each is marked `projected` (point 5 of the task, whose whole text is the change of *Method*). No entry is marked `the cycle's`, and none adds a pair of examples or a field the task left open.

## The kinds added to the list of `script-language` (Q2) and why none is a script

The task's list was `.py`, `.md`, `.gitignore`, `.gitattributes`, `.python-version`. Added:

- `.yml` (here `.github/workflows/tests.yml`): the CI configuration, data in YAML that names the commands CI runs; its `run:` lines are commands written in a configuration, like a command written in a `.md` file, and which commands CI may run is the invariant `ci-checking-commands`. I hold it to be no script. The kind is the ending `.yml`, so another `.yml` file also passes; a person who wants it stricter narrows it to the name `tests.yml`.
- `ruff.toml`: the configuration of the linter, data in TOML, read by Ruff.
- `requirements-quality.in`: the list of the packages the linter is installed from, one name to a line.
- `requirements-quality.txt`: the same list with the sums of the files, read by `pip`; it is data, not a program.

The first is listed by its ending, the others by their names, so a second file of those names' kinds (another `.toml`, another `.txt`) is reported until a change adds it with its reason. I hold none of the four to be a script, so I return no question.

## Reaches beyond the handoff's selection

- `foundations/part_map.md` and the decisions were read as the handoff selected. Beyond it: `elements/common/foundation_source.py` (whole), for `MAIN_BRANCHES` and `git`, which the test of `element-directory-contents` imports; `elements/common/rules.md` lines 78-90 (`{fork-point}` and `{merge-onto}`), for what {merge-onto} is; `elements/invariants/skill/write.md`, `decide_entry.md`, `draft.md`, `elements/common/way_of_working.md` (whole), for writing the entries; `elements/common/test_elements_pending_marker.py` (the exemplar of repository test) and `elements/common/test_guidelines_place.py` (head), for form; `agent-instructions/test_linter_invariant.py` (head) and `ruff.toml`, to find which linter rules block (`E402` does not, so the `noqa: E402` of the imports is kept as in the neighbouring files); `task-cycle/tracked_private_paths_check.py` (head), for the private-paths check I ran; `.github/workflows/tests.yml`, for the CI file. Why: the handoff's selection did not name them and each was needed for the point named.

## Working copies

- `.runs/author/common.txt` and `.runs/author/part-map.txt` (outputs of the two focused gate runs) stand in `.runs/author/`; they are ignored by git and kept as the evidence the orchestrator may read. No worktree, clone or other copy was made. The breaks of section "The failing run" were made in the worktree and undone before the commit.

## Unread material

none — every foundation entry the handoff names was read whole: decisions WAY-38, WAY-89, WAY-09, WAY-08, WAY-61, WAY-03, WAY-44, WAY-60, WAY-62, WAY-63, WAY-69, WAY-321, WAY-344, WAY-379, WAY-385, WAY-392, WAY-393, WAY-394, WAY-395, WAY-399, WAY-401 (WAY-328 withdrawn, Q1; WAY-385 was read to the end of its rationale and WAY-344 only to the *Scope*, the part that bears on where a script reads a file; WAY-395 to the end of its first *Verification* line, the rest being the recipe fields the guidelines copy); the invariants `python-version-declared`, `script-language`, `script-imports`, `element-directory-contents`, `cross-part-imports` and, of those whose *Part* reads `every` or names `part-map` or `elements-common`, `skill-entry-points`, `instruction-file-imports`, `record-copy-image-files`, `guidelines-file-place`, `ruff-blocking-rules` and `function-and-file-size`, plus lines 1-210 of the file; the facts `python-stdlib-modules`, `git-path-patterns`; the glossary terms `element`, `repository test`, `files test`, `git test`; the whole part map; `guidelines/coding.md` and `guidelines/testing.md`. The decisions WAY-44, WAY-60, WAY-61, WAY-62, WAY-63 and the others were read from heading to the next heading.

## Searches not found or unclear

- The task names WAY-328, withdrawn on this base (Q1 of the handoff); not looked up further.
- `guidelines/coding-<kind>.md`: I found no kind that matches a test file, so none was read.
- The task says git tracks only five kinds; it also tracks `.yml`, `.in`, `.txt` and `ruff.toml` (Q2 of the handoff), handled above.

## Choices, with the way rejected and the cost if wrong

1. The condition {merge-onto} in `element-directory-contents`: the repository test is skipped, with a reason that the run names, where no main branch exists; rejected: checking always (fails on a repository where the sentence is vacuously true) and failing where none exists (the same). Cost if wrong: on a checkout with no `origin/HEAD`, `main` or `master` the invariant gets no result (WAY-63) and the skip is named in the report; CI sets `origin/HEAD` in its workflow.
2. "Pointer" in `element-directory-contents` is the section `## Examples` of the template naming, in backticks, a `foundations/*.md` file that git tracks; rejected: any mention of `foundations/` in the template (the section `## Links` or a note would pass) and `examples.md` alone (the template of the environment facts has none and the task says that is how it stands). Cost if wrong: a template that points in other words (without a path in backticks) is reported and the author rewrites the pointer.
3. An element directory is every directory directly under `elements/` except `common`, with the five elements asserted present (subset), so that a sixth directory is checked and the test cannot quietly see none. Rejected: a fixed list of the five (a new element would pass unchecked) and a list of `elements/*` with `common` included (it holds no template and is the shared part). Cost if wrong: another shared directory under `elements/` would be reported until `SHARED` names it.
4. `python-version-declared` accepts `3.14` and `3.14.<patch>` in a single-line `.python-version` that git tracks; rejected: exactly `3.14` only. Cost if wrong: a patch-version pin passes, which the sentence ("declares Python 3.14") allows.
5. The version of the running interpreter is compared to `.python-version` by major and minor number; rejected: comparison with the literal 3.14 (the invariant `python-version-declared` holds that value, and Q2's answer names the declared version).
6. Expected values: the version `3.14` is a literal from the sentence of `python-version-declared`; the lists of kinds are the task's lists plus the four added kinds; the element names are those of the *Part* of the invariant, read as literals; no expected value comes from a computation of the code under test (`MAIN_BRANCHES` and `imports` are the definitions of {merge-onto} and of the reach, as `rules.md` and the invariant give them, not a result checked against itself).

## Problems observed, concerns

- Concern: a `.py` file that holds a script in another language (`#!/bin/sh` and shell text) passes `script-language`, since the test recognises a script by the kind of the file name, as the settlement chose; the reader of `script-imports` would report such a file as "cannot be read as Python" only when it fails to parse. Not fixed: the settlement (row 1) chose the list of kinds, and a parse check would be a new rule the task does not ask for.
- Concern: a file git tracks that the working tree lacks makes `outside_imports` report `cannot be read as Python`, as the neighbour test of `cross-part-imports` does; not changed.
- Observed, no cause verified: the full `gate/run_tests.py elements/common` takes about 135 seconds on this machine, longer than the two minutes a foreground call allows.
