---
name: review-change
description: Use to review the code of one change in a the-way task cycle as an agent that did not make it — a planned slice, the whole change, the fix of earlier findings, or a later change to an open request. Read-only; returns PASS or FAIL, graded findings and the checks it ran.
---

# Review a change

Reviews one range of commits of a task's change for the cycle `implement-task`, which dispatches
every code review: of a planned slice that touches a trust boundary or holds an operation that
cannot be undone, of the whole change, of the fix of a review's findings, of the commits of the
return step, of the reconciliation with the target branch, and of each later change to the open
request. The reviewer did not make the change. The cycle decides what happens after the review;
this skill holds only how the review is made and reported.

This skill lives in `task-cycle/review/` of the-way. In the-way itself, the-way is the checkout or
worktree the session works in; in a product, it is the product's pinned `.the-way`.

## 1. Read

- The dispatch: what is reviewed — a slice by its number, the whole change, a fix, the return step's
  commits, the reconciliation with the target branch or a later change — the base and head commits
  of the range, and the report path. The return step's commits are reviewed as section 2 gives,
  against the task and the foundation entries the return step writes or corrects.
- For the review of the whole change, read `whole_change.md` and follow it: what you read and
  what you check besides section 2. You alone among the reviewers select your
  own foundation and guidelines: the entries of the parts the change touches by "Reading the
  foundation" in `elements/common/way_of_working.md`, and the guidelines of those parts by
  `product-guidelines/reading.md`, each entry and guideline file whole (WAY-150, WAY-213).
- For any other review — of a slice, a fix, the return step's commits, the reconciliation with the
  target branch or a correction — what the dispatch names, as the orchestrator selected it
  (WAY-150): the passages of the task, spec and plan it carries word for word, each with its file
  as its address, the foundation entries by identifier, each whole, and
  the guideline files, each whole (WAY-213). A slice's reviewer gets the selection its executor
  got and judges the slice against the passages of the task the dispatch gives, not the plan
  alone.
- The author's report. It is a set of claims to verify, not evidence: a rationale in it — kept
  simple on purpose, left for later — never lowers a finding's grade.
- For the review of a fix, or of a correction made for the human's remarks on the request, read
  `fix.md` and follow it: what you read and what bounds the review.
- The diff of the range, computed yourself: `git diff <base>..<head>` and `git log <base>..<head>`.
  Never `HEAD~1`, which drops all but the last commit. Confirm that `git rev-parse HEAD` is the
  head you were given; on a mismatch, ask the orchestrator which range to review, as a question of
  section 4, before you go on.

Beyond what the dispatch names — and, in the review of the whole change, beyond what you select —
where you need something more — a decision, an invariant, a passage of the
task, the guidelines of a part it did not cover — reach for it selectively: search for its
identifier or a word and read the passage found, a foundation entry whole, never a whole file of
the foundation, and a guideline file whole (WAY-150, WAY-213). Name each such reach in your report
— what, where and why.

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
- Against the guidelines: compare a change of code with each rule of the guidelines you read that
  has no invariant and that the change reaches (WAY-168).
- Where the change writes or changes a product's guidelines, compare them with
  `product-guidelines/template.md` (in a product, `.the-way/product-guidelines/template.md`) and,
  where the-way gives one, the template of their discipline,
  `product-guidelines/<discipline>/template.md` (in a product,
  `.the-way/product-guidelines/<discipline>/template.md`), at the commit of the-way the product pins
  (WAY-170).
- A reserved choice: does the change settle a language, a framework, a library, a store of data, a
  way of logging in or a place to run that the task, the spec and the foundation do not settle?
  Read `project-level/technology/reserved_choices.md` (in a product,
  `.the-way/project-level/technology/reserved_choices.md`) and judge the choice by it. A change
  that takes a reserved choice is a finding, Important by the general grade of section 3, a missed requirement.
- The tests: do they fail when the behaviour they protect breaks, and pass for a reason other than
  the code computing its own expected value? A test that asserts nothing is a finding.
- Where the dispatch or the part map names a trust boundary the change touches — network, keys,
  deployment, files from outside — check hostile input at it. Where the change holds an operation
  that cannot be undone, check that it only prepares it.
- The author's own-work check: does the requirement it names fit where this change is weakest, and
  would its check catch that requirement unmet?
- For a user interface, the states the applicable styleguide requires and the author's screenshot
  evidence (WAY-219).
- Run the checks that tell this change apart from a broken one: focused tests, a scratch run. Run
  them in a separate worktree of the head commit when they need files changed; never change the
  reviewed worktree, its index or branch. The full suite is the cycle's own run before
  the request; do not repeat it. A check you could not run is unverified, and says why.
- A command that may run longer than your harness keeps its prompt cache — five minutes by default
  for a subagent in Claude Code — runs in the background, and you wait for it in stretches of under
  about four minutes, reading its output between them (WAY-255).
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
A finding that a change departs from a foundation entry it writes or changes is
Important when the change's files do what the entry forbids, fail to do what it
requires, or restate it differently, including more broadly or without a
qualification (WAY-263).

A finding blocks when you grade it Critical or Important and it lies within the task (WAY-161).
List under **Declined to judge** each behaviour you considered and set aside as outside the task,
one line each with the reason; an empty list means you set nothing aside. A finding that goes
beyond the task says so in its own words and counts as out of scope, whatever its grade; so does
each line of Declined to judge. Each finding carries its place in the code, what is wrong, why it
matters and the evidence: the test, check or line that shows it.

## 4. Report

Write the full report to the dispatch's report path. Its first line is `PASS <head sha>` or
`FAIL <head sha>` and nothing else — or `questions` while the review waits for an answer (below);
`FAIL` means at least one blocking finding. Then:

- the findings by grade, each with its place in the code, reasoning and evidence, and in the
  review of the whole change of a plan, each blocking finding with the slice it comes from, or
  none;
- for the review of a fix, each finding of the findings file as fixed or remains, and kept or
  withdrawn where contested; for a correction, each remark as made or not;
- **Declined to judge**;
- each check you ran, as its command and exit code or, for a manual check, its method and what it
  showed; each check you could not run, with the reason;
- each reach beyond the dispatch (section 1): what, where and why.
- **Searches not found or unclear:** each thing you looked for and did not find, or that was
  unclear, wherever it arose — in the
  instructions, handoff, task, foundation or product code — or `none`.

Return to the orchestrator only the first line, the counts of blocking, Minor and out-of-scope
findings, and the report path (WAY-148). Where the review cannot proceed without an answer, do not
guess: write a report whose first line is `questions`, with each question and the answer you
recommend, return that line and the report path, and wait to be resumed; the report gets its
`PASS` or `FAIL` first line when the review is finished.
