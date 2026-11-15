# Handoff — executor of slice 3, task `scripts-after-foundation-review`

You are the executor of one slice of a plan in a task cycle of the-way (`implement-task`). The
person who requested the cycle has delegated intermediate choices to the orchestrator; nothing here
is the human's approval. Ask no human. A question you cannot settle from the files named here
returns with the status `questions`; a fact or permission no source gives returns `blocked`.

## Where and what you make

- Worktree (work from its root, never from another checkout): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. The-way is the checkout you work in; it is no product's `.the-way`. Target branch `foundations`; base of the task `7f5c5a56f67d9ff40554240594ca0bde59773cb3`. The foundation entries of the plan are already written on the branch (commits `da9d816` and `bfb774c`); read an entry as they left it.
- Method, read whole: `task-cycle/change/SKILL.md` (`make-change`); variant: **a slice, or the retry of a slice**. You read `task-cycle/change/slice.md` when its step comes, and each other file the method names only when the step or variant that names it comes. You have no skill tool: a skill a method names by its name alone is the `SKILL.md` whose frontmatter `name:` is that name, read as a file.
- Your stage and its boundary: make slice 3 of the plan and nothing else, commit it on the task branch (in English messages, files added by path, never `git add -A`, nothing under `.runs/`), and return before review. You run **no run of the whole gate** (WAY-160); you run the focused checks of the slice's *Checks*.
- Frozen task: `.runs/task-cycles/scripts-after-foundation-review/task.md`. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md`. Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` — your slice is copied below; read the other parts of these files only as your slice's *Read* names them.
- Answers of step 4: trust boundary **yes** — a slice whose *Risk* names a trust boundary changes a script that takes in untrusted data (a transcript, a register, a locations file, a copy of a record from git history, a price list): write the reading so that crafted input cannot make the script crash with a stack trace, write outside its places, run a command or put text of the input into a result unescaped; the review of the slice is told to check that. Irreversible operation: none.
- Your class of model: **cheaper (a model cheaper than the orchestrator's)**.
- Directory for your working copies: `.runs/executor-3/` of the worktree.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/executor-3-report.md`, in the form `make-change` gives; with the **Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`), the own-work check, each check you ran with its command and exit code, the choices you made and the foundation entries or code you reached beyond what is named (what, where and why), and the working copies line.
- The tests of the slice are written first and fail on the base for the reason the slice gives; where the slice says a test is red on the base, the report states its failing run and its passing run.
- A change of a test that holds a sentence of a decision by a line `decision:` or an invariant's test is named in your report (WAY-03), so that the request names it.
- Another task changes `elements/common/foundation_check.py` and the sentence of WAY-344 in parallel; leave what is not in your slice alone.

## Your slice, copied from the plan word for word

### Slice 3 — The stage report holds the cache writes of each lifetime for each stage and model

- **Goal:** the detailed section of the report of `task-cycle/cycle_stages.py` (*Stages: start, waiting for tools and tokens by model*) gains, after *Files named*, the columns *Cache write (5 minutes)* and *Cache write (1 hour)* (D1): for each row and each model, the tokens the model's responses wrote to the cache at each lifetime, from `message.usage.cache_creation.ephemeral_5m_input_tokens` and `ephemeral_1h_input_tokens`, summed like the other counts, whole numbers in the form of the other token cells. *Input* keeps its meaning and its figure (input, cache writes and cache reads together); the line "Tokens in all", the whole-cycle table by model and the first table keep their figures and columns; the module description and the paragraph above the section say that *Input* holds the writes and what the two columns are. A Codex row writes `0` and `0`, with no warning and no `unknown`; a row with no token usage keeps the model `—` or `unknown` and zero counts. Where the two lifetimes of a response do not add up to its `cache_creation_input_tokens`, a `Warning:` line names the transcript, the figures stand as read and the exit code is 0. The new fields join the *Needed* list of Slice 2 (`message.usage.cache_creation` and its two lifetimes, absent or no whole number: exit 2 naming the field), under the same one test and the same pin. The tests: the detailed table of a Claude Code stage holds the two columns with the figures of the two lifetimes of its responses, a Codex row holds `0` and `0`, a row of one model with both lifetimes keeps them apart; and the test across the two scripts — the same Claude Code transcript given to `cycle_stages.py` and `cycle_measures.py` gives the same tokens written at each lifetime in the totals of both. `task-cycle/cycle_measures.py` and `mechanism_measures.md` do not change. After the slice the audit still reads the report: its reading ignores nothing it needs, and no other script changes here.
- **Change:** `task-cycle/cycle_stages.py` · `task-cycle/test_cycle_stages.py`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/spec.md:87-98` D1, the route · `.runs/task-cycles/scripts-after-foundation-review/spec.md:132-135` D1, the price of the route · `.runs/task-cycles/scripts-after-foundation-review/spec.md:169-174` D2, Codex rows · `.runs/task-cycles/scripts-after-foundation-review/spec.md:249-264` D4, new data, Codex row, the warning · `.runs/task-cycles/scripts-after-foundation-review/spec.md:308-324` D4, the test, the test across the two scripts, the series of the cost · `.runs/task-cycles/scripts-after-foundation-review/task.md:34-34` To do 7 · `foundations/decisions.md:7343-7382` WAY-337 · `foundations/decisions.md:7384-7469` WAY-339 · `foundations/decisions.md:2741-2852` WAY-344 · `foundations/invariants.md:116-145` script-language, script-imports, script-subprocesses · `foundations/part_map.md:101-111` task-cycle · `task-cycle/cycle_measures.py` the whole file, for the figures of the test across the two scripts
- **Model:** cheaper
- **Risk:** trust boundary — `task-cycle/cycle_stages.py`
- **Checks:** start from the new tests in `task-cycle/test_cycle_stages.py` (the two columns of a Claude Code stage, `0` and `0` of a Codex row, the two lifetimes of one model kept apart, the test across the two scripts, the transcript without `message.usage.cache_creation`), red on the base; `python -B -m unittest discover -s task-cycle -p "test_cycle_stages.py"`; `python -B -m unittest discover -s task-cycle -p "test_cycle_measures.py"`; `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Cost -k StagesForms` (the audit still reads the report of the earlier forms)
- **Depends on:** Slice 2


## The foundation entries of your *Read* as they stand now

The ranges the plan names are those of the base. Where they differ from the plan's, these hold; find a passage of the plan or a range of code by its heading or name where an earlier slice changed its file.

- `foundations/decisions.md:7391-7431` WAY-337
- `foundations/decisions.md:7432-7585` WAY-339
- `foundations/decisions.md:2741-2901` WAY-344
- `foundations/invariants.md:116-125` script-language
- `foundations/invariants.md:126-135` script-imports
- `foundations/invariants.md:136-145` script-subprocesses
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
