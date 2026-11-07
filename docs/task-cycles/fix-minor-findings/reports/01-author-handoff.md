# Handoff 01 — the one author, the whole change

**Delegation.** Mariusz (the human) asked for a task cycle on one ready task; the orchestrator
(me) has delegated intermediate choices to you through me. Nothing here is the human's approval.

**Worktree.** `C:\Storage\repos\the-way\.runs\worktrees\fix-minor-findings` (branch
`task/fix-minor-findings`, base `86cc21e876f27f5d7d3ffd811ba11b687ac04cc6`). Work only there. Never
touch `C:\Storage\repos\the-way` or any other worktree. This is the-way itself: the checkout is the
process, and there is no `.the-way` pin.

**Method.** Read `task-cycle/change/SKILL.md` whole, in the worktree, and follow it as "the whole
change as the one author". Read a file it names (`fix.md`, `slice.md`, `ui_check.md`) only when its
step comes. You make the code of the change AND the foundation step: read
`task-cycle/skill/foundation_step.md` whole before you write the decision entries, and the skill of
the decisions element (`elements/decisions/skill/SKILL.md`, with the template and `examples.md`)
when you write an entry. Run `python -B elements/common/foundation_check.py` after writing entries.
Stage boundary: you return after your commits and report; you do not review, run the full gate
(`gate/run_tests.py` is the orchestrator's), take the return step, or open a request. Run focused
tests only (`python -B gate/run_tests.py <directory>` for a directory you touched, and
`python -B -m unittest` for a single test file). Write no scripts without need; the change is prose.

**Frozen task.** `C:\Storage\repos\the-way\.runs\worktrees\fix-minor-findings\.runs\task-cycles\fix-minor-findings\task.md`
(the original task document, copied; read it whole, including *Questions to settle* with answers,
*Questions carried to cycle*, *Decisions in play* and *Settlements to record*). No spec, no plan.
Rows 1, 2, 3 of *Settlements to record* are yours to write whole; their meaning is the row's, their
wording is yours.

**Answers of step 4.** Trust boundary: no. Irreversible operation: no. Open design choice: none.
One author without a plan. Author class: `same` as the orchestrator.

**What the task wants, in one paragraph.** The cycle fixes the Minor findings of the review of the
whole change (those not marked outside the task's scope) before it opens the request: inside the one
fix that already runs for a blocking finding, or, with no blocking finding, in one fix for them alone
with one review of that fix. If the review of a Minor-only fix finds a new Critical or Important
finding, the cycle reverts that fix's commits on the branch (a revert commit, so they stay in
history) and opens the request on the code the whole-change review accepted; the Minor findings and
the new finding go to the request's description; no third round. A fix that also carried Minor
findings because it ran for a blocking finding ends as WAY-162 gives today. The request's item for
unfixed findings the user or the human will feel (item 8 of *For you to decide*,
`task-cycle/skill/request_template.md` around lines 184-189) asks for each such finding that the cycle
did not fix (outside the task's scope, Minor of reviews after the whole-change review, Minor of a
reverted fix): "fix it in this request, or make a task of it?", where one answer may cover the whole
list. "Fix it" runs a correction (`task-cycle/skill/correction.md`) with one fix and one review;
what the correction leaves unfixed is put by the request only with the question of a task or stays
in the lower part, so the loop ends after one correction. Findings nobody will feel stay in the lower
part as today.

**Choices the orchestrator has already made for you** (record them in your report as given; do not
re-open them; each has its row in the cycle record):

- Q1: `task-cycle/skill/correction.md` gets a short paragraph (it does not rely on "The remarks
  bind" alone): an answer to item 8 of the request that asks for the fix makes the findings it
  names the remarks the correction binds; the correction's review ends as every review does; the
  findings that remain unfixed after it go only with the question of a task, or stay in the lower
  part. State this in `correction.md`, and the corrected request's variant in
  `request_template.md` ("A correction" row) accordingly.
- Q2: the fix for Minor findings alone is made by the same agent a blocking fix of the same route
  would be: the one author (resumed, on its class), and on the planned route a fresh agent with
  `make-change` on the orchestrator's class (a Minor finding names no slice). The review of that fix
  is by the reviewer of the whole change, resumed, or fresh given its report. Put this into "The end
  of a code review" of `task-cycle/skill/SKILL.md` (lines about 358-384), where the assignment of
  fixes by class is.
- Q3: the fix takes in only the Minor findings that the report of the review of the whole change
  lists and has not marked outside the task's scope. A Minor finding of a slice review that the
  whole-change reviewer does not repeat stays unfixed in the request's list, as today.
- Q4: a reverted fix's new Critical or Important finding stands in the request's *Minor findings*
  list beside the Minor findings the fix tried, marked with its grade and as found by the review of
  the reverted fix, with the reviewer's words and its place in the code; WAY-289 judges it for
  *For you to decide* like any unfixed finding. No new heading in the description, and
  `task-cycle/request_check.py` is not changed.

**Files to expect to change (a search will tell you more; each file you change, you read whole
first):**

- `foundations/decisions.md`: WAY-161 (the Minor-only fix is no longer a violation; Rationale and
  *Rejected* to reflect answer 1 and its *Not chosen* A, C, D as the task gives them), WAY-162 (the
  revert for a Minor-only fix and no third round; its *Verification*, *Rationale*, *Rejected* from
  answer 2 and its *Not chosen* a, c), WAY-289 (the two-answer question from answer 3 and its *Not
  chosen* a, c; *Verification*). Edit in place; the decisions keep their identifiers. Check WAY-163,
  WAY-287, WAY-229 and WAY-136 for lines your edits make untrue, and fix them in the same change.
  The settlement rows say the meaning is the human's; the wording of the *Rejected* is yours.
- `task-cycle/skill/SKILL.md`: "The end of a code review" (the pass with Minor findings, the Minor-only
  fix, its review, the revert), step 9 and step 12 where they speak of Minor findings, the sentence
  at the end of "The end of a code review" about where Minor findings go, and "Correction after
  review".
- `task-cycle/skill/request_template.md`: item 8 of *For you to decide*, the *Minor findings* and
  *Findings outside the task's scope* paragraphs, the variants table row for a correction, and any
  other line your search finds.
- `task-cycle/skill/correction.md` (Q1).
- `task-cycle/change/fix.md` (the findings file now holds in-scope Minor findings too, after the
  blocking ones; Minor findings are yours to fix when they are in the findings file) and
  `task-cycle/review/fix.md` (its findings file likewise; a Minor finding that remains after the fix
  does not block; only a new or remaining Critical or Important does). Check
  `task-cycle/review/SKILL.md` and `task-cycle/review/whole_change.md` for lines that need to
  change (for example, how the whole-change review lists its findings so the findings file can be
  cut from them).
- `agent-instructions/README.md`: it describes the hand-made change to the-way outside a cycle. Keep
  its route unless the cycle's change makes a line untrue; say in your report what you left alone and
  why.
- Tests: change a test only where it checks text you change; add none for prose (the rule "Test
  behaviour, not text" of the method). `task-cycle/test_request_check.py` quotes WAY-162 and
  `task-cycle/request_check.py` fixes the headings: run both focused (`python -B gate/run_tests.py
  task-cycle`).

**Foundation to read by identifier** (each whole, `###` heading to the next heading): decisions
WAY-161, WAY-162, WAY-163, WAY-287, WAY-289, WAY-229, WAY-136, WAY-148, WAY-135. Part map entries of
`decisions`, `task-cycle`, `agent-instructions`. Invariants whose *Part* names one of them or
`every`, and the glossary entries of the words you use. The foundation step's search of the whole
foundation (WAY-33) is yours: look for every other line that says Minor findings are never fixed, or
that a fix runs for blocking findings only, in `foundations/`, `task-cycle/`, `elements/`,
`project-level/`, `agent-instructions/`, `installation/` and `product-guidelines/`, and correct it.

**Rules.** English for code, comments, commit messages (the repository's existing style: `docs:`,
`feat:` prefixes; look at `git log --oneline -10`). Commit with `git add <paths>` and
`git commit`, never `git add -A`; several commits are fine (decisions; cycle documents). Wrap prose
at 100 characters as the existing files do. Write plain language; no new jargon. Do not touch
`.runs/`. Do not dispatch subagents.

**Report.** `C:\Storage\repos\the-way\.runs\worktrees\fix-minor-findings\.runs\task-cycles\fix-minor-findings\reports\01-author.md`,
as `task-cycle/change/SKILL.md` section 6 gives, with: for each entry written, one sentence of its
meaning in English and one in Polish (the task document's language), marked `row <n>` or `the
cycle's`; the own-work check; **Searches not found or unclear**; every choice with the way rejected
and its cost if wrong; what you left alone and why. Return to me only the status, the commits, a
one-line check result and the report path.
