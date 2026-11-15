---
title: "the way: wytyczne kodu i testów samego the way (koniec stanu przejściowego WAY-328)"
status: draft
created: 2026-11-15
updated: 2026-11-15
tags: [zadanie]
related: "the project note of the process project"
---

# the way: wytyczne kodu i testów samego the way (koniec stanu przejściowego WAY-328)

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- WAY-328 zwalnia kod i testy samego the way z ogólnych wytycznych kodu i z wytycznych testów, jakie dostaje produkt, do czasu osobnych zadań, które je napiszą: „A separate task that writes the general coding guidelines of the-way's own takes the coding guidelines out of this decision, one that writes its testing guidelines takes the testing guidelines out of it, and once both are written the decision is withdrawn.”
- Takiego zadania dotąd nie było, a *Rationale* WAY-328 mówi, że odstępstwo „has no time limit”.
- Kod the way urósł od #98 z 20 299 do 33 510 linii Pythona (+65% w trzy dni, 62 pliki; przy znaczniku przeglądu 2026-11-06 — 16 857), a nowy skrypt skopiował starą konwencję wbrew późniejszej regule (`agent-instructions/agent_type_copies.py`, zob. P16 w pliku danych).
- Bez wytycznych nic nie chroni kodu i testów the way, nowy kod kopiuje stary, a recenzent nie ma reguły rozmiaru, więc każdą uwagę o strukturze kodu ocenia jako Minor (WAY-363; `foundation_check.py` urósł z 694 do 984 linii).

### To do

1. Napisać `guidelines/coding.md` z `product-guidelines/coding/template.md`, tak jak każe jego sekcja „Writing the files”: *Applies to* — dziesięć części z odpowiedzi 2; `### Linter` z decyzją i niezmiennikiem lintera (odpowiedzi 1–3); `### Formatter` i `### Dependency audit` jako `none —` z decyzjami odstępstwa (pytanie o formatowanie, odpowiedź 6); sześć reguł o awariach i logach jako `none —` z decyzją odstępstwa (odpowiedź 7); `### Size of a function and a file` z decyzją i niezmiennikiem rozmiaru (odpowiedzi 8–10); dwie dalsze reguły całego kodu z odpowiedzi 12; tabelę `## Kinds of code` z sześcioma wierszami (odpowiedź 13); pod `## Examples` 18 reguł ruffa, które zostają przykładami (odpowiedź 2).
2. Napisać sześć plików `guidelines/coding-<rodzaj>.md` — `check`, `measuring-report`, `generator`, `repository-changer`, `command-runner`, `shared-module` — z wzorcem, regułą i niezmiennikiem z odpowiedzi 13 oraz tabelą `## Files of this kind` według przydziału plików w *Context*; plik, którego wszystkie miejsca `do not copy` poprawiono przed bazą cyklu albo w tym zadaniu, stoi jako `copy`.
3. Napisać `guidelines/testing.md` z `product-guidelines/testing/template.md`, tak jak każe jego sekcja „Writing the file”: pięć poziomów (odpowiedź 14) z tabelą części (odpowiedź 15), przepisami (odpowiedź 17) i wzorcami (odpowiedź 18); źródła wartości oczekiwanych (odpowiedź 16); `## Not tested on purpose` (odpowiedź 19); `### Mutation testing` jako `none —` z decyzją odstępstwa (odpowiedź 20); `### Trust boundaries` z sześcioma nowymi niezmiennikami i tabelą autoryzacji bez wierszy (odpowiedź 21); `### AI in tests` bez decyzji o narzędziu, bo testy the way nie używają żadnego narzędzia AI.
4. Dodać ruffa 0.17.1, tak jak każe sekcja „The tools of the standing checks” szablonu kodu i odpowiedź 3: `ruff.toml` w korzeniu (`required-version = "==0.17.1"`, `target-version = "py314"`, domyślny zestaw bez preview, zatrzymujące dokładnie 389 reguł z odpowiedzi 2), `requirements-quality.in` i `requirements-quality.txt` z sumami SHA-256 każdego koła, instrukcję instalacji w sekcji „Running the tests” `README.md`. Jeśli job CI z requestu #127 stoi w bazie cyklu, dodać do niego krok instalacji z pliku wymagań; polecenie sprawdzania zostaje jedno (WAY-16).
5. Napisać test niezmiennika lintera: uruchamia przypięty ruff ze środowiska z odpowiedzi 3, znalezionego w głównym checkoucie tak, jak mówi odpowiedź 25, z `--ignore-noqa` na dziesięciu częściach, pada, gdy ruff zgłasza złamanie albo nie może ruszyć, i stoi oznaczony jako naruszony (odpowiedź 5).
6. Napisać test niezmiennika rozmiaru: liczy linie funkcji (razem z zagnieżdżonymi) i plików skryptów modułem `ast`, poza przebiegiem lintera, przy porażce wymienia każdą funkcję i plik ponad progiem z rozmiarem, i stoi oznaczony jako naruszony (odpowiedzi 8–10).
7. Napisać testy czterech reguł rodzajów z odpowiedzi 13: `generator` bez `--write` nie zmienia żadnego pliku; `repository-changer` bez `--apply` albo potwierdzenia nic nie zmienia; `command-runner` oddaje kod wyjścia dziecka bez zmian; import `shared-module` niczego nie wykonuje.
8. Dopisać do sześciu istniejących testów odmowy z odpowiedzi 21 cytowanie ich nowych niezmienników granic.
9. Każdy test z punktów 5–8 zobaczyć raz padający (WAY-08, WAY-61).
10. Przez `the-way-maintain-instruction-files` dopisać do `AGENTS.md` the way dwie linie: `guidelines/coding.md` z warunkiem zmiany kodu the way i `guidelines/testing.md` z warunkiem pisania albo zmiany testu, bez żadnego polecenia (WAY-212, WAY-16).
11. Przez `the-way-update-part-map` dodać `guidelines/**` do plików części `agent-instructions` (WAY-167), a `ruff.toml`, `requirements-quality.in` i `requirements-quality.txt` do części `repository`.
12. Przyczyna 1: lista sekcji definicji wypisana w `project-level/test_readiness_check.py`.
13. Przyczyna 2: oczekiwany blok `AGENTS.md`, lista skilli i punkt wejścia wypisane w `installation/test_install.py`.
14. Przyczyna 3: brakujące pole liczby tokenów w zapisach sesji kończy `task-cycle/cycle_stages.py` tak, jak każe WAY-344.
15. Przyczyna 4: testy z jej miejsc podają skryptom czas z ustalonej wartości zamiast prawdziwego zegara i stałych uśpień.
16. Przyczyny 5 i 23: test fundamentu w `elements/common/test_foundation_check.py` podaje kontroli bazę wprost albo sprawdza tylko to, co od bazy nie zależy, i sprawdza tylko znaleziska swoich dwóch niezmienników.
17. Przyczyna 6: test liczenia audytu z jej miejsca biegnie na repozytorium zbudowanym w katalogu tymczasowym.
18. Przyczyna 7, wycinek: git w `process-audit/test_audit_count.py` biegnie bez globalnej i systemowej konfiguracji użytkownika.
19. Przyczyna 17, wycinek: brakujące pole w `agent-instructions/skill_entry_points.py` kończy skrypt kodem 2 z nazwą pliku i pola.
20. Przyczyny 26, 27, 30 i 33: miejsca wzięte z odpowiedzi 5 w `process-audit/test_audit_count.py`, `installation/test_install.py`, `task-cycle/cycle_measures.py` i `task-cycle/cycle_stages.py` poprawione tak, jak mówi *Fix* każdej przyczyny.

### Questions to settle

- Jedno zadanie na obie dyscypliny czy dwa osobne (WAY-328 mówi o osobnym zadaniu dla wytycznych kodu i osobnym dla wytycznych testów)?
  - Answer: jedno zadanie pisze wytyczne kodu i wytyczne testów the way, a skill każdej dyscypliny prowadzi jej sprawy w tym doprecyzowaniu; odpowiedź daje fundament. Żaden z trzech powodów podziału z WAY-372 nie zachodzi: zadanie zmienia jedno repozytorium i nie czeka na nic spoza doprecyzowania.
  - Source: `foundations/decisions.md` przy `21ecb62`, WAY-247, ok. linii 6016: "One task of a product may write both its coding guidelines and its testing guidelines, the skill of each discipline leading that discipline's matters in the task's refinement."; WAY-372, ok. linii 8758–8763: "the reasons are three: a part cannot start or finish without something outside the refinement of the task, such as access the agent lacks or another task's result; the parts change different repositories (WAY-140); or a later step of the refinement offers a separate task."
- G5, #98-1. Czy pierwszy plik nowego rodzaju kodu w the way musi mieć wytyczne rodzaju z wierszem indeksu (WAY-216)?
  - Answer: odpowiedź stoi tylko w tym dokumencie, bez zdania we wpisie fundamentu. Po scaleniu tego zadania the way ma indeks rodzajów w `guidelines/coding.md`, WAY-328 zostaje wycofana i WAY-216 obowiązuje the way jak każdy produkt. Do scalenia odstępstwo WAY-328 obejmuje też wytyczne rodzaju. Pytanie w zadaniu „the way: dziennik decyzji po przeglądzie fundamentu …” odsyła tutaj.
  - Not chosen:
    - zdanie dopisane do WAY-328 w zadaniu o dzienniku decyzji — zdanie zniknie razem z WAY-328 po scaleniu tego zadania, a do tego czasu jest jeszcze jedną pozycją do recenzji
    - zdanie dopisane do `product-guidelines/reading.md` — wyjątek dla samego the way trafia do tekstu, który przypina każdy produkt; tę drogę odrzuca już *Rejected* WAY-328
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „1 a — to zadanie i tak usuwa przyczynę pytania; odesłanie w Z1 (sesja the-way-dziennik-po-przegladzie-doprec) dopisz tylko w tym dokumencie.”
- Jakie narzędzia stałej kontroli ma kod the way: linter, formater, audyt zależności?
  - Answer: punktem wyjścia jest spójność z loop2. Proponowany linter to ruff, chyba że rozpoznanie pokaże powód przeciw; bez szerokiego porównania narzędzi. Audyt zależności: odstępstwo z powodem, bo the way nie ma bibliotek zewnętrznych. Formater: osobne pytanie niżej — w loop2 ruff tylko sprawdza kod, a automatyczne formatowanie Pythona jest tam odłożone (`guidelines/coding.md` loop2, sekcja „Odłożone rodzaje i formatowanie”).
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „Mariusz nie wskazał narzędzia. Punkt wyjścia: spójność z loop2, który ma w wytycznych ruff (lint i formatowanie) i shellcheck — zaproponuj ruff, chyba że rozpoznanie pokaże powód przeciw; nie rób szerokiego porównania. […] Audyt zależności: the way nie ma bibliotek zewnętrznych — odstępstwo z podanym powodem; alerty Dependabota proponuje już #127.”

