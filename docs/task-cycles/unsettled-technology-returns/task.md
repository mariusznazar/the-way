---
title: Wybór technologii, której projekt nie ustalił, wraca do Mariusza zamiast zapaść po cichu w zadaniu
status: draft
created: 2026-10-25T16:00
updated: 2026-10-31
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# Wybór technologii, której projekt nie ustalił, wraca do Mariusza zamiast zapaść po cichu w zadaniu

Status: ready for cycle
Project relation: independent

## Description

### Need

- Gdy w trakcie zadania wychodzi potrzeba języka, frameworka, biblioteki, magazynu danych, sposobu logowania użytkownika albo miejsca uruchomienia, których projekt nie wybrał, proces nie każe wrócić z tym wyborem do człowieka.
- Mariusz zgłasza, że widzi taki wybór dopiero w PR, gdy kod już na nim stoi, a zmiana wymaga przerobienia napisanego kodu; w źródłach nie ma zapisanego przypadku.
- Krok ustalania technologii (`settle-technology`) nie ma drogi poza definicją projektu, więc produkt z zatwierdzoną definicją może otworzyć nowy wybór tylko przez ponowne przejście tej definicji; pierwszym takim przypadkiem jest wybór observability w `loop2` (krok 4 lekcji 10xDEVS m3l5).
- Odbiorcą jest Mariusz, który rozstrzyga wybór przed napisaniem kodu, i agent cyklu, który dziś musi taki wybór podjąć sam.

### To do

1. Krok technologii daje się uruchomić poza definicją projektu, przy każdej sytuacji, w której decydujemy o stacku, z dopiskiem, po co go uruchamiamy; działa wtedy zawsze przy dokumencie zadania, a uruchomienie bez zadania zaczyna się od założenia tego dokumentu przez `refine-task` (pytanie 1).
2. Tak uruchomiony krok czyta dokument zadania tam, gdzie przy definicji czyta definicję, trzyma listę wyborów i postęp w tym dokumencie, tak że da się go wznowić, nie przechodzi bramki gotowości i kończy się powrotem do doprecyzowania zadania (pytanie 1).
3. Tak uruchomiony krok rozstrzyga sprawy z dopisku i z zadania, a resztę pracy wykonuje jak przy definicji: badanie, opcje ze źródłami, krytyka, testy ryzyk, tabela z konsekwencjami i wybór człowieka (pytanie 4); wybór, który trzyma już decyzja, otwiera tylko wskazanie człowieka, a wynik jest wtedy zmianą tej decyzji (pytanie 7).
4. Każdy rozstrzygnięty wybór trafia do dokumentu zadania razem z odrzuconymi opcjami, źródłem każdej różnicy między opcjami, brakami wybranej opcji i przyjętymi ryzykami, czyli tym, czego cykl potrzebuje, żeby wpisać decyzję; szablon dokumentu zadania dostaje na to miejsce, bo dziś go nie ma (pytanie 1).
5. Doprecyzowanie zadania, które widzi potrzebę wyboru podlegającego regule z WAY-121, a żadna decyzja ani definicja go nie rozstrzyga, uruchamia krok technologii przy tym zadaniu; zadanie nie jest gotowe, dopóki Mariusz go nie rozstrzygnie (pytanie 2).
6. Zadanie z planu projektu robi to samo przy swoim dokumencie, a zatwierdzona definicja zostaje nietknięta (pytanie 1); w doprecyzowaniu prowadzonym przez orkiestratora projektu refiner zgłasza krok przez plik rozmowy, agentów uruchamia orkiestrator, a tabela wyborów idzie paczką rundy.
7. Cykl zadania nie podejmuje takiego wyboru sam, także gdy żadne źródło nie odpowiada: agent oddaje raport bez kodu, próba jest odrzucana, a cykl otwiera zablokowany szkic requestu z nazwanym wyborem (pytanie 3).
8. Po zamknięciu takiego szkicu przez Mariusza dokument zadania wraca do `Status: refining`, jego wcześniej przyjęte odpowiedzi i wiersze zostają, krok technologii działa przy nim, Mariusz akceptuje cały zmieniony dokument i rusza nowy cykl (pytanie 3).
9. Reguła zatrzymania niesie przykłady wyborów granicznych (pytanie 2).
10. Wszystkie inne wybory zostają w cyklu zadania jak dziś: agent wybiera sam, a wybór trafia do tabeli wyborów cyklu, do której prowadzi link z requestu; nowe narzędzia wybierane w skillach wytycznych zostają na drodze tych skilli (pytania 2 i 5).

