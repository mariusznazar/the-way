# Fix report — the seven Minor findings of the review of the whole change

## Status

`done`. Each of the seven findings is fixed by the wording its text gives; none is contested. Where two fixes met, the choice is named below.

## Commits (range from `e51d835`)

- `6e4669e` Fix the Minor findings of the review: name the transitional-state decisions in steps 4 and 7 of the review, drop the rules and the wording that WAY-327, WAY-353 and WAY-354 carried in prose, say where a command and the pointer stand in the steps of an item, and re-wrap final_review.md

One commit; the foundation check passes on it (exit 0, `0 errors`).

## Files changed

- `foundations/decisions.md` — WAY-327 (binding sentence, Verification), WAY-353 (Verification), WAY-354 (Rationale), in place
- `task-cycle/skill/request_template.md` — the fifth-part bullet and the example
- `foundation-review/SKILL.md` — steps 4 and 7
- `foundation-review/weak_points.md` — the end of the section on transitional states
- `project-level/task/skill/final_review.md` — the paragraph re-wrapped

## The findings, one by one

1. **Steps 4 and 7 of `foundation-review/SKILL.md` did not name the new kind of item — fixed.** Step 4 now reads "the proposals about the foundation, the
   decisions that describe a transitional state, the groups of remarks, and the data file that holds the lists (WAY-302, WAY-354)". Step 7 now reads "The
   review is done when the human has decided on every proposal, has answered for every decision that describes a transitional state and has decided on every
   group." Step 7 says "has answered", not "decided", because where the human names an existing task nothing is proposed (`proposals.md`).
2. **WAY-354's Rationale carried "the review does not search", a rule in prose — fixed by dropping it from both places** (the finding's second way). The
   Rationale now says only why the human is asked; the sentence "The review does not look for the task that ends the state, since…" is gone from
   `weak_points.md`, which now ends "Step 6 asks the human at each whether a task exists that ends the state." The binding sentence is unchanged: it says
   the review asks the human, which is what binds.
3. **"as before" — fixed in the three places the finding names.** WAY-327's binding sentence: "the human who checks by hand writes a remark after the
   check." Its Verification: "and the three answers of its group". `request_template.md`: "…the human who checks by hand writes a remark after the check."
   I searched the same three files for another "as before" about this change and found none.
4. **WAY-353's Verification named the rejected script as a violation — fixed by dropping the clause** (the finding's first way). The *violates* line now
   holds the two cases the binding sentence forbids: a place pointed at by a line number alone, and a source that leaves out the line or the revision. The
   script stays in *Rejected*, where it belongs.
5. **The steps rule and its example — fixed in the three ways the finding gives.**
   - The pointer: the example item now ends with `(Checks, 2)` after the steps.
   - The command: the rule now says "A step may give a command to type, written without the name of a file of the repository; where the place or the
     command cannot be told without such a name, the step describes it in words and the item ends with its pointer to the lower part, where the name stands."
     **The reading taken:** a command is plain words for the human, and WAY-286 bans file names and identifiers of entries, not commands; so a command stays
     in a step while no file name stands in it, and a file name goes to the lower part through the item's pointer. This is the smallest reading that fits
     WAY-286 (no file name in the top part) and WAY-327 (the steps give where to go, what to do and what to see). It adds no way to answer and does not
     touch the skeleton or the form check. A command whose every form carries a file path (such as a test runner given a script path) falls under the
     second half: the step says "run the tests of the part, as the pointer gives", and the path stands in *Checks*.
   - The invitation: "If you want to look first, and write a remark with what you saw:" became "The steps of the check by hand, whose result you write down
     as a remark:", placed after the question, so it reads as the fifth part and offers no fourth way.
6. **WAY-354's Rationale cited WAY-329 for more than it says — fixed** by the finding's second way. It now reads "the tasks of a product lie outside its
   repository (WAY-320) and only the line of a task of a project plan has an identifier that a decision derives (WAY-329), so an entry has no name to give
   a task outside a plan." The last clause is my inference from the first two and is marked by "so" as such.
7. **Form of two files — `final_review.md` fixed, `draft.md` left as it is.** The paragraph `Check that every blocking question…` is re-wrapped to
   about 100 characters; the words are unchanged. `draft.md` needs no change: the finding itself judges the rule standing in three files acceptable
   and asks for the wrap only. I also joined one over-long line I made in `decisions.md` (WAY-354 Rationale) to the 100-column wrap of its neighbours.

## Where two fixes pulled against each other

Findings 2 and 6 both touch the same sentence of WAY-354's Rationale. I wrote one sentence that drops "the review does not search" (2) and restates the
WAY-329 reason without claiming more than the decision says (6). Findings 3 and 5 both touch the remark and the answers in the request template; I
applied 3 to the sentence about the answers and 5 to the pointer, the command sentence and the example separately, so neither undoes the other.

## Checks (each with command and true exit code; no pipe hid a code)

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` | 0, `0 errors` |
| `python -B task-cycle/private_paths_check.py <file>` for each of the 5 changed files | 0 for each |
| own-work check: `python -B <scratchpad>/ownwork.py .` — puts the template's example item (with the new pointer) into the three groups of `VALID` of `task-cycle/test_request_check.py` and runs the form check | 0, `problems: []` |
| `python -B gate/run_tests.py task-cycle` | 0, 365 tests OK |
| `python -B gate/run_tests.py project-level` | 0, 275 tests OK |

Not run: the whole gate (as the handoff says). `foundation-review/` has no tests. Findings 1, 2 and 6 change prose and a decision's wording that
no test reads; they are shown by the foundation check (every `WAY-` reference resolves) and by reading the changed lines.

## Own-work check

- Requirement most likely missed by this fix: the template's example item must still pass the form check after it gained the pointer line and a blank
  line inside the item (a blank line before the pointer could split the item or the group).
- Check: the own-work script above. It showed `problems: []`, so the item with the blank line and the pointer stays within the group.

## Reach beyond the dispatch

None beyond the files named in the findings. I read `task-cycle/change/fix.md` whole (the variant's file). `reports/review-whole-change-report.md` was not
needed: each finding was clear from its text and the lines it names.

## Unread material

- `reports/review-whole-change-report.md`: not read (the handoff says to read it only where a finding needs its context; none did).
- Everything else the handoff names — `fix-handoff.md`, `fix-findings.md`, `task-cycle/change/fix.md` — read whole. Every file I changed I had read
  whole in the first round and re-read where I edited it; `foundation-review/SKILL.md` and `weak_points.md` were read whole in the first round and the
  edited passages again here.

## Searches not found or unclear

- None. (Finding 3's mention of WAY-297 and WAY-07 precedent is the reviewer's; I did not look it up, since the finding keeps the fix regardless.)

## Problems observed

None new.
