# Handoff — review of the reconciliation with the target branch

Delegation: the person who requested this cycle delegated intermediate choices to the orchestrator;
questions go to the orchestrator. Nothing here is the human's approval.

Worktree (read-only): `the task's worktree (the repository's root)`.
Method: `task-cycle/review/SKILL.md` of the worktree, read whole (entry point
`.claude/skills/the-way-review-change/SKILL.md`); your variant is the review of the reconciliation
with the target branch; read other files it names only when the step or variant that names them comes.
Read also `agent-instructions/README.md`.

What happened: the whole change (one decision, then numbered WAY-330, in `foundations/decisions.md`;
reviewed PASS at `5922ffc`, fix included) was reconciled with `origin/foundations`, which had moved
from `e9a0f92` to `3bcad13`. The merge commit is `c32cfe14ce85a2a8c81b54bdeff0f74a9b65550a`
(parents `5922ffc` and `3bcad13`; confirm by `git rev-parse HEAD`). Range to review: the merge's
changes to the task's side — `git diff 5922ffc..HEAD` shows the whole of the target's news; the part
that is the reconciliation itself is what differs from `3bcad13` in the foundation:
`git diff 3bcad13..HEAD` (it must show only the task's decision, renumbered, and nothing else).

The conflict: both sides appended entries after WAY-329 in `foundations/decisions.md`. The target
branch took WAY-330…WAY-343 for the decisions of the process audit, so the task's decision became
**WAY-344** (title and body unchanged otherwise), placed after WAY-343. The target also added a
17th part, `process-audit`, to the part map and to the *Scope* of WAY-328; the task's decision
names "every part of the-way's part map" in *Scope*, so `process-audit` was added to its *Scope*
(the task text says 16 parts, written when the map had 16).

Ask: do the two sides still hold together? In particular — (1) the merge result is the target's
entries unchanged plus the one entry, with no loss or alteration of either side; (2) WAY-344's
*Scope* equals the 17 parts of `foundations/part_map.md` exactly; (3) no entry of the target
(WAY-330…WAY-343, WAY-328, and the part `process-audit` of the part map) contradicts WAY-344 or is
made false by it, and WAY-344 claims nothing about the audit's new script
`process-audit/audit_count.py` or its tests; (4) numbering: no other entry or file refers to the
task's decision under its old number WAY-330 (`git grep` for text that means the old number), and
`python -B elements/common/foundation_check.py` passes.

Foundation entries the merge brought in that bear on the change (read whole): WAY-328; the
`process-audit` entry of `foundations/part_map.md`; WAY-330 and WAY-343 of the target (the audit's
first and last decisions) and any other of WAY-331…WAY-342 whose title bears on scripts, exit codes
or tests of the audit. The task: `docs/task-cycles/scripts-fail-on-missing-fields/task_frozen.md`
(from the line `# Skrypty the way sprawdzają…`); WAY-344 as the whole-change review passed it:
`docs/task-cycles/scripts-fail-on-missing-fields/reports/review_whole_report.md` and
`review_fix_report.md` in the same directory.
You do not run `gate/run_tests.py`; the orchestrator runs it on this tree.

Report: `docs/task-cycles/scripts-fail-on-missing-fields/reports/review_merge_report.md`;
first line `PASS <sha>` or `FAIL <sha>`; graded findings, the checks you ran with command and exit
code, **Unread material** and **Searches not found or unclear** (each `none` where empty). Return
the status, first line, checks, report path, questions.
