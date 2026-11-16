# Findings of the review of the whole change, for the fix

Reviewer's report: `reports/review-whole-report.md`, first line `FAIL c8eef488248495d5b4e26b8a3a0cf01b79fbb352`. Range `4758840f..c8eef488`. The blocking finding and then the Minor findings within the task, in the reviewer's words. The reviewer marks no finding outside the task's scope.

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
