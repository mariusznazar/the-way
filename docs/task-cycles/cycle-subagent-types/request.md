**State: ready** — two items wait for your answer: whether to close a rare hole in the installer in this request, and whether a fresh reviewer should read the part of the decision log the review of the whole change left unscreened; the rest you only accept by merging.

## What you will see

In Claude Code, the stages of a task cycle now run as two agent types that the process defines itself, instead of the general agent. One type is for every stage but the author of the change; the other is for the one author, who is resumed after each review. Both give the agent every tool of the session except the tool that calls skills, so the agent no longer starts with the list of all skills in its context and reads the method of its stage as a file by its path. The one author's type also keeps the agent's prompt cache for an hour instead of five minutes, so a review between its turns no longer makes it write its whole context again. The cycle's own instructions say which type each stage gets, and what the orchestrator does where the session has no such type (another harness, or a session started before the definitions existed): dispatch as before and write that in the record.

The installer puts the two definitions into a product from the pinned process commit, next to the skill entries, and changes or deletes only the files it wrote itself; the preview shows them before you confirm. A session working on the process itself has the same definitions as generated, tracked copies, so cycles of the process use them too. A session that started before the folder of definitions existed does not load them: the first cycle after this merge, run from such a session, runs its stages without the types and records it.

The task asked for one probe on the Claude Code version in use, and it ran. On Claude Code 2.1.325 with model Claude Sonnet 5.5, a fresh session started in the task's worktree dispatched an agent of each type and a general agent. Both agents of the new types reported that their context holds no list of skills and that they have no skill tool; the general agent reported both. The agent of the stage type began with 25,321 tokens of context, the author type with 25,369 (all of it written to the one-hour cache), the general agent with 37,109, so the start is about 32 percent lighter. The task estimated 37 percent from a table of tool definitions; this is the measured figure for one start, one version and one model, not an average.

### Underneath

Each type is a small definition file in the process repository, a script generates the tracked copies for sessions on the process itself and a test compares them with it, and the installer writes the same files into a product as a new group it owns; three new decisions and seven new environment facts record why.

## For you to decide

### Needed from you

none

### Fix or let through

1. If a product's folder for agent settings is a Windows junction (a folder shortcut) to another place, the installer follows it and writes the process's files there — the new agent definitions and, since before this change, the skill entries — instead of refusing. Only the person who owns the product can make such a junction, since git does not carry one in a clone, so the realistic case is a developer who set it up for themselves; the effect would be files written outside the product folder. Ways: fix it in this request — one more check in the installer, a test and one round of review of a change at the installer's boundary; make a task of it — the installer stays as it was before this change; let it through — the same, with no task. I recommend making a task of it, since the same hole existed before this change and the change adds no new kind of exposure. Fix it now, make a task of it, or let it through? (Minor findings, 3; Findings outside the task's scope, 1)
2. The review of the whole change read 8 decisions of its selection whole and did not run through the rest of the decision log by title, so a decision outside those 8 that bears on this change could have gone unseen; the reviewer knows of none. If one did, it shows up later as two decisions that say different things, when someone relies on the wrong one. Ways: read it in this request — a fresh reviewer reads what stayed unread, which costs one more review and changes nothing unless it finds something; make a task of it; let it through — the author's search of the whole foundation and the return step's comparison already covered the entries this change touches. I recommend letting it through for that reason. Read it now, make a task of it, or let it through?

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

