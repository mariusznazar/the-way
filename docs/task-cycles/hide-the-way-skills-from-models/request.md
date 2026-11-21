**State: ready** — corrected for your remarks on the first description; the code is finished and reviewed, the CI run on the new last head is still running, and one item (1) waits for your answer.

## What you will see

Claude Code no longer offers the-way's own skills to the model. A session that works on the-way, and a session in a product that carries the-way as a submodule, now see only the skills that exist for that session. This removes the second set of 23 skills that a product's session received after it read any file from the submodule, 21 of which duplicated the product's own skills and cut the descriptions of all skills short.

- Every entry file that makes a skill of the-way available now carries a "hidden from the model" setting in its header. Claude Code's documentation says such a skill is removed from the model's context and that a human can still start it by name. In a session on the-way you start a skill by typing `/the-way-<name>`, as before; a loose request without the slash no longer brings in a skill of the-way.
- In a session on the-way, when one skill tells the session to use another skill of the-way, the session now opens that skill's file in its own checkout and follows it, instead of calling the skill. Each entry file lists every skill with the path of its file, so the session knows where to look. Fifteen skills that spoke about this hand-over now say it for both cases: on the-way itself the file is read; in a product the hand-over stays as it was, through the product's own entry files, which the installer writes and which this change does not touch.
- The instructions for agents and the introduction of the repository now say that a human starts the skills and that skills hand work on through their files.
- The foundation records the decision, the matching rule and a new fact about Claude Code's behaviour, with a quotation from its documentation read on 2026-11-21.
- Codex, as your adviser checked by hand, lists all 23 entry files and ignores the new setting, so in Codex the skills stay visible to the model; the description of the part in the part map now says so, and says that the hiding is Claude Code's behaviour.

The task asked for one check in a real Claude Code session. A reviewer made it with two real sessions: in a layout like a product, with a real submodule holding the 23 entry files, none of them reached the model after a file in the submodule was read, and the product's own skill of the same name stayed on the list; in a layout like the-way, none was offered to the model, and a hidden skill still started with its slash command.

### Underneath

The change is one new line in the generator of the entry files, the 46 entry files it regenerated (one set for Claude Code, an identical set for Codex), a reworded hand-over sentence in the entry text and in 15 skills, and the entries of the foundation that carry the rule.

## For you to decide

### Needed from you

none

### Fix or let through

1. The correction left four small notes of its review unfixed, and two of them you may feel: the hand-over paragraph is now repeated in 15 skill files while the foundation says a shared way of working should stand in one place and be read from there, and the next task of the queue that changes skill files will meet that; and nobody has checked in a session that an agent really follows the new hand-over through the file (the probe sessions checked only that the skills are hidden). Whoever changes the skill files next either edits 15 copies or finds out later that an agent did not follow the hand-over. Making a task of it costs a later task; undoing it, nothing. Letting it through accepts both. Make a task of it?
   (Minor findings, 4 and 5)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. The cycle added a rule the task does not state: each entry file lists every skill with the path of its file, and the decision and the matching rule say so. The task says a session reaches another skill by reading its file "by path", and a name alone gives no path; the other way, a search by name in every hand-over, would cost an extra step in each and could find a copy under a working directory of another run. The price is 23 more lines in each of 46 entry files, read only when a skill is started. The decision says: in the-way itself a skill hands work on by reading the other skill's file from the session's own checkout, each entry file giving the path of every skill; the rule says each entry file holds the setting, tells the session not to call another skill of the-way but to read its file, and lists every skill with its path.
3. The cycle reworded one sentence in the description of the part that holds the entry files: it used to say the entry files make the skills visible to sessions; it now says they are how a human starts the skills in sessions, which Claude Code keeps from the model because of the field in their header while Codex ignores that field and the skills stay visible to the model there, because the old sentence would have said the opposite of the new decision.
4. The test that checks the rule about entry files now also checks that each entry file carries the setting in both copies, that it tells the session not to call another skill but to read its file, and that it lists every skill with its path; the rule's sentence was reworded to say so, and the test's old checks were kept. Its failure message and the matching sentence in the instructions for agents now name every cause the test reports. The foundation check run on the finished change listed no rule whose sentence was corrected while its test stayed as it was.
5. This correction answered your answers to three items of the first description, the Codex check, the unread decisions and the two small notes; the cycle judged that the task and the foundation did not require what the correction changed, so these were not required.

## Cost

