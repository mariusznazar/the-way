---
title: "the way: skille do rozwijania frameworka nie mają trafiać do produktów, które podpinają go jako podmoduł"
status: draft
created: 2026-11-21T11:00
updated: 2026-11-21
tags: [zadanie]
related: "a link to the author's project note"
---

# the way: skille do rozwijania frameworka nie mają trafiać do produktów, które podpinają go jako podmoduł

Status: ready for cycle
Project relation: independent
Defect introduced by: none

## Description

### Need

- W produkcie, który podpina the way jako podmoduł `.the-way` (dziś loop2), sesja po pierwszym odczycie pliku z `.the-way/` dostaje drugi komplet skilli the way: 23 wejścia z `.the-way/.claude/skills/`, które służą do rozwijania samego frameworka.
- 21 z nich dubluje nazwą wejścia produktu i pojawia się z przedrostkiem `.the-way:`, a dwa (`the-way-audit-process`, `the-way-maintain-instruction-files`) w produkcie są zbędne.
- Nic nie idzie źle, bo te wejścia same rozpoznają produkt i odsyłają do skilli produktu, ale lista skilli dochodzi do limitu długości, więc opisy wszystkich skilli są przycinane, a agent wybiera skill po opisie.
- Odczuwają to sesje prowadzące projekt i cykle w loop2 oraz ich podagenci: w tygodniu 15–21.11 dotyczyło to 90 ze 101 startów podagentów ogólnych w loop2.
- Koszt: ok. 4 tys. tokenów na start podagenta, ok. 30 USD w miesiącu na produkt tej skali; każdy kolejny produkt na the way dostanie to samo.

### To do

1. Każde wejście do skilla the way, które generuje `agent-instructions/skill_entry_points.py` (`.claude/skills/the-way-<nazwa>/SKILL.md` i jego kopia w `.agents/skills/`), ma w nagłówku `disable-model-invocation: true`, więc Claude Code nie pokazuje go modelowi ani w repozytorium the way, ani w produkcie, który niesie je w `.the-way/`.
2. W sesji na samym the way, tam, gdzie wejście albo skill the way każe użyć innego skilla the way, sesja dociera do niego, czytając jego `SKILL.md` po ścieżce w checkoucie albo worktree, w którym pracuje, a nie wywołując skill — model nie może już wywołać ukrytego skilla. W produkcie przekazanie zostaje bez zmian: przez wejście produktu, które pisze instalator.
3. Sekcja `## Skills` w `AGENTS.md` the way mówi, że skille the way uruchamia człowiek, w Claude Code poleceniem `/the-way-<nazwa>`, a skill przekazuje pracę innemu przez jego plik.

### Acceptance criteria

- Sesja Claude Code wystartowana w repozytorium, które ma w podkatalogu wygenerowane wejścia the way w `.claude/skills/`, po przeczytaniu pliku z tego podkatalogu nie ma żadnego z tych wejść na liście skilli podanej modelowi — sprawdzone raz w prawdziwej sesji; stały test sprawdza samo pole w nagłówku obu kopii.
- Sesja w repozytorium the way dalej uruchamia każdy skill the way poleceniem `/the-way-<nazwa>`, a skill the way odsyłający do innego skilla the way dalej prowadzi do jego kopii z checkoutu albo worktree, w którym sesja pracuje.

### Questions to settle

