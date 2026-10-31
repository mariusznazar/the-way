FAIL

# Review of the revised spec — unsettled-technology-returns

Spec: `.runs/task-cycles/unsettled-technology-returns/spec.md`, as revised once for the nine findings
of `reports/spec-review.md`, read against the end of `reports/designer.md` and the orchestrator's
answers in `reports/designer-revision-handoff.md`. Paths are relative to the worktree. All nine
findings are resolved. The way finding 9 was resolved brought one new finding, below.

## The nine earlier findings

| # | Finding | State | Where |
|---|---|---|---|
| 1 | A run for a choice outside the rule had no way in | resolved | `spec.md:313-316`, `:352-357`; three cases in `resolve_gaps.md`, the rule deciding only the first |
| 2 | A held choice met three sentences that send it away | resolved | `spec.md:111-118`, `:252-254`; one exception each, for exactly the decision the human opened |
| 3 | A remark on a blocked request had no home | resolved | `spec.md:189-200`, `:250-251`; `correction.md` gains the case, told apart by the record's field |
| 4 | `git fetch --prune` broke the same decision | resolved | `spec.md:415-428`; four named steps in order, prune excluded with its reason |
| 5 | "Important by WAY-263" did not hold | resolved | `spec.md:248`, `:486-487`; as the orchestrator answered |
| 6 | The rule on doubt was broader than its entry | resolved | `spec.md:233-236`, `:272`, `:294-296`, `:300-301`; taken out, as the orchestrator answered |
| 7 | A run at an accepted document left `ready for cycle` | resolved | `spec.md:133-134`, `:321-324` |
| 8 | No marker for a choice a projected decision settles | resolved | `spec.md:89-92`, `:331-334`, `:358-361`, `:466`; as the orchestrator read question 7 |
| 9 | The same choice in two members of a round had no form | resolved, with the new finding below | `spec.md:369-378` |

## New finding

### 10. A request for a run, sent as a question, reaches an agent whose method answers it

Kind: a contradiction with the task and the foundation, brought by the revision.

To give finding 9 its canonical question, `spec.md:369-371` has the refiner write a request for a run
"as a question of its turn too", so that the answering agent marks it. That holds for every run of
an orchestrated round, since the refiner cannot know beforehand that another member names the same
choice. The first version kept the request as a *Child-work request*, which the answering agent does
not answer.

The answering agent answers every question it reads, by `project-level/lead/answering.md`, which the
spec does not change:

- Lines 34-36: "If no authorized source answers, prepare the complete question to the human, available
  ways, what each costs and your recommendation." For a technology choice, these would be options
  with costs and a recommendation from an agent that did no research, cites no source, and has passed
  no critique and no test of risks.
- Lines 21-25: an answer "by a quotation from the approved definition, plan, current foundation or
  another task document". For a choice the human opened though a decision holds it, the decision
  itself is such a quotation, and the agent would answer the question with what the human has just
  reopened.

The first path reaches the human in the round package as an ordinary question, in place of the table
of the run or beside it. That goes against To do 3 and question 4, under which the run does the
research, the options with sources, the critique, the tests of risks and the table. It goes against
WAY-122 ("every option is offered only after a critique") and WAY-138. The second path closes what
question 7 opens. Decision 4 says only that the agent "marks" the question; a builder working from it
has no reason to touch `answering.md`, and the agent that follows that file never sees the spec.

What the builder has to know: `answering.md` joins the files the change touches, and says that a
question which requests a run gets only its canonical ID and affected tasks, with no answer and no
human question, since the run answers it. `conversation_template.md`, which holds the question's
fields, has to show such a question apart, in a way the agent can recognise. The alternative is to
keep the request a *Child-work request* and have the agent read those for the canonical mark. Either
way the spec has to name the change.

## Reaches beyond the handoff

- `project-level/lead/answering.md`, read whole: `spec.md:369-372` sends a new kind of question to
  the agent it instructs. It is the file of finding 10.

## Checks

Read-only review; no command ran. No file changed but this report.

## Searches not found or unclear

- Not checked: the GitHub page at `spec.md:431` was not opened. The review reached no host
  documentation.
- Unclear: `spec.md:108-109` still gives as the reason for always showing the candidate that "the
  cycle otherwise writes no decision of it", while `spec.md:151-154` now says that the return step may
  still write such a choice. It stands under *Cost if wrong* and sets no behaviour, so it is no finding.
