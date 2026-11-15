# Executor report — slice 15 (the test of the rule of a shared module)

**Status:** done

**Commits:** `8dce794` — "Test that importing the fingerprint module runs nothing" (on branch `task/the-way-coding-and-testing-guidelines`, base `878c88d`).

**Check result:** all focused checks passed; none failed or was skipped.

**Report path:** `.runs\task-cycles\the-way-coding-and-testing-guidelines\reports\executor-15-report.md`

## Files changed

- `relation-model/test_fingerprint.py`: +30 / -0 (committed in `8dce794`).
  - Added imports `subprocess` and `tempfile`.
  - Added constant `IMPORT_TIMEOUT = 30` with a comment.
  - Added test method `test_importing_the_module_runs_nothing` with the comment line `# invariant: shared-module-import-runs-nothing`.
- `relation-model/fingerprint.py`: changed for a moment twice to see the test fail, then restored with `git checkout --`. Net change zero; `git diff -- relation-model/fingerprint.py` is empty.

## What the test does

It starts a new interpreter (`sys.executable`, flags `-I -B`) with `-c` code that puts the module's directory first on `sys.path` and imports `fingerprint`. Its stdin is a pipe the test does not write to and keeps open until the import ends. Its stdout and stderr are temporary files. The test asserts: exit code 0, empty stdout, empty stderr.

If the import reads its stdin, it blocks on the open pipe. The test then kills the process after `IMPORT_TIMEOUT` and fails with "importing the module waits for its input".

## Checks run

Each check is listed with its command and exit code.

1. Baseline before any edit: `python -B relation-model/test_fingerprint.py` — exit 0, 12 tests OK.
2. Breaks, failing runs (both seen failing for the expected reason):
   - `print("imported")` added at module level after `LENGTH = 8`. Command: `python -B relation-model/test_fingerprint.py Fingerprint.test_importing_the_module_runs_nothing` — exit 1. Failure: `AssertionError: b'imported\r\n' != b''` at the output assertion.
   - `sys.stdin.read()` added at the same place. Same command — exit 1, after 30.0 s. Failure: `AssertionError: importing the module waits for its input` (the timeout branch).