The cycle's working time across all sessions was 1 hour 14 minutes, 38 of them waiting for tools; the change took one author, one review of the whole change, one fix of its six small findings with its review, and correction 1 with its own fresh review, which also read four decisions whole; no third round. Tokens in all: 56.1 million (41.8 million on Claude Sonnet 5.5, 14.2 million on Claude Opus 5.5, 0.06 million on Claude Haiku 5.5, which only read two documentation pages). The reviewers ran on Opus 5.5, as you asked. Table of stages: RECORD_LINK/stages.md.

## How to merge

Merge with a merge commit, not a squash or a rebase, so that the link to the record of the cycle, which points at one commit by its identifier, stays reachable. The count of merges since the last review of the foundation is 27 of 60, so no review is due.

<details>
<summary>Po polsku</summary>

**Stan: gotowe** — poprawione dla Twoich uwag do pierwszego opisu; kod jest gotowy i sprawdzony przez recenzentów, przebieg CI na nowej ostatniej głowie jeszcze trwa, a jeden punkt (1) czeka na Twoją odpowiedź.

## Co zobaczysz

Claude Code nie pokazuje już modelowi skilli samego the way. Sesja na the way i sesja w produkcie, który podpina the way jako podmoduł, widzą teraz tylko te skille, które dla niej istnieją. Znika drugi komplet 23 skilli, który sesja w produkcie dostawała po odczytaniu jakiegokolwiek pliku z podmodułu — 21 z nich dublowało skille produktu i powodowało przycinanie opisów wszystkich skilli.

- Każdy plik wejściowy, który udostępnia skill the way, ma teraz w nagłówku ustawienie „ukryty przed modelem”. Dokumentacja Claude Code mówi, że taki skill znika z kontekstu modelu, a człowiek dalej może go uruchomić po nazwie. W sesji na the way skill uruchamiasz, wpisując `/the-way-<nazwa>`, jak dotąd; luźna prośba bez ukośnika nie wciąga już skilla the way.
- W sesji na the way, gdy jeden skill każe użyć innego skilla the way, sesja otwiera teraz plik tego skilla w swoim checkoucie i idzie za nim, zamiast wywoływać skill. Każdy plik wejściowy wylicza wszystkie skille ze ścieżką ich pliku, więc sesja wie, gdzie szukać. Piętnaście skilli, które o tym mówiły, opisuje przekazanie dla obu przypadków: na samym the way plik się czyta; w produkcie przekazanie zostaje takie jak było, przez wejścia produktu, które pisze instalator i których ta zmiana nie rusza.
- Instrukcje dla agentów i wstęp repozytorium mówią teraz, że skille uruchamia człowiek, a skille przekazują sobie pracę przez swoje pliki.
- Fundament zapisuje decyzję, regułę, która ją pilnuje, i nowy fakt o zachowaniu Claude Code z cytatem z jego dokumentacji, czytanej 2026-11-21.
- Codex, jak sprawdził ręcznie Twój doradca, wylicza wszystkie 23 pliki wejściowe i ignoruje nowe ustawienie, więc w Codexie skille zostają widoczne dla modelu; opis części w mapie części mówi to teraz i mówi, że ukrywanie to zachowanie Claude Code.

Zadanie prosiło o jedno sprawdzenie w prawdziwej sesji Claude Code. Recenzent zrobił je w dwóch prawdziwych sesjach: w układzie jak w produkcie, z prawdziwym podmodułem z 23 plikami wejściowymi, żaden z nich nie trafił do modelu po odczytaniu pliku z podmodułu, a własny skill produktu o tej samej nazwie został na liście; w układzie jak w the way żaden nie został pokazany modelowi, a ukryty skill dalej uruchamiał się swoim poleceniem z ukośnikiem.

### Pod spodem

Zmiana to jedna nowa linia w generatorze plików wejściowych, 46 plików, które wygenerował od nowa (jeden komplet dla Claude Code i identyczny dla Codexa), przeformułowane zdanie o przekazaniu w tekście wejścia i w 15 skillach oraz wpisy fundamentu, które niosą regułę.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

brak

### Napraw albo przepuść