- Którędy wejścia do rozwijania the way mają znikać z listy skilli sesji w produkcie?
  - Answer: a — pole `disable-model-invocation: true` we wszystkich wejściach, dopisywane przez `skill_entry_points.py`; sesje na the way Mariusz zaczyna od `/the-way-…`, więc koszt luźnej prośby bez ukośnika jest bliski zeru, a cofnięcie to jedna zmiana skryptu.
  - Not chosen:
    - b) instalator dopisuje `skillOverrides: "off"` w `.claude/settings.json` produktu przy przestawieniu przypięcia — dokumentacja Claude Code mówi, że w ustawieniach projektu wpisy pasują tylko do nazw skilli, więc nazwa bez przedrostka schowałaby też własne wejście produktu (21 z 23), a działanie nazwy z przedrostkiem `.the-way:` nie jest opisane; instalator zacząłby pisać w ustawieniach produktu; cofnięcie średnie, w każdym produkcie.
    - wejścia w the way nieśledzone przez gita, generowane lokalnie przy instalacji kopii roboczej albo hookiem startu sesji — każdy cykl the way pracuje w świeżym worktree, który startowałby bez wejść, tak samo świeży klon i sesja w chmurze; WAY-127 już ten wariant odrzuca.
    - ręczna lista wyłączeń w ustawieniach loop2 — gdy the way dołoży skill, lista zestarzeje się po cichu i nowy duplikat wróci (Mariusz, 21.11, przy zakładaniu zadania).
  - Source: doradca dnia w imieniu Mariusza (tryb samodzielny), 2026-11-21: „1 a — pole disable-model-invocation: true dopisywane przez skill_entry_points.py; sesje na the way Mariusz zaczyna od /the-way-…, więc koszt luźnej prośby jest bliski zeru, a cofnięcie to jedna zmiana skryptu.” — oraz o wariancie nieśledzonym: „Jeśli przegrywa — zostaje a bez dyskusji.”
- Czy w produkcie skille the way też przekazują sobie pracę przez czytanie pliku?
  - Answer: a — czytanie pliku tylko w repozytorium the way; produkt bez zmian, zachowuje sprawdzenie przypięcia, a akapit o miejscu the way i tak rozdziela oba przypadki.
  - Not chosen:
    - b) czytanie pliku wszędzie — produkt traci sprawdzenie przypięcia przy przekazaniu, a zachowanie produktów zmienia się bez potrzeby tego zadania.
  - Source: doradca dnia w imieniu Mariusza (tryb samodzielny), 2026-11-21: „1 a — czytanie pliku tylko w repozytorium the way, produkt bez zmian (zachowuje sprawdzenie przypięcia; akapit i tak rozdziela oba przypadki).”

## Context

