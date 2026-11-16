---
title: the way — wykrywać testami niezgodną wersję Pythona, dodatkowe zależności i brakujące pliki
status: draft
created: 2026-10-25T16:00
updated: 2026-11-14
tags: [zadanie]
related: "the project note in the author's backlog"
---

# the way — wykrywać testami niezgodną wersję Pythona, dodatkowe zależności i brakujące pliki

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Cztery niezmienniki the way — `python-version-declared`, `script-language`, `script-imports` i `element-directory-contents` — mają dziś metodę `review`: sprawdza je ręcznie agent przeglądający każdą zmianę, do której sięgają, a nie test.
- Gdyby przegląd przeoczył skrypt w innym języku albo import pakietu spoza biblioteki standardowej, każdy produkt przypinający the way musiałby zapewnić dodatkowy interpreter albo pakiet (WAY-38, uzasadnienie); to ryzyko, nie potwierdzony incydent.
- Test przenosi te sprawdzenia z pamięci przeglądającego do bramki testów, którą przechodzi każda zmiana.

### To do

1. Test niezmiennika `python-version-declared`: sprawdza, że repozytorium deklaruje Python 3.14 w `.python-version`.
2. Test niezmiennika `script-language`: sprawdza, że każdy skrypt śledzony przez git jest plikiem Pythona, przy czym za możliwy skrypt uznaje każdy śledzony plik spoza listy dozwolonych rodzajów (pytanie 1).
    - lista dozwolonych rodzajów na dziś: pliki `.py` i `.md` oraz pliki `.gitignore`, `.gitattributes` i `.python-version`
    - plik każdego innego rodzaju test zgłasza; nowy rodzaj, który nie jest skryptem, autor zmiany dopisuje do listy w teście
    - polecenie zapisane w treści pliku `.md` (np. w skillu) nie jest skryptem
3. Test niezmiennika `script-imports`: sprawdza, że żaden skrypt śledzony przez git nie importuje modułu innego niż moduł biblioteki standardowej Pythona 3.14 albo plik Pythona śledzony przez git.
    - widzi importy w tym samym zasięgu co test niezmiennika `cross-part-imports`, a import, którego nazwy nie da się wyliczyć, zgłasza (pytanie 3)
    - na interpreterze innym niż wersja z `.python-version` pada z komunikatem, który podaje obie wersje (pytanie 2)
4. Test niezmiennika `element-directory-contents`: sprawdza, że tam, gdzie istnieje `{merge-onto}`, każdy katalog elementu ma szablon, przykłady albo odesłanie do wpisów the way służących za przykłady, oraz skill.
5. W `foundations/invariants.md` wpisy pod nagłówkami `## python-version-declared`, `## script-language`, `## script-imports` i `## element-directory-contents` dostają `Method: test` w miejsce `Method: review`.

### Questions to settle

- Pytanie 1: po czym test `script-language` rozpoznaje skrypt wśród plików śledzonych przez git?
  - Answer: po liście dozwolonych rodzajów plików — każdy śledzony plik musi być `.py`, `.md` albo jednym z plików konfiguracji repozytorium (`.gitignore`, `.gitattributes`, `.python-version`); każdy inny test traktuje jak możliwy skrypt i zgłasza, a rodzaj, który skryptem nie jest, autor zmiany dopisuje do listy w teście.
  - Not chosen:
    - rozpoznawanie po cechach skryptu (rozszerzenie z listy języków skryptowych, linia `#!`, bit wykonywalności) — skrypt w języku spoza listy i bez `#!` przejdzie po cichu, czego WAY-38 nie dopuszcza („a check that quietly sees nothing would pass”).
  - Source: Mariusz (przez doradcę dnia), 2026-11-14: „1 a — lista dozwolonych rodzajów plików” — na pytanie z drogami a (lista dozwolonych rodzajów; koszt: zgłosi też plik niebędący skryptem, np. `.json` albo obrazek, i autor dopisuje go do listy) i b.
