# Handoff — the agent of the plan's *Foundation entries*

The person who requested this cycle has delegated intermediate choices to the orchestrator; every
answer below is the orchestrator's, never that person's approval. You write foundation entries of
the-way on the task branch and commit them. You write no code and no test, and you do not run the
product's gate.

## Where you work

- Worktree (work from its root): `the root of the worktree`,
  branch `task/the-way-coding-and-testing-guidelines`. Base of your range (also slice 1's base):
  `2d593214e4ce11676880b1f3ac3aa75884e023ab`. This is the-way itself; no `.the-way`, no pin.
- Your stage: the foundation step of the plan — "the agent of the plan's *Foundation entries*" of
  `task-cycle/skill/foundation_step.md`. Read that file whole, and read `task-cycle/change/SKILL.md`
  (`make-change`) whole for reading, the own-work check, commits and the report; of the files it
  names, only when the step that names them comes. Neither of the two tells you to run the gate.
  A skill that a method names by its name alone is the `SKILL.md` whose frontmatter `name:` is that
  name; you have no skill tool, so read it as a file.
- Your directory for working copies: `.runs/foundation-entries/`.
- Your full report: `.runs/task-cycles/the-way-coding-and-testing-guidelines/reports/entries-report.md`.

## Working copies (word for word from the orchestrator's skill)

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

## What you write

Entries **E1 to E38** of the table *Foundation entries* in
`.runs/task-cycles/the-way-coding-and-testing-guidelines/plan.md` (lines 14–65; read the table and the
*Choices* at its end, and the orchestrator's additions at the very end). **Not** E39 and E40: slices
1 and 18 write those part-map lines with the files they add. The frozen task is
`.runs/task-cycles/the-way-coding-and-testing-guidelines/task.md`; read it whole. Each row of its
*Settlements to record* named in the plan's table is yours, written whole in the place its column
*Goes to* names, by the `SKILL.md` of its element (`elements/decisions/skill/SKILL.md`,
`elements/invariants/skill/SKILL.md`, `elements/glossary/skill/SKILL.md`,
`elements/environment-facts/skill/SKILL.md`), its meaning the row's and its wording yours (WAY-134).
Rows 16 and 17 go to the guidelines (slice 21) and rows 5, 24 to code or guidelines: write no entry
for them. The identifiers in the plan's table are proposals; take the identifier each element's
rules give, and return the identifier of every entry in your report, one table row per entry
(`E<n>`, kind, identifier, the row of *Settlements to record*, the sentence of its meaning in English
and one in Polish, and the mark `row <n>`, `projected` or `the cycle's`).

Orchestrator's answers that bind your writing (recorded as autonomous choices):

- **Eleven parts, not ten.** `product-guidelines` holds a Python file (`test_skill_references.py`) at
  the base, so the parts the linter and the size rule read are the eleven parts with Python code:
  `elements-common`, `part-map`, `relation-model`, `project-level`, `task-cycle`, `gate`,
  `agent-instructions`, `instruction-files`, `installation`, `process-audit` and
  `product-guidelines`. Wherever a row says "ten parts" the entry names these eleven, and the
  *Scope*/*Part* of E2, E7, E22, E23 follows. Note this change of the row's count in your report.
- Row 6 and row 15 (`ruff-blocking-rules` and the size invariant) enter with `Violated: yes` as the
  rows say (WAY-51); the tests they cite are written by slices 16 and 17 — where an invariant's
  *Verification* has to name a test file that does not exist yet, name the file the plan gives
  (`agent-instructions/test_linter_invariant.py`, `agent-instructions/test_size_invariant.py`) and
  run the foundation check with `--skip-test-citations`, as the plan says; the six refusal invariants
  (E28–E33) cite existing tests and slices 2, 4, 5, 6, 8 and 11 add the lines `# invariant: …` to
  them — the same switch applies.
- The four kind-rule invariants (E24–E27, row 19) cite tests written by slices 12–15; same switch.
- E17 withdraws WAY-328; E16 changes WAY-09; E18 and E19 correct the three places that name WAY-328
  (the sentence of the *Rationale* and the item of the *Rejected* of WAY-344, and the example in the
  *Verification* of WAY-363); no other place of the foundation names it (the planner searched). After
  these edits search the whole foundation once for the entries your entries touch and correct them
  in the same change (WAY-33); no second search follows.
- Row 14 and E7: the rule of size counts a function with its nested functions and a file of a script
  by lines, thresholds 80 and 1000, tests outside, no exceptions.
- The three glossary terms `files`, `git` and `repository` for the levels of tests (E34–E36): form by
  `elements/glossary/skill/SKILL.md`; take the words of rows 21–23.

## What to read (the orchestrator's selection, WAY-150)

- The `SKILL.md`, `template.md` and examples of each element you write, and
  `elements/common/rules.md`, `elements/common/way_of_working.md` (the method of reading; the
  selection below is the orchestrator's, so you need not repeat it).
- Decisions, by identifier, whole with *Rationale* and *Rejected* for those you change or withdraw
  (WAY-328, WAY-09, WAY-38, WAY-344, WAY-363) and for those you write beside (WAY-167, WAY-168,
  WAY-172, WAY-173, WAY-198, WAY-199, WAY-202, WAY-203, WAY-204, WAY-205, WAY-206, WAY-212, WAY-231,
  WAY-232, WAY-235, WAY-240–WAY-242, WAY-247, WAY-252, WAY-253, WAY-360, WAY-361, WAY-365); the
  orchestrator's index is `.runs/task-cycles/the-way-coding-and-testing-guidelines/decision_index_orchestrator.md`
  (51 decisions in full, 133 by heading), `elements/common/decision_index.py` writes your own.
- `foundations/part_map.md`, `foundations/glossary.md`, `foundations/invariants.md` (the invariants
  of the parts touched and `script-subprocesses`, `test-method-citation`, `installation-paths-through-links`
  as the form of a boundary invariant), `foundations/environment_facts.md`.
- `product-guidelines/coding/template.md` and `product-guidelines/testing/template.md`: what the
  guidelines of slices 21 and 22 will carry; read them for the sentences your decisions and
  invariants must make true (the sections "Departing from the rules on failures and logs", "The
  tools of the standing checks", "Writing the files" of the coding template).
- No guidelines of the-way exist yet.

## Checks

`python -B elements/common/foundation_check.py --skip-test-citations` exits 0 on your range, and
`python -B elements/common/foundation_check.py` named only for the citations (it may fail on the
tests not yet written: report which). Commit by path (`git add <path>…`, never `-A`), messages in
English, as the repository's history does. The product's gate is not yours (WAY-160).

## What you return

Status, your commits, a one-line check result with command and exit code, the report path, your
questions and concerns, **Unread material** and **Searches not found or unclear** (`none` is an
answer; a missing section is returned to you for repair), the working-copies line, and the table of
identifiers. A question for the human only where `foundation_step.md` allows it.