- Mechanizm: Claude Code wczytuje skille z `.claude/skills/` podkatalogu poniżej katalogu startu przy pierwszym odczycie albo edycji pliku w tym podkatalogu i trzyma je do końca sesji (fakt środowiska `claude-code-nested-skills` w fundamencie the way).
- Każde `.claude/skills/` w korzeniu the way staje się w produkcie zagnieżdżonym `.the-way/.claude/skills/`, a sesja na the way startuje w korzeniu the way, więc samo przeniesienie wejść w inne miejsce repozytorium nie rozdzieli obu przypadków.
- Dokumentacja Claude Code (https://code.claude.com/docs/en/skills, czytana 2026-11-21), § Restrict Claude's skill access: „**Hide individual skills** by adding `disable-model-invocation: true` to their frontmatter. This removes the skill from Claude's context entirely.”
- Ta sama strona, tabela „Control who invokes a skill”: przy `disable-model-invocation: true` Claude nie wywołuje skilla sam, a człowiek dalej może go wywołać poleceniem `/nazwa`.
- Ta sama strona, § Override skill visibility from settings: „In user, project, and local settings, Claude Code matches entries against skill names only.” — strona nie mówi, czy klucz z przedrostkiem katalogu (`.the-way:the-way-plan-task`) się dopasuje.
- Ta sama strona, § Restrict Claude's skill access: reguła `deny` z nazwą bez przedrostka (`Skill(deploy)`) blokuje też skill zagnieżdżony wypisany jako `apps/web:deploy`; strona nie mówi, czy zablokowany skill znika z listy.
- Codex wczytuje `.agents/skills` tylko od katalogu bieżącego w górę do korzenia repozytorium (fakt `codex-repository-skills`), więc w produkcie kopie z `.the-way/.agents/skills/` go nie dotyczą.
- Pomiar z 21.11 i skrypt do sprawdzenia skutku: notatka `anatomia_kosztu_sesji_dane/start_po_zmianie.md`, sekcja 2, i skrypt `09_start_po_zmianie.py` w tym samym katalogu notatek autora (prywatne, poza repozytorium).
- Wejścia w `loop2/.claude/skills/the-way-*` pisze instalator the way przy przestawieniu przypięcia; z nich loop2 korzysta i zadanie ich nie zmienia.
- `instruction-files/tool_loading.md`, punkt „Skills in context”, już opisuje to pole: opis skilla jest w kontekście każdej sesji, chyba że skill ma `disable-model-invocation: true`.
- Skutek w loop2 widać dopiero po przestawieniu jego przypięcia: podagent ogólny uruchomiony z sesji, która przeczytała plik z `.the-way/`, ma startować z tyloma skillami, ile ma produkt (w pomiarze z 21.11: 58), nie z 81 — w załączniku `skill_listing` na początku zapisu jego sesji.

## Questions carried to cycle

- Czy Codex wczytuje skill z `.agents/skills/`, którego nagłówek ma pole `disable-model-invocation`, i czy dalej go uruchamia? Gdyby nie, kopie w `.claude/skills/` i `.agents/skills/` musiałyby się różnić, czego dziś zabrania niezmiennik `skill-entry-points` — wtedy cykl pyta Mariusza, zanim je rozdzieli.

## Human actions

none

## Decisions in play

- WAY-127 — How does a session working on the-way itself reach the-way's skills? (`foundations/decisions.md`): „A session working on the-way itself reaches each skill of the-way as the project skill `the-way-<name>` through two identical tracked entry points, `.claude/skills/the-way-<name>/SKILL.md` and `.agents/skills/the-way-<name>/SKILL.md`, which a script of `agent-instructions` generates from the skill's `SKILL.md`. An entry point reads its skill, and each file the skill names when the step that names that file comes rather than all of them at the start, from the checkout or worktree the session works in — where it was started, or where it was last moved — stops itself in a product, and hands another the-way skill on under the `the-way-` prefix. No global link reaches a skill of the-way other than one to `instruction-files/`, whose skill, judging a repository that pins the-way, follows that repository's pinned copy instead, and the-way is not installed in itself.”
  - Zmiana, którą robi zadanie (odpowiedź a na pytanie wyżej): wejście ma w nagłówku `disable-model-invocation: true`, więc model go nie widzi ani nie wywołuje; człowiek uruchamia skill poleceniem `/the-way-<name>`, a w sesji na samym the way skill przekazuje pracę innemu skillowi the way przez jego `SKILL.md` czytany po ścieżce w checkoucie albo worktree sesji, nie przez wywołanie skilla z przedrostkiem; w produkcie przekazanie idzie dalej przez wejście produktu (odpowiedź a na drugie pytanie). Za tym idą *Rationale* i *Verification* decyzji oraz niezmiennik `skill-entry-points`, który z niej wynika.

## Settlements to record

Candidates: 2 shown, 2 accepted — 2026-11-21

| # | Settlement | Goes to | Source | What the cycle would otherwise guess |
|---|---|---|---|---|
| 1 | Wejścia do skilli the way mają w nagłówku `disable-model-invocation: true`, więc model ich nie widzi ani w the way, ani w produkcie; człowiek uruchamia je przez `/the-way-…`, a w sesji na samym the way skill przekazuje pracę innemu przez jego plik czytany po ścieżce, w produkcie bez zmian. | sentence of WAY-127 | pytania „Którędy wejścia do rozwijania the way mają znikać z listy skilli sesji w produkcie?” i „Czy w produkcie skille the way też przekazują sobie pracę przez czytanie pliku?” (ich *Not chosen*) | czy chować wejścia polem w nagłówku, czy wpisem instalatora w ustawieniach produktu, i czy skille dalej przekazują sobie pracę wywołaniem skilla |
| 2 | Claude Code usuwa z kontekstu modelu skill z `disable-model-invocation: true` (opis znika z listy, model go nie wywołuje), a człowiek dalej uruchamia go poleceniem `/nazwa`; decyzja ma stać na fakcie, który wyjdzie przy przeglądzie źródeł. | environment fact | Context, cytat z https://code.claude.com/docs/en/skills § Restrict Claude's skill access, czytane 2026-11-21; przyjęte przez doradcę dnia w imieniu Mariusza, 2026-11-21: „wiersz 2 przyjęty — fakt środowiska z cytatem dokumentacji i datą odczytu; decyzja ma stać na fakcie, który wyjdzie przy przeglądzie źródeł” | na czym WAY-127 opiera *Based on* zmiany — bez faktu cykl oparłby decyzję na notatce `instruction-files/tool_loading.md`, która faktem fundamentu nie jest |

## Out of scope

- Przestawienie przypięcia the way w loop2 i pomiar skutku tam — osobny krok loop2 po scaleniu.
