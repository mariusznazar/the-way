# Return step report — gate-parallel-directories

**Status:** done. **Commits:** none. The foundation held nothing that no longer matched the code at head `9282e6f`
(range `f749cfc`..`9282e6f`), so nothing was corrected and the worktree is clean (`git status --short` prints nothing).

## What was compared with the code

| Entry | Compared with | Result |
|---|---|---|
| WAY-366 (row 1) | `gate/run_tests.py` and its tests: default all directories at once, `--jobs N`, `--jobs 1` one after another, each report whole under its `== <directory>` line when its process ends | matches, including the interrupt fix (queued directories are cancelled) |
| WAY-367 (row 2) | step 4 of `task-cycle/skill/SKILL.md` (the check in git, no base run, the list from the merged branch's record copy, the source written into *Verification*, the fall back to running the gate, the run of the failing tests on the base), `record_template.md` *Verification*, `request_template.md` item 4 and *Checks* | matches in each sentence of the binding part and of *Verification* |
| WAY-349 (changed) | step 10 and step 2 of `SKILL.md`, `record_template.md` line 100 and *Verification* | matches: the run on the starting state goes through the script only in a cycle that makes it, and the file is created by the first run that is made |
| WAY-16, WAY-55, WAY-160, WAY-243 (the task's *Decisions in play*) | the same files | unchanged and true: one gate command with the option inside it (WAY-16); runner in `gate/`, the cycle decides when it runs (WAY-55); the orchestrator alone runs the gate and the list rests on its result (WAY-160); the run of the failing tests on the base is diagnosis only (WAY-243) |
| WAY-350, WAY-63 (found by the search) | `gate_times.py` and its new test; the exit codes of the runner | WAY-350 still counts runs of the script (a directory inside a run is no other run); WAY-63 and invariant `gate-exit-code` read the same as the runner behaves (its tests pass); the new exit code 2 for a wrong `--jobs` or `--slowest` is an error of the call |
| Part map: `gate`, `task-cycle` (trust boundary `task-cycle/gate_times.py`), `agent-instructions`, `test-runner-command` | the files changed | matches. `gate_times.py` is unchanged and its test now reads the real runner's output. `test-runner-command` says the command keeps "its name, its argument and its exit codes": the name, the argument DIRECTORY and the exit codes are kept; the surface sentence does not name the two options, and the task's *Context* says the new option does not violate it, so it is left as it is |

Search for stale words, run over the tracked files outside `docs/` (`passed on the base`, `16 minutes`, `run on the
base`, `the base alone`, `starting state`): every hit reads true after the change. `agent-instructions/README.md:59`
says "about 16 minutes with `--jobs 1`, and less by default"; the 16 minutes is the old measured time, and "less by
default" is unmeasured here (the full run is the orchestrator's), so the orchestrator may replace it with the time its own
`gate_times.md` row gives.

## What the step writes

- **Decisions written or changed:** none in this step (WAY-366, WAY-367 and the change to WAY-349 were written by the
  foundation step, in `9bea9a1`).
- **Invariants:** none. No rule of the task, a decision or the human asks for one beyond `gate-exit-code`, which holds.
- **Environment facts:** none. The change rests on `unittest`'s `durations` parameter (Python 3.12 and later) and on
  git's `<commit>^2^{tree}`; no decision's *Based on* and no invariant's *Rests on* needs either, and the template writes a
  fact only for those two uses (WAY-90, WAY-73).
- **Glossary terms:** none. The words the change uses (gate, starting state, directory, report) carry their ordinary
  or already-entered meaning; no term is used against its entry.
- **Part-map changes:** none.
- **Choices that bind after the merge (WAY-36):** none written. The author's choices (the option names, all directories at
  once as the default, the failed directories in the order of their names, `--jobs` ignored with a directory, the last
  copy of a record) stand in the runner's docstring, the README, step 4 and the report `author-report.md`; the task and
  WAY-366 settle what binds the process, and these bind only through those files, so they stay rows of the questions table.
- **Rows of *Settlements to record*:** both written by the foundation step: row 1 as WAY-366, row 2 as WAY-367.
- **Projected entries:** none (an independent task).

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `git status --short` | 0 | clean |

No other check was run: nothing was committed, and the handoff asks for focused checks only where something is committed.

## Reaches beyond the handoff

`foundations/environment_facts.md` (the list of its headings and `elements/environment-facts/template.md`, lines 1 to 60, for
the rule on which facts are written), to decide the environment-facts line above. Nothing else.

## Unread material

- `elements/environment-facts/template.md` after line 60 and the entries of `foundations/environment_facts.md` (headings
  only).
- `reports/whole-review-report.md` and `reports/fix-review-report.md`: not opened (the handoff says their Minor findings are
  not for this step).
- The rest named by the handoff I read whole: the handoff, `task-cycle/skill/return_step.md`, `foundation_step.md` (in the
  author's work, earlier) and the entries named above (read at the foundation step and again by `grep` and the diffs of this
  step, not reread whole from the heading for WAY-16, 55, 160, 243, 350 and 63).

## Searches not found or unclear

- The method says to write an environment fact for each source outside the product that the change rests on; its
  template limits the facts to those a decision or an invariant rests on, so I found no fact to write and say so rather
  than add one no entry cites. If the orchestrator holds that the `durations` parameter is such a source, the entry is
  its call.
- The handoff names no entry beyond the change's own, so "the entries the task names" were taken from the task's *Decisions
  in play*.
