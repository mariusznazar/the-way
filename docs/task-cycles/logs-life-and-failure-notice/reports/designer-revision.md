# Report — revision of the spec by its designer

Status: done

Spec: `.runs/task-cycles/logs-life-and-failure-notice/spec.md`, revised in place.
Review answered: `.runs/task-cycles/logs-life-and-failure-notice/reports/spec-review.md`.

## What changed for each finding

**Finding 1, D6 step 2 against row 4 (orchestrator's ruling: keep step 2).**

- D6's "Two readings picked" is now "Three readings picked". The new first reading names step 2 as a
  reading of row 4, with the ruling's reason: row 4 guards against filling an item in without the
  human's choice, the choice here stands in the entry, the human reads the quote on accepting the
  document and can still ask for a run, and asking would offer a run that cannot reopen a projected
  decision of an approved definition (WAY-267).
- D6 step 3: the question now asks about what the skill does not say and no decision and no approved
  definition answers.
- *Foundation entries*, WAY-139: its meaning carries the exception, so the entry, row 4 as read here
  and D6 say one thing.
- *Goals*: the line on the deployment list says the same, and points to D6.
- D6's *Cost if wrong* now prices three readings.

**Finding 2, the condition of step 1 narrower than the criterion.**

- D4 now gives one condition, in the same words in `SKILL.md` step 1, the `list.md` bullet and
  `failure_notice.md`: it holds unless the definition, or a decision of the foundation, keeps the
  product on the machine on which it is made. It is true for a silent definition and reads what the
  definition and the foundation say, with no marker in it.
- D4 gives why: the look comes before any marker in `list.md`, the first project is the case To do 3
  exists for, and a run takes no second look after a wave.
- D2 points both places to that condition.
- *Foundation entries*, the new decision: its meaning and *Verification* carry the same condition,
  with a silent definition as an example.
- I added "or a decision of the foundation" to the review's example wording: a product whose foundation
  already keeps it local would otherwise take the item on each silent definition until answered.

**Finding 3, no place for the rewrite.**

- D1 gains "Writing the result over the nested entry": the rule stands in `settle.md` sub-step 7. A
  nested entry goes to `record-decision` as the entry the result rewrites; a projected decision is
  replaced under its heading, with its meaning sentence; a decision of the foundation is projected as
  its change, `#### <PREFIX>-<NN> — <question>`. The nested line goes when the item ends `— projected`.
- *Files*: the row of `settle.md` now names sub-steps 1 and 7.
- No file of `elements/decisions/` or `elements/common/` changes, and the closing line of *Files* says
  so. The forms of both headings already stand there, an entry going through projected mode again has
  a precedent at step 7 of `define-project`, and what was missing is only who names the entry, which
  is the hand-over's. So the route need not be judged anew on this ground.
- `task_run.md` replaces sub-step 7 with its own *Write*, so it gains nothing here.

**From the review's *Searches*, not a finding:** WAY-139's *Relations* now name `derives from` for both
entries.

## The four checks

1. Placeholder, `TBD` or empty section: none.
2. Contradiction: none found. I checked the condition across D1's table, D2, D4 and the new decision's
   meaning, and D6's steps and readings against WAY-139's meaning and *Goals*. The list of unchanged
   files agrees with the *Files* table.
3. Several independent changes: no, as before.
4. Requirements readable two ways: the two the review found are settled here. One reading to note: D4's
   condition makes a silent definition meet row 3's criterion, which the spec already held and now
   states as the one condition.

## Reaches

- `elements/decisions/skill/SKILL.md`, lines 40–56: the two headings of a projected decision.
- `elements/decisions/skill/decide_entry.md`, whole: that it searches the log, as the review says.
- `project-level/definition_template.md`, search for the headings: line 309 gives both forms.
- `project-level/readiness_check.py:67`: that a heading `#### <PREFIX>-<NN> — <question>` gives its
  question to condition g, so an item of a projected change passes.

## Searches not found or unclear

- **A rule in `elements/` that says a projected entry is replaced:** not found, which the review also
  says. The rule now comes from the hand-over in `settle.md` sub-step 7; an agent following only
  `record-decision`, with no such hand-over, still has none. That is the existing state and this change
  does not need more.
- **Whether a yes to row 3's criterion for a silent definition overreaches the row:** unclear in the
  row's words. Both the review and the handoff ask for that outcome, so it stands, named in D4.
