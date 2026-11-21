# Handoff — the return step

You are the one author of this change, resumed (`the-way-author`), for the return step (step 11 of
the cycle). The change is finished and reviewed: the review of the whole change passed
(`reports/review-whole-report.md`, `PASS 739097886195c9ea02b30cc03894e2c64cebb4cf`), its Minor findings
were fixed in `77ddfbf7` and that fix passed its review (`reports/review-fix-1-report.md`,
`PASS 77ddfbf70f4dd8da1a57446f99f1dde1fba1157d`). The head is `77ddfbf7` in the worktree
`the root of the worktree`; the base is `80006b25`.

- Stage and method: the return step of `task-cycle/skill/return_step.md` — read it whole — which
  writes as the foundation step writes: `task-cycle/skill/foundation_step.md`, read whole, and the
  `SKILL.md` of an element, at the path it gives, only when you write an entry of that element.
  `task-cycle/change/SKILL.md` (`make-change`) is your method as before.
- Compare with the code of the change: the foundation entries the change writes or changes (the new
  rule `### Turning off git's automatic maintenance` of `guidelines/testing.md`, which is row 1 of
  *Settlements to record*; the description at the head of `task-cycle/gate_times.py`, which WAY-394
  makes the source of expected values; the tests that hold a sentence of a decision by `decision:`
  or cite an invariant in the two test files you changed), the entries the task names (WAY-03,
  WAY-394, WAY-402 in its *Decisions in play*), the entries your search of the foundation found
  (the search of WAY-33 you made in the foundation step) and the entries your own search by the names
  and words the change's code adds finds — one search, made even where no entry is written: the
  names and words are `maintenance.auto`, `gc.auto`, `self.marks`, `failing_dir`, `failing_with`'s new
  parameters `separator` and `then`, "different places" — and the part map of the touched parts
  (`foundations/part_map.md`, entries `task-cycle`, the one `agent-instructions` only if a test of it
  names a file you changed). Correct in the same change whatever no longer matches. Settlement row 2
  is the code change and writes no entry. Do not found a shared helper for building test
  repositories, and write no entry that is deferred.
- The frozen task, read whole: `.runs/task-cycles/small-fixes-after-pr-155/task.md`. Your own
  reports, `reports/author-report.md` and `reports/author-fix-1-report.md`, hold what you did.
- Your directory for working copies: `.runs/author/` (made by you, removed before you return, named
  in the report). Commit by path; never push. If the return step changes nothing, you commit nothing,
  and say so.
- Report: `.runs/task-cycles/small-fixes-after-pr-155/reports/author-return-report.md`. It names, as the
  record's *Return step* gives it: the foundation compared with the code, decisions, invariants,
  environment facts, glossary terms, part-map changes, projected entries, and the place each row of
  *Settlements to record* went to (row 1: `guidelines/testing.md`; row 2: the code of
  `task-cycle/gate_times.py`). Include its **Unread material**, **Searches not found or unclear**
  (`none` is an answer), the own-work check and the line on working copies. Run
  `python -B elements/common/foundation_check.py` if you change a foundation entry, with its exit code.
  Return your status, commits, a one-line check result and the report's path.
