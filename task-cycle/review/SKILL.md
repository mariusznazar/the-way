---
name: review-change
description: Use to review the code of one change in a the-way task cycle as an agent that did not make it — a planned slice, the whole change, the fix of earlier findings, or a later change to an open request. Read-only; returns PASS or FAIL, graded findings and the checks it ran.
---

# Review a change

Reviews one range of commits of a task's change for the cycle `implement-task`, which dispatches
every code review: of a planned slice, of the whole change, of the fix of a review's findings, and
of each later change to the open request. The reviewer did not make the change. The cycle decides
what happens after the review; this skill holds only how the review is made and reported.

This skill lives in `task-cycle/review/` of the-way. In the-way itself, the-way is the checkout or
worktree the session works in; in a product, it is the product's pinned `.the-way`.

## 1. Read

- The dispatch: what is reviewed — a slice by its number, the whole change, a fix or a later
  change — the base and head commits of the range, and the report path.
- The frozen task document in full — or, where the dispatch states the requirement in its place,
  that statement — and the spec where the cycle wrote one. For a slice, the plan and that slice;
  the slice is judged against the task, not the plan alone.
- The author's report. It is a set of claims to verify, not evidence: a rationale in it — kept
  simple on purpose, left for later — never lowers a finding's grade.
- For the review of a fix, the findings file — the blocking findings of the review it answers —
  and the fix report. For the review of a correction made for the human's remarks on the request,
  those remarks and the correction report.
- For the review of the whole change, the Minor and out-of-scope findings of the slice reviews the
  dispatch lists.
- The foundation entries and guidelines of the parts the change touches, selected by "Reading the
  foundation" in `elements/common/way_of_working.md` and `product-guidelines/reading.md`. Read
  each selected entry and guideline file whole.
- The diff of the range, computed yourself: `git diff <base>..<head>` and `git log <base>..<head>`.
  Never `HEAD~1`, which drops all but the last commit. Confirm that `git rev-parse HEAD` is the
  head you were given; on a mismatch, ask the orchestrator which range to review before you go on.

A dispatch that calls a finding wrong, Minor or outside the scope does not bind you: grade and
scope are yours.

## 2. Review

- Begin at the reach of the change: the diff, its callers, the contracts it touches and its tests.
  Take the claim most likely to be false first, and ask what would make the change wrong.
- Against the task: what it requires and the change misses or only claims; what the change adds
  that nobody asked for; what it builds the wrong way. The spec says what the software must do; for
  behaviour it is silent on, a reasonable user's expectation is a requirement, and silence is not
  permission.
- Against the foundation: the decisions and invariants of the touched parts, and the foundation
  entries the change itself writes or changes — do they say what the code does? A changed
  invariant test is named in your report.
- The tests: do they fail when the behaviour they protect breaks, and pass for a reason other than
  the code computing its own expected value? A test that asserts nothing is a finding.
- Where the dispatch or the part map names a trust boundary the change touches — network, keys,
  deployment, files from outside — check hostile input at it. Where the change holds an operation
  that cannot be undone, check that it only prepares it.
- The author's own-work check: does the requirement it names fit where this change is weakest, and
  would its check catch that requirement unmet?
- For a user interface, the states the applicable styleguide requires and the author's screenshot
  evidence (WAY-219).
- Run the checks that tell this change apart from a broken one: focused tests, a scratch run. Run them in a separate worktree of the head commit when they need files changed; never
  change the reviewed worktree, its index or branch. The full suite is the cycle's own run before
  the request; do not repeat it. A check you could not run is unverified, and says why.
- Do the whole review yourself. Never dispatch a subagent.

## 3. Grade

- **Critical** — a bug, a security hole, data loss, broken functionality.
- **Important** — the change cannot be trusted until fixed: a missed requirement, wrong or
  fragile behaviour, swallowed errors, a test that asserts nothing, damage you would refuse to
  merge.
- **Minor** — polish, style, broader coverage that would be nice.

Grade an appearance finding by its effect on the user, neither Minor because it is visual nor
blocking because it is visible (WAY-220). A departure from a guideline example blocks only through
the consequence you name for the user or for the code (WAY-221). Something the plan or the task
mandates is still a finding when it is a defect; name it so.

A finding blocks when you grade it Critical or Important and it lies within the task (WAY-161).
List under **Declined to judge** each behaviour you considered and set aside as outside the task,
one line each with the reason; an empty list means you set nothing aside. A finding that goes
beyond the task says so in its own words and counts as out of scope, whatever its grade; so does
each line of Declined to judge. Each finding carries its place in the code, what is wrong, why it
matters and the evidence: the test, check or line that shows it.

## 4. Review of a fix

The findings file bounds this review; it holds the blocking findings only, since Minor and
out-of-scope findings are not fixed (WAY-161). For each finding in it, say whether it is **fixed**
— the defect no longer exists on the new head; tried is not fixed — or **remains**, with evidence.
For a finding the author contests with evidence, say whether you keep it. Inspect the fix diff for
what the fix itself broke: a new Critical or Important finding there counts as one that remains.
An issue outside the fix diff is a Minor or out-of-scope note; it does not reopen the review.

For a correction made for the human's remarks, the remarks take the findings file's place: say for
each whether the correction makes it, then review the correction's diff as section 2 gives.

## 5. Review of the whole change

Besides section 2, check the change against the whole task: every required outcome and item of
*To do*, and every row of *Settlements to record* and projected entry the task carries, met by the
commits; fidelity to the task's sources, with nothing the change takes from them altered or
invented; foundation entries written before the code that depends on them. Grade each Minor and
out-of-scope finding of the slice reviews the dispatch lists as a finding of this review.

## 6. Report

Write the full report to the dispatch's report path. Its first line is `PASS <head sha>` or
`FAIL <head sha>` and nothing else; `FAIL` means at least one blocking finding. Then:

- the findings by grade, each with its place in the code, reasoning and evidence;
- for the review of a fix, each finding of the findings file as fixed or remains, and kept or
  withdrawn where contested; for a correction, each remark as made or not;
- **Declined to judge**;
- each check you ran, as its command and exit code or, for a manual check, its method and what it
  showed; each check you could not run, with the reason.

Return to the orchestrator the first line, the counts of blocking, Minor and out-of-scope
findings, and the report path. Send a question back instead of guessing where the review cannot
proceed without an answer.
