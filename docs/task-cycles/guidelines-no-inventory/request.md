**State: ready** — the change is complete and reviewed; two points wait below for your yes.

## What you will see

The process gains one rule for the guidelines that every product writes for its agents: a rule in them does not list what the product's code looks like today, and does not repeat what a recorded decision or a tool's own settings file already says. What stays in a rule is what the author of the code is to do. The same rule says what the process will not do on this ground: it does not replace a sentence that describes a well-known practice with just the practice's name, and it does not take out a case that follows from the rule's purpose, because the trial on your game gave no proof for either. The rule reaches only new text. A product's existing guidelines are cleaned by that product's own task, and the skills that write guidelines get no new step for it.

The trial result is also recorded as a fact the rule rests on: three small tasks with hidden tests, five runs each, for three variants of the guidelines file (the old one, a shorter one, none), all 45 runs passed, so the trial could not tell the variants apart. Nothing about running a task cycle, writing code or testing changes for a product.

### Underneath

One new decision in the log, one new sentence in the shared template of product guidelines and one new entry in the file of environment facts; no code, no test and no script changes.

## For you to decide

1. The recorded fact names its source by the address of your private game repository: the text of the request of that earlier cycle, at a fixed commit. People without access to the repository cannot open the address, and the public repository of the process now carries the name of the private one. The cycle used the source the task named, and the form of it was its own choice. Merge with the entry as it is, or drop the entry and its link from the decision? (Choices, 1)
2. The text of one commit message on the branch also names that private repository; rewriting it would have changed the reviewed commits, so it was left. Fix it in this request, or make a task of it? (Minor findings, 1)

## Cost

About 16 minutes of working time in the orchestrator's and the agents' turns, plus about 16 minutes of the full test run, on the clock of the machine; 14.2 million tokens in all, almost all of them input read again from the cache, every stage on one model, Sonnet 5.5. One review of the whole change that found one serious problem and six small ones, one fix, one review of the fix that passed, and no review of the final step because it changed nothing. The table of stages is in the record, linked below.

## How to merge

Merge with a merge commit, not a squash: the link to the record of the cycle, by the commit that adds it, survives only when the commits are kept, and the repository's recent merges are merge commits. The record is added in one commit and removed in the next, so the target branch never holds it.

<details>
<summary>W Twoim języku</summary>

**Stan: gotowy** — zmiana jest kompletna i zrecenzowana; poniżej czekają dwa punkty na Twoje „tak”.

## Co zobaczysz

Proces dostaje jedną regułę dla wytycznych, które każdy produkt pisze dla swoich agentów: reguła w nich nie spisuje, jak dziś wygląda kod produktu, i nie powtarza tego, co mówi już zapisana decyzja albo plik ustawień narzędzia. W regule zostaje to, co ma zrobić autor kodu. Ta sama reguła mówi też, czego proces z tego powodu nie robi: nie zamienia zdania opisującego znaną praktykę na samą nazwę praktyki i nie zdejmuje przypadku, który wynika z celu reguły, bo próba na Twojej grze nie dała dowodu na żadne z tych dwóch. Reguła dotyczy tylko nowego tekstu. Istniejące wytyczne produktu czyści jego własne zadanie, a skille piszące wytyczne nie dostają nowego kroku.

Wynik próby jest też zapisany jako fakt, na którym reguła stoi: trzy małe zadania z ukrytymi testami, po pięć przebiegów dla trzech wariantów pliku wytycznych (stary, krótszy, żaden), wszystkie 45 przebiegów przeszło, więc próba nie odróżniła wariantów. W prowadzeniu cyklu zadania, pisaniu kodu i testowaniu produktu nic się nie zmienia.

### Pod spodem

Jedna nowa decyzja w dzienniku, jedno nowe zdanie we wspólnym szablonie wytycznych produktów i jeden nowy wpis w pliku faktów o środowisku; żaden kod, test ani skrypt się nie zmienia.

