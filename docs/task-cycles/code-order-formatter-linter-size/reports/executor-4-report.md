# Report — executor-4, slice 4 (the full check of the foundation in the gate)

**Status:** done

## Commits and files

Range `037f6c93..HEAD`, one commit:

- `2620dcc3` Run the whole check of the foundation in the gate under own-foundation-check-report

| File | Added | Removed |
|---|---|---|
| `elements/common/test_foundation_check.py` | 17 | 3 |
| `README.md` | 2 | 2 |

`elements/common/foundation_check.py` is unchanged.

What changed:

- `test_the_way_foundation_check_reports_no_error` is new, under the comment "the-way's own foundation", after
  the narrow test. It runs `foundation_check.py` on `THE_WAY` with no switch and no base argument (the
  script finds the base in git as before), and asserts exit code 0. It cites F3 by the line
  `# invariant: own-foundation-check-report`. The comment at the expected value names its source:
  the "Exit code:" paragraph at the head of `foundation_check.py`.
- The narrow test `test_the_way_foundation_passes` is untouched, still cited by `map-reference-target` and
  `test-method-citation`. The block comment above `OWN_FINDINGS` said the other findings "depend on the
  branch a clone calls its main one"; I reworded it to say they concern the foundation beyond the two
  invariants and that the whole check stands in the new test (WAY-08; cause 23). The "branch name" cause
  (cause 5) is dropped from the comment since the checks below show no such dependence.
- `README.md`: the paragraph that opens "Two invariants of the foundation of the-way" now says the whole
  check runs in the gate too, under `own-foundation-check-report`, beside the two invariants of the narrow
  test.

## Checks (command, exit code)

All commands from the worktree root. `<ruff>` = `the Ruff of the quality environment of the main checkout`.

| Check | Result |
|---|---|
| `python -B elements/common/foundation_check.py` before the test existed | exit 1: `foundations/invariants.md:180: own-foundation-check-report reads test and no test cites it` (the one error the new citation resolves) |
| `python -B gate/run_tests.py elements/common` with the new test (working tree = commit content) | exit 0, 271 tests OK (178 s) |
| `python -B elements/common/foundation_check.py` | exit 0, `0 errors` |
| `<ruff> format --check --config ruff.toml elements/common/test_foundation_check.py` | exit 0 |
| `<ruff> check --config ruff.toml --ignore-noqa elements/common/test_foundation_check.py` | exit 0 |
| **Seen failing (WAY-08):** line `A reference to a decision the log does not hold: WAY-9999.` appended to the tracked `README.md` (uncommitted), then `python -B gate/run_tests.py elements/common` | exit 1, `FAIL: test_the_way_foundation_check_reports_no_error`, `AssertionError: 1 != 0 : README.md:240: \`WAY-9999\` names no decision of the log`, 1 failure of 271. Only this test failed; the narrow test stayed green. `git checkout -- README.md` restored it; `git status` clean afterwards. |
| Clone of the task branch, only main branch a local `main` (at `d69fb20b`, merge base known), `origin` remote removed, `refs/remotes/origin/HEAD` absent (checked: absent), then `python -B gate/run_tests.py elements/common` | exit 0, 271 tests OK; `foundation_check.py` in it: exit 0, `0 errors`, no listed line |
| Shallow clone (`git clone --depth 1 file:///...`, `is-shallow-repository` true), `python -B gate/run_tests.py elements/common` | exit 0, 271 tests, OK (skipped=1); `foundation_check.py` in it: exit 0, `0 errors`, one listed line "the commit the branch left the main branch from is not known" |

Logs of the three gate runs: `reports/executor-4-broken-run.log`, `reports/executor-4-clone-main-run.log`,
`reports/executor-4-clone-shallow-run.log` (in `.runs/task-cycles/code-order-formatter-linter-size/reports/`).

The one skip in the shallow clone is `test_element_directory_contents...test_every_element_directory_holds_a_template_examples_or_a_pointer_and_a_skill`
("no main branch exists, so {merge-onto} does not"); it is an existing test, not part of this slice.

## Own-work check (WAY-164)

- Requirement most likely not met: acceptance criterion "the foundation test passes in a local clone whose
  main branch is called `main`, and fails when the foundation holds a reference to a decision that does not
  exist".
- Check: ran the gate in a clone with only a local `main` and no `origin/HEAD`, and in a shallow clone;
  ran the gate with `WAY-9999` in a tracked file.
- Showed: passes in both clones, fails once with the exact reference named in the message.
- Weakest point checked: the clone with a known base (`main` at `d69fb20b`), where `check_held` can
  report a decision added or changed by this branch that nothing holds. The run gave no error and no listed
  line, so every decision this branch changed (WAY-382, WAY-385) is held. A different base (a `main` far
  behind) was not tried: with a base that is much older, decisions added since by other tasks and held by
  nothing would be an error, which is the check working, not a dependence on the branch name.

Mutations in the head: asserting `returncode in (0, 1)` would pass a broken foundation (the failing run
above proves the assertion is exact); dropping the citation line makes the script itself report the
uncited invariant (exit 1, seen before the test was written); passing `--skip-test-citations` would
hide the uncited-invariant report (the test passes no switch).

## Trust boundaries

None of the named files was touched.

## Choices

- Wrote a second subprocess call, not a shared helper with the narrow test, so the narrow test and its two
  citations stay byte-for-byte as they were. Rejected: a shared helper (touches a test two other
  invariants cite). Cost if wrong: six duplicated lines.
- Left the shallow-clone skip alone: not this slice's.

## Reaches beyond the handoff

None.

## Unread material

- `.runs/.../task.md`: read lines 30-109 (the named passages are inside).
- The foundation entries named by range (WAY-08, WAY-03, WAY-61, WAY-321, `map-reference-target`,
  `test-method-citation`, `own-foundation-check-report`, part map `elements-common` and
  `foundation-check-command`, glossary `repository test`, `rules.md` `{fork-point}`): each read whole.
- `foundation_check.py`: read whole. `guidelines/testing.md`, `guidelines/coding.md`: whole.
- `test_foundation_check.py`: read lines 1-1291 and 2215-2281 only; the middle (tests of the script on
  made-up products) was not needed for the change and I changed no line in it.

## Searches not found or unclear

none

## Working copies

- `.runs/executor-4/clone-main/` (local clone with only local `main`) and `.runs/executor-4/clone-shallow/`
  (shallow clone): both removed (`rm -rf`; the listing of `.runs/executor-4/` afterwards shows only the
  three `.log` files, which I copied into `reports/` and left in place too). No worktree made, so
  `git worktree remove`/`prune` was not needed. Nothing remains.
