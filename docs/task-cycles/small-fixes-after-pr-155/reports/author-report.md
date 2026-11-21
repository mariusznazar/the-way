# Author report — small-fixes-after-pr-155

**Status:** done

Worktree `the root of the worktree`, branch `task/small-fixes-after-pr-155`,
base `80006b25feb4c5a6ffdb8f75d993051eecbc745d`. Nothing pushed.

## Commits

- `ac7f22a0` — Turn off git's automatic maintenance in the configuration of origin.git in the fixture
  of the tests of remove_merged_worktrees.py (To do 1, the foundation entry of row 1).
- `73909788` — Test the four simplifications of the nested-output rule of gate_times.py and drop the
  clearing of the marks that changes no result (To do 2, 3, 4).

## Files changed (added / removed lines, `git diff --stat 80006b25..HEAD`)

- `task-cycle/test_remove_merged_worktrees.py` — +13 / -4 (the two comments rewritten, two `git config`
  lines in `Fixture.__init__`)
- `guidelines/testing.md` — +12 / -0 (the new rule `### Turning off git's automatic maintenance`)
- `task-cycle/gate_times.py` — +3 / -4 (the line `self.marks.clear()` removed, the comment at
  `self.marks` and the sentence of the description on memory changed)
- `task-cycle/test_gate_times.py` — +131 / -4 (four new tests of `NestedRunTest`, the helper `failing_dir`,
  and two defaulted parameters, `separator` and `then`, of the helper `failing_with`; no existing test
  changed)

(`git diff --numstat 80006b25..HEAD`; the 4 removed lines of `test_gate_times.py` are the lines of
`failing_with` that the widened helper replaces.)

## What was made

1. `Fixture.__init__` sets `maintenance.auto false` and `gc.auto 0` in the configuration of `origin.git`
   right after `git init --bare`. The two comments the task names are corrected: the one at
   `ENVIRONMENT` now says the variables reach the processes the tests start and that `Fixture` sets both
   in `origin.git`'s configuration, because receive-pack gets none of them; the one in the test says
   `ENVIRONMENT` and `Fixture` together keep the maintenance off.
2. Four new tests in `NestedRunTest`, each naming in a comment, at the expected value, the sentence of the
   description at the head of `gate_times.py` the value was worked out from:
   - `test_a_comparison_line_of_an_earlier_directory_is_not_this_nested_runs_first_line` — change (i);
   - `test_a_comparison_line_in_the_second_nested_run_does_not_hide_the_first_ones_lines` — change (ii);
   - `test_a_comparison_line_after_the_first_nested_run_does_not_hide_the_second_ones` — change (iii);
   - `test_a_flood_of_comparison_lines_in_a_nested_directory_leaves_the_first_lines_place` — change (v).
3. `self.marks.clear()` removed from `Times.summarise`; the comment at `self.marks` no longer says "in this
   segment".
4. The sentence of the description on memory now ends "and, in the whole output, the last 100 different
   places of lines that hold `== ` after text, each place once."

Foundation step: row 1 goes to `guidelines/testing.md` as a further rule (`Decision: none`, `Invariant:
none`) in the brief form the human's answer asks for; no shared helper founded. Row 2 is the code change
of points 3 and 4 and writes no entry. A search of `maintenance.auto`, `gc.auto` and "automatic
maintenance" in the whole worktree (WAY-33) found the statement nowhere but in the test file, so the row
ties to no existing entry. Entry for the request (marked `row 1`):

- English: A git test that turns off git's automatic maintenance sets it in the configuration of each
  repository it builds, the bare remote one too, and not in environment variables alone, because git
  passes none of them to the side that takes a `push` to a local repository.
- Polish: Test gita, który wyłącza automatyczne porządkowanie gita, ustawia to w konfiguracji każdego
  repozytorium, które buduje, także gołego repozytorium zdalnego, a nie tylko zmiennymi środowiska,
  bo git nie przekazuje ich stronie przyjmującej `push` do repozytorium lokalnego.

The rule carries *Good* and *Bad* lines the row does not give; they are the cycle's wording of the same
meaning (the rule is marked `row 1`; the *Good* and *Bad* lines are the part added beyond the row).

