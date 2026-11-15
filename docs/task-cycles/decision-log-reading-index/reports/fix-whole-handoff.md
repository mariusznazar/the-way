# Handoff: the fix of the whole-change review's findings, task `decision-log-reading-index`

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator; no answer it
gives is the human's approval. You never ask the human. The cycle has one human contact, the request.

## What you do

- You are a fresh agent fixing the findings of the review of the whole change, on the same branch
  (`task/decision-log-reading-index`, worktree `the task's worktree`, head
  `55f1a24ddcece1ba8c48a5e27595a34072939359`). The findings span the foundation work and two slices, so a fresh agent fixes
  them. Nobody else writes in this worktree while you work.
- The findings file, the reviewer's words: `reports/whole-findings.md` (full path
  `.runs/task-cycles/decision-log-reading-index/reports/whole-findings.md`):
  one blocking finding, I1, and the Minor findings within the task m1–m5. The review's full report is
  `reports/review-whole-report.md` beside it (read the passages the findings cite, not the whole report).
  m6 and N1 are not yours.
- Method: `task-cycle/change/SKILL.md`, the variant "the fix of a review's findings"; read `task-cycle/change/fix.md`. For a
  change to a decision of `foundations/decisions.md` follow `elements/decisions/skill/SKILL.md` (read as a file; the cycle's
  types have no skill tool) and `task-cycle/skill/foundation_step.md` for how an entry is written. WAY-150's rewording of I1 keeps
  the meaning the task's rows 1, 2, 3, 5, 6 give (`.runs/task-cycles/decision-log-reading-index/task.md`, *Settlements to record*);
  the reviewer's variant (a) is the smaller fix, and where you choose, say which and why in the report.
- What you fix and where: I1 in `foundations/decisions.md` (WAY-150, and the pair of *Verification* examples where your wording
  makes one stop holding the sentence, as WAY-12 gives) and in `elements/common/way_of_working.md` where the rule must stay
  in step; m1 and m2 in `task-cycle/cycle_measures.py` and `task-cycle/test_cycle_measures.py` (m1: a `MemoryError` of a huge
  line ends with exit 2 and `Error:` naming the file and line, with a test — the file is a trust boundary: crafted input
  stays exit 2 or uncounted, never a traceback; m2: make the subtest assert or delete it); m3 in `task-cycle/skill/SKILL.md`
  (step 12's description of `cycle_measures.py`); m4 in `elements/common/decision_index.py` and
  `elements/common/test_decision_index.py` (follow the finding; the error is exit 2 with the message form of WAY-344); m5 in
  `project-level/lead/answering.md`, `project-level/lead/skill/SKILL.md` and `task-cycle/cycle_measures.py`.
  Nothing else: no change beyond the findings, no change of `foundations/decisions.md` outside WAY-150 (and a pair of examples the
  new wording needs). If you hold a finding wrong, answer with evidence instead of changing code.
- Checks: run the affected checks again, not the product's full gate (the orchestrator runs it): `python -B elements/common/foundation_check.py`
  (0 errors), `python -B gate/run_tests.py elements/common`, `python -B gate/run_tests.py task-cycle`,
  `python -B gate/run_tests.py project-level` where you changed a file there, and `python -B gate/run_tests.py process-audit`
  only if you touch `process-audit/` (you should not). Commit by `git add <paths>`, never `git add -A`; messages in English,
  imperative; one commit for I1 and one for the Minor findings is welcome, but not required.
- Report: `.runs/task-cycles/decision-log-reading-index/reports/fix-whole-report.md`, written as a file at that exact path, as `fix.md`
  gives it, with checks' commands and exit codes, the own-work check, **Unread material**, **Searches not found or unclear**, the
  working copies line, and for each entry you changed one sentence of its meaning in English and one in Polish, marked `the cycle's`
  where no row of the task gives it.

## Foundation entries and files to read

WAY-150, WAY-12, WAY-263, WAY-344, WAY-18 and WAY-21 in `foundations/decisions.md` (find each by its heading `### WAY-NN`, read each whole,
to the next `#` heading); `elements/common/way_of_working.md` "Reading the foundation" whole; every file you change, whole, before you change it.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed.
The files that a product's own tools and tests make by themselves are no working copy of the agent
and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a
worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside
its report what the report needs, and states in the report where each copy stood and that it was
removed. Where a removal fails, the agent finishes all the same and names in the report the
remainder, with its full path and the reason it stayed.

Your directory for working copies: `.runs/fix-whole/`.
