# Return step — friction-at-source

## Status

`done`. Nothing needed correcting; no commit. Head stays `6e4669e`, the working tree is clean.

## Foundation compared with code

Compared at the head `6e4669e`, the fix included, each entry with the files that restate it:

- **WAY-327 (changed in place) against `task-cycle/skill/request_template.md`.** The binding sentence (fifth part for an item about an unrun check the
  human can do by hand; three to six steps; same answers; the human writes a remark after checking; the writer checks against the fifth part too)
  matches: step 2 of "Write, check, publish", kind 4, the bullet in "What an item carries" and the second example all say the same, and the example
  carries three steps, the three answers of the group and the pointer `(Checks, 2)`. The form check and the skeleton are untouched, as WAY-286 and WAY-290
  say; the own-work check of the fix (the example item through the form check) passed. No "as before" is left in either place.
- **WAY-353 (new) against `project-level/task/template.md`, `skill/draft.md`, `skill/final_review.md`.** All three say heading or quotation, the line
  only as a hint, and the *Source* of an answer keeps its line and revision. The *Source* line of the skeleton in the template is unchanged.
- **WAY-354 (new) and the term `transitional state` against `foundation-review/`.** `weak_points.md` (the list, made by reading, not by a word),
  `with_the_human.md` (item 2, one at a time, the question whether a task ends the state, the task made on the human's yes), `proposals.md` (the proposal and
  the data file) and `SKILL.md` (steps 2, 4, 6, 7) agree with the binding sentence; no file asks for a field in a decision's entry or a question at
  refinement. The meaning of the glossary entry is the one the foundation-review files use; every use of the words in tracked files was listed by search
  (`transitional`) and is in that meaning.
- **Entries the task names — WAY-286, 287, 289, 290, 24, 302, 305, 36, 37, 01.** None is contradicted: WAY-286 (no file names in the top part) is met by
  the steps rule; WAY-287 and WAY-289 keep their three groups and three answers; WAY-290 still judges no content and the template says the steps are not
  checked by the script; WAY-24 (no field for a review in an entry) and WAY-302 (a proposal becomes a task, the review changes nothing) fit WAY-354; WAY-305
  (weak points) is untouched; WAY-36 keeps out a rule that ends with its own change, and the review skill says the same; WAY-37 has nothing waiting for what
  this change brings; WAY-01 holds, since WAY-354 describes a state the product has and the decisions hold no plan.
- **Entries the search of the foundation found** (first-round report): WAY-301, 303, 304 (tag and remarks), WAY-24/302/305 (what the review does),
  WAY-36: unchanged and still true.
- **Part map.** The touched parts `task-cycle`, `project-level`, `foundation-review`, `decisions`, `glossary` keep their descriptions and file lists;
  no file was added, moved or removed, so no file needs an assignment. `python -B elements/common/foundation_check.py` (which checks the assignment of
  every file to a part) passes.

## Decisions written or changed

`none` in this step. (The change itself wrote WAY-353 and WAY-354 and changed WAY-327 in the foundation step; they stand as committed.)

### The choice the handoff names: a step may give a command to type, without a file name

Judged a choice of wording, not a choice that binds; it stays in the questions table (a row for the request's item 5, *You accept by merging*), and I
write no entry for it. Reason:

- WAY-286 forbids, in the top part of a description, file names and identifiers of entries; a command is neither. That a step may carry a command is
  therefore already allowed by the decision that exists. The template sentence says how the two meet and where a name that cannot be left out goes (the
  item's pointer to the lower part, which the template already requires of any item whose evidence stands there). It adds no new constraint on later
  work that a later author could not read from WAY-286 and that pointer rule.
- Writing it into WAY-327's binding sentence would add a rule the task did not settle (the task's row 3 covers the fifth part, not its wording of
  commands), and the foundation step and the return step write nothing beyond the task. A later request that goes the other way — a step with a file name —
  breaks WAY-286 and is caught there.
- Where the reviewer or the human disagrees, the cost is one sentence in the template and a decision to write; that is the cheap side.

## Invariants

`none`. The task, no decision and the human set no rule for an invariant; the change adds no behaviour that an invariant should hold.

## Environment facts

`none`. The change rests on no source outside the product that the foundation lacks: WAY-353's Rationale quotes the register of problems of 2026-11-12 as
a measurement with its date, as WAY-352 does with `Based on: none`; WAY-354's search of the log is a search of the product's own file.

## Glossary terms

None written in this step. `transitional state` (row 4) was written in the foundation step and stands as committed. No term was used against its entry,
so no use needed correcting.

## Part-map changes

`none`.

## Projected entries

`none` (the task is independent and carries no project definition).

## Rows of *Settlements to record* written

All four were written by the foundation step; none was missed:

- row 1 → WAY-353 (new)
- row 2 → WAY-354 (new)
- row 3 → WAY-327 (changed in place)
- row 4 → the glossary term `transitional state` (new)

No row is tied to an entry already stated (the search found none), so the request names no kept row under item 5 for that reason.

## Commits

None. The compared entries and files match after the fix.

## Checks (command and true exit code)

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` at `6e4669e` (output to a file, code read at once) | 0, `0 errors` |
| `git status --short` | clean |
| tests of directories: not run — no file was changed in this step | — |
| whole gate: not run, as the handoff says | — |

## For the orchestrator

- The command-in-a-step choice is a choice of the change beyond the task's wording that the human meets when working with the process: it belongs in the
  request's item 5 (*You accept by merging*), with the reason above and with the way not taken (a command barred from steps) — see the first-round report,
  choice 3, and the fix report, finding 5.
- No part-map assignment is needed.

## Unread material

- `task-cycle/skill/foundation_step.md`: read whole in the first round; not re-read here (the return step writes nothing).
- Everything else: this step re-read the three decisions whole, the glossary entry, the changed passages of `request_template.md` and the
  `foundation-review/` files from the head, and listed the uses of `transitional` and of "four parts" by search. The ten entries named in the task's
  *Decisions in play* were read whole in the first round and compared here by the passages the change touches, not re-read.

## Searches not found or unclear

- None. (The `git grep` for "four parts" found only `request_template.md` and the decision itself; the other hits, `audit_count.py` and
  `problem_register.md`, speak of another set of four.)
