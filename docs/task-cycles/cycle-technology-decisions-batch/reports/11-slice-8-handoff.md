# Handoff — slice 8

The person who requested this cycle delegated its intermediate choices to the orchestrator; no answer
here is that person's approval. You never ask the human: a question goes back to the orchestrator in
your report.

- Worktree (work only from its root): `the task's worktree root`, branch `task/cycle-technology-decisions-batch`. This is the-way itself; there is no pinned process.
- Your method and variant: `make-change` — read `task-cycle/change/SKILL.md` whole; your variant is **a slice, or the retry of a slice**, so read `task-cycle/change/slice.md` when the method sends you there. Read `agent-instructions/README.md` too.
- Stage and boundary: slice 8 of `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` only. Change only the files of the slice's *Change* line; commit them with `git add <path>` (no `git add -A`); commit messages in English. Run the slice's *Checks* yourself (focused; never the full `python -B gate/run_tests.py` without a directory). The slice's *Model* sets your class.
- Frozen task (read whole): `.runs/task-cycles/cycle-technology-decisions-batch/task.md` (Polish). Plan: `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` (your slice section is copied below word for word; the plan's *Foundation entries* and *Choices* are in the plan). No spec.
- Foundation entries already written in this cycle (commits `85c5395` .. `f3b90d5` on this branch, in `foundations/decisions.md`; the report is `.runs/task-cycles/cycle-technology-decisions-batch/reports/02-foundation-entries-report.md`): read the plan's *Foundation entries* table, then read the decisions your slice depends on in their current text. Row 1 is the **new decision WAY-322** (current range in the list below if your slice reads it); it covers every matter of an agent's way to the running product that the step lists — the base holds a fifth matter beyond the task's four, the place of the screenshots — and the failure notice; word your files to agree with it. WAY-165, WAY-166 and WAY-139 were reworded in place.
- Answers of step 4: trust boundary — no file of this slice is named as a trust boundary (the change as a whole touches one, in slice 3); irreversible operation — no.
- **Drift:** the task's line numbers and the plan's cite older commits; find each place by its content. Where the current text of a place already says what the item asks, change nothing there and say so in your report.
- Report path: `.runs/task-cycles/cycle-technology-decisions-batch/reports/11-slice-8-report.md` (full report as the method gives it, with the own-work check, **Searches not found or unclear**, reaches beyond this handoff, and each check with its command and exit code).
- Return: status, your commits, a one-line check result naming what failed or did not run, and the report path.

- **Foundation entry row 3 (read it, it binds this slice):** the foundation step reworded `foundations/decisions.md` WAY-139 in place (commit `a0c6607`; `derives from WAY-165` added to it): its item "how to read the logs" is now tied to the logs decision as the items on the record's life and on a failure are. Read WAY-139 whole in its current text (range above) and word `project-level/task/skill/resolve_gaps.md` to agree with it; the report of that step is `.runs/task-cycles/cycle-technology-decisions-batch/reports/02-foundation-entries-report.md`.


## The slice (plan section, word for word)

### Slice 8 — The refinement skill: the logs item, lasting exclusions and the split

- **Goal:** the refine-task skill says, each place found by its content: (item 16 and row 3) in `project-level/task/skill/resolve_gaps.md` the deployment-skill check handles three items apart, how to read the logs, how long the record of the logs lives and how a human learns of a failure: where a decision of the foundation or an approved definition the task carries answers the item, the refinement quotes it with its location and asks nothing, and the task's *To do* gains the item that writes the answer into the skill; a logs decision silent on how an agent reads the logs answers nothing for that item, as one silent on the record's life answers nothing for the item on the record's life; without such a decision the item goes as it does today. Foundation entry row 3 is written before this slice and binds it; word the file to agree with it. (item 25) `project-level/task/template.md`, under *Out of scope*, says that an exclusion that lasts beyond the task and that later work builds on is a decision candidate — a row of *Settlements to record* or a decision — as `project-level/task/skill/SKILL.md` ("Carry the foundation decisions", WAY-26) says; where the current sentence already says it, change nothing. (item 30) in `project-level/task/skill/read_sources.md` the sentence "Check that this is one task. If it joins independent outcomes, identify the split." is replaced by the sentence item 30 gives, word for word. Prose only.
- **Change:** `project-level/task/skill/resolve_gaps.md` · `project-level/task/template.md` · `project-level/task/skill/read_sources.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:52-52` To do, item 16 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:70-70` To do, item 25 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:79-79` To do, item 30 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:96-101` Questions to settle, question 3 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:172-172` Settlements to record, row 3 · Foundation entries row 3 · `project-level/task/skill/SKILL.md:48-52` 4. Carry the foundation decisions · `foundations/decisions.md:400-439` WAY-13 · `foundations/decisions.md:685-714` WAY-26 · `foundations/decisions.md:3760-3820` WAY-139 · `foundations/decisions.md:4754-4838` WAY-165 · `foundations/part_map.md:77-91` project-level
- **Model:** cheaper
- **Risk:** none
- **Checks:** `python -B gate/run_tests.py project-level` · `python -B elements/common/foundation_check.py --skip-test-citations` · `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` · `git diff --check`
- **Depends on:** Foundation entries row 3

## Passages the slice reads

#### Task passage: To do, item 16 (task.md:52-52)

```text
16. WAY-139 wiąże pozycję skilla wdrożenia „how to read the logs” z decyzją o logach tak jak pozycje o życiu zapisu i o awarii: gdy decyzja fundamentu albo zatwierdzonej definicji, którą zadanie niesie, na to odpowiada, doprecyzowanie ją cytuje, a zadanie dostaje punkt, który przepisuje odpowiedź do skilla; bez takiej decyzji pozycja idzie jak dziś. `project-level/task/skill/resolve_gaps.md` mówi to samo (pytanie 3; theway#024-9; WAY-165 „how an agent reads it”).
```

#### Task passage: To do, item 25 (task.md:70-70)

```text
25. Szablon zadania mówi, że trwałe wykluczenie, na którym opiera się dalsza praca, należy do decyzji, jak `project-level/task/skill/SKILL.md:51` (theway#041-2; `project-level/task/template.md:203-204`).
```

#### Task passage: To do, item 30 (task.md:79-79)

```text
30. Krok czytania źródeł przy doprecyzowaniu zadania zaczyna od jednego zadania i dzieli je tylko z nazwanego powodu (AIR-618 — Mariusz w kilku sesjach cofał rekomendowany podział; `project-level/task/skill/read_sources.md:23`): zdanie „Check that this is one task. If it joins independent outcomes, identify the split.” → „Check that this is one task. Keep one task by default: each split adds a full cycle. Identify a split only where a part cannot start or finish without something outside this refinement — access the agent lacks, another task's result — or where a later step of this skill offers one, and name that reason; a task's size alone (WAY-13) you name as a signal and leave the split to the human.”
```

#### Task passage: Questions to settle, question 3 (task.md:96-101)

```text
- Pytanie 3: które miejsce odpowiada, jak czytać logi wdrożonego produktu — skill wdrożenia (WAY-139) czy decyzja o logach (WAY-165)?
  - Answer: decyzja o logach; WAY-139 wiąże pozycję „how to read the logs” z decyzją fundamentu albo zatwierdzonej definicji tak jak pozycje o życiu zapisu i o awarii, a skill powtarza jej odpowiedź; bez takiej decyzji pozycja idzie jak dziś, jako punkt *To do*. Słaby punkt przyjęty z tą drogą: skill dalej powtarza tekst decyzji, więc zmiana decyzji wymaga przepisania go do skilla.
  - Not chosen:
    - skill mówi, jak logi czyta człowiek, a decyzja, jak czyta je agent — dalej dwie odpowiedzi, zwykle takie same, więc mogą się rozjechać.
    - zostawić jak jest — rozjazd wychodzi dopiero, gdy agent trafi na dwa różne przepisy.
  - Source: Mariusz, 2026-11-08: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; WAY-139 `foundations/decisions.md:3642-3652`, WAY-165 `:4636-4638`, `foundations` `a3206c1`.
```

#### Task passage: Settlements to record, row 3 (task.md:172-172)

```text
| 3 | Pozycję skilla wdrożenia „how to read the logs” wiąże się z decyzją o logach tak jak pozycje o życiu zapisu i o awarii; skill powtarza jej odpowiedź. | decision | pytanie 3 | czy zmienić WAY-139, czy tylko `resolve_gaps.md` |
```

## Entries and files the slice reads, with current ranges

- Foundation entries row 3
- `project-level/task/skill/SKILL.md:48-52` 4. Carry the foundation decisions
- `foundations/decisions.md:403-442` WAY-13 (current range)
- `foundations/decisions.md:688-717` WAY-26 (current range)
- `foundations/decisions.md:3764-3842` WAY-139 (current range)
- `foundations/decisions.md:4783-4868` WAY-165 (current range)
- `foundations/part_map.md:77-91` project-level
