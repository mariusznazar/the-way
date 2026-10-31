# Designer's report — unsettled-technology-returns

**Status:** done

Spec: `.runs/task-cycles/unsettled-technology-returns/spec.md`, written from the handoff
`reports/designer-handoff.md`, under `task-cycle/spec/SKILL.md` and `design.md`, at base `2dbf1e7`.

## Questions sent and their answers

None. No batch went to the orchestrator: the handoff told me to settle the five choices, and every
way that would have changed the meaning of an approved decision beyond the task document had a way
that avoids it.

No WAY-30 question stands. The one design that would have raised one is named below, under choice 3:
teaching the plan-state reader to skip a returned cycle. The spec does not take it.

Three points the task does not settle and the spec picks, for the spec's reviewer to read first:

1. **Doubt leans to reserved** (spec, decision 3). The task accepts that the boundary rests on an
   agent's judgment (question 2) but gives no direction for doubt. Cost of the pick: a wrongly
   stopped cycle. Cost of the other way: a doubtful choice reaches Mariusz in the request with code
   on it, which is what the task removes.
2. **A new decision no row carries** (the third new decision, "How does a task leave a cycle that
   met a reserved choice, and how does it come back?"). Its rules bind after the merge, so WAY-36
   puts them in the log. The two carried questions gave rise to it. It changes no approved decision
   and rests on `foundation_step.md`'s "each entry a reviewed spec or the plan names".
3. **The boundary example of the icon source** (decision 3). The task's Context calls that case
   disputable and gives no verdict. The spec applies the rule of question 2 to it: it stays with the
   task unless it adds something to pay for.

## Ways weighed and why the rejected ones lost

Each way with its cost stands in the spec under its decision.

- **Choice 1, the place in the document.** Chosen: section *Technology* for the list and notes, three
  new fields under the settled question, the row from step 5 of `refine-task`. Lost: one section for
  everything (against question 1 and WAY-134); new table columns (a cell takes no line break); the
  step writing the row (the human would not see it in the candidate table); a committed comparison
  file (writes the choice into the repository before any work).
- **Choice 2, the request with no code.** Chosen: push the commit that adds the record, open the draft
  on it, then push the removal. Lost: the pair first (rests on a host accepting an empty diff, for
  which I found no host's documentation); the record left on the branch (breaks step 12's rule); no
  request (WAY-227).
- **Choice 3, the next cycle.** Chosen: same name, new branch, nothing changed in WAY-147 or steps 5
  and 12, and the project orchestrator moves the row on the human's word after removing the earlier
  trace. Lost: the reader skipping a returned cycle (changes the trust-boundary file
  `project-level/plan_state.py` and `project-plan-state-evidence`, and changes the meaning of WAY-153
  beyond the task, so WAY-30); `<name>-2` (breaks WAY-147, and the reader could never read the task
  as done); a separate directory for returned records (loses the trail to the request); reusing the
  branch (step 4 forbids it).
- **Choice 4, the shape of the rule.** Chosen: one rule file `project-level/technology/reserved_choices.md`,
  one cycle file `task-cycle/skill/reserved_return.md`, one run file
  `project-level/technology/task_run.md`, a new status `reserved`. Lost: `returned` with a field;
  `blocked` (wrong retry, keeps the work); the rule copied into each method; the rule in the decision
  alone; a second skill for tasks; inline branches in each step file; a blanket substitution
  sentence (a research agent never sees it).
- **Choice 5, the entries.** Three new decisions, one new glossary term and the six edits row 3 names.
  My search found no other entry the change makes untrue; the entries checked stand in the spec.

## Trust boundary

The design changes none of the part map's trust-boundary files. `project-level/plan_state.py` was
read, not changed. The cycle record's note that the spec may reach it does not come true.

## The four checks

1. **Placeholder, `TBD`, empty section:** none. A search for `TBD` gave 0, and each of the six
   sections is filled.
2. **Contradictions:** one found and fixed. Decision 3's discard named only the task's base; it now
   also names the commit that moved the pin, as decision 2 does. I also checked decision 1 against
   WAY-134: moving the row to step 5 removed a contradiction in my first design, where the step wrote
   the row while the section read `TODO`.
3. **Several independent changes:** yes in parts, and the task settles it: question 6 chose one task.
   The run at a task and the stopping rule could stand apart, and the spec keeps them together. The
   size is about twenty prose files, generated entry points and ten foundation entries; the route is
   the orchestrator's.
4. **A requirement readable two ways:** three fixed. Doubt on the rule leans to reserved. A choice
   settled in an accepted task document counts as settled, whether or not the step ran. The row comes
   from `refine-task`, not the step.

Two corrections came from checking the spec against the sources. The example "override of a transitive
dependency's version" went beyond the task's "nadpisanie `qs`" and now reads "an override of one
dependency". And `test_plan_state.py:297` already pins the conflict half of the planned test, so the
spec now asks only for the other half.

## Reaches beyond the dispatch

- `.runs/task-cycles/unsettled-technology-returns/cycle.md`: read by my mistake while reading the
  record's template. Only the orchestrator reads it (WAY-148). Nothing in the spec rests on it.
- `foundations/decisions.md`, WAY-142 (the states and the plan), WAY-257 (recognising the moment),
  WAY-19 (new number or edit), WAY-115 (candidates), WAY-116 and the text of WAY-172 and WAY-242 (the
  other blocked drafts), found by searching "blocked draft"; all for choices 3, 4 and 5.
- `foundations/glossary.md`, `open design choice`: a reserved choice meets its definition, which is
  why the check for one comes first.
- `foundations/invariants.md`, `skill-rule-source`, `project-plan-check`, `project-definition-form`,
  `project-readiness-gate`; `foundations/part_map.md`, project-level, task-cycle and the surfaces.
- `elements/decisions/template.md`, `elements/decisions/skill/projected.md`, `decide_entry.md`,
  `elements/common/skill/SKILL.md` (how a task's candidates are built), the section "How a skill asks":
  for how the cycle's writer reads a row.
- `task-cycle/review/SKILL.md`, `whole_change.md`, `task-cycle/spec/review.md`,
  `task-cycle/skill/spec_review.md`, `plan_member.md`, `planning.md`, and
  `project-level/task/skill/find_settlements.md`, `draft.md`: all needed for choices 1 and 4.
- `project-level/plan_check.py:396-403`, `project-level/test_plan_state.py:292-315`,
  `agent-instructions/skill_entry_points.py:111-128`, `installation/README.md`: to check claims the spec
  makes.
- The web, for choice 2 and choice 5: a search on requests with no changed files, and GitHub's page
  "Deleting and restoring branches in a pull request"
  (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/deleting-and-restoring-branches-in-a-pull-request),
  which gives "You can restore the head branch of a closed pull request." Read 2026-10-31.

## Searches not found or unclear

- No host's documentation found on whether a request with commits but no changed files can open, or
  whether one stays open when a later push empties its diff. The only source found is a remark in a
  third-party thread on Pagure (https://pagure.io/pagure/pull-request/5501) that GitHub and GitLab
  allow empty pull requests; I did not verify it. Decision 2's order avoids the first question; the
  second stays unverified, and the spec states the cost.
- GitLab's behaviour on a closed merge request's commits after its branch is deleted: not looked up
  beyond that search. Decision 5 states what is lost where a host does not keep them.
- `plan_state.py`'s behaviour was read and not run. The claim that a remote-tracking ref keeps the
  trace after the branch is deleted on the host rests on `plan_state.py:106-107` and `:115-118`; the
  test decision 5 asks for will show it.
- The task's Context gives no verdict on the icon-source case and does not say what the `qs` override
  was: see the points above.
- The handoff and the task cite `task-cycle/skill/SKILL.md` around 184-186 and 211-213; at base the
  sentences stand at 186-188 and 213-214. The handoff had warned of the shift.
- `project-level/lead/answering.md` was searched for "choice" and "technolog", not read whole. It
  showed nothing that lets the answering agent settle a reserved choice, and the spec does not change
  it.

# Revision after the spec's review

**Status:** done

The review `reports/spec-review.md` returned `FAIL` with nine findings. The handoff
`reports/designer-revision-handoff.md` answered findings 5, 6 and 8. All nine are revised in
`spec.md`. No question goes to the orchestrator: no finding needs a decision's meaning changed
beyond what the task carries (WAY-30). The three skill sentences of finding 2 apply what WAY-30 and
question 7 already say.

## What each finding changed

1. **A run for a choice outside the rule had no way in.** Decision 4, *Refinement*: `resolve_gaps.md`
   now runs the step in three cases, the rule deciding only the first; the others are a note the
   refinement started from, and the human asking during refinement. Step 0 says that the note passes
   to the run whatever the rule says of the choice. *Start*: a run refinement starts for a reserved
   choice takes that choice as its note. The list's note item reads "as it was given", since such a
   note is not the human's words.
2. **A held choice met three sentences that send it away.** Decision 1, new bullet: one exception
   each in `resolve_gaps.md:10-12`, `find_settlements.md:21-22` and `carry_foundation.md:13-15`, for
   exactly the decision the human opened. Any other collision, and a change of an approved
   definition, go as those sentences give. Both files joined the table in decision 3.
3. **A remark on a blocked request had no home.** Decision 2, new bullet: `correction.md` gains the
   case. The agent tells it apart by the record's field *Reserved choice*, which the record template
   now gives `none` or the choice. With no code nothing is corrected and the agent's report says what
   the request takes. With code, a changed remark that no longer needs the choice is an ordinary
   correction.
4. **`git fetch --prune` broke the same decision.** Decision 5 fixes the removal as four named steps
   in order, with `git branch -dr` on the one ref after the host's branch goes, and says why prune is
   not used. The item left this to the maker and is gone from *Left to the maker*.
5. **"Important by WAY-263" did not hold.** By the handoff's answer: `task-cycle/review/SKILL.md`
   grades it by the general grade of section 3, a missed requirement, with no citation of WAY-263.
   WAY-263 joined the entries searched and left unchanged.
6. **The rule on doubt.** By the handoff's answer: taken out of decision 3, of the orchestrator's
   step 1 and of the ways weighed. In its place stands that a choice is under the rule or is not, one
   an agent cannot place is no third kind, and the judgment rests on the examples. The dropped rule
   stands among the ways rejected, and the cost is named: a doubtful choice reaches the human in the
   request with code on it. My first report's point 1 no longer holds.
7. **A run at an accepted document left `ready for cycle`.** *Start* of `task_run.md` sets
   `Status: refining` before anything else changes, for any document not in its cycle. Decision 1's
   readiness bullet no longer says "keeps".
8. **No marker for a projected decision.** By the handoff's reading: decision 1 has a fourth marker,
   `— projected: <question>`. *List* says that no run reopens such a choice and that a human who
   wants it changed goes the way `resolve_gaps.md:10-12` and WAY-118 give. `project_plan_task.md` and
   the first new decision's meaning carry it; that meaning names To do 6 as its source, since row 1
   does not say it.
9. **One choice in two members of a round.** Decision 4, new bullet: the refiner's request for a run
   is a question of its turn, so the answering agent marks one canonical question. One run stands at
   the document of the affected task with the lowest number, its report's head names every affected
   document, and the other refiner copies the settled question whole. The template's sentence on a
   canonical answer extends to the three new fields. Each member keeps its row, and the second cycle
   ties its row to the first's entry (WAY-134).

The review's items under *Searches not found or unclear*:

- The GitHub sentence now carries its address and the date read.
- The worktree: step 1 of the removal covers a cycle that ran in a checkout that stays.
- A row the human strikes: *Cost if wrong* of decision 1 now says that the return step cannot see the
  cut and may still write the choice. It sets no new behaviour.
- The claim that no host's documentation accepts a request with no net diff stays as it was: it rests
  on the search reported above.

## The four checks, again

1. **Placeholder, `TBD`, empty section:** none. A search for `TBD` gave nothing.
2. **Contradictions:** a search for "doubt" leaves only the rejected way and the cost, and a search
   for `fetch --prune` only the reason it is not used. One found in revising and fixed: a record older
   than this change has no field *Reserved choice*, so `correction.md` reads a missing field as
   `none`. Decision 1's opening said that nothing else moves in the template, which the canonical
   sentence made untrue; it now says that the existing sections stay.
3. **Several independent changes:** as before; question 6 keeps them together. The revision adds
   `carry_foundation.md` to the files the change touches.
4. **A requirement readable two ways:** the choice under the rule is now read one way, by finding 6.
   The stage at which the status moves is now read one way, by finding 7.

## Reaches beyond the handoff in this revision

- `project-level/task/skill/carry_foundation.md:12-15`, `task-cycle/skill/correction.md:15-17` and
  `project-level/lead/conversation_template.md:37-42`: to check the lines the review cites. All read
  as it says.

## Searches not found or unclear in this revision

- A later task's choice that an earlier, unmerged task already settled, outside one round: finding 9
  covers one round only, and the spec gives no form for two rounds. A second run would research it
  again and the human would see it again. The cost is one repeated run; nothing is written twice,
  since WAY-134 ties the second row.
- A plan row reading `ready for cycle` whose document a run set to `refining` outside a round: the
  spec leaves it to the next reconciliation, as `draft.md` already leaves an accepted document
  refined again. `implement-task` step 1 reads the document's status, so no cycle takes it.
