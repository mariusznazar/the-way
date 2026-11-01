---
title: Ustalić, co produkt zapisuje w logach, żeby dało się sprawdzać jego działanie
status: draft
created: 2026-10-25T16:00
updated: 2026-11-01
tags: [zadanie]
related: "[[(P) Proces pracy nad produktem]]"
---

# Ustalić, co produkt zapisuje w logach, żeby dało się sprawdzać jego działanie

Status: ready for cycle
Project relation: independent

## Description

### Need

- Agent ma drogę do logów działającego produktu, ale nic w the way nie mówi, co kod ma do nich zapisywać.
- Przegląd zmiany wyłapuje „połknięte” błędy, czyli awarie, które kod ukrywa, tylko w kodzie tej jednej zmiany (`task-cycle/review/SKILL.md:92-93`).
- Szablon wytycznych kodu nie ma żadnej reguły o błędach ani o logach (`product-guidelines/coding/template.md`).
- Agent piszący kod i agent recenzujący zmianę nie mają wspólnej reguły, według której oceniliby, czy zmiana zostawia ślad po awarii.
- Mariusz zgłasza, że odczuwa to wtedy, gdy w działającym produkcie coś się psuje, a w logu nic nie ma.
- Mariusz zgłasza, że bez zmiany produkt rośnie bez śladu po awariach; dziś to nie przeszkadza, bo jedynym użytkownikiem jest Mariusz, a zacznie przy pierwszym obcym użytkowniku.

### To do

1. Szablon wytycznych kodu the way (`product-guidelines/coding/template.md`) dostaje osobną, wymaganą część o błędach i logach: reguły pliku ogólnego `guidelines/coding.md`, każda pod własnym nagłówkiem, z *Invariant* `none` (pytanie 6), które mówią, jak kod pisze zapis:
   - awaria, czyli sytuacja, w której produkt nie zrobił tego, o co go poproszono albo co miał zrobić sam, z innego powodu niż przewidziana odmowa, także gdy zawiodła usługa z zewnątrz, zapisuje się zawsze razem z przyczyną — z oryginalnym błędem, nie samym napisem — raz, tam, gdzie kod ją obsługuje; każdy osobno działający program produktu ma jedno ostatnie miejsce, które zapisuje to, czego nie obsłużył żaden kod; przewidziana odmowa, na przykład złe hasło, jest zwykłą odpowiedzią i reguła jej nie dotyczy (pytania 5 i 9);
   - awarii się nie chowa: nie zamienia się w odpowiedź „wszystko w porządku” ani w pustą listę; tryb awaryjny, w którym produkt działa dalej bez jednej funkcji, wolno tylko wtedy, gdy ustali go zadanie, zapisując go jako decyzję produktu, i zawsze zostawia linię w logu (pytanie 5);
   - linia przepływu, czyli tego, co produkt robi dla jednej sprawy, od żądania albo zadania w tle do jego końca, niesie identyfikatory, które łączą zdarzenia tego przepływu, każdy pod tą samą nazwą w każdej linii, tak żeby szukanie znalazło całą sprawę, a postać linii wybiera produkt w swojej decyzji (pytanie 4); identyfikatorów nie niesie linia spoza przepływu, na przykład start programu albo skrypt budowania, ani linia z ostatniego miejsca, które zwykle nie wie, czego sprawa dotyczyła (pytanie 9);
   - zdarzenia biznesowe, które wymienia zakres produktu, zostawiają linię w logu (pytanie 8);
   - w logu nie ma sekretów ani danych osobowych, a wyjątkiem od zakazu danych osobowych są identyfikatory z listy zakresu produktu; kod nie zapisuje całych obiektów ani treści żądań, co nie dotyczy samego błędu; gdy oryginalny błąd cytuje takie wartości, zakaz ma pierwszeństwo przed regułą o przyczynie: zapisuje się błąd bez tych wartości, z jego rodzajem, kodem i miejscem w kodzie (pytania 3 i 10).
2. Skill wytycznych kodu (`maintain-coding-guidelines`, `product-guidelines/coding/`) proponuje tę część przy zakładaniu, odświeżaniu i rozszerzaniu wytycznych produktu, na drodze z pytania 2.
3. Kroki tego skilla (`settle.md`, `task_document.md`, `hand_back.md`) prowadzą do decyzji w dzienniku produktu, która:
   - przyjmuje tę część albo odstępuje od niej z powodem; skill pyta o część w całości i przyjmuje odstępstwo od pojedynczej reguły, gdy człowiek je zgłosi;
   - ustala zasadę zakresu produktu: jakie identyfikatory i jakie zdarzenia biznesowe loguje (pytania 1 i 12);
   - mówi, że pozycję zgodną z zasadą agent dopisuje sam, a to, co wskazuje osobę, wymaga zgody człowieka (pytania 1 i 10); numer użytkownika nadany w produkcie skill stawia przed człowiekiem przy przyjęciu listy, a dopisanie go później też wymaga zgody;
   - mówi, jaką postać ma linia (pytanie 4).

   Listę na dziś, przy przyjęciu z tego, co produkt ma w kodzie albo w planie, niesie reguła zakresu w `guidelines/coding.md`; jest obietnicą produktu, nie spisem stanu kodu (pytania 1 i 12).
