---
name: make-change
description: Use to make the code of one change in a the-way task cycle — as the one author of a change without a plan, as the executor of a planned slice, as the agent fixing a review's findings, or for a correction after the human's remarks on the request. Covers reading, tests, the own-work check, when to return without code, commits and the report.
---

# Make a change

Makes one change of a task for the cycle `implement-task`: the whole change where one author holds
it, one slice of a plan, the fix of a review's findings, or a correction for the human's remarks on
the open request. Another agent reviews the result with
`review-change`; the cycle decides what follows. This skill holds only how the change is made and
reported.

This skill lives in `task-cycle/change/` of the-way. In the-way itself, the-way is the checkout or
worktree the session works in; in a product, it is the product's pinned `.the-way`.

## 1. Read

- The dispatch: what you make — the change, a slice by its number, a fix or a correction — the
  worktree, and the report path.
- The frozen task document in full, and the spec where the cycle wrote one. For a slice, the plan:
  your slice, its *Read* list and the plan's *Foundation entries*. The task binds where the plan
  says less.
- For a fix, the findings file — the blocking findings of the review — and the code it names. The
  review's Minor and out-of-scope findings are not yours to fix (WAY-161).
- For a correction, the human's remarks on the request; each remark binds.
- The foundation entries and guidelines of the parts your change touches, selected by "Reading the
  foundation" in `elements/common/way_of_working.md` and `product-guidelines/reading.md`. Read
  each selected entry and guideline file whole.
- Every file you change, whole, before you change it.

When a value in the task, spec or plan does not pass your own reckoning — an example number, a
boundary, a command — say so in your report instead of bending the code to it. When reading stops
yielding, make an exploratory edit where the change starts, follow what breaks, and revert the edit
before you commit.

## 2. Tests

- **Test first where it fits.** Where you can name the first failing test in one sentence — a rule,
  a calculation, a contract, a bug to reproduce — write it before the code. Where you cannot —
  configuration, formatting, wiring, prose — write the code and the tests the behaviour needs.
- **A failure is an assertion failing for the expected reason.** A test that stops on a missing
  module, file or function has not failed yet: create the empty function or file first, so the
  test reaches its assertion and fails there. Then make it pass.
- **An invariant's test is seen failing once**, with the command that later shows it passing;
  record both runs as command and exit code. Run it before the code that satisfies it; where the
  code already has the behaviour, break that behaviour for a moment in the worktree, see the test
  fail, and restore the code before you commit.
- **Name the break each test catches.** Before writing a test, name the change in the code that
  should make it fail, and whether that change would be a bug or a deliberate decision. A test only
  a deliberate decision can fail — a constant's value, a message's wording — checks nothing worth
  keeping; test the behaviour that depends on the decision.
- **Derive expected values without the code under test**: literals and hand-checked examples, the
  input and expected value written out. An expectation the code or its helpers compute passes
  whatever the code does.
- **Test behaviour, not text.** A script is run on chosen inputs and its output or exit code
  asserted; a text that instructs agents is tested by what an agent does with it; prose for people
  gets no test.
- **Exercise the real thing.** Replace only what is slow or outside; never assert on the
  replacement itself.
- Before you finish, mutate the code in your head — a wrong constant or branch, a missing side
  effect, an empty return, unchecked empty or hostile input. A mutation no test catches is behaviour
  left unprotected.
- Never weaken an assertion, skip a test or relax a lint rule to make a check pass.

## 3. Check your own work

- Name the requirement of the task — for a slice, of your slice read against the task — that your
  work most likely does not meet, write the check that would catch it, run it and report what it
  showed (WAY-164).
- Changing a user interface, check the states of the affected components that the applicable
  styleguide requires, and inspect a screenshot of the running product by the route its foundation
  settles; where it settles none, check the states in code and mark the screenshot unchecked with
  that reason (WAY-219). Where the settled route fails, report the failed or unperformed check
  itself, not the missing-route reason. Reading code shows no rendered appearance.
- Run the focused checks of your change: the slice's *Checks*, the tests you wrote and the tests of
  the code you touched. The full suite is the cycle's run before the request; do not run it.

## 4. When the plan and the code disagree

- A small mismatch — a name, a path, a signature that moved — adapt to the code and report it in
  one line.
- A structural one — the plan assumes something that is not there, or the change needs a different
  shape — stop and report what the plan expected, what you found and why it matters.
- When unsure which it is, treat it as structural.

## 5. When you return without code

Return a report that holds no code and no diff, with the status `returned`, and leave the branch
for the cycle to reset, when:

- the change needs a choice the task, the spec and the foundation do not settle — the choice,
  where it shows, the ways open and what you found (WAY-135); a choice of how to make what they
  settle is yours to make and to name in the report;
- the change or your slice is more than you can hold — where the size lies (WAY-136).

Where the work cannot go on for a missing fact or permission, it is not returned: commit what you
have made, set the status `blocked` and name the smallest fact or permission missing. The committed
work stays for the cycle.

## 6. Commit and report

Commit your work before you return; never return an uncommitted change. Do the work yourself;
never dispatch a subagent.

Write the full report to the dispatch's report path:

- **Status:** `done`, `done with concerns`, `questions`, `returned` or `blocked` (section 5);
- the files changed, with added and removed line counts, and the commits;
- each check you ran as its command and exit code, the failing run of each test written first and
  of each invariant's test included; each check you did not run, with the reason;
- the own-work check of section 3: the requirement, the check and what it showed;
- every choice you made with the way rejected and its cost if wrong, every adaptation of section 4,
  and a changed invariant test, named;
- for a fix, each blocking finding as fixed — how, with the check that shows it — or contested,
  with the evidence; for a correction, each remark as made, and how;
- problems as observed, with their evidence; a cause only where you verified it, and how; a guessed
  cause marked as a guess.

Return to the orchestrator the status, the commits, a one-line check result and the report path.
Where the work cannot proceed without an answer, do not guess: commit what you have, return every
question you can already see in one batch with the status `questions`, each with the answer you
recommend, and wait to be resumed with the answers. The status `blocked` is for a missing fact or
permission (section 5) and for a question the cycle's foundation step leaves to the human.
