PASS 2dd1bbb07a6fd5f68f704bb119079baa4bae3066

# Review of correction 1, for the human's remarks on the open request

Range `54b28445be17c4580cb2477c71dc6dd2b9076fc3..2dd1bbb07a6fd5f68f704bb119079baa4bae3066`. `git rev-parse HEAD` printed the head. There are three commits: `229a3b84`, `ff33314c` and `2dd1bbb0`. They change four files: `task-cycle/gate_times.py`, `task-cycle/test_gate_times.py`, `process-audit/test_process_versions.py` and `process-audit/test_series_summary.py`. Method: `task-cycle/review/SKILL.md` with `task-cycle/review/fix.md`. The remarks stand in place of a findings file.

I read WAY-02 whole, from its heading to the next heading (`foundations/decisions.md:458`-`503`), and WAY-12 whole (`:766`-`823`).

## Blocking findings

None.

## Minor findings

### m1 — one wrong reading of the timing script remains: a nested run that starts at the start of a line, with a line holding `== ` after text inside its first directory

- Place: `task-cycle/gate_times.py:238` (`opened = any(self.count - mark == directories - 1 for mark in self.marks)`) and `:260`.
- What is wrong: suppose a nested run starts at the start of a line, and its first directory's output holds a line with `== ` after text, such as `    assert p == q` in a failing test. That line stands exactly `<m> - 1` lines `== ` before the nested summary. The rule then takes it for the nested run's first directory, which is wrong here, and takes one line too few. The result is a made-up directory carrying another directory's time. This is the same kind of silent wrong answer as N1.
- Evidence: the case table, built by me (`review-correction-1-cases.txt` beside this report, the script `review-correction-1-cases.py`). The author's case X gives `[ ['gate', None], ['x', '0.5']]` where `[ ['gate', '0.5']]` is right. So does my variant X1, a nested run of one directory whose only test prints `assert x == y`. The rule of slice 2 (`8359dc25`) reads both right. The base `54b28445` reads both wrong too, so this correction does not cause the case; it is the one part of the N1 class still left.
- Why Minor and not blocking:
  - The remark asks that the rule read both cases right with a test for each. It does: cases A and C, and the confirmed N1 input (see below).
  - The case left needs nested output printed at the start of a line. The-way's gate never prints it that way:
    - `gate/run_tests.py:139` always opens its output with `== <directory>`;
    - every call of the runner in `gate/test_run_tests.py` captures the output (`:146`-`154`, `:476`-`490`), and the tests pass it as the message of an assertion, so it stands after `AssertionError: … : `.
  - I agree with the author that no rule based on counts alone separates X from case C. I tried one rule that also used the total surplus: it reads X right and breaks C, because the surplus of a cut-off run looks the same as X's extra line.
  - N1 itself, of the same class and more likely, was graded Minor.
- Suggestion: say the limit in the docstring. At `:23` the words "the nested run's first directory stands after text there" state as a fact what is only an inference.

### m2 — the tests do not pin what sets the new rule apart from the reviewer's direction, nor the check over all marks

- Place: `task-cycle/test_gate_times.py`, `NestedRunTest`.
- What is wrong: I wrote mutants of `gate_times.py` and ran `NestedRunTest` against each (`review-correction-1-mutants.txt`). These mutants all pass every test:
  - `opened = bool(self.marks)`, the reviewer's direction, which drops the exactness check that is the author's stated reason for the rule;
  - only the last mark checked;
  - only the first mark checked;
  - the marks not cleared at a summary line;
  - no removal of duplicate marks.

  Two of them read cases of my own wrongly, cases that the head reads right:
  - the direction misreads "X with the outer marker elsewhere": an earlier directory's traceback holds `assert x == y`, and the nested run starts at the start of a line. It gives `[ ['other','0.002'],['gate',None],['x','0.500']]`;
  - "only the last mark" misreads "N1 + A": two directories print nested runs, and the middle directory of the second prints `assert x == y`. It gives `[ ['other','0.002'],['gate1','0.001'],['y1','0.600']]`.
- Why it matters: a later edit back to the simpler rule would pass the gate and bring back a wrong reading. The remark's two cases do have their tests, and they fail where they should: the base rule fails only the N1 test, and "opened never" and "not less one" fail the tests of A and C. So this is broader coverage, not a missing requirement.

