# Executor report — slice 13 — The test of imports between parts does not fail on `compile` that nothing runs

**Status:** done

**Worktree:** `the root of the task's worktree`, branch `task/scripts-after-foundation-review`

## Commits

- `ef0a5ae` — Read compile in the imports test only where exec or eval runs its result

## Files changed

- `elements/part-map/test_cross_part_imports.py` — 37 lines added, 9 removed

## What changed

- A `compile` call is now read as code only where `exec` or `eval` runs its result. A pre-pass in `Resolver.runs` collects the `compile` calls that `exec` or `eval` runs (the argument followed through one name, as `follow` does), and the walk reads a `compile` call only when it is in that set. `exec` and `eval` given file text still fail, and so does `exec(compile(open(...).read(), ...))` and `code = compile(...); exec(code)`.
- `compile` with a mode the check cannot read still fails, standing alone as well (choice 1 below).
- Changed text: the module docstring bullets that describe the reads, the `source` docstring ("Code given to `exec` or `eval`, or to `compile` whose result they run."), a comment above `BUILTINS`, and a docstring on `test_each_form_of_code_run_by_exec_eval_or_compile_is_read`.
- Test list `test_each_form_of_code_run_by_exec_eval_or_compile_is_read`: the standalone row `compile(open(...).read(), 'screen', mode='exec')` is replaced by `exec(compile(open(...).read(), 'screen', mode='exec'))` and `code = compile(open(...).read(), 'screen', mode='exec'); exec(code)`, both expected to fail.
- New test `Code.test_compile_standing_alone_is_no_dependency`: four forms (two file-text compiles with a keyword and a positional mode, an assigned compile, and a literal-text compile) expected to give no problems and no dependency.

## Checks

Test-first (red on the base, before the code change), command `python -B gate/run_tests.py elements/part-map`:
- Exit code 1. `Ran 40 tests`, `FAILED (failures=4)`. All four failures are subtests of `test_compile_standing_alone_is_no_dependency` (the four standalone forms). The list test with its new rows passed on the base, so those rows guard the existing behaviour. Log: `.runs/executor-13/red-run.txt`.

After the change (same command):
- Exit code 0, `Ran 40 tests`, `OK`. Logs: `.runs/executor-13/green-run.txt` (before one docstring line was shortened) and `.runs/executor-13/green-run-2.txt` (final), both under the worktree's `.runs/executor-13/`.
- Line-length check (awk, lines over 100 characters) in the changed file: no output.

Not run:
- The whole gate, by the handoff's instruction (WAY-160).

## Own-work check (section 3)

- Requirement: a `compile` whose result nothing runs is no dependency, while `exec`, `eval` and a `compile` run by `exec` or `eval` still fail on file text.
- Check: the test list rows for `exec(compile(...))` and the assigned `compile` followed by `exec(code)`, and the four new standalone subtests. Run as above.
- Result: all pass after the change; the standalone subtests fail on the base as expected.
- Not done: a deliberate mutation of the code (for example, removing the `run_results` gate) was not run. The four standalone subtests are what such a mutation would turn red, since they are red on the base for the same reason.

## Choices

1. A `compile` whose mode is not a literal (`compile('import json', 'x', MODE)`) still gives "runs code the check cannot read" even standing alone. The existing test row that holds this case stays unchanged. Rejected: passing every standalone `compile` regardless of mode. Cost if wrong: a standalone `compile` with a computed mode fails the check (conservative, not a quiet pass). The slice did not name this case.
2. The run set is a pre-pass over `exec`/`eval` calls, not a mark made while walking. Reason: `ast.walk` does not guarantee the `exec` call is visited before the `compile` call assigned to a name. Cost: a `compile` result that reaches `exec` through a call the check cannot follow (for example `exec(f(code))`) is not tied to the `compile` call; `exec(f(...))` itself still fails, because the argument is not readable, so this is not a quiet pass.
3. The module docstring's sentence on `compile` (the bullet on code given as a string) is reworded; the invariant sentence in `foundations/invariants.md` is not touched.

## Invariant test named (WAY-03)

This slice alters the invariant test of `cross-part-imports`, so the request names it:
- File: `elements/part-map/test_cross_part_imports.py`.
- The invariant's test function, `TheWay.test_the_way_imports_only_from_allowed_parts` (marked `# invariant: cross-part-imports`), is unchanged in its source. The check it runs now reads `compile` differently: a `compile` whose result nothing runs is no dependency. The-way's own tree passes this check (part of the 40 tests above).
- Changed: the list `test_each_form_of_code_run_by_exec_eval_or_compile_is_read` (one standalone row replaced by two rows that still fail), its docstring, and the new `Code.test_compile_standing_alone_is_no_dependency`.
- The invariant sentence ("by running it as a script with `runpy`, `exec` or a new process") is not changed.

## Reaches beyond the handoff (section 1)

- `foundations/decisions.md` WAY-03 and WAY-44, `foundations/invariants.md` cross-part-imports, `foundations/part_map.md` part-map, `.runs/task-cycles/scripts-after-foundation-review/task.md` lines 41 and 127: read as named.
- `task-cycle/change/SKILL.md` and `task-cycle/change/slice.md`: read whole, as named.
- Global rule files, delivered by a hook on the first matching action (not named by the handoff): `a rule or note file of the author's, outside the repository` and `a rule or note file of the author's, outside the repository`. Read as delivered; the git rule was followed for the commit (English message, `-m`, explicit path). A one-off `python -c` was blocked once by the hook and not run.
- `gate/run_tests.py`: run, not read.
- Commit author: the commit carries `the author's e-mail address`, which the git rule says a repo on the `mariusznazar` account gets. Noted, not changed.

## Unread material

- `.runs/task-cycles/scripts-after-foundation-review/plan.md` slice 13: read only as copied in the handoff (the plan itself not opened, as the handoff says).
- Everything else named by the handoff was read whole, except the two task lines, which were read as single lines.

## Searches not found or unclear

- None.

## Working copies

- None made. The run logs in `.runs/executor-13/` (`red-run.txt`, `green-run.txt`, `green-run-2.txt`) are logs, not working copies, and stay in the executor's own directory. No worktree was created, so nothing was removed.
