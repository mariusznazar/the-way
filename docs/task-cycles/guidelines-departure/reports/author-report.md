# Author report — guidelines-departure

**Status:** done

## Files and commits

- `foundations/decisions.md`: +47 / -0 (new entry WAY-327, placed after WAY-326, before *Withdrawn identifiers*).
- Commit `7442841` — "Record the departure of the-way from the general coding guidelines and the testing guidelines" on `task/guidelines-departure`. Worktree clean (the report lies under ignored `.runs/`).

## One entry or two (my choice)

One entry, WAY-327. Row 2 (a change that adds a part to the part map adds it to the *Scope* of the departure) only keeps the *Scope* of row 1 true; it is no independent question, so it stands as the second binding sentence of the same entry (decide_entry.md: "keep the question the rest serves"). Cost if wrong: a reviewer who wants row 2 as its own decision splits it into a WAY-328 and edits WAY-327's second sentence out; no other entry refers to either yet.

Heading: "Does the-way hold its own code and tests to the general coding guidelines and the testing guidelines of a product?"

## Checks

- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0, "0 errors".
- Own-work check. Requirement most likely unmet: *Scope* lists exactly the 16 parts of the part map. Check: a Python snippet read the *Scope* of WAY-327 and the parts of `foundations/part_map.md` (sections with a **Files:** line, excluding surface sections) and compared them as sets — result `True`, 16 listed, 16 distinct, identical to the task's list. Same snippet found none of should/will/MUST/SHALL in the binding sentences. Run once, passed first time.
- Not run: the product's gate (the orchestrator runs it, per handoff); no test, since no code or invariant was required.

## Meaning of each entry

- the cycle's / row 1 + row 2 (WAY-327), English: The-way does not hold its own code and tests to the general coding guidelines or the testing guidelines of a product, with no time limit and in all 16 parts of its part map, so no task of the-way waits for such guidelines; a change that adds a part to the map adds it to the decision's *Scope*.
- row 1 + row 2 (WAY-327), Polish: The way nie podlega własnym wytycznym kodowania ani wytycznym testów produktu, bez terminu ważności i we wszystkich 16 częściach swojej mapy części, więc żadne zadanie the way nie czeka na takie wytyczne; zmiana, która dodaje część do mapy części, dopisuje ją do *Scope* tej decyzji.

(The entry is written whole from rows 1 and 2, so its mark is `row 1` and `row 2`; no part of it is "the cycle's".)

## Choices

- *Relations*: `derives from WAY-217 · derives from WAY-173` (WAY-217 gives the departure and the rule that it applies only within the decision's scope; WAY-173 gives that a departure is a decision of the log with its reason). No `narrows WAY-215`: WAY-215 itself opens with "Unless a departure under WAY-217 applies", so this decision goes against nothing. Cost if wrong: one relation line to add.
- *Based on*: `none` — the only source is the human's answer, a decider's motive, not a source outside the product. *Origin*: `none` (the task document is private and goes away; the reasoning fits the entry).
- *Verification*: no invariants, a pair of examples only. I wrote no invariant for "every part is in *Scope*" because the task asked for none and it would need code and a test (see concerns).
- *Rejected*: only the three ways the task keeps in its *Not chosen* — (a) own guidelines, (c) WAY-215/reading saying the rule excludes the-way, and the narrower scope of nine parts with code — each with its cost; wording rewritten without file names or counts (template). No way of mine added.
- The styleguide exclusion appears in the *Rationale* and in a "violates" example, not in the binding sentences (the binding sentences name the two disciplines the departure covers).
- WAY-209 and WAY-244 (skill proposals "before the first code/test") not tied by *Relations*: they bind skills' proposals for a product with no code/tests, not this question; the-way already has both.

## Concerns

- Nothing checks mechanically that a new part reaches this *Scope*; only review and the request's reading of the decision do. An invariant plus test ("each part of the map is in the *Scope* of WAY-327") would close it; it is a possible follow-up for the orchestrator or the human, not required by the task. If left, the failure shows only when a later task of the-way over a new part is refined and the agent finds the part outside *Scope*.
- Cost of the decision as recorded: nothing of a product's guidelines protects the-way's code and tests (stated in *Rationale*).

## Reaches beyond the handoff

- `elements/common/way_of_working.md`, `elements/decisions/template.md`, `elements/common/rules.md`, `elements/decisions/skill/{SKILL,read,decide_entry}.md`, `elements/decisions/examples.md` — read whole, as the record-decision skill's steps 1-2 name them (examples.md names WAY-03; I did not read WAY-03, see Unread material).
- `foundations/part_map.md` (selected parts `decisions` and the list of parts; read the first 30 lines and lines 160-240 and a section scan, to verify the 16 identifiers and distinguish parts from surfaces) — to check the Scope identifiers.
- `product-guidelines/reading.md` lines 1-80 — to see how a departure is read, so the wording fits.
- Search of the whole foundation (WAY-33) by grep for "depart", "the-way itself", "agent-instructions/README", "guidelines": read whole WAY-173, WAY-202 (heads and verification), WAY-09 (beginning), WAY-10 (beginning), WAY-298, WAY-299 (beginning), WAY-326. Findings: no decision answers this question in passing; nothing to move; no glossary term needed ("departure" is used in the plain sense of WAY-217/WAY-173); no collision with another decision.

## Unread material

- `foundations/decisions.md` WAY-03 (named by `elements/decisions/examples.md` as the example of a decision's form): not read; I took the form from the template and from WAY-215, WAY-217, WAY-209, WAY-244, WAY-326, which I read whole.
- WAY-09, WAY-10, WAY-298, WAY-299, WAY-202: read in part (headings and the parts shown above); they are reaches of my search, not named by the handoff.
- `foundations/part_map.md`: read in part (first parts, product-guidelines and the surfaces), as above.
- `product-guidelines/reading.md`: read lines 1-80 of it.
- The handoff's named files, read whole: the task, WAY-215, WAY-217, WAY-209, WAY-244, `task-cycle/change/SKILL.md`, `task-cycle/skill/foundation_step.md`, the record-decision skill and files it names. I did not read the part map entries of every part ("the part map's entries for the part `decisions`" were read), nor the invariants file (the skill's step 1 selection for the part `decisions`: I searched the invariants file only by grep for "guidelines").

## Searches not found or unclear

- No `guidelines/` directory and no decision on a departure for the-way found in the log, as the task's *Context* says (confirmed by grep for "depart").
- Unclear: `elements/decisions/skill/SKILL.md` step 3 says *Verification* names invariants "those step 4.4 writes"; I wrote none, so *Verification* holds only the pair of examples, a form the template allows.
- The handoff's selection step 1 (decisions whose *Scope* names `decisions`) I did not run in full: the decisions I read by identifier and by the search above were enough for this entry, but I did not read whole every decision whose *Scope* names `decisions`.
