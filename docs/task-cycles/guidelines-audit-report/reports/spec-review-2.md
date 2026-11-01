PASS

# Review of the revised spec — guidelines-audit-report

Reviewed: the revised `.runs/task-cycles/guidelines-audit-report/spec.md`, read whole, with
`reports/designer-revision.md`, against the frozen `task.md`, base `2f51e6c`, and the first review
`reports/spec-review.md`. No new finding. All three earlier findings are resolved, and the three
further matters and the reading of WAY-247 hold.

## The earlier findings

### 1. A cause the check withdraws, or lowers out of the top, leaves no record — resolved

- `Checked:` now stands on every cause the check went back to, and a cause lowered out of the top
  keeps it, with the weight it had (`spec.md:318-320`).
- A withdrawn cause leaves the order and stays in the list as a `Withdrawn:` item with the weight it
  had and its `Checked:` (`spec.md:329-335`), so the critic reads what the author dropped.
- The change reaches every place that needs it: the table of decision 8 (`spec.md:297`), the check of
  `hand_back.md` (`spec.md:394-399`), decision 13 (`spec.md:449-453`) and entry F (`spec.md:490`).
  To do 5 and row 6 are met.

### 2. The last audit lowers and withdraws the other discipline's causes — resolved

- The contradiction is gone. Item 1 now gives each skill a cause's first weight (`spec.md:218`), and
  item 3 says who lowers or withdraws, in the form of the cause's discipline (`spec.md:226-229`,
  `453`).
- A settled status stays as the human settled it and goes back to the human with the top
  (`spec.md:236-241`). Decisions 10 and 12 agree (`spec.md:397`, `439-441`), and
  `coding/hand_back.md:11` stays true.
- See "The reading of WAY-247" below for whether C needs `narrows`.

### 3. A boundary with no test on purpose becomes a cause — resolved

- Decision 11 keeps the cause for a boundary a test is due at under WAY-235 and says a boundary that
  is only the configuration of someone else's service is no cause (`spec.md:416-422`). Decision 5
  and entry B follow (`spec.md:180-181`, `486`).
- Does this change row 2, which the handoff forbids? No. WAY-235 frames the test of refusal as due at
  every boundary but that kind, To do 2 pairs a cause with "jedna naprawa", which that boundary
  cannot have, and question 5 speaks of the risk of a missing test, and none is missing there. So the
  row keeps its meaning, and `foundation_step.md` raises no question. Entry B says the limit in its
  sentence, so the human sees it at the merge.

## The reading of WAY-247

The designer holds that a weight is no discipline's matter under WAY-247, so C names no `narrows`.
The reading holds:

- WAY-247's two examples and its rationale are all about what a discipline's guidelines come to
  carry. A cause's weight is not carried there: which causes a task takes ends with the task
  (`spec.md:302`, WAY-36).
- WAY-25 asks for `narrows` where two decisions both apply and collide. With the settled answers left
  to the human, nothing a skill settles for its discipline is moved by the end.
- The refusal has a named cost (`spec.md:262-263`), and it is small.

One thin place, no finding: where a settled status goes back to the human, the skill of the other
discipline puts the question. The human answers and that skill settles nothing, so the reading's "the
end never changes it" holds, and a builder has nothing to guess.

## The three further matters

The handoff named one matter and counted two; the designer settled three. None goes beyond the task:
each is what decision 6 or decision 10, both within the open choices, needs in order to work.

1. **The condition of an audit that stops** (`spec.md:219-222`). It reads by the audit that runs,
   which closes the case of the first review's *Searches*. It rests on the skills of a task joining
   code and tests, as the lead sentence of decision 6 sets, so a styleguide audit and a task carrying
   one discipline end as any other. The agent running the other skill's step 1 is a small new step,
   and the only way the first audit can know. Holds.
2. **How the two skills follow each other** (`spec.md:223-225`, `399`). Needed: without it the first
   hand-back would reach step 4 and the second audit would never run. It reaches only a joint task
   with two audits, so it does not change `refine-task`'s work elsewhere. Holds.
3. **Who writes the backlog** (`spec.md:382-384`). To do 7 gives the route, and WAY-215 gives
   `refine-task` the write. "Before handing back" and "comes with the hand-back" describe one moment
   in one session; a builder gets the same result from either. Holds.

## What the revision broke besides

Nothing. Read again for it: decisions 4, 6, 7, 8, 9, 10, 12, 13, entries B, C and F, the check of
`hand_back.md`, and how a `Withdrawn:` item meets the rule of the top, the `do not copy` mark and an
audit whose causes are all withdrawn.

## Reaches beyond the dispatch

- `project-level/task/skill/resolve_gaps.md`, whole, to see what handing back to `refine-task` step 3
  meets.
- A search of `project-level/task`, `project-level/lead` and the `hand_back.md` files for what they
  say of handing back, and of `product-guidelines` and `project-level` for where `recognize.md` and the
  discipline skills are named.

## Searches not found or unclear

- **`refine-task` step 3 names no discipline skill.** `resolve_gaps.md` does not start one; a
  discipline's `SKILL.md` says it takes over there. So the hand-back to step 3 works only by what
  `hand_back.md` itself says of the other skill. Decision 6 words it so, and the maker has to write
  it there, and correct "hands back to its step 4" at `coding/SKILL.md:31` and `testing/SKILL.md:30`,
  both among the files to change.
- **The other skill's `recognize.md`.** Item 2 has a session read a file of the other skill, which
  decision 5 does not list. Read as covered by the constraint on WAY-256 and WAY-265
  (`spec.md:54-55`): coding's and testing's step 3 name it, with its condition.
- **A joint task with fewer than two audits.** Who starts the other skill stays as unsaid as it is
  today, as the designer says. The revision does not worsen it.
- **An audit stopped, then the other audit dropped** because the human separates the work. No
  skill then ends the list and nothing in `final_review.md` would notice. Not reported: the case is
  rare, the earlier spec had it too, and the human sees the document whole at acceptance.
- **Naming the course in entry A's *Rationale*** and **`elements/glossary/template.md:50-51`** stand
  as the first review left them.