4. Te same kroki stawiają przed człowiekiem wybór biblioteki, która zapisuje linię, drogą `new_tools.md`, gdy produkt jej potrzebuje, a krok technologii uruchamiają tylko przy wyborze zastrzeżonym (pytanie 4); `settle.md` nazywa przy tej części jej słabe punkty z pytań 1, 3, 5, 8 i 9.
5. Skill przeglądu (`task-cycle/review/SKILL.md`, sekcja „Review”) dostaje dwie ogólne linie, które nie nazywają tej części:
   - zmianę kodu porównuje się z każdą regułą przeczytanych wytycznych, która nie ma niezmiennika, a do której zmiana sięga (WAY-168), więc kod produktu, który tej części nie przyjął, nie jest z nią porównywany;
   - przy zmianie, która pisze albo zmienia wytyczne, same wytyczne porównuje się z szablonem wspólnym i, gdzie the way go daje, z szablonem ich dyscypliny, na przypiętym commicie the way (WAY-170), i tak recenzent zauważa brak tej części (pytanie 2).

### Questions to settle

- Pytanie 1: co stoi w decyzji produktu o zakresie — sama lista identyfikatorów i zdarzeń, sama zasada, czy zasada z listą na dziś — i co dzieje się, gdy dochodzi nowa pozycja?
  - Answer: zasada z listą na dziś — decyzja produktu ma zasadę i aktualną listę identyfikatorów i zdarzeń, przy przyjęciu z tego, co produkt ma w kodzie albo w planie; pozycję zgodną z zasadą agent dopisuje sam w zmianie, która ją wnosi, i człowiek widzi ją przy scalaniu; nowe znaczenie wymaga zgody człowieka (WAY-172).
  - Not chosen:
    - sama lista — człowiek widzi każdą pozycję, ale każda nowa zmienia decyzję i przechodzi przez skill wytycznych, a gdy wyjdzie dopiero w cyklu, cykl staje i czeka na człowieka; nowe zdarzenia przychodzą z każdą funkcją
    - sama zasada — nowa pozycja nie wymaga zgody i cykl nie staje, ale człowiek nie widzi listy, recenzent wszystko ocenia czytając, a ustalenie „które identyfikatory” się zmienia
  - Source: Mariusz, 2026-10-31: „3” — na drogę 3 przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: ręcznie pisana lista może rozjechać się z kodem, a to, czy pozycja pasuje do zasady, ocenia agent; WAY-172, `foundations/decisions.md:4776-4777`, `foundations` `ea4694e`.
  - Zastąpione w części odpowiedzią na pytanie 12: lista stoi w regule wytycznych, nie w decyzji.
- Pytanie 2: jak ta część wchodzi do produktu, który ma już wytyczne kodu, i od kiedy go wiąże — skoro odświeżenie jej nie obejmuje, a rozszerzenie bada przy tym każde stałe sprawdzenie, choć część nie ma narzędzia?
  - Answer: zwykłym rozszerzeniem — część nie dostaje własnej drogi; odświeżenie, które zauważy jej brak, proponuje ją, „tak” człowieka zmienia zadanie w rozszerzenie, a „nie” jest odstępstwem z powodem; część wiąże produkt od jego decyzji, a brak części zauważa przegląd pierwszej zmiany pliku `guidelines/coding.md` po przejściu na nowszą wersję the way.
  - Not chosen:
    - wąska droga tylko dla tej części — taniej przy każdym produkcie, ale trzeba zmienić WAY-211, skill dostaje kolejny stały tryb, a linter nie dostaje nowych reguł przy tej okazji
    - część nieobowiązkowa dla produktów z wytycznymi — nikt nie dostaje uwagi w przeglądzie, ale to odchodzi od „przyjmuje albo odstępuje z powodem”, brak części wygląda jak przeoczenie, a produkt, który przyjmie ją pierwszy, może zostać jedynym, który ją ma
  - Source: Mariusz, 2026-11-01: „1” — na drogę 1 przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: produkt dowiaduje się o części dopiero przy zmianie wytycznych albo gdy sam otworzy rozszerzenie; `product-guidelines/coding/starting_set.md:10-11`, WAY-170, `foundations/decisions.md:4695-4697`, WAY-173, `foundations/decisions.md:4812-4814`, `foundations` `ea4694e`.
