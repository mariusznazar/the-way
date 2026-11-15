# Handoff — executor of slice 17, task `scripts-after-foundation-review`

You are the executor of one slice of a plan in a task cycle of the-way (`implement-task`). The
person who requested the cycle has delegated intermediate choices to the orchestrator; nothing here
is the human's approval. Ask no human. A question you cannot settle from the files named here
returns with the status `questions`; a fact or permission no source gives returns `blocked`.

## Where and what you make

- Worktree (work from its root, never from another checkout): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. The-way is the checkout you work in; it is no product's `.the-way`. Target branch `foundations`; base of the task `7f5c5a56f67d9ff40554240594ca0bde59773cb3`. The foundation entries of the plan are already written on the branch (commits `da9d816` and `bfb774c`); read an entry as they left it.
- Method, read whole: `task-cycle/change/SKILL.md` (`make-change`); variant: **a slice, or the retry of a slice**. You read `task-cycle/change/slice.md` when its step comes, and each other file the method names only when the step or variant that names it comes. You have no skill tool: a skill a method names by its name alone is the `SKILL.md` whose frontmatter `name:` is that name, read as a file.
- Your stage and its boundary: make slice 17 of the plan and nothing else, commit it on the task branch (in English messages, files added by path, never `git add -A`, nothing under `.runs/`), and return before review. You run **no run of the whole gate** (WAY-160); you run the focused checks of the slice's *Checks*.
- Frozen task: `.runs/task-cycles/scripts-after-foundation-review/task.md`. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md`. Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` — your slice is copied below; read the other parts of these files only as your slice's *Read* names them.
- Answers of step 4: trust boundary **yes** — a slice whose *Risk* names a trust boundary changes a script that takes in untrusted data (a transcript, a register, a locations file, a copy of a record from git history, a price list): write the reading so that crafted input cannot make the script crash with a stack trace, write outside its places, run a command or put text of the input into a result unescaped; the review of the slice is told to check that. Irreversible operation: none.
- Your class of model: **same (the orchestrator's class)**.
- Directory for your working copies: `.runs/executor-17/` of the worktree.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/executor-17-report.md`, in the form `make-change` gives; with the **Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`), the own-work check, each check you ran with its command and exit code, the choices you made and the foundation entries or code you reached beyond what is named (what, where and why), and the working copies line.
- The tests of the slice are written first and fail on the base for the reason the slice gives; where the slice says a test is red on the base, the report states its failing run and its passing run.
- A change of a test that holds a sentence of a decision by a line `decision:` or an invariant's test is named in your report (WAY-03), so that the request names it.
- Another task changes `elements/common/foundation_check.py` and the sentence of WAY-344 in parallel; leave what is not in your slice alone.

## Your slice, copied from the plan word for word

### Slice 17 — The measures of a real Codex cycle, run and corrected

- **Goal:** `task-cycle/cycle_measures.py` is run on the session records of a real cycle led in Codex that lie under the user's `~/.codex/sessions` (the 78 records there name the-way and `implement-task`; pick one whole cycle, with its subagents, and the session of a nested Claude Code helper where the cycle has one, read from the Claude Code home), with `--output` naming a file in the executor's own directory under `.runs/` of this worktree; the run reads and writes nothing else outside `.runs/`. The executor reports **counts and facts only**: the number of agents of each tool, whether each cycle-level measure of the file has a value or `unknown` and why, whether the cache figures of the Codex agents are `unknown` as the script's description says, and whether the nested helper's measures are full; **no absolute path of the user's disk, no user name and no content of a session**. A measure that comes out wrong or empty where the script should give it is a defect of this cycle: the executor fixes it in `task-cycle/cycle_measures.py` with the test first in `task-cycle/test_cycle_measures.py` (a fixture of the form the real record had, made by hand and with no real content) and reports what it fixed; where nothing is wrong, it changes nothing. The spec leaves this script as it is for the route of the cache writes, so a change here is a change for this item only. Where the user's Codex home, Claude Code home or the records cannot be opened, the executor reports it and does not guess. The output of the run and the executor's directory are removed before it returns (only the counts stay in its report).
- **Change:** `task-cycle/cycle_measures.py` · `task-cycle/test_cycle_measures.py`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/task.md:38-38` To do 11 · `.runs/task-cycles/scripts-after-foundation-review/task.md:80-84` Questions to settle 6 · `foundations/decisions.md:7384-7469` WAY-339 · `foundations/decisions.md:2741-2852` WAY-344 · `foundations/decisions.md:7007-7072` WAY-308 · `foundations/part_map.md:101-111` task-cycle
- **Model:** same — it judges real data and may change a trust-boundary script on what it sees
- **Risk:** trust boundary — `task-cycle/cycle_measures.py`
- **Checks:** the run above, with its counts in the report; where a defect is fixed, the new test red on the base and `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"`
- **Depends on:** none


## The foundation entries of your *Read* as they stand now

The ranges the plan names are those of the base. Where they differ from the plan's, these hold; find a passage of the plan or a range of code by its heading or name where an earlier slice changed its file.

- `foundations/decisions.md:7432-7585` WAY-339
- `foundations/decisions.md:2741-2901` WAY-344
- `foundations/decisions.md:7055-7121` WAY-308
- `foundations/part_map.md:101-112` task-cycle

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

## Added by the orchestrator for this slice (the real run of *To do* 11)

- The human's answer to question 6 of the task permits this run on the user's real data: the session records of Codex cycles lie under the user's `.codex/sessions` directory (about 78 records name the-way and `implement-task`, state of 2026-11-15) and the Claude Code home under the user's `.claude` directory; both are **only read**. Find the user's home directory through the environment of the shell (for example `$HOME` or `Path.home()`); never write one of those paths, the user name or the content of a session into a file that is committed, into the report or into the commit message.
- Choose one whole cycle: its orchestrator rollout and its subagents' rollouts, and, where the cycle has one, the session of a nested Claude Code helper. Give `task-cycle/cycle_measures.py` the session identifiers or paths as its description says and `--output` a file in `.runs/executor-17/` of the worktree. Write nothing else outside `.runs/executor-17/`.
- Your report holds **counts and facts only** (as the slice says); describe a path of the disk only as "the user's Codex home" or "the user's Claude Code home". If a measure comes out wrong or empty, fix `task-cycle/cycle_measures.py` with the test first (a fixture made by hand, no real content). Remove `.runs/executor-17/` and every log before you return; start no background watcher.
