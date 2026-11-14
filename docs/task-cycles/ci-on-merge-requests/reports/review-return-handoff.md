# Handoff — the review of the return step

You review the commits of the return step of the task `ci-on-merge-requests`, as an agent that did
not make them.

- Worktree: `the worktree of the task`; work from its root; read-only, you
  change nothing and commit nothing. Method: `task-cycle/review/SKILL.md` (the return step's commits
  are reviewed as its section 2 gives, against the task and the foundation entries the return step
  writes or corrects), read whole.
- Range: `23f08e917bdaa803b590135d79382da1bcdb8a43..b344595` — compute it yourself
  (`git diff 23f08e9..b344595`, `git log 23f08e9..b344595`) and confirm `git rev-parse HEAD` is
  `b344595...`. One commit, one file (`installation/README.md`, one clause).
- The return step's report, a set of claims to verify: `reports/return-step-report.md`; the handoff it
  was given: `reports/return-step-handoff.md`; both in
  `.runs/task-cycles/ci-on-merge-requests/reports/`. The frozen task:
  `.runs/task-cycles/ci-on-merge-requests/task.md` (read whole). The return step's rule:
  `task-cycle/skill/return_step.md`.
- The question for you: does the commit do what the return step requires, and is the claim of its report
  true — that no decision or invariant rests on the sentence it removed (that on GitHub the check is
  named by the job's name), that the other claims of the report (the entries compared; no new
  environment fact, glossary term or invariant; the rows of *Settlements to record*, each where it
  goes) hold? Search the foundation yourself for what rests on the removed sentence and for the
  other claims you judge likely false; read an entry whole before you grade a finding on it.
  The change passed its review of the whole change and of its fix (`PASS 23f08e9`); you review the
  return step's commit and what its report claims, not the earlier range again.
- Trust boundary: yes, as before; the commit touches no code.
- Checks: you may run `python -B elements/common/foundation_check.py` and a single directory's tests;
  never the whole gate.
- Report: `.runs/task-cycles/ci-on-merge-requests/reports/review-return-report.md`, first line
  `PASS <sha>` or `FAIL <sha>`, with the checks you ran (command, exit code), **Unread material** and
  **Searches not found or unclear** (`none` is an answer). Return that first line, a one-line check
  result and the path.
- Working copies: your directory is `.runs/review-return/`; the paragraph of the earlier handoffs,
  "Working copies", stands word for word (remove the copy and say so; none may be needed).
