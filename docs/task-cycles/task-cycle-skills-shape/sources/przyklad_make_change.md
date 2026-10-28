---
title: "Przykład przebudowy: make-change przed i po"
status: draft
created: 2026-10-28
updated: 2026-10-28
tags: []
related: "[[(P) Proces pracy nad produktem]]"
---

Ocena skillem `the-way-maintain-instruction-files` (tryb oceny, rodzaj „skill”), na `task-cycle/change/SKILL.md` w `foundations` `cf11541` (1777 słów). Repo bez zmian.

Kto czyta skill: agent, którego orkiestrator cyklu wysyła z `make-change` w jednym z pięciu wariantów — jedyny autor zmiany, wykonawca kawałka planu (także ponowna próba kawałka), poprawka uwag przeglądu, korekta po uwagach człowieka do PR-a. Zlecenie mówi wprost, który to wariant (`SKILL.md:21–22`), więc moment „to jest mój wariant” agent rozpoznaje na starcie.

Skrypt sprawdzający: 0 błędów, 1 ostrzeżenie — `AGENTS.md:20` wskazuje `_zadania\`, folder w prywatnych notatkach autora, którego w repo nie ma; dotyczy pliku głównego, nie tego skilla.

## Tabela

| # | Fragment | Kiedy potrzebny / czy agent rozpozna moment | Werdykt | Powód | Podstawa |
|---|---|---|---|---|---|
| 1 | `:1–4` opis we frontmatterze | zawsze — wejście generowane do `the-way-make-change`; w cyklu zlecenie nazywa metodę wprost / nie ma momentu do rozpoznania | keep | opis jest wyzwalaczem i źródłem wejść | krok: WAY-127 |
| 2 | `:6–12` „Makes one change of a task…” — obraz całości | przy każdym użyciu / nie ma momentu | keep | obraz całości zostaje w `SKILL.md` | WAY-256 |
| 3 | `:14–15` gdzie leży the way | przy każdym użyciu (sięganie po fundament i skille elementów) / nie ma momentu | keep | jak wyżej | WAY-127 |
| 4 | `:19–22` „Read what your dispatch names…”, zlecenie | przy każdym użyciu / nie ma momentu | keep | wspólne dla wariantów | WAY-150 |
| 5 | `:23–25` jedyny autor: całe zadanie i spec | tylko wariant „jedyny autor” / tak — zlecenie mówi „the change” | keep, przeredagować na wiersz tabeli wariantów | jedna instrukcja; plik obok zastąpiłby ją jednym odsyłaczem i nic nie zmniejszył | krok cyklu (`task-cycle/skill/SKILL.md:144`) |
| 6 | `:24–28` kawałek: sekcja planu i fragmenty z *Read*, zadanie wiąże tam, gdzie plan mówi mniej | tylko wariant „kawałek” / tak — zlecenie podaje numer kawałka | move → `slice.md` | wytyczne jednego wariantu | WAY-148, WAY-229 |
| 7 | `:29–31` wpisy fundamentu i wytyczne ze zlecenia | przy każdym użyciu / nie ma momentu | keep | wspólne | WAY-213 |
| 8 | `:32–33` poprawka: plik uwag, Minor i spoza zakresu nie Twoje | tylko wariant „poprawka” / tak — zlecenie podaje plik uwag | move → `fix.md` | wytyczne jednego wariantu | WAY-161 |
| 9 | `:34` korekta: każda uwaga człowieka wiąże | tylko wariant „korekta” / tak | keep, wiersz tabeli wariantów | jedna instrukcja, jak w wierszu 5 | krok cyklu (`task-cycle/skill/SKILL.md:456`) |
| 10 | `:35–36` ponowna próba kawałka | tylko kawałek, i to ponawiany / tak — zlecenie podaje raport nieudanej próby | move → `slice.md` | wariant wariantu kawałka | krok cyklu |
| 11 | `:37` każdy zmieniany plik w całości | przy każdym użyciu / nie ma momentu | keep | wspólne | krok czynności |
| 12 | `:39–45` sięganie poza zlecenie | przy każdym użyciu, gdy czegoś brakuje / tak — brak widać w trakcie pracy | keep | wspólne | WAY-213, WAY-150 |
| 13 | `:47–50` wartość, która się nie zgadza; edycja próbna | przy każdym użyciu / tak | keep | wspólne | krok czynności |
| 14 | `:52–80` sekcja 2, testy (390 słów) | przy każdej zmianie z kodem — prawie każdej / tak | keep | dotyczy wszystkich wariantów; wyjątek „proza bez testu” sekcja sama nazywa | WAY-253 (mutacje), kroki czynności |
| 15 | `:84–86` sprawdzenie własnej pracy (wstawka o kawałku: 4 słowa) | przy każdym użyciu / nie ma momentu | keep | wspólne | WAY-164 |
| 16 | `:87–91` zmiana interfejsu: stany, zrzut ekranu | tylko gdy zmiana dotyka interfejsu / tak — agent wie, że zmienia ekran | move → `ui_check.md`; odsyłacz: „Before you finish a change that alters what a screen shows, read `ui_check.md`” | wytyczne jednego wariantu treści zmiany | WAY-219 |
| 17 | `:92–97` sprawdzenia skupione, bez pełnego zestawu; długie polecenie w tle | przy każdym użyciu / nie ma momentu | keep | wspólne | WAY-160, WAY-255 |
| 18 | `:99–105` sekcja 4, plan a kod | tylko kawałek (jedyny autor nie ma planu) / tak | move → `slice.md` | wytyczne jednego wariantu | krok cyklu |
| 19 | `:107–120` sekcja 5, powrót bez kodu (wstawka o kawałku: 1 zdanie) | przy każdym użyciu / tak — moment to wybór, którego zadanie nie rozstrzyga | keep; wstawkę o kawałku przenieść do `slice.md` | wspólne | WAY-135, WAY-136 |
| 20 | `:122–138`, `:141–150` commit i raport | przy każdym użyciu / nie ma momentu | keep | wspólne | WAY-148 |
| 21 | `:139` raport poprawki | tylko poprawka / tak | move → `fix.md` | razem z wierszem 8 | WAY-161 |
| 22 | `:140` raport korekty | tylko korekta / tak | keep, wiersz tabeli wariantów | jedna instrukcja | krok cyklu |

Sprzeczności między plikami ładowanymi razem: nie znalezione — sprawdzone z `task-cycle/skill/SKILL.md` w miejscach, które wysyłają `make-change` (`:280`, `:289`, `:293`, `:350`, `:381`, `:456`).

## Po przebudowie

```
task-cycle/change/
  SKILL.md       obraz całości; krok 1 zaczyna się tabelą wariantów:
                   jedyny autor → przeczytaj całe zadanie i spec (jedna linia)
                   kawałek / ponowna próba → przeczytaj `slice.md`
                   poprawka → przeczytaj `fix.md`
                   korekta → każda uwaga człowieka wiąże; w raporcie każda jako zrobiona i jak (jedna linia)
                 dalej wspólne: czytanie, testy, sprawdzenie własnej pracy (z odsyłaczem do `ui_check.md`),
                 powrót bez kodu, commit i raport
  slice.md       czytanie kawałka, ponowna próba, plan a kod (dziś sekcja 4), wstawki o kawałku z sekcji 3 i 5
  fix.md         plik uwag, Minor i spoza zakresu nie Twoje, raport poprawki
  ui_check.md    stany komponentów i zrzut ekranu
```

Ile czyta agent (słowa, w przybliżeniu): dziś każdy 1777. Po: jedyny autor bez zmiany interfejsu ok. 1450, kawałek ok. 1650, poprawka ok. 1500; zmiana interfejsu dokłada ok. 70.

Zysk w mierze serii: `make-change` niósł 12,0 mln tokenów od 2026-09-01; po przebudowie ok. 10–10,5 mln przy tej samej pracy. Zysk wymaga zmiany WAY-125 — bez niej agent wczyta wszystkie pliki na starcie.