### m3 — the docstring's statement on memory is slightly looser than the code

- Place: `task-cycle/gate_times.py:32`-`33` against `:195`-`197` and `:207`.
- What is wrong: the docstring says the script keeps "the places of the last 100 lines that hold `== ` after text". The code keeps the last 100 distinct places, each place once. The bound is what matters, and it holds: the memory test fails when the deque has no bound. Wording only.

## Each remark, made or not

1. **Timing script (Minor finding 1, N1): made.** The new rule reads all of these right, each by a test of the file and by my case table, under all of `gt_head`:
   - case A, `test_two_directories_that_each_print_a_nested_run_each_keep_their_own_time`;
   - case C, `test_a_whole_nested_run_beside_one_cut_off_is_read_by_the_one_with_a_summary_line`;
   - the confirmed N1 input, `test_a_line_with_a_comparison_in_a_nested_failing_test_cuts_no_lines_taken`. Its expected value `[ ["gate", "0.500"]]` is worked out by hand in its comment. The test fails on the base rule and passes at the head;
   - a marker in the enclosing traceback before the failure message, `test_a_line_with_a_comparison_before_the_failure_message_cuts_no_lines_taken`, and my variant of it with a nested run of 3;
   - every earlier test.

   My own cases, read right as well: N1 with `<m> = 2`, an `assert` in the first nested directory, fix 1's `assert a == b` case, a nested run at the start of a line with no marker, and N1 + A.

   The author departs from the direction `min(lines, <m> - 1, surplus)`. I judge the departure sound: it reads a case right that the direction reads wrong ("X with the outer marker elsewhere"), and every case the direction reads right. What remains is m1 (Minor) and m2 (Minor).

   - Trust boundary: crafted input stays refused and harmless.
     - The registry's refusal (invariant `gate-times-refuses-impossible-entry`, `RegistryTest`) is untouched and passes.
     - Numbers are still ASCII and at most nine digits (`RAN`, `SUMMARY` unchanged).
     - A crafted summary of 0 or of 999999999 directories after a marker gives no error and no negative take: `directories - 1` is used only where `count - mark == directories - 1 ≥ 0`.
     - Memory stays bounded: `marks` has `maxlen=100`, `any()` runs over at most 100 marks per summary line, and the new flood test fails when the deque has no bound.
     - The exit code, the `Error:` forms and `relay` are unchanged in the diff.
2. **Lines `decision:` (Minor finding 4, M2): made.** Nine lines were added, each quoting word for word the start of a binding sentence, with nothing after the closing quote. I checked with `git diff … | grep '^+.*decision:' | grep -v '"$'`, which found none. Each sentence start is in `foundations/decisions.md`:
   - WAY-339 "The audit shows each series as an image of all its cycles" (`:8628`), the sentence that ends "for the times of the gate both take only the runs that WAY-350 compares";
   - WAY-417 "The answer Q1 of the audit, whether a contradiction" (`:9000`);
   - WAY-417 "The answer Q3, whether the median cost" (`:9009`).

   Each line stands at a test that holds the part the `tests:` clause names:
   - in `test_process_versions.py`: `:1294`, `:1356` (Q3 and the fall in the rows of the versions), `:1714` (Q1 in the image), `:1979` (Q1 on each side) and `:2018` (the gate times on the runs compared);
   - in `test_series_summary.py`: `Q1Numbers` `:93`, `CountImage` `:156`, `CountComparison` `:351` and `GateComparison` `:478`. I read each of these tests and checked what it asserts.

   This follows WAY-02 (the number, then the quoted start of three words or more) and WAY-12 (the line beside the test). `foundation_check.py` exits 0 at the head. A control shows the check reads this file: one changed letter in the `:478` quote made it exit 1 with "the quotation stands in no binding sentence of `WAY-339`".
3. **The comment of `process-audit/test_series_summary.py:93` (M1): made.** It now reads "Five cycles: two yes, two no and one unknown." and no longer points to the removed pair of examples.
4. **Let through: respected.**
   - `process-audit/SKILL.md` and `process-audit/audit_count.py` are not in the range (`git diff --stat 54b28445..2dd1bbb0` on them is empty).
   - `foundations/` is not in the range, so no binding sentence changed.
   - The syntax tree of `process-audit/audit_count.py` without the module docstring is the same at `268b2b07` and at the head (my script compared them and printed `same`).

## Declined to judge

