PASS 99340e95f2afae7557f8165598071ea1c4f467b4

# Review of slice 11 (a planned slice), range d84dc5b..99340e9

`git rev-parse HEAD` is `99340e95f2afae7557f8165598071ea1c4f467b4`, the head given. One commit,
one file: `instruction-files/test_check_instructions.py`, +1 −0. The diff adds
`        # invariant: check-instructions-refuses-outside-links` as the first line of the body of
`test_a_file_link_out_of_the_repository_is_neither_read_nor_listed`
(`instruction-files/test_check_instructions.py:767`). `instruction-files/check_instructions.py` is
not in the range.

## Findings

### Critical
none

### Important
none

### Minor
none

Considered and found sound:

- The identifier is exactly E33's (`check-instructions-refuses-outside-links`,
  `foundations/invariants.md:538`). The line is a comment in a `.py` file, so it meets
  `test-method-citation` (`foundations/invariants.md:166-175`). `--skip-test-citations` exits 0.
  The full foundation check reports 6 errors and none names this invariant; I did not list the six
  (they belong to other slices, as the executor's report says).
- The test cited is the one the task names (task.md answer 21: `test_check_instructions.py:759`,
  now line 766 plus the citation line). It asserts the refusal the invariant states: the link yields
  only `("info", "read", "AGENTS.md", "a link out of the repository, not read")`, the exit code is 0,
  and the marker of the outside file is not in the output. The test is not circular; the expected
  values are literals.
- Failing run: with the refusal broken the test fails (see the checks), so it fails when the
  behaviour it protects breaks (WAY-08).
- The test skips through `make_file_link` where a link cannot be made
  (`instruction-files/test_check_instructions.py:85-89`). On this machine it ran, so the skip path is
  not exercised and the report does not need the "unchecked on this machine" statement. The
  executor's report does not claim a failing run it did not make.
- Trust boundary: the script is not changed (`git diff d84dc5b 99340e9 --stat` lists one file). The
  slice does only what it says. Crafted input at the file: the link to a file outside the repository
  is the crafted input, and the test of it passes unbroken and fails broken.
- The executor's concern (the file was edited without being read whole) concerns the method of the
  executor, not the change: the change is one comment line and I read the test, its helpers and the
  guard in `check_instructions.py:235-262` whole around the change. Not graded.

## Declined to judge

- Four other tests (`test_a_chain_longer_than_the_hop_limit_is_not_read`,
  `test_a_chain_of_two_links_that_leaves_the_repository_is_not_read`,
  `test_a_chain_that_reaches_a_network_path_through_a_link_is_not_followed`,
  `test_a_link_to_a_network_path_is_never_looked_up`) also failed with the refusal broken. They do not
  carry the citation and are not part of the slice; that the invariant is shown by one test is what
  the task asks (item 8, answer 21). Setting aside as outside the task.
- The six uncited invariants of other slices (full foundation check, 6 errors): other slices.

## Checks run

- `python -B instruction-files/test_check_instructions.py -v` in the reviewed worktree: exit 0;
  `Ran 105 tests`, `OK (skipped=5)`; the cited test is `ok` (not skipped). The five skips are other
  tests (FIFO, and four needing the real path of a link as on POSIX).
- Refusal broken in a worktree of `99340e9` in `.runs/review-11/wt` (line 256 of
  `instruction-files/check_instructions.py`, `if entry.is_symlink() and leads_out(...)` changed to
  `if False and ...`), same command: exit 1; `FAILED (failures=5, skipped=5)`; the cited test
  `test_a_file_link_out_of_the_repository_is_neither_read_nor_listed` is among the failures.
- `git status --short` and `git diff --stat` in the reviewed worktree after my checks: empty, so
  `git diff -- instruction-files/check_instructions.py` is empty there.
- `python -B elements/common/foundation_check.py --skip-test-citations`: exit 0, `0 errors`.
- `python -B elements/common/foundation_check.py` (with citations), as an own check: `6 errors`,
  none naming `check-instructions-refuses-outside-links`; grep shows the identifier only in
  `foundations/invariants.md:538` and `instruction-files/test_check_instructions.py:767`.
- Not run: the product gate (`python -B gate/run_tests.py`), by the handoff. `ruff` not run: the
  change is a comment line and the slice's checks do not name it.

## Reach beyond the dispatch

- `foundations/invariants.md:530-550` around E33, and the `script-language`, `script-imports`,
  `script-subprocesses`, `cross-part-imports` invariants were not needed for a comment line; I did
  not read them beyond `test-method-citation` and E33. Reason: the change adds no code.
- `instruction-files/check_instructions.py:235-285` and
  `instruction-files/test_check_instructions.py:1-30, 85-104, 755-790` read to judge the test
  against the refusal.

## Unread material

- `foundations/decisions.md` WAY-48, WAY-235 and WAY-08 were not reread whole by me; I judged the
  slice against the invariant E33 (which derives from them), the task passages, and `test-method-citation`.
  `foundations/part_map.md` (instruction-files) was not read.
- `script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`: not read, since
  the slice adds no Python code, only a comment.
- Plan *Choices* and the orchestrator's additions at the end of `plan.md`: not read; the handoff
  restates the additions that apply, and none of the plan's choices touches a comment line.
- `instruction-files/test_check_instructions.py` read in parts (1-30, 85-104, 755-790), not whole.

## Searches not found or unclear

none

## Working copies

- `.runs\review-11\wt` — a
  detached worktree of `99340e9` with the refusal broken. Removed with `git worktree remove --force`
  then `git worktree prune`; `.runs/review-11` removed (`.runs` holds only `review-8/` and
  `task-cycles/`).
