# Handoff — executor of slice 13, task `scripts-after-foundation-review`

You are the executor of one slice of a plan in a task cycle of the-way (`implement-task`). The
person who requested the cycle has delegated intermediate choices to the orchestrator; nothing here
is the human's approval. Ask no human. A question you cannot settle from the files named here
returns with the status `questions`; a fact or permission no source gives returns `blocked`.

## Where and what you make

- Worktree (work from its root, never from another checkout): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. The-way is the checkout you work in; it is no product's `.the-way`. Target branch `foundations`; base of the task `7f5c5a56f67d9ff40554240594ca0bde59773cb3`. The foundation entries of the plan are already written on the branch (commits `da9d816` and `bfb774c`); read an entry as they left it.
- Method, read whole: `task-cycle/change/SKILL.md` (`make-change`); variant: **a slice, or the retry of a slice**. You read `task-cycle/change/slice.md` when its step comes, and each other file the method names only when the step or variant that names it comes. You have no skill tool: a skill a method names by its name alone is the `SKILL.md` whose frontmatter `name:` is that name, read as a file.
- Your stage and its boundary: make slice 13 of the plan and nothing else, commit it on the task branch (in English messages, files added by path, never `git add -A`, nothing under `.runs/`), and return before review. You run **no run of the whole gate** (WAY-160); you run the focused checks of the slice's *Checks*.
- Frozen task: `.runs/task-cycles/scripts-after-foundation-review/task.md`. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md`. Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` — your slice is copied below; read the other parts of these files only as your slice's *Read* names them.
- Answers of step 4: trust boundary **yes** — a slice whose *Risk* names a trust boundary changes a script that takes in untrusted data (a transcript, a register, a locations file, a copy of a record from git history, a price list): write the reading so that crafted input cannot make the script crash with a stack trace, write outside its places, run a command or put text of the input into a result unescaped; the review of the slice is told to check that. Irreversible operation: none.
- Your class of model: **cheaper (a model cheaper than the orchestrator's)**.
- Directory for your working copies: `.runs/executor-13/` of the worktree.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/executor-13-report.md`, in the form `make-change` gives; with the **Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`), the own-work check, each check you ran with its command and exit code, the choices you made and the foundation entries or code you reached beyond what is named (what, where and why), and the working copies line.
- The tests of the slice are written first and fail on the base for the reason the slice gives; where the slice says a test is red on the base, the report states its failing run and its passing run.
- A change of a test that holds a sentence of a decision by a line `decision:` or an invariant's test is named in your report (WAY-03), so that the request names it.
- Another task changes `elements/common/foundation_check.py` and the sentence of WAY-344 in parallel; leave what is not in your slice alone.

## Your slice, copied from the plan word for word

### Slice 13 — The test of imports between parts does not fail on `compile` that nothing runs

- **Goal:** the test `elements/part-map/test_cross_part_imports.py` no longer fails on `compile` given the text of a file of another part where nothing runs the result; `exec` and `eval` given that text still fail, and `compile` whose result `exec` or `eval` runs still fails (the tuple `BUILTINS` and the branch "Code given to `exec`, `eval` or `compile`" of `source`, and the description of the test that names `compile`, are changed to say so). The test list `test_each_form_of_code_run_by_exec_eval_or_compile_is_read` is changed: the form `compile(open(...).read(), 'screen', mode='exec')` standing alone is no dependency, the forms run by `exec` or `eval` are. **WAY-03: this slice alters the invariant test of `cross-part-imports`, so the request names it.** The sentence of the invariant ("by running it as a script with `runpy`, `exec` or a new process") is not changed.
- **Change:** `elements/part-map/test_cross_part_imports.py`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/task.md:41-41` To do 14 · `.runs/task-cycles/scripts-after-foundation-review/task.md:127-127` Decisions in play, WAY-03 · `foundations/decisions.md:1628-1672` WAY-03 · `foundations/decisions.md:2364-2413` WAY-44 · `foundations/invariants.md:348-357` cross-part-imports · `foundations/part_map.md:17-25` part-map
- **Model:** cheaper
- **Risk:** none
- **Checks:** start from the changed form list of `test_each_form_of_code_run_by_exec_eval_or_compile_is_read` and a new test of `compile` standing alone, red on the base; `python -B gate/run_tests.py elements/part-map`
- **Depends on:** none


## The foundation entries of your *Read* as they stand now

The ranges the plan names are those of the base. Where they differ from the plan's, these hold; find a passage of the plan or a range of code by its heading or name where an earlier slice changed its file.

- `foundations/decisions.md:1628-1673` WAY-03
- `foundations/decisions.md:2364-2414` WAY-44
- `foundations/invariants.md:348-357` cross-part-imports
- `foundations/part_map.md:17-26` part-map

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
