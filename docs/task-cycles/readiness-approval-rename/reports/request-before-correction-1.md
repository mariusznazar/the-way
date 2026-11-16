**State: ready** — the code is finished and reviewed and the CI run on the last head passed; two items below wait for your answer.

## What you will see

In the process, one word no longer means two things. "Gate" now means only the command that runs all the tests. The moment when you approve a project definition is called the "readiness approval", the section where the approval is written is the "approval record", and a definition that is ready for you to approve has the status "awaiting approval" (it was "ready for gate"). The rule that the checking script for a definition follows has a new name too. Wherever the process or its scripts spoke of the approval as a "gate", they now say "approval", so an agent that leads a project definition cannot take "the gate" for "run the tests" any more.

Two other words are separated the same way. The key of the file that lists where your notes live is now called a "key", not an "entry", and a task's place in the backlog is called "the task's line in the backlog". "Entry" now means an entry of the foundation. One more sentence, in the step that researches a technology, no longer says "read off" for a property taken from documentation; "read off" stays for a value a tool gives. The glossary also explains a new term, the "projected entry": the wording, written in a project definition, of a foundation entry that the foundation is to hold once a task's code makes it true.

A product that moves its pinned version of the process past this change has two edits to make in its own files. In its approved project definitions, the heading `## Gate record` becomes `## Approval record`, because the checking script now refuses the old heading and the old status. In the section about the backlog of its main instructions file, "the entry `tasks` under …" and the similar sentences become "the key `tasks` under …". The only product that has approved definitions today, loop2, makes both edits itself when it moves its pin; nothing in this request touches it.

### Underneath

The change is a rename of words in 59 files — the glossary, the decision log, the project steps, two checking scripts and their tests, the instruction file and the generated skill entry points — plus one new glossary entry and two new tests that hold the refusal of the old heading and the old status; no rule of the process changed its meaning.

## For you to decide

### Needed from you

none

### Fix or let through

1. The agent that reviewed the whole change read 23 of the 199 decisions it selected in full and named four decisions that bear on this change as read only in the passages the change touches, not in full. In those four, the change only replaces words, and the reviewer judged the meaning kept in each place it changed. If one of the four was changed wrongly, a later agent that relies on it would work from a wrong sentence and nobody would see the rename was the cause. Having a fresh reviewer read the four in full costs one more review round; undoing it, nothing. Making a task of it leaves the four unread until someone takes it; undoing it, nothing. Letting it through accepts the risk; undoing a wrong sentence later costs a correction. I recommend letting it through, since the review compared every changed line against the task and the decisions' meaning. Its weak point: the reviewer's own check does not prove the four read whole. Read them in this request, make a task of it, or let it through? (Course of the cycle, Route)

2. After this change the word "entry" is still used in the description of a cycle's record for an item of a list (a line of the record's table), which is a third meaning beside the foundation entry. The task said that "entry" would mean only the foundation entry after this change. The reviewer found no sentence that is true in one meaning and false in the other, so the rule for splitting meanings is not broken today; but a reader who knows the glossary may still take a "record entry" for a foundation entry. Fixing it now costs a further round of correction and review in the same files (about thirteen places); undoing it, nothing. Making a task of it costs a later cycle; undoing it, nothing. Letting it through leaves the third meaning standing; undoing it later costs one task. I recommend making a task of it, since the task named only the two meanings the foundation review found and this one needs its own judgment of which word to use. Its weak point: until that task is done, the claim that "entry" means only a foundation entry is not true for the cycle's record. Do it in this request, make a task of it, or let it through? (Findings outside the task's scope, 1)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

3. The first clause of the decision about the readiness approval now reads "The readiness approval is blocked by a missing section, …" in place of "The readiness gate blocks a definition with a missing section, …". I chose this because the approval is an act of yours and cannot block anything; the script that checks the definition is what holds it back. The reviewer judged the meaning kept. The other way was "the readiness approval blocks a definition", which would have said the approval does something it does not.
4. In one rejected way of an earlier decision, "intermediate human gates" became "intermediate human approvals", because "gate" in the glossary now means only the test command. The sentence still rejects the same way.
5. In the two checking scripts and their tests, the names that carried "gate" in the approval meaning were renamed with it (for example the constant for the heading and the function that checks it), and the file of the project step that describes the approval is now named after it. The other choice was to leave the code names alone, but then the old word would stand in the meaning that moved. Nothing outside the project steps imports those names.
6. The two new tests that hold the refusal of the old heading and status cite the invariant about the form of a definition, not the one about readiness checks that I named in the fix handoff, because its sentence is the one that covers an unexpected section and an invalid status.
7. Four existing tests of the audit script were edited, because the messages of the script now say "key" where they said "entry": three expected pieces of message text and four test names changed; the checks they make are as strong as before and the script accepts and refuses exactly what it did.
8. Foundation entries the cycle changed that you did not see at the task: the same word-for-word renames in 21 other decisions and in the withdrawn row of one more (the decisions that spoke of the approval as a gate, or of a key of the locations file as an entry, or of a backlog entry); no decision changed its meaning. Each is listed under *Foundation entries*.

