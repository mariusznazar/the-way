---
title: Doprecyzować próbę krótszych wytycznych produktu — znane praktyki jednym słowem, decyzje projektu zostają
status: draft
created: 2026-11-07T21:00
updated: 2026-11-08
tags: [zadanie]
related: "the project note of the process work on a product"
---

## Po co to

- **Jak jest dziś:** Wytyczne produktu `loop2` (pliki w `guidelines/`, z których agenci cyklu the way biorą reguły pisania kodu i testów) liczą 14 plików, około 2700 linii. Reguły powstają, gdy agent zrobi coś inaczej, niż Mariusz chce, ale nie ma metody ich usuwania, więc wytyczne tylko przybywają. Nie wiadomo, ile zdań powtarza to, co model i tak wie, a ile niesie decyzje projektu, których nikt poza wytycznymi nie przekaże.
- **Kto to odczuwa:** agent każdego etapu cyklu, który czyta wskazane wytyczne w całości, i Mariusz, który chciałby wiedzieć, czy da się mieć mniej reguł przestrzeganych równie dobrze. Lekcja kursu Mega.DEV o harnessach mówi, że pliki czytane przez agentów często mają być „well crafted and very concise”, a Adam Gospodarczyk pracuje na niewielu regułach, które agenci przestrzegają.
- **Co jeśli nic:** Dziś nic się nie psuje: recenzja w cyklu porównuje zmianę z wytycznymi i łapie odstępstwa. Wytyczne będą dalej rosły, a pytanie, czy da się je skrócić bez straty, zostanie bez odpowiedzi.

# the way: wytyczne produktów bez spisu stanu i powtórzeń decyzji — decyzja po próbie na loop2

Status: ready for cycle
Project relation: independent

## Description

### Need

- Wytyczne produktu tylko przybywają: the way ma drogę wyjścia dla reguły pliku instrukcji (WAY-130), ale nie dla reguły wytycznych, bo reguła wytycznych niesie decyzję produktu, a WAY-130 pozwala takiej regule stać bez błędu agenta za nią (WAY-168, uzasadnienie).
- Wytyczne `loop2` liczą 14 plików i 2717 linii (`wc -l guidelines/*.md`, `loop2` `01b26d5`, 2026-11-08), a każdy agent cyklu czyta wskazane mu pliki w całości (WAY-213).
- Mariusz chce wiedzieć, czy plik wytycznych da się skrócić tak, żeby agenci przestrzegali go równie dobrze, i chce to wiedzieć z próby, nie z przekonania.
- Metoda dzieli każde zdanie pliku na jedną z pięciu grup: znana praktyka (zastępuje ją nazwa, którą model zna, np. „fail loudly”), decyzja projektu (zostaje), przypadek wyprowadzalny z celu (kandydat do zdjęcia, chyba że powstał, bo agent go z celu nie wyprowadził), spis stanu (wychodzi z reguły) i powtórzenie decyzji albo konfiguracji (zdanie powtarzające decyzję z pola *Decision* reguły albo wartość z pliku konfiguracji, np. wersję narzędzia, wychodzi z reguły; zostaje to, co autor kodu ma zrobić). Piątą grupę Mariusz przyjął w doprecyzowaniu zadania `loop2` (tamten dokument, pytanie 3, 2026-11-08), bo cztery nie wystarczyły.
- Próba idzie na `guidelines/coding.md` w `loop2` osobnym zadaniem loop2 (pytanie 1); to zadanie zamienia jej wynik we wpis dziennika decyzji the way.

### To do

1. Dziennik decyzji the way mówi, że zdania spisu stanu i powtórzenia decyzji albo wartości z konfiguracji wychodzą z wytycznych produktów, a zdań znanej praktyki i przypadków wyprowadzalnych z celu nie zamienia się na nazwę ani nie zdejmuje; nowego tekstu pilnuje szablon, istniejące wytyczne czyści zadanie produktu (pytania 2, 5 i 7).
2. Wspólny szablon wytycznych produktu `product-guidelines/template.md` mówi, że reguła wytycznych nie spisuje stanu ani nie powtarza decyzji ani wartości z konfiguracji (pytanie 5).

