# Handoff — designer of the spec of the task `scripts-after-foundation-review`

You are the designer of a spec in a task cycle of the-way (`implement-task`). The person who
requested this cycle has delegated intermediate choices to the orchestrator; no answer here is the
human's approval. Ask no human; send questions to the orchestrator in your report.

## Where and what

- Worktree (work from its root): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`, base `7f5c5a56f67d9ff40554240594ca0bde59773cb3`. The-way is the checkout you work in.
- Method, read whole: `task-cycle/spec/SKILL.md` (`write-spec`); variant: the designer writing the spec. You read `design.md` beside it when its step comes, and a file it names only when its step comes. You have no skill tool: a skill a method names is the `SKILL.md` whose frontmatter `name:` is that name, read as a file.
- Spec path: `.runs/task-cycles/scripts-after-foundation-review/spec.md`. Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/designer-report.md`.
- Frozen task, whole: `.runs/task-cycles/scripts-after-foundation-review/task.md`. A plan of the cycle's planner exists, `.runs/task-cycles/scripts-after-foundation-review/plan.md`; it is **not** a source for you and does not bind: a new plan will be written from your spec. You may read its Slice 2 to see the planner's list of what the route has to keep, which is copied below.
- Answers of step 4: trust boundary yes (`process-audit/audit_count.py`, `task-cycle/cycle_stages.py`, `task-cycle/cycle_measures.py`); irreversible operation none.
- Directory for your working copies: `.runs/designer/`.
- Never run the gate. You run no test and no other check (the method says so for this stage).

## The open design choice you settle (the only one)

The task asks (*To do* 7, *Questions to settle* 3, *Settlements to record* 5) that the cost of a cycle in the audit prices the cache writes of 5 minutes and of 1 hour each at its own price, with a price-list column *Cache write (1 hour)*. Its *Context* says: "WAY-339 mówi, że tokeny zapisane do pamięci podręcznej jako miara użycia pamięci „are never columns of the stage report" i liczy je osobny skrypt (`task-cycle/cycle_measures.py`); którędy liczenie audytu dostaje zapisy rozdzielone po modelu i czasie życia do wyceny w *To do* 7, wybiera cykl." Claude Code transcripts give the split (`usage.cache_creation.ephemeral_5m_input_tokens` and `ephemeral_1h_input_tokens`); `task-cycle/cycle_stages.py` today adds `cache_creation_input_tokens` to *Input* (about line 576).

Settle:

1. **The route**: through which file and script the audit count receives, for each stage row and each model, the cache writes of each lifetime — a form of `stages.md` written by `task-cycle/cycle_stages.py`, a table or a file of its own, or the file of the measures written by `task-cycle/cycle_measures.py`. Give the ways weighed, what each costs if wrong, and the one chosen.
2. **The foundation sentences the route makes untrue** and the wording the foundation step must give them: the sentences of WAY-339 (second paragraph: the tokens written to the cache "are never columns of the stage report"; and which script measures the cost), of WAY-337 (how the cost is measured, the share of fix rounds), of WAY-344 (the list of the earlier forms of `stages.md` that the count reads with no line `Error:`, and the rule for a reading a change reworks) and any other entry the search of the foundation finds. The foundation step will rewrite WAY-339 and WAY-344 in place for the task's rows 3 and 4 and 1 and 2 anyway; your spec says what it must add or change for this route. Do not write the entries.
3. **What the route requires of each script**, so that a planner can cut slices: the form of the new data, how an earlier form (copies of earlier cycles, no split) is still read with no `Error:`, no new `unknown` and no change of the exit code, how a Codex row is read (a Codex rollout gives no cache write: such a row has none to price, it is no `unknown`), where the series of the cost is split (the task's row 3: a change of `task-cycle/cycle_stages.py` splits it; a route through `task-cycle/cycle_measures.py` makes that a second script that measures the cost, which you say), and the one test per reading of a file that WAY-344 asks where the route reworks how a script reads a file.

What the route has to keep (the planner's list, copied word for word):

  1. the cost per stage row and model: the share of the cost in fix rounds (WAY-337) ties turns to rows, so a split held for the whole cycle only is no route;
  2. the copies that hold no split: a `stages.md` of an earlier form gives the cost it gives today (its cache writes inside *Input*, priced as input, an approximation), with no line `Error:`, no new `unknown` and no change of the exit code;
  3. WAY-339 and WAY-344 as the foundation step wrote them … A route that makes a sentence of either untrue is allowed only where the spec names the sentence and the wording that the foundation step gives it;
  4. a Codex rollout gives no cache write: a Codex row reads as a row with no writes to price, never as `unknown`, so no Codex cycle loses its cost; the cache figures of `mechanism_measures.md` stay `unknown` for Codex, as today;
  5. WAY-344 for each reading of a file that the change reworks: where it reworks how a script reads a Claude Code transcript, the rule binds the whole reading of that transcript (every field the script reads of it, no other file), with one test that gives the transcript without a field and asserts the failure that names it;
  6. what `process-audit/audit_count.py` reads of `stages.md` today (its columns, its older form, the *Files named* column that an earlier form lacks) is not broken.

The planner's concern about this choice (copied word for word from its report):

> The route of the cache writes (Slice 2) is not free of the foundation. Whatever route Slice 2 takes, it meets a sentence of WAY-339 or WAY-344: WAY-339 says the tokens written to the cache are counted by `task-cycle/cycle_measures.py` into `mechanism_measures.md` and "are never columns of the stage report", and that the cost is measured by `cycle_stages.py`; WAY-344 lists the earlier forms of `stages.md` the count reads with no `Error:`, and a new column or table in `stages.md` is not among them; and `cycle_stages.py` reads transcripts leniently, so a new read of `usage.cache_creation` there brings the whole reading of that transcript under WAY-344. The fix-round share needs the split per stage row and model, which pushes toward columns in `stages.md` (the sentence "never columns" then fails) and away from the file of the measures (a second script then measures the cost, and the series of the cost would need to split on it too).

Do not widen the task: settle only this choice. Items and settlements the task already settles (the two exceptions of WAY-344, the two kinds of series, the unknown measure of a tool the cycle changes, the new column of the price list) are decided; where your route touches them, say how.

## What you read (named by the orchestrator, WAY-150)

Foundation entries, each whole, from `foundations/decisions.md` (heading `### WAY-nnn`): WAY-337, WAY-339, WAY-344, WAY-330, WAY-350, WAY-38, WAY-07, WAY-135. From `foundations/invariants.md`: `audit-series-script-paths`, `script-language`, `script-imports`, `script-subprocesses`. `foundations/part_map.md`: the entries `task-cycle` and `process-audit`. The glossary entries of the terms you use (the file is short; `foundations/glossary.md` whole).

Code, as far as the ways need (read to design, not to write; large files by search and range): `task-cycle/cycle_stages.py` (the description of the module, the report it writes, the reading of Claude Code usage, the Codex reading), `task-cycle/cycle_measures.py` (the description, the readers of responses and of sessions, lines about 235–261 where both lifetimes are already read), `process-audit/audit_count.py` (the module description about lines 59–74 the cost and the two forms of the stage report; constants about 309–324; `stage_table`, `section_table`, `older_table` about 920–1044; `priced`, `cost_at`, `priced_older` about 1255–1316; `read_prices` about 824–890), `process-audit/price_list.md`, and the tests of these only by test names.

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
