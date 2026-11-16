**State: draft** — the CI run on the last head, which is the final gate, has not ended yet; once it is green the request is marked ready, and then one item below waits for your answer.

## What you will see

The agents that review or make a change in a cycle are supposed to judge it from what they are handed, not from the reasoning of the agent that leads the cycle. Until now the only ban on reading the leading agent's log stood in the leading agent's own instructions, which the agents of the stages never read, so the ban worked only when the leading agent remembered to write it into each message by hand. In one earlier cycle a reviewer did open that log, to see whether the leading agent had already ruled on a question, and said so itself; it found no ruling there and no harm to its assessment was found.

After this change every handoff that the leading agent writes tells the agent, in one fixed sentence, that the cycle's log and the other files of the cycle's record folder — other agents' handoffs, reports and lists of findings — are not its to read unless its handoff names them. A reviewer is still given the author's report, since its handoff names it; nothing is taken away from what a stage is handed. The rule is also written into the decision that governs how stages hand their work over, with the reason: the log, the other handoffs and the other reports hold the leading agent's answers to the agents' questions, and an agent that knows that reasoning before it assesses may assess under its influence.

### Underneath

One sentence is added to the list of what every handoff carries in the leading agent's skill, and one existing decision of the log is extended in place, with its checks, its reason and the ways that were not chosen.

## For you to decide

### Needed from you

none

### Fix or let through

1. The review of the whole change named two decisions of the log — the one on how a row of settlements the human accepted is carried into the foundation, and the one on what a handoff names — as bearing on the change, and read only their rules and the opening of their fields, not their reasons and rejected ways, and nobody closed that gap. If those two decisions say something that the new wording of the handoff rule goes against, it would show the next time an agent hands work over, as a handoff that follows one rule and breaks the other, and the cycle would have to correct it then. Having a fresh reviewer read them whole costs one more review and a round of waiting; undoing it, nothing. Making a task of it leaves the gap standing until someone reads them; undoing it, nothing. Letting it through accepts that the review's later checking — the fix review read the changed text against the task's own words and found it faithful — is enough; undoing it, a correction after a clash is found. I recommend letting it through, since the change adds to one decision and removes no sentence the two rest on, and the author's search of the log found no other entry on who reads the cycle's record. Its weak point: the author's search was by words, and a clash that uses other words would not be found. Have a fresh reviewer read them in this request, make a task of it, or let it through? (Checks, 4)

### You accept by merging

none

## Cost

Counted before this request was published: working time 0:24:02 across the orchestrator and its agents, of which 0:09:32 was waiting for tools; 13.1 million tokens (9.6 million on Sonnet 5.5, 3.4 million on Opus 5.5, which did the reviews, as you asked, and not on `fable`). One review round ran a fix and a review of the fix: the review of the whole change failed once (one blocking finding and two Minor ones, all fixed) and the review of the fix passed; the return step changed nothing, so it needed no review. The table of stages stands in the record, linked under *Course of the cycle*.

One directory of an earlier task still stands because the cleaning script could not tell it was no longer needed; nothing in this request waits for it and you may remove it by hand. Its name, branch and reason stand in *Checks*.

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then. Nothing here waits for a review of the foundation.

<details>
<summary>W języku zadania (po polsku)</summary>

**Stan: szkic** — przebieg CI na ostatnim commicie, czyli końcowa bramka testów, jeszcze się nie skończył; gdy będzie zielony, PR zostanie oznaczony jako gotowy, a wtedy na Twoją odpowiedź czeka jedna pozycja poniżej.

## Co zobaczysz

Agenci, którzy robią zmianę albo ją recenzują w cyklu, mają oceniać ją na podstawie tego, co dostali, a nie na podstawie rozumowania agenta prowadzącego cykl. Dotąd jedyny zakaz czytania dziennika agenta prowadzącego stał w jego własnej instrukcji, której agenci etapów nie czytają, więc zakaz działał tylko wtedy, gdy agent prowadzący pamiętał, żeby dopisać go ręcznie do każdej wiadomości. W jednym wcześniejszym cyklu recenzent otworzył ten dziennik, żeby sprawdzić, czy prowadzący rozstrzygnął już jakieś pytanie, i sam to zgłosił; nie znalazł tam rozstrzygnięcia i nie stwierdzono szkody dla jego oceny.

