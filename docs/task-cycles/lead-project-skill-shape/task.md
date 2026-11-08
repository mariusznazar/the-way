---
title: "the way, seria skilli 10/11: lead-project według zmienionej WAY-256 — kroki, przez które przechodzi każde użycie, w SKILL.md, warianty i krok 5 w plikach obok"
status: draft
created: 2026-11-08
updated: 2026-11-08
tags: [zadanie]
related: "the project note of the author's process work"
---

# lead-project według zmienionej WAY-256 — kroki, przez które przechodzi każde użycie, w SKILL.md, warianty i krok 5 w plikach obok

Status: ready for cycle
Project relation: independent

## Description

### Need

- Skill `lead-project` the way to jeden plik `project-level/lead/skill/SKILL.md` o 2580 słowach na `foundations` `a3206c1`, bez żadnego pliku obok w swoim katalogu `project-level/lead/skill/`; WAY-256 każe fragment jednego kroku albo wariantu trzymać w pliku obok skilla.
- Skill ma kroki 0–5; w nich stoją fragmenty potrzebne tylko w jednym wariancie: powrót zadania z zamkniętego requestu do doprecyzowania (`project-level/lead/skill/SKILL.md:61–77`, 240 słów, tylko na słowo człowieka, WAY-269), zlecenie przebiegu `settle-technology` (`:113–118`, 67 słów) i cały krok 5, zmiana planu albo definicji (`:189–219`, 399 słów).
- W ośmiu prawdziwych użyciach skilla w `loop2` (2026-10-24 – 2026-11-06) orkiestrator przeszedł kroki 0–4 w każdym, krok 5 ze zmianą planu w siedmiu, a zmianę definicji z bramką gotowości w czterech; powrotu zadania z zamkniętego requestu ani przebiegu `settle-technology` nie było w żadnym, a oba fragmenty stały w skillu tylko w dwóch ostatnich użyciach. Kroki 4 i 5 szły wewnątrz rundy kroku 3, a krok 1 powtarzał się po scaleniach.
- Orkiestrator czytał `SKILL.md` w całości raz, w pierwszych 2–6 wywołaniach modelu, i niósł go przez ok. 80–250 kolejnych wywołań.
- Agenci nieśli tekst skilla przez ok. 2,4 mln tokenów od 2026-09-01 — dziesiąty wynik serii, z czego 0,1 mln w sesjach w samym repo the way (miara serii, the ranking file of the series: 5 odczytów, 5 agentów).
- WAY-256 i `instruction-files/kind_skill.md:13–14` każą przenieść do pliku obok procedurę kroku także wtedy, gdy dochodzi do niej każde użycie skilla; przy `lead-project` pełny kształt dałby typowej sesji ok. 5–15% słów więcej, a celem serii jest koszt (pytanie 3).

### To do

1. WAY-256 jest zmieniona w miejscu według wiersza 1 *Settlements to record*: krok skilla zostaje w `SKILL.md`, dopóki zapisy sesji nie pokażą, że część użyć go pomija, a do plików obok idą warianty i takie kroki (pytania 3 i 11). *Rationale* i *Rejected* WAY-256 mówią to samo co nowe zdania wiążące: zdania, które przeczą wierszowi 1 (`foundations/decisions.md:7605`, `:7609`, `:7634` na `a3206c1`), cykl przeredagowuje, a powód i sposoby niewybrane bierze ze źródła wiersza 1. Tak samo mówią `instruction-files/kind_skill.md:9`, `:13–14` i `:20` oraz uzasadnienia WAY-125 (`foundations/decisions.md:3011–3013`) i WAY-127 (`:3121–3123`), a także każde inne miejsce, które jednorazowe przeszukanie całego fundamentu (WAY-33) znajdzie powtarzające starą regułę. Ta zmiana stoi przed oceną skilla, bo ocena stosuje regułę po zmianie.
2. `lead-project` jest oceniony skillem `the-way-maintain-instruction-files` w trybie oceny, z plikiem rodzaju „skill”, po przeszukaniu zapisów sesji, które `instruction-files/judging.md:7–9` stawia przed tabelą — zapisów Claude Code w the session-records folder of Claude Code for the product `loop2`, w tym ośmiu użyć wymienionych w *Context*.
3. Skill jest przebudowany według tej oceny: kroki 0–4 zostają w `SKILL.md`; do plików obok w `project-level/lead/skill/` idą krok 5 (pytanie 4) i trzy warianty — powrót zadania z zamkniętego requestu do doprecyzowania (`project-level/lead/skill/SKILL.md:61–77`), zlecenie przebiegu `settle-technology` (`:113–118`) i zmiana definicji z bramką gotowości (co najmniej `:202–219`; zdania `:197–201` służą też zmianie planu bez zmiany definicji, a dokładną granicę ustala ocena). `SKILL.md` wymienia każdy plik wariantu przy kroku, który do niego prowadzi, z warunkiem, kiedy się go czyta (WAY-265). Nagłówki kroków 0–5 i numery 3.1–3.6 zostają.
4. Poza `project-level/lead/skill/` i zmianą z punktu 1 nic się nie zmienia: `project-level/lead/answering.md`, `project-level/lead/conversation_template.md` i pliki innych skilli zostają, jak są (pytania 1 i 2).
5. Request podaje tabelę oceny skilla: fragment zacytowany dosłownie z zakresem linii na `a3206c1`, kiedy jest potrzebny, czy agent rozpozna ten moment, werdykt i miejsce po przebudowie (WAY-257, WAY-311).
6. Request podaje liczby słów przed przebudową i po niej na sześciu drogach z pytania 5.
7. Request podaje jako propozycje werdykty „remove” i „reword” zmieniające treść reguły w skillu.

