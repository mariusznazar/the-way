# Report — slice 3 (a blocked draft request shown as blocked by the plan-state reader)

**Status:** done

## Commits and files

- `8b5662d` Report a task whose cycle ended in a blocked draft request as blocked in the plan-state reader
- `project-level/plan_state.py` +22 -7: new constant `BLOCKED_DRAFT`; `record_pointers` became
  `record_requests` (one `git grep`, two `-e` patterns: the PR URL pattern as before and the fixed
  wording), returning the pointers and the record paths whose line equals `BLOCKED_DRAFT` exactly
  (trailing space, tab and CR tolerated); `task_report` prints, after the PR pointer lines,
  `evidence <n> <name>: blocked draft request in record <path> commit <sha>`.
- `project-level/test_plan_state.py` +75: four tests (below).
- `task-cycle/skill/blocked_finding.md` +5 -3 and `task-cycle/skill/reserved_return.md` +3 -1: the
  field *Request URL and status* of the record copy reads, word for word and alone on its line,
  `blocked draft, opened on this commit`, the wording `project-level/plan_state.py` recognises.
  `reserved_return.md` already carried the wording; `blocked_finding.md` did not.

No proposal, conflict, exit code or existing line changed; the only subprocess is still Git (the same
`git grep` call, one more pattern).

## Test first

New tests: `test_blocked_draft_record_is_reported_as_blocked_from_the_field_line_only`,
`test_blocked_draft_field_with_crlf_and_trailing_blanks_is_the_same_field`,
`test_blocked_draft_wording_off_the_field_line_prints_nothing_of_the_record`,
`test_record_with_a_pull_request_url_keeps_its_pointer_and_is_not_blocked`.

- Failing run (before the code): `python -B -m unittest discover -s project-level -p "test_plan_state.py"`,
  exit 1, `Ran 44 tests`, `FAILED (failures=2)`: the first two above failed on their assertion
  (`AssertionError: Lists differ: [] != ['evidence 1 reports: blocked draft request in record
  docs/task-cycles/reports/record.md commit <sha>']`, "Second list contains 1 additional elements").
  The other two (crafted input, real PR URL) assert absence / the existing line and passed before the
  code, as they should: they guard the new code against over-matching (see mutation below).
- Passing run (after): same command, exit 0, `Ran 44 tests ... OK`.

## Checks

- `python -B -m unittest discover -s project-level -p "test_plan_state.py"` — exit 0 (44 tests).
- `python -B gate/run_tests.py project-level` — exit 0 (275 tests, OK).
- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0 (`0 errors`).
- `git diff --check` — exit 0.
- Not run: the full `gate/run_tests.py` (the cycle's run), tests of `task-cycle` (no test reads the
  two skill files; grep for `blocked_finding|reserved_return` in `*.py` finds only my comment).

## Own-work check

Requirement most likely not met: "no other text of the record reaches the output" at the trust
boundary (crafted `Request URL and status` line). Check: a test of ten crafted records (wording in
prose; after another label; quoted with `> `; indented; three partial wordings; wording followed by
`; propose 1 reports: in cycle -> done` and a fake `evidence ...` line; ESC/BEL after the wording;
ESC inside the wording; Cyrillic `o` in the wording; label changed to `state`) — each must print no
blocked line, no new proposal, no ESC/BEL. Passed. A record with CRLF and trailing blanks is
recognised and prints a clean line. Mutation: the match loosened to `BLOCKED_DRAFT in text` — the
crafted test failed on 8 subcases (the later ones also fail because earlier commits stay in the
history the reader reports); code restored before the commit. The line is built from the fixed words,
the Git-listed path (through `display`) and the commit id from `git log`; the record text is only
compared, never printed.

## Reaches beyond the dispatch

None. I read `task-cycle/change/SKILL.md`, `change/slice.md`, `agent-instructions/README.md`, the
files of the *Change* line and the ranges the handoff gives (decisions 4331-4362, 4707-4744, 8276-8340;
invariants 301-327; part map 203-210; `record_template.md` 176-195; invariant test 285-345).

## Choices

- Exact full-line match, no tolerance for backticks, a trailing full stop or annotations. Rejected:
  a looser match (`in`, or markup allowed) — it would let text on the field's line other than the
  wording be taken as the wording; cost if wrong: a record written with markup is not recognised and
  the task shows as before (no request). The two skill files now say "word for word and alone on its
  line".
- The line must start with `- ` (the record template's form) at column 0.
- One `git grep` with two patterns instead of a second call — the same Git read, as the goal gives.
  `record_pointers` renamed `record_requests` (it now returns two lists; its one caller updated; no
  other file used the name).
- Output wording: `blocked draft request in record <path> commit <sha>`; the goal fixes the contents
  (task, commit, record file, blocked draft), not the exact words.
- The new tests carry no `# invariant:` tag: they are not the test of an invariant (the invariant
  tests live in `test_plan_state_invariant.py`, unchanged).

## Drift / mismatches

- The handoff's line numbers (`plan_state.py:27`, `:146-158`) matched the current file; the places
  were found by content.
- Known limit, same as for PR pointers: a record that quotes the field line inside a fenced example
  would also be read as blocked (the reader does not parse Markdown fences).

## Searches not found or unclear

none
