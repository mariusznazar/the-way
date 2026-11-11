---
title: "the way: cotygodniowy audyt, czy proces faktycznie staje się lepszy, tańszy i szybszy"
status: draft
created: 2026-11-11T22:00
updated: 2026-11-11
tags: [zadanie]
related: "the project note in the author's notes"
---

# the way: cotygodniowy audyt, czy proces faktycznie staje się lepszy, tańszy i szybszy

Status: ready for cycle
Project relation: independent

## Description

### Need

- Cykle zadań zapisują uwagi o tarciu w procesie, a poprawki z nich wchodzą do the way, ale nic nie sprawdza okresowo, czy proces staje się lepszy, tańszy i szybszy, ani czy wdrożona poprawka usuwa problem.
- Mariusz decyduje, w co inwestować pracę nad the way i setupem agentów, na podstawie pojedynczych spraw, a nie obrazu całości.
- Usprawnieniem jest zmiana, która poprawia jakość, koszt i czas naraz albo dwie z nich bez szkody, lub z minimalną szkodą, dla trzeciej.

### To do

1. Audyt dostaje własną część the way z własnym katalogiem: wpis w mapie części i zmiana WAY-09, która dopisuje ten katalog do listy katalogów repozytorium.
2. Szablon rejestru problemów: przy każdym problemie zapis cyklu, z którego pochodzi (repozytorium i commit zapisu), etapy, które go zgłosiły, klasa, waga, sprawa, do której należy, jej los i — dla sprawy wdrożonej — commit the way z poprawką. Szablon niesie startową listę klas (potwierdzenie; sprawdzenie niewykonane albo niepewne; niejasność rozstrzygnięta wyborem agenta; brak w fundamencie produktu; znany problem zostawiony; nieaktualne odwołanie w zadaniu albo planie; uwaga o procesie) i skalę wagi (brak problemu, Minor, Important, Critical — skala recenzji cyklu z poziomem zerowym); użytkownik dostosowuje go do siebie.
3. Polecenie liczenia audytu czyta zapisy cykli z repozytoriów, które wskazuje użytkownik, oraz rejestr problemów, i daje:
   - przy każdym cyklu: wersję the way, na której cykl działał (*Process pin* zapisu), liczbę uwag, problemy według klasy i wagi (ten sam problem z kilku etapów raz), koszt w stałych cenach, udział rund poprawek po recenzji w koszcie, czas pracy agentów i czas czekania na narzędzia;
   - przy każdej sprawie wdrożonej: powroty problemu w cyklach, których wersja the way zawiera poprawkę, i osobno w cyklach bez niej;
   - przy każdej sprawie otwartej: liczbę cykli, w których problem wrócił, i liczbę dni czekania;
   - przy każdej wersji procesu: medianę kosztu cyklu w stałych cenach oraz odpowiedzi na trzy pytania o uproszczenie reguł specu i planu — czy sprzeczność z ustaleniami produktu wyszła dopiero po napisaniu kodu, czy więcej niż co trzeci kawałek planu wrócił jako za duży, czy koszt cyklu spada.
4. Koszt w stałych cenach liczy się cennikiem modeli z datą, który leży w części audytu; nowy cennik zaczyna nową serię. Zmiana formatu raportu etapu, listy klas albo instrukcji recenzenta też zaczyna nową serię, a wynik nie porównuje liczb z różnych serii wprost.
5. Skill audytu prowadzi cotygodniową sesję: czyta wynik liczenia, pokazuje Mariuszowi sprawy do zważenia — bez nadawania priorytetu z samej częstości — i zapisuje wynik audytu w miejscu użytkownika.
6. Rejestr problemów i miejsce wyników audytu wskazują wpisy pliku lokalizacji użytkownika pod `the-way`; skill i polecenie znajdują je tak jak backlog, a gdy wpisu brak, pytają człowieka.
7. `stages.md` w zapisie cyklu podaje osobno czas czekania na narzędzia; wywołanie podagenta nie jest czekaniem na narzędzie, liczy się jako praca podagenta.
8. Polecenie liczenia da się uruchomić bez człowieka, tak żeby harmonogram systemu mógł je odpalić w nocy z piątku na sobotę.

### Questions to settle

- Skąd audyt bierze klasę i wagę każdego problemu oraz powiązanie problemu z poprawką, która miała go usunąć?
  - Answer: the way określa szablon rejestru problemów — przy każdym problemie cykl, klasa, waga, sprawa i jej los, w tym to, czy cykl miał poprawkę — a audyt czyta rejestr wskazany wpisem w pliku lokalizacji użytkownika. Rejestr wypełnia narzędzie użytkownika; inny użytkownik the way dostosowuje szablon do siebie.
  - Not chosen:
    - audyt sam czyta zapisy cykli i sam nadaje klasę i wagę — te same uwagi oceniają dwa agenty, mogą ocenić inaczej, a powiązanie z poprawką trzeba odtwarzać
    - the way przejmuje przegląd uwag cykli — największa zmiana, a uwagi zamieniają się w sprawy raz w tygodniu zamiast co noc
  - Source: Mariusz, 2026-11-11: „zdecydowanie B”; „jeśli zaproponujemy szablon to inny użytkownik the way może go dostosować tak samo”
