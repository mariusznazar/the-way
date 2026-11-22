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
  `product-guidelines/reading.md`. Read each guideline file whole (WAY-213). Write the index of
  your selection of decisions with the script the method gives, and read the index of the whole
  selection; run through the questions of the decisions outside the change's topic sections where
  the method gives that run, and open whole the decisions the method names. Count how many decisions
  of the index you read whole, for your report (WAY-150). The invariants, the part-map entries and
  the glossary entries you selected are read whole.
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
  `.the-way/product-guidelines/<discipline>/template.md`), at the commit of the-way the product
  pins.
- A reserved choice: does the change settle a language, a framework, a library, a store of data, a
  way of logging in or a place to run that the task, the spec and the foundation do not settle?
  Read `project-level/technology/reserved_choices.md` (in a product,
  `.the-way/project-level/technology/reserved_choices.md`) and judge the choice by it. A change
  that takes a reserved choice is a finding, Important by the general grade of section 3, a missed requirement.
- The tests: do they fail when the behaviour they protect breaks, and pass for a reason other than
  the code computing its own expected value? A test that asserts nothing is a finding.
- Code that passes a test without meeting the requirement the test stands for. Look in the code of
  the product that the change touches for a branch or a returned value made for the very input a
  test uses; the expected value of a test written into the product's code; a comment that names a
  special case for a test; and a change to the outcome of a comparison that a test makes, with no
  change to the test, such as an overloaded comparison operator. Only code whose branch, value or
  comparison exists to make a test pass is the finding: a special case that the requirement itself
  asks for is none. A finding of such code is graded as section 3 gives (WAY-409).
- Where the dispatch or the part map names a trust boundary the change touches — network, keys,
  deployment, files from outside — check hostile input at it. Where the change holds an operation
  that cannot be undone, check that it only prepares it.
- The author's own-work check: does the requirement it names fit where this change is weakest, and
  would its check catch that requirement unmet?
- The walk of the author, or of the executor of a slice, through the running product, in its
  report: does its judgment that the change alters, or does not alter, behaviour a user sees agree
  with the change; do its cases follow from the requirements of the task and not from the code
  alone; does each case it left unchecked give a reason?
- For a user interface, the states the applicable styleguide requires and the author's screenshot
  evidence; a screenshot file among the commits of the range is a finding (WAY-316). A
  screenshot you take to show the human lies in the place the foundation settles for screenshots,
  outside the product's repository, and your report names its address; where the foundation settles
  none, keep none (WAY-316). The file the screenshot tool writes by itself is a working
  copy, as the dispatch's paragraph on working copies gives.
- Run the checks that tell this change apart from a broken one: focused tests, a scratch run. Run
  them in a worktree of the head commit, in your directory for working copies that the dispatch
  names, when they need files changed; never change the reviewed worktree, its index or branch. The
  full suite is the cycle's own run before the request; do not repeat it. A check you could not run
  is unverified, and says why.
- A command that may run longer than your harness keeps its prompt cache — five minutes by default
  for a subagent in Claude Code — runs in the background, and you wait for it in stretches of under
  about four minutes, reading its output between them, and you end your turn only after it has
  ended and you have read its result (WAY-255). A run that has not ended 30 minutes after it
  started you stop and report as unfinished, with its command and the last lines of its output, in
  place of waiting on; the check it stood for is unverified, and says why (WAY-255, WAY-160).
- Do the whole review yourself. Never dispatch a subagent.

## 3. Grade

- **Critical** — a bug, a security hole, data loss, broken functionality.
- **Important** — the change cannot be trusted until fixed: a missed requirement, wrong or
  fragile behaviour, swallowed errors, a test that asserts nothing, damage you would refuse to
  merge.
- **Minor** — polish, style, broader coverage that would be nice.