Changed invariant tests, in plain words: the invariant about the readiness check now has the identifier `project-readiness-check` (it was `project-readiness-gate`), as you chose; its tests changed only in the line that cites it and in the words of their inputs, with no assertion weakened. Four tests of the plan and technology checks changed their inputs only. Two tests are new (above). The foundation check listed no invariant for a corrected sentence, and no test of a decision changed.

## Cost

About 1 hour 6 minutes of active stages in about 71 million tokens: the author on Sonnet (the change, the fix of three Minor findings, the return step), three reviews on Opus (the whole change, the fix, the reconciliation with the target branch) and the orchestrator on Sonnet. One fix round ran after the first review, and it was not blocking. The table of stages is in the committed record, linked below. No working copy of an agent and no directory of an earlier task is waiting for you, except one directory of an earlier task that the cleaning script could not tell was finished (below); nothing in this request waits for it.

## How to merge

Merge with a merge commit, not squash or rebase, so that the link to the cycle's record, which names a commit, stays reachable. Nothing in this request waits for a review of the foundation.

<details>
<summary>W języku zadania (po polsku)</summary>

**Stan: gotowe** — kod jest gotowy i sprawdzony, a przebieg CI na ostatnim commicie przeszedł; dwie pozycje poniżej czekają na Twoją odpowiedź.

## Co zobaczysz

W procesie jedno słowo nie znaczy już dwóch rzeczy. „Gate” znaczy teraz tylko polecenie uruchamiające wszystkie testy. Moment, w którym zatwierdzasz definicję projektu, nazywa się „readiness approval”, sekcja, w której zatwierdzenie jest zapisane, to „approval record”, a definicja gotowa do zatwierdzenia ma status „awaiting approval” (był „ready for gate”). Reguła, według której skrypt sprawdzający definicję, też ma nową nazwę. Wszędzie tam, gdzie proces albo jego skrypty nazywały zatwierdzenie „gate”, mówią teraz „approval”, więc agent prowadzący definicję projektu nie weźmie już „the gate” za „uruchom testy”.

Dwa inne słowa rozdzielono tak samo. Klucz pliku, który wskazuje, gdzie leżą Twoje notatki, nazywa się teraz „key”, a nie „entry”, a miejsce zadania w backlogu — „the task's line in the backlog”. „Entry” znaczy teraz wpis fundamentu. Jedno zdanie w kroku badania technologii nie mówi już „read off” o właściwości wziętej z dokumentacji; „read off” zostaje dla wartości, którą podaje narzędzie. Słownik tłumaczy też nowy termin „projected entry”: brzmienie, zapisane w definicji projektu, wpisu fundamentu, który fundament ma przyjąć, gdy kod zadania uczyni go prawdziwym.

Produkt, który przesuwa przypiętą wersję procesu za tę zmianę, ma do zrobienia dwie poprawki we własnych plikach. W zatwierdzonych definicjach projektu nagłówek `## Gate record` zmienia się na `## Approval record`, bo skrypt sprawdzający odrzuca teraz stary nagłówek i stary status. W sekcji o backlogu głównego pliku instrukcji „the entry `tasks` under …” i podobne zdania zmieniają się na „the key `tasks` under …”. Jedyny produkt z zatwierdzonymi definicjami, loop2, zrobi obie poprawki sam przy przesunięciu wersji; to żądanie go nie dotyka.

### Pod spodem

Zmiana to zamiana słów w 59 plikach — słownik, dziennik decyzji, kroki projektu, dwa skrypty sprawdzające i ich testy, plik instrukcji i wygenerowane punkty wejścia skilli — plus jeden nowy wpis słownika i dwa nowe testy, które utrzymują odrzucenie starego nagłówka i starego statusu; żadna reguła procesu nie zmieniła znaczenia.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