## Do rozstrzygnięcia

1. Zapisany fakt podaje źródło przez adres Twojego prywatnego repozytorium z grą: tekst requestu tamtego cyklu, przy ustalonym commicie. Osoby bez dostępu do repozytorium nie otworzą tego adresu, a publiczne repozytorium procesu niesie teraz nazwę prywatnego. Cykl użył źródła, które wskazało zadanie, a jego postać była już wyborem cyklu. Scalić z wpisem tak, jak jest, czy usunąć wpis i jego powiązanie z decyzją? (Choices, 1)
2. Treść jednego komunikatu commita na gałęzi też podaje nazwę tego prywatnego repozytorium; przepisanie go zmieniłoby zrecenzowane commity, więc zostało. Poprawić to w tym requeście, czy zrobić z tego zadanie? (Minor findings, 1)

## Koszt

Około 16 minut czasu pracy w turach orkiestratora i agentów, plus około 16 minut pełnego uruchomienia testów, wg zegara maszyny; łącznie 14,2 mln tokenów, prawie wszystkie to wejście czytane ponownie z pamięci podręcznej, każdy etap na jednym modelu, Sonnet 5.5. Jedna recenzja całej zmiany, która znalazła jeden poważny problem i sześć drobnych, jedna poprawka, jedna recenzja poprawki zakończona wynikiem pozytywnym i brak recenzji kroku końcowego, bo nic nie zmienił. Tabela etapów jest w zapisie cyklu, linkowanym niżej.

## Jak scalić

Scal commitem scalającym, nie squashem: link do zapisu cyklu, przez commit, który go dodaje, przetrwa tylko przy zachowaniu commitów, a ostatnie scalenia w repozytorium to commity scalające. Zapis dodaje jeden commit i usuwa następny, więc gałąź docelowa nigdy go nie trzyma.

</details>

## Technical changes

The change adds one rule about what a rule of a product's guidelines may hold, and records the trial that stopped it short of renaming practices. The three commits and the group of files each touched:

- `cd9d5af` — the decision WAY-312 in `foundations/decisions.md` (+54) and the bullet "A rule lists no state and repeats no decision or value" in the required form of `product-guidelines/template.md` (+5).
- `6df733c` — the fact `shorter-guidelines-trial` in `foundations/environment_facts.md` (+6), and WAY-312's *Based on* and *Rationale* brought to it.
- `ae5dff6` — the fix of the review of the whole change: WAY-312's second sentence now binds whatever edits a product's guidelines, a product's own task included, with a "violates" example for that task (the one blocking finding); the fact's sentence has one subject, the 45 of 45 on the model Sonnet 5.5; the *Rationale* marks the author's inferences as such; the bullet's exemption is narrowed to the `### Logging scope` list; the cost figures that disagreed with the cited source are replaced by a statement that holds under both; two long lines are reflowed. The whole change is +69 −0 in three files.

The return step compared the entries with the repository and the part map, found nothing to change and committed nothing. The base and the head both keep the part map as it was.

## Checks

- Gate: `python -B gate/run_tests.py` on `ae5dff6`, the tree of this request (the target branch did not move since the base `deded3f`): exit 0, 804 tests in 9 directories, every directory passed. The same command on the base: exit 0, 804 tests, every directory passed. No check failed, none did not run.
- Foundation check: `python -B elements/common/foundation_check.py` on `ae5dff6`: exit 0, 0 errors.
- Own-work checks: the author's first check found claims in the first *Rationale* that the cited passages do not give and they were removed in `6df733c`; the check after the fix on the changed lines found no unmarked claim beyond the fact; the return step checked both quoted passages again against the source: both found word for word.
- Form check of this description: `python -B task-cycle/request_check.py .runs/task-cycles/guidelines-no-inventory/request.md --task .runs/task-cycles/guidelines-no-inventory/task.md` — last run and number of runs: written after this commit.
- Check of private paths on this description and on the copy of the record: written after the commit that adds the record.
- Process remarks check, on the original and on the copy: written after the commit that adds the record.
- Not run: no test of the product changed, so no focused test ran; the address of the cited source was verified against the local clone of the private repository, not against GitHub.

