PASS 739097886195c9ea02b30cc03894e2c64cebb4cf

# Review of the whole change — small-fixes-after-pr-155

Range `80006b25feb4c5a6ffdb8f75d993051eecbc745d..739097886195c9ea02b30cc03894e2c64cebb4cf`, two commits
(`ac7f22a0`, `73909788`), one author, no spec, no plan, no slice reviews. `git rev-parse HEAD` in the
worktree gave `739097886195c9ea02b30cc03894e2c64cebb4cf`, the head given.

Changed files (`python -B task-cycle/change_file_sizes.py 80006b25 73909788`):

| File | Before | After | Change |
|---|---|---|---|
| `guidelines/testing.md` | 270 | 282 | +12 |
| `task-cycle/gate_times.py` | 465 | 464 | -1 |
| `task-cycle/test_gate_times.py` | 878 | 1005 | +127 |
| `task-cycle/test_remove_merged_worktrees.py` | 840 | 849 | +9 |

Counts: 0 blocking, 5 Minor within the task, 1 Minor outside the task.

## Findings

### Critical

none

### Important

none

### Minor (within the task)

**m1 — `task-cycle/test_remove_merged_worktrees.py:120-123` and `:37-39`: the new comments say the
receiving side gets none of the variables of `ENVIRONMENT`, which is wider than what git does.**
The comment in `Fixture.__init__` reads "Git hands the side that takes a `push` to a local
repository none of the variables of ENVIRONMENT"; the one at `ENVIRONMENT` reads "it takes a `push`
through git's own receive-pack, which gets none of these variables" and calls the bare repository "no
such process of the tests" (a repository is no process). Git unsets before `git-receive-pack` only
`GIT_CONFIG_COUNT GIT_CONFIG_PARAMETERS GIT_PREFIX` (and the variables that locate a repository): the
author's own trace shows the line `run_command: unset GIT_CONFIG_COUNT GIT_CONFIG_PARAMETERS
GIT_PREFIX; 'git-receive-pack …origin.git'` (`reports/author-trace-before.txt:13`), and the same trace
holds receive-pack's own lines (`built-in: git receive-pack …`, line 16), which it could write only
because `GIT_TRACE`, a variable of `ENVIRONMENT` in that run, reached it. `GIT_CONFIG_GLOBAL`,
`GIT_CONFIG_NOSYSTEM` and the author and committer variables reach it as well. Why it matters: To do 1
asks these comments to say what is true after the earlier ones did not; a later reader who takes the
comment at its word believes receive-pack also reads the user's global configuration, and reasons
about the fixture from a wrong fact. Suggested wording: "none of the variables that carry
configuration (`GIT_CONFIG_COUNT` and its keys and values)". The rule in `guidelines/testing.md:181`
("git passes none of them") follows the wording of row 1 of *Settlements to record*, where "them" reads
as the variables that turn maintenance off; it needs no change of its own.

**m2 — `guidelines/testing.md:179-182` against `task-cycle/test_remove_merged_worktrees.py:126`: the
fixture the rule comes from does not do what the rule's sentence says for its second repository.**
The rule: "A git test that turns off git's automatic maintenance sets it in the configuration of each
repository it builds, the bare remote one too, and not in environment variables alone". `Fixture`
builds two repositories, `origin.git` and `main` (`git(self.root, "init", "-b", target,
str(self.main))`, line 126), and sets `maintenance.auto`/`gc.auto` in the configuration of
`origin.git` alone; `main` has them from `ENVIRONMENT` alone. Today this has no effect: every git
process in `main` is started by the tests or by the script under test with `env=ENVIRONMENT` (lines 67,
197, 209), and `state()` leaves `.git` out of the snapshot (line 86). Why it matters: the only test the
rule reaches is the one it was written from, and it departs from the rule's sentence (its *Good* line,
line 176, is narrower and is met); the next review that compares a git test with the rule finds the
rule and its source disagreeing. The rule's wording is row 1 of the task's settlements, accepted by
the human, so the cheap fix lies in the code: two lines `git(self.main, "config", "maintenance.auto",
"false")` and `git(self.main, "config", "gc.auto", "0")`. Narrowing the rule instead would change an
accepted settlement and needs the human.

**m3 — `task-cycle/test_gate_times.py:454-455`: the comment of the test of change (v) restates the
description's sentence in words that contradict the test.** It says "the places of the last 100
different lines that hold `== ` after text are kept, each place once, so the 101 lines of `y2` are one
place"; the description at `task-cycle/gate_times.py:32-33` says "the last 100 different places of
lines that hold `== ` after text, each place once". "The last 100 different lines" counts lines, and the
101 lines of `y2` are 101 different lines, so the first half of the comment's sentence says the
opposite of its second half. To do 2 asks each new test to name the sentence of the description its
value comes from (WAY-394, `guidelines/testing.md`, "Where the expected value comes from"); the
sentence is named, but misquoted. Fix: quote the description's words.

**m4 — `task-cycle/test_gate_times.py:435-438`: the output of the test of change (iii) is not what
unittest prints, against the class's own statement.** The `then` text gives `gate1` a second failing
test, while `gate1`'s report still prints `F`, `Ran 1 test in 0.500s` and `FAILED (failures=1)` (from
`failing_with`, lines 195 and 200); the docstring of `NestedRunTest` says "The outputs are written out
by hand, as the runner and unittest print them" (line 219). No expected value depends on it (the time
is the first `Ran` line after the nested summary, whatever its count), and the author named it. Fix:
let `failing_with` take the test-count line, or print `FF`, `Ran 2 tests` and `FAILED (failures=2)`
when `then` is given.

**m5 — `reports/author-report.md`: no sentence on whether the change alters behaviour a user sees.**
`task-cycle/change/SKILL.md:172-177` asks the one author, where the change alters no behaviour a user
sees in the running product, to say "that it alters none, with one sentence why" (WAY-406); the report
holds no walk and no such sentence (a search for "walk", "running product" and "behaviour a user" in it
finds nothing). The judgment the sentence would carry is right: the change alters no result of
`gate_times.py` (my mutant `iv_clear_back`, the code with `self.marks.clear()` restored, passes every
test of `NestedRunTest`; the argument under *Trust boundary* below), and the rest is tests, comments
and a guideline. The request's description should carry the sentence.

### Minor (outside the task)

**o1 — `task-cycle/gate_times.py:197`: no test pins the bound of 100 places that the rewritten sentence
of the description names.** My mutant `r3_marks_maxlen_10` (`deque(maxlen=10)`) passes every test of
`NestedRunTest`, the memory test of a flood included. The gap is older than the change (the base has
the same `maxlen` and the same tests); the task asks only for the four changes (i), (ii), (iii), (v).
Outside the task's scope.

## Against the task

- **To do 1** — met. `Fixture.__init__` sets `maintenance.auto false` and `gc.auto 0` in `origin.git`
  right after `git init --bare` (lines 124-125); the two comments the task names no longer claim that
  the variables reach `origin.git` (lines 35-39, 457-460); see m1 for what they claim instead.
- **To do 2** — met. Four new tests; my own run of the four changes on a worktree of the head (script
  `reports/review-whole-mutate.py`, output `reports/review-whole-mutants.txt`) agrees with the author's:
  (i) red on `test_a_comparison_line_of_an_earlier_directory_is_not_this_nested_runs_first_line`;
  (ii) red on `…_in_the_second_nested_run_…` and `…_flood_…`; (iii) red on `…_after_the_first_nested_run_…`
  and three others; (v) red on `…_flood_…`; the head green on all. Each red is for the right reason:
  each failure message gives exactly the wrong result the task records for that change —
  (i) `[['other','0.002'],['gate','unknown'],['x','0.500']]` (the task's `None` as the record writes it),
  (ii), (iii) and (v) `[['other','0.002'],['gate1','0.001'],['y1','0.600']]` — and no test errors.
  I worked out each expected value by hand from the description (`gate_times.py:17-24`) and got the
  test's value in each: (i) the `assert x == y` line of `other` stands before three lines `== `, not
  `<m>`−1 = 1, so the summary of two takes `x` and `y`; (ii) `a` stands before 2 = `<m>`−1 lines (`b`,
  `c`), the `assert x == y` of `b` before one, so the summary of three takes `b`, `c` and the summary of
  two `y1`; (iii) `x2` stands before one line, `assert a == b` before two, so the second summary takes
  `y2` and the first `y1`; (v) the 101 lines of `y2` are one place, so `x2`'s place survives and the
  result is that of the test of two nested runs. The existing tests of `NestedRunTest` are unchanged;
  `failing_with` with its defaults gives byte for byte the text it gave before (the old f-string is
  the new one with `separator` and `then` at their defaults).
- **To do 3** — met. `self.marks.clear()` is gone from `Times.summarise`; the comment at `self.marks`
  no longer says "in this segment".
- **To do 4** — met. The sentence now ends "in the whole output, the last 100 different places of
  lines that hold `== ` after text, each place once", which is what the code does: places only grow, so
  the check `self.marks[-1] != self.count` keeps each place once, and `maxlen=SUMMARIES_KEPT` keeps 100.
  No other file holds the old sentence (search below).
- **Acceptance criterion 1** — met, shown in the author's report and again by my run above.
- **Acceptance criterion 2** — met. I ran the author's `trace_push.py` again myself, on worktrees of
  the head and of the base: head `trace lines: 136`, `lines naming git-receive-pack: 12`, `lines that run
  git maintenance or git gc: 0`; base `148`, `12`, `12` (`reports/review-whole-trace-head-result.txt`,
  `reports/review-whole-trace-base-result.txt`; git 2.55.0.windows.3). The only lines of the head's
  trace that hold `maintenance` or ` gc` are the fixture's two `git config` lines. The trace still
  shows receive-pack running in `origin.git` four times, so the zero is no trace that missed it.
- **Settlements to record, row 1** — met in `guidelines/testing.md:172-182`, as a further rule after
  the required ones (`product-guidelines/testing/template.md:87-89`), *Decision* `none` with its reason
  in one sentence ("because …", WAY-168, `product-guidelines/template.md:88-89`), *Invariant* `none`.
  The rule's sentence keeps the row's meaning; it adds the clause "so maintenance runs there in the
  background after the push returns", which is the fact of To do 1, and *Good*/*Bad* lines, both
  optional (WAY-168). No shared helper exists (each test file defines its own `git`), so the human's
  reservation does not apply. See m2.
- **Settlements to record, row 2** — met by To do 3 and 4.
- **Questions to settle** — the answer (remove the line) is carried out; nothing more was removed.
- **Out of scope** — the change adds no test of the case of remark m1 and does not change the rule of
  reading nested output: the only line of code changed is the removed `self.marks.clear()`.

## Against the foundation and the guidelines

- **WAY-394, WAY-232** — each new expected value comes from the description at the head of the script
  and the comment names that sentence (see m3 for one misquote).
- **WAY-402, WAY-253** — no mutation tool was added; the author's mutants and mine are one-off checks
  in ignored directories, removed.
- **WAY-03** — a changed invariant test: `ApplyTest.test_a_dry_run_removes_nothing_and_apply_removes_only_what_is_marked`
  in `task-cycle/test_remove_merged_worktrees.py` (`# invariant: repository-changer-acts-only-when-told`).
  Its comment and the `Fixture` it builds changed; its assertions did not. The change takes noise out
  of what the snapshot sees and weakens nothing the invariant's sentence asks. The author's report
  names it for the request; the request must name it.
