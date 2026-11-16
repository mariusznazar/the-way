FAIL c8eef488248495d5b4e26b8a3a0cf01b79fbb352

# Review of the whole change — agent-test-bypass

Range `4758840f..c8eef488` (two commits: `477ea5ad` the three environment facts, `c8eef488` the two
decisions and the skill edits); `git rev-parse HEAD` in the worktree is `c8eef488248495d5b4e26b8a3a0cf01b79fbb352`.
Route: one author without a plan, so this review is the only review of the change; findings come
from no slice.

Counts: 1 blocking (Important), 3 Minor within the task, 0 out of scope.

## Findings

### Important

**I1. Two restatements of WAY-410 drop its second case, the test the agent cannot pass by general code.**

- Places:
  - `task-cycle/skill/SKILL.md:16-24` (the early-stop paragraph at the head of the skill): "Stop
    early only when … or when an agent's question about a test that contradicts the requirement is
    settled by no source (WAY-410). A slow step, a failed test or an unclear way to make the change
    is work to resolve, within that one retry for a slice, not a reason to ask the human."
  - `task-cycle/skill/request_template.md:570` (the new variant row), its *First line*:
    "`**State: blocked** — a test and the requirement contradict, and nothing the task settles says
    which holds`"; and in the same row, in *For you to decide*, "the ways open — the requirement
    stands and the test changes, or the test stands and the requirement changes".
- What is wrong: WAY-410 (written by this change) covers two cases with one way — "a test that
  expects what the requirement of the task rules out, **or that it cannot make pass by code that
  meets the requirement for every input**" — and the orchestrator's paragraph
  (`task-cycle/skill/SKILL.md:309-324`) and sub-step 4 of step 9 (`SKILL.md:468-473`) carry both.
  The head of the skill lists the early stops as an exhaustive list ("Stop early only when") and
  names only the contradiction; its next sentence then says that "a failed test … is not a reason to
  ask the human". An orchestrator that reads the head — the agent saw no contradiction and could not
  pass the test by general code, and no source settles it — finds in it that the cycle does not stop
  and that a failed test is work to resolve, which is what WAY-410 rules out. The new row's first
  line, the line the human reads first, states "a test and the requirement contradict" for every
  request of this variant, also where the agent saw no contradiction (the same row's next column
  admits that case: "where the agent saw no contradiction, the requirement it could not meet by
  general code"); and "nothing the task settles" names one of the four sources WAY-410 gives (the
  task, the spec, a decision, the sentence of an invariant). The "ways open" name only the two ways
  of a contradiction.
- Why it matters: WAY-263 grades as Important a change whose files restate an entry it writes
  "differently, including more broadly or without a qualification"; here the change's own files
  hold a narrower account of WAY-410 beside the full one, and the narrower one stands where it
  governs (the list of early stops, the request's first line). Task *Questions to settle* 3 chose
  that both cases go the same way and rejected "only an explicit contradiction".
- Evidence: the quoted lines; WAY-410's first binding sentence (`foundations/decisions.md:6909-6913`);
  the author's own-work check asserts the presence of the full wording in `SKILL.md` and the template
  and has no assertion that no narrower restatement stands elsewhere, so it passes on this head.
- A fix that would meet it (a suggestion, not a requirement): at `SKILL.md:20`, "an agent's question
  about a test that contradicts the requirement, or that it cannot pass by general code, is settled
  by no source (WAY-410)", and in the next sentence an exception for that case; in the template's
  first line, e.g. "a test and the requirement disagree, or no general code passes the test, and no
  source settles which holds", and a third way open for the second case.
- Scope: within the task (*To do* 3 and 4, *Questions to settle* 3, *Settlements to record* row 2).
- Contradiction: yes — WAY-410 (the entry the change writes) and the answer to *Questions to
  settle* 3 of the task.

### Minor (all within the task)

**M1. `task-cycle/skill/SKILL.md:322-324` — the stages "not run" assume a question met before the review of the whole change.**
The paragraph says, for every blocked draft of a question about a test: "The review of the whole
change, the return step and the reconciliation with the target branch have not run, and the request
names them as not run." `task-cycle/change/SKILL.md` section 2 binds every variant of `make-change`
— the fix of a review's findings and a correction among them — and the author's report (concern 4)
says so. A fix after the review of the whole change, or the return step, that meets such a test
would have the request say that the review of the whole change has not run when it has; a correction
that meets one finds the instruction to "open a blocked draft request" where the request is already
open, and neither this paragraph nor `correction.md` says that the request returns to a draft marked
`blocked` (the way `correction.md` gives for a reserved choice). The ordinary case, a first author
or a slice's executor, reads right. Suggested wording: "the stages that have not run on this code —
of the review of the whole change, the return step and the reconciliation — are named as not run";
and, for a correction, one sentence that the open request returns to a draft marked `blocked`.

**M2. `foundations/decisions.md:7393-7395` (WAY-409, *Rejected*) — the zero count is attributed to a register the task does not name for it.**
The entry reads "no case is known from the 83 task cycles of the process's author counted in his
register of problems of 2026-11-12 (his own record, not open to a reader of this repository)". The
task gives the zero only in *Questions to settle* 1, *Not chosen*: "zero przypadków w 83 cyklach",
with no record or date; the register of 2026-11-12 appears only in *Context*, for a different count
("trzy wiersze o czerwonym przebiegu nowego testu w 83 cyklach"), and *Po co to* says only "W
źródłach nie ma przypadku z cykli Mariusza". Joining the two passages is the author's inference
(the author says so, concern 3); the same number 83 makes it likely but the task does not state it,
and the entry presents it as where the zero was counted. Suggested wording, which keeps what WAY-90
asks (what was counted, over which cycles, the product's own, record not open): "no case is known
in the 83 task cycles of the process's author (his own record, not open to a reader of this
repository)". Graded Minor: the figure and the reasoning are the task's; only the stated place and
date of the count go beyond it.

**M3. Pointers to the new rule name the paragraph before it.**
Sub-step 4 of step 9 (`task-cycle/skill/SKILL.md:468-469`, "as the paragraph on an agent that
returns `questions` gives it"), the list of the record's copies (`SKILL.md:806-807`, "the paragraph
on an agent that returns `questions`") and the new template row (`request_template.md:570`,
"`SKILL.md`, "An agent that returns `questions`"") send the reader to the paragraph that opens "An
agent that returns `questions` gets your answers as step 6 answers the designer's — … the smallest
reversible reading …" (`SKILL.md:303-307`), while the rule stands in the next paragraph, "A question
about a test is answered otherwise (WAY-410)" (`SKILL.md:309`). The next paragraph follows at once
and opens with "otherwise", so a reader finds it; a reader who stops at the named one reads the
opposite answer. Suggested wording: "the paragraph on a question about a test".

## Judgments on the points the dispatch named

1. **Partly read material of the author.** I read whole WAY-85, WAY-161, WAY-162, WAY-263, WAY-90,
   WAY-27, WAY-229, WAY-227, WAY-135, WAY-268, WAY-269, WAY-404, WAY-405, WAY-05, WAY-12, WAY-293,
   the environment facts template and the glossary entries the change uses; the binding sentences
   of WAY-13, WAY-69, WAY-73, WAY-82, WAY-136, WAY-232, WAY-233, WAY-287 and WAY-289 from the index.
   The new entries agree with them: the three facts follow the form and WAY-85 (each quotes § 3.1
   or names the model measured); WAY-409's grade agrees with WAY-161 and WAY-263; WAY-410's blocked
   draft agrees with WAY-227 and WAY-287 (`blocked` in the first sentence, what the cycle needs and
   the stages not run under *Needed from you*); no conflict with WAY-232/WAY-233 (the test side),
   WAY-73 (each new fact is named by a decision's *Based on*) or WAY-82. The one disagreement found
   is I1, inside the change's own files. `walkthrough.md` was not needed: see point 9.
2. **Sources.** Every passage of the three new facts and both figures were checked, not a sample,
   against copies I downloaded (system card PDF, arXiv HTML `2510.20270v1` and PDF `2510.20270v1`),
   text extracted with `pdftotext -enc UTF-8`, matched after collapsing whitespace by a script that
   only read the files. All 7 passages of `claude-test-special-casing` stand in the card (§ 6 and
   § 6.2 headings confirmed: "6 Excessive Focus on Passing Tests", "6.2 Recommendations for Agentic
   Coding Use-Cases"); all 7 of `impossiblebench-cheating-strategies` stand in the HTML and the PDF
   (§ 4.1 "Types of Cheating"); all 4 of `impossiblebench-abort-option` stand in the PDF (§ 5.3
   "Effect of Feedback Loop"), and in the HTML as a reader sees it — the HTML sets "54%" and "9%"
   as MathML whose rendered text is the same. "from 54% to 9%" and "o3 from 49% to 12%" stand in
   the PDF; "much less pronounced for Claude Opus 4.1" in both. The result per passage is kept in
   `.runs/task-cycles/agent-test-bypass/reports/review-whole-source-quotes.txt`.
3. **Concern 1 (Claude Opus 4.1).** Faithful: the fact quotes "However, the effect is much less
   pronounced for Claude Opus 4.1" and WAY-410's *Rationale* says the size is no promise for the
   process's agents. The phrase "as WAY-85 gives" is a little loose — WAY-85 requires the sentence
   only where none of the measured models is of the agents' publisher, and Claude Opus 4.1 was
   measured — but saying it is accurate and harmless; no finding. The task's own text
   (`task.md:53`, `:72`) still reads as written; it was not changed.
4. **Concern 2 (WAY-328).** WAY-328 is withdrawn and WAY-392 now has the-way adopt the testing
   template, so the reason "nie w the way (WAY-328)" is false today; writing it would have put a
   false reason in the log. Dropping it and keeping the two reasons that hold is right and no
   finding; the human may be told at the merge. The other *Not chosen* are carried: Q1 both into
   WAY-409's *Rejected*; Q2 all three and Q3 the one into WAY-410's *Rejected*; Q4 is the *Out of
   scope* trial and rightly enters no entry. The *Rejected* names no way the writer derived, as the
   decisions template requires for a decision written from a row (WAY-134).
5. **Concern 3 (83 cycles).** See M2.
6. **Reach.** Both edits are needed. `review/fix.md` bounds what the review of a fix inspects ("what
   the fix itself broke"); without the clause the look of *To do* 1 ("w każdym przeglądzie …
   poprawki i korekty") would not reach the review of a fix; the review of a correction already
   goes through section 2 (`fix.md:27-28`). `correction.md` gives the blocked request of *To do* 3 its
   way on after the human's answer and keeps it out of the wait for CI, as for the other blocked
   kinds. Neither adds behaviour beyond the task.
7. **Template, kind 2 and agreement.** The row follows the pattern of "A question from the
   foundation step" and "A reserved choice" and carries the agent's question (what the test
   expects, the requirement, what was tried; the test's name in **Route**). Kind 2 admits the
   question and the status `questions`. `SKILL.md` points to `blocked_finding.md` for the wording of
   *Request URL and status* instead of restating it, so the invariant `blocked-request-wording`
   (two files) holds. `task-cycle/request_check.py` reads no row of the table of variants: its
   only template-reading test (`test_request_check.py`, `TemplateTest`) reads the skeleton's
   headings and the example of the decision section; its state line admits `blocked`. The author's
   claim holds. The disagreement is I1 (first line) and M3 (pointer).
8. **Narrowness and qualifications.** The reviewer's skill is narrow as the task intends: "Only code
   whose branch, value or comparison exists to make a test pass is the finding: a special case that
   the requirement itself asks for is none" (`review/SKILL.md:90-92`), graded "Important at the
   least, in every review, so that it blocks" (`:136-137`), the same as WAY-409. The author's
   bullet (`change/SKILL.md:90-99`) keeps every qualification of WAY-410, the exception for a test
   of behaviour the task expressly changes included. The orchestrator's paragraph keeps the four
   sources, the quote, "the smallest reversible reading never answers it" and the blocked draft;
   sub-step 4 keeps the no-retry. The two places that drop a qualification are I1.
9. **Coverage.** *To do* 1 (review/SKILL.md section 2 and 3, fix.md), 2 (change/SKILL.md sections
   1, 2, 5, 6), 3 (SKILL.md answer paragraph, sub-step 4), 4 (template kind 2 and row) and 5 (three
   facts, both decisions citing `claude-test-special-casing` and `impossiblebench-test-modification`
   in *Based on*, figures checked in the PDF) are met; rows 1 and 2 of *Settlements to record* are
   WAY-409 and WAY-410, row 2's "zawęża regułę ponowienia z WAY-229" as `narrows WAY-229`. Nothing
   unasked is added; the *Out of scope* trial appears nowhere in the diff (searched). The author's
   walk: "none — the change alters no behaviour a user sees in a running product" agrees with the
   change, which alters only process text and foundation entries of the-way; no code, no test and
   no script changed (the diff's eight files are Markdown).

## The author's own-work check (WAY-164)

The requirement it names — that the skills restate the two decisions without widening them or
dropping a qualification — is where this change is weakest, and rightly chosen. The check asserts
that each element of the decisions is present (18 assertions); it cannot see a second, narrower
restatement elsewhere in the same files, which is what I1 is, so it would not catch the requirement
unmet in that form.

## The structure of the code the change leaves

`python -B task-cycle/change_file_sizes.py 4758840f c8eef488`: eight Markdown files modified, +207
lines net (`task-cycle/skill/SKILL.md` 860→888, `foundations/decisions.md` 11175→11308, the others
+1 to +18). The rule of size in `guidelines/coding.md` ("The rule covers scripts; a test file stands
outside it") reaches none of these files, so the size test was not run in worktrees of the base and
head: it measures scripts, and the range changes none. No code without a user, no name that stopped
being true. No finding.

## Declined to judge

none

## Checks

- `python -B elements/common/foundation_check.py` (reviewed worktree) — exit 0, `0 errors`.
- `python -B gate/run_tests.py task-cycle` (reviewed worktree, focused directory run) — exit 0,
  534 tests, `OK (skipped=2)`.
- `python -B task-cycle/change_file_sizes.py 4758840f c8eef488` — exit 0 (numbers above).
- Source check: `curl -sSL` of the three addresses — exit 0 each; `pdftotext -enc UTF-8` of both
  PDFs — exit 0 each; a passage-matching script run with `python -I -B` — exit 0, 21 lines of
  result, kept in `reports/review-whole-source-quotes.txt`.
- `python -B elements/common/decision_index.py --output … --sections` — exit 0; the index run with
  sections, parts and `--decision` — exit 0 (after two runs that ended with exit 2 because I gave
  `--decision` bare numbers; the script takes `WAY-NN`).
- Manual: the diff read whole; search of the diff for the *Out of scope* trial (one hit, the "83"
  of M2, unrelated); `grep` of the-way for the other uses of "smallest reversible" and of the
  wording `blocked draft, opened on this commit`; reading of `request_check.py` and its
  `TemplateTest`.
- Not run: the full gate (the cycle's own run, per the dispatch); the size test in worktrees of base
  and head (no script changed, see above).

## Reaches beyond the dispatch

- `elements/decisions/template.md` lines 76-115 and 186-201 — to judge the *Rejected* of a decision
  written from a row (it settled that the left-out parts of the sources' lists may not enter
  *Rejected*, so I raised no WAY-100 finding) and the `narrows` relation.
- `elements/environment-facts/template.md` whole — the form of the three facts.
- `task-cycle/skill/blocked_finding.md` whole, `task-cycle/skill/correction.md` lines 1-80,
  `task-cycle/record_template.md` lines 224-230, `foundations/invariants.md` lines 1-115 and the
  entries `blocked-request-wording`, `blocked-request-label` — the wording of a blocked record and
  its invariant.
- `task-cycle/request_check.py` (by grep) and `task-cycle/test_request_check.py` lines 899-925 — point 7.
- `task-cycle/spec/design.md` (grep for "smallest reversible") — other places of that rule.
- The author's own-work check script, read whole.

## Working copies

- `.runs/review-whole/` held the decision index, the
  section list, an extraction script, the downloaded system card and ImpossibleBench (HTML and PDF)
  with their extracted texts, the matching script, the size and foundation-check outputs and the
  test output. Removed whole. Kept in `reports/`: `review-whole-source-quotes.txt`. No worktree or
  clone was made; nothing remains.

## Unread material

- Decisions of the index of my selection read whole: 18 (WAY-05, WAY-12, WAY-27, WAY-85, WAY-90,
  WAY-135, WAY-161, WAY-162, WAY-227, WAY-229, WAY-263, WAY-268, WAY-269, WAY-293, WAY-404, WAY-405,
  WAY-409, WAY-410). The index lists 63 in full (binding sentences read) and 105 by heading (run
  through; of them WAY-27, WAY-268, WAY-269, WAY-404 and WAY-405 opened whole). Decisions bearing on
  the change known from the index and not opened whole: WAY-03, WAY-13, WAY-69, WAY-73, WAY-82,
  WAY-100, WAY-136, WAY-164, WAY-232, WAY-233, WAY-287, WAY-289 — their binding sentences left open
  nothing the review had to judge.
- Guideline files: `guidelines/coding.md` and `guidelines/testing.md` not read whole; I judged that
  the change reaches no code or test (eight Markdown files of process text and foundation entries),
  so `product-guidelines/reading.md` selects none; of `coding.md` I read the rule of size (lines
  75-83) and the *Applies to* headers of every guideline file.
- `foundations/invariants.md`: read lines 1-115 and the two blocked-request invariants; the other
  invariants whose *Part* names `task-cycle` (scripts, imports, sizes, refusals of crafted input)
  known by heading only — they hold scripts the change does not touch.
- `foundations/glossary.md`: the entries of the terms the change uses (environment fact, foundation
  step, gate, open design choice, reserved choice, return step, slice); not read whole.
- `foundations/environment_facts.md`: the diff and the existing `impossiblebench-test-modification`
  entry; the other entries not read.
- `task-cycle/change/walkthrough.md`: not read; the change alters no behaviour a user sees.

## Searches not found or unclear

- `elements/common/decision_index.py --decision` takes `WAY-03`, not `03` or `3`; its usage line
  says `--decision NUMBER`, which I read as the bare number, and the script ended with exit 2
  ("no decision 3").
- The place where the task's "zero przypadków w 83 cyklach" was counted: the task does not say
  (see M2).