## Foundation entries

- WAY-312 (`row 1`, with the part of `row 2` on the product's own cleaning task and the skills): the shared template holds that a rule of a product's guidelines lists no state of the code or the product and repeats neither a decision nor a configuration value; nothing that edits a product's guidelines replaces a known-practice sentence with its name or takes out a case that follows from a rule's purpose; a product's own task cleans existing guidelines and the skills of guidelines get no search step.
- The bullet "A rule lists no state and repeats no decision or value" in the shared template of product guidelines (`row 2`): a rule does not list the state of the code or the product and repeats neither a decision nor a configuration value; the list of `### Logging scope` is the product's promise and no such state.
- `shorter-guidelines-trial` (`row 3`): in the report of a trial of a shorter guidelines file in one product, all 45 runs of three tasks with hidden tests passed on the model Sonnet 5.5, five runs per task for each of three arms (the old file, a shorter one, no file).
- No invariant, glossary term or part-map entry is written or changed; no entry is marked `the cycle's`.

## Minor findings

1. Minor, of the review of the whole change (M5), not fixed: "Commit `cd9d5af`'s body names the private repository. Place: `git log deded3f..6df733c`, body of `cd9d5af`: "The environment fact of the trial on loop2 waits for its source." The handoff asked whether the name appears anywhere but the fact's *Source* line. In tracked files it does not: `git grep -i loop2 -- . ':!.runs'` hits only `foundations/environment_facts.md:208`. It does appear in this commit message, and the message is also stale now. Fixing it needs a reword, which is the orchestrator's decision." The orchestrator did not reword: it would change every reviewed commit, and the name already stands, approved, in the fact (the questions table, Q2).
2. Minor, of the review of the fix: "Line 9822 of `foundations/decisions.md` ("tokens, and in a product such a rule may not exist, ... a one-off") is 130 characters. The fix's own edit left it that way. This is polish only." (`foundations/decisions.md`, the *Rejected* paragraph of WAY-312.)
3. Minor, of the review of the fix: "Sentence 2 now says "Nothing that edits a product's guidelines ...". The WAY-173 route, where a product departs from a rule by a decision of its own log, is not mentioned. This is arguably right for this row, since the decision derives from WAY-173. A reader might still ask whether a product's decision can lift the ban." (`foundations/decisions.md`, WAY-312, second sentence.)
4. Minor, of the review of the fix: "The replacement, "a heavy one, hours of agent time and tens of millions of tokens", is a paraphrase. Against the task's own 119 million, "tens of millions" understates by a little. This blocks nothing." (`foundations/decisions.md`, WAY-312, *Rejected*.)

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** a ready independent task: record, as a decision of the process, that a product's guidelines hold no state lists and no repeats of decisions or configuration values, keep the shared template in line, and record the trial result as a fact; sources were the task document (accepted rows 1–3), the earlier trial's request and record in the private repository of the game (read only), and the foundation of the-way at `deded3f`.
- **Process pin:** not applicable; the-way itself, nothing moved.
- **Spec:** none written; no open design choice (the three rows settle their entries).
- **Route:** one author without a plan, on the same class of model as the orchestrator because the decision had to be worded against a log of nearly 10 000 lines. The author returned `blocked` once for the source of the fact; the orchestrator supplied the task's own source and resumed it. Review of the whole change: `FAIL 6df733c`; one fix; review of the fix: `PASS ae5dff6`; the return step changed nothing, so no review of it.
- **Plan:** none
- **Choices:** 2 (the form of the fact's source, and leaving the commit message as it is), in the questions table of the record, see Record.
- **Blocking findings left:** none
- **Record:** pending the commit that adds it.
