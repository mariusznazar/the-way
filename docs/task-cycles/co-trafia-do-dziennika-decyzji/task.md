---
title: "the way: co trafia do dziennika decyzji — pytanie „dokąd to idzie”, próg wejścia, reguły wytycznych bez wpisu, test wskazujący zdanie decyzji"
status: draft
created: 2026-11-12T23:00
updated: 2026-11-13
tags: [zadanie]
related: "the project note in the author's notes"
---

## Po co to

- **Jak jest dziś:** Rozstrzygnięcie trafia do dziennika decyzji produktu, jeśli wiąże po scaleniu zmiany — i to jest jedyny próg. Przechodzi go każdy opis zachowania produktu, więc dziennik gry ma 388 wpisów i 970 KB i przybywa mu kilkanaście wpisów dziennie. Są wśród nich reguły pisania kodu powtórzone w wytycznych, pojedyncze napisy, które stoją też w kodzie i w teście, instrukcje pracy agenta i części jednego pytania pod osobnymi numerami. Testy powołują się na numery decyzji, ale sam numer w komentarzu testu nie mówi, czy test pilnuje zdania decyzji, czy tylko o nim wspomina.
- **Kto to odczuwa:** Agenci, którzy do każdego zadania wybierają i czytają decyzje — agent sprawdzający całą zmianę zna dziś większość z nich tylko z tytułu. Ja, gdy przyjmuję tabelę rozstrzygnięć zadania i nie widzę, gdzie każde rozstrzygnięcie wyląduje.
- **Co jeśli nic:** Dziennik rośnie dalej w tym tempie, a każde sprzątanie odrasta. Nie wiadomo, których zdań decyzji nie pilnuje żaden test — szacunek z próby: około 90 wpisów gry w całości i około 55 w części.

# the way: co trafia do dziennika decyzji — pytanie „dokąd to idzie”, próg wejścia, reguły wytycznych bez wpisu, test wskazujący zdanie decyzji

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Dziś jedynym progiem wejścia do dziennika decyzji produktu jest pytanie, czy rozstrzygnięcie wiąże po scaleniu zmiany (szablon decyzji, „Plan test”, WAY-36); przechodzi go każdy opis zachowania produktu.
- Pięć reguł procesu razem każe pisać wpis z niemal każdego rozstrzygnięcia: kandydatem do tabeli rozstrzygnięć jest każda odpowiedź, jedynym progiem jest „wiąże po scaleniu”, nowa reguła obok istniejącej decyzji dostaje nowy numer (WAY-19), każda reguła wytycznych musi wskazać decyzję (WAY-168), a rozumowanie stoi we wpisie.
- Skutek w produkcie, który używa the way: dziennik gry ma 388 wpisów i 970 KB i rośnie o kilkanaście wpisów dziennie; w próbie 20 ostatnich wpisów 5 należało gdzie indziej (linie skilli, reguła wytycznych), a 7 było częściami dwóch pytań.
- Testy produktu powołują się na numery decyzji, ale wzmianka numeru w komentarzu wygląda tak samo przy teście, który zdanie decyzji sprawdza, i przy takim, który je tylko wspomina; nie da się wyliczyć zdań decyzji, których nie pilnuje nic.
- Gdy zmiana poprawia zdanie niezmiennika sprawdzanego testem, a test zostaje, nic tego nie zgłasza; w produkcie gry znalazł się taki przypadek dla 2 ze 111 niezmienników.
- Odbiorcą są agenci, którzy do każdego zadania wybierają i czytają decyzje, oraz Mariusz, który przyjmuje tabelę rozstrzygnięć zadania i ma widzieć, gdzie każde rozstrzygnięcie wyląduje.

### To do