## Checks (from the worktree; exit codes read from the commands, not from a pipe)

| Command | Exit code | Result |
|---|---|---|
| `python -B -m unittest discover -s task-cycle -p "test_gate_times.py"` | 0 | Ran 50 tests, OK (skipped=1; the signal test on Windows) |
| `python -B gate/run_tests.py task-cycle` | 0 | Ran 561 tests, OK (skipped=2) |
| `python -B gate/run_tests.py agent-instructions` | 0 | Ran 53 tests, OK (the formatter and linter invariants run there) |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` (run after the foundation step) |
| `ApplyTest.test_a_dry_run_removes_nothing_and_apply_removes_only_what_is_marked`, 20 runs one after another in `task-cycle` with `python -B -m unittest test_remove_merged_worktrees.ApplyTest.<name>` | 20 of 20 exit 0 | held every time (it fails only now and then, so 20 green runs are evidence of the fix, no proof; the proof is the trace below) |

The full gate was not run (WAY-160).

## Proof 1 — each of the changes (i), (ii), (iii), (v), written once into a copy of `gate_times.py`

One-off check by hand, no mutation tool (WAY-402). Script: `reports/author-mutate.py` (it reads
`task-cycle/gate_times.py`, makes each change in a copy in a directory of its own under `.runs/author/`
— removed since — copies `test_gate_times.py` beside it, and runs `python -B -m unittest
test_gate_times.NestedRunTest` in that directory). Every replacement is asserted to match exactly one
place. Command, from the worktree root: `python -B -I .runs/author/mutate.py` (exit 0). Result file:
`reports/author-mutants-result.txt`.

Base: the code of the change (with `self.marks.clear()` removed):

```
mutant current: exit 0; red: []
mutant i: exit 1; red: ['test_a_comparison_line_of_an_earlier_directory_is_not_this_nested_runs_first_line']
mutant ii: exit 1; red: ['test_a_comparison_line_in_the_second_nested_run_does_not_hide_the_first_ones_lines', 'test_a_flood_of_comparison_lines_in_a_nested_directory_leaves_the_first_lines_place']
mutant iii: exit 1; red: ['test_a_comparison_line_after_the_first_nested_run_does_not_hide_the_second_ones', 'test_a_comparison_line_in_the_second_nested_run_does_not_hide_the_first_ones_lines', 'test_a_flood_of_comparison_lines_in_a_nested_directory_leaves_the_first_lines_place', 'test_two_directories_that_each_print_a_nested_run_each_keep_their_own_time']
mutant v: exit 1; red: ['test_a_flood_of_comparison_lines_in_a_nested_directory_leaves_the_first_lines_place']
```

The changes written: (i) `opened = bool(self.marks)`; (ii) `opened = bool(self.marks) and self.count -
self.marks[-1] == directories - 1`; (iii) the same with `self.marks[0]`; (v) the condition of
`Times.line` replaced by `if BLOCK in text:`.

Because the task's probe ran against the code that still had `self.marks.clear()`, the same four were run
against that code too (the clear restored in the copy), to see that the new tests do not rely on its
removal:

```
mutant i: exit 1; red: ['test_a_comparison_line_of_an_earlier_directory_is_not_this_nested_runs_first_line']
mutant ii: exit 1; red: [... the second_nested_run ... and ... flood_of_comparison_lines ...]
mutant iii: exit 1; red: ['test_a_comparison_line_after_the_first_nested_run_does_not_hide_the_second_ones']
mutant v: exit 1; red: ['test_a_flood_of_comparison_lines_in_a_nested_directory_leaves_the_first_lines_place']
```

(Full names are in `reports/author-mutants-result.txt`.) With the clear removed, the existing test
`test_two_directories_that_each_print_a_nested_run_each_keep_their_own_time` also turns red on (iii); the
new test of (iii) is red on it with and without the clear.

Probe of point 3 (the answer under *Questions to settle* says removing the line changes no result):
`python -B -I .runs/author/probe.py` (exit 0; script `reports/author-probe.py`) read 200 000 random
outputs of ten kinds of lines with the code of the change and with the clear restored and compared
`Times.result()`: `random outputs: 200000; different results: 0`.

## Proof 2 — `GIT_TRACE` of a `push` into `origin.git` of the fixture

Script `reports/author-trace_push.py`: it makes `GIT_TRACE=<file>` part of `ENVIRONMENT` of the test
module, builds the `Fixture` (its own pushes: the root commit), then `fixture.task("merged")` (a push of
the branch and a push of the merge), and a fourth push of `task/unmerged`, waits 3 seconds, reads the trace
and counts the lines that start `run_command`, `start_command`, `built-in` or `exec` with `git maintenance`
or `git gc`. Command, from the worktree root: `python -B -I .runs/author/trace_push.py task-cycle
.runs/author/trace_after.txt` (exit 0). Traces kept in `reports/author-trace-after.txt` and
`reports/author-trace-before.txt`, summaries in `reports/author-trace-*-result.txt`.

Before (the test file of `HEAD` of `80006b25`, run from a copy):

```
trace lines: 148
lines naming git-receive-pack: 12
lines that run git maintenance or git gc: 12
  trace: run_command: git maintenance run --auto --quiet --detach   (4 times, each with start_command and built-in)
