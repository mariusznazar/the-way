# Designer's report — logging-guidelines

Status: `done`
Spec: `.runs/task-cycles/logging-guidelines/spec.md`
Base: `foundations` `ea4694e`. No tracked file changed; no commit made; the only two files written are
the spec and this report.

## Result

The product's decision on the new rules is one entry of its own. The coding template gains six
required rules after the standing checks, the sixth being `### Logging scope`, which holds the list.
"Przepływ" becomes `case flow` and "część" becomes `the rules on failures and logs`; neither takes a
glossary entry. Rows 1–8 become eight decisions, with a ninth from the spec, numbered from WAY-271.

## Questions sent and their answers

None. The handoff gave the three choices to this spec and every other point could be settled from
the task, the foundation or the smallest reading. Each reading picked is named below, and none is a
reserved choice: the library that writes a line stays with a product's human.

## Ways weighed

| Choice | Chosen | Rejected, and why |
|---|---|---|
| The product's decision | one entry of its own, at most three binding sentences | part of the decision adopting the template: adoption plus four items do not fit three sentences, a product adding the rules edits an old decision, and a generally worded adopting decision could pull rules in at a later pin. Several entries: the task speaks of one decision, and a departure would have to drop each |
| A departure from one rule | the same entry, with the reason in *Rationale* | a second entry with `narrows`: more for one question (WAY-19) |
| "Przepływ" | `case flow` | bare `flow`: keeps the meaning of critical flow in a foundation (WAY-104, WAY-45); `request flow`: drops a background job; `operation`: no sense of end to end; `trace`: a record and a tool; bare `case`: an entry would cost every product a qualifier |
| "Część" | `the rules on failures and logs` | `part`: the map's; `section`: a `##` heading's; `set`: a linter's in the same file |
| The rule of scope | a sixth rule | merging identifiers and events: against question 8; a list in each rule: two places, and no single rule as To do 3 names; a `##` section: against question 12 |
| Place in the form | after `### Dependency audit`, before further rules | after further rules: an open-ended placeholder has no end |
| Departure from all the rules | each of the six headings holds `none —` | one collapsed heading: an exception to WAY-171 for six saved lines |
| Readiness | not ready without the decision, carried by a new entry, not by WAY-202 | ready without it: the "optional" way question 2 turned down; a change of WAY-202: these are no standing check |
| Library research | none, as today's route for a library | added to `research.md`: research runs at step 2, before the form that shows the need is chosen at step 4, and the task does not ask for it |
| A library under the test | `derives from WAY-268` | `narrows WAY-268`: the reserved limb is tested first, so nothing is gone against |
| The file where a program starts | stays as the task says | widening the audit: changes WAY-200 and WAY-201, which no row carries |

Beyond the handoff's words, the spec also fixes `logs` over bare `the log`, because in these templates
`the log` is the decision log, and `item` over `entry`, a glossary term.

## The four checks

1. Placeholders, `TBD`, empty sections: none.
2. Contradictions: three corrected on rereading. The Constraints line cited "Rule 3 of To do 1" where
   To do 1 as a whole was meant. E9's readiness left out the refresh D5 includes. D6 claimed that no
   cycle could pick a library only by way of the form of a line, which did not cover a cycle that
   keeps the form; it now rests on the example row and the blocked draft request.
3. Several independent changes: no. To do 5 could stand alone, but the task holds it with the rest and
   the rules make its need concrete; one change.
4. Two readings: picked in D9 (the last-resort line; "each separately running program"), and in D6
   (WAY-268) and the *Rejected* of E7.

## Reaches beyond the dispatch

- `product-guidelines/testing/settle.md`, `product-guidelines/testing/task_document.md`: how a sister
  skill words adoption and departure.
- WAY-19, WAY-99, WAY-104, WAY-199, WAY-200, and the first half of WAY-267: the numbering rule, the
  bare-word rule that decides D2, and what D8 and D6 rest on. WAY-104 was the deciding reach.
- `elements/glossary/template.md`, read whole for the test the handoff names by directory.
- `elements/common/way_of_working.md`, section "How a skill asks"; `.runs/.../cycle.md`, for the
  orchestrator's reading of the open choice.
- Searches of tests, `README.md`, `installation/README.md`, `elements/common/foundation_check.py` and
  the rest of `foundations/`; a run of `python -B elements/common/foundation_check.py .`, 0 errors.
- `foundations/glossary.md`, `foundations/part_map.md` and `foundations/invariants.md` were read whole,
  not by the entries named: `task-cycle/spec/SKILL.md` says never a whole file of the foundation.
  They are short; the departure changed nothing in the result. `foundations/decisions.md` was read by
  ranges.

No note of the author and no repository of any product was read, apart from the task document.

## Searches not found or unclear

- The handoff says rows 2 and 3 name the step of technology. Neither row does in the frozen task. I
  read this as question 5's source and the Context's line on where logs go, and checked agreement with
  WAY-165, WAY-268 and WAY-270 on that reading. No correction is needed; WAY-270's "two questions …
  nowhere else" stays true, since row 3 takes a different thing from the same lesson.
- To do 1 says a last-resort line carries no identifiers; row 2 says it may carry none. Read as row 2
  (D9).
- WAY-268's "the tools the skills of guidelines choose stay on those skills' routes" does not say
  whether such a tool is tested for reservation first. Row 7 needs that it is, and the spec reads it so.
  If the reviewer reads the clause as exempting every such tool, E7 needs `narrows WAY-268` with its
  area, a change of one field and one sentence.
- `elements/decisions/template.md` has *Rejected* hold the ways the row's source keeps. Row 7's source,
  question 4, keeps two ways that answer the form of a line and not who chooses a library. The spec
  gives them to E5 and `unknown` to E7. The literal reading would put them in E7 as well.
- "Each separately running program": whether a build script is one is not said. The word stays as
  written.
- The file `foundations/environment_facts.md` was searched for overlap, not read: nothing relevant.
- The base run of the gate had finished when last looked at: 615 tests, every directory passed. Noted
  only because the handoff said it was running.
