# Report 13 — correction 1, for the human's remarks

**Status:** done

## Commit

- `8cbcac0` feat: cross-part-imports counts running another part's file as a script as importing it

It sits on `task/part-boundaries-test`, on top of `79bd480`. I did not touch `docs/task-cycles/`.

## Files changed (`git diff --numstat 79bd480..HEAD`)

| File | + | − |
|---|---|---|
| `elements/part-map/test_cross_part_imports.py` | 421 | 69 |
| `foundations/invariants.md` (sentence of `cross-part-imports`, rewritten in place) | 1 | 1 |
| `elements/invariants/examples.md` (its example line) | 1 | 1 |

All three files keep LF line endings (`git ls-files --eol`: `i/lf w/lf`). No line of the test file is longer than 100 characters.

## Each remark, as made, and how

Mariusz's words, quoted in `reports/11-remarks-1.md`: "a ja bym to jeszcze dociągnął w ramach tego tak samo poszerzenie zdania niezmiennika i testu". The remarks file reads them as two items.

### Remark 1 — fix the review's Minor findings M1 and M2 in this request

**M1 — a name the check could not find was dropped in silence.** Before, an import whose name matched no file the check could see counted as no dependency, and nothing was reported. Now, an import whose first name is not in `sys.stdlib_module_names` and resolves to no tracked file is reported as a problem:

`<file>:<line>: imports `<name>`, which is neither a module of the standard library nor a file the check sees`

- The rule also covers a relative import that resolves to nothing, shown as `.name`.
- It also covers `runpy.run_module` and `-m <module>` with a name that resolves to nothing.
- The reviewer's example is now a fixture: `core/lib.py: import helper`, where `helper` exists only in `shell/`, and a test of `shell` puts `core` on `sys.path`. Test: `test_name_the_check_does_not_see_fails`.
- On the real tree, every import that is not from the standard library resolves; the test on the real tree reports no problems.

**M2 — branches the docstring claims had no fixture.** Each branch the reviewer named now has one:

| Branch | Fixture |
|---|---|
| `sys.path.extend([…])` | `core/f.py` in `test_import_through_each_form_of_sys_path_is_seen` |
| `sys.path = […]` | `core/g.py`, same test |
| `sys.path += […]` | `core/h.py`, same test |
| relative import against the package | `test_relative_import_resolves_against_the_package`: `app/core/view.py: from ..shell import screen`. From the root, the same name would reach `shell/screen.py`, so a check that resolves it as an absolute import gives a different answer. |
| the `__init__.py` candidate | `test_package_and_each_prefix_of_a_dotted_name_are_seen`: `import shell` → `shell/__init__.py` |
| dotted prefixes | same test: `import shell.screen` → both `shell/__init__.py` and `shell/screen.py` |
| the file's own directory | `test_import_through_the_own_directory_is_seen`: `core/engine.py: import rules`. Without the own directory, `rules` would be a name the check does not see (M1). |
| a marked sentence wrapped over lines | `test_marked_sentence_wrapped_over_lines_is_read` |

### Remark 2 — widen the sentence of the invariant and its test

**The rule now.** Running a Python file of another part as a script counts as importing it. The test reads the run in each of these forms:

- `runpy.run_path(<path>)`, by position or as `path_name=`, under the name `runpy`, an alias of it, or `from runpy import run_path [as …]`;
- `runpy.run_module(<name>)`, by position or as `mod_name=`, in the same three ways;
- a command line of the running interpreter, `sys.executable`. It can be written out as a list or tuple, `[sys.executable, …]`, `+` other arguments included. It can also be the arguments of any call: `subprocess.*`, `os.execv`, `os.execl` or a local wrapper such as the installation tests' `command(sys.executable, …)`.

**How a command line is read.**
- Options are skipped; `-W` and `-X` take the next argument as their value.
- `-c` and `-` run code and stdin, so they run no file.
- `-m <module>` and `-m<module>` run a module; the module is resolved as an import is.
- Anything else is the script's path, worked out with the existing evaluator.
- A path to a directory runs that directory's `__main__.py`.

**What fails the test**, following the principle that a check that quietly sees less would pass:
- a run target the check cannot work out;
- a command line with `*args` before the script;
- a run of a path in the repository that is not a tracked Python file;
- any use of `sys.executable` the check cannot read as a command line.

**What is no dependency:**
- a path in a directory made at run time by `tempfile` (`mkdtemp`, `TemporaryDirectory`, `gettempdir`, and `.name` of one);
- a path outside the repository's root;
- code given with `-c`;
- a module of the standard library.

**The evaluator now also reads:**
- `Path.with_name()`;
- `self.<name>` attributes the file assigns;
- a name assigned more than once, where every assignment gives the same value.