- Jakie masz preferencje co do testów the way — poziomy, miejsce plików, co test podmienia i czym?
  - Answer: wytyczne opisują stan dzisiejszy jako regułę: `unittest`, pliki testów obok skryptów w katalogu części, jedno polecenie `gate/run_tests.py`. Testy na prawdziwych plikach repozytorium są dozwolone tam, gdzie sprawdzają regułę samego repozytorium. Atrapy tylko dla zegara i tego, czego test nie może zrobić na tymczasowym repozytorium git; git i system plików są prawdziwe, w katalogu tymczasowym. Bez rozpoznania innych narzędzi.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „Mariusz nie zgłaszał preferencji co do testów („nie wiem”): wytyczne opisują stan dzisiejszy jako regułę — unittest, pliki testów obok skryptów w katalogu części, jedno polecenie gate/run_tests.py; testy na prawdziwych plikach repozytorium dozwolone tam, gdzie sprawdzają regułę samego repozytorium; atrapy tylko dla zegara i tego, czego test nie może zrobić na tymczasowym repozytorium git (git i system plików — prawdziwe, w katalogu tymczasowym).”
- Czy kod the way dostaje automatyczne formatowanie?
  - Answer: nie — formatowanie odłożone jak w loop2, odstępstwo z powodem: w kolejce the way stoi kilkanaście zadań, których dokumenty wskazują miejsca w plikach `.py` liniami, a przeformatowanie 61 plików przesunęłoby je i dało konflikt każdej otwartej gałęzi. Formater wchodzi kiedyś razem dla the way i loop2, osobną decyzją; to droga na później, zapisana w odstępstwie, bez zadania.
  - Not chosen:
    - ruff format z jednym przeformatowaniem całego kodu w tym zadaniu — jeden commit w 61 plikach, `git blame` wskazuje na niego, konflikty w każdej gałęzi otwartej w chwili scalenia; zysk: koniec sporów o układ kodu
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „1 b — formatowanie odłożone jak w loop2, odstępstwo z powodem: spójność z loop2 była punktem wyjścia Mariusza, w kolejce the way stoi kilkanaście zadań, których dokumenty wskazują miejsca w plikach .py liniami, a przeformatowanie 61 plików przesunęłoby je i dało konflikt każdej otwartej gałęzi; formater wprowadzić razem dla obu produktów osobną decyzją (zapisz to w Rejected/odstępstwie jako drogę na później, bez zakładania zadania).”
- Źródło odpowiedzi na pytania 1–24 niżej, o ile pytanie nie mówi inaczej: doradca dnia w imieniu Mariusza, 2026-11-15, odpowiedź na decyzje pokazane w `.runs/refine_wytyczne_decyzje_do_odpowiedzi.md` repozytorium the way: „1 a, 2 a, 3 a, 4 a, 5 a, 6 a (Twoje brzmienie), 7 a, 8 b, 9 a, 10 a, 11 a, 12 c, 13 a, 14 a, 15 przyjmuję podział jak w pliku, 16 a, 17 przyjmuję, 18 a, 20 a, 21 a, 22 a, 23 a, 24 a.” Decyzje przeszły wcześniej krytykę świeżego agenta (`.runs/refine_wytyczne_krytyka_zestawu.md`, rozstrzygnięcie autora w `.runs/refine_wytyczne_krytyka_rozstrzygniecia.md`).
- 1. Czy kod the way dostaje linter — narzędzie, które czyta każdy plik Pythona i zatrzymuje zmianę wnoszącą znany rodzaj błędu albo przestarzały zapis?
  - Answer: tak — ruff, jak w loop2. To pierwsza zależność the way spoza samego Pythona: musi być zainstalowany wszędzie, gdzie działa bramka, a bez niego bramka jest czerwona.
  - Not chosen:
    - odstępstwo od lintera z powodem — zero kosztu dziś, nic nie zatrzymuje powrotu błędów, które próbny przebieg znalazł, ani nowych
  - Source: „1 a”.
- 2. Które reguły ruffa zatrzymują zmianę?
  - Answer: ruff 0.17.1, pełny domyślny zestaw tej wersji bez preview (407 reguł), `target-version = "py314"`, czyta wszystkie części z kodem Pythona: elements-common, part-map, relation-model, project-level, task-cycle, gate, agent-instructions, instruction-files, installation, process-audit, testy też. Zatrzymuje 389 reguł; 18 reguł, które w próbnym przebiegu oznaczyły choć raz kod niewart zmiany, stoi w przykładach: UP031, ISC004, PLW1510, RUF100, FURB167, FLY002, I001, B023, UP017, SIM117, UP012, RUF015, SIM102, C419, RUF012, SIM114, SIM905, SIM115. Komentarz wyłączający regułę nie działa (`--ignore-noqa` w teście niezmiennika). Błąd jednego pliku poprawia się w tym pliku; wyłączenie reguły dla całego the way to zmiana decyzji, którą zatwierdza Mariusz (WAY-203, WAY-204).
  - Not chosen:
    - podział loop2 1:1 (D-30, 14 przykładów) — zatrzymywałby 9 reguł, które tu oznaczyły dobry kod (m.in. B023 10 zgłoszeń, FLY002 15, UP017 7), i przepuszczał RUF059, którego 17 zgłoszeń było wartych poprawki
  - Source: „2 a”.
- 3. Jak przypiąć wersję ruffa, żeby na każdej maszynie sprawdzał to samo?
  - Answer: jak w loop2: `ruff.toml` w korzeniu z `required-version = "==0.17.1"` (ruff odmawia pracy w innej wersji), plik wymagań narzędzi jakości (`.in` z `ruff==0.17.1` i `.txt` z sumami SHA-256 każdego koła, tylko koła), instalacja do lokalnego środowiska w `.runs/` według instrukcji w README, test niezmiennika uruchamia ruffa z tego środowiska; w CI dochodzi tylko krok instalacji, polecenie sprawdzania zostaje jedno (WAY-16); Dependabot widzi ruffa w pliku wymagań. Wzór: `ruff.toml`, `requirements-quality.in`, `requirements-quality.txt` i README repozytorium loop2.
  - Not chosen:
    - tylko blokada wersji w `ruff.toml` — jeden plik mniej, bez sum kontrolnych i bez alertów Dependabota
  - Source: „3 a”.
- 4. Czy test lintera mieści się w WAY-38 i niezmienniku `script-subprocesses`?
  - Answer: zadanie dopisuje do WAY-38 i do `script-subprocesses` zdanie, że testy stałych kontroli uruchamiają przypięte narzędzie ze środowiska zadeklarowanego w repozytorium.
  - Not chosen:
    - uznanie pliku wymagań za zadeklarowane polecenie bez zmiany tekstu — zero zmian fundamentu, ale kolejny agent może ten odczyt zakwestionować i zatrzymać cykl
  - Source: „4 a”.
- 5. Co z 37 miejscami w 19 plikach, które dziś łamią reguły zatrzymujące?
  - Answer: niezmiennik lintera oznaczony jako naruszony (WAY-205, WAY-51); zadanie poprawia tylko 17 miejsc w czterech plikach, które i tak zmienia: `task-cycle/cycle_stages.py`, `task-cycle/cycle_measures.py`, `installation/test_install.py`, `process-audit/test_audit_count.py` (przyczyny 26, 27, 30 i 33 listy audytu). Słaby punkt: do sprzątnięcia reszty żaden test nie pokaże zgłoszenia wracającego do sprzątniętego pliku ani nowego pliku — tylko przegląd.
  - Not chosen:
    - poprawa wszystkich 37 — wbrew WAY-205 („the task that brings the linter cleans every file of the product” w *violates*), a część poprawek RUF059 zmienia zachowanie, np. powód odrzucenia w liczeniu audytu
    - oznaczenie bez żadnej poprawki — wzorzec raportu pomiarowego zostaje z dwoma błędami, które skopiuje każdy nowy plik rodzaju
  - Source: „5 a”.
- 6. Jakim powodem stoi odstępstwo od audytu zależności, skoro the way zadeklaruje ruffa?
  - Answer: „kod the way nie importuje niczego spoza biblioteki standardowej; jedyną zadeklarowaną zależnością jest linter w wersji przypiętej decyzją” — przeformułowanie powodu z odpowiedzi o narzędziach stałej kontroli, który po dodaniu ruffa przestałby być prawdziwy.
  - Not chosen:
    - powód bez zmiany („the way nie ma bibliotek zewnętrznych”) — przestaje być prawdziwy w chwili scalenia
  - Source: „6 a (Twoje brzmienie)”.
- 7. Czy kod the way przyjmuje reguły o awariach i logach?
  - Answer: nie — jedna decyzja, osobna od decyzji przyjmującej szablon kodu, odstępuje od wszystkich sześciu (droga 4 sekcji „Departing from the rules on failures and logs”): skrypty the way nie piszą logów, wynik wypisują na konsolę, a o awarii mówią kodem wyjścia i linią `Error:`; brakujące pole czytanego pliku obejmuje WAY-344. Każdy z sześciu nagłówków ma tylko `none — <WAY-NN>`. Słaby punkt: zasada „nie udawaj, że poszło dobrze” nie stoi w wytycznych jako reguła.
  - Not chosen:
    - przyjęcie samego `### Hiding a failure` w brzmieniu szablonu i odstępstwo od pięciu — reguła mówi o linii w logach, których the way nie ma
  - Source: „7 a”.
- 8. Jaki próg rozmiaru funkcji i pliku?
  - Answer: funkcja 80 linii, plik 1000 linii. Rozmiar funkcji to liczba jej linii razem z funkcjami w niej zagnieżdżonymi, rozmiar pliku to liczba jego linii — jak liczył próbny przebieg (`.runs/coding/sizes_count.py`). Liczy osobny test w zestawie, oparty na `ast` z biblioteki standardowej, biegnący poza przebiegiem lintera (ruff nie ma reguły liczby linii); przy porażce wymienia każdą funkcję i plik ponad progiem z rozmiarem. Przy `21ecb62` ponad progiem stoi 11 funkcji i 2 pliki skryptów (`process-audit/audit_count.py` 2991, `task-cycle/cycle_stages.py` 1009). Koszt: zadania z kolejki, które zmieniają `audit_count.py` albo `cycle_stages.py` („audyt: sprzeczność po kodzie”, „dwa znaczenia słowa gate”, „mapa części: zależności, linia zadania”, „skrypty: brakujące pole”), zaczną od wyniesienia części (WAY-365), a `audit_count.py` jedno wyniesienie pod próg nie sprowadzi. Słabe punkty: liczba linii nic nie mówi o tym, czy funkcja jest dobrze zrobiona, a funkcję można dzielić tylko po to, by zmieściła się pod progiem.
  - Not chosen:
    - funkcja 60 / plik 800 — ponad progiem 19 funkcji i 4 pliki
    - funkcja 100 / plik 1500 — ponad progiem 7 funkcji i 1 plik
    - odstępstwo od reguły — każda uwaga recenzenta o strukturze kodu zostaje drobna (WAY-363)
  - Source: „8 b”.
- 9. Czy reguła rozmiaru obejmuje testy?
  - Answer: nie — tylko skrypty; zasady testów stoją w wytycznych testów (WAY-231). Pliki testów rosną dalej (`process-audit/test_audit_count.py` ma 3185 linii).
  - Not chosen:
    - także testy, osobną regułą wytycznych testów — 5 plików testów ponad 1000 linii i kolejne niezmienniki oznaczone jako naruszone
  - Source: „9 a”.
