# Handoff — slice 6

The person who requested this cycle delegated its intermediate choices to the orchestrator; no answer
here is that person's approval. You never ask the human: a question goes back to the orchestrator in
your report.

- Worktree (work only from its root): `the task's worktree root`, branch `task/cycle-technology-decisions-batch`. This is the-way itself; there is no pinned process.
- Your method and variant: `make-change` — read `task-cycle/change/SKILL.md` whole; your variant is **a slice, or the retry of a slice**, so read `task-cycle/change/slice.md` when the method sends you there. Read `agent-instructions/README.md` too.
- Stage and boundary: slice 6 of `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` only. Change only the files of the slice's *Change* line; commit them with `git add <path>` (no `git add -A`); commit messages in English. Run the slice's *Checks* yourself (focused; never the full `python -B gate/run_tests.py` without a directory). The slice's *Model* sets your class.
- Frozen task (read whole): `.runs/task-cycles/cycle-technology-decisions-batch/task.md` (Polish). Plan: `.runs/task-cycles/cycle-technology-decisions-batch/plan.md` (your slice section is copied below word for word; the plan's *Foundation entries* and *Choices* are in the plan). No spec.
- Foundation entries already written in this cycle (commits `85c5395` .. `f3b90d5` on this branch, in `foundations/decisions.md`; the report is `.runs/task-cycles/cycle-technology-decisions-batch/reports/02-foundation-entries-report.md`): read the plan's *Foundation entries* table, then read the decisions your slice depends on in their current text. Row 1 is the **new decision WAY-322** (current range in the list below if your slice reads it); it covers every matter of an agent's way to the running product that the step lists — the base holds a fifth matter beyond the task's four, the place of the screenshots — and the failure notice; word your files to agree with it. WAY-165, WAY-166 and WAY-139 were reworded in place.
- Answers of step 4: trust boundary — no file of this slice is named as a trust boundary (the change as a whole touches one, in slice 3); irreversible operation — no.
- **Drift:** the task's line numbers and the plan's cite older commits; find each place by its content. Where the current text of a place already says what the item asks, change nothing there and say so in your report.
- Report path: `.runs/task-cycles/cycle-technology-decisions-batch/reports/09-slice-6-report.md` (full report as the method gives it, with the own-work check, **Searches not found or unclear**, reaches beyond this handoff, and each check with its command and exit code).
- Return: status, your commits, a one-line check result naming what failed or did not run, and the report path.

- **Also read, whole (new decision of the cycle's foundation step, row 1):** `foundations/decisions.md` WAY-322 (heading `### WAY-322`, to the end of its entry just before `## Withdrawn identifiers`), and WAY-165, WAY-166, WAY-121 in their current text. WAY-322 says the matters of an agent's way to the running product that the step lists, and how a human learns of a failure, cannot be struck from the list; a human to whom a matter does not apply answers it like any choice. The step lists, at this base, a fifth matter beside the task's four (logs, interface, development data, failure notice): the place of the screenshots. Word `list.md`, `start.md` and `running_product.md` by the family as the foundation holds it, not by four matters only.
- Item 17 first point: WAY-165's rewording (entry `e651200`) is the model for the sentence in `project-level/definition_template.md`; item 15 is mirrored by WAY-166's rewording (entry `2ec17d4`).


## The slice (plan section, word for word)

### Slice 6 — The technology step: listed matters, resumed runs and recommendation

- **Goal:** the skill `project-level/technology/` says, each place found by its content: (item 10) when the step shows the list for confirmation, the matters of the logs, the interface, the development data and the failure notice cannot be struck from it; the human to whom a matter does not apply answers it like any choice, and that answer settles it, so on resuming it does not return as open (`list.md`, `start.md`, `running_product.md`); (item 11) a run at a task interrupted between writing the note and writing its item, once resumed, lists the choice of that note and does not close without it (`task_run.md`, the bullets of "Start" on a list with a note the section already holds and on a list with no open item); (item 12) the look for a projected decision on resuming (`start.md`), when it ends the item `— projected`, removes the line nested under it, as sub-step 7 of `settle.md` does; (item 13) the look at how a human learns of a failure (`failure_notice.md`) also looks for a projected decision of this definition and then gives `— projected`, as `list.md` does for a matter it finds a projected decision for, and not `— open`; (item 15) where no option of the agent's way to the running product can be used by an agent, `settle.md` has the recommendation go by the other consequences and say in one sentence that no option lets an agent check the running product this way, so the check stays with the human; and `project-level/definition_template.md`, where it carries WAY-166's sentence, says the same; (item 17, first point) in `project-level/definition_template.md` the sentence that names data set up from scratch and a dedicated test environment that persists reads as WAY-165 reads after Foundation entries item 17: examples, none ruled out. Foundation entries rows 1 and 2 and item 17 are written before this slice and bind it; word the files to agree with them. Prose only.
- **Change:** `project-level/technology/list.md` · `project-level/technology/start.md` · `project-level/technology/running_product.md` · `project-level/technology/failure_notice.md` · `project-level/technology/task_run.md` · `project-level/technology/settle.md` · `project-level/definition_template.md`
- **Read:** `.runs/task-cycles/cycle-technology-decisions-batch/task.md:46-49` To do, items 10 to 13 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:51-51` To do, item 15 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:56-57` To do, item 17, first point · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:83-95` Questions to settle, questions 1 and 2 · `.runs/task-cycles/cycle-technology-decisions-batch/task.md:166-171` Settlements to record, rows 1 and 2 · Foundation entries row 1 · Foundation entries row 2 · Foundation entries item 17 · `project-level/technology/SKILL.md` · `project-level/technology/research.md` · `elements/common/way_of_working.md:20-45` How a skill asks · `foundations/decisions.md:2568-2621` WAY-113 · `foundations/decisions.md:2827-2918` WAY-121 · `foundations/decisions.md:2979-3039` WAY-123 · `foundations/decisions.md:4754-4838` WAY-165 · `foundations/decisions.md:4839-4869` WAY-166 · `foundations/decisions.md:8096-8161` WAY-267 · `foundations/decisions.md:8293-8373` WAY-270 · `foundations/invariants.md:218-227` project-technology-record · `foundations/part_map.md:77-91` project-level
- **Model:** same — rules for resuming an interrupted run interact across five files of the step
- **Risk:** none
- **Checks:** `python -B gate/run_tests.py project-level` · `python -B elements/common/foundation_check.py --skip-test-citations` · `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` · `git diff --check`
- **Depends on:** Foundation entries row 1 · Foundation entries row 2 · Foundation entries item 17

## Passages the slice reads

#### Task passage: To do, items 10 to 13 (task.md:46-49)

```text
10. Krok, pokazując listę do potwierdzenia (`list.md:31-32`), mówi, że sprawy logów, interfejsu, danych deweloperskich i powiadamiania o awarii nie da się z niej wykreślić; człowiek, którego sprawa nie dotyczy, odpowiada na nią jak na każdy wybór, a ta odpowiedź ją rozstrzyga, więc przy wznowieniu nie wraca jako otwarta (pytanie 1; theway#024-1 = theway#065-12; `start.md:15-16`, `running_product.md:34-35`).
11. Przebieg przy zadaniu przerwany między zapisaniem notatki a zapisaniem jej pozycji, wznowiony, listuje wybór z tej notatki, zamiast zamknąć się bez niego (theway#063-9; `task_run.md:27-29`, `:37`).
12. Odszukanie decyzji rzutowanej przy wznowieniu (`start.md:22-26`), kończąc pozycję `— projected`, usuwa linię zagnieżdżoną pod nią, jak robi to `settle.md` (podkrok 7) (theway#065-1).
13. Spojrzenie na powiadamianie o awarii (`failure_notice.md:13-15`) szuka też decyzji rzutowanej tej definicji i daje wtedy `— projected`, jak `list.md:21-22`, zamiast `— open` (theway#065-4).
```

#### Task passage: To do, item 15 (task.md:51-51)

```text
15. Gdy żadna opcja sprawy dostępu agenta do działającego produktu nie pozwala agentowi jej użyć, krok poleca opcję według pozostałych skutków i mówi wprost jednym zdaniem, że żadna opcja nie pozwala agentowi sprawdzić działającego produktu tą drogą, więc to sprawdzenie zostaje przy człowieku; WAY-166 i plik kroku mówią to samo (pytanie 2; theway#024-5).
```

#### Task passage: To do, item 17, first point (task.md:56-57)

```text
17. WAY-165:
    - zdanie o danych deweloperskich nie czyta się jak zamknięta para dwóch opcji: dane stawiane od zera i trwałe środowisko testowe są przykładami, żadna nie jest wykluczona, a opcje daje badanie (WAY-122), jak mówi już uzasadnienie („neither is ruled out”); to samo zdanie w `project-level/definition_template.md:182-184` (theway#024-2);
```

#### Task passage: Questions to settle, questions 1 and 2 (task.md:83-95)

```text
- Pytanie 1: co dzieje się ze sprawą logów, interfejsu, danych deweloperskich albo powiadamiania o awarii, którą człowiek wykreślił z listy wyborów technologii?
  - Answer: tych czterech spraw nie da się wykreślić; człowiek, którego sprawa nie dotyczy, odpowiada na nią jak na każdy wybór (np. „narzędzie nie ma logów, agent czyta wyjście konsoli”), a odpowiedź ją rozstrzyga. Słaby punkt przyjęty z tą drogą: przy produkcie, którego sprawa nie dotyczy, człowiek pisze jedno zdanie odpowiedzi zamiast skreślenia.
  - Not chosen:
    - wykreślona sprawa zostaje na liście z nowym oznaczeniem `— struck` — nowe oznaczenie w trzech szablonach i w sprawdzeniu gotowości, a sprawa stoi rozstrzygnięta bez odpowiedzi, wbrew WAY-165, i agent cyklu zgaduje, skąd czyta logi.
    - zostawić jak jest — przy każdym wznowieniu człowiek wykreśla to samo i dwa razy ogląda listę.
  - Source: Mariusz, 2026-11-08: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; `project-level/technology/list.md:31-32`, `start.md:13-16`, `running_product.md:17-20`, `foundations` `a3206c1`.
- Pytanie 2: co rekomenduje krok technologii, gdy żadna opcja sprawy dostępu agenta do działającego produktu nie pozwala agentowi jej użyć?
  - Answer: krok poleca opcję według pozostałych skutków i mówi wprost jednym zdaniem, że żadna opcja nie pozwala agentowi sprawdzić działającego produktu tą drogą, więc to sprawdzenie zostaje przy człowieku. Słaby punkt przyjęty z tą drogą: krok nie szuka drugi raz opcji, której agent mógłby użyć; brak wychodzi przed wyborem i odpowiada na niego człowiek.
  - Not chosen:
    - krok najpierw szuka dalej opcji, której agent może użyć (np. wysyłanie logów do miejsca, które agent czyta), i dopiero bez wyniku idzie drogą a — dłuższe badanie przy każdej takiej sprawie, często dodatkowa usługa do opłacenia, a WAY-122 i tak każe szukać opcji badaniem.
    - krok nie poleca nic — wyjątek od WAY-113, człowiek odpowiada bez podpowiedzi.
    - zostawić jak jest — przypadek wychodzi przy pierwszym produkcie z takim hostingiem i każdy agent rozwiąże go inaczej.
  - Source: Mariusz, 2026-11-08: „a” — na drogę a przedstawioną w rozmowie doprecyzowania; WAY-166 `foundations/decisions.md:4697-4700`, `foundations` `a3206c1`.
```

#### Task passage: Settlements to record, rows 1 and 2 (task.md:166-171)

```text
Candidates: 8 shown, 5 accepted — 2026-11-08

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Sprawy logów, interfejsu, danych deweloperskich i powiadamiania o awarii nie da się wykreślić z listy wyborów technologii; człowiek, którego sprawa nie dotyczy, odpowiada na nią jak na każdy wybór, a odpowiedź ją rozstrzyga. | decision | pytanie 1 | czy zapisać zakaz wykreślania w decyzji (WAY-121, WAY-165) z odrzuconymi drogami, czy tylko w `list.md` |
| 2 | Gdy żadna opcja sprawy dostępu agenta do działającego produktu nie pozwala agentowi jej użyć, krok poleca opcję według pozostałych skutków i mówi jednym zdaniem, że to sprawdzenie zostaje przy człowieku. | decision | pytanie 2 | czy dopisać przypadek do WAY-166, czy tylko do pliku kroku; co polecić, gdy nie ma czego polecić |
```

## Entries and files the slice reads, with current ranges

- Foundation entries row 1
- Foundation entries row 2
- Foundation entries item 17
- `project-level/technology/SKILL.md`
- `project-level/technology/research.md`
- `elements/common/way_of_working.md:20-45` How a skill asks
- `foundations/decisions.md:2571-2624` WAY-113 (current range)
- `foundations/decisions.md:2830-2921` WAY-121 (current range)
- `foundations/decisions.md:2982-3042` WAY-123 (current range)
- `foundations/decisions.md:4783-4868` WAY-165 (current range)
- `foundations/decisions.md:4869-4917` WAY-166 (current range)
- `foundations/decisions.md:8144-8209` WAY-267 (current range)
- `foundations/decisions.md:8341-8421` WAY-270 (current range)
- `foundations/invariants.md:218-227` project-technology-record
- `foundations/part_map.md:77-91` project-level
