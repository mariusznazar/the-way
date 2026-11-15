# Handoff: planner, task `decision-log-reading-index`

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator, which
answers your questions from the task, its sources, the foundation and the code; no answer is the
human's approval. You never ask the human. The cycle has one human contact, the request.

## Where you work

- Worktree (your working directory): `the task's worktree`, branch
  `task/decision-log-reading-index`, base `21ecb627f885de438e2209d7ff5c137b1e1b9d83` (target branch
  `foundations`). You write no code, no test and no foundation entry, and make no commit.
- Method of your stage: `task-cycle/plan/SKILL.md` of this worktree (`plan-task`). Read it whole; read
  a file it names only when its step or variant comes. The script `task-cycle/slice_size.py` is there.
- Variant: you write the plan of the whole change from a frozen task, with no spec and no earlier plan.
- Boundary: you write `plan.md` and its size report `plan-size.md` in
  `.runs/task-cycles/decision-log-reading-index/`, your report to
  `.runs/task-cycles/decision-log-reading-index/reports/planner-report.md`, and return. You start no slice.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed.
The files that a product's own tools and tests make by themselves are no working copy of the agent
and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a
worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside
its report what the report needs, and states in the report where each copy stood and that it was
removed. Where a removal fails, the agent finishes all the same and names in the report the
remainder, with its full path and the reason it stayed.

Your directory for working copies: `.runs/planner/`.

## The frozen task

`.runs/task-cycles/decision-log-reading-index/task.md` — read it whole. It is `Status: ready for
cycle`, `Project relation: independent`, accepted 2026-11-14. Its *To do* 1–8, its *Acceptance
criteria*, its answered questions 0–4, its *Questions carried to cycle*, its *Decisions in play* and
the 7 rows of its *Settlements to record* are the whole change. The task is in Polish; the plan and
the foundation entries are in English, as the repository's are.

## Answers of step 4

- Trust boundary: **yes**. The part map names `task-cycle/cycle_measures.py` (with `cycle_stages.py`
  and `gate_times.py`) as a trust boundary of the part `task-cycle`: it reads session transcripts from
  outside the repository. *To do* 8 extends it, so the slice that changes it is marked with that risk
  and gets a review of its own aimed at crafted transcript input.
- Irreversible operation: **no**.
- Open design choice at start: none; no reserved choice. The orchestrator judged that the change needs
  division, for this reason: it spans a new script with
  tests, the division of the 331-entry decision log into sections with a comparison script and the
  consumers of the log's form, the reading rule and five decisions and the review, report and
  request-template wording, and an extension of the measuring script with tests.
- Where you find an open design choice or a reserved choice the task does not settle, write no plan and
  return a report of it, as your method gives.

## What you read

Foundation entries by identifier (read each whole, in `foundations/decisions.md`, found by its heading
`### WAY-NN`):

- the task's *Decisions in play*: WAY-150, WAY-18, WAY-21, WAY-326, WAY-347, WAY-05, WAY-12, WAY-02,
  WAY-52, WAY-33;
- the cycle's own rules for the plan: WAY-135, WAY-136, WAY-229, WAY-160, WAY-243, WAY-161, WAY-162;
- the parts the change touches are `decisions`, `elements-common` and `task-cycle` (and perhaps
  `gate`, `installation` or `process-audit` where a script, a test directory or a consumer of the log
  moves): read the part map's entries of those parts (`foundations/part_map.md`) and, by the method
  "Reading the foundation" in `elements/common/way_of_working.md` (read it), the decisions whose
  *Scope* names them and the invariants whose *Part* names them or `every` — you may select by the
  search that method gives; the log is large, so read whole what bears on your cut, not the whole log.

The-way has no guideline files of its own (no coding, testing or styleguide file of a product); read
`product-guidelines/reading.md` only if your method sends you there.

Code and tests to read to cut slices, as far as needed: `elements/common/foundation_check.py` and its
test, `elements/common/migrate_foundation.py`, `elements/common/way_of_working.md`,
`elements/decisions/template.md`, the skill under `elements/decisions/skill/`, `task-cycle/cycle_measures.py`
and `task-cycle/test_cycle_measures.py`, `task-cycle/review/SKILL.md`, `task-cycle/skill/SKILL.md`,
`task-cycle/skill/request_template.md`, `installation/install.py` and its tests where they name the log.

## The orchestrator's own reading, for your check (hints, not binding — verify each)

- In `foundations/decisions.md` an entry starts at `### WAY-NN — …`, and the file opens with
  `# Decision log` and a short paragraph. A section heading `## …` placed in it will, as the code stands,
  be taken by `blocks(lines, "### ")` in `elements/common/foundation_check.py` as part of the body of
  the entry before it; "Reading the foundation" step 2 also gives an entry's range as ending at "the
  next heading (`###` in the decision log, `##` in the other foundation files)". Which scripts, tests,
  skills and rules take the log's form — the checker, `migrate_foundation.py`, `installation/install.py`,
  the part map's and the template's descriptions — is for you to find and to assign to slices.
- The task says the sections get "numbers unchanged, content of each entry byte for byte the same,
  confirmed by a script comparing the entries before the division and after", and that the cycle proposes
  the list of 20–30 sections and the assignment of entries; Mariusz accepts the list at the merge. Decide
  in the plan which slice makes the assignment, and that the assignment is read off the entries' own
  *Scope* and questions, not guessed.
- *Questions carried to cycle*: (a) how the measuring script recognises that a tool call brought the log or
  an index into an agent's context; (b) where the cycle finds the sessions of the last game cycle and the
  last the-way cycle for the "before" measure. Settle (a) in the slice that writes the script (say how
  precisely, and what stays approximate); (b) is the orchestrator's — name in the plan what the "before"
  step needs from it and make no slice that runs it.
- The index script has to work on the log of any product, with a product's pinned the-way copy, with and
  without sections.
- `task-cycle/cycle_measures.py` starts a new series of measures in the audit of the process
  (`process-audit/SKILL.md`, "Measures are compared inside a series only"): find what, if anything, the
  change must record there.

## Foundation entries

The task's rows 1–7 of *Settlements to record* go to sentences of WAY-150, WAY-18 and WAY-347
through the skill `record-decision` (`elements/decisions/skill/`; read as a file). Per `plan-task`, list
them under *Foundation entries*, written before any slice; say where the reading rule, the template and
the other files that restate the rules are edited and by which slice.

## Report

Write the full report to `.runs/task-cycles/decision-log-reading-index/reports/planner-report.md` as
your method gives, and return its status, its commits (none), its one-line check result, its questions
and concerns, your **Unread material**, your **Searches not found or unclear** and the report's path.