- Pytanie 3: jak pogodzić „id użytkownika” z regułą „w logu nie ma danych osobowych”, także gdy oryginalny błąd sam niesie dane osobowe albo sekret, i czy ta reguła opiera się na prawie, czyli czy produkt w ogóle może od niej odstąpić?
  - Answer: w logu nie ma danych osobowych ani sekretów, poza identyfikatorami z listy decyzji produktu; agent dopisuje na listę sam tylko numer nadany wewnątrz produktu, nic nieznaczący poza nim, a e-mail, imię, telefon czy adres w roli identyfikatora to nowe znaczenie, które wymaga zgody człowieka; kod nie zapisuje całych obiektów ani treści żądań, a błąd, który może nieść takie dane, zapisuje bez nich; reguła jest wyborem szablonu, nie powtórzeniem prawa, więc produkt może od niej odstąpić z powodem, a prawo obowiązuje go niezależnie od tego (WAY-86).
  - Not chosen:
    - dosłownie żadnych danych osobowych — najprostsze brzmienie, ale odpada id użytkownika, więc nie da się prześledzić akcji jednego użytkownika w czasie
    - tylko to z danych osoby, co wymienia lista — sprzeczność znika bez dalszych reguł, ale agent dopisuje na listę sam, więc mógłby dopisać też e-mail i reguła nic by nie chroniła
  - Source: Mariusz, 2026-11-01: „3” — na drogę 3 przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: recenzent widzi kod, a nie to, co błąd zawiera w działaniu, więc nietypowy przeciek może przejść, a to, czy id użytkownika w logu jest zgodne z prawem, ocenia produkt; RODO, art. 4 pkt 1, https://gdpr-info.eu/art-4-gdpr/: „in particular by reference to an identifier such as a name, an identification number, location data, an online identifier”; motyw 26, https://gdpr-info.eu/recitals/no-26/: „by the use of additional information should be considered to be information on an identifiable natural person.”; art. 5 ust. 1 lit. c, https://gdpr-info.eu/art-5-gdpr/: „adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed”; przeczytane 2026-11-01; odczytanie, że RODO nie zakazuje logowania danych osobowych, jest lekturą agenta, nie opinią prawną.
  - Zastąpione w części odpowiedzią na pytanie 10: granica dla agenta dotyczy tylko tego, co wskazuje osobę.
- Pytanie 4: czy postać linii logu ustala szablon, czy każdy produkt w swojej decyzji, i kto wybiera bibliotekę, która tę linię zapisuje?
  - Answer: szablon wymaga stałości, a postać wybiera produkt — każdy identyfikator stoi pod tą samą nazwą w każdej linii, tak żeby szukanie znalazło całą sprawę, a produkt mówi w swojej decyzji, jak to robi; bibliotekę, która zapisuje linię, wybiera człowiek na istniejącej drodze skilla wytycznych, w zadaniu, które przyjmuje część, a krok technologii wchodzi tylko wtedy, gdy wybór jest wyborem zastrzeżonym (WAY-268).
  - Not chosen:
    - szablon narzuca jedną postać — każdy produkt wygląda tak samo i narzędzia do logów dobrze taki zapis czytają, ale wiąże też małe produkty, często wymaga biblioteki, a odstępstwo trzeba uzasadniać tam, gdzie nie ma szkody
    - szablon milczy o postaci — najmniej tekstu, ale reguła o identyfikatorach jest spełniona także wtedy, gdy nazwy się rozjeżdżają, a szukanie gubi linie, i nikt tego nie zgłosi
  - Source: Mariusz, 2026-11-01: „2” — na drogę 2 przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: recenzent sprawdza stałość nazw czytając kod, więc rozjazd w rzadko zmienianym pliku może przejść niezauważony; zadanie o kroku technologii z PR https://github.com/mariusznazar/the-way/pull/65, pytanie 3; `product-guidelines/coding/new_tools.md:3-7`, `project-level/technology/reserved_choices.md:11-13`, `foundations` `ea4694e`.
- Pytanie 5: co liczy się jako błąd, który trzeba zapisać i którego nie wolno schować — czy także przewidziane odmowy, na przykład złe hasło, i zamierzony tryb awaryjny, w którym produkt działa dalej bez jednej funkcji?
  - Answer: rozróżnienie w szablonie — awaria to coś, co nie powinno się zdarzyć w poprawnie działającym produkcie; przewidziana odmowa, na przykład złe hasło, to zwykła odpowiedź i reguła jej nie dotyczy; awaria zapisuje się raz, tam, gdzie kod ją obsługuje; tryb awaryjny, w którym produkt działa dalej bez jednej funkcji, wolno tylko wtedy, gdy ustali go zadanie, i zawsze zostawia linię w logu.
  - Not chosen:
    - dosłownie — brak wyjątków do oceny, ale log pełen złych haseł i powtórzeń, a tryb awaryjny zakazany, więc padnięcie jednej funkcji wyłącza całą stronę
    - każdy produkt definiuje awarię sam — definicja pasuje do produktu, ale to kolejna pozycja w decyzji, większość produktów napisze to samo, a audyty przestają być porównywalne
  - Source: Mariusz, 2026-11-01: „2” — na drogę 2 przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: granicę między awarią a odmową ocenia agent i recenzent, a tryb awaryjny zostawia linię w logu, ale użytkownik widzi działającą stronę, więc nikt się nie dowie, jeśli logów nikt nie czyta; to, jak człowiek dowiaduje się o awarii, rozstrzyga krok technologii.
  - Zastąpione w części odpowiedzią na pytanie 9: definicja awarii jest szersza.
