# Findings of the review of the whole change, for the fix

From `reports/review-whole-report.md` (`FAIL f52c565772f125fe5ebb17f0a0fb98ee7e56fe6e`), in the reviewer's words. Blocking findings first, each with the reviewer's mark of contradiction with the settlements; after them the Minor findings of the review of the whole change that lie within the task, to be fixed in the same round (they name no slice, so they change neither the agent nor the class).

## Blocking findings

#### I1 — The foundation check reports 12 errors at the head, so the test of the invariant `own-foundation-check-report` fails and the gate is red

- **Place:** the `decision:` lines of `process-audit/test_process_versions.py` at lines 1745,
  1765, 1778, 1975, 1991, 2013, 2050, 2080, 2095, 2129, 2159 and 2176.
- **What is wrong:** each of these lines cites a decision by a quotation the foundation check
  refuses: a passage of the *Verification* and not of a binding sentence (1745 `WAY-417 "the rows of
  the versions of a series give Q1 as a word while its image"`, 1975 `WAY-417 "on each side of a
  comparison before and after a fix"`), a quotation with an ellipsis (1765 `WAY-417 "The answer Q1
  of the audit ... is given for each group of cycles"`), a sentence of WAY-339 quoted as WAY-417's
  (1778), a quotation that does not begin a sentence (1991, 2050, 2080, 2095, 2129), a quotation
  broken over two lines (2013, 2159) and text after the quotation (2176). `elements/common/
  foundation_check.py` lists all twelve and ends with exit code 1.
- **Why it matters:** the invariant `own-foundation-check-report` (method `test`) says the check,
  run with no switch on the-way as a commit leaves it, reports no error; its test
  `elements/common/test_foundation_check.py:2504`
  (`FoundationCheckTest.test_the_way_foundation_check_reports_no_error`) fails at the head, so
  `python -B gate/run_tests.py elements/common`, and the full gate, fail. No slice from 6 on ran
  the foundation check or the `elements/common` directory; the slice checks named
  `process-audit` and `agent-instructions` only. The change cannot be merged with a red gate.
