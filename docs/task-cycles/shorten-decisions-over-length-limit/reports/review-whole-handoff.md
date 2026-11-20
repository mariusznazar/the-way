# Handoff — the review of the whole change (`review-change`)

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. You are an agent that did not make the change. Read-only: change no tracked file and make no commit. You grade and scope your own findings.

## What you review

- Worktree and branch: the root of the task's worktree, `task/shorten-decisions-over-length-limit`. Work from its root.
- The whole change on the route "one author without a plan" (no spec, no plan, no slices; the one review is this one). Range: base `bafe3904a80f3f74e6a722dc3d8dc8be1ed882cc` to head `ef8aa061`; confirm that `git rev-parse HEAD` is `ef8aa061…` before you go on. Two commits: `2f31b30f` and `ef8aa061`. The author's foundation entry (the new decision WAY-416) lies in this range.
- Method: `task-cycle/review/SKILL.md`, read whole; for the whole change, `whole_change.md` beside it as the skill gives. Your report path: `.runs/task-cycles/shorten-decisions-over-length-limit/reports/review-whole-report.md`; its first line is `PASS <sha>` or `FAIL <sha>`. This file is the input of the cycle's scripts (`task-cycle/remarks_check.py`), and its name begins with `review`, not with a word Claude Code refuses; if a write is refused all the same, return the report whole as your answer. Your directory for working copies: `.runs/review-whole/` of the worktree.
- The frozen task, whole: `.runs/task-cycles/shorten-decisions-over-length-limit/task.md` — its *To do* 1–13, *Acceptance criteria*, *Questions to settle* (the settlements and their sources), *Decisions in play* and row 1 of *Settlements to record* are what you judge against; check the coverage of every item and of the row, and the fidelity of the new decision to the row and to the sources (the cycle's rule: a part the writer adds that the row does not give makes the entry `the cycle's`; the report marks it).
- The author's report: `.runs/task-cycles/shorten-decisions-over-length-limit/reports/author-report.md` — a set of claims to verify, not evidence. In particular verify yourself: (1) that the binding sentences of the ten entries of the task's table are word for word those of the base, except one word in WAY-150; (2) the split of WAY-344: that each sentence, each clause of *Verification*, each sentence of *Rationale* and each rejected way stands in exactly one of WAY-344 and WAY-416, with the cuts the report lists, and that the two cut sentences read as sentences; (3) every reference to WAY-344 in code, tests, skills, guidelines and other entries, whether it concerns a sentence that moved (the report lists the ones it left and why); (4) that no entry has a paragraph over 3 sentences or 300 words or more than 600 words in all, and that WAY-19 does not contradict WAY-05 as the task's point 10 requires; (5) points 11–13.
- Answers of the cycle's step 4: the change touches no trust boundary and holds no operation that cannot be undone.
- Checks to know: the orchestrator ran `python -B elements/common/foundation_check.py` on the head: exit 0, `0 errors`. The author ran focused tests of `process-audit`, `agent-instructions`, `elements/common`, `task-cycle` (exit 0 each). No full gate has run; it is CI's on the request (WAY-160). You may run focused `python -B gate/run_tests.py <directory>` runs; do not run the full gate.

## Gaps the cycle carries into this review

The author did not read `guidelines/coding.md` and `guidelines/testing.md` whole, and read the large `process-audit/` files (`test_audit_count.py`, `audit_count.py`, `record_reading.py`, `problem_register.py`) only around the lines it changed; it did not read `elements/common/foundation_check.py`. The change touches those files in comments, a docstring and lines `decision:` of tests only (the author says). Judge by the diff whether that holds, and read those guidelines yourself as your own selection requires.

## Minor and out-of-scope findings of earlier reviews

None — no earlier review in this cycle. The author's report lists three observations under "Problems and concerns" (the template's "Changing a decision" still reads the older wording of WAY-19; the precedence sentence of WAY-416 is held by no test; a citation of "the settlement 6 of the task" in a test). Grade and scope them as you see fit.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository.

`cycle.md` and the other files of the record directory — other agents' handoffs, reports and findings — are not yours to read, except those named here.

## Report

As `task-cycle/review/SKILL.md` gives, with the checks you ran (command and exit code), the number of decisions you read whole, **Unread material** and **Searches not found or unclear** (`none` is an answer), for each blocking finding the contradiction mark with the settlements, and the Minor findings with their scope. Return the first line of the report, the changed files with line counts, and the report path.