1. Korekta zostawiła niepoprawione cztery drobne uwagi swojej recenzji, a dwie z nich możesz odczuć: akapit o przekazaniu pracy jest teraz powtórzony w 15 plikach skilli, choć fundament mówi, że wspólny sposób pracy ma stać w jednym miejscu i stamtąd być czytany, a następne zadanie z kolejki, które zmienia pliki skilli, na to trafi; oraz nikt nie sprawdził w sesji, że agent naprawdę idzie za nowym przekazaniem przez plik (sesje próbne sprawdziły tylko, że skille są ukryte). Kto następny zmienia pliki skilli, albo poprawia 15 kopii, albo dopiero później odkrywa, że agent nie poszedł za przekazaniem. Zrobienie z tego zadania kosztuje późniejsze zadanie; cofnięcie nic nie kosztuje. Przepuszczenie przyjmuje oba. Zrobić z tego zadanie?
   (Minor findings, 4 and 5)

### Przyjmujesz przez scalenie

Scalenie przyjmuje te punkty; jeśli któryś Ci nie odpowiada, powiedz który.

2. Cykl dodał regułę, której zadanie nie podaje: każdy plik wejściowy wylicza wszystkie skille ze ścieżką ich pliku, a decyzja i odpowiadająca jej reguła o tym mówią. Zadanie mówi, że sesja dociera do innego skilla, czytając jego plik „po ścieżce”, a sama nazwa ścieżki nie daje; druga droga, wyszukiwanie po nazwie przy każdym przekazaniu, dodałaby krok w każdym z nich i mogłaby znaleźć kopię w katalogu roboczym innego przebiegu. Cena to 23 linie więcej w każdym z 46 plików wejściowych, czytanych dopiero przy uruchomieniu skilla. Decyzja mówi: na samym the way skill przekazuje pracę, czytając plik drugiego skilla z checkoutu sesji, a każdy plik wejściowy podaje ścieżkę każdego skilla; reguła mówi, że każdy plik wejściowy ma to ustawienie, każe sesji nie wywoływać innego skilla the way, tylko czytać jego plik, i wylicza każdy skill ze ścieżką.
3. Cykl przeformułował jedno zdanie opisu części, która trzyma pliki wejściowe: dawniej mówiło, że pliki wejściowe czynią skille widocznymi dla sesji; teraz mówi, że są sposobem, w jaki człowiek uruchamia skille w sesjach, które Claude Code ukrywa przed modelem przez pole w ich nagłówku, podczas gdy Codex to pole ignoruje i skille zostają tam widoczne dla modelu, bo stare zdanie mówiłoby odwrotnie niż nowa decyzja.
4. Test pilnujący reguły o plikach wejściowych sprawdza teraz także, że każdy plik wejściowy ma to ustawienie w obu kopiach, że każe sesji nie wywoływać innego skilla, tylko czytać jego plik, i że wylicza każdy skill ze ścieżką; zdanie reguły przeformułowano, żeby to mówiło, a dotychczasowe sprawdzenia testu zachowano. Jego komunikat o błędzie i odpowiadające mu zdanie w instrukcjach dla agentów wymieniają teraz każdą przyczynę, którą test zgłasza. Sprawdzenie fundamentu na gotowej zmianie nie wskazało reguły, której zdanie poprawiono, a test zostawiono bez zmian.
5. Ta korekta odpowiadała na Twoje odpowiedzi do trzech punktów pierwszego opisu: sprawdzenie Codexa, nieprzeczytane decyzje i dwie drobne uwagi; cykl uznał, że zadanie ani fundament nie wymagały tego, co korekta zmienia, więc nie były wymagane.

## Koszt

Czas pracy cyklu we wszystkich sesjach to 1 godzina 14 minut, z czego 38 czekania na narzędzia; zmianę zrobił jeden autor, a recenzje to jedna recenzja całej zmiany, jedna poprawka jej sześciu drobnych uwag z recenzją oraz korekta 1 z własną świeżą recenzją, która przeczytała też w całości cztery decyzje; bez trzeciej rundy. Tokeny łącznie: 56,1 mln (41,8 mln na Claude Sonnet 5.5, 14,2 mln na Claude Opus 5.5, 0,06 mln na Claude Haiku 5.5, który tylko czytał dwie strony dokumentacji). Recenzenci pracowali na Opus 5.5, jak chciałeś. Tabela etapów: RECORD_LINK/stages.md.

## Jak scalić

Scal przez merge commit, nie squash ani rebase, żeby link do zapisu cyklu, który wskazuje jeden commit po identyfikatorze, pozostał osiągalny. Liczba scaleń od ostatniego przeglądu fundamentu to 27 z 60, więc przegląd nie jest potrzebny.

</details>

## Technical changes