- **Evidence:** `python -B elements/common/foundation_check.py` at the head: exit 1, `12 errors`
  (the twelve lines above). The same check at `3b34de03` (slice 5): `0 errors`; at `0ee90d8e`: 2;
  at `29a1c6ae`: 3; at `ca55d4e8`: 12. The invariant's test at the head: exit 1, `FAILED
  (failures=1)`; at the base: exit 0.
- **Slice:** spans slice 6 (`0ee90d8e`, `29a1c6ae`: lines 1745, 1765, 1778) and slice 7
  (`ca55d4e8`: the other nine).
- **Fix direction:** each `decision:` line quotes, on its line, the start of a binding sentence of
  the decision it names, word for word and with nothing after the closing quote; for WAY-417 the
  sentences begin "The answer Q1 of the audit, whether a contradiction", "The answer Q2 of such a
  group", "The answer Q3, whether the median cost" and "The image of a series, which sets no two
  groups"; for WAY-339 "The audit shows each series as an image of all its cycles" and "That
  comparison is made for each fixed issue of the register". Then run the check and
  `python -B gate/run_tests.py elements/common`.

Contradiction: yes — invariant `own-foundation-check-report`

#### I2 — WAY-417, which the change writes, says that Q2 of every group, a version included, is the two sums with their answer; the row of a version gives the answer alone

- **Place:** `foundations/decisions.md:9002-9004` (WAY-417, the Q2 sentence);
  `process-audit/version_analysis.py:1016-1035` (`count_rows`) with
  `process-audit/audit_report.py:73-80` (`COUNT_HEADER`); the texts that repeat the sentence,
  `process-audit/SKILL.md:244-254` and `process-audit/audit_report.py:176-179`.
- **What is wrong:** WAY-417 reads "The answer Q2 of such a group is the sum of the slices planned
  and the sum of the slices returned too large over its cycles, with the answer that those sums
  give", and "such a group" is each of "the cycles of one version of the process, the cycles of a
  whole series, the cycles on one side of a comparison". The image and each side of a comparison
  give *Slices planned* and *Slices returned too large*; the row of a version gives *Plans read* and
  the answer, with no sums. The skill and the result's own prose then tell the reader that Q2 of a
  group, a version among them, is the two sums, and a reader of the rows of the versions finds no
  sums. The entry also says "over its cycles" where the code sums over the cycles whose plans are
  read.
- **Why it matters, and why Important:** WAY-263 — the change's files fail to do what an entry the
  change itself writes requires. The task's answer gives Q2 as "sumy odcinków planowanych i zbyt
  dużych z odpowiedzią z tych sum, jak dziś dla wersji", and the plan's slice 6 keeps "the Q2 and Q3
  cells ... of the versions as they are", so the rows of the versions follow the task and WAY-417's
  sentence states it more broadly than the task settles. The review of slice 8 graded the text side
  Minor and left the code against WAY-417 to this review; nothing shows a wrong figure, but the
  entry and the code disagree.
- **Evidence:** WAY-417 at `foundations/decisions.md:8998-9004`; the version row written at
  `version_analysis.py:1026-1035` holds six cells, `[commit, day, cycles, Q1, plans read, answer]`;
  the image (`series_summary.py:151-165`) and the sides of a comparison (`count_comparison`,
  `series_summary.py:262-270`) hold the sums. The test
  `test_the_rows_of_the_versions_stay_and_give_q1_as_numbers_of_their_cycles`
  (`test_process_versions.py:1744-1762`) asserts the six cells of a version row.
- **Slice:** spans the plan's *Foundation entries* (`a946862b`, the Q2 sentence of WAY-417) and slice
  6 (`0ee90d8e`, the rows of the versions); slice 8 (`f52c5657`) repeats the sentence in the skill.
- **Fix direction, two ways:** (a, recommended) narrow the sentence of WAY-417 to what the task
  settles — the answer Q2 of a group is the answer that the sum of the slices planned and the sum of
  the slices returned too large over its cycles whose plans are read give, and the image of a series
  and each side of a comparison show the two sums beside it — and bring `process-audit/SKILL.md`
  and the prose of `audit_report.py` in line; no code and no test changes. (b) Add the two sums as
  columns of the row of a version: one form in every row, but a change of the result that the task
  did not ask for and of the expected values of every test of a version row of the count.

Contradiction: yes — WAY-417


## Minor findings within the task

Every Minor finding below lies within the task unless it says otherwise.

1. **`task-cycle/gate_times.py:233-248` (`Times.nested`, the cap `taken = min(lines, directories,
   surplus)`) — from the review of slice 2, M1, kept.** The planned rule lets each earlier summary
   line take up to its own `<m>` lines, while a nested run in a failure message has only `<m> - 1`
   lines at the start of a line (its first directory stands after text); two directories that each
   print a nested run (the review's case A gave `[ ['other', '0.002'], ['gate1', '0.001'], ['b',
   '0.600']]` for expected `other 0.002`, `gate1 0.500`, `gate2 0.600`), or a nested output cut off
   before its summary line beside a whole one (case C), are misread as point 8 says they must not
   be. Minor: in the-way only `gate/` prints a nested runner output, so the case cannot arise today,
   and the rows concerned are of failed runs, which WAY-350 does not compare. It is a defect of the
   rule the plan mandates; the direction the slice review gives (start a nested run after the last
   line of its segment that holds `== ` after text) changes the planned rule.
2. **`task-cycle/gate_times.py:75`, `:165`, `:167`, `:205-209` (`PIECES_KEPT = 100`,
   `Piece.own`, `Piece.after`) — from the review of slice 2, M2, kept.** The ceiling of memory for
   crafted output grew about four times (100 pieces keeping two copies of a `Ran` time of up to
   `LINE_LIMIT` each, where 50 blocks kept one). It stays bounded, as the plan requires; cutting the
   kept seconds at a length no real time reaches, or keeping one string where both fields come from
   one line, would bring it back.
3. **`task-cycle/gate_times.py:82-84` (`SUMMARY` uses `\d`) — from the review of slice 2, M3,
   kept.** A crafted summary line with Unicode digits (`٣ tests in ٣ directories; every directory
   passed`) is read as a summary line and takes a real directory as nested; the effect is a wrong row
   of a crafted output, no failure and no change of the exit code. `[0-9]{1,9}` would match what
   the runner prints and nothing else, as `RAN` (`:80`) does.
4. **`process-audit/SKILL.md:276-277` — from the review of slice 8, Minor 2, kept.** "the series
   whose rows give nothing but `unknown`" no longer fits a series of the count of remarks, whose Q1
   cell is always three numbers (`yes 0 · no 0 · unknown 3`); read literally it never groups such a
   series. A clause such as "for Q1, a series whose every version reads `yes 0 · no 0 · unknown n`"
   settles it.
5. **`process-audit/audit_count.py:201`, `:157`, `:160` — from the review of slice 8, Minor 3,
   kept.** Docstring lines of 146, 101 and 104 characters, line 201 an old line joined without
   rewrapping. Layout only. The same holds for the new string at `process-audit/audit_report.py:176`
   (over 100 characters) and for the Markdown files of point 9 after the rename:
   `elements/common/reaching_another_skill.md:6` is one line of 533 characters and `:3` of 131, and
   the replaced paragraph of each of the 15 skills has a line of 107 to 115 characters (the longer
   path was put in by a substitution, not rewrapped); `task-cycle/skill/return_step.md:9-11` is
   rewrapped so that line 11 holds three words.
6. **The review of slice 8, Minor 1 (`process-audit/SKILL.md:244-254`, Q2 of a version as the
   sums), is taken into I2** and is not a finding of its own here.
7. **`process-audit/series_summary.py:273-293` (`mechanism_comparison`) — from the report of
   executor 7, a concern graded here.** A comparison of the mechanism measures stands wherever cycles
   stand on both sides of a fix, also where no cycle on either side gives a value, and then it writes
   15 pairs of rows of `0` and `unknown` for that issue, in each such series, and 15 unknown values
   (grouped by `unknown_field` into 15 pairs). The task asks for a comparison "w każdej serii, w
   której po obu stronach poprawki stoją cykle", so the code follows it word for word; but a reader
   of a register with many fixed issues gets many tables of nothing, the noise the task's *Need*
   names. A version with no value already gets one row with `—`; the same for a comparison, or a
   comparison only where a value stands on both sides, would cut it.
8. **`process-audit/audit_report.py:181-182` — the prose says "*Unknown values* says why an answer
   is unknown", but an unknown Q2 or median of an image, and an unknown Q2 of a side of a comparison
   of the count, give no line of *Unknown values*** (only the rows of the versions and the verdicts
   of the comparisons do: `count_image` drops `PlanSums.why`, `series_summary.py:155-165`). The
   reason follows from the versions' own lines, so a reader can find it; the sentence says more than
   the result holds.
9. **`process-audit/test_audit_count.py:304` (`AuditCountCase.section`) — from the report of
   executor 6, graded here.** The base helper reads every table line under a series heading, which
   is wrong for a series that now opens with an image; its only users are in
   `process-audit/test_process_versions.py`, where `VersionsCase.section` (`:91`) overrides it. A
   helper of the shared test case that no test can use as it stands.
10. **`foundations/part_map.md:67-75` (`elements-common`) — the part answers for "the way of working
    shared by foundation-entry skills", while `elements/common/reaching_another_skill.md` now serves
    the nine skills of `project-level`, `product-guidelines` and `foundation-review` as well.** The
    plan's *Choices* leaves it to the return step (WAY-11 compares the part map of the touched
    parts with the code); named here so that the return step does not miss it.

No Minor finding lies outside the task.

