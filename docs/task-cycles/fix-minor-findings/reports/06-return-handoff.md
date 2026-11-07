# Handoff 06 — the return step

**Stage.** The return step of the cycle (WAY-11), by the one author, resumed, on its class. Not a
review, not a fix of findings, not the gate. Worktree
`C:\Storage\repos\the-way\.runs\worktrees\fix-minor-findings`, branch `task/fix-minor-findings`,
head `a2a4b83`. Do not change the state of other branches or worktrees.

**Method.** Read `task-cycle/skill/return_step.md` whole (in the worktree), and
`task-cycle/skill/foundation_step.md` with it, as the return step writes as the foundation step
writes; the skill of an element when you write an entry of it.

**What to compare.** The foundation entries the change edited (WAY-161, WAY-162, WAY-289, WAY-297),
those the task names (*Decisions in play*: WAY-161, 162, 163, 287, 289) and those your search of
the foundation found, and the part map entries of `decisions`, `task-cycle`, `agent-instructions`,
each against the files of the repository as they stand at `a2a4b83`. Correct in the same change
whatever no longer matches. Write an invariant only for a rule the task, a decision or the human
sets; none is asked for here.

**Facts you need.**

- The review of the whole change is `PASS 820f963` (reports/02-review.md); the fix for its four
  Minor findings is `a2a4b83`, reviewed `PASS a2a4b83` (reports/05-review-fix.md).
- The reviewer of the fix found one Minor finding in your fix: WAY-162's binding text now has four
  sentences where WAY-05 says one to three. By the rule this change writes (WAY-161: a Minor finding
  of a review after the whole-change review is not fixed), the cycle does NOT fix it, and the return
  step does not touch it either — leave it exactly as it is. If your comparison finds it makes
  another entry untrue, say so in the report.
- The reviewer's one finding outside the task's scope (the request template's item 8 now points at
  `correction.md`, which the hand-made route of `agent-instructions/README.md` lacks) is not to be
  fixed either.
- Other records: Q1-Q4 and the choices of reports/01-author.md stand.

**Report.** `C:\Storage\repos\the-way\.runs\worktrees\fix-minor-findings\.runs\task-cycles\fix-minor-findings\reports\06-return.md`,
in the fields the cycle record's *Return step* gives: foundation compared with code (the entries
and what no longer matched, or none); decisions written or changed; invariants; environment facts;
glossary terms; part-map changes; projected entries; rows of *Settlements to record* written (rows
1-3 → WAY-161, WAY-162, WAY-289). Plus checks as command and exit code, **Searches not found or
unclear**. Commit only if you correct something (`git add` by path). Return only status, commits
(or `none`), a one-line check result, and the report path.