### Questions to settle

- Pytanie 1: gdzie krok technologii zapisuje wybór, gdy nie działa przy definicji projektu — także dla zadań niezależnych, które definicji nie mają?
  - Answer: w dokumencie zadania — krok zawsze działa przy jakimś zadaniu, a uruchomienie bez zadania zaczyna się od jego założenia; wybór i odrzucone opcje trafiają do *Questions to settle* i do wiersza *Settlements to record*, a cykl wpisuje decyzję do dziennika razem z kodem, który z niej korzysta; definicja przed bramką gotowości działa jak dziś. Odpowiedź obejmuje też zadania niezależne: zatrzymanie dotyczy ich tak samo.
  - Not chosen:
    - od razu w dzienniku decyzji, osobnym requestem, bez zadania — sprzeczne z WAY-01 („a planned feature is written into the foundation before it is built” to naruszenie): dziennik opisywałby coś, czego produkt jeszcze nie ma, a po porzuceniu pracy wpis zostałby fałszywy; trzeba by zmienić WAY-01
    - w zatwierdzonej definicji projektu — jeden wybór oznacza ponowną bramkę gotowości i ponowne sprawdzenie planu (WAY-118, WAY-156), a zadania niezależne definicji nie mają, więc i tak potrzebowałyby drugiej drogi
  - Source: Mariusz, 2026-10-30: „A” — na drogę A przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: nawet mały wybór wymaga dokumentu zadania, wybór bez kodu pełnego cyklu, a dokument musi utrzymać porównanie i źródła, bo raport kroku leży poza gitem.
- Pytanie 2: które wybory stacku zatrzymują zadanie — tylko te, które reguła przynależności z WAY-121 kieruje do projektu, czy każdy nowy element stacku, także mała biblioteka?
  - Answer: ta sama reguła co w projekcie — zatrzymuje wybór, którego późniejsze ustalenie mogłoby zmienić podział pracy na zadania albo który dokłada coś do uruchamiania, opłacania lub kopii zapasowej; wybór, który jedno zadanie może podjąć i zmienić samo, zostaje przy zadaniu; baza danych i tracker błędów zatrzymują, mała biblioteka do formatowania dat nie; WAY-121 zostaje w tej części bez zmian, a nowa reguła niesie przykłady wyborów granicznych.
  - Not chosen:
    - każdy nowy element stacku, także najmniejsza zależność — każda drobna biblioteka to zatrzymany cykl, badanie, krytyka, testy ryzyk i tabela dla Mariusza, a WAY-121 trzeba by zawęzić, bo wprost zostawia takie wybory zadaniu
    - jak wyżej, a nowe zależności dodatkowo wymienione osobną linią w requeście — jedna linia więcej w opisie requestu, pomyłka agenta widoczna dopiero w PR, gdy kod już stoi; dodatkowa reguła na problem, którego nikt nie zapisał
  - Source: Mariusz, 2026-10-31: „A” — na drogę A przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: mała biblioteka dalej idzie z pamięci modelu, a o przypadkach granicznych decyduje osąd agenta; `foundations/decisions.md:2629`, `project-level/technology/list.md:16`, `foundations` `00c0a74`.
