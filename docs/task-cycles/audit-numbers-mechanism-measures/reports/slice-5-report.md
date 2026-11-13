# Report — slice 5

**Status:** done

**Commits** (slice range, base to head): `8a8f636..0e75a4b4c7a23e0200a4d5762543b8701f2bbb9b`, one commit,
`0e75a4b` "Count the cost from the table of tokens by model where the stage report has no section, and end with
exit code 1 on a missing field of stages.md".

**Files changed**
- `process-audit/audit_count.py`: +236 −46
- `process-audit/test_audit_count.py`: +324 −9

No other file. `TREE_PATHS` is not edited; `task-cycle/cycle_stages.py` and the `change`, `plan`, `review`, `spec`
directories are untouched.

## What the change does

- `stage_table` (new; it replaces `stage_tokens`) picks the form by the file's own signs. The heading of the
  section means the newer form, read as before (`section_table`). Without the heading, the older form is read from
  the table whose header row begins with `Model` (`older_table`), found exactly once. A table twice gives the cost
  unknown with a reason and no `Error:`.
- The older form's rows are priced by the same list through the new `cost_at`. `priced` now uses it too. A model with
  no price, a model `unknown`, a cached input above its input, or a count that is no number gives the cost unknown
  with a reason (`priced_older`).
- The older form's share is `unknown` with the reason "gives no turns" (`OLDER_NO_TURNS`). The number of rounds is
  still read from the record's `Review rounds` item.
- Missing fields (WAY-344 as row 6 settles it):
  - newer form: each of the 8 columns of the section's table, and the table itself where the heading has none;
  - older form: `Input`, `Cached input` and `Output`;
  - neither heading nor `Model` table: the section and the table, two fields;
  - one of the two time lines present without the other: the other is missing; neither present is the earlier form,
    with no error.
  - `Files named` is never missing. A header with every column in another order, or with another column beside
    them, misses none and is refused with a reason as before.
- Each missing field adds a line to `cycle.missing` and rows to *Unknown values*, and `main` prints
  `Error: repository `<key>`: cycle `<folder>`: the file `stages.md` of the copy lacks the field `<field>`` on stderr
  after the result is written. Key and folder are cut to 200 characters and escaped with `display`. Exit code 1
  joins the other cases that give it.
- The module docstring (cost, missing fields, exit codes) and the *Cost* section's text in the result are brought
  to this.

## Checks (command and exit code)

| Check | Command | Exit |
|---|---|---|
| New tests fail on the base | `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Cost -k Times -k StagesForms -k ProcessVersions`, run with the new tests and the base `audit_count.py` | 1: 71 tests, 31 failures and 1 error. The error is a mistake in my test (a string added to an int in the helper `older_row`), fixed before the code. Re-run of that one test on the base: 7 failures, for the expected reasons. |
| Same focused command after the change | same | 0 (71 tests OK) |
| `StagesForms` alone, after the change | `... -k StagesForms` | 0 (12 tests OK) |
| Whole file, once at the end | `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` | 0 (148 tests OK, 212 s) |
| No changed line in the assignment of `TREE_PATHS` | `git diff 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- process-audit/audit_count.py \| grep -c TREE_PATHS` | the count is 0, so no diff line mentions `TREE_PATHS` |
| Reviewed task-cycle files untouched | `git diff --quiet 2292f334d5499f45b68b00c477cd76a2effd7537 HEAD -- task-cycle/cycle_stages.py task-cycle/change task-cycle/plan task-cycle/review task-cycle/spec` | 0 |
| Private paths, after the commit | `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` | 0 (1 test OK) |
| Gate `gate/run_tests.py` | not run, as the handoff says | |

The tests that failed on the base before the code, by class:
- `Cost`: the older form priced by hand (`0.010650`); its share unknown with the reason and its rounds from the record;
  unpriceable rows; table written twice; table in fenced code; other order or another column.
- `StagesForms`: every missing-field test (8 newer columns, the other name, two columns at once, the heading
  without a table, 3 older columns, neither sign, two time-line directions, the cut and escaped text, the
  other cycles still counted).
- `ProcessVersions`: the older and the newer form are never in one comparison.

Tests that pass on the base too, as guards of what must not change: neither time line is the earlier form with no
error, `Files named` is never missing, columns in another order or with another beside them are refused.

## Own-work check (section 3)

- **Requirement most likely not met:** "the cost is given for every cycle of the older form without a new `Error:`",
  since the reading of `stages.md` is reworked and a form the new rules do not know would now end the weekly run with
  exit code 1. The check is to run the command on real history rather than on my own fixtures.
- **Check:** `python -B process-audit/audit_count.py --locations <temporary file> --repository the-way --today 2026-11-13`.
  The temporary locations file (in the scratchpad) names the template of the register, a results directory in the
  scratchpad and this worktree as the `the-way` checkout, so it reads the-way's own history and writes nothing into any
  repository.
- **Result:** exit 0, 75 cycles, 73 with a cost, no `Error:` line. 71 of those 73 have the share `unknown`
  (the older form), and the 2 without a cost have no `stages.md` in the copy. Every real older report in
  the-way's history is therefore read, with the cost known. The product repositories of the author were not read.
