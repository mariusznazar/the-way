FAIL

# Spec review 2 — pr-description-schema (revised spec)

Reviewed: the revised `docs/task-cycles/pr-description-schema/spec.md` against the earlier review
(`reports/spec-review.md`), the designer's revision report (`reports/designer-revision.md`), the
frozen task and the foundation entries the review handoff names.

## The earlier findings

1. **WAY-114's new meaning dropped how an entry is shown: resolved.** `spec.md:670-686` keeps the
   gate clause unchanged ("shown as one sentence in the human's language with the entry beside
   it"), adds the row case, and at the merge gives the plain sentence with no identifier in the
   decision section and the block, with the entry by its identifier in the lower part's list. This
   matches row 1 and the task's answer that the change concerns the decision section only.
2. **Restatements of WAY-10 and WAY-114 outside the foundation were missing: resolved.** D2's second
   table (`spec.md:216-232`) names `task-cycle/skill/SKILL.md:204-205`,
   `elements/common/way_of_working.md:134-136`, `elements/glossary/template.md:48-49`,
   `elements/decisions/template.md:131` and `elements/common/critique/SKILL.md:20-22`, each with
   what it becomes. It names the gate files as holding, which is right now that the gate clause
   stays. D9 points to the table (`spec.md:592-593`).
3. **The blocked routes could not fill the record's *Description*: resolved.** D3
   (`spec.md:260-280`) gives what the committed copy holds on step 12, on the record-first routes
   and after a correction, with a fixed wording where the check runs after the commit. D4's "Where
   the cycle runs it" (`spec.md:367-375`) says the same.
4. **No route for a form error the orchestrator holds wrong: resolved as a route, but the revision
   puts it into the foundation in a way the foundation forbids.** See new finding A. The route
   itself (`spec.md:383-404`, D7 `:544`) ends the loop and keeps the block. It never writes `none`
   or English to silence a language error, and it puts the case before the human.

The earlier unclear search (a plan's position as `--task`) is settled in D4 and D8. See new
finding B for what that settlement measures.

## What the revision broke

### A. The exception is written into row 6's entry, which changes a row's meaning

`spec.md:652-663`, the row-6 decision: "An error the orchestrator holds wrong, with its evidence, is
the exception, foreseen in the binding sentences … the request opens as a draft that names the
error … This exception is the cycle's design, not the row's words. It goes in this task's own
request as a choice beyond the task (D5)."

Row 6 of *Settlements to record* reads "Cykl przed otwarciem PR-a uruchamia skrypt sprawdzający
formę opisu i poprawia opis, dopóki skrypt zgłasza błędy" — it corrects while the script reports
errors, with no exception. WAY-134 (`foundations/decisions.md:3213-3218`) has the cycle write each
kept row whole, "keeping its meaning". Where the meaning cannot hold, the cycle asks the human
rather than write another entry. Its *Verification* names "the cycle writes the entry with another
meaning" as a breach. `task-cycle/skill/foundation_step.md:25-27` says "The writer never writes a
row with another meaning". An entry that lets the request open while the script still reports an
error narrows the row's meaning. The spec admits the exception is "not the row's words".

It also collides with the spec's own D5 item 6 (`spec.md:475-483`) and the new WAY-114, which keep
entries written from rows out of the decision section as already accepted. Marking the same entry
as a "choice beyond the task" under item 5 shows it to the human after all, but as a mixed entry
that is part row and part cycle.

The builder, and the foundation step that words the entry, would write an entry that the review
of the whole change has to flag against WAY-134. The rules allow a clean form: write row 6 whole as
the row says it. Put the exception in a decision of its own, written from the spec. It answers a new
question (WAY-19), such as "What does the cycle do with a form error it holds wrong?", and its
*Relations* read `narrows` the row-6 decision. As an entry the cycle wrote, it stands in *For you to
decide* under D5 item 6. The other permitted way is to ask the human. The spec should choose one.

### B. The plan case measures English markers the spec says are excluded or in the definition's language

D4 unit 3 (`spec.md:321-324`) measures a TASK with neither `### Need` nor `### To do`, such as a
plan, "on all of its text other than headings, table header rows and table separators". It says
"The plan template keeps those in English and the rest in the definition's language
(`project-level/plan/template.md:18-23`)". The cited lines say more: "The headings, the header
lines, the column headings, the states and the markers below are in English, whatever that
language" (`project-level/plan/template.md:22-23`). Its form adds English text outside headings and
header rows:

- the `Status:` and `Definition:` lines;
- the states (`to refine`, `yes`/`no`);
- entry identifiers and slugs;
- `none` under *Phases*;
- change-log lines ("written from the definition at fingerprint").

The measure the spec gives counts all of these toward English function words ("from", "the", "at",
"over"). A Polish plan with short *Goal* cells can then read as English. The held-wrong route of
D4 keeps the block from being lost, but every such request would open as a `draft` with a false
error. Since the spec's claim about the source is wrong, the builder either follows the measure as
written or guesses at a different one. The spec should name what is measured in a plan, for example
only the *Goal* cells and the text of *Open questions*, or what is stripped: the header lines,
the State, Preparatory, Depends on and Document columns, the markers and the change log.

## Reaches beyond the handoff

- `project-level/plan/template.md:1-80`: the passage the revision cites for the plan case
  (finding B).
- `task-cycle/skill/foundation_step.md:7-27` and WAY-134's binding sentences and *Verification*
  (`foundations/decisions.md:3201-3245`), read again for finding A.
- `elements/decisions/template.md:123-135` ("Changing a decision", WAY-19's new question rule),
  for the form finding A proposes.

## Searches not found or unclear

- Whether the-way has, or expects, changes that carry out a plan's position, so whether finding B
  would show in practice: no such change was looked for in the history. The finding rests on the
  spec's own statement of the measure.
- The designer's open point on `task-cycle/skill/SKILL.md:193-197`, the route of a blocked draft
  for a question from the foundation step, was not judged. The revision did not change it.
