# Findings of the review of the return step, for the fix

Reviewer's report: `reports/review-return-report.md`, first line `FAIL 91f6c8841c07247739eec2830737155e8c8d42da`. Range `1a17406a..91f6c884`. The one blocking finding, in the reviewer's words; the review of the return step lists no Minor finding within the task.

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
