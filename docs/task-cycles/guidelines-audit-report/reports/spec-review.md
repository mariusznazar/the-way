FAIL

# Review of the spec — guidelines-audit-report

Reviewed: `.runs/task-cycles/guidelines-audit-report/spec.md`, against the frozen `task.md`, base
`2f51e6c`. Three findings. Each one needs a sentence or two of the spec, not a new design.

## Findings

### 1. A cause the check withdraws, or lowers out of the top, leaves no record of the check (requirement changed; contradiction within the spec)

- To do 5 and row 6: "to, co się nie potwierdzi, obniża albo wycofuje, a przy każdej sprawdzonej
  przyczynie zapisuje, że ją sprawdził". The spec's own entry F keeps it: "each check is recorded"
  (`spec.md:443`).
- Decision 8: "A cause the agent withdraws leaves the list with no line" (`spec.md:305`), and
  `Checked:` is "Only for the top" (`spec.md:295-296`).
- So a cause the check changed most leaves no trace. A withdrawn cause has no line. A cause lowered
  below the top has a line with no mark, which `hand_back.md` does not ask for (`spec.md:358-361`).
- Why it changes the build: the record is written only where the check confirmed the cause. The
  critic reads the full list "so a critic can see a heavier cause standing too low"
  (`spec.md:260-261`), but sees nothing of a heavy cause its author withdrew. That is the very case
  question 6 names as the weak point: the author checks its own conclusion, and independence comes
  only from the critique.
- To settle: where a withdrawn cause's check stands (for example a line of its own, with what was
  gone back to and what was seen, which the human and the critic can read), and that `Checked:`
  stays on a cause the check moved out of the top. Decision 13 and the last check of `audit_end.md`
  follow from that.

### 2. In a joint task the audit that runs last lowers and withdraws the other discipline's causes, which decision 6 calls that discipline's matter (contradiction within the spec and with WAY-247; a guess that matters)

This is the first reading the designer asks to have looked at.

- Decision 6, item 1: "Each skill finds and weighs its own causes, the discipline's matter WAY-247
  leaves to it" (`spec.md:218`). Item 3: the audit that runs last "merges both audits' causes,
  orders them, goes back to check the top" (`spec.md:222-223`). Going back lowers or withdraws
  (To do 5, `spec.md:405`), and that is weighing the other discipline's cause.
- The closing claim "WAY-247 is not narrowed" (`spec.md:230-231`) holds for the merging, the order
  and the top: those are the task's, and that reading stands. It does not hold for the check as the
  spec words it. If lowering stays a discipline's matter, C and WAY-247 collide, and WAY-25 asks for
  `narrows WAY-247` with its area in C's sentences. If it is the end's matter, item 1 has to say so.
- Consequence the spec leaves open: the audit that runs first has already passed its step 4
  (`spec.md:221`), and that step settles with the human "the status of each of its files"
  (`coding/settle.md:26-27`, `coding/task_document.md:34`). Then the testing skill, running last,
  withdraws a coding cause, and decision 12 says the cause "takes that `do not copy` with it"
  (`spec.md:396-397`). That undoes an answer the human gave, in another skill's session, with no
  route. The check of `hand_back.md` does not see it, and "no choice stands settled without the
  human's words" (`coding/hand_back.md:11`) stops being true of that status.
- To settle: who may lower or withdraw a cause of the other discipline, and whether C names
  `narrows WAY-247`; and what happens to a status the first audit already settled when the last
  audit withdraws its cause. For example, the status stands and goes back to the human with the top.

### 3. A boundary with no test on purpose becomes a cause (contradiction with WAY-235; a guess that matters)

- Decision 11: "a boundary with none is also a cause, its place the boundary's name"
  (`spec.md:378-379`), with no exception.
- WAY-235: "a boundary that is only the configuration of someone else's service stays with the
  review of WAY-48", and its rationale says such a test "would have its test check someone else's
  code". `testing/settle.md:35-36` and `testing/template.md:189` carry the same exception.
