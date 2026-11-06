# Report 23 — correction 2, for the human's remarks

**Status:** done

## Commits

- `022fb7b` feat: cross-part-imports reads code given with -c, import functions and exec, and files left out on purpose
- `7aad48b` docs: re-wrap the allowed-dependencies paragraph of the part map template and WAY-44 at 100 characters

Both sit on `task/part-boundaries-test`, on top of `5a84a30`. I did not touch `docs/task-cycles/`.

## Files changed (`git diff --numstat 5a84a30..HEAD`)

| File | + | − |
|---|---|---|
| `elements/part-map/test_cross_part_imports.py` | 450 | 135 |
| `foundations/invariants.md` (sentence of `cross-part-imports`, in place) | 1 | 1 |
| `elements/part-map/template.md` (re-wrap only) | 5 | 5 |
| `foundations/decisions.md` (WAY-44, re-wrap only) | 6 | 7 |

All four files keep LF line endings (`git ls-files --eol`: `i/lf w/lf`). No line of the test file is longer than 100 characters.

## Each remark, as made, and how

Mariusz's words, quoted in `reports/21-remarks-2.md`: "nie lubię dodatkowych drobnych zadań / drobne rzeczy powinny być robione przy okazji, żeby potem nie zostawały na dodatkowe zadania i dodatkowe sesje / dociągnij e drobne luki w teście i przy okazji można też te M3 i M4 dorzucić".

### Remark 1 — close the small gaps of the test

**Code given with `-c` (review 14, M1).**
- The constant is parsed with `ast` as the code of a file. Its imports and runs are resolved from the repository's root, and they count at the line of the command.
- `-c<code>` written in one piece is read too.
- The code's `sys.argv` is taken from the command line. A name the code assigns from `sys.argv[<i>]`, or by unpacking `sys.argv[<i>:]`, takes the value of that argument, as the evaluator works it out in the file that runs the command.
- Fails as "runs code the check cannot read":
  - code the check cannot work out (`os.environ[…]`);
  - `-c` with nothing after it;
  - code that does not parse.
- Code on standard input (`-`) now fails as "runs a command line the check cannot read". It passed before.
- On the real tree, the one `-c` run, `project-level/test_plan_state_subprocesses_invariant.py:139`, is now read whole. Its code assigns `reader, … = sys.argv[1:]`, adds `Path(reader).parent` to `sys.path` and runs `reader`. The check works these out as `project-level/` and `project-level/plan_state.py`, of the file's own part: one more edge, 44 → 45, and the tree still passes.

**Python's import functions.**
- `importlib.import_module(<name>[, package])` and `__import__(<name>)` are read as imports when the check can work out the name. The name may be a constant, a name the file assigns, or the keywords `name=` and `package=`.
- They are read under `importlib.`, `builtins.`, an alias of the module, or `from importlib import … as …`.
- A relative `import_module` name is resolved against `package`.
- Fails as "imports a module the check cannot work out":
  - a name the check cannot work out;
  - a relative name with no package;
  - `__import__` with a `level` other than 0.
- A name of the standard library is no dependency. Any other name that resolves to no file fails as an import does (M1 of review 04).

**`exec`, `eval` and `compile`.**
- A constant string, or bytes, given to them, directly or through a name the file assigns, is parsed as code: `exec` and `compile(..., 'exec')` as a file, `eval` and `compile(..., 'eval')` as an expression.
- It is read with the directories of the file that runs it, and counts at the line of the call.
- `exec(compile(...))` is read once, at `compile`.
- The text of a file — `open(<path>).read()`, `<path>.read_text()` or `.read_bytes()` — given to them counts as running that file.
- Fails as "runs code the check cannot read":
  - code the check cannot work out (`os.environ[…]`, `sys.stdin.read()`);
  - a `compile` mode it cannot work out;
  - code that does not parse.
- A path it cannot work out fails as "runs a file the check cannot work out".
- Code given as a string can hold more code given as a string. It is read down to five levels; a sixth fails as "runs code given as a string nested too deep for the check".

**The two branches of review 14, M2, now have teeth.**
- **A run into a temporary directory.** `TEMPORARY` is now an object, not a path-like string, so a step that took it for a path fails with a `TypeError`. The mutation `elif what is not TEMPORARY` → `elif True` now fails `test_run_of_a_file_in_a_temporary_directory_is_no_dependency` and the real-tree test.
- **A path outside the root.** New fixture `test_run_of_a_file_outside_the_root_is_no_dependency` (`runpy.run_path(os.path.join(HERE, '..', '..', 'outside', 'screen.py'))`). The mutation of `relative()` returning `../…` now fails it.

**The principle is kept:** every new form the check cannot work out fails the test; none passes by seeing less.

### Remark 2 — M3 (review 04): a Python file left out on purpose

