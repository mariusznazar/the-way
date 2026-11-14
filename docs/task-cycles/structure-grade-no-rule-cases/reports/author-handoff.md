# Handoff — the one author of the change

You are the one author of a change in a task cycle of the-way. The person who requested the cycle
has delegated intermediate choices to the orchestrator; no answer you get is that person's approval.

- Worktree (work only here, start every command from its root):
  `the root of the task's worktree`, branch
  `task/structure-grade-no-rule-cases`, base commit `1be90579bf3daa618dd87c06bd56042eabb642c1`
  (target branch `foundations`). The repository is the-way itself: no pin, no `.the-way`.
- Method of your stage: `task-cycle/change/SKILL.md` (`make-change`). Read it whole; read a file it
  names, one beside it included, only when the step or variant that names it comes. Your variant is
  "the whole change as the one author".
- Frozen task, read it whole: `docs/task-cycles/structure-grade-no-rule-cases/task.md`. No spec,
  no plan: the task leaves no open design choice and one author holds the change.
- Answers of step 4: trust boundary — no; irreversible operation — no; open design choice — none;
  reserved choice — none; route — one author without a plan; your class — `cheaper`.
- The task carries no row of *Settlements to record* and no projected entry. The change to WAY-363
  is an edit in place of an existing decision (WAY-07, `agent-instructions/README.md` "Start a
  change"). For the foundation step read `task-cycle/skill/foundation_step.md`, and for the edit of
  the decision `elements/decisions/skill/SKILL.md` with the `template.md` and `examples.md` beside
  it, as the step that names them comes. Do the search of the whole foundation once the wording is
  settled (WAY-33) and correct in the same change what it finds.

## What you read besides

- Files you change, each whole where short, otherwise the parts named: `task-cycle/review/SKILL.md`
  (section 3, `## 3. Grade`, the sentence that starts "A finding about the structure of code that
  lies below the threshold of the rule of size"), `foundations/decisions.md` (the whole entry
  WAY-363, from its heading to the next `###`).
- The text the new wording must agree with: `task-cycle/review/whole_change.md`, section "The
  structure of the code the change leaves", its last bullet ("Where that heading holds `none —`,
  or the product's guidelines hold no such rule, there is no such test, the first numbers and the
  diff are your material, and a finding of structure is Minor (WAY-363).").
- Foundation entries, by identifier, each whole (heading to next heading): WAY-363 (the entry you
  change), WAY-362, WAY-360, WAY-361, WAY-161, WAY-364 (the neighbour whose form the entry follows),
  WAY-328 (the-way holds no coding guidelines), WAY-07, WAY-33.
- Other places that speak of a product without the rule and may need no change, which the task says
  already use the general wording: `task-cycle/plan/SKILL.md` (about line 182),
  `task-cycle/change/SKILL.md` (about line 56), `product-guidelines/coding/settle.md` (about line
  89). Also `product-guidelines/coding/template.md` (about line 78) cites WAY-363; judge it by your
  search.
- The-way has no coding guidelines (WAY-328), so none are read, and the change touches no code,
  test or interface.

## Boundary of your stage

- Make the change the task's *To do* items 1–4 and *Acceptance criteria* require, in the commits of
  the task branch, and nothing the *Out of scope* section lists. Do not touch the sentence in
  *Rejected* of WAY-360 about "the same chance in the grade".
- Where the entry's lines change, wrap them as the rest of the entry and of the log are wrapped,
  including the sentence of *Rationale* that starts "The reviewer still judges the scope of each
  finding" (task *To do* 4).
- Run the focused checks the change calls for: at least
  `python -B elements/common/foundation_check.py` and the tests of the directories whose files you
  change (`python -B gate/run_tests.py <directory>`), each with its command and exit code in the
  report. Do not run the whole gate: the orchestrator runs it.
- Do the own-work check as `make-change` gives it, and name the weakest point of the change and the
  check you made against it.
- Do not start the review, the return step or the request, and do not seek approval. Return at your
  boundary.

## Report

Write the full report to
`docs/task-cycles/structure-grade-no-rule-cases/reports/author-report.md`
as `make-change` gives it, with **Unread material** and **Searches not found or unclear** sections
(`none` where there is nothing). Return its status, your commits, a one-line check result naming
what failed or did not run, and the report's path.
