# Handoff to the author — the fix of the Minor findings of the whole-change review

You are the one author, resumed. Same worktree `the task's worktree (the repository's root)`,
branch `task/readiness-approval-rename`. Your variant: **the fix of a review's findings**
(`task-cycle/change/SKILL.md`, row "the fix of a review's findings"; read `task-cycle/change/fix.md`
whole). The delegation, the answers of step 4 (trust boundary: yes; irreversible operation: no) and your
rules of the first handoff stand.

**Findings file:** `.runs/task-cycles/readiness-approval-rename/reports/fix-findings.md` (the reviewer's
three Minor findings within the task, in its words; no blocking finding). The review's report is not
yours to read. The reviewed head is `79c9bfb95e772cb21810a78fc42607f99d726da0`; your fix's range runs from it.

**Scope.** Fix only those three findings, each as small as it asks (finding 2: rewrap only the lines the
rename lengthened over the file's own wrapping, never lines your rename did not touch; do not rewrap
decision text beyond the added lines; keep every sentence word for word). Finding 3: add one test case
each in `project-level/test_readiness_check.py` — the old heading `## Gate record` is reported as no
section of the template, and `Status: ready for gate` is reported — placed by the file's own layout and
the test guidelines, with the `# invariant: project-readiness-check` citation line where the file's
neighbouring tests carry one; see each fail once against the old behaviour (add the old name to the
allowed set in a working copy or equivalent) and pass. A fix that grows beyond its findings is the
likeliest to draw a new serious finding. Run the affected focused checks again
(`python -B gate/run_tests.py project-level`, `process-audit`, `python -B elements/common/foundation_check.py`,
and `agent-instructions` if a skill description changed) with command and exit code. Do not run the full gate.
Commit by path; message in English.

**Report** to `.runs/task-cycles/readiness-approval-rename/reports/author-fix-report.md`: each finding
as fixed (how, with the check that shows it) or contested with evidence, commits, checks with commands
and exit codes, **Unread material**, **Searches not found or unclear** (`none` if nothing), working
copies (directory `.runs/author-fix/`, removed before you return; state where each stood).

Return only status, commits, a one-line check result and the report path.