- Pytanie 6: co z tej części da się sprawdzać skryptem albo linterem, a co zostaje osądem recenzenta, i czy część dostaje reguły, czy same przykłady?
  - Answer: reguły, nie przykłady, bo regułą czyni ją decyzja przyjmująca ją w dzienniku produktu, a nie możliwość sprawdzenia skryptem; reguły tej części czyta przegląd zmiany (*Invariant* `none`), chyba że tani test sprawdza całą regułę na konwencji kodu; test łapiący tylko jej fragment, na przykład pusty blok, jest regułą zestawu lintera produktu pod jego własnym niezmiennikiem, gdy przejdzie próbę z WAY-203, a nie regułą tej części; o tym, czy naruszenie blokuje zmianę, rozstrzyga ocena recenzenta.
  - Source: WAY-168, `foundations/decisions.md:4617-4620`, `foundations` `ea4694e`: „what a product's guidelines hold that names no such decision is an example, not a rule. A rule names an invariant only where a cheap test of the product's suite checks the rule on a convention of the product's code; a rule no such test can check names none, and the review of each change the rule reaches compares the change with it.”; WAY-203, `foundations/decisions.md:5454-5456`, tamże: „A rule of a linter's set stands among the rules that block a change in the product's decision adopting the set, and so is checked by the invariant of the one rule of the product's coding guidelines on its linter, only where every report it gives on the product's code leads to a change of code worth making”; `task-cycle/review/SKILL.md:106`, tamże: „A finding blocks when you grade it Critical or Important and it lies within the task (WAY-161).”
- Pytanie 7: czy dodanie tej części do istniejących wytycznych kodu może być odświeżeniem?
  - Answer: nie — obejmuje coś nowego, więc jest rozszerzeniem; co robi odświeżenie, które zastaje wytyczne bez tej części, rozstrzyga pytanie 2.
  - Source: WAY-251, `foundations/decisions.md:7180-7183`, `foundations` `ea4694e`: „a refresh updates or corrects accepted guidelines within the scope they already cover, including adapting them to a new version of a tool the product already uses. An extension covers something new, and its research checks whether to use what the product already has or something else”.
- Pytanie 8: czy zdarzenia wymienione w decyzji produktu muszą w ogóle zostawiać linię w logu, skoro część mówi o tym, jak kod pisze zapis?
  - Answer: tak, osobną regułą części — zdarzenia, które wymienia decyzja produktu, zostawiają linię w logu.
  - Not chosen:
    - bez reguły, tylko decyzja produktu — krótsza część i lista i tak wiąże, ale wytyczne milczą, więc reguła działa tylko wtedy, gdy ktoś trafi na tę decyzję
    - bez zdarzeń w zakresie — sama lista identyfikatorów i najmniej pracy, ale to zmienia ustalenie Mariusza, a log pokazuje awarie, nie to, co działo się przed nimi
  - Source: Mariusz, 2026-11-01: „1” — na drogę 1 przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: reguła obejmuje tylko zdarzenia z listy, a nowe dopisuje agent, więc funkcja, której nikt na listę nie wpisze, dalej nie zostawi linii.
- Pytanie 9: co z awarią, której żaden kod nie obsłużył, i z awarią czegoś spoza produktu, skoro „tam, gdzie kod ją obsługuje” nie mówi, gdzie zapisać tę pierwszą, a „nie powinno się zdarzyć w poprawnie działającym produkcie” może nie objąć tej drugiej?
  - Answer: szersza definicja i ostatnie miejsce zapisu — awaria to sytuacja, w której produkt nie zrobił tego, o co go poproszono albo co miał zrobić sam, z innego powodu niż przewidziana odmowa, także gdy zawiodła usługa z zewnątrz; awaria zapisuje się tam, gdzie kod ją obsługuje, a produkt ma jedno ostatnie miejsce, które zapisuje to, czego nie obsłużył żaden kod; ta definicja zastępuje definicję z pytania 5.
  - Not chosen:
    - tylko szersza definicja — mniej do zrobienia, a sprawy z zewnątrz są objęte, ale awaria, której nikt nie obsłużył, dalej może nie zostawić śladu, czyli objaw z początku zadania zostaje
  - Source: Mariusz, 2026-11-01: „1” — na drogę 1 przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: ostatnie miejsce zapisuje zwykle bez identyfikatorów sprawy, a gdy pada cały program, zapisze tylko tyle, ile zdąży.
- Pytanie 10: czy granica z pytania 3 dotyczy wszystkich identyfikatorów, czy tylko tych, które wskazują osobę, skoro „tylko numer nadany wewnątrz produktu” zatrzymałby też identyfikator transakcji od dostawcy płatności?
  - Answer: granica dotyczy tylko osób — agent sam dopisuje każdy identyfikator rzeczy, na przykład zamówienia, transakcji czy żądania; zgody człowieka wymaga wszystko, co wskazuje osobę, także e-mail, imię, telefon, adres zamieszkania i adres IP; wyjątkiem jest numer użytkownika nadany w produkcie, który ustala się przy przyjęciu listy; ta granica zastępuje „tylko numer nadany wewnątrz produktu” z pytania 3.
  - Not chosen:
    - granica dosłownie, tylko numer nadany wewnątrz produktu — najostrzejsza i agent prawie niczego nie ocenia, ale numer transakcji i numer zamówienia zatrzymują cykl i czekają na człowieka
  - Source: Mariusz, 2026-11-01: „2” — na drogę 2 przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: to agent ocenia, czy numer wskazuje osobę, numer zamówienia też da się powiązać z konkretną osobą przez dane produktu, a ocena zgodności z prawem zostaje przy produkcie.
