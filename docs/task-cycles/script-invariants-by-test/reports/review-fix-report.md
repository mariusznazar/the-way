PASS 540aed04f5a3fd981b8c8b13addd0121ca2a3ff3

# Review of the fix of the Minor findings — script-invariants-by-test

Range of the fix: `4bc1667c` to `540aed04`. In the worktree, `git rev-parse HEAD` gives
`540aed04f5a3fd981b8c8b13addd0121ca2a3ff3`, which is the head I was given. The fix is one commit:
- `elements/part-map/test_script_invariants.py` moved to `agent-instructions/test_script_invariants.py`
  (76% similar).
- `elements/common/test_element_directory_contents.py` changed.
- Diff size: +76 / -31.

The findings file holds the four Minor findings M1 to M4 and no blocking finding. The fix brings no new
Critical or Important finding, so this review passes. It adds one new Minor finding, N1.

## Findings of the findings file

- **M1: fixed.** `.yml` has left `SUFFIXES`. It now passes only through
  `PLACES = ((".github/workflows/", ".yml"),)` (`agent-instructions/test_script_invariants.py:58-61`),
  which `possible_scripts` reads (`:78-82`). The comment beside it gives the reason: CI configuration,
  whose commands `ci-checking-commands` keeps. The reach of the entry now matches that reason.
  Evidence: in a worktree of the head I tracked a root `tools_deploy.yml` holding the same playbook as
  before. `python -B -m unittest discover -s agent-instructions -p test_script_invariants.py -k test_every_file_git_tracks`
  gave exit 1 with `AssertionError: Lists differ: [] != ['tools_deploy.yml']`; on `4bc1667c` the same
  case gave exit 0. The new test `test_a_configuration_file_outside_the_place_of_its_kind_is_reported`
  checks the reach permanently.
- **M2: fixed.**
  - The test of a name that cannot be worked out now asserts one report at `a.py:2:`, not the reader's
    wording (`:237-239`).
  - The six-forms test asserts `yaml` without the backticks of the message.
  - `missing()` returns pairs `(directory, what)`. The five `Missing` tests assert the pairs, so
    rewording a message breaks none of them. The sentence now stands only as the failure message of the
    repository test, where no assertion depends on it.
  - Comments now name the source of each value: at `:149-151`, `:199-200` and `:204-205`, in the
    docstring of `Missing`, and in the docstring of `MergeOntoExists`.
  - No assertion was weakened. Each still checks which directory lacks which thing, and which file and
    line hold an import.
- **M3: fixed, by moving the file.**
  - The tests now stand in `agent-instructions`. WAY-38 and WAY-89 both name that part in their
    *Scope*, so a later change to the file finds them with `--part agent-instructions`. That was the
    consequence M3 named.
  - The part's *Depends on* names `part-map`, so the import of `imports` through
    `sys.path.insert(0, os.path.join(HERE, "..", "elements", "part-map"))` is allowed.
  - The test of `cross-part-imports` passes with the file in its new place (part-map run below).
  - `git grep` at `540aed04` finds no tracked file that names the old path. Positive control: the same
    search finds `test_cross_part_imports` in the moved file.
- **M4: fixed.** A missing or empty `.python-version` now reaches `wrong_interpreter` as `None` and
  gets a message that names the file (`:94-100`, `:175-177`). Evidence: with `.python-version` moved
  away in the worktree of the head, `-k test_no_python_file_git_tracks` gave exit 1 and
  `AssertionError: .python-version is missing or holds no version, so the version of Python the tests have to run on is not declared (this run is on Python 3.14)`.

## New findings in the fix diff

### Critical / Important

none

### Minor

**N1 — `agent-instructions/test_script_invariants.py:26-28` — the docstring overstates the map's sentence (within the task).**
The docstring says the tests stand in `agent-instructions`, "whose map sentence covers the tests of the-way's own code rules".
The sentence in `foundations/part_map.md:161-166` names something else: instructions, skill entry points,
copies of agent types, hooks, configuration of agents' tools and of CI, and "the guidelines of the-way's
own code that those instructions point to". It names no tests of code rules. The part does hold such
tests already (`test_linter_invariant.py`, `test_size_invariant.py`), so the placement stands by
practice, not by the sentence. Consequence: a reader who trusts the docstring finds a different
sentence in the map. One of two fixes would settle it:
- the docstring says what the map does say, its *Depends on* and WAY-38/WAY-89's *Scope*; or
- the return step widens the sentence of `agent-instructions`.

Nothing in any test result depends on it.

## Whether the author's skipped checks needed repeating

Both were cheap, so I repeated them on the fixed head rather than rely on the unit tests:
- the break of `element-directory-contents` after `missing()` was rewritten;
- the run of the moved `script-imports` test on Python 3.12.

Both gave the failure expected, and every invariant test was seen failing again in its new form:
- `python-version-declared`: `.python-version` written as `3.13`. `-k PythonVersionDeclared` → exit 1,
  `.python-version declares '3.13', not Python 3.14`.
- `script-language`: the `tools_deploy.yml` case above → exit 1.
- `script-imports`: a tracked `agent-instructions/zz_break.py` with `import yaml` → exit 1, line
  `agent-instructions/zz_break.py:1: imports \`yaml\`…`.
  `py -3.12 -B -m unittest discover -s agent-instructions -p test_script_invariants.py -k test_no_python_file_git_tracks`
  → exit 1, with the message naming 3.14 and 3.12. The missing file case is under M4 above.
- `element-directory-contents`: `git mv elements/glossary/skill/SKILL.md …` → `-k test_every_element`
  exit 1, `[('elements/glossary', 'skill')]` with the explanatory message. The backticked pointer in
  `elements/environment-facts/template.md` replaced by words → exit 1,
  `[('elements/environment-facts', 'examples')]`.
- After every break was undone, the whole moved file passed: exit 0, OK.

## Checks run

- `python -B gate/run_tests.py elements/part-map`, in the reviewed worktree → exit 0, 40 tests, OK.
- `python -B gate/run_tests.py agent-instructions` → exit 0, 50 tests, `OK (expected failures=2)`. The
  two expected failures are the tests of `ruff-blocking-rules` and `function-and-file-size`, which read
  `Violated: yes`.
- `python -B gate/run_tests.py elements/common` → exit 0, 270 tests, OK.
- `python -B elements/common/foundation_check.py`, with no switch → exit 0, `0 errors`. The three moved
  tests still cite their invariants.
- Ruff 0.17.1 (`check --config ruff.toml --no-cache --ignore-noqa`) on the two changed files → exit 0,
  `All checks passed!`.
- `git status --short` of the reviewed worktree after the runs → clean.
- The size of functions and files does not apply: both changed files are test files, which stand
  outside the rule (WAY-385).

## Declined to judge

none

## Reaches beyond the dispatch

- `foundations/part_map.md`, the entry `agent-instructions` (already read whole in the review of the
  whole change): to judge the move of M3 and the docstring of N1.

## Working copies

- `.runs/review-whole/head` was a worktree of
  `540aed04`. Its breaks were made and undone there. It was removed with `git worktree remove --force`,
  then `git worktree prune`.
- The run outputs stood in `.runs/review-whole/`. That directory was removed. Nothing remains.

## Unread material

none. I read whole: the handoff, `task-cycle/review/fix.md`, the findings file, the author's fix report
and the fix diff. The selection of the review of the whole change still holds, since the fix adds no
part beyond `agent-instructions`, whose map entry I read whole.

## Searches not found or unclear

- `git grep` for the old path `elements/part-map/test_script_invariants` at `540aed04`: no match. That
  is the expected result. The positive control is described under M3.
