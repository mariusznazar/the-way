PASS ff70e690d155eb98ba6dd6a5be23275ed0f50285

# Review of correction 1 (the human's remarks) - code-order-formatter-linter-size

Range `34d9970e..ff70e690`, two commits: `65ef8dd5` (four test names of `process-audit/test_audit_count.py`) and
`ff70e690` (*Relations* of WAY-385). `git rev-parse HEAD` gives `ff70e690d155eb98ba6dd6a5be23275ed0f50285`, the head
given. Changed files: `process-audit/test_audit_count.py` 4 insertions, 4 deletions; `foundations/decisions.md`
1 insertion, 1 deletion.

## The remarks

Bound by `reports/correction-1-remarks.md`, read whole.

- **Item 3, first point — four test names that say "entry": made.** Lines 545, 556, 1428 and 4986 now read
  `..._is_not_among_its_sub_items`, `..._are_not_its_sub_items`, `test_a_sub_item_of_review_rounds_...`,
  `test_crafted_sub_items_of_review_rounds_...`, the word of `process-audit/test_record_items.py` and of the record
  template. The diff of the file holds the four `def` lines and no other line (a search of the diff's changed lines
  without `def test_` finds none), so no assertion, expected value or `decision:` / `invariant:` line changed
  (WAY-233, WAY-03); the fourth test's `decision: WAY-404 "... the sub-item of the round ..."` line stands as it was
  and now agrees with the name. `git grep` of the four old names over the repository outside `.runs/` finds nothing.
  The `entry` words left in the file (lines 982-994, a key of the locations file; 1274-1276, a line of a JSON
  transcript; 4730, 4772, 4861, "foundation entries" in plan texts) are no item of a record's list.
- **Item 3, second point — WAY-385 names WAY-382: made.** `foundations/decisions.md:10796` now reads
  `derives from WAY-379 · derives from WAY-360 · derives from WAY-361 · derives from WAY-382`; the diff of the file is
  that one line, so the binding sentences, *Scope*, *Based on*, *Verification*, *Origin*, *Rationale* and *Rejected*
  are unchanged. The type is right by `elements/decisions/template.md`, "Relations and precedence" (lines 225-242):
  the list is closed to `derives from` (a higher decision this one serves) and `narrows` (a decision this one
  deliberately goes against in a narrower area, with the area stated in the binding sentences of the one that
  prevails). WAY-385 goes against nothing of WAY-382: its sentence counts lines "on the code as the formatter of
  WAY-382 leaves it", so it rests on WAY-382 and serves it, and states no area of precedence; `narrows` would record
  a collision that does not exist. The relation stands in the entry that depends on the other (WAY-18) and names it
  by its number alone (WAY-02). WAY-382's *Relations* (`derives from WAY-379 · derives from WAY-173`) names no
  relation back, so no mutual relation arises.
- **Items let through — untouched.** The range changes only the two files above, and in `test_audit_count.py` only
  the four `def` lines: the brackets of the `except` lines, the fix of the flaky test
  (`task-cycle/test_remove_merged_worktrees.py`, empty diff) and `installation/install.py` (`plan` at 109 lines,
  empty diff) are untouched.

## Findings

### Critical

none

### Important

none

### Minor

none

## Declined to judge

none

## Checks

| Command | Exit |
|---|---|
| `git diff 34d9970e..ff70e690` (and `--stat`) | 0 (two files, 5 insertions, 5 deletions) |
| `git diff 34d9970e..ff70e690 -- process-audit/test_audit_count.py \| grep -E '^[+-] ' \| grep -v 'def test_'` | 1 (no changed line other than the four `def` lines) |
| `git grep -n -E 'is_not_among_its_entries\|are_not_its_entries\|an_entry_of_review_rounds\|crafted_entries_of_review_rounds' -- . ':!.runs'` | 1 (not found) |
| `git diff 34d9970e..ff70e690 -- installation/install.py task-cycle/test_remove_merged_worktrees.py` | 0 (empty) |
| `python -B elements/common/foundation_check.py` | 0 ("0 errors") |
| `python -B gate/run_tests.py process-audit` | 0 (277 tests, OK, 362 s) |

The full gate was not run (the dispatch forbids it). The new *Relations* line is 109 characters, where the log wraps
most lines near 100; two other *Relations* lines of the log already run past 100, no rule of width binds the log, and
`foundation_check.py` parses it, so this is no finding.

## Reaches beyond the dispatch

- `elements/decisions/template.md`, the line of the form of *Relations* (line 36) and the section "Relations and
  precedence" (lines 225-242): named by the dispatch as the rule to judge by; read those passages, not the whole file.

## Working copies

`.runs/review-correction/` of the worktree held the outputs of the two runs (`fc.txt`, `pa.txt`). No worktree, clone
or screenshot was made. The directory was removed before return; nothing remains.

## Unread material

- `elements/decisions/template.md`: read at lines 36-108 and 225-244, not whole.
- `process-audit/test_audit_count.py`: read at the diff and the lines a search for `entr` found, not whole.
- The fixer's evidence in `reports/fixer-correction-checks/`: not read; the runs were repeated instead.

## Searches not found or unclear

- The four old test names outside `.runs/`: not found (the expected result).
