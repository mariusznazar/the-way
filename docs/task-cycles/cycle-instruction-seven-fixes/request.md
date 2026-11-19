**State: draft** — the request opens as a draft while the record's link and the result of the tests on its last head are still to be added; one item below waits for your answer

## What you will see

Seven gaps in the instructions that the agents of a task cycle follow are closed, each in the words the task gave, and three sentences are written into the decisions that bind the process.

- Screenshots shown to you no longer count as a forbidden write outside the repository: the list of what the cycle may write outside it now names the place the product's foundation settles for screenshots, so a cycle does not push them into a public repository against its instruction.
- When a change leaves more slices with no review of their own than one final reviewer can compare with their sources, the agent leading the cycle may have groups of them reviewed in the plan's order, and writes down the grouping and why.
- When an agent refuses to write its report although the file's name is allowed, the agent leading the cycle saves the report it got back in its answer, unchanged, at the report's path, and notes the refusal and the agent's model in the cycle's log, never in the report itself.
- The size measure of a slice no longer counts a whole large file of decisions as read when the slice names only the part of it that it changes; a slice that names no part still counts the whole file. The two instructions that tell the planner what to name and the agent what to read say the same.
- A decision proposed from a note keeps a rejected way with `no cost to the product known` where the note keeps no cost or only a cost of the process, and leaves out a way that is only a way of recording an answer.
- An agent that starts a long command in the background ends its turn only after the command has ended and it has read its result, instead of answering "still waiting for the tests".
- Agents remove a copy by its full path, never through a shell variable, and the cycle removes an earlier copy of its record the same way before it makes a new one.

### Underneath

Four instruction files of the cycle, one measuring script with its test, the decision template and three decisions of the decision log changed; nothing of a product changed.

## For you to decide

### Needed from you

none

### Fix or let through

1. Two small gaps that the final reviewer found stay in the instructions, because the task gave their wording and fixing them goes beyond it. First, the new sentence about groups of reviews calls the agent leading the cycle "the lead", a word used nowhere else in the process, so a reader may take it for another actor than the one the sub-step addresses. Second, a plan that names part of a code file the slice changes is now measured by that part, while the agent is told to read such a file whole, so a slice can come out as fitting when it is larger; the reviewer's own run counted 548 characters where the old measure counted 25 907. Whoever runs a cycle meets the first as a moment of doubt and the second only when a plan names a range of a code file, which the task did not intend. Fixing both in this request costs a correction with one more review and changes wording the task settled; making a task of them costs a later task; undoing either costs nothing. Letting them through costs nothing today, and the first stays a small confusion and the second a measure that can under-count. I recommend making a task of the second and letting the first through, since the second can hide a slice that is too large, while the first only needs a better word. The weak point: a task for the second may be answered by narrowing the new rule, which would reopen a sentence you accepted. Fix them in this request, make a task of them, or let them through? (Findings outside the task's scope, 1 and 2)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. A file that a slice changes and that the plan names both whole and by a part counts whole in the size measure: the plan says the agent reads it whole, so a smaller count would hide what is read. The task's sentence can be read the other way. The other reading is the part count winning, which would make an explicit whole reading count less than it is.
3. Two ways the note kept for the sentences about reviews of groups and about waiting for results ("only the instructions, the decision unchanged"; "only the two instructions") are left out of the rejected ways of those decisions, because they are ways of where an answer is recorded, which the new sentence about rejected ways keeps out. The other reading would list them with the costs the note gives, three clauses more.
4. The change reaches a collision that the task left in place: one decision says that only a human makes an effect outside the repository, while another says that screenshots lie outside the repository; the instructions now carry the exception, the decisions do not. Writing the exception into the decisions would restore the sentence you rejected when you accepted the task.
5. Three decisions carry text you did not see in the task, which agents will compare later changes with, so they are marked as the cycle's own: for each, the cycle extended the examples that say what complies and what violates, and, for the sentence on rejected ways, a reason it takes from your task. Each entry says the following in plain words. The rule on groups of reviews is judged by the agent leading the cycle and not by a size measure; the rule on waiting makes an agent read the result of its command before it ends its turn; the rule on rejected ways keeps a no-cost way with the words `no cost to the product known` and leaves out a way of recording. The examples stand word for word under the entries in the lower part. (Foundation entries)

