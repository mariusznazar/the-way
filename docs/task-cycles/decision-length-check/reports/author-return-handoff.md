# Handoff — the return step

You are the one author, resumed for the return step (step 11 of the cycle). The person who requested
this cycle delegated intermediate choices to the orchestrator; no answer here is that person's
approval.

- Worktree and branch: the task's worktree, `task/decision-length-check`.
  The change is reviewed: the review of the whole change failed once and the review of its fix passed
  (`PASS 9c7f9b71`); the head you start from is `9c7f9b71`.
- Your method: `task-cycle/change/SKILL.md`; your stage is the return step, not one of its variants.
  Read `task-cycle/skill/return_step.md` whole, and `task-cycle/skill/foundation_step.md` whole with
  the `SKILL.md` of an element at the path that file gives, when you write an entry of that element
  (the return step writes as the foundation step writes).
- What to compare with the code: the entries the change writes or changes (WAY-05 as it stands in
  `foundations/decisions.md`; the sentence of `elements-common` in `foundations/part_map.md`), those the
  task names (*Decisions in play* of `.runs/task-cycles/decision-length-check/task.md`: WAY-12, WAY-02,
  WAY-22, WAY-385), those your search of the foundation found, and the part map of the touched parts
  (`decisions`, `elements-common`, `agent-instructions`, `repository`) — including whether the part map
  entry of `elements-common` and any invariant or glossary entry still match the code with
  `elements/common/foundation_text.py` in it. Correct in the same change whatever no longer matches.
  Include in your comparison the pair of examples of WAY-05 (the task's point 6): the part the test now
  holds must be out of it, and *Verification* must name that test by its `tests:` clause.
- The choices that stand as rows of the questions table of the record and need no entry are, from the
  orchestrator's record: the move of the readers of an entry's text into `foundation_text.py` with
  the names kept importable from `foundation_check` (WAY-385 and WAY-365 already bind the rule), and
  the wording of the check's message. Judge, as `return_step.md` gives, whether either is a choice that
  binds after the merge and has a place in the log; where it has none, enter nothing.
- Commit nothing unless something no longer matches. Your report says so either way, in the form the
  record's *Return step* gives it: foundation compared with code, decisions, invariants, environment
  facts, glossary terms, part-map changes, projected entries and rows of *Settlements to record*
  written (each row with its identifier), or `none`.
- Your directory for working copies: `.runs/author-return/`; remove it before you return. Do not run
  the product's full gate. Where you change a file, run again the focused checks it affects and the
  check of the foundation, each with command and exit code.
- Your report: `.runs/task-cycles/decision-length-check/reports/author-return-report.md`, with its
  status, commits, checks, **Unread material**, **Searches not found or unclear** and working copies.
