---
title: "the way: instalator wpisuje do instrukcji agentów produktu pełną ścieżkę skryptu sprawdzającego fundament"
status: draft
created: 2026-11-22T15:05
updated: 2026-11-22
tags: [zadanie]
related: "the author's project note on the work process"
---

## Po co to

- **Jak jest dziś:** instalator the way wpisuje do instrukcji agentów każdego produktu (plik `AGENTS.md`) zdanie, w którym skrypt sprawdzający fundament (`foundation_check.py`) stoi samą nazwą, bez ścieżki. Sprawdzarka plików instrukcji bierze tę nazwę za ścieżkę do pliku, którego nie ma, i zgłasza ostrzeżenie. Od scalenia zadania the way z 22.11 (PR #157) obowiązuje decyzja WAY-418: produkt trzyma zero takich ostrzeżeń, a recenzent blokuje zmianę, na której głowie jakieś stoi. W loop2 po przepięciu na nową wersję the way zostało dokładnie to jedno ostrzeżenie.
- **Kto to odczuwa:** agenci cykli w loop2 i w każdym innym produkcie z the way — recenzent zablokuje ich zmianę za ostrzeżenie, którego nie mogą naprawić, bo ręczną poprawkę instalator nadpisze przy następnym przepięciu. Mariusz — jako cykl, który stanie albo wróci do niego z uwagą nie do usunięcia.
- **Co jeśli nic:** pierwszy cykl loop2 po przepięciu dostanie blokującą uwagę nie do naprawienia; albo cykl stanie, albo ktoś będzie ją przepuszczał ręcznie wbrew nowej decyzji — w każdym cyklu każdego produktu.

# the way: instalator wpisuje do instrukcji agentów produktu pełną ścieżkę skryptu sprawdzającego fundament

Status: ready for cycle
Project relation: independent
Defect introduced by: https://github.com/mariusznazar/the-way/pull/157

## Description

### Need

- Blok, który instalator the way wpisuje między znacznikami `<!-- the-way:begin -->` i `<!-- the-way:end -->` do głównego `AGENTS.md` produktu, daje w każdym produkcie ostrzeżenie `dead-path` sprawdzarki plików instrukcji (`instruction-files/check_instructions.py`): zdanie „Until the part map has its first parts, `foundation_check.py` reports every file git tracks as claimed by no part…” podaje skrypt samą nazwą, a sprawdzarka szuka pliku `foundation_check.py` w korzeniu produktu.
- Od WAY-418 recenzja całej zmiany w cyklu traktuje każde ostrzeżenie sprawdzarki w przebiegu na głowie zmiany jako uwagę Important w zakresie zadania, bez porównania z bazą — więc agenci cyklu produktu dostają uwagę, której nie mogą usunąć, bo ręczną poprawkę bloku instalator nadpisze przy następnym przepięciu.
- W loop2 po przepięciu na fad52af3 sprawdzarka zgłasza: `WARN dead-path AGENTS.md:34 \`foundation_check.py\` does not exist`.

### To do

1. Zdanie bloku instalatora, które zaczyna się od „Until the part map has its first parts” (`installation/install.py`, funkcja `product_guidance`, ok. :207), podaje skrypt sprawdzający fundament pełną ścieżką `{SUBMODULE}/elements/common/foundation_check.py`, jak dwa sąsiednie zdania bloku, tak że sprawdzarka plików instrukcji nie zgłasza na nim ostrzeżenia.
2. Test, który trzyma główny `AGENTS.md` produktu na zerze ostrzeżeń sprawdzarki plików instrukcji w produkcie zbudowanym pełną instalacją, przed pierwszym przebiegiem jakiegokolwiek skilla (bez katalogu `.runs/`), żeby kolejne zdanie bloku nie wprowadziło ostrzeżenia w każdym produkcie.

### Questions to settle

- 1. Czy zadanie obejmuje też ostrzeżenie `` `.runs/` does not exist ``, które sprawdzarka daje na samym bloku instalatora w produkcie bez katalogu `.runs/` (świeży klon, CI)?
  - Answer: tak, w zakresie, ale zdania o `.runs/` się nie zmienia: pełna instalacja zostawia `.runs/` osobną linią w `.gitignore` produktu, więc w produkcie po instalacji sprawdzarka daje na `.runs/` tylko `info`. Test buduje produkt pełną instalacją, nie samym tekstem bloku. Gdyby instalacja nie zostawiała `.runs/` w `.gitignore`, poprawką byłoby dopisywanie `.runs/` do `.gitignore` przez instalator, a dopowiedzenie w zdaniu tylko wtedy, gdyby instalator nie mógł ruszać `.gitignore`.
  - Not chosen:
    - dopowiedzenie w zdaniu, że `.runs/` nie istnieje, dopóki skill nie zapisze w nim pierwszego pliku — opiera się na liście fraz sprawdzarki, a mechanizm `.gitignore` i tak jest wymagany zdaniem bloku
    - poza zakresem, test zakłada `.runs/` przed sprawdzeniem — świeży klon i CI dalej pokazują ostrzeżenie, wbrew WAY-418, a test ukrywa ten przypadek
  - Source: doradca dnia w imieniu Mariusza, 2026-11-22: „1 — tak, ostrzeżenie o `.runs/` jest w zakresie (WAY-418 nie robi wyjątku, a test ma sprawdzać prawdziwy stan po instalacji). […] Jeśli tak — ostrzeżenie znika samo w produkcie po instalacji, test ma budować produkt pełną instalacją, a zdania nie ruszamy.”; fakt: przebieg `installation/install.py . --apply --url <the-way>` @ fad52af3 na pustym repozytorium w katalogu tymczasowym, 2026-11-22 — `.gitignore` = `.runs/`, katalogu `.runs/` brak, sprawdzarka: `INFO dead-path AGENTS.md:8 \`.runs/\` stands under a name the .gitignore at the root gives alone…` i jedno ostrzeżenie, `WARN dead-path AGENTS.md:10 \`foundation_check.py\` does not exist`; `installation/install.py:306` @ fad52af3 (`ignore_change`), `instruction-files/check_instructions.py:604` @ fad52af3 (`dead_path_note`)
- 2. Jak zdanie „Until the part map has its first parts, …” ma podawać skrypt sprawdzający fundament?
  - Answer: pełną ścieżką `{SUBMODULE}/elements/common/foundation_check.py` (w produkcie `.the-way/elements/common/foundation_check.py`), jak w dwóch sąsiednich zdaniach bloku — spójność bloku i realne sprawdzenie ścieżki przez sprawdzarkę, więc test z punktu 2 wyłapie przeniesienie skryptu. W klonie bez zainicjowanego podmodułu ta ścieżka da ostrzeżenie, ale taki klon to nie stan produktu po instalacji i stoi w nim już 86 ostrzeżeń tego samego rodzaju (po dwa z każdego wejścia skilla w `.claude/skills/` i `.agents/skills/` oraz `.the-way/installation/README.md` z tego samego bloku), więc 87. niczego nie zmienia. Sąsiednie zdania tej słabości nie mają: sprawdzarka nie sprawdza fragmentu ze spacją, więc `python -B …` nie jest dla niej ścieżką.
  - Not chosen:
    - nazwa słowami, bez odwrotnych apostrofów („that check reports…”) — agent szukający nazwy skryptu jej tu nie znajdzie, zdanie zależy od sąsiedniego akapitu, a sprawdzarka nie ma czego sprawdzić
    - forma polecenia `python -B {SUBMODULE}/elements/common/foundation_check.py`, identyczna z sąsiednimi zdaniami — nie daje ostrzeżenia w żadnym klonie, ale nic nie sprawdza ścieżki, więc przeniesiony skrypt przejdzie test niezauważony
  - Source: doradca dnia w imieniu Mariusza, 2026-11-22: „2 — a, pełna ścieżka `{SUBMODULE}/elements/common/foundation_check.py`, jak w dwóch sąsiednich zdaniach. Spójność bloku i realne sprawdzenie ścieżki; klon bez zainicjowanego podmodułu nie wnosi nowego rodzaju ostrzeżenia.”; po sprostowaniu przesłanki, 2026-11-22: „1 a — pełna ścieżka, popraw uzasadnienie (dzięki za sprostowanie; klon bez zainicjowanego podmodułu to nie stan produktu po instalacji, więc 87. ostrzeżenie tam nic nie zmienia).”; fakt: `instruction-files/check_instructions.py:466` @ fad52af3 (`if " " in token: return False`); przebieg sprawdzarki na produkcie po prawdziwej instalacji z opróżnionym `.the-way`, 2026-11-22 — `0 error, 86 warn, 3 info`

## Context

- Dwa sąsiednie zdania bloku podają ten skrypt pełną ścieżką w poleceniu, którego sprawdzarka nie bierze za ścieżkę, bo zawiera spację: „There `python -B .the-way/elements/common/foundation_check.py` checks this repository's foundation…” i „…which runs `python -B .the-way/elements/common/foundation_check.py` too…” (`installation/install.py` @ fad52af3, ok. :203 i :211).
- Sprawdzarka bierze za ścieżkę tekst w odwrotnych apostrofach, który kończy się znanym rozszerzeniem albo zawiera `/` lub `\`, i szuka go od korzenia repozytorium (`looks_like_path`, `check_dead_paths` w `instruction-files/check_instructions.py` @ fad52af3, ok. :450 i :630); ostrzeżenie spada do `info`, gdy zdanie mówi, że nazwana rzecz „does not exist” albo się „does not load” (lista `NOT_LOADED_PHRASES`, ok. :125), i gdy pierwszy człon ścieżki stoi osobną linią w głównym `.gitignore` (`dead_path_note`, ok. :604).
- Ostrzeżenie na `foundation_check.py` stało w bloku już przed PR #157 — sprawdzarka z 2a2f4106 zgłasza je na tym samym bloku; PR #157 dodał WAY-418, z którym blok instalatora przestał się zgadzać, a zdanie z gołą nazwą zastał.
- Tekst bloku przypina test `installation/test_install.py` (stałe z oczekiwanym tekstem bloku, ok. :70–:81); zmiana zdania zmienia jego oczekiwaną wartość, z przyczyną po stronie wymagania: WAY-418.
- W produkcie po pełnej instalacji, w którym katalog `.runs/` jeszcze nie powstał, ścieżka `.runs/` ze zdania „The skills of the-way keep their working files under `.runs/`…” nie daje ostrzeżenia: instalator dopisuje `.runs/` do `.gitignore`, a sprawdzarka obniża do `info` ścieżkę, której pierwszy człon stoi osobną linią w głównym `.gitignore`. Ostrzeżenie o `.runs/` daje sam blok bez reszty instalacji.
- Według mapy części `installation` zależy od `instruction-files`, więc test instalatora może uruchamiać sprawdzarkę plików instrukcji.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-418 — What does a change do with a warning of the script that checks the instruction files? — „The product keeps the script that checks its instruction files at no warning: a change that adds a warning corrects the path or names it where the script does not read it, as it corrects an error. A warning of the script in a run on the head of the change is a finding of the review of the whole change, Important and within the task's scope, with no comparison with the base.” (`foundations/decisions.md` @ fad52af3, *Scope:* instruction-files, task-cycle, installation)

## Settlements to record

Candidates: 3 shown, 2 accepted — 2026-11-22

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Blok instalatora podaje skrypt sprawdzający fundament w zdaniu „Until the part map has its first parts…” pełną ścieżką `{SUBMODULE}/elements/common/foundation_check.py`, jak dwa sąsiednie zdania. | data or code: `installation/install.py`, funkcja `product_guidance`, z testem, który przypina tekst bloku | Questions to settle, pytanie 2 | czy nazwać skrypt pełną ścieżką, formą polecenia `python -B …`, czy słowami bez odwrotnych apostrofów |
| 2 | Główny `AGENTS.md` produktu zaraz po pełnej instalacji, zanim powstał `.runs/`, nie daje żadnego ostrzeżenia sprawdzarki plików instrukcji. | invariant | To do, punkt 2; Questions to settle, pytanie 1; doradca dnia w imieniu Mariusza, 2026-11-22: „2 a — niezmiennik z testem `# invariant:`, wzorem installation-claude-guidance: test i tak powstaje, a niezmiennik sprawia, że reguła przetrwa następne zmiany bloku.” Nie wybrane: sam test bez wpisu w fundamencie — regułę trzymałyby tylko czerwony test i recenzja wg WAY-418, a usunięcia testu nic poza recenzją by nie wyłapało. | czy test dostaje niezmiennik w `foundations/invariants.md` i linię `invariant:`, czy zostaje samym testem bez wpisu w fundamencie |

## Out of scope

- Przepięcie loop2 na wersję the way z tą poprawką — po scaleniu loop2 dostaje kolejne przepięcie, które zdejmie ostrzeżenie.