## Cost

About 40 minutes of work (the orchestrator, one author on Sonnet 5.5 in three turns, one reviewer on Fable 5.2 in two turns), 33.2 million tokens in all, of which 10.7 million on Fable 5.2; one review round with its fix (four Minor findings, fixed, passed). The table of stages is in the record: `docs/task-cycles/cycle-instruction-seven-fixes/stages.md` at the commit that adds it (see *Record*).

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then. The foundation has waited for a review through 24 merges since the tag of the last review, with the threshold at 60, so no reminder is due.

<details>
<summary>W Twoim języku</summary>

**Stan: wersja robocza** — request jest otwarty jako szkic, dopóki nie dopiszę linku do zapisu cyklu i wyniku testów na ostatnim commicie; jedna pozycja poniżej czeka na Twoją odpowiedź

## Co zobaczysz

Zamknięto siedem luk w instrukcjach, którymi kierują się agenci cyklu zadania, każdą w brzmieniu z zadania, i zapisano trzy zdania w decyzjach, które wiążą proces.

- Zrzuty ekranu pokazywane Tobie nie są już zakazanym zapisem poza repozytorium: lista tego, co cykl może zapisać poza nim, wymienia miejsce, które fundament produktu wyznacza na zrzuty, więc cykl nie wypchnie ich do publicznego repozytorium wbrew zleceniu.
- Gdy zmiana zostawia więcej kawałków bez własnego przeglądu, niż jeden recenzent końcowy porówna ze źródłami, prowadzący cykl może zlecić przeglądy ich grup w kolejności planu i zapisuje podział z powodem.
- Gdy agent odmawia zapisu raportu, choć nazwa pliku jest dozwolona, prowadzący cykl zapisuje raport z jego odpowiedzi bez zmian pod ścieżką raportu i notuje odmowę z modelem agenta w dzienniku cyklu, nigdy w samym raporcie.
- Miara rozmiaru kawałka nie liczy już całego dużego pliku decyzji jako czytanego, gdy kawałek wskazuje tylko jego zmieniany fragment; kawałek, który nie wskazuje fragmentu, nadal liczy cały plik. Dwie instrukcje mówiące planiście, co wskazać, i agentowi, co czytać, mówią to samo.
- Decyzja pisana z notatki zachowuje odrzucony wariant z `no cost to the product known`, gdy notatka nie podaje kosztu albo podaje tylko koszt procesu, i pomija wariant będący jedynie sposobem zapisania odpowiedzi.
- Agent, który puszcza długie polecenie w tle, kończy turę dopiero po tym, jak polecenie się skończyło i przeczytał jego wynik, zamiast odpowiadać „jeszcze czekam na testy”.
- Agenci kasują kopię pełną ścieżką, nigdy przez zmienną powłoki, a cykl kasuje wcześniejszą kopię zapisu w ten sam sposób, zanim zrobi nową.

### Pod spodem

Zmieniły się cztery pliki instrukcji cyklu, jeden skrypt pomiarowy z testem, szablon decyzji i trzy decyzje dziennika decyzji; nic z produktu się nie zmieniło.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Napraw albo przepuść