- 10. Które funkcje i pliki zostają w całości ponad progiem jako wyjątki?
  - Answer: żadne. Niezmiennik rozmiaru stoi oznaczony jako naruszony, dopóki 11 funkcji i 2 pliki nie zostaną podzielone (WAY-51); do tego czasu tylko przegląd pilnuje, by sprzątnięty albo nowy plik nie przerósł.
  - Not chosen:
    - wyjątki wskazane przez Mariusza po jednym, z powodem
  - Source: „10 a”.
- 11. Czy cykl tego zadania wynosi części przed własnymi poprawkami w plikach ponad progiem (`task-cycle/cycle_stages.py`, `process-audit/test_audit_count.py`, `elements/common/test_foundation_check.py`)?
  - Answer: nie — reguła rozmiaru obowiązuje po scaleniu tego zadania, a jej niezmiennik i tak wchodzi oznaczony jako naruszony.
  - Not chosen:
    - tak — zadanie rośnie o podział `cycle_stages.py`
  - Source: „11 a”.
- 12. Jakie reguły obowiązują cały kod the way?
  - Answer: dwie reguły bez niezmiennika, pilnowane przez przegląd każdej zmiany: każdy skrypt zaczyna się opisem, jak go uruchomić (`python -B …`) i co znaczą jego kody wyjścia, i ma jedno stałe miejsce startu zwracające kod wyjścia (dziś łamie ją 8 plików, m.in. 7 bez `-> int` i `installation/install.py` bez `main`); brakujące pole czytanego pliku obsługuje się tak, jak każe WAY-344 — reguła wskazuje WAY-344 i nie powtarza jej treści.
  - Not chosen:
    - test i poprawka 8 plików w tym zadaniu — siedem zmian w jednej linii plus przebudowa startu `installation/install.py`
    - test z niezmiennikiem oznaczonym jako naruszony
  - Source: „12 c”.
- 13. Jakie rodzaje kodu ma the way, które pliki są ich wzorcami i co z nich sprawdza test?
  - Answer: sześć rodzajów, każdy z wzorcem i plikiem `guidelines/coding-<rodzaj>.md`:
    - `check` — wzorzec `task-cycle/tracked_private_paths_check.py`; bez reguły sprawdzanej testem;
    - `measuring-report` — wzorzec `task-cycle/cycle_measures.py` po poprawce jego dwóch miejsc lintera; bez reguły sprawdzanej testem;
    - `generator` — wzorzec `agent-instructions/skill_entry_points.py` po poprawce kodu wyjścia przy brakującym polu; reguła: bez `--write` nie zmienia żadnego pliku;
    - `repository-changer` — wzorzec `task-cycle/remove_merged_worktrees.py`; reguła: bez `--apply` albo potwierdzenia nic nie zmienia;
    - `command-runner` — wzorzec `task-cycle/gate_times.py`; reguła: skrypt owijający jedno polecenie oddaje jego kod wyjścia bez zmian;
    - `shared-module` — wzorzec `relation-model/fingerprint.py`; reguła: import niczego nie wykonuje.
    Każda reguła rodzaju ma niezmiennik z testem (WAY-198). Statusy plików jak w `.runs/coding/kinds_audit.md`; osiem miejsc w siedmiu plikach ma status `do not copy`, wszystkie wobec WAY-344.
  - Not chosen:
    - `task-cycle/private_paths_check.py` jako wzorzec rodzaju `check` — lepiej pokazuje odczyt argumentów, nie pokazuje sprawdzania brakującego pola
  - Source: „13 a”.
- 14. Jakie poziomy mają testy the way?
  - Answer: pięć: unit; test plików (pliki w katalogu tymczasowym i proces Pythona, bez gita); test gita (repozytoria git zbudowane w katalogu tymczasowym); test repozytorium (prawdziwy checkout the way, sprawdza właściwość samego repozytorium); e2e w znaczeniu dziedziny — cała ścieżka sesji przez kilka skryptów. Trzy hasła słownika the way (WAY-240) dla testu plików, testu gita i testu repozytorium, a słownik the way dostaje też każdy produkt, który przypina the way.
  - Not chosen:
    - unit, integracyjny (pliki i git razem), e2e i test repozytorium — dwa hasła, znika rozróżnienie, czy test potrzebuje gita
  - Source: „14 a”.
- 15. Gdzie leży złożoność każdej części: w obliczeniach czy w połączeniach?
  - Answer: w obliczeniach — elements-common, part-map, relation-model, project-level, task-cycle, instruction-files, process-audit; w połączeniach — gate, agent-instructions, installation. Wpływa tylko na to, gdzie kiedyś działałoby narzędzie testów mutacyjnych.
  - Source: „15 przyjmuję podział jak w pliku”.
- 16. Skąd test bierze wartość oczekiwaną (WAY-232)?
  - Answer: z fundamentu the way, z jego słownika, z szablonów i skilli, które skrypt wykonuje, oraz z opisu na początku skryptu (kody wyjścia, format wyniku). Słaby punkt: autor zmienia kod i opis w jednym commicie, a test idzie za oboma.
  - Not chosen:
    - bez opisu skryptu — kody wyjścia większości skryptów nie stoją w żadnym innym dokumencie
  - Source: „16 a”.
- 17. Co wiąże w przepisach poziomów?
  - Answer: pliki `test_*.py` w katalogu części, obok skryptu, który testują, pod `unittest`; atrapy tylko zegara i tego, czego test nie zrobi na tymczasowym repozytorium git — git i system plików prawdziwe, w katalogu tymczasowym, a na poziomie testu repozytorium prawdziwy checkout; wartości wypisane w teście ze źródłem w komentarzu; czas podawany z zewnątrz (jak `--today`), bez stałych przerw; *Command*: `python -B gate/run_tests.py <katalog>` — bramka zawęża tylko do katalogu; odstępstwo od pola *Time limit*, bo the way nie ma pliku z limitem, a limity stoją przy samych wywołaniach; każdy poziom dostaje *Purpose* — do czego służy i kiedy go nie używać.
  - Source: „17 przyjmuję”.
- 18. Które testy są wzorcami poziomów (WAY-242)?
  - Answer: unit — `relation-model/test_fingerprint.py::Fingerprint.test_a_tab_is_kept`; test plików — `task-cycle/test_cycle_measures.py::RewriteEdgesTest.test_a_rewrite_of_2000_tokens_is_not_counted`; test gita — `project-level/test_plan_state_invariant.py::PlanStateEvidence.test_fresh_remote_record_composes_both_transitions`; test repozytorium — `elements/common/test_elements_pending_marker.py::TrackedFilesUnderElementsTest.test_no_tracked_file_under_elements_holds_the_pending_marker`; e2e — `process-audit/test_audit_count.py::Cost.test_the_stage_report_cycle_stages_writes_gives_the_share`. Zadanie poprawia w `process-audit/test_audit_count.py` uruchamianie gita pod globalną konfiguracją użytkownika (wycinek przyczyny 7), żeby kopie wzorca e2e nie przejęły tej wady.
  - Not chosen:
    - zgoda, że kopie wzorca e2e przejmą wadę
  - Source: „18 a”.
- 19. Czy jest coś, czego the way świadomie nie testuje?
  - Answer: tak — the way świadomie nie testuje automatycznie tego, co agent faktycznie robi, idąc za skillem; testy sprawdzają formę i spójność tekstów skilli. Zachowanie agentów sprawdzają przegląd cykli przez człowieka przy scaleniu i audyt procesu (process-audit), nie bramka. Powód: test zachowania wymagałby uruchamiania modelu w każdej bramce — koszt tokenów i wynik niedeterministyczny. Warunek powrotu: powtarzający się błąd zachowania agenta, którego audyt nie łapie przed scaleniem.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „19 (słowami): Tak — the way świadomie nie testuje automatycznie tego, co agent faktycznie robi, idąc za skillem; testy sprawdzają formę i spójność tekstów skilli. Zachowanie agentów sprawdzają przegląd cykli przez człowieka przy scaleniu i audyt procesu (process-audit), nie bramka. Powód: test zachowania wymagałby uruchamiania modelu w każdej bramce — koszt tokenów i wynik niedeterministyczny. Warunek powrotu: powtarzający się błąd zachowania agenta, którego audyt nie łapie przed scaleniem.”
- 20. Czy the way przyjmuje narzędzie testów mutacyjnych — takie, które wprowadza do kodu drobne błędy i sprawdza, czy test je złapie?
  - Answer: nie — odstępstwo od reguły testów mutacyjnych (WAY-252): recenzent sprawdza to w głowie (WAY-253), a narzędzie byłoby kolejną zależnością uruchamianą przy każdej zmianie. Warunek powrotu: błąd po scaleniu w części obliczeniowej, który przepuściła brakująca asercja.
  - Not chosen:
    - przyjęcie narzędzia dla części obliczeniowych — osobny wybór technologii, z kosztem konfiguracji
  - Source: „20 a”.
- 21. Jakie niezmienniki dostają granice zaufania the way (WAY-235)?
  - Answer: sześć nowych niezmienników odmowy, każdy wywiedziony z WAY-48 · WAY-235 jak `installation-paths-through-links` i cytujący istniejący test odmowy: `project-level/readiness_check.py` — `project-level/test_readiness_check.py:571`; `task-cycle/cycle_stages.py` — `task-cycle/test_cycle_stages.py:707`; `task-cycle/cycle_measures.py` — `task-cycle/test_cycle_measures.py:466`; `task-cycle/gate_times.py` — `task-cycle/test_gate_times.py:298`; `process-audit/audit_count.py` — `process-audit/test_audit_count.py:468`; `instruction-files/check_instructions.py` — `instruction-files/test_check_instructions.py:759`. Oczekiwaną odmowę mówi zdanie niezmiennika; tabela autoryzacji nie ma wierszy, bo the way nie ma użytkowników ani uprawnień. Słabe punkty: test granicy `gate_times.py` jest pewny dopiero po poprawce przyczyny 4; test `check_instructions.py` pomija się na maszynie, która nie robi linków symbolicznych; reguła jest tak dobra jak mapa części, która nazywa granice.
  - Not chosen:
    - osobna nowa decyzja o odmowach dla spreparowanego wejścia — dodatkowy wpis, który powtarza niezmienniki
  - Source: „21 a”.
- 22. Które przyczyny listy audytu zadanie bierze?
  - Answer: czołówkę 1–5 oraz 6, 23, wycinek 17 (`agent-instructions/skill_entry_points.py:114`, warunek wzorca generatora) i 17 miejsc lintera z odpowiedzi 5 (przyczyny 26, 27, 30, 33 w czterech plikach); resztę odkłada razem. Żadna przyczyna nie waży `grave`, więc nie ma pytania o zadanie w backlogu.
  - Not chosen:
    - tylko czołówka 1–5
  - Source: „22 a”.