### Questions to settle

- Pytanie 1: jak podzielić pracę — przeróbka pliku wytycznych, kilka cykli na nowej wersji, ocena i wpis decyzji — i na którym pliku robić próbę?
  - Answer: dwa zadania. Przeróbka `guidelines/coding.md` w `loop2` to zadanie produktu `loop2`, refinowane jego `refine-task` i skillem wytycznych kodu, ze zmienionymi znaczeniami zatwierdzanymi w dokumencie tamtego zadania (WAY-172). To zadanie the way pisze wpis decyzji i czeka na wynik próby. Sposób oceny próby ustala pytanie 3. Słaby punkt przyjęty z tą drogą: sześć reguł o awariach i logach, z których pochodzą wszystkie przykłady metody, to w większości tłumaczenie szablonu wytycznych kodu the way (*Context*), więc udana próba pociągnie też zmianę szablonu i decyzji WAY-271–276.
  - Not chosen:
    - próba od razu na szablonie the way (`product-guidelines/coding/template.md` i WAY-271–276), a `loop2` bierze nowy tekst przy przesunięciu pinu — decyzje the way, z których korzysta każdy produkt, zmieniają się przed dowodem, a część `loop2` spoza szablonu (linter, przykłady) zostaje niesprawdzona;
    - próba w the way na kopii pliku, bez zmiany `loop2`, z oceną na sucho recenzją dawnych requestów ze starą i nową wersją — tania i bez ryzyka, ale mierzy recenzenta, nie autora kodu, a zadanie samo zastrzega, że recenzja nie może być jedynym przyrządem.
  - Source: Mariusz, 2026-11-08: „A” — na pytanie „Która droga?”, przy drodze A, której słabość nazwano: wynik dotyczy tekstu w jednej trzeciej z szablonu the way.
- Pytanie 2: jaki wynik dała próba na `loop2` i jej ocena?
  - Answer: pomiar nie rozstrzygnął niczego o nazwach praktyk i przypadkach wyprowadzalnych, bo testy nie widzą pliku:
    - Dwóch agentów niezależnie przypisało 121 jednostek pliku do pięciu grup; zgodzili się w 111, a dziesięć spornych zdań zostało bez zmian.
    - Trzy zadania próbne z ukrytymi testami, każde po pięć przebiegów ze starym plikiem, z krótszym (255 linii, z nazwami praktyk i bez przypadków wyprowadzalnych) i bez pliku wytycznych: 45 z 45 przejść, po 5 z 5 w każdym wariancie i zadaniu.
    - Według recenzentów cyklu: większość pilnowanego zachowania niesie sam kod (pomocnik logów odmawia tego, czego zdania zabraniają), agenci bez pliku i tak czytali decyzję o logach i pomocnik, a przy pięciu przebiegach 5 z 5 zgadza się nawet z odsetkiem przejść około 55%.
    - Do `loop2` weszło tylko skrócenie o spis stanu i powtórzenia decyzji albo konfiguracji: `guidelines/coding.md` z 361 do 308 linii; request mówi, że to skrócenie „zostało uzasadnione decyzja po decyzji, nie zmierzone”.
    - Mariusz przy scalaniu (odpowiedź 7, przekazana przez inną sesję): bez zadania na mocniejszą próbę teraz; rozstrzyga to to zadanie w swoim pytaniu 2.
  - Source: request `loop2` #68 (`task/proba-krotszych-wytycznych`), opis, scalony 2026-11-08, commit scalający `331688e`; zapis cyklu `docs/task-cycles/proba-krotszych-wytycznych` przy `9c0dfc8`.