Po tej zmianie każde zlecenie, które pisze agent prowadzący, mówi agentowi jednym stałym zdaniem, że dziennik cyklu i pozostałe pliki katalogu zapisu cyklu — zlecenia, raporty i listy znalezisk innych agentów — nie są jego do czytania, chyba że jego zlecenie je wskazuje. Recenzent nadal dostaje raport autora, bo jego zlecenie go wskazuje; nic nie jest odbierane z tego, co etap dostaje. Reguła jest też zapisana w decyzji, która rządzi tym, jak etapy przekazują pracę, razem z powodem: dziennik, cudze zlecenia i cudze raporty zawierają odpowiedzi agenta prowadzącego na pytania agentów, a agent, który zna to rozumowanie przed własną oceną, może oceniać pod jego wpływem.

### Pod spodem

Do listy tego, co niesie każde zlecenie, w skillu agenta prowadzącego dochodzi jedno zdanie, a jedna istniejąca decyzja dziennika jest rozszerzona w miejscu: z jej sprawdzianami, uzasadnieniem i wariantami, których nie wybrano.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

none

### Napraw albo przepuść

1. Przegląd całej zmiany uznał dwie decyzje dziennika — tę o tym, jak wiersz uzgodnionych ustaleń trafia do fundamentu, i tę o tym, co wskazuje zlecenie — za dotyczące zmiany, a przeczytał tylko ich reguły i początek pól, bez uzasadnień i odrzuconych wariantów, i nikt tej luki nie domknął. Gdyby te dwie decyzje mówiły coś, co nowe brzmienie reguły zlecenia narusza, wyszłoby to przy następnym przekazaniu pracy, jako zlecenie, które stosuje jedną regułę i łamie drugą, i cykl musiałby wtedy poprawiać. Przeczytanie ich w całości przez nowego recenzenta kosztuje jeszcze jeden przegląd i rundę czekania; cofnięcie nic nie kosztuje. Zrobienie z tego zadania zostawia lukę, aż ktoś je przeczyta; cofnięcie nic nie kosztuje. Przepuszczenie przyjmuje, że wystarcza późniejsze sprawdzenie — przegląd poprawki porównał zmieniony tekst ze słowami zadania i uznał go za wierny; cofnięcie to korekta po znalezieniu sprzeczności. Rekomenduję przepuścić, bo zmiana dopisuje do jednej decyzji i nie usuwa żadnego zdania, na którym tamte dwie stoją, a przeszukanie dziennika przez autora nie znalazło innego wpisu o tym, kto czyta zapis cyklu. Słaby punkt: przeszukanie autora szło po słowach, więc sprzeczność ujęta innymi słowami nie zostałaby znaleziona. Czy nowy recenzent ma je przeczytać w tym PR-ze, zrobić z tego zadanie, czy przepuścić? (Checks, 4)

### Akceptujesz przez scalenie

none

## Koszt

Policzony przed opublikowaniem tego PR-a: czas pracy 0:24:02 orkiestratora i jego agentów, w tym 0:09:32 czekania na narzędzia; 13,1 mln tokenów (9,6 mln na Sonnet 5.5, 3,4 mln na Opus 5.5, który robił przeglądy, tak jak prosiłeś, a nie na `fable`). Jedna runda przeglądu miała poprawkę i przegląd poprawki: przegląd całej zmiany odpadł raz (jedna uwaga blokująca i dwie drobne, wszystkie naprawione), a przegląd poprawki przeszedł; krok powrotny niczego nie zmienił, więc nie potrzebował przeglądu. Tabela etapów stoi w zapisie, z linkiem w *Course of the cycle*.

Katalog jednego wcześniejszego zadania nadal stoi, bo skrypt czyszczący nie umiał rozpoznać, że nie jest już potrzebny; nic w tym PR-ze na niego nie czeka i możesz go usunąć ręcznie. Jego nazwa, gałąź i powód są w *Checks*.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do zapisu cyklu przeżywa tylko wtedy. Nic tu nie czeka na przegląd fundamentu.

</details>

## Technical changes

The change is two commits on the base `3cbaeb9`, the author's work and the fix of the review of the whole change; the return step made no commit, and the request holds the record's pair of commits besides.

1. `de24e5b` — the change itself. `task-cycle/skill/SKILL.md`: after the sentence that lists what every handoff carries, the sentence of the task, word for word: "It tells the agent that `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and findings — are not its to read unless its handoff names them." The task's line reference to the sentence "ending 'and the report path.'" no longer matched, since the list grew; the new sentence stands after the list sentence that now ends "(WAY-148)." `foundations/decisions.md`: WAY-148 changed in place: its binding sentence, both lists of its *Verification*, its *Rationale* and its *Rejected*.
2. `91e1fa9` — the fix of the review of the whole change: the *Rationale* no longer says that the reviewer of loop2's cycle was influenced, but that it read the log, found no ruling there and that no harm was found; the premise of the binding sentence names `cycle.md` alone ("since only the orchestrator reads `cycle.md`"), so it no longer clashes with an agent reading a file its handoff names; the clause about what the orchestrator's skill does today is replaced by "the sentence then stands in one place".