### Acceptance criteria

- Poza WAY-256 i miejscami z punktu 1 *To do* żadna reguła nie znika ani nie zmienia znaczenia: każdy fragment skilla stoi po przebudowie w `SKILL.md` albo w pliku obok, który wymienia krok albo wariant, w którym jest potrzebny.
- Każdy przeredagowany warunek wariantu albo odsyłacza jest porównany z bazą i nie dodaje drogi ani żadnej nie gubi, a przy każdym nowym zdaniu — także zdaniu otwierającym plik obok — autor nazywa, co ono wyłącza.
- Warunek każdego odsyłacza do pliku wariantu obejmuje każdą drogę do niego i jest sformułowany przez dojście do kroku, nie przez start na nim: powrót zadania — krok 1 na starcie sesji i krok 1 powtórzony po scaleniu w jej środku; zlecenie `settle-technology` — pierwsza i każda dalsza tura rundy, także po wznowieniu z plików rozmowy; krok 5 — wynik `plan change` w akapicie po 3.6 i zmieniona definicja w kroku 0 (`:37–39`); zmiana definicji — krok 5 i odzyskiwanie otwartej bramki w kroku 0 (`:45`).
- Każde zdanie przeniesione do pliku obok autor czyta osobno, zwłaszcza zaimki i słowa wskazujące („below”, „above”, „this step”, „(step 6)” w 3.3, `:134`), a odwołania z kroków, które zostają w `SKILL.md`, do tekstu, który wyszedł (np. „step 5's definition gate” w kroku 4, `:168–169`), dalej trafiają.
- Czytelnik spoza skilla trafia na odsyłacz pod tym samym nagłówkiem: `project-level/plan/template.md:102` („only as `lead-project` gives”), `project-level/plan/skill/hand_over.md:16`, `project-level/plan/skill/delegated_mode.md:3–4`, `project-level/skill/delegated_mode.md:4–7` oraz krytycy i doprecyzowujący, którym zlecenie wskazuje część skilla (*Context*); request mówi przy każdym, co czytelnik traci, jeśli cokolwiek.
- Edycja WAY-256 mieści się w trzech zdaniach wiążących (WAY-05); jej *Rationale* bierze powód ze źródła wiersza 1, a *Rejected* — sposoby, których Mariusz nie wybrał.
- Recenzent przechodzi ręcznie drogi 1, 4 i 6 z pytania 5, od `SKILL.md` do pliku ostatniego kroku, tak jak zrobiłby to agent, wypisuje, co na każdej zostaje i co odpada, i porównuje każdy wiersz tabeli oceny z miejscem, w którym fragment naprawdę stanął.
- Opis skilla (`description`) i kod w Pythonie się nie zmieniają, więc wejścia `the-way-*` też nie.
- Liczby słów powstają po ostatniej zmianie liczonego pliku, a pomocniczy skrypt porównuje z plikami każdą liczbę podaną w requeście, także w prozie; liczbę z tego dokumentu, która nie zgadza się z plikiem w podanym zakresie wierszy, request zgłasza jako rozbieżność.

### Questions to settle

- 1. Co oprócz `project-level/lead/skill/SKILL.md` przebudowa może ruszyć?
  - Answer: tylko katalog `project-level/lead/skill/` — `SKILL.md` i nowe pliki obok. `project-level/lead/answering.md`, `project-level/lead/conversation_template.md` i pozostałe pliki the way zostają bez zmian; ocena może przenieść samo polecenie czytania któregoś z nich z kroku 0 na krok, który go używa.
  - Not chosen:
    - także przebudowa `answering.md` i `conversation_template.md` — kilkaset słów mniej u orkiestratora i może u doprecyzowujących, ale to nie są skille, plik rozmowy czyta sześć innych skilli, więc zmiana dotyka ich czytelników, a recenzent oceniałby treść, nie tylko miejsce.
    - zostawić skill jak jest — nic dziś nie kosztuje, bo WAY-256 nie wiąże fragmentów stojących bez zmian, ale seria kończy się z otwartą pozycją, a orkiestrator niesie od startu dwa nieużywane warianty i krok 5.
  - Source: Mariusz, 2026-11-08: „A” — na rekomendację A, ze słabym punktem nazwanym w pytaniu: największy tekst czytany na starcie — szablony planu i zadania oraz oba pliki z `project-level/lead/`, razem ok. 6300 słów — zostaje bez zmian, więc zysk w słowach będzie skromny. Stan: `answering.md` to cała metoda agenta odpowiadającego; `conversation_template.md` czytają doprecyzowujący, odpowiadający, tury zlecone `plan-project` i `define-project` oraz trzy skille wytycznych.
  - Rozszerzenie po pytaniu 3 (pytanie 10): wybór B1 zmienia WAY-256, więc zadanie zmienia też miejsca, które powtarzają starą regułę — `instruction-files/kind_skill.md:9`, `:13–14`, `:20`, uzasadnienia WAY-125 i WAY-127 oraz inne, które znajdzie przeszukanie całego fundamentu (punkt 1 *To do*). Mariusz, 2026-11-08: „tak, zgadzam się” — na rekomendację zgody, ze słabym punktem nazwanym w pytaniu: zakres przeszukania nie jest zamknięty co do pliku. Bez zmiany narzędzie oceny dalej każe przenosić kroki, do których dochodzi każde użycie.
- 2. Które z pięciu uwag pierwszego przeglądu fundamentu the way (2026-11-07), przypisanych temu zadaniu, wchodzą do przebudowy?
  - Answer: żadna — theway#063-4, #063-5, #069-7, #069-8 i #026-19 zmieniają treść reguł, a cztery z nich leżą poza `project-level/lead/skill/`; zostają w pliku uwag, a gdzie trafią, rozstrzyga pytanie o domknięcie serii.
  - Not chosen:
    - dołączyć uwagi — recenzent ocenia treść pięciu reguł, a pomiar po scaleniu pokazuje skutek dwóch zmian naraz; #069-8 to cztery słowa, ale w pliku `plan-project`, wbrew odpowiedzi na pytanie 1, a orkiestrator `lead-project` nic przez nią nie traci, bo jego krok 0 sam każe uruchamiać sprawdzenia na całych oryginałach.
  - Source: Mariusz, 2026-11-08: „tak, zgadzam się” — na rekomendację „żadna”, ze słabym punktem nazwanym w pytaniu: seria kończy się na tym zadaniu, więc uwagi nie mają już kolejnego zadania serii, do którego by przeszły. Stan: uwagi stoją w the file of remarks of the first review of the foundation in the author's notes, sekcja „Dopisek: przebudowa lead-project (seria skilli 10/11)”; przebiegu `settle-technology` w rundzie, którego dotyczą #063-4 i #063-5, nie było w żadnym z ośmiu użyć w `loop2`.
- 3. Jak rozłożyć skill na pliki obok, skoro w `loop2` każde użycie przeszło kroki 0–4, siedem z ośmiu krok 5, a cztery zmianę definicji?
  - Answer: tylko warianty idą do plików obok — powrót zadania z zamkniętego requestu do doprecyzowania (`project-level/lead/skill/SKILL.md:61–77`), zlecenie przebiegu `settle-technology` (`:113–118`) i zmiana definicji z bramką gotowości (`:197–219` w pytaniu; krytyk pokazał, że `:197–201` służy też zmianie planu, więc w *To do* stoi `:202–219`); kroki 0–4 zostają w `SKILL.md`, a krok 5 rozstrzyga pytanie 4. Szacunek w pytaniu, przed pytaniem 4: typowa sesja ok. 2350–2450 słów skilla zamiast 2580 (−5 do −9%).
  - Not chosen:
    - pełny kształt: plik na każdy krok 0–5 i na trzy warianty — `SKILL.md` ok. 600–800 słów, suma plików o ok. 500–800 więcej; typowa sesja ok. 2700–3000 słów (+5 do +15%), sesja bez zmiany definicji ok. 2400–2700, sesja kończąca się na uzgodnieniu postępu ok. 1300; w mierze serii wynik bliski zera (±10%), zysk w mniejszej liczbie instrukcji naraz na początku sesji.
    - pełny kształt bez osobnego pliku zmiany definicji — plik mniej, ale w trzech sesjach na osiem orkiestrator niesie ok. 300 słów bramki, której nie używa.
  - Source: Mariusz, 2026-11-08: „a czemu rekomendujesz A skoro naszym celem jest żeby było taniej? […] ja wybieram B” — wbrew rekomendacji pełnego kształtu; słaby punkt nazwany w pytaniu: wariant jest niezgodny z WAY-256, bo każdy krok to fragment jednego kroku, a wyjątek dla pierwszego kroku Mariusz odrzucił w zadaniu 4. Rekomendacja pełnego kształtu wyszła z WAY-256 („the measure is the instructions in play, not the words”) i z ustalenia serii z zadania 4, nie z celu serii, którym jest koszt.
  - Pytanie przeciw wyborowi (WAY-113), kotwica — notatka serii, „Otwarte wątki / decyzje”: „procedura każdego kroku idzie do pliku obok także wtedy, gdy dochodzi do niej każdy przebieg, kroki pierwsze włącznie […] wyjątek dla pierwszego kroku odrzucony tamże” (Mariusz, 2026-10-30). Odpowiedź: Mariusz, 2026-11-08: „B obowiązuje, B1” — wybór wchodzi do WAY-256 jako reguła ogólna: krok, do którego w zapisach sesji dochodzi każde użycie skilla, zostaje w `SKILL.md`, a do plików obok idą warianty i kroki, które część użyć pomija; rozstrzyga pomiar z zapisów sesji. Not chosen:
    - wyjątek nazwany tylko dla `lead-project` — najmniejsza zmiana, ale przy następnym skillu o tym samym profilu sprawa wraca, a wyjątek nazwany po skillu zamiast po plikach już raz zawiódł (wniosek z zadania 5).
    - bez zmiany fundamentu, wyjątek tylko w opisie zadania — PR łamie wiążącą decyzję, recenzent to zgłosi, a następna sesja uzna skill za niezgodny.
  - Słaby punkt B1 nazwany w pytaniu: zmienia znaczenie decyzji, na której stoi seria; skille przebudowane wcześniej z plikiem kroku, do którego dochodzi każde użycie, przestają pasować do reguły, choć jej nie łamią, bo WAY-256 nie wiąże fragmentów stojących bez zmian. Mariusz, 2026-11-08: „jeśli nie zauważyłem tego przy poprzednich przebudowach to pewnie tamte skille przy jakiejś okazji trzeba będzie jeszcze raz przebudować”.
- 4. Gdzie staje krok 5, skoro B1 wysyła do plików obok kroki, które część użyć pomija, a krok 5 pominęło jedno z ośmiu użyć (`323c603d`)?
  - Answer: krok 5 idzie do pliku obok, a zmiana definicji z bramką gotowości do osobnego pliku wariantu, który `SKILL.md` wymienia przy kroku 5 z warunkiem, kiedy się go czyta (WAY-265).
  - Not chosen:
    - krok 5 w jednym pliku razem ze zmianą definicji — plik mniej, ale w trzech sesjach na osiem orkiestrator niesie ok. 300 słów bramki, której nie używa, wbrew części WAY-256 o wariantach, której B1 nie zmienia.
    - krok 5 zostaje w `SKILL.md`, do pliku idzie tylko zmiana definicji — najtańsze w typowej sesji (ok. 50 słów mniej), ale wymaga czytania „każde użycie” jako „prawie każde”, czego B1 nie daje, a recenzent zgłosi niezgodność z regułą, którą zapisuje to samo zadanie.
  - Source: Mariusz, 2026-11-08: „a” — na rekomendację a, ze słabym punktem nazwanym w pytaniu: krok potrzebny w siedmiu sesjach na osiem dostaje plik, więc te siedem płaci ok. 40–60 słów odsyłacza i zdania otwierającego.
- 5. Na jakich drogach request liczy słowa przed przebudową i po niej?
  - Answer: na sześciu: (1) kroki 0–5 ze zmianą definicji i bramką gotowości; (2) kroki 0–5 ze zmianą planu bez zmiany definicji; (3) bez kroku 5, także sesja kończąca się na uzgodnieniu postępu; (4) powrót zadania z zamkniętego requestu (krok 1), potem kroki 0–5 ze zmianą planu; (5) runda ze zleceniem przebiegu `settle-technology` (krok 3.1), kroki 0–5 ze zmianą planu; (6) krytyk albo doprecyzowujący, któremu zlecenie wskazuje część skilla, np. „definition-change route”. Na każdej dwie liczby: sam tekst skilla oraz suma z plikami czytanymi obok w kroku 0, które się nie zmieniają — `project-level/plan/template.md`, `project-level/task/template.md`, `project-level/lead/conversation_template.md`, `project-level/lead/answering.md`, sekcje „How a skill asks” i „Reading the foundation” `elements/common/way_of_working.md` oraz `project-level/plan/skill/reading_definition_and_plan.md`. Pliki wywoływanych skilli (`plan-project`, `define-project`, `settle-technology`, `critique`), plan, definicja i pliki produktu są poza liczeniem. Odsyłacz „Read <plik>” liczy się jako przeczytanie i wykonanie. Słowa liczy skrypt jak `wc -w` w locale C, w stanie „przed” na `a3206c1`; każda liczba w requeście stoi z zakresem wierszy, z którego pochodzi. Recenzent przechodzi ręcznie drogi 1, 4 i 6.
  - Not chosen:
    - trzy drogi z sesji (1–3) — krótszy request, ale znika sprawdzenie, czy powrót zadania i badanie technologii są osiągalne z kroków, które je wymieniają, choć krok 1 powtarza się po scaleniach w środku sesji.
    - jedna liczba, słowa w `SKILL.md` — najtaniej, ale pokaże ok. −20%, gdy typowa sesja zyskuje kilka procent.
  - Source: Mariusz, 2026-11-08: „A” — na rekomendację A, ze słabym punktem nazwanym w pytaniu: to liczby słów w plikach, nie zachowanie agenta. Szacunek z pytania, sam tekst skilla, 2580 słów przed na każdej drodze: (1) ok. 2400–2550, (2) ok. 2050–2250, (3) ok. 1950–2100, (4) ok. 2300–2500, (5) ok. 2150–2350, (6) ok. 2400–2550; suma plików ok. 2750–2950, o ok. 170–370 więcej niż dziś; pliki czytane obok w kroku 0 mają razem 7253 słowa (w pytaniu podano 7261, licząc nagłówki następnych sekcji).
- 6. Kiedy i czym mierzymy niesiony tekst po scaleniu?
  - Answer: przy następnym prawdziwym użyciu skilla w `loop2`, skryptami serii z datą początkową po scaleniu, nie przy domknięciu zadania; do tego czasu główną miarą zostają słowa z requestu, a gdy użycie pójdzie w Codexie, porównanie liczy się osobno z jego zapisów.
  - Not chosen:
    - pomiar przy domknięciu — liczba mówi tylko, ile czasu minęło, a wygląda jak wynik.
  - Source: odpowiedź z zadania 8 (the author's note of task 8 of the series, pytanie 6): Mariusz, 2026-10-31: „Tak” — ze słabymi punktami nazwanymi tam: porównanie może długo czekać, a `skill_carry_cost.py` potrzebuje parametru daty; przeniesiona do zadań 6, 7 i 11. Przeniesienie pokazano Mariuszowi 2026-11-08, z dopiskiem, że `lead-project` szedł w `loop2` osiem razy w dwa tygodnie; Mariusz, 2026-11-08: „ok”.
- 7. Czy agenci cyklu czytają metody z worktree zadania?
  - Answer: tak — z worktree zadania, jak w zadaniach 2–9 i 11, bez kopii the way na commicie bazowym; kopii potrzebowało tylko zadanie 1 (PR #50, `.runs/the-way-base/`), bo zmieniało skille cyklu, a `task-cycle/` na `a3206c1` nie wymienia `lead-project`.
  - Not chosen:
    - kopia the way na commicie bazowym — krok więcej na starcie, który nic nie chroni.
  - Source: odpowiedź z zadania 8 (the author's note of task 8 of the series, pytanie 7): Mariusz, 2026-10-31: „Tak”. Stan: zapisy cykli PR-ów #50–#85 w historii gita (`docs/task-cycles/*/cycle.md`). Przeniesienie pokazano Mariuszowi 2026-11-08, po jego pytaniu „na pewno wcześniejsze zadania serii nie szły drogą cyklu? chyba było różnie”; Mariusz, 2026-11-08: „ok”.
- 8. Którą drogą idzie zadanie i czy czeka na wytyczne samego the way?
  - Answer: przechodzi cykl `implement-task`, jak wszystkie zadania serii, a integruje się drogą z `agent-instructions/README.md` (branch z `foundations`, test całości, request do `foundations`); nie czeka na wytyczne samego the way, bo katalogu `guidelines/` nie ma, a zadanie zmienia tylko pliki Markdown i wpis fundamentu.
  - Not chosen:
    - czekać na wytyczne samego the way — seria stoi bez żadnego zysku.
  - Source: odpowiedź z zadania 8 (the author's note of task 8 of the series, pytanie 8): Mariusz, 2026-10-31: „Tak”. Stan: każdy PR serii, #50–#85, ma zapis cyklu w `docs/task-cycles/`. Przeniesienie pokazano Mariuszowi 2026-11-08 w poprawionym brzmieniu; Mariusz, 2026-11-08: „ok”.
- 9. Co robi sesja domykająca zadanie 10, skoro to ostatnie zadanie serii, a punkty 3 i 4 domknięcia z „Ustalone” nie mają następnego zadania?
  - Answer: seria kończy się jednym zadaniem następczym — sesja domykająca przepisuje „Handoff dla AI” notatki serii na doprecyzowanie zadania „przejrzeć skille przebudowane w serii pod regułę wiersza 1 *Settlements to record* pomiarem z zapisów sesji”, razem z parametrem daty w `skill_carry_cost.py` i porównaniami niesionego tekstu po serii, i dodaje jego linię do `_tasks_active.md` z datą dnia domknięcia; uwagi z PR-ów serii i pięć uwag z przeglądu fundamentu (pytanie 2) zostają, gdzie stoją, a handoff wymienia je jako materiał do wyboru, nie zakres.
  - Not chosen:
    - seria bez następcy, handoff zastąpiony listą tego, co zostało — najmniej pracy, ale cztery rzeczy wiszą w zamkniętej notatce, do której nie prowadzi żadna linia zadania.
    - osobne zadanie na każdą z czterech rzeczy, przez `/park` — każda ma linię, ale cztery linie naraz, z czego dwie to w praktyce listy do przejrzenia, nie zadania.
  - Source: Mariusz, 2026-11-08: „A” — na rekomendację A, ze słabym punktem nazwanym w pytaniu: jedno zadanie łączy przegląd i pomiar, więc gdy któryś skill długo nie pójdzie w `loop2`, przegląd poczeka na pomiar albo pójdzie bez niego.
- 11. Jak liczy się „każde użycie” w regule wiersza 1 — które zapisy, od kiedy i co, gdy zapisów nie ma albo jest ich mało?
  - Answer: liczą się zapisy sesji, które człowiek może otworzyć (Claude Code i Codex, jak w przeszukaniu z `instruction-files/judging.md:7–9`), z użyć od chwili, gdy krok stoi w skillu; krok zostaje w `SKILL.md`, dopóki zapisy nie pokażą, że część użyć go pomija — także wtedy, gdy zapisów nie ma; warianty idą do plików obok jak dotąd, bo wariant widać z tekstu skilla. Trzecie zdanie WAY-256, o fragmencie potrzebnym na kilku krokach, zostaje bez zmian.
  - Not chosen:
    - bez zapisów obowiązuje stara reguła, od pierwszego zapisanego użycia rozstrzyga pomiar — najmniejsza zmiana WAY-256, ale nowy skill dostaje pełny kształt, a po pierwszym użyciu może dostać przebudowę z powrotem; jedna sesja przesądza o kształcie.
    - jak wyżej, z progiem np. pięciu zapisanych użyć — jedna sesja nie przesądza, ale liczba jest arbitralna i niezmierzona, a do progu skill nosi pełny kształt.
  - Source: Mariusz, 2026-11-08: „a” — na rekomendację a, ze słabym punktem nazwanym w pytaniu: krok często pomijany, a jeszcze niezmierzony, jest niesiony, dopóki ktoś nie policzy zapisów, i reguła odwraca domyślny kształt, w którym przebudowano wcześniejsze skille serii; sprawdzi to zadanie następcze z pytania 9. Pytanie otworzył krytyk dokumentu (2026-11-08): wiersz 1 nie mówił, które zapisy się liczą, od kiedy, ani co przy zerze albo jednym użyciu.

## Context

- Zadanie jest dziesiątym z jedenastu zadań serii przebudowy skilli the way i ostatnim niescalonym; ustalenia wspólne serii stoją w the author's note of the series, sekcje „Ustalone” i „Otwarte wątki / decyzje”.
- Podstawą jest `foundations` po PR #86, commit `a3206c17932cac9bc6ac33ecfe026a2a50fbe9d5`; `project-level/lead/` zmienił się ostatnio w `db3845c` (PR #69), a PR #85 i #86 go nie dotknęły.
- Osiem użyć skilla w `loop2` (zapisy Claude Code w the session-records folder of Claude Code for the product `loop2`): `07e46a7b` (2026-10-24), `41653e57` (10-25), `2ec66018` (10-28), `df5b6e70` (10-29), `1a87a55b` (10-30), `323c603d` (11-01), `469eeb85` (11-02/03), `e4d91c6d` (11-06); `59bc959f` (10-29) tylko wymienia skill. Sesje do 11-01 czytały wcześniejszą wersję skilla, bez powrotu zadania (WAY-269), bez zlecenia `settle-technology` i bez odsyłacza do `reading_definition_and_plan.md`; obecną czytały `469eeb85` i `e4d91c6d`.
- Krok 5 pominęła tylko `323c603d`: brakujące zadanie poszło przekazaniem do osobnej sesji `refine-task`, nie przez `plan-project`. Zmianę definicji z bramką miały `41653e57` (dwa razy), `2ec66018`, `df5b6e70` i `469eeb85`.
- Ok. 19 agentów potomnych — krytycy, doprecyzowujący, odpowiadający i `plan-project` — otworzyło `SKILL.md` tego skilla, prawie zawsze tylko jedną część (krok 3, 4, 5 albo reguły stanów); zlecenie krytyka w `df5b6e70` podaje „`...\project-level\lead\skill\SKILL.md` (definition-change route and what it blocks)”. W całości przeczytał go tylko odpowiadający w `1a87a55b`.
- Do skilla odsyłają z zewnątrz `project-level/plan/template.md:102`, `project-level/plan/skill/SKILL.md:25`, `project-level/plan/skill/delegated_mode.md:3–4`, `project-level/plan/skill/hand_over.md:16`, `project-level/skill/SKILL.md:28`, `project-level/skill/delegated_mode.md:4–7`, `orchestrated_mode.md` trzech skilli wytycznych i `product-guidelines/coding/SKILL.md:88`, `product-guidelines/testing/SKILL.md:79` — po nazwie skilla, bez numeru kroku.
- `installation/install.py:33` przypisuje nazwie skilla ścieżkę `project-level/lead/skill/SKILL.md`, a `installation/test_lead_installation.py` sprawdza jego wejścia; `task-cycle/` go nie wymienia.
- W zapisach Codexa ścieżka skilla pada w 37 plikach (6 `.jsonl`, 31 `.jsonl.zst`), przy kontroli pozytywnej 18 plikach `.jsonl` ze ścieżką `project-level/task/skill`; 34 to sesje w repo the way albo w vaulcie, a obejrzany zapis z `loop2` (2026-10-29) to cykl `implement-task`, nie użycie skilla.
- Pliki czytane w kroku 0 obok skilla, bez zmian w tym zadaniu: `project-level/plan/template.md` (cały, 1855 słów), `project-level/task/template.md` (cały, 2213), `project-level/lead/conversation_template.md` (cały, 1419), `project-level/lead/answering.md` (cały, 775), sekcje „How a skill asks” (`elements/common/way_of_working.md:20–38`, 204) i „Reading the foundation” (`:52–91`, 496), `project-level/plan/skill/reading_definition_and_plan.md` (cały, 291); razem 7253; liczone jak `wc -w` w locale C na `a3206c1`.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-256** — „A fragment of a skill — one the skill of `instruction-files` proposes for any skill, the skills of the-way's process included, or one a change to a skill of the-way adds or rewords — that only one step or one variant of the skill needs stands in a file beside the skill that the step names, or, where it is a rule or a way of working WAY-35 places in an element's template or in the part the elements share, there. The skill's `SKILL.md` keeps the picture of the whole, the rules of working that hold across its steps and the pointers, and a fragment of one step or variant that is one instruction, which would otherwise stand in a file beside the skill, stays in `SKILL.md` where its pointer would stand, since the pointer is an instruction too; beyond that, a fragment's place follows from whether a use of the skill needs it at that step, never from the count of words or lines of the file. A fragment that some steps of the skill need, not all, stands by what it is: a rule of working that the agent has to keep during those steps stays in the skill's `SKILL.md`, and text the agent reads or consults, such as a procedure, a list or a template, stands in a file beside the skill that each of those steps names, a step after the first having that file read unless an earlier step did; fragments that stand unchanged are not bound by it.” — zmienia się w miejscu według wiersza 1 *Settlements to record*.
- **WAY-257** — „For every rule and fragment it judges, the skill of `instruction-files` asks when an agent needs it and whether an agent recognises that moment when it comes, and every row of its judgement, whatever its verdict, shows both answers beside the verdict.” — nie zmienia się.
- **WAY-265** — „In a skill rebuilt or changed according to WAY-256, the file of a variant that a step's file points to is named in the skill's `SKILL.md` at that step as well, with the condition under which it is read. A step's file that stands unchanged, with the variant file it points to, is not bound by it.” — nie zmienia się.
- **WAY-311** — „The table of a judgement of the skill of `instruction-files` gives a fragment that goes to several places a row for each part, each row with one of the four verdicts — keep, move, remove or reword — and gives each proposal to add a rule or to change one a row of its own.” — nie zmienia się; wiąże tabelę oceny.
- **WAY-30** (fragment) — „An exception written in advance into a decision's binding sentences is not a contradiction, and no exception lives only in a task document, plan or cycle record.” — nie zmienia się; dlatego reguła z pytania 3 wchodzi do WAY-256, a nie tylko do tego dokumentu.
- **WAY-05** (fragment) — „A decision entry opens with one to three binding sentences — in the present tense, describing a state that is to be true, concrete enough to check” — nie zmienia się; ogranicza edycję WAY-256.
- **WAY-152** (fragment) — „The project orchestrator leads a handed-over project plan from tasks to refine to human-accepted tasks ready for their cycles and keeps the plan's states consistent with evidence” — nie zmienia się; niesie obraz całości w `SKILL.md`.
- **WAY-154** (fragment) — „the project orchestrator hands agents only its path and routing, never relays its contents” — nie zmienia się; niesie kroki 2–4, które zostają w `SKILL.md`.
- **WAY-156** (fragment) — „An in-scope task split, new task, order or dependency change is delegated to a plan-project agent and logged with its reason, while a scope change goes to the human […] a subagent always performs the definition's readiness gate” — nie zmienia się; niesie krok 5 i plik zmiany definicji.
- **WAY-269** (fragment) — „For a task of a project plan, on the human's word, the project orchestrator removes by name that one cycle's worktree or working directory, its local branch, its branch on the host and that branch's remote-tracking ref, and then moves the plan's row back to `to refine`, with a line in the plan's log of changes naming the request.” — nie zmienia się; niesie plik wariantu powrotu zadania.
- **WAY-127** (fragment) — „An entry point reads its skill, and each file the skill names when the step that names that file comes rather than all of them at the start, from the checkout or worktree the session works in” — nie zmienia się; droga sesji na samym the way.
- **WAY-259** — „An entry point written into a product tells an agent to read the skill at `.the-way/<path>` in full. It tells the agent to read a file the skill names inside `.the-way` when the step or variant that names the file comes, not all named files at the start.” — nie zmienia się; droga sesji w produkcie.

## Settlements to record

Candidates: 10 shown, 1 accepted — 2026-11-08

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Krok skilla zostaje w `SKILL.md`, dopóki zapisy sesji, które człowiek może otworzyć, nie pokażą, że część użyć od chwili, gdy krok stoi w skillu, go pomija; do plików obok idą warianty i takie kroki. Trzecie zdanie WAY-256, o fragmencie potrzebnym na kilku krokach, zostaje bez zmian. | decision | Pytania 3 i 11. Pytanie 3, odpowiedź na pytanie przeciw wyborowi: Mariusz, 2026-11-08, „B obowiązuje, B1”; sposoby niewybrane stoją pod pytaniem 3. Powód do *Rationale*: Mariusz, 2026-11-08, „a czemu rekomendujesz A skoro naszym celem jest żeby było taniej?” — przy skillu, którego każde użycie przechodzi każdy krok, plik na każdy krok daje więcej czytanych słów, niż oszczędza (pełny kształt `lead-project`: +5 do +15% w typowej sesji) | czy przebudować kroki 0–4 do plików obok według WAY-256 w dzisiejszym brzmieniu (+5 do +15% słów w typowej sesji), czy zostawić je w `SKILL.md` jako wyjątek żyjący tylko w dokumencie zadania, czego WAY-30 zabrania — i czy edycja WAY-256 jest edycją w miejscu |

## Out of scope

- Domknięcie zadania po scaleniu, według notatki serii (sekcja „Ustalone”, punkt „Domknięcie każdego zadania serii przestawia serię na następne zadanie”) i pytania 9: odhaczyć linię „seria skilli 10/11” w `_tasks_active.md`, zaktualizować w notatce serii „Otwarte wątki / decyzje”, przepisać jej „Handoff dla AI” na doprecyzowanie zadania następczego „przejrzeć skille przebudowane w serii pod regułę wiersza 1 pomiarem z zapisów sesji” i dodać jego linię do `_tasks_active.md` z datą dnia domknięcia.
- Przebudowa skilli przebudowanych wcześniej w serii pod regułę wiersza 1 — zadanie następcze z pytania 9.
- Przesunięcie przypięcia the way w `loop2` i uruchomienie tam instalatora z nowej wersji — krok `loop2` przed zmierzonym użyciem (notatka serii, „Ustalone”).
- Uwagi z PR-ów serii i pięć uwag z przeglądu fundamentu (pytanie 2).