- Pytanie 3: co jest sprawdzianem spoza nowych wytycznych i ile cykli wystarczy, żeby ocenić próbę?
  - Answer: próba kontrolna na 2–3 regułach, których zdania przeróbka zamienia na nazwę praktyki albo z których zdejmuje przypadki wyprowadzalne z celu. Na każdą regułę powstaje małe zadanie, które ją wywołuje, i test, który rozstrzyga wynik bez czytania kodu (np. baza nie odpowiada, więc odpowiedź jest błędem, a nie pustą listą, a wiersz awarii nie niesie `message`). Agent robi każde zadanie kilka razy ze starym plikiem i kilka razy z nowym; wynikiem jest liczba przejść testu na starym i na nowym pliku. Nie liczy się cykli `loop2` po przeróbce. Słaby punkt przyjęty z tą drogą: sprawdzone są tylko reguły, dla których napisano zadanie, i tylko dzisiejszy model.
  - Not chosen:
    - ocena Mariusza przy scalaniu requestów `loop2` po przeróbce — Mariusz, 2026-11-08: „to jest tak abstrakcyjne i tak niedeterministyczne, że nie jestem w stanie tego sensownie ocenić”;
    - dodatkowa recenzja każdego requestu `loop2` ze starą wersją pliku — jedna sesja na request; zgłoszeń, których nie ma, nikt nie odsiewa, a bez punktu wyjścia liczba odstępstw nic nie mówi; reguły o awariach i logach rusza mało zmian, więc pięć requestów zbiera się tygodniami;
    - ta sama recenzja z rozstrzyganiem przez Mariusza i punktem wyjścia sprzed przeróbki — rozstrzyganie wymaga osądu kodu, którego Mariusz nie da (powód jak przy pierwszej drodze);
    - bez pomiaru, z decyzją obejmującą tylko spis stanu i wartości przepisane z konfiguracji — tanio, ale bez odpowiedzi, czy nazwa praktyki zastępuje zdanie.
  - Source: Mariusz, 2026-11-08: „tak, próba kontrolna na 2–3 regułach” — na pytanie, czy wynik w postaci „test przeszedł 5 z 5 razy ze starym plikiem i 3 z 5 z nowym” byłby czymś, na czym da się oprzeć decyzję, przy drodze, której słabość nazwano: sprawdzone są tylko reguły z zadaniem i tylko dzisiejszy model.
- Pytanie 6: gdzie biegnie próba kontrolna i kiedy krótszy plik wchodzi do `loop2` — przed jej wynikiem czy razem z nim?
  - Answer: w zadaniu `loop2`: obejmuje ono klasyfikację, krótszy plik, 2–3 zadania próbne z testami i przebiegi agenta ze starym i nowym plikiem, a jego request pokazuje liczby przejść. Pomiar biegnie na gałęzi z całym krótszym plikiem. Po dobrym wyniku do `loop2` wchodzą tylko skrócone zdania własne `loop2`; zdania przepisane z szablonu wytycznych kodu the way zostają w `loop2` bez zmian i dochodzą do niego dopiero przez zmianę szablonu w the way i przesunięcie pinu, więc D-252 dalej „departs from none”. Słaby punkt przyjęty z tą drogą: zadanie `loop2` staje się eksperymentem, a jego cykl sam wymyśla, jak uruchamiać agenta wielokrotnie; zmiana szablonu i decyzji WAY-271–276 staje się realną pracą (pytanie 5).
  - Not chosen:
    - cały krótszy plik wchodzi do `loop2` razem z wynikiem — wymaga zmiany D-252 na odstępstwo od szablonu (WAY-173); Mariusz w zadaniu `loop2`, 2026-11-08: „nie podoba mi się odchodzenie od szablonu”;
    - gałąź w całości do kosza, wynik służy tylko decyzji — zdania spisu stanu, które nie zmieniają znaczenia, zostają w pliku bez powodu;
    - krótszy plik wchodzi najpierw, próba kontrolna jako trzecie zadanie `loop2` — krótszy plik działa we wszystkich cyklach `loop2`, zanim ktoś sprawdzi, że nie szkodzi, i dochodzi jeden dokument zadania więcej;
    - próbę kontrolną robi Mariusz poza cyklem, na krótszym pliku z gałęzi — zadania próbne i testy powstają bez recenzji cyklu, a czas Mariusza idzie na kilkanaście przebiegów.
  - Source: Mariusz, 2026-11-08: „A” — na pytanie „Która droga?”, przy drodze A, której słabość nazwano: cykl sam wymyśla, jak uruchamiać agenta wielokrotnie; granica scalania: Mariusz, 2026-11-08: „ok zróbmy połączenie” — na zderzenie tej odpowiedzi z jego odpowiedzią na pytanie 1 zadania `loop2` („tak, gałąź do kosza z powtórzeniem scalonych zadań”), przy połączeniu zaproponowanym przez sesję zadania `loop2`.
