PASS 7aad48b78acd8ba2dabed0c15a09dff9f2da562b

# Report 24 — review of correction 2, for the human's remarks

Range reviewed: `5a84a30..7aad48b78acd8ba2dabed0c15a09dff9f2da562b` (`git rev-parse HEAD` =
`7aad48b78acd8ba2dabed0c15a09dff9f2da562b`), commits `022fb7b` (test, invariant) and `7aad48b`
(re-wrap). `git diff --stat 5a84a30 990950b` is empty, as the dispatch says. Files:
`elements/part-map/test_cross_part_imports.py` (+450 −135), `foundations/invariants.md` (1 line),
`elements/part-map/template.md` (re-wrap), `foundations/decisions.md` (WAY-44, re-wrap). Bounded by
`reports/21-remarks-2.md`.

Counts: blocking 0, Minor 3, out of scope 0.

## Each remark

**1a. Code given with `-c` — made.** The constant is parsed and read from the root, with `sys.argv`
taken from the command line (`elements/part-map/test_cross_part_imports.py:442-453`, `:201-218`,
`:618-635`); `-c<code>` and code from a name the file assigns are read; code the check cannot
read, `-c` with nothing after it and code that does not parse fail. On the real tree the one `-c`
run (`project-level/test_plan_state_subprocesses_invariant.py:139`) resolves to
`project-level/plan_state.py`, its own part, with no problem (scratch `dashc_real.py`).

**1b. `importlib.import_module` and `__import__` — made** (`:384-403`, `:481-487`): constant or
assigned names, `name=`/`package=` keywords, relative names against `package`, aliases, `level`
other than 0 failing; a standard-library name is no dependency, any other unresolved name fails.

**1c. `exec`, `eval`, `compile` — made** (`:405-426`, `:488-498`): string or bytes code parsed in
the mode given, `open(<path>).read()`, `.read_text()`, `.read_bytes()` counted as running the file,
`exec(compile(...))` read once, nesting bounded at five with a loud failure beyond.

**1d. The two branches of review 14, M2 — made.** `TEMPORARY` is now an object (`:75`), so taking
it for a path fails; new fixture `test_run_of_a_file_outside_the_root_is_no_dependency`
(`:1003-1006`). Both mutations that survived in review 14 are now killed (below).

**2. M3, files left out on purpose — made.** `parts()` reads the `Files left out on purpose` table
with `foundation_check`'s own `table` and `LEFT_OUT` (`:111`, `:132-133`); fixture
`test_python_file_left_out_on_purpose_is_no_failure` (`:1148-1156`).

**3. M4, re-wrap — made.** `elements/part-map/template.md:94-98` (lines 99, 98, 99, 99, 59
characters) and WAY-44 at `foundations/decisions.md:1079-1084` (100, 100, 93, 96, 98, 57); the
short line "another. For a file that" is gone. `git diff --word-diff=porcelain` over both files
shows no changed word.

The sentence of `cross-part-imports` (`foundations/invariants.md:310`) now names import functions,
`exec` and "the code it runs as a string included"; the direction of the marked exception from
report 08 stays. The only test citing it, on the real tree, passes and reads each form.

## Findings

### Minor

**M1 — `compile` alone counts as running code.** `:488-498` reads `compile(...)` wherever it
stands, and the fixture `compile(open(<screen>).read(), 'screen', mode='exec')` (`:1117`) pins it
as a forbidden import; scratch probe: `code = compile('import shell.screen', 'x', 'exec')` with no
`exec` → forbidden. `compile` runs nothing, so the test fails code the sentence (which names `exec`
and code "it runs") does not forbid, and the remark asked for `compile` "where they run code". The
error is on the strict side and loud; no instance on the tree.

**M2 — a file left out on purpose is a silent bridge between parts.** `check()` skips an import of
a left-out file (`:657-658`) and does not read the left-out file's own imports. Scratch probe: a
left-out `tools/build.py` that imports `shell/screen.py`, imported by `core/engine.py` → `([], [])`,
though `core` may not depend on `shell`. The sentence covers only files of a part, so this matches
it; the remark asked only that the left-out file not fail. Reporting an import *of* a left-out file
from a file of a part would close it.

**M3 — `sys.argv` unpacking with a starred target misplaces the names after it.** `from_argv`
(`:210-218`) skips a starred element but keeps counting positions, so in `a, *b, last =
sys.argv[1:]` `last` gets `argv[start + 2]` whatever `b` takes. Scratch probe: with one element
for `b` the result is right by chance; with none or two it is wrong (out of range → loud, or another
argument → a wrong path, which may be a tracked file of an allowed part). Rare; marking every name
after a starred one as unknown would make it loud.

## Declined to judge

- `importlib.util.spec_from_file_location`, `getattr(importlib, 'import_module')` and other loaders
  the author names as limits — probes give `([], [])`; the remarks name `-c`, the import functions
  and `exec`/`eval`/`compile`, and the sentence names no other loader.
- *Derives from* of `cross-part-imports` — as answered in report 14: keep `WAY-299 · WAY-44`; the
  widened meaning is accepted at the merge through the request's section for the human's
  decisions (WAY-114).

## Checks run

- `git rev-parse HEAD` → `7aad48b…`, exit 0; `git diff --stat 5a84a30 990950b` → empty, exit 0;
  `git diff 5a84a30..7aad48b` read whole; the test file read whole.
- `python -B gate/run_tests.py elements/part-map` → exit 0, 39 tests OK.
- `python -B elements/common/foundation_check.py` → exit 0, `0 errors`.
- `git diff --word-diff=porcelain 5a84a30..HEAD -- foundations/decisions.md elements/part-map/template.md`
  → no changed word; line lengths by `awk` as given under remark 3; no line over 100 in the test.
- Probes in
  `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\83b0c1f3-84b6-4cee-b776-f504fe498fa9\scratchpad\reviewer\`:
  `gaps3.py` (M1–M3 and the declined loaders), `dashc_real.py` (the real `-c` run) → exit 0.
- Mutations `…\scratchpad\reviewer\mutate4.py` on a copy outside the tree (real-tree test pointed
  at the worktree), each `python -B -m unittest test_cross_part_imports`, output
  `…\scratchpad\reviewer\mutate4.txt`: unmutated → exit 0; each of 13 mutations → exit 1, none survived: left-out
  table ignored, temporary taken for a path, path outside the root allowed (the two survivors of
  review 14), `-c` code unread, import functions unread, `exec`/`eval`/`compile` unread, unparsable
  code silent, nesting unbounded, `sys.argv` ignored (fails the real-tree test too), standard input
  passing, relative import as absolute, unresolved names silent, `.read_text()` unread.
- `git status --short` in the worktree afterwards → empty.
- Not run: the whole gate — the orchestrator's.

## Reaches beyond the dispatch

- `reports/04-review-report.md` and `reports/14-review-correction-1-report.md` — my own, for the
  places the remarks quote.

## Searches not found or unclear

- Unclear: whether "running it as a script with `runpy`, `exec` …" is meant to cover `eval` and
  `compile`, which the test reads but the sentence does not name; I judged it under M1.