3. Restore: `git checkout -- relation-model/fingerprint.py`, then `git diff -- relation-model/fingerprint.py | wc -l` — exit 0, output 0 lines.
4. Passing run after restore: `python -B relation-model/test_fingerprint.py` — exit 0, 13 tests OK (0.05 s).
5. Focused directory run: `python -B gate/run_tests.py relation-model` — exit 0, 13 tests OK.
6. Linter: `<main checkout>/.runs/quality-venv/Scripts/ruff.exe check --config ruff.toml --no-cache --ignore-noqa relation-model/test_fingerprint.py` — exit 0, "All checks passed!".
7. Foundation check: `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0 (stdout discarded).
8. Tree after commit: `git status --short` — empty. `git diff 878c88d --stat` — `relation-model/test_fingerprint.py | 30 +++`.
9. Commit author check (`git log --format='%h %ae'`): the private address is used, as the git rule says for repositories on this account.

Not run: the product's full gate (`python -B gate/run_tests.py` without a directory), which the handoff forbids (WAY-160).

## Own-work check (section 3 of make-change)

- **Requirement most likely not met:** the test must actually run a new interpreter process and must detect reads of the input, not only output. A test that only checks output would pass a module that reads stdin at import.
- **Check written:** the stdin-read break above, which makes the test wait and then fail through the timeout branch.
- **What it showed:** the timeout branch fails as intended (exit 1, reason "waits for its input").
- **Mutation thinking:** a missing `-I` or a wrong path in `sys.argv[1]` would make the import fail with exit code 1 and an error on stderr — caught by the exit-code and stderr assertions. A module that writes to stderr only is caught by the stderr assertion. A module whose import writes nothing and reads nothing passes, which is the intended behaviour.
- **Not checked by a break:** a module that makes a child process at import. The invariant says nothing about that beyond output and input; the test would catch it only if the child wrote output or hung on input. Noted, not added.

## Choices made

- **Reading of "with its input closed".** The slice says the process imports the module "with its input closed". Literally closed stdin (EOF) cannot detect a read: a read of EOF returns empty and the test would pass. So I kept the input as an open, empty pipe that the test closes only after the import ends. A read blocks and shows as a timeout. Way rejected: `stdin=subprocess.DEVNULL` (reads succeed silently, so reads are undetected). Cost if wrong: if the human meant literal EOF, the test checks less about reads; the output and exit-code checks still hold.
- **Timeout of 30 s.** Way rejected: no timeout (a reading import would hang the whole test run). Cost if wrong: an extremely slow machine could take over 30 s on a tiny module and fail falsely; negligible for this module.
- **Temporary files for stdout and stderr** instead of pipes. Way rejected: `stdout=PIPE` with `wait()` (risk of deadlock when the child writes more than a pipe buffer). Cost: none measurable.
- **Interpreter flags `-I -B`.** `-I` ignores environment variables and the current directory on `sys.path`, so the test imports the file under test, not another `fingerprint` module. The test's own `sys.dont_write_bytecode` line and the `-B` flag keep bytecode out of the tree.

No adaptation of section 4 (plan and code disagreed nowhere). No changed invariant test. No small mismatch found in the handoff's values.

## Questions

None.

## Weakest point and its check

The stdin-hold choice: the test detects reads by a timeout, so its verdict on reads depends on the timeout and on how the pipe behaves on Windows. Check made: the stdin-read break above, run on this machine — it failed through the timeout branch, after 30 s, with exit code 1. The passing run came back in about 0.05 s with the module restored.

## Unread material

- `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md`: read in the handoff's ranges plus a few lines around each — lines 30–39 (items 4–13), 134–148 (question 13 and its neighbouring answer 14), and 530–533 (row 17 to 20). The rest of the task was not read.
- `foundations/part_map.md`: read lines 27–34 as named, plus lines 1–5 (the head of the file), which the handoff did not name.
- `.runs/task-cycles/the-way-coding-and-testing-guidelines/plan.md`: read the *Choices* section (lines 1003–1020) and the *Orchestrator's additions* section (lines 1021–1041), which the handoff's last paragraph makes binding. Did not read the rest of the plan (the other slices' sections, *Foundation entries*, *Coverage*).
- `ruff.toml`: read whole (not named by the handoff; needed for the linter check).
- `task-cycle/change/SKILL.md` and `task-cycle/change/slice.md`: read whole (method files).
- `a file of the author's private notes`: read (delivered by the environment's rules hook, and it governs commits).
- Foundation entries read whole: WAY-08 (`foundations/decisions.md` 1750–1779), WAY-198 (8517–8548), WAY-386 to WAY-391 (9925–10058, all six), invariants `script-language`, `script-imports`, `script-subprocesses`, `fingerprint-definition` (read as neighbour), `map-reference-target` (neighbour), `test-method-citation`, `cross-part-imports`, `shared-module-import-runs-nothing` (E27). The boundary lines before the entries (decisions 1780, 8549) were checked to be the next headings.
- Not read: the guideline files of the-way for coding and testing (`guidelines/coding*.md`, `guidelines/testing.md`); the handoff names none of them for this slice. `foundations/decisions.md` WAY-392 and beyond, the other invariants, the other slices.

## Searches not found or unclear

- Unclear: "with its input closed" (see Choices). Resolved as described; flagged for the orchestrator.
- Not searched: any other test in the-way that starts a new interpreter process, to compare a house style for `subprocess` calls. Not needed for the slice.
- Nothing else was looked for and not found.

## Working copies

None made. No worktree, clone, script or prepared input was created in `.runs/executor-15/` or anywhere else. The temporary files used by the test are created by the test itself and removed on exit by `tempfile`.
