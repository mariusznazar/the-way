# Review handoff — whole change, instruction-files-router

The user invoked the-way-implement-task and delegated intermediate choices to the orchestrator; the
goal is a reviewable pull request into `foundations`. You review the whole change as an agent that
made none of it.

- Worktree: `C:/Storage/repos/the-way-wt/instruction-files-router`, branch
  `task/instruction-files-router`. Work from its root; read-only — change no file except your report.
- Method: read `task-cycle/review/SKILL.md` of this worktree whole, with every file it names, and
  follow it for the review of the whole change. Also read `agent-instructions/README.md` (the-way is
  the top-level repository).
- Range: `0b8c1bd613b94bce290e49aad9eaf1d0b2587b02..634fa3b` (base `foundations` at `0b8c1bd`; one
  commit `634fa3b`). One author without a plan; no spec, no slices.
- Frozen task: `.runs/task-cycles/instruction-files-router/task.md` — read it whole (Polish). Check
  coverage of every item of *To do* 1–9 and every row 1–7 of *Settlements to record*, and fidelity to
  the task's answers under *Questions to settle* and to *Out of scope*.
- Author's report: `.runs/task-cycles/instruction-files-router/reports/author-report.md`.
  The author returned `done with concerns`: beyond the files the handoff named (`SKILL.md`, one file
  per kind of text, a shared file only where row 5's condition holds), it added
  `instruction-files/judging.md` for what only the judging mode needs, arguing from the criterion the
  change writes. The author's handoff is beside it (`author-handoff.md`) for what was asked.
- Answers of step 4: trust boundary — yes in letter: `instruction-files/check_instructions.py` is the
  part's trust boundary; check that its change is to the module docstring only and alters no handling
  of the files it reads. Irreversible operation — no. Human actions — none.
- Foundation and guidelines: select your own foundation reading by the parts of the change, as your
  method gives ("Reading the foundation" in `elements/common/way_of_working.md`). Guidelines: the-way
  has no `guidelines/`; the task settles that it writes no code.
- Gate: do not run `python -B gate/run_tests.py` without a directory; the orchestrator runs it. Run
  the focused checks your review needs (e.g. `python -B elements/common/foundation_check.py`,
  `python -B agent-instructions/skill_entry_points.py`, `python -B gate/run_tests.py instruction-files`,
  `git diff --check 0b8c1bd..634fa3b`), each with its command and exit code in the report.
- User's read-only references for skills and knowledge artifacts, relevant to judging the text:
  `C:/Storage/The Brain/The Brain/Notes/Areas/(A) Claude code/konwencje_skilli_i_commandow.md`,
  `C:/Storage/The Brain/The Brain/.ai/rules/knowledge_artifacts.md`; before any script,
  `C:/Storage/The Brain/The Brain/.ai/rules/scripts.md`.

Write the full report to
`C:/Storage/repos/the-way-wt/instruction-files-router/.runs/task-cycles/instruction-files-router/reports/review-report.md`,
its first line `PASS <sha>`, `FAIL <sha>` or `questions`, as your method gives. Return only that first
line, a one-line check result naming what failed or did not run, and the report's path.