3. The cycle chose where the definitions live and what they are called, since the task left it open: the source is a folder of the process's cycle files, a new script generates byte-identical tracked copies for the process's own sessions (the existing script for skill entries is not stretched), and the types are named with the process's prefix, "the-way-stage" and "the-way-author", so that a product's own agent of a plain name cannot be taken for them. The tools are given by denying the skill tool, with no list of tools, so connected servers keep their tools. The price: two scripts to remember for generated files instead of one, and a rename would touch the definitions, one constant of the installer and its tests.
4. The decision about how long agents may wait for a command gained one sentence the task does not give: where Claude Code falls back to the five-minute cache because a subscription is spending usage credits, the one author still keeps its own waits under about four minutes, as every agent does. The task asked only that the author's cache lives an hour. I kept it because without it an author that waits long on the strength of the hour would write its whole context again in that fallback; the reviewer recommended leaving it and naming it here.
5. The four method names (`write-spec`, `plan-task`, `make-change`, `review-change`) stay in the orchestrator's instructions as labels of the four method files, and the instructions now give each file's path and say that an agent never calls a skill for them; I did not replace every one of about 25 "with <name>" clauses by a path, since the handoff paragraph already requires the path and the text would repeat four paths 25 times. The reviewer judged that this fulfils the task. The price: a reader of a clause alone sees a skill name until they read the step that defines it.
6. Foundation entries the cycle wrote or changed that you did not see at the task document:
   - the decision about how long an agent waits for a command now says the one author's cache lives an hour, set by its type, and keeps the rejection of an hour for every agent with an account by kind of agent;
   - the decision about what may enter the process repository now also allows the copies of the agent definitions;
   - the decision about which version of the process a product uses now says the first commit of a pin move also carries the agent definitions the installer rewrote;
   - the part map names the definitions, their copies and what the installer rewrites and deletes, in three entries;
   - seven environment facts record what the Claude Code and Codex documentation pages say that these decisions stand on (five about Claude Code, two about Codex), each with an archived copy that already existed, and the three new decisions and the changed one now cite them;
   - one sentence of the decision about Codex was corrected in the return step, since it said more than the cited page.
7. The command that installs the process into a product changes its surface: besides skill entries it now writes, replaces and deletes the process's own agent definitions in the product's folder for agent definitions, refuses a file that is not its own, and never removes that folder.

## Cost

