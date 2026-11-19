---
title: "the way: porządek kodu Pythona — automatyczne formatowanie, błędy lintera, podział za dużych funkcji i plików, ostre testy obu reguł i pełne sprawdzenie fundamentu w bramce"
status: draft
created: 2026-11-16T09:22
updated: 2026-11-19
tags: [zadanie]
related: "a note of the author's backlog"
---

# the way: porządek kodu Pythona — automatyczne formatowanie, błędy lintera, podział za dużych funkcji i plików, ostre testy obu reguł i pełne sprawdzenie fundamentu w bramce

Status: ready for cycle
Project relation: independent
Defect introduced by: https://github.com/mariusznazar/the-way/pull/125

## Description

### Need

- Kod Pythona the way nie ma automatycznego formatowania: 78 z 79 plików `.py` ma inny układ, niż ustawiłby formater, a układ zależy od agenta, który pisał plik.
- Kod łamie dwie własne reguły the way, a bramka testów jest mimo to zielona, bo testy obu reguł są oznaczone jako oczekiwana porażka: 24 miejsca naruszają blokujące reguły lintera ruff (WAY-380), a 11 funkcji ma ponad 80 linii i 2 pliki ponad 1000 linii (WAY-385).
- Test w bramce, który sprawdza fundament the way, pilnuje tylko dwóch niezmienników (`map-reference-target`, `test-method-citation`), bo w pełnej wersji padał w klonie z inaczej nazwaną główną gałęzią i dawał obu niezmiennikom wynik `fail` za błędy, które ich nie dotyczą; zwykły błąd fundamentu, np. numer, który nie wskazuje żadnej decyzji, nie czerwieni bramki.
- Test `task-cycle/test_remove_merged_worktrees.py` pada losowo na Linuksie, bo zależy od konserwacji, którą Git robi w tle w tymczasowym repozytorium testu.
- Słowo „entry” znaczy w kilku miejscach the way coś innego niż wpis fundamentu, choć słownik the way daje mu jedno znaczenie.
- Odczuwają to agenci cykli the way: nowe naruszenie lintera, rozmiaru albo fundamentu przechodzi przez bramkę i łapie je dopiero przegląd; Mariusz pośrednio, bo bałagan rośnie niezauważony.

### To do

