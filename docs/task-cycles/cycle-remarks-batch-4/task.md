---
title: "the way: zadanie zbiorcze z uwag cykli — pole Origin, kolejność bramki, numerowane nagłówki w skrypcie uwag, TODO w Rests on"
status: draft
created: 2026-11-11T09:50
updated: 2026-11-11
tags: [zadanie]
related: "(a note in the author's private notes)"
---

## Po co to

- **Jak jest dziś:** cykle zadań w loop2 i w samym the way zostawiają w zapisach przebiegu uwagi o tym, gdzie skill the way nie pasował do sytuacji. Przegląd warstwy AI z 2026-11-11 przyjął cztery z nich. (1) Pole *Origin* decyzji wskazuje w loop2 notatki zadań z vaultu, które po domknięciu zadania są kasowane — ponad połowa takich odsyłaczy już prowadzi donikąd, a agenci wpisują tam raz notatkę, raz `none`, raz pytanie z zadania. (2) Pełne testy produktu (bramka, w loop2 ok. 35 minut) idą przed końcowym porównaniem decyzji z kodem, a to porównanie prawie zawsze coś poprawia — w 5 z 5 zapisanych cykli loop2 — więc bramkę trzeba puszczać drugi raz albo cykl odchodzi od kolejności z własnej inicjatywy. (3) Skrypt, który pilnuje, żeby wątpliwości agentów z raportów trafiły do uwag procesowych, nie rozpoznaje nagłówka z numerem („## 12. Searches not found or unclear”); w dwóch raportach na 99 tak było i w jednym wątpliwość przepadła bez śladu. (4) Gdy reguła produktu pilnowana testem zależy od faktu o środowisku, którego produkt jeszcze nie spisał, szablon, skrypt sprawdzający i wspólne reguły mówią trzy różne rzeczy o tym, co wpisać.
- **Kto to odczuwa:** Ty — dostajesz w opisach PR-ów drobne uwagi o tych polach do rozstrzygnięcia, czekasz ok. pół godziny dłużej na PR, a wątpliwości z raportów z numerowanymi sekcjami nie docierają do Twojego przeglądu; agent prowadzący cykl, który traci rundy poprawek na sprzecznych wskazówkach.
- **Co jeśli nic:** każde zadanie loop2, które pisze albo zmienia decyzje, dokłada odsyłacze do notatek, które za chwilę znikną; prawie każdy cykl płaci drugi przebieg testów; długie raporty z numerowanymi sekcjami dalej po cichu gubią wątpliwości; każdy niezmiennik pisany na wzór testu z the way powtarza rundę poprawek i zostawia na gałęzi głównej nieme `TODO`.

# the way: zadanie zbiorcze z uwag cykli — pole Origin, kolejność bramki, numerowane nagłówki w skrypcie uwag, TODO w Rests on

Status: ready for cycle
Project relation: independent

## Description

### Need

- Cykle zadań w loop2 i w samym the way zostawiają w zapisach przebiegu uwagi o miejscach, w których skill the way nie pasował do sytuacji; przegląd warstwy AI z 2026-11-11 przyjął cztery z nich do zmiany w the way.
- Pole *Origin* decyzji: w loop2 agenci wpisują tam notatki zadań z prywatnego vaultu, kasowane po domknięciu zadania, więc odsyłacze prowadzą donikąd; szablon decyzji nie mówi wprost, że notatki zadania tam nie ma.
- Kolejność bramki: skill cyklu każe puścić pełne testy produktu (krok 10) przed krokiem powrotu (krok 11), a krok powrotu prawie zawsze zmienia drzewo, więc bramka idzie drugi raz.
- Skrypt uwag procesowych (`task-cycle/remarks_check.py`) nie rozpoznaje nagłówka sekcji z numerem, więc wątpliwość z takiego raportu może nie trafić do uwag cyklu i do przeglądu Mariusza.
- Opisowe `TODO` w polu *Rests on* niezmiennika: szablon niezmienników daje postać `TODO — <the fact, with its source>`, wspólne reguły zakazują `TODO` na gałęzi głównej, odkąd fakty środowiska mają wpisy, a skrypt sprawdzający fundament odrzuca postać opisową.
- Odbiorcą jest Mariusz, który rozstrzyga te uwagi w opisach PR-ów i czeka na drugi przebieg bramki, oraz agent prowadzący cykl, który traci rundy poprawek na sprzecznych wskazówkach.

### To do

1. W `elements/decisions/template.md`, w sekcji `## Origin`, zdanie „The task a decision was made in is not recorded: git history gives it.” zastąpić:
   > The task a decision was made in is not recorded, and a task document is never named in *Origin*, wherever the product keeps its tasks: the place of tasks is where work is found, never a source an entry points to (WAY-27). What it holds of the reasoning goes into the entry's *Rationale* and *Rejected*; *Origin* then reads `none`.
2. W `task-cycle/skill/SKILL.md`, w kroku 10, po jego pierwszym zdaniu dopisać:
   > Start it once step 11's return step and any review of it are done, on the tree they leave: the return step needs no result of the gate, so one run covers both. Where the gate then fails and its fix changes code, the return step compares that fix's range too.
3. W WAY-160, w *Verification*, przykład zgodny „the orchestrator runs the gate after the review of the whole change and again after the return step changed the tree” zastąpić (przez skill zapisu decyzji, `record-decision`):
   > the orchestrator runs the gate once on the tree the return step and its review leave, and again where the merge with the target branch changed it
4. `task-cycle/remarks_check.py` rozpoznaje nagłówek sekcji, w którym przed słowami `Searches not found or unclear` stoi numer sekcji (`12.`, `12)`, `3.1`); docstring skryptu opisuje nagłówek tak:
   > a heading, at any level, whose text is `Searches not found or unclear`, after an optional section number such as `12.`, with an optional trailing colon, emphasis or parenthesis
   
   a `task-cycle/test_remarks_check.py` ma przypadek z nagłówkiem `## 12. Searches not found or unclear`.
5. `elements/common/foundation_check.py` czyta pole *Rests on*, którego wartość zaczyna się od `TODO`, w całości jako `TODO`, bez dzielenia na pozycje; test na postać opisową z przecinkiem, np. `TODO — the store of documents, once a task chooses it`. Samo `TODO` bez opisu w *Rests on* skrypt zgłasza jako błąd, z podpowiedzią, żeby opisać brakujący fakt; test i na ten przypadek.
6. WAY-71 (przez `record-decision`) i jego odbicie w `elements/common/rules.md` — zdanie o `TODO` na gałęzi głównej brzmi:
   > The main branch holds `TODO` only in an invariant's *Rests on*, in the form `TODO — <the fact, with its source>`, naming a fact the product's foundation does not hold yet; a change that leaves one there puts it before the human.

7. Szablon opisu PR-a (`task-cycle/skill/request_template.md`) każe pokazać człowiekowi każde opisowe `TODO` w *Rests on*, które zmiana zostawia na gałęzi głównej, z faktem, którego brakuje.

### Questions to settle

- Czy szablon decyzji ma dopuścić w *Origin* notatkę zadania, gdy niesie ona uzasadnienie decyzji?
  - Answer: nie — notatki zadania nigdy nie wpisujemy w *Origin*; to, co niesie z uzasadnienia, idzie do *Rationale* i *Rejected* wpisu, a *Origin* brzmi wtedy `none`.
  - Not chosen:
    - dopuścić notatkę zadania w *Origin*, gdy niesie uzasadnienie — zalegalizowałoby martwe odsyłacze.
  - Source: Mariusz, 2026-11-11, notatka tego zadania przed doprecyzowaniem, „Co zmienić”, punkt 1 („Nocny skan proponował dopuścić notatkę zadania, gdy niesie uzasadnienie — to zalegalizowałoby martwe odsyłacze, więc odpadło.”).
- Czy zakaz notatki zadania w *Origin* obejmuje też produkt, który trzyma zadania w katalogu własnego repozytorium, i jakim zdaniem szablon go uzasadnia?
  - Answer: tak — zakaz obowiązuje wszędzie, a powód brzmi tak, żeby był prawdziwy także przy zadaniach w repozytorium: miejsce zadań służy do znajdowania pracy, nie jest źródłem, na które wskazuje wpis (zasada z uzasadnienia WAY-27).
  - Not chosen:
    - zostawić brzmienie z notatki („it lies outside the repository (WAY-27) and is deleted when its task closes”) — w produkcie trzymającym zadania w repozytorium oba powody są nieprawdziwe, więc agent może uznać, że zakaz go nie dotyczy, i wpisać w *Origin* dokument zadania, który potem zniknie.
  - Source: Mariusz, 2026-11-11, „tak” (odpowiedź na pytanie, czy zakaz ma obowiązywać także tam, gdzie zadania leżą w repozytorium).
- Kiedy orkiestrator cyklu puszcza bramkę wobec kroku powrotu?
  - Answer: raz, po kroku powrotu i jego przeglądzie, na drzewie, które zostawiają; gdy bramka padnie, a jej poprawka zmieni kod, krok powrotu porównuje też zakres tej poprawki; drugi przebieg tylko tam, gdzie scalenie gałęzi docelowej zmieniło drzewo.
  - Not chosen:
    - powtarzać po kroku powrotu tylko sprawdzenia czytające fundament — w loop2 pliki fundamentu czytają też testy niezmienników i część testów symulacji, więc the way nie wie, co trzeba powtórzyć.
  - Source: Mariusz, 2026-11-11, notatka tego zadania przed doprecyzowaniem, „Co zmienić”, punkt 2.
- Czy skrypt uwag ma dodatkowo wypisywać raporty, w których nie znalazł sekcji?
  - Answer: nie — skrypt tylko rozpoznaje nagłówek z numerem.
  - Not chosen:
    - linia wyniku wymieniająca raporty bez znalezionej sekcji — z 7 takich plików 4 to nie raporty etapów, tylko inne pliki w `reports/`, więc linia byłaby głównie szumem.
  - Source: Mariusz, 2026-11-11, notatka tego zadania przed doprecyzowaniem, „Co zmienić”, punkt 3.
- Co gałąź główna może mieć w *Rests on* niezmiennika, gdy fakt, od którego zależy, nie jest jeszcze spisany?
  - Answer: opisowe `TODO — <the fact, with its source>`, które zmiana zostawiająca je na gałęzi głównej pokazuje człowiekowi.
  - Not chosen:
    - zostawić zakaz `TODO` i dopisać jego pilnowanie do skryptu — zatrzymywałby cykl na spisywaniu faktu spoza zadania.
  - Source: Mariusz, 2026-11-11, notatka tego zadania przed doprecyzowaniem, „Co zmienić”, punkt 4.
- Czy skrypt sprawdzający fundament ma zgłaszać gołe `TODO` (bez opisu faktu) w *Rests on*?
  - Answer: tak — samo `TODO` w *Rests on* jest błędem, a skrypt podpowiada, żeby opisać brakujący fakt; szablon niezmienników daje temu polu tylko postać `TODO — <the fact, with its source>`.
  - Not chosen:
    - przepuszczać gołe `TODO` — zero pracy, ale nieme `TODO`, jak to w loop2, dalej przechodzi przez skrypt i pilnuje go tylko reguła w tekście.
  - Source: Mariusz, 2026-11-11, „tak” (odpowiedź na pytanie, czy skrypt ma odrzucać samo `TODO` bez opisu brakującego faktu w *Rests on*).
- Gdzie człowiek widzi opisowe `TODO` w *Rests on*, które zmiana zostawia na gałęzi głównej („puts it before the human”)?
  - Answer: w opisie PR-a; w którym jego punkcie — wybór cyklu.
  - Source: Mariusz, 2026-11-11, przegląd warstwy AI, sprawa AIR-629 — wybór wariantu „Po krytyce (opisowe `TODO` dozwolone, pokazywane Tobie w PR)”, opisanego jako „Brak faktu jest nazwany w repozytorium i widoczny w opisie PR-a”; odpowiedź „ró” przyjęta jako „rób”.
- Czy brak własnych wytycznych kodowania i testów the way wstrzymuje to zadanie (WAY-215), skoro zmienia skrypty i testy?
  - Answer: nie wstrzymuje — zadanie idzie jak dotychczasowe zadania the way; sprawa wytycznych zostaje przy zadaniu „Ustalić, czy rozwój the way wymaga własnych wytycznych kodowania i testów”.
  - Not chosen:
    - wstrzymać zadanie w `waiting for human` do scalenia zadania o wytycznych — cztery poprawki stałyby, a dzisiejsze skutki (drugi przebieg bramki, gubione wątpliwości) trwałyby dalej; tamto zadanie nie ma wybranego kierunku, więc czekanie nie ma końca.
  - Source: Mariusz, 2026-11-11, „a” (odpowiedź na pytanie z wariantami (a) nie wstrzymuje, (b) wstrzymuje).

## Context

- Źródło: przegląd warstwy AI z 2026-11-11, sprawy AIR-624 (Origin), AIR-626 (bramka), AIR-628 (skrypt uwag), AIR-629 (`TODO` w *Rests on*) w rejestrze przeglądów w prywatnych notatkach Mariusza; obowiązują brzmienia z tego dokumentu, nie pierwotne propozycje z rejestru.
- Miejsca zmian sprawdzone na `foundations` @ `e3825a8` 2026-11-11: `elements/decisions/template.md:215-216`, `task-cycle/skill/SKILL.md:356`, `foundations/decisions.md:4561-4562` (WAY-160), `task-cycle/remarks_check.py:16-18` i `:124` (`names_section`), `elements/common/foundation_check.py:94` (`ITEM`) i `:407` (sprawdzenie *Rests on*), `elements/common/rules.md:20-21`.
- W loop2 z 359 decyzji 298 wskazuje w *Origin* notatki z vaultu; 28 z 53 wskazanych notatek już nie istnieje — stan na 2026-11-11, wg notatki tego zadania.
- WAY-27 już dziś wymienia jako naruszenie „*Origin* points to a private note”, a w *Rejected* „*Origin* pointing to the notes where the reasoning was worked out — no reader can open them”.
- Bramka w loop2 trwa ok. 35 minut; krok powrotu coś poprawił w 5 z 5 zapisanych cykli loop2 (wg notatki tego zadania).
- Krok 12 skilla cyklu już dziś każe puścić bramkę ponownie, gdy drzewo końcowe różni się od sprawdzonego w kroku 10 (`task-cycle/skill/SKILL.md:431-432`), więc przypadek scalenia gałęzi docelowej jest pokryty.
- Nagłówek z numerem wystąpił w 2 raportach na 99: `the-way` PR #89 (`author-report.md`, `## 12.`) i `loop2` PR #67 (`05-slice3-report.md`, `## 7.` — pozycja o zakresie D-349 nie trafiła do zapisu cyklu).
- Skrypt sprawdzający fundament odrzuca dziś każde opisowe `TODO` w *Rests on*, nie tylko z przecinkiem: próba na `e3825a8` dała dla `TODO — the store of documents` błąd „is no identifier of a fact”, a dla wersji z „, once a task chooses it” dwa takie błędy; gołe `TODO` przechodzi bez błędu.
- Postać opisowa jest już w the way w użyciu: `elements/invariants/template.md:44`, `elements/environment-facts/skill/decide_entry.md:3`, `project-level/test_readiness_check.py:45`.
- Przypadek gołego `TODO`: loop2 PR #70 (`test-granic-czesci`) zostawił gołe `TODO` w `invariants.md` na `main`.
- the way nie ma katalogu `guidelines/`; sprawą własnych wytycznych the way zajmuje się osobne zadanie „Ustalić, czy rozwój the way wymaga własnych wytycznych kodowania i testów” (stan `[?]`).

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-160 — How does the task-cycle orchestrator run the finished change's gate?** Zadanie zmienia przykład zgodny w *Verification* (To do 3), a do *Rejected* dopisuje: „rerunning after the return step only the checks that read the foundation — the-way does not know which checks of a product read its foundation” (Mariusz, 2026-11-11, zgoda na propozycję).
  > The task-cycle orchestrator itself runs the product's gate on the tree that goes into the request, and the request gives its command and exit code and names each check that failed or did not run; a check that did not run is unchecked, never passed. The gate's run is the orchestrator's alone: no author, executor or reviewer runs it, and neither a plan's *Checks* nor a handoff names a run of it.
  >
  > - complies: the orchestrator runs the gate after the review of the whole change and again after the return step changed the tree, and the request gives the command and its exit code;
- **WAY-71 — Does every field of a foundation entry appear in every entry, and what may it hold?** Zadanie zmienia zdanie o `TODO` na gałęzi głównej (To do 6) i uzasadnienie, które mówi, że po pojawieniu się faktów luka musi zostać zamknięta, a do *Rejected* dopisuje: „keeping the ban on `TODO` on the main branch and having the script enforce it — a cycle would stop to write a fact outside its task” oraz „letting a bare `TODO` pass — the main branch would hold a gap that names no fact” (Mariusz, 2026-11-11, zgoda na propozycję).
  > Every field an element's template gives an entry of its kind appears in every entry of its kind, holding a value, or `none` or `TODO` where the template gives it that word: `none` says nothing is there, `TODO` that something is missing. The main branch holds `TODO` only in an invariant's *Rests on*, until the facts element has entries. `elements/common/foundation_check.py` reports a missing field, or a word not given it, as an error.
  >
  > *Rationale:* … Before facts have entries, an invariant can expose a needed fact as `TODO` instead of falsely claiming `none`; once they do, the gap must be resolved.
- **WAY-27 — Where may this repository point for its reasoning?** Bez zmiany; reguła *Origin* (To do 1) na nim stoi.
  > Nothing in this repository points to a source outside it that its readers cannot reach: every entry carries its whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to. The one exception is the place of its tasks, named in the `## Backlog` section of its root `AGENTS.md` and nowhere else, by an entry of the locations file of WAY-320 and never by a path.
- **WAY-17 — Which links between foundation entries are mandatory?** Bez zmiany; wymaga, żeby niezmiennik nazywał fakty, na których stoi.
  > Every link of the chain fact → decision → invariant → test is written in the entry that depends on the other, and none is optional: a decision and an invariant name the environment facts they rest on, an invariant derived from a decision names that decision, and a check names its invariant.
- **WAY-163 — What does the cycle run before it opens a request its code review blocked?** Bez zmiany; przy PR-ze zablokowanym przeglądem bramka idzie bez kroku powrotu, co zgadza się z To do 2.
  > Before the cycle opens a request that a remaining blocking finding blocks (WAY-162), it runs the product's gate on the change and writes its cycle record with its record of stages, while it makes no further slice and runs neither the reconciliation with the target branch nor the return step on code its review has not accepted, and the request names each of these that has not run on that code.
- **WAY-294 — How does the cycle make sure its process remarks hold every item its stage reports give?** Bez zmiany; To do 4 poszerza rozpoznawanie sekcji w skrypcie, który ta decyzja ustanawia.
  > Before every commit that adds the cycle record to the product's repository, the orchestrator runs the-way's script that lists each item other than `none` under **Searches not found or unclear** in the record's stage reports — the `.md` files of the cycle's `reports/` directory whose name holds neither `handoff` nor `findings` — that the record's process remarks do not hold word for word, appends each listed item word for word with its stage name and full report path, and runs the script again until it lists nothing.

## Settlements to record

Candidates: 5 shown, 0 accepted — 2026-11-11

none

## Out of scope

- Stare wpisy *Origin* w loop2 wskazujące notatki z vaultu — osobne zadanie w (P) Loop, zależne od tego.
- Gołe `TODO` w `invariants.md` loop2 na `main` — po przypięciu nowego the way skrypt je zgłosi, a opisanie go należy do tamtej aktualizacji w loop2.
- Numeracja kroków 10 i 11 w skillu cyklu — zostaje; zmienia się tylko chwila puszczenia bramki.