Working time of the cycle's agents across the orchestrator's session up to this description: 1 hour 21 minutes 36 seconds, of which 42 minutes 52 seconds waiting for tools. Models: the orchestrator, the author and every reviewer Claude Sonnet 5.5 (the author on the orchestrator's class, since the change reaches four parts and a trust boundary and writes decisions); about 77.7 million tokens, 75.9 million of them cached input and 296 thousand output. Review rounds: the review of the whole change passed with eight Minor findings within the task; one fix and one review of it, which passed with three new Minor findings; the return step's commit had its own review, which passed with one Minor finding within the task and one outside it. The gate ran once, on the final tree, and passed (764 seconds). The table of stages is in the committed record.

## How to merge

Merge with a merge commit, not a squash or a rebase: the link to the record survives only when the commits are kept. The foundation has waited for a review through 34 merges since the last tag; the review is the skill `the-way-review-foundation`, started in a session in this repository, and nothing in this request waits for it.

<details>
<summary>Po polsku</summary>

**Stan: gotowa** — dwie pozycje czekają na Twoją odpowiedź: czy w tej prośbie zamknąć rzadką dziurę w instalatorze oraz czy świeży recenzent ma przeczytać część dziennika decyzji, której przegląd całej zmiany nie przejrzał; resztę tylko przyjmujesz przez scalenie.

## Co zobaczysz

W Claude Code etapy cyklu zadania idą teraz dwoma typami agentów, które proces definiuje sam, zamiast zwykłym agentem ogólnym. Jeden typ jest dla każdego etapu poza autorem zmiany, drugi dla jednego autora, który jest wznawiany po każdym przeglądzie. Oba dają agentowi każde narzędzie sesji poza narzędziem wywołującym skille, więc agent nie startuje już z listą wszystkich skilli w kontekście, a metodę swojego etapu czyta jako plik po ścieżce. Typ jednego autora trzyma też pamięć podręczną agenta przez godzinę zamiast pięciu minut, więc przegląd między jego turami nie każe mu zapisywać całego kontekstu od nowa. Instrukcje cyklu mówią, jaki typ dostaje każdy etap i co robi orkiestrator, gdy sesja takiego typu nie ma (inna uprząż albo sesja uruchomiona, zanim definicje powstały): zleca jak dotąd i zapisuje to w zapisie cyklu.

Instalator wstawia obie definicje do produktu z przypiętego commita procesu, obok wejść skilli, i zmienia albo usuwa tylko pliki, które sam zapisał; podgląd pokazuje je przed potwierdzeniem. Sesja pracująca nad samym procesem ma te same definicje jako wygenerowane, śledzone kopie, więc cykle procesu też z nich korzystają. Sesja uruchomiona, zanim katalog definicji istniał, ich nie ładuje: pierwszy cykl po tym scaleniu, prowadzony z takiej sesji, puści swoje etapy bez tych typów i to zapisze.

Zadanie prosiło o jedną sondę na używanej wersji Claude Code i ona się odbyła. Na Claude Code 2.1.325 z modelem Claude Sonnet 5.5 świeża sesja uruchomiona w katalogu roboczym zadania zleciła po agencie każdego z dwóch typów oraz agenta ogólnego. Agenci obu nowych typów zgłosili, że ich kontekst nie ma listy skilli i że nie mają narzędzia skilli; agent ogólny zgłosił jedno i drugie. Agent typu etapów zaczął z 25 321 tokenami kontekstu, typ autora z 25 369 (całość zapisana do pamięci godzinnej), agent ogólny z 37 109, więc start jest lżejszy o około 32 procent. Zadanie szacowało 37 procent z tabeli definicji narzędzi; to jest zmierzona wartość jednego startu, jednej wersji i jednego modelu, nie średnia.

### Pod spodem

Każdy typ to mały plik definicji w repozytorium procesu, skrypt generuje śledzone kopie dla sesji na samym procesie, a test porównuje je z definicją, zaś instalator wpisuje te same pliki do produktu jako nową grupę, którą sam posiada; trzy nowe decyzje i siedem nowych faktów o środowisku zapisują, dlaczego.

## Do twojej decyzji

### Wymagane od Ciebie

none

### Do poprawienia albo przepuszczenia

1. Jeśli katalog produktu na ustawienia agentów jest junction Windows (skrótem do folderu) wskazującym inne miejsce, instalator idzie za nim i zapisuje pliki procesu tam — nowe definicje agentów i, już przed tą zmianą, wejścia skilli — zamiast odmówić. Taki junction może zrobić tylko właściciel produktu, bo git nie przenosi go przy klonowaniu, więc realny przypadek to programista, który ustawił go sobie sam; skutkiem byłyby pliki zapisane poza katalogiem produktu. Warianty: poprawić to w tej prośbie — jedno dodatkowe sprawdzenie w instalatorze, test i jedna runda przeglądu zmiany na granicy zaufania instalatora; zrobić z tego zadanie — instalator zostaje taki, jaki był przed tą zmianą; przepuścić — to samo, bez zadania. Polecam zrobić z tego zadanie, bo ta sama dziura istniała przed tą zmianą, a zmiana nie dodaje nowego rodzaju ekspozycji. Poprawić teraz, zrobić zadanie czy przepuścić? (Minor findings, 3; Findings outside the task's scope, 1)
2. Przegląd całej zmiany przeczytał w całości 8 decyzji ze swojego wyboru i nie przejrzał reszty dziennika decyzji po tytułach, więc decyzja spoza tych 8, która ma związek z tą zmianą, mogła zostać niezauważona; recenzent żadnej takiej nie zna. Gdyby taka była, wyjdzie później jako dwie decyzje mówiące co innego, gdy ktoś oprze się na niewłaściwej. Warianty: przeczytać to w tej prośbie — świeży recenzent czyta, co zostało nieprzeczytane, co kosztuje jeszcze jeden przegląd i niczego nie zmienia, jeśli nic nie znajdzie; zrobić z tego zadanie; przepuścić — wyszukanie autora w całym fundamencie i porównanie kroku zwrotnego objęły już wpisy, których ta zmiana dotyka. Polecam przepuścić z tego powodu. Przeczytać teraz, zrobić zadanie czy przepuścić?

### Przyjmujesz przez scalenie

Scalenie przyjmuje te pozycje; jeśli któraś Ci nie odpowiada, powiedz która.

3. Cykl wybrał, gdzie leżą definicje i jak się nazywają, bo zadanie zostawiło to otwarte: źródłem jest katalog plików cyklu w procesie, nowy skrypt generuje identyczne bajt w bajt śledzone kopie dla sesji na samym procesie (istniejący skrypt wejść skilli nie jest rozciągany), a typy mają przedrostek procesu, „the-way-stage” i „the-way-author”, żeby własnego agenta produktu o zwykłej nazwie nie dało się wziąć za nie. Narzędzia dane są przez zabranie narzędzia skilli, bez listy narzędzi, więc podłączone serwery zachowują swoje narzędzia. Cena: dwa skrypty do zapamiętania przy plikach generowanych zamiast jednego, a zmiana nazwy dotknęłaby definicji, jednej stałej instalatora i jego testów.
4. Decyzja o tym, jak długo agenci mogą czekać na polecenie, zyskała jedno zdanie, którego zadanie nie podaje: tam, gdzie Claude Code wraca do pamięci pięciominutowej, bo subskrypcja wydaje kredyty ponad plan, jeden autor nadal trzyma własne oczekiwania poniżej około czterech minut, jak każdy agent. Zadanie prosiło tylko, żeby pamięć autora żyła godzinę. Zostawiłem je, bo bez niego autor czekający długo na podstawie godziny zapisałby w tym powrocie cały kontekst od nowa; recenzent polecił je zostawić i nazwać tutaj.
5. Cztery nazwy metod (`write-spec`, `plan-task`, `make-change`, `review-change`) zostają w instrukcjach orkiestratora jako etykiety czterech plików metod, a instrukcje podają teraz ścieżkę każdego pliku i mówią, że agent nigdy nie wywołuje do nich skilla; nie zastąpiłem ścieżką każdej z około 25 klauzul „z <nazwą>”, bo akapit o zleceniu już wymaga ścieżki, a tekst powtarzałby cztery ścieżki 25 razy. Recenzent uznał, że to spełnia zadanie. Cena: czytelnik samej klauzuli widzi nazwę skilla, dopóki nie przeczyta kroku, który ją definiuje.
6. Wpisy fundamentu, które cykl napisał lub zmienił, a których nie widziałeś przy dokumencie zadania:
   - decyzja o tym, jak długo agent czeka na polecenie, mówi teraz, że pamięć jednego autora żyje godzinę, ustawia ją jego typ, i zachowuje odrzucenie godziny dla każdego agenta wraz z rachunkiem według rodzaju agenta;
   - decyzja o tym, co może wejść do repozytorium procesu, dopuszcza teraz także kopie definicji agentów;
   - decyzja o tym, której wersji procesu używa produkt, mówi teraz, że pierwszy commit przesunięcia przypięcia niesie też definicje agentów, które przepisał instalator;
   - mapa części wymienia definicje, ich kopie oraz to, co instalator przepisuje i usuwa, w trzech wpisach;
   - siedem faktów o środowisku zapisuje, co mówią strony dokumentacji Claude Code i Codexa, na których te decyzje stoją (pięć o Claude Code, dwa o Codexie), każdy z istniejącą już zarchiwizowaną kopią, a trzy nowe decyzje i zmieniona je teraz cytują;
   - jedno zdanie decyzji o Codexie poprawił krok zwrotny, bo mówiło więcej niż cytowana strona.
7. Polecenie, które instaluje proces w produkcie, zmienia swoją powierzchnię: poza wejściami skilli zapisuje teraz, zastępuje i usuwa własne definicje agentów procesu w katalogu produktu na definicje agentów, odmawia przy pliku, który nie jest jego, i nigdy nie usuwa tego katalogu.

## Koszt

Czas pracy agentów cyklu w sesji orkiestratora do tego opisu: 1 godzina 21 minut 36 sekund, z czego 42 minuty 52 sekundy to oczekiwanie na narzędzia. Modele: orkiestrator, autor i każdy recenzent Claude Sonnet 5.5 (autor na klasie orkiestratora, bo zmiana dotyka czterech części i granicy zaufania oraz pisze decyzje); około 77,7 mln tokenów, z czego 75,9 mln to wejście z pamięci podręcznej, a 296 tys. wyjście. Rundy przeglądu: przegląd całej zmiany zakończył się wynikiem PASS z ośmioma uwagami Minor w zakresie zadania; jedna poprawka i jeden jej przegląd, PASS z trzema nowymi uwagami Minor; commit kroku zwrotnego miał własny przegląd, PASS z jedną uwagą Minor w zakresie zadania i jedną poza nim. Bramka biegła raz, na końcowym drzewie, i przeszła (764 sekundy). Tabela etapów jest w zatwierdzonym zapisie.

## Jak scalić

Scal commitem scalającym, nie squashem ani rebase: link do zapisu przetrwa tylko przy zachowanych commitach. Fundament czeka na przegląd po 34 scaleniach od ostatniego tagu; przegląd to skill `the-way-review-foundation`, uruchamiany w sesji w tym repozytorium, a nic w tej prośbie na niego nie czeka.

</details>

## Technical changes

1. Commit `07cb56a` — the two definitions `task-cycle/agent-types/the-way-stage.md` and `task-cycle/agent-types/the-way-author.md` (frontmatter `disallowedTools: Skill`, no `tools` list, no `omitClaudeMd`, no `model`; the author's adds `experimental: cacheTtl: 1h`; each with a two-paragraph body), the generator `agent-instructions/agent_type_copies.py` that writes byte-identical tracked copies into `.claude/agents/` and lists a stray one, the copies, `agent-instructions/test_agent_type_copies.py` (copies equal the generator's output, cites the invariant `derived-file-content`) and `task-cycle/test_agent_types.py` (content checks of the definitions).
2. Commit `1239ae2` — `installation/install.py` (a new group of files the installer owns: `AGENT_TYPES`, an own-file rule by regular UTF-8 file `the-way-<words>.md`, header name equal to the file name and a closing sentence of the description; REPLACE and DELETE only of its own; refusals before anything is written; never removes `.claude/agents/`), `installation/README.md`, `installation/test_agent_types_installation.py` (12 tests, each as preview and with `--apply`), `task-cycle/skill/SKILL.md` (a paragraph on the types after the handoff paragraph, and clauses at steps 2, 3 and 9), `task-cycle/skill/foundation_step.md`, `task-cycle/skill/return_step.md`, `task-cycle/change/SKILL.md`, `task-cycle/plan/SKILL.md` (a method is a file read by its path, never a skill called), `task-cycle/record_template.md` (the record names the type of a dispatch or why none), the decision log, the part map, `AGENTS.md`, `README.md` and `instruction-files/judging.md` (what the installer writes and the command that generates the copies).
3. Commit `2245f08` — line breaks of the paragraph added to `task-cycle/skill/SKILL.md`; no word changed.
4. Commit `b0ab508` — the fix of the Minor findings of the review of the whole change: the conditions of the 10.5 thousand token figure stated as not recorded (M2), added lines wrapped (M3), the path of the method file at the first mention of each method name in `planning.md`, `spec_review.md`, `return_step.md` and `correction.md` (M4), "where it has no skill tool" in `task-cycle/plan/SKILL.md` and `foundation_step.md` (M5), the kind of an installer path named by `is_agent_definition` instead of by a file name (M6), the orchestrator told to look at the agent types its dispatch tool offers (M8); M1 and M7 contested.
5. Commit `f1ff7d6` — the return step wrote seven environment facts (`claude-code-subagent-skills-denied`, `claude-code-subagent-cache-ttl`, `claude-code-subagent-cache-ttl-credits`, `claude-code-subagent-agent-directories`, `claude-code-subagent-instruction-files`, `codex-project-agents`, `codex-agent-skills-config`), changed the *Based on* of WAY-255, WAY-368, WAY-369 and WAY-370 to name them, and corrected WAY-370's *Rationale*.

## Checks

- The gate on the final tree `f1ff7d6`: `python -B task-cycle/gate_times.py --output docs/task-cycles/cycle-subagent-types/gate_times.md -- python -B gate/run_tests.py`, exit 0, 1265 tests in 10 directories, every directory passed, 764 seconds. No gate ran on the base: `715ae20` is a merge commit whose tree equals that of its second parent, so the list of failing tests was taken from the final gate of the earlier cycle `gate-parallel-directories` (its record at commit `575f286`, *Verification*): exit 0, 1238 tests, none failing. No check failed or did not run, and none failed and passed again.
- The acceptance probe, run by the orchestrator with `claude -p --model claude-sonnet-5-5 --allowedTools Agent` from the task's worktree on Claude Code 2.1.325, twice (once for the stage type and a general agent, once for the author type), both exit 0: the agents of both types report no list of skills in their context and no tool named Skill, the general agent reports both. First-call context from the subagent transcripts: stage type 25,321 tokens, author type 25,369 (`ephemeral_1h_input_tokens` 25,367, `ephemeral_5m_input_tokens` 0), general agent 37,109. One start each; one version and one model.
- Focused checks of the author, each exit 0: `python -B elements/common/foundation_check.py` (0 errors), the gates `agent-instructions` (25 tests), `task-cycle` (394), `instruction-files` (104, 5 skipped, not by this change), `installation` (56) and `installation/test_agent_types_installation.py` (12). Mutation checks: the installer's own-file rule and stale rule broken five ways, the generator four ways and the definitions five ways, each caught by a test; the fix's helper `is_agent_definition` made always false and always true, caught each time.
- Own-work check of the author: the requirement most likely unmet was the probe's, which the author could not run and the orchestrator did; the installer's trust boundary is held by twelve crafted-input tests (a user's file at a definition path, a header naming another type, a missing mark, non-UTF-8, a directory at the path, `.claude` or `.claude/agents` as a file, a symlinked `.claude`, a symlinked `.claude/agents`, a symlinked definition, a dangling symlink), each refused before anything was written. The reviewers repeated them with a CRLF own file, a stale own file, a lookalike and a symlinked agents folder, and found a Windows junction at `.claude` accepted (Findings outside the task's scope, 1).
- The state of user-interface screens: not applicable, the change touches no screen.
- `python -B task-cycle/review_reminder.py origin/foundations`: exit 0, `tag: foundation-review/2026-11-06`, `merges: 34`, `threshold: 30`, `reminder: yes`.
- `python -B task-cycle/cycle_stages.py` and `python -B task-cycle/cycle_measures.py` for the orchestrator's session: both exit 0.
- On the copy of the record and on this description: written and checked after this description was first published (see the edit that adds the record's link).

## Foundation entries

- WAY-368, row 1: in Claude Code the cycle runs the one author as an agent of the type `the-way-author` and every other stage agent as `the-way-stage`, two types without the skill tool, so a method is a file read by its path; the installer writes the definitions of the pinned commit and the copies for the process's own sessions are generated.
- WAY-369, row 2: the two types start with the instruction files of the session; no definition sets `omitClaudeMd`.
- WAY-370, row 3: where the session has none of the types — another harness, or a session started before they could load — the cycle dispatches as before and records it in the row of the dispatch; there are no types for Codex.
- WAY-255, `the cycle's`: the one author's prompt cache lives an hour, set by its type; its waits stay under about four minutes; the hour for every agent stays rejected, with the account by kind of agent.
- WAY-09 and WAY-34, `the cycle's`: the repository also holds the copies of the agent definitions under `.claude/agents/`; the first commit of a pin move carries the agent definitions the installer rewrote.
- The part-map entries `task-cycle`, `agent-instructions` and `installation-command`, `the cycle's`: they name the definitions, their copies and what the installer rewrites and deletes; `installation-command` is a surface and is altered.
- Seven environment facts, `the cycle's` (return step): the sources of the cache lifetime and its usage-credits fallback, the skill tool denied, the folders Claude Code watches for definitions, the instruction files a type loads, and Codex's project agents and per-skill setting.

No invariant, glossary entry or projected entry is written, and no invariant test or *Violated* mark is changed.

## Minor findings

1. Review of the whole change, M1 (declined by the author, kept by the reviewer). `foundations/decisions.md` WAY-255, binding paragraph and *Verification*: "its waits stay under about four minutes as well, since Claude Code falls back to five minutes where a subscription spends usage credits", plus the complies/violates examples. The reviewer: "The task's To do 6 gives only 'the one author's cache lives an hour'; its Context gives the fallback as a fact and prescribes no rule about waits. The sentence is therefore a binding rule the task does not give. It keeps today's behaviour for waits (no cost if left) ... I grade it Minor and recommend leaving it, naming it in the request so the human sees it was the author's addition." (Item 4 above.)
2. Review of the whole change, M7 (declined; the probe has run). `installation/README.md`, the row for the definitions, and WAY-368 *Rationale* state that an agent of the types "starts without the list of skills". The reviewer: "If the probe shows the list stays, these two statements and WAY-368's premise change together. Not a defect of the files today; a dependency on the probe." The probe showed the list gone.
3. Review of the fix, N1. `task-cycle/skill/SKILL.md` line 209 (135 columns), `task-cycle/skill/correction.md` lines 29 and 37 (131 and 123), `task-cycle/skill/foundation_step.md` line 19 (130), `task-cycle/skill/planning.md` line 8 (120), `task-cycle/skill/spec_review.md` line 5 (124). The reviewer: "They are the lines of M4, M5 and M8 inserted without rewrapping the paragraph, so the finding M3 reopens for them in layout only. ... Layout only; no test fails on them."
4. Review of the fix, N2. `installation/install.py`, docstring of `is_agent_definition`, second line, 101 columns: "one column over the 100 of the file's other lines. Layout only."
5. Review of the fix, N3, remark. `task-cycle/record_template.md`, the Events sentence: "now ends '…and why.' on its own line and the next line 'Name handoff and report paths and input and output commits, so work' is short; the paragraph reads correctly, only the break is odd. No action."
6. Review of the return step, Minor 1. `foundations/decisions.md` WAY-370, *Rationale*, second sentence: "'a setting for each' reads as one setting per skill, which the passage does not say. ... Suggested wording: 'Codex turns off the skills of an agent one skill at a time, with `skills.config`, so ...'." A departure of a rationale clause from the fact it paraphrases; the binding sentence and the fact agree with the source.

## Findings outside the task's scope

1. Review of the whole change, O1, Minor. `installation/install.py` `check_parents`: "accepts a Windows directory junction as a regular directory (`is_symlink()` is false for a junction, `is_dir()` true). I tried it: a product with `.claude` as a junction to a directory outside the product, `printf 'y\n' | python -B installation/install.py <product> --url <worktree> --apply` exit 0, and `outside1/agents/the-way-author.md`, `outside1/agents/the-way-stage.md` and the `skills/the-way-*` entry points were written outside the product. The same holds for the skills' entry points since before this change (the check is shared), so the new agent paths add no new exposure class; and a junction cannot arrive with a clone (git carries symlinks, not junctions), only from the product's own user. Pre-existing; a task of its own if the human wants it (`os.path.isjunction` in `check_parents`)." (Item 1 of *Fix or let through*.)
2. Review of the whole change, O2, Minor. "A stray product file `.claude/agents/the-way-ghost.md` whose header names `the-way-author` is kept (correct) but then two files of the product's agent directory carry the name `the-way-author`; Claude Code resolves the duplicate by its own rule. The installer cannot and should not decide it. Noted only."
3. Review of the return step, Minor 2, out of scope. `foundations/decisions.md` WAY-255, *Based on*, the first three quotes of the prompt-caching page: "still quotes the prompt-caching page ... These quotes were in WAY-255 before this task ... A later change of WAY-255 or the review of the foundation may turn them into facts."

## Course of the cycle

- **Task and sources:** an independent task from the author's backlog, ready for cycle: the stages of a cycle in Claude Code run as two agent types of the process with no skill tool, the installer and the process's own sessions carry the definitions, the one author's cache lives an hour, and every method is pointed at by its file path. Sources: the task's four answers of 2026-11-12 and 2026-11-13, its three settlement rows, the decisions in play; the-way at `715ae20` of `foundations`.
- **Process pin:** none; the-way itself, base `715ae20` of `foundations`; no gate on the base (the list was taken from the earlier cycle's final gate, none failing).
- **Spec:** none written; no open design choice (the source location, the generator, the names and the wording were choices of how to make what the task settles).
- **Route:** one author without a plan, class `same` (Sonnet), because the change reaches four parts and a trust boundary and writes decisions; review of the whole change by a fresh reviewer on Sonnet (`PASS`, eight Minor findings within the task); one fix and one review of it by the same reviewer (`PASS`, three new Minor findings); return step with its own review (`PASS`). No stage ran under the new types, since the orchestrator's session started before the definitions existed (the fallback of WAY-370).
- **Plan:** none on this route.
- **Choices:** 4 choices of the cycle beyond the questions answered by a binding source (the record's questions table, Q4 to Q7; items 3 to 5 above and the class of the return step's review).
- **Blocking findings left:** none.
- **Record:** the link by the SHA of the commit that adds it, written after the commit.