1. Dwie drobne luki, które znalazł recenzent końcowy, zostają w instrukcjach, bo zadanie podało ich brzmienie, a poprawka wychodzi poza nie. Po pierwsze, nowe zdanie o grupach przeglądów nazywa agenta prowadzącego cykl „the lead”, słowem, którego proces nigdzie indziej nie używa, więc czytelnik może wziąć je za innego wykonawcę niż ten, do którego zwraca się podpunkt. Po drugie, plan, który wskazuje fragment pliku kodu zmienianego przez kawałek, jest teraz mierzony tym fragmentem, a agent ma czytać taki plik w całości, więc kawałek może wyjść „mieści się”, choć jest większy; własny przebieg recenzenta policzył 548 znaków tam, gdzie stara miara liczyła 25 907. Kto prowadzi cykl, spotka pierwszą jako chwilę wątpliwości, a drugą dopiero gdy plan wskaże zakres pliku kodu, czego zadanie nie zamierzało. Poprawa obu w tym requeście kosztuje korektę z jednym przeglądem więcej i zmienia brzmienie, które zadanie rozstrzygnęło; zadanie na nie kosztuje późniejsze zadanie; cofnięcie któregokolwiek nic nie kosztuje. Przepuszczenie nic dziś nie kosztuje, a pierwsza zostaje drobnym zamieszaniem, druga miarą, która może zaniżać. Polecam zrobić zadanie na drugą i przepuścić pierwszą, bo druga może ukryć kawałek zbyt duży, a pierwsza wymaga tylko lepszego słowa. Słaby punkt: zadanie na drugą może się skończyć zawężeniem nowej reguły, co otworzy zdanie, które przyjąłeś. Naprawić w tym requeście, zrobić zadanie czy przepuścić? (Findings outside the task's scope, 1 i 2)

### Przyjmujesz przez scalenie

Scalenie przyjmuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

2. Plik, który kawałek zmienia, a który plan wskazuje zarazem w całości i fragmentem, liczy się w mierze rozmiaru w całości: plan mówi, że agent czyta go w całości, więc mniejsza liczba ukryłaby to, co się czyta. Zdanie zadania da się przeczytać odwrotnie. Odwrotne czytanie to wygrywający fragment, który sprawiłby, że jawne czytanie w całości liczy się mniej, niż jest.
3. Dwa warianty, które notatka zachowała dla zdań o przeglądach grup i o czekaniu na wynik („tylko instrukcje, decyzja bez zmian”; „tylko dwie instrukcje”), zostały poza odrzuconymi wariantami tych decyzji, bo są sposobami zapisania odpowiedzi, a nowe zdanie o odrzuconych wariantach takie pomija. Odwrotne czytanie wpisałoby je z kosztami z notatki, o trzy zdania dłużej.
4. Zmiana dotyka zderzenia, które zadanie zostawiło: jedna decyzja mówi, że efekt poza repozytorium robi tylko człowiek, a druga, że zrzuty leżą poza repozytorium; instrukcje niosą teraz wyjątek, decyzje nie. Wpisanie wyjątku do decyzji przywróciłoby zdanie, które odrzuciłeś, przyjmując zadanie.
5. Trzy decyzje niosą tekst, którego nie widziałeś w zadaniu i z którym agenci będą porównywać późniejsze zmiany, więc są oznaczone jako własne cyklu: dla każdej cykl rozszerzył przykłady mówiące, co jest zgodne, a co narusza, a dla zdania o odrzuconych wariantach dopisał powód wzięty z Twojego zadania. Każdy wpis mówi prosto: reguła o grupach przeglądów jest osądem prowadzącego cykl, nie miarą rozmiaru; reguła o czekaniu każe agentowi przeczytać wynik polecenia, zanim zakończy turę; reguła o odrzuconych wariantach zachowuje wariant bez kosztu ze słowami `no cost to the product known` i pomija wariant będący zapisem odpowiedzi. Przykłady stoją słowo w słowo pod wpisami w dolnej części. (Foundation entries)

## Koszt

Około 40 minut pracy (prowadzący, jeden autor na Sonnet 5.5 w trzech turach, jeden recenzent na Fable 5.2 w dwóch turach), łącznie 33,2 mln tokenów, z czego 10,7 mln na Fable 5.2; jedna runda przeglądu z poprawką (cztery drobne uwagi, poprawione, przeszły). Tabela etapów jest w zapisie cyklu: `docs/task-cycles/cycle-instruction-seven-fixes/stages.md` w commicie, który ją dodaje (zob. *Record*).

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do zapisu cyklu przeżywa tylko wtedy. Fundament czekał na przegląd przez 24 scalenia od tagu ostatniego przeglądu, przy progu 60, więc przypomnienie nie jest należne.

</details>

## Technical changes

Three commits of the change, then three of the fix of the Minor findings:

- `2a0df03c`: `task-cycle/slice_size.py` counts a changed file that *Read* names by ranges by those ranges, a file *Read* names whole or does not name whole; three tests in `task-cycle/test_slice_size.py`, one seen failing before the code.
- `fc88ee2c`: `task-cycle/skill/SKILL.md` (the list of exceptions of the cycle's writes names the screenshot; the review of groups of slices; the refused report; the removal of a copy by its path in "Working copies" and in the step that copies the record), `task-cycle/plan/SKILL.md` (*Read* names the range of an entry a slice changes), `task-cycle/change/SKILL.md` and `task-cycle/review/SKILL.md` (the end of a turn after a command's result, WAY-255; the reading of a file of the foundation by ranges).
- `bcaddc2b`: `elements/decisions/template.md` and `foundations/decisions.md`: the sentences of WAY-136, WAY-255 and WAY-134.
- `76b6b172`, `20210259`, `52801a69`: the fix of four Minor findings of the review of the whole change: the first paragraphs of WAY-136 and WAY-134 within the template's three sentences, the *Rationale* of WAY-134 states the task's reason, the number in the comment of one test, a reflowed line.

## Checks

- **Final gate:** the CI run on this request's last head; its result is added when the run ends, in a later edit.
- **Failing before the change:** none, taken from the merged request https://github.com/mariusznazar/the-way/pull/150, whose CI run on its last head (https://github.com/mariusznazar/the-way/actions/runs/44578468147) passed in both checks; the base `0b43a27d` is a merge commit with the tree of its second parent, so no gate ran on the base.
- **Focused runs** (`python -B gate/run_tests.py <directory>`, exit 0): `task-cycle` 537 tests, `elements/common` 271, `agent-instructions` 52, `instruction-files` 105, `product-guidelines` 14, by the author and the reviewer; the new test of `slice_size.py` failed before the code (the run's FAILED line, 1 of 19; the author ran it through a pipe, so its exit code was not captured) and passed after it (exit 0, 19 tests). The cycle ran no full gate on its own system and has no local time of it.
- **The check of the foundation** (`python -B elements/common/foundation_check.py`, no switch): exit 0, `0 errors`, no `listed:` line, by the author, the reviewers and the writer of this description.
- **Linter:** the pinned Ruff on the two changed Python files by the reviewer, exit 0 at the reviewed head and at the head of the fix; the author could not run it (not installed in its session).
- **Own-work check:** the author named its weakest point (a slice naming a range of a large log must be measured by the range while a slice naming none still counts the whole file) and checked it with a plan of two slices against the real log (8 521 characters and `fits` with the range; 916 646 characters and `too large` without; both `too large` on the base) and with three mutations of the script, each caught by the new tests; the reviewer repeated it with four mutations, each caught.
- **Walk through the running product:** not performed; the foundation of the-way settles no way to a running product for itself, and the change is texts of instructions, a measuring script and decisions, with no screen, answer of an interface or command of a product.
- **Reviews:** whole change, `PASS` at `bcaddc2b` (0 blocking, 4 Minor within the task, 2 outside it), run on Fable 5.2; the fix of the 4 Minor findings by the same author, the review of the fix `PASS` at `52801a69` (0 blocking, 0 remaining, 0 new); the return step committed nothing and so had no review. The reviewer read the index of its whole selection (56 decisions in full, 110 by heading) and 10 decisions whole; WAY-05, WAY-12, WAY-385 and WAY-293 it knew from the index and the template and did not open whole.
- **Review of the foundation:** 24 merges since the tag `foundation-review/2026-11-15`, threshold 60: no reminder.
- **Form check** of this description: `python -B task-cycle/request_check.py .runs/task-cycles/cycle-instruction-seven-fixes/request.md --task .runs/task-cycles/cycle-instruction-seven-fixes/task.md`: the last run is added with the link to the record; **check of private paths**: `python -B task-cycle/private_paths_check.py .runs/task-cycles/cycle-instruction-seven-fixes/request.md`: the last run is added with it; the three checks on the copy of the record are added with the link to it.
- **Working copies left:** none. **Directories of earlier tasks kept:** none.

## Foundation entries

- **WAY-136** (marked `row 1` and `the cycle's`): where the slices that have no review of their own are more than one reviewer of the whole change can compare with their sources, the orchestrator may, by its own judgment and not by a measure, dispatch reviews of groups of them in the plan's order, as for a slice with a review of its own, and records the grouping and its reason. Its *Rejected* is reconciled with the sentence, one way kept by the row's source (a criterion for the groups taken from a measure of the slices' size, off in two directions) added with its cost.
  - complies, added: "a change that rewrites many entries of the foundation from many notes has the slices without a review of their own reviewed in groups, in the plan's order, the grouping and its reason recorded"
  - violates, added: "reviews of groups of slices are dispatched with no grouping and reason recorded, or by a measure in place of the orchestrator's judgment"
- **WAY-255** (marked `row 2` and `the cycle's`): an agent that waits for a command that runs long by running it in the background ends its turn only after the command has ended and it has read its result.
  - complies, added: "and returns its report after reading the result"
  - violates, added: "an agent ends its turn with a note that it still waits for the tests it started in the background, in place of their result"
- **WAY-134** (marked `row 3` and `the cycle's`): a way not chosen that the row's source keeps with no cost, or with only a cost of the process such as a gate to reopen or a step to repeat, stands in the rejected options with `no cost to the product known`, and a way that is itself a way of the process rather than of the product, such as how or when an answer is recorded, stays out of them. The same sentence stands in `elements/decisions/template.md`, point 5.
  - complies, added: "a decision row whose source keeps a way with only the cost of a gate to reopen gives that way `no cost to the product known` in the decision's rejected options, and leaves out the way that only chose when the answer is recorded"
  - violates, added: "the cycle puts in the rejected options a way of the process, such as when an answer is recorded, or leaves a way whose source keeps no cost without the words `no cost to the product known`"

No topical section of the decision log is opened; no kept row tied to an entry already stated; no invariant, surface or *Violated* mark changed; no test holds a sentence of these decisions by a line `decision:`. The foundation check lists no invariant for a corrected sentence.

## Minor findings

none — the four Minor findings of the review of the whole change that lie within the task were fixed (the fix passed its review); the review of the fix left none and found none.

## Findings outside the task's scope

Both are the reviewer's, marked outside the task's scope because the task gives the wording they concern.

1. **Minor — "the lead" names the orchestrator by a word the-way uses nowhere else.** Place: `task-cycle/skill/SKILL.md:508`. The skill addresses its reader as "you", the decisions say "the orchestrator" (WAY-136 as this change writes it included), and a search of the task-cycle skills and the glossary finds "the lead" in this one sentence only; a reader can take it for another actor than the one the rest of the sub-step addresses. The word is the task's, given word for word and confirmed under its first question, so changing it goes beyond the task.
2. **Minor — the measure and the reading differ for a changed file that is no file of the foundation.** Place: `task-cycle/slice_size.py:194-196` against `task-cycle/change/SKILL.md:37-38`. The sentence of point 4(a) counts by its ranges every file of *Change* that *Read* names by ranges; the sentence of point 4(c) lets the agent read by ranges only "a file of the foundation", and every other file it changes whole. A plan that names in *Read* a range of a file of code the slice changes is now measured by the range while its agent reads the whole file. Evidence: scratch run below, slice 4 — `task-cycle/remove_merged_worktrees.py` in *Change* with `:1-10` in *Read* counts 548 characters at the head and 25 907 at the base. The task's answer on point 4(c) gives as its aim that the measure and the reading count the same; both sentences are the task's, so the difference is a gap of the task and its closing goes beyond it.

## Course of the cycle

- **Task and sources:** the task "seven fixes of the cycle's instructions from the remarks after the last cycles" of the author's backlog, independent, accepted with its three settlements on 2026-11-19; sources: the cases AIR-666 to AIR-671 and AIR-673 of the daily review of the process.
- **Process pin:** the-way itself, `0b43a27d`; no pin to move.
- **Spec:** none; the task left no open design choice, every point gives its wording and the questions it left open are answered in the task.
- **Route:** one author without a plan, class `same` (Sonnet 5.5), because the change crosses two parts, writes three binding sentences in the decision log and changes a script with a test over a large log; reviews by agents on Fable 5.2 at the user's instruction.
- **Plan:** none.
- **Choices:** 2 other choices of the cycle (a file named both whole and by ranges counts whole; the ways of the process stay out of the *Rejected*), besides the class of the author; the questions table is in the record.
- **Blocking findings left:** none.
- **Record:** pending — the link by the SHA of the commit that adds the copy is added after it.
