PASS 4905a56544ff8d9600af406d52afdfcd588e3493

# Review of the whole change — scripts-fail-on-missing-fields

Range `e9a0f926dc9758f6554e8c0a30925d3e4d68cfed..4905a56544ff8d9600af406d52afdfcd588e3493`. `git rev-parse HEAD` printed
`4905a56544ff8d9600af406d52afdfcd588e3493`, the head given. `git log` of the range: one commit. `git diff --stat`: one file,
`foundations/decisions.md`, 79 insertions. Route: one author, no plan, no slices.

Verdict: no blocking finding. 0 blocking, 4 Minor within the task, 2 outside the task's scope.

## Coverage of the task

*To do* item 1 and its six sub-points, and the rows of *Settlements to record*, against the entry WAY-330
(`foundations/decisions.md:10939-11016`):

| Item | Where in the entry | Verdict |
|---|---|---|
| Separate decision beside WAY-328 | the new entry follows WAY-329 and precedes *Withdrawn identifiers*; number 330 held by no entry and no withdrawn number (`grep WAY-330 foundations/*.md` finds only the entry) | met |
| Row 1 / sub-point 1: script checks the fields it needs; missing or renamed field gives an error naming it; no guessing; absence is no empty value | binding sentence 1 | met, wording faithful |
| Sub-point 2 and row 4: a field is any named thing the script looks for data by — section heading, row label, table column, JSON key | binding sentence 1 (a section heading, a row label, a table column or a JSON key) | met |
| Sub-point 3 and row 1: new scripts; in a changed script the whole reading of each file whose way of reading the change reworks, all fields of that file, no other file, no other part of the script | binding sentence 2 | met |
| Sub-point 4 and row 3: exit code 2 with file and field; form-checking script lists the missing field it checks as a finding with exit code 1 | binding sentence 2; two *Verification* examples | met |
| Sub-point 5 and row 2: one test per covered reading, file without one field, asserts the failure naming it; review answers for the other fields | binding sentence 3 | met |
| Sub-point 6: *Scope* names all 16 parts; a new part is added to it | binding sentence 3 and *Scope* | met. I compared the 16 headings with a `- **Files:**` line of `foundations/part_map.md` with the *Scope* items as sets: equal; the set equals WAY-328's *Scope* too |

Fidelity. *Rejected* holds the eight *Not chosen* ways of the four questions of *Questions to settle*, each with its cost taken
from the task (Q1 a and c; Q2 a and b; Q3 a and b; Q4 b and c), and no way of the writer's own (WAY-134). The binding part adds no
requirement beyond the task. The entry claims nothing about existing scripts. Out of scope (review and repair of existing scripts)
is untouched: no script, test or skill file changed. Binding sentences: three (counted by sentence stops in my scratch run), present tense, no *should*, *will*, RFC 2119 capitals; no carriage returns; `git diff --check` clean.

Foundation check of the entry against the entries I read: WAY-328 unchanged, its price sentence still true; WAY-38's quiet-pass
sentence is quoted faithfully; exit 2 in the entry fits WAY-294's *Rejected* and `task-cycle/skill/SKILL.md:502` ("Exit 2 is no
listing: fix the call, or the file that could not be read."); no invariant states an exit code that the new rule contradicts
(`record-copy-image-check`, `gate-exit-code` speak of one script each and the rule claims nothing of existing scripts); WAY-12's
"tests live only with invariants" is read in Minor 1 below. The claim of the task's *Context* that `task-cycle/test_remarks_check.py`
cites no invariant is true (`grep -c 'invariant:'` gave 0).

## Judgement of the author's three concerns and two additions

1. **The *Verification* pair of examples.** Acceptable. Every example restates a row (the `due` -> `due_date` case is the task's
   *Context*; the section-heading rework, the form-checker with exit 1, the new-part-to-*Scope* sentence and the missing test are rows
   1-3) and nothing about existing scripts. The pair is optional in the template. By the letter of the skill's step 3 a pair is
   added "where the human gives one or accepts one you propose"; no human gave or accepted this one, so it stands only through the
   merge. Graded Minor 3, because it needs naming in the request, not a change.
2. **The last sentence of *Rationale* about WAY-12.** Source-backed (task *Context*, bullet on WAY-12) and the reading is right for
   the repository's practice, but it sits in prose. Graded Minor 1.
