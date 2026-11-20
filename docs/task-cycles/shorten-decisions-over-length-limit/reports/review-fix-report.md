PASS 644cbe517f92a837201ea91a57d21dac88ea5fd7

# Review of the fix — shorten-decisions-over-length-limit

Range: `ef8aa061..644cbe51` (one commit, `644cbe51`). `git rev-parse HEAD` =
`644cbe517f92a837201ea91a57d21dac88ea5fd7`, as dispatched. The change touches one file,
`foundations/decisions.md` (174 lines added, 180 removed). No other file and no test changed.

## Findings of the findings file

- **Minor 3 (the new paragraph breaks are not rewrapped in the raw text) — fixed.** I read each of
  the twelve division points at the new head:
  - The paragraph after each break now opens on a full line. WAY-150 at 1671 opens "Of the decisions
    it finds by *Scope*, …", WAY-405 at 8819 opens "Where the lines under the item …", and WAY-154 at
    5667 opens "Agent turns, questions and explicit waits …".
  - Each paragraph before a break ends where its words run out.
  - WAY-287's two long lines now wrap: the first paragraph ends at 7684, and the second opens at 7686.
  - Of the 168 lines the fix adds, none is over 100 characters (counted in characters, not bytes).
  - The only short added lines are the last lines of paragraphs ("out of them." at 5478, "the lower
    part." at 7696), not stubs at the start or in the middle of a paragraph.

## New findings in the fix diff

none. The fix changes line breaks only. My own check over the whole log, comparing `ef8aa061` with
`644cbe51`, found:

- the log has 1070 blocks separated by blank lines both before and after the fix;
- each block holds the same words in the same order, line breaks apart;
- the words of the whole file are identical;
- the count of blank lines is 1069 before and after.

So no word of any entry changed in binding sentences, fields, *Rationale* or *Rejected*. No blank line
was added or removed: not between a heading and its first paragraph, not between paragraphs, and not
before a field. The author's report says a first run of its script had dropped the blank line after a
heading. That is not in the committed change: the block comparison would show it.

## Declined to judge

none

## Checks run

- `git rev-parse HEAD` — `644cbe517f92a837201ea91a57d21dac88ea5fd7`, exit 0.
- `git diff --stat ef8aa061..644cbe51` — only `foundations/decisions.md`.
- `python -B .runs/review-whole/cmpfix.py` (my own script) — exit 0. It reads the log at both commits
  and compares three things: the blocks between blank lines (words only), the words of the whole
  file, and the count of blank lines. It also lists added lines over 100 characters or under 20.
  Results are as given above.
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`, no `listed:` line.
- Manual: I read the two lines on each side of the twelve division points at the new head.
- Not run: test directories (no test file changed); the full gate (CI's, WAY-160); ruff (not
  installed, and no Python file changed).

## Reaches beyond the dispatch

none

## Working copies

`.runs/review-whole/cmpfix.py`, its output `cmpfix_out.txt` and `fc.txt` (the output of the foundation
check) were removed after this report was written. The directory is left empty.

## Unread material

none. The handoff, `task-cycle/review/fix.md`, the findings file and the fix report were read whole.
The fix diff was checked in full by the comparison script and by reading each division point.

## Searches not found or unclear

none