- Pytanie 2: co robi test `script-imports`, gdy testy biegną na interpreterze innym niż Python 3.14?
  - Answer: test pada z komunikatem, który mówi, że testy trzeba uruchomić na wersji Pythona deklarowanej w `.python-version`, i podaje wersję, na której biegnie.
  - Not chosen:
    - test się pomija z powodem — niezmiennik nie dostaje wyniku, bramka kończy się na zielono, a zakazany import przechodzi po cichu;
    - test bierze listę modułów interpretera, na którym biegnie — na 3.12 przepuszcza `import cgi`, a zgłasza poprawny `import annotationlib`, więc sprawdza co innego niż reguła.
  - Source: Mariusz (przez doradcę dnia), 2026-11-14: „2 a — test pada z komunikatem o wersji”; różnice list sprawdzone 2026-11-14 interpreterami 3.14 i 3.12 na tej maszynie (`sys.stdlib_module_names`: `annotationlib` i `compression` tylko w 3.14, `cgi`, `telnetlib`, `crypt` tylko w 3.12).
- Pytanie 3: które importy wykonywane dynamicznie test `script-imports` ma widzieć?
  - Answer: ten sam zasięg co test niezmiennika `cross-part-imports`: `import`, `from … import`, `importlib.import_module`, `__import__`, `runpy`, kod podany do `-c` i do `exec`, `eval`, `compile`; import, którego nazwy nie da się wyliczyć, jest naruszeniem.
  - Not chosen:
    - tylko instrukcje `import` i `from … import` — `importlib.import_module("yaml")` przechodzi ten test, a zielony wynik `script-imports` opiera się wtedy na teście innego niezmiennika.
  - Source: Mariusz (przez doradcę dnia), 2026-11-14: „3 a — ten sam zasięg co test granic między częściami”; zasięg istniejącego testu: docstring `elements/part-map/test_cross_part_imports.py` na `f4af75d`.

## Context

- Pierwotne brzmienie zadania: „the way: testy dla czterech niezmienników trzymanych dziś przeglądem — `python-version-declared`, `script-language`, `script-imports`, `element-directory-contents` (przegląd fundamentu po odchudzaniu, R77)”.
- Na `f4af75d` git śledzi tylko pliki `.md` i `.py` oraz `.gitignore`, `.gitattributes` i `.python-version`; żaden śledzony plik nie ma bitu wykonywalności ani linii `#!`.
- Na `f4af75d` `.python-version` zawiera `3.14`, a mapa części daje ten plik części `repository`.
- Test `elements/part-map/test_cross_part_imports.py` (niezmiennik `cross-part-imports`) już dziś czyta każdy import każdego śledzonego pliku Pythona — `import`, `from … import`, `importlib.import_module`, `__import__`, `runpy`, kod podany do `-c`, `exec`, `eval`, `compile` — i zgłasza nazwę, która nie jest ani modułem z `sys.stdlib_module_names` interpretera, na którym biegnie, ani śledzonym plikiem; zgłasza też import, którego nazwy nie umie wyliczyć (docstring pliku, akapity „every `import` and `from ... import` statement” i „A use of `sys.executable`”).
- Bramka `gate/run_tests.py` nie sprawdza wersji interpretera, na którym biegnie.
- Fakt `python-stdlib-modules` (`foundations/environment_facts.md`), na którym stoi `script-imports`, mówi, że bibliotekę standardową Pythona 3.14 wyznaczają nazwy z `sys.stdlib_module_names` w interpreterze 3.14.
- Na `f4af75d` katalogi `elements/decisions/`, `elements/part-map/`, `elements/invariants/` i `elements/glossary/` mają `examples.md`; `elements/environment-facts/` go nie ma, a jego `template.md` w sekcji „## Examples” odsyła do wpisów `foundations/environment_facts.md` the way; każdy z pięciu ma `skill/SKILL.md`.
- `{merge-onto}` w the way: gałąź główna według `elements/common/rules.md` to ta, którą wskazuje `refs/remotes/origin/HEAD`, dziś `foundations`, więc warunek niezmiennika `element-directory-contents` jest dziś spełniony.
- Test postawiony poza `elements/part-map/`, który sięga po kod tamtego testu, jest importem między częściami, który sprawdza `cross-part-imports`; część `gate` nie zależy według mapy od żadnej innej.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-38 — In what are the scripts of the-way written? — „Every script of the-way runs on the version of Python the repository declares, with its standard library alone, and installs nothing. […]” (`foundations/decisions.md:1146` na `f4af75d`) — zadanie dodaje testy niezmienników `script-language` i `script-imports`, które z niej wynikają; zmiany w niej nie robi.
- WAY-89 — Which version of Python do the scripts of the-way run on, and when does it move? — „The scripts of the-way run on Python 3.14, which the repository declares in `.python-version`, and the declared version moves when the version in use leaves bugfix support, never because a newer version comes out.” (`foundations/decisions.md:2184` na `f4af75d`) — zadanie dodaje testy niezmienników `python-version-declared` i `script-imports`; zmiany w niej nie robi.
- WAY-09 — What may enter the process repository? — „A directory reaches the main branch only once it holds what its part requires: an element its template and rules, examples or a pointer to entries of the-way that serve as its examples, and a skill that writes its entries; […]” (`foundations/decisions.md:268` na `f4af75d`) — zadanie dodaje test niezmiennika `element-directory-contents`; zmiany w niej nie robi.
- WAY-08 — How is an invariant checked? — „Every invariant names its method of checking: a test of the product's test suite where a cheap test can check its sentence, and review otherwise […]. An invariant's test is seen failing once, with the command that later shows it passing — run before the code that satisfies it, or, where the code already has the behaviour, against that behaviour broken for a moment.” (`foundations/decisions.md:238` na `f4af75d`) — każdy z czterech testów trzeba raz zobaczyć czerwonym; kod the way już spełnia te niezmienniki, więc na chwilę psuje się zachowanie.
- WAY-61 — How is an invariant's method of checking written? — „An invariant's method of checking reads `test` once a test of the product's test suite, written in the product's language and run by the command that runs the product's tests, cites it, and `review` until then […]. A test checks what its invariant's sentence is about, as it stands on the commit being checked […].” (`foundations/decisions.md:1608` na `f4af75d`) — z niej wynika punkt 5; testy sprawdzają repozytorium the way takie, jakie jest na sprawdzanym commicie.
- WAY-328 — Does the-way hold its own code and tests to the general coding guidelines and the testing guidelines of a product? — „The-way departs, for its own code and its own tests, from the general coding guidelines and from the testing guidelines of a product, under WAY-217: in each part named in *Scope*, neither is missing, so a task of the-way that writes code, or writes or changes a test, in such a part waits for neither.” (`foundations/decisions.md:11228` na `f4af75d`) — *Scope* obejmuje każdą część mapy, więc zadanie na wytyczne nie czeka; zmiany w niej nie robi.

