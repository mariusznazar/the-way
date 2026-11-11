# Handoff — the return step again, after the correction, cycle `cycle-remarks-batch-4`

You are the one author, resumed, for the **return step** (step 11 of `implement-task`), repeated
because the human's remarks changed decisions, templates and a script. It is not a row of
`make-change`. The orchestrator acts on the user's delegation; nothing here is the human's approval.

- Worktree (from its root): `.runs/worktrees/cycle-remarks-batch-4`; head
  `10d443fa64e4b21d6bf63c0140ab6cecf1ab1f96`. The change under comparison is the range
  `e3825a82386a61930a86f8517fc0c5f422fc2833..10d443f` (the correction `14b7680..10d443f` is reviewed,
  `PASS 10d443f`; the full gate on this tree passed: exit 0, 880 tests).
- Read whole: `task-cycle/skill/return_step.md`, `task-cycle/skill/foundation_step.md`, and the skill of
  an element when you write an entry of it.
- Compare with the code: the entries the change and the correction write or change (WAY-160, WAY-71,
  WAY-287), those the task names (WAY-27, WAY-17, WAY-163, WAY-294), WAY-58 (it names *Derives from*), the
  glossary entries `gate` and `return step`, and the part-map entries `decisions`, `task-cycle`,
  `elements-common`, against the files of the repository on this head; the human's remarks are
  `reports/11-correction-remarks.md`. Correct in the same change whatever no longer matches. Commit only
  what no longer matches; if nothing does, commit nothing.
- The reviewer's remaining Minor finding N-1 (a mixed list such as `python-stdlib-modules · TODO` in
  *Rests on* is read the opposite way from the rule) is for the human; do not fix it, name it if you meet
  it. The same holds for any finding left to the human earlier.
- The full gate is already run on this tree. If you commit, run only focused checks; a commit starts a
  review of its range and a second gate run.
- Report: `docs/task-cycles/cycle-remarks-batch-4/reports/17-correction-return-step-report.md`
  with the fields of the record's *Return step* (foundation compared with code; decisions, invariants,
  environment facts, glossary terms, part-map changes, projected entries, rows of *Settlements to
  record* — each written or `none`), each check with command and exit code, **Unread material**,
  **Searches not found or unclear**. Return status, commits, a one-line check result and the report path.
