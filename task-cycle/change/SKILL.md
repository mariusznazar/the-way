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

Your dispatch says which of these you make; read for it as its row gives.

| You make | Read |
|---|---|
| the whole change as the one author | As the one author of a change without a plan, the frozen task document whole, and the spec where the cycle wrote one: you make the whole change. |
| a slice, or the retry of a slice | `slice.md`, for how to read the plan and the task, how to read the failed executor's report, and what to do when the plan and the code disagree. |
| the fix of a review's findings | `fix.md`, for the findings file, what is not yours to fix, a finding of a reserved choice, and what the report of a fix holds. |
| a correction for the human's remarks | For a correction, the human's remarks on the request; each remark binds. For a correction, the report holds each remark as made, and how. |

Read what your dispatch names; the orchestrator has selected it for your work (WAY-150).

- The dispatch: what you make — the change, a slice by its number, a fix or a correction — the
  worktree, and the report path.
- The foundation entries the dispatch names by identifier, each whole, and the guideline files it
  names, each whole (WAY-213). Where you write a foundation entry through an element's skill, that
  skill selects the reading the entry needs.
- Every file you change, whole, before you change it.

Where you need something the dispatch does not name — a decision, an invariant, a passage of the
task, the guidelines of a part it did not cover — reach for it selectively: search for its
identifier or a word and read the passage found, a foundation entry whole, never a whole file of
the foundation, and a guideline file whole (WAY-213). Name each such reach in your report — what,
where and why — so that the orchestrator sees the gap in its selection. Where what is missing
still changes what the work means after that reach, return with the status `questions` instead of
guessing (section 6).

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
  left unprotected. Skip this for a part whose mutation tool the product's testing guidelines
  adopt: the reviewer of your change runs the tool there (WAY-253).
- Never weaken an assertion, skip a test or relax a lint rule to make a check pass.

## 3. Check your own work

- Name the requirement of the task — for a slice, of your slice read against the passages of the
  task your dispatch gives — that your work most likely does not meet, write the check that would
  catch it, run it and report what it showed (WAY-164).
- Before you finish a change that alters what a screen shows, read `ui_check.md`.
- Run the focused checks of your change: the slice's *Checks*, the tests you wrote and the tests of
  the code you touched. The full suite is the cycle's run before the request; do not run it, also
  where a plan's *Checks* or your handoff names it — report that as a mismatch (WAY-160).
- A command that may run longer than your harness keeps its prompt cache — five minutes by default
  for a subagent in Claude Code — runs in the background, and you wait for it in stretches of under
  about four minutes, reading its output between them (WAY-255).

## 4. When the plan and the code disagree

Where you make a slice, this section stands in `slice.md`.

## 5. When you return without code

Where the work needs a language, a framework, a library, a store of data, a way of logging in or a
place to run that the task, the spec and the foundation do not settle, read
`project-level/technology/reserved_choices.md` (in a product,
`.the-way/project-level/technology/reserved_choices.md`) and follow it before the cases below, also
where the need looks like a choice of how to make the change. A reserved choice is no such choice:
take no part of it and return the status `reserved`, with a report that holds the choice, where it
shows, the limb of the rule that reserves it, what you searched and the ways you saw, and no code
and no diff. Leave the branch for the cycle to reset, the commits of earlier slices included.

Return a report that holds no code and no diff, with the status `returned`, and leave the branch
for the cycle to reset, when:

- the change needs a choice the task, the spec and the foundation do not settle — for a slice, one
  you searched the task and spec for, as section 1 gives, and found unsettled — the choice,
  where it shows, the ways open and what you found (WAY-135); a choice of how to make what they
  settle is yours to make and to name in the report;
- the change or your slice is more than you can hold — where the size lies (WAY-136).

Where the work cannot go on for a missing fact or permission, it is not returned: commit what you
have made, set the status `blocked` and name the smallest fact or permission missing. The committed
work stays for the cycle to resume or, for a slice's retry, to reset.

## 6. Commit and report

Commit your work before you return; never return an uncommitted change. Do the work yourself;
never dispatch a subagent.

Write the full report to the dispatch's report path:

- **Status:** `done`, `done with concerns`, `questions`, `returned`, `reserved` or `blocked`
  (section 5); the report of `reserved` holds what section 5 gives and no code;
- the files changed, with added and removed line counts, and the commits;
- each check you ran as its command and exit code, the failing run of each test written first and
  of each invariant's test included; each check you did not run, with the reason;
- the own-work check of section 3: the requirement, the check and what it showed; when a check
  failed and passed when run again, both runs as command and exit code (WAY-262);
- each reach beyond the dispatch (section 1): what, where and why;
- **Searches not found or unclear:** each thing you looked for and did not find, or that was
  unclear, wherever it arose — in the
  instructions, handoff, task, foundation or product code — or `none`;
- with the status `questions`, every question you can already see, each with the answer you
  recommend;
- every choice you made with the way rejected and its cost if wrong, every adaptation of section 4,
  and a changed invariant test, named;
- problems as observed, with their evidence; a cause only where you verified it, and how; a guessed
  cause marked as a guess.

Return to the orchestrator only the status, the commits, a one-line check result naming what
failed or did not run, and the report path (WAY-148). Where the work cannot proceed without an
answer, do not guess: commit what you have, write every question you can already see into the
report in one batch, each with the answer you recommend, return with the status `questions`, and
wait to be resumed with the answers. The questions stand in the report, so they survive an
interrupted session. The status `blocked` is for a missing fact or permission (section 5) and for a
question the cycle's foundation step leaves to the human.