1. Wprowadzić automatyczne formatowanie kodu Pythona the way formaterem ruffa (`ruff format`) w wersji, którą przypina WAY-381, z szerokością linii 100 i resztą ustawień domyślnych, tylko dla plików `.py`, i przeformatować nim raz cały kod wszystkich części, które WAY-379 wymienia w *Scope* (WAY-205); przeformatowanie stoi w osobnym commicie bez żadnej innej zmiany, a hash tego commita w nowym pliku `.git-blame-ignore-revs` w katalogu głównym repozytorium, który dołącza do plików części `repository` w mapie części.
2. Dodać niezmiennik formatera — każdy plik `.py` tych części stoi tak, jak zostawia go formater, i nie ma w nim komentarza `fmt: off`, `fmt: on` ani `fmt: skip` — i jego test w zestawie testów, wywoływany jednym poleceniem bramki obok testu lintera (WAY-16, WAY-205); przeformatować raz w układzie formatera przykład kodu Pythona w `installation/README.md` (blok testu `TrackedFilesTest`, ok. linii 114); `### Formatter` w `guidelines/coding.md` przestaje czytać `none — WAY-382` i dostaje decyzję oraz niezmiennik, jak daje reguła *Formatter* szablonu wytycznych kodu (`product-guidelines/coding/template.md`); sekcja README „Installing the linter” mówi o formaterze.
3. Naprawić wszystkie naruszenia blokujących reguł lintera (dziś 24: UP022 7, PERF102 3, UP037 3, RUF059 3, PIE810 2, FURB188 2, F541, PYI034, PLR1704, TRY004 po 1), w plikach, w których stoją, bez wyłączania reguł (WAY-380).
4. Zmienić progi reguły rozmiaru w WAY-385 na 110 linii dla funkcji i 1200 linii dla pliku skryptu i podzielić każdą funkcję i każdy plik skryptu ponad tymi progami po przeformatowaniu.
5. Zdjąć oznaczenie oczekiwanej porażki z testów obu reguł (`agent-instructions/test_linter_invariant.py`, `agent-instructions/test_size_invariant.py`), a w fundamencie przestawić niezmienniki `ruff-blocking-rules` i `function-and-file-size` na `Violated: no` i usunąć z ich decyzji, wytycznych i opisów testów zdania o znanych naruszeniach (WAY-51).
6. Przywrócić w teście fundamentu the way w bramce (`elements/common/test_foundation_check.py`, test pod komentarzem „the-way's own foundation”) pełne sprawdzenie fundamentu, tak by przechodził przy dowolnej nazwie głównej gałęzi klonu i cytował nowy niezmiennik pełnego sprawdzenia, a dotychczasowy wąski test zostawić przy `map-reference-target` i `test-method-citation`; poprawić zdanie README, które mówi, że w bramce sprawdzane są tylko dwa niezmienniki (akapit, który zaczyna się od „Two invariants of the foundation of the-way”).
7. Uniezależnić test `ApplyTest.test_a_dry_run_removes_nothing_and_apply_removes_only_what_is_marked` w `task-cycle/test_remove_merged_worktrees.py` od konserwacji Gita w tle (plik `maintenance.lock` tworzony i kasowany w tymczasowym repozytorium testu).
8. Zastąpić słowo „entry” tam, gdzie nie znaczy wpisu fundamentu, słowem, które pasuje w danym miejscu: dziennik zmian planu (WAY-145 i `project-level/lead/skill/SKILL.md`, „their change-log entries”), rejestr uruchomień polecenia testów (`task-cycle/gate_times.py`, zdanie niezmiennika `gate-times-refuses-impossible-entry` — jego identyfikator zostaje, bo zmiana brzmienia nie zmienia identyfikatora (`elements/common/rules.md`) — i opis rejestru w WAY-350), frazę „file/entry/section” (`project-level/lead/conversation_template.md`, `project-level/lead/answering.md`), ok. 24 nazwy testów i jeden komentarz testu (`process-audit/test_record_items.py`, komentarz „a doubled item, an entry in neither form, a findings file named twice”); zwykłe słowo w zwykłym znaczeniu nie dostaje wpisu w słowniku (WAY-95).

### Acceptance criteria

- Bramka (`python -B gate/run_tests.py`) jest zielona w CI na Linuksie i na Windowsie bez żadnego testu oznaczonego jako oczekiwana porażka w `agent-instructions/test_linter_invariant.py` i `agent-instructions/test_size_invariant.py`.
- Test fundamentu the way przechodzi także w lokalnym klonie, którego główna gałąź nazywa się `main`, i pada, gdy w fundamencie the way stoi odwołanie do decyzji, której nie ma.

### Questions to settle

- Czy porządek kodu idzie jednym zadaniem, razem z podziałem za dużych plików i z pełnym sprawdzeniem fundamentu w bramce?
  - Answer: tak, wszystko w jednym zadaniu.
  - Not chosen:
    - przywrócić ostre testy od razu, bez sprzątania — bramka byłaby czerwona w każdym cyklu, aż ktoś posprząta, i zatrzymałaby kolejkę the way;
    - podział dużych plików jako osobne, późniejsze zadanie — Mariusz wybrał jedno zadanie.
  - Source: Mariusz, 2026-11-16, przegląd decyzji trybu samodzielnego (pozycje 6 i 7 „You accept by merging” w opisie PR-a https://github.com/mariusznazar/the-way/pull/136), „1 b, 2 a”
- Czy kod the way dostaje automatyczne formatowanie?
  - Answer: tak; powód odłożenia z WAY-382 (konflikty z gałęziami zadań, które wskazują miejsca w plikach `.py` numerami linii) Mariusz uznał za nieaktualny, gdy kolejka zejdzie.
  - Not chosen:
    - zostawić WAY-382 („The-way's code has no automatic formatter”) — układ dalej zależy od agenta.
  - Source: Mariusz, 2026-11-16, rozmowa z doradcą dnia
- Jaka szerokość linii formatera?
  - Answer: 100 znaków (b).
  - Not chosen:
    - 88, domyślna ruffa i Blacka — przybywa 13 454 linii netto, ponad progami 80/1000 zostaje 22 funkcje i 6 plików;
    - 120 — najmniej zmian (+4 185 linii, 16 funkcji i 4 pliki), ale linie dłuższe niż w reszcie repozytorium.
  - Source: Mariusz, 2026-11-19, „1 b 2 d”; liczby z przeformatowania kopii `foundations` przy `bec6c3d2` ruffem 0.17.1 (przy 100: +8 597 linii netto, 20 funkcji i 4 pliki ponad 80/1000)
- Co z progami reguły rozmiaru, skoro formatowanie rozciąga funkcje i pliki?
  - Answer: przeliczamy próg na sformatowany kod tak, by miał tę samą ostrość co 80/1000 na kodzie bez formatowania (11 funkcji i 2 pliki ponad progiem): 110 linii dla funkcji i 1200 dla pliku (d); zmienia to WAY-385.
  - Not chosen:
    - zostaje 80/1000, dzielimy wszystko (a) — ok. 9 funkcji dzielonych tylko dlatego, że formater je rozciągnął;
    - dzielimy tylko pliki, test funkcji zostaje oczekiwaną porażką (b) — reguła w fundamencie dzieli się na dwie, a funkcje rosną bez czerwonej bramki;
    - podnieść progi do np. 100/1500 (c) — WAY-385 ten wariant już odrzuciła, a po formatowaniu i tak zostaje co dzielić.
  - Source: Mariusz, 2026-11-19, „1 b 2 d”; przy `bec6c3d2` sformatowanym na 100 próg 110/1200 zostawia ponad progiem 11 funkcji i 2 pliki (`process-audit/audit_count.py` 3602, `task-cycle/cycle_stages.py` 1273)
- Czy commit samego przeformatowania trafia do pliku `.git-blame-ignore-revs`?
  - Answer: tak (a); przeformatowanie idzie osobnym commitem bez innej zmiany, a jego hash trafia do `.git-blame-ignore-revs`.
  - Not chosen:
    - nie (b) — `git blame` wskazuje commit formatowania przy każdej przeformatowanej linii, a prawdziwego autora szuka się ręcznie przed tym commitem.
  - Source: Mariusz, 2026-11-19, „3a”
- Czy pełne sprawdzenie fundamentu w bramce dostaje własny niezmiennik?
  - Answer: tak (a) — pełny test cytuje nowy niezmiennik, a `map-reference-target` i `test-method-citation` zostają przy dzisiejszym wąskim teście; „kilka sekund drugiego uruchomienia kontroli to akceptowalna cena za to, że błąd fundamentu czerwieni jedną właściwą regułę”.
  - Not chosen:
    - bez własnego niezmiennika (b) — pełny test wraca pod cytowaniem dwóch dotychczasowych niezmienników, więc każdy błąd fundamentu daje im wynik `fail` za błąd, który ich nie dotyczy (przyczyna 23 audytu wytycznych), a kolejne zawężenie testu nie wymaga zmiany fundamentu.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-19, „4 a”
- Czy formater obejmuje też przykłady Pythona w plikach Markdown?
  - Answer: nie (b) — formater i jego niezmiennik obejmują tylko pliki `.py`; jedyny dziś przykład, który formater by przestawił (`installation/README.md`, blok kodu testu `TrackedFilesTest`, ok. linii 114), przeformatować raz w tej samej zmianie w układzie formatera, bo produkt kopiuje go do swoich testów; reguły na Markdown nie ma.
  - Not chosen:
    - tak, jak domyślnie robi ruff (a) — niezmiennik obejmuje przykłady w 249 plikach Markdown, a nieuformatowany przykład w skillu albo README czerwieni bramkę.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-19, „5 b, z jednym dodatkiem”
- Czy komentarze wyłączające formater są zakazane?
  - Answer: tak (a), spójnie z WAY-380 — test formatera pada, gdy w pliku `.py` części, które reguła formatera obejmuje, stoi komentarz `fmt: off`, `fmt: on` albo `fmt: skip`.
  - Not chosen:
    - bez zakazu (b) — taki komentarz łapie tylko przegląd zmiany, a bramka przepuszcza plik w innym układzie.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-19, „6 a”

## Context

- Liczby z tego dokumentu sprawdzono 2026-11-19 ruffem 0.17.1 z `.runs/quality-venv` przy commicie `bec6c3d2` i potwierdzono przy `d69fb20b`; zmieniają się z każdym scalonym zadaniem.
- Formater przy każdej szerokości rozkłada wywołania, których argumenty dziś są wyrównane pod nawiasem, na jeden argument w linii; stąd przyrost linii, a nie z samej szerokości.
- Pozycje 2–5 i 7 opisu PR-a https://github.com/mariusznazar/the-way/pull/136 (sekcja „You accept by merging”) są źródłem punktów 3–6 *To do*.
- Punkt 7: opis PR-a https://github.com/mariusznazar/the-way/pull/144 (sekcja *Checks*, pozycja 1 „For you to decide”) — test padł w pierwszej próbie CI na Linuksie z `FileNotFoundError` na `maintenance.lock` i przeszedł w powtórce; autor proponuje pomijać pliki blokad Gita albo wyłączyć konserwację w tle w repozytoriach testu.
- Punkt 8: opis PR-a https://github.com/mariusznazar/the-way/pull/148 (pozycja 1 „Fix or let through”, sekcja „Findings outside the task's scope”, Minor findings 2 i 3) wymienia miejsca i te użycia „entry”, które zostają, bo mają znaczenie z dziedziny: wyjście `git worktree list`, drzewa Gita, transkrypty sesji, wpisy dziennika decyzji w skryptach, które go porównują, „entry point”.
- Linia „Defect introduced by” dotyczy punktu 7: test powstał w PR-ze #125 i pada na poprawnym kodzie; reszta zadania to utrzymanie i zmiana decyzji.
- Jedyne z 24 miejsc lintera, którego typowa poprawka zmienia zachowanie, to TRY004 w `task-cycle/cycle_stages.py` (`raise ValueError(value)` w bloku `try`, który łapie `ValueError` i zamienia go na błąd brakującego pola; zamiana na `TypeError` dałaby wywrotkę skryptu zamiast kodu wyjścia 2).
- Test fundamentu w bramce zawęziono commitem `f16616c0` z dwóch przyczyn audytu wytycznych (zapis cyklu zadania wytycznych kodu i testów the way, commit `a0ffa8073a`, przyczyny 5 i 23): „ten sam commit przechodzi w jednym klonie i pada w drugim” oraz „test cytowany przez dwa niezmienniki pada przy każdym błędzie fundamentu, więc oba niezmienniki dostają wynik `fail` za błąd, który ich nie dotyczy”; pierwszej nie udało się 2026-11-19 odtworzyć w klonie bez `origin/HEAD`, `main` i `master`; skrypt `elements/common/foundation_check.py` wylicza bazę porównań z `refs/remotes/origin/HEAD`, potem `main`, potem `master` (docstring, akapit, który zaczyna się od „The state the branch left”).
- Formatowanie loop2 idzie osobnym zadaniem (a note of the author's backlog), które ma otwarte ustawienia ruffa; szerokość 100 jest wyborem the way, nie loop2.

## Questions carried to cycle

- Kolejność naprawy lintera względem przeformatowania; podział funkcji i plików idzie po przeformatowaniu, bo progi liczą kod sformatowany.
- Jak test fundamentu w bramce ustala bazę porównań w klonie z inną nazwą głównej gałęzi i w płytkim klonie CI.
- Czy drugie przeformatowanie, potrzebne, gdy `foundations` przyniesie przed scaleniem nowy nieformatowany kod, też trafia do `.git-blame-ignore-revs`.
- Jak uniezależnić niestabilny test: wyłączyć konserwację Gita w tle w repozytoriach testu (także w `origin.git`) czy wyjąć `origin.git` z migawki stanu, co zgadza się z opisem funkcji `state` („git's own directories left out”).
- Do jakiego rodzaju kodu należą moduły wydzielone przy podziale plików i czy testy importują przeniesione nazwy z nowego miejsca.

## Human actions

none

## Decisions in play

- **WAY-382** — zadanie ją zmienia: kod the way dostaje formater ruffa z szerokością linii 100, tylko dla plików `.py`, z zakazem komentarzy `fmt:` (odpowiedzi na pytania o formatowanie, szerokość, Markdown i komentarze). Dziś: „The-way's code has no automatic formatter, so `### Formatter` of its coding guidelines reads `none — WAY-382`. A formatter enters the-way only by a decision of this log that adopts it and by one reformatting of the whole of its code in the task that brings it (WAY-205).”
- **WAY-385** — zadanie ją zmienia: progi 110 linii dla funkcji i 1200 dla pliku (odpowiedź na pytanie o progi). Dziś: „A function of a script of the-way has at most 80 lines, counted with the functions nested in it, and a file of a script has at most 1000 lines, in each part that WAY-379 names; a test file stands outside the rule, and no function and no file is kept whole over a threshold as an exception. A test of the suite counts the lines with the `ast` module of the standard library, runs apart from the run of the linter and, where it fails, names every function and file over a threshold with its size (WAY-361).”
- **WAY-379** — jej *Verification* („the rule of the formatter reads `none —` with the decision that departs from it”) przestaje się zgadzać po zmianie WAY-382; zdanie wiążące się nie zmienia: „The-way adopts the template of the coding discipline for the code of each part named in *Scope* […] The-way departs from the template only by a decision of this log that gives the reason.”
- **WAY-205** — „A formatter enters a product by one reformatting of the whole of its code in the task that brings the formatter.” Jej *Verification*: „the task that brings a formatter reformats every file of the product once, and the formatter's invariant holds from that commit”.
- **WAY-51** — „an invariant is marked violated only by a change of the foundation that a human accepts […] the test of a marked invariant stands in the product's suite marked as an expected failure in the product's test tool, and the change in which it starts to pass removes that marking and the mark of the invariant.”
- **WAY-380** — „A comment in the code that turns a rule off has no effect, a fault of one file is fixed in that file, and turning a rule off for the whole of the-way, or moving a rule between the blocking rules and the examples, is a change of this decision.”
- **WAY-381** — „The version of Ruff is pinned by `required-version = "==0.17.1"` in `ruff.toml` […] while the one command that runs the checks stays `python -B gate/run_tests.py` (WAY-16).”
- **WAY-16** — „One command runs all of a product's tests, the tests of its invariants among them — the same command for an agent, for a human and for whatever runs it when a change is merged — and no list of checks written by hand stands beside it.”
- **WAY-08** — „An invariant's test is seen failing once, with the command that later shows it passing — run before the code that satisfies it, or, where the code already has the behaviour, against that behaviour broken for a moment.”
- **WAY-03** — „A change that alters an invariant test, or a test that holds a sentence of a decision by a line `decision:`, names that test in its request, so that the agent reviewing the change and the human merging it see it.”
- **WAY-233** — „changing the expected value of an existing test, deleting a test, weakening an assertion, and skipping or disabling a test are one kind of change, each made with its cause on the side of the data or of the requirement and a pointer to the evidence of that cause”.
- **WAY-95** — „A word takes a glossary entry when it means, in the product, something other than a reader who knows the product's field takes it to mean”.
- **WAY-145** — punkt 8 zmienia w niej słowo: „with an entry in the plan's log of changes giving the reason”.
- **WAY-350** — punkt 8 zmienia w niej słowo: „and an entry whose times cannot be, such as an end in the far future, deleted and counted for nothing”.

## Settlements to record

Candidates: 7 shown, 5 accepted — 2026-11-19

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Kod the way dostaje automatyczne formatowanie formaterem ruffa z szerokością linii 100 i resztą ustawień domyślnych, wprowadzone jednym przeformatowaniem całego kodu. | sentence of WAY-382 | pytania „Czy kod the way dostaje automatyczne formatowanie?” i „Jaka szerokość linii formatera?” | szerokość linii (domyślne 88 dałoby 6 plików i 22 funkcje do podziału) i czy WAY-382 zmienić, czy dopisać obok nowej decyzji |
| 2 | Funkcja skryptu the way ma najwyżej 110 linii, a plik skryptu najwyżej 1200 linii, liczone na kodzie po formatowaniu — ta sama ostrość co 80/1000 na kodzie sprzed formatera. | sentence of WAY-385 | pytanie „Co z progami reguły rozmiaru, skoro formatowanie rozciąga funkcje i pliki?” | czy zostawić 80/1000 i dzielić ok. 20 funkcji, czy zmienić progi i na jakie |
| 3 | Kontrola fundamentu (`elements/common/foundation_check.py`) nie zgłasza żadnego błędu w fundamencie the way, a sprawdza to pełny test w bramce, który cytuje ten niezmiennik. | invariant | pytanie „Czy pełne sprawdzenie fundamentu w bramce dostaje własny niezmiennik?” | czy przywrócony pełny test cytuje własny niezmiennik, czy dalej `map-reference-target` i `test-method-citation`, które wtedy dostają `fail` za cudze błędy |
| 4 | Formater i jego niezmiennik obejmują tylko pliki `.py`; przykłady Pythona w plikach Markdown nie podlegają regule. | sentence of WAY-382 | pytanie „Czy formater obejmuje też przykłady Pythona w plikach Markdown?” | domyślne zachowanie ruffa, które formatuje też bloki kodu w 249 plikach `.md` |
| 5 | Komentarz `fmt: off`, `fmt: on` albo `fmt: skip` w pliku, który obejmuje reguła formatera, jest zakazany, a test formatera na nim pada. | sentence of WAY-382 | pytanie „Czy komentarze wyłączające formater są zakazane?” | test formatera, który przepuszcza plik z takim komentarzem, bo `ruff format --check` go respektuje |

## Out of scope

none