- **Mutations considered in my head:** the fence check of the older table (a test); a swapped direction of the
  time-line check (two subtests); `Total tokens` not checked as a number (a test); the share given as `0.0%` for
  the older form with rounds `none` (a test); adding `cycle_measures.py` to `TREE_PATHS` (the new series test fails at
  v2); a missing `not inside` on the heading search (the existing test of a heading in fenced code). Not caught: a
  `Model` table that starts right after another table's rows with no blank line is not found as a table start (see
  Choices); no test.

## Reaches beyond the handoff

- `process-audit/SKILL.md:143-145` (read with grep): says `stages.md` without the working-time lines or the section
  of tokens by model gives no times and no cost. That is now stale. The file is not in this slice's *Change* list, so I
  did not edit it; the orchestrator should decide whether another slice or the return step carries it.
- The real-history run above (git history of this repository, read-only).
- `task-cycle/remarks_check.py` (`display`, `split_lines`, `fenced_flags`), seen through the part of
  `audit_count.py` that imports it; not changed.

## Unread material

- `process-audit/audit_count.py`: read whole.
- `process-audit/test_audit_count.py`: read lines 1-220, 370-440, 670-1120, 1250-1330, 1840-1970, 2100-2150; the
  other classes (`CycleFound`, `ProcessPin`, `Remarks`, `CraftedInput`, `Locations`, most of `RegisterCount` and `Run`)
  I did not read. They ran in the whole-file run (148 tests, exit 0).
- `foundations/decisions.md` WAY-337, 338, 339, 343, 344, 331, 328, 38, 352; `foundations/invariants.md`
  script-imports, cross-part-imports, tracked-file-private-paths; `foundations/part_map.md` process-audit and External
  context: read whole, as the ranges the handoff gives.
- `task-cycle/cycle_stages.py:858-954` and `process-audit/price_list.md`: read whole.
- `task.md` passages: carried by the handoff word for word; I did not open `task.md` itself.
- `plan.md`: not opened (the handoff says it need not be).

## Searches not found or unclear

- "the `Error:` line names both" (neither heading nor table): the slice says in one place that the line names both
  fields and in another that each missing field gets one `Error:` line. I wrote one line per field, so the two
  appear on two lines, both naming the file. If one line holding both names was meant, it is a small change in `main`.
- "Foundation entries rows 6, 8" are in the task's table; WAY-344 and WAY-352 carry them. WAY-352 (*Verification*:
  "violates: its share of fix rounds is `0.0%`") matches what I did. No gap found.

## Choices (each with the rejected way and the cost if wrong)

1. **The older table is found by its header row** (a line starting `|` whose first cell is `Model`, outside code
   fences, not directly under another table row). Rejected: any line whose first cell is `Model` — a model named
   `Model` in a body row would count as a second table. Cost if wrong: a `Model` table glued to the rows of another
   table is not found, so the cycle gets two `Error:` lines for the section and the table; the real reports separate
   them by a blank line (confirmed by the real-history run).
2. **`Total tokens` must be a number too**, and the header must equal the five columns in order, otherwise the table is
   refused with a reason. Rejected: reading only the three columns the cost uses, by their place. Cost if wrong: a
   report whose total is garbled loses its cost, which the slice's "a token count that is no number" allows.
3. **Field names for the `Error:` line** have no backticks inside (`column Start of the table of the section Stages:
   start, waiting for tools and tokens by model`, `line Waiting for tools`, `section Stages: ...`, `table with the
   first cell Model`), since the line writes the name between backticks. Rejected: the bare column name, which
   would not tell a column from the time line of the same name. Cost if wrong: a test that expects the bare name
   as the whole field text fails; the bare name is a substring of mine.
4. **Two rows in *Unknown values* per missing table field** (`Cost` and `Fix rounds share`), one per time-line
   field (the time it gives). The reasons for the older form's share are two rows of `Fix rounds share` where the
   record's rounds also cannot be read (the form's reason and the record's). Cost if wrong: a longer table.
5. **Times tests of `Times` append an older-form table** to each stage text they give, since a file with only
   time lines now lacks the section and the table. The one test that gives no `stages.md` is unchanged (a missing
   file is no missing field of a file; it stays exit 0 with the values unknown, as before).
6. **The test of the missing `stages.md` file** stays outside the new rule, the file not being a field. Cost if wrong:
   such a cycle gives exit 0, not 1.
7. The test that changed its meaning: `test_stages_md_without_the_per_model_section_leaves_the_cost_unknown` is replaced
   by `test_stages_md_without_the_section_is_priced_from_the_table_of_tokens_by_model` (row 8). The fixtures that
   gave only time lines are given the table in `Times`.

## Problems as observed

- A shell step of my own, a Python patch passed through a Bash heredoc with doubled backslashes, wrote real line
  breaks into string literals of the test file and gave a syntax error. I checked `git diff --stat`, reset the test
  file with `git checkout`, and redid every edit with the Edit tool. Nothing from that attempt is in the commit.
- The whole file takes 160 to 215 s here (the base: 161 s for 129 tests), longer than the 120 s default of the
  harness; I ran it in the background.
