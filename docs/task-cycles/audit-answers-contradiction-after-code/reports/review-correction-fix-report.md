PASS 47a47fecbeec3957b13bf7b34eb120f5b035e0b1

# Review of the fix of correction 1 — audit-answers-contradiction-after-code

- Range: base `b3bd8f4e1b401ab38ccf6e22f2fa96847c508490` to head
  `47a47fecbeec3957b13bf7b34eb120f5b035e0b1`, one commit (`git rev-parse HEAD` in the reviewed worktree
  gives the head; the worktree is clean). Files: `process-audit/record_items.py`,
  `process-audit/test_record_items.py`.
- Method: `review-change` (`task-cycle/review/SKILL.md`) with `task-cycle/review/fix.md`; the findings
  file `reports/review-correction-findings.md` (R-1 alone) bounds the review.
- Counts: 0 blocking, 1 Minor (new in the fix, within the task), 0 out of scope. Of the findings file:
  R-1 fixed.

## The findings of the findings file

### R-1 — fixed

- The predicate now reads `alone = lines[0][1] is not None and lines[0][0] == base and all(...)`
  (`process-audit/record_items.py:234`): the first line under the item must be an entry at the
  entries' indent, which is the fix the finding gives. The docstring (`:223-227`) states why a first
  line deeper than the entries after it continues nothing.
- The record of the finding (first entry `open design choice` deeper, then `size`) and the same with a
  third entry `reserved choice` give `unknown` at the head; at `b3bd8f4` both gave `('no', None)`
  (probe below). So do the same shapes with a numbered list, with a tab-indented first entry (tabs
  become 4 spaces in `split_lines`), with a fenced block before the deeper entry, with control
  characters in the first entry, and with a 2,000,000-space indent on the first entry.
- **The reason fits both cases.** It now reads "a line of the item `Discarded attempt` is no entry or
  stands at another indent than its entries: write each attempt as an entry, all at one indent, and
  nothing else beside them" (`:257-259`). For a plain line beside the entries, "is no entry" holds; for
  a first entry deeper than the rest, "stands at another indent" holds. The two earlier assertions
  of the old wording (one in a loop of three records) now assert the new one through the constant
  `BESIDE` (`test_record_items.py:15`, `:163`, `:202`); their records are unchanged.
- The test the finding asks for: `test_an_entry_first_under_the_item_and_deeper_than_the_next_one_is_not_dropped`
  (`test_record_items.py:171`), four records, each `unknown` with that reason, and the same entries at
  one indent giving `yes`. With the test file of the head on the code of `b3bd8f4`,
  `python -B -m unittest test_record_items` fails with `FAILED (failures=8)`, the four subtests of this
  test among them, so it fails when the defect is back.
- **No right answer of `b3bd8f4` lost** among those the handoff names: the six records of
  `test_audit_count.ProcessVersions.test_the_marker_of_a_discarded_attempt_gives_q1` (held by the
  `process-audit` run, exit 0); the sub-entry case `deeper` (`test_record_items.py:210-212`, unchanged,
  `no`), joined by a new test of a sub-entry under the first entry with an entry after it
  (`:191`, `no`); the details-as-a-list form (`yes` for `open design choice`, `no` for `size`, probe and
  `:142`); the four denials of review #100 (the `process-audit` run). The probe also shows unchanged
  answers for the record of I-2 (`unknown`, two reasons), one or two entries at one indent, the item's
  line reading a marker or `none`, text beside the entries, and an entry reading `none`.
- **No new wrong `yes` or `no`:** across 30 crafted records at the head against `b3bd8f4`, every answer
  that changed went from `yes` or `no` to `unknown`; none went to a different `yes` or `no`, and none
  from `unknown` to an answer. No hang: 100,000 entries with a deeper first entry 0.16 s, 100,000
  entries of alternating indents 0.18 s, a 2,000,000-space indent 0.02 s, 50,000 markers in a deeper
  first entry 0.01 s; no crash; every reason a fixed string.

## New findings in the fix

### Minor

**N-1 (within the task). Two answers that were right at `b3bd8f4` by chance are now `unknown`, and the
author's report says something the code does not do.**

- A record whose first entry is deeper and whose entry at the base is `open design choice` — e.g.
  `    - reason: \`size\`` then `  - reason: \`open design choice\`` — gave `yes` at `b3bd8f4` and gives
  `unknown` at the head (probe: `deeper size first, odc`, and `zigzag size4 odc2 size4`). The `yes` was
  true of the record, but it came from the same dropping of the first entry that R-1 named, so it was
  no reading the code could stand behind; `unknown` is the answer the finding asked for, and no wrong
  answer results. Noted only because the handoff asks about answers lost.
- The author's report, *The own-work check*: "A first entry shallower than the later ones gives
  `unknown` by the same condition (the first line is not at `base`)". It does not: a first entry
  shallower than the later ones is at `base`, the later ones are its sub-entries and are not read, as
  the test `deeper` requires (probe: `shallower first odc, deeper size` gives `yes`, `shallower first
  size, deeper odc` gives `no`, as at `b3bd8f4`). The behaviour is the one the earlier review kept as
  Minor M-1 (`reports/review-correction-report.md`); only the claim is wrong, and no code or test rests
  on it.

## Declined to judge

none

## Checks run

In a worktree of the head,
`the root of the task's worktree\.runs\review-correction-fix\head`:

- `python -B gate/run_tests.py process-audit` — exit 0, 269 tests, OK.
- `python -B gate/run_tests.py task-cycle` — exit 0, 534 tests, OK (1 skipped: Windows gives a killed process no signal number).
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- Manual: a probe script running `record_items.read_contradiction` on 30 crafted records at the head and
  at `b3bd8f4` (a second worktree), as listed above.
- Manual: the head's `test_record_items.py` run on the code of `b3bd8f4` (in the worktree of
  `b3bd8f4`): `python -B -m unittest test_record_items` in `process-audit` — exit 1,
  `FAILED (failures=8)`, 31 tests.
- Not run: the product's full gate, by the handoff.

## Reaches beyond the dispatch

None: the fix's two files, the findings file, the fix report and my own earlier report.

## Working copies

Two detached worktrees under
`the root of the task's worktree\.runs\review-correction-fix\` —
`head` (47a47fe) and `prev` (b3bd8f4, with the head's test file copied in for the failing run) — and the
probe script, its outputs and the check outputs in the same directory. The head's test file in `prev` was put back with `git checkout`, then each worktree
was removed with `git worktree remove --force` (exit 0 for each), then `git worktree prune`, and the
directory `.runs/review-correction-fix/` deleted; `git worktree list` names neither and the reviewed
worktree is clean. No remainder. Nothing kept in `reports/`: the probe's records and answers that
the report needs stand in it.

## Unread material

- `process-audit/test_record_items.py`: the diff and the tests of the item *Discarded attempt* around
  it, not whole. Nothing else of the dispatch left unread.

## Searches not found or unclear

none
