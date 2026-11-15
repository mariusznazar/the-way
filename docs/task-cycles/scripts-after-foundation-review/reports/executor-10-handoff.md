# Handoff — executor of slice 10, task `scripts-after-foundation-review`

You are the executor of one slice of a plan in a task cycle of the-way (`implement-task`). The
person who requested the cycle has delegated intermediate choices to the orchestrator; nothing here
is the human's approval. Ask no human. A question you cannot settle from the files named here
returns with the status `questions`; a fact or permission no source gives returns `blocked`.

## Where and what you make

- Worktree (work from its root, never from another checkout): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. The-way is the checkout you work in; it is no product's `.the-way`. Target branch `foundations`; base of the task `7f5c5a56f67d9ff40554240594ca0bde59773cb3`. The foundation entries of the plan are already written on the branch (commits `da9d816` and `bfb774c`); read an entry as they left it.
- Method, read whole: `task-cycle/change/SKILL.md` (`make-change`); variant: **a slice, or the retry of a slice**. You read `task-cycle/change/slice.md` when its step comes, and each other file the method names only when the step or variant that names it comes. You have no skill tool: a skill a method names by its name alone is the `SKILL.md` whose frontmatter `name:` is that name, read as a file.
- Your stage and its boundary: make slice 10 of the plan and nothing else, commit it on the task branch (in English messages, files added by path, never `git add -A`, nothing under `.runs/`), and return before review. You run **no run of the whole gate** (WAY-160); you run the focused checks of the slice's *Checks*.
- Frozen task: `.runs/task-cycles/scripts-after-foundation-review/task.md`. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md`. Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` — your slice is copied below; read the other parts of these files only as your slice's *Read* names them.
- Answers of step 4: trust boundary **yes** — a slice whose *Risk* names a trust boundary changes a script that takes in untrusted data (a transcript, a register, a locations file, a copy of a record from git history, a price list): write the reading so that crafted input cannot make the script crash with a stack trace, write outside its places, run a command or put text of the input into a result unescaped; the review of the slice is told to check that. Irreversible operation: none.
- Your class of model: **cheaper (a model cheaper than the orchestrator's)**.
- Directory for your working copies: `.runs/executor-10/` of the worktree.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/executor-10-report.md`, in the form `make-change` gives; with the **Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`), the own-work check, each check you ran with its command and exit code, the choices you made and the foundation entries or code you reached beyond what is named (what, where and why), and the working copies line.
- The tests of the slice are written first and fail on the base for the reason the slice gives; where the slice says a test is red on the base, the report states its failing run and its passing run.
- A change of a test that holds a sentence of a decision by a line `decision:` or an invariant's test is named in your report (WAY-03), so that the request names it.
- Another task changes `elements/common/foundation_check.py` and the sentence of WAY-344 in parallel; leave what is not in your slice alone.

## Your slice, copied from the plan word for word

### Slice 10 — The skill and the template of the audit say what the count now does

- **Goal:** the prose of `process-audit/` that describes the count follows what Slices 6 to 9 made: `process-audit/SKILL.md` (the paragraph "Measures are compared inside a series only", the step on *Process versions* and the paragraph on a new class, the kinds of `unknown` of the first step, and the passage that lists the forms of `stages.md` the count reads — where it says the share of fix rounds is `unknown` where `stages.md` has no column *Files named* — brought to the list of forms of the spec's D2: the older table of tokens by model, the detailed section without the two time lines, without *Files named*, without the two columns of the cache writes (priced with the writes inside *Input*, an approximation), and the newer form; and the note on *Unknown values*) and `process-audit/problem_register.md` (the sentences that a date of *Added* or *Withdrawn* starts a series of the cost, which now starts a series of the count of remarks and none of the cost). No `description:` of a skill changes; where one must, run `python -B agent-instructions/skill_entry_points.py --write`, handle any obsolete output path it reports, commit all its output and do not edit the output by hand. No behaviour of the count changes; the tests of the module that read `process-audit/problem_register.md` as the template still pass.
- **Change:** `process-audit/SKILL.md` · `process-audit/problem_register.md`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/task.md:32-37` To do 5 to 10 · `.runs/task-cycles/scripts-after-foundation-review/task.md:145-148` Settlements to record, rows 3 to 6 · `.runs/task-cycles/scripts-after-foundation-review/spec.md:139-150` D2, the form and the missing field · `.runs/task-cycles/scripts-after-foundation-review/spec.md:363-365` D5, the skill · `foundations/decisions.md:7384-7469` WAY-339 · `process-audit/audit_count.py:1-330` the description of the module as Slices 5 to 9 left it
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` (the template still reads); `python -B agent-instructions/skill_entry_points.py` prints that the entry points are current
- **Depends on:** Slice 6 · Slice 7 · Slice 8 · Slice 9


## The foundation entries of your *Read* as they stand now

The ranges the plan names are those of the base. Where they differ from the plan's, these hold; find a passage of the plan or a range of code by its heading or name where an earlier slice changed its file.

- `foundations/decisions.md:7432-7585` WAY-339

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