- Pytanie 11: co z nazwami własnymi w kopii tego dokumentu, skoro cykl publikuje ją w publicznej historii repozytorium?
  - Answer: dokument nie niesie nazw prywatnych produktów, ścieżek do notatek ani nazw prywatnych gałęzi; zakaz czytania jest ogólny, pierwsze użycie części i krok po scaleniu stoją w osobnej notatce, której cykl nie kopiuje, a to, żeby cykl w ogóle nie publikował takich nazw, idzie osobnym zadaniem.
  - Not chosen:
    - zostaje jak jest — dokument jest kompletny i nic nie trzeba przenosić, ale nazwy i układ katalogów trafiają do publicznej historii, a każde kolejne zadanie dokłada swoje
    - czyszczenie tylko tego dokumentu — kolejne zadania dalej publikują nazwy
  - Source: Mariusz, 2026-11-01: „3” — na drogę 3 przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: ogólny zakaz chroni pomiar słabiej niż lista, a przypomnienie po scaleniu leży w innym pliku; `task-cycle/skill/SKILL.md:381-386`, `foundations` `ea4694e`.
- Pytanie 12: gdzie stoi lista na dziś — w decyzji produktu czy w regule jego wytycznych — skoro dopisanie pozycji do decyzji jest zmianą decyzji, którą WAY-30 każe zatwierdzać przed kodem?
  - Answer: w decyzji produktu stoi zasada, a lista na dziś stoi w regule jego wytycznych, w `guidelines/coding.md`, więc dopisanie pozycji nie zmienia decyzji; granica dla agenta z pytania 10 stoi w decyzji; ta odpowiedź zastępuje „decyzja produktu ma zasadę i aktualną listę” z pytania 1 i „tą samą decyzją” z podziału w Context w części dotyczącej listy.
  - Not chosen:
    - lista w decyzji, bez dodatkowego zapisu — bez zmian w wyborze z pytania 1, ale spór o zmianę decyzji zostaje i dwa cykle mogą go rozstrzygnąć różnie
    - lista w decyzji, a nowa decyzja the way zawęża WAY-30 — lista zostaje w dzienniku, a pierwszeństwo jest zapisane, ale to stały wyjątek od zasady, że decyzji nie zmienia się bez zgody człowieka
  - Source: Mariusz, 2026-11-01: „3” — na drogę 3 przedstawioną w rozmowie doprecyzowania, ze wskazanym słabym punktem: granica z pytania 10 musi stać w decyzji, a recenzent musi pilnować, czy dopisana pozycja ją szanuje; lista nie jest też w dzienniku, który przeszukuje się przy zmianie fundamentu; WAY-30, `foundations/decisions.md:761-763`, `foundations` `ea4694e`.

## Context

