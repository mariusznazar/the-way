PASS 77ddfbf70f4dd8da1a57446f99f1dde1fba1157d

# Review of fix 1 — small-fixes-after-pr-155

Range `739097886195c9ea02b30cc03894e2c64cebb4cf..77ddfbf70f4dd8da1a57446f99f1dde1fba1157d`, one commit
(`77ddfbf7`). `git rev-parse HEAD` in the worktree gave `77ddfbf70f4dd8da1a57446f99f1dde1fba1157d`, the
head given. Method: `task-cycle/review/SKILL.md` with `task-cycle/review/fix.md`; bounded by
`reports/fix-1-findings.md` (m1–m5, all Minor, no blocking finding).

Changed files (`git diff --numstat` and `python -B task-cycle/change_file_sizes.py 73909788 77ddfbf7`):

| File | Added / removed | Lines before → after |
|---|---|---|
| `task-cycle/test_gate_times.py` | +9 / -6 | 1005 → 1008 |
| `task-cycle/test_remove_merged_worktrees.py` | +10 / -7 | 849 → 852 |

Result: m1–m4 fixed, the answer to m5 right; no new Critical or Important finding in the fix diff; no
new Minor finding.

## Each finding

- **m1 — fixed.** `task-cycle/test_remove_merged_worktrees.py:37-40` now says a push to `origin.git`
  "is taken by git's own receive-pack, a process the tests do not start, which gets none of the
  variables that carry configuration (GIT_CONFIG_COUNT and its keys and values)"; `:121-124` says the
  same of the side that takes a push. This agrees with the trace line `unset GIT_CONFIG_COUNT
  GIT_CONFIG_PARAMETERS GIT_PREFIX` (`reports/author-trace-before.txt:13`); the parenthesis names which
  variables are meant, so `GIT_CONFIG_GLOBAL` and `GIT_CONFIG_NOSYSTEM`, which do reach receive-pack,
  are not claimed. The repository is no longer called a process.
- **m2 — fixed.** `Fixture.__init__` now runs `git(self.main, "config", "maintenance.auto", "false")`
  and `git(self.main, "config", "gc.auto", "0")` right after `git init` of `main`
  (`test_remove_merged_worktrees.py:128-129`), so both repositories the fixture builds meet the rule of
  `guidelines/testing.md:179-182`; the comment at `ENVIRONMENT` now says the fixture sets both "in the
  configuration of each repository it builds", which is true. The rule was not narrowed. The tests of
  the file pass (check below).
- **m3 — fixed.** The comment of the test of change (v) (`test_gate_times.py:457-458`) quotes "the last
  100 different places of lines that hold `== ` after text, each place once", word for word the end of
  the sentence at `task-cycle/gate_times.py:32-33`.
- **m4 — fixed.** `failing_with` (`test_gate_times.py:180-204`) prints `FF`, `Ran 2 tests in <s>s` and
  `FAILED (failures=2)` when `then` is given, as unittest prints two failures, and the docstring says
  so. My comparison of the function of `73909788` with the new one: for calls without `then` the text is
  byte for byte the same; with `then` it holds all three lines. The four mutants give the same reds as
  before the fix (below), so the expected values still depend on what they did.
- **m5 — answer right.** `reports/author-fix-1-report.md` now holds the sentence: the change alters no
  behaviour a user sees in the running product, because it alters no result of `gate_times.py`, and the
  rest is tests, comments and a guideline. That agrees with the change: the only change of product code
  is the removed `self.marks.clear()`, and my mutant `iv_clear_back` (the line restored) passes every
  test of `NestedRunTest` again on the new head; the general argument is in
  `reports/review-whole-report.md`, *Trust boundary*. The author's report rests the claim on the random
  probe alone, which never reaches the bounds of 100; the argument covers them, so the conclusion holds.

## The fix diff itself

Only the two test files changed; `task-cycle/gate_times.py`, the trust boundary, is untouched. No
assertion was changed, weakened or removed; the test that cites
`repository-changer-acts-only-when-told` (`ApplyTest.test_a_dry_run_removes_nothing_and_apply_removes_only_what_is_marked`)
keeps its assertions and gains two lines of setup in its `Fixture` — a changed invariant test under
WAY-03, named in the author's report for the request. No code of the product was changed, so no code
made to pass a test (WAY-409). The linter and the formatter pass.

## Declined to judge

- `o1` of the review of the whole change (no test pins the bound of 100): outside the task, not in the
  findings file.

## Checks

| Command or method | Exit code | Result |
|---|---|---|
| `python -B -m unittest discover -s task-cycle -p "test_gate_times.py"` (worktree) | 0 | OK, 1 skipped |
| `python -B -m unittest discover -s task-cycle -p "test_remove_merged_worktrees.py"` (worktree) | 0 | OK |
| `python -B gate/run_tests.py agent-instructions` (worktree; linter, formatter, size) | 0 | OK |
| `python -B elements/common/foundation_check.py` (worktree) | 0 | `0 errors` |
| `python -B task-cycle/change_file_sizes.py 73909788 77ddfbf7` (worktree) | 0 | table above |
| `python -B -I mutate.py <worktree of 77ddfbf7> <output>` (my script of the first review, `reports/review-whole-mutate.py`) | 0 | head green; (i), (ii), (iii), (v) red on the same tests and with the same wrong results as before; `iv_clear_back` green; output `reports/review-fix-1-mutants.txt` |
| `python -B cmp.py`: `failing_with` of `73909788` against that of `77ddfbf7` | 0 | `old calls identical: True`; with `then`: `FF`, `Ran 2 tests`, `failures=2` all present |

Not run: the full gate (WAY-160); the `GIT_TRACE` proof again — the fix adds configuration to `main`
only, which takes no push; the author ran it again (`reports/author-fix-1-trace-after.txt`, 0 runs of
maintenance).

## Reach beyond the dispatch

none.

## Working copies

`.runs/review-fix-1/` held the outputs of the
checks, a copy of my mutation script, a comparison script with copies of the two versions of
`test_gate_times.py`, and a git worktree `wt-head` (detached at `77ddfbf7`). The worktree was removed
with `git worktree remove --force` and `git worktree prune`, the directory with `rm -rf` by its full
path. Kept beside this report: `review-fix-1-mutants.txt`. Remainder: none.

## Unread material

none — the handoff, `task-cycle/review/fix.md`, the findings file, the author's fix report and the
whole fix diff were read whole; `reports/author-fix-1-mutants-result.txt` and
`reports/author-fix-1-trace-after.txt` were not opened, since I ran the mutants myself and the trace's
result stands in the author's report.

## Searches not found or unclear

none
