PASS bafe8ad993136690789e361159e716c08af0371b

# Review of correction 1 — installer-preview-ignores-line-endings

- Range: `81a21f51..bafe8ad993136690789e361159e716c08af0371b`, one commit, "Join the agent
  definitions row of the installer README on one line", touching `installation/README.md` alone.
  `git rev-parse HEAD` in the worktree gives the head the dispatch names.
- Bound: the human's remarks, `reports/correction-1-remarks.md`, one remark. Only a new Critical or
  Important finding in the correction's diff fails this review.
- Counts: blocking 0, Minor 0, out of scope 0.

## The human's remarks

1. **Made.** The remark asks to join the two lines of the agent-definitions row so the row renders
   whole. `installation/README.md:60` is now one line. It equals the old line 60, one space, and the
   old line 61, word for word: a script comparison gave `True`, and neither old line had a space at
   the join. Every other line of the file is identical between `81a21f51` and `bafe8ad9`. The file
   went from 309 to 308 lines, and `git diff --stat` shows one insertion and two deletions. The table
   "Files in the product" (`:50-63`) has the header, the delimiter row and twelve rows. Each starts
   and ends with `|` and has two cells outside code spans, as the header does. The line after the
   table is blank. So row 60 renders as one table row, and no other row changed.

The correction also introduces nothing new. The text is the text the fix review already found true,
and the file still has LF line endings only. Between `ee4cbe35` (the head of the fix review) and
`81a21f51`, `installation/` did not change: `git diff --stat ee4cbe35..81a21f51` is empty for it
(that range adds and removes the cycle's record).

## New in the correction's diff

### Critical

none

### Important

none

### Minor

none

## Declined to judge

none

## Checks run

| Check | Command | Exit | Result |
|---|---|---|---|
| Head of the range | `git rev-parse HEAD` | 0 | `bafe8ad993136690789e361159e716c08af0371b`, as dispatched |
| Log and diff | `git log --oneline 81a21f51..HEAD`, `git diff --stat 81a21f51..HEAD`, `git diff 81a21f51..HEAD` piped to `cat -A` | 0 | one commit; `installation/README.md`, 1 insertion and 2 deletions in one hunk |
| Row, other lines, table form | `python -B .runs/review-whole/check_row.py <worktree> 81a21f51 bafe8ad9`: compares the row with the old two lines joined by one space and the other lines with each other, and counts each table line's cells outside code spans | 0 | joined row `True`; other lines equal `True`; no CRLF; table `:50-63` with 2 cells on every line, each line starting and ending with `\|`; blank line after the table |
| Nothing else changed since the fix review | `git diff --stat ee4cbe35..81a21f51` | 0 | no change under `installation/` |
| Reviewed worktree untouched | `git status --short` | 0 | empty |

Not run: tests, since the correction changes README text alone and the dispatch asks for none; and
the full gate, which the dispatch forbids. The rendering itself was not viewed on GitHub. The table
form was checked by its pipes and cells, as the dispatch gives.

## Reaches beyond the dispatch

none

## Working copies

The comparison script `check_row.py` was in
`.runs/review-whole/` and was
removed. Its output is quoted in the checks above. The directory stays, empty. No worktree or clone
was made.

## Unread material

- `installation/README.md` beyond the table (`:50-63`) and the diff was not re-read. The script
  compared every other line of the file between the two commits.
- Otherwise none: the remarks, the author's correction report and the whole diff were read whole.

## Searches not found or unclear

none