- **WAY-243** — the flaky test is fixed at its cause, not run again or skipped.
- **WAY-168** — the new rule only says how to write tests, so `none` in *Decision* is right.
- **`guidelines/coding.md`** — `gate_times.py` shrinks by one line; the size invariant's test passes on
  both base and head; the linter and the formatter pass (`agent-instructions` run below). The test files
  are outside the rule of size. **`guidelines/coding-command-runner.md`** — the exit code is untouched.
- **Code made to pass a test (WAY-409)** — none: the only change of product code removes a line.
- **Structure** — no function or file grew past a threshold; no code lost its user; the comment at
  `self.marks` is true again after the removal.

## Trust boundary — `task-cycle/gate_times.py`

- **The removed line.** A mark taken before the previous summary line stands at least as many lines
  `== ` before the current summary line as the current segment holds (`self.count - mark >=
  self.count - self.segment`), so it can match `directories - 1` only where the segment has at most
  `directories - 1` lines, and then `min(lines, directories - 1, surplus)` equals `min(lines,
  directories, surplus)`. Eviction does not change this: the marks of the current segment are the most
  recent, so with the clear or without it the deque holds the same marks of the current segment. Order
  of the summary lines and where the lines with `== ` after text stand do not enter the argument. The
  author's probe (random outputs of up to 30 lines of ten kinds) never reaches the bound of 100 marks,
  100 pieces or 100 summaries, so it alone would not be enough; with the argument above it is.
