---
title: Podgląd instalatora the way nie oznacza zmiany przy plikach, które różnią się tylko końcówkami linii
status: draft
created: 2026-10-25T16:00
updated: 2026-11-14
tags: [zadanie]
related: "the project note of the author's backlog"
---

# Podgląd instalatora the way nie oznacza zmiany przy plikach, które różnią się tylko końcówkami linii

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Instalator the way (`installation/install.py`) przed zapisem pokazuje podgląd: przy każdym pliku, który zapisuje w produkcie — punktach wejścia skilli (`SKILL.md` w `.claude/skills/` i `.agents/skills/`) i definicjach typów agentów w `.claude/agents/` — wypisuje `CREATE` (nowy), `KEEP` (bez zmian) albo `REPLACE` (do podmiany).
- O `KEEP` albo `REPLACE` decyduje porównanie surowych bajtów pliku na dysku z bajtami nowej treści, a nowa treść ma zawsze końcówki LF.
- Gdy git, którym pobrano produkt, działa z `core.autocrlf=true` — domyślnym ustawieniem Gita na Windowsie — pliki na dysku mają końcówki CRLF, więc przy każdym podbiciu wersji the way podgląd oznacza `REPLACE` każdy z tych plików, także te o niezmienionej treści, a różnica wypisana pod nimi jest pusta.
- Z takiego podglądu nie widać, które skille naprawdę się zmieniają, a jedna prawdziwa zmiana może zginąć wśród pozornych i zostać zatwierdzona bez przejrzenia; instalator też nigdy nie odpowiada „Already installed; no changes”, tylko pyta o zgodę na zapis.
- Odbiorcą jest ten, kto instaluje albo aktualizuje the way w produkcie na komputerze z takim ustawieniem gita — Mariusz na innym komputerze albo po przeinstalowaniu Gita, inna osoba, agent w ich sesji.

### To do

1. Plik, który instalator zapisuje w produkcie, a który różni się od nowej treści tylko końcówkami linii (CRLF zamiast LF), dostaje w podglądzie `KEEP`, bez różnicy pod spodem, i instalator go nie przepisuje; gdy żaden plik nie zmienia treści i wersja the way się nie przesuwa, instalator odpowiada „Already installed; no changes”. Miejsce zmiany: funkcja `file_action` w `installation/install.py`, zdanie `path.read_bytes() == content.encode("utf-8")` (około linii 435).

## Context

- Na komputerze Mariusza objaw dziś nie występuje: systemowy `the system-wide gitconfig of Git for Windows` ma `core.autocrlf=true`, ale `~/.gitconfig` ma `core.autocrlf=input` i to ono obowiązuje; podgląd instalatora na `loop2` z commitu `f4af75d` the way pokazał 2026-11-14 50 × `KEEP`, 2 × `CREATE` i żadnego `REPLACE`, a `git ls-files --eol` pokazuje wszystkie 58 plików skilli i agentów jako `i/lf w/lf`.
- Wspólne pliki instalator porównuje już po wyrównaniu końcówek: `agents_change` w `installation/install.py` zestawia blok w `AGENTS.md` po `text.replace("\r\n", "\n")`, a przy zapisie bloku zachowuje końcówkę pliku.
- Plik z CRLF pozostawiony bez zmian niczego nie psuje w historii: git zapisuje go w repozytorium z LF tak samo jak plik z LF.
- Istniejące testy instalatora leżą w `installation/test_install.py`; test `test_preview_apply_rerun_and_preserve_foundation` sprawdza dziś odpowiedź „Already installed; no changes” po drugim uruchomieniu na drzewie z LF.
- Linia `Defect introduced by:` brzmi `none`, bo porównanie bajtów stoi od pierwszej wersji instalatora (`3b2a0cb`), a żadne zadanie ani wpis fundamentu nie wymagał niewrażliwości na końcówki linii — to luka, której wcześniejsze zadania nie przewidziały, nie odejście od wymagania.
- Zadanie powstało z linii backlogu: „the way: podgląd instalatora pokazuje „REPLACE” przy punktach wejścia skilli, których treść się nie zmienia, gdy produkt ma `core.autocrlf=true` (pliki w drzewie z CRLF, instalator pisze LF i porównuje surowe bajty) — porównywać po normalizacji końców linii”.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- WAY-34 — Which version of the process does a product use?: „A newer version of the process enters a product only in one commit of the product that moves the pin, made when a task of the product needs a change of the process […]” Zadanie tego nie zmienia; podgląd, którego dotyczy, to podgląd tego przesunięcia.
- WAY-328 — Does the-way hold its own code and tests to the general coding guidelines and the testing guidelines of a product?: „The-way departs, for its own code and its own tests, from the general coding guidelines and from the testing guidelines of a product, under WAY-217: in each part named in *Scope*, neither is missing, so a task of the-way that writes code, or writes or changes a test, in such a part waits for neither.” Część `installation` stoi w jej *Scope*, więc zadanie nie czeka na wytyczne.

## Settlements to record

Candidates: 1 shown, 0 accepted — 2026-11-14

none

## Out of scope

- Plik z prawdziwą zmianą treści instalator dalej zapisuje z końcówkami LF, jak dziś.
- Ustawienie gita na komputerze Mariusza (`core.autocrlf=input`) zostaje bez zmian.