**The real tree** (scratch listing `…\scratchpad\author\c_runs.txt`):
- 30 runs. 25 run a file of their own part, among them `relation-model/test_fingerprint.py:108` and `gate/run_tests.py:96`, which runs its own file. Five, in `installation/test_install.py`, run a temporary copy of the-way.
- `project-level/test_plan_state_subprocesses_invariant.py:82` stands inside a string literal and is not counted.
- `:139` passes code with `-c`, so it runs no file.
- No run is a problem.
- The real-tree test still passes. The only imports between parts are the two seen before: `project-level/readiness_check.py:46` → `relation-model/fingerprint.py`, and the test itself → `elements/common/foundation_check.py`.

**The sentence, rewritten in place.** The identifier is kept, as `elements/invariants/skill/write.md` gives for a changed entry.

Wording on `{fork-point}`, the base `dfd50e5`: the entry did not exist. At the reviewed `fbea390` it read:

> No Python file git tracks imports, by an `import` or `from … import` statement and through a directory it adds to `sys.path` as well, a Python file git tracks of another part that the *Depends on* of its own part does not name, unless the importing file is a test, named `test_*.py`, and the imported file belongs to a part of test helpers, or an invariant "the part `<X>` does not depend on `<Y>`" reads `Violated: yes`, where `<X>` is the part of the importing file and `<Y>` the part of the imported one.

New wording:

> No Python file git tracks imports a Python file git tracks of another part that the *Depends on* of its own part does not name — by an `import` or `from … import` statement, through a directory it adds to `sys.path` as well, or by running it as a script with `runpy` or in a new process of the running interpreter — unless the importing file is a test, named `test_*.py`, and the imported file belongs to a part of test helpers, or an invariant "the part `<X>` does not depend on `<Y>`" reads `Violated: yes`, where `<X>` is the part of the importing file and `<Y>` the part of the imported one.

**The test that cites it, checked against the new wording.** `test_the_way_imports_only_from_allowed_parts` is the only test citing the invariant, and it now reads imports and runs. The exceptions apply to runs as to imports. Shown by `test_run_a_marked_invariant_names_passes`, plus the shared exception code that every run goes through.

The other fields are unchanged: *Method* `test`, *Rests on* `git-path-patterns`, *Derives from* `WAY-299 · WAY-44`, *Part* `every`, *Violated* `no`.

**The example line** in `elements/invariants/examples.md` now ends "kept by a test that reads the map, the imports of the product's language and the runs of one file as a script by another".

### WAY-299, the template and the part-map sentence: not changed

The handoff asked whether these still agree with the wider invariant.

- **WAY-299** has a product hold one invariant that a file imports only allowed files, its test reading "the imports of the product's own languages". What counts as an import in a language is the product's to state. The-way's invariant counts a run as an import, which keeps WAY-299's sentence true for the-way: it is still the one invariant, with the same exceptions. Its *Verification* names `cross-part-imports`, and its complies/violates pair says nothing about runs. Widening WAY-299 would widen the duty of products, which the remarks do not ask for.
- **The part-map template, "Allowed dependencies"** states the same duty in the same words, and names `cross-part-imports` as the-way's own. No sentence of it says a run is no import.
- **The sentence of the part `part-map`** ("the test that holds the imports of the-way's code to the dependencies it allows") still holds, since runs count as imports.
- **A search** of `foundations/`, the template, `elements/invariants/` and `task-cycle/skill/` for runpy, "as a script", "is no import" and "process of its own" found no text saying a run is no import. The only hit beyond the new sentence was an unrelated sentence of the decision log (line 1313), which uses "of its own" in another meaning.

## Meaning of each entry changed

| Entry | Mark | Meaning (English) | Meaning (Polish) |
|---|---|---|---|
| `cross-part-imports` (rewritten in place) | the cycle's (by Mariusz's remark) | In the-way no Python file imports a file of a part its own part's *Depends on* does not name — by an import statement, through `sys.path` too, or by running it as a script with `runpy` or in a new process of the running interpreter — except a test importing a part of test helpers and an import a marked "X does not depend on Y" invariant covers, X being the importing file's part. | W the way żaden plik Pythona nie importuje pliku części, której *Depends on* jego części nie dopuszcza — instrukcją import, także przez `sys.path`, ani uruchamiając go jako skrypt przez `runpy` lub w nowym procesie bieżącego interpretera — poza importem z testu do części pomocników testów i importem objętym oznaczonym niezmiennikiem „X nie zależy od Y”, gdzie X to część pliku importującego. |

## Checks (command → exit code)

All commands run from the worktree root.