`parts()` now reads the table "Files left out on purpose" as `foundation_check.py` does. It uses `table` and `LEFT_OUT`, imported from `foundation_check`. A file on the list that no part claims is no failure, and the test does not read it: it has no part, so its imports cross no boundary the map draws. An import of such a file is no dependency either.

The pattern extraction stays a copy, kept in step with `foundation_check.check_files`. Its docstring now says so. `elements-common` offers the parsing helpers but no assignment function, and the handoff asked to reuse only what `elements-common` already offers.

Fixture: `test_python_file_left_out_on_purpose_is_no_failure`.

### Remark 3 — M4 (review 04): re-wrap at 100 characters

- **`elements/part-map/template.md`**, the paragraph of "Allowed dependencies" that held the 122-character line: lines 94–98, re-wrapped at 100.
- **`foundations/decisions.md`**, WAY-44's binding paragraph from "their own; the files that serve the tests…" to its end: 7 lines to 6. The short line "another. For a file that" is gone.

The re-wrap script asserted that the sequence of words is identical before and after, and `git diff --word-diff=porcelain` shows no changed word.

## The sentence of `cross-part-imports`, rewritten in place

As `elements/invariants/skill/write.md` gives for a changed entry.

Wording on `{fork-point}`: the entry did not exist on the base `dfd50e5`. As reviewed at `ef083d1` it read:

> No Python file git tracks imports a Python file git tracks of another part that the *Depends on* of its own part does not name — by an `import` or `from … import` statement, through a directory it adds to `sys.path` as well, or by running it as a script with `runpy` or in a new process of the running interpreter — unless …

New wording:

> No Python file git tracks imports a Python file git tracks of another part that the *Depends on* of its own part does not name — by an `import` or `from … import` statement or an import function, through a directory it adds to `sys.path` as well, or by running it as a script with `runpy`, `exec` or a new process of the running interpreter, the code it runs as a string included — unless the importing file is a test, named `test_*.py`, and the imported file belongs to a part of test helpers, or an invariant "the part `<X>` does not depend on `<Y>`" reads `Violated: yes`, where `<X>` is the part of the importing file and `<Y>` the part of the imported one.

The test that cites it, `test_the_way_imports_only_from_allowed_parts`, reads each form the new wording names. It passes on the tree.

The other fields are unchanged: *Method* `test`, *Rests on* `git-path-patterns`, *Derives from* `WAY-299 · WAY-44`, *Part* `every`, *Violated* `no`.

The example line in `elements/invariants/examples.md` is unchanged. It names "the imports of the product's language and the runs of one file as a script by another", and still holds.

**WAY-299, the template's words and the part-map sentence:** not changed. They name imports, and the-way's invariant counts these forms as imports, as reasoned in report 13. Nothing in them says an import function or `exec` is no import.

## Meaning of each entry changed

| Entry | Mark | Meaning (English) | Meaning (Polish) |
|---|---|---|---|
| `cross-part-imports` (rewritten in place) | the cycle's (by Mariusz's remark) | In the-way no Python file imports a file of a part its own part's *Depends on* does not name — by an import statement or an import function, through `sys.path` too, or by running it as a script with `runpy`, `exec` or a new process of the interpreter, code it runs as a string included — except a test importing a part of test helpers and an import a marked "X does not depend on Y" invariant covers, X being the importing file's part. | W the way żaden plik Pythona nie importuje pliku części, której *Depends on* jego części nie dopuszcza — instrukcją lub funkcją importu, także przez `sys.path`, ani uruchamiając go jako skrypt przez `runpy`, `exec` lub w nowym procesie interpretera, łącznie z kodem uruchamianym jako napis — poza importem z testu do części pomocników testów i importem objętym oznaczonym niezmiennikiem „X nie zależy od Y”, gdzie X to część pliku importującego. |
| WAY-44 | — | Re-wrap only; no word changed, so its meaning is unchanged. | — |

## Checks (command → exit code)

All commands run from the worktree root.

1. **Mutations of the new branches.** Script `…\scratchpad\author\author_mutations3.py`, output in `…\author\c2_mutations.txt`: 28 mutations, each applied to the worktree file and followed by `python -B gate/run_tests.py elements/part-map`. **Each gave exit 1; none survived.** Each mutation, with the tests that failed:
   - `-c` unread → the `-c` fixtures and the real tree
   - `-c` written in one piece unread → `test_each_form_of_code_given_to_the_interpreter_is_read`
   - `sys.argv[<i>]` dropped; `sys.argv[<i>:]` dropped (the latter also the real tree)
   - `-c` code read from another directory than the root
   - code that does not parse passes silently
   - `-c` with no code passes silently
   - import functions unread
   - relative `import_module` name
   - the `package=` keyword
   - the `level` of `__import__`
   - a module name the check cannot work out passes silently
   - `from importlib import … as` dropped; `import importlib as` dropped
   - `exec` unread
   - `compile` read twice
   - `open(…).read()` unread; `.read_text()` unread
   - names not followed to their code
   - bytes code dropped
   - the `eval` mode; the `compile` mode
   - code the check cannot read passes silently
   - standard input passes
   - a temporary path taken for a path (also the real tree)
   - a path outside the root allowed
   - a file left out on purpose fails
   - unbounded nesting