brak

### Popraw albo przepuść

1. Agent, który sprawdzał całą zmianę, przeczytał w całości 23 z 199 wybranych decyzji i cztery decyzje dotyczące tej zmiany nazwał przeczytanymi tylko we fragmentach, których zmiana dotyka. W tych czterech zmiana tylko zastępuje słowa, a recenzent uznał znaczenie za zachowane w każdym zmienionym miejscu. Gdyby jedna z czterech została zmieniona błędnie, późniejszy agent, który na niej polega, pracowałby ze złym zdaniem i nikt nie zobaczyłby, że przyczyną była zamiana słów. Świeży recenzent czytający te cztery w całości to jedna runda przeglądu więcej; cofnięcie — nic. Zadanie na to zostawia cztery nieprzeczytane do czasu jego wzięcia; cofnięcie — nic. Przepuszczenie przyjmuje ryzyko; cofnięcie błędnego zdania później kosztuje poprawkę. Polecam przepuścić, bo przegląd porównał każdą zmienioną linię z zadaniem i znaczeniem decyzji. Słaby punkt: sprawdzenie recenzenta nie dowodzi, że cztery zostały przeczytane w całości. Przeczytać je w tym żądaniu, zrobić z tego zadanie, czy przepuścić? (Course of the cycle, Route)

2. Po tej zmianie słowo „entry” jest wciąż używane w opisie zapisu cyklu dla pozycji listy (wiersza tabeli zapisu), czyli w trzecim znaczeniu obok wpisu fundamentu. Zadanie mówiło, że po tej zmianie „entry” znaczy tylko wpis fundamentu. Recenzent nie znalazł zdania prawdziwego w jednym znaczeniu i fałszywego w drugim, więc reguła rozdzielania znaczeń nie jest dziś złamana; ale czytelnik znający słownik może wziąć „wpis zapisu” za wpis fundamentu. Poprawa teraz to kolejna runda poprawki i przeglądu w tych samych plikach (około trzynaście miejsc); cofnięcie — nic. Zadanie na to to późniejszy cykl; cofnięcie — nic. Przepuszczenie zostawia trzecie znaczenie; cofnięcie później kosztuje jedno zadanie. Polecam zrobić z tego zadanie, bo zadanie nazwało tylko dwa znaczenia, które znalazł przegląd fundamentu, a to wymaga własnego osądu, jakiego słowa użyć. Słaby punkt: do czasu tego zadania twierdzenie, że „entry” znaczy tylko wpis fundamentu, nie jest prawdziwe dla zapisu cyklu. Poprawić w tym żądaniu, zrobić zadanie, czy przepuścić? (Ustalenia poza zakresem zadania, 1)

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, napisz która.

3. Pierwsze zdanie decyzji o zatwierdzeniu gotowości brzmi teraz „The readiness approval is blocked by a missing section, …” zamiast „The readiness gate blocks a definition with a missing section, …”. Wybrałem to, bo zatwierdzenie jest Twoim aktem i niczego nie może blokować; wstrzymuje je skrypt sprawdzający definicję. Recenzent uznał znaczenie za zachowane. Innym wariantem było „the readiness approval blocks a definition”, które mówiłoby, że zatwierdzenie robi coś, czego nie robi.
4. W jednym odrzuconym wariancie wcześniejszej decyzji „intermediate human gates” zmieniono na „intermediate human approvals”, bo „gate” w słowniku znaczy teraz tylko polecenie testów. Zdanie nadal odrzuca ten sam wariant.
5. W dwóch skryptach sprawdzających i ich testach nazwy z „gate” w znaczeniu zatwierdzenia zmieniono razem ze słowem (na przykład stałą nagłówka i funkcję, która go sprawdza), a plik kroku projektu opisującego zatwierdzenie nazwano od niego. Innym wyborem było zostawienie nazw w kodzie, ale wtedy stare słowo stałoby w znaczeniu, które się zmieniło. Nic poza krokami projektu tych nazw nie importuje.
6. Dwa nowe testy, które utrzymują odrzucenie starego nagłówka i statusu, powołują się na niezmiennik o formie definicji, a nie na ten o sprawdzeniu gotowości, który wskazałem w poleceniu poprawki, bo jego zdanie obejmuje nieoczekiwaną sekcję i błędny status.
7. Zmieniono cztery istniejące testy skryptu audytu, bo komunikaty skryptu mówią teraz „key” tam, gdzie mówiły „entry”: trzy oczekiwane fragmenty komunikatu i cztery nazwy testów; sprawdzenia są tak mocne jak wcześniej, a skrypt przyjmuje i odrzuca dokładnie to, co dotąd.
8. Wpisy fundamentu zmienione przez cykl, których nie widziałeś przy zadaniu: te same zamiany słów w 21 innych decyzjach i w wycofanym wierszu jednej kolejnej (decyzje, które nazywały zatwierdzenie „gate”, klucz pliku lokalizacji „entry” albo zadanie w backlogu „backlog entry”); żadna decyzja nie zmieniła znaczenia. Każdą wymieniono w *Foundation entries*.