- Pytanie 4: czy próba obejmuje też instrukcje agentów Mariusza w jego prywatnych notatkach (główny plik instrukcji, reguły, playbooki), czy tylko wytyczne produktu?
  - Answer: tylko wytyczne produktu; wpis decyzji mówi o wytycznych produktów. Słaby punkt przyjęty z tą drogą: odpowiedź dla instrukcji Mariusza przyjdzie później, osobnym zadaniem, jeśli wynik okaże się zachęcający.
  - Not chosen:
    - także instrukcje Mariusza — próba kontrolna sprawdza reguły pisania kodu, więc decyzja dla instrukcji stałaby bez dowodu, a pliki spoza the way nie są wiązane wpisem w jego dzienniku.
  - Source: Mariusz, 2026-11-08: „tylko wytyczne produktu” — na pytanie o zasięg próby, przy drodze, której słabość nazwano: odpowiedź dla instrukcji przyjdzie później.
- Pytanie 5: jeśli wpis decyzji powie „tak”, czy zmiana tego zadania dostosowuje też skille i szablony wytycznych the way (`product-guidelines/`), czy robi to osobne zadanie?
  - Answer: zmiana tego zadania dopisuje do wspólnego szablonu wytycznych produktu (`product-guidelines/template.md`) regułę, że reguła wytycznych nie spisuje stanu ani nie powtarza decyzji ani wartości z konfiguracji, więc skille wytycznych przestają dopisywać takie zdania w nowym tekście; istniejących wytycznych nic samo nie czyści, w produkcie robi to jego własne zadanie. Słaby punkt przyjęty z tą drogą: 13 pozostałych plików wytycznych `loop2` zostaje, jakie są, dopóki Mariusz nie zleci zadania.
  - Not chosen:
    - jak wyżej, a do tego krok w trybach audytu trzech skilli wytycznych, który szuka takich zdań w istniejących wytycznych — zmiana trzech skilli naraz, a tryb odświeżenia wytycznych kodu ma ciężkie wymagania wstępne, które w zadaniu `loop2` trzeba było pominąć;
    - osobne zadanie na szablon, to zadanie pisze tylko wpis decyzji — do czasu drugiego zadania agenci piszący wytyczne według szablonu dalej dopisują zdania, które decyzja każe usuwać.
  - Source: Mariusz, 2026-11-08: „A” — na pytanie „Który zakres ma mieć zmiana tego zadania?”, przy drodze A, której słabość nazwano: istniejące wytyczne zostają, dopóki nie zlecisz zadania.
- Pytanie 7: co mówi wpis decyzji the way po tym wyniku?
  - Answer: częściowe „tak”: zdania spisu stanu i powtórzenia decyzji albo konfiguracji wychodzą z wytycznych produktów; zdań znanej praktyki i przypadków wyprowadzalnych z celu nie zamienia się na nazwę ani nie zdejmuje, bo próba nie dała na to dowodu. Słaby punkt przyjęty z tą drogą: ta część stoi na rozumowaniu, nie na pomiarze, którego dla niej nie da się zrobić (pytanie 3).
  - Not chosen:
    - wpis czeka na mocniejszą próbę, z regułami, które agent łamie bez pliku, i z więcej niż pięcioma przebiegami — poprzednia próba kosztowała około 2¼ godziny i 119 mln tokenów, a w `loop2` takiej reguły może nie być, bo zachowania pilnuje kod;
    - „nie”, skrócenie w `loop2` zostaje jednorazowe — odrzuca też część bez sporu, a wytyczne innych produktów dalej tylko przybywają;
    - pełne „tak”, wszystkie pięć grup — wniosek z braku sygnału, a Mariusz chciał odpowiedzi „z próby, nie z przekonania”.
  - Source: Mariusz, 2026-11-08: „A” — na pytanie „Który wariant ma powiedzieć wpis?”, przy drodze A, której słabość nazwano: stoi na rozumowaniu, nie na pomiarze.

