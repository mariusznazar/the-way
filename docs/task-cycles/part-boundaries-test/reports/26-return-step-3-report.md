# Report 26 — the return step, again after correction 2

**Status:** done, no correction needed

**Commits:** none. The head stays at `7aad48b`, and the worktree is clean.

This step was repeated only for what remarks 2 touched, as `task-cycle/skill/correction.md` gives.

## What was compared with the code at `7aad48b`

| Entry | What I compared | Result |
|---|---|---|
| `cross-part-imports`, sentence as rewritten | Each form the sentence names has a reader in the test: <ul><li>`import` / `from … import` statements, and import functions (`importlib.import_module`, `__import__`), through `sys.path` too;</li><li>runs with `runpy`, `exec` (a file's text) and a new process of `sys.executable`;</li><li>code run as a string (`-c`, `exec`, `eval`, `compile`).</li></ul> The exceptions for test helpers and marked invariants apply to all of them alike. Where the test cannot work out a form, it fails, so it is stricter than the sentence, never looser. *Method* `test`, *Part* `every`, *Rests on* `git-path-patterns`, *Derives from* `WAY-299 · WAY-44` and *Violated* `no` all still hold: the test passes on the tree. | matches |
| Its example line in `elements/invariants/examples.md` | "kept by a test that reads the map, the imports of the product's language and the runs of one file as a script by another". This still describes the test at the level of a summary: import functions are imports, and a file run through `exec` is a run. | matches, no edit |
| WAY-44, re-wrapped | Words unchanged (correction 2's script asserted it, and the diff shows no changed word). The rule "a file … is an error of the check of the foundation, unless the map lists that file as left out on purpose" now agrees with the test, which lets such a Python file pass. | matches |
| WAY-299 | Names the products' duty in terms of imports. The-way's invariant counts these forms as imports. Nothing in WAY-299 says an import function, `exec` or code run as a string is no import. | matches, no edit |
| Part-map template, "Allowed dependencies" and "Files left out on purpose" | The duty is stated in WAY-299's words. The template keeps "The list is the only exception to 'every tracked file has a part'", and the test now takes the list as `foundation_check.py` does. | matches, no edit |
| `foundations/part_map.md`, "Files left out on purpose" | It lists `README.md` alone. The test reads the table with `foundation_check`'s own `table` and `LEFT_OUT`; read so, the list gives `['README.md']`. It is no Python file, so the test is unaffected, and the reading matches `foundation_check.py`, which takes `cells[0]` of the same rows. | matches |
| `script-imports` | The test imports `ast`, `os`, `re`, `subprocess`, `sys`, `tempfile` and `unittest`, and `foundation_check` (a tracked file). The `importlib`, `runpy`, `exec` and `-c` lines are fixture text inside string literals. | matches |
| `script-subprocesses` | The test starts only git: `git init` and `git add` in its fixture repositories, and `git ls-files` and `check-attr` through `foundation_check.git`. | matches |

**What the test sees on the real tree.**
- 38 Python files, 45 edges, no problems, no marked pairs.
- Two edges cross parts, both allowed: the test → `elements/common/foundation_check.py`, and `project-level/readiness_check.py:46` → `relation-model/fingerprint.py`.
- 31 runs, among them the `-c` code at `project-level/test_plan_state_subprocesses_invariant.py:139`, and none that the check cannot read.

## What the return step writes

- **Environment facts:** none. `importlib`, `exec`, `eval`, `compile` and `-c` belong to the language at the declared version, as reasoned for imports in report 10.
- **Glossary:** none.
- **Rows of *Settlements to record*:** none missed.
- **Choices that bind after the merge:** none to write as a separate entry. The forms of import that remarks 2 add stand in the invariant's sentence. The test's own choices stay rows of the questions table:
  - code given as a string is read down to five levels;
  - `-c` code is read from the root, with `sys.argv` from the command line;
  - code given to `exec` is read with the directories of the file that runs it.

## Checks (command → exit code)

All commands run from the worktree root.

- `python -B gate/run_tests.py elements/part-map` → **exit 0** (39 tests, OK).
- `python -B elements/common/foundation_check.py` → **exit 0** (`0 errors`).
- `python -B …\scratchpad\author\author_self.py elements/part-map/test_cross_part_imports.py …\author\rs3_self.txt` → **exit 0**. This lists the test's own imports and the processes it starts.
- `python -B …\scratchpad\author\author_edges.py <worktree> …\author\rs3_edges.txt` → **exit 0** (output above).
- `python -B …\scratchpad\author\author_runs2.py <worktree> …\author\rs3_runs.txt` → **exit 0**: 31 runs, 0 `UNKNOWN`.
- `python -B -c "…foundation_check.table(read('.', PART_MAP), LEFT_OUT)…"` → **exit 0**, `['README.md']`.
- **Not run:** the whole gate. It passed on `7aad48b` (756 tests), and the handoff keeps it for the orchestrator.

## Own-work check

**The requirement most likely missed:** that the test's new reading of "Files left out on purpose" differs from `foundation_check.py`'s on the real map, so the two would disagree about which files have a part.
- Check: the table read with `foundation_check`'s own helpers, against `foundation_check.check_files`, which takes `cells[0]` of the same rows; and the test on the real tree.
- Result: both give `README.md`, and the test passes with no problems.

## Searches not found or unclear

- **Unclear, carried from reports 13, 20 and 23:** *Derives from* stays `WAY-299 · WAY-44`, while the forms of import come from Mariusz's remarks. No correction was made.
- The Minor findings of review 24 are not this step's to fix; they go to the request. They are:
  - `compile` alone counted as running code;
  - a left-out file bridging two parts unseen;
  - starred unpacking of `sys.argv`.
