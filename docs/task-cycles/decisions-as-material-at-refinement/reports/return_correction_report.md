# Return report — repeated for the correction

Status: `done`. Commits: none (nothing needed correcting). Head compared: `c8bf864`; worktree clean.

## Return step (record form)

- **Foundation compared with code:** read WAY-113 whole, sentence by sentence, as it stands, and compared it with the files the handoff names and with the entries that link to it.
  - Binding sentence (three sentences): the general question; the refinement carve-out for a definition, a task document, the technology step and "the entries written during that refinement"; the cycle and entries written outside such a refinement as before, with the boundary of WAY-315. Agrees with `elements/common/way_of_working.md` "How a skill asks" (same split, same example "projected entries of a definition"), `project-level/technology/settle.md` sub-step 6 (answer written as given, a question only for a quoted contradiction), `elements/common/skill/task_variant.md` step 4 (same), `project-level/lead/skill/SKILL.md` step 5 and `project-level/task/skill/orchestrated_mode.md` (the questions the project orchestrator requires are those for a quoted contradiction; a choice that changes a decision or follows a loose remark is an exception).
  - *Verification* (complies and violates): names a task or a project definition and the entries written during it; agrees with the binding sentence.
  - *Rationale*: the sentence "Where an entry is written outside such a refinement or a cycle runs, the answer is about to bind, so the question stays; the entries written during a refinement ... follow the rule of the refinement" agrees with the binding sentence; the earlier sentence "it is kept for an answer in the person's own words" speaks of the general rule and is followed at once by the refinement carve-out, so the two do not collide. No stale sentence found.
  - *Rejected*: agrees (the two ways of the task's question 2).
  - Linked entries: WAY-123 (derives from WAY-113: "lets the choice stand without a question asked after it" and its Rejected "every choice shown on its own, followed by a question against it"), WAY-155 (derives; its question to the human is a question of decision, not one against an answer), WAY-174 (derives; asks the human the choices, no question against an answer), WAY-315 (names WAY-113 among the looser rules that hold only before the cycle): all still true.
  - What no longer matched and its correction: none.
- **Decisions written or changed:** none in this step (the correction already changed WAY-113 in `c8bf864`).
- **Invariants written or changed:** none.
- **Environment facts:** none.
- **Glossary terms:** none.
- **Part-map changes:** none.
- **Projected entries written whole or in part:** none.
- **Rows of *Settlements to record* written:** unchanged from the first return step: row 1 WAY-313; row 2 WAY-314; row 3 WAY-113; row 4 WAY-134 (with WAY-115, WAY-124); row 5 WAY-315.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0 ("0 errors"), on the head compared (no edit in this step).
- Not run: the full gate (it passed on this head, per the handoff); no focused directory, since no file changed.

## Reaches beyond the handoff

- `elements/common/skill/definition_variant.md` step 4 (lines 34-48): read to check the entry-writing rule of a definition against WAY-113.

## Searches not found or unclear

- Unclear, left unchanged: `elements/common/skill/definition_variant.md` step 4 item 1 still lets the "implication" move ("you wrote X; from X follows Y — does Y hold?") and an anchor "from the human's words or from the material" challenge a settlement of an entry written during a definition's refinement, while WAY-113 now says that for those entries the question against an answer is asked only for a contradiction with a quoted earlier sentence of the human. The task's point 3 names only the "collision" move for narrowing, and the earlier dispatch said not to touch the "implication" move; I did not change it. If the orchestrator reads WAY-113's new sentence to cover the implication move, that one move and the words "or from the material" need a matching narrowing.
