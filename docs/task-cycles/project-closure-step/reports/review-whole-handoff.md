# Handoff — review of the whole change (task `project-closure-step`)

## Who and what

You are a fresh reviewer of the strongest class, and you made none of this change. Review the whole
change of one task cycle of the-way with `review-change`. The orchestrator of the cycle dispatches you;
questions go to it, never to the human. Your review is read-only: you change no file of the worktree,
and you commit nothing.

- Worktree: `the task's worktree`, branch `task/project-closure-step`. Work
  from its root. The-way is its own process: every path below is a path in this worktree.
- Method: `task-cycle/review/SKILL.md` (`review-change`), the review of the whole change. Read that file
  whole, and `task-cycle/review/whole_change.md` as it tells you; read any other file it names only when
  the step that names it comes.
- Range: base `cb5feab98c697354ae79a8f559b950fbf10d0030`, head `ee85f143` (confirm with
  `git rev-parse HEAD`; compute the diff yourself with `git diff <base>..<head>` and
  `git log <base>..<head>`).
- Your directory for working copies: `.runs/review-whole/`.
- Your report: `.runs/task-cycles/project-closure-step/reports/review-whole-report.md`; its first line
  is `PASS <sha>` or `FAIL <sha>` as `review-change` gives it.
- `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and
  findings — are not yours to read, except the two this handoff names below.

## Working copies (word for word from the cycle's skill)

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed,
except a screenshot that is shown to the human: that one goes where `task-cycle/change/ui_check.md`
says, to the place the product's foundation settles for screenshots, and into the agent's directory
only where no such place is settled. The files that a product's own tools and tests make by
themselves are no working copy of the agent and stay outside this rule. Before the agent returns,
each time it returns, it removes its copy — a worktree with `git worktree remove --force`, then
`git worktree prune` — keeps in `reports/` beside its report what the report needs, and states in
the report where each copy stood and that it was removed. Where a removal fails, the agent finishes
all the same and names in the report the remainder, with its full path and the reason it stayed.

## What the change is for

- The frozen task, to read whole: `.runs/task-cycles/project-closure-step/task.md` (Polish). Its
  *To do* items 1–7 are the change; *Settlements to record* rows 1–6 are the foundation entries the
  change carries; *Decisions in play* and *Out of scope* bound it. Its `Project relation:` is
  `independent`: no project plan, no projected entry. There is no spec and no plan: the route is one
  author without a plan, so there are no slices and no slice reviews; you judge the whole change.
- The author's report, a set of claims to verify, not evidence:
  `.runs/task-cycles/project-closure-step/reports/author-report.md`. Its checks, choices and concerns are
  yours to test.
- Check the coverage of every *To do* item and every row of *Settlements to record* against the diff
  (the row 4 goes to an invariant; rows 1, 2, 3, 5, 6 to decisions), and the source fidelity of the
  foundation entries against the row and the task passages that the author's report quotes. Note what
  the entries add that no row gives; the author marked those `the cycle's`.

## Answers of step 4 you review under

- Trust boundary: **yes**. `project-level/plan_check.py` and `project-level/plan_state.py` are trust
  boundary files of the part `project-level` and the change touches both. Check crafted input at that
  boundary yourself — a `Status:` line with a malformed date, a closed plan with a row in another state, a
  `done — goal delivered in task <n>` row pointing at a dropped task, a doubled `Status:` line, trailing
  spaces and non-ASCII digits, CRLF — and report what you ran.
- Irreversible operation: **no**. The step the skill describes writes into the human's notes only after
  the human accepts a preview; check that the step's file cannot be read as writing before the acceptance.
- Checks failing on the base: none (the base is a merge commit with the tree of its second parent; the
  merged request's CI passed).
- The change does not move the pin; it is not a plan member.

## Choices and points the orchestrator wants checked

These are the author's claims and the orchestrator's choices; test each, do not accept them.

1. The orchestrator's autonomous choice Q1, which the author carried out in `ee85f143`: a projected entry
   of the plan goes with a withdrawn task where its `Written by` cell names that task, also where a
   finished task realizes part of it, and also with the withdrawn tasks of `Realized by` where every
   task of that cell is withdrawn and `Written by` names no withdrawn task. Judge against the task's
   *To do* 3 and *Questions to settle* item F, whether the section reads that way and whether another
   reading of the task's words would be required.
2. WAY-415 records that it `narrows WAY-154` and states which writes prevail (the first document of a
   withdrawn task and the line it lacks). The author marked WAY-411 to WAY-415 `the cycle's` for the
   pairs of examples and the paragraph of precedence; judge whether the precedence is warranted by what the
   human accepted in the task and whether any other decision collides (WAY-140, WAY-153, WAY-145,
   WAY-269 are named in the author's search).
3. The author added a finding to `plan_check.py` that the task does not ask for: a second `Status:` line is a
   `form` finding. Judge whether it belongs to the task, breaks any earlier plan that passed the check, or
   disagrees with `plan_state.py`.
4. `plan_state.py` on a closed plan: exit 0, one line `closed: …`, no Git observation. Check the task's
   *To do* 5 and WAY-153 against it.
5. The word: the author calls the item the closing adds to the plan's change log a "closing item", where the
   task says "wpis zamknięcia" ("entry"), since the glossary gives "entry" the foundation's meaning. Judge
   the wording of the step's file, the template and the entries against the glossary.
6. The new step's file `project-level/lead/skill/closure.md` and the lead skill's pointer to it against
   WAY-256 and WAY-265, and against the whole of *To do* 1–7 (the condition of start, the three places,
   what travels with the task, the content of the closing item, the status, the preview before any
   write and the acceptance, the definition left as it is). Read the file as an agent would at the
   moment the step comes: could it follow it without guessing?
7. Size and form: WAY-385 thresholds and the formatter and linter invariants on the changed scripts
   (the author ran Ruff outside the gate; the `agent-instructions` directory's tests hold the standing
   rules).

## Reading

Select your own foundation and guidelines as `review-change` gives for the whole change: the touched
parts are `project-level` (scripts, skill files, template), the decisions and invariants files and the part
map (foundation). The orchestrator's pointers, to start from and not to bound you: the decisions of the
task's *Decisions in play* (WAY-142, WAY-145, WAY-146, WAY-118, WAY-153, WAY-107), WAY-126, WAY-134,
WAY-154, WAY-256, WAY-265, WAY-385, WAY-379, WAY-382, the new WAY-411 to WAY-415; the invariants
`project-plan-form`, `project-plan-check`, `project-plan-state-evidence`, `skill-entry-points`; the
guidelines `guidelines/coding.md`, `guidelines/coding-check.md`, `guidelines/coding-measuring-report.md`,
`guidelines/testing.md`.

Do not run the product's full gate (`python -B gate/run_tests.py` with no directory): its run is the
orchestrator's or CI's. You may run the tests of one directory
(`python -B gate/run_tests.py project-level`) and the foundation check
(`python -B elements/common/foundation_check.py`); report each with its command and exit code.

Name in your report each reach beyond this handoff and your own selection, your **Unread material** and
your **Searches not found or unclear**, as `review-change` gives.
