FAIL 6a984c5ee378ec217dfd794f3559a24faeecb7ef

# Review of the whole change — decision-log-second-round

Range `ec7929d..6a984c5` (28 commits: foundation entries `8d04d89`, `e643371`, `ece1f71`, `208f63c`,
`5c10ee4`; slices 1-23). `git rev-parse HEAD` in the worktree is `6a984c5ee378ec217dfd794f3559a24faeecb7ef`,
the head given. Every slice and the foundation entries had no review of their own; this review is
theirs (WAY-136).

## What holds

- To do 1-3 by script (`git show ec7929d:foundations/decisions.md` against the head log): the base
  log had 334 entries and 42 withdrawn numbers, the head has 197 entries and 179 withdrawn numbers.
  137 entries left the log and exactly those 137 numbers were added to *Withdrawn identifiers*; no
  entry left without a row, no row without a leaving entry. Of the table: group A, 115 rows, 108
  withdrawn and 7 kept (WAY-263, 287, 294, 295, 297, 363, 364); group C, 26 rows, 23 withdrawn and 3
  kept (WAY-93, 94, 97); group D: all 6 withdrawn with their target as successor; group E:
  WAY-09 and WAY-312 stay, changed; groups B and F: every entry stays. WAY-374 to WAY-376 stay.
  Every *Why* names the place the plan gives; four differ from the table's "Miejsce" by the plan's
  recorded choice (WAY-304 `remarks.md`, WAY-112 `idea.md`, WAY-322 `list.md`, WAY-338
  `cycle_stages.py`).
- Settlement of question 2: the second paragraph of WAY-100 (`foundations/decisions.md`, WAY-100) is
  the task's English text word for word (compared by hand against `task.md:430`); *Verification*
  has the complying example the task asks for.
- To do 5: `elements/decisions/template.md:42-45` points to WAY-100 with no wording of its own;
  `elements/common/skill/read.md:9-11` sends the reader to the rule on the question of a decision.
- To do 6: WAY-29 has the third binding sentence, its *Verification* and *Rationale*;
  `elements/decisions/template.md:298-300` (Recovered decisions) and `task-cycle/spec/design.md:27-30`
  ask the same.
- Settlement of question 3 / To do 4: 14 entries keep `derives from WAY-100`, 10 gain it, 10 lose it
  (WAY-128-133, 137, 139, 140, 173); seven *Based on* read `TODO — <what is missing>` (WAY-138,
  142, 143, 144, 146, 147, 164), which the field's form allows. No *Based on* or *Rejected* was
  filled from memory.
- References: `python -B elements/common/foundation_check.py` exits 0 with the one expected
  `listed:` line for `tracked-file-private-paths`. The F6 rewordings of binding sentences (WAY-128,
  134, 215, 216, 276, 316, 328, 360) each say in words what the withdrawn number said; the F5 merges
  (WAY-292 → 288, 317 → 316, 323 → 309, 347 → 339, 369 → 368) carry the binding sentences, examples,
  *Rationale* and *Rejected* of the merged entry, read against the base.
- Reason sentences: read by hand against each withdrawn entry's *Rationale* at the base for the
  entries the diff gives a sentence (about 120); each says the entry's reason, none names a file,
  count or measurement the entry does not give. Exceptions are the findings below.