- Gdzie w repozytorium the way stoi audyt?
  - Answer: we własnej części, z własnym katalogiem, tak jak przegląd fundamentu — audyt nie odpowiada ani na pytanie cyklu zadania, ani na pytanie elementu fundamentu.
  - Not chosen:
    - wewnątrz `task-cycle/` — część cyklu zaczyna odpowiadać za ocenę całego procesu w czasie, inne pytanie niż przeprowadzenie jednego zadania, a jej decyzje przegląda każdy agent cyklu
  - Source: Mariusz, 2026-11-11: „własna część”
- Czy osobny czas czekania na narzędzia w `stages.md` (punkt 7) idzie osobnym zadaniem?
  - Answer: nie — zostaje w tym zadaniu; cykl i tak dzieli zmianę na kawałki, a całość wyjdzie spójnie.
  - Not chosen:
    - osobne małe zadanie the way — dodatkowy, choć krótki cykl; w zamian to zadanie dotykałoby tylko nowej części, mapy części i WAY-09
  - Source: Mariusz, 2026-11-11: „zadanie i tak będzie podzielone na kawałeczki - nie widzę potrzeby podziału, a wyjdzie spójnie”
- Czy brak własnych wytycznych kodowania i testów the way wstrzymuje to zadanie (WAY-215), skoro pisze skrypt i testy?
  - Answer: nie wstrzymuje — zadanie idzie jak dotychczasowe zadania the way; sprawa wytycznych zostaje przy zadaniu „Ustalić, czy rozwój the way wymaga własnych wytycznych kodowania i testów”.
  - Not chosen:
    - wstrzymać zadanie do powstania wytycznych — stałoby co najmniej przez jedno, a raczej dwa zadania i ich cykle; kod napisany teraz dopasuje audyt wytycznych, tak jak cały istniejący kod the way
  - Source: Mariusz, 2026-11-11: „nie czeka”
- Gdzie leżą wyniki audytu?
  - Answer: w miejscu użytkownika poza repozytoriami, wskazanym wpisem w pliku lokalizacji użytkownika.
  - Not chosen:
    - w repozytorium the way — repozytorium jest publiczne, a wyniki niosą nazwy produktów i treść uwag z ich cykli
  - Source: Mariusz, 2026-11-11: „tak”

## Context

- Pytania, miary i rytm audytu Mariusz ustalił 2026-11-11 w rozmowie; zebrane są w notatce projektu „Audyt usprawniania procesu — pytania, miary i rytm”.
- Dziś klasyfikację uwag cykli na proces, produkt i sam zapis oraz zamianę ich w sprawy robi nocny przegląd w prywatnym setupie Mariusza; zapisuje przy cyklu tylko liczbę uwag w każdej kategorii.
- `stages.md` zapisu cyklu podaje tokeny według rodzaju i modelu oraz czas etapów, a czas etapu łączy pracę modelu z czekaniem na narzędzia (`task-cycle/cycle_stages.py`).

## Questions carried to cycle

none

## Human actions

- Założyć w harmonogramie zadań systemu uruchamianie liczenia audytu w nocy z piątku na sobotę — in the cycle
- Dodać do backlogu cotygodniowe zadanie przeprowadzenia audytu — in the cycle

## Decisions in play

- WAY-09 — What may enter the process repository? Zadanie zmienia ją: lista katalogów repozytorium zyskuje katalog części audytu, a zdanie o tym, co katalog musi zawierać, zyskuje jego zawartość. Brzmienie dziś: „On the main branch, this repository holds `foundations/` with the entries of the-way itself, a directory for each part of the process other than `repository` — `elements/<element>/` for each foundation element, `elements/common/` for what the elements share, `relation-model/`, `gate/`, `installation/`, `agent-instructions/`, `instruction-files/`, `project-level/`, `product-guidelines/`, `foundation-review/` and `task-cycle/` — the files that configure the whole repository, which its part map gives to the `repository` part (WAY-44), the root agent instruction files and the project skill entry points under `.claude/skills/` and `.agents/skills/`, which the map gives to `agent-instructions` (WAY-44), and a `README.md` that describes the repository. A directory reaches the main branch only once it holds what its part requires: (…) `foundation-review/` the skill that reviews a product's foundation against the product, with the files it names; `task-cycle/` what the design of the task cycle sets.”
- WAY-103 — Who is the-way for? „The-way is built first for its author and aims at anyone who builds a technology product and adopts the process for their own needs; the process is written for the agents that carry out the task cycle too.”
- WAY-140 — How does a task change something outside the product's repository? „A task's effect outside the product's repository — on a server, in DNS, on keys or on an external account — is made only by a human, through a human action the task document names and places before the cycle or in it, while reading outside the repository stays with the agent (…)”
- WAY-260 — What does each task-cycle stage report about what it could not find or understand? „Every task-cycle stage's report states each thing the agent looked for and did not find, or found unclear, wherever it arose, or `none`; it keeps this separate from the report's account of each reach beyond the dispatch. The orchestrator copies every such item other than `none` word for word, with the stage name and full report path, into the cycle record's *Process remarks on the-way*, without combining repeated items.”
- WAY-296 — In what form does the cycle record hold its process remarks? „The cycle record holds its process remarks in the one form its template gives, which the check of WAY-294 reads, and in no section or file of their own.”
- WAY-320 — Where does a user keep the places outside every repository that the files of the-way name? „A user's places on their own disk that lie outside every repository, such as the place of a product's tasks and the place of its projects, are kept in one file, `~/.the-way/locations.json` (…) a file that points to such a place names its entry in the locations file.”

