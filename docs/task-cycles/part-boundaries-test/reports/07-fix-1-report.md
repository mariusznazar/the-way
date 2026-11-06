# Report 07 — fix of the review's findings, round 1

**Status:** done

## Commit

- `fbea390` fix: cross-part-imports lets an import pass only by a marked invariant of its own direction

It sits on `task/part-boundaries-test`, on top of `b4a5509`.

## Files changed (`git diff --numstat b4a5509..HEAD`)

| File | + | − |
|---|---|---|
| `foundations/invariants.md` | 1 | 1 |
| `elements/part-map/test_cross_part_imports.py` | 11 | 0 |

Both files keep LF line endings (`git ls-files --eol`: `i/lf w/lf`).

## I1 — fixed

**The finding holds.** The invariant's sentence named the two parts of a marked invariant without a direction. The settlement it comes from keeps the direction: row 3 says "the import the invariant covers", meaning an import from X to Y. WAY-299, the template and the test keep it too.

**How it is fixed.** In `foundations/invariants.md`, the clause of `cross-part-imports` changed.

- Before: `or an invariant "the part `<X>` does not depend on `<Y>`" naming the two parts reads `Violated: yes`.`
- After: `or an invariant "the part `<X>` does not depend on `<Y>`" reads `Violated: yes`, where `<X>` is the part of the importing file and `<Y>` the part of the imported one.`

This is the reviewer's recommended wording. Its meaning now matches row 3, WAY-299 (`foundations/decisions.md`, "says part X depends on today"), the template ("says it depends on today") and the test's check `(part, other) in marked`.

**New test.** Before this fix, no test caught a check that accepted the pair in either order. I added `test_marked_invariant_of_the_other_direction_lets_no_import_pass` to `elements/part-map/test_cross_part_imports.py`. It builds a small repository where:
- the marked invariant is "The part `shell` does not depend on `core`." with `Violated: yes`;
- `core/engine.py` imports `shell/screen.py` through `sys.path`.

The test asserts that this import is still forbidden: `[("core/engine.py", 7, "shell/screen.py", "core", "shell")]`.

## Checks (command → exit code)

All commands run from the worktree root.

1. **Mutation, to see the new test fail.** I changed the check to accept either order: `(part, other) in marked` became `(part, other) in marked or (other, part) in marked`. Then `python -B gate/run_tests.py elements/part-map` → **exit 1**. The failing test was the new one: `test_marked_invariant_of_the_other_direction_lets_no_import_pass`. I restored the file from a copy; a grep for `(other, part) in marked` then found no match.
2. **Passing run.** `python -B gate/run_tests.py elements/part-map` → **exit 0**, 13 tests, OK.
3. **Foundation check.** `python -B elements/common/foundation_check.py` → **exit 0**, `0 errors`. This run was after the commit.
4. **Not run:** the whole gate. The handoff keeps that run for the orchestrator.

## Own-work check

**The requirement most likely missed:** that no other text in the change still states the exception without its direction.
- Check: `git grep -n "naming the two parts\|names the two parts"` over the whole tree.
- Result: no match.
- I also re-read the clauses in WAY-299, the template and the test that state this exception. Each already names X as the part that depends today, so none needed an edit.

**A second requirement:** that the new test fails for the expected reason. Shown in check 1: it fails on an assertion, and only under the order-blind mutation.

## Reaches beyond the dispatch

`reports/04-review-report.md` was named for context. I did not read it, because the findings file quotes the finding whole.

## Searches not found or unclear

**One unclear point: a shared scratch directory.**

What happened:
- My first mutation run used the helper script `mutate.py` in my scratch directory, `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\83b0c1f3-84b6-4cee-b776-f504fe498fa9\scratchpad\`.
- Another agent had replaced that script at 20:39 with its own suite of mutations, which works on a copy of the test, `mut\orig.py`. From its contents, this was most likely the reviewer.
- So that first run did not mutate the worktree, and its exit 0 shows nothing. I do not count it.
- The worktree file was never changed by it: `git diff` showed only my intended edit.
- I redid the mutation with a script under a different name, `author_mutate.py`. That run is check 1.

What it means for the cycle: the reviewer's agent and this agent appear to share one scratch directory. A later agent may again overwrite another's helper files there without any sign.

## Remarks not mine to fix

The findings file names only I1. The reviewer's Minor findings go to the request; I made no change for them.
