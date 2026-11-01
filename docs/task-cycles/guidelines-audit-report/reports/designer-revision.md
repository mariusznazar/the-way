# Designer's report of the revision — guidelines-audit-report

Status: done
Spec: `.runs/task-cycles/guidelines-audit-report/spec.md`
Review answered: `.runs/task-cycles/guidelines-audit-report/reports/spec-review.md`

The task's *To do*, answers and rows stand as they were. No tracked file changed and no commit was
made (`git status --short` empty).

## The three findings

### 1. A cause the check withdraws, or lowers out of the top, leaves no record

- Decision 8: `Checked:` now stands on every cause the check went back to, the top and a cause lowered
  out of it, and says the weight the cause had. A withdrawn cause leaves the order and stays in the
  list as a `Withdrawn:` item after the last cause, with the cause, the weight it had and its
  `Checked:`. A cause the author's verdict on the critique withdraws takes the same form. The critic
  reads them in the list, and the human hears one line at step 4, with where they stand.
- Followed in decision 10 (the check of `hand_back.md`), decision 13 (the shared text) and entry F
  (the record covers a cause the check lowers or withdraws).
- Rejected and recorded: a withdrawn cause with no line, and `Checked:` on the top alone.

### 2. The last audit lowers and withdraws the other discipline's causes

- **Who:** decision 6. Item 1 now says each skill gives a cause its first weight. Item 3 says that from
  there the causes are the list's, and the audit that runs last lowers or withdraws a cause of either
  discipline, in the form of the discipline that found it (decision 13).
- **`narrows WAY-247`: no, and C says so.** What WAY-247 leaves to a skill is what its discipline's
  guidelines carry, as its violating example shows, and all of that is settled at the skill's own
  step 4, which the end never changes. A weight is no meaning of the guidelines and binds only the
  skill (WAY-173). Entry C now states the area plainly: the last audit may lower or withdraw a cause
  of either discipline and changes nothing the human settled for a discipline. The cost if this
  reading is refused is named in decision 6: C gains `narrows WAY-247` and a sentence of its area.
- **A status already settled:** decision 6 and decision 12. It stays as the human settled it, and
  goes back to the human with the top, as one question for each, keep or change, with what the check
  saw. The answer stands under the question that settled it, with its own source, so
  `coding/hand_back.md:11` stays true. Decision 10's check asks for that answer. A `do not copy` still
  a proposal goes with its withdrawn cause, as before.

### 3. A boundary with no test on purpose

Decision 11: a boundary that is only the configuration of someone else's service has no test due, so
the audit says so beside it and it is no cause. The cause is kept for every boundary a test is due at
under WAY-235. Decision 5's *Takes* and entry B follow, and *Foundation entries* records that row 2
stays whole for those boundaries, since its sources do not speak of the other kind, so no question
under `foundation_step.md` arises.

## The matters left to the maker

The handoff says two and names one. The review's *Searches* leave three open that a sentence settles,
so all three are settled:

1. **The condition of decision 6, item 2** is worded by the audit that runs: an audit stops after
   weighing where the other skill's step 1, run before this audit ends, gives that skill the audit in
   this task and it has not yet run. The route of one kind and a new level count as no audit.
2. **How the two skills follow each other,** on which decision 6 rests: an audit that stopped hands
   back to `refine-task` step 3, for the other skill, and only the skill of the audit that runs last
   hands back to step 4. This reaches only the joint task with two audits; the wider gap, a joint task
   with fewer, stays as it is today.
3. **Who writes the backlog:** decision 10 now says the write is `refine-task`'s and comes with the
   hand-back, so the skill's table of what it never writes stays true where git tracks the backlog.

## The four checks

1. Placeholder, `TBD` or empty section: none (`TODO|TBD` counted 0 in the spec).
2. Contradictions: none left. Read again after the edits: decisions 6, 8, 10, 12, 13, entries B, C and
   F, and "nothing narrows" in decision 4 agree. A `Withdrawn:` item stands outside the check that
   every cause reads `Taken:` or `Deferred:`, and the check names it apart.
3. Several independent changes: no; the same 19 files.
4. Two readings: "a test is due at" is tied to WAY-235; "the audit that runs" to each skill's step 1.

## Reaches beyond the dispatch

- `product-guidelines/testing/template.md:186-192`, to confirm the exception the review cites.
- `task-cycle/spec/design.md` and the spec's own earlier reads, as before.

## Searches not found or unclear

- The handoff says "two matters" and names one, the condition of decision 6, item 2. I could not tell
  which the second is, so I took both candidates; see above.
- WAY-48 itself was not read in this revision: the exception stands in WAY-235's binding sentences and
  in `testing/settle.md:35-36`, which were read.
- Whether a weight is a discipline's matter under WAY-247 is a reading: the decision's text does not
  define "that discipline's matters", and only its example points to what the guidelines carry.
- `elements/glossary/template.md:50-51` and naming the course in entry A's *Rationale* stand as the
  first report and the review left them.
