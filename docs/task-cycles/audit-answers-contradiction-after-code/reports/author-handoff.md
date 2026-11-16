# Handoff to the one author — the audit answers whether a contradiction came out after the code

## Delegation

The person who requested this cycle (Mariusz, the-way's author) has delegated every intermediate
choice to the orchestrator. Do not ask the human anything. A question goes to the orchestrator in
your report as `questions`; where the task, the foundation and the code leave a choice of how to make
the change open, make the smallest reversible choice that fulfils the task, and name it in your
report. Never widen the task.

## Where you work

- The worktree: `the root of the task's worktree` — the root of
  the-way for this change, on the branch `task/audit-answers-contradiction-after-code`, base
  `aba5ee92a0734c2e775cc69662af669bf6455795`. Work from its root. Read nothing from another checkout
  of the-way. Commit on this branch only, naming files by path (`git add <path>`, never `git add -A`
  or `.`), with commit messages in English.
- Your directory for working copies is `.runs/author/` of the worktree.
- Your report: `.runs/task-cycles/audit-answers-contradiction-after-code/reports/author-report.md`.

## Method and stage

- The method: `task-cycle/change/SKILL.md` (`make-change`). Your variant, in the words of its row:
  "the whole change as the one author". Read that `SKILL.md` whole, and a file it names, one beside it
  included, only when the step or variant that names the file comes.
- Your stage: the whole change as the one author — the foundation step with the code. The foundation
  step is `task-cycle/skill/foundation_step.md`: read it whole, and the `SKILL.md` of an element, at
  the path it gives, when you write an entry of that element. Return before review: the return step
  is a later stage, for which you will be resumed.
- Your class: `same` as the orchestrator's. Your report states the own-work check and its commands.

## The task

The frozen task is `.runs/task-cycles/audit-answers-contradiction-after-code/task.md` — read it
whole. It requires: the six items of *To do*, the answers of *Questions to settle* as it states them
(1 to 5), and the four rows of *Settlements to record*: rows 1, 2 and 4 are entries of the foundation
(rows 1 and 4 as decisions of the log, row 2 as a sentence of WAY-337), row 3 is the code of
`process-audit/audit_count.py` and goes to no entry. Nothing in *Out of scope*, *Human actions* or
*Questions carried to cycle* places work on you beyond that.

## The answers of the two questions at start

- Trust boundary: **yes**. `process-audit/audit_count.py` is the trust boundary of the part
  `process-audit` in `foundations/part_map.md`; it reads files of cycle records from git history,
  which are untrusted input. Your change makes it read two forms it does not read today (a
  marker in *Discarded attempt* and an entry of *Review rounds* opened with `review`). A record text
  crafted to look like a marker or an entry must not produce a wrong `yes` or `no`, a hang or an
  unbounded result; the reviewers check this.
- Irreversible operation: **no**.

## Route and known facts that bear on the change

- Open design choice: none. Reserved choice: none. Route: one author without a plan.
- **Size (WAY-365, WAY-385).** `process-audit/audit_count.py` has 3310 lines against the threshold
  of 1000 for a file of a script, and the invariant `function-and-file-size` is marked violated. You
  add to it, so **the first commit that changes the code moves a part of that file out into a module
  of its own with no change of behaviour**, with the tests that cover it as its check; name that
  choice among those your report lists, with the reason for the part you moved. The commit after it
  adds the change. Choose the part by what the change touches (the reading of the record's items
  `Discarded attempt` and `Review rounds`, near `review_rounds` and `read_contradiction`) and keep
  every name the tests and other scripts import working, or correct each importer in the same
  commit. A function you write or change stays at most 80 lines.
- **Series (WAY-339).** A change to a file under `task-cycle/review` starts a new series of the count
  of remarks; a change to `task-cycle/record_template.md`, to the files in `task-cycle/skill/` and
  to `process-audit/audit_count.py` does not (`TREE_PATHS` in `audit_count.py`). Do not change
  `TREE_PATHS` unless the task's text requires it.
- **A missing field (WAY-344).** `audit_count.py` is the command that counts the audit: where you
  rework the reading of a file in it, the whole reading of that file follows WAY-344 as its sentence
  states for that command; each reading you rework has one test that gives the file without a field
  it needs and asserts the failure that names it, unless WAY-344 gives the field as no missing field.
- The cycle records of the-way in git history hold the forms the count has to read: older records
  have `Review rounds` entries opened with `findings` and `Discarded attempt: none`; do not
  rewrite any of them.

## What you read

The foundation entries, by identifier — read each whole, selected as "Reading the foundation" in
`elements/common/way_of_working.md` gives for the parts `task-cycle` and `process-audit`; run
`elements/common/decision_index.py` with its output in your directory for working copies:

- the decisions of the task's *Decisions in play*: WAY-337, WAY-339, WAY-135, WAY-263;
- the decisions the orchestrator found to bear on the work: WAY-344, WAY-365, WAY-385, WAY-161,
  WAY-162, WAY-229, WAY-260, WAY-294, and the section "Process audit" of the decision log;
- the invariants whose *Part* names `task-cycle` or `process-audit`, and `function-and-file-size`;
- the glossary entries of the terms you use.

The guidelines, each whole: `guidelines/coding.md`, `guidelines/coding-measuring-report.md`
(`audit_count.py` counts figures from a history and writes a report), `guidelines/testing.md`.

The files the task names, whole where you change them: `task-cycle/review/SKILL.md` (section
"3. Grade"), `task-cycle/skill/SKILL.md` (the paragraph that opens "For a fix, it gives the findings
file" and the two paragraphs that open "An agent that meets an open design choice while it makes the
change" and "A one-author change that proves too large"), `task-cycle/skill/reserved_return.md`
(section "Discard the attempt"), `task-cycle/record_template.md` (the items *Discarded attempt* and
*Review rounds*), `process-audit/audit_count.py` (the functions `review_rounds`,
`read_contradiction`, `phrase_starts`, `denied_before` and what they use), `process-audit/test_audit_count.py`,
and `process-audit/SKILL.md` where it states Q1. Where another file of `task-cycle/` or
`process-audit/` states the form of *Discarded attempt* or *Review rounds*, or what Q1 reads, search
the repository once and correct it in the same change (WAY-33).

## Working copies

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

## Checks

- Run the focused checks of the directories you change — `python -B gate/run_tests.py process-audit`,
  `python -B gate/run_tests.py task-cycle`, and the directory of any other file you change — and
  `python -B elements/common/foundation_check.py` for the foundation entries; the test of
  `ruff` and the size test run in the directory `agent-instructions`.
- **Do not run the product's full gate** (`python -B gate/run_tests.py` with no directory): its run is
  the orchestrator's (WAY-160), and the day advisor must signal before each full run. Where a test of
  another directory may break by your change, run that directory.
- Your own-work check, as `make-change` gives it, is part of the report.

## The report

Write the full report to the path above, as `make-change` gives it. Return: its status, the commits,
a one-line check result naming what failed or did not run, and the report's path. The report holds
your questions and concerns, each reach beyond this handoff, **Unread material** (what this handoff
names that stayed unread or was read in part, or `none`) and **Searches not found or unclear** (each
thing you looked for and did not find or found unclear, or `none`). Each foundation entry you write
is marked `row <n>`, `projected` or `the cycle's` with its two sentences of meaning, as
`task-cycle/skill/foundation_step.md` gives.
