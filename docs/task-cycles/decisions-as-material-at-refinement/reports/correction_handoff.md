# Handoff — a correction for the human's remarks

Stage: a correction for the human's remarks (the row "a correction for the human's remarks" of
`task-cycle/change/SKILL.md`; read that `SKILL.md` whole again for it). You are the author, resumed.

- Worktree and branch as before; head `ff395cf82bce445339f47c495a917a01f70e8fc4`, which carries your
  commits and two commits of the cycle's record (an addition and its removal; they change no file of
  the final tree). The fix range of this correction starts at `ff395cf`.
- The remarks, which bind, whole: `docs/task-cycles/decisions-as-material-at-refinement/reports/correction_remarks.md`
  (in the worktree). In short: fix the stale *Rationale* sentence of WAY-113 and, as the reviewer's
  words say, let its *Verification* name a definition's refinement and its entries; touch nothing
  that items 1–3 accepted.
- Scope: WAY-113 in `foundations/decisions.md` (its *Rationale*, its *Verification*, and, if the
  *Rejected* or any other part of the entry says the old rule, that), and any sentence of a file the
  same stale reading appears in (search `elements/common/way_of_working.md`, `project-level/`,
  `elements/common/skill/` for "where an entry is written" and the equivalent). Change no meaning of
  the binding sentence, which the human accepted. Edit the entry in place; keep the English style of
  the entry. Do not run the full gate.
- After the edit run `python -B elements/common/foundation_check.py` and the focused directories
  your edit can affect; report each with command and exit code.
- Commit by path on the task branch, English message, worktree clean. The record `.runs/` stays out.
- Report: `docs/task-cycles/decisions-as-material-at-refinement/reports/correction_report.md` in the
  worktree (as `make-change` gives for a correction: each remark as made, and how; checks with
  command and exit code; the own-work check; reaches; **Searches not found or unclear**). Return only
  status, commits, a one-line check result and the report path.