- Pytanie 3: co dzieje się z zadaniem, gdy taki wybór wychodzi dopiero w cyklu, którego jedynym kontaktem z człowiekiem jest request?
  - Answer: stop i powrót do doprecyzowania — agent oddaje raport bez kodu, próba jest odrzucana, a cykl otwiera zablokowany szkic requestu z nazwanym wyborem; Mariusz go zamyka, zadanie wraca do doprecyzowania, krok technologii działa przy nim, Mariusz akceptuje nowy dokument i rusza nowy cykl; nowa jest tylko reguła zastrzegająca taki wybór dla człowieka.
  - Not chosen:
    - ciąg dalszy w tym samym requeście, z wynikiem kroku jako uwagą do requestu — wybór ląduje w komentarzu, a nie w dokumencie zadania, wbrew odpowiedzi na pytanie 1, zamrożona kopia zadania rozjeżdża się z tym, co cykl robi, i potrzebny jest nowy mechanizm
    - pauza w trakcie cyklu, z pytaniem do człowieka — sprzeczne z WAY-227 („the cycle stops between stages to ask the human for an approval a stage asks for” to naruszenie); trzeba by zmienić tę decyzję i cykl przestałby działać bez nadzoru
  - Source: Mariusz, 2026-10-31: „A” — na drogę A przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: przy późnym wykryciu w zadaniu z planem przepadają zrobione kawałki, a bramka w doprecyzowaniu nie wyłapie wyboru tam przeoczonego; `task-cycle/skill/SKILL.md:16-23`, `foundations` `00c0a74`.
- Pytanie 4: czy krok uruchomiony z dopiskiem rozstrzyga tylko to, o czym mówi dopisek, czy także zagląda do logów, interfejsu i danych deweloperskich?
  - Answer: tylko to, o czym mówi dopisek — lista wyborów to sprawy z dopisku i z zadania, a człowiek ją potwierdza, dopisuje do niej albo skreśla; trzech spraw drogi agenta do działającego produktu krok sam nie sprawdza, chyba że dopisek ich dotyczy, jak przy observability w `loop2`; reszta kroku zostaje bez zmian (badanie każdego wyboru przez świeżego agenta, opcje ze źródłami, krytyka, testy ryzyk, tabela z konsekwencjami); reguła z pytania 2 mówi tylko, co samo zatrzymuje zadanie, a człowiek może uruchomić krok dla każdego wyboru.
  - Not chosen:
    - dopisek plus trzy sprawy, gdy zadanie wnosi coś widocznego dla użytkownika — zadanie o czymś innym może dostać do trzech dodatkowych wyborów, każdy z badaniem i krytyką; zbliża się do odrzuconego w WAY-121 pytania o te sprawy w doprecyzowaniu każdego zadania
  - Source: Mariusz, 2026-10-31: „A” — na drogę A przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: zadanie niezależne, które wnosi pierwszy ekran, nie dostaje z automatu ustalenia, jak agent do niego dotrze, i agent improwizuje jak dziś; `project-level/technology/running_product.md:7`, `foundations` `00c0a74`.
- Pytanie 5: czy nowe narzędzia wybierane w skillach wytycznych (linter, narzędzie testów, biblioteka komponentów) zostają na własnej drodze, czy też wracają do kroku technologii?
  - Answer: zostają na swojej drodze — nowa reguła mówi wprost, że te narzędzia rozstrzyga skill wytycznych, a jego drogi nie zmienia.
  - Not chosen:
    - też idą do kroku technologii — jedna droga dla wszystkich wyborów, ale trzeba zmienić trzy skille i co najmniej sześć decyzji (WAY-185, WAY-186, WAY-210, WAY-211, WAY-248, WAY-249), a zadanie wybierające kilka narzędzi naraz dostaje dłuższą ścieżkę, bez zapisanego przypadku, że obecna droga zawiodła
  - Source: Mariusz, 2026-10-31: „A” — na drogę A przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: droga wytycznych nie ma testów ryzyk z WAY-138; `product-guidelines/coding/SKILL.md:132-133`, `foundations` `00c0a74`.
