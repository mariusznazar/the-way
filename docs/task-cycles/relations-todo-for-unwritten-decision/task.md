---
title: the way: zadanie oparte na zaplanowanej, jeszcze niezapisanej decyzji nie ma jak jej wskazać i staje przed scaleniem
status: draft
created: 2026-10-25T16:00
updated: 2026-11-14
tags: [zadanie]
related: "a note of the author's backlog"
---

## Po co to

- **Jak jest dziś:** Gdy decyzja pisana w zadaniu produktu wywodzi się z decyzji, która jest już zaplanowana i zatwierdzona w definicji projektu, ale jeszcze nie trafiła do spisanych zasad produktu, pole *Relations* nie ma dozwolonego zapisu tego powiązania — PR staje przed scaleniem. Dla reguł (niezmienników) tę samą lukę zamknęła zmiana z 2026-11-11; dla decyzji ta sama zmiana `TODO` w *Relations* wprost zakazała.
- **Kto to odczuwa:** Ty — przy scalaniu takiego PR-a dostajesz dodatkowe wpisy do zaakceptowania albo PR stoi zablokowany. Agent prowadzący zadanie ma do wyboru same złe drogi: wpisać nieprawdę („brak powiązania”), zostawić „do zrobienia” i zablokować scalenie albo dopisać wpis częściowy.
- **Co jeśli nic:** Wystąpiło raz — w `loop2`, PR #3 (szkielet aplikacji), obejście trzema wpisami częściowymi, każdy do Twojej akceptacji. Przypadek, którego obejście nie załatwi (kod nie spełnia żadnej części zaplanowanej decyzji), na razie nie wystąpił; może się pojawić w każdym zadaniu, które bierze definicję projektu za źródło.

# the way: decyzja wywodząca się z decyzji jeszcze niezapisanej dostaje w *Relations* opisowe `TODO`

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- Decyzja pisana w cyklu zadania produktu może wywodzić się z decyzji, której fundament produktu jeszcze nie ma — najczęściej z decyzji zaprojektowanej w zatwierdzonej definicji projektu, której żaden kod jeszcze nie spełnia, więc nie wolno jej zapisać (WAY-126).
- WAY-17 każe zapisać to powiązanie w *Relations* decyzji zależnej, a WAY-71 nie daje *Relations* żadnej postaci dla decyzji, której fundament nie ma: `none` jest nieprawdą, a `TODO` odrzuca skrypt sprawdzający fundament.
- Wpis częściowy z WAY-126 pozwala obejść lukę, gdy kod spełnia część decyzji zaprojektowanej, kosztem dodatkowego wpisu do akceptacji Mariusza; gdy kod nie spełnia żadnej części, obejścia nie ma i PR stoi.
- *Derives from* niezmiennika ma już na gałęzi głównej postać `TODO — <the decision, and where it is expected>`; zadanie daje tę samą postać *Relations* decyzji.
- Odbiorcą jest Mariusz, który rozstrzyga taki przypadek przy scaleniu, oraz agent cyklu, który dziś nie ma prawdziwego zapisu do wyboru.

### To do

