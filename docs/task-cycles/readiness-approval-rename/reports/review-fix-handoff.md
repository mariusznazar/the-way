# Handoff to the reviewer — the review of the fix (once)

You are the reviewer of the whole change, resumed. Same worktree
`the task's worktree (the repository's root)`, same rules (read-only on the branch, no full gate,
delegation as before). Method: `task-cycle/review/SKILL.md`, the review of a fix.

**Range of the fix:** `79c9bfb95e772cb21810a78fc42607f99d726da0` (the head you reviewed) to `cef14df7`
(two commits: `8bb897b6`, `cef14df7`; 26 files, +196 −98).

**What the fix answers:** your three Minor findings within the task, in your words, in
`.runs/task-cycles/readiness-approval-rename/reports/fix-findings.md`. The author's fix report:
`.runs/task-cycles/readiness-approval-rename/reports/author-fix-report.md`. Your own earlier report is
`reports/review-whole-report.md`; the finding of yours that is outside the task's scope (the `entry` in a
record's list) is not part of this fix and is not fixed.

**What to judge.** Each of the three findings fixed as asked (finding 2: only lines the rename
lengthened were rewrapped, word for word, with no change of meaning and no other line touched; the
author says a whitespace-collapsed text of every touched Markdown file is the same before and after, and
lists the added lines left over 100 characters on purpose — judge whether that is right); no new
Critical or Important finding in the fix (only these count; a new Minor finding goes to the request's
list). Check particularly:
- the Python rewraps in `project-level/readiness_check.py` (the `STATUS` pattern split into two raw
  strings must be the same pattern; trust boundary: yes, crafted input as before — the old heading and old
  status still refused, nothing else accepted or refused differently), `plan_check.py`,
  `test_plan_check.py`, `test_plan_state.py`, `test_readiness_check.py`, `process-audit/audit_count.py`;
- the two new tests in `project-level/test_readiness_check.py`: the author cited
  `# invariant: project-definition-form` instead of `project-readiness-check` (its reason is in the fix
  report; judge it against the sentence of that invariant), and says it saw each fail against the old
  behaviour and pass; the test names say "before the rename";
- the author did not rerun every focused check after the second commit `cef14df7` (only
  `project-level/test_plan_check.py` and `foundation_check.py`); the fix report's Commits line was patched
  for that commit — run the affected focused checks yourself once, with command and exit code;
- no word of a decision's binding sentence or a skill description changed through the rewrap (a skill
  description rewrap would need the entry points regenerated: check
  `python -B agent-instructions/skill_entry_points.py`).

**Report** to `.runs/task-cycles/readiness-approval-rename/reports/review-fix-report.md`, first line
`PASS <sha>` or `FAIL <sha>`, with grades as before, **Unread material**, **Searches not found or
unclear** (`none` if nothing), the checks you ran with command and exit code, working copies (your
directory `.runs/review-fix/`; remove before returning and state it). Return only the first line, a
one-line check result and the report path.