- Pytanie 6: czy uruchomienie kroku z dopiskiem i regułę zatrzymania robimy jednym zadaniem, czy dwoma?
  - Answer: jednym zadaniem — obie części wchodzą jednym cyklem i jedną paczką zmian w decyzjach.
  - Not chosen:
    - dwa zadania, najpierw krok z dopiskiem, zaraz po nim reguła zatrzymania — mniejszy i szybszy pierwszy cykl, ale drugi cykl kosztuje osobno, WAY-121 i WAY-135 rusza się dwa razy, a do jego końca agent wybiera sam, jak dziś
    - tylko krok z dopiskiem, reguła zatrzymania odłożona do pierwszego prawdziwego przypadku — najtaniej i bez martwego tekstu, ale wbrew „brak stacku w planie to temat do zatrzymania się” i werdyktowi „przejmuję” z kursu, a pierwszy przypadek Mariusz zobaczy dopiero w PR
  - Source: Mariusz, 2026-10-31: „A” — na drogę A przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: reguła może nigdy nie zadziałać i zostać tekstem bez pożytku, a zadanie o observability czeka na większą zmianę, niż potrzebuje.
- Pytanie 7: czy uruchomienie kroku z dopiskiem może otworzyć wybór, który rozstrzyga już decyzja fundamentu?
  - Answer: może, gdy wskaże to człowiek — dopisek albo zmiana listy przez człowieka otwiera wybór, który trzyma decyzja; krok przechodzi go jak każdy inny, a wynik jest w dokumencie zadania zmianą tej decyzji (WAY-30); sam agent decyzji nie otwiera, a automatyczne zatrzymanie dotyczy tylko wyborów nierozstrzygniętych.
  - Not chosen:
    - nie może, krok rozstrzyga tylko to, czego nic nie trzyma — reguła jest prostsza, ale zmiana technologii szłaby zwykłym doprecyzowaniem, bez badania i krytyki, a w `loop2` wybór, dokąd idą logi, nie przeszedłby przez krok
  - Source: Mariusz, 2026-10-31: „A” — na drogę A przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: `held by` przestaje być ostateczne, więc rozpędzone uruchomienie mogłoby naruszać kolejne decyzje; `project-level/technology/list.md:18-22`, `foundations` `00c0a74`.

## Context