Zmienione testy niezmienników, prostymi słowami: niezmiennik o sprawdzeniu gotowości ma teraz identyfikator `project-readiness-check` (był `project-readiness-gate`), tak jak wybrałeś; jego testy zmieniły się tylko w linii, która go cytuje, i w słowach danych wejściowych, bez osłabienia asercji. Cztery testy sprawdzeń planu i technologii zmieniły tylko dane wejściowe. Dwa testy są nowe (wyżej). Sprawdzenie fundamentu nie wskazało żadnego niezmiennika z poprawionym zdaniem i żaden test decyzji się nie zmienił.

## Koszt

Około 1 godziny 6 minut aktywnych etapów, około 71 mln tokenów: autor na Sonnecie (zmiana, poprawka trzech drobnych uwag, krok zwrotny), trzy przeglądy na Opusie (cała zmiana, poprawka, uzgodnienie z gałęzią docelową) i orkiestrator na Sonnecie. Po pierwszym przeglądzie odbyła się jedna runda poprawki, nie blokująca. Tabela etapów jest w zatwierdzonym zapisie, podlinkowanym niżej. Żadna kopia robocza agenta ani katalog wcześniejszego zadania na nic nie czeka, poza jednym katalogiem wcześniejszego zadania, którego skrypt czyszczący nie umiał uznać za zakończony (niżej); nic w tym żądaniu na niego nie czeka.

## Jak scalić

Scal commitem scalającym, nie squashem ani rebase, żeby link do zapisu cyklu, który wskazuje commit, pozostał osiągalny. Nic w tym żądaniu nie czeka na przegląd fundamentu.

</details>

## Technical changes

