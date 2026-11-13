# Handoff — close the unread material of the review of the whole change

You reviewed the whole change (head `2c27260`; its fix `faee0f8` passed too). Your report's **Unread material** says you read 23 decisions whole, ran no pass by title
through the rest of the 323, did not read WAY-33, WAY-35, WAY-36, WAY-77, WAY-78, WAY-80, WAY-114 and WAY-150 whole (some bear on reflowed sentences),
read only part of the invariants, the part-map entries `invariants` and `glossary`, and the glossary entries of the words the changed sentences use, and read `elements/common/rules.md`, `elements/decisions/template.md` only by grep lines.

Close that gap now, as `task-cycle/review/whole_change.md` and WAY-150 give it, on the final head `faee0f8` of `task/close-decision-pending-templates`
(worktree `the root of the task's worktree`):

1. run through all decisions of the selection by title, open and read whole every one whose title points to a bearing on the change, and read whole the eight named above;
2. read whole the remaining invariant entries of the touched parts, the `invariants` and `glossary` part-map entries, the glossary entries of the terms the changed sentences use, and `elements/common/rules.md`;
3. judge again, against what you read, whether the change (range `fca8491`..`faee0f8`) breaks, contradicts or leaves stale any of it.

Write the result to `reports/gap-review-report.md` in the record directory. First line `PASS <sha>`, `FAIL <sha>` or `questions`; list any new finding with its grade
and place, and count the decisions you read whole and by title this time. Same sections as before: checks with command and exit code, Unread material and Searches not found or unclear.
