**State: draft** — the code is finished and reviewed, and the final check (the CI run on this request's last head) has not finished yet; three items below wait for your answer.

## What you will see

Claude Code no longer offers the-way's own skills to the model. A session that works on the-way, and a session in a product that carries the-way as a submodule, now see only the skills that exist for that session. This removes the second set of 23 skills that a product's session received after it read any file from the submodule, 21 of which duplicated the product's own skills and cut the descriptions of all skills short.

- Every entry file that makes a skill of the-way available now carries a "hidden from the model" setting in its header. Claude Code's documentation says such a skill is removed from the model's context and that a human can still start it by name. In a session on the-way you start a skill by typing `/the-way-<name>`, as before; a loose request without the slash no longer brings in a skill of the-way.
- In a session on the-way, when one skill tells the session to use another skill of the-way, the session now opens that skill's file in its own checkout and follows it, instead of calling the skill. Each entry file lists every skill with the path of its file, so the session knows where to look. Fifteen skills that spoke about this hand-over now say it for both cases: on the-way itself the file is read; in a product the hand-over stays as it was, through the product's own entry files, which the installer writes and which this change does not touch.
- The instructions for agents and the introduction of the repository now say that a human starts the skills and that skills hand work on through their files.
- The foundation records the decision, the matching rule and a new fact about Claude Code's behaviour, with a quotation from its documentation read on 2026-11-21.

The task asked for one check in a real Claude Code session. A reviewer made it with two real sessions: in a layout like a product, with a real submodule holding the 23 entry files, none of them reached the model after a file in the submodule was read, and the product's own skill of the same name stayed on the list; in a layout like the-way, none was offered to the model, and a hidden skill still started with its slash command.

### Underneath

The change is one new line in the generator of the entry files, the 46 entry files it regenerated (one set for Claude Code, an identical set for Codex), a reworded hand-over sentence in the entry text and in 15 skills, and the entries of the foundation that carry the rule.

## For you to decide

### Needed from you

none

### Fix or let through

1. Nobody checked whether Codex still loads the entry files that now carry the new setting. The Codex documentation and the open skills standard do not say what a client does with a setting it does not know, and a test run of Codex on this machine stopped because its default model is refused for this account. If Codex refuses such a skill, a session in Codex on the-way finds none of its skills until the setting is taken out of Codex's copy, which today's rule forbids, since both copies must be identical; the model hiding itself is not Codex's concern in products, because Codex does not read the nested copy there. Checking now costs a few minutes of your time by hand; a failure then needs a decision from you to let the two copies differ, plus a round of correction with review. Making a task of it leaves Codex unchecked until someone opens it; undoing it costs nothing. Letting it through accepts that risk; if Codex refuses the skills, the first person to use Codex on the-way finds out. I recommend checking it by hand now, since it takes minutes and is the only open risk of the change. Its weak point: a Codex session may behave differently in your setup than in the next person's. Check it now (and write a remark), make a task of it, or let it through?
   The steps of the check by hand, whose result you write down as a remark:
   1. Open a Codex session in the folder of the task's worktree.
   2. Type `$` (or run `/skills`) and look at the list of skills.
   3. The skills whose names start with `the-way-` should be on the list, and starting one should open it.

   (Checks, 1)
2. The review of the whole change read 3 of the 50 selected decisions whole and read the other 47 by their main sentences, among them four that bear on this change: what assigns a file to a part of the repository, where a fragment of a skill stands, which citations become entries about the environment, and how it is settled whether a rule of an instruction file works. If one of them has a clause this change breaks, the next person who changes those skill files runs into it. A fresh reviewer reading the four whole costs another review round of about ten minutes and some tokens; undoing it costs nothing. Making a task of it leaves them unread; undoing it costs nothing. Letting it through accepts that gap; undoing it costs a correction later. I recommend letting it through, since the reviewer ran through all 157 decision headings outside its topic and found no clash. Its weak point: reading only a main sentence can miss a clause that adds a condition. Read them in this request, make a task of it, or let it through?
   (Checks, 3)
3. Two small notes of the review of the fix were left unfixed, as the rules ask: the description of the part in the part map says the skills are "hidden from the model" without saying that this is Claude Code's behaviour, and the summary of the invariant test's failure message and the matching sentence in the instructions for agents name only three of the causes the test reports. Whoever reads the part map may take the hiding as settled for Codex, and whoever meets a failure of the test reads the lines below the message, which name every cause, so no one is misled. Fixing them here costs a round of correction with a review of about ten minutes; undoing it costs nothing. Making a task of it leaves two unqualified sentences until someone changes them; undoing it costs nothing. Letting it through accepts that. I recommend letting it through, since neither misleads a reader of the test's output and both are one sentence. Its weak point: the part map is read by agents that may repeat the sentence as settled. Fix them here, make a task of them, or let them through?
   (Minor findings, 1 and 2)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

4. The cycle added a rule the task does not state: each entry file lists every skill with the path of its file, and the decision and the matching rule say so. The task says a session reaches another skill by reading its file "by path", and a name alone gives no path; the other way, a search by name in every hand-over, would cost an extra step in each and could find a copy under a working directory of another run. The price is 23 more lines in each of 46 entry files, read only when a skill is started. The decision says: in the-way itself a skill hands work on by reading the other skill's file from the session's own checkout, each entry file giving the path of every skill; the rule says each entry file holds the setting, tells the session not to call another skill of the-way but to read its file, and lists every skill with its path.
5. The cycle reworded one sentence in the description of the part that holds the entry files: it used to say the entry files make the skills visible to sessions; it now says they are how a human starts the skills in sessions, hidden from the model, because the old sentence would have said the opposite of the new decision.
6. The test that checks the rule about entry files now also checks that each entry file carries the setting in both copies, that it tells the session not to call another skill but to read its file, and that it lists every skill with its path; the rule's sentence was reworded to say so, and the test's old checks were kept. The foundation check run on the finished change listed no rule whose sentence was corrected while its test stayed as it was.

## Cost

The cycle's working time was 58 minutes, 33 of them waiting for tools; the whole change took one author, one review of the whole change, one fix of its six small findings and one review of that fix, and no third round. Tokens in all: 42.7 million (30.5 million on Claude Sonnet 5.5, 12.2 million on Claude Opus 5.5, 0.06 million on Claude Haiku 5.5, which only read two documentation pages). The reviewers ran on Opus 5.5, as you asked. Table of stages: see the record's link in the lower part.

## How to merge

Merge with a merge commit, not a squash or a rebase, so that the link to the record of the cycle, which points at one commit by its identifier, stays reachable. The count of merges since the last review of the foundation is 27 of 60, so no review is due.

<details>
<summary>Po polsku</summary>

**Stan: wersja robocza** — kod jest gotowy i sprawdzony przez recenzentów, a końcowy test (przebieg CI na ostatniej głowie tego żądania) jeszcze się nie skończył; trzy punkty niżej czekają na Twoją odpowiedź.

## Co zobaczysz

Claude Code nie pokazuje już modelowi skilli samego the way. Sesja na the way i sesja w produkcie, który podpina the way jako podmoduł, widzą teraz tylko te skille, które dla niej istnieją. Znika drugi komplet 23 skilli, który sesja w produkcie dostawała po odczytaniu jakiegokolwiek pliku z podmodułu — 21 z nich dublowało skille produktu i powodowało przycinanie opisów wszystkich skilli.

- Każdy plik wejściowy, który udostępnia skill the way, ma teraz w nagłówku ustawienie „ukryty przed modelem”. Dokumentacja Claude Code mówi, że taki skill znika z kontekstu modelu, a człowiek dalej może go uruchomić po nazwie. W sesji na the way skill uruchamiasz, wpisując `/the-way-<nazwa>`, jak dotąd; luźna prośba bez ukośnika nie wciąga już skilla the way.
- W sesji na the way, gdy jeden skill każe użyć innego skilla the way, sesja otwiera teraz plik tego skilla w swoim checkoucie i idzie za nim, zamiast wywoływać skill. Każdy plik wejściowy wylicza wszystkie skille ze ścieżką ich pliku, więc sesja wie, gdzie szukać. Piętnaście skilli, które o tym mówiły, opisuje przekazanie dla obu przypadków: na samym the way plik się czyta; w produkcie przekazanie zostaje takie jak było, przez wejścia produktu, które pisze instalator i których ta zmiana nie rusza.
- Instrukcje dla agentów i wstęp repozytorium mówią teraz, że skille uruchamia człowiek, a skille przekazują sobie pracę przez swoje pliki.
- Fundament zapisuje decyzję, regułę, która ją pilnuje, i nowy fakt o zachowaniu Claude Code z cytatem z jego dokumentacji, czytanej 2026-11-21.

Zadanie prosiło o jedno sprawdzenie w prawdziwej sesji Claude Code. Recenzent zrobił je w dwóch prawdziwych sesjach: w układzie jak w produkcie, z prawdziwym podmodułem z 23 plikami wejściowymi, żaden z nich nie trafił do modelu po odczytaniu pliku z podmodułu, a własny skill produktu o tej samej nazwie został na liście; w układzie jak w the way żaden nie został pokazany modelowi, a ukryty skill dalej uruchamiał się swoim poleceniem z ukośnikiem.

### Pod spodem

Zmiana to jedna nowa linia w generatorze plików wejściowych, 46 plików, które wygenerował od nowa (jeden komplet dla Claude Code i identyczny dla Codexa), przeformułowane zdanie o przekazaniu w tekście wejścia i w 15 skillach oraz wpisy fundamentu, które niosą regułę.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

brak

### Napraw albo przepuść

1. Nikt nie sprawdził, czy Codex dalej wczytuje pliki wejściowe, które mają teraz to nowe ustawienie. Dokumentacja Codexa i otwarty standard skilli nie mówią, co klient robi z nieznanym ustawieniem, a próbny przebieg Codexa na tej maszynie zatrzymał się, bo jego domyślny model jest odrzucany dla tego konta. Jeśli Codex odrzuca taki skill, sesja Codexa na the way nie znajdzie żadnego swojego skilla, dopóki ustawienie nie zostanie usunięte z kopii Codexa, czego dzisiejsza reguła zabrania, bo obie kopie muszą być identyczne; samo ukrywanie przed modelem nie dotyczy Codexa w produktach, bo Codex nie czyta tam zagnieżdżonej kopii. Sprawdzenie teraz kosztuje kilka minut Twojego czasu ręcznie; porażka wymagałaby Twojej decyzji o rozdzieleniu kopii i rundy poprawki z recenzją. Zrobienie z tego zadania zostawia Codexa niesprawdzonego, aż ktoś go otworzy; cofnięcie nic nie kosztuje. Przepuszczenie przyjmuje to ryzyko; jeśli Codex odrzuci skille, pierwsza osoba używająca Codexa na the way się o tym dowie. Rekomenduję sprawdzić teraz ręcznie, bo to minuty i jedyne otwarte ryzyko zmiany. Słaby punkt: sesja Codexa może u Ciebie zachować się inaczej niż u następnej osoby. Sprawdzić teraz (i zapisać uwagę), zrobić z tego zadanie, czy przepuścić?
   Kroki sprawdzenia ręcznego, którego wynik zapisujesz jako uwagę:
   1. Otwórz sesję Codexa w katalogu worktree zadania.
   2. Wpisz `$` (albo uruchom `/skills`) i spójrz na listę skilli.
   3. Skille o nazwach zaczynających się od `the-way-` powinny być na liście, a uruchomienie jednego powinno go otworzyć.

   (Checks, 1)
2. Recenzja całej zmiany przeczytała w całości 3 z 50 wybranych decyzji, a pozostałe 47 po ich głównych zdaniach, w tym cztery, które dotyczą tej zmiany: co przypisuje plik do części repozytorium, gdzie stoi fragment skilla, które cytaty stają się wpisami o środowisku i jak rozstrzyga się, czy reguła pliku instrukcji działa. Jeśli któraś ma klauzulę, którą ta zmiana łamie, następna osoba zmieniająca te pliki skilli na nią trafi. Świeży recenzent czytający te cztery w całości to kolejna runda recenzji (ok. dziesięć minut) i trochę tokenów; cofnięcie nic nie kosztuje. Zrobienie z tego zadania zostawia je nieprzeczytane; cofnięcie nic nie kosztuje. Przepuszczenie przyjmuje tę lukę; cofnięcie kosztuje późniejszą poprawkę. Rekomenduję przepuścić, bo recenzent przeszedł przez wszystkie 157 nagłówków decyzji spoza swojego tematu i nie znalazł kolizji. Słaby punkt: czytanie samego głównego zdania może pominąć klauzulę dodającą warunek. Przeczytać je w tym żądaniu, zrobić z tego zadanie, czy przepuścić?
   (Checks, 3)
3. Dwie drobne uwagi recenzji poprawki zostały niepoprawione, jak chcą reguły: opis części w mapie części mówi, że skille są „ukryte przed modelem”, nie mówiąc, że to zachowanie Claude Code, a podsumowanie komunikatu o błędzie testu reguły i odpowiadające mu zdanie w instrukcjach dla agentów wymieniają tylko trzy z przyczyn, które test zgłasza. Ktoś czytający mapę części może uznać ukrywanie za rozstrzygnięte także dla Codexa, a ktoś, kto trafi na porażkę testu, czyta linie pod komunikatem, które wymieniają każdą przyczynę, więc nikt nie jest wprowadzony w błąd. Poprawka tutaj to runda poprawki z recenzją (ok. dziesięć minut); cofnięcie nic nie kosztuje. Zrobienie z tego zadania zostawia dwa niekwalifikowane zdania, aż ktoś je zmieni; cofnięcie nic nie kosztuje. Przepuszczenie to przyjmuje. Rekomenduję przepuścić, bo żadne nie wprowadza w błąd czytelnika wyniku testu i oba to jedno zdanie. Słaby punkt: mapę części czytają agenci, którzy mogą powtórzyć to zdanie jako rozstrzygnięte. Poprawić je tutaj, zrobić z nich zadanie, czy przepuścić?
   (Minor findings, 1 and 2)

### Przyjmujesz przez scalenie

Scalenie przyjmuje te punkty; jeśli któryś Ci nie odpowiada, powiedz który.

4. Cykl dodał regułę, której zadanie nie podaje: każdy plik wejściowy wylicza wszystkie skille ze ścieżką ich pliku, a decyzja i odpowiadająca jej reguła o tym mówią. Zadanie mówi, że sesja dociera do innego skilla, czytając jego plik „po ścieżce”, a sama nazwa ścieżki nie daje; druga droga, wyszukiwanie po nazwie przy każdym przekazaniu, dodałaby krok w każdym z nich i mogłaby znaleźć kopię w katalogu roboczym innego przebiegu. Cena to 23 linie więcej w każdym z 46 plików wejściowych, czytanych dopiero przy uruchomieniu skilla. Decyzja mówi: na samym the way skill przekazuje pracę, czytając plik drugiego skilla z checkoutu sesji, a każdy plik wejściowy podaje ścieżkę każdego skilla; reguła mówi, że każdy plik wejściowy ma to ustawienie, każe sesji nie wywoływać innego skilla the way, tylko czytać jego plik, i wylicza każdy skill ze ścieżką.
5. Cykl przeformułował jedno zdanie opisu części, która trzyma pliki wejściowe: dawniej mówiło, że pliki wejściowe czynią skille widocznymi dla sesji; teraz mówi, że są sposobem, w jaki człowiek uruchamia skille w sesjach, ukrytymi przed modelem, bo stare zdanie mówiłoby odwrotnie niż nowa decyzja.
6. Test pilnujący reguły o plikach wejściowych sprawdza teraz także, że każdy plik wejściowy ma to ustawienie w obu kopiach, że każe sesji nie wywoływać innego skilla, tylko czytać jego plik, i że wylicza każdy skill ze ścieżką; zdanie reguły przeformułowano, żeby to mówiło, a dotychczasowe sprawdzenia testu zachowano. Sprawdzenie fundamentu na gotowej zmianie nie wskazało reguły, której zdanie poprawiono, a test zostawiono bez zmian.

## Koszt

Czas pracy cyklu to 58 minut, z czego 33 czekania na narzędzia; zmianę zrobił jeden autor, a recenzje to jedna recenzja całej zmiany, jedna poprawka jej sześciu drobnych uwag i jedna recenzja tej poprawki, bez trzeciej rundy. Tokeny łącznie: 42,7 mln (30,5 mln na Claude Sonnet 5.5, 12,2 mln na Claude Opus 5.5, 0,06 mln na Claude Haiku 5.5, który tylko czytał dwie strony dokumentacji). Recenzenci pracowali na Opus 5.5, jak chciałeś. Tabela etapów: zobacz link do zapisu w dolnej części.

## Jak scalić

Scal przez merge commit, nie squash ani rebase, żeby link do zapisu cyklu, który wskazuje jeden commit po identyfikatorze, pozostał osiągalny. Liczba scaleń od ostatniego przeglądu fundamentu to 27 z 60, więc przegląd nie jest potrzebny.

</details>

## Technical changes

- `f9cae3a6` — `agent-instructions/skill_entry_points.py` writes `disable-model-invocation: true` in the header of each entry point (one constant, `HIDING_FIELD`) and replaces `sibling_names` by `skill_list`, which lists every skill as `` - `name`: `path` ``; the paragraph that told a session to use another skill as the project skill with the `the-way-` prefix now says to read that skill's `SKILL.md` under the same root; the first paragraph (stop in a product, use the product's own project skill) is unchanged. `agent-instructions/test_skill_entry_points.py` and `gate/test_skills_reach_the_way_sessions.py` (the end-to-end test of the invariant `skill-entry-points`) are changed to match; the 46 entry points under `.claude/skills/` and `.agents/skills/` are regenerated (`python -B agent-instructions/skill_entry_points.py --write`), 15 → 40 lines each in the final state.
- `f3188faa` — the paragraph "where the-way lies" of 15 skills (`elements/{common,decisions,environment-facts,glossary,invariants,part-map}/skill/SKILL.md`, `foundation-review/SKILL.md`, `product-guidelines/{coding,styleguide,testing}/SKILL.md`, `project-level/{lead,plan,task}/skill/SKILL.md`, `project-level/skill/SKILL.md`, `project-level/technology/SKILL.md`) distinguishes the-way itself (a named skill is read as a file) from a product (the project skill with the prefix); `AGENTS.md` `## Skills` and the `README.md` section "Using the skills" say that a human starts a skill with `/the-way-<name>` and a skill hands work on through its file.
- `7d063ef2` — WAY-127 (sentence, *Rationale*, *Rejected*, *Verification*, *Based on* gains `claude-code-skill-model-hiding`), the invariant `skill-entry-points`, the new environment fact `claude-code-skill-model-hiding`, the sentence of the part-map entry `agent-instructions`.
- `90ac8500`, `2bd0efde`, `f1efc257` — the fix of the six Minor findings of the review of the whole change: the invariant's test now requires the words that send a session to the file, with a failing case; the entry text and the texts of `AGENTS.md`, `README.md` and WAY-127 qualify the hiding as Claude Code's; the 15 paragraphs point at the entry point's list first and fall back to a search limited to the files git lists; the lead skill's brief of a dispatched agent carries the file's path; the docstring and message of the test and `AGENTS.md` say what the test checks; WAY-127's *Scope* gains `foundation-review` and `product-guidelines`.
- The return step compared WAY-127, the invariant and the fact with the generator, the 46 entry points, the 15 paragraphs, `AGENTS.md`, `README.md` and the test; nothing no longer matched, no entry written, no commit, so no review of it ran.

