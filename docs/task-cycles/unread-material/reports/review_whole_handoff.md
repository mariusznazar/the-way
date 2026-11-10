# Handoff — review of the whole change

## Delegation

The person who requested this cycle (the-way's author) delegated intermediate choices to the
orchestrator. Nothing here is that person's approval. You judge; you change nothing.

## Where and what

Worktree: `the task's worktree` (read-only for you; work from
its root). This is the-way itself, with no `main`; read `agent-instructions/README.md` for the route.
Method: `task-cycle/review/SKILL.md` (project skill `the-way-review-change`). Stage: **the whole
change**. Read the `SKILL.md` whole, and `task-cycle/review/whole_change.md` when it tells you to.

Range: base `02c3d47f8891b66507687b40665b323f3d20def8` to head `afa43439b39b66fc1e737897b0c6b8b0e11aa129`
(two commits: `ca376a0` foundation entries, `afa4343` methods and template).
One-author route: no slices, no plan, no spec.

Frozen task (read whole): `docs/task-cycles/unread-material/task.md`
Author's report (read it): `docs/task-cycles/unread-material/reports/author_report.md`

Answers of the orchestrator's step 4: trust boundary — no; irreversible operation — no; no open
design choice, no reserved choice; one author without a plan.

Check coverage of every item of *To do* (points 1–4), every row of *Settlements to record* (rows
1–4, each as an entry of its kind) and source fidelity: the words the task quotes (the dopisek of
point 1 is quoted word for word; the dropped last sentence of the older note must not appear).

## Points the orchestrator wants judged (information, not grades — you grade)

- The author's report names choices and concerns; judge each against the task:
  1. row 4 written as an in-place edit of WAY-287 (not a new decision);
  2. the new request item numbered 14, not beside the skipped steps (to avoid renumbering the
     references by number);
  3. three ways not chosen added to WAY-150's *Rejected*;
  4. "closed on the way" meaning the reviewer or a fresh one read what stayed unread;
  5. the section named **Unread material** and placed before **Searches not found or unclear** in
     every method; the edge of `task-cycle/remarks_check.py` the author describes and left alone.
- **A gap carried to you (WAY-325's third-way test case):** the author's own report says it read
  65 of its 160 selected decisions whole and skimmed 94 by title only, did not read the glossary
  entries of the terms the work uses, and read WAY-82 in part. You select your own foundation and
  guidelines, so your reading closes this gap only as far as your selection covers it: read the
  glossary entries of the terms the change uses, and check the change against the decisions of its
  topic (the report cycle: WAY-148, WAY-150, WAY-159, WAY-213, WAY-260, WAY-286, WAY-287, and the
  two new ones) and against every decision of your selection whose title points at reports,
  handoffs, the request description or reading.
- Checks the author ran (it reports `task-cycle`, `elements/common`, `agent-instructions` and
  `instruction-files` directories green and the foundation check with 0 errors) are the author's;
  the orchestrator runs the full gate. You may run focused checks to verify a finding.

## What you read and how

You select your own foundation by "Reading the foundation" in `elements/common/way_of_working.md`
and the guidelines by `product-guidelines/reading.md` (this repository has no `guidelines/`; say
so under unread material if relevant). Your own reading follows the method as the branch states it
(`task-cycle/review/SKILL.md` section 1 now has the title-screening of decisions) — apply it, and in
your report count the decisions you read whole and those by title only.

## Your report

Write it to
`docs/task-cycles/unread-material/reports/review_whole_report.md`
as the method gives it. Its first line is `PASS <sha>` or `FAIL <sha>`, then `questions` if you
must ask. Include your checks with command and exit code, the reaches beyond the handoff, and
**Searches not found or unclear**. This method on the branch asks for a section about unread
material; as the method of the pinned checkout you run under is the branch itself, include it,
with the counts of decisions read whole and by title only. For each blocking finding, give the
file and line; findings graded Critical/Important/Minor; mark findings outside the task's scope.
Return the first line, the changed files with line counts, and the report path.
