FAIL 881c1ea6fd8e471545a01481bee8da954ba6dcf1

# Review of slice 18 (rework after the real run of the count), range e8bef720..881c1ea6

`git rev-parse HEAD` = `881c1ea6fd8e471545a01481bee8da954ba6dcf1`, the head given. One commit in the range (`881c1ea`). Variant: the review of a slice.
Blocking: 1 (Important). Minor: 1. Out of scope: 0.

## Verdict in short

The code does what To do 10 and Questions to settle 5 ask: the section *Unknown values* is one table, one row for each pair of a field and a reason, with the count and the first three examples, and the real register gives 106 rows for 1605 values (against 1605 rows before the rework and 501 lines on the task's base). The grouping, the normalization of the field and the handling of crafted text are right and tested. What fails is the one thing the handoff asked me to judge last: **a sentence about where the full list of a pair stands is not true** (finding I1), the same kind of defect as the earlier slice 9's finding.

## Findings

### Important (blocking)

**I1. "The full list ... is in a new run of the count" is false, in three places, and the places named do not cover every value of the table.**

Places:
- `process-audit/audit_count.py:285-290` (module description of the result's sections): "the full list of its values is where they come from: the register's own values (its refused rows and the problems of a cycle it names) in the register, and the cycles' values in the copies of their records in the history of git and in a new run of the count."
- `process-audit/audit_count.py:3204-3208` (the intro paragraph of the section in the result, which the reader of every audit reads): "The full list of a pair is where its values come from: ... the values of the cycles, in the copies of the cycles' records in the history of git, and in a new run of the count."
- `process-audit/SKILL.md:166-169` (step 1 of the weekly session): "the full list of a pair stays where its values come from: the register's own values in the register, the cycles' values in the copies of their records in git history and in a new run of the count."

What is wrong: a new run of the count does not give the full list of a pair. The count has no option that lists more than three examples (`audit_count.py:3247-3250`: its arguments are `--locations`, `--repository`, `--prices`, `--today`), and I ran it again on the real register (below): it writes the same table, a count and three examples for each pair. So "in a new run of the count" names a place that does not hold what the sentence says it holds. The copies of the cycles' records in git history do hold the raw material, so that half is true; the other half is not. Second, the two places named (the register's refused rows and problems of a cycle it names; "the cycles' values") do not cover every value the table now holds: `analysis.unknown` also holds `the fix of issue ...` and `waiting of issue ...` (`audit_count.py:2382-2427`), and `versions.unknown` and `measured.unknown` hold `version ...`, `Mechanism measures of version ...`, `Gate times of version ...`, `cost falls, version ...` (`audit_count.py:2686-2885`). These are neither the register's refused rows or its problems, nor the values of one cycle; the sentence "the full list of a pair is where its values come from" is written as general and says nothing true or false of them as named. The whole-table sentence ("every value the count did not establish ... the full list of a pair ... ") therefore claims more than the two named places hold.

Why it matters: this is what the slice 9 review (reports/slice-9-findings.md, I1) found and the rework's handoff names as the right repair ("the right repair of that finding is the wording"): a reader of the audit who needs the cycles that make up a pair of 42 values reads in the result that a new run gives them, runs the count, and gets the same three. The reader and the session of `process-audit/SKILL.md` step 1 are told something false about where information is. WAY-330 itself is not violated (it is about where the class, weight and cost come from); the harm is a false statement in the result and in the skill, which the task's To do 10 ("the full list stays in the register") exists to keep true.

Evidence: the three sentences above; `--help`-level arguments at `audit_count.py:3247-3250`; the real run below, where a pair of many values shows the count and three examples only.

Fix direction (the author's to choose): say what is true for each place: the register's own values (its refused rows and problems of a cycle it names) are in the register; the cycles' values are in the copies of their records in git history, which a reader reads there and which the count reads again, with no listing beyond the three examples; the values about issues and about versions are made by the count from the register and from those copies, and the result keeps their count and three examples. Drop "a new run of the count" as a place of the full list, or give the count a way to write the full list (an option) and test it. The three sentences, and the module sentence at line 285, change together.

### Minor

**M1. Two comments of the code still say the unknown values are "given in full".**
- `process-audit/audit_count.py:2279` (docstring of `Analysis`): "the values it leaves unknown as (repository, record, value, why), each in full (`unknown`), and the values the register holds back ... (`held`)".
- `process-audit/audit_count.py:2309-2310` (comment in `analyse`): "The values the register holds back ... are the ones grouped by field and reason; every other unknown value is given in full."
After the rework every value goes through `unknown_rows`, so both sentences are false; the first also keeps the two lists `unknown` and `held` described as two kinds of treatment. They are comments for the next author of the file, so not blocking by themselves; they are a sentence about where a full list stands that is not true. Fix with I1.

### Out of scope

None.

## Declined to judge

None set aside. (The changed `process-audit/SKILL.md`, outside the slice's *Change* list, was judged: it follows the code in what it says of grouping and of three examples, and has the false half of I1 in the same sentence; its other changed sentences are true.)

## Judged and found right (what I checked)

- **To do 10 / Questions to settle 5 / Settlements row 6:** one line for each pair of a field and a reason, with the number of values and a few examples (three, in the order the values come: `unknown_rows`, `audit_count.py:2454-2468`). The two old tables, `register_unknown_rows` and `REGISTER_UNKNOWN_HEADER` are gone; nothing else reads them (searched the repository).
- **Is every value present?** The real run (below): the "Values" column sums to 1605, the same number of values as before the rework. No value is lost, only grouped. The entries fed to the table are the cycles' values, the deduplicated `analysis.unknown + versions.unknown + measured.unknown`, and `analysis.held` (`audit_count.py:3210-3214`): every source the old two tables read.
- **Normalization (`unknown_field`):** three patterns (row number, the issue's name in `the fix of issue` and `waiting of issue`, the commit at the end of a value naming a version); the reason is never changed, so the pair is exactly "field and reason". I ran the function on adversarial strings (200000 repetitions of `version `, of the issue prefix, of `row 1 of `, a long run of spaces): each takes at most 0.04 s, so no catastrophic backtracking. A value with a newline is simply not normalized (the `.` does not cross it); that makes a pair of its own, not a crash.
- **Crafted text:** every cell, the examples included, goes through `table` and `cell` (`audit_count.py:3025-3029`, `3001-3006`: one line, no bar, control characters written out); the held values are cut at `TEXT_CAP` as before. `test_audit_count.CraftedInput` (the test that reads the bar and the 200-character cut) passes with the new table. No write outside the places the script writes; no command run beyond what the module did.
- **Determinism:** pairs in the order each first occurs, examples in the order of the values; the entries come from lists built in a fixed order.
- **Tests:** three new or changed tests are red on the base's `audit_count.py` and green on the head: `test_more_than_three_values_of_a_pair_are_counted_and_three_are_listed` (count 5, three examples, no later value in the result, one line of the pair), `test_issues_that_differ_only_in_their_names_make_one_pair_for_each_kind_of_value`, `test_the_cycles_whose_pin_is_unknown_for_a_fixed_issue_make_one_pair_with_three_examples` (slice 9's case changed to the rule: four cycles, one pair, count 4, three examples). The helper `rows("Unknown values")` now returns the examples of the table (complete where no pair has more than three values), so the tests that read it still check values and not only counts; four tests that expected the register's pairs read `register_pair_rows()`. I found no test that passes without the code doing the work (the three new ones fail on the base).
- **Invariants:** `script-language`, `script-imports`, `script-subprocesses`: the change adds two compiled regular expressions and one `Counter` use (`re` and `collections` were already imported; standard library only), no new import, no subprocess. No invariant's test is changed. No test holds a `decision:` line that the change touches (WAY-03: none named).
- **Reserved choices:** the change takes none.
- **Trust boundary (answer yes):** the input is the register and the copies of records from git history; hostile text reaches the result only through `cell`, as above; a crash on crafted input: none found in the regexes or the table code; a write outside `audit_results`: none (the run wrote two files in the directory I gave).

## Checks I ran (command and exit code)

- `python -B -m unittest discover -s process-audit -p "test_audit_count.py"`, from the worktree root: 230 tests, OK, exit 0.
- `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"`: 3 tests OK, exit 0.
- The three new or changed tests run in a working copy of the head with `process-audit/audit_count.py` of the base (`e8bef72`) put in: `python -B -m unittest test_audit_count.RegisterCount.<the three tests>` from its `process-audit/`: 3 failures by assertion (the pair lists empty), exit 1. Red on the base, as the executor says.
- The count on the real register, through a copy of the locations file in `.runs/review-18/` whose `audit_results` entry points to `.runs/review-18/result` (the original file, the register and the repositories only read): `python -B process-audit/audit_count.py --locations <the copy>`: exit 0, 0 `Error:` lines. *Unknown values*: **106 rows** in the one table, the "Values" column sums to **1605**, 17 pairs of one value, 53 distinct fields, at most 7 rows for one field, the longest line 518 characters; the section is 111 lines with its heading and introduction. This agrees with the executor's 106 rows and 1605 values. By kind, counts only: I did not break them down further than the executor's report, which I did not contradict.
- A scratch call of `unknown_field` on adversarial strings (above): at most 0.04 s each, exit 0.
- No run of the whole gate (WAY-160).

## Reaches beyond the dispatch

- `process-audit/audit_count.py` around lines 2270-2330, 2380-2430, 2680-2890, 3000-3030, 3240-3260 and a search of the repository for `holds back`, `held back`, `Field of the register`, `register_unknown`, `MAX_LISTED`, `more values the register`, `in full`: to find what else says where a list stands and what else reads the old tables (found the stale comments of M1; no other reader).
- `process-audit/SKILL.md` lines 125-140, 160-225: to see whether other sentences of the skill rest on the old form of *Unknown values* (they hold: they name the reasons and the file and field, which the table keeps in its *Why* column).
- `.runs/task-cycles/scripts-after-foundation-review/spec.md` (the passages on WAY-344 and the section of settlements I searched) and the task lines 30-40 and 70-90, as the handoff names them.

## Working copies

- A worktree of the head with the base's `audit_count.py` put in, in `.runs/review-18/wt`: removed with `git worktree remove --force` and `git worktree prune`.
- The copy of the locations file, the result directory, the stdout and stderr files in `.runs/review-18/`: removed; the directory itself was removed. No other copy; nothing of the user's disk is in this report.

## Unread material

- `task-cycle/review/whole_change.md` and `fix.md`: not read, as the variant says.
- The plan: not read beyond what the handoff copies; the spec: only the passages above and a search for the settlements.
- `foundations/decisions.md`: WAY-330 (lines 7357-7392) and WAY-320 (7231-7302) read whole; `foundations/invariants.md:116-145` and `foundations/part_map.md:124-135` read whole. The three reports of the executor: the rework handoff and report read whole; the first report `executor-18-report.md` not read (the rework report carries what bears on the range). `reports/slice-9-findings.md` read in the part of its blocking finding I1.
- The diff of `process-audit/test_audit_count.py` read whole; the whole test file not read; the module `audit_count.py` read in the places above, not whole.

## Searches not found or unclear

- A command or option of the count that writes the full list of a pair: not found (there is none), which is the ground of I1.
- A place in the foundation that says where the full list of the values of *Unknown values* stands: not found (WAY-330 speaks of the register, not of this list); the sentences judged are those of the module description, the result and the skill.
- "Settlements row 6" of the handoff: I read it as *Questions to settle* 6 of the task (the real run), which the task text at lines 75-84 gives; unclear which row of a settlements table the handoff means, and nothing turned on it.
