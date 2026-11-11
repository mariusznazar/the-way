# Handoff — review of the whole change, cycle `cycle-remarks-batch-4`

You review the whole change of one task as an agent that did not make it. The orchestrator of the
cycle dispatches you on the user's delegation; nothing here is the human's approval. You are
read-only: change no file, make no commit.

## Where and what

- Worktree (work only here, from its root): `.runs/worktrees/cycle-remarks-batch-4`
  on branch `task/cycle-remarks-batch-4`.
- Method: `task-cycle/review/SKILL.md` of this worktree, whole; variant **the whole change**, so also
  `task-cycle/review/whole_change.md`, whole, and the files the method names when their step comes.
- Range: base `e3825a82386a61930a86f8517fc0c5f422fc2833` to head `0d59ce9` (confirm with
  `git rev-parse HEAD` the full SHA you review). Commits: `3effb9b`, `77ecd4a`, `0d59ce9`.
- Frozen task, whole: `docs/task-cycles/cycle-remarks-batch-4/task.md`.
  Check every To do item, every answered question of *Questions to settle*, the *Decisions in play*
  and *Out of scope*. *Settlements to record* is `none`; no projected entry is carried.
- The author's report: `docs/task-cycles/cycle-remarks-batch-4/reports/02-author-report.md`
  (claims to verify, not evidence).
- Route: one author without a plan, no slices, no spec. No review of an earlier slice exists.
- Answers of the cycle's start: the change touches no trust boundary and holds no irreversible
  operation. This is the-way itself (`agent-instructions/README.md` applies; the-way has no
  `guidelines/` directory).
- The author's mechanical check passed (clean worktree, non-empty range). Files outside what the
  task's To do names, passed to you as information: `task-cycle/skill/blocked_finding.md`, the
  WAY-287 entry in `foundations/decisions.md`, `elements/invariants/template.md`. Judge them against
  the task and the foundation; their grade and scope are yours.
- Material the author's report says it did not read, which you are able to judge, carried to you:
  WAY-290, WAY-295, WAY-296, WAY-298, WAY-300 (named in the author's handoff), and the part-map entries
  `decisions`, `task-cycle`, `elements-common`, the glossary and the invariants of the parts the
  change touches. Select your own foundation as your method gives; read the carried items when you
  judge that the change bears on them.
- The orchestrator runs the product's gate (`python -B gate/run_tests.py`) itself; you do not. Focused
  checks of directories are yours to run if you need them; do not start the full gate (another
  process may use the machine).

## Report

Write it to `docs/task-cycles/cycle-remarks-batch-4/reports/04-review-report.md`
as the method gives (first line `PASS <sha>` or `FAIL <sha>`, graded findings with `file:line`
anchors, scope of each finding, the checks you ran with command and exit code, the count of decisions
read whole and by title, **Unread material**, **Searches not found or unclear**). Return the first
line, the number of findings by grade, and the report path.
