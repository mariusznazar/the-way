# Findings of the review of correction 1, for the fix

Cut word for word from `reports/review-correction-report.md` (head `b3bd8f4e1b401ab38ccf6e22f2fa96847c508490`): the blocking finding only. The Minor findings of a review of a correction are not fixed (they go to the request's list).

### Important

**R-1. An entry indented deeper than the next one, standing first under the item, is dropped: an
item whose first entry is `open design choice` gives Q1 `no`.** (Within the task; it counts as I-2
remaining, WAY-162.)

- Place: `process-audit/record_items.py:233-234`, the new predicate of the correction:
  ```python
  alone = lines[0][1] is not None and all(
      marker is not None or indent > base for indent, marker in lines)
  ```
  It asks that the first line be an entry, not that it stand at the entries' indent (`base`, the
  smallest indent of an entry). A first entry deeper than `base` passes, and `discarded_entries` then
  returns only the entries at `base` (`:235`), so the first entry is passed over in silence. The
  docstring's reason for letting deeper lines through — "A plain line deeper than the entries continues
  one of them" (`:225-226`) — does not hold for a line that comes before any entry at `base`: there is
  nothing for it to continue.
- Evidence (my probe at the head, `read_contradiction` on the record):
  ```
  - Discarded attempt:
      - reason: `open design choice`
    - reason: `size`
  - Review rounds: none
  ```
  gives `('no', None)` at the head and at `428cc45`; at `ab2c8c8` it gave `unknown`. The same with a
  third entry `- reason: \`reserved choice\`` gives `('no', None)`. As Markdown, the two lines are two
  entries of one list under the item (the first is indented by 2 within the item's content, the second
  by 0, and the second is no continuation of the first), so the record holds two attempts, one of them
  an open design choice.
- Why it matters: a false `no` for a cycle that had an open design choice — the answer on which the
  human weighs whether a cycle needed a spec, and the kind of answer the remark says this task removes.
  The handoff asks that crafted input with deeper and shallower indents give no wrong `yes` or `no`;
  `record_items.py` reads lines from git history and calls them untrusted (`:4-5`). Writing the first
  entry at a different indent than the ones added later is an ordinary slip when a leader adds an
  entry to a list it wrote in an earlier turn.
- Fix, checked: add `lines[0][0] == base and` to the predicate. In a worktree of the head with that
  one change, the probe gives `unknown` for both records above, and
  `python -B -m unittest test_record_items` in `process-audit` passes, 29 tests (the test
  `deeper` at `test_record_items.py:183-185`, a sub-entry under an entry at `base`, still gives `no`).
  The reason it then gives, "a plain line stands beside the entries", is wrong for a line that is an
  entry; a reason that names lines at another indent than the entries fits both cases. A test with the
  record above.
- Contradiction: yes — WAY-404 (the reason stands "at the start of each entry under the item, one
  entry for each attempt", and its *Verification*: "an item of several entries gives yes where any of
  them has the marker `open design choice`") and the task's *To do* 3 (`yes` where *Discarded attempt*
  has the marker `open design choice`).
