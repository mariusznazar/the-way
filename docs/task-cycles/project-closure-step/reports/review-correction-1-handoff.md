# Handoff — review of correction 1 (task `project-closure-step`)

You are a fresh reviewer of the strongest class, and you made none of this change. Review, with
`review-change` (`task-cycle/review/SKILL.md`), a correction made for the human's remarks on the open request
https://github.com/mariusznazar/the-way/pull/150, as `task-cycle/review/fix.md` gives it for a correction: read
that file whole and follow what it says you read and what bounds the review. The remarks stand in place of a
findings file. Read-only: change and commit nothing. Questions go to the orchestrator.

- Worktree and branch: `the task's worktree`, `task/project-closure-step`. Work from its
  root.
- Range of the correction: base `935109fba7458cef123b1e2b749a32f48902b34b` (the request's head before the
  correction), head `4101de84` (confirm `git rev-parse HEAD`; a return step of the correction may add a commit
  after it that is reviewed apart; your range ends at `4101de84`). Compute `git diff 935109fb..4101de84` and
  `git log 935109fb..4101de84` yourself: two commits, `43e9c4a7` and `4101de84`, 6 files
  (`project-level/plan_check.py`, `project-level/test_plan_check.py`, `foundations/invariants.md`,
  `project-level/plan/template.md`, `project-level/lead/skill/closure.md`, `project-level/lead/skill/SKILL.md`).
- The remarks that bind, word for word, are in
  `.runs/task-cycles/project-closure-step/reports/correction-1-remarks.md`. The one that asks for work (item 2):

  > 2. **A closed plan passes the check although two of its tasks are each marked "delivered by the other"** —
  > **fix in this request**: the check refuses a closed plan where following "delivered by another task" never
  > reaches a task that is done (a loop of such rows, of any length), with a test for the pair and for a longer
  > loop. It is a small addition to the check this request already changes, and the harm is the one the closing
  > exists to prevent; a task for it would cost a whole cycle to read the same code again.

  Items 1 and 3 are let through with no task and items 4–12 accepted: a change that touches what they let
  through or accept is outside the correction. The orchestrator's choice Q5 carried by the correction (not in the
  remarks): the closing step also holds a row whose chain of deliveries never reaches a done task, as it
  already holds a row delivered in a dropped task (`closure.md` section 1 and the lead skill's step 1);
  judge it against the task (*To do* 2 and 5 in `.runs/task-cycles/project-closure-step/task.md`, Polish) and
  the earlier choice it extends.
- The author's report of the correction, a set of claims to verify:
  `.runs/task-cycles/project-closure-step/reports/author-correction-1-report.md`.
- Trust boundary: **yes** (`plan_check.py` is a trust boundary file of the part `project-level`): check crafted
  input yourself — loops of two, three and more rows, a loop with a tail and shared tails, self-reference,
  delivery in a task the plan lacks, a long chain and a plan of a thousand rows (the follow must end and not
  recurse), rows in the closed plan in other states, a handed-over plan holding the same rows (the check is for
  closed plans only), CRLF, and that the findings come at the right row — and report what you ran. Irreversible
  operation: no.
- You may run `python -B gate/run_tests.py project-level` and `elements/common/foundation_check.py` and the
  tests of one directory; not the whole gate. Report each check with its command and exit code.
- Your report: `.runs/task-cycles/project-closure-step/reports/review-correction-1-report.md`, first line
  `PASS <sha>` or `FAIL <sha>`, graded findings (Critical, Important, Minor, outside the task's scope), **Unread
  material**, **Searches not found or unclear**. Your directory for working copies:
  `.runs/review-correction-1/`; the same paragraph on working copies as in the earlier handoffs holds (make
  nothing outside it, remove it before you return, state it in the report).
- Select your own foundation and guidelines for the parts the correction touches, as `review-change` gives for
  a correction; the pointers to start from: the invariants `project-plan-check` and `project-plan-form`, WAY-142,
  WAY-146, WAY-385, WAY-379, WAY-382, and `guidelines/coding.md`, `coding-check.md`, `testing.md`.
- The files of the record directory other than those named here are not yours to read.
