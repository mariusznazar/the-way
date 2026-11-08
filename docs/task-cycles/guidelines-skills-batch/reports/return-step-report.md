# Return step — guidelines-skills-batch

Head compared: `2c46cb75cbcf30e5d495dda9dfe2f919ef0325fc`. Commit of this step: `f5ae96f` (Align the summary of where each guidelines skill hands back with its hand_back.md).

## Return step (fields of `task-cycle/record_template.md`)

- **Foundation compared with code:**
  - WAY-216 (new kind: only the standing checks it touches; a language no check reads makes an extension) against `coding/SKILL.md` "A new kind" and step 4, `recognize.md`, `settle.md`, `hand_back.md`, `task_document.md`, and `reading.md` / `guideline_findings.md` on the first unindexed kind: matches; the reading files send the first-kind task to `maintain-coding-guidelines`, which gives the mode at step 1, so they need no change. `narrows WAY-202` matches `settle.md` ("the task is not ready without one for each" now limited for a new kind).
  - WAY-240 (precedence over WAY-95, scope `product-guidelines, glossary`) against `testing/template.md`, `testing/settle.md`, `elements/glossary/template.md`: match. WAY-95 is not edited: WAY-25 puts the record in the prevailing decision, and its *violates* example for narrower meanings now reads against WAY-240 only in WAY-240's area.
  - WAY-282 (stopped audit closes the list when the work is separated) against `audit_end.md` ("An audit that stopped, with no audit to follow", "Before handing back"), both `hand_back.md`: match.
  - WAY-310 against `coding/template.md` departure way 2: matches; WAY-171's list is unchanged and nothing else in the repository holds the label (grep `Personal data`).
  - WAY-311 against `instruction-files/judging.md`: matches (WAY-311 cited there); consistent with WAY-257.
  - Entries of the task's *Decisions in play* compared with the code the change touched: WAY-172 (styleguide `SKILL.md` two ways: matches; `coding/SKILL.md` and `testing/SKILL.md` keep "only through the task document" — the reviewers' out-of-scope finding O1, left), WAY-171, WAY-204 (rerun of the trial on the chosen set rests on "a trial run of the set": matches), WAY-215, WAY-242, WAY-247, WAY-251, WAY-256, WAY-265, WAY-274 and WAY-276 (`coding/template.md`: matches), WAY-278 (item 8 extends the `none —` reading from a refresh to the first guidelines and an extension, which WAY-278 does not contradict), WAY-168 (grep for "since"/"because" in `coding/template.md`: no rule carries a reason now). WAY-95 and WAY-272/273/275 compared through the text the templates restate.
  - **What no longer matched, corrected in `f5ae96f`:** the summary sentence in "Where the skill works" of `coding/SKILL.md` and `testing/SKILL.md` said the skill hands back to step 3 "where its audit stops for the other skill's"; after item 19 the rule in `hand_back.md` and `audit_end.md` is "while the other skill has not led its matters", also where it has no audit. Both sentences now say that. Nothing else differed.
  - Part map of the touched parts (`product-guidelines`, `project-level`, `instruction-files`, `decisions`, `glossary`): responsibilities, files and dependencies still match; no file is unclaimed; the glossary template line is inside `elements/glossary/**`.
- **Decisions written or changed:** none in this step (the change wrote WAY-240, WAY-216, WAY-282 edited and WAY-310, WAY-311 new, in the foundation step).
- **Invariants written or changed:** none. No task, decision or human sets a rule that a cheap test checks here.
- **Environment facts:** none. The change rests on no source outside the product that the foundation lacks.
- **Glossary terms:** none. No word of the change takes a WAY-95 entry that is not there; "exemplar", "standing check", "gate" are used as their entries give.
- **Part-map changes:** none.
- **Projected entries written whole or in part:** none (the task is independent, no project definition).
- **Rows of *Settlements to record* written:** none in this step; rows 1-5 were written by the foundation step: row 1 WAY-240, row 2 WAY-310, row 3 WAY-311, row 4 WAY-282, row 5 WAY-216 (report `author.md`).

## Choices of my reports checked against `return_step.md` (WAY-36)

- `author.md` choices (move of the "choice found in the tests" sentence; pointers kept in both places; the clause "touches" and its later removal; the unspecified trigger of the stopped skill's return; the unspecified verdict of a proposal row; "in its own text" for the kept rule's meaning): each is skill text the task's items ask for or a detail left open, not a choice that binds beyond the text it sits in. None is a decision the rule gives an entry for; they stay rows of the questions table.
- `fix-1.md` choices (M4, M8 smaller readings; M1 cell content; I1 fix placed in `settle.md`): same; rows of the questions table.
- Item 19 ("a skill hands back to step 3 while the other has not led") and items 13, 15, 17 are task items with no row in *Settlements to record* (the table says "9 shown, 5 accepted"). The task accepts five entries only, so I wrote no entry for these; they stay rows of the questions table.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — 0 errors, exit 0.
- `python -B -m unittest installation.test_coding_guidelines_installation installation.test_testing_guidelines_installation` — exit 0 (4 tests).
- `python -B gate/run_tests.py agent-instructions` — exit 0 (18 tests).
- `python -B instruction-files/check_instructions.py .` — exit 0 (0 errors, 1 warn from the unchanged root `AGENTS.md`).
- `product-guidelines/**` has no test directory. Not run: the full gate.

## Reaches beyond the dispatch

- `task-cycle/record_template.md` section "Return step" (the fields of this report) and `foundations/invariants.md` (grep of `Part:` lines for the touched parts, to see whether an invariant concerns them): none does.
- `reports/review-whole-report.md` lines 115-130, only to see what O1 and O2 are and leave them.

## Searches not found or unclear

- The task says "9 shown, 5 accepted" but names only the five accepted rows; I cannot tell which of the four others (if any) is item 19 or 17, so I took "no row" as "no entry".
- Whether WAY-95 should name WAY-240 in its own *Verification* (an example now read against WAY-240's area) is unclear; WAY-25 puts the record in WAY-240 only. I left it.
- The questions of `author.md` listed under "Searches not found or unclear" (the audit of dependencies under "touches", the trigger of the stopped skill's return, the verdict of a proposal row in `judging.md`) remain open; no source settles them.
