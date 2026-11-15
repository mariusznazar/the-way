# Handoff — executor of slice 11, task `scripts-after-foundation-review`

You are the executor of one slice of a plan in a task cycle of the-way (`implement-task`). The
person who requested the cycle has delegated intermediate choices to the orchestrator; nothing here
is the human's approval. Ask no human. A question you cannot settle from the files named here
returns with the status `questions`; a fact or permission no source gives returns `blocked`.

## Where and what you make

- Worktree (work from its root, never from another checkout): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. The-way is the checkout you work in; it is no product's `.the-way`. Target branch `foundations`; base of the task `7f5c5a56f67d9ff40554240594ca0bde59773cb3`. The foundation entries of the plan are already written on the branch (commits `da9d816` and `bfb774c`); read an entry as they left it.
- Method, read whole: `task-cycle/change/SKILL.md` (`make-change`); variant: **a slice, or the retry of a slice**. You read `task-cycle/change/slice.md` when its step comes, and each other file the method names only when the step or variant that names it comes. You have no skill tool: a skill a method names by its name alone is the `SKILL.md` whose frontmatter `name:` is that name, read as a file.
- Your stage and its boundary: make slice 11 of the plan and nothing else, commit it on the task branch (in English messages, files added by path, never `git add -A`, nothing under `.runs/`), and return before review. You run **no run of the whole gate** (WAY-160); you run the focused checks of the slice's *Checks*.
- Frozen task: `.runs/task-cycles/scripts-after-foundation-review/task.md`. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md`. Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` — your slice is copied below; read the other parts of these files only as your slice's *Read* names them.
- Answers of step 4: trust boundary **yes** — a slice whose *Risk* names a trust boundary changes a script that takes in untrusted data (a transcript, a register, a locations file, a copy of a record from git history, a price list): write the reading so that crafted input cannot make the script crash with a stack trace, write outside its places, run a command or put text of the input into a result unescaped; the review of the slice is told to check that. Irreversible operation: none.
- Your class of model: **cheaper (a model cheaper than the orchestrator's)**.
- Directory for your working copies: `.runs/executor-11/` of the worktree.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/executor-11-report.md`, in the form `make-change` gives; with the **Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`), the own-work check, each check you ran with its command and exit code, the choices you made and the foundation entries or code you reached beyond what is named (what, where and why), and the working copies line.
- The tests of the slice are written first and fail on the base for the reason the slice gives; where the slice says a test is red on the base, the report states its failing run and its passing run.
- A change of a test that holds a sentence of a decision by a line `decision:` or an invariant's test is named in your report (WAY-03), so that the request names it.
- Another task changes `elements/common/foundation_check.py` and the sentence of WAY-344 in parallel; leave what is not in your slice alone.

## Your slice, copied from the plan word for word

### Slice 11 — The generator of the agent type copies ends with exit code 2 at a missing `name:` or `description:`

- **Goal:** `agent-instructions/agent_type_copies.py`, given a definition of an agent type with no line `name:` or no line `description:`, ends with exit code 2 and a message on stderr that names the file and the missing field, and writes nothing; every other error of the generator stays at exit code 1 with `Error: <message>`, and the description of the exit codes ("Exit code: 0 on success; 1 with `Error: <message>` …") names both. A line that stands under another name or in another form is not claimed as missing unless the definition has no such line at all (WAY-344). One test starts from a definition without `name:` and one without `description:` and asserts the code and the field named.
- **Change:** `agent-instructions/agent_type_copies.py` · `agent-instructions/test_agent_type_copies.py`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/task.md:29-29` To do 2 · `.runs/task-cycles/scripts-after-foundation-review/task.md:51-58` Questions to settle 1 · `foundations/decisions.md:2741-2852` WAY-344 · `foundations/decisions.md:2545-2569` WAY-38 · `foundations/invariants.md:116-145` script-language, script-imports, script-subprocesses
- **Model:** cheaper
- **Risk:** none
- **Checks:** start from the new tests in `agent-instructions/test_agent_type_copies.py` (a definition without `name:`, one without `description:`), red on the base; `python -B -m unittest discover -s agent-instructions -p "test_agent_type_copies.py"`; `python -B agent-instructions/agent_type_copies.py` exits 0 and prints that the copies are current (the tracked copies are untouched)
- **Depends on:** none


## The foundation entries of your *Read* as they stand now

The ranges the plan names are those of the base. Where they differ from the plan's, these hold; find a passage of the plan or a range of code by its heading or name where an earlier slice changed its file.

- `foundations/decisions.md:2741-2901` WAY-344
- `foundations/decisions.md:2545-2570` WAY-38
- `foundations/invariants.md:116-125` script-language
- `foundations/invariants.md:126-135` script-imports
- `foundations/invariants.md:136-145` script-subprocesses

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