## Context

- Zdania sekcji o awariach i logach w `loop2` `guidelines/coding.md:155-268` to w większości tłumaczenie szablonu wytycznych kodu the way: np. `coding.md:190-193` („Awarii nie zamieniaj ani w odpowiedź »wszystko w porządku«, ani w pustą listę. […]”) odpowiada `product-guidelines/coding/template.md:190-193`, a `coding.md:209-212` (przypadek wyprowadzalny z celu) odpowiada `template.md:198-200`.
- Szablon każe produktowi podać te zdania: „each rule's bullet gives what the product's text says of how to apply it” (`product-guidelines/coding/template.md:182`), a decyzja `loop2` D-252 „adopts all six rules on failures and logs of the coding template of its pinned the-way and departs from none of them” (`loop2` `foundations/decisions.md`, `01b26d5`).
- Reszta `loop2` `guidelines/coding.md` to treść własna `loop2`: reguły lintera, formatera i audytu zależności (`coding.md:30-153`), w których stoją m.in. wersje narzędzi i liczby reguł przepisane z konfiguracji, oraz przykłady reguł Ruffa (`coding.md:270-348`).
- Źródła metody: lekcja s01e04 kursu Mega.DEV o harnessach (plik wizji i styleguide „have to be well crafted and very concise”, bo są doklejane do kontekstu często) i opis pracy Adama Gospodarczyka z agentami w prywatnych notatkach Mariusza — kotwice („one word pulls in a whole concept”), kierunek zamiast przepisu, poprawianie przyczyny zamiast odpowiedzi, przypomnienia w trakcie zadania.
- Skill `maintain-coding-guidelines` nie ma trybu, który przepisuje tekst wytycznych bez zmiany ich kontroli: tryb odświeżenia wymaga zbioru startowego z badaniem, próbnego uruchomienia narzędzi i audytu rodzajów; w zadaniu `loop2` Mariusz przyjął pominięcie tych kroków (tamten dokument, pytanie 8, 2026-11-08). Odpowiedź na pytanie 5 tej luki nie zamyka: zadanie produktu, które czyści istniejące wytyczne, trafi na nią tak jak zadanie `loop2`.
- Sześć reguł o awariach i logach szablonu wytycznych kodu (`product-guidelines/coding/template.md:184-215`) nie ma zdań spisu stanu ani wartości z konfiguracji, a przy odpowiedzi na pytanie 7 zdania znanej praktyki zostają, więc zmiana szablonu i decyzji WAY-271–276, którą zapowiadał słaby punkt pytania 1, nie zachodzi.
- Lista `### Logging scope` nie jest spisem stanu: szablon wytycznych kodu każe tekstowi powiedzieć, że „the list is the product's promise and no inventory of its code” (`product-guidelines/coding/template.md:208-213`, WAY-274), a „The list of `### Logging scope` is no such copy” (`template.md:313-315`).
- Zmiana tego zadania pisze wpis w `foundations/decisions.md` i zdanie w `product-guidelines/template.md`, które nie są kodem, testem ani interfejsem, więc czytanie wytycznych produktu nie ma tu czego wybrać; the way nie ma własnych `guidelines/`.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-168 — „A binding rule of a product's guidelines names by identifier the decision of the product's log that carries its choice and says what to do and how, and may give a use that follows it and one that breaks it, each in one line, while its reasons and rejected options stand in that decision alone; what a product's guidelines hold that names no such decision is an example, not a rule.” Reguła po usunięciu spisu stanu i powtórzeń dalej mówi, co robić i jak.
- WAY-169 — „A change that changes the binding part of a decision or an invariant brings every rule of the guidelines naming it in line in the same change, its author finding those rules by the entry's identifier.” Reguła, która nie powtarza decyzji, ma mniej do wyrównania, gdy decyzja się zmienia.
- WAY-171 — „Every file of a product's guidelines holds, in this order, the header lines *Discipline* and *Applies to* […] and the sections `## When to read`, `## Rules`, `## Examples` and `## Where in code` […]. `## Where in code` names by their paths the files and directories of the product the guidelines point to and copies no value from them […].” Krótsza wersja zachowuje tę formę.
- WAY-172 — „A new or changed meaning of a product's guidelines is a decision of the product's log, new or changed, and the code that uses it is made only once the human who accepts decisions (WAY-14) has approved it, in the document of the task that needs it […]. Using a meaning that a decision of the product's log already carries takes no approval, and neither does changing a value that keeps its meaning.” Zadanie produktu, które usuwa zdania z jego wytycznych, rozstrzyga przy każdym, czy znaczenie się nie zmienia; jeśli się zmienia, potrzebuje zgody Mariusza w dokumencie zadania.
- WAY-173 — „The rules a template of a discipline of the-way carries and what the-way's skill of that discipline proposes bind a product only through a decision of the product's log adopting them, and the product departs from any of them only by a decision of its log that gives the reason.”
- WAY-213 — „[…] the agent reads each file named whole, never excerpts of it or a review checklist in its place […].” Uzasadnienie: „guidelines are short and hold together only as a whole, so a file goes to an agent whole”.
- WAY-130 — „The skill of `instruction-files` proposes a rule, and a change to the-way's repository instruction files adds one, only to remove a mistake agents made more than once, found in records of their work, and names that mistake where it proposes or adds the rule, unless the rule carries a decision the repository records or a step of an activity in the file that leads that activity. The skill proposes to take out a rule added for a mistake once that mistake can no longer be named, or once agents working without it show that it is not needed.” *Scope* nie obejmuje `product-guidelines`.
- WAY-100 — „A method or practice borrowed from outside a product binds its way of working only through a decision that names what is adopted, where it applies, and why. When an agent recognizes a likeness to a method or practice no decision has adopted, it asks a human before treating it as a rule.” Nazwa praktyki w regule (np. „fail loudly”) przywołuje praktykę spoza produktu, z tym, czego żadna decyzja nie przyjęła.
- WAY-271 — „The template of the coding discipline requires six rules on failures and logs in the general file of a product's coding guidelines, after the rules of its standing checks, each under a heading of its own […].” Treść tych reguł dają WAY-272–276 i `product-guidelines/coding/template.md:184-215`.