3. **Concern 1 (WAY-12 letter vs the required test)**: same as 2.
4. **Concern 2 (part-map surfaces that "keep their exit codes")**: not a collision of two decisions; a change of a surface goes
   through WAY-49, and the entry claims nothing about existing scripts. Outside the task; listed under out of scope.
5. **Concern 3 (`remarks_check.py` exits 0 without a `reports/` directory)**: existing script, outside the task; I did not verify
   it. Listed under Declined to judge.

## Blocking findings

None. Slice of origin: none (no plan).

## Minor findings within the task

1. `foundations/decisions.md:10991-10992`, last sentence of *Rationale*: "Tests of a script's behaviour stand without an invariant,
   since WAY-12 concerns how a decision is checked." What is wrong: it states, in prose, how an agent is to read WAY-12 against the
   test this entry requires; WAY-05 puts what a decision forces on later work in a binding sentence or a field, never in prose, and
   WAY-12 itself still says "tests live only with invariants" with no relation to this entry. Why it matters: an agent reading WAY-12
   alone, or comparing a change with it, meets a rule it will take as forbidding the test that WAY-330 requires; the only place that
   resolves it is the rationale of another entry. Evidence: WAY-12 binding sentence; template line 130 "Tests live only with
   invariants"; WAY-25 on unrecorded collisions. Not Important: the human's task states this reading (*Context*, WAY-12 bullet) and the
   practice agrees (`test_remarks_check.py`). Suggested: keep the sentence, name it in the request's section for the human's decisions
   as the cycle's wording, and leave a narrowing of WAY-12's wording to a separate change.
2. `foundations/decisions.md:10972-10975`, *Verification* violates, "a change adds a reading of a file with no test that gives the
   file without a field": it drops the qualification of the binding sentence, which covers the readings of a new script and the
   reading of a file a changed script reworks. A change that adds a reading of a further file to an existing script is covered only if
   "reworks the way of reading" is taken to include it; the entry does not say so, and the task's Q2 answer says "gdy zmiana go
   dotyka". Effect: an agent comparing a change may judge more or less sharply than the binding part. Suggested: say in the example
   "a new script, or a changed script's reworked reading of a file, with no test ...". Minor, not Important, because the example
   reads reasonably as the stricter side of an ambiguity the task itself leaves.
3. `foundations/decisions.md:10959-10960` and the pair of examples: the writer's own additions (the relation `derives from WAY-38`,
   the pair of examples, the WAY-12 sentence) are not carried by any row. The row text and Q1 answer say "spokrewniona z WAY-38 jako
   reguła z tej samej rodziny"; WAY-32 defines `derives from` as "a higher decision this one serves", which is a stronger claim than
   "same family", though the *Rationale* does rely on WAY-38's quiet-pass sentence, so the relation is defensible. They are accepted
   by the human only at the merge (WAY-114), so the request must name them in its section for the human's decisions as the cycle's
   choices. Suggested: that naming; no change to the entry.
4. `foundations/decisions.md:11014`, *Rejected*: "the skills that read exit codes know only 0, 1 and 2" is a statement of what the
   process's tools do today, which WAY-05 and the template allow only where the entry quotes a source; here it is the writer's
   paraphrase of the task's *Not chosen*. It goes false as soon as a code is added. Suggested: end the clause at "each would have to
   be extended". Minor.

## Minor findings outside the task's scope

1. The part map's surfaces `tracked-private-paths-command`, `project-plan-state-command` and `foundation-check-command`
   (`foundations/part_map.md:197-217`) promise to keep "its exit codes". A later change that gives one of those scripts exit code 2
   for a missing field changes what the surface promises; WAY-49 governs that, and WAY-330 states nothing about existing scripts.
   Author's concern 2; the task gives no direction.
2. A word: "field" in WAY-330 (a thing a script looks for data by in a file) and "field" of an entry (*Scope*, *Based on*; WAY-71,
   invariant `map-reference-target`) are two uses in one foundation, and the glossary holds no entry for it. WAY-330 defines its use
   in its own binding sentence, and I found no sentence a reader would read wrongly for lack of an entry (WAY-297), so Minor and not
   in the task's reach.

## Declined to judge

- The behaviour of any existing script of the-way against the new rule, including the author's concern 3 (`remarks_check.py` with
  no `reports/` directory): out of scope of the task (review and repair of existing scripts).