## Settlements to record

Candidates: 13 shown, 12 accepted — 2026-11-11

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | the way określa szablon rejestru problemów, audyt czyta rejestr wskazany wpisem w pliku lokalizacji użytkownika, a wypełnia go narzędzie użytkownika, który dostosowuje szablon do siebie | decision | Questions to settle: „Skąd audyt bierze klasę i wagę…” | czy audyt sam czyta zapisy cykli i sam nadaje klasę i wagę |
| 2 | Audyt jest własną częścią the way z własnym katalogiem, osobno od cyklu zadania | decision | Questions to settle: „Gdzie w repozytorium the way stoi audyt?” | czy położyć audyt w `task-cycle/` |
| 3 | Wyniki audytu leżą w miejscu użytkownika poza repozytoriami, wskazanym wpisem w pliku lokalizacji | decision | Questions to settle: „Gdzie leżą wyniki audytu?” | czy zapisywać wyniki w repozytorium the way |
| 4 | Każdy problem ma wagę w czterech poziomach (brak problemu, Minor, Important, Critical) i klasę z listy, którą szablon zaczyna, a audyt poszerza | decision | Mariusz, 2026-11-11: „tak” na cztery poziomy i listę startową klas poprawianą w audycie | skala wagi (np. pięć poziomów) i zamknięta lista klas |
| 5 | Audyt liczy problemy, nie uwagi: ten sam problem zgłoszony przez kilka etapów cyklu to jeden problem | decision | Mariusz, 2026-11-11: „to są zwyczajnie problemy wpuszczone bez poprawki”; próbka: jeden brak zgłoszony przez trzy etapy | czy liczyć każdą uwagę osobno |
| 6 | O tym, czy poprawka działa, rozstrzygają cykle, których wersja the way ją zawiera, a nie data | decision | Context: pytania audytu; zapis cyklu niesie *Process pin* | porównanie przed i po dacie wdrożenia poprawki |
| 7 | Częstość powrotów sprawy jest materiałem do ważenia przez człowieka; audyt nie nadaje z niej priorytetu | decision | Mariusz, 2026-11-11: „czy to, że coś jest częste oznacza, że automatycznie rośnie priorytet? nie, więc to trzeba zważyć zawsze” | ranking spraw według liczby powrotów |
| 8 | Koszt cyklu to koszt w stałych cenach według cennika z datą i udział rund poprawek w koszcie, bez mianownika wielkości zadania | decision | Mariusz, 2026-11-11: „Koszt mierzymy tymi dwiema liczbami bez mianownika.” | suma tokenów albo koszt na zmienioną linię |
| 9 | Czas cyklu to czas pracy agentów bez czekania na człowieka i osobno czas czekania na narzędzia | decision | Mariusz, 2026-11-11: „miałem na myśli głównie czas pracy agentów, ale pewnie do pary można dorzucić też czas kiedy agent czekał na skrypty - oczekiwania na mnie nie wliczałbym” | czas od startu do scalenia |
| 10 | Nowy cennik oraz zmiana formatu raportu etapu, listy klas albo instrukcji recenzenta zaczynają nową serię; miary porównuje się w obrębie serii i wersji procesu, nie tydzień do tygodnia | decision | rozmowa 2026-11-11: wzrost uwag po WAY-260; Mariusz przyjął ocenę na cyklach wersji procesu | porównanie tydzień do tygodnia przez zmianę formatu |
| 11 | Audyt nie odtwarza zamrożonych dawnych zadań na starej i nowej wersji procesu | decision | Mariusz, 2026-11-11: „tak, zestaw zamrożonych zadań skreślamy” | dołożenie zestawu kontrolnego zadań |
| 12 | Audyt odbywa się raz w tygodniu, osobno od przeglądu tygodnia; liczenie biegnie bez człowieka w nocy z piątku na sobotę, a sesję wyzwala cotygodniowe zadanie w backlogu | decision | Mariusz, 2026-11-11: „wolałbym dedykowane zadanie pod audyt, nie mieszałbym tego z przeglądem tygodnia”; „liczenie automatyczne przed sobotą, spoko” | audyt w przeglądzie tygodnia albo na żądanie |

## Out of scope

- Przestawienie nocnego przeglądu w prywatnym setupie Mariusza na szablon rejestru problemów — osobne zadanie poza repozytorium the way.
