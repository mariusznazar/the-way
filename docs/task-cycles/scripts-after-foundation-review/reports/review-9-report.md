FAIL b6f800c19d85ab449527b49b1e2f255f3b25d85f

# Review of slice 9, task `scripts-after-foundation-review` (range 6e3ab99..b6f800c, one commit)

`git rev-parse HEAD` is `b6f800c19d85ab449527b49b1e2f255f3b25d85f`, the head given. Counts: 1 blocking, 1 Minor, 0 out of scope.

## Findings

### Important (blocking)

**I1. Values that are not in the register are folded into the register's pairs, and the claim "the full list stays in the register" is false for them.**
Place: `process-audit/audit_count.py` `analyse` (the `unknown.append((cycle.repository, cycle.record, "Process pin", why))` of the fixed-issue loop, about line 2382) and `register_unknown_rows`, called on `analysis.unknown` in `render` (about line 3198); the description sentence at about line 259 ("the full list stays in the register") and the intro paragraph of the section.
What is wrong: `analysis.unknown` is not only the register's refused rows and the problems whose cycle is not read. It also holds one value for each cycle whose *Process pin* the ancestry check could not decide against a fix (`ambiguous`, `lacks commit`). Those values come from the cycles' records and the-way's history, not from the register. The new code groups them under the field `Process pin` with a count and three examples; the cycle, repository and reason of every other one are gone from the result, and no file holds them. The result then states "the full list stays in the register", which is wrong for these. The executor named this as its choice 4 and left it to the orchestrator; the task (row 6 of Settlements, To do 10) speaks of "wartości rejestru" and of the full list staying in the register, so the grouping was meant for the register's own values.
Why it matters: a reader of the audit who has to find which cycles' pin is unknown for a fixed issue could read each of them before this change (up to the old limit); now they can read three of each pair and the rest are lost, while the text says they are kept. The same fold gives the waiting-of-issue values their per-issue lines (see M1), so the group is not purely the register's either.
Evidence: `git diff` of `render` (the loop over `analysis.unknown` is replaced by the loop over `versions.unknown + measured.unknown`, and `analysis.unknown` goes whole into `register_unknown_rows`); the test `test_a_fixed_issue_whose_pin_lacks_the_commit...` (about line 2632 of the test file) now reads `Process pin` from `pair_rows()` and finds the cycle only as an example of the pair. No test has more than three cycles with an unknown pin, so none shows the loss.
Fix direction (the author's to choose): keep the values that the ancestry check adds to `analysis.unknown` (and the per-issue `the fix of issue`, `waiting of issue` values) in the first table, one row each as before, and group only `register.refused` and the problems of an unread cycle; or state in the description and the intro paragraph that these values are given by pair with three examples and that their full list is not kept anywhere, and decide that on purpose.

### Minor

**M1. The number of lines still follows the number of issues, because the field of an issue's value carries the issue's name.**
Place: `process-audit/audit_count.py` `register_unknown_rows` (the field is the value with only `row N of ` normalised), fed by `the fix of issue \`name\`` (about line 2371) and `waiting of issue \`name\`` (about lines 2398-2416).
What is wrong: each issue with an unknown fix or an unknown waiting is its own pair, so the section has one line for each such issue. I ran a scratch register with 3000 open issues each with a problem of an unread cycle: 3001 pair rows (result of 9117 lines); with 3000 fixed issues whose fix is not in the history: 3000 pair rows. The limit that bounded this (`MAX_LISTED`) is gone and nothing replaces it for these values. A real register has far fewer issues than problem rows, so the flood the task names (about 830 lines from problem rows) is gone, and the pair is read literally (field includes the name); the cost shows only with a large register of issues. Graded Minor because the task's line is "one line for each pair of a field and a reason" and the field of such a value is arguably the issue's.
Evidence: scratch test in `.runs/review-9/test_scratch.py` (removed with the directory, see Working copies): prints `pairs 3001` and `pairs 3000`. Resolving I1 by keeping those values in the first table would leave this as it was before the change.

## Declined to judge

- `process-audit/SKILL.md` lines 161-162 still say a refused row's entry in *Unknown values* "names row `<n>` of *Problems*"; stale after this change. The plan gives the prose of `process-audit/` (including "the note on *Unknown values*") to a later slice (the goal at `plan.md` line 117, `Change: process-audit/SKILL.md · process-audit/problem_register.md`), so it is outside this slice.
- The executor's remark that the template as shipped holds no problem rows and so does not give "about 830 lines" alone: the task's sentence (line 114) is a statement of the situation, not a requirement on the template; the test uses 830 problems of one pair as the stand-in, which I judge to meet the Checks' intent.

## WAY-03

No invariant test and no test holding a `decision:` line changed. The changed tests that asserted on the cap and on the register's rows: `RegisterCount.test_a_register_far_larger_than_a_real_one_lists_its_unknown_rows_in_part` replaced by `...gives_one_line_for_each_pair`; about twenty `RegisterCount` assertions now read `pair_rows()`; `CraftedInput.test_crafted_text_of_a_register_value_reaches_its_pair_as_one_cut_line_with_no_bar` added. These tests assert the new description, which agrees with the code, so the tests are not weakened; I1 is about what they cannot show (three-example truncation of non-register values).

## What I verified (no finding)

- The description (module docstring) and the new headings agree with the code: the sentence on *Unknown values* and the list of sections name the second table; `MAX_LISTED` and the "not listed here" line are gone (`grep` finds neither in the tree outside `.runs`). Apart from I1, the claim "the full list stays in the register" holds for the register's refused rows.
- Determinism: pairs come out in order of first occurrence in a list deduplicated with `dict.fromkeys`; the counts are from a `Counter` (insertion-ordered); the existing same-bytes test passes.
- Crafted text: every cell of the second table goes through `table()` and `cell()` (one line, no bar, control characters through `display`); the repository of a problem is cut to 200 characters at its source (about line 2317) and the examples are three at most; the new `CraftedInput` test covers a bar, a control character and an over-long name. A hostile register gives no crash, write or command in this slice's reach; the only open point is the line count (M1).
- Scripts invariants: no new import (`re` and `Counter` were in the module), no subprocess, Python only (`script-language`, `script-imports`, `script-subprocesses`).
- The tests fail when the behaviour breaks: the dropped grouping would fail the 830-row test, `EXAMPLES` changed would fail the example assertions, the dropped row-number normalisation would fail the pair counts. The executor's red run on the base (21 failures) is its claim; I did not repeat it.
- The grouping does not drop `versions.unknown` and `measured.unknown`: they are written in the first table through `dict.fromkeys`, as the old merge in `main` gave them.

## Checks run

1. `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Run -k RegisterCount -k CraftedInput` — 68 tests, OK, exit 0 (the exit printed was that of `tail`; the unittest line reads `OK`).
2. Whole file `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` — 227 tests, OK, exit 0.
3. Scratch run in `.runs/review-9/test_scratch.py` (subclass of `RegisterCount`, 3000 open issues and 3000 fixed issues) — both ran, exit 0 of the count, pair counts as in M1.
4. Not run: a red run of the new tests on the base (the executor's claim; the focused tests of the head pass); the whole gate (WAY-160).

## Reach beyond the dispatch

- `.runs/task-cycles/scripts-after-foundation-review/plan.md` line 117 and a grep of the plan for `SKILL.md` — to place the stale `process-audit/SKILL.md` text (Declined to judge).
- `process-audit/SKILL.md` lines 150-175 — to read the stale passage.
- `process-audit/audit_count.py` lines 2300-2425, 2975-3030, and `grep` for `TEXT_CAP` — to follow where each value of `analysis.unknown` comes from and how a cell is cut.

## Unread material

- `process-audit/audit_count.py` read in the diff and in the parts named above, not whole; `process-audit/test_audit_count.py` read in the diff, and in the helpers and the changed tests only.
- The task passages and foundation entries of the dispatch were read whole as named (task lines 37, 75-79, 114, 148; `foundations/decisions.md:7357-7390`; `foundations/invariants.md:116-145`; `foundations/part_map.md:124-135`).
- `foundations/decisions.md:7309-7341` (the range named under *Read*) is not the same as the orchestrator's `7357-7390` and was not read as such.

## Searches not found or unclear

- The "about 830 lines" of the slice's Goal: not reproducible from the template alone (it holds no problem rows), as the executor reports; the test stands in with 830 problems.
- Whether `Process pin` and `the fix of issue` values were meant as "values of the register": unclear from the task (it says "wartości rejestru"); see I1.

## Working copies

- `.runs/review-9/test_scratch.py` — a scratch test file; stood in `.runs/review-9`. removed (the directory `.runs/review-9/` is gone, nothing remains); the pair counts of the scratch run are kept in finding M1.