- Źródło: kurs 10xDEVS, lekcja m2l4, wiersz 3 — „decyzja techniczna oparta na sprawdzalnym źródle, nie na pamięci modelu”, werdykt „przejmuję” (`C:\Storage\The Brain\The Brain\Notes\Projects\(P) Przejście 10xDEVS\mapa_pakietu_10x.md`, sekcja „m2l4”).
- Mariusz: „`settle-technology` dotyczy stacku — brak stacku w planie to temat do zatrzymania się”.
- Mariusz, 2026-10-29: „Krok technologii powinien się odpalać przy każdej sytuacji kiedy decydujemy o stacku, więc powinien być też do uruchomienia ad hoc z dopiskiem, że będziemy pracować nad uzupełnieniem observability”.
- Ta sama potrzeba wyszła przy zadaniu o drodze agenta do działającego produktu, pytanie 7, gdzie ścieżkę z zadania do kroku technologii odłożono właśnie do tego zadania (`C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\krok_technologii_droga_agenta_do_produktu.md:51`).
- Z tej ścieżki korzysta zadanie o observability w kroku technologii (`C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\zadanie_observability_w_kroku_technologii.md`), które dopisuje do kroku pytania o trwałość logów i dowiadywanie się o awarii.
- „Sposób logowania” z listy wyborów to logowanie użytkownika, nie logi aplikacji.
- Dziś, gdy żadne źródło nie odpowiada, wybór podejmuje agent prowadzący cykl: „Where no source answers, the orchestrator picks the smallest reversible reading that fulfils the task; never ask the human and never widen the task.” (`task-cycle/spec/design.md:15-16`, tak samo `task-cycle/skill/SKILL.md:184-186` i `:211-213`, `foundations` `00c0a74`).
- Dziś krok technologii zapisuje wyłącznie do definicji: „The step writes into the definition only, never into the product's foundation” (`project-level/technology/SKILL.md:25`, `foundations` `00c0a74`), a jego początek i koniec zależą od definicji (`project-level/technology/start.md:5-8`, `project-level/technology/close.md:6-11`).
- Pierwotny opis zadania mówił, że taki wybór projektuje skill `brainstorming`; cykl już go nie używa (WAY-125), a jego miejsce zajął `write-spec`.
- Pierwotny opis zadania mówił też, że to pierwszy przebieg drogi jednego autora; ta droga była już używana, a o trasie tego zadania rozstrzyga jego cykl (WAY-136).
- Pierwotne brzmienie zadania: „the way: wybór stacku, którego definicja projektu nie rozstrzygnęła (język, framework, biblioteka, magazyn danych, sposób logowania, miejsce uruchomienia — WAY-121), zatrzymuje zadanie i wraca do `settle-technology`, gdzie rozstrzyga go człowiek; reszta zostaje w cyklu jak dziś”.
- Wybór, który zmienia podział pracy w planie projektu, wraca do planu istniejącą regułą: „A mismatch returns to the plan, not an unrecorded change in the task document.” (`project-level/task/skill/project_plan_task.md:22-23`, `foundations` `00c0a74`).
- Mechanizm zatrzymania już istnieje: „Where a binding rule reserves a decision to a human and the code cannot proceed without it, open a blocked draft request with the evidence and stop.” (`task-cycle/skill/SKILL.md:21-23`, `foundations` `00c0a74`).
- Prośbę o pracę agentów refiner przekazuje przez plik rozmowy, a dyspozycje wykonuje orkiestrator projektu (`project-level/task/skill/orchestrated_mode.md:17-20`, `foundations` `00c0a74`).
- Pomiar z krytyki dokumentu: 25 zapisów cykli `loop2` na `main` z okresu 2026-10-05 do 2026-10-30; agent wybrał sam w 3 przypadkach (dublet testowy `smtp-server`, nadpisanie `qs`, źródło ikon game-icons), żaden nie spełnia wyraźnie reguły z pytania 2, ostatni jest dyskusyjny; pomiar przeszukiwał pliki i tabele wyborów, nie czytał każdego zapisu w całości, a `loop2` ma pełną definicję, więc zadania niezależne są w nim niedoreprezentowane.
- The-way nie ma własnego katalogu `guidelines/`; zadanie zmienia tekst skilli i wpisy fundamentu, a pracę nad samym the-way prowadzi `agent-instructions/README.md`.
- Po scaleniu sesja, która dostanie link do requestu, przestawia nośnik wiersza 3 w sekcji „m2l4” pliku `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Przejście 10xDEVS\mapa_pakietu_10x.md` na numer decyzji zapisanej z wiersza 2 *Settlements to record*.

## Questions carried to cycle

- Jak wygląda zablokowany szkic requestu, gdy odrzucona próba nie zostawia kodu, a gałąź trzyma tylko parę commitów zapisu cyklu.
- Jak nowy cykl tego samego zadania nazywa swój zapis, skoro poprzedni leży już pod tą nazwą w historii, i kto cofa wiersz planu projektu ze stanu `in cycle`.

## Human actions

none

## Decisions in play

Wybór: decyzje z *Scope* `project-level` albo `task-cycle` według „Reading the foundation”, wyszukanie słów „technolog”, „stack”, „library”, „framework” w dzienniku decyzji i wpisy, do których te decyzje prowadzą, na `foundations` `00c0a74`.

