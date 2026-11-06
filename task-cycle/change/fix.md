# Fixing a review's findings

What the fix of a review's findings reads and reports, and what it does with a finding of a reserved
choice.

## Read

- For a fix, the findings file — the blocking findings of the review, and after them, in the fix
  after the review of the whole change, its Minor findings within the task — and the code it names.
  A finding the file does not hold is not yours to fix: the review's out-of-scope findings and its
  other Minor findings (WAY-161).
- Make the fix of a Minor finding as small as the finding asks. A fix that grows beyond its
  findings is the likeliest to draw a new serious finding, and a new Critical or Important finding
  in a fix made for Minor findings alone gives the whole fix up.

## A finding of a reserved choice

- For a finding that the change takes a reserved choice, the fix removes the choice from the change.
  Where you cannot remove it, return the status `reserved`, as section 5 of `SKILL.md` gives.

## Report

- For a fix, the report holds each finding of the file as fixed — how, with the check that shows
  it — or contested, with the evidence. A Minor finding you hold wrong, or cannot fix within the
  task, is contested the same way; it blocks nothing and goes to the request's list.