## Checks

1. The final gate is the CI run on the request's last head: the result is written here once the run ends. The cycle ran no full gate on its own system. The agents' focused checks: `python -B -m unittest discover -s task-cycle -p "test_*.py"` 534 tests OK, 2 skipped, exit 0, and `python -B -m unittest discover -s elements/common -p "test_*.py"` 257 tests OK, exit 0 (author, on `de24e5b`; the task-cycle run repeated on `91e1fa9`, exit 0); `python -B elements/common/foundation_check.py` run by the orchestrator on `91e1fa9` without `--skip-test-citations`: exit 0, `0 errors`, no `listed:` line.
2. Tests failing before the change: none. The base is a merge commit with the tree of its second parent, so no gate ran on it; the list was taken from the checks of the merged request #142, whose CI run 43836009733 on its last head had `tests` and `tests-windows` green, and from the cycle record of that request.
3. Own-work checks: the author's — a multiline search of the skill for the task's sentence across its line break found it once, and the foundation check passed on the first run after the edit; the author of the fix — the new sentence about the earlier cycle read against the task's lines "szkody nie stwierdzono" and "(it had not)", and the foundation check green. The reviewer of the fix compared the same sentence with the earlier cycle's report at `273446f`.
4. The review of the whole change read 5 of the 115 decisions of its selection whole, after reading the index of the whole selection; it named WAY-134 and WAY-213 as bearing on the change and read only their rules and the opening of their fields (item 1 of *Fix or let through*). The review of the fix read its whole material and named nothing unread. The author's report named the part map and `elements/decisions/examples.md` as not read whole; the reviewer of the whole change read the entry of the `task-cycle` part and the examples whole, and the return step searched the part map for the record's words and found none.
5. The target branch: `git fetch origin` — `origin/foundations` is still the base `3cbaeb9`, so no merge and no renumbering were needed (the change writes no new decision). `python -B task-cycle/review_reminder.py origin/foundations`: tag `foundation-review/2026-11-15`, 15 merges, threshold 60, `reminder: no`.
6. The task's items: no screenshot or user-interface state applies; the change touches no trust boundary and holds no operation that cannot be undone.
7. Description checks and checks on the copy of the record: written in the edit that adds the record's link.
8. Directories of earlier tasks kept, with no absolute path: audit-answers-contradiction-after-code · task/audit-answers-contradiction-after-code · commits not on the remote, and the branch has no merge git can see on the target branch. Working copies left by agents: none.

## Foundation entries

- WAY-148 — a stage agent reads `cycle.md` and the other files of the cycle's record directory only where its handoff names them, the handoff tells it so, and the reason is the independence of its assessment. Marked `row 1`: it carries row 1 of *Settlements to record* whole, as a change of the existing decision and not as a new entry. Its *Rejected* now holds the four ways the task did not choose.
- No invariant, no test and no surface is changed, and no *Violated* mark is set or cleared; the foundation check lists no invariant for a corrected sentence. No test cites WAY-148 by a line `decision:`.

## Minor findings

1. Found by the review of the fix (`PASS 91e1fa9`), within the task, not fixed: "The phrase "and found no ruling there, and no harm to the assessment was found" puts two "and" clauses side by side and uses "found" twice, so it is a little heavy to read. Its meaning is clear and faithful to the source. It does not block." Place: `foundations/decisions.md:6099-6100`.

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** the task is independent: every handoff of the cycle tells its agent that the cycle's log and the other files of the record folder are not its to read unless its handoff names them, with WAY-148 extended in step; sources: the task document, accepted 2026-11-14, and the foundation at `3cbaeb9`.
- **Process pin:** none; the-way itself is the process.
- **Spec:** none: the task leaves no open design choice, as its three answered questions and its one settlement row show.
- **Route:** one author without a plan, class `same` (Sonnet), since the change rewrites the binding text, the checks, the reason and the rejected ways of a decision and asks for the search of the whole foundation; the fix by the same author; the return step by the same author, with no commit. The reviews ran on Opus 5.5, as the command that started the cycle asked, since `fable` is switched off.
- **Plan:** none.
- **Choices:** 4 other choices, none of them beyond the task's text that changes what the foundation binds; the table is in the record.
- **Blocking findings left:** none.
- **Record:** the link is added in the edit that adds the record's commit.
