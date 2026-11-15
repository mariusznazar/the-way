# Executor report — slice 20: the guidelines of the kinds `repository-changer` and `command-runner`

**Status:** done with concerns

**Commits** (branch `task/the-way-coding-and-testing-guidelines`, base `cb6c208`):
- `f7c64a2` Write the guidelines of the kinds repository-changer and command-runner
- `734798f` Leave the exit codes and the fixed code of the wrong use out of the two kinds' guidelines (a value copied from code or a decision, which the slice's Goal rules out; made as a second commit, not an amend)

**Check result:** no check failed. `foundation_check.py` exit 0; `tracked-file-private-paths` exit 0. Nothing skipped except the gate, which I never run.

**Report path:** `.runs\task-cycles\the-way-coding-and-testing-guidelines\reports\executor-20-report.md`

## Files changed

- `guidelines\coding-repository-changer.md` — new, 47 lines (commit `f7c64a2`); second commit changed 2 lines.
- `guidelines\coding-command-runner.md` — new, 42 lines (commit `f7c64a2`); second commit changed 5 lines.

Form: the same as the sibling kind files already in the base (`coding-generator.md`, `coding-shared-module.md`, `coding-check.md`): heading, *Discipline*, *Applies to*, *When to read*, `## Files of this kind` (File | Status | Decision), `## Rules` with one rule (*Decision*, *Invariant*, *Good*, *Bad*, how to apply), `## Examples` with "The rest of the exemplar", `## Where in code`.

## Status of each row, checked against the code

**`repository-changer`** (rule: E25 `repository-changer-acts-only-when-told`, decision WAY-389)

- `task-cycle/remove_merged_worktrees.py` — `exemplar` (WAY-389). Read whole. The removal runs only where `arguments.apply` is set (`run()`, the line `applied = apply_removals(...) if arguments.apply else None`); without it only `report()` runs. The one step before the gate is the fetch, which moves remote-tracking refs inside `.git`, not a tracked file, and `--no-fetch` skips it. Probe: exit 0, git state unchanged. Consistent with the exemplar role.
- `elements/common/migrate_foundation.py` — `copy`. Read in `run()`, `main()` and the default report path. Tracked files are written and removed only under `if apply:`. Without `--apply` it writes only its report, by default to `.runs/foundation_migration.md`, which `.gitignore` line 2 ignores. Probe: `python -B elements/common/migrate_foundation.py . --report <a path under .runs/executor-20/>` exit 1, which is the script's own count of "14 places for a human" with 0 changes; git state unchanged. **Concern:** `--report PATH` takes any path, and `run()` opens it with mode `"w"` before the gate (about lines 948–951). A trial given a tracked file as `--report` overwrites that file, which breaks the invariant's wording ("change no file that the repository tracks"). I did not probe that case, since it overwrites a file. Kept `copy` as the plan says; see question 1.
- `installation/install.py` — `do not copy`. Its act gate holds: without `--apply` it prints "Preview only" and returns before any write (`run()`, about lines 633–635); the confirmation is about line 641; `verify_remote` and every write come after it (from about line 646). The `do not copy` reason is the missing-field handling, not the gate: `skill_wrapper` raises `RuntimeError` on a missing description (lines 135–136), and the `__main__` block turns any such error into `Error:` with exit 1 (lines 690–693), while WAY-388 says WAY-344 gives exit code 2 for a missing field. Not run (read only).

**`command-runner`** (rule: E26 `command-runner-passes-exit-code`, decision WAY-390)

- `task-cycle/gate_times.py` — `exemplar` (WAY-390). Read whole. `exit_code()` returns the child's code, or `128 - code` for a negative code, which is a signal (lines 269–270); `main()` returns that code unchanged (line 325). Exit 2 is used only for the script's own failures (lines 278, 305, 324). Probes: child `sys.exit(7)` gave exit 7; child `sys.exit(0)` gave exit 0. The signal branch is read, not probed.
- `gate/run_tests.py` — `copy`. It runs no command it is given. It starts itself once per test directory (`run_directory`, command `[sys.executable, -B, <itself>, <directory>]`) and ends with its own 0, 1 or 2. The command-runner rule does not reach it. Kept `copy` as the plan's allocation; see question 2.

## Choices made

