# Slice 6 report: the measures of each process version, series kept apart

**Status:** done with concerns

**Commits** (branch `task/weekly-process-audit`, base `7bb25c3`):
- `260b650` Count the process versions in series with their three answers
- `2e7168c` Read a discarded attempt that opens with none as unknown

The first session ended in a crash after the main commit's code was written and tested. The second session found the work committed and a four-line fix plus its test uncommitted, finished the fix, reran the checks, and committed. The final gate run and the stdin run were repeated on the final tree.

**Files changed** (`git show --numstat`):

| File | Added | Removed |
|---|---|---|
| `process-audit/audit_count.py` | 406 | 4 |
| `process-audit/test_audit_count.py` | 186 | 3 |

## What was done

- `audit_count.py` groups each cycle by the full commit of the-way its *Process pin* resolves to (`Ancestry.commit`, the resolution slice 5 uses). Pins that are unknown, unresolvable, ambiguous or whose commit has no readable date are *no version*, with their reasons in *Unknown values*, and are in no series.
- Versions are ordered by committer date (`git log -1 --format=%ct`), ties by the full hash.
- Series split between consecutive versions at: a new price list (never fires within one run: one list per run); a date of *Added* or *Withdrawn* on or between the two versions' days; a register whose *Classes* table or a class row does not read (splits at every pair); or any change under `task-cycle/change`, `task-cycle/plan`, `task-cycle/review`, `task-cycle/spec` and `task-cycle/cycle_stages.py` (`git diff --quiet`; exit 1 or any other failure = changed).
- New section `## Process versions` (after `## Cost`), one `### Series n` table per series, each with a line saying why it begins there, and `### No version` when some cycles stand apart. Columns: version, committed day, cycles, cycles with a known cost, median cost (`money()`, the Cost table's digits), Q1, plans read (`k of m`), Q2, Q3.
- Per version: median cost of the cycles with a known cost (mean of the two middle values for an even count); Q1, Q2 and Q3 as in the orchestrator's binding choice 6, with the readings below.
- The docstring describes the versions, the series rule and the three questions. The Cost section and the stage report's form are untouched.
- Each new value that cannot be read is `unknown` with a reason in *Unknown values*; text from records reaches the result only as fixed reasons, commits and numbers.

**How a change of a report's form is told from another change of the reviewed files:** it is not. Any change under the five paths starts a series, as the conservative choice (c) requires. The result cannot separate a change of form from another change of those files.

## How each question reads the record (WAY-338, WAY-340)

- **Q1, from *Discarded attempt* and *Review rounds*:**
  - Item exactly `none` and *Review rounds* gives no findings files (`none`) → `no`.
  - Item exactly `none` and *Review rounds* names findings files → `unknown` (the findings are not in the record).
  - Item exactly `none` and *Review rounds* in prose (no findings file) → `unknown`.
  - Item opens with `none` and holds more text → `unknown` (fix 2e7168c).
  - Item contains `open design choice` → `yes`.
  - Anything else, or the item missing or doubled → `unknown`.
  - A version is `yes` if any cycle is yes, `no` if every cycle is no, else `unknown`.
- **Q2, from *Plan* and *Slices returned too large*:**
  - *Plan* opening with `none` → the cycle is left out (one-author route).
  - Otherwise the planned count is the one standalone figure written before the word `slices`. Zero or two-plus figures, or no `slices` word (for example `two slices`), → unknown.
  - *Slices returned too large*: `none` = 0; otherwise the number of entries at the item's base indent; anything else → unknown. Too-large greater than planned → unknown.
  - Version answer: `yes` where 3 × the sum of too-large over the sum of planned, of the readable cycles, is above the sum of planned; `no` where not; `unknown` where no cycle's plan is readable. *Plans read* shows `readable of planned` so the partial basis is visible.
- **Q3:** median against the previous version of the same series; `yes` where strictly lower, `no` where not lower, `unknown` where there is no previous version or a median is unknown.

**Forms seen in the archive** (`git show` of the 85 added copies of `docs/task-cycles/*/cycle.md`, plus the stdin run's 71 cycles): no archived record has a *Discarded attempt* other than `none`, and no *Slices returned too large* other than `none`; so the open-design-choice text and the list form are reading rules from the template, not observed forms. *Review rounds* is mostly prose in the archive. *Plan* is `none on the one-author route`, `none.`, or a count such as `11 slices` or `[plan.md](plan.md), … 8 slices`; number words (`two slices`, `six slices`) are not counted.

## Checks

| Command | Exit code | Result |
|---|---|---|
| `python -B gate/run_tests.py process-audit` on `7bb25c3`, before any change (baseline) | 0 | Ran 87 tests, OK (586 s) |
| `python -B -m unittest test_audit_count.ProcessVersions test_audit_count.PriceBoundary`, before the feature code | 1 | 4 failures and 1 error. The error is `AttributeError: no attribute 'Version'`, a missing name, not an assertion; it is the first-failing state of the price-boundary test, recorded as such. |
| same, after the feature code | 0 | Ran 5, OK |
| same, after the rounds test was added | 0 | Ran 6, OK |
| `python -B -m unittest test_audit_count.ProcessVersions.test_a_discarded_attempt_opening_with_none_is_not_read_as_a_design_choice`, on `260b650`'s code | 1 | failure (red) |
| same, after fix 2e7168c | 0 | OK |
| Mutation M1: `3 * large > planned` → `>=` | 1 | `test_a_third_is_not_above_a_third…` fails; restored byte-identical |
| Mutation M2: class boundary `<=` → `<` | 1 | `test_versions_compare…` fails (the class is added on v3's day); restored |
| Mutation M3: median takes the lower middle value | 1 | `test_versions_compare…` fails; restored |
| Mutation M4: tree check disabled | 1 | `test_a_change_of_the_reviewed_files…` fails; restored |
| Mutation M5: findings-file check in *Review rounds* disabled | 1 | `test_a_review_round_with_discarded_none…` fails; restored |
| `python -B gate/run_tests.py process-audit`, after the 3 positional assertions were fixed (first full run after the feature) | 0 | Ran 93, OK (658 s) |
| `python -B gate/run_tests.py process-audit`, on `2e7168c` (final tree) | 0 | Ran 94, OK (142 s). The earlier run of this check (in the crashed session) left a log without its summary, so it was repeated. |
| `python -B -m py_compile process-audit/audit_count.py process-audit/test_audit_count.py` | 0 | ok |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 | checked 279 files, 0 listed |
| Run on this repository with stdin closed: `python -B process-audit/audit_count.py --locations <scratchpad>/run9/locations.json --today 2026-11-11 <&-` (the temporary locations file names the-way with its `repository` entry set to this worktree; temporary register and results directory in the scratchpad) | 0 | `Wrote count-2026-11-11.md and count-latest.md: 71 cycles in 1 of 1 repositories.` The result has 20 series and 53 version rows. |

**Not run:** the full suite (WAY-160), as the slice's *Checks* name the gate. The run with stdin closed was made with the-way under the key `the-way`; an earlier run with the same cycles under another key read the-way's own cycles as product pins and gave 37 *no version* cycles, so the key matters (see Concerns).

**Test changes to existing tests:** three tests (`test_a_missing_stages_md_is_unknown`, `test_a_file_too_large_is_not_read`, `test_a_symbolic_link_leaving_the_record_is_not_followed`) read `Unknown values` by position `[0]`. The new process questions add rows that come first, so the assertions now select the `Waiting for tools` rows through a new helper `reasons_of`. The asserted text and the strictness are unchanged. The gate caught this; I did not change any expected value.

## Own-work check (WAY-164)

- **Requirement most likely unmet:** a version's answer or median looks measured but comes from a misread item, or a comparison crosses a series boundary.
- **Checks:** (1) crafted-input tests: a 200,000-digit *Plan* figure (must stall nothing and read unknown), `two slices`, a doubled *Plan*, a prose *Review rounds*, `none — no open design choice…`, and an exactly-one-third case (1 of 3 is not above a third); (2) mutations M1–M5 above, each caught; (3) hand reading of one real cycle, `product-guidelines-styleguide` (record `cf27d79…`, pin `96623ed…`): *Plan* `…foundation stages F1–F4 and 8 slices…` → 8 planned (the `1` and `4` in `F1`/`F4` are not standalone figures); *Slices returned too large: none* → 0; 0 × 3 > 8 is false → `no`; the run shows `1 of 1 | no`, which agrees.
- **What it showed:** every check gave the expected result. The mutations caught each boundary (exact third, class boundary inclusive of the version's day, lower-middle median, the tree rule, the findings rule).

## Choices made (the way rejected and the cost if wrong)

1. **Version = full commit that `rev-parse --disambiguate` names in the-way's checkout; ordered by committer date, ties by hash.** Rejected: the day of the commit as the sort key (ties would be common). Cost: none seen.
2. **Series split by any change under the five reviewed paths (binding choice 3c), without telling form changes from others.** Rejected: a finer rule that reads stage report forms (would need a parser of the stage report, out of this slice). Cost: on the-way's own history, 53 versions fall into 20 series, so Q3 has no previous version for most versions and cannot be answered (see Concerns).
3. **Class dates: a date on either version's day counts (inclusive); a refused *Classes* row or table splits at every pair.** Rejected: exclusive bounds, and ignoring refused rows. Cost: more series than strictly needed.
4. **Price-list boundary implemented as a per-version price field, but never fires within a run.** Rejected: a subprocess test of it, which cannot be built with one price list per run; the boundary is tested by calling `series_boundary` on two versions (`PriceBoundary`). Cost: the check named in the slice does not exist as written (see Questions).
5. **Q1: `none` exactly is no, and `none` followed by more text is unknown (fix 2e7168c).** Rejected: `none` as the start of the text being enough for no, and a phrase check on `none` text being yes. Cost: a `none …` text that really means nothing was discarded reads unknown, not no.
6. **Q1: findings named in *Review rounds* with `none` discarded → unknown.** Rejected: no (the findings' content is unknown). Cost: Q1 is unknown in most of the-way's history (see Concerns).
7. **Q2: the planned count is the one standalone figure before the word `slices`; zero or two-plus figures → unknown.** Rejected: the first integer before the word (orchestrator's wording), which would read `3` in `3 rows, 11 slices` as the slice count, a wrong figure. Cost: a plan that names its slices in number words, or with two figures before the word, is unknown.
8. **Q2 partial basis: sums over the cycles whose plan reads, with `Plans read` showing the basis.** Rejected: unknown whenever any planned cycle does not read. Cost: a `no` may rest on part of a version; the count is visible in the cell.
9. **Q3 compares against the previous version in the same series only.** Cost: none beyond the series count.
10. **Process versions and the price list read once per run.** Cost: a replaced price list reprices every cycle at once, so the old series cannot be shown in the same result.

## Questions

1. **The price-list check.** The slice names a subprocess test with "one cycle after a new price list", but one run has one price list, so the boundary cannot be seen in a run. Recommended answer: accept the unit test `PriceBoundary` as the check of that boundary.
2. **The series rule.** The-way's own history gives 20 series for 53 versions, and Q3 is unknown for every version. Recommended answer: keep the conservative rule (it is binding), and let the human see in the first weekly result that Q3 rarely answers while the reviewed paths keep changing; a finer rule belongs to a later slice.
3. **The Q2 count.** Recommended answer: accept "exactly one figure before the word `slices`" (choice 7) over the first integer.
4. **The Q2 partial basis.** Recommended answer: accept the readable-cycles sums with `Plans read` shown (choice 8).

## Concerns

- **Almost no answers on the-way's own history.** Costs are unknown for 70 of 71 cycles because their `stages.md` has no per-model section (an earlier form), so no median exists and Q3 is unknown everywhere. Q1 is unknown for all 53 versions: 55 cycles have *Review rounds* in prose, which the binding reading treats as unknown. Q2 answers `no` for 7 versions and is unknown for 46. The first result will be mostly `unknown`; this is the honest state of the archive, not a defect in the count.
- **The key of the-way matters.** The-way's own cycles pin commits in-the-way only when read under the key `the-way` (with its `repository` entry). Under another key, 37 of them became *no version*. The weekly configuration (slice 7 and the skill) must name the key `the-way`.
- **The Q1 and Q2 readings are narrow**, as choices 5–7 say; each `unknown` is a reason in *Unknown values*.
- **The gate log of the crashed session** lost its summary; the gate was repeated on the final tree.

## Reaches beyond the handoff

- `.ai/rules/scripts.md` read before writing a throwaway debug script (scratchpad `debug_items.py`, used to read one record; not in the worktree).
- Archive survey with `git log` and `git show` over `docs/task-cycles` in the-way's history (85 added copies), output in the scratchpad `archive_items.txt`.
- `task-cycle/remarks_check.py`: read lines 60–150 (`MARKER`, `reads_none`, `indent_of`, `fenced_flags`, `split_lines`, `display`); not whole.
- `process-audit/problem_register.md`: copied as the register of the stdin run.
- `task-cycle/record_template.md`: read whole.
- The stdin run used the default price list `process-audit/price_list.md` beside the script; I did not open it.

## Unread material

- `.runs/task-cycles/weekly-process-audit/reports/slice4_report.md`, `reports/correction_report.md` and `reports/slice5_handoff.md`: listed in the handoff's *Notes of the orchestrator* as what the result already holds; not read.
- `.runs/task-cycles/weekly-process-audit/plan.md`: not read (the handoff says so).
- `foundations/decisions.md` at the current ranges WAY-334, WAY-336 and WAY-338 (`10952–10972`, `10995–11035`, `11056–11080`): not read whole; the handoff's copied rows for foundation entries 4, 8 and 10 were used.
- `task-cycle/cycle_stages.py`: named by path in the tree rule; not read.
- `price_list.md`: used by the run, not opened.
- Everything else the handoff names was read: `task.md` lines 23–36 and 91–108, `foundations/decisions.md` WAY-38 and WAY-48, `foundations/invariants.md` script-language, script-imports, script-subprocesses, `foundations/glossary.md` open design choice and slice, `task-cycle/record_template.md`, `process-audit/audit_count.py` and `test_audit_count.py` whole, `slice5_report.md` and `slice5_fix_report.md`, `task-cycle/change/SKILL.md` and `slice.md` whole.

## Searches not found or unclear

- A record whose *Discarded attempt* names a discarded design choice: none in the archive; the phrase reading is from the template.
- A record whose *Slices returned too large* lists entries: none in the archive; the list reading is from the template.
- The single-line form `- Plan: none. Spec: none. Discarded attempt: none. Slices returned too large: none.` in one archived record: its items are not at the margin, so they read as missing (unknown). That record is one of the 12 cycles whose *Discarded attempt* is missing.
- Whether `git diff --end-of-options` is needed: not used. The arguments to `git diff --quiet` are full hashes from `rev-parse` and fixed paths; no record text is passed to git as an option.
