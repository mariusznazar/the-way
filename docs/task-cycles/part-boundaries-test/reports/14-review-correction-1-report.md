FAIL 8cbcac0b8dab89fcd56257955bd6f5c62c1194ff

# Report 14 — review of correction 1, for the human's remarks

Range reviewed: `79bd480..8cbcac0b8dab89fcd56257955bd6f5c62c1194ff` (`git rev-parse HEAD` =
`8cbcac0b8dab89fcd56257955bd6f5c62c1194ff`), one commit `8cbcac0`; `git diff --stat fbea390 79bd480`
is empty, so the tree before the correction is the one I reviewed in report 08. Files:
`elements/part-map/test_cross_part_imports.py` (+421 −69), `foundations/invariants.md` (1 line),
`elements/invariants/examples.md` (1 line). Bounded by `reports/11-remarks-1.md`.

Counts: blocking 1 (Important), Minor 2, out of scope 0.

## Each remark

**Remark 1, M1 — made.** An absolute import, or a `-m`/`run_module` name, whose first name is not
in `sys.stdlib_module_names` and resolves to no tracked file is now a problem
(`elements/part-map/test_cross_part_imports.py:389-392`, called at :399, :413, :419); a relative
import that resolves to nothing is one too. My probe from report 04 is now the fixture
`test_name_the_check_does_not_see_fails` (:630-643). Mutation "unseen-silent" fails 3 tests.

**Remark 1, M2 — made.** Each branch I named has a fixture, and each mutation I ran in report 04
that survived is now killed (table under *Checks*): `extend`, whole `sys.path` assignment (with
`+=` in the same fixture), relative import, `__init__.py`, dotted prefixes, own directory, wrapped
marked sentence.

**Remark 2, the widening — made, with one gap (I1 below).** The sentence
(`foundations/invariants.md:310`) now counts "running it as a script with `runpy` or in a new
process of the running interpreter", keeps both exceptions and the direction fixed in report 08,
and the example line (`elements/invariants/examples.md:15-17`) says the test reads runs. The test
reads `runpy.run_path`/`run_module` (positional, keyword, alias, `from runpy import`) and command
lines of `sys.executable`; on the real tree it finds 30 runs, 6 of them into temporary directories,
none across parts, no problem (scratch `…\scratchpad\reviewer\runs_real.txt`), matching the
author's listing.

## Findings

### Important

**I1 — a command line of `sys.executable` whose script is joined on after the list is read as
running no file, and passes in silence.**

- Place: `elements/part-map/test_cross_part_imports.py:298-322` (`command_line`): when the
  elements after the interpreter are only options, or none, the loop ends without a target and
  without a problem; `command` (:279-282) reads only the list literal, so a script added by `+` or
  `.append` is never seen. The fixture `subprocess.run([sys.executable])` (:783) pins "no target,
  no problem" as intended.
- What is wrong: the remark asks that a new process of the running interpreter given a path counts
  as an import "and its test reads such runs"; the docstring (:19) promises "A use of
  `sys.executable` the check cannot read as a command line fails it" and (:26-27) "a check that
  quietly sees less would pass". Both are false for these forms, which are ordinary ways to build
  a command line (the tree already has `[sys.executable, "-B", RUNNER] + list(arguments)`,
  `gate/test_run_tests.py:55`, one argument away from it).
- Evidence: scratch probe
  `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\83b0c1f3-84b6-4cee-b776-f504fe498fa9\scratchpad\reviewer\gaps.py`,
  each line placed in `core/engine.py` of the test's own fixture repository, where `core` may not
  depend on `shell`:
  - `subprocess.run([sys.executable, '-B'] + [os.path.join(HERE, '..', 'shell', 'screen.py')])`
    → `([], [])`;
  - `subprocess.run([sys.executable] + [<same path>])` → `([], [])`;
  - `cmd = [sys.executable]` / `cmd.append(<same path>)` / `subprocess.run(cmd)` → `([], [])`.
  The same run written as one list is reported as forbidden (`test_each_form_of_a_run_is_seen`).
- Why Important: this is the requirement the remark adds, and the gap is of the kind remark 1
  (M1) asked to remove: the invariant's only test passes while seeing less. No instance on
  today's tree.
