# Handoff — planner of the task `scripts-after-foundation-review`

You are the planner of a task cycle of the-way (`implement-task`). The person who requested this
cycle has delegated intermediate choices to the orchestrator; no answer in this handoff is the
human's approval. Ask no human; send questions back to the orchestrator in your report.

## Where and what

- Worktree (work from its root, never from another checkout): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`, base commit `7f5c5a56f67d9ff40554240594ca0bde59773cb3` (target branch `foundations`). The-way is the checkout you work in; it is no product's `.the-way`.
- Method of your stage, read whole: `task-cycle/plan/SKILL.md` (`plan-task`). A file it names, one beside it included, you read only when the step or variant that names it comes. You have no skill tool: a skill a method names is the `SKILL.md` whose frontmatter `name:` is that name, read as a file.
- Your stage and its boundary: write the plan of the whole change, `plan.md`, and its size report, `plan-size.md`, in `.runs/task-cycles/scripts-after-foundation-review/`; write no code, no test and no foundation entry; return before any slice is made.
- Frozen task, read whole: `.runs/task-cycles/scripts-after-foundation-review/task.md` (the approved task document; in it, *To do* 1–20, *Questions to settle* 1–9 with the answers, *Decisions in play*, *Settlements to record* 1–8, *Context*, *Out of scope*). No spec exists: the orchestrator found no open design choice (the route by which the audit count receives the cache writes split by model and lifetime, *To do* 7, is left by the task to the cycle: it is a choice of how to make what the task settles, so the executor of the slice that makes it names it in its report, and you name in the plan the slice that owns it and what the choice has to keep).
- Answers of step 4 of the cycle: trust boundary: **yes** — the files of the task that the part map names as trust boundaries are `process-audit/audit_count.py`, `task-cycle/cycle_stages.py` and `task-cycle/cycle_measures.py` (and `task-cycle/gate_times.py` if a slice must touch it); every slice whose files include one of these carries the mark in *Risk*. Irreversible operation: **no** (no slice holds one).
- Route: the orchestrator selected planning because twenty items across several parts do not fit one agent.
- Directory for your working copies: `.runs/planner/` of the worktree.
- Report: `.runs/task-cycles/scripts-after-foundation-review/reports/planner-report.md`, in the form the method gives, with **Unread material** and **Searches not found or unclear** (each `none` where nothing).
- Waiting for the human or an advisor: the plan's *Checks* name focused checks and **never a run of the whole gate** (WAY-160). The orchestrator runs the gate itself, and, by the task's own instruction, writes that the tree is ready and waits for a signal from the day's advisor before each full run.

## What you read (named by the orchestrator, WAY-150)

Foundation entries, each whole, from `foundations/decisions.md` unless noted (find each by its heading `### WAY-nnn`):

- the decisions the task's *Decisions in play* names: WAY-03, WAY-294, WAY-309, WAY-320, WAY-328, WAY-337, WAY-339, WAY-344, WAY-368;
- the decisions of the parts touched: WAY-07, WAY-38, WAY-89, WAY-135, WAY-136, WAY-150, WAY-160, WAY-229, WAY-308, WAY-324, WAY-330, WAY-350 and WAY-33;
- the invariants of `foundations/invariants.md`: `script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`, `tracked-file-private-paths`, `audit-series-script-paths`, `record-copy-image-files`, `review-tag-pattern`, `skill-entry-points`, `test-method-citation`, `return-step-record`;
- `foundations/part_map.md` whole (it is short) and `foundations/glossary.md` whole (it is short);
- the way of working the skills share, `elements/common/way_of_working.md`, and the rules of form `elements/common/rules.md`, only for the *Foundation entries* the plan lists.

The-way holds no guidelines of its own under WAY-328 (its departure: neither the coding nor the testing guidelines of a product is missing); there are no guideline files to read.

You read the code and the tests the change touches as far as you need to cut slices and to name each slice's files and *Read*: at least the files the *To do* names (`process-audit/audit_count.py`, `process-audit/test_audit_count.py`, `process-audit/test_audit_series_scripts.py`, `process-audit/price_list.md`, `agent-instructions/agent_type_copies.py` and its test, `task-cycle/cycle_stages.py`, `task-cycle/cycle_measures.py` and their tests, `elements/common/foundation_check.py` and `test_foundation_check.py`, `elements/part-map/test_cross_part_imports.py`, `task-cycle/remarks_check.py`, `task-cycle/private_paths_check.py`, `task-cycle/tracked_private_paths_check.py` with their tests, `installation/README.md`, `installation/test_styleguide_installation.py`, `installation/test_testing_guidelines_installation.py`, the skill files of `product-guidelines/` and `project-level/` for item 15). Several of these files are large (`audit_count.py` is several thousand lines): read them by searching and by ranges, never whole.

## What the plan must cover

- Every item of *To do* (1–20), every row of *Settlements to record* (1–8) and every answered question. The two decisions WAY-339 and WAY-344 are rewritten in place (WAY-07) with their *Verification* and *Rationale* (rows 1–4; the cycle's foundation step or the plan's *Foundation entries* writes them by `task-cycle/skill/foundation_step.md` through the skill of the element, as the method says); row 8 is a glossary term; rows 5–7 go to code or data, not to the foundation.
- Group the items by the files they change so that two slices never edit the same file in a way that makes the order matter without the plan saying so: *To do* 1, 3, 5, 6, 7, 8, 9, 10 all change `process-audit/audit_count.py` and its tests; 4, 7, 8, 11 change `task-cycle/cycle_stages.py` and `task-cycle/cycle_measures.py`; 12–13 `elements/common`; 14–15 tests of the foundation; 16–18 scripts and their tests of `task-cycle`; 19 and 20 `installation`.
- *To do* 11 is a run on real data (`task-cycle/cycle_measures.py` on the session records of a real Codex cycle that lie under the user's `~/.codex/sessions`, and `process-audit/audit_count.py` on the real register of problems through a **copy** of the locations file given by `--locations` whose `audit_results` entry points to the executor's own directory under `.runs/`). It is the last code slice's check and may change code (a wrong or empty measure is fixed in this cycle). The executor reports the **results as counts and facts**, with no absolute path of the user's disk, no user name and no content of a session; the orchestrator puts them in the request. The run never writes outside `.runs/`; where the user's locations file or sessions cannot be opened, the executor reports it and does not guess.
- Honour the order that the items force: for example the cache-write columns of the price list (7) and the split of the cache writes in the stage script (the executor decides how the audit count receives them) before the calculation of the cost; the series split (5, 6) with the new price list; item 8 uses what 5 and 6 settle about series; item 10 before the real run of 11.
- Honour the scope of each item literally; items outside the task: `#100-6`, `#120-2`, the function `read_contradiction` of `audit_count.py` (another task rewrites it) and the sibling tasks named in *Context* — leave them alone.
- Each slice names its tests: a test that fails on the base and passes after (written with the change), the focused command (`python -B gate/run_tests.py <directory>` or one test file), and for a change of a reading of a file under WAY-344 the one test that gives the file without a field and asserts the failure that names it.
- Slices whose files include a trust-boundary file are marked in *Risk*; slices that change a test held by an invariant (`cross-part-imports`, the tests that hold a line `decision:`, WAY-03) say so, so that the request names the test.

## What you may not do

Do not run the gate. Do not edit anything outside `.runs/` and the plan files named above. Do not read the user's locations file, session records or register of problems — a slice's executor does, within *To do* 11.

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