- `79c9bfb9` — the change, by the one author: the projected meaning of "gate" renamed in the English text of tracked files (`readiness gate` → `readiness approval`, `gate record` → `approval record`, `ready for gate` → `awaiting approval`, `project-readiness-gate` → `project-readiness-check`, the file `project-level/skill/readiness_gate.md` → `project-level/skill/readiness_approval.md`, bare "the gate" in that meaning by hand); `project-level/readiness_check.py` and `project-level/plan_check.py` read the section `## Approval record` and the status `awaiting approval` (names `APPROVAL_RECORD`, `APPROVAL_LINES`, `check_approval_record`, `APPROVAL_FINGERPRINT`), with their tests and `project-level/test_plan_state*.py`; `project-level/definition_template.md` carries the new heading and status; the glossary entry `gate` names the approval in *Not*; `entry` → `key` for the locations file in `AGENTS.md`, `project-level/backlog_place.md`, `process-audit/SKILL.md`, `process-audit/audit_count.py` (messages and docstrings; the code names `entry_path`, `REGISTER_ENTRY` and the like stay) and its tests, decisions WAY-27, WAY-107, WAY-320, WAY-330, WAY-344 and the row of WAY-342; "backlog entry" → "the task's line in the backlog" in WAY-140, `task-cycle/record_template.md`, `task-cycle/skill/SKILL.md`, `project-level/test_plan_state.py`, `foundation-review/with_the_human.md`; `read off` reworded in `project-level/technology/research.md` and the rationale of WAY-280; the new glossary entry `projected entry`; the six skill entry points of `define-project`, `plan-project` and `settle-technology` regenerated.
- `8bb897b6`, `cef14df7` — the fix of the three Minor findings of the review of the whole change: "every repository key that holds a key `repository`" in `process-audit/SKILL.md` and the docstring of `process-audit/audit_count.py`; the lines the rename lengthened over the files' own wrapping rewrapped word for word (21 Markdown files and six Python files); two tests added to `project-level/test_readiness_check.py`, `test_the_heading_of_the_record_before_the_rename_is_reported` and `test_the_status_value_before_the_rename_is_reported`.
- `50bc1993` — the merge of `origin/foundations` (`bec6c3d2`, the request #147 of the task `agent-test-bypass`) into the branch, with no conflict; no decision of this task is new, so none was renumbered.
- For products that pin the-way (To do 6 of the task): in each approved project definition, the heading `## Gate record` becomes `## Approval record`; in `## Backlog` of the product's main `AGENTS.md`, "the entry `tasks` under …" and the like become "the key `tasks` under …". Out of the task's scope here: the repository loop2 and its own files.

## Checks

- Final gate: the CI run on this request's last head `4d7ad796` (the commit that removes the record's copy), https://github.com/mariusznazar/the-way/actions/runs/43904193819, first attempt: `tests` (Linux) pass, 1m15s; `tests-windows` pass, 10m21s. Every check passed in the one run; none was rerun and no test failed.
- The list of failing checks before the change, taken from the merged request https://github.com/mariusznazar/the-way/pull/146, since the base `4758840f` is a merge commit with the tree of its second parent and no gate ran on it: none (both checks of its one CI run passed).
- Focused checks by the author and the reviewers (each with command and exit 0): `python -B gate/run_tests.py project-level` (281 tests), `process-audit` (276), `agent-instructions` (50, 2 expected failures of invariants marked violated), `elements/common` (270), `task-cycle` (534, 2 skipped), `gate` (36); `python -B elements/common/foundation_check.py` without `--skip-test-citations` on the finished change, after the merge: exit 0, `0 errors`, no `listed:` line; `python -B agent-instructions/skill_entry_points.py`: exit 0, entry points current; `python -B agent-instructions/agent_type_copies.py`: exit 0.
- The invariant's test seen failing once and passing after, by the author (the old heading and the old status put back in `readiness_check.py`: exit 1, then exit 0), and the two new tests each seen failing against their mutation by the reviewer of the fix (old status added to `STATUS`; old heading added to `SECTIONS`). The reviewer of the whole change also ran crafted input at the two files on the trust boundary: an approved definition with `## Gate record` is refused (exit 1; also with `--before-approval` and `--fingerprint`), `Status: ready for gate` is refused, a definition holding both headings and one with a lower-case heading are refused; `plan_check.py` reports the form; the fingerprint of an approved definition does not change.
- Own-work check (WAY-164): the author named as most likely missed a use of a moved word left in the English text of a tracked file, and searched `git ls-files` for the old phrases across line breaks, for paragraphs holding "gate" with approval words, and for "entry" near words of the locations file: the only hit was a line break that split "the gate records" (the test command, left as it is). No walk through a running product was made: the change alters the text of messages, names and sentences, and no screen.
- The full gate was not run on the cycle's own system: CI runs on this request and is the final gate (WAY-160). A start signal was not needed.
- `python -B task-cycle/review_reminder.py origin/foundations`: exit 0, 21 merges, `reminder: no`. The copy of the record: `python -B task-cycle/private_paths_check.py docs/task-cycles/readiness-approval-rename` run 1 exit 1 (11 listings: nine files, the paths of the worktree and of the author's notes and one note link), run 2 exit 0 (0 listed, after one rewriting applied to every text file); `python -B task-cycle/image_files_check.py docs/task-cycles/readiness-approval-rename` exit 0 (1 run); `python -B task-cycle/remarks_check.py` exit 0 (on the original 2 runs: run 1 exit 1 with 10 items listed and appended word for word, run 2 exit 0; on the copy 1 run, exit 0, 10 items). The description: `python -B task-cycle/request_check.py <description> --task <frozen task>` exit 0 and `python -B task-cycle/private_paths_check.py <description>` exit 0, run before the request opened and again after the record's link was added.
- One directory of an earlier task stays: `agent-test-bypass`, branch `task/agent-test-bypass`, reason: the branch has no merge git can see on `origin/foundations` (not merged, merged by squash or rebase, or its request open or closed). No working copy of an agent stays.

## Foundation entries

- `gate` (glossary term, row 1): the term means only the command that runs all the tests; *Not* names the human's approval of a project definition with the quoted word "readiness approval".
- `projected entry` (glossary term, row 2): the wording, under a project definition's "Projected foundation changes", of an entry of a product's foundation — a decision, an invariant, a glossary term, an environment fact or a change to the part map — or of a change to one, that the foundation is to hold once a task's code makes it true; `entry` is unchanged.
- `project-readiness-check` (invariant, row 4): the identifier of the invariant that was `project-readiness-gate`; its sentence and its tests are the same. Also cited in the *Verification* of WAY-118 and by the `invariant:` lines of the tests.
- WAY-320 and WAY-140 (rows 5 and 6): the locations file holds keys by name and a file that points to such a place names its key; the cycle's record of the request is written in "the task's line in the backlog"; the meanings are unchanged.
- Row 3 went to the code and the template (`awaiting approval`), so no entry was written for it.
- `the cycle's`, found by the search of the whole foundation (WAY-97), word-for-word renames with no change of meaning: WAY-27, WAY-106, WAY-107, WAY-113, WAY-114, WAY-118, WAY-121, WAY-126, WAY-134, WAY-142, WAY-145, WAY-147, WAY-227, WAY-267, WAY-270, WAY-280, WAY-313, WAY-314, WAY-330, WAY-344, WAY-374 and the withdrawn row of WAY-342; the invariant `project-plan-form` and the parts `project-level` and *External context* of the part map in the same way. The first clause of WAY-118 was reworded (item 3 above).
- No decision, invariant, fact or topical section was written new; the return step found nothing that no longer matches and committed nothing.

## Minor findings

Minor findings of the review of the fix, within the task, not fixed (WAY-161):

1. `process-audit/SKILL.md:106-108` — "the rewrap leaves a ragged paragraph: 'Offer to add the key to the file, create the file or the repository key where / they are missing, and write / only on the human's yes.' The words and the rendered Markdown are unchanged. Only the source reads unevenly: the script broke one line and did not reflow it with the next. This is cosmetic, with no effect on a reader of the rendered text."

The three Minor findings of the review of the whole change (the phrase "every key that holds a key `repository`", the lines not rewrapped, no test of the old heading and status) were fixed in `8bb897b6`.

## Findings outside the task's scope

1. Outside the task — "entry" in a third meaning, an item of a list in a cycle's record (the reviewer's words): "To do 10 says that after items 9 and 10 'entry' means only an entry of the foundation. The tracked text still uses 'entry' for an item of a record's list: `task-cycle/record_template.md:43`, `:57`, `:59`, `:63`, `:74`, `:238`, `:265-266`; `task-cycle/skill/SKILL.md:234`, `:386-387`, `:395-396`, `:754-757`, `:768`. The task names only the two meanings that the foundation review found (a key of the locations file, a task's line in the backlog), and I found no sentence that is true in one of these meanings and false in the other, which is the test of WAY-99. So this is no missed requirement of this task. Whether the record's 'entry' passes the test of WAY-99 is a question for another task, or for the next review of the foundation." (Line numbers are those of the reviewed head.)