```

After (the fixed `Fixture`):

```
trace lines: 136
lines naming git-receive-pack: 12
lines that run git maintenance or git gc: 0
```

Lines searched: `grep -cE "git (maintenance|gc)\b" reports/author-trace-after.txt` gives `0`; the only lines
holding the words `maintenance` or `gc` in the whole trace are the two `built-in: git config
maintenance.auto false` and `built-in: git config gc.auto 0` of the fixture's own setup. The trace shows
`run_command: unset GIT_CONFIG_COUNT GIT_CONFIG_PARAMETERS GIT_PREFIX; 'git-receive-pack ...origin.git'`
(line 17), the fact the task records, and no `git maintenance` after it.

Limits: the trace does not say in which directory each line ran (git 2.55.0.windows.3; GIT_TRACE has no
directory field); that the 12 lines before are those of `origin.git`'s receive-pack follows from their
number matching 4 pushes at 3 lines each, from the task's own probe, and from the 0 after the config of
`origin.git` alone changed. The test of point 1 cannot be made red on demand (it is flaky); this trace
is its evidence, as the task's *Acceptance criteria* ask.

## Tests that cite an invariant or a decision, named for the request (WAY-03)

- `ApplyTest.test_a_dry_run_removes_nothing_and_apply_removes_only_what_is_marked` in
  `task-cycle/test_remove_merged_worktrees.py`, the line `# invariant: repository-changer-acts-only-when-told`.
  Its assertions did not change; only the comment at its head and the `Fixture` it uses changed. This is
  a test of an invariant touched by the change.
- No test of `NestedRunTest` cites a decision or an invariant; the four new ones carry no `invariant:` or
  `decision:` line. The tests that cite `command-runner-passes-exit-code` and
  `gate-times-refuses-impossible-entry` in `task-cycle/test_gate_times.py` are unchanged. No invariant's
  test was changed in its assertions.

## Own-work check (WAY-164)

- The requirement my work most likely does not meet: acceptance criterion 1 — that each of the four changes
  turns a test of `NestedRunTest` red *for the right reason*, not because a new helper fails or the text
  is not what the case says. Check: `Proof 1` above, and the by-hand derivation of each expected value
  from the description (written in the comment of each test). For (i), (ii), (iii) and (v) the mutants
  give a wrong result the task names (the (i) mutant makes `x` a block of the output, the (ii) and (iii)
  mutants leave `y1` a block), not an error. It showed each mutant red on the test(s) named above and the
  current code green on all of `NestedRunTest` (50 tests of the file, exit 0).
- The weakest point: the expected value of the test of (v) and (iii) hangs on the memory bound of the
  marks (100 places) and on the order of the marks, and the helper `failing_with` was widened
  (`separator`, `then`) so the cases could be built from it. The `then` text of (iii) says
  `Ran 1 test` and `FAILED (failures=1)` in `gate1` while it holds two failing tests, which is not what
  unittest prints; the Ran line is read as the directory's time either way, so no result depends on it,
  but a reader may stop at it.
