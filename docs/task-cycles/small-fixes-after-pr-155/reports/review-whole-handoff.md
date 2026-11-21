# Handoff — the review of the whole change

You are a fresh reviewer of the whole change of a task cycle of the-way (agent type `the-way-stage`).
You made none of it. The human who asked for this cycle has delegated intermediate choices to the
orchestrator; no answer of the orchestrator is that person's approval. You alone grade and scope
your findings.

## Where you work

- Worktree: `the root of the worktree`, branch `task/small-fixes-after-pr-155`.
  You read; you change no tracked file and make no commit.
- Method: `task-cycle/review/SKILL.md` (`review-change`), read whole, and a file it names only when
  the step or variant that names the file comes. The review of the whole change on the one-author
  route.
- Range to review: from the task's base `80006b25feb4c5a6ffdb8f75d993051eecbc745d` to the head
  `73909788` (two commits: `ac7f22a0` and `73909788`). Read the full diff of the range
  (`git diff 80006b25..73909788`): `guidelines/testing.md`, `task-cycle/gate_times.py`,
  `task-cycle/test_gate_times.py`, `task-cycle/test_remove_merged_worktrees.py`.
- Your directory for working copies: `.runs/review-whole/` (under the ignored `.runs/` of the worktree).
- Your report: `.runs/task-cycles/small-fixes-after-pr-155/reports/review-whole-report.md`. This file is
  the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it), the case the note on
  report names leaves open; write it there. Its first line is `PASS <sha>` or `FAIL <sha>` as the
  method gives it.
- `cycle.md` and the other files of `.runs/task-cycles/small-fixes-after-pr-155/` — other agents'
  handoffs, reports and findings — are not yours to read unless this handoff names them.

## Working copies (word for word from the cycle's rule)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed. It
removes a copy, as any directory, by its path written out in full in the command, never through a
shell variable: an empty variable turns the removal on the directory the shell stands in.

## What you review against

- The frozen task, read whole: `.runs/task-cycles/small-fixes-after-pr-155/task.md`. Check every item
  of *To do* 1–4, both *Acceptance criteria*, the two *Settlements to record* rows (row 1 goes to
  `guidelines/testing.md`; row 2 is the code change) and *Out of scope* (the case of remark m1 and a
  change of the rule itself are let through by the human: a finding that asks for either is outside
  the task's scope). The answer under *Questions to settle* (remove `self.marks.clear()`) is the
  human's, given through the day's advisor; it is settled.
- No spec and no plan: one author held the change, so there are no slices and no slice reviews;
  your review is the one review of the whole change. There are no Minor findings of earlier reviews.
- The author's report: `.runs/task-cycles/small-fixes-after-pr-155/reports/author-report.md`, with
  the evidence it keeps beside it in `reports/`: `author-mutate.py`, `author-mutants-result.txt`,
  `author-probe.py`, `author-trace_push.py`, `author-trace-before.txt`, `author-trace-after.txt` and
  the two `author-trace-*-result.txt`. Its **Unread material** says the author did not open the
  decision log, the invariants file or the glossary, only the sentences of WAY-03, WAY-394 and WAY-402
  as the task quotes them: judge the change against those entries yourself, from your own selection.
  Check the author's proofs, not their claims: you may run the author's scripts in your directory, or
  make mutants of your own; judge whether each of the changes (i), (ii), (iii), (v) of *To do* 2
  turns a test of `NestedRunTest` red *for the right reason*, whether each expected value is worked out
  from the description at the head of `task-cycle/gate_times.py` as WAY-394 asks, and whether the
  `GIT_TRACE` proof shows what the second acceptance criterion asks.
- Foundation and guidelines: select your own, by the parts the change touches (`task-cycle`, and the
  guidelines file `guidelines/testing.md` the change edits), as "Reading the foundation" in
  `elements/common/way_of_working.md` gives and `product-guidelines/reading.md` gives for guidelines;
  write the index of your selection to a file in your directory (`elements/common/decision_index.py`)
  and state in your report how many decisions you read whole. The task's *Decisions in play* are WAY-03,
  WAY-394 and WAY-402. The change edits a test that cites the invariant
  `repository-changer-acts-only-when-told` and adds a rule to the testing guidelines: judge that rule
  as `review-change` gives for a guideline's example and against the decisions on testing guidelines.

## Answers of the orchestrator at the start of the cycle

- Trust boundary: **yes**. `task-cycle/gate_times.py` is a trust boundary file of the part
  `task-cycle` (the part map): it reads the output of the gate, which includes what failing tests
  print. The change removes one line of it (`self.marks.clear()`) and rewrites a comment and a
  sentence of its description. Check crafted input at that boundary: output where the removed line
  could change a result, lines that hold `== ` after text, summary lines out of order, floods and
  bounds of memory. The author's probe reports 0 differing results on 200 000 random outputs of ten
  kinds of lines; judge whether the kinds were enough.
- Irreversible operation: no. Open design choice and reserved choice: none.

## Checks

You may run focused checks in your directory or the worktree: `python -B -m unittest discover -s
task-cycle -p "test_gate_times.py"`, `python -B gate/run_tests.py task-cycle`, `python -B
elements/common/foundation_check.py`. The full gate is not yours to run (WAY-160). Report each check
with its command and exit code. Your report holds, as the method gives, its **Unread material** and
**Searches not found or unclear** sections (`none` is an answer) and the line on working copies.
Return your report's first line, the changed files with their line counts, and the report's path.
