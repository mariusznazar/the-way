# Handoff — review of the whole change, `defects-found-after-merge`

## Delegation and place

The person who requested this cycle has delegated intermediate choices to the orchestrator; nothing
here is that person's approval. You are read-only: change no tracked file, make no commit. Work in
the worktree `the task's worktree, which is the repository's root` (branch
`task/defects-found-after-merge`); start every command at its root. Scratch files go outside the
repository.

## Stage and method

Stage: the review of the whole change, by an agent that did not make it. Method:
`task-cycle/review/SKILL.md` of this worktree, whole; then `task-cycle/review/whole_change.md`
(the variant "the whole change"), whole. Read other files the method names only when the step that
names them comes.

Range: base `6814c6f6c9ff2b29d34612fa5cc86945ec3a2812` to head `10c0f9eed88d05b2cff8145d2c58227e94346c6d`
(four commits of the one author). The change is on the one-author route: no spec, no plan, no slices.
The process root is the-way itself; no pin moved.

## What the change must do

The frozen task, to read whole: `.runs/task-cycles/defects-found-after-merge/task.md` (Polish). Its
four *To do* items, the answers of *Questions to settle*, *Questions carried to cycle* and the eleven
accepted rows of *Settlements to record* are what to check coverage and source fidelity against —
each row has to stand written whole as a decision (or tied to an entry that already states it), and
the files must say what the rows say.

The author's report: `.runs/task-cycles/defects-found-after-merge/reports/author-report.md`.
Orchestrator's answers the author was given: trust boundary no, irreversible operation no; the new
kind of item of the request description is 17, placed in *You accept by merging* after kind 15; the
record item for corrections stands in *Request handoff* before `Process remarks on the-way`, which
stays the last item of the record.

## Gaps the orchestrator carries to you

- The author's **Unread material** says it read whole only part of the decisions whose *Scope* names
  `process-audit`, and did not read WAY-331, 332, 336, 338, 340, 341, 344 and 347 to 351 (it judged
  them by title as concerning the price list, the schedule, the results' place and the measures of
  context). Judge from your own selection whether any of them bears on the change, and read it whole
  where its title points to a bearing.
- The author's **Searches not found or unclear**: (1) the user's nightly review of cycles, which
  reads the record, is outside the repository, so only `task-cycle/remarks_check.py` and
  `process-audit/audit_count.py` were checked against the new record item; (2) `draft.md` as the
  place in the refinement skill that has the line filled is the author's judgment, no file lists the
  task document's header lines; (3) "fixing task" and "correction" have no glossary entry.
- The author edited WAY-287 in place (the task names it under *Decisions in play* with the change it
  makes). Check that the edit is only what the task says.

## Task-specific points to check

- Every file the change writes or edits says one thing: kind 17, the pair `source · kind`, the
  source `item <n>` as the number of a kind, the line `Defect introduced by:` and its forms, the
  classes `defect-found-at-request` and `defect-found-after-merge`, `after the merge` and `at the
  request` in *Stages*. Contradictions between the five new decisions, WAY-287 and the files are
  findings.
- The sentence in *Question settled* that a document written before the line has none and "no line
  means not assessed, not `none`".
- That the tests the author added test the form the readers accept and would fail on the break named
  in the author's report.
- No private path or note link in a committed file.

## Report

Write the full report to `.runs/task-cycles/defects-found-after-merge/reports/reviewer-report.md`.
Its first line is `PASS <sha>` or `FAIL <sha>` with the head's hash. Grade each finding (Critical,
Important, Minor) and name which are outside the task's scope; name for each blocking finding that it
comes from no slice (the one-author route). State how many decisions you read whole and how many by
title only, and list the checks you ran with command and exit code, your **Unread material**
and your **Searches not found or unclear** (each `none` where none). Return the first line of the
report, the report's path and a one-line check result.