- `f9cae3a6` — `agent-instructions/skill_entry_points.py` writes `disable-model-invocation: true` in the header of each entry point (one constant, `HIDING_FIELD`) and replaces `sibling_names` by `skill_list`, which lists every skill as `` - `name`: `path` ``; the paragraph that told a session to use another skill as the project skill with the `the-way-` prefix now says to read that skill's `SKILL.md` under the same root; the first paragraph (stop in a product, use the product's own project skill) is unchanged. `agent-instructions/test_skill_entry_points.py` and `gate/test_skills_reach_the_way_sessions.py` (the end-to-end test of the invariant `skill-entry-points`) are changed to match; the 46 entry points under `.claude/skills/` and `.agents/skills/` are regenerated (`python -B agent-instructions/skill_entry_points.py --write`), 15 → 40 lines each in the final state.
- `f3188faa` — the paragraph "where the-way lies" of 15 skills (`elements/{common,decisions,environment-facts,glossary,invariants,part-map}/skill/SKILL.md`, `foundation-review/SKILL.md`, `product-guidelines/{coding,styleguide,testing}/SKILL.md`, `project-level/{lead,plan,task}/skill/SKILL.md`, `project-level/skill/SKILL.md`, `project-level/technology/SKILL.md`) distinguishes the-way itself (a named skill is read as a file) from a product (the project skill with the prefix); `AGENTS.md` `## Skills` and the `README.md` section "Using the skills" say that a human starts a skill with `/the-way-<name>` and a skill hands work on through its file.
- `7d063ef2` — WAY-127 (sentence, *Rationale*, *Rejected*, *Verification*, *Based on* gains `claude-code-skill-model-hiding`), the invariant `skill-entry-points`, the new environment fact `claude-code-skill-model-hiding`, the sentence of the part-map entry `agent-instructions`.
- `90ac8500`, `2bd0efde`, `f1efc257` — the fix of the six Minor findings of the review of the whole change: the invariant's test now requires the words that send a session to the file, with a failing case; the entry text and the texts of `AGENTS.md`, `README.md` and WAY-127 qualify the hiding as Claude Code's; the 15 paragraphs point at the entry point's list first and fall back to a search limited to the files git lists; the lead skill's brief of a dispatched agent carries the file's path; the docstring and message of the test and `AGENTS.md` say what the test checks; WAY-127's *Scope* gains `foundation-review` and `product-guidelines`.
- `429cade1` — correction 1, for the human's remarks: the part-map entry `agent-instructions` says that Claude Code keeps the entry points from the model because of the field in their header while Codex ignores the field and the skills stay visible to the model there; the docstring and the failure message of the invariant test and the matching sentence of `AGENTS.md` name every cause the test reports (read from `entry_problems` and `problems`), the test's checks unchanged. Remark 1 (the Codex result) is a result of the record, no code; remark 2 is the reading of four decisions whole by a fresh reviewer.
- The return step compared WAY-127, the invariant and the fact with the generator, the 46 entry points, the 15 paragraphs, `AGENTS.md`, `README.md` and the test; nothing no longer matched, no entry written, no commit, so no review of it ran.

## Checks