Grade an appearance finding by its effect on the user, neither Minor because it is visual nor
blocking because it is visible. Appearance can carry the meaning by which a person chooses an
action, so a visual fault can change behaviour as seriously as incorrect code, and its consequence
draws the line without a second severity scale. A departure from a guideline example blocks only
through the consequence you name for the user or for the code. The same holds for a departure from
the part of an exemplar no script checks. Binding rules and their invariants keep their force, and
this criterion gives the orchestrator no authority to regrade or discard your finding. Examples
teach useful ways without acquiring the force of approved rules, and a comparison with no concrete
consequence turns taste into a blocker. Something the plan or the task
mandates is still a finding when it is a defect; name it so.
A finding of code that passes a test without meeting the requirement (section 2) is Important at
the least, in every review, so that it blocks (WAY-409).
A finding that a change departs from a foundation entry it writes or changes is
Important when the change's files do what the entry forbids, fail to do what it
requires, or restate it differently, including more broadly or without a
qualification (WAY-263).
A finding that a word should have a glossary entry, or that a word of the process lacks the
qualifier WAY-104 gives it in a product's foundation, is Minor unless it cites a sentence the files
hold that a reader would read wrongly for lack of it; with such a sentence it is graded as any other
finding. This does not reach the renaming of a word with two meanings (WAY-99), and a glossary entry
the change writes or changes is graded as the paragraph above gives (WAY-297).
A finding about the structure of code that lies below the threshold of the rule of size in the
product's coding guidelines is Minor, and so is every such finding where the product has no rule
of size, whatever the reason: for example, the product departed from the rule by a decision, it has
no coding guidelines at all, or its guidelines were written before the rule existed. You judge its
scope as for any finding; a finding about a function or a file over a threshold is graded as any
other finding (WAY-363).
A finding that a foundation entry departs from the form of its template, where the entry's content
agrees with the code, is Minor unless it cites a sentence a reader would read wrongly through the
departure; with such a sentence it is graded as any other finding. A finding that the entry's
content does not agree with the code stays Important, as the paragraph on WAY-263 above gives
(WAY-364).

A finding blocks when you grade it Critical or Important and it lies within the task (WAY-161).
List under **Declined to judge** each behaviour you considered and set aside as outside the task,
one line each with the reason; an empty list means you set nothing aside. A finding that goes
beyond the task says so in its own words and counts as out of scope, whatever its grade; so does
each line of Declined to judge. Each finding carries its place in the code, what is wrong, why it
matters and the evidence: the test, check or line that shows it, or the path in `reports/` of the
probe that shows it.

Each blocking finding also carries its mark of contradiction with the settlements, written under the
finding as `Contradiction: yes — <the entry or the settlement>` or as `Contradiction: no`. It is
`yes` where the finding says that the change does something against an entry of the foundation,
one the change itself writes included, or against a settlement of the task document: an answer
under its *Questions to settle*, a row of its *Settlements to record* or a decision of its
*Decisions in play*; the finding names that entry or settlement. It is `no` for every other
blocking finding, a point of *To do* left undone among them, since an unmet requirement is no
contradiction. The mark gives the finding no other grade and no other scope, and it is yours to
judge, as the grade is. The cycle carries it to its record, from which the audit of the process
reads whether a contradiction came out only after the code was written (WAY-404).

## 4. Report

Write the full report to the dispatch's report path. Its first line is `PASS <head sha>` or
`FAIL <head sha>` and nothing else — or `questions` while the review waits for an answer (below);
`FAIL` means at least one blocking finding. Then:

- the findings by grade, each with its place in the code, reasoning and evidence, each blocking
  finding with its mark of contradiction (section 3), and in the review of the whole change of a
  plan, each blocking finding with the slice it comes from, or none;
- for the review of a fix, each finding of the findings file as fixed or remains, and kept or
  withdrawn where contested; for a correction, each remark as made or not;
- **Declined to judge**;
- each check you ran, as its command and exit code or, for a manual check, its method and what it
  showed; each check you could not run, with the reason;
- each reach beyond the dispatch (section 1): what, where and why.
- each working copy you made: where it stood and that you removed it, or the remainder with its
  full path.
- **Unread material:** what of the dispatch — in the review of the whole change, of your own
  selection — you did not read whole, with what you read of it, or `none`. In the review of the
  whole change the section opens with how many decisions of the index of your selection you read
  whole, as section 1 counts them, and goes on with each decision that bears on the change and
  stayed unread, and each guideline file you did not read whole, or `none` after the count. Keep it
  apart from the next section.
- **Searches not found or unclear:** each thing you looked for and did not find, or that was
  unclear, wherever it arose — in the
  instructions, handoff, task, foundation or product code — or `none`.

Return to the orchestrator only the first line, the counts of blocking, Minor and out-of-scope
findings, a one-line check result naming what failed or did not run, and the report path
(WAY-148). Where the review cannot proceed without an answer, do not
guess: write a report whose first line is `questions`, with each question and the answer you
recommend, return that line and the report path, and wait to be resumed; the report gets its
`PASS` or `FAIL` first line when the review is finished.