## Checks

1. Codex was not checked. Nothing run on Codex shows how it treats a skill whose header holds `disable-model-invocation: true`: the Codex documentation (https://developers.openai.com/codex/skills, redirected to https://learn.chatgpt.com/docs/build-skills) names only `name` and `description` as fields of `SKILL.md` and puts the invocation policy in `agents/openai.yaml`; the Agent Skills specification (https://agentskills.io/specification) is silent on unknown fields and its client guidance says not to block loading "on cosmetic issues"; a `codex exec` run in a scratch repository stopped on the refused default model of Codex 0.163.0. Both copies carry the field and stay byte-identical (the task's *Questions carried to cycle*, answered as an autonomous choice, Q1 of the record).
2. Acceptance criterion 1 (a real session): the author ran a probe repository (Claude Code 2.1.330, `haiku`) with a hand-made nested skill pair; the reviewer of the whole change ran two real sessions (same version and model): a product layout (a real `.the-way` submodule with the 23 generated entry points, a product skill `the-way-critique` at the root, a nested control skill without the field) — after a file in `.the-way/` was read, none of the 23 reached the model (`dynamic_skill.skillNames` of the transcript), the product's skill stayed on the list; the-way's layout — none of the 23 offered, a hidden skill still started with its `/name` command. Evidence: `reports/review-whole-probe-evidence.txt` of the record. Unchecked: loop2 itself and the skill list of a subagent started from such a session (the task's *Out of scope*), an interactive session instead of `-p` mode, other Claude Code releases.
3. The review of the whole change (`PASS 7d063ef278748884de28577f582b2ab0767d068d`) read 3 decisions of the index of its selection whole (WAY-127, WAY-34, WAY-35), the other 47 by their sentence and *Scope*, ran through the 157 headings outside its sections, and names WAY-44, WAY-256, WAY-90 and WAY-131 as bearing on the change and read only by their sentences.
4. Final gate: the CI run on this request's last head — (to fill: link, `tests`, `tests-windows`).
5. Failing before the change: none, taken from the merged request https://github.com/mariusznazar/the-way/pull/153, whose CI run on its last head (https://github.com/mariusznazar/the-way/actions/runs/44748054270) passed in both checks; the base `19e5774a` is a merge commit with the tree of its second parent, so no gate ran on the base.
6. `python -B elements/common/foundation_check.py` on the head `f1efc257`: exit 0, `0 errors`, no `listed:` line (the author, the reviewer and the orchestrator).
7. Focused runs (`python -B gate/run_tests.py <directory>`, exit 0): `agent-instructions`, `gate`, `elements/common`, `elements/part-map`, `instruction-files`, `product-guidelines`, `project-level`, `task-cycle`, `installation` (alone, about 703 s) by the author; `agent-instructions`, `gate`, `product-guidelines` by the reviewers. Failing runs the author reported before the code was written: the invariant test (exit 1, 23 problem lines, the first report said 46 and the fix report corrected it), the generator tests (exit 1, six assertions), the new case of the invariant test (exit 1, then 0 after the fix); the file `reports/author-invariant-test-failing-run.txt` and its two companions hold them. `python -B agent-instructions/skill_entry_points.py` without `--write`: exit 0, "entry points are current".
8. Own-work checks: the author named acceptance criterion 1 as its weakest point and checked it on a probe repository, and a search of every `SKILL.md` and its neighbours for a text that still tells a session to call a skill of the-way; the reviewer repeated the first with real generated entry points and found no text left that tells a session of the-way to call a skill (the remaining ones belong to products).
9. Not run: `ruff check` and `ruff format --check` as separate commands (the formatter's test in `agent-instructions` ran and passed); the whole gate on the cycle's own system (CI is the final gate).
10. Review of the foundation: 27 merges since the tag `foundation-review/2026-11-15`, threshold 60: no reminder.
11. The form check of this description: `python -B task-cycle/request_check.py .runs/task-cycles/hide-the-way-skills-from-models/request.md --task .runs/task-cycles/hide-the-way-skills-from-models/task.md` and the check of private paths on it (`python -B task-cycle/private_paths_check.py .runs/task-cycles/hide-the-way-skills-from-models/request.md`): (to fill: last runs); the three checks on the copy of the record: (to fill).
12. Working copies left: none; directories of earlier tasks kept: none (the script of step 4 removed the one directory of a merged task).

## Foundation entries

- WAY-127 — `row 1`, and the clause that each entry point gives the path of every skill is `the cycle's`: the entry points of the-way's skills carry `disable-model-invocation: true`, so the model is offered none; a human starts a skill with `/the-way-<name>`, a skill hands another on by reading its `SKILL.md` in the-way itself, and a product's hand-over stays through its own entry point. Its *Rejected* gained three ways from the task's *Not chosen* (settings written by the installer, a hand list of exclusions, the file hand-over in a product too); its *Scope* gained `foundation-review` and `product-guidelines`.
- `skill-entry-points` (invariant) — `row 1`, and the list of paths is `the cycle's`: each pair of entry points is byte-identical, holds the field, tells a session not to call another such skill but to read its `SKILL.md`, and lists every such skill with the path of its `SKILL.md`. Its test, `gate/test_skills_reach_the_way_sessions.py`, is changed to check the three added properties; the failing and the passing run are in item 7 of *Checks*.
- `claude-code-skill-model-hiding` (environment fact) — `row 2`: Claude Code removes a skill with `disable-model-invocation: true` from Claude's context, so its description is not in context and Claude does not invoke it on its own, while the user can still invoke it.
- the part-map entry `agent-instructions`, one sentence — `the cycle's`: the entry points are described as the way a human starts the-way's skills, hidden from the model, not as what makes them visible to sessions on it.

No pair of examples was added; the *complies* and *violates* examples of WAY-127 for the paragraphs of skills were reworded in place.

## Minor findings

1. `foundations/part_map.md:170-171` says "through which a human starts the-way's skills in sessions on it, hidden from the model" without limiting it to Claude Code, and so does the failure message of the invariant test at `gate/test_skills_reach_the_way_sessions.py:229` ("is not hidden from the model"). The reviewer: "both texts describe the field more than they claim Codex behaviour"; found new by the review of the fix, not fixed (WAY-161).
2. The failure message (`gate/test_skills_reach_the_way_sessions.py:228-229`) and `AGENTS.md:19-21` name three causes: missing, differs from its copy, lacks the field. The test also reports an entry point whose text lacks a required sentence or a line of the list of skills, a wrong name or description, and an orphan directory (`entry_problems` and `problems`). The reviewer: "The summaries are incomplete, not wrong."
3. Two lines of WAY-127 are longer than the 100 columns the rest of the file keeps: `foundations/decisions.md:3344` and `:3397`. The reviewer: "It is form only; no check covers it."

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** the task "skille do rozwijania frameworka nie mają trafiać do produktów, które podpinają go jako podmoduł", an independent task, `Status: ready for cycle`, updated 2026-11-21; the Claude Code documentation page read on 2026-11-21; the Codex and Agent Skills pages read the same day.
- **Process pin:** the-way itself; no pin to move; the checkout was at `19e5774a`, equal to the remote.
- **Spec:** none: the task's rows and answers leave no open design choice; how the entry text and the skills phrase the file hand-over is a way of making what the task settles, named in the author's report.
- **Route:** one author without a plan, class `same` as the orchestrator's (Sonnet 5.5), because the change spans many parts and writes a decision, an invariant and an environment fact; reviewers on Opus 5.5 by the human's instruction.
- **Plan:** none.
- **Choices:** 4 rows in the questions table of the record (Codex answered as an autonomous choice; the model of the reviewers; the unread decisions the author listed; the clause on the list of paths).
- **Blocking findings left:** none.
- **Record:** (to fill: link by the SHA of the commit that adds it)