- Q10 has no second case: no withdrawn entry `narrows` a staying entry except WAY-292 and WAY-323,
  which were merged into their targets; no withdrawn entry states a precedence in words ("prevails
  over") either.

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

### Out of scope

12. **Working copies left under `.runs/`** — `.runs\fc.txt`
    and the empty directories `.runs\executor-3`, `executor-6`, `executor-11`, `executor-14`,
    `executor-15`, `executor-16`, `executor-17`, `executor-22`, `executor-23`. Not part of the
    change (ignored by git); the record should name them under working copies left (WAY-373).
    Outside the task.

## Declined to judge

- `elements/decisions/skill/SKILL.md:61-62` (a line between two bullets of projected mode): it
  stands so at the base; outside the task.
- Whether WAY-204, WAY-205 and WAY-235, which cite Google or OWASP, adopt a practice: their
  sources read as evidence for a rule of their own (WAY-205 states what it does instead of Google's
  condition); I left the orchestrator's classification.
- Whether the 15 entries whose *Rejected* says nothing of what the practice leaves out should get a
  sentence: the task forbids inventing it; the request carries them (Q3).

## The orchestrator's choices

- Q3 (leave *Rejected*, list in the request; `TODO` in *Based on*): right; it keeps the task's
  rule that a `TODO` stays `TODO` and the field's form.
- Q5 (WAY-173, WAY-140 lose the relation): right by answer 3; WAY-173 applies WAY-100 to the-way's
  own template but adopts nothing; its *Rationale* still cites WAY-100 in prose, which is enough.
- Q4 (WAY-204, WAY-258 no relation; WAY-167 gets it): right for WAY-204 and WAY-167; I would have
  chosen otherwise for WAY-258 (finding 4).
- Q8/Q10 (ten kept): right for WAY-263 (its *Rejected* is the move), WAY-294 and WAY-295 (the only
  record of the precedence over WAY-344 and over WAY-294, WAY-25), WAY-93, 94, 97 (`narrows WAY-02`)
  and WAY-297, 363, 364 (`narrows WAY-161`): withdrawn, each would leave a template rule colliding
  with a staying decision and nothing recording the precedence (WAY-25, WAY-32), and the skill or
  template names each (WAY-293). Not right for WAY-287, and WAY-202 shares WAY-263's ground
  (finding 6). No withdrawn entry narrows a staying decision (checked by script).
- Q6 (log work before slice 1), Q7 (`project-definition-form` → none, `map-reference-target` →
  WAY-02), Q9 (one agent, three turns): right.
- Q11 (slices 6-23 on sonnet): acceptable as a cost; the findings of this review come from a haiku
  slice (4) and two sonnet slices (14, 21), so the class did not decide quality here.
- WAY-358 merged into the withdrawn WAY-357: the route is acceptable (the list's form allows a
  withdrawn successor, the rule stands in the record template); the missing reason is finding 3.

## Checks run

| Command or method | Exit code / result |
|---|---|
| `git rev-parse HEAD` | `6a984c5ee378ec217dfd794f3559a24faeecb7ef`, the head given |
| `python -B elements/common/foundation_check.py` | 0; `0 errors`; one line `foundations/invariants.md:86: listed: tracked-file-private-paths ...` (to be named in the request) |
| `python -B gate/run_tests.py elements/common` | 0; 201 tests OK |
| `python -B gate/run_tests.py process-audit` | 0; 182 tests OK |
| `python -B gate/run_tests.py installation` | 0; 60 tests OK |
| `python -B gate/run_tests.py task-cycle` | 0; 440 tests OK |
| `python -B gate/run_tests.py gate` | 1; 36 tests, 1 failure: `test_run_tests.DirectoriesAtOnce.test_by_default_every_directory_runs_at_the_same_time` ("did not meet the others", a timing test). The cycle record's *Verification* lists the same test as flaky on the base; the change touches only the docstring of `gate/run_tests.py`, so the failure is not the change's. Run once, not rerun (WAY-243). |
| `python -B task-cycle/change_file_sizes.py ec7929d 6a984c5` | 0; 117 files, lines 33917 → 30179; no code file grew by more than 7 lines; the-way holds no `guidelines/coding.md`, so there is no test of the rule of size (WAY-328), and no finding of structure |
| script (scratchpad `cov.py`): table groups against base and head log | as "What holds" says |
| script `narrows.py`: relations of withdrawn entries to staying ones; relations of staying entries to withdrawn ones | only WAY-292, WAY-323 narrowed a staying entry (both merged) |
| script `prevail.py`: precedence or "template alone" wording in withdrawn entries | found WAY-202's *Rejected* (finding 6) |
| script `logdiff.py`: diff of each of the 74 changed live entries | read whole |
| script `adopt.py`: staying entries naming an outside practice without the relation | WAY-258 (finding 4); others evidence only |
| manual: the diff of the 116 files outside the log (4398 lines) | read whole |
| manual: each added reason sentence against the withdrawn entry's *Rationale* at the base (`rat.txt`, 137 rationales) | faithful except findings 1-3 |

No working copy of the repository was made; every check ran read-only in the reviewed worktree.

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-25, WAY-35, WAY-199, WAY-216, WAY-258, WAY-263, WAY-293 at the
  head: to judge Q8/Q10, finding 2, finding 1 and finding 4.
- `foundations/part_map.md` parts `relation-model`, `gate`, `instruction-files`, `installation`:
  for finding 5.
- `task-cycle/slice_size.py` (grep), `task-cycle/record_template.md:212-237`,
  `elements/environment-facts/template.md` whole, `product-guidelines/template.md:1-40`,
  `elements/invariants/template.md` (grep *Derives from*), `project-level/lead/skill/definition_change.md`
  (grep): to check where a withdrawn rule's reason stands.
- `reports/executor-4-report.md`, `executor-14-report.md`, `executor-21-report.md`: for findings
  2, 1, 3.

## Working copies

None of the repository. Scripts and their outputs stood in the session scratchpad
(`the session's scratch directory`),
outside every repository. Nothing was written under `.runs/review-whole/`.

## Unread material

- Decisions of my selection (the change touches nearly every part, so the selection is the whole
  log): read whole 5 staying decisions (WAY-25, 35, 258, 263, 293) and 24 withdrawn entries at the
  base (WAY-37, 41, 56, 64, 80, 112, 117, 171, 189, 202, 207, 218, 221, 272, 275, 292, 296, 304,
  317, 336, 346, 356, 358, 371); read by title only the other 192 staying decisions, of which the
  69 other changed entries were also read in their diffs with context, not whole. The *Rationale*
  of all 137 withdrawn entries and the binding sentences of 41 of them were read at the base.
- WAY-02 (the rule behind To do 2 and finding Q10) read only in its diff and in the task's quote;
  WAY-100 read in its diff and binding sentences, not its unchanged *Verification* lines.
- Guidelines: the-way holds no guideline files for its own parts (WAY-328); `product-guidelines/reading.md`
  was read in its diff, not whole, so its selection was not run by me.
- `plan.md` read at lines 1-60, 84-123, 560-589 and by grep; not whole.
- The executor reports of slices 1-2, 5-13, 15-20, 22-23 (slices 3, 4, 14, 21 read whole), `planner-handoff.md`, the executor
  handoffs and the survey JSON files: not read; I relied on the handoff's list of mismatches the
  mechanical checks passed on, and on the diff.
- `reports/foundation-report.md`, `planner-report.md`, `cycle.md`, `task.md:1-490`: read whole.

## Searches not found or unclear

- A sentence anywhere outside the log that a fault of one file is not fixed by changing the exemplar
  (WAY-207): not found (finding 1).
- A file that states the reason of WAY-358's pairs: not found (finding 3).
- In the part map, the contents the base WAY-09 required of `installation`, `gate`,
  `elements/common`, `project-level`: not found (finding 5).
- Whether "held there" in `elements/common/rules.md:54` refers to anything in that file: not found.
