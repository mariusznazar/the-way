# Handoff — the fix of the review's findings, cycle `cycle-remarks-batch-4`

You are the one author, resumed, for **the fix of a review's findings**. Read `task-cycle/change/fix.md`
whole first (the method's row for this variant). The orchestrator acts on the user's delegation;
nothing here is the human's approval.

- Worktree (from its root): `.runs/worktrees/cycle-remarks-batch-4`, branch
  `task/cycle-remarks-batch-4`; the reviewed head is `0d59ce9e4b4e5cd76029c405b878f94cb33df56f`. Your
  fix range runs from it.
- Findings file (the reviewer's words): `docs/task-cycles/cycle-remarks-batch-4/reports/05-fix-findings.md`
  — one blocking finding (I-1), then the Minor findings of the whole-change review within the task:
  M-1, M-2, M-3, M-5 and M-6. The full report is `reports/04-review-report.md`.
- Report: `docs/task-cycles/cycle-remarks-batch-4/reports/06-fix-report.md`
  (own-work check, each check with command and exit code, **Unread material**, **Searches not found
  or unclear**, and for each finding what you did or why you hold it wrong, with evidence).

## Orchestrator's rulings, which bind the fix (autonomous choices, recorded in the cycle record)

1. **I-1:** widen item 15 of `task-cycle/skill/request_template.md` to what the task words and the
   three entries say: every descriptive `TODO` in an invariant's *Rests on* that stands on the main
   branch after the change — the change writes, keeps or merely does not remove it — is shown, with
   the fact it lacks. Do **not** change the sentence the task gives for WAY-71 and `rules.md`
   (To do 6): its wording is the human's. Make WAY-287 (binding sentence and rationale) and every
   place you wrote about "an entry the change edits" agree with the wider reading, and drop the
   narrowing argument ("a `TODO` in an entry the change does not touch is not the change's"). Say in
   the item how the cycle finds them (the invariants file of the tree after the change). Record in
   your report the cost this takes on (one item per request while an old gap stands).
2. **M-5:** fix only the part inside the task — an example of the new item in WAY-287's *Verification*.
   Do not change WAY-71's *Scope* or add a *Relations* link: that changes an approved decision beyond the
   task (WAY-114); the reviewer marks it as outside.
3. **M-6:** take the reviewer's second way — keep the task's *complies* sentence for WAY-160 as
   given, and make the added rationale sentence a plain statement of the price, without saying that the
   fix "sends the return step back" (the rule stands in `task-cycle/skill/SKILL.md` step 10, where the
   task puts it).
4. **M-3:** say in the docstring of `elements/common/foundation_check.py` that only a value that
   begins with `TODO` is read as a missing fact; do not widen the check. Keep what the tests hold.
5. **M-1, M-2:** as the findings say.
6. **M-4** (WAY-71's *Verification* example `Based on: TODO`) is **not** in your fix: whether *Based on* may
   read `TODO` is the human's decision; the request will carry it.

## Boundaries

- Commit with `git add <paths>` and English messages; do not push; touch nothing under `.runs/` but
  your report. Run the focused checks the changes affect (`python -B gate/run_tests.py task-cycle`,
  `elements/common`, `python -B elements/common/foundation_check.py .`); the orchestrator runs the full
  gate. Another process may use the machine: start no full gate.
- A finding you hold wrong, answer with evidence in your report; a finding you cannot fix without a
  decision of the human, return as `returned` or `blocked` as `fix.md` gives.
- Return the status, commits, a one-line check result and the report path.