- Whether WAY-12's wording should be narrowed: a separate change, not asked by the task.
- Whether `derives from WAY-38` versus `none` is the better relation: the task says "spokrewniona"; both read within it (Minor 3).

## Checks run

- `python -B elements/common/foundation_check.py` (cwd = the worktree) — exit code 0, output `0 errors`.
- `git rev-parse HEAD` — exit 0, `4905a56544ff8d9600af406d52afdfcd588e3493`.
- `git log e9a0f92..HEAD`, `git diff --stat`, `git diff` of the range — exit 0; one commit, one file, 79 insertions.
- `git diff e9a0f926dc9758f6554e8c0a30925d3e4d68cfed HEAD --check` — exit 0.
- Scratch run (`python -I`, input read-only): parts of the part map with a `- **Files:**` line = 16; WAY-330 *Scope* = same set;
  WAY-328 *Scope* = same set; no carriage return in the entry; no *should*, *will*, *must*, MUST, SHALL, MAY in the binding
  sentences. Exit 0. Scratch script in
  a scratch script in the reviewer's temporary directory
  (prints decision entries by number).
- `git status --short` of the worktree before and after — clean (I changed no file but this report).
- Not run: `gate/run_tests.py` (the orchestrator's, by the handoff). No test exists or was written; the change is one foundation
  entry, and the entry sets no invariant, so no invariant test is changed.

## Reaches beyond the dispatch

- `elements/decisions/template.md` and `elements/decisions/skill/SKILL.md` whole: to judge the form of the entry and step 3's rule on
  a pair of examples (the handoff pointed to the form of WAY-03 and the method).
- `task-cycle/skill/SKILL.md:495-509`: to confirm the reading of exit 2 the entry relies on.
- `task-cycle/test_remarks_check.py` (one `grep -c`): to confirm the task's claim of a test without an invariant.
- `foundations/part_map.md` lines 170-249 and the surfaces there: to judge the author's concern 2.
- `task-cycle/review/whole_change.md` and `elements/common/way_of_working.md` lines 40-120: the method.

## Unread material

Counts of the decisions of my selection (WAY-150). The change touches `decisions`, and the new entry's *Scope* names all 16 parts
(WAY-44), so every one of the 288 decisions of the log is in the selection; 40 were read whole (including WAY-330 itself) and
248 by title only.

- Read whole (40): WAY-03, 05, 09, 12, 17, 18, 19, 21, 22, 25, 30, 32, 33, 36, 38, 51, 63, 71, 89, 113, 114, 134, 148, 164, 173,
  217, 228, 260, 290, 294, 295, 299, 309, 321, 323, 324, 326, 328, 329, and WAY-330.
- Run through by title (248): every other decision of the log, by the list of the 288 titles printed from `foundations/decisions.md`.
- Decisions that bear on the change and stayed unread: none that I judge to bear on it beyond those opened. Of the titles, those
  nearest to the topic (scripts, exit codes, tests) that I did not open whole were WAY-125, 150, 161, 162, 316, 325, which concern
  the cycle's methods, the selection of reading, findings and the record-copy check, and WAY-229-246 and 252-254 on a product's
  tests, which WAY-328 sets aside for the-way's own tests.
- Guideline files: none exist (WAY-328); none to read.
- Invariants: all 356 lines of `foundations/invariants.md` read whole. Part map: lines 1-249 read whole. Glossary: whole (179 lines).
- `task-cycle/request_check.py` and the rest of the code of scripts: not read (a foundation entry only).
- The author's Unread material (WAY-03 and the rest) is passed to me by the handoff: WAY-03 read whole by me; I compared the form
  against WAY-03, WAY-05, WAY-328 and WAY-329.
- Cycle files not read: the cycle record and the handoffs to other stages (not in my dispatch).

## Searches not found or unclear

- none found for anything I looked for.
- Unclear: whether a pair of examples that the writer proposes and no human has accepted may stand in an entry that the cycle writes
  from rows (the skill's step 3 says "where the human gives one or accepts one you propose"; WAY-114 puts the acceptance at the
  merge); I treated the merge as the acceptance and graded it Minor 3.
- Unclear: what "reworks the way of reading" covers in the binding sentence when a change adds the reading of a further file to an
  existing script (Minor 2).
