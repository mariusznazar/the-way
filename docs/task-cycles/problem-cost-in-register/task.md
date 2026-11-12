---
title: the way — koszt jednego wystąpienia problemu w rejestrze audytu procesu, obok wagi
status: draft
created: 2026-11-12
updated: 2026-11-12
tags: [zadanie]
related: "the project note of the process in the author's notes"
---

# Koszt jednego wystąpienia problemu w rejestrze audytu procesu, obok wagi

Status: ready for cycle
Project relation: independent

## Description

### Need

- Rejestr problemów audytu daje każdemu problemowi wagę w skali ocen przeglądu cyklu (no problem, Minor, Important, Critical); waga mówi, jak bardzo problem zagroził zmianie, ale nie mówi, ile kosztował.
- Przy uwagach o tarciu procesu waga zlewa się w Minor, choć jedna uwaga kosztuje kilka kroków agenta (powtórzone polecenie, zła ścieżka i wyszukiwanie), a inna całą dodatkową rundę agentów (osobne uzgodnienie z gałęzią docelową ze świeżym przeglądem i pełną bramką).
- Mariusz na cotygodniowym audycie waży, ile kosztuje nawrót sprawy, a ile jej poprawka, i dziś rejestr nie daje mu do tego żadnego materiału o koszcie.

### To do

1. Szablon rejestru `process-audit/problem_register.md` dostaje w tabeli *Problems* kolumnę kosztu jednego wystąpienia problemu oraz, obok tabeli *Weights*, tabelę pięciu stałych poziomów kosztu z ich znaczeniami, które użytkownik może dostosować, nie zmieniając poziomów.
2. Polecenie liczące `process-audit/audit_count.py` czyta koszt każdego problemu i odrzuca wiersz, którego koszt nie jest poziomem z tabeli poziomów, tak jak dziś odrzuca nieznaną wagę; tabelę poziomów, która nie ma dokładnie tych pięciu poziomów, traktuje tak, jak dziś tabelę wag bez czterech poziomów wagi.
3. Wynik liczenia przy każdej sprawie poprawionej, otwartej i porzuconej podaje, ile jej problemów stoi na każdym poziomie kosztu.
4. Skill audytu `process-audit/SKILL.md` pokazuje człowiekowi koszt przy sprawach jako materiał do ważenia, bez ustawiania z niego priorytetu ani kolejności.

### Questions to settle

- Czy poziomy kosztu są stałe w the-way, jak poziomy wagi, czy są listą, którą użytkownik prowadzi i poszerza, jak klasy?
  - Answer: stałe w the-way, jak poziomy wagi; użytkownik zmienia tylko ich znaczenia.
  - Not chosen:
    - lista prowadzona i poszerzana przez użytkownika, jak klasy — polecenie liczące nie zna kolejności poziomów, więc koszt staje się kategorią, nie skalą, a każda zmiana listy przerywa serię pomiarów, jak dziś zmiana listy klas
  - Source: Mariusz, 2026-11-12: „tak, mają być stałe”
- Jakie poziomy ma skala kosztu?
  - Answer: pięć poziomów, każdy droższy od poprzedniego; problem dostaje najwyższy poziom, do którego sięgnął jego faktyczny koszt (to, co mogło się stać, mówi waga):
    - `nothing` — wystąpienie nic nie kosztowało: potwierdzenie albo uwaga bez skutku;
    - `steps` — kilka kroków jednego agenta w jego etapie, które agent sam naprawił: ponowione polecenie, zła ścieżka i wyszukiwanie, powtórzony odczyt;
    - `stage` — etap albo jego spora część zrobiona jeszcze raz, albo duża dodatkowa lektura czy sprawdzenie u tego samego agenta;
    - `round` — dodatkowe uruchomienie agenta: runda poprawek, dodatkowe uzgodnienie z gałęzią docelową, nowy przegląd, ponowiony kawałek;
    - `human` — czas człowieka: pytanie, decyzja, ręczne sprawdzenie, poprawka po scaleniu.
  - Not chosen:
    - cztery poziomy, bez `stage` — łatwiej je przydzielić, ale ponowione polecenie i ponowna lektura kilkuset kilobajtów fundamentu lądują na tym samym poziomie
    - `human` poza skalą, jako osobna oś — czas człowieka to inna waluta niż tokeny agentów, ale każdy wiersz dostaje trzecią ocenę, a wynik liczenia trzecią oś
  - Source: Mariusz, 2026-11-12: „5 poziomów”, na propozycję pięciu poziomów pokazaną w rozmowie
- Gdzie wynik liczenia pokazuje koszt: przy cyklach, przy sprawach, czy w obu miejscach?
  - Answer: przy sprawach — przy każdej sprawie poprawionej, otwartej i porzuconej wynik podaje, ile jej problemów stoi na każdym poziomie kosztu.
  - Not chosen:
    - przy cyklach, jako druga tabela „klasa × koszt” obok „klasa × waga” — żaden krok sesji audytu jej nie czyta, a to, czy cykle tanieją, mierzy już koszt cyklu (WAY-337)
    - w obu miejscach — wynik dłuższy, a połowa nowych liczb trafia do tabeli, której sesja nie czyta
  - Source: Mariusz, 2026-11-12: „przy sprawach”

## Context

