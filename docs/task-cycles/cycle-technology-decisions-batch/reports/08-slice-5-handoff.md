# Handoff — slice 5

The person who requested this cycle delegated its intermediate choices to the orchestrator; no answer
here is that person's approval. You never ask the human: a question goes back to the orchestrator in
your report.

- Worktree (work only from its root): `the task's worktree root`, branch `task/cycle-technology-decisions-batch`. This is the-way itself; there is no pinned process.
- Your method and variant: `make-change` — read `task-cycle/change/SKILL.md` whole; your variant is **a slice, or the retry of a slice**, so read `task-cycle/change/slice.md` when the method sends you there. Read `agent-instructions/README.md` too.
- Stage and boundary: slice 5 of `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` only. Change only the files of the slice's *Change* line; commit them with `git add <path>` (no `git add -A`); commit messages in English. Run the slice's *Checks* yourself (focused; never the full `python -B gate/run_tests.py` without a directory). The slice's *Model* sets your class.
- Frozen task (read whole): `.runs/task-cycles/cycle-technology-decisions-batch/task.md` (Polish). Plan: `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` (your slice section is copied below word for word; the plan's *Foundation entries* and *Choices* are in the plan). No spec.
- Foundation entries already written in this cycle (commits `85c5395` .. `f3b90d5` on this branch, in `foundations/decisions.md`; the report is `.runs/task-cycles/cycle-technology-decisions-batch/reports/02-foundation-entries-report.md`): read the plan's *Foundation entries* table, then read the decisions your slice depends on in their current text. Row 1 is the **new decision WAY-322** (current range in the list below if your slice reads it); it covers every matter of an agent's way to the running product that the step lists — the base holds a fifth matter beyond the task's four, the place of the screenshots — and the failure notice; word your files to agree with it. WAY-165, WAY-166 and WAY-139 were reworded in place.
- Answers of step 4: trust boundary — no file of this slice is named as a trust boundary (the change as a whole touches one, in slice 3); irreversible operation — no.
- **Drift:** the task's line numbers and the plan's cite older commits; find each place by its content. Where the current text of a place already says what the item asks, change nothing there and say so in your report.
- Report path: `.runs/task-cycles/cycle-technology-decisions-batch/reports/08-slice-5-report.md` (full report as the method gives it, with the own-work check, **Searches not found or unclear**, reaches beyond this handoff, and each check with its command and exit code).
- Return: status, your commits, a one-line check result naming what failed or did not run, and the report path.

## The slice (plan section, word for word)

### Slice 5 — The installer test no longer depends on the commit that is current when it runs

- **Goal:** (item 9) `installation/test_install.py`: the test `test_moving_the_pin_to_the_same_process_changes_only_the_gitlink`, and any other test in the file that compares with `self.commit` taken in `setUp`, does not fail when someone commits to the-way's own repository while the full test run is going. The expected commit is taken from what the test installs from, at the point it installs, not from a read made earlier of the live repository's head (the places: `setUp`, `installed_from_a_remote`, `later_process`, the assertions of that test and of `test_guidance_names_only_scripts_the_pinned_commit_holds`). No change to the installer's behaviour and to `installation/install.py`. Show the failure the item describes before the fix, for example with a throwaway copy of the repository in which a commit is made between `setUp` and the install, and say in the report how it was shown.
- **Change:** `installation/test_install.py`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:42-42` To do, item 9 · `installation/README.md:78-116` Moving the pin · `foundations/invariants.md:291-299` installation-claude-guidance · `foundations/part_map.md:157-165` installation · `foundations/decisions.md:905-940` WAY-34
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B -m unittest discover -s installation -p "test_install.py"` · `python -B -m unittest discover -s installation -p "test_installed_guidance.py"` · `git diff --check`
- **Depends on:** none

## Passages the slice reads

#### Task passage: To do, item 9 (task.md:42-42)

```text
9. Test instalatora `test_moving_the_pin_to_the_same_process_changes_only_the_gitlink` nie pada, gdy w trakcie pełnego przebiegu testów ktoś zrobi commit w repozytorium the-way (theway#070-12; `installation/test_install.py:39`, `:145-149`, `:216`, `:228`).
```

## Entries and files the slice reads, with current ranges

- `installation/README.md:78-116` Moving the pin
- `foundations/invariants.md:291-299` installation-claude-guidance
- `foundations/part_map.md:157-165` installation
- `foundations/decisions.md:908-943` WAY-34 (current range)
