# Handoff — the return step (the one author, resumed)

Take the return step of the task `ci-on-merge-requests`. The review of the whole change and of its
fix has passed (`PASS 23f08e9`); the change stands at head `23f08e917bdaa803b590135d79382da1bcdb8a43`
on `task/ci-on-merge-requests`, base `21ecb627f885de438e2209d7ff5c137b1e1b9d83`.

- Read whole `task-cycle/skill/return_step.md` (it names what you compare and write) and, as it
  says, `task-cycle/skill/foundation_step.md`, and the `SKILL.md` of an element, at the path
  `foundation_step.md` gives, when you write an entry of that element. Your method for commits is
  `task-cycle/change/SKILL.md` (the return step is not one of its rows: it takes none).
- Compare with the code, as the return step gives: the entries the change writes or changes (WAY-16,
  WAY-206, WAY-160, WAY-09, the three environment facts), those the task names (*Decisions in play*:
  WAY-16, WAY-206, WAY-34, WAY-160, WAY-133), those your search found, and the part map of the
  touched parts (`agent-instructions` with `.github/workflows/**`, `installation`, `task-cycle`,
  `product-guidelines`). Correct in the same change whatever no longer matches. The rows of
  *Settlements to record* of the frozen task (`.runs/task-cycles/ci-on-merge-requests/task.md`):
  rows 1, 2, 4 and 6 are written as sentences of WAY-16, WAY-206 and WAY-160, row 3 as the comment of
  `.github/workflows/tests.yml`, row 5 as the installer's block; say in the report that each stands
  where it goes and whether the code makes any row or projected entry true that the foundation step
  missed.
- Sources outside the product the change rests on that the foundation does not hold: you wrote three
  environment facts in the fix; say which others, if any, remain (the two sentences of
  `installation/README.md` you could not source were removed; the claim that the check is named by
  the job's name is on `installation/README.md:170` and its page is named in your report: if it is a
  source the change rests on, write its fact or remove the sentence). Write no entry for a thing
  nothing rests on.
- Glossary: any word of the change used in a meaning for which WAY-95 gives it an entry (for example
  "required check", "bypass", "CI") — write or correct it, or say none.
- Invariants: write one only for a rule the task, a decision or the human sets; the human's task set
  none beyond what the existing `ci-checking-commands` holds. Say in the report that none is written,
  or which.
- Choices that bind after the merge: the choices of your two reports (part of the CI file, place of
  the description, the pinned actions, `concurrency`, the exemption of blocked requests from the wait)
  go to a row of the questions table of the record unless the questions of the decisions template
  place them in the log; say for each which it is and write an entry only where the template says.
- The report: `reports/return-step-report.md` in `.runs/task-cycles/ci-on-merge-requests/`, as the
  record's *Return step* item gives (foundation compared with code; decisions, invariants,
  environment facts, glossary terms, part-map changes, projected entries and rows of settlements,
  each written or `none`), with the commands and exit codes of your checks, **Unread material** and
  **Searches not found or unclear**. If you commit, return the range from `23f08e9` to your head; a
  fresh reviewer will review it. If you commit nothing, say so.
- Checks: focused only (`python -B elements/common/foundation_check.py`, the tests of the directories
  you change, one at a time). Run no whole gate.
- Working copies: your directory is `.runs/return-step/`; the rule of your earlier handoffs, "Working
  copies", stands word for word; remove the copy and report it.