- WAY-01 — „On the main branch, the foundation describes the product as it is”; naruszeniem jest „a planned feature is written into the foundation before it is built”. Dlatego wybór nie trafia do dziennika przed kodem (pytanie 1).
- WAY-30 — „A change to a decision that a task needs is written into the task's plan, or into its task document where no plan is written”; „no exception lives only in a task document, plan or cycle record”. Dlatego zmiany istniejących decyzji niesie wiersz 3 tabeli niżej.
- WAY-106 — „The project level reads a product's foundation and records prospective changes in the project definition; it writes no foundation entries.” Krok dalej nie pisze wpisów fundamentu; poza definicją pisze do dokumentu zadania.
- WAY-118 — „A change to those sections after approval goes through the gate again before breakdown relies on it.” Zatwierdzona definicja zostaje nietknięta, więc bramka nie wraca (pytanie 1).
- WAY-156 — „A fresh subagent then checks the plan again through plan-project step 0, and no task gains ready for cycle while that definition gate remains open.” Nie działa, bo definicja się nie zmienia (pytanie 1).
- WAY-121 — „A choice belongs on the list when settling it later could change how the work is cut into tasks, or when it adds something the product has to run, pay for or back up; a choice one task can make and change alone stays with that task.” Reguła zostaje i wyznacza, co zatrzymuje zadanie (pytanie 2); pierwsze zdanie tej decyzji mówi dziś tylko o kroku „before a project definition goes through its readiness gate”, jej *Verification* nazywa naruszeniem „the first task of the breakdown chooses the database”, a *Rejected* odrzuca „the step after the readiness gate” i „the first tasks of the breakdown”. Zadanie tego nie znosi: wybór należący do projektu dalej ustala się przed bramką, a nowa droga służy temu, co definicja pominęła albo czego nie ma w żadnej definicji, i przez nią wybór podejmuje człowiek, nie zadanie. Definicji nie zmienia, więc odrzucony tam koszt ponownej bramki nie powstaje.
- WAY-122 — „The options of each technology choice a project needs come from research of that choice against the project definition”. Staje się nieprawdziwa w tym brzmieniu; poza definicją badanie idzie względem zadania i dopisku (pytanie 4, wiersz 3).
- WAY-123 — „The step that settles a project's technology shows the options of each choice by their consequences for the product”. Obowiązuje też poza definicją (pytanie 4, wiersz 3).
- WAY-137 — „Where the options of a place to run differ in no consequence for the product and more than one of them is the simplest and cheapest, the step that settles a project's technology recommends, of those, the one an agent works with best”. Obowiązuje też poza definicją (pytanie 4, wiersz 3).
- WAY-138 — „The step that settles a project's technology tests the option it recommends for each choice it settles”; „each risk taken reaches the decision of that choice in its *Rationale*”; „it tests no choice a decision of the foundation holds”. Obowiązuje też poza definicją, a ryzyka idą przez dokument zadania; wybór otwarty przez człowieka nie jest już trzymany przez decyzję, więc przechodzi testy (pytania 1, 4 i 7, wiersz 3).
- WAY-165 — „the logs ask where the record of what the running product does goes and how an agent reads it”. Obowiązuje, gdy dopisek dotyczy tych spraw (pytanie 4).
- WAY-166 — „In a choice of an agent's way to the running product, whether an agent can use an option is a consequence for the product”. Obowiązuje, gdy dopisek dotyczy tych spraw (pytanie 4).
- WAY-219 — „Where the foundation settles no such way, they inspect the states in code and mark the screenshot unchecked”; *Rejected*: „stopping the cycle for an unsettled way to the interface”. Zostaje: brak drogi agenta do działającego produktu sam nie zatrzymuje cyklu, a zatrzymuje go tylko wybór podlegający regule z WAY-121 (pytania 2 i 4).
- WAY-124 — „It is ready when the human has seen and accepted its complete document, its required outcome is stated, every known question blocking that outcome is answered”. Nierozstrzygnięty wybór jest pytaniem blokującym.
- WAY-134 — „the task document keeps the rows the human accepts and, where the human chose among ways shown, each way not chosen”; „The task's cycle writes each kept row whole into the foundation”. To droga wyboru do dziennika (pytanie 1).
- WAY-135 — „An agent that meets an open design choice while it makes the change returns a report that holds no code, the attempt is discarded with the foundation entries the cycle wrote for it, and a fresh agent given the report writes the spec”. Przy wyborze zastrzeżonym dla człowieka raport jest ten sam, ale spec nie powstaje, tylko cykl się zatrzymuje (pytanie 3, wiersz 3).
- WAY-154 — „Only a refiner changes the task document's body”; WAY-155 — „makes an unanswered choice a question to the human with options, costs and a recommendation”. Przez te drogi przechodzi wybór w doprecyzowaniu prowadzonym przez orkiestratora projektu.
- WAY-227 — „Decisions reserved to a human by the foundation remain reserved; when required code cannot proceed without one, the cycle opens a blocked draft request.” Nowa reguła jest tym zastrzeżeniem (pytanie 3).
- WAY-185 — „A new library of components or a new way of styling is a choice the skill leaves to the human as a question of the task, never one it settles”; WAY-186 — „every difference no source supports refuted by a critique before the human sees the rules”; WAY-210 — „A new linter, formatter or audit of dependencies is a choice the skill leaves to the human as a question of the task, never one it settles”; WAY-211 — „every claim no source supports refuted by a critique before the human sees the options”; WAY-248 — „A new test tool or a library of property tests is a technology choice the skill leaves to the human as a question of the task, never one it settles”; WAY-249 — „every claim no source supports refuted by a critique before the human sees the set”. Droga nowych narzędzi w skillach wytycznych, bez zmian (pytanie 5).
- WAY-100 — „A method or practice borrowed from outside a product binds its way of working only through a decision that names what is adopted, where it applies, and why.” Wiersz 2 nazywa, co przejmuje z lekcji m2l4.
- `project-technology-record` — „Before approval, the project readiness check rejects a definition whose Technology section is missing or reads `none`”. Dotyczy tylko definicji; bez zmiany znaczenia.

