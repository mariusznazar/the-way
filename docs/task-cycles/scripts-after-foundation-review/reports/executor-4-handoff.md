# Handoff — executor of slice 4, task `scripts-after-foundation-review`

You are the executor of one slice of a plan in a task cycle of the-way (`implement-task`). The
person who requested the cycle has delegated intermediate choices to the orchestrator; nothing here
is the human's approval. Ask no human. A question you cannot settle from the files named here
returns with the status `questions`; a fact or permission no source gives returns `blocked`.

## Where and what you make

- Worktree (work from its root, never from another checkout): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. The-way is the checkout you work in; it is no product's `.the-way`. Target branch `foundations`; base of the task `7f5c5a56f67d9ff40554240594ca0bde59773cb3`. The foundation entries of the plan are already written on the branch (commits `da9d816` and `bfb774c`); read an entry as they left it.
- Method, read whole: `task-cycle/change/SKILL.md` (`make-change`); variant: **a slice, or the retry of a slice**. You read `task-cycle/change/slice.md` when its step comes, and each other file the method names only when the step or variant that names it comes. You have no skill tool: a skill a method names by its name alone is the `SKILL.md` whose frontmatter `name:` is that name, read as a file.
- Your stage and its boundary: make slice 4 of the plan and nothing else, commit it on the task branch (in English messages, files added by path, never `git add -A`, nothing under `.runs/`), and return before review. You run **no run of the whole gate** (WAY-160); you run the focused checks of the slice's *Checks*.
- Frozen task: `.runs/task-cycles/scripts-after-foundation-review/task.md`. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md`. Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` — your slice is copied below; read the other parts of these files only as your slice's *Read* names them.
- Answers of step 4: trust boundary **yes** — a slice whose *Risk* names a trust boundary changes a script that takes in untrusted data (a transcript, a register, a locations file, a copy of a record from git history, a price list): write the reading so that crafted input cannot make the script crash with a stack trace, write outside its places, run a command or put text of the input into a result unescaped; the review of the slice is told to check that. Irreversible operation: none.
- Your class of model: **cheaper (a model cheaper than the orchestrator's)**.
- Directory for your working copies: `.runs/executor-4/` of the worktree.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/executor-4-report.md`, in the form `make-change` gives; with the **Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`), the own-work check, each check you ran with its command and exit code, the choices you made and the foundation entries or code you reached beyond what is named (what, where and why), and the working copies line.
- The tests of the slice are written first and fail on the base for the reason the slice gives; where the slice says a test is red on the base, the report states its failing run and its passing run.
- A change of a test that holds a sentence of a decision by a line `decision:` or an invariant's test is named in your report (WAY-03), so that the request names it.
- Another task changes `elements/common/foundation_check.py` and the sentence of WAY-344 in parallel; leave what is not in your slice alone.

## Your slice, copied from the plan word for word

### Slice 4 — The price list prices the cache writes of one hour, in both tables

- **Goal:** `process-audit/price_list.md` has the column *Cache write (1 hour)* beside *Cache write (5 minutes)* in the Anthropic table, and both write columns in the OpenAI table, where each cell is `—` (OpenAI gives no price of a write, and a Codex row has none to price). The price of each Anthropic model is **read on the day of the run from the Anthropic pricing page the list names (`https://platform.claude.com/docs/en/about-claude/pricing`) with the web tool, never written from memory**; a model for which the page gives none is `—`. The list date is that day; so that the date stays true, every other price of both pages the list names is read again the same day and corrected where the page differs. Where the page cannot be opened or does not give a price, the cells stay `—`, the report says so, and the orchestrator then asks the human. The description of how the command uses the columns says that, for the newer form of the stage report, the cache writes of 5 minutes and of 1 hour are each priced at the price of their own column, the input that is neither a read nor a write at *Input*, the cached input at *Cached input* and the output at *Output*; that a `—` in a write column means no price for that lifetime (a model so marked is priced while the row holds no writes of that lifetime, and a row that holds some has the cost `unknown`), whereas a `—` in *Input*, *Cached input* or *Output* is a model with no price at all; and that the earlier forms of the stage report, with their cache writes inside *Input*, are priced as input, an approximation; the sentence "Cache writes (*Cache write (5 minutes)*) are not priced: …" is gone. The sentence that a new list starts a new series of the cost stays true (WAY-339). Nothing in `process-audit/audit_count.py` changes here. **Order, and why:** this slice comes before the audit slice (Slice 7) that requires both write columns in every table, so that every commit leaves the real list readable by the audit as it stands, which ignores a column it does not read; were the audit slice first, the real list would end the count with exit 2 until this one landed, and the audit's tests that read the shipped list would fail between them. The two are kept apart, and not made in one slice, because this one is a price read from a web page and Slice 7 reads about 136 000 tokens of audit code and tests.
- **Change:** `process-audit/price_list.md`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/task.md:34-34` To do 7 · `.runs/task-cycles/scripts-after-foundation-review/task.md:65-69` Questions to settle 3 · `.runs/task-cycles/scripts-after-foundation-review/task.md:113-113` Context, the price list · `.runs/task-cycles/scripts-after-foundation-review/spec.md:159-167` D2, the prices · `.runs/task-cycles/scripts-after-foundation-review/spec.md:176-178` D2, the older table · `.runs/task-cycles/scripts-after-foundation-review/spec.md:358-362` D5, the price list · `foundations/decisions.md:7343-7382` WAY-337 · `foundations/decisions.md:7384-7469` WAY-339 · `foundations/decisions.md:3332-3413` WAY-368 · `process-audit/audit_count.py:824-890` read_prices
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B -c "import sys; sys.path.insert(0, 'process-audit'); import audit_count; audit_count.read_prices('process-audit/price_list.md')"` exits 0 (the list still reads); `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k PriceBoundary -k Locations`; the report gives, for each price changed or read, the page and the day
- **Depends on:** none


## The foundation entries of your *Read* as they stand now

The ranges the plan names are those of the base. Where they differ from the plan's, these hold; find a passage of the plan or a range of code by its heading or name where an earlier slice changed its file.

- `foundations/decisions.md:7391-7431` WAY-337
- `foundations/decisions.md:7432-7585` WAY-339
- `foundations/decisions.md:3380-3462` WAY-368

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