- 23. Gdzie stoją wytyczne the way i co z tego wynika?
  - Answer: katalog `guidelines/` w korzeniu the way: zmiana WAY-09, `guidelines/**` do części `agent-instructions` (WAY-167), wycofanie WAY-328, poprawka miejsc, które powołują się na WAY-328 — przykładu w *Verification* WAY-363 („a script of this repository, which has no coding guidelines (WAY-328)”), zdania *Rationale* WAY-344 („The-way departs from the guidelines of a product for its own code (WAY-328)”) i pozycji *Rejected* WAY-344 („the rule as an exception written into WAY-328”) — oraz dwie linie wskaźników w `AGENTS.md` the way (WAY-212, WAY-16); `ruff.toml` i pliki wymagań do części `repository`. Katalog trafia też do `.the-way/` w produktach, a czytanie wytycznych szuka ich w korzeniu produktu.
  - Not chosen:
    - bez katalogu — wytyczne nie mają gdzie stać, WAY-328 zostaje
  - Source: „23 a”.
- 24. Kiedy ruff 0.17.1 ma być zainstalowany na komputerze Mariusza?
  - Answer: przed cyklem — bramka cyklu bez ruffa jest czerwona; to czynność człowieka.
  - Not chosen:
    - w trakcie cyklu — pierwsze uruchomienia bramki w cyklu kończą się na czerwono
  - Source: „24 a”; doradca dnia w imieniu Mariusza, 2026-11-15: „24: instalacja ruffa na komputerze Mariusza to czynność człowieka — zapisz ją w Human actions jako „before the cycle, not done”; przekażę ją Mariuszowi i odhaczę po zrobieniu.”
- 25. Skąd test lintera bierze ruffa, gdy bramka biegnie w katalogu roboczym cyklu albo recenzenta, w którym `.runs/` (pomijany przez gita) nie istnieje?
  - Answer: test szuka środowiska `.runs/quality-venv` w głównym checkoucie repozytorium, przez wspólny katalog gita (`git rev-parse --git-common-dir`); jedna instalacja obsługuje każdy katalog roboczy, recenzenta też, a w CI ścieżka wychodzi ta sama. Niezgodną wersję widać od razu, bo ruff z `required-version` odmawia pracy. Słaby punkt: katalog roboczy, który podnosi wersję ruffa, ma czerwoną bramkę do przeinstalowania ruffa w głównym checkoucie.
  - Not chosen:
    - własne środowisko albo dowiązanie w każdym katalogu roboczym, zakładane przez cykl — zmiana skilli cyklu, które działają też w produktach, albo ręczny krok przy każdym katalogu, także recenzenta (stan dzisiejszy loop2)
    - ruff zainstalowany dla całego użytkownika i brany z PATH — odejście od odpowiedzi 3, bez sprawdzania sum kontrolnych przy uruchomieniu
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „1 a — test szuka środowiska w głównym checkoucie przez git rev-parse --git-common-dir; powód: jedna instalacja obsługuje każdy katalog roboczy i recenzenta, a niezgodna wersja widać od razu przez required-version; czynność człowieka zostaje: instalacja ruffa 0.17.1 do .runs/quality-venv w <main checkout>.”
- 26. Czy the way przyjmuje szablon wytycznych kodu i szablon wytycznych testów (WAY-173)?
  - Answer: tak — dwie decyzje przyjmujące, każda z odstępstwami już ustalonymi: w kodzie formatowanie, audyt zależności i sześć reguł o awariach i logach (te ostatnie osobną decyzją, odpowiedź 7); w testach testy mutacyjne (odpowiedź 20) i pole *Time limit* (odpowiedź 17). Reguła `### AI in tests` wchodzi bez decyzji o narzędziu, bo testy the way nie używają żadnego narzędzia AI.
  - Not chosen:
    - bez decyzji przyjmujących — reguły wytycznych nie mają decyzji, na którą się powołują, i nic nie wiążą (WAY-173)
  - Source: doradca dnia w imieniu Mariusza, 2026-11-15: „2 a — dwie decyzje przyjmujące szablony, z ustalonymi odstępstwami.”; *To do* przyjęte tamże: „3 tak — przyjmuję To do z oboma wnioskami (a i b).”

## Context

- Mariusz zdecydował w przeglądzie fundamentu 2026-11-14: założyć zadanie — „to istotne”.
- Plik danych przeglądu: `a file of the author's private notes` — sekcja „Fundament” → „Decyzje opisujące stan przejściowy”, punkt 5 (WAY-328), oraz tabela „Słabe punkty” (wiersze WAY-328 i WAY-363).
- Sprawdzony commit przeglądu: `21ecb627f885de438e2209d7ff5c137b1e1b9d83` (gałąź `foundations`); liczby linii w pliku danych odnoszą się do niego.
- Stan przy `21ecb62` (rozpoznanie skilli wytycznych): kod the way to wyłącznie Python 3.14 z samą biblioteką standardową — 24 skrypty i 38 plików testów `unittest` w 10 częściach mapy.
- Repozytorium nie ma lintera, formatera, audytu zależności ani katalogu `guidelines/`, a skrypty nie piszą logów, tylko wypisują wynik na konsolę.
- Próbny przebieg ruffa 0.17.1 (domyślny zestaw bez preview, Python 3.14) na `21ecb62`, w osobnym checkoucie i tymczasowym środowisku: wynik i oceny świeżego agenta w `.runs/coding/` repozytorium the way (`ruff_check_0.17.1.json`, `ruff_statistics.txt`, `ruff_verdicts.md`, `blocking_files.txt`, `ruff_format_check.txt`); liczenie rozmiarów w `.runs/coding/sizes.md` (skrypt `sizes_count.py` obok).
- Przegląd rodzajów kodu (świeży agent): `.runs/coding/kinds_audit.md` repozytorium the way; przegląd testów według poziomów i granic zaufania: `.runs/testing/tests_audit.md`.
- Przydział 24 skryptów do rodzajów przy `21ecb62` (z `.runs/coding/kinds_audit.md`); plik bez dopisku ma status `copy`:
  - `check`: `task-cycle/tracked_private_paths_check.py` (wzorzec), `task-cycle/image_files_check.py`, `task-cycle/private_paths_check.py`, `task-cycle/remarks_check.py`, `task-cycle/request_check.py` (`do not copy` — ok. l. 397, przyczyna 16), `project-level/readiness_check.py`, `project-level/plan_check.py`, `elements/common/foundation_check.py`, `instruction-files/check_instructions.py`;
  - `measuring-report`: `task-cycle/cycle_measures.py` (wzorzec), `task-cycle/change_file_sizes.py`, `task-cycle/review_reminder.py`, `process-audit/audit_count.py`, `task-cycle/slice_size.py` (`do not copy` — ok. l. 162, przyczyna 16), `task-cycle/cycle_stages.py` (`do not copy` — ok. l. 403 i 557, przyczyna 3), `project-level/plan_state.py` (`do not copy` — ok. l. 478, przyczyna 17);
  - `generator`: `agent-instructions/skill_entry_points.py` (wzorzec po poprawce, ok. l. 114, przyczyna 17), `agent-instructions/agent_type_copies.py` (`do not copy` — ok. l. 77, przyczyna 17);
  - `repository-changer`: `task-cycle/remove_merged_worktrees.py` (wzorzec), `elements/common/migrate_foundation.py`, `installation/install.py` (`do not copy` — ok. l. 136, przyczyna 17);
  - `command-runner`: `task-cycle/gate_times.py` (wzorzec), `gate/run_tests.py`;
  - `shared-module`: `relation-model/fingerprint.py` (wzorzec).
- Próbny przebieg ruffa: 649 zgłoszeń w 55 plikach od 26 reguł (`.runs/coding/ruff_statistics.txt`). Reguły, których choć jedno zgłoszenie świeży agent ocenił jako niewarte zmiany (przykłady): UP031 310, ISC004 150, PLW1510 44, RUF100 26, FURB167 21, FLY002 15, I001 13, B023 10, UP017 7, SIM117 4, UP012 3, SIM102 2, RUF015 2, C419 1, RUF012 1, SIM114 1, SIM115 1, SIM905 1. Reguły z samymi zgłoszeniami wartymi zmiany (zatrzymują): RUF059 17, UP022 8, PERF102 3, FURB162 2, FURB188 2, UP037 2, PIE810 1, PLR1704 1, RUF007 1 — razem 37 miejsc w 19 plikach. Oceny z uzasadnieniem: `.runs/coding/ruff_verdicts.md`.
- Granice zaufania z mapy części i ich testy odmowy (`.runs/testing/tests_audit.md`, „Trust boundaries”): każda z dziewięciu ma test odmowy. Trzy mają już niezmiennik — `project-level/plan_check.py` (`project-plan-form`), `project-level/plan_state.py` (`project-plan-state-evidence`), `installation/install.py` (`installation-paths-through-links`, którego testy pomijają się na maszynie bez linków symbolicznych i junction); sześć bez niezmiennika wymienia odpowiedź 21.
- Czego przeglądy i próbne przebiegi nie widziały: przegląd rodzajów czytał tylko 24 skrypty, bez testów; próbny przebieg ruffa nie sprawdzał reguł preview ani formatowania poza liczbą plików do przepisania; poza czołówką i przyczynami 11 i 18 żadnej przyczyny nikt nie sprawdził w kodzie; zapisów sesji Codexa (przyczyna 3) nie mierzono; wszystkie liczby stoją przy `21ecb62`.
- `Defect introduced by: none`: zadanie wypełnia lukę, którą WAY-328 nazwała i przyjęła, a nie usuwa wady wobec wcześniejszego zadania.
- Fakt środowiska składu domyślnego zestawu ruffa 0.17.1 cytuje, jak `ruff-default-rules` w loop2, plik źródłowy przy tagu: `https://raw.githubusercontent.com/astral-sh/ruff/0.17.1/crates/ruff_linter/src/settings/mod.rs` § `DEFAULT_SELECTORS` (407 reguł); 37 miejsc łamiących reguły zatrzymujące: `.runs/coding/blocking_files.txt`.
- Rozmiary liczone przy `21ecb62`; zadanie „the way: skrypty po przeglądzie fundamentu — brakujące pole…”, scalone przed tym, przesunie liczby funkcji i plików ponad progiem.
- The audit's list; places 1 to 5 are its top. Kolejność w wadze `heavy` po krytyce: dawne 2 i 3 przed dawnym 1, bo usuwają więcej przy tym samym zasięgu; dawna przyczyna 27 rozbita na przyczyny 27–34, po jednej na regułę lintera, bo żadna jedna poprawka nie usuwa ich razem. Sprawdzenie obniżyło dwie przyczyny spoza czołówki (11 i 18); żadnej nie wycofało.
- 1 — `heavy` — testy kontroli gotowości definicji biorą listę sekcji z kodu, który sprawdzają, więc sekcja usunięta z kodu znika też z danych testu i kontrola przepuszcza definicję bez niej, a ok. 70 testów dalej przechodzi — stoi pierwsza, bo jedna poprawka zdejmuje ślepy punkt największej liczby testów
  - Places: `project-level/test_readiness_check.py:92` (pomocnik `definition()`, `order = order or list(readiness_check.SECTIONS[:-1])`)
  - Fix: lista sekcji definicji wypisana w teście
  - Removes: 1 miejsce, ślepy punkt ok. 70 testów
  - Reaches: `one file`
  - Checked: przeczytany pomocnik i krotka `SECTIONS` w `project-level/readiness_check.py:48` — dane testu idą za krotką
  - Taken: odpowiedź 22