- **Floods.** `reports/review-whole-flood.py`, base against head, 300 000 summary lines each: after 100
  places of `== ` after text, base 1.69 s and head 4.30 s, peak memory 28 846 and 27 550 bytes; a place,
  a line `assert x == y` and a summary line alternating, base 6.05 s and head 8.11 s, peak 39 554 and
  33 010 bytes; the same result on both (50 blocks listed, the same count not listed). Memory stays
  bounded; the time per summary line rises on such a flood, because each summary line now checks up to
  100 marks where the clear had left none, but the bound the task's answer names, 100 marks per
  summary line, is the same, and a gate's output holds one summary line per run. No finding.

## Declined to judge

- The case of remark m1 of the earlier review: the task lets it through (*Out of scope*).
- The other tests with a bare remote (`project-level/test_plan_state*.py`, `installation/test_install.py`):
  they do not turn git's maintenance off, so the new rule does not reach them, and the task's context
  says they compare no state of that directory.
- Whether `then` should print two failing tests in other existing tests: none of the existing tests
  uses it.

## Checks

| Command or method | Exit code | Result |
|---|---|---|
| `python -B -m unittest discover -s task-cycle -p "test_gate_times.py"` (worktree) | 0 | 50 tests, OK, 1 skipped (signal on Windows) |
| `python -B gate/run_tests.py task-cycle` (worktree) | 0 | 561 tests, OK, 2 skipped |
| `python -B gate/run_tests.py agent-instructions` (worktree; linter, formatter, size, entry points) | 0 | 53 tests, OK |
| `python -B elements/common/foundation_check.py` (worktree) | 0 | `0 errors` |
| `python -B task-cycle/change_file_sizes.py 80006b25 73909788` (worktree) | 0 | table above |
| `python -B -m unittest discover -s agent-instructions -p "test_size_invariant.py"`, in a worktree of the head and one of the base | 0, 0 | 4 tests OK on both; nothing pushed over a threshold |
| `python -B -I mutate.py <head worktree> <output>` (`reports/review-whole-mutate.py`) | 0 | current green; i, ii, iii, v red as above; `iv_clear_back` green; my own `r1` (`directories` for `directories - 1`) and `r2` (`opened = False`) red; `r3` (maxlen 10) green, see o1; `r4` (`self.count not in self.marks`, an equivalent) green |
| `python -B -I trace_push.py <head worktree>/task-cycle <trace>` and the same on the base (the author's script) | 0, 0 | head 0 maintenance lines, base 12 |
| `python -B -I flood.py <base gate_times.py> <head gate_times.py>` (`reports/review-whole-flood.py`) | 0 | figures under *Trust boundary* |
| `python -B elements/common/decision_index.py --output … --section … --part task-cycle --part agent-instructions --decision WAY-03 --decision WAY-394 --decision WAY-402` | 0 | 57 decisions in full, 105 by heading (`reports/review-whole-decision-index.md`); a first run with `--decision 3` ended with exit 2, `no decision 3`: the switch takes `WAY-03` |
| By hand: the expected value of each new test worked out from the description | — | each agrees with the test (see To do 2) |

Not run: the full gate (WAY-160, the cycle's own run). The flaky test cannot be made red on demand;
its evidence is the trace.

## Reach beyond the dispatch

- `task-cycle/change/SKILL.md:104-178` — the author's method, to judge what the author's report owes on
  the walk through the running product (m5).
- `foundations/decisions.md`, WAY-406 whole — opened from the run through the headings, for m5.
- `foundations/invariants.md`: `repository-changer-acts-only-when-told`, `command-runner-passes-exit-code`,
  `gate-times-refuses-impossible-entry`, `test-method-citation`, `script-subprocesses`,
  `function-and-file-size`, each whole — the invariants of the touched parts that bear on the change.
- `foundations/glossary.md`, entry `git test` — the rule uses the term.
- `foundations/part_map.md`, entries `task-cycle` and `agent-instructions` — the parts of the changed
  files.

## Working copies

- `.runs/review-whole/` held the decision index,
  my scripts and their outputs, and two git worktrees, `wt-head` (detached at `73909788`) and
  `wt-base` (detached at `80006b25`). The worktrees were removed with `git worktree remove --force` and
  `git worktree prune`, the directory with `rm -rf` by its full path. Kept beside this report:
  `review-whole-mutate.py`, `review-whole-mutants.txt`, `review-whole-flood.py`,
  `review-whole-trace-head-result.txt`, `review-whole-trace-base-result.txt`,
  `review-whole-decision-index.md`. The trace runs built the test's own `Fixture`, which makes and
  removes its directories in the system's temporary directory by itself (a product's own test, outside
  the rule). Remainder: none.

## Unread material

Of the 162 decisions of the index of my selection (57 listed in full, 105 by heading), I read 9 whole:
WAY-03, WAY-168, WAY-232, WAY-243, WAY-261, WAY-350, WAY-394, WAY-402, WAY-406. The other 48 listed in
full I read by their binding sentences in the index; among those that bear on the change, WAY-253,
WAY-389, WAY-390 and WAY-172 stayed unread beyond their binding sentences. Guideline files: none
unread — `guidelines/testing.md`, `guidelines/coding.md` and `guidelines/coding-command-runner.md` read
whole; `guidelines/coding-repository-changer.md` not selected, since the change does not change a
repository changer, only its test. Of the author's evidence, `author-trace-after.txt` was read by
search, not whole; `author-mutate.py` was not opened, since I ran mutants of my own.

## Searches not found or unclear

- `last 100 lines|since the last summary line|marks\.clear` in the worktree outside `.runs/`: not
  found (positive control: `in the whole output, the last 100` found in `task-cycle/gate_times.py`).
- `maintenance\.auto|gc\.auto` outside `.runs/`: only `guidelines/testing.md` and
  `task-cycle/test_remove_merged_worktrees.py`.
- `walk|running product|behaviour a user` in `reports/author-report.md`: not found (m5).
- Unclear: `decision_index.py --decision` takes `WAY-03`, not `3`; its help does not say which.