- Podział ustalony przez Mariusza (17.10 i 29.10.2026): wytyczne mówią, **jak** kod pisze zapis, a produkt przyjmuje tę część decyzją w swoim dzienniku albo odstępuje od niej z powodem — tak jak przy wytycznych testów (WAY-173).
- Z tego samego podziału: tą samą decyzją produkt ustala swój zakres: które identyfikatory i które zdarzenia biznesowe loguje.
- **Dokąd** idą logi, **jak długo** żyją i czy jest narzędzie do śledzenia błędów rozstrzyga krok technologii, nie wytyczne, także gdy narzędzie trzeba podpiąć w kodzie; koszt tego podpięcia krok pokazuje przy wyborze (zadanie scalone w PR https://github.com/mariusznazar/the-way/pull/65, pytanie 3).
- Wytyczne działają przy pisaniu kodu i w recenzji, nie w definicji projektu (Mariusz, 17.10 i 29.10.2026).
- Pierwszy przegląd całego kodu nie potrzebuje nowego skilla: rozszerzenie wytycznych kodu ocenia każdy plik każdego nazwanego rodzaju kodu względem reguł, które zadanie ustala, i wskazuje plik i linię, więc w produkcie z kodem nowa część od razu pokaże, gdzie kod ją łamie (`product-guidelines/coding/kinds.md:5-16`, `foundations` `ea4694e`).
- Ten przegląd nie obejmuje kodu spoza nazwanych rodzajów, na przykład pliku startowego programu, w którym zwykle stoi ostatnie miejsce zapisu.
- Audyt pokazuje, nie naprawia: kończy się statusem `do not copy`, a znalezisko może zostać odłożone z powodem (`product-guidelines/coding/task_document.md:36-38`); stary kod poprawia się dopiero wtedy, gdy zadanie produktu weźmie te znaleziska do *To do*.
- WAY-168 każe przeglądowi porównać zmianę z regułą bez niezmiennika, a te same obietnice stoją w `product-guidelines/template.md:80-81`, `product-guidelines/testing/template.md:85` i `product-guidelines/styleguide/template.md:63`; recenzent dostaje pliki wytycznych, ale sekcja „Review” skilla przeglądu wymienia je tylko przy stanach interfejsu (`task-cycle/review/SKILL.md:55-87`, `foundations` `ea4694e`).
- Wyjaśnienie reguł z To do 1, które nie wchodzi do szablonu, bo reguła nie niesie uzasadnienia (WAY-168), a uzasadnienie decyzji the way opisuje je własnymi słowami, bez nazwy produktu (WAY-27): po numerze zamówienia, id użytkownika i id żądania da się prześledzić całą historię zamówienia, akcje użytkownika w czasie i połączenia między aplikacjami; lekcja mówi o chowaniu błędów, że najpierw przestaje się ukrywać, co dzieje się w systemie, a dopiero potem naprawia przyczynę.
- Przejęcie z lekcji wiąże tylko przez decyzję, która nazywa, co przejmuje, gdzie i dlaczego (WAY-100); WAY-270 obejmuje z tej lekcji wyłącznie dwa pytania kroku technologii (`foundations/decisions.md:7960-7962`, `foundations` `ea4694e`).
- Z 18 przyjętych wierszy *Settlements to record* powstało 8 scalonych, na słowo Mariusza z 2026-11-01: „zachowujemy wszystkie i poscalaj je”.
- The-way nie ma własnego katalogu `guidelines/`; zadanie zmienia tekst szablonu i skilli oraz wpisy fundamentu, a pracę nad samym the-way prowadzi `agent-instructions/README.md`.
- Agent tego zadania, w doprecyzowaniu i w cyklu, pracuje tylko w repozytorium the way i poza tym dokumentem nie czyta notatek ani repozytoriów żadnego produktu: późniejszy krok sprawdza, czy proces sam dojdzie do ustaleń o logach produktu, a zmiana, która je zna, unieważnia ten pomiar.
- Krok po scaleniu i pierwsze użycie części stoją poza tym dokumentem; nie wykonuje ich agent cyklu.
- Pierwotne brzmienie zadania: „the way: wytyczne do konstruowania obserwowalności produktu (np. observability-guide) — co produkt loguje, w jakiej postaci, jak logi się utrzymuje; dziś krok technologii ma ustalić tylko drogę agenta do działającego produktu i technologię logów, a treści logów nic w the way nie wymaga; działa przy pisaniu kodu i w recenzji (cykl zadania), nie w definicji projektu; do zważenia: reguła the way dla każdego produktu czy decyzja każdego produktu”.

## Questions carried to cycle

- Czy decyzja produktu o tej części jest częścią decyzji przyjmującej szablon wytycznych kodu (`product-guidelines/coding/settle.md:21-22`), czy osobnym wpisem, skoro zdania wiążące decyzji mieszczą się w jednym do trzech (`elements/decisions/template.md:94`).
- Jakim angielskim słowem szablon nazywa „przepływ”, skoro słownik the way ma tylko „critical flow” w węższym znaczeniu (`foundations/glossary.md:25-27`), i „część”, skoro „part” znaczy tam część mapy produktu; znaczenie „przepływu” podaje To do 1.

## Human actions

none

## Decisions in play

Wybór: decyzje z *Scope* `product-guidelines` i `task-cycle` według „Reading the foundation”, wyszukanie słów „log”, „swallow”, „personal data” w fundamencie i w `task-cycle/`, wpisy, do których te decyzje prowadzą, na `foundations` `ea4694e`.

- WAY-168 — „A binding rule of a product's guidelines names by identifier the decision of the product's log that carries its choice and says what to do and how”; „a rule no such test can check names none, and the review of each change the rule reaches compares the change with it.” Niesie odpowiedź na pytanie 6 i To do 5.
- WAY-170 — „the review of a change that writes or changes them compares them with the template every product's guidelines share and, where the-way gives one, the template of their discipline, at the commit of the-way the product pins.” Dotyczy pytania 2.
- WAY-171 — „each rule of `## Rules` stands under a heading of its own”; „a section or a rule that a template of the-way requires and the product drops holds only `none —` followed by the product's decision that departs from it.” Tak stoją reguły części i tak wygląda odstępstwo.
- WAY-172 — „A new or changed meaning of a product's guidelines is a decision of the product's log, new or changed, and the code that uses it is made only once the human who accepts decisions (WAY-14) has approved it, in the document of the task that needs it, as WAY-30 has a change to a decision approved, or, where that document does not settle it, at a blocked draft request on whose branch the cycle proposes the decision. Using a meaning that a decision of the product's log already carries takes no approval, and neither does changing a value that keeps its meaning.” Rozstrzyga koszty dróg w pytaniu 1.
- WAY-173 — „The rules a template of a discipline of the-way carries and what the-way's skill of that discipline proposes bind a product only through a decision of the product's log adopting them, and the product departs from any of them only by a decision of its log that gives the reason.” Niesie podział z Context i brzmienie To do 5.
- WAY-174 — „The-way's skills `maintain-styleguide`, `maintain-coding-guidelines` and `maintain-testing-guidelines` put to the human every choice they settle for a product's guidelines, a choice they recommend included”. Tak skill stawia wybór zakresu produktu przed człowiekiem.
- WAY-22 — „a decision is a choice between options, with its rationale, and it binds later work until a change replaces, narrows or withdraws it”. Dlatego zdarzenia z decyzji produktu wiążą (pytanie 8).
- WAY-30 — „A change to a decision that a task needs is written into the task's plan, or into its task document where no plan is written, and approved with that plan or document by the human who accepts decisions (WAY-14) before the code that needs it is made”; „An exception written in advance into a decision's binding sentences is not a contradiction, and no exception lives only in a task document, plan or cycle record.” Dlatego lista nie stoi w decyzji (pytanie 12): dopisanie pozycji do decyzji byłoby jej zmianą.
- WAY-25 — „Where two decisions both apply and collide, the one that prevails names the other in *Relations* as `narrows`, and its binding sentences state the area where it prevails”. Dotyczy pytania 12 i pierwszeństwa zakazu danych przed regułą o przyczynie.
- WAY-167 — „those of the coding discipline stand in a file `guidelines/coding.md`, which holds the product's standing checks, the rules of the whole of its code and a table naming each other file of the discipline with when to read it”. Tam stoi ta część.
- WAY-207 — „turning a rule of the linter off for the whole product is a change of the product's decision adopting the linter's set, which the human approves as WAY-172 gives a changed meaning.” Przykład, że zmiana listy w decyzji przyjmującej idzie do człowieka (pytanie 12).
- WAY-161 — „a finding blocks when the reviewer grades it Critical or Important and has not itself marked it as outside the task's scope”. Dotyczy tego, czy naruszenie reguły blokuje zmianę (pytanie 6), i uwagi o braku części przy niezwiązanej zmianie (pytanie 2).
- WAY-169 — „A change that changes the binding part of a decision or an invariant brings every rule of the guidelines naming it in line in the same change”. Dotyczy zmiany zasady, nie pozycji listy, gdy lista nie stoi w decyzji (pytanie 12).
- WAY-268 — „A technology choice whose later settling could change how the work is cut into tasks, or that adds something the product has to run, pay for or back up, and that no decision of the foundation, no approved definition the task carries and no accepted answer of its task document settles, is a reserved choice”. Niesie granicę wyboru biblioteki (pytanie 4).
- WAY-201 — audyt, na którym stoi punkt o pierwszym przeglądzie w Context: „The audit the skill `maintain-coding-guidelines` makes of a product that has code ends with a proposed exemplar for each kind of code the product holds files of”.
- WAY-202 — „The template of the coding discipline requires three standing checks of a product's code — a linter, a formatter and an audit of dependencies”; „They bind a product from the task that writes its coding guidelines, which is complete only once it holds, for each of the three standing checks, a decision of the product's log adopting it or departing from it with the reason.” Część nie jest narzędziem, więc nie jest czwartym stałym sprawdzeniem; od kiedy wiąże — pytanie 2.
- WAY-203 — „A rule of a linter's set stands among the rules that block a change in the product's decision adopting the set, and so is checked by the invariant of the one rule of the product's coding guidelines on its linter”. Niesie odpowiedź na pytanie 6.
- WAY-208 — „the general file of its coding guidelines names each such part in *Applies to*.” Plik ogólny obejmuje więc każdą część z kodem, a reguła o identyfikatorach wyłącza linie spoza przepływu (To do 1).
- WAY-209 — „in a product with no code, the general file of its coding guidelines, with its standing checks, comes into being before the first task that writes the product's code”. Produkt bez kodu przyjmuje część przed pierwszym przepływem (pytanie 1).
- WAY-210 — „it extends what exists rather than setting a second tool beside it.” Reguła, którą sprawdza linter, idzie do lintera produktu.
- WAY-211 — „The skill researches at every extension and never at a refresh (WAY-251).” Koszt w pytaniu 2.
- WAY-213 — „the agent reads each file named whole, never excerpts of it or a review checklist in its place, while the reviewer of the whole change selects the guidelines of its own review.” Część dociera do autora i recenzenta bez zmiany wyboru plików; To do 5 dopisuje tylko porównanie.
- WAY-221 — „Binding rules and their invariants retain their force”. Dotyczy pytania 6.
- WAY-225 — „What can be derived from what the product executes — code, configuration, infrastructure as code, runtime traces — is derived, never written by hand, and what is derived describes the state. Rules are written by hand: what is allowed and what the product promises”; naruszenie: „a hand-written list of the product's endpoints kept next to the code”. Lista z pytania 1 stoi po stronie tego, co produkt obiecuje, więc nie jest spisem stanu kodu.
- WAY-251 — „An extension covers something new, and its research checks whether to use what the product already has or something else”. Niesie odpowiedź na pytanie 7.
- WAY-165 — *Rejected*: „what the product logs and in what form, in the same decision — that rule acts where code is written and reviewed, in the task cycle, not where a project settles its technology.” Zgadza się z podziałem z Context.
- WAY-270 — „lists how a human learns of a failure of the running product as a choice of its own”. Bez zmiany: narzędzie do śledzenia błędów rozstrzyga krok technologii.
- WAY-27 — „Nothing in this repository points to a source outside it that its readers cannot reach: every entry carries its whole reasoning, and what is seen only in such a source is described in the entry instead of being pointed to.” Decyzja the way opisuje więc własnymi słowami to, co przejmuje, zamiast odsyłać do źródła.
- WAY-86 — „A binding rule — a law, a contract, a licence — needs no adoption: what it requires is an environment fact, and the product is held to it until a human settles, in a decision, that the rule does not apply.” Dotyczy pytania 3.
- WAY-100 — „A method or practice borrowed from outside a product binds its way of working only through a decision that names what is adopted, where it applies, and why.” Nowa decyzja nazywa, co przejmuje z lekcji.

## Settlements to record

Candidates: 22 shown, 18 accepted — 2026-11-01

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Szablon wytycznych kodu the way wymaga osobnej części o błędach i logach, każda reguła pod własnym nagłówkiem. | decision | To do 1; Context, podział | czy część jest wymagana w szablonie, czy to przykład |
| 2 | Awaria to sytuacja, w której produkt nie zrobił tego, o co go poproszono albo co miał zrobić sam, z innego powodu niż przewidziana odmowa, także gdy zawiodła usługa z zewnątrz, a przewidziana odmowa, na przykład złe hasło, to zwykła odpowiedź i reguła jej nie dotyczy; awaria zapisuje się zawsze razem z przyczyną, z oryginalnym błędem, a nie samym napisem, raz, tam, gdzie kod ją obsługuje; każdy osobno działający program produktu ma jedno ostatnie miejsce, które zapisuje to, czego nie obsłużył żaden kod, a linia z tego miejsca może nie nieść identyfikatorów. | decision | To do 1; odpowiedzi na pytania 5 i 9 | czy logować złe hasła i każdą warstwę kodu, czy padnięcie dostawcy jest awarią i czy dopisać ostatnie miejsce do programu |
| 3 | Awarii się nie chowa: nie zamienia się w odpowiedź „wszystko w porządku” ani w pustą listę; tryb awaryjny, w którym produkt działa dalej bez jednej funkcji, wolno tylko wtedy, gdy ustali go zadanie, zapisując go jako decyzję produktu, i zawsze zostawia linię w logu; regułę tę the way przejmuje z lekcji 10xDEVS m3l5, bo przyczyny awarii, której nie widać, nie da się znaleźć. | decision | To do 1; odpowiedź na pytanie 5; Context, wiersz o lekcji | czy pusta lista po awarii jest zgodna z regułą, skąd później wiadomo, że tryb awaryjny był zamierzony, i czy decyzja nazywa, co przejmuje (WAY-100) |
| 4 | Zasada zakresu produktu stoi w jego decyzji, a lista na dziś identyfikatorów i zdarzeń, przy przyjęciu z tego, co produkt ma w kodzie albo w planie, stoi w regule jego wytycznych i jest obietnicą produktu, nie spisem stanu kodu; pozycję zgodną z zasadą agent dopisuje sam w zmianie, która ją wnosi, a człowiek widzi ją przy scalaniu; agent dopisuje sam każdy identyfikator rzeczy, a zgody człowieka wymaga wszystko, co wskazuje osobę, także e-mail, imię, telefon, adres zamieszkania i adres IP; numer użytkownika nadany w produkcie ustala człowiek przy przyjęciu listy, a dopisanie go później też wymaga zgody. | decision | odpowiedzi na pytania 1, 3, 10 i 12; To do 3 | czy każda nowa pozycja zatrzymuje cykl i czy agent może sam dopisać adres IP albo numer użytkownika |
| 5 | Zdarzenia biznesowe, które wymienia zakres produktu, zostawiają linię w logu; linia przepływu niesie identyfikatory, każdy pod tą samą nazwą w każdej linii, tak żeby szukanie znalazło całą sprawę, a linia spoza przepływu ich nie niesie; postać linii wybiera produkt w swojej decyzji. | decision | To do 1; odpowiedzi na pytania 4 i 8 | czy zdarzenie z listy może nie zostawić linii, czy nazwy mogą się różnić i czy szablon narzuca zapis z nazwanymi polami |
| 6 | W logu nie ma sekretów ani danych osobowych, a wyjątkiem od zakazu danych osobowych są identyfikatory z listy zakresu produktu; kod nie zapisuje całych obiektów ani treści żądań, co nie dotyczy samego błędu; gdy oryginalny błąd cytuje takie wartości, zakaz ma pierwszeństwo przed regułą o przyczynie i zapisuje się błąd bez nich, z jego rodzajem, kodem i miejscem w kodzie; zakaz danych osobowych jest wyborem szablonu, nie powtórzeniem prawa, więc produkt może od niego odstąpić z powodem, a prawo obowiązuje go niezależnie od tego. | decision | To do 1; odpowiedzi na pytania 3 i 10 | czy id użytkownika wolno zapisać, co ustępuje, gdy błąd niesie dane osoby, i czy produkt może odstąpić od zakazu |
| 7 | Bibliotekę, która zapisuje linię, wybiera człowiek na drodze skilla wytycznych, w zadaniu, które przyjmuje część, a krok technologii wchodzi tylko wtedy, gdy wybór jest wyborem zastrzeżonym. | decision | odpowiedź na pytanie 4 | czy agent cyklu wybiera bibliotekę sam |
| 8 | Część wchodzi do produktu z wytycznymi zwykłym rozszerzeniem, bez własnej drogi; odświeżenie, które zauważy jej brak, proponuje ją, „tak” człowieka zmienia zadanie w rozszerzenie, a „nie” jest odstępstwem z powodem. | decision | odpowiedź na pytanie 2 | czy dopisać wąską drogę bez badania i co robi odświeżenie, które zastaje wytyczne bez tej części |

## Out of scope

- Rozszerzenie wytycznych kodu konkretnego produktu o tę część.
