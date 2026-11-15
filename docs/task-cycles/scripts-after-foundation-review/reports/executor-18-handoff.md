# Handoff — executor of slice 18, task `scripts-after-foundation-review`

You are the executor of one slice of a plan in a task cycle of the-way (`implement-task`). The
person who requested the cycle has delegated intermediate choices to the orchestrator; nothing here
is the human's approval. Ask no human. A question you cannot settle from the files named here
returns with the status `questions`; a fact or permission no source gives returns `blocked`.

## Where and what you make

- Worktree (work from its root, never from another checkout): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. The-way is the checkout you work in; it is no product's `.the-way`. Target branch `foundations`; base of the task `7f5c5a56f67d9ff40554240594ca0bde59773cb3`. The foundation entries of the plan are already written on the branch (commits `da9d816` and `bfb774c`); read an entry as they left it.
- Method, read whole: `task-cycle/change/SKILL.md` (`make-change`); variant: **a slice, or the retry of a slice**. You read `task-cycle/change/slice.md` when its step comes, and each other file the method names only when the step or variant that names it comes. You have no skill tool: a skill a method names by its name alone is the `SKILL.md` whose frontmatter `name:` is that name, read as a file.
- Your stage and its boundary: make slice 18 of the plan and nothing else, commit it on the task branch (in English messages, files added by path, never `git add -A`, nothing under `.runs/`), and return before review. You run **no run of the whole gate** (WAY-160); you run the focused checks of the slice's *Checks*.
- Frozen task: `.runs/task-cycles/scripts-after-foundation-review/task.md`. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md`. Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` — your slice is copied below; read the other parts of these files only as your slice's *Read* names them.
- Answers of step 4: trust boundary **yes** — a slice whose *Risk* names a trust boundary changes a script that takes in untrusted data (a transcript, a register, a locations file, a copy of a record from git history, a price list): write the reading so that crafted input cannot make the script crash with a stack trace, write outside its places, run a command or put text of the input into a result unescaped; the review of the slice is told to check that. Irreversible operation: none.
- Your class of model: **same (the orchestrator's class)**.
- Directory for your working copies: `.runs/executor-18/` of the worktree.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/executor-18-report.md`, in the form `make-change` gives; with the **Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`), the own-work check, each check you ran with its command and exit code, the choices you made and the foundation entries or code you reached beyond what is named (what, where and why), and the working copies line.
- The tests of the slice are written first and fail on the base for the reason the slice gives; where the slice says a test is red on the base, the report states its failing run and its passing run.
- A change of a test that holds a sentence of a decision by a line `decision:` or an invariant's test is named in your report (WAY-03), so that the request names it.
- Another task changes `elements/common/foundation_check.py` and the sentence of WAY-344 in parallel; leave what is not in your slice alone.

## Your slice, copied from the plan word for word

### Slice 18 — The audit count run on the real register of problems, and corrected

- **Goal:** `process-audit/audit_count.py` is run on the user's real register of problems through a **copy** of the user's locations file, given by `--locations`, whose `audit_results` entry under `the-way` points to a directory in the executor's own directory under `.runs/` of this worktree; the original locations file, the register and the repositories are only read, and nothing is written outside `.runs/`. Where the count refuses a result directory that lies inside a checkout it reads, the executor reports that and does not choose another place; the orchestrator then decides. The executor reports **counts and facts only**: the exit code, the number of lines of *Unknown values* (it was about 830 on the template, which Slice 9 reduces) and of lines for each kind, whether the measures of the Codex cycle and of the nested Claude Code helper are present in *Mechanism measures*, and the number of `Error:` lines; **no absolute path of the user's disk, no user name, no name of a repository or product and no content of the register or of a cycle**. A result that is wrong or empty where the count should give it is a defect of this cycle: the executor fixes it in `process-audit/audit_count.py` with the test first in `process-audit/test_audit_count.py` and reports what it fixed; where nothing is wrong, it changes nothing. Where the locations file or the register cannot be opened, the executor reports it and does not guess. The copy of the locations file, the result and the executor's directory are removed before it returns.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/task.md:37-38` To do 10 and 11 · `.runs/task-cycles/scripts-after-foundation-review/task.md:75-84` Questions to settle 5 and 6 · `foundations/decisions.md:7309-7341` WAY-330 · `foundations/decisions.md:7183-7253` WAY-320 · `foundations/invariants.md:116-145` script-language, script-imports, script-subprocesses · `foundations/part_map.md:124-134` process-audit
- **Model:** same — it judges real data and may change a trust-boundary script on what it sees
- **Risk:** trust boundary — `process-audit/audit_count.py`
- **Checks:** the run above, with its counts in the report; where a defect is fixed, the new test red on the base and `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` · `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"`
- **Depends on:** Slice 9 · Slice 17


## The foundation entries of your *Read* as they stand now

The ranges the plan names are those of the base. Where they differ from the plan's, these hold; find a passage of the plan or a range of code by its heading or name where an earlier slice changed its file.

- `foundations/decisions.md:7357-7390` WAY-330
- `foundations/decisions.md:7231-7302` WAY-320
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

## Added by the orchestrator for this slice (the real run of *To do* 11, the count)

- The human's answer to question 6 of the task permits this run on the user's real register of problems, **read only**. The user's locations file is `.the-way/locations.json` under the user's home directory (find the home through the environment of the shell); it is only read. Make a **copy** of it in `.runs/executor-18/`, in which the entry `audit_results` under `the-way` points to a directory in `.runs/executor-18/` of this worktree, and give the copy to the count with `--locations`. Everything the count writes goes to that directory; nothing is written elsewhere.
- Where the count refuses a result directory that lies inside a checkout it reads (the plan's concern 7), report that exactly and stop that run: do not move the result to another place and do not edit the copy to avoid the refusal; the orchestrator decides with the advisor.
- Your report holds **counts and facts only** (exit code, the number of lines of *Unknown values* and of each kind, whether the Codex cycle's and the nested helper's measures stand in *Mechanism measures*, the number of `Error:` lines): no path of the disk, no user name, no name of a repository or product, and no content of the register or of a cycle; describe a place only as "the user's locations file", "the register of problems". If a result is wrong or empty where the count should give it, fix `process-audit/audit_count.py` with the test first (a hand-made fixture, no real content) and report what you fixed. Remove `.runs/executor-18/` and every log before you return; start no background watcher.
