# Handoff — executor of slice 7, task `scripts-after-foundation-review`

You are the executor of one slice of a plan in a task cycle of the-way (`implement-task`). The
person who requested the cycle has delegated intermediate choices to the orchestrator; nothing here
is the human's approval. Ask no human. A question you cannot settle from the files named here
returns with the status `questions`; a fact or permission no source gives returns `blocked`.

## Where and what you make

- Worktree (work from its root, never from another checkout): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. The-way is the checkout you work in; it is no product's `.the-way`. Target branch `foundations`; base of the task `7f5c5a56f67d9ff40554240594ca0bde59773cb3`. The foundation entries of the plan are already written on the branch (commits `da9d816` and `bfb774c`); read an entry as they left it.
- Method, read whole: `task-cycle/change/SKILL.md` (`make-change`); variant: **a slice, or the retry of a slice**. You read `task-cycle/change/slice.md` when its step comes, and each other file the method names only when the step or variant that names it comes. You have no skill tool: a skill a method names by its name alone is the `SKILL.md` whose frontmatter `name:` is that name, read as a file.
- Your stage and its boundary: make slice 7 of the plan and nothing else, commit it on the task branch (in English messages, files added by path, never `git add -A`, nothing under `.runs/`), and return before review. You run **no run of the whole gate** (WAY-160); you run the focused checks of the slice's *Checks*.
- Frozen task: `.runs/task-cycles/scripts-after-foundation-review/task.md`. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md`. Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` — your slice is copied below; read the other parts of these files only as your slice's *Read* names them.
- Answers of step 4: trust boundary **yes** — a slice whose *Risk* names a trust boundary changes a script that takes in untrusted data (a transcript, a register, a locations file, a copy of a record from git history, a price list): write the reading so that crafted input cannot make the script crash with a stack trace, write outside its places, run a command or put text of the input into a result unescaped; the review of the slice is told to check that. Irreversible operation: none.
- Your class of model: **same (the orchestrator's class)**.
- Directory for your working copies: `.runs/executor-7/` of the worktree.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/executor-7-report.md`, in the form `make-change` gives; with the **Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`), the own-work check, each check you ran with its command and exit code, the choices you made and the foundation entries or code you reached beyond what is named (what, where and why), and the working copies line.
- The tests of the slice are written first and fail on the base for the reason the slice gives; where the slice says a test is red on the base, the report states its failing run and its passing run.
- A change of a test that holds a sentence of a decision by a line `decision:` or an invariant's test is named in your report (WAY-03), so that the request names it.
- Another task changes `elements/common/foundation_check.py` and the sentence of WAY-344 in parallel; leave what is not in your slice alone.

## Your slice, copied from the plan word for word

### Slice 7 — The cost prices the cache writes of each lifetime at its own price

