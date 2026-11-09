# Handoff — the return step (step 11 of `implement-task`), by the resumed one author

You are resumed as the author for the return step. Stage: the return step, not a row of `make-change`'s
variants.

- Worktree: `the root of the task's worktree`, branch `task/locations-file`,
  head `ba36539` (change reviewed `PASS ba36539`). Base `17b83bf`.
- Read whole: `task-cycle/skill/foundation_step.md` and `task-cycle/skill/return_step.md`; read the
  skill of an element when you write an entry of that element.
- Frozen task: `.runs/task-cycles/locations-file/task.md`. Rows 1–3 of *Settlements to record* are
  written already (WAY-27 and WAY-107 edited, WAY-320 new, invariant `tracked-file-private-paths`,
  `outbound-link-reach` edited).
- Do: compare the foundation entries the change writes or changes, those the task names, those your
  search found, and the part map of the touched parts, with the files of the repository, and correct
  in the same change whatever no longer matches (WAY-11). Check in particular: the part map's entry of
  `project-level` and `task-cycle` against the new files (`project-level/backlog_place.md`,
  `task-cycle/test_tracked_files_private_paths.py`); `invariants.md` and the test; any decision or
  glossary term that now reads differently (WAY-95). Write no invariant for behaviour merely because
  none covers it. If nothing no longer matches, commit nothing.
- Record, for each field, as `task-cycle/record_template.md` gives under *Return step*: foundation
  compared with code; decisions written or changed; invariants written or changed; environment
  facts; glossary terms; part-map changes; projected entries; rows of *Settlements to record*
  written.
- Report: try `.runs/task-cycles/locations-file/reports/return-step-report.md` once; if the Write
  tool refuses, return the full report as text and do not work around it. Include every check with
  its command and exit code, and **Searches not found or unclear**.
- Leave the worktree clean; commit on the task branch only if you changed something. Return status,
  commits, one-line check result, report path.