## Course of the cycle

- **Task and sources:** an independent task: separate the two meanings of "gate", write the glossary entry `projected entry`, move the other two words of the review of the foundation of 2026-11-14 (`entry`, `read off`); its six settlements were accepted on 2026-11-15. The cycle found one claim of the task's context that does not match the files (`task-cycle/skill/foundation_step.md` holds no locations-key "entry") and one wrong address (the question of WAY-342 stands in a row of the withdrawn identifiers, not in WAY-376); both are in the process remarks of the record.
- **Process pin:** not applicable; this is the process repository itself, base `4758840f`.
- **Spec:** none: the task leaves no open design choice.
- **Route:** one author without a plan, class `same` (Sonnet), because the places are enumerated by search and each use needs a judgment of meaning; reviews on Opus. The review of the whole change read 23 of 199 selected decisions whole and named WAY-344, WAY-106, WAY-134 and WAY-147 as read in their changed passages only (WAY-34 as untouched by the change); WAY-134 was read whole by the reviewer of the reconciliation.
- **Plan:** none.
- **Choices:** 7 of the author recorded in the questions table (the file name, the Python names, the first clause of WAY-118, the `read off` places, `intermediate human approvals`, the messages and tests of the audit script, the invariant the new tests cite) and the session's instruction on reviewers' model, see the record.
- **Blocking findings left:** none.
- **Record:** https://github.com/mariusznazar/the-way/tree/3685852031fd9b1e229f91d7b0ac0166761cf8c8/docs/task-cycles/readiness-approval-rename (the commit `36858520`; the table of stages is `stages.md` in it).
