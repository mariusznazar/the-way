# Fix report — the Minor findings of the whole-change review

**Status:** done

**Commits:** `8bb897b6` (on `79c9bfb9`, the reviewed head; 26 files, +192 −96) and a second small commit wrapping two lines my first pass missed (one in `decisions.md` WAY-118's neighbour at the *Rationale* of the settling-technology decision, one in `test_plan_check.py`); after it `project-level/test_plan_check.py` ran 124 tests OK (exit 0) and `foundation_check.py` gave 0 errors.

## Finding 1 — "every key that holds a key `repository`": fixed

`process-audit/SKILL.md:125` and the docstring of `process-audit/audit_count.py:25-26` now read "every repository
key that holds a key `repository`" (the docstring line was rewrapped so it stays under 100 columns). Check: the
`process-audit` run below, exit 0.

## Finding 2 — lines not rewrapped: fixed, with named exceptions

- Markdown: a script took every line added by the rename (the diff `4758840f..HEAD`, Markdown files other than
  the glossary) that was over 100 characters and whose old line was not over 100, and broke it at the last space
  outside backticks that leaves at least 25 characters for the second line, with the indentation of a list
  continuation. No other line was touched. The glossary stays one line per definition, so it was left alone. A whole
  text of every touched file with its white space collapsed is the same before and after (checked by script, all
  files True). 21 files.
- Python and test files, by hand, only where a line the rename lengthened can be broken without a rename of code:
  `readiness_check.py` (docstring line 1, the `STATUS` pattern split in two raw strings with the same pattern, the
  message at the old line 290), `plan_check.py` (docstring bullet; three lines of that bullet reflowed),
  `test_plan_check.py` (docstring, `definition()` continuation), `test_plan_state.py` (the copied record line, the
  tuple at the old line 424), `test_readiness_check.py` (a comment, the expected message), `audit_count.py`
  (docstring). Words are unchanged.
- **Left over 100 on purpose** (each added line the rename lengthened that is still over 100): the names of three
  test methods in `project-level/test_plan_check.py` (an identifier cannot be wrapped; renaming them would change
  what they say), the glossary lines, rows of tables and one data line in a sample plan in
  `task-cycle/test_request_check.py:136` (it is test data of a list item; wrapping it would change what the test
  parses). Lines that were already over 100 before the rename (for example `foundations/decisions.md` table rows,
  `part_map.md:269`, `definition_template.md:81-82`) were not touched.
- Check: after the fix, `git diff 79c9bfb9` shows no added line over 100 characters except the above; the five
  runs below are green.

## Finding 3 — the old heading and the old status: fixed

Two tests added to `project-level/test_readiness_check.py`, class `Structure`, next to the neighbouring cases:

- `test_the_heading_of_the_record_before_the_rename_is_reported`: a whole definition with `## Gate record` in place of
  `## Approval record` gives ``("structure", "`## Gate record` is no section of the template")``.
- `test_the_status_value_before_the_rename_is_reported`: `Status: ready for gate` gives exactly one finding, of
  condition `structure`.

Each carries the citation `# invariant: project-definition-form`, **not** `project-readiness-check` as the handoff
said: the neighbouring tests of those two kinds cite `project-definition-form`, whose sentence is "…no valid `Status:`
line, a missing, repeated or unexpected required second-level section…" — the exact thing these two cases hold; the
sentence of `project-readiness-check` is about gaps, open questions and candidates. Each also names its source in a
comment (the human's answers to questions 1 and 4 of the task, 2026-11-14). The test names say "before the rename" so
that the old words stand only as input data.

Seen failing once, in a working copy of `project-level/readiness_check.py` (backup in `.runs/author-fix/`, restored):

- with `ready for gate` added to the `STATUS` pattern: `python -B -m unittest discover -s project-level -p
  test_readiness_check.py -k old_gate` → exit 1, 1 test, 1 failure (the status test);
- with `"Gate record"` added to `SECTIONS` as an alias (and so accepted as a section): the heading test fails (and so
  do many others, since the alias breaks the order check; the heading test among them);
- with the working copy restored: the same file, 81 tests, OK (exit 0).

## Checks (command, exit code)

- `python -B gate/run_tests.py project-level` — 0 (281 tests)
- `python -B gate/run_tests.py process-audit` — 0 (276 tests)
- `python -B gate/run_tests.py agent-instructions` — 0 (the linter and size tests among them)
- `python -B elements/common/foundation_check.py` — 0, "0 errors"
- No skill description changed in this fix, so no entry point was regenerated. The full gate was not run.

## Unread material

- `task-cycle/change/fix.md`, the findings file and the fix handoff: read whole. The review report was not read (as the
  handoff says). Files edited were read in the regions the wraps touched, not whole.

## Searches not found or unclear

- The handoff says to cite `project-readiness-check` on the new tests; the neighbours cite `project-definition-form`
  (see above) — I used that, and name it so the orchestrator can ask for the other if it wants it.

## Working copies

- `.runs/author-fix/` held the wrapping scripts, a backup of `readiness_check.py` used for the failing run, and the
  outputs of the runs. It is removed before this return; nothing remains.