## Settlements to record

Candidates: 3 shown, 3 accepted — 2026-11-14

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Test `script-language` rozpoznaje skrypt po liście dozwolonych rodzajów plików (`.py`, `.md`, `.gitignore`, `.gitattributes`, `.python-version`): każdy inny śledzony plik zgłasza jako możliwy skrypt, a rodzaj, który skryptem nie jest, autor zmiany dopisuje do listy. | data or code: test niezmiennika `script-language`, lista z komentarzem podającym powód | pytanie 1 (wybór człowieka między pokazanymi drogami) | czy rozpoznawać skrypt po liście dozwolonych rodzajów, czy po rozszerzeniach języków skryptowych, linii `#!` i bicie wykonywalności |
| 2 | Test `script-imports` na interpreterze innym niż wersja z `.python-version` pada z komunikatem, który podaje obie wersje. | data or code: test niezmiennika `script-imports`, z komentarzem podającym powód | pytanie 2 (wybór człowieka między pokazanymi drogami) | czy test na złej wersji pada, pomija się, czy bierze listę modułów interpretera, na którym biegnie |
| 3 | Test `script-imports` widzi importy w tym samym zasięgu co test `cross-part-imports` (także `importlib.import_module`, `__import__`, `runpy`, `-c`, `exec`, `eval`, `compile`), a import, którego nazwy nie da się wyliczyć, zgłasza. | data or code: test niezmiennika `script-imports` | pytanie 3 (wybór człowieka między pokazanymi drogami) | czy czytać tylko instrukcje `import`, czy też importy wykonywane wywołaniem, i co zrobić z nazwą, której nie da się wyliczyć |

## Out of scope

- Test niezmiennika `script-subprocesses` (też z WAY-38, metoda `review`).