1. Codex, checked by hand by the human's adviser in the human's name (remark 1 of correction 1, https://github.com/mariusznazar/the-way/pull/154#issuecomment-7062821019): a Codex session (codex-cli 0.163.0, model gpt-5.6-luna; the default model of the account is refused) opened in the folder of the task's worktree at `48e64f10`, where both copies carry `disable-model-invocation: true` in all 23 entry files, listed all 23 skills whose names start with `the-way-`; Codex ignores the setting, so in Codex the skills stay visible to the model. The documentation pages (https://developers.openai.com/codex/skills, https://agentskills.io/specification) are silent on unknown fields, and the cycle's own `codex exec` probe stopped on the refused default model. No environment fact is written for it: the reviewer of correction 1 judged none is needed while no decision rests on Codex's treatment of the field (Minor findings, 3).
2. Acceptance criterion 1 (a real session): the author ran a probe repository (Claude Code 2.1.330, `haiku`) with a hand-made nested skill pair; the reviewer of the whole change ran two real sessions (same version and model): a product layout (a real `.the-way` submodule with the 23 generated entry points, a product skill `the-way-critique` at the root, a nested control skill without the field) — after a file in `.the-way/` was read, none of the 23 reached the model (`dynamic_skill.skillNames` of the transcript), the product's skill stayed on the list; the-way's layout — none of the 23 offered, a hidden skill still started with its `/name` command. Evidence: `reports/review-whole-probe-evidence.txt` of the record. Unchecked: loop2 itself and the skill list of a subagent started from such a session (the task's *Out of scope*), an interactive session instead of `-p` mode, other Claude Code releases.
3. The review of the whole change (`PASS 7d063ef278748884de28577f582b2ab0767d068d`) read 3 decisions of the index of its selection whole (WAY-127, WAY-34, WAY-35) and named WAY-44, WAY-256, WAY-90 and WAY-131 as read only by their sentences. At your remark, a fresh reviewer on Opus 5.5 (`PASS 429cade12c23fb9053fec841094258b6fde4ffda`) read those four whole, with WAY-35 and WAY-127, and judged the whole change against them: WAY-44 and WAY-90 comply; for WAY-256 and WAY-131 nothing blocks (Minor findings, 4 and 5). Its **Unread material**: the skills beyond the hand-over paragraph and 45 of the 46 entry points were not read (the generator check confirms them current).
4. Final gate: the CI run on this request's last head (to fill). Before correction 1: the CI run https://github.com/mariusznazar/the-way/actions/runs/44904633789 on the head `48e64f10`, first attempt: `tests` (Linux) pass, 1m44s; `tests-windows` pass, 10m30s; the run on the earlier head `f1efc257` (https://github.com/mariusznazar/the-way/actions/runs/44904546927) was cancelled by the next push. The cycle ran no full gate on its own system, since CI runs on a request into `foundations`.
5. Failing before the change: none, taken from the merged request https://github.com/mariusznazar/the-way/pull/153, whose CI run on its last head (https://github.com/mariusznazar/the-way/actions/runs/44748054270) passed in both checks; the base `19e5774a` is a merge commit with the tree of its second parent, so no gate ran on the base.
6. `python -B elements/common/foundation_check.py` on the head `f1efc257`: exit 0, `0 errors`, no `listed:` line (the author, the reviewer and the orchestrator).
7. Focused runs (`python -B gate/run_tests.py <directory>`, exit 0): `agent-instructions`, `gate`, `elements/common`, `elements/part-map`, `instruction-files`, `product-guidelines`, `project-level`, `task-cycle`, `installation` (alone, about 703 s) by the author; `agent-instructions`, `gate`, `product-guidelines` by the reviewers. Failing runs the author reported before the code was written: the invariant test (exit 1, 23 problem lines, the first report said 46 and the fix report corrected it), the generator tests (exit 1, six assertions), the new case of the invariant test (exit 1, then 0 after the fix); the file `reports/author-invariant-test-failing-run.txt` and its two companions hold them. `python -B agent-instructions/skill_entry_points.py` without `--write`: exit 0, "entry points are current". After correction 1 (`429cade1`): `gate` (36 tests) and `agent-instructions` (53 tests) exit 0 by the author and the fresh reviewer; `instruction-files`, `elements/part-map` and `elements/common` exit 0 by the author; `foundation_check.py` exit 0, `0 errors`; the generator exit 0, "entry points are current".
8. Own-work checks: the author named acceptance criterion 1 as its weakest point and checked it on a probe repository, and a search of every `SKILL.md` and its neighbours for a text that still tells a session to call a skill of the-way; the reviewer repeated the first with real generated entry points and found no text left that tells a session of the-way to call a skill (the remaining ones belong to products).
9. Not run: `ruff check` and `ruff format --check` as separate commands (the formatter's test in `agent-instructions` ran and passed); the whole gate on the cycle's own system (CI is the final gate).
10. Review of the foundation: 27 merges since the tag `foundation-review/2026-11-15`, threshold 60: no reminder.
11. The form check of this description: `python -B task-cycle/request_check.py .runs/task-cycles/hide-the-way-skills-from-models/request.md --task .runs/task-cycles/hide-the-way-skills-from-models/task.md` and the check of private paths on it (`python -B task-cycle/private_paths_check.py .runs/task-cycles/hide-the-way-skills-from-models/request.md`): (to fill: last runs); the three checks on the copy of the record: (to fill); the remarks check on the original after correction 1: run 1 exit 1 (6 items listed, appended word for word to the process remarks), run 2 exit 0.
12. Working copies left: none; directories of earlier tasks kept: none (the script of step 4 removed the one directory of a merged task).

## Foundation entries

- WAY-127 — `row 1`, and the clause that each entry point gives the path of every skill is `the cycle's`: the entry points of the-way's skills carry `disable-model-invocation: true`, so the model is offered none; a human starts a skill with `/the-way-<name>`, a skill hands another on by reading its `SKILL.md` in the-way itself, and a product's hand-over stays through its own entry point. Its *Rejected* gained three ways from the task's *Not chosen* (settings written by the installer, a hand list of exclusions, the file hand-over in a product too); its *Scope* gained `foundation-review` and `product-guidelines`.
- `skill-entry-points` (invariant) — `row 1`, and the list of paths is `the cycle's`: each pair of entry points is byte-identical, holds the field, tells a session not to call another such skill but to read its `SKILL.md`, and lists every such skill with the path of its `SKILL.md`. Its test, `gate/test_skills_reach_the_way_sessions.py`, is changed to check the three added properties; the failing and the passing run are in item 7 of *Checks*.
- `claude-code-skill-model-hiding` (environment fact) — `row 2`: Claude Code removes a skill with `disable-model-invocation: true` from Claude's context, so its description is not in context and Claude does not invoke it on its own, while the user can still invoke it.
- the part-map entry `agent-instructions`, one sentence — `the cycle's`: the entry points are described as the way a human starts the-way's skills in sessions, which Claude Code keeps from the model because of the field in their header while Codex ignores that field and the skills stay visible to the model there (the second half added by correction 1, for your remark 3).

No pair of examples was added; the *complies* and *violates* examples of WAY-127 for the paragraphs of skills were reworded in place.

## Minor findings

1. Two lines of WAY-127 are longer than the 100 columns the rest of the file keeps: `foundations/decisions.md:3344` and `:3397`. The reviewer of the fix: "It is form only; no check covers it." Left unfixed since the review of the fix (WAY-161).
2. (M1, review of correction 1) `gate/test_skills_reach_the_way_sessions.py:228-234` and `AGENTS.md:19-24` say "the line of another skill"; the check also reports a missing line for the entry point's own skill, and both texts open with wording ("whose entry points break…", "each way an entry point breaks…") that does not fit two of the causes they list: a skill file that cannot be read, and a leftover `the-way-*` directory.
3. (M2, review of correction 1) `foundations/part_map.md:170-173`: the statement about Codex rests only on the hand check of remark 1, so nothing in the foundation would flag it if Codex starts honouring the field; it says "the field" without naming it; the clause "and the script that generates them" now reads ambiguously. The reviewer: WAY-90 does not apply, because no decision rests on how Codex treats the field; if WAY-127 were ever to rely on the Codex result it would need an environment fact, since the comment is at a public address.
4. (M3, review of correction 1) WAY-256 with WAY-35: the change rewrites the same hand-over paragraph of about 80 words in 15 skill files, 6 of them element skills, while WAY-35 has an element's skill read the shared way of working from one place. In 14 of the 15 it reads as a single instruction, which WAY-256 allows to stay in place, and WAY-127's *Verification* asks for the paragraph in each skill; the exception is `project-level/lead/skill/SKILL.md:20-27`, which adds a second instruction that only sessions on the-way itself use. The tension is between WAY-127 and WAY-35, and the next task of the queue will meet it.
5. (M4, review of correction 1) WAY-131: the description of this request says a session "now opens that skill's file … and follows it"; no session checked that an agent follows this hand-over rule; the probe sessions checked only that the skills are hidden, and used control skills as WAY-131 asks.

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** the task "skille do rozwijania frameworka nie mają trafiać do produktów, które podpinają go jako podmoduł", an independent task, `Status: ready for cycle`, updated 2026-11-21; the Claude Code documentation page read on 2026-11-21; the Codex and Agent Skills pages read the same day.
- **Process pin:** the-way itself; no pin to move; the checkout was at `19e5774a`, equal to the remote.
- **Spec:** none: the task's rows and answers leave no open design choice; how the entry text and the skills phrase the file hand-over is a way of making what the task settles, named in the author's report.
- **Route:** one author without a plan, class `same` as the orchestrator's (Sonnet 5.5), because the change spans many parts and writes a decision, an invariant and an environment fact; reviewers on Opus 5.5 by the human's instruction.
- **Plan:** none.
- **Choices:** 5 rows in the questions table of the record (Codex answered as an autonomous choice; the model of the reviewers; the unread decisions the author listed; the clause on the list of paths; the Codex result of your remark 1).
- **Blocking findings left:** none.
- **Corrections:** correction 1, for the human's remarks (https://github.com/mariusznazar/the-way/pull/154#issuecomment-7062821019), remarks `reports/correction-1-remarks.md` of the record, no reset (one commit on `48e64f10`): the pairs `item 4 · not-required`, `item 14 · not-required`, `item 8 · not-required`.
- **Record:** RECORD_LINK