2. **The earlier mutation sets, rerun on the new code.**
   - `…\author\author_mutations.py` and `…\author\author_mutations2.py`, outputs `…\author\c2_old1.txt` and `c2_old2.txt`: of 34, 21 still applied and **all 21 gave exit 1**.
   - The 13 that no longer matched, because their code moved into the class `Reading`, I ported to the new code. 11 are in `…\author\author_mutations4.py`, output `…\author\c2_ported.txt`, and **all 11 gave exit 1**: `relative-as-absolute`, `no-own-dir`, `runpy-ignored`, `runpy-keyword`, `temporary-name`, `same-value-names`, `main-of-directory`, `untracked-run-target`, `module-run-unseen`, `starred`, `run-edge-dropped`.
   - The other two, `from-runpy-import` and `dash-c`, are covered by `from-import-alias` and `dash-c-unread` of check 1.
   - Each script restored the file. `git diff --stat` after each run showed only the intended changes.
3. **Passing run.** `python -B gate/run_tests.py elements/part-map` → **exit 0**, 39 tests, OK. Run after all the mutation runs; the commit holds the same file.
4. **Foundation check.** `python -B elements/common/foundation_check.py` → **exit 0**, `0 errors`.
5. **`elements/common`.** `python -B gate/run_tests.py elements/common` → **exit 0**, 109 tests. It runs the foundation check on the-way, which reads the changed decisions and invariants.
6. **Real-tree listings.**
   - `…\author\author_edges.py` → exit 0: 38 files, 45 edges, no problems, the same two edges between parts, both allowed.
   - `…\author\author_runs2.py` → exit 0: 31 runs, among them the `-c` code at `:139`, and 0 that the check cannot work out.
7. **Not run:** the whole gate, as the handoff says.

## Limits that stay

- **Names and assignments.** Names are worked out from plain assignments in the file, regardless of scope. Parameters, and names bound by unpacking, `for` or `with`, are not read. The exception is unpacking `sys.argv` in `-c` code. A run or import that rests only on such a name fails the test.
- **Relative paths.** A relative path is taken against the repository's root. A `cwd=` given to a process is not read.
- **The interpreter and the functions are recognised under the names written** (`sys.executable`, `runpy.`, `importlib.`, `builtins.`, the bare built-ins, and the aliases the file makes by `import … as` and `from … import … as`). A function reached in another way — assigned to a variable, or `getattr(importlib, 'import_module')` — is not read. Another use of `sys.executable` fails the test.
- **Code given as a string is read down to five levels.** Deeper code fails the test.
- **The code `exec` runs is read with the directories of the file that runs it**, not with globals the call passes.
- **Other mechanisms that load code** — `importlib.util.spec_from_file_location`, `zipimport`, `pkgutil` and the loaders of `importlib.machinery` — are not read. The remarks name `-c`, the import functions and `exec`, `eval` and `compile`. The-way's tree uses none of these.

## Own-work check

**The requirement most likely missed:** that reading `-c` code fails the-way's own tree. The one `-c` run's code adds to `sys.path`, and runs, a path it takes from `sys.argv`, which an unread `sys.argv` would leave unknown.
- Check: the real-tree listing (check 6), and the test on the real tree (check 3).
- Result: the code is read, its `sys.argv[1:]` unpacking worked out to `project-level/plan_state.py`, no problem reported, and the test passes. The mutation that drops the unpacking ("`sys.argv[<i>:]` dropped" in check 1) fails the real-tree test, which shows the tree depends on it.

**A second requirement:** that the code moved into the class `Reading` keeps the teeth it had. Check 2 shows it: 32 of the earlier 34 mutations rerun or ported, all caught. The other two are covered by check 1.

## Reaches beyond the dispatch

- `reports/04-review-report.md` (M3, M4) and `reports/14-review-correction-1-report.md` (M1, M2) — read for their places and the reviewers' words, as the remarks file names them.
- `project-level/test_plan_state_subprocesses_invariant.py:19-32` — read for the `-c` code's use of `sys.argv`, which the check must work out on the real tree.

## Searches not found or unclear

- **Not found:** `exec`, `eval`, `compile`, `importlib` or `__import__` in any tracked Python file outside the test (`git grep`). The new readers have no instance on the real tree; their fixtures alone give them teeth.
- **Unclear, carried from reports 13 and 20:** *Derives from* stays `WAY-299 · WAY-44` for a sentence whose forms of import come from Mariusz's remarks. No decision carries them in so many words.
