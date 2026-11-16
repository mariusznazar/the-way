PASS cef14df7d49d57e40cd3c20dc77ea48e83e2a259

# Review of the fix — readiness-approval-rename

Range of the fix: `79c9bfb95e772cb21810a78fc42607f99d726da0..cef14df7d49d57e40cd3c20dc77ea48e83e2a259`
(`8bb897b6`, `cef14df7`; 26 files, +196 −98). `git rev-parse HEAD` in the worktree gives
`cef14df7d49d57e40cd3c20dc77ea48e83e2a259`. The findings file
(`reports/fix-findings.md`) holds no blocking finding and three Minor findings within the task, so
only a new Critical or Important finding in the fix diff could fail this review (WAY-162).

## The findings of the findings file

1. **"every key that holds a key `repository`" — fixed.** `process-audit/SKILL.md:125` and the
   module docstring of `process-audit/audit_count.py:25-26` now read "every repository key that holds
   a key `repository`". This matches "repository key" in `project-level/backlog_place.md` and
   `process-audit/SKILL.md:106`. The docstring line after it was rewrapped with its words unchanged.

2. **Lines not rewrapped — fixed.** Evidence:
   - Every one of the 21 touched Markdown files and `project-level/plan_check.py` gives the same text
     with white space collapsed, at `79c9bfb9` and at `cef14df7` (checked file by file). No word of a
     decision, binding sentence or skill text changed. `foundations/decisions.md` is among the 21.
   - None of the changed Markdown lines stands inside a code fence or a table row (checked by
     script). Each new continuation line starts with no list, quote, heading or table marker, so the
     Markdown renders as before.
   - No skill description was touched: the frontmatter of `project-level/lead/skill/SKILL.md` is
     unchanged, and `python -B agent-instructions/skill_entry_points.py` prints "entry points are
     current".
   - The files whose collapsed text differs differ only as expected. In
     `project-level/readiness_check.py`, `STATUS` split into two adjacent raw strings is the same
     pattern string (compared in Python: `True`), and the message at line 291 joins to the same text.
     In `test_plan_check.py`, `test_plan_state.py` and `test_readiness_check.py`, the split string
     literals join to the same values, and the expected message of
     `ApprovalRecord.test_an_approval_record_naming_the_foundation_commit_searched_is_reported` is the
     same string. `process-audit/SKILL.md` and `audit_count.py` hold the rewording of finding 1 and
     the rewrap.
   - Added lines still over 100 characters since the base `4758840f`:
     - `foundations/decisions.md:11188` and `foundations/part_map.md:269`: table rows.
     - `project-level/definition_template.md:81-82`: already 148 and 145 characters at the base.
     - `project-level/test_plan_check.py:337` and `:345`: test method names, which are identifiers.
     - `task-cycle/test_request_check.py:136`: a list item of a sample plan that the test parses.

     Each is a reasonable exception, as the author's report says.

3. **No test pins the refusal of the old heading and status — fixed.** Two tests were added to
   `project-level/test_readiness_check.py`, class `Structure`:
   - `test_the_status_value_before_the_rename_is_reported` (line 171): `Status: ready for gate` in an
     otherwise valid definition gives exactly `["structure"]`.
   - `test_the_heading_of_the_record_before_the_rename_is_reported` (line 196): `## Gate record` in
     place of `## Approval record` gives "`## Gate record` is no section of the template".

   Each names its source, the human's answers to questions 1 and 4 of the task. I saw each one fail
   against its own mutation, in a worktree of the head:
   - With `ready for gate` added to `STATUS`, the status test fails and the heading test passes.
   - With `"Gate record"` added to `SECTIONS` as well (both mutations together), the heading test
     fails.
   - On the unchanged head, both pass.

   (When both mutations were applied together, the status test passed. This was not a gap in the test:
   the alias adds a missing-section finding of its own, also of condition `structure`, which the
   status test's assertion reads.) The author cites `# invariant: project-definition-form`, not
   `project-readiness-check`. That is right: the sentence of `project-definition-form`
   (`foundations/invariants.md:208-209`) is "rejects a definition with no valid `Status:` line, a
   missing, repeated or unexpected required second-level section", which is exactly what these two
   cases hold. The sentence of `project-readiness-check` is about gaps, open questions and candidate
   searches. The neighbouring tests of the same kind cite `project-definition-form` too.

## New findings in the fix diff

**Critical / Important:** none.

**Minor (new; goes to the request's list, blocks nothing):**

- `process-audit/SKILL.md:106-108` — the rewrap leaves a ragged paragraph:

  > Offer to add the key to the file, create the file or the repository key where
  > they are missing, and write
  > only on the human's yes.

  The words and the rendered Markdown are unchanged. Only the source reads unevenly: the script broke
  one line and did not reflow it with the next. This is cosmetic, with no effect on a reader of the
  rendered text.

## Declined to judge

- The finding outside the task (`entry` in a record's list), not part of this fix, as the handoff says.

## Checks run

- `python -B .runs/review-fix/crafted.py` (the crafted-input script of the review of the whole change,
  `reports/review-whole-crafted.py`, run on the head) — exit 0. Its output is identical, byte for byte,
  to `reports/review-whole-crafted-out.txt`. The old heading and the old status are still refused, and
  nothing else is accepted or refused differently.
- Mutation check in a worktree of the head (`.runs/review-fix/wt`):
  `python -B -m unittest discover -s project-level -p test_readiness_check.py -k before_the_rename`.
  - `STATUS` plus `ready for gate` — exit 1 (the status test fails).
  - `STATUS` plus `ready for gate`, and `SECTIONS` plus `Gate record` — exit 1 (the heading test
    fails).
  - Unchanged head — exit 0.
- `python -B elements/common/foundation_check.py` — exit 0, "0 errors".
- `python -B agent-instructions/skill_entry_points.py` — exit 0, "entry points are current".
- `python -B gate/run_tests.py project-level` — exit 0 (281 tests)
- `python -B gate/run_tests.py agent-instructions` — exit 0 (50 tests, 2 expected failures of invariants marked violated, as before)
- `python -B gate/run_tests.py process-audit` — exit 0 (276 tests)
- Collapsed-white-space comparison of each of the 26 files at `79c9bfb9` and `cef14df7` (git show,
  `tr`) — 21 Markdown files and `plan_check.py` the same; the 4 others differ as described above.
- A script check that no changed Markdown line stands in a code fence or a table — none does.
- A list of every added line over 100 characters between `4758840f` and `cef14df7`, outside the
  glossary and the skill descriptions — the seven named under finding 2.
- Not run: the full gate (handoff), `elements/common` and `task-cycle` (the fix touches only Markdown
  there, whose collapsed text is unchanged).

## Working copies

- `.runs/review-fix/wt`, a worktree of `cef14df7` for the mutation check — removed with
  `git worktree remove --force`, then `git worktree prune`.
- `.runs/review-fix/` held the copy of the crafted-input script, its output and the outputs of the
  test runs — removed before return. Nothing remains.

## Unread material

The findings file, the fix report, the handoff and `task-cycle/review/fix.md` were read whole, and so
was the full diff of the fix. The touched files were read in the regions the diff touches; the
Markdown files' unchanged text is shown by the collapsed comparison. `foundations/invariants.md` was
read at `project-definition-form` only. No decision was read anew: the fix changes the words of none.

## Searches not found or unclear

- The fix report gives the failing run as `… -k old_gate` with "1 test, 1 failure". No test name in
  the head holds `old_gate` (the new tests say `before_the_rename`), so that command as written would
  run no test. The run I made by the real names shows each test failing against its mutation, so this
  is only an inexact line in the report.