- The test of point 1 holds by the trace and by 20 green runs; it cannot be made red now on demand.

## Choices (with the way rejected and the cost if wrong)

- Set both `maintenance.auto false` and `gc.auto 0` in `origin.git`, though the trace showed that
  `maintenance.auto` alone stops the process: an older git on CI that runs `gc --auto` from receive-pack
  stops on `gc.auto` too. Rejected: one setting only. Cost if wrong: one more `git config` line.
- Widened the helper `failing_with` by two defaulted parameters and added `failing_dir` (the shape of the
  helpers of the earlier review's `review-correction-1-cases.py`), instead of writing the four outputs
  by hand in each test. Rejected: hand-written text in each test, which would repeat the long failing
  reports four times. Cost if wrong: a test of the file that calls `failing_with` could change with the
  helper; none of the existing ones does, as their calls give the same text (all 50 tests of the file
  pass).
- Removed no more than `self.marks.clear()` in code (the task's answer), kept the other comment at
  `self.latest` unchanged.
- The size rule (WAY-365): the change adds nothing to a function or file of `gate_times.py`; it removes
  lines. No move of a part out was made.

## Reach beyond the dispatch

- `product-guidelines/template.md` and `product-guidelines/testing/template.md`: read whole, to write
  the rule of `guidelines/testing.md` in the form the guideline files take (the handoff names the
  `SKILL.md` of the testing guidelines, which points to those two files for the form of a rule). Reason:
  the skill itself holds no form of a rule.
- the two global rule files of the author for scripts and for git (the user's global rules for scripts
  and for commits).
- `task-cycle/remarks_check.py` head, to see how the report is read.

## Working copies

- `.runs/author/` held the copies of `gate_times.py` with each change (`final_*` and `withclear_*`), the
  copy of `test_remove_merged_worktrees.py` of the base (`before/`), the probe copies and the scripts.
  Removed with `rm -rf` by its full path before returning; no git worktree was made, so none to prune.
  Kept in `reports/` beside this report: `author-mutate.py`, `author-mutants-result.txt`,
  `author-probe.py`, `author-trace_push.py`, `author-trace-before.txt`, `author-trace-after.txt`,
  `author-trace-before-result.txt`, `author-trace-after-result.txt`. The scripts name `.runs/author/`
  paths; run them again by making that directory.
- The `Fixture` of the tests makes directories in the system's temporary directory by itself (a
  product's own test); outside this rule, and removed by the test.
- Remainder: none.

## Unread material

none — every file the handoff names for reading was read whole (`task-cycle/change/SKILL.md`,
`task-cycle/skill/foundation_step.md`, `product-guidelines/testing/SKILL.md`, the task, the three
guidelines files, the three files changed). Not read at all: the decision log entries WAY-03, WAY-38,
WAY-160, WAY-228, WAY-232, WAY-233, WAY-234, WAY-235, WAY-243, WAY-253, WAY-350, WAY-390, WAY-392,
WAY-393, WAY-394, WAY-398, WAY-402 and the invariant and glossary entries the handoff lists in
`foundations/` — I read the sentences of WAY-03, WAY-394 and WAY-402 as quoted in the task's *Decisions in
play*, and the guidelines files that cite the others; I did not open `foundations/decisions.md`,
`decision-index.md` or the invariants file. `git show 399b46c7:...` I read two of five files:
`review-correction-1-cases.py` and `review-correction-1-mutants.txt`; not `review-correction-1-report.md`,
`review-correction-1-cases.txt` and `review-correction-1-mutate.py`.

## Searches not found or unclear

- none found missing. Unclear: the handoff says the two proofs are to be "copied into the record", and
  the dispatch's own rule on working copies says copies are removed; I kept the proofs' scripts and
  outputs in `reports/` as that rule allows.
- The `GIT_TRACE` of git 2.55.0.windows.3 gives no working directory per line, so that the lines of
  `origin.git`'s receive-pack are told from the main checkout's only by their number and the `receive-pack`
  lines before them (see Limits above).