1. Szablon decyzji (`elements/decisions/template.md`, sekcja „Decision or invariant”, po akapicie „**Plan test:**”) ma pytanie „dokąd to idzie”: rozstrzygnięcie, które przeszło test planu, przechodzi po kolei pięć pytań, a pierwsze „tak” wskazuje jego miejsce — instrukcja pracy agenta idzie do skilla albo pliku instrukcji; reguła pisania kodu, testów albo wyglądu do wytycznych tej dyscypliny; pojedynczy napis, liczba, lista albo położenie do danych albo kodu produktu, z testem, który je trzyma, i z komentarzem przy wartości, gdy powód jest nieoczywisty; sam brak funkcji nie jest zapisywany, chyba że inny wpis na nim stoi; część pytania, na które odpowiada już istniejący wpis, staje się jego zdaniem. Wpisem dziennika zostaje tylko to, co przeszło wszystkie pięć. Pod pytaniami stoi zdanie progu: wpis powstaje tylko tam, gdzie ktoś, kto decyzji nie zna, zrobiłby inaczej, a test, który go zatrzyma, nie powie mu dlaczego. W dzienniku samego the way pytanie pierwsze brzmi inaczej: reguła stojąca w jednym skillu albo szablonie the way stoi tam z jednym zdaniem powodu, a wpisem zostaje tylko wtedy, gdy niesie wybór z realnym kosztem — taki, przy którym ktoś mógłby rozsądnie zaproponować odrzucony wariant; wtedy skill albo szablon wskazuje tę decyzję (pytanie 1).
2. Tabela rozstrzygnięć przy doprecyzowaniu zadania (szablon zadania `project-level/task/template.md`, sekcja „Settlements to record” i jej opis pod „What each section carries”, oraz pliki kroku `elements/common/skill/task_variant.md`, `elements/common/skill/build_table.md`) ma kolumnę „dokąd idzie”, wypełnioną pytaniem z punktu 1; Mariusz dalej widzi i przyjmuje każde rozstrzygnięcie, także to, które nie trafi do dziennika. Cykl zapisuje każdy przyjęty wiersz w miejscu, które ta kolumna wskazuje, w tej samej zmianie co kod.
3. Krok zwrotny cyklu (`task-cycle/skill/return_step.md`, zdanie, które otwiera „It compares with the code”) i skill zapisujący decyzję (`elements/decisions/skill/decide_entry.md`, punkt, który otwiera „Apply the template's plan test”) stosują to samo pytanie: tam, gdzie kończy się ono poza dziennikiem, nie powstaje wpis, tylko reguła wytycznych, linia skilla albo wartość z testem, zapisana w tej samej zmianie, a raport kroku nazywa miejsce każdego rozstrzygnięcia.
4. Szablon wytycznych (`product-guidelines/template.md`, akapit, który otwiera „This file defines the form”, i pole *Decision* w „Required form”): reguła, która mówi tylko, jak pisać kod, testy albo wygląd, stoi w wytycznych sama, z powodem w jednym zdaniu, a jej *Decision* czyta `none`; reguła, która wykonuje wybór produktu z realnym kosztem, dalej wskazuje decyzję. Regułę bez decyzji człowiek przyjmuje jako wiersz tabeli rozstrzygnięć zadania („dokąd idzie”: reguła wytycznych), przed kodem; regułę, którą cykl znalazł sam, opis prośby o scalenie wymienia wśród tego, czego człowiek nie widział w zadaniu, i człowiek przyjmuje ją przy scaleniu. Przyjęcia przed kodem (WAY-172) wymagają odtąd tylko reguły z decyzją, a reguła z szablonu dyscypliny the way dalej wiąże produkt tylko przez decyzję, która ją przyjmuje (WAY-173, bez zmiany) (pytanie 4).
5. Szablon decyzji (sekcja „Changing a decision”, zdanie, które otwiera „A number stands for the question”, i sekcja „Binding sentences”, punkt „One to three sentences”): część pytania, na które odpowiada istniejący wpis, staje się jego zdaniem, o ile nie da się jej zmienić bez zmiany tamtego wpisu; niezależne pytania dalej dostają osobne numery. Pierwszy akapit wpisu odpowiada na pytanie główne jednym do trzech zdań, a każda dołączona część dostaje własny akapit zdań wiążących, też z jednym do trzech zdań (pytanie 3).
6. Test, który pilnuje zdania decyzji, ma obok linię `decision: <numer>` z cytatem początku zdania, którego pilnuje, tak jak testy niezmienników mają `invariant: <identyfikator>`; sama wzmianka numeru w pliku testu niczego nie pilnuje. Skrypt kontroli fundamentu sprawdza, że cytat stoi we wpisie o tym numerze, i wskazuje test, którego cytat po zmianie brzmienia zdania już we wpisie nie stoi (pytanie 6). Pole *Verification* szablonu decyzji (sekcja „Verification”) nazywa takie testy, a parę przykładów „zgodne / łamie” zostawia tylko dla tej części zdania, której nie pilnuje żaden test. Zdanie decyzji trzymane takim testem nie dostaje niezmiennika wyprowadzonego z decyzji; niezmiennik zostaje dla reguły bez wyboru za sobą i dla reguły, na której stoi kilka decyzji. Zmiana testu z linią `decision:` jest wymieniana w opisie prośby o scalenie tak jak zmiana testu niezmiennika (pytanie 2). Uzasadnienie i warianty odrzucone zostają we wpisie w całości.
7. Skrypt kontroli fundamentu (`elements/common/foundation_check.py`) wylicza decyzje, które nie mają ani niezmiennika, ani testu z linią `decision:`, ani pary przykładów: decyzję, którą zmiana dodaje albo zmienia, zgłasza jako błąd, a starą wypisuje jako pozycję listy, która bramki nie zatrzymuje (pytanie 5).
8. Gdy zmiana poprawia zdanie niezmiennika, którego metoda to `test`, a żaden plik z jego linią `invariant:` się w tej zmianie nie zmienił, skrypt wypisuje ten niezmiennik, a opis prośby o scalenie go wymienia.
9. Decyzje the way wymienione w *Decisions in play* jako zmieniane mówią po zmianie to, co punkty 1–8.

### Questions to settle

- 1. Czy pytanie „dokąd to idzie” stosuje się do dziennika samego the way, i w jakim brzmieniu pytanie pierwsze (instrukcja pracy agenta idzie do skilla) — skoro produktem the way są właśnie skille i szablony, a WAY-293 odrzuciło już wyjątek „wybór zapisany w tekście skilla albo szablonu bez wpisu”?
  - Answer: (b) — w the way reguła stojąca w jednym skillu albo szablonie stoi tam z jednym zdaniem powodu; wpisem zostaje tylko wybór z realnym kosztem (ktoś mógłby rozsądnie zaproponować odrzucony wariant), i wtedy skill wskazuje decyzję. WAY-293 zmienia się częściowo. W produktach pierwsze pytanie zostaje dosłowne.
  - Not chosen:
    - (a) the way stosuje pierwsze pytanie dosłownie, reguła pracy agenta idzie do skilla bez wpisu — powody i odrzucone warianty wyborów procesu giną z dokumentem zadania, a późniejsza zmiana może przerobić linię skilla bez sprzeczności z żadnym wpisem, więc recenzent nie ma czego jej przeciwstawić.
    - (c) dziennik the way bez pierwszego pytania, każda reguła skilla albo szablonu the way zostaje decyzją — dziennik the way rośnie dalej w obecnym tempie (w próbie 30 wpisów ok. 13 tylko powtarzało jeden szablon albo skill).
  - Source: Mariusz (przez doradcę dnia), 2026-11-13, „1 b — reguła stojąca w jednym skillu albo szablonie stoi tam z jednym zdaniem powodu, wpisem zostaje tylko wybór z realnym kosztem (ktoś mógłby rozsądnie zaproponować odrzucony wariant), wtedy skill wskazuje decyzję; WAY-293 zmienia się częściowo, w produktach pierwsze pytanie zostaje dosłowne” (odpowiedź na pytanie z drogami a, b, c i rekomendacją b).
- 2. Czy zdanie decyzji trzymane testem z linią `decision:` dalej dostaje niezmiennik wyprowadzony z decyzji (WAY-22: „what of it a commit can make false is written as an invariant derived from it”), czy linia `decision:` go zastępuje?
  - Answer: (a) — linia `decision:` zastępuje niezmiennik wyprowadzony z decyzji; niezmiennik zostaje dla reguły bez wyboru za sobą i dla reguły, na której stoi kilka decyzji; zmiana testu z linią `decision:` jest wymieniana w opisie prośby o scalenie jak zmiana testu niezmiennika. Zmienia WAY-22, WAY-12 i WAY-03.
  - Not chosen:
    - (b) WAY-22 bez zmian, każda sprawdzalna część nowej decyzji dalej dostaje niezmiennik, a linia `decision:` tylko oznacza istniejące testy, które dziś wspominają numer — zmiana sprowadza się do porządkowania starych testów, a nowe decyzje dalej rodzą pary wpisów (decyzja i niezmiennik).
  - Source: Mariusz (przez doradcę dnia), 2026-11-13, „2 a, 3 b, 4 a, 5 c, 6 b — wszystkie zgodnie z Twoimi rekomendacjami” (odpowiedź na pytanie z drogami a, b i rekomendacją a; cena drogi a podana w pytaniu: zdanie decyzji traci znacznik „produkt dziś łamie tę regułę” i kontrolę, że niezmiennik oznaczony jako sprawdzany testem ma test).
- 3. Jak poluzować limit „jedno do trzech zdań wiążących” (WAY-05), gdy część pytania staje się zdaniem istniejącego wpisu?
  - Answer: (b) — jedno do trzech zdań na każdą część: pierwszy akapit odpowiada na pytanie główne, każda dołączona część dostaje własny akapit, też z jednym do trzech zdań. Zmienia WAY-05.
  - Not chosen:
    - (a) bez liczby, każde zdanie wiążące odpowiada na pytanie wpisu albo na jego część — nic mechanicznie nie trzyma wpisu krótko, a w WAY-05 słabnie zasada „to, co wiąże, ma być krótkie”.
    - (c) wyższa stała granica, np. do sześciu zdań — liczba z powietrza, która pęknie przy pierwszym temacie z siedmioma częściami.
  - Source: Mariusz (przez doradcę dnia), 2026-11-13, „2 a, 3 b, 4 a, 5 c, 6 b — wszystkie zgodnie z Twoimi rekomendacjami” (odpowiedź na pytanie z drogami a, b, c i rekomendacją b).
- 4. Kto i kiedy przyjmuje regułę wytycznych bez decyzji, skoro WAY-172 każe każde nowe znaczenie wytycznych przyjąć jako decyzję przed kodem, a WAY-173 każe regule z szablonu the way wiązać produkt tylko przez decyzję, która ją przyjmuje?
  - Answer: (a) — regułę bez decyzji człowiek przyjmuje jako wiersz tabeli rozstrzygnięć zadania („dokąd idzie”: reguła wytycznych), przed kodem; regułę, którą cykl znalazł sam, opis prośby wymienia wśród tego, czego człowiek nie widział w zadaniu, i człowiek przyjmuje ją przy scaleniu. WAY-172 dotyczy odtąd tylko reguł z decyzją; WAY-173 bez zmian.
  - Not chosen:
    - (b) każda reguła bez decyzji czeka jak w WAY-172, cykl, który znajdzie nową regułę, staje na zablokowanej prośbie o scalenie — cykle stają przy drobnych regułach w rodzaju „nazwa testu opisuje zachowanie”.
    - (c) jak (a), a do tego reguły szablonu the way, które mówią tylko „jak pisać”, wchodzą do wytycznych produktu bez decyzji przyjmującej, zmiana WAY-173 — reguła wiąże produkt spoza jego dziennika, a odejście od niej nie ma gdzie stanąć.
  - Source: Mariusz (przez doradcę dnia), 2026-11-13, „2 a, 3 b, 4 a, 5 c, 6 b — wszystkie zgodnie z Twoimi rekomendacjami” (odpowiedź na pytanie z drogami a, b, c i rekomendacją a; cena drogi a podana w pytaniu: regułę znalezioną w cyklu kod stosuje, zanim człowiek ją zobaczy).
- 5. Czy decyzja bez niezmiennika, bez testu z linią `decision:` i bez pary przykładów jest błędem skryptu kontroli fundamentu (zatrzymuje bramkę), czy tylko pozycją listy?
  - Answer: (c) — błąd tylko dla decyzji, które zmiana dodaje albo zmienia; stare zostają pozycjami listy, która bramki nie zatrzymuje.
  - Not chosen:
    - (a) błąd dla każdej takiej decyzji — w produkcie gry żadna zmiana nie przejdzie, dopóki porządki (osobne zadanie) nie nadrobią ok. 65 wpisów.
    - (b) tylko lista, bez zatrzymania bramki — nowe niepilnowane decyzje dalej przybywają, a lista rośnie.
  - Source: Mariusz (przez doradcę dnia), 2026-11-13, „2 a, 3 b, 4 a, 5 c, 6 b — wszystkie zgodnie z Twoimi rekomendacjami” (odpowiedź na pytanie z drogami a, b, c i rekomendacją c; cena drogi c podana w pytaniu: skrypt musi znać stan, od którego gałąź odeszła, a każda nowa decyzja musi mieć test, niezmiennik albo parę przykładów).
- 6. Jak linia `decision:` w teście wskazuje zdanie decyzji, którego test pilnuje, a nie cały wpis?
  - Answer: (b) — numer i cytat początku zdania, np. `decision: D-12 "Okno końca przejścia…"`; skrypt sprawdza, że cytat stoi we wpisie, a po zmianie brzmienia zdania wskazuje test do przejrzenia. Zmienia WAY-02.
  - Not chosen:
    - (a) sam numer (`decision: D-12`) — słabość wyboru z pytania o części jednego pytania (numer w teście wskazuje większy wpis) zostaje niezałatana.
    - (c) numerowane zdania albo akapity (`D-12/2`) — zmiana kolejności zdań psuje odwołania, a WAY-02 odrzuca dopiski przy numerze, bo czyta się je jak wersję.
  - Source: Mariusz (przez doradcę dnia), 2026-11-13, „2 a, 3 b, 4 a, 5 c, 6 b — wszystkie zgodnie z Twoimi rekomendacjami” (odpowiedź na pytanie z drogami a, b, c i rekomendacją b; cena drogi b podana w pytaniu: każda zmiana brzmienia zdania wymaga poprawki cytatów w testach).

## Context

- Kierunek pięciu zmian Mariusz wybrał 2026-11-12 przy przeglądzie raportu o dzienniku decyzji (raport `odchudzenie_dziennika_decyzji.md`, notatki Mariusza): decyzje 2 („reguła wytycznych bez decyzji: zmienić”), 3 („pojedyncze teksty i liczby: wyprowadzić — wartość w danych albo kodzie z testem, nieoczywisty powód jako komentarz przy wartości”), 4 („część pytania to zdanie istniejącego wpisu: zmienić”; „nie ma tu dobrej decyzji”) i punkt 6 („uzasadnienie i warianty odrzucone zostają w całości; przykłady tylko przy klauzuli bez testu”; próg wejścia; wariant „zachowanie gry w ogóle poza dziennikiem” odrzucony, bo gubi wypróbowane i odrzucone warianty).
- Ustalenie 7 raportu ma angielskie brzmienia „jest → ma być” punktów a–g, od których warto zacząć; ustalenie 6 to sprawdzian nowych reguł na 20 ostatnich wpisach gry (z 20 zostałoby 10).
- Punkt 8 pochodzi z karty D2 raportu `fundamenty_a_kod_loop2.md` (notatki Mariusza), z której zostaje tylko najtańsza część (a): w produkcie gry złapałaby ona 2 przypadki ze 111 niezmienników w dniu powstania; nie wiadomo, ile fałszywych alarmów da sama zmiana sformułowania zdania.
- W dzienniku the way, inaczej niż w dzienniku gry, testów decyzji prawie nie ma: z 304 wpisów (stan `2292f334`) 263 ma tylko parę przykładów, a 21 cytują testy, bo regułą jest zdanie w szablonie albo skillu, a nie zachowanie programu.
- Skrypt kontroli fundamentu jest powierzchnią, na której stoją produkty: wpis `foundation-check-command` mapy części the way obiecuje, że zachowuje ścieżkę, argument i kody wyjścia.
- Na wynik tego zadania czeka zadanie „przegląd fundamentu, którego nie da się pominąć” (jego linia ma `⛔ the-way-co-trafia-do-dziennika-decyzji`).
- Numery linii w raporcie są ze stanu `foundations` `2292f334`; miejsca w plikach wskazują wyżej nagłówki i cytaty.
- Rozmiar: zadanie zmienia kilkanaście decyzji i ok. dziesięciu plików procesu; punkt 8 nie zależy od pozostałych i mógłby być osobnym zadaniem (WAY-13: rozmiar to sygnał, decyzja o podziale należy do Mariusza; zadanie zostaje jedno).

## Questions carried to cycle

- Jak skrypt kontroli fundamentu poznaje stan, od którego gałąź odeszła (punkty 7 i 8), nie zmieniając ścieżki, argumentu ani kodów wyjścia, które obiecuje powierzchnia `foundation-check-command`.
- Który skrypt wypisuje niezmiennik ze zmienionym zdaniem i niezmienionym testem (punkt 8) i w którym miejscu opisu prośby o scalenie go wymienia.
- Czy kolumna „dokąd idzie” zastępuje kolumnę *Kind* tabeli rozstrzygnięć, czy stoi obok niej.

## Human actions

none

## Decisions in play

- **WAY-36 — Is a rule a decision or does it belong in a plan?** Bez zmiany zdania; test planu zostaje pierwszym progiem, a pytanie „dokąd to idzie” staje po nim (*To do* 1, 3).
  > A rule enters the decision log only when it still binds once the change that brings it has been merged; a rule that ends with a piece of work […] stays in the plan of that work, or in the choices of its cycle record where no plan is written.
- **WAY-293 — What prevails where a task or its spec excludes the entry for a choice?** Zmiana częściowa: reguła „wybór wiążący po scaleniu trafia do fundamentu” staje się „trafia w miejsce, które wskazuje pytanie »dokąd to idzie«”, a w the way reguła stojąca w jednym skillu albo szablonie stoi tam z jednym zdaniem powodu, chyba że niesie wybór z realnym kosztem; wariant odrzucony „an exception for every choice written in the text of a skill or template, with no entry” zostaje przyjęty w tym zakresie (*To do* 1; pytanie 1).
  > Where a task or its spec explicitly excludes an entry in the foundation for a choice, that exclusion prevails over the rule that a choice binding after the merge is written into the foundation, and the choice stays a row of the cycle record's questions table; without such an exclusion the rule applies as before.
- **WAY-11 — How does a task end?** Zmiana: krok zwrotny zapisuje przyjęte rozstrzygnięcia w miejscach, które wskazuje pytanie „dokąd to idzie”, nie tylko w fundamencie (*To do* 3).
  > […] In the same change it writes […] the accepted settlements (WAY-134) and projected entries (WAY-126) the task carries that are not yet written. […]
- **WAY-134 — How does a task carry what its refinement settles for the foundation?** Zmiana: tabela ma kolumnę „dokąd idzie”, kandydatem jest też rozstrzygnięcie, które trafi do wytycznych, skilla albo danych i kodu produktu, a cykl zapisuje każdy przyjęty wiersz w jego miejscu (*To do* 2).
  > […] A candidate is a decision, an invariant, a glossary term, or an environment fact a candidate decision or invariant rests on […]. The task's cycle writes each kept row whole into the foundation in its foundation step, or in its return step where the foundation step missed it […]
- **WAY-19 — How are decisions numbered?** Zmiana: część pytania, na które odpowiada istniejący wpis, jest jego zdaniem, o ile nie da się jej zmienić bez tamtego wpisu (*To do* 5).
  > A number stands for the question a decision answers, carries the product's prefix and is given in the order entries are written; a new question gets the next free number, and a new rule next to an existing decision is a new question. […]
- **WAY-05 — How is a decision entry written?** Zmiana: jedno do trzech zdań wiążących na pytanie główne i na każdą dołączoną część, każda w swoim akapicie (*To do* 5; pytanie 3).
  > A decision entry opens with one to three binding sentences — in the present tense, describing a state that is to be true, concrete enough to check — followed by fields a script or an agent reads, then rationale and rejected options in prose […]
- **WAY-12 — How is a decision checked?** Zmiana: testy żyją też przy zdaniach decyzji, oznaczone linią `decision:`; *Verification* nazywa je, a para przykładów stoi tylko przy części zdania, której nie pilnuje żaden test (*To do* 6, 7; pytania 2, 5).
  > A decision names in *Verification* the invariants derived from it, by the identifiers of their entries, where such invariants exist, and tests live only with invariants. A decision may also carry a pair of examples […]
- **WAY-22 — Is a rule a decision or an invariant?** Zmiana: zdanie decyzji trzymane testem z linią `decision:` nie dostaje wyprowadzonego niezmiennika; niezmiennik zostaje dla reguły bez wyboru i dla reguły, na której stoi kilka decyzji; wariant odrzucony „moving a checkable sentence out of its decision” zostaje przyjęty dla pojedynczych wartości, które idą do danych albo kodu z testem i komentarzem (*To do* 1, 6; pytanie 2).
  > […] A rule that records a choice is a decision, and what of it a commit can make false is written as an invariant derived from it; a rule with no choice behind it is an invariant alone.
- **WAY-03 — Who may change an invariant test, and when?** Zmiana: zmiana testu z linią `decision:` też jest wymieniana w opisie prośby o scalenie (*To do* 6; pytanie 2).
  > Any change may alter an invariant test, in any step of its task, implementation included. A change that alters an invariant test names that test in its request, so that the agent reviewing the change and the human merging it see it.
- **WAY-02 — How does whatever depends on an entry refer to it?** Zmiana: linia `decision:` w teście niesie obok numeru cytat początku zdania, którego pilnuje (*To do* 6; pytanie 6).
  > Every foundation entry has a permanent identifier, and everything that depends on it — other entries, tests, documents and code comments — refers to it by that identifier alone, with no fingerprint and no version beside it, and names an entry the foundation holds. […]
- **WAY-65 — How does a check cite its invariant, and which files are invariant tests?** Bez zmiany; wzór dla linii `decision:` i podstawa punktu 8.
  > A test cites, at the test that checks it, each invariant it checks as `invariant: <identifier>`. A file is an invariant test of a change when it cites an invariant on the commit the branch left the main branch from or on the commit being checked.
- **WAY-168 — What does a rule of a product's guidelines hold beside the foundation entries that carry it?** Zmiana: reguła, która mówi tylko, jak pisać kod, testy albo wygląd, stoi w wytycznych sama, z powodem w jednym zdaniu; reguła, która wykonuje wybór z realnym kosztem, dalej wskazuje decyzję (*To do* 4).
  > A binding rule of a product's guidelines names by identifier the decision of the product's log that carries its choice and says what to do and how […], while its reasons and rejected options stand in that decision alone; what a product's guidelines hold that names no such decision is an example, not a rule. […]
- **WAY-167 — Where do a product's guidelines stand, and what are their files named?** Zmiana w uzasadnieniu: wytyczne niosą też reguły własne, bez decyzji (*To do* 4).
  > A product's guidelines are written by hand and stand outside its foundation, in the directory `guidelines/` at the root of its repository […]
- **WAY-171 — What form does a file of a product's guidelines take?** Zmiana: pole *Decision* reguły może czytać `none` (*To do* 4).
  > […] each rule of `## Rules` stands under a heading of its own with the fields *Decision*, *Invariant*, *Good* and *Bad*, the last two reading `none` where the rule gives no such use. […]
- **WAY-172 — How is a new or changed meaning of a product's guidelines approved?** Zmiana: przyjęcia przed kodem wymaga reguła z decyzją; regułę bez decyzji człowiek przyjmuje w tabeli rozstrzygnięć zadania albo, gdy znalazł ją cykl, przy scaleniu (*To do* 4; pytanie 4).
  > A new or changed meaning of a product's guidelines is a decision of the product's log, new or changed, and the code that uses it is made only once the human who accepts decisions (WAY-14) has approved it […]
- **WAY-173 — Does what the-way's template of a discipline of guidelines carries bind a product directly?** Bez zmiany (pytanie 4).
  > The rules a template of a discipline of the-way carries and what the-way's skill of that discipline proposes bind a product only through a decision of the product's log adopting them, and the product departs from any of them only by a decision of its log that gives the reason. […]
- **WAY-26 — How are trade-off principles and non-goals written?** Bez zmiany; mówi już to, co pytanie „sam brak funkcji nie jest zapisywany, chyba że inny wpis na nim stoi”.
  > […] What the product does not do only because no work has brought it yet is no non-goal: where later work builds on it, a decision states what the product does today.

## Settlements to record

Candidates: 12 shown, 12 accepted — 2026-11-13

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Rozstrzygnięcie, które przeszło test planu, przechodzi po kolei pięć pytań „dokąd to idzie” (skill, wytyczne, dane albo kod z testem, sam brak — nic, część istniejącego wpisu — jego zdanie); wpisem zostaje tylko to, co przeszło wszystkie, i tylko tam, gdzie ktoś, kto decyzji nie zna, zrobiłby inaczej, a test, który go zatrzyma, nie powie mu dlaczego; to samo pytanie stosują krok zwrotny i skill zapisujący decyzję. | decision (zmiana WAY-11) | *To do* 1, 3; *Context*, kierunek z 2026-11-12 (decyzje 3 i 6 raportu) | czy pytania dopisać tylko w szablonie, czy też w kroku zwrotnym i skillu decyzji, i w jakiej kolejności |
| 2 | W the way reguła stojąca w jednym skillu albo szablonie stoi tam z jednym zdaniem powodu, a wpisem zostaje tylko wybór z realnym kosztem, który skill wtedy wskazuje; w produktach pierwsze pytanie zostaje dosłowne. | decision (zmiana WAY-293) | *Questions to settle*, pytanie 1 | czy stosować pytanie o skill w dzienniku the way dosłownie |
| 3 | Tabela rozstrzygnięć zadania ma kolumnę „dokąd idzie”, Mariusz przyjmuje w niej każde rozstrzygnięcie, także to spoza dziennika, a cykl zapisuje każdy przyjęty wiersz w jego miejscu. | decision (zmiana WAY-134) | *To do* 2; *Context*, kierunek z 2026-11-12 | czy wiersze spoza dziennika w ogóle trafiają do tabeli |
| 4 | Reguła wytycznych, która mówi tylko, jak pisać kod, testy albo wygląd, stoi w wytycznych sama, z powodem w jednym zdaniu; reguła, która wykonuje wybór z realnym kosztem, dalej wskazuje decyzję. | decision (zmiana WAY-168, WAY-167, WAY-171) | *To do* 4; *Context*, decyzja 2 raportu | czy każda reguła wytycznych dalej potrzebuje decyzji |
| 5 | Regułę wytycznych bez decyzji człowiek przyjmuje jako wiersz tabeli rozstrzygnięć przed kodem, a znalezioną w cyklu — przy scaleniu, z opisu prośby; reguła z szablonu the way dalej wiąże produkt tylko przez decyzję przyjmującą. | decision (zmiana WAY-172) | *Questions to settle*, pytanie 4 | czy cykl, który znajdzie taką regułę, ma stanąć na zablokowanej prośbie |
| 6 | Część pytania, na które odpowiada istniejący wpis, jest jego zdaniem, o ile nie da się jej zmienić bez tamtego wpisu; niezależne pytania dostają osobne numery. | decision (zmiana WAY-19) | *To do* 5; *Context*, decyzja 4 raportu | czy dalej dawać nowy numer każdej regule obok istniejącej decyzji |
| 7 | Pierwszy akapit wpisu odpowiada na pytanie główne jednym do trzech zdań, a każda dołączona część ma własny akapit z jednym do trzech zdań. | decision (zmiana WAY-05) | *Questions to settle*, pytanie 3 | ile zdań wiążących może mieć scalony wpis |
| 8 | Test, który pilnuje zdania decyzji, ma linię `decision: <numer>`; *Verification* nazywa takie testy, para przykładów stoi tylko przy części zdania bez testu, a uzasadnienie i warianty odrzucone zostają w całości. | decision (zmiana WAY-12) | *To do* 6; *Context*, punkt 6 raportu | czy usuwać przykłady i skracać uzasadnienia przy wpisach z testem |
| 9 | Zdanie decyzji trzymane testem z linią `decision:` nie dostaje wyprowadzonego niezmiennika; niezmiennik zostaje dla reguły bez wyboru i dla reguły, na której stoi kilka decyzji; zmiana takiego testu jest wymieniana w opisie prośby. | decision (zmiana WAY-22, WAY-03) | *Questions to settle*, pytanie 2 | czy pisać do zdania z testem także niezmiennik |
| 10 | Linia `decision:` niesie obok numeru cytat początku zdania, którego test pilnuje, a skrypt kontroli wskazuje test, którego cytat we wpisie już nie stoi. | decision (zmiana WAY-02) | *Questions to settle*, pytanie 6 | czy linia wskazuje sam numer wpisu |
| 11 | Decyzja bez niezmiennika, testu z linią `decision:` i pary przykładów jest błędem kontroli fundamentu, gdy zmiana ją dodaje albo zmienia, a stara jest tylko pozycją listy. | decision | *Questions to settle*, pytanie 5 | czy taka decyzja zatrzymuje bramkę |
| 12 | Gdy zmiana poprawia zdanie niezmiennika sprawdzanego testem, a żaden plik z jego linią `invariant:` się nie zmienił, skrypt to wypisuje, a opis prośby o scalenie to wymienia. | decision | *To do* 8; *Context*, karta D2 raportu o fundamentach gry | czy tylko wypisać, czy zatrzymać bramkę |

## Out of scope

- Przepisywanie istniejących wpisów obu dzienników — osobne zadania: porządki dziennika gry i zadanie AIR-518 dla dziennika procesu.
- Sposób, w jaki agenci czytają dziennik (generowany spis, podział na tematy) — osobne zadanie o spisie decyzji.
- Jednorazowe przejście po decyzjach gry, które przy każdej wskazuje test albo nazywa część zdania bez testu — zadanie pierwszych porządków dziennika gry.