## Settlements to record

Candidates: 7 shown, 3 accepted — 2026-11-08

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Zdania spisu stanu i powtórzenia decyzji albo wartości z konfiguracji wychodzą z wytycznych produktów; zdań znanej praktyki i przypadków wyprowadzalnych z celu nie zamienia się na nazwę ani nie zdejmuje, bo próba nie dała na to dowodu. | decision | pytanie 7 | czy wpis pozwala też zamieniać zdania na nazwy praktyk i zdejmować przypadki wyprowadzalne, jak robiła krótsza wersja próbna |
| 2 | Nowego tekstu wytycznych pilnuje reguła wspólnego szablonu; skille wytycznych nie szukają takich zdań w istniejących wytycznych, czyści je zadanie produktu. | decision | pytanie 5 | czy dopisać krok szukania takich zdań do trybów audytu trzech skilli wytycznych |
| 3 | Na próbie w `loop2` (trzy zadania, po pięć przebiegów Sonnet 5.5) testy przeszły 45 z 45 razy ze starym plikiem, z krótszym i bez pliku, więc pomiar nie odróżnił pliku z nazwami praktyk od pełnego. | environment fact | pytanie 2 | czy *Based on* wpisu z wiersza 1 nazywa fakt, którego zmiana (próba, która znajdzie różnicę) otwiera decyzję, czy cytuje request tylko jako zdarzenie |

## Out of scope

- Instrukcje agentów Mariusza w jego prywatnych notatkach (pytanie 4).
- Przeróbka `loop2` `guidelines/coding.md` — osobne zadanie `loop2` (pytanie 1).
