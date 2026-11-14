# Handoff to the one author — the fix of the review of the whole change

You are resumed as the one author of this change, for the fix of a review's findings. Method:
`task-cycle/change/SKILL.md`, variant "the fix of a review's findings". Worktree (work from its
root): `the root of the task's worktree`, branch
`task/own-measurement-in-decision`, reviewed head `c76debc`. The fix's range runs from it.

Findings file, in the reviewer's words: `reports/reviewer-whole-findings.md` (in
`.runs/task-cycles/own-measurement-in-decision/`). One blocking finding (1) and four Minor findings
(2-5), all within the task; fix all five in one fix. The whole review report is
`reports/reviewer-whole-report.md` if a finding needs its context.

The orchestrator's answers on how to fix:
- Finding 1: use the wording of the environment facts template ("is a citation, and a fact where this
  section asks for one") or the reviewer's suggestion; the two templates must say the same thing.
- Finding 2 (WAY-256): you could not name the skill, so add the sentence to the two places where the
  estimate stands (orchestrator's choice; it replaces the earlier choice to leave the entry unchanged).
  Its word is "estimate" where the entry says estimate; the sentence says the figure is this
  product's own and its record is not open to a reader.
- Finding 3: one sentence in WAY-90's rationale naming the price: a measurement of the product's own
  agents is found by no fact search (WAY-33), so when the measured model is replaced nothing flags
  the decision that rests on it — in the form the log gives a price. Keep WAY-17 consistent.
- Finding 4: repeat a short clause in WAY-229's *Rejected* next to its figures.
- Finding 5: rewrap the inserted clauses to the file's line wrapping (same text, no new meaning);
  where you rewrap an entry you edited, leave nothing else in it changed.
- Do not change WAY-312 (left unchanged on purpose: its fact's source opens).
- Run the affected checks again (`foundation_check.py --skip-test-citations`, `private_paths_check.py` on
  each file you changed, `python -B gate/run_tests.py elements/common`), answer with evidence a finding you hold
  wrong, commit by explicit paths, no push, do not run the full gate.

Write your report to `reports/author-fix-report.md` (same directory): status, commit(s), each finding
with what you did, each check with command and exit code, **Unread material**, **Searches not found
or unclear**, and your own-work check. Return status, commits, a one-line check result and the path.
