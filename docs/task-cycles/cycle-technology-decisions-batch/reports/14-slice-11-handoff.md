# Handoff — slice 11

The person who requested this cycle delegated its intermediate choices to the orchestrator; no answer
here is that person's approval. You never ask the human: a question goes back to the orchestrator in
your report.

- Worktree (work only from its root): `the task's worktree root`, branch `task/cycle-technology-decisions-batch`. This is the-way itself; there is no pinned process.
- Your method and variant: `make-change` — read `task-cycle/change/SKILL.md` whole; your variant is **a slice, or the retry of a slice**, so read `task-cycle/change/slice.md` when the method sends you there. Read `agent-instructions/README.md` too.
- Stage and boundary: slice 11 of `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` only. Change only the files of the slice's *Change* line; commit them with `git add <path>` (no `git add -A`); commit messages in English. Run the slice's *Checks* yourself (focused; never the full `python -B gate/run_tests.py` without a directory). The slice's *Model* sets your class.
- Frozen task (read whole): `.runs/task-cycles/cycle-technology-decisions-batch/task.md` (Polish). Plan: `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` (your slice section is copied below word for word; the plan's *Foundation entries* and *Choices* are in the plan). No spec.
- Foundation entries already written in this cycle (commits `85c5395` .. `f3b90d5` on this branch, in `foundations/decisions.md`; the report is `.runs/task-cycles/cycle-technology-decisions-batch/reports/02-foundation-entries-report.md`): read the plan's *Foundation entries* table, then read the decisions your slice depends on in their current text. Row 1 is the **new decision WAY-322** (current range in the list below if your slice reads it); it covers every matter of an agent's way to the running product that the step lists — the base holds a fifth matter beyond the task's four, the place of the screenshots — and the failure notice; word your files to agree with it. WAY-165, WAY-166 and WAY-139 were reworded in place.
- Answers of step 4: trust boundary — no file of this slice is named as a trust boundary (the change as a whole touches one, in slice 3); irreversible operation — no.
- **Drift:** the task's line numbers and the plan's cite older commits; find each place by its content. Where the current text of a place already says what the item asks, change nothing there and say so in your report.
- Report path: `.runs/task-cycles/cycle-technology-decisions-batch/reports/14-slice-11-report.md` (full report as the method gives it, with the own-work check, **Searches not found or unclear**, reaches beyond this handoff, and each check with its command and exit code).
- Return: status, your commits, a one-line check result naming what failed or did not run, and the report path.

## The slice (plan section, word for word)

### Slice 11 — Part map: the task cycle depends on the installer

- **Goal:** (item 29) in `foundations/part_map.md` the part `task-cycle` lists `installation` in its *Depends on*, because the cycle skill sends the agent to `installation/README.md` for moving the pin (`installation` and `task-cycle` then depend on each other, as `installation` and `product-guidelines` already do). Follow the skill of the part-map element (`elements/part-map/skill/SKILL.md`) for the edit and WAY-33 for the search of the whole foundation afterwards. No other entry of the map changes.
- **Change:** `foundations/part_map.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:78-78` To do, item 29 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:102-107` Questions to settle, question 4 · `task-cycle/skill/SKILL.md:37-48` step 2, the move of the pin · `installation/README.md:78-116` Moving the pin · `foundations/decisions.md:872-904` WAY-33 · `foundations/decisions.md:1113-1163` WAY-44 · `foundations/decisions.md:9426-9479` WAY-299 · `foundations/invariants.md:146-155` map-reference-target · `foundations/invariants.md:328-336` cross-part-imports · `elements/part-map/skill/SKILL.md` · `elements/part-map/skill/decide_entry.md` · `elements/part-map/skill/write.md` · `elements/part-map/template.md`
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B elements/common/foundation_check.py --skip-test-citations` · `python -B gate/run_tests.py elements/part-map` · `git diff --check`
- **Depends on:** none

## Passages the slice reads

#### Task passage: To do, item 29 (task.md:78-78)

```text
29. Mapa części dopisuje `installation` do *Depends on* części `task-cycle`, bo skill cyklu przy przesuwaniu przypięcia odsyła do `installation/README.md` (pytanie 4; theway#050-9; `task-cycle/skill/SKILL.md:41-43`, `foundations/part_map.md:98-99`).
```

#### Task passage: Questions to settle, question 4 (task.md:102-107)

```text
- Pytanie 4: czy cykl zadania może zależeć od instalatora?
  - Answer: tak; mapa części dopisuje `installation` do zależności `task-cycle`, a przepis przesunięcia przypięcia zostaje w `installation/README.md`. Słaby punkt przyjęty z tą drogą: `task-cycle` i `installation` zależą od siebie nawzajem, jak już `product-guidelines` i `installation`.
  - Not chosen:
    - skill cyklu sam opisuje przesunięcie przypięcia — ten sam przepis w dwóch miejscach, które rozjadą się przy następnej zmianie instalatora.
    - zostawić mapę i zapisać rozjazd jako znany — mapa dalej nie mówi prawdy, a każdy krok powrotu zgłosi to od nowa.
  - Source: Mariusz, 2026-11-08: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; `foundations/part_map.md:98-99`, `task-cycle\skill\SKILL.md:41-43`, `foundations` `a3206c1`.
```

## Entries and files the slice reads, with current ranges

- `task-cycle/skill/SKILL.md:37-48` step 2, the move of the pin
- `installation/README.md:78-116` Moving the pin
- `foundations/decisions.md:875-907` WAY-33 (current range)
- `foundations/decisions.md:1116-1166` WAY-44 (current range)
- `foundations/decisions.md:9488-9541` WAY-299 (current range)
- `foundations/invariants.md:146-155` map-reference-target
- `foundations/invariants.md:328-336` cross-part-imports
- `elements/part-map/skill/SKILL.md`
- `elements/part-map/skill/decide_entry.md`
- `elements/part-map/skill/write.md`
- `elements/part-map/template.md`