1. WAY-71 (przez skill zapisu decyzji, `record-decision`): zdanie wiążące, które otwiera „The main branch holds `TODO` only where an entry stands on something the product's foundation does not hold yet”, wymienia obok *Rests on*, *Derives from* i *Based on* także *Relations* decyzji, w postaci `TODO — <the decision, and where it is expected>`, dla decyzji, z której wpis się wywodzi, a której fundament jeszcze nie ma — każdej, nie tylko zaprojektowanej w definicji projektu; po znanych powiązaniach stoi jako ostatnia pozycja, jak w pozostałych polach. *Origin* zostaje bez `TODO`. Uzasadnienie (zdanie „*Relations* and *Origin* are what an author states about the entry itself when writing it, so a gap there is a field left unfilled, never a thing the foundation lacks.”), *Verification* (przykład naruszenia „a decision reads `TODO` in *Relations* or *Origin*”) i *Rejected* idą za zmianą, jak podaje *Decisions in play*.
2. `elements/common/rules.md`, sekcja „Every field, and the words `none` and `TODO`”, punkt otwierany „The main branch holds `TODO` only where” (ok. linii 20): to samo co w punkcie 1.
3. `elements/decisions/template.md`: w bloku „Decision entry” linia `- **Relations:** derives from WAY-x · narrows WAY-y | none` dostaje postać `TODO — <the decision, and where it is expected>`; zdanie „*Relations* and *Origin* never read `TODO`: the script reports it (WAY-71).” mówi odtąd, że *Origin* nigdy nie czyta `TODO`, a *Relations* bierze tylko postać opisową, i że gołe `TODO` w *Relations* skrypt zgłasza jako błąd.
4. `elements/common/foundation_check.py` przyjmuje w *Relations* decyzji opisowe `TODO`, jako jedyną albo ostatnią pozycję po znanych powiązaniach, tak jak dziś w *Rests on*, *Derives from* i *Based on* (słownik `MISSING`, warunek *Relations* w `DECISION_WORDS`), nie traktuje go jako odwołania do wpisu, a gołe `TODO` w *Relations* zgłasza jako błąd z podpowiedzią postaci; docstring (akapit „In an invariant's *Rests on* or *Derives from*, or a decision's *Based on*”) idzie za tym. `elements/common/test_foundation_check.py` ma przypadki: samo opisowe `TODO`, `derives from WAY-x · TODO — …` z dalej sprawdzanym `WAY-x`, gołe `TODO` jako błąd.
5. WAY-126 (przez `record-decision`) dostaje zdanie wiążące: zmiana, która zapisuje do fundamentu wpis zaprojektowany, zastępuje jego identyfikatorem każde opisowe `TODO`, które go wskazuje — w *Relations* decyzji i w *Derives from* niezmiennika.
6. `task-cycle/skill/request_template.md`, punkt **16.** („*Something an entry stands on that the foundation does not hold yet*”): lista opisowych `TODO`, które opis PR-a pokazuje człowiekowi, obejmuje też `TODO — <the decision, and where it is expected>` w *Relations* decyzji.

### Questions to settle

- Czy zmieniamy regułę, a jeśli tak — jaką postać dostaje *Relations* decyzji dla decyzji jeszcze niezapisanej?
  - Answer: tak — *Relations* decyzji dostaje tę samą postać, którą od 2026-11-11 ma *Derives from* niezmiennika: `TODO — <the decision, and where it is expected>`, na końcu listy powiązań; zmienia to WAY-71, wspólne reguły, szablon decyzji i skrypt sprawdzający fundament z testami, bez sprawdzania definicji projektu przez skrypt.
  - Not chosen:
    - postać `TODO — projected: <definicja>, <pytanie wpisu>`, którą skrypt sprawdza z definicją — martwe odwołania wychwyci automat, ale koszt wyraźnie większy: skrypt fundamentu musiałby czytać definicje projektów, a w polu powiązań stanęłaby druga postać obok tej, którą mają niezmienniki.
    - wpis częściowy z WAY-126 jako droga domyślna — zmienia się tylko tekst, ale jedynego przypadku, który został w zakresie („kod nie spełnia żadnej części”), to nie rozwiązuje.
    - zamknąć zadanie bez zmiany — dziś nic nie kosztuje; przy wystąpieniu kosztuje zablokowany PR i jedną turę Mariusza.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, „1 a” (wariant: dopuścić w *Relations* postać z *Derives from* niezmiennika).
- Czy postać obejmuje każdą decyzję jeszcze niezapisaną, czy tylko zaprojektowaną w zatwierdzonej definicji?
  - Answer: każdą decyzję, której fundament jeszcze nie ma, jak u niezmienników.
  - Not chosen:
    - tylko decyzję zaprojektowaną w zatwierdzonej definicji — węższa furtka, ale reguła *Relations* różniłaby się od reguły *Derives from*, a ograniczenia nikt nie sprawdzałby automatycznie.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, „2 a”.
