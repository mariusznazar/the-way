# Handoff — executor of slice 8, task `scripts-after-foundation-review`

You are the executor of one slice of a plan in a task cycle of the-way (`implement-task`). The
person who requested the cycle has delegated intermediate choices to the orchestrator; nothing here
is the human's approval. Ask no human. A question you cannot settle from the files named here
returns with the status `questions`; a fact or permission no source gives returns `blocked`.

## Where and what you make

- Worktree (work from its root, never from another checkout): `the root of the task's worktree`, branch `task/scripts-after-foundation-review`. The-way is the checkout you work in; it is no product's `.the-way`. Target branch `foundations`; base of the task `7f5c5a56f67d9ff40554240594ca0bde59773cb3`. The foundation entries of the plan are already written on the branch (commits `da9d816` and `bfb774c`); read an entry as they left it.
- Method, read whole: `task-cycle/change/SKILL.md` (`make-change`); variant: **a slice, or the retry of a slice**. You read `task-cycle/change/slice.md` when its step comes, and each other file the method names only when the step or variant that names it comes. You have no skill tool: a skill a method names by its name alone is the `SKILL.md` whose frontmatter `name:` is that name, read as a file.
- Your stage and its boundary: make slice 8 of the plan and nothing else, commit it on the task branch (in English messages, files added by path, never `git add -A`, nothing under `.runs/`), and return before review. You run **no run of the whole gate** (WAY-160); you run the focused checks of the slice's *Checks*.
- Frozen task: `.runs/task-cycles/scripts-after-foundation-review/task.md`. Reviewed spec: `.runs/task-cycles/scripts-after-foundation-review/spec.md`. Plan: `.runs/task-cycles/scripts-after-foundation-review/plan.md` — your slice is copied below; read the other parts of these files only as your slice's *Read* names them.
- Answers of step 4: trust boundary **yes** — a slice whose *Risk* names a trust boundary changes a script that takes in untrusted data (a transcript, a register, a locations file, a copy of a record from git history, a price list): write the reading so that crafted input cannot make the script crash with a stack trace, write outside its places, run a command or put text of the input into a result unescaped; the review of the slice is told to check that. Irreversible operation: none.
- Your class of model: **same (the orchestrator's class)**.
- Directory for your working copies: `.runs/executor-8/` of the worktree.
- Report path: `.runs/task-cycles/scripts-after-foundation-review/reports/executor-8-report.md`, in the form `make-change` gives; with the **Unread material** (what this handoff names that stayed unread or was read in part, or `none`), **Searches not found or unclear** (each thing looked for and not found or unclear, or `none`), the own-work check, each check you ran with its command and exit code, the choices you made and the foundation entries or code you reached beyond what is named (what, where and why), and the working copies line.
- The tests of the slice are written first and fail on the base for the reason the slice gives; where the slice says a test is red on the base, the report states its failing run and its passing run.
- A change of a test that holds a sentence of a decision by a line `decision:` or an invariant's test is named in your report (WAY-03), so that the request names it.
- Another task changes `elements/common/foundation_check.py` and the sentence of WAY-344 in parallel; leave what is not in your slice alone.

## Your slice, copied from the plan word for word

### Slice 8 — A cycle that changed the tool that measures gives that tool's measures as unknown

- **Goal:** in `process-audit/audit_count.py`, a cycle of the-way whose own change changes the tool that wrote a file of its copy gives the measures that tool wrote as `unknown`, with the reason that the cycle changed the tool that wrote them, and the other measures of the cycle as it does today, under the version it ran on (WAY-339, row 4). The tools and what each wrote: `task-cycle/cycle_stages.py` — the times, the cost and the share of fix rounds from `stages.md`; `task-cycle/cycle_measures.py` — `mechanism_measures.md`; `task-cycle/gate_times.py` or `gate/run_tests.py` — `gate_times.md`. The tools are taken from what Slice 6 settled about series (the same paths, not a second list that can drift). The cycle changed the tool where the files of the tool differ between the version it ran on and the commit of its last copy of the record in the-way's own history (`git diff --quiet`, a failure counting as changed, as `differs` does); the executor names in its report how it finds that commit and why a cycle of another repository is left as it is (item 8 holds for cycles of `the-way` only), and a copy of an earlier cycle is not put in doubt by it. The comment at `MEASURES_FILE` ("A copy holding neither is an earlier form.") says what the module description says ("A copy that holds neither is of an earlier cycle or of one whose script failed"), in the same words (To do 9). The tests: for each of the three groups of tools, a cycle whose copy changes it gives that group's values `unknown` with the reason and the other values as before, and a cycle that changes none gives all as before.
- **Change:** `process-audit/audit_count.py` · `process-audit/test_audit_count.py`
- **Read:** `.runs/task-cycles/scripts-after-foundation-review/task.md:35-36` To do 8 and 9 · `.runs/task-cycles/scripts-after-foundation-review/task.md:70-74` Questions to settle 4 · `.runs/task-cycles/scripts-after-foundation-review/task.md:133-133` Decisions in play, WAY-339 · `.runs/task-cycles/scripts-after-foundation-review/task.md:146-146` Settlements to record, row 4 · `foundations/decisions.md:7384-7469` WAY-339 · `foundations/decisions.md:7471-7506` WAY-350 · `foundations/invariants.md:398-407` audit-series-script-paths · `foundations/invariants.md:116-145` script-language, script-imports, script-subprocesses · `foundations/part_map.md:101-111` task-cycle · `foundations/part_map.md:124-134` process-audit
- **Model:** same — a new reading of git history that must not put the cycles of earlier forms in doubt
- **Risk:** trust boundary — `process-audit/audit_count.py`
- **Checks:** start from the new tests of classes `MechanismMeasures`, `GateRunsMeasures` and `Times` (one per group of tools) and of class `ProcessVersions`, red on the base; `python -B -m unittest discover -s process-audit -p "test_audit_count.py" -k MechanismMeasures -k GateRunsMeasures -k Times -k ProcessVersions -k MeasureVersions`; then the whole file `python -B -m unittest discover -s process-audit -p "test_audit_count.py"` and `python -B -m unittest discover -s process-audit -p "test_audit_series_scripts.py"`
- **Depends on:** Slice 7 · Slice 6


## The foundation entries of your *Read* as they stand now

The ranges the plan names are those of the base. Where they differ from the plan's, these hold; find a passage of the plan or a range of code by its heading or name where an earlier slice changed its file.

- `foundations/decisions.md:7432-7585` WAY-339
- `foundations/decisions.md:7586-7622` WAY-350
- `foundations/invariants.md:398-407` audit-series-script-paths
- `foundations/invariants.md:116-125` script-language
- `foundations/invariants.md:126-135` script-imports
- `foundations/invariants.md:136-145` script-subprocesses
- `foundations/part_map.md:101-112` task-cycle
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
