# Handoff — slice 2

The person who requested this cycle delegated its intermediate choices to the orchestrator; no answer
here is that person's approval. You never ask the human: a question goes back to the orchestrator in
your report.

- Worktree (work only from its root): `the task's worktree root`, branch `task/cycle-technology-decisions-batch`. This is the-way itself; there is no pinned process.
- Your method and variant: `make-change` — read `task-cycle/change/SKILL.md` whole; your variant is **a slice, or the retry of a slice**, so read `task-cycle/change/slice.md` when the method sends you there. Read `agent-instructions/README.md` too.
- Stage and boundary: slice 2 of `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` only. Change only the files of the slice's *Change* line; commit them with `git add <path>` (no `git add -A`); commit messages in English. Run the slice's *Checks* yourself (focused; never the full `python -B gate/run_tests.py` without a directory). The slice's *Model* sets your class.
- Frozen task (read whole): `.runs/task-cycles/cycle-technology-decisions-batch/task.md` (Polish). Plan: `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` (your slice section is copied below word for word; the plan's *Foundation entries* and *Choices* are in the plan). No spec.
- Foundation entries already written in this cycle (commits `85c5395` .. `f3b90d5` on this branch, in `foundations/decisions.md`; the report is `.runs/task-cycles/cycle-technology-decisions-batch/reports/02-foundation-entries-report.md`): read the plan's *Foundation entries* table, then read the decisions your slice depends on in their current text. Row 1 is the **new decision WAY-322** (current range in the list below if your slice reads it); it covers every matter of an agent's way to the running product that the step lists — the base holds a fifth matter beyond the task's four, the place of the screenshots — and the failure notice; word your files to agree with it. WAY-165, WAY-166 and WAY-139 were reworded in place.
- Answers of step 4: trust boundary — no file of this slice is named as a trust boundary (the change as a whole touches one, in slice 3); irreversible operation — no.
- **Drift:** the task's line numbers and the plan's cite older commits; find each place by its content. Where the current text of a place already says what the item asks, change nothing there and say so in your report.
- Report path: `.runs/task-cycles/cycle-technology-decisions-batch/reports/04-slice-2-report.md` (full report as the method gives it, with the own-work check, **Searches not found or unclear**, reaches beyond this handoff, and each check with its command and exit code).
- Return: status, your commits, a one-line check result naming what failed or did not run, and the report path.

## The slice (plan section, word for word)

### Slice 2 — The slice executor's current ranges and the request template's two pointers

- **Goal:** (item 4) `task-cycle/change/slice.md` says that where the ranges of lines the dispatch gives differ from the ranges in the plan, the dispatch's current ranges hold, as `task-cycle/skill/planning.md` ("A slice's handoff") gives the orchestrator; (item 6, first point) in `task-cycle/skill/request_template.md` the item of *For you to decide* on *Questions* points to `task-cycle/skill/foundation_step.md`, the file that says which questions the foundation step allows; (item 6, second point) the item on additions to a product's logging scope says where the author of the request finds them: in the diff of the change to the product's logging-scope rule (WAY-274). Prose only.
- **Change:** `task-cycle/change/slice.md` · `task-cycle/skill/request_template.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:31-31` To do, item 4 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:33-35` To do, item 6 · `task-cycle/skill/planning.md:26-37` A slice's handoff · `task-cycle/skill/foundation_step.md` · `foundations/decisions.md:4119-4179` WAY-148 · `foundations/decisions.md:8480-8529` WAY-274 · `foundations/decisions.md:8982-9024` WAY-287 · `foundations/invariants.md:86-94` tracked-file-private-paths
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py --skip-test-citations` · `python -B -m unittest discover -s task-cycle -p "test_request_check.py"` · `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` · `git diff --check`
- **Depends on:** none

## Passages the slice reads

#### Task passage: To do, item 4 (task.md:31-31)

```text
4. Skill wykonawcy kawałka (`task-cycle/change/`) mówi, że gdy zakresy linii w zleceniu różnią się od zakresów z planu, obowiązują bieżące (theway#039-3; reguła dla prowadzącego stoi w `skill/planning.md:36-37`).
```

#### Task passage: To do, item 6 (task.md:33-35)

```text
6. W szablonie opisu PR-a (`skill/request_template.md`):
   - punkt *Questions* wskazuje plik `skill/foundation_step.md`, który mówi, na jakie pytania krok fundamentu pozwala (theway#050-3; `:165`);
   - punkt o dopisaniach do listy tego, co produkt loguje, mówi, gdzie ich szukać: w zmianie reguły zakresu logowania produktu w diffie (theway#074-3; `:219-221`).
```

## Entries and files the slice reads, with current ranges

- `task-cycle/skill/planning.md:26-37` A slice's handoff
- `task-cycle/skill/foundation_step.md`
- `foundations/decisions.md:4141-4208` WAY-148 (current range)
- `foundations/decisions.md:8528-8577` WAY-274 (current range)
- `foundations/decisions.md:9030-9074` WAY-287 (current range)
- `foundations/invariants.md:86-94` tracked-file-private-paths