- Czy WAY-126 ma wprost kazać zadaniu, które zapisuje wpis zaprojektowany, zastąpić odsyłające do niego `TODO` jego identyfikatorem?
  - Answer: tak — jedno zdanie w WAY-126, obejmujące *Relations* decyzji i *Derives from* niezmiennika.
  - Not chosen:
    - zostawić to ogólnej WAY-37 i przeszukaniu całego fundamentu (WAY-33) — nic nie kosztuje, ale przykłady WAY-37 to szablon, mapa części i skrypt, więc agent musi sam skojarzyć, że wpis czeka też na decyzję.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, „3 a”.
- Czy brak własnych wytycznych kodowania i testów the way wstrzymuje to zadanie (WAY-215), skoro zmienia skrypt i jego testy?
  - Answer: nie wstrzymuje — zadanie idzie jak dotychczasowe zadania the way; sprawa wytycznych zostaje przy zadaniu „Ustalić, czy rozwój the way wymaga własnych wytycznych kodowania i testów”.
  - Not chosen:
    - wstrzymać zadanie do tamtego zadania — tamto nie ma wybranego kierunku, więc czekanie nie ma końca.
  - Source: doradca dnia w imieniu Mariusza, 2026-11-14, „4 a”.

## Context

- Źródło: sprawa AIR-469 w archiwum rejestru przeglądów warstwy AI w prywatnych notatkach Mariusza; uwaga cyklu `loop2@5928e7b:docs/task-cycles/app-skeleton/cycle.md:141` — „(1) the-way has no main-branch form for a relation to a projected entry not yet written (T11)”.
- W PR #3 `loop2` cykl obszedł lukę wpisami częściowymi D-04, D-05 i D-07; od tamtej pory (2026-10-05) w historii `foundations/decisions.md` `loop2` żadna decyzja nie miała `TODO` w *Relations* — stan na 2026-11-14.
- Zmiana `10d443f` z 2026-11-11 (PR #97) dopuściła opisowe `TODO` w *Derives from* niezmiennika i *Based on* decyzji, a w *Relations* i *Origin* decyzji je odrzuciła; zadanie zbiorcze, z którego wyszła, dotyczyło *Rests on* i nie rozważało decyzji zaprojektowanej.
- Postać `TODO — <the decision, and where it is expected>` stoi dziś w the way w `elements/common/foundation_check.py` (docstring i słownik `MISSING`), `elements/common/rules.md`, `elements/invariants/template.md`, WAY-71 i `task-cycle/skill/request_template.md` — rewizja `6fa755c`.
- Opisowe `TODO` zamyka wartość pola: opis biegnie do jej końca, więc przecinek ani ` · ` w nim niczego nie dzielą (szablon decyzji, punkt o *Based on*).
- WAY-32 zna dwa typy powiązań, `derives from` i `narrows`; z decyzją jeszcze niezapisaną żadna nie może się zderzyć, więc w praktyce `TODO` w *Relations* wskazuje decyzję, z której wpis się wywodzi.
- the way nie ma katalogu `guidelines/`; sprawą własnych wytycznych the way zajmuje się osobne zadanie „Ustalić, czy rozwój the way wymaga własnych wytycznych kodowania i testów”.
- Możliwy duplikat ze sprawy AIR-469 („część uwag zrobiłeś poza PR-em”) się nie potwierdził: na `foundations` @ `6fa755c` skrypt dalej odrzuca `TODO` w *Relations*.

## Questions carried to cycle

none

## Human actions

none

## Decisions in play

- **WAY-71 — Does every field of a foundation entry appear in every entry, and what may it hold?** Zadanie zmienia zdanie wiążące, uzasadnienie i *Verification*, jak podaje To do 1, a do *Rejected* dopisuje drogi niewybrane z pytań 1 i 2 (Mariusz przez doradcę dnia, 2026-11-14, „1 a, 2 a”): postać `TODO — projected: <definition>, <question>` sprawdzana przez skrypt z definicją; wpis częściowy jako jedyna droga; tylko decyzja zaprojektowana w zatwierdzonej definicji.
  > Every field an element's template gives an entry of its kind appears in every entry of its kind, holding a value, or `none` or `TODO` where the template gives it that word: `none` says nothing is there, `TODO` that something is missing. The main branch holds `TODO` only where an entry stands on something the product's foundation does not hold yet: in an invariant's *Rests on*, in the form `TODO — <the fact, with its source>`; in an invariant's *Derives from*, in the form `TODO — <the decision, and where it is expected>`; and in a decision's *Based on*, in the form `TODO — <what is missing, with its source>`; where an entry stands on several things and only some are missing, the missing one is the last item of the value and reads as the form of its field, after the known items; a change that leaves one there puts it before the human. `elements/common/foundation_check.py` reports a missing field, or a word not given it, as an error.
  >
  > *Rationale:* … *Relations* and *Origin* are what an author states about the entry itself when writing it, so a gap there is a field left unfilled, never a thing the foundation lacks.
- **WAY-126 — How does a projected entry enter the foundation?** Zadanie dopisuje zdanie wiążące z To do 5 (Mariusz przez doradcę dnia, 2026-11-14, „3 a”); reszta bez zmiany.
  > A projected entry of an approved project definition enters the product's foundation in the change of the first task whose code makes it true — the task the plan assigns, or a task that uses the definition as a source only, even where the plan assigns the entry to another task — whole, in the wording the readiness gate approved, with the projected terms and environment facts it uses or rests on and with no record of approval copied from the gate, since the merge of the task's request brings it in; where the code makes only part of it true, the agent writes that part and the human accepts its meaning at the merge (WAY-114). The task the plan assigns writes what of the entry the foundation does not yet hold, and a projected entry no code makes true. The return step reads the projected entries of the task's sources as well as the foundation, writes one the code makes true that the foundation step missed — an invariant with its test run on that code — and writes a new entry only for a rule none of them states.
- **WAY-17 — Which links between foundation entries are mandatory?** Bez zmiany; to z niej wynika obowiązek zapisania powiązania.
  > Every link of the chain fact → decision → invariant → test is written in the entry that depends on the other, and none is optional: a decision and an invariant name the environment facts they rest on, an invariant derived from a decision names that decision, and a check names its invariant.
- **WAY-37 — What happens to entries that wait for something when it arrives?** Bez zmiany; WAY-126 po zmianie stosuje ją wprost do wpisu zaprojektowanego.
  > A change that brings what entries of the foundation wait for — an element's template, the part map, a script — also fixes every entry that waits for it, in the same change. The author of the change finds those entries in its one search of the whole foundation (WAY-33).
- **WAY-32 — What types of relation can a decision name?** Bez zmiany; opisowe `TODO` nie jest trzecim typem powiązania, tylko luką w miejscu powiązania, którego jeszcze nie da się nazwać.
  > A decision names its relation to another decision with one of two types, and the list is closed: `derives from` — a higher decision this one serves; `narrows` — a decision this one deliberately goes against in a narrower area.
- **WAY-287 — What does a request put before the human for a decision?** Bez zmiany; To do 6 poszerza listę w szablonie opisu PR-a, który ją realizuje (punkt 16).

## Settlements to record

Candidates: 3 shown, 0 accepted — 2026-11-14

none

## Out of scope

- Sprawdzanie przez skrypt, czy opisowe `TODO` wskazuje istniejącą definicję i jej wpis — odrzucone w pytaniu 1.
- *Origin* decyzji — zostaje bez `TODO`.
- Nowe przypięcie the way w `loop2` i przegląd wpisów częściowych D-04, D-05, D-07 w `loop2` — sprawa `loop2`, nie tego zadania.

## Pierwotne brzmienie zadania

> the way: dozwolona na głównej gałęzi postać odwołania do wpisu zaprojektowanego w zatwierdzonej definicji, którego fundament jeszcze nie ma (*Relations* decyzji, *Derives from* niezmiennika); wpis częściowy z WAY-126 pokrywa większość przypadków — luka zostaje, gdy kod nie spełnia żadnej części wpisu — sprawa AIR-469 w zeszycie ai-review lub archiwum