- 2 — `heavy` — testy instalatora oczekują bloku `AGENTS.md` i punktu wejścia skilla wytworzonych przez sam instalator, więc przechodzą, cokolwiek instalator wpisze produktowi, a agenci produktu dostaliby błędne wskazówki bez czerwonego testu
  - Places: `installation/test_install.py:20` (`NAMES` z `install.SKILLS`), `:21` (`BLOCK = install.agents_block()`), `:447`, `:459` (`install.skill_wrapper(...)` jako oczekiwany tekst)
  - Fix: oczekiwany blok, lista skilli i punkt wejścia wypisane w teście
  - Removes: 4 miejsca
  - Reaches: `one file`
  - Checked: przeczytane linie 15–24 i 452–462; `test_installed_guidance.py` sprawdza tylko import `@AGENTS.md` w `CLAUDE.md`, nie treść bloku
  - Taken: odpowiedź 22
- 3 — `heavy` — gdy zapis sesji Claude Code albo Codexa nie ma liczby tokenów pod oczekiwaną nazwą, raport etapów liczy ją jako zero bez słowa, więc koszt cyklu w audycie wychodzi zaniżony i nikt tego nie widzi
  - Places: `task-cycle/cycle_stages.py:403` (funkcja `read_codex_agent`, rekordy Codexa, `usage.get("input_tokens", 0)` ok. l. 437–439), `task-cycle/cycle_stages.py:557` (funkcja `read_claude_agent`, `usage = message.get("usage") or {}`, odpowiedzi Claude Code, ok. l. 575–579)
  - Fix: brakujące pole liczby tokenów kończy skrypt tak, jak każe WAY-344, nazwą pliku i pola
  - Removes: 2 miejsca
  - Reaches: `one file`
  - Checked: przeczytane obie funkcje przy `21ecb62` — każdy brakujący klucz `usage` daje 0, bez noty agenta i bez kodu błędu; krytyk zmierzył 120 najnowszych zapisów sesji Claude Code repozytorium the way (19 414 odpowiedzi) — żadnej bez `usage` ani bez któregoś klucza tokenów, więc to zabezpieczenie przed przyszłą zmianą formatu; zapisów Codexa nie mierzono
  - Taken: odpowiedź 22
- 4 — `heavy` — testy zależne od prawdziwego zegara i obciążenia maszyny potrafią zaczerwienić bramkę na niezmienionym kodzie, a autor zmiany nie ma jak dojść, czemu — stoi czwarta mimo większego zasięgu, bo czerwona bramka bez przyczyny kosztuje każdy cykl, który na nią trafi
  - Places: `task-cycle/test_gate_times.py:32` (prawdziwy zegar w `now_ms`, także 262, 278, 298, 324, 346), `task-cycle/test_gate_times.py:146` (test `test_directories_that_end_out_of_the_order_of_their_names_each_get_their_own_time`, `time.sleep(1)`), `gate/test_run_tests.py:392` (test `test_each_report_stands_whole_under_its_own_line_in_the_order_directories_end`, `pause=2.0`), `gate/test_run_tests.py:474` (test `test_the_option_names_the_slowest_tests_with_their_time`), `process-audit/test_audit_count.py:182` (pomocnik `run_count`, limit czasu ściennego 120 s i 60 s), `process-audit/test_audit_count.py:2378` (test `test_the_same_input_gives_the_same_bytes_in_both_files`, dwa przebiegi bez `--today` po obu stronach północy)
  - Fix: testy podają skryptom czas z ustalonej wartości (jak `--today`) zamiast prawdziwego zegara i stałych uśpień
  - Removes: 6 znalezisk
  - Reaches: `several parts`
  - Checked: przeczytane `now_ms` i test z `time.sleep(0.1)` w `test_gate_times.py`, wzorzec `^0\.\d{3}s` w `test_run_tests.py:474`, `timeout=120` w `run_count` i test dwóch przebiegów bez `--today`
  - Taken: odpowiedź 22
- 5 — `heavy` — test fundamentu the way woła kontrolę na żywym checkoucie, a kontrola bierze bazę z `origin/HEAD`, `main` albo `master`, więc ten sam commit przechodzi w jednym klonie i pada w drugim
  - Places: `elements/common/test_foundation_check.py:1525` (test `test_the_way_foundation_passes`)
  - Fix: test podaje kontroli bazę wprost albo sprawdza tylko to, co od bazy nie zależy
  - Removes: 1 miejsce
  - Reaches: `one file`
  - Checked: przeczytany test (l. 1524–1528) — uruchamia skrypt na `THE_WAY` bez ustalonej bazy
  - Taken: odpowiedź 22
- 6 — `heavy` — test liczenia audytu biegnie na prawdziwym checkoucie the way i czyta zapisy cykli ze wszystkich gałęzi lokalnych i zdalnych, więc jeden zły zapis na dowolnej gałęzi klonu czerwieni go niezależnie od commitu
  - Places: `process-audit/test_audit_count.py:2435` (test `test_the_way_without_a_repository_entry_is_this_checkout`)
  - Fix: test biegnie na repozytorium zbudowanym w katalogu tymczasowym
  - Removes: 1 miejsce
  - Reaches: `one file`
  - Taken: odpowiedź 22
- 7 — `medium` — git w testach biegnie pod globalną konfiguracją użytkownika, więc na maszynie z innym `core.autocrlf`, podpisywaniem commitów albo globalnym hookiem testy padają albo działają na innym repozytorium; dziś na maszynie Mariusza żaden nie pada
  - Places: 13 plików, m.in. `elements/common/test_foundation_check.py:194`, `elements/common/test_migrate_foundation.py:547`, `elements/part-map/test_cross_part_imports.py:741`, `process-audit/test_audit_count.py:15`, `task-cycle/test_tracked_private_paths_check.py:36`, `task-cycle/test_change_file_sizes.py:20`, `gate/test_run_tests.py:117`, `installation/test_install.py:180`, `installation/test_agent_types_installation.py:282`, `installation/test_lead_installation.py:120`
  - Fix: jedno środowisko gita w testach, które odcina konfigurację globalną i systemową, jak we wzorcu poziomu git
  - Removes: 13 plików
  - Reaches: `several parts`
  - Taken: wycinek `process-audit/test_audit_count.py:15` (stała `GIT_ENV`; odpowiedź 18, wzorzec e2e)
  - Deferred: pozostałe 12 plików (odpowiedź 22)
- 8 — `medium` — testy biorą wartość oczekiwaną ze stałej albo funkcji sprawdzanego kodu, więc stała zmieniona przez pomyłkę przesuwa też oczekiwanie
  - Places: `task-cycle/test_request_check.py:792`, `task-cycle/test_request_check.py:328`, `task-cycle/test_cycle_stages.py:752`, `instruction-files/test_check_instructions.py:860`, `process-audit/test_audit_count.py:2140`, `gate/test_skills_reach_the_way_sessions.py:32`
  - Fix: wartości oczekiwane wypisane w teście, ze źródłem w komentarzu
  - Removes: 6 miejsc
  - Reaches: `several parts`
  - Deferred: odpowiedź 22
- 9 — `medium` — testy granic zaufania i linków pomijają się po cichu na systemie, który nie robi linków symbolicznych, junction albo FIFO, więc niezmiennik granicy nie ma na tej maszynie wyniku, a bramka jest zielona
  - Places: `instruction-files/test_check_instructions.py:89`, `:789`, `:961`; `installation/test_install.py:665`, `:680`, `:782`; `installation/test_agent_types_installation.py:254`; `task-cycle/test_remove_merged_worktrees.py:486`, `:519`
  - Fix: pominięcie zależne od systemu staje się widoczne w raporcie bramki i każda granica ma przypadek, który biegnie na każdym systemie
  - Removes: 9 miejsc
  - Reaches: `several parts`
  - Deferred: odpowiedź 22
- 10 — `medium` — test przypadku nie-UTF-8 na granicy instalatora przyjmuje każdy kod różny od zera, więc awaria skryptu przeszłaby jako odmowa
  - Places: `installation/test_coding_guidelines_installation.py:163`, `installation/test_testing_guidelines_installation.py:152`
  - Fix: test oczekuje kodu i komunikatu odmowy
  - Removes: 2 miejsca
  - Reaches: `one part`
  - Deferred: odpowiedź 22
- 11 — `medium` — test usuwania katalogów roboczych decyduje o pominięciu po wyniku przebiegu, więc skrypt, który usunąłby trzymany plik, daje pominięcie zamiast błędu
  - Places: `task-cycle/test_remove_merged_worktrees.py:575`, `:593`
  - Fix: warunek pominięcia sprawdzany przed przebiegiem
  - Removes: 2 miejsca
  - Reaches: `one file`
  - Checked: obniżona z `grave` — usuwany katalog należy do scalonego zadania i jest tym, który skrypt ma usunąć, więc pominięcie nie ukrywa utraty danych; na Linuksie oba testy pomijają się zawsze
  - Deferred: odpowiedź 22
- 12 — `medium` — trzy testy instalacji jednego skilla wpisują liczbę wszystkich punktów wejścia the way (42), więc każdy nowy skill czerwieni trzy testy niezwiązane z nim
  - Places: `installation/test_coding_guidelines_installation.py:110`, `installation/test_styleguide_installation.py:93`, `installation/test_testing_guidelines_installation.py:99`
  - Fix: test sprawdza punkt wejścia swojego skilla, nie liczbę wszystkich
  - Removes: 3 miejsca
  - Reaches: `one part`
  - Deferred: odpowiedź 22
- 13 — `medium` — podmiana gita albo funkcji sprawdzanego kodu tam, gdzie prawdziwy git w katalogu tymczasowym jest tani, więc test nie widzi, kiedy prawdziwy git mówi co innego
  - Places: `task-cycle/test_remove_merged_worktrees.py:635`, `project-level/test_plan_state.py:341`, `instruction-files/test_check_instructions.py:1042`
  - Fix: prawdziwy git w katalogu tymczasowym
  - Removes: 3 miejsca
  - Reaches: `several parts`
  - Deferred: odpowiedź 22
- 14 — `medium` — test sprawdza tylko nieobecności i przechodzi, gdy raport etapów nie zwraca żadnego wiersza
  - Places: `task-cycle/test_cycle_stages.py:153`
  - Fix: test oczekuje wierszy, które mają zostać
  - Removes: 1 miejsce
  - Reaches: `one file`
  - Deferred: odpowiedź 22
- 15 — `medium` — drugi przebieg migracji fundamentu zmienia produkt, który dzielą inne testy klasy, więc stanu po jednym przebiegu nikt nie sprawdza
  - Places: `elements/common/test_migrate_foundation.py:657`
  - Fix: drugi przebieg na własnej kopii produktu
  - Removes: 1 miejsce
  - Reaches: `one file`
  - Deferred: odpowiedź 22