- **Goal:** in `process-audit/audit_count.py`, the audit reads the newer form of the detailed section of `stages.md` and prices it, as the spec's D2 and D5 fix. **Form:** the header of the detailed table has three forms, each a prefix of the next — the columns the audit needs (`#`, `Stage`, `Start`, `Waiting for tools`, `Model`, `Input`, `Cached input`, `Output`); those and *Files named*; those, *Files named* and the two columns *Cache write (5 minutes)* and *Cache write (1 hour)*, in that order; a header of another form is refused with a reason, as today; the row type holds the two counts, zero for the earlier forms. **Missing field:** a table with neither write column is the earlier form, read as today (no `Error:`, the same cost, the same exit code, no new `unknown`); a table with one and not the other has a missing field: the cost is `unknown` with the reason, the result is written, the run ends with exit 1 and the `Error:` line names `stages.md` and the column that is missing; the pair is never missing when neither stands, as *Files named* is never. **Cost of a row of the newer form:** the input that is neither a cache read nor a write at *Input*, the cache read at *Cached input*, the writes of 5 minutes and of 1 hour each at its write price, the output at *Output*; a row whose cached input and writes together exceed its input is `unknown` with a reason; a row of an earlier form and the older table of tokens by model are priced exactly as today. **Price list:** `read_prices` reads both write columns of every table as it reads the other three; a table that lacks one ends the run with exit 2 and an `Error:` that names the option `--prices` and the column, never the path; a write cell is a number or `—`; a `—` in a write column is no price for that lifetime (a model so marked is priced while the row holds none of that lifetime and the cost is `unknown`, with the reason, where it holds some, never a price borrowed from another column), and a `—` in *Input*, *Cached input* or *Output* stays a model with no price at all; the price table keeps the two cases apart. **Codex:** a Codex row has `0` and `0` and is priced as today. The module description is changed where it says "Cache writes are inside *Input* … priced as input: an approximation" (it holds for the earlier forms, and says what the newer form does), the paragraph that lists the fields of `stages.md` under WAY-344 gains the two columns as a pair that is never missing when both are absent, and the description of the price list gains the new column and the rule for `—`; the text of the section *Cost* follows. The tests, each first red on the base: a copy of the earlier form without the write columns gives the cost it gave, no `Error:`, no new `unknown`, the same exit code; a copy with one write column only gives the cost `unknown`, writes the result, ends with exit 1 and the line that names `stages.md` and the column; a copy of the newer form prices a row with writes of both lifetimes at the two prices (figures that tell the 5-minute price from the 1-hour price), a Codex row with zero writes at the old price, a model with `—` in a write column and writes as `unknown`, a model with `—` and no writes as priced, and a row whose cached input and writes exceed its input as `unknown`; and the one test of the price list: a table without *Cache write (1 hour)* ends with exit 2 and an `Error:` naming `--prices` and the column. The existing tests that build a price list gain both write columns.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/task.md:34-34` To do 7 · `.runs/task-cycles/scripts-after-foundation-review/task.md:111-113` Context, cache writes, WAY-339 and the route · `.runs/task-cycles/scripts-after-foundation-review/task.md:147-147` Settlements to record, row 5 · `.runs/task-cycles/scripts-after-foundation-review/spec.md:137-178` D2, what the audit does with the columns · `.runs/task-cycles/scripts-after-foundation-review/spec.md:329-357` D5, form and reading, the module description, the tests · `foundations/decisions.md:7343-7382` WAY-337 · `foundations/decisions.md:2741-2852` WAY-344 · `process-audit/price_list.md` the price list as Slice 4 left it · the form of the stage report that Slice 3 wrote: the function report of the file task-cycle/cycle_stages.py, found by its name
- **Model:** same — it joins the writer of Slice 3, the price list of Slice 4 and the reading of three forms under WAY-344
- **Risk:** trust boundary — `process-audit/audit_count.py`
- **Checks:** start from the new tests of class `Cost` and of class `StagesForms`, and the test of the price list in class `Cost` or `Locations`, red on the base; `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k Cost -k StagesForms -k Locations -k PriceBoundary`; then the whole file `python -B -m unittest discover -s process-audit -p "test_audit_count.py"`; `python -B process-audit/audit_count.py --help` exits 0
- **Depends on:** Slice 3 · Slice 4 · Slice 6


## The foundation entries of your *Read* as they stand now

The ranges the plan names are those of the base. Where they differ from the plan's, these hold; find a passage of the plan or a range of code by its heading or name where an earlier slice changed its file.

- `foundations/decisions.md:7391-7431` WAY-337
- `foundations/decisions.md:2741-2901` WAY-344

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

## Added by the orchestrator for this slice

- The test `Cost.test_the_stage_report_cycle_stages_writes_gives_the_share` of `process-audit/test_audit_count.py` has been red since Slice 3, because the audit refuses the eleven-column header that `task-cycle/cycle_stages.py` now writes. **It must be green at the end of your slice**, with the audit reading the newer form as the spec's D2 gives; that test runs the stage script on a transcript and gives the audit its output, so it is the one test across the two scripts. Run the whole `test_audit_count.py` at the end and report its result; this is the only slice that may turn it green.
- The audit file and its test file together are about 136 000 tokens: read them by ranges and by search, whole only the ranges you change.
- Slice 6 (done) changed the grouping of versions into series; the list of what starts a series of the cost is `task-cycle/cycle_stages.py` and the price list: do not change it.
