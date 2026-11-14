PASS

# Review of the revised spec: co trafia do dziennika decyzji

Revised spec: `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md`, compared with `spec-reviewed.md` (a full `diff` of the two, then the changed passages read in place, then the lines of D1 to D3 around them). The designer's report and the orchestrator's rulings (`reports/designer-report.md`, `reports/designer-revision-handoff.md`) were read.

## Each earlier finding

1. **The line for an unknown base broke the installer test: resolved.** D1 now writes the `listed:` line only where the working tree's `foundations/decisions.md` holds at least one decision. I checked the real fixture: `installation/install.py` (`empty_foundations`, line 97) writes `decisions.md` as `# Decision log\n`, no decision, so `test_empty_foundations_have_valid_form` sees no extra line and its loop over every line but the count line still passes. Constraints now names that test, says every other existing test that runs the script or reads its report passes as it stands, says the change edits no installation test, and says `test_cross_part_imports.py` keeps the names it imports. D9 adds the case "no commit and an empty log (no such line)". The test fixtures of `test_foundation_check.py` hold decisions and no commit, so they do get the line, and they assert with `assertIn` and "0 errors", which it does not disturb.
2. **The temporary pair had no file: resolved.** D2 now says where the two halves stand (a bullet in `elements/decisions/skill/SKILL.md` step 3, a clause in `task-cycle/skill/return_step.md`), and the list of D6 names both (the `SKILL.md` step 3 second bullet, and `return_step.md` "also gets the clause of D2 that trims the pair"). The foundation step follows that `SKILL.md` ("by following the pinned `SKILL.md` of its element"), so the first half reaches the writer; the second half is in the file the return step reads. The open alternative stays in the line for the human.
3. **WAY-12 lacks "rationale and rejected stay whole": resolved.** In D3 and in the WAY-12 line of *Foundation entries*.
4. **A file missing at the base: resolved.** A new D1 bullet: a base that lacks `foundations/decisions.md` or `foundations/invariants.md` makes the base unknown for that file, never empty; no decision counts as changed on account of the first, no invariant is listed on account of the second, and the line is written under the rule of finding 1 naming the file. D9 has both cases. The sentence in D2, "heading absent at the base" = new, still reads literally, but D1 states the exception in its own words ("not read as every entry is new"), so a builder has one reading.

## What the revision changed besides, checked

- The word "binding part" became "binding sentences" in D2 and D3, with one sentence saying why (the glossary's "binding part" may include fields). A search of the revised spec finds "binding part" once, in that explaining sentence, and nowhere in an older passage; D8 and the *Foundation entries* lines already used "binding sentences". No contradiction.
- The new notes on WAY-241, WAY-237, WAY-235, WAY-268 and WAY-17, read against the log:
  - WAY-241 and WAY-237 concern fields and items of the testing template that name a decision, and WAY-173 keeps a product bound to a template rule only through its adopting decision; leaving them is consistent.
  - WAY-235 narrows WAY-168 for trust boundaries and the testing template's trust-boundary rule still names its adopting decision, so the reworded WAY-168 does not collide with it.
  - WAY-268 says every non-reserved choice is "entered in the cycle record's questions table", which does not forbid an entry as well; the spec's line (the places of D6 govern a choice that binds after the merge, an excluded choice stays a row as WAY-293 keeps it) agrees with it. The spec's wording "stay in the questions table" for those choices is looser than WAY-268's "entered in" but means the same.
  - WAY-17: true as stated (the only decision of the real log whose *Verification* holds neither invariant nor pair); the consequence is correctly drawn.
  - WAY-135 and WAY-136 are not named anywhere in the revised spec, so no line about them needed judging. I had read their binding sentences for the first review; nothing in them bears on the change.
- The D9 test for an invariant with no *Method* is in; it follows the Constraint on WAY-344.
- The Constraints bullet "every existing test runs with no base known and must pass as it stands" and the new empty-log rule do not collide: fixtures with decisions get the line and pass; fixtures with an empty log (the installer's) get none.
- I checked D1 to D3, D6 and D9 for the older passages that now read otherwise: the Non-goals ("no change of ... the discipline templates") still agree with D7; the Goals list still holds ("a test that holds a decision's sentence have a form each"); D4's "where the base is unknown no invariant is listed" agrees with the new D1 bullet. No sentence of an older passage contradicts a changed one.

## New findings

None.

## Notes, not findings

- The two bullets of `SKILL.md` step 3 (the pair "only for the part no test holds" and, beside it, "carries a pair for now when a later slice writes the test") read as opposed at a glance; D2's paragraph "Where the two halves of the rule stand" explains the order, and the planner should keep the bullets side by side with the reason. This is wording, left to the maker.
- WAY-268's phrase "stay in the questions table" in the spec's line could be copied verbatim by the foundation step's search into WAY-268; the wording to use is WAY-268's own.

## Unread material

- The revised spec: read as a full `diff` against the reviewed spec and in place around every changed line (D1 whole, D2 whole, D3 beginning, D6's "Who applies it", D9, the *Foundation entries* and the *Other decisions* lists); the unchanged passages (Intent, Goals, D4, D5, D7, D8, Left to the maker) were read whole in the first review and are byte-identical in the diff.
- WAY-241, WAY-237 and WAY-235: read whole in the first review (binding sentences, *Verification*, *Rationale*) for WAY-241 and WAY-237 and to the end of *Rationale* for WAY-235; WAY-268 binding sentences, *Verification* and *Rationale* start read in this review.
- WAY-135 and WAY-136: binding sentences only (first review, about twenty lines each); *Rationale* and *Rejected* not read.
- Everything else named in the first handoff keeps the "Unread material" of `reports/spec-reviewer-report.md`.
- I ran no test and no script.

## Searches not found or unclear

- A place in the revised spec that still words the unknown-base rule without the "at least one decision" condition: none found (D1, Constraints, D9 agree).
- A use of "binding part" in the revised spec other than in the explaining sentence of D2: none found.
- A mention of WAY-135 or WAY-136 in the revised spec: none found.
- Any other test in the repository that runs `foundation_check.py` on a repository with no commit and a non-empty log, which the unknown-base line would break: none found (only `installation/test_install.py` runs it on a product, and that product's log is empty).