- 16 — `medium` — skrypt czyta brakujące pole jako pusty tekst i idzie dalej, wbrew WAY-344
  - Places: `task-cycle/slice_size.py:162` (kawałek bez *Read*), `task-cycle/request_check.py:397` (dokument zadania bez `### Need` albo `### To do`)
  - Fix: brakujące pole kończy skrypt, jak każe WAY-344, albo szablon nazywa pole opcjonalnym
  - Removes: 2 miejsca
  - Reaches: `one part`
  - Deferred: odpowiedź 22
- 17 — `light` — brakujące pole kończy skrypt kodem 1, a nie 2, jak każe WAY-344; wywołujący nie odróżni braku pola od innego błędu
  - Places: `agent-instructions/skill_entry_points.py:114`, `agent-instructions/agent_type_copies.py:77` (naprawia go zadanie „the way: skrypty po przeglądzie fundamentu …”), `installation/install.py:136`, `project-level/plan_state.py:478`
  - Fix: kod 2 z nazwą pliku i pola
  - Removes: 4 miejsca
  - Reaches: `several parts`
  - Taken: wycinek `agent-instructions/skill_entry_points.py:114` (funkcja `read_skill`, `raise GeneratorError(f"{path}: frontmatter has no '{field}:' with a value")`; odpowiedź 22, warunek wzorca generatora)
  - Deferred: `installation/install.py:136`, `project-level/plan_state.py:478` (kody wyjścia tego skryptu przypina powierzchnia `project-plan-state-command`); `agent-instructions/agent_type_copies.py:77` naprawia zadanie „the way: skrypty po przeglądzie fundamentu …” (odpowiedź 22)
- 18 — `light` — testy instalacji instalują z żywego checkoutu albo z klonu `HEAD`, więc zmiany niezatwierdzone nie trafiają do instalowanego źródła
  - Places: `installation/test_install.py:50`, `installation/test_installed_guidance.py:30`, `installation/test_styleguide_installation.py:48`, `installation/test_testing_guidelines_installation.py:43`
  - Fix: jedno źródło instalacji w teście, klon z ustalonego commitu
  - Removes: 4 miejsca
  - Reaches: `one part`
  - Checked: obniżona z `heavy` — commit w innym checkoucie nie zmienia `HEAD` tego, z którego biegnie test, a klon `HEAD` w `test_install.py` jest zamierzony (komentarz l. 46–47)
  - Deferred: odpowiedź 22
- 19 — `light` — testy zakładają, że katalog tymczasowy systemu leży poza każdym repozytorium, albo używają w nim stałej nazwy pliku
  - Places: `elements/common/test_foundation_check.py:266`, `elements/common/test_migrate_foundation.py:715`, `task-cycle/test_remove_merged_worktrees.py:662`, `task-cycle/test_tracked_private_paths_check.py:206`, `task-cycle/test_change_file_sizes.py:232`, `task-cycle/test_review_reminder.py:304`, `project-level/test_readiness_check.py:579`, `project-level/test_plan_check.py:1008`
  - Fix: własny katalog tymczasowy testu, sprawdzony jako leżący poza repozytorium
  - Removes: 8 miejsc
  - Reaches: `several parts`
  - Deferred: odpowiedź 22
- 20 — `light` — testy porównują całe brzmienie komunikatu tam, gdzie umową jest tylko odmowa, kod albo status, więc przeredagowanie komunikatu czerwieni testy przy niezmienionym zachowaniu
  - Places: 20 miejsc w 17 plikach; pierwsze: `project-level/test_readiness_check.py:101`, `elements/common/test_foundation_check.py:247`, `installation/test_install.py:721`, `agent-instructions/test_agent_type_copies.py:169`, `agent-instructions/test_skill_entry_points.py:183`; pełna lista w `.runs/testing/tests_audit.md` (znaleziska F3 o brzmieniu)
  - Fix: test sprawdza kod wyjścia i słowo, które nazywa przypadek
  - Removes: 20 miejsc
  - Reaches: `several parts`
  - Deferred: odpowiedź 22
- 21 — `light` — testy sprawdzają wewnętrzne wywołania kodu zamiast wyniku, więc przebudowa bez zmiany zachowania je czerwieni
  - Places: `instruction-files/test_check_instructions.py:248`, `:459`, `:599`; `task-cycle/test_remove_merged_worktrees.py:653`; `process-audit/test_audit_count.py:313`, `:1696`, `:2975`; `project-level/test_plan_state.py:471`; `gate/test_run_tests.py:326`; `task-cycle/test_gate_times.py:410`
  - Fix: test sprawdza wynik widoczny z zewnątrz
  - Removes: 10 miejsc
  - Reaches: `several parts`
  - Deferred: odpowiedź 22
- 22 — `light` — wynik testów zależy od checkoutu albo interpretera, a nie od commitu: lista modułów biblioteki standardowej uruchomionego Pythona, lista plików katalogu roboczego
  - Places: `task-cycle/test_cycle_measures.py:794`, `task-cycle/test_gate_times.py:401`, `task-cycle/test_agent_types.py:44`
  - Fix: test czyta to, co śledzi git, i nazwy modułów Pythona 3.14
  - Removes: 3 miejsca
  - Reaches: `one part`
  - Deferred: odpowiedź 22
- 23 — `light` — test cytowany przez dwa niezmienniki pada przy każdym błędzie fundamentu, więc oba niezmienniki dostają wynik `fail` za błąd, który ich nie dotyczy
  - Places: `elements/common/test_foundation_check.py:1524` (test `test_the_way_foundation_passes`)
  - Fix: test sprawdza tylko znaleziska tych dwóch niezmienników
  - Removes: 1 miejsce
  - Reaches: `one file`
  - Taken: odpowiedź 22, razem z przyczyną 5 (ten sam test)
- 24 — `light` — test opisuje zachowanie dzisiejsze jako oczekiwane („Recorded behaviour, not a wish”), więc padnie przy jego poprawce
  - Places: `task-cycle/test_remarks_check.py:185`
  - Fix: test oczekuje zachowania wymaganego albo znika
  - Removes: 1 miejsce
  - Reaches: `one file`
  - Deferred: odpowiedź 22
- 25 — `light` — komentarz wyprowadza wartość oczekiwaną inaczej niż asercja (linia 17 wobec 21)
  - Places: `elements/common/test_foundation_check.py:572`
  - Fix: komentarz wyprowadza 21
  - Removes: 1 miejsce
  - Reaches: `one file`
  - Deferred: odpowiedź 22
- 26 — `light` — nieużyte nazwy z rozpakowania udają wartości, których nikt nie czyta; w jednym miejscu liczenie audytu odrzuca konkretny powód, a test migracji nie sprawdza kodu wyjścia
  - Places: 4 pliki (17 zgłoszeń reguły lintera, która ma blokować)
  - Fix: nazwy zastąpione `_` albo użyte
  - Removes: 4 pliki
  - Reaches: `several parts`
  - Taken: 13 miejsc w `process-audit/test_audit_count.py` (odpowiedź 5)
  - Deferred: `elements/common/migrate_foundation.py:395`, `:676`, `elements/common/test_migrate_foundation.py:660`, `process-audit/audit_count.py:1140` (odpowiedź 5)
- 27 — `light` — testy instalacji i instalator przechwytują wyjście procesu starą formą (`stdout=PIPE, stderr=PIPE`) zamiast `capture_output`, którą linter ma blokować
  - Places: `installation/install.py:83`, `installation/test_agent_types_installation.py:24`, `installation/test_coding_guidelines_installation.py:20`, `installation/test_install.py:25`, `installation/test_installed_guidance.py:15`, `installation/test_lead_installation.py:19`, `installation/test_styleguide_installation.py:24`, `installation/test_testing_guidelines_installation.py:19` (UP022)
  - Fix: `capture_output=True`
  - Removes: 8 miejsc
  - Reaches: `one part`
  - Taken: `installation/test_install.py:25` (odpowiedź 5)
  - Deferred: pozostałe 7 miejsc (odpowiedź 5)
- 28 — `light` — pętla bierze pary klucz–wartość słownika, choć używa tylko jednej strony
  - Places: `elements/common/foundation_check.py:587`, `:596`, `installation/install.py:459` (PERF102)
  - Fix: `.keys()` albo `.values()` zamiast `.items()`
  - Removes: 3 miejsca
  - Reaches: `several parts`
  - Deferred: odpowiedź 5
- 29 — `light` — adnotacja typu w cudzysłowie, zbędnym w Pythonie 3.14
  - Places: `process-audit/audit_count.py:2133`, `:2321` (UP037)
  - Fix: adnotacja bez cudzysłowu
  - Removes: 2 miejsca
  - Reaches: `one file`
  - Deferred: odpowiedź 5
- 30 — `light` — obejście litery `Z` przy czytaniu daty, które Python 3.14 robi sam
  - Places: `task-cycle/cycle_measures.py:121`, `task-cycle/cycle_stages.py:225` (FURB162)
  - Fix: `datetime.fromisoformat` bez podmiany `Z`
  - Removes: 2 miejsca
  - Reaches: `one part`
  - Taken: odpowiedź 5 (oba pliki zadanie i tak zmienia; `cycle_measures.py` to wzorzec raportu pomiarowego)
- 31 — `light` — ręczne obcinanie przedrostka albo przyrostka tekstu
  - Places: `agent-instructions/test_instruction_files.py:160`, `instruction-files/check_instructions.py:296` (FURB188)
  - Fix: `removeprefix` albo `removesuffix`
  - Removes: 2 miejsca
  - Reaches: `several parts`
  - Deferred: odpowiedź 5
- 32 — `light` — dwa sąsiednie `startswith` zamiast jednego z krotką
  - Places: `gate/test_skills_reach_the_way_sessions.py:62` (PIE810)
  - Fix: jedno `startswith` z krotką
  - Removes: 1 miejsce
  - Reaches: `one file`
  - Deferred: odpowiedź 5
- 33 — `light` — ręczne składanie par kolejnych elementów
  - Places: `task-cycle/cycle_measures.py:352` (RUF007)
  - Fix: `itertools.pairwise`
  - Removes: 1 miejsce
  - Reaches: `one file`
  - Taken: odpowiedź 5 (`cycle_measures.py` to wzorzec raportu pomiarowego)
- 34 — `light` — pętla nadpisuje parametr funkcji
  - Places: `task-cycle/test_remarks_check.py:346` (PLR1704)
  - Fix: inna nazwa zmiennej pętli
  - Removes: 1 miejsce
  - Reaches: `one file`
  - Deferred: odpowiedź 5

## Questions carried to cycle

none

## Human actions

- Instalacja ruffa 0.17.1 na komputerze Mariusza do środowiska `.runs/quality-venv` głównego checkoutu the way (`<main checkout>`; odpowiedź 25), tak jak README loop2 instaluje swoje narzędzia (`python -m venv .runs/quality-venv`, potem `.runs/quality-venv/Scripts/python.exe -m pip install ruff==0.17.1`), żeby bramka the way mogła go uruchomić — before the cycle, done (2026-11-15, `ruff 0.17.1`)

## Decisions in play

Brzmienie z `foundations/decisions.md` i `foundations/invariants.md` przy `21ecb62`.

