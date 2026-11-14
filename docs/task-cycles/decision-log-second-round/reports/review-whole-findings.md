# Findings of the review of the whole change that the fix takes (cut word for word from reports/review-whole-report.md, lines 46-173: the blocking findings and the Minor findings within the task; the out-of-scope finding 12 is left out)

## Findings

### Important (blocking, within the task)

1. **A clause of WAY-207's rule stands nowhere after the withdrawal** —
   `product-guidelines/coding/template.md:144-156` (rule **Linter**). Slice 14, `5959aa9` (and a
   gap of the plan, whose text for this file named only the approval clause as missing).
   WAY-207 at the base: "a fault of one file is fixed in that file, never by turning a rule of the
   linter off for the whole product nor by changing the exemplar for that file's sake". The
   template now holds the first half and the approval clause, but nothing in the template, the
   skill `maintain-coding-guidelines` or a staying decision says that the exemplar is not changed
   for one file's sake (WAY-199 covers approval of an exemplar change, not this; `grep exemplar
   product-guidelines/coding/` shows no such sentence). The entry's *Verification* names exactly
   that as a violation: "the exemplar is changed so that a new file departing from it passes the
   rules a script checks from it". To do 2 asks that the rule of a withdrawn entry stand in its
   place; part of it is lost, so a later agent may change an exemplar for one file's sake with no
   rule against it. The executor saw it (`reports/executor-14-report.md`, Findings) and left it.
   Fix: add the clause to the rule of the linter or to the section on files of a kind, with the
   reason the entry gives ("the exemplar is what every later file of its kind follows").

2. **A rule of the shared way of working is restated in an element's skill, against WAY-35** —
   `elements/environment-facts/skill/read.md:7-10`. Slice 4, `6283bb2`.
   The plan's text for this file was "remove WAY-37 (line 6)" and "Make no other change". The
   executor added a new bullet with WAY-37's rule ("A change that brings what entries of the
   foundation wait for also fixes every entry that waits for it, in the same change") and its
   reason, which already stand once in `elements/common/way_of_working.md:114-118`. WAY-35: "the
   way of working the skills share stands once in that part, and a skill reads the rules and that
   way of working from there instead of restating them"; its *Rejected*: "rules restated in the
   skill next to the template — two copies that drift". The change's file does what a decision of
   the-way forbids. Fix: remove the bullet (the first bullet of the file already sends the reader
   to `way_of_working.md`).

3. **WAY-358's rule has no sentence of its reason anywhere** — `task-cycle/record_template.md:217-225`.
   Slice 21, `e94b13d`, with the route chosen in F5 (`e643371`).
   WAY-358 (group D) could not become a paragraph of WAY-357, which F4 withdrew; the cycle's route
   — its number on the list with WAY-357 as successor, its rule in the record template — puts it
   under To do 2, which asks for the rule in its place "z jednym zdaniem powodu". The template
   holds the pairs `<source> · <kind>` but no reason for them, and the entry's *Rationale* ("a pair
   keeps apart who raised a correction, which is read, and what was wrong, which is judged, so
   that two numbers come out of the pairs: a defect that the review of the change let through,
   `remark · defect`, and a defect that the cycle saw and left, `item · defect`") now stands in no
   file; its *Rejected* is lost as the handoff says. The executor names this
   (`reports/executor-21-report.md`, "Beside the files: WAY-358"). Without the reason, the next
   agent who simplifies the pairs into one cause has nothing to say why the audit needs them apart.
   Fix: one sentence after line 225, from that *Rationale*.

4. **WAY-258 adopts an outside practice and lacks `derives from WAY-100`** —
   `foundations/decisions.md`, WAY-258 (*Relations*: `derives from WAY-256`). Foundation row F3,
   `8d04d89` (the orchestrator's Q4).
   Its *Rationale*: "Anthropic's guide for skill authors ... recommends references one level deep
   from the skill's main file; ... the decision keeps the same depth for Codex and Cursor on that
   word", and its *Rejected*: "a cap on the lines of a skill's main file, as the same guide
   recommends". It names the practice, what it takes and what it leaves out — the pattern of the
   addition to WAY-100 — so by the answer to question 3 ("tylko te, które nazywają przejętą
   praktykę") and To do 4 ("i decyzji, które przejmują praktykę bez niej") it carries the relation.
   The planner and the orchestrator held it borderline and gave none; the entry's own words are
   not borderline. Cost of leaving it: a reader following WAY-100's dependants misses one adoption,
   and To do 4's set is incomplete. Fix: add `derives from WAY-100` to its *Relations*.

### Minor (within the task)

5. **Group E, WAY-09: the part map does not hold all the inventory the binding sentence dropped** —
   `foundations/decisions.md` WAY-09 (first paragraph), `foundations/part_map.md`. Foundation row
   F7, `208f63c`. The table moved the directory inventory to the part map "where it repeats it",
   and WAY-09 now says a directory other than an element's reaches the main branch once it holds
   "what the sentence of its part in the part map names". The part map's sentences name
   responsibilities, not all the contents the base sentence required: `installation` ("preparing a
   product repository to use one pinned commit") no longer requires its tests and its README,
   `gate` its tests, `elements/common` the script that migrates a foundation from the earlier form,
   `project-level` its readiness check, plan check, reader of plan states and their tests. The
   foundation agent named part of it ("with its tests" stands only in *Verification*). The
   completeness rule bites only when a new directory is added, so the effect today is small; the
   human accepted the move on the claim that the map already holds the inventory, which is only
   partly so. Either the part map's sentences gain what is missing, or the request says what the
   rule no longer requires.

6. **Q8/Q10: the keep criteria are applied unevenly** — `foundations/decisions.md` WAY-287 kept,
   WAY-202 withdrawn. Orchestrator's choice; no slice. WAY-287 is kept because staying entries rely
   on it (WAY-289, WAY-274, WAY-293), but the same holds for many withdrawn entries (WAY-271 for
   WAY-273/274/276, WAY-286 for WAY-287/288/316, WAY-202 for WAY-203/206/216, WAY-226 for
   WAY-104/240, WAY-40 for WAY-44/48/52, WAY-217 for WAY-215/328, WAY-219 for WAY-316/319). And
   WAY-202 had WAY-263's ground: its *Rejected* "the three named in the template alone — nothing
   would bind the refinement to check them" and its *Verification* violation "the three stand in
   the template and in no decision of the-way" are the move this change made. I would have
   withdrawn WAY-287 as the table says, and either kept WAY-202 with WAY-263 or named it to the
   human beside WAY-263 with the same reason. The request should at least put WAY-202 before the
   human with WAY-263's reason. The other nine keeps are right (see the choices below).

7. **A dangling "there" and a repeated clause in the identifier rule** —
   `elements/common/rules.md:52-56`. Slice 3, `21a3e94`. "Splitting or merging part map entries, or
   environment fact entries, or invariant entries held there, gives each entry that comes out of it
   a new identifier, and any other change keeps it" — "held there" is WAY-64's phrase for "held on
   the commit the branch left the main branch from" and has no antecedent here; "and any other
   change keeps it" repeats the sentence before. The meaning matches the base ("Splitting or
   merging entries ..."); a reader may stumble on "there".

8. **The projected-mode reason repeated in four element skills, beyond the plan** —
   `elements/decisions/skill/SKILL.md:64-66`, `elements/environment-facts/skill/SKILL.md:47-48`,
   `elements/glossary/skill/SKILL.md:50-51`, `elements/invariants/skill/SKILL.md:62-63`. Slice 4,
   `6283bb2`. The plan asked no reason in slice 4; the sentence "Projecting keeps a future ...
   visible in the definition without claiming that it already holds" already stands in
   `elements/common/projected_mode.md:4` (slice 3), which each skill reads first. Four copies of
   one sentence to keep in step; no reader gains from them.

9. **Rule sentences added where the rule already stands elsewhere** — Minor duplications a later
   edit must keep in step: `project-level/lead/skill/route_changes.md:18-20` repeats
   `project-level/lead/skill/definition_change.md:10` (slice 18, `735455e`);
   `product-guidelines/coding/kinds.md:10-11` repeats the first-file half that
   `product-guidelines/coding/SKILL.md:133-134` holds (slice 13, `ab75f6c`);
   `elements/common/skill/build_table.md:23-25` repeats step 5 of the variants (slice 3);
   `product-guidelines/styleguide/starting_rules.md:3-4` states the timing the skill's description
   already gives (slice 15, `93f1989`).

10. **Lines over the wrapping width and one punctuation slip** — added lines exceed the 100
    columns their files keep: `product-guidelines/template.md:13`, `gate/run_tests.py:17`,
    `foundation-review/weak_points.md:28`, `instruction-files/judging.md:16`,
    `project-level/skill/read_foundation.md:7`, `task-cycle/review/whole_change.md:34`,
    `elements/glossary/template.md:86`, several in `task-cycle/skill/SKILL.md` (steps 4, 9, 10 and
    the stage reports), and in the log the rewritten lines of WAY-215, 216, 243, 276, 288, 309,
    316, 328, 339, 360, 368; `process-audit/audit_count.py:52-54` ends a semicolon list item with a
    full stop (slice 8). Polish.

11. **The own-work checks of the slices aimed at the number removal, not at the weakest point**
    (WAY-164) — slices 4, 14 and 21 among others named "a number stays or a sentence around it
    changes" and checked it by grep; the weakest point of these slices is a rule left incomplete
    or a sentence added beyond the plan, which a grep cannot catch, so findings 1-3 passed. Noted
    for the fix: its own-work check should read each touched rule against its entry at the base.