- Possible fix: a command line that ends with no target, no `-c`, no `-` and no `-m` fails as "runs
  a command line the check cannot read" (and the fixture at :783 moves to the failing cases), or a
  list of `sys.executable` that is an operand of `+` or a name later mutated fails the same way.

### Minor

**M1 — code given with `-c` is not read, so a run or import inside it passes unseen.**
`elements/part-map/test_cross_part_imports.py:312-313`. Probe (same `gaps.py`):
`subprocess.run([sys.executable, '-c', 'import runpy; runpy.run_path("shell/screen.py")'])` →
`([], [])`. The author names this limit (report 13, "Limits"); the code string is a constant the
check could parse with `ast` as it parses files. Minor: the only `-c` on the tree
(`project-level/test_plan_state_subprocesses_invariant.py:139`) runs code of its own part.

**M2 — two claimed branches still have no fixture with teeth.** Mutations on a copy outside the
tree survive with every test green: treating a run into a temporary directory like any other path
(`:420`, `elif target != TEMPORARY` → `elif True`), and allowing a path outside the root (`:373`,
`relative()` returning `../…`). The first is redundant today (a temporary path also falls out
through `relative()`); the second leaves the docstring's "a path outside the repository's root
… is no dependency" (:18) with no test.

## Declined to judge

- `importlib.import_module`, `__import__` and `exec` of a file's text — the remark names `runpy`
  and new processes of the interpreter; the sentence names neither.
- A file of another part copied into a temporary directory and run there — the sentence covers
  files git tracks, and the remark's "Python file of another part" is read the same way; the
  installation tests that run a temporary copy of the-way belong to `installation`, whose *Depends
  on* names most parts anyway.
- A `cwd=` given to the process (author's named limit) — a relative script path is then checked
  against the root and fails loudly (`runs `screen.py`, which is no Python file git tracks`), not
  silently.
- M3 and M4 of report 04 — not asked by the remarks.

## The author's question on *Derives from*

Keep `WAY-299 · WAY-44`; no finding. The template (`elements/invariants/template.md:126-131`) asks
for an outside source in *Derives from* only for an entry that no decision entry carries. WAY-299
carries this invariant and leaves to the product's test what counts as an import in its own
language; counting a run as one is the-way's choice for its own entry. Its meaning is not from a
row, so the human accepts it at the merge through the request's section for the human's decisions
(WAY-114): the orchestrator's to write, outside this diff.

## Checks run

- `git rev-parse HEAD` → `8cbcac0…`, exit 0; `git diff --stat fbea390 79bd480` → empty, exit 0;
  `git diff 79bd480..8cbcac0` read whole.
- `python -B gate/run_tests.py elements/part-map` → exit 0, 28 tests OK.
- `python -B elements/common/foundation_check.py` → exit 0, `0 errors`.
- No line over 100 characters in the test file or `elements/invariants/examples.md` (awk).
- Mutation run
  `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\83b0c1f3-84b6-4cee-b776-f504fe498fa9\scratchpad\reviewer\mutate2.py`
  on a copy outside the tree (the real-tree test pointed at the worktree), each
  `python -B -m unittest test_cross_part_imports`: unmutated → exit 0; killed (exit 1):
  relative-as-absolute, no-extend, no-assign-whole, no-prefixes, no-own-dir, no-init-candidate,
  marked-first-line-only, unseen-silent, marked-either-order, runs-dropped, run-problems-dropped,
  dash-c-as-path, helper-for-everyone; survived (exit 0): temporary-as-no-file-dropped,
  outside-root-allowed (M2).
- Probe `…\scratchpad\reviewer\gaps.py` → results under I1 and M1.
- Listing `…\scratchpad\reviewer\runs_real.py` → 30 runs on the real tree, no unknown run.
- `git status --short` in the worktree afterwards → empty.
- Not run: the whole gate — the orchestrator's.

## Reaches beyond the dispatch

- `elements/invariants/template.md` "Links" — for the author's question on *Derives from*.
- `git grep sys.executable` over the tree and `foundations/part_map.md` `installation` — to judge
  the forms the tree uses and the temporary-copy case.

## Searches not found or unclear

- Not found: a fixture for a run of a path outside the root that is not a temporary directory (M2).
- Unclear: whether "running it as a script … in a new process of the running interpreter" covers
  code a `-c` argument runs; I read it as covering a file that code runs, hence M1, but kept it
  Minor.
