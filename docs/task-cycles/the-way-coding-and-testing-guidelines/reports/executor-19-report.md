# Executor report — slice 19: the guidelines of the kinds `measuring-report` and `generator`

**Status:** done with concerns

The concerns are three mismatches between the task's Context and the code at the base, listed under
*Concerns*. None changes a status of the table below; the statuses were checked against the code.

## Commits

- `cb6c208` Write the guidelines of the kinds measuring-report and generator (branch
  `task/the-way-coding-and-testing-guidelines`, base `38c1ff87b1ac2ad9ba45974df3373737db0a9cd6`)

## Files changed

| File | Added | Removed |
|---|---|---|
| `guidelines\coding-measuring-report.md` | 42 | 0 |
| `guidelines\coding-generator.md` | 43 | 0 |

Both files are new and follow the form of `guidelines/coding-check.md` and
`guidelines/coding-shared-module.md`. Rules: `measuring-report` reads `none — WAY-387`; `generator`
has one rule, *Decision* WAY-388, *Invariant* `generator-writes-only-with-write`. No value is copied
from code or a decision, and no path of a user's disk or note link stands in either file.

## Checks

| Check | Command | Exit code | Result |
|---|---|---|---|
| Foundation, before staging | `python -B elements/common/foundation_check.py` | 0 | `0 errors` (318 files) |
| Foundation, after staging | same | 0 | `0 errors` (320 files) |
| Private paths | `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 | `checked: 320 files, 0 listed` |
| Focused tests | `python -B gate/run_tests.py agent-instructions` | 0 | 35 tests, `OK (expected failures=2)` (the two expected failures are the existing ones) |
| Pinned linter on the exemplars | `<ruff> check --no-cache --ignore-noqa task-cycle/cycle_measures.py agent-instructions/skill_entry_points.py` | 0 | `All checks passed!` (ruff 0.17.1) |
| Pinned linter on the copy-status files of the tables | same, on the other seven files | 1 on `process-audit/audit_count.py` (RUF059 at line 1259; UP037 at lines 2293, 2506, 2580) and on `task-cycle/cycle_stages.py` (TRY004 at line 598); 0 on the other five | see *Concerns* |

The full gate was not run (WAY-160). No test was written and no invariant test was seen failing
again, because the change is prose with no code; the invariant's existing tests are the ones the
focused run executed.

Slice dependencies checked in the base history: Slice 4 (`ced0fd9`, `49be485`), Slice 5 (cycle
measures, linter clean), Slice 10 (`0645ec7`, `cf302df`, `d84dc5b`), Slice 12 (`c86b09b`) and
Slice 18 (`38c1ff8`) are all in the base.

## Own-work check

- **Requirement:** each reference of the two files names an entry the foundation holds and has not
  withdrawn (WAY-387, WAY-388, WAY-344 and the invariant `generator-writes-only-with-write`), and each
  status matches the code.
- **Check 1, references:** I changed `WAY-388` to `WAY-999` in `guidelines/coding-generator.md`,
  ran `python -B elements/common/foundation_check.py`, and it exited 1 with two findings
  (`guidelines/coding-generator.md:16` and `:23`, "names no decision of the log"). I restored the
  file from a copy, the file is identical to the index again, and the check exited 0.
- **Check 2, statuses against the code:** see the table below; for each file the method is stated.
- **Check 3, the rule's invariant:** the invariant's tests are cited at
  `agent-instructions/test_skill_entry_points.py:259` and `agent-instructions/test_agent_type_copies.py:75`;
  the focused run of `agent-instructions` passed (exit 0).

## Statuses checked against the code

Checked at the base `38c1ff8` plus the commits of Slices 4, 5, 10 and 12.

**`measuring-report`**

- `task-cycle/cycle_measures.py` — `exemplar` (WAY-387). Read whole. It has a usage docstring with
  the exit codes, `main(...) -> int` at line 727, one `sys.exit(main())`, and its missing transcript
  field ends the run with exit 2 (`member`, `whole`, `identifier` at lines 170–188). Ruff passes.
- `task-cycle/change_file_sizes.py` — `copy`. Usage docstring, `main -> int` (line 247), one entry
  point. Grep for defaulted field reads (`.get(…, default)`, `or {}`, `or []`, `or ""`): none.
  Checked in part only; not read whole. Ruff passes.
- `task-cycle/review_reminder.py` — `copy`. Usage docstring, `main -> int` (line 105), one entry
  point; same grep, nothing. Not read whole. Ruff passes.
- `process-audit/audit_count.py` — `copy`. Usage docstring with exit codes, `main -> int` (line
  3249), one entry point. The grep found only `by_issue.get(name, [])` (line 2371) and `why or ""`
  (line 2832), which are a dictionary lookup and a text, not reads of a field. Not read whole, 3310
  lines. Ruff reports four blocking-set places (RUF059 at line 1259, UP037 at 2293, 2506, 2580), which
  sit under the `ruff-blocking-rules` invariant marked violated, as the plan's *Choices* gives.
- `task-cycle/slice_size.py` — `do not copy`, confirmed. Line 162 reads an absent `*Change*` and
  `*Read*` as a problem (`problems.append("the slice has neither …")`), a missing field reported as an
  item, which WAY-344 forbids for a script that is not a form check. The Context names this place as
  cause 16; see *Concerns*.
- `task-cycle/cycle_stages.py` — `copy`, confirmed. The two places the Context gives (`payload.get("usage") or {}`
  and `usage.get(…, 0)` for Codex token counts) are gone: Slice 4 (`ced0fd9`) reads them through
  `required` and `required_count` (lines 382–391) and ends with exit 2. `main -> int` at line 1145,
  one entry point. Ruff reports TRY004 at line 598, which the plan's *Choices* keeps under the marked
  invariant. See *Concerns*.
- `project-level/plan_state.py` — `do not copy`, confirmed. An absent `Status:` line is recorded as a
  finding (lines 468–469 and 474–475) and the script ends with exit 1 (`if findings: return …, 1`,
  line 478), a missing field as an item with exit 1, which WAY-344 forbids. `main(argv=None)` has no
  `-> int` (line 485), a rule-16 fault as well. Ruff passes.

**`generator`**

- `agent-instructions/skill_entry_points.py` — `exemplar` (WAY-388). Read whole. A missing `name:` or
  `description:` raises `MissingFieldError` (lines 52–53, 108), which `main` turns into exit 2 with a
  message naming the file and the field (lines 253–255). Without `--write` the run only prints
  `would create|change` and orphans (lines 240–249). Ruff passes.
- `agent-instructions/agent_type_copies.py` — `copy`, confirmed. The Context's `do not copy` at line
  77 is corrected: the definition reader raises `MissingFieldError` (line 48) and `main` returns 2
  for it (lines 168–170); the write is gated on `--write` (lines 157–162). Ruff passes.

## Reaches beyond the handoff

- `decisions.md` WAY-379 (lines 9695–9725), read to find the kinds' definitions; the decision gives
  no definition of each kind, so the *When to read* lines of the two files were written from the
  exemplars' own docstrings and the task's answer 13.
- `foundations/decisions.md` lines 9925–10070, the six exemplar decisions WAY-386 to WAY-391, read as
  the E8 entries; the handoff named E8 without their range.
- `.ai/rules/git.md` of the user's notes, read before the commit as the user's rules require.

## Working copies

None made. The one output file I wrote (a focused-test log in `.runs/executor-19/`) was removed with
its directory. The mutation of `WAY-388` was made on the file itself and reverted from a copy that
was deleted afterwards.

## Unread material

- `foundations/invariants.md`: `script-language`, `script-imports`, `script-subprocesses`,
  `cross-part-imports` and `test-method-citation` were not read. The orchestrator's additions name
  them only where the slice adds or edits a Python file; this slice changes no Python file.
- `.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md`: read only at the ranges the
  handoff gives (lines 20–40, 125–150, 214–230, 525–540). Other passages were not read.
- `task-cycle/change/SKILL.md`, `task-cycle/change/slice.md`: read whole.
- `agent-instructions/test_skill_entry_points.py` and `agent-instructions/test_agent_type_copies.py`:
  not read; only their citation lines and the focused run.
- `.runs/coding/kinds_audit.md`, `.runs/coding/ruff_verdicts.md`, `.runs/coding/blocking_files.txt`,
  which the task names as the source of the Context's statuses: not read. The statuses were checked
  against the code, not against that audit.
- Within the handoff's *Read* list, every named passage was read; `cycle_measures.py` and
  `skill_entry_points.py` were read whole. Their docstrings' exit codes are the guidelines' basis.

## Searches not found or unclear

- The Context's cause label for `task-cycle/slice_size.py` line 162 is 16 (the two general rules:
  a usage docstring with exit codes, and one entry point). The line at the base is a reading of an
  absent field, which fits cause 17 / WAY-344 instead. I did not find a line of rule 16 that breaks
  in that file; the file does have a usage docstring and `main -> int`. The status `do not copy`
  stands either way.
- The Context's line for `project-level/plan_state.py` (line 478) is the exit-1 return. The fault is the
  absent `Status:` reading at lines 468–475. The status stands.
- The plan's wording "both its places of `do not copy` are corrected in this change" for
  `task-cycle/cycle_stages.py` could mean this task or the base. I found the correction made by
  Slice 4 (`ced0fd9`), which is in the base, so I took the status as `copy` at the base; no change of
  this slice touches that file.
- I did not find where the 37 blocking-rule places named in the plan's *Choices* are listed per file,
  beyond the four I ran ruff on; the list of ruff reports for `audit_count.py` and `cycle_stages.py`
  above is what the pinned tool gave on the base today.

## Questions

None blocking. Recommended answers, for the orchestrator's decision:

1. Accept the statuses as they stand (`copy` for `cycle_stages.py` and `agent_type_copies.py`,
   `do not copy` for `slice_size.py` and `plan_state.py`). Recommended, since each status matches the
   code at the base.
2. Correct the Context's cause labels for `slice_size.py` and `plan_state.py` in the task record, or
   leave them as record. Recommended: leave as record; the labels do not reach the guidelines.

## Concerns

- **Cause labels.** See *Searches not found or unclear*: the Context's cause numbers for `slice_size.py`
  and `plan_state.py` do not match the lines the Context cites. The statuses stand.
- **Ruff reports in files of `copy` status.** `process-audit/audit_count.py` has four blocking-set
  reports and `task-cycle/cycle_stages.py` one TRY004. Both are under the marked `ruff-blocking-rules`
  invariant by the plan's choice. A later copy of either file would copy that report; the guideline
  says a copy is allowed, so the reviewer should know it.
- **Three copy-status files checked in part.** `change_file_sizes.py`, `review_reminder.py` and
  `audit_count.py` were not read whole; the check was the shape of each and a grep for defaulted
  reads. The weakest point is this: a WAY-344 fault that a default-free grep does not show would stay
  unseen. That reading is the reviewer's to check.

## Weakest point and its check

The copy-status statuses of the three files not read whole (see *Concerns*). Check made: the shape of
each file (docstring with usage and exit codes, `main -> int`, one entry point) and a grep for
defaulted field reads on `.get(`, `or {}`, `or []` and `or ""`. Result: no field read defaulted to an
empty value in `change_file_sizes.py` or `review_reminder.py`; two non-field defaults in `audit_count.py`.

## Problems observed

- The mutation check above shows that `elements/common/foundation_check.py` reads the references of
  the guideline files, so the references in both files are checked by the gate.
- `git ls-files guidelines` lists the two files of Slice 18 and, after this commit, the two new ones.
