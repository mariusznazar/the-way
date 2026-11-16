# Fix report — the review's findings I1-I6 and M1-M6

**Status:** done

**Commit:** `cdbde3d2` (range from the reviewed head `940893de`). Files changed: `foundations/decisions.md`, `task-cycle/change/walkthrough.md`, `task-cycle/change/SKILL.md`, `task-cycle/skill/request_template.md`. Every finding is fixed; none is contested.

## Findings

| Finding | What I did | Evidence |
|---|---|---|
| I1 | `walkthrough.md` section 4: the column "By what" now names only ways of the running product (screen in a browser, call of an API, command in a terminal, reading of the data the running product holds); "a reading of the code" is removed, and a new point says that a reading of the code is no way to the running product and fills no row of that column, so a case only the code could check stays unchecked with that reason. | `git diff 940893de -- task-cycle/change/walkthrough.md`; settlement: the answer under the question on `test-run` (column filled by the product's way). |
| I2 | `request_template.md`, *Checks*: removed the added "its cases with the verdict of each (WAY-406)"; the top part keeps "the cases and verdicts of the author's walk ... among them" in the reports. The description now holds of the walk only what *To do* 5 asks: unchecked cases (kind 4) and out-of-scope errors (kind 8). | `git diff 940893de -- task-cycle/skill/request_template.md`. |
| I3 | Three things. (a) WAY-408's second paragraph now names the group: the description puts each such error before the human "under *Fix or let through*, with the question whether to make a task of it, which merging lets through". (b) Precedence recorded as WAY-25 gives: WAY-408 *Relations* now read `derives from WAY-239 · narrows WAY-289` (the `derives from WAY-289` is dropped), and the binding sentence says "in this area this decision prevails over WAY-289, under which the cycle puts before the human only what it judges will be felt"; the *Rationale* says why, and the *violates* example gains "or leaves it out because the cycle judges it will not be felt". (c) Kind 8 of the template gains the sentence that the walk's reported errors stand in that item with no judgment of what is felt and only the question "Make a task of it?"; *Findings outside the task's scope* gains the place where such an error stands. No new kind number (so `correction.md`'s handling of item 8 covers it). | WAY-287 second paragraph (a decision adds a kind and names the group); WAY-25. Passages of what the human accepted that give the outcome, for the request to quote under WAY-408 (marked `the cycle's`): *To do* 5, "błąd spoza zakresu zadania znaleziony przy przejściu trafia do sekcji dla decyzji człowieka jako sprawa do rozstrzygnięcia (zrobić z niego zadanie czy puścić)"; row 5, "błąd poza zakresem zadania zgłasza do PR-a jako sprawę dla człowieka". |
| I4 | `walkthrough.md` section 1: now "A skill of the product may hold the steps of operation and cites the decision, so search the product's skills for the identifier of each of those decisions and read each skill found", the direction WAY-121 gives. | the sentence added to WAY-121 ("a skill of the product may hold the steps of operation and cites that decision"). |
| I5 | WAY-406 *Rejected*: removed "and, of the courses, a limit on simultaneous instances of agents and a field of how to check in each part of the part map"; the rest of the "left out" list stands (it is the task's own list of what stays at VOX). | the answer under the question on the addendum ("Poza zadaniem") and *Out of scope*; WAY-134. |
| I6 | WAY-407 *Scope* is now `task-cycle, project-level`. | part map entry `project-level`; WAY-238 *Scope*. |
| M1 | WAY-406 rewritten into a first paragraph of three sentences (who walks, for which changes, the method), a second paragraph (audit moves the walk to a stage of its own; the fix does not repeat it) and a third (no settled way: not performed, cases unchecked, one item with the screenshot), each of 1 to 3 sentences. WAY-319: the added sentence stands in a paragraph of its own. | `foundations/decisions.md`, WAY-406 and WAY-319. |
| M2 | WAY-406 *Rationale*: "a team of the author's" is now "a team of the human who owns this process"; "no step of the cycle made an agent find ..." is replaced by a statement that holds with no history of the process ("an agent that finds what the tests leave out ... catches an error the tests let through"). | same. |
| M3 | `change/SKILL.md` section 6: the bullet now opens "as the one author or the executor of a slice" and says "(the fix and a correction report no walk)". | same. |
| M4 | WAY-121 *violates*: the broken line is re-flowed. | same. |
| M5 | `walkthrough.md` section 5: the block of effects cites "WAY-406; WAY-13 for what cannot be undone". | same. |
| M6 | WAY-407 and WAY-408 now say "the author of a change or the executor of a slice" in their binding sentences, the *Verification* and the *Rationale* (and "the agent" where the sense holds for both). | same. |

Other entries changed under WAY-33: the WAY-406 pair of examples reads for the executor too (unchanged in meaning); the WAY-408 pair; `request_template.md` kind 8 and the lower part's *Findings outside the task's scope*; no other entry names the changed sentences (searched `walk through the running product`, `WAY-408`, `WAY-289`, `WAY-407` across the tracked files).

## Checks

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| `python -B task-cycle/private_paths_check.py <file>` for `foundations/decisions.md`, `task-cycle/change/SKILL.md`, `task-cycle/change/walkthrough.md`, `task-cycle/skill/request_template.md` | 0 each |
| `python -B gate/run_tests.py task-cycle` | 0 (534 tests, OK, 2 skipped) |
| `python -B gate/run_tests.py elements/common` | 0 (257 tests, OK) |

Not run: the full gate; `project-level` and `agent-instructions` tests (no file of those directories changed in the fix).

## Own-work check (WAY-164)

- **Requirement most likely not met:** *To do* 5 and row 5 — every out-of-scope error the walk finds reaches the human in the description, whatever the orchestrator's judgment.
- **Check:** read the three places that carry it against each other: WAY-408 (binding sentence and *violates*), kind 8 of `request_template.md` and *Findings outside the task's scope*, and ran `foundation_check.py` for the new `narrows` relation (exit 0, no mutual narrowing with WAY-289, which names no relation to WAY-408).
- **Showed:** the path is closed at each step (reported by the author in `SKILL.md` section 6, restated in kind 8 without the felt-judgment, listed in the lower part); the check found no error.

## Reaches beyond the dispatch

None beyond reading `task-cycle/change/fix.md`, `agent-instructions/README.md` ("Make the change"), and a search of `task-cycle/` for references to kind numbers (`correction.md` handles "item 8"), to avoid adding a kind.

## Unread material

The review's report (not mine to read, per the handoff). `foundations/decisions.md`: WAY-25 and WAY-287 read by their passages through a search, not whole. `task-cycle/skill/correction.md`: read by the lines the search found (60-110), not whole.

## Searches not found or unclear

- The handoff's alternative for I3 ("settle the collision by the decision that prevails, or word WAY-408 and kind 8 so that they agree"): I did both; the passages that give the outcome are those quoted in the I3 row, which the request is to quote under WAY-408.
- No place in the template names a kind of item for the *Fix or let through* group that holds "errors the author reported"; I kept the item in kind 8 rather than adding a kind number, and it is the reviewer's to judge whether a kind of its own is needed.

## Working copies

`.runs/author-fix/` held the outputs of the checks; removed before I returned.