1. **Mutations of the checker.** Script `…\scratchpad\author\author_mutations.py`, output in `…\scratchpad\author\c_mutations.txt`. It applied 29 mutations one at a time, each to the worktree file, and ran `python -B gate/run_tests.py elements/part-map` after each. It restored the file at the end; `git diff` afterwards showed only the intended change.

   **Every mutation gave exit 1, and no mutation survived.** Each mutation, with the tests that failed:
   - `extend`, `whole-sys-path-assign` → `test_import_through_each_form_of_sys_path_is_seen`
   - `relative-as-absolute` → `test_relative_import_resolves_against_the_package`
   - `no-init-candidate`, `no-prefixes` → `test_package_and_each_prefix_of_a_dotted_name_are_seen`
   - `no-own-dir` → `test_import_through_the_own_directory_is_seen` (and the real tree)
   - `marked-first-line` → `test_marked_sentence_wrapped_over_lines_is_read`
   - `m1-unseen-silent` → `test_name_the_check_does_not_see_fails` (and two more)
   - `runpy-ignored`, `runpy-keyword`, `from-runpy-import` → run tests
   - `list-command-unread`, `positional-command-unread` → `test_each_form_of_a_run_is_seen`
   - `dash-m`, `dash-m-joined`, `valued-option`, `dash-c`, `exec-skip` → run tests
   - `temporary-calls`, `temporary-name` → `test_run_of_a_file_in_a_temporary_directory_is_no_dependency` (and the real tree)
   - `self-attributes`, `same-value-names` → `test_run_through_names_the_file_assigns_is_seen` (and the real tree)
   - `with-name` → `test_each_form_of_a_run_is_seen` (and the real tree)
   - `main-of-directory` → `test_run_of_a_directory_runs_its_main`
   - `executable-elsewhere`, `untracked-run-target`, `module-run-unseen`, `starred` → `test_run_the_check_cannot_work_out_fails`
   - `run-edge-dropped` → three run tests
2. **Passing run.** `python -B gate/run_tests.py elements/part-map` → **exit 0**, 28 tests, OK. Run after the mutations, before the commit; the commit holds the same file.
3. **Foundation check.** `python -B elements/common/foundation_check.py` → **exit 0**, `0 errors`.
4. **`elements/common`.** `python -B gate/run_tests.py elements/common` → **exit 0**, 109 tests. Its test runs the foundation check on the-way, which reads the changed invariants file.
5. **Real-tree listings, scratch scripts outside the repository:**
   - `…\author\author_edges.py` → exit 0: 38 files, 44 edges, no problems, two edges between parts, both allowed;
   - `…\author\author_runs.py` → exit 0: 30 runs, none that the check cannot work out.
6. **Not run:** the whole gate. The handoff keeps it for the orchestrator.

## Limits of the widened check (named)

- **Names and assignments.** Names are worked out from their plain assignments anywhere in the file, `name = …` and `self.name = …`, regardless of scope. Parameters, and names bound by unpacking, `for` or `with`, are not read. A run whose path rests only on such a name fails as one the check cannot work out. On the-way, `installation/test_install.py`'s `later` is bound by unpacking in some methods; it works out through its one plain assignment, which gives the same temporary path.
- **Relative paths.** A relative script path is taken against the repository's root, the working directory of the gate and the scripts. A `cwd=` given to the process is not read.
- **Code given with `-c` is not parsed.** A file that such code runs, given as an argument (`project-level/test_plan_state_subprocesses_invariant.py:139` runs `plan_state.py` of its own part this way), is not seen.
- **Not read:** `importlib.import_module`, `__import__` and `exec` of a file's text. The remark names `runpy` and new processes of the interpreter; the sentence names import statements and runs as a script.
- **The interpreter is recognised only under the name `sys.executable`.** Every other use of it fails the test. A process started with another program, `"python"` say, is not read; the invariant `script-subprocesses` keeps such starts out of the-way's scripts.

## Own-work check

**The requirement most likely missed:** that the widened test still passes on the-way's real tree while seeing every run there, so that it neither fails on today's code nor passes by seeing nothing.
- Check: the listing of runs (check 5) against `git grep -n "sys.executable\|runpy\.\|run_module\|run_path" -- '*.py'`, the same search the handoff names.
- Result: every hit in a code position appears in the listing: 30 runs, the `-c` run left out by design. `project-level/test_plan_state_subprocesses_invariant.py:82` is not listed because it is inside a string. The real-tree test passes.

**A second requirement:** that each form the docstring claims has a fixture with teeth. Check 1 shows it: all 29 mutations are caught, among them each M2 branch and each new run form.

## Reaches beyond the dispatch

- `reports/04-review-report.md` — read M1 and M2 whole for their places and the reviewer's suggested fix, as the handoff points to it.
- `installation/test_install.py`, `installation/test_*_installation.py`, `project-level/test_plan_state*.py` — read where they run Python files, to make the evaluator work out their targets: `later`, `self.product`, `self.temporary`, `READER`, `INSTALL`.

## Searches not found or unclear

- **Unclear: does the widened sentence still derive from WAY-299 alone?** *Derives from* stays `WAY-299 · WAY-44`. The runs clause comes from Mariusz's remark, which no decision of the log carries in so many words. I read it as WAY-299 leaving to the product what counts as an import in its language. I did not quote the remark in *Derives from* as a source outside the log: it has no address a reader could open. The review may take this up.
- **Not found:** any decision or template sentence that says a run is no import, so nothing needed correcting beside the invariant.