- Polecenie liczące znajduje tabelę rejestru po dokładnym wierszu nagłówka (`process-audit/audit_count.py:1391` @ 55afa8e), więc rejestr bez nowej kolumny zostanie po zmianie odrzucony; brak pola kończy się błędem, który je nazywa (WAY-344).
- Rejestr Mariusza ma na 2026-11-12 pustą tabelę *Problems*, więc przejście nie przenosi żadnych wierszy.
- Wiersze rejestru dopisuje nocna sesja przeglądu zapisów cykli, narzędzie Mariusza poza the-way (WAY-330); jej reguły zmienia Mariusz, nie cykl tego zadania.
- Na to zadanie czeka ocena wsteczna zapisów cykli od 29.10.2026, żeby jej wiersze dostały koszt od razu, a nie w drugim przejściu.
- Na próbce oceny wstecznej 2026-11-12 waga i koszt rozdzieliły przypadki, których sama waga nie odróżnia: kolizja numeru decyzji przy scaleniu wyszła Minor, ale kosztowała rundę; edycja w głównej kopii repozytorium wyszła Important, ale kosztowała kilka kroków.

## Questions carried to cycle

none

## Human actions

- Dopisać kolumnę kosztu i tabelę poziomów do własnej kopii rejestru i koszt do reguł nocnej sesji, która go wypełnia — in the cycle (Mariusz, 2026-11-12: przy PR-ze poprosi cykl, żeby zrobił to w Obsidianie)

## Decisions in play

- WAY-330 — Where does the audit of the process get the class and weight of each problem, and the tie of a problem to the fix meant to remove it? — „The-way gives a template of a register of problems, which holds for each problem the cycle it comes from, its class and weight, the issue it belongs to — the one matter that like problems of several cycles make — and that issue's fate, the fix of an implemented issue included. A user's own tool fills the register and the user adapts the template to their own needs; the audit reads the register that an entry of the user's locations file names and gives no problem a class or a weight itself.”
  - Zmiana, którą wprowadza zadanie: rejestr trzyma dla każdego problemu także koszt jednego wystąpienia na stałej skali pięciu poziomów, a audyt nie nadaje go sam, tak jak klasy i wagi.
- WAY-328 — Does the-way hold its own code and tests to the general coding guidelines and the testing guidelines of a product? — „The-way departs, for its own code and its own tests, from the general coding guidelines and from the testing guidelines of a product, under WAY-217: in each part named in *Scope*, neither is missing, so a task of the-way that writes code, or writes or changes a test, in such a part waits for neither.”
- WAY-333 — How is a problem that the audit counts graded and classed? — „Each problem the audit counts has a weight on a scale of four levels — no problem, Minor, Important and Critical — and a class from a list that the template of the register starts and the audit widens. Minor, Important and Critical are the grades of the review of a cycle (WAY-161), and no problem is the level below them.”
- WAY-336 — Does how often an issue comes back set its priority? — „How often an issue comes back is material that the audit shows the human to weigh; the audit sets no priority from it and ranks no issue by the number of its returns.”
- WAY-339 — When do the measures of the audit stop being comparable? — „A new price list, or a change of the form of a stage report, of the list of classes or of the instructions of the reviewer, starts a new series of measures. The audit compares measures only within one series, and judges a version of the process by the cycles that ran on it, never one week against another.”
- WAY-344 — What does a script of the-way do when a file it reads lacks a field it needs? — „A script of the-way that reads a file an agent or a human writes checks that the file holds each field the script needs — a field being any named thing the script looks for data by in the file: a section heading, a row label, a table column or a JSON key — and where a field is missing or stands under another name the script ends with an error that names it, never guessing and never reading the absence as an empty value.”

## Settlements to record

Candidates: 6 shown, 3 accepted — 2026-11-12

| # | Settlement | Kind | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Skala kosztu ma pięć stałych poziomów — `nothing`, `steps`, `stage`, `round`, `human` — każdy droższy od poprzedniego; problem dostaje najwyższy poziom, do którego sięgnął jego koszt, a użytkownik dostosowuje tylko znaczenia poziomów. | decision | *Questions to settle*: pytania o stałość poziomów i o poziomy skali | ile poziomów i jakie, czy użytkownik może dodać poziom, który poziom dostaje problem kosztujący na kilku poziomach |
| 2 | Wynik liczenia pokazuje koszt przy sprawach — przy każdej sprawie poprawionej, otwartej i porzuconej liczbę jej problemów na każdym poziomie kosztu — a nie przy cyklach. | decision | *Questions to settle*: pytanie o miejsce kosztu w wyniku liczenia | czy dodać tabelę kosztu przy cyklach, przy sprawach, czy w obu miejscach |
| 3 | „Koszt wystąpienia” problemu to poziom na skali pięciu poziomów, czym innym niż koszt cyklu, który audyt podaje w pieniądzach po stałych cenach (WAY-337). | glossary term | wynik liczenia ma już sekcję *Cost* z kosztem cykli (`process-audit/audit_count.py:2012` @ 55afa8e), a zadanie wprowadza drugi „koszt” | jak nazwać kolumnę i tabelę poziomów, żeby nie zlały się z sekcją *Cost* wyniku |

## Out of scope

- Ocena wsteczna zapisów cykli do rejestru — osobna robota w vaulcie, która czeka na to zadanie.
