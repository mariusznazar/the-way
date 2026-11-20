# Handoff — the return step after correction 2

You are the one author, resumed for the return step after correction 2 (the correction and its fix are
reviewed: `PASS a8753bb8`). The person who requested this cycle delegated intermediate choices to the
orchestrator; no answer here is that person's approval.

- Worktree and branch: the task's worktree, `task/decision-length-check`, head `a8753bb8`.
- Method: `task-cycle/skill/return_step.md` whole, and `task-cycle/skill/foundation_step.md` where you would
  write an entry. Compare with the code the entries correction 2 wrote or changed — WAY-05 (the limit of 600
  words for all the binding sentences, the error and the list for it, a further paragraph for each part of the
  entry's own question, its *Verification* with the `tests:` clause and the pair of examples, its *Rejected*),
  the template `elements/decisions/template.md` — and those it touches (WAY-12, WAY-02, WAY-19, WAY-22,
  WAY-385) and the part map of the touched parts, with `check_length` and the other code of the check
  (`elements/common/foundation_check.py`, `elements/common/foundation_text.py`, the head description of the
  script) and its tests. Correct in the same change whatever no longer matches. Do not change WAY-19 and do
  not fix the two Minor findings of the review of correction 2 (the name of a part in WAY-19 against WAY-05; "for
  this report alone" in `agent-instructions/README.md`) nor the Minor finding of the review of the fix
  (the words "all the binding sentences together at most 600 words" inside the optional block of the entry
  form of the template): they are findings of a correction and go to the request's list; say in your report that
  you left them.
- Say, in the form of the record's *Return step*, whether the two settlements of the remarks (the limit for the
  whole entry; the paragraph for a part of the entry's own question) stand written in WAY-05 and the template, and
  the marks the foundation step gave them in your report of correction 2 (`row n`, `the cycle's`), so that the
  request can place them.
- Commit nothing unless something no longer matches. Do not run the full gate. Where you change a file, run the
  focused checks it affects and `python -B elements/common/foundation_check.py`, each with command and exit
  code.
- Your directory for working copies: `.runs/author-correction-2-return/`; remove it before you return. Make no
  file outside the worktree.
- Your report: `.runs/task-cycles/decision-length-check/reports/author-correction-2-return-report.md`, with its
  status, commits, **Unread material**, **Searches not found or unclear** and working copies.
