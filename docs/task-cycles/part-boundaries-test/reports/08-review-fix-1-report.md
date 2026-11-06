PASS fbea3903ab27e1f508b743065dc23b9da8b90828

# Report 08 — review of the fix of findings 1

Range reviewed: `b4a55092d8710ff59ec0110b2038f32ff5705ad2..fbea3903ab27e1f508b743065dc23b9da8b90828`
(`git rev-parse HEAD` = `fbea3903ab27e1f508b743065dc23b9da8b90828`), one commit `fbea390`, two files:
`foundations/invariants.md` (1 line), `elements/part-map/test_cross_part_imports.py` (+11).
Bounded by `reports/05-findings-1.md`, which holds I1 only.

Counts: blocking 0, Minor 0, out of scope 0.

## Findings of the findings file

**I1 — fixed.** `foundations/invariants.md:310` now reads "…or an invariant "the part `<X>` does
not depend on `<Y>`" reads `Violated: yes`, where `<X>` is the part of the importing file and `<Y>`
the part of the imported one." The placeholders are bound and the direction matches row 3 of the
task's *Settlements to record* ("importu objętego niezmiennikiem „część X nie zależy od Y”"),
WAY-299 (`foundations/decisions.md:9107`), the template (`elements/part-map/template.md:98`) and the
check `(part, other) in marked` (`elements/part-map/test_cross_part_imports.py:274`). Nothing
else in the tree still states the exception without a direction (`git grep "naming the two
parts"` → no match). Not contested by the author.

## The fix diff itself

- The new test `test_marked_invariant_of_the_other_direction_lets_no_import_pass`
  (`elements/part-map/test_cross_part_imports.py:454-463`) asserts a real result: a reversed marked
  invariant ("The part `shell` does not depend on `core`.", `Violated: yes`) leaves the import
  `core/engine.py` → `shell/screen.py` forbidden. Its `.replace` does take effect: had it not, the
  fixture would equal the marked case of the test above, where the import passes, and the new test
  would fail, but it passes.
- It fails when the behaviour breaks: my own mutation (check accepting either order), on a copy
  outside the tree, fails exactly this test.
- The changed sentence keeps the rest of the entry as it was; the fields are unchanged; the entry
  stays one line, as the file's other entries are.
- Nothing new found in the fix diff.

## Declined to judge

- The Minor findings M1–M4 of `reports/04-review-report.md` — not in the findings file; they go to
  the request (WAY-161).

## Checks run

- `git rev-parse HEAD` → `fbea3903…`, exit 0; `git diff b4a5509..fbea390` read whole.
- `python -B gate/run_tests.py elements/part-map` → exit 0, 13 tests OK.
- `python -B elements/common/foundation_check.py` → exit 0, `0 errors`.
- `git grep -n "naming the two parts"` → exit 1 (no match).
- Mutation on a copy in
  `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\83b0c1f3-84b6-4cee-b776-f504fe498fa9\scratchpad\reviewer\elements\part-map\test_cross_part_imports.py`
  (`(part, other) in marked` → `((part, other) in marked or (other, part) in marked)`, the test on
  the-way's tree pointed at the worktree): `python -B -m unittest test_cross_part_imports` → exit 1,
  one failure, `test_marked_invariant_of_the_other_direction_lets_no_import_pass`.
- `git status --short` in the worktree afterwards → empty.
- Not run: the whole gate — reserved for the orchestrator.

## Reaches beyond the dispatch

- `task-cycle/review/fix.md`, as the method gives for a fix. No foundation entry beyond those the
  finding quotes.

## Searches not found or unclear

- Unclear, now settled: the author's report (07, "Searches not found or unclear") notes that it
  shares a scratch directory with the reviewer. My earlier `mutate.py` and `mut\` there were mine;
  this review's scratch files sit in `…\scratchpad\reviewer\` only, as the orchestrator asked.
