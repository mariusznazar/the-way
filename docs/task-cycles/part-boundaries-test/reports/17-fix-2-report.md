# Report 17 — fix of the review's findings on correction 1

**Status:** done

## Commit

- `ef083d1` fix: cross-part-imports reads a command line joined with + and fails one with no script
  written out

It sits on `task/part-boundaries-test`, on top of `8cbcac0`. I did not touch `docs/task-cycles/`.

## File changed (`git diff --numstat 8cbcac0..HEAD`)

| File | + | − |
|---|---|---|
| `elements/part-map/test_cross_part_imports.py` | 36 | 10 |

The file keeps LF line endings (`git ls-files --eol`: `i/lf w/lf`). No line is longer than 100 characters.

## I1 — fixed

**The finding holds.** Some command lines of `sys.executable` passed the test as running no file:
- one whose script is joined on with `+` (`[sys.executable, '-B'] + [path]`);
- one built as `[sys.executable]` and then grown with `.append`;
- the bare `[sys.executable]`.

The fixture `subprocess.run([sys.executable])` pinned that as intended. Both of the reviewer's suggested ways are now made.

**1. A list joined with `+` is read whole.** `command()` reads a `+` whose left side is a command line of the interpreter.
- The left side can itself be such a `+`.
- The elements of the right side are added when they are written out as a list or tuple. Otherwise the right side stands as an element the check cannot read.
- The inner list of such a `+` is read only through the `+`, never on its own (the `joined` set in `runs()`).

So `[sys.executable, '-B'] + [path]` and `([sys.executable] + ['-B']) + [path, '--apply']` are read as runs of `path`.

**2. A command line with nothing written out fails.** Two cases now fail as "runs a command line the check cannot read":
- a command line that ends with no script, no `-c`, no `-` and no `-m`;
- one that reaches an element not written out before its script, such as `+ sys.argv[1:]`.

This covers `[sys.executable]`, `cmd = [sys.executable]; cmd.append(…)`, and `command(sys.executable, '-B')`.

The docstring now says so: "written out as a list, a list joined with `+` to more elements, or the arguments of a call", and "a command line whose script, code or module is not written out where the check reads it — joined on later, or by `+` of what is no list" fails.

**Fixtures.**
- `test_each_form_of_a_run_is_seen` gains two forms, each reported as the forbidden import `core/engine.py` → `shell/screen.py`:
  - `[sys.executable, '-B'] + [<path>]`
  - `([sys.executable] + ['-B']) + [<path>, '--apply']`
- `test_run_the_check_cannot_work_out_fails` gains four lines, each reported as `core/engine.py:7: runs a command line the check cannot read`:
  - `subprocess.run([sys.executable])` (moved from the cases that run no file)
  - `subprocess.run([sys.executable, '-B'] + sys.argv[1:])`
  - `cmd = [sys.executable]; cmd.append(<path>); subprocess.run(cmd)`
  - `command(sys.executable, '-B')`

**The real tree is unchanged.** It still has 30 runs and none that the check cannot read. The one joined form, `[sys.executable, "-B", RUNNER] + list(arguments)` at `gate/test_run_tests.py:55`, names `RUNNER` before the joined part, so it reads as before.

## Checks (command → exit code)

All commands run from the worktree root.

1. **Mutations of the fix.** Script `…\scratchpad\author\author_mutations2.py`, output in `…\scratchpad\author\f2_mutations.txt`. Each mutation was applied to the worktree file, followed by `python -B gate/run_tests.py elements/part-map`. The file was restored at the end; `git diff --stat` then showed only the fix. Each mutation gave **exit 1**:
   - command line ending with no target passes silently → `test_run_the_check_cannot_work_out_fails`
   - right side of `+` not read → `test_each_form_of_a_run_is_seen`
   - `+` not read as a command line → `test_each_form_of_a_run_is_seen`
   - inner list also read on its own → `test_each_form_of_a_run_is_seen`, `test_run_the_check_cannot_work_out_fails`
   - an element not written out not treated as unreadable → `test_run_the_check_cannot_work_out_fails`
2. **Passing run.** `python -B gate/run_tests.py elements/part-map` → **exit 0**, 28 tests, OK. This includes `test_the_way_imports_only_from_allowed_parts` on the-way's tree.
3. **Foundation check.** `python -B elements/common/foundation_check.py` → **exit 0**, `0 errors`.
4. **Real-tree listing of runs.** `python -B …\scratchpad\author\author_runs.py <worktree> …\scratchpad\author\f2_runs.txt` → **exit 0**: 30 runs, no `UNKNOWN`.
5. **Not run:** the whole gate. One is running in the worktree on `8cbcac0`, as the handoff says.

## Own-work check

**The requirement most likely missed:** that the fix makes the-way's own tree fail on a command line it now reads differently.
- Check: the listing of runs (check 4), and the test on the real tree (check 2).
- Result: no run that the check cannot work out, and the test passes. The only `+` form on the tree has its script before the joined part.

**A second requirement:** that a `+` is not read twice. Without the `joined` set, the inner list `[sys.executable, '-B']` would also be read alone, end with no target, and fail.
- Check: mutation "inner list also read on its own" (check 1).
- Result: it fails two tests.

## Reaches beyond the dispatch

None. I did not read `reports/14-review-correction-1-report.md`, because the findings file quotes I1 whole.

## Searches not found or unclear

- **Unclear: a stale mutation in the earlier set.** The earlier suite, `…\author\author_mutations.py`, holds a mutation `starred` that matched the old line `if isinstance(element, ast.Starred):`. That line now reads `if element is None or isinstance(element, ast.Starred):`, so `starred` would no longer apply. The new mutation "an element not written out not treated as unreadable" covers the changed line. I did not rerun the earlier suite of 29: the handoff asks for the affected checks, and one gate already runs in the worktree.
- The review's Minor findings (M1 `-c` code, M2 two branches without teeth) were not mine to fix; they go to the request.
