# Correction 1 report — installer-preview-ignores-line-endings

**Status:** done
**Commit:** `bafe8ad9` on `task/installer-preview-ignores-line-endings` (on top of `81a21f51`; not pushed)

## The remark

Fix item 1 of the request: the table row of the agent definitions in `installation/README.md` was broken
over two lines by the earlier fix, so the row was cut after "as git stores them,".

## What I did

I joined the two lines with one space, at `installation/README.md:60`. The words are unchanged. No other
line changed. The row now reads "… byte for byte as git stores them, and name no commit; a checkout may
write them with CRLF line endings, which the installer keeps as they are. …".

## Checks

- `git diff` (command: `git diff`): one hunk, `@@ -60,2 +60 @@`. It removes two lines and adds one, the
  joined row. Exit 0.
- `git diff -U0 | grep '^@@'`: one hunk only, so no other line changed.
- Table rows: the rows above (`:57-59`) and below (`:61-63`) are unchanged, as the diff shows.
- Tests: not run. The change is README text only, and the handoff asks for no test; I did not touch any
  other file, so `python -B gate/run_tests.py installation` was not needed.

## Own-work check

- Requirement: the row renders whole, with the same words and no other change. Check: `git diff` above
  shows one hunk of two lines removed and one added, and the joined text is the old two lines with one
  space. Result: passes.

## Unread material

- `reports/correction-1-remarks.md`: read whole (the remark, word for word).
- `task-cycle/change/SKILL.md`: read in an earlier round of this session; the correction variant
  (section 1, "a correction for the human's remarks") and section 6 (the report) were applied from it.
- Nothing else.

## Searches not found or unclear

- None.

## Working copies

- None made. `.runs/author/` is untouched in this step.
