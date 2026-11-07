# Handoff 02 — review of the whole change

**Delegation.** The orchestrator of a the-way task cycle (me) dispatches you; Mariusz delegated
intermediate choices to the orchestrator. Nothing here is the human's approval.

**Worktree.** `C:\Storage\repos\the-way\.runs\worktrees\fix-minor-findings`. Branch
`task/fix-minor-findings`. Read-only: never change this worktree, its index or its branch. If a
check needs files changed, use a separate worktree of the head commit under
`C:\Storage\repos\the-way\.runs\` (and remove it afterward). This is the-way itself, with no pin.

**Method.** Read `task-cycle/review/SKILL.md` whole (in the worktree) and follow it as "the review
of the whole change": it names `whole_change.md`, which you read; `fix.md` is not yours. You select
your own foundation and guidelines by "Reading the foundation" in
`elements/common/way_of_working.md`. Never dispatch a subagent.

**Range.** Base `86cc21e876f27f5d7d3ffd811ba11b687ac04cc6`, head `820f963` (two commits: `8eafea5`
decisions, `820f963` cycle documents). Confirm `git rev-parse HEAD` is `820f963...` first.

**Task.** The frozen task document, whole:
`C:\Storage\repos\the-way\.runs\worktrees\fix-minor-findings\.runs\task-cycles\fix-minor-findings\task.md`.
Review the change against it: its *To do* items 1–3, its *Questions to settle* with their answers
(and *Not chosen*), *Decisions in play*, and the three rows of *Settlements to record*. Check
coverage of every task item, every settlement row, and source fidelity (the entries must carry the
rows' meaning; the wording may differ; the *Rejected* of each entry should hold the task's *Not
chosen* ways). This is a change to prose and decision text, not code; the checks that matter are
whether the texts agree with each other and with the rows, whether any line elsewhere in the
repository is now untrue (a search of the whole repository for statements that Minor findings are
never fixed, or that a fix runs for blocking findings only, outside `.runs/` and `docs/task-cycles/`),
and `python -B elements/common/foundation_check.py` plus the focused tests of `task-cycle` and
`agent-instructions` (`python -B gate/run_tests.py task-cycle` etc.; do not run the whole gate).

**Author's report** (claims to verify, not evidence):
`C:\Storage\repos\the-way\.runs\worktrees\fix-minor-findings\.runs\task-cycles\fix-minor-findings\reports\01-author.md`.

**Answers of step 4.** Trust boundary: no. Irreversible operation: no. One author without a plan,
no spec. The foundation entries the change writes: WAY-161 (row 1), WAY-162 (row 2), WAY-289
(row 3), and WAY-297 (the cycle's, a consequence edit); also check them against the rest of the
foundation (WAY-263: restating an entry differently, more broadly or without a qualification is
Important).

**Choices the cycle made, which bind the author (judge whether they are sound, but they are not
defects for being the cycle's):**

- The fix for Minor findings is made by the one author (resumed, own class); on a planned route by a
  fresh agent on the orchestrator's class. Its review is by the whole-change reviewer.
- The fix takes in only the Minor findings that the whole-change report lists and has not marked
  outside the task's scope.
- A reverted fix's new Critical or Important finding goes to the request's *Minor findings* list
  with its grade; no new heading, so `task-cycle/request_check.py` is unchanged.
- `correction.md` gets its own paragraph for the answer "fix it in this request".
- `agent-instructions/README.md` (the hand-made route outside a cycle) is left unchanged on
  purpose.
- The revert of a failed Minor-only fix is made by the orchestrator, in one revert commit.

**Report.** Write it to
`C:\Storage\repos\the-way\.runs\worktrees\fix-minor-findings\.runs\task-cycles\fix-minor-findings\reports\02-review.md`
as `review-change` section 4 gives (first line `PASS <sha>` or `FAIL <sha>`; findings by grade
with place, reasoning and evidence; **Declined to judge**; checks as command and exit code; reaches;
**Searches not found or unclear**). Mark every finding that lies outside the task's scope as such in
its own words. List each Minor finding with its place in the code so the cycle can fix it; the cycle
will fix the in-scope Minor findings of your report. Return only the first line, the counts of
blocking, Minor and out-of-scope findings, a one-line check result, and the report path.
