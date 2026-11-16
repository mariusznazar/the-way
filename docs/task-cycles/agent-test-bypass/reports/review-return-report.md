FAIL 91f6c8841c07247739eec2830737155e8c8d42da

# Review of the return step's commits — agent-test-bypass

Range `1a17406a..91f6c884`, one commit (`91f6c884`, "Return step: name in WAY-409 and WAY-410 what
they leave out of the practices they take"), one file, `foundations/decisions.md`, 9 lines added,
2 removed. `git rev-parse HEAD` in the worktree is `91f6c8841c07247739eec2830737155e8c8d42da`, the
head given. Reviewed as section 2 of `task-cycle/review/SKILL.md` gives, against the task and the
entries the return step writes or corrects.

Counts: 1 blocking (Important, within the task), 0 Minor, 1 out of scope.

## Findings

### Important — within the task

**1. The return step added to the *Rejected* of WAY-409 and WAY-410 ways no human weighed, which
WAY-134 forbids, and settled on its own a collision between WAY-100 and WAY-134 that no relation
orders.**

Place: `foundations/decisions.md:6977-6980` (WAY-410, *Rejected*, from "; from ImpossibleBench's
option" to the end) and `foundations/decisions.md:7399-7403` (WAY-409, *Rejected*, from "; from the
card and the paper, what the decision leaves out" to the end).

What is wrong. Both decisions are written from rows 1 and 2 of the task's *Settlements to record*,
and both are marked `the cycle's` (the author's first report, `author-report.md` line 45: each
carries a pair of examples no row gives). For such a decision three texts of the foundation say the
same thing:

- WAY-134, binding sentence: the cycle "gives a decision written from a row as its rejected options
  only the ways not chosen that the row's source keeps, `none considered` where the human said so,
  or `unknown`"; its *violates* example: "the cycle fills a decision's rejected options with ways
  it derives from what the cycle would otherwise guess".
- `elements/decisions/template.md:88-93`: "A way the writer derives — from what the cycle would
  otherwise guess, from the cost of the way chosen, or from the foundation — never enters it
  (WAY-134)."; and `:94-95`: "The *Rejected* of a decision marked `the cycle's` takes `unknown`,
  unless a statement of the human names the ways weighed — then those ways, or `none considered`
  where the human said so."
- `task-cycle/skill/foundation_step.md:39-42`, by which the return step writes (`return_step.md`:
  "It writes, as the foundation step writes"): a row's entry needs no question for "a decision's
  *Rejected*, which takes the ways not chosen that the row's source keeps, … as the decisions'
  template gives (WAY-134), and an entry marked `the cycle's` takes it as that template gives".

The rows' sources (*Questions to settle*, questions 1, 2 and 3, their *Not chosen*) keep exactly the
ways the entries held at `1a17406a`. The added items — the card's system prompt, its monitoring of
edit and test-run cycles, the paper's read-only or hidden tests, its "fourth strategy", its
transcript monitors, its immediate termination — stand in no *Not chosen* and in no statement of the
human; they and the reasons beside them ("the review reads the diff and not the course of the
work", "a prompt is no way out for an agent that cannot meet the requirement") are the writer's
derivation from the sources.

On the author's doubt about the mark `the cycle's`: the template's rule for that mark does not lead
to `unknown` here, since a statement of the human (the *Not chosen* of each answer) names the ways
weighed; so the rows' ways were right to keep, and that same rule leaves no room for anything else.
Both template rules agree: the rows' ways, and nothing the writer adds.

On WAY-100: its second paragraph does ask a decision that adopts a practice from outside to put
what it leaves out in *Rejected*, and the task's *Decisions in play* names WAY-100 for these
signals. For a decision written from a row whose source keeps no such parts, WAY-100 and WAY-134
cannot both hold. Neither names the other in *Relations*, so no precedence is recorded. WAY-25
gives the route: "A collision between two decisions with no precedence recorded is never settled
silently by the agent that meets it … otherwise the agent stops and asks", and
`foundation_step.md:42-46` makes it a question for the human unless what the human accepted gives
the outcome. Nothing the human accepted gives this outcome: the task's line on WAY-100 speaks of
binding "through a decision", not of *Rejected*. The author's reason for preferring WAY-100, that
it is "the more specific" rule (`author-return-report.md` line 32), does not hold: WAY-100 is
specific to borrowed practices, WAY-134 to decisions written from rows, and neither is contained in
the other. The return step also had no remit for it: `return_step.md` corrects "whatever no longer
matches" the code, and the missing left-out parts were no mismatch with the code; they stood at
`1a17406a`, the head the whole change was reviewed at, and that review considered WAY-100 there and
raised no finding, citing the template (`review-whole-report.md` lines 212-214). The return step
reversed a reading the cycle had already settled.

Why it matters. The template's table names who reads *Rejected*: "the agent proposing an option
already weighed, who says what has changed since". The sentence a reader reads wrongly is WAY-410's
"from the card's mitigations, the system prompt that stresses general solutions — here the agent
commits its work and is resumed with the answer, and a prompt is no way out for an agent that
cannot meet the requirement": a later agent who proposes a system prompt against special-casing
reads it as a way already weighed and rejected, and must argue against a rejection no human made,
for a reason no human accepted. The same holds for WAY-409's transcript monitors and read-only
tests. The request presents each `the cycle's` entry by one sentence of its meaning and its added
pair (`request_template.md:514-515`), not by its *Rejected*, so the human merging would accept these
rejections without seeing them. A made-up rejection looks like a real one; this is what WAY-134
guards against.

Grade. Read as a departure from the form of the template, the finding cites a sentence a reader
reads wrongly, so WAY-364 grades it as any other finding. As any other finding it is Important: the
change's text does what a binding decision in force on a touched part (WAY-134, scope `decisions`,
`task-cycle`) forbids, and it settles a precedence that WAY-25 reserves to the human.

What must come out: the two added clauses, both entries restored to their *Rejected* at
`1a17406a` — WAY-410 ending "…has no other way out than the workaround." and WAY-409 ending "…but
the first case passes the review unseen." (in effect, the revert of `91f6c884`). The question of
the collision belongs before the human, as finding 2 says, not in the entries.

Evidence for the second question of the handoff, whether the added sentences are true of the
sources and the entries (each claim checked against the passages the foundation holds; the sources
were not opened again):

- True and held: "making the tests read-only or hidden" (`impossiblebench-test-modification`, § 5.2
  "Effect of hiding tests and making tests read-only"); "recording extra states" as a strategy
  (`impossiblebench-cheating-strategies`, § 4.1); "the immediate termination of an agent that flags
  the task" (`impossiblebench-abort-option`, § 5.3 "the agent doing so will be immediately
  terminated"); the leaving out of recording extra states agrees with the *Price* of WAY-409's
  *Rationale* ("a workaround that no signal names, such as recording extra states …, may pass").
- Held by the task and not by the cited fact: "its monitoring of long cycles of edits and test
  runs" — the task's *Context* quotes the card's "Excessive edit / test-execution cycles on a single
  file"; `claude-test-special-casing` holds only "Comments that suggest test-specific handling" and
  "Unexpected modifications to test files".
- Held by no entry and no file of the record: "the card's system prompt that stresses general
  solutions" (in both entries) and "its monitors that read transcripts" (the paper). Neither
  `claude-test-special-casing` nor any ImpossibleBench fact quotes them; the claims cannot be checked
  against what the decisions name in *Based on*.
- Inexact: "its fourth strategy (recording extra states)" — in the paper's list, as the fact gives
  it, recording extra states is the third of four, special-casing the fourth; a reader comparing with
  the fact takes "fourth" for special-casing, which WAY-409 takes.
- Reasons that do not fit their items: "the review reads the diff and not the course of the work"
  explains leaving out monitors of the course of the work, not the system prompt nor recording extra
  states, which shows in the diff; "a change to a test file is read under WAY-233" — WAY-233 has the
  scope `product-guidelines` and binds a product that has adopted the testing template, while
  WAY-409's own second paragraph rests on holding "whether or not the product has adopted the
  template of the testing discipline".

These points need no fix of their own: they leave with the removal above.

Contradiction: yes — WAY-134 (and `elements/decisions/template.md:88-95`, the rule on the
*Rejected* of a decision written from a row and of a decision marked `the cycle's`); WAY-25 for the
precedence settled without the human.

### Out of scope

**2. The foundation records no precedence between WAY-100 and WAY-134 for a decision written from
a row that adopts a practice from outside (Important by its effect; outside the task, not
blocking).**

Place: WAY-100 (`foundations/decisions.md:199-201`, "puts what it leaves out of the practice in
*Rejected*") and WAY-134 (`foundations/decisions.md:5285-5287`, "only the ways not chosen that the
row's source keeps").

What is wrong: where a row's source keeps no left-out parts of the practice, the two entries cannot
both hold, and neither names the other in *Relations*. This cycle read the collision both ways —
the review of the whole change by the template, the return step by WAY-100 — and each reading is
defensible from one entry. Every later cycle whose row adopts an outside practice meets it again.
The task does not ask for it to be settled, and recording a precedence changes a decision this task
does not carry, so it is outside the task. Recommended for the request's list, with the answer I
recommend: WAY-134 narrows WAY-100 for a decision written from a row, and the refinement of a task
whose row adopts a practice carries the parts left out among the *Not chosen* of the row's answer,
so that they reach *Rejected* as ways the human weighed. Leaving it unrecorded costs nothing today
but gives the next cycle the same choice between two readings.

## Third question of the handoff: mismatches the return step left

None found. At the head, compared with the two entries:

- WAY-409 against `task-cycle/review/SKILL.md` (section 2, the bullet "Code that passes a test
  without meeting the requirement…", lines 86-92; section 3, lines 136-137), `task-cycle/review/fix.md`
  lines 19-21 (the look named for a fix) and 27-28 (a correction's diff reviewed as section 2 gives):
  the four signals, the qualifier "only code whose branch, value or comparison exists to make a test
  pass", "Important at the least", and every review (slice, whole change, fix, return step,
  reconciliation and correction) agree.
- WAY-410 against `task-cycle/change/SKILL.md` (lines 48-50, 91-100, 147-148, 185),
  `task-cycle/skill/SKILL.md` (lines 19-24, 311-330, 472-478, 810-813),
  `task-cycle/skill/request_template.md` (lines 4-5, 224-227, the new row at 570) and
  `task-cycle/skill/correction.md` (lines 57-59, 74-75): both cases, the commit, the question naming
  the test, quoting the requirement and saying what was tried, the exception for a test the task
  expressly changes, the four sources of the orchestrator's answer, the blocked draft with the
  question under *Needed from you*, and no retry on a class higher for a slice's executor agree. The
  skill's addition that the author gives "the answer you recommend" is the general rule of section 6
  of `change/SKILL.md`, not a restatement that broadens the entry.

No skill file changed in the range; the restatements the review of the whole change found were
fixed in `1a17406a` and passed its review, and I do not reopen them.

## Declined to judge

- The content of the skills and the request template beyond their agreement with WAY-409 and
  WAY-410 — reviewed and passed by the review of the whole change and of its fix, not changed in
  this range.
- Whether WAY-409 and WAY-410 violate WAY-100 by naming no left-out parts at `1a17406a` — the review
  of the whole change judged that state and the cycle decided it; the open collision goes to
  finding 2.

## Checks

- `git rev-parse HEAD` — exit 0, `91f6c8841c07247739eec2830737155e8c8d42da`, the head given.
- `git log 1a17406a..91f6c884` and `git diff 1a17406a..91f6c884` — exit 0; one commit, one file.
- `git diff 4758840f..1a17406a -- task-cycle/` — exit 0; read to compare the skills with the two
  entries (third question).
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- Manual: the added sentences compared with the passages of the facts `claude-test-special-casing`,
  `impossiblebench-test-modification`, `impossiblebench-cheating-strategies`,
  `impossiblebench-abort-option` and with the task's *Context*; a search of the record directory for
  "prompt", "general solution" and "Excessive" (results above).
- Not run: the product's full gate — not the reviewer's, as the dispatch gives; no test reads the
  decision log's *Rejected*.

## Reaches beyond the dispatch

- `task-cycle/skill/foundation_step.md`, read whole — the return step writes as it gives, and it
  defines the mark `the cycle's` (lines 28-46).
- WAY-25 (`foundations/decisions.md:1162-1171`), binding sentences — the rule on a collision with no
  precedence recorded, which the template cites.
- `impossiblebench-test-modification` (`foundations/environment_facts.md:30-34`) — the source of
  "read-only or hidden" tests.
- `.runs/task-cycles/agent-test-bypass/reports/author-report.md` (lines 39-45, 93) — whether the two
  entries are marked `the cycle's`.
- `.runs/task-cycles/agent-test-bypass/reports/review-whole-report.md` lines 195-254 and
  `review-whole-source-quotes.txt` — whether the review of the whole change already judged WAY-100,
  and which source passages it verified.
- `elements/decisions/skill/SKILL.md` — searched for "the cycle's" as the dispatch asked; no hit
  (see below).
- `task-cycle/skill/request_template.md` lines 306-310 and 514-515, by search — what the request shows of
  an entry marked `the cycle's`.

## Working copies

None made. `.runs/review-return/` was never created;
nothing remains to remove.

## Unread material

- WAY-100, WAY-134, WAY-263, WAY-364, WAY-409, WAY-410, WAY-233: read whole except WAY-100's
  *Rejected* past line 252 and WAY-134's *Rationale* past line 5345, whose ends were not needed for
  the judgment.
- `elements/decisions/skill/SKILL.md`: not read whole; searched only for the mark `the cycle's`.
- The task: read whole.

## Searches not found or unclear

- `elements/decisions/skill/SKILL.md` — the dispatch says it speaks of the mark `the cycle's`; a
  search for "the cycle's" in it found nothing. The mark is defined in
  `task-cycle/skill/foundation_step.md:28-34` and its *Rejected* rule stands in
  `elements/decisions/template.md:94-95`.
- "The card's system prompt that stresses general solutions" and "the paper's monitors that read
  transcripts": not found in any fact of `foundations/environment_facts.md`, in the task, or in the
  record's reports.