- **Rule's *Decision* field** = the decision that designates the exemplar (WAY-389 for `repository-changer`, WAY-390 for `command-runner`), since the rule's sentence is that designation's. Rejected: naming the E25/E26 entries, which have no decision identifier. Cost if wrong: a reviewer expects another decision; low.
- **Applies to** = the parts the kind's files lie in, as the invariants' *Part* fields and the decisions' *Scope* fields give: `task-cycle · elements-common · installation` and `task-cycle · gate`. Rejected: `task-cycle` alone, which would leave the other files' parts unnamed. Cost if wrong: a standing check that reads the parts would miss a file; none found.
- **Sentence on reports**: "A report may be written to a path that git ignores." Rejected: saying nothing about reports, which would make the trial's report look like a violation of the rule. Cost if wrong: small; it is the author's instruction, and it is the very case of question 1.
- **Examples carry no values** (no exit codes, no numbers), since the Goal says "No value is copied from code or a decision". The *Bad* line of `command-runner` says "one fixed exit code" instead of the decision's "exit code 1". The one value left is `128 plus the signal number` in the rule itself, which is the invariant's own sentence (the rule the Goal names), not a copy of code.
- **Good / Bad lines** are my wording; the template allows one line each.
- **Rule kept to the invariant**: no rule text beyond what E25 and E26 state, plus the report sentence above. The exemplars' other behaviour is only an example.

## Own-work check (`make-change` section 3)

- **Requirement most likely not met:** each status matches the code, and no example copies a value from code. **Check:** read each file's act gate and exit path; probes listed below; grep of the two files for `exit`, `128`, numbers.
- **What it showed:** statuses match the code for the exemplars and for `install.py`. `migrate_foundation.py` `copy` is contradicted only by the `--report` edge (question 1). Two examples carried exit codes; the second commit removed them.
- No check failed, so there is no pair of failing and passing runs to report.

## Checks run (command and exit code)

