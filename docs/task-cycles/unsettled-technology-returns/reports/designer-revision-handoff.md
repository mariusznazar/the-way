# Handoff — the designer's one revision

The review of the spec returned `FAIL`. Its report, with nine findings, is
`.runs/task-cycles/unsettled-technology-returns/reports/spec-review.md`. Read it whole. Revise
`spec.md` once for every finding and append to `reports/designer.md` what each finding changed.
You keep the boundary of your first dispatch: you write only those two files, make no commit and
return `done` or `questions`.

## Orchestrator's answers

Two findings leave a choice the task does not settle. They are answered here, as the smallest
reading that fulfils the task, and they bind the revision.

- **Finding 6, the rule on doubt.** Take the rule out: a choice an agent cannot place is no third
  kind. Question 2's answer accepted that "o przypadkach granicznych decyduje osąd agenta", and row
  2 reserves a choice under the rule and leaves every other in the cycle. The examples To do 9 asks
  for are what helps the agent's judgment. The cost of being wrong is named in the task: a doubtful
  choice reaches the human in the request with code on it.
- **Finding 5, the grade.** WAY-263 does not change, since no row carries that and it does not reach
  a later task. `task-cycle/review/SKILL.md` grades a change that takes a reserved choice by the
  general grade of its section 3, a missed requirement, with no citation of WAY-263 for it.

For finding 8, read question 7 as it stands: it speaks of a decision of the foundation, and To do 6
keeps an approved definition untouched. So a choice a projected decision of an approved definition
settles is not reopened by a run; the list marks it `projected` as `list.md` does, and a human who
wants it changed goes the way `resolve_gaps.md` and WAY-118 give.

Where a finding needs a sentence of a skill changed that the spec had left as it stands, name the
file in the spec. Where it would need a decision's meaning changed beyond what the task carries,
return it as a question (WAY-30).
