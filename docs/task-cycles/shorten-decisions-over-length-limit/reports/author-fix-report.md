# Author fix report — shorten-decisions-over-length-limit

## Status

`done`

## Commits

Range `ef8aa061..644cbe51`:

- `644cbe51` — Rewrap the raw lines of the new paragraphs of the ten divided decisions and of WAY-287 to 100 columns.

File changed: `foundations/decisions.md`, 174 added and 180 removed lines (line breaks only). No test file, no other file.

## Findings

Minor 3 of the review (the raw lines of the new paragraph breaks are not rewrapped) — **fixed**.

How: a script of mine (`rewrap_breaks.py`, removed afterwards) took, for each of the ten entries and WAY-287, the binding sentences at the base and at the head, and rewrapped at 100 columns (break at a space, `textwrap` with no break of words or at hyphens) every paragraph of the head whose words are no paragraph of the same entry at the base, that is, both halves of each division and the first paragraph of WAY-287 whose lines ran past 100 columns. Paragraphs that the division left whole were not touched, nor were the blank lines, fields, *Rationale*, *Rejected*, WAY-344 and WAY-416. A first run also removed the blank line after a heading (the script stripped the leading newline of the first paragraph); I saw it in the hunks, reset the file and ran the corrected script, so the committed change has none. The twelve places of the finding are in the 12 hunks of the diff (WAY-148's break stood at a line start and needed only its blank line, which the hunks show as a join with a neighbour).

Shown by: the word-for-word comparison and the counts below.

## Checks

- `python -B .runs/author/compare_binding.py` — exit 0. The ten entries identical to the base except `first` -> `second` in WAY-150; WAY-287 `document —` -> `document. The section stands`; WAY-19, WAY-344 and WAY-416 as before (paragraphs 210 + 131 and 257 + 195 words).
- `python -B .runs/author/compare_prose.py` — exit 0; same result as before (nothing dropped from WAY-344's *Rationale*, *Rejected* or *Verification*).
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`, no line `listed:`.
- Counts in the eleven entries touched (my script `line_stats.py`, removed afterwards; a stub line is a non-blank line under 20 characters), at `ef8aa061` and after the fix:

| Where | Lines over 100 columns before -> after | Stub lines before -> after |
|---|---|---|
| binding sentences of the eleven entries | 11 -> 0 | 7 -> 5 |
| whole entries (fields, *Rationale*, *Rejected* too) | 27 -> 16 | 23 -> 21 |

  The five stub lines left in the binding sentences are the last lines of paragraphs, which end on a short line where the paragraph's words run out ("the whole list." in WAY-289, "their domain." in WAY-150, "out of them." and "*Rejected*." in WAY-134, "the lower part." in WAY-287); none is a stub at the start or in the middle of a paragraph. The lines over 100 columns and the stubs left in the whole entries stand in fields, *Rationale* and *Rejected* that the division did not touch, and are not part of the finding.
- Not run: any test directory (no test file changed), the full gate (WAY-160), ruff (not installed).

## Own-work check

- Requirement most likely unmet: "change no word, no sentence, only line breaks move".
- Check: the word-for-word comparison above (exit 0, same result as at `ef8aa061`), the count of added blank lines in the diff (the hunks keep each blank line between paragraphs), and the line numbers of the hunks, none of which falls in WAY-344 or WAY-416.
- Showed: no change of words; the foundation check still passes.

## Reaches beyond the handoff

none

## Working copies

Made in `.runs/author/`: `rewrap_breaks.py`, `line_stats.py`, the text of the commit message; all removed. Left, as the handoff asks: `compare_binding.py` and `compare_prose.py`.

## Unread material

`task-cycle/change/fix.md` read (the first 25 lines, which hold the whole of what it gives); the handoff and the findings file read whole; nothing else named.

## Searches not found or unclear

none