- How the timing script reads nested output in shapes the-way's gate does not print: a nested runner output inside a multi-line diff of `assertEqual`, or written straight to stdout. These lie beyond the remark and the task. m1 names the one such shape the reviewed rule reads wrong.

## Checks run

| Check | Command | Exit | Result |
|---|---|---|---|
| Tests of the timing script at the head | `python -B -m unittest discover -s task-cycle -p "test_gate_times.py"` (worktree of the head) | 0 | 46 tests OK, 1 skipped |
| Foundation check | `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| Control of the foundation check | the same, after one changed letter in the quote at `test_series_summary.py:478`; restored with `git checkout` | 1 | 1 error at `:478`, as expected |
| Series summary tests | `python -B -m unittest test_series_summary` (in `process-audit/`) | 0 | 49 tests OK |
| The five tests that gained lines | `python -B -m unittest test_process_versions -k …` (the five test names) | 0 | 5 tests OK |
| Formatter and skills (the shortened name) | `python -B gate/run_tests.py agent-instructions` | 0 | 53 tests OK |
| task-cycle directory | `python -B gate/run_tests.py task-cycle` | 0 | 557 tests OK, 2 skipped |
| Hand cases against four rules: slice 2 `8359dc25`, base `54b28445`, head, the reviewer's direction; plus three mutants | `python -B -I cases.py <rules dir>` | 0 | table in `review-correction-1-cases.txt` |
| Mutants against `NestedRunTest` | `python -B -I mutate.py <head worktree> <rules dir>` | 0 | `review-correction-1-mutants.txt`; the file was restored, and `git status` of the worktree was clean |
| Syntax trees of `audit_count.py`, `268b2b07` against the head, without the module docstring | `python -B -I ast_cmp.py` | 0 | `same` |

Not run: `python -B gate/run_tests.py process-audit` (about six minutes). The correction changes no code of `process-audit`, only comments in two test files, and I ran both of those test files' affected tests.

## Reaches beyond the handoff

- `foundations/decisions.md`: WAY-339 `:8608`-`8679` and WAY-417 `:8998`-`9028`, to check each quotation against its binding sentence and each line against its `tests:` clause.
- `foundations/invariants.md:541`-`549` (`gate-times-refuses-impossible-entry`): the trust boundary.
- `guidelines/testing.md:125`-`140` (*Trust boundaries*), the section the handoff names.
- `gate/run_tests.py` (what it prints first, `:139`) and `gate/test_run_tests.py:140`-`200`, `:470`-`490`: to judge whether case X can arise in the-way's gate.
- `git show 0d0c7266` and `8359dc25:task-cycle/gate_times.py`: the earlier rules, to compare their readings.
- `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/review-return-step-report.md`, lines 14-148 (M1, M2, the answers), which the handoff names.

## Working copies

- Worktree of `2dd1bbb0` at `.runs/review-correction-1/head`. Removed with `git worktree remove --force` by its full path, then `git worktree prune`.
- Scripts, rule copies, logs and the two copies of `audit_count.py` lived in `.runs/review-correction-1/`. The directory was removed by its full path.
- Kept beside this report: `review-correction-1-cases.py`, `review-correction-1-cases.txt`, `review-correction-1-mutate.py` and `review-correction-1-mutants.txt`. The rule files the scripts read are rebuilt from git:
  - `gt_orig` = `git show 8359dc25:task-cycle/gate_times.py`;
  - `gt_base` = `git show 54b28445:task-cycle/gate_times.py`;
  - `gt_head` = `git show 2dd1bbb0:task-cycle/gate_times.py`;
  - the direction and the other mutants are `gt_head` with the line `opened = …` replaced, as in `review-correction-1-mutate.py`.
- No remainder.

## Unread material

- `.runs/task-cycles/small-fixes-from-ai-review-and-audit/reports/review-return-step-report.md`: lines 14-148 read (M1, M2, the answers to the handoff's points); the rest (the checks, reaches and working copies of that review) not read.
- `guidelines/testing.md`: only the section *Trust boundaries* the handoff names; the rest of the file not read.

## Searches not found or unclear

- `grep -n nested foundations/*.md guidelines/*.md`: no foundation entry or guideline states how the timing script must read a nested runner output. The rule is held only by the script's docstring and its tests, so m1 and m2 are judged against the remark and the docstring, not against an entry.
