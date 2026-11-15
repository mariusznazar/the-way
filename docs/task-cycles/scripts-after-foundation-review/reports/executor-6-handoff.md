# Handoff — executor of slice 6, task `scripts-after-foundation-review`

You are the executor of one slice of a plan in a task cycle of the-way (`implement-task`). The
person who requested the cycle has delegated intermediate choices to the orchestrator; nothing here
is the human's approval. Ask no human. A question you cannot settle from the files named here
returns with the status `questions`; a fact or permission no source gives returns `blocked`.

## Where and what you make

- Worktree (work from its root, never from another checkout): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. The-way is the checkout you work in; it is no product's `.the-way`. Target branch `foundations`; base of the task `7f5c5a56f67d9ff40554240594ca0bde59773cb3`. The foundation entries of the plan are already written on the branch (commits `da9d816` and `bfb774c`); read an entry as they left it.
- Method, read whole: `task-cycle/change/SKILL.md` (`make-change`); variant: **a slice, or the retry of a slice**. You read `task-cycle/change/slice.md` when its step comes, and each other file the method names only when the step or variant that names it comes. You have no skill tool: a skill a method names by its name alone is the `SKILL.md` whose frontmatter `name:` is that name, read as a file.
- Your stage and its boundary: make slice 6 of the plan and nothing else, commit it on the task branch (in English messages, files added by path, never `git add -A`, nothing under `.runs/`), and return before review. You run **no run of the whole gate** (WAY-160); you run the focused checks of the slice's *Checks*.
- Frozen task: `.runs/task-cycles/scripts-after-foundation-review/task.md`. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md`. Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` — your slice is copied below; read the other parts of these files only as your slice's *Read* names them.
- Answers of step 4: trust boundary **yes** — a slice whose *Risk* names a trust boundary changes a script that takes in untrusted data (a transcript, a register, a locations file, a copy of a record from git history, a price list): write the reading so that crafted input cannot make the script crash with a stack trace, write outside its places, run a command or put text of the input into a result unescaped; the review of the slice is told to check that. Irreversible operation: none.
- Your class of model: **same (the orchestrator's class)**.
- Directory for your working copies: `.runs/executor-6/` of the worktree.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/executor-6-report.md`, in the form `make-change` gives; with the **Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`), the own-work check, each check you ran with its command and exit code, the choices you made and the foundation entries or code you reached beyond what is named (what, where and why), and the working copies line.
- The tests of the slice are written first and fail on the base for the reason the slice gives; where the slice says a test is red on the base, the report states its failing run and its passing run.
- A change of a test that holds a sentence of a decision by a line `decision:` or an invariant's test is named in your report (WAY-03), so that the request names it.
- Another task changes `elements/common/foundation_check.py` and the sentence of WAY-344 in parallel; leave what is not in your slice alone.

## Your slice, copied from the plan word for word

### Slice 6 — Two kinds of series: the cost and the count of remarks

- **Goal:** in `process-audit/audit_count.py`, the grouping of the versions of the process into series gives two kinds, and each comparison stays inside its own kind. A series of the cost ends at a change of the price list or of the script that measures the cost, `task-cycle/cycle_stages.py` (and of no other script: the spec's D5), between two versions, and nowhere else; the median cost and the answer Q3 are compared inside it. A series of the count of remarks ends wherever a series of the cost ends, and also at a date of *Added* or *Withdrawn* of the register's list of classes, at a change of the form of a stage report, of the list of classes or of the instructions of the reviewer, that is, of the files of the-way under `task-cycle/change`, `task-cycle/plan`, `task-cycle/review` and `task-cycle/spec`, and of `task-cycle/agent-types/the-way-stage.md`, whose text the reviewer receives as its instruction (the list of the module description, the paragraph "the tree of the-way under `task-cycle/change`, …"); the answers Q1 and Q2 are compared inside it. `git diff --quiet` as now, a failure counting as changed. The section *Process versions* and its description say, per series, why it begins where it does, and no cell sets a number of one kind of series beside a number of the other; the description of the module, the sentences that call the test "deliberately conservative", the text of the section and the reasons of a series are rewritten to this rule. The module description and the result keep `Q1`, `Q2` and `Q3` and the section *Measure versions* as they are. The new tests start from: a change of `task-cycle/agent-types/the-way-stage.md` starts a series of the count and none of the cost; a change of a file under `task-cycle/review` starts a series of the count and none of the cost; a change of `task-cycle/cycle_stages.py` starts both; a new price list starts both.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/task.md:32-33` To do 5 and 6 · `.runs/task-cycles/scripts-after-foundation-review/task.md:59-64` Questions to settle 2 · `.runs/task-cycles/scripts-after-foundation-review/task.md:133-133` Decisions in play, WAY-339 · `.runs/task-cycles/scripts-after-foundation-review/task.md:145-145` Settlements to record, row 3 · `.runs/task-cycles/scripts-after-foundation-review/spec.md:341-346` D5, the split of the series · `foundations/decisions.md:7384-7469` WAY-339 · `foundations/invariants.md:398-407` audit-series-script-paths · `foundations/invariants.md:116-145` script-language, script-imports, script-subprocesses · `foundations/part_map.md:124-134` process-audit
- **Model:** same — the grouping, its description and its tests change together, and the rule must hold for every comparison of the section
- **Risk:** trust boundary — `process-audit/audit_count.py`
- **Checks:** start from the tests of class `ProcessVersions` and of class `PriceBoundary` named above, red on the base; `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k ProcessVersions -k PriceBoundary -k MeasureVersions`; then `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` and `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"` (the invariant `audit-series-script-paths` holds)
- **Depends on:** Slice 5


## The foundation entries of your *Read* as they stand now

The ranges the plan names are those of the base. Where they differ from the plan's, these hold; find a passage of the plan or a range of code by its heading or name where an earlier slice changed its file.

- `foundations/decisions.md:7432-7585` WAY-339
- `foundations/invariants.md:398-407` audit-series-script-paths
- `foundations/invariants.md:116-125` script-language
- `foundations/invariants.md:126-135` script-imports
- `foundations/invariants.md:136-145` script-subprocesses
- `foundations/part_map.md:124-135` process-audit

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
