# Return step — task `project-closure-step`

**Status:** done. Head before the step `d4cfe710`; the step committed one commit, `e9a7a81f`
(`foundations/decisions.md` only). Worktree `the task's worktree`, branch
`task/project-closure-step`.

## Return step, as the record gives it

- **Foundation compared with code** (the entries the change writes or changes, those the task names, those the
  search found, the part map; each against `plan_check.py`, `plan_state.py`, `closure.md`, the lead skill, the plan
  template and `task_line.md` at the head):
  - WAY-414, binding sentence against `closure.md` section 2. Did not match: the file searches a change of a
    current decision by its number, while the sentence gave a decision the question of its heading and any other
    entry its identifier or term. Corrected: the sentence now reads "by the question the heading of a new decision
    holds, by the number of the current decision it changes, or by the identifier or term of any other entry, as the
    plan keeps the heading word for word". The pair of examples already carried the number case.
  - WAY-411 ("the tasks the human withdrew") and WAY-412 *Rejected* ("a task of its own or dropped") against the one
    word the fix settled. Did not match. Corrected: "the dropped tasks"; "a task of its own or given up for good".
  - Matched, no change: WAY-411 (the lead skill's step 1 names `closure.md` with its condition; no skill of its
    own); WAY-412 (three places, the closing writes the move, a new file only where no note exists; `closure.md`
    sections 3 and 4); WAY-413 (`closure.md` section 6 shows the closing item, the `Status:` change and the full text
    of each move; the choice of places is no acceptance); WAY-415 (document `refining`, full layout, `source only`;
    line stays, new line only where none; section completed, no second one; `task_line.md` and `closure.md`; the
    precedence paragraph names only the first body); WAY-142 (the `Status:` line reads `draft`, `handed over` or
    `closed`; the code and the template match; the sentence says "delivered in another task" and the check adds that
    the task is not dropped, which stands in the invariant and the template, so I left the sentence as a summary);
    invariant `project-plan-check` against `check_closed` (a row in another state, a row delivered in a dropped
    task, closed plans only); `project-plan-form` through the template (one `Status:` line, `closed` form, calendar
    date); WAY-145 (the closing leaves the question lines of the plan as they are, `closure.md` section 4); WAY-146
    (the script's check of a closed plan is a structure check no critique repeats; its title says "before handed
    over" and I left it, as the task names the entry only for the sentence quoted in its *Decisions in play*);
    WAY-118 (the definition untouched, `closure.md` section 8); WAY-153 and `project-plan-state-evidence` (the reader
    reads no Git evidence for a closed plan and proposes nothing; both speak of a handed-over plan and say nothing of
    a closed one); WAY-107 (places and the rules of the task place are found as `backlog_place.md` and `task_line.md`
    give; the closing writes no rule of a line of its own beyond the derivation the-way gives); WAY-154 (the
    precedence of WAY-415); the part map entry of `project-level` (names the closing, "dropped"); the surface
    `project-plan-state-command` (exit codes kept; the new exit 0 for a closed plan is in the script's description).
  - The two notes of the review of the fix: both were mismatches of an entry with the code and are corrected above.
    The other two (the place where the goal, questions and entries travel, where the human answers that the existing
    document stands; the sentence of `task_line.md` line 15 "a refiner makes one. This is the one place of the
    rule") I judge review findings, not mismatches of an entry or the part map with the code: the file `closure.md`
    carries the first (sections 3, 4, 6), and `task_line.md` says in its next bullet that the project orchestrator
    makes the line at a closing. I corrected neither.
- **Decisions written or changed:** WAY-414, WAY-411, WAY-412 (wording only, as above), each already marked `the
  cycle's` / `row n` by the foundation step; the WAY-414 passage that is the cycle's is the one the foundation step
  gave: "as the plan keeps the heading word for word, and compares the text of what it finds with the projected
  change", beside the key for each kind. The edited sentence of this step, word for word: "by the question the
  heading of a new decision holds, by the number of the current decision it changes, or by the identifier or term
  of any other entry, as the plan keeps the heading word for word" (the number case follows the pair of examples
  WAY-414 already carries, "for a change to a current decision whose number stands without the change it writes
  that the decision stands without it"). No pair of examples added by this step.
- **Invariants written or changed:** none in this step.
- **Environment facts:** none.
- **Glossary terms:** none. The word "closing item" is no term used in another meaning; "entry" keeps its meaning.
- **Part-map changes:** none in this step.
- **Projected entries written whole or in part:** none (the change has `Project relation: independent`).
- **Rows of *Settlements to record* written:** none in this step; the foundation step wrote rows 1 to 6 (WAY-411,
  WAY-412, WAY-413, `project-plan-check`, WAY-414, WAY-415).

## The choices of the cycle that bind after the merge (WAY-36)

| Choice | Decision | Where it stands |
|---|---|---|
| Q1: projected entries that go with a withdrawn task are those whose `Written by` names a dropped task | stays out of the log | an instruction of how an agent works that stands in one skill and carries no choice of real cost: `closure.md` section 2 holds it; WAY-412's sentence ("the entry the task was to write") already says the same in general |
| Q2: a dropped task made a task of its own that already has a document: the preview shows it and asks which stands, the new place refers to the old | stays out of the log; a row for the human | `closure.md` sections 3, 4 and 6 hold it, and WAY-415's pair of examples (added by the fix, `the cycle's`) carries it for comparison; the request puts it before the human, who has not settled it, so no binding sentence is written |
| Q3: a row `done — goal delivered in task <n>` whose task is dropped holds the closing before the preview | stays out of the log | an instruction of the skill (`SKILL.md` step 1, `closure.md` section 1); the check of the same row in a closed plan is already the invariant `project-plan-check` and the plan template |

Nothing in the task's *Out of scope* (the plans and definition of `loop2`; the pin of a product) was touched.

## Checks (command and exit code)

- `python -B elements/common/foundation_check.py`: exit 0, `0 errors`.
- No test or script changed in this step, so no test directory was run; the tests of `project-level` and the other
  directories ran green at `d4cfe710` (the report of the fix) and this step changes one decision's wording.

## Working copies

None made; `.runs/author/` stands empty.

## Unread material

none. (`task-cycle/skill/return_step.md`, `task-cycle/skill/foundation_step.md` and the handoff read whole; the
record template's *Return step* section read; the entries and files compared were read in this and the earlier
tasks of the session.)

## Searches not found or unclear

none. (`elements/decisions/skill/SKILL.md` was read for the step in the first handoff; the two sentences edited here
are wording of entries already written, so no new search of the whole foundation was needed beyond the one made at
the foundation step.)
