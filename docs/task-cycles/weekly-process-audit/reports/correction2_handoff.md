# Handoff — the second correction for the human's remarks (`make-change`: "a correction for the human's remarks")

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. Their answer below binds you. Your questions go to the orchestrator, never to the human.

## Where you work

- Worktree (work from its root, read every file from it): `the worktree of the task`, branch `task/weekly-process-audit`, HEAD `410113b`.
  The correction's range starts there. The target branch has not moved since the last merge.
- Method: `task-cycle/change/SKILL.md` whole (you make "a correction for the human's remarks"); how your work will be reviewed: `task-cycle/review/fix.md`.
- Report path: `docs/task-cycles/weekly-process-audit/reports\correction2_report.md`.

## The human's answer (their words, which bind)

On the request's item of *Fix or let through* about unfixed findings the human or the process will feel, the orchestrator recommended fixing (a) and (b) in this request. The human answered:

> załatajmy jeszcze te dwa drobiazki

Those two are:

**(a)** `process-audit/audit_count.py`, `read_contradiction` (the first of the three questions: did a contradiction with the product's settlements come out only after code was written). The reviewer's words
(review of the fix of the whole change, n1): "the guard looks for a denying word anywhere in the whole item, not next to the phrase. A real discarded attempt in the template's form holds such words in its
other parts: `- Discarded attempt: 10:32, open design choice found in the auth flow; report reports/x.md; foundation entries none; reset to abc1234; next route: spec` reads `unknown` on the head (run). Safe
direction (never a wrong `yes`), but Q1's `yes` will rarely be given for the template's own form. Direction: look only at the words just before the phrase."

**(b)** The column of an open issue that counts cycles. The reviewer's words (review of the return step, F3): the open issue's column counts the cycles where the problem *stands*, while the task and the
decision on frequency (WAY-336) ask for the cycles where it *came back*. The task (To do 3): "przy każdej sprawie otwartej: liczbę cykli, w których problem wrócił, i liczbę dni czekania". A problem that
stands in its first cycle has not come back there; the number a human weighs is one too high.

## What to do

1. **(a)** Look only at the words just before the phrase "open design choice" in the *Discarded attempt* item for a denial, so that the template's own form of a real discarded attempt reads `yes`
   where it names an open design choice and no denial stands directly before the phrase; keep `unknown` for everything the item cannot say, and never a wrong `yes` (a negated phrase —
   "no open design choice", "not an open design choice", "without an open design choice" — stays `no` or `unknown` as the code decides today). Test first: the reviewer's example reads `yes`; a negated
   example does not; crafted input (a very long item, control characters, a bar) breaks no cell and no pattern backtracks.
2. **(b)** The open issue's count of cycles becomes the cycles in which its problems came back: the cycles in which a problem of the issue stands, except the first of them (the earliest cycle by the
   commit of the *Record* the register names, ties by the cycle's identity); zero where it stands in one cycle only; the header says what it counts ("came back in"); where refused rows or an unknown
   cycle make the count uncertain it keeps the form `at least n` / `unknown` that the table already uses. The days of waiting keep counting from the earliest record commit. Keep the order of the issues
   the register's (no ranking). Change the module docstring, the paragraph of the table in the result, `process-audit/SKILL.md` (its matter of what still waits, which cites this column) and the
   wording of the decision on frequency only where a sentence is now false (read WAY-336 whole; edit it in place through the project skill `the-way-record-decision` only if its words are wrong
   after the change). If you change `process-audit/SKILL.md`, run `python -B agent-instructions/skill_entry_points.py` and, if it asks, `--write`, and commit its output.
3. Update the tests whose expectations change for (b) and say in your report which, and why none is weakened. Keep every lesson of the earlier trust-boundary reviews: no backtracking pattern, no unguarded
   conversion, every cell through `cell()`, size caps, a failure of one cycle is `unknown` for that cycle.
4. Do not touch the other open findings (the decision's "pins no commit" wording, the missing sentence on a bar in a class meaning, the other Minor findings): the human did not ask for them.
5. Commit with `git add <paths>`, messages in English.

## Checks (each as command and exit code in your report)

`python -B gate/run_tests.py process-audit`, `python -B elements/common/foundation_check.py`, `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths`,
`python -B agent-instructions/skill_entry_points.py` (nothing to create or change), and a run of `process-audit/audit_count.py` with stdin closed on a temporary locations file naming this worktree
and a temporary register and results directory. Do not run the full suite: the cycle runs it. Long commands: run them in the background and wait in stretches under four minutes.

## Report

As `make-change` gives: status, commits, a one-line check result, questions, concerns, each reach beyond this handoff, **Unread material**, **Searches not found or unclear**, the own-work check; and
for each of (a) and (b), how the correction makes it, with a before and an after of the example.
