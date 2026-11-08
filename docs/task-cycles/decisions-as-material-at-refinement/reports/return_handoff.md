# Handoff — the return step

Stage: the return step (step 11 of `implement-task`), by the one author resumed. It is none of the
rows of `make-change`; read `task-cycle/skill/return_step.md` whole, and
`task-cycle/skill/foundation_step.md` whole, since the return step writes as the foundation step
writes; read the skill of an element when you write an entry of that element.

- Worktree and branch as before; the head is `d496942c2f3eb7af16ee8edd96904603869ad6aa` (your
  first commits `8316d28`, `3cf2a09` and the fix `d496942`). The change was reviewed (PASS) and the
  orchestrator's full gate passed on this head (exit 0, 804 tests).
- Compare with the code the entries the change writes or changes (WAY-313, WAY-314, WAY-315, WAY-113,
  WAY-115, WAY-124, WAY-134, WAY-138, WAY-165, WAY-267, WAY-111), those the task names, those your
  search of the foundation found, and the part map of the touched parts (`decisions`,
  `elements-common`, `project-level`), with the files of the repository, and correct in the same
  change whatever no longer matches. The fix of the Minor findings changed wording in several of
  them after the foundation step wrote them, so compare them with the files as they stand now.
- Write a record of what you compared, found and corrected in the report below, under the headings
  of the record's *Return step* (foundation compared with code; decisions written or changed;
  invariants; environment facts; glossary terms; part-map changes; projected entries; rows of
  *Settlements to record* written, each row number with its identifier).
- Commit only if you correct something: by path, English message, worktree clean. If nothing needs
  correcting, commit nothing and say so.
- Run `python -B elements/common/foundation_check.py` after any edit of the foundation and the
  focused directories your edits can affect; do not run the full gate.
- Report: `docs/task-cycles/decisions-as-material-at-refinement/reports/return_report.md`,
  with checks (command, exit code), reaches and **Searches not found or unclear**. Return only
  status, commits (or none), a one-line check result and the report path.