Zmieniane albo wycofywane przez to zadanie (zgoda: odpowiedzi pod *Questions to settle*, WAY-314):

- **WAY-328** — „The-way departs, for its own code and its own tests, from the general coding guidelines and from the testing guidelines of a product, under the shared reading of product guidelines: in each part named in *Scope*, neither is missing, so a task of the-way that writes code, or writes or changes a test, in such a part waits for neither. The *Scope* names every part of the-way's part map, and a change that adds a part to the part map adds that part to this decision's *Scope*. A separate task that writes the general coding guidelines of the-way's own takes the coding guidelines out of this decision, one that writes its testing guidelines takes the testing guidelines out of it, and once both are written the decision is withdrawn.”
  - Zmiana: wycofana, bo zadanie pisze oba rodzaje wytycznych (odpowiedź 23).
- **WAY-09** — „On the main branch, this repository holds `foundations/` with the entries of the-way itself, a directory for each part of the process other than `repository`, which the part map of the-way names with its files, the files that configure the whole repository, which its part map gives to the `repository` part (WAY-44), the root agent instruction files, the project skill entry points under `.claude/skills/` and `.agents/skills/` and the copies of the cycle's agent type definitions under `.claude/agents/`, which the map gives to `agent-instructions` (WAY-44), and a `README.md` that describes the repository. A directory reaches the main branch only once it holds what its part requires: […]”
  - Zmiana: repozytorium trzyma też katalog `guidelines/` z wytycznymi samego the way, który mapa daje części `agent-instructions` (odpowiedź 23, WAY-167).
- **WAY-38** — „Every script of the-way runs on the version of Python the repository declares, with its standard library alone, and installs nothing. It calls git, the Python interpreter running it, and the commands a product declares in its own repository, reading their output through an adapter for the format. Where a product declares no such command, the script reports what it could not check, never agreement.”
  - Zmiana: zdanie, że testy stałych kontroli uruchamiają przypięte narzędzie ze środowiska zadeklarowanego w repozytorium (odpowiedź 4); to samo zdanie dochodzi do niezmiennika `script-subprocesses`: „No script git tracks starts a program other than git, the Python interpreter running the script, or a command the product declares in its repository.”
- **WAY-344** — „A script of the-way that reads a file an agent or a human writes checks that the file holds each field the script needs […] and where a field is missing or stands under another name the script ends with an error that names it, never guessing and never reading the absence as an empty value. […] a missing field ends the script with exit code 2 and a message that names the file and the field […]” (część wiążąca bez zmian).
  - Zmiana: *Rationale*, zdanie „The-way departs from the guidelines of a product for its own code (WAY-328), so no guideline of a product asks that a script check its input, and new code copies the code already there; this rule is the requirement that stands in the-way's own log.”, oraz pozycja *Rejected* otwierająca się „the rule as an exception written into WAY-328 —” mówią o stanie sprzed tego zadania i dostają brzmienie zgodne z wytycznymi the way, których reguła wskazuje WAY-344 (odpowiedzi 12 i 23).
- **WAY-363** — „A reviewer grades as Minor a finding about the structure of code that lies below the threshold of the rule of size in the product's coding guidelines, and every such finding in a product that has no rule of size, whatever the reason: for example, it departed from the rule by a decision, it has no coding guidelines at all, or its guidelines were written before the rule existed. […] A finding about a function or a file over a threshold is graded as any other finding.”
  - Zmiana: przykład w *Verification* „a script of this repository, which has no coding guidelines (WAY-328), grew by forty lines in one function” przestaje być prawdziwy i dostaje inny przykład (odpowiedź 23).

Wiążące zadanie bez zmiany:

- **WAY-14** — „A decision, and every change to it, binds once a human accepts it, never an agent. In the-way, that human is Mariusz.”
- **WAY-16** — „One command runs all of a product's tests, the tests of its invariants among them — the same command for an agent, for a human and for whatever runs it when a change is merged — and no list of checks written by hand stands beside it.”
- **WAY-48** — „A trust boundary is recorded at the part that holds it, as a pattern of the code files which take in what the product does not control […] A change that touches the files of a boundary is checked for crafted input, and its review is aimed at that risk.”
- **WAY-51** — „On the main branch an invariant the product does not meet today stays whole and is marked violated at its entry; an invariant is marked violated only by a change of the foundation that a human accepts, never by a step of implementation. […] the test of a marked invariant stands in the product's suite marked as an expected failure in the product's test tool, and the change in which it starts to pass removes that marking and the mark of the invariant. While an invariant is marked violated, […] the review of each change to the files of the parts the invariant names keeps a cleaned file or a new one from breaking it again until the mark is cleared.”
- **WAY-167** — „A product's guidelines are written by hand and stand outside its foundation, in the directory `guidelines/` at the root of its repository […] those of the coding discipline stand in a file `guidelines/coding.md`, which holds the product's standing checks, the rules of the whole of its code and a table naming each other file of the discipline with when to read it, and in a file `guidelines/coding-<kind>.md` for each kind of code that has an exemplar […]. The directory `guidelines/` belongs to the part of the product's map whose files direct whoever carries out its tasks, as its instruction files and skills do.”
- **WAY-168** — „A binding rule of a product's guidelines says what to do and how […]. A rule that executes a choice of the product with a real cost names by identifier the decision of the product's log that carries the choice, […] and a rule that only says how to write code, tests or the look of the product reads `none` in *Decision* and gives its reason in one sentence. A rule names an invariant only where a cheap test of the product's suite checks the rule on a convention of the product's code […].”
- **WAY-172** — „A new or changed meaning of a product's guidelines that carries a choice with a real cost is a decision of the product's log, new or changed, and the code that uses it is made only once the human who accepts decisions (WAY-14) has approved it, in the document of the task that needs it […]. A new or changed rule that only says how to write code, tests or the look of the product, with no decision, is accepted by the human as a row of the task's table of settlements before the code that uses it […].”
- **WAY-173** — „The rules a template of a discipline of the-way carries and what the-way's skill of that discipline proposes bind a product only through a decision of the product's log adopting them, and the product departs from any of them only by a decision of its log that gives the reason. […]”
- **WAY-198** — „A decision of a product's log designates, for a kind of code, the one file of the product that is the exemplar of that kind, naming in backticks its path and the kind's identifier, and what of that exemplar a script can check […] stands in the coding guidelines of that kind as rules, each naming an invariant. The rest of the exemplar stands there as an example and binds no later code.”
- **WAY-199** — „[…] The coding guidelines of a kind give beside the path of each file of the kind they list its status, `exemplar`, `copy` or `do not copy`, and beside the exemplar's path the decision that designates it.”
- **WAY-202** — „The template of the coding discipline requires three standing checks of a product's code — a linter, a formatter and an audit of dependencies — […]. A product departs from any of them only by a decision of its log that gives the reason. They bind a product from the task that writes its coding guidelines, which is complete only once it holds, for each of the three standing checks, a decision of the product's log adopting it or departing from it with the reason.”
- **WAY-203** — „A rule of a linter's set stands among the rules that block a change […] only where every report it gives on the product's code leads to a change of code worth making […]. A comment in the code that turns off a rule that blocks has no effect: where the tool can be told so by a flag or its configuration, the test of the linter's invariant runs it so […].”
- **WAY-204** — „[…] a rule with one report that leads to no such change goes among the examples […]. The human approves that split in the product's decision adopting the set […]. The invariant of the linter rests on one environment fact, the rules the set holds at the edition the adopting decision names, and that decision gives the blocking rules as the set less the rules it keeps among the examples.”
- **WAY-205** — „Where a product's code already breaks the rules of its linter's set that block, the skill `maintain-coding-guidelines` proposes the linter's invariant over the whole of that code, marked violated until the code is cleaned (WAY-51). A formatter enters a product by one reformatting of the whole of its code in the task that brings the formatter.”
- **WAY-206** — „The skill `maintain-coding-guidelines` proposes an audit of dependencies that checks a change and fails it only where a version of a dependency that the change brings in against `{fork-point}` has a known vulnerability […].”
- **WAY-212** — „A product's root `AGENTS.md`, outside the block the-way's installer writes, points to its coding guidelines by one line naming `guidelines/coding.md` by its path in backticks with the condition of changing the product's code, written as the skill of `instruction-files` gives a pointer, and no line of it names a file `guidelines/coding-<kind>.md`. […]”
- **WAY-215** — „Unless an approved departure under the shared reading of product guidelines applies, a task […] writing code in a product with no general coding guidelines or writing or changing a test in a product with no testing guidelines […] stays in refinement as `waiting for human` […]; refinement independent of that answer continues, and a task writing those guidelines does not wait for its own output. […]”
- **WAY-216** — „A task that creates the first file of a kind of code whose row the general coding index lacks gains in *To do* the designation of that kind's exemplar […] and its kind guidelines with their index row […].”
- **WAY-231** — „Testing is a discipline of a product's guidelines of its own […]. A kind of code of a product's coding guidelines is code of the product other than its tests, and the patterns a product's tests follow stand in its testing guidelines at the level of test they belong to.”
- **WAY-232** — „The template of the testing discipline requires the rule that the expected value of every test of a product comes from a source other than the code under test — a document of the product its testing guidelines name as a source […] — and never from what the code gives today […]. Where a test's name does not show the source of a value, a comment in the test names it […].”
- **WAY-235** — „The template of the testing discipline requires […] for each trust boundary of the product's part map at least one invariant that the boundary refuses crafted input or unauthorised access, checked by a permanent test that checks the refusal directly, takes the expected refusal from the product's decisions on permissions and is seen failing once; […]”
- **WAY-240** — „[…] a level whose name means in the product something other than in the field, "integration" above all, is a term of the product's glossary, defined by the resources a test of that level may touch […]. For each part the guidelines apply to, they say in one sentence whether its complexity lies in computation or in its connections. […]”
- **WAY-241** — „The template of the testing discipline gives a product's testing guidelines, for each level, a recipe of the same fields […] each field that binds naming the product's decision that carries it […]. The field of the command names the gate and how it narrows to the level, a file or a test, where the gate can, and otherwise reads `none`; the field of the time limit points to the configuration file that holds it; and no recipe lists commands of the test tool of its own.”
- **WAY-242** — „The exemplar test of a level of a product's tests is designated by a decision of the product […]: where the level already has tests, the skill `maintain-testing-guidelines` compares them and proposes the exemplar from that comparison […].”
- **WAY-247** — „One task of a product may write both its coding guidelines and its testing guidelines, the skill of each discipline leading that discipline's matters in the task's refinement.”
- **WAY-252** — „[…] A product adopts the rule by a decision naming the tool and the parts it runs on, chosen among the parts whose complexity lies in computation, or departs from it by a decision that gives the reason.”
- **WAY-253** — „[…] In every other part, the author mutates the code in their head before finishing — a wrong constant or branch, a missing side effect, an empty return, unchecked empty or hostile input — and treats a mutation no test catches as behaviour left unprotected.”
- **WAY-312** — „[…] a rule lists no state of the product's code or of the product and repeats neither a decision of the product's log nor a value taken from a configuration file […].”
- **WAY-360** — „The template of the coding discipline requires, in the general file of a product's coding guidelines, a rule of the size of a function and a file under the heading `### Size of a function and a file`, after the six rules on failures and logs, with an invariant of its own and a test of its own, outside the set of rules of the product's linter. A product sets its thresholds after a trial run on its existing code and writes its exceptions in its decision on the rule […]. Where code other than the exceptions of the product's decision stands over a threshold, the rule's invariant is marked violated until that code is cleaned (WAY-51).”
- **WAY-361** — „The test of a product's rule of size, when it fails, names every function and file over a threshold with its size, and the reviewer of the whole change runs it as an ordinary test of the product's suite on the state before the change and on the state after it. A product has no command of its own that gives the sizes of functions […] (WAY-16).”
- **WAY-365** — „Where a slice of a plan adds to a function or a file that stands over the threshold of the product's rule of size, the plan begins with a slice that moves a part of that function or file out without a change of behaviour […]. The author of a change without a plan makes that move the first commit that changes the code. […]”
- **WAY-372** — „[…] the reasons are three: a part cannot start or finish without something outside the refinement of the task, such as access the agent lacks or another task's result; the parts change different repositories (WAY-140); or a later step of the refinement offers a separate task. A task's size alone is no reason […].”

