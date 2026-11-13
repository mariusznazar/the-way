# Report — merge of `origin/foundations` into the request's branch (correction 1)

**Status:** done

**Merge commit:** `73fb11d` ("Merge foundations into task/defects-found-after-merge, renumber this
branch's decisions WAY-353 to WAY-357 as WAY-355 to WAY-359"). Parents: `a3152c9` and
`65b6d7007ec4fffad998612e5c521eee93c7b8b5`.

## What was done

- `foundations/decisions.md`: the conflict (one block) resolved by keeping the target branch's
  WAY-353 and WAY-354 unchanged first, then this branch's five decisions in their order, renumbered
  353→355, 354→356, 355→357, 356→358, 357→359 in one pass of a regular expression (so no number was
  changed twice). Every reference inside the five (*Relations*, rationale, verification text) was
  renumbered with them: 8 numbers inside the block (WAY-354→356 in WAY-356's text "of WAY-353"→355;
  WAY-358's "as WAY-353 gives it"→355; WAY-358's *Relations* WAY-355→357; plus the five headings).
  No decision of the target branch changed. No conflict marker remains.
- The reference outside the block that this branch wrote: WAY-287, `(WAY-356)` → `(WAY-358)`,
  1 line (`foundations/decisions.md`, line 9176).
- Lines of this branch's other files (identified from `git diff 6814c6f a3152c9`, renumbered by
  line, so that the target branch's own WAY-353 mentions were left):

| File | Lines changed |
|---|---|
| `foundations/decisions.md` | 9 numbers' lines (8 in the five decisions, 1 in WAY-287) |
| `project-level/task/skill/draft.md` | 2 lines (354→356, 353→355) |
| `project-level/task/template.md` | 2 lines (354→356, 353→355) |
| `task-cycle/record_template.md` | 2 lines (355→357, 356→358) |
| `task-cycle/skill/correction.md` | 2 lines (355→357; 355,356→357,358) |
| `task-cycle/skill/request_template.md` | 1 line (kind 17: 356→358) |

  Not changed on purpose: the target branch's WAY-353 mentions in `draft.md` line 35,
  `template.md` line 234 and `final_review.md` line 10, and its WAY-354 mentions in `foundation-review/`.
  `process-audit/problem_register.md`, `process-audit/test_audit_count.py` and
  `task-cycle/test_remarks_check.py` held no such number.

## Step 3: do the two sides hold together

Read `git diff 6814c6f origin/foundations` for the four files:

- `task-cycle/skill/request_template.md`: the target branch added a fifth part to "What an item
  carries" for a kind 4 item (a check the human can do by hand), a sentence in kind 4 and an example.
  It added no kind and renumbered none; kind 17 and my sentence for `target-branch · none` stand
  where they were and do not touch its parts. Merged without conflict. No correction.
- `project-level/task/template.md`: the target branch added a closing paragraph (pointing at a place
  to change by heading or quotation); this branch added the line `Defect introduced by:` in the
  header and its explanation at lines 101 to 108. Different places, no collision. No correction.
- `project-level/task/skill/draft.md`: the target branch added a paragraph after the one on Context;
  this branch's fill-in step stands before it. The two read in sequence and do not repeat or
  contradict each other (read lines 14 to 42). No correction.
- `foundations/glossary.md`: the target branch added the term "transitional state". This branch
  writes no glossary entry and uses that term nowhere. No correction.

## Step 4: stale references

`git grep -n "WAY-35[3-9]"` over tracked files after the renumbering, read against the table: the
remaining hits are the target branch's WAY-353 (`draft.md:35`, `template.md:234`, `final_review.md:10`)
and WAY-354 (`foundation-review/*`), and this branch's renumbered ones. In `decisions.md` the only
remaining numbers 353 to 359 are the headings and the references within the renumbered decisions and
WAY-287. No stale reference found.

## Checks

- `python -B elements/common/foundation_check.py --skip-test-citations .` — exit 0, 0 errors.
- `python -B gate/run_tests.py task-cycle` — exit 0 (367 tests OK).
- `python -B gate/run_tests.py process-audit` — exit 0 (180 tests OK).
- `python -B gate/run_tests.py project-level` — exit 0 (275 tests OK).
- `python -B gate/run_tests.py elements/common` — exit 0 (144 tests OK).
- `python -B gate/run_tests.py agent-instructions` — exit 0 (18 tests OK).
- `python -B gate/run_tests.py foundation-review` — exit 1 with "no test found in foundation-review":
  the directory holds no test file; this is no failing test.
- `git diff --check` — no output. Full gate not run, no review started.

## Questions

none

## Concerns

- The kind 17 sentence I wrote in correction 1 does not name a decision number, so the renumbering
  did not touch it.
- The line count in the commit's file list for `decisions.md` includes the target branch's decisions
  that the merge brought in.

## Unread material

none (the five decisions and WAY-287 were read whole earlier in this session under their old
numbers; the target branch's WAY-353 and WAY-354 were read for their headings and the boundaries of
their blocks, and each was left byte for byte as the target branch has it)

## Searches not found or unclear

none
