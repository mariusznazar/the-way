# Return step report — task `rejected-from-refinement`

**Status:** done

Worktree `C:\Storage\repos\the-way\.runs\worktrees\rejected-from-refinement`, branch
`task/rejected-from-refinement`. Read whole: `task-cycle/skill/return_step.md`,
`task-cycle/skill/foundation_step.md`, `agent-instructions/README.md` ("Make the change").

## Commits

- `c6ee066` docs: carry the ways not chosen where guideline skills and the round answerer restate
  answers — `product-guidelines/coding/SKILL.md` (+2 −1), `product-guidelines/styleguide/SKILL.md`
  (+1 −1), `product-guidelines/testing/SKILL.md` (+2 −1), `project-level/lead/answering.md` (+6 −4).

## Return step (record fields)

- **Foundation compared with code:**
  - WAY-134 (changed): matches `project-level/task/template.md` (*Not chosen* under the answer;
    row *Source* for a choice outside *Questions to settle*), `elements/decisions/template.md`
    (*Rejected* from the row's source, `none considered`, `unknown`), `task-cycle/skill/foundation_step.md`
    (no question for *Rejected*), `elements/common/skill/SKILL.md` step 4, `resolve_gaps.md`,
    `final_review.md`. **Did not match:** three places still listed what reaches *Questions to
    settle* or what a refiner copies without the ways not chosen — the *Questions to settle* item of
    "What reaches the task document" in `product-guidelines/coding/SKILL.md:73–78`,
    `product-guidelines/styleguide/SKILL.md:66–68`, `product-guidelines/testing/SKILL.md:65–71`.
    Corrected: each now adds "and the ways the human did not choose under it as the task template
    gives (WAY-134)". Their "Write each answer under its question … as `refine-task` step 3 gives"
    already reaches the new rule through `resolve_gaps.md`; unchanged.
  - WAY-154 (changed): matches `project-level/lead/skill/SKILL.md`, `conversation_template.md` and
    `orchestrated_mode.md`. **Did not match:** `project-level/lead/answering.md:43–45` (canonical
    answer copied as "answer and source") and `:58–59` (refiners "transfer resolved answers with
    provenance"). Corrected: both now name the ways the human did not choose.
  - WAY-29: matches — recovered decisions keep `unknown` / quoted / human-given rationale and
    rejected options in `elements/decisions/template.md` "Recovered decisions"; the guideline skills'
    "rationale is the human's words or `unknown`" concerns recovered choices and stays.
  - WAY-35: matches — the rule of the *Rejected* field stands in the decision template; the
    `record-decision` skill was not given it.
  - WAY-113: matches — the task template's "the cost the question gave it" takes the costs from the
    decision question WAY-113 requires.
  - Entries the search found (WAY-05, WAY-11, WAY-118, WAY-124, WAY-155, WAY-172, WAY-227,
    WAY-242): no mismatch with the files.
  - Part map of the touched parts (`decisions`, `project-level`, `task-cycle`, `elements-common`,
    `product-guidelines`): no file added, moved or removed; responsibilities unchanged. None.
- **Decisions written or changed:** WAY-134, WAY-154 (both in `1267e73`); none in this step.
- **Invariants written or changed:** none.
- **Environment facts:** none.
- **Glossary terms:** none — "ways not chosen" is used in its ordinary meaning.
- **Part-map changes:** none.
- **Projected entries written whole or in part:** none.
- **Rows of *Settlements to record* written:** row 1 — WAY-134.

## Checks

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` | 0 (0 errors) |
| `python -B gate/run_tests.py agent-instructions` | 0 (18 tests OK) |
| check of added lines over 100 columns (`git diff -U0`) | none |

Not run: the full gate (the orchestrator's). No test file reads the corrected passages (I searched
test files for "words and date", `answering.md` and "copy that answer" and found none). No test written:
these are prose corrections.