## Settlements to record

Candidates: 39 shown, 34 accepted — 2026-11-15

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | The way przyjmuje szablon wytycznych kodu z odstępstwami od formatera, od audytu zależności i — osobną decyzją — od sześciu reguł o awariach i logach. | decision | pytanie 26 (jego *Not chosen*) | czy reguły `guidelines/coding.md` mają decyzję, na którą się powołują |
| 2 | The way przyjmuje szablon wytycznych testów z odstępstwami od testów mutacyjnych i od pola *Time limit*, a `### AI in tests` wchodzi bez narzędzia. | decision | pytanie 26 | czy przyjąć szablon testów w całości, czy tylko reguły, które cykl uzna za pasujące |
| 3 | Kod the way sprawdza ruff 0.17.1 pełnym domyślnym zestawem bez preview, `target-version = "py314"`, w dziesięciu częściach z kodem Pythona, testy też; 18 reguł z odpowiedzi 2 stoi w przykładach, reszta zatrzymuje zmianę, komentarz wyłączający regułę nie działa, a wyłączenie reguły dla całego the way to zmiana decyzji. | decision | pytania 1 i 2 | wybór lintera, zestawu i podziału reguł |
| 4 | Wersję ruffa przypina `required-version` w `ruff.toml` i plik wymagań z sumami SHA-256 każdego koła, ruff stoi w środowisku `.runs/quality-venv` instalowanym według README, a CI dostaje tylko krok instalacji. | decision | pytanie 3 | samą blokadę wersji bez sum i bez pliku dla Dependabota |
| 5 | Test lintera szuka środowiska `.runs/quality-venv` w głównym checkoucie, przez wspólny katalog gita, żeby jedna instalacja obsłużyła każdy katalog roboczy. | data or code: test niezmiennika lintera i sekcja „Running the tests” `README.md` | pytanie 25 | środowisko obok testu, czyli czerwoną bramkę w każdym katalogu roboczym cyklu |
| 6 | Żaden plik dziesięciu części nie łamie reguły ruffa, która zatrzymuje zmianę; niezmiennik stoi oznaczony jako naruszony, dopóki pozostałe miejsca nie zostaną poprawione. | invariant | pytanie 5 | niezmiennik obowiązujący od scalenia i poprawę wszystkich 37 miejsc |
| 7 | Domyślny zestaw ruffa 0.17.1 to 407 reguł z `DEFAULT_SELECTORS` w `crates/ruff_linter/src/settings/mod.rs` przy tagu `0.17.1`. | environment fact | *Context* (fakt składu zestawu); WAY-204 („The invariant of the linter rests on one environment fact”); przyjęte: doradca dnia w imieniu Mariusza, 2026-11-15: „7 tak, 8 tak, 28 tak” | skład zestawu z pamięci albo z dokumentacji innej wersji |
| 8 | Ruff 0.17.1 z ustawieniem `required-version` kończy się błędem, gdy uruchomiona wersja go nie spełnia. | environment fact | pytania 3 i 25 (ich *Answer*: „ruff odmawia pracy w innej wersji”); przyjęte: doradca dnia w imieniu Mariusza, 2026-11-15: „7 tak, 8 tak, 28 tak” | własne sprawdzanie wersji w teście lintera |
| 9 | Testy stałych kontroli uruchamiają przypięte narzędzie ze środowiska zadeklarowanego w repozytorium. | sentence of WAY-38 | pytanie 4 | czy test lintera łamie WAY-38, i zatrzymanie cyklu na tym pytaniu |
| 10 | To samo zdanie dochodzi do niezmiennika `script-subprocesses`. | invariant | pytanie 4 | niezmiennik, który dalej zabrania testowi uruchomić ruffa |
| 11 | Kod the way nie ma automatycznego formatowania; formater wchodzi kiedyś razem dla the way i loop2 osobną decyzją. | decision | pytanie „Czy kod the way dostaje automatyczne formatowanie?” | przeformatowanie 61 plików |
| 12 | The way odstępuje od audytu zależności, bo jego kod nie importuje niczego spoza biblioteki standardowej, a jedyną zadeklarowaną zależnością jest linter w wersji przypiętej decyzją. | decision | pytanie 6 | powód odstępstwa, który przestaje być prawdziwy w chwili scalenia |
| 13 | The way odstępuje od wszystkich sześciu reguł o awariach i logach, bo jego skrypty nie piszą logów, a o awarii mówią kodem wyjścia i linią `Error:`. | decision | pytanie 7 | przyjęcie `### Hiding a failure` przełożonego na konsolę |
| 14 | Funkcja skryptu ma najwyżej 80 linii razem z zagnieżdżonymi, plik skryptu najwyżej 1000 linii; testów reguła nie obejmuje, wyjątków nie ma, a liczy test oparty na `ast`, biegnący poza przebiegiem lintera. | decision | pytania 8, 9 i 10 | progi, zasięg na testy i wyjątki |
| 15 | Żadna funkcja i żaden plik skryptu nie przekracza progu; niezmiennik stoi oznaczony jako naruszony do podziału 11 funkcji i 2 plików. | invariant | pytania 8 i 10 | niezmiennik obowiązujący od scalenia albo wyjątki |
| 16 | Każdy skrypt zaczyna się opisem, jak go uruchomić (`python -B …`) i co znaczą jego kody wyjścia, i ma jedno stałe miejsce startu zwracające kod wyjścia; bez niezmiennika. | guidelines: coding | pytanie 12 | test i poprawkę 8 plików w tym zadaniu |
| 17 | Brakujące pole czytanego pliku obsługuje się tak, jak każe WAY-344; reguła wskazuje WAY-344 i nie powtarza jej treści. | guidelines: coding | pytanie 12 | przepisanie treści WAY-344 do wytycznych |
| 18 | The way ma sześć rodzajów kodu z wzorcami z odpowiedzi 13: `check`, `measuring-report`, `generator`, `repository-changer`, `command-runner`, `shared-module`. | decision | pytanie 13 | podział na rodzaje i wybór wzorców |
| 19 | Cztery niezmienniki reguł rodzajów: generator bez `--write` nie zmienia pliku, repository changer bez `--apply` albo potwierdzenia nic nie zmienia, command runner oddaje kod wyjścia dziecka bez zmian, import shared module niczego nie wykonuje. | invariant | pytanie 13 | reguły rodzajów bez testu albo inne reguły |
| 20 | Testy the way mają pięć poziomów: unit, test plików, test gita, test repozytorium i e2e w znaczeniu dziedziny. | decision | pytanie 14 | trzy poziomy nazwami dziedziny |
| 21 | Test plików (`files`): pliki w katalogu tymczasowym i proces Pythona, bez gita. | glossary term | pytanie 14 | znaczenie nazwy poziomu z dziedziny |
| 22 | Test gita (`git`): repozytoria git zbudowane w katalogu tymczasowym. | glossary term | pytanie 14 | jw. |
| 23 | Test repozytorium (`repository`): prawdziwy checkout the way, sprawdzający właściwość samego repozytorium. | glossary term | pytanie 14 | jw. |
| 24 | Złożoność leży w obliczeniach w częściach elements-common, part-map, relation-model, project-level, task-cycle, instruction-files, process-audit, a w połączeniach w gate, agent-instructions, installation. | guidelines: testing | pytanie 15 | przydział `task-cycle`, który ma i jedno, i drugie |
| 25 | Wartość oczekiwaną test bierze z fundamentu the way, jego słownika, szablonów i skilli, które skrypt wykonuje, oraz z opisu na początku skryptu. | decision | pytanie 16 | źródła bez opisu skryptu |
| 26 | W przepisach poziomów wiąże: `test_*.py` obok skryptu pod `unittest`, atrapy tylko zegara i tego, czego nie da się zrobić na tymczasowym repozytorium git, wartości ze źródłem w komentarzu, czas podawany z zewnątrz, *Command* `python -B gate/run_tests.py <katalog>`, *Purpose* każdego poziomu; od pola *Time limit* the way odstępuje. | decision | pytanie 17 | które pola przepisu wiążą |
| 27 | Wzorce poziomów to pięć testów z odpowiedzi 18. | decision | pytanie 18 | wybór wzorców z 38 plików testów |
| 28 | The way świadomie nie testuje automatycznie tego, co agent robi, idąc za skillem; wraca do tego przy powtarzającym się błędzie zachowania agenta, którego audyt nie łapie przed scaleniem. | decision | pytanie 19; przyjęte: doradca dnia w imieniu Mariusza, 2026-11-15: „7 tak, 8 tak, 28 tak” | `none` w `## Not tested on purpose` |
| 29 | The way odstępuje od testów mutacyjnych; wraca do nich przy błędzie po scaleniu w części obliczeniowej, który przepuściła brakująca asercja. | decision | pytanie 20 | przyjęcie narzędzia dla części obliczeniowych |
| 30 | Sześć niezmienników odmowy granic zaufania, wywiedzionych z WAY-48 · WAY-235 i cytujących testy z odpowiedzi 21. | invariant | pytanie 21 | osobną decyzję o odmowach albo brak niezmienników |
| 31 | Repozytorium the way trzyma katalog `guidelines/`, który mapa daje części `agent-instructions`. | sentence of WAY-09 | pytanie 23 | katalog niedozwolony przez WAY-09 |
| 32 | WAY-328 zostaje wycofana. | sentence of WAY-328 | pytanie 23 | pozostawienie WAY-328 przy napisanych wytycznych |
| 33 | *Rationale* i pozycja *Rejected* WAY-344, które powołują się na WAY-328, mówią o stanie po napisaniu wytycznych the way. | sentence of WAY-344 | pytanie 23 | zdania o stanie, który przestał istnieć |
| 34 | Przykład w *Verification* WAY-363 o skrypcie the way bez wytycznych kodu dostaje inny przykład. | sentence of WAY-363 | pytanie 23 | przykład, który przestał być prawdziwy |

## Out of scope

none