## Settlements to record

Candidates: 5 shown, 3 accepted — 2026-10-31

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Krok technologii działa też poza definicją projektu, przy dokumencie zadania: uruchamia się go z dopiskiem, po co, uruchomienie bez zadania zaczyna się od założenia dokumentu, krok rozstrzyga sprawy z dopisku i z zadania, trzech spraw drogi agenta do działającego produktu sam nie sprawdza, resztę pracy wykonuje jak przy definicji, człowiek może go uruchomić dla każdego wyboru, także takiego, który trzyma już decyzja, a wtedy wynik jest zmianą tej decyzji, a wybór trafia do tego dokumentu i cykl wpisuje decyzję razem z kodem, który z niej korzysta. | decision | odpowiedzi na pytania 1, 4 i 7 | czy wybór zapisać od razu w dzienniku decyzji albo przerobić zatwierdzoną definicję, czy dokładać przy okazji wybory logów, interfejsu i danych deweloperskich, i czy wolno ruszyć wybór, który trzyma decyzja |
| 2 | Wybór, którego późniejsze ustalenie mogłoby zmienić podział pracy na zadania albo który dokłada coś do uruchamiania, opłacania lub kopii zapasowej, a którego żadna decyzja ani definicja nie rozstrzyga, jest zastrzeżony dla człowieka: w doprecyzowaniu wraca do kroku technologii, a w cyklu agent oddaje raport bez kodu, próba jest odrzucana, cykl otwiera zablokowany szkic requestu z nazwanym wyborem i zadanie wraca do doprecyzowania; każdy inny wybór zostaje w cyklu, a nowe narzędzia skilli wytycznych zostają na drodze tych skilli; to przejęcie z lekcji 10xDEVS m2l4: decyzja techniczna oparta na sprawdzalnym źródle, nie na pamięci modelu. | decision | odpowiedzi na pytania 2, 3 i 5; Context, wiersz o źródle | czy agent prowadzący cykl wybiera najmniejszą odwracalną drogę, czy zatrzymać się na małej bibliotece, i czy linter wybierany przy wytycznych przekazać do kroku technologii |
| 3 | Decyzje o kroku technologii WAY-121, WAY-122, WAY-123, WAY-137 i WAY-138 obowiązują też poza definicją projektu, a WAY-135 dostaje wyjątek: przy wyborze zastrzeżonym dla człowieka po raporcie bez kodu nie powstaje spec, tylko cykl się zatrzymuje. | decision | odpowiedzi na pytania 1, 3 i 4 | czy zostawić te decyzje w brzmieniu mówiącym tylko o projekcie i czy po raporcie bez kodu pisać spec |

## Out of scope

- Pytania o to, jak długo żyją logi i skąd człowiek dowiaduje się o awarii — zadanie `C:\Storage\The Brain\The Brain\Notes\Projects\(P) Proces pracy nad produktem\_zadania\zadanie_observability_w_kroku_technologii.md`.
- Przestawienie przypięcia the way w `loop2` i sam wybór observability w `loop2` — krok 4 lekcji 10xDEVS m3l5.