- So for that boundary a missing test is the settled state, not a flaw. It gets no invariant, so
  the rule "A boundary's cause whose fix is the test its accepted invariant brings stands `Taken:`"
  (`spec.md:382-383`) cannot reach it, it has no fix for `Fix:`, and "one fix removes" it is false.
  Still it must stand `Taken:` or `Deferred:` (`spec.md:359`). Weighed by its stake, a login
  boundary can reach the top, take the place of a real cause, and if `grave` draw the backlog
  question for a test the foundation says not to write.
- To do 2 and question 5 do not speak of this boundary. The audit today only says whether a test
  exists, so nothing forced the question until the boundary became a cause.
- To settle: whether a boundary left to the review under WAY-235 is outside the list, which keeps
  To do 2 for every boundary a test is due at. The maker cannot tell from the spec, and the answer
  changes `testing/audit.md` and the shared file.

## The designer's other readings

- Decision 9, the rule of the top: within To do 6. Traced for no, four, five and six `grave` causes
  and for fewer than three causes; each stays in what the task allows and reaches the same top.
- Decision 8, the list in *Context*, a *To do* item naming a cause by number: no finding. To do 6
  places the list "niżej w dokumencie", today's three `task_document.md` already send an audit's
  results to *Context*, and the task's document stays one whole for the cycle's author.

## Reaches beyond the dispatch

- WAY-48, `foundations/decisions.md:1119-1147`, for what a trust boundary is, for finding 3.
- WAY-95 and WAY-99, `foundations/decisions.md:2012-2039` and `2091-2116`, to judge decision 3 on
  `finding` and `cause`.
- The glossary's `debt` entry, `foundations/glossary.md:31-35`, and all its headings, for the claim
  that no entry names a grade or a finding.
- `elements/common/way_of_working.md:1-55`, for "How a skill asks", cited at `spec.md:281`.
- `product-guidelines/coding/template.md:180-191`, cited at `spec.md:137`.
- `project-level/task/skill/read_sources.md` and `final_review.md`, and `project-level/lead/skill/SKILL.md:150-219`
  with the hits of `plan change` under `project-level/`, for decision 10's route.
- The author's rule on searches, `C:\Storage\The Brain\The Brain\.ai\rules\search.md`, required by
  his global instructions before a claim of absence. It holds method and nothing of the task.

## Searches not found or unclear

- **Retired word and limit.** A first search over the repository, with a filter excluding `.runs/`,
  returned nothing, because the worktree itself lies under `.runs/`. Repeated with `git grep`:
  the eight lines of decision 3 and the two ordinary hits at `foundations/decisions.md:3401` and
  `7327` are as the spec says. WAY-250's "three to five" wraps across two lines, so the search for
  the limit misses it; it was read in place.
- **No test reads these files.** `git grep` over `*.py` for `product-guidelines` gives six lines in
  four files, each the path of a `SKILL.md`, as decision 14 says. Positive control: those hits.
- **Glossary.** No entry for `finding`, `cause`, `weight`, a grade or a blocking finding, from the
  list of headings read whole.
- **How two skills of one joint task follow each other.** Neither WAY-247 nor any `SKILL.md` says;
  each `hand_back.md` hands back to `refine-task` step 4, and nothing says who then starts the other
  skill. The gap stands today and is no finding of this spec, but decision 6 rests on it.
- **Joint task where the other discipline runs no audit.** Decision 6, item 2 reads "the product has
  what the other audit reads", which the route of one kind or a new level also meets. Read as
  settled by "A task with one audit to run ends as any other" (`spec.md:227`), so not reported; the
  maker has to word the condition by the audit that runs, not by what the product has.
- **Who writes the backlog.** Decision 10 says the skill writes no backlog and has the session add
  the task at the skill's step 5, by a file of `refine-task`. In coding and testing the table says
  the skill writes no other tracked file. Outcome unaffected, so not reported; it reads oddly only
  where a product's backlog is tracked.
- **Naming the course in entry A's *Rationale*.** WAY-27's verification speaks of *Origin* and of a
  rationale that rests on what is not said. The row names the course and the spec describes the
  pattern, so it was read as compliant. The designer reports the same doubt.
- **`elements/glossary/template.md:50-51`** holds a `TODO` on when two uses carry two meanings;
  decision 3 uses the sentence as it stands, and so did this review.