1. `python -B elements/common/foundation_check.py` — exit 0 ("0 errors"), run after the first commit's files and after the second commit's edit.
2. `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` — exit 0 ("checked: 322 files, 0 listed").
3. `python -B task-cycle/gate_times.py --output <.runs/executor-20>/probe.md --registry <.runs/executor-20>/registry -- python -c "import sys; sys.exit(7)"` — exit 7.
4. The same command with `sys.exit(0)` — exit 0.
5. `python -B task-cycle/remove_merged_worktrees.py --no-fetch --repository .` — exit 0; the dry run printed a `keep` or `remove` line with reasons for each directory and removed nothing (the output file is gone with the working copy; I saw only its last lines); `git status --porcelain` before and after the two probes (5 and 6) was identical.
6. `python -B elements/common/migrate_foundation.py . --report <.runs/executor-20>/migration_trial.md` — exit 1 (the script's own count of 14 places for a human, 0 changes written); git state unchanged.
7. `git status --porcelain` after the second commit — empty.

**Not run, with reasons:** the product gate `python -B gate/run_tests.py` without a directory (forbidden for this cycle, WAY-160); the invariant tests of the scripts (not in this slice's *Checks*, and I wrote no test); `installation/install.py` (only read, since it plans against the environment and the remote).

## Working copies

- `.runs/executor-20/` in the worktree: holds the probe outputs of checks 3–6 (probe record, gate registry folder, the two trial outputs). It stood there only for those probes. **Removed** with `rm -rf` before this report; nothing kept, since every result is in this report. No worktree or clone was made.

## Questions (each with the recommended answer)

1. **`elements/common/migrate_foundation.py` is `copy`.** Its `--report PATH` writes to any path before the act gate (about lines 948–951), so a trial with a tracked file as `--report` overwrites that file. Options: (a) keep `copy` and make the script refuse a tracked report path, a code change outside this slice; (b) mark it `do not copy` now. **Recommended: (b) now**, and set it back to `copy` when (a) lands. Cost of (b): the table says the file is not a model to copy, which is true until (a) lands. Cost of keeping `copy`: a later repository changer copies a trial that writes tracked files when given a tracked path.
2. **`gate/run_tests.py` is `copy` in `command-runner`, though it wraps no command**, so the rule does not reach it. Options: (a) keep the row as the plan allocates it; (b) remove the row. **Recommended: (a)**, since the audit allocated it and the row says `copy`, not an exemplar. Cost of (a): a reader may take its exit-code handling as a model for the rule, which the example section does not warn about. Cost of (b): the audit's list of the kind's files no longer matches.
3. **`guidelines/coding.md` is not in the base**, so its "Kinds of code" table has no rows for these two kinds. The plan puts `guidelines/coding.md` in Slice 21 (`plan.md`, from line 802). **Recommended:** confirm that Slice 21 adds a row for `repository-changer` (file `guidelines/coding-repository-changer.md`) and one for `command-runner` (file `guidelines/coding-command-runner.md`). I did not read Slice 21, so this is unclear to me.

## Unread material

- `foundations/invariants.md`: `script-language`, `script-imports`, `script-subprocesses`, `cross-part-imports`, `test-method-citation` — not read. The orchestrator's addition applies them to slices that add or edit a Python file; this slice adds none.
- `.runs/task-cycles/the-way-coding-and-testing-guidelines/plan.md`: Slices 13 and 14 (only their heading lines, found by grep at lines 508 and 545) — not read; not used by this slice's text.
- `foundations/decisions.md` WAY-344 (heading at line 2823) — not read; WAY-388's sentence stands in for it.
- Everything else the handoff names was read in the ranges it gives, or in wider ranges that contain them: `task.md` lines 28, 130–147, 218–224, 531–532 (read as 120–230 and 525–536); E8 (WAY-386 to WAY-391), E25, E26; decisions WAY-167, WAY-168, WAY-173, WAY-312, WAY-198, WAY-199; `invariants.md` `tracked-file-private-paths` (86–95), `repository-file-location`, `ci-checking-commands`, `derived-file-content`, `map-reference-target`, `guidelines-file-place`; `product-guidelines/template.md` and `product-guidelines/coding/template.md` (whole); `task-cycle/remove_merged_worktrees.py` and `task-cycle/gate_times.py` (whole); the plan's *Choices* and "Orchestrator's additions" (lines 1003–1041) and Slice 20's section.

## Reach beyond the handoff

- `plan.md` Slice 18 and Slice 19 sections (lines 689–768): to see the form that "Slice 18 gives".
- Sibling kind files already in the base: `guidelines/coding-shared-module.md`, `guidelines/coding-generator.md`, `guidelines/coding-check.md` (whole): to match their form.
- `installation/install.py` (lines 1–40, 120–150, 560–693, and grep of the rest), `elements/common/migrate_foundation.py` (grep, lines 83 and 918–992), `gate/run_tests.py` (lines 1–150): to check the statuses against the code.
- `.gitignore` line 2 (grep); `plan.md` lines 802 and 938 (grep): to find which slice owns `guidelines/coding.md`.
- Global rules read before the commit and the writing: `a file of the author's private notes`, `...\.ai\rules\knowledge_artifacts.md`, `...\.ai\rules\scripts.md` (the last was delivered by a hook after a blocked call; I re-ran the call).

## Searches not found or unclear

- `guidelines/coding.md`: absent in the base; whether Slice 21 adds the two kinds' rows is unclear to me (question 3).
- Whether `gate/run_tests.py` belongs to the kind `command-runner` (question 2).
- Whether an invariant's wording covers a `--report` path given by the human (question 1).
- The base tests of the two invariants (E25 and E26): not located or run by me; not part of this slice's *Checks*.

## Addendum — orchestrator's answers and the change they require

The orchestrator answered the three questions (recorded as its autonomous choices, not the human's approval):

1. Done. `elements/common/migrate_foundation.py` is now `do not copy` in the table of `guidelines/coding-repository-changer.md`. The file's note under the table gives the reason, names function `run()` (not a line), and says the status is a finding of this slice's check against the code, not of the audit of the kinds. Commit `316a698` (Mark migrate_foundation.py do not copy in the repository changer's guidelines).
2. Kept. `gate/run_tests.py` stays `copy` in `guidelines/coding-command-runner.md`, as the plan allocates it.
3. Accepted. Slice 21 writes the index rows of all six kinds in `guidelines/coding.md`; no row was added by this slice.

Checks rerun after the change to `guidelines/coding-repository-changer.md`:
- `python -B elements/common/foundation_check.py` — exit 0 ("0 errors")
- `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` — exit 0 ("checked: 322 files, 0 listed")

Commits of this slice now: `f7c64a2`, `734798f`, `316a698`. `git status --porcelain` is empty.
