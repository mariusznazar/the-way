# Handoff — the return step, `review-structure-form-class`

## Delegation

You are the one author of this change, resumed for the return step (step 11 of the cycle). The orchestrator is the one you ask; no human answers
during the cycle. The review of the whole change (`FAIL 5353268`) and of its fix (`PASS c6af26a`) are done; the head to compare is `c6af26a`.

## Where

- Worktree (work from its root, and nowhere else): `the worktree's root`; branch
  `task/review-structure-form-class`; base `65b6d70`; head `c6af26a`.
- Report path (write your full report there): `docs/task-cycles/review-structure-form-class/reports/return-step-author-report.md`

## Method

Read `task-cycle/skill/return_step.md` whole and follow it, with `task-cycle/skill/foundation_step.md` (read it whole too, since the return step
writes as the foundation step writes). Read the skill of an element only when you write an entry of that element.

## What to compare

With the files at `c6af26a` (the fix included): WAY-355 to WAY-360, WAY-229 and WAY-164 (as the fix and the foundation step left them), the ten entries
of the task's *Decisions in play* that the change does not edit (WAY-161, WAY-297, WAY-263, WAY-51, WAY-135, WAY-16, WAY-271, WAY-278, WAY-168,
WAY-173, WAY-203, WAY-05, WAY-27, WAY-328 — compare each with the new entries, none edited), the part map entries of `task-cycle`,
`product-guidelines` and `decisions`, the glossary words the change uses (`standing check`, `binding sentence`, `open design choice` and any other
you meet — a term used against its entry takes the use corrected), and the invariants of the touched parts. Search the whole foundation and the
files of `task-cycle/` and `product-guidelines/` once more for a sentence that still lists what the review of the whole change checks, what the
plan begins with, or what the template of coding guidelines requires, and no longer matches the new files (for instance `task-cycle/skill/*.md`,
`product-guidelines/audit_end.md`, `product-guidelines/template.md`, `task-cycle/review/SKILL.md` section 2, `process-audit/`). Correct in the same
change what no longer matches; write nothing the task does not carry except what the return step's rules give. Rows of *Settlements to record*:
check that each of rows 1–6 is written (WAY-355 to WAY-360) and name the row of each.

## Boundaries

- Commit only if you correct something; naming files by path, never `git add -A`; messages in English in the form of the existing log; do not push.
  No commit is a result: say so. Do not run the whole gate. Run `python -B elements/common/foundation_check.py` (exit code in the report) and the
  focused checks for what you change, each with command and exit code.
- Report as `return_step.md` and `make-change` give: status, commits (or none), the entries compared and what no longer matched with its
  correction, the fields of the record's *Return step* (decisions, invariants, environment facts, glossary terms, part-map changes, projected entries,
  rows written), **Unread material** and **Searches not found or unclear** (each `none` where there is nothing). Write the report to
  `return-step-author-report.md` only.
- Do not start any next stage.
