PASS 6e4669e

# Review of the fix of the Minor findings, `friction-at-source`, range `e51d835..6e4669e`

Head confirmed: `git rev-parse HEAD` printed `6e4669eb6f2257a454e3141c6bf816e35a45394f`. One commit, 5 files. The worktree stayed unchanged (`git status --short` empty).
Counts: 0 blocking; 0 new findings; 0 of my seven Minor findings remain; 1 Minor note outside the fix's reach (below).

## The seven findings

1. **Fixed.** `foundation-review/SKILL.md` step 4 now lists "the decisions that describe a transitional state" among what `proposals.md` holds (WAY-354).
   Step 7 now reads "has decided on every proposal, has answered for every decision that describes a transitional state and has decided on every
   group". "Answered" fits the case where the human names an existing task and nothing is proposed. The end condition now names the new item.
2. **Fixed**, by the finding's second way. "the review does not search" is gone from WAY-354's *Rationale* (`foundations/decisions.md`, about
   `:11759-11768`) and the sentence "The review does not look for the task..." is gone from `foundation-review/weak_points.md`, which ends
   "Step 6 asks the human at each whether a task exists that ends the state." `git grep -n "does not search\|does not look for the task"` over
   `foundation-review`, `request_template.md` and `project-level/task` finds nothing. The binding sentence of WAY-354 was not touched.
3. **Fixed** in the three places named. WAY-327's binding sentence now ends "writes a remark after the check." Its Verification says "the three
   answers of its group". `request_template.md` (fifth-part bullet) has no "as before". `git grep -n "as before"` over the touched files finds none.
   The binding sentence is still three sentences (WAY-05).
4. **Fixed**, by the finding's first way. WAY-353's *violates* now holds the two cases its binding sentence covers (a place pointed at by a line
   number alone; a *Source* that leaves out the line or the revision). The script stays in *Rejected*.
5. **Fixed** in the three ways the finding gives. (a) The pointer: the example item ends with "(Checks, 2)" after the steps, in the form the
   template gives for pointers ("(Minor findings, 3)", `request_template.md:189`), which holds no file name or identifier. (b) The command: the rule
   says a step may give a command to type, written without a file name, and that where the place or command cannot be told without one the step
   describes it in words and the item ends with the pointer to the lower part. That is coherent with WAY-286 (no file names in the top part) and
   WAY-327 (where to go, what to do, what to see), and adds no answer. (c) The invitation: "The steps of the check by hand, whose result you write
   down as a remark:" reads as the fifth part, not as a fourth way, so WAY-327's *violates* is not near. The example still passes the form check
   (own-work check below).
6. **Fixed**, by the finding's second way. The *Rationale* now says the tasks lie outside the repository (WAY-320) and "only the line of a task of a
   project plan has an identifier that a decision derives (WAY-329), so an entry has no name to give a task outside a plan". The WAY-329 clause now
   says what WAY-329 says, and the inference is marked by "so".
7. **Fixed** for what the finding asks: `project-level/task/skill/final_review.md` is re-wrapped, the longest line is 101 characters, and its words
   are unchanged (the diff shows the same sentence in a new wrap). `draft.md` is left, as the finding allowed ("no fix needed beyond the wrap").

## Settlements and entries after the fix

- Row 1 (WAY-353): meaning unchanged; the file statements (`project-level/task/template.md`, `draft.md`, `final_review.md`) still say the same.
  The *Verification* now follows the binding sentence.
- Row 2 (WAY-354): binding sentence, scope, relations and *Rejected* unchanged. The files (`weak_points.md`, `proposals.md`, `with_the_human.md`,
  `SKILL.md` steps 2, 4, 6, 7) now all name the new kind of item and none adds a rule the entry lacks.
- Row 3 (WAY-327): fifth part, three to six steps, same answers, still stated alike in the entry, the template's rule and the example.
  The new "a step may give a command" is in the template only and the entry is silent on it; none of the entry's *violates* cases
  touches it, so there is no conflict.
- Row 4 (glossary): untouched.

## Declined to judge

- Whether a command in the top part of a description is wanted at all (WAY-286 is silent on commands; the fix reads it as allowed). The finding
  asked for it to be said, and it is said. Outside this fix.

## New findings in the fix diff

none.

Minor note outside the fix diff (goes to the request's list, no block): the rule "a step may give a command" in `request_template.md` is the
author's reading of how WAY-286 and WAY-327 meet, and no decision states it. If the human wants it to bind, it is a candidate for WAY-327's binding
sentence. It is within the task's reach and this fix's answer to my finding 5, so I raise no finding.

## Checks run (true exit codes; none through a pipe)

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py > <scratchpad>\fc2.txt 2>&1; echo "fc exit $?"` | 0, `0 errors` |
| `python -B <scratchpad>\ownwork.py .` (the author's own-work check of the first round, read by me before; puts the example item with its new pointer into the three groups of `VALID` and runs the form check) | 0, `problems: []` |
| `python -B gate/run_tests.py task-cycle > <scratchpad>\tc2.txt 2>&1` | 0, 365 tests OK |
| `python -B gate/run_tests.py project-level > <scratchpad>\pl2.txt 2>&1` | 0, 275 tests OK |
| `git grep -n "as before\|does not search\|does not look for the task" -- foundation-review task-cycle/skill/request_template.md project-level/task` | 1, no match (nothing printed; exit 1 is `git grep`'s code for no match) |

Not run: the whole gate (the orchestrator's). `foundation-review/` has no tests, so findings 1, 2 and 6 are shown by reading the diff and by the
foundation check. `skill_entry_points.py` was not run again: the front matter of no skill file was touched in this commit (`git diff e51d835..6e4669e --stat`
lists the five files named by the author, none with a front matter change).

## Reach beyond the handoff

- `task-cycle/skill/request_template.md:184-192`: read, to check that the pointer form of the example matches the template's own form for pointers.
- `foundations/decisions.md` WAY-327, 353, 354 at the new head: read whole in the changed passages (the full entries were read in the first round).

## Unread material

none beyond the choice below: the decisions and invariants of the first review's selection are not read again, since the findings file bounds this
review (counts of the first round stand: 32 whole, 175 by title only of 207). The fix author's report and the findings file were read whole.

## Searches not found or unclear

none
