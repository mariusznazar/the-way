**State: ready** — one item in *Fix or let through* waits for your answer; the rest you accept by merging.

## What you will see

When you install or update the-way in a product on a computer where Git writes files with Windows line endings (CRLF), the installer's preview no longer marks every unchanged skill and agent file as "to be replaced". A file whose text is the same as the new one, and differs only in line endings, now shows `KEEP`, with no difference printed under it, and the installer does not rewrite it. When nothing else changes and the version of the-way does not move, the installer answers "Already installed; no changes" instead of asking you to confirm a write. A file whose text really changes is still shown as `REPLACE` with only its real change under it, and is written with the installer's own (LF) line endings, as before. The installer's README says this in one sentence and lists the new cases among the ones its tests check.

### Underneath

The installer decided "keep or replace" by comparing the raw bytes of the file with the new text, so any file written with CRLF counted as different; it now treats a CRLF line ending as the same as an LF one before comparing, the way it already did for the shared instruction file. Nothing else in the installer changed.

## For you to decide

### Needed from you

none

### Fix or let through

1. The one Minor finding this request leaves is cosmetic. In the installer's README, the table row that describes the agent definitions was broken over two lines by the fix for the review's remarks, so on GitHub the table shows that row cut after "as git stores them," and the rest of the sentence as a separate row. Nothing is lost or false, and the text reads on, but whoever reads the table on GitHub sees it broken until someone joins the two lines. Fixing it in this request costs one more round (a one-line fix and a review of it, about ten minutes and the tokens of one short review); undoing it costs nothing. Making a task of it leaves the broken row until that task is done; undoing it costs nothing. Letting it through leaves it, and undoing it later costs the same one-line fix. I recommend letting it through, since a reader still gets the whole sentence and the round costs more than the blemish. Its weak point: the README is what a person reads first when installing, and a visibly broken table costs trust more than its size suggests. Fix it in this request, make a task of it, or let it through? (Minor findings, 1)

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. The installer treats only the two-character CRLF as a line ending that may be ignored. A lone carriage return, or a file that lacks its last line ending, counts as a real difference and the file is replaced (and so loses a stray carriage return). A file whose text is the same but whose line endings are mixed (some CRLF, some LF) is kept as it is. The other way, treating a lone carriage return like a line ending too, would also keep files that really differ; I did not take it for that reason.
3. No new rule was written in the foundation: the tests that came with the change hold the rule, and the author's question whether to add an invariant for it was answered no, since an invariant would only repeat the tests and would need a note about Git's setting that nothing else uses yet. If you want it as an invariant, say so, and it becomes a task.

## Cost

The cycle took about 42 minutes of working time, 25 of them waiting for tools, and 22.3 million tokens in all: 7.5 million on the author's model (haiku), 7.4 million on the orchestrator's (sonnet) and 7.4 million on the reviewers' (opus; the strongest model allowed in this session). It had one review of the whole change, one fix round for its five Minor findings and one review of that fix; the return step changed nothing. The gate on the base commit took 14 minutes on this computer and passed. The table of stages is in the committed record: `docs/task-cycles/installer-preview-ignores-line-endings/stages.md` at commit `<RECORD_SHA>`.

## How to merge

Merge with a merge commit that keeps the commits, since the link to the record survives only then. Nothing in this request waits for a review of the foundation.

<details>
<summary>W Twoim języku</summary>

**Stan: gotowy** — jedna pozycja w „Do poprawy albo przepuszczenia” czeka na Twoją odpowiedź; resztę akceptujesz przez scalenie.

## Co zobaczysz

Gdy instalujesz albo aktualizujesz the way w produkcie na komputerze, na którym Git zapisuje pliki z końcówkami linii Windows (CRLF), podgląd instalatora nie oznacza już każdego niezmienionego pliku skilla i agenta jako „do podmiany”. Plik, którego treść jest taka sama jak nowa i różni się tylko końcówkami linii, dostaje teraz `KEEP`, bez różnicy wypisanej pod spodem, i instalator go nie przepisuje. Gdy nic więcej się nie zmienia, a wersja the way się nie przesuwa, instalator odpowiada „Already installed; no changes” zamiast prosić o zgodę na zapis. Plik z prawdziwą zmianą treści dalej dostaje `REPLACE` z samą prawdziwą zmianą pod spodem i jest zapisywany z własnymi (LF) końcówkami instalatora, jak dotąd. README instalatora mówi o tym jednym zdaniem i dopisuje nowe przypadki do listy tych, które sprawdzają jego testy.

### Pod spodem

Instalator uznawał „zostaw albo podmień” po porównaniu surowych bajtów pliku z nową treścią, więc każdy plik zapisany z CRLF liczył się jako inny; teraz przed porównaniem traktuje końcówkę CRLF tak samo jak LF, jak już robił to dla wspólnego pliku instrukcji.

## Do rozstrzygnięcia

### Potrzebne od Ciebie

brak

### Do poprawy albo przepuszczenia

1. Jedyna uwaga drobna, którą ten request zostawia, jest kosmetyczna. W README instalatora wiersz tabeli opisujący definicje agentów został poprawką po uwagach z przeglądu rozbity na dwie linie, więc na GitHubie tabela pokazuje ten wiersz urwany po „as git stores them,”, a resztę zdania jako osobny wiersz. Nic nie ginie ani nie jest nieprawdziwe i tekst da się czytać dalej, ale kto czyta tabelę na GitHubie, zobaczy ją rozbitą, dopóki ktoś nie złączy tych dwóch linii. Poprawa w tym requeście kosztuje jeszcze jedną rundę (poprawka jednej linii i jej przegląd, około dziesięciu minut i tokeny jednego krótkiego przeglądu); cofnięcie nic nie kosztuje. Zrobienie z tego zadania zostawia rozbity wiersz do czasu tego zadania; cofnięcie nic nie kosztuje. Przepuszczenie zostawia go tak, jak jest, a późniejsze cofnięcie kosztuje tę samą poprawkę jednej linii. Rekomenduję przepuścić, bo czytelnik i tak dostaje całe zdanie, a runda kosztuje więcej niż ta skaza. Słaby punkt: README to pierwsze, co czyta osoba instalująca, a widocznie rozbita tabela kosztuje więcej zaufania, niż wynika z jej rozmiaru. Poprawić w tym requeście, zrobić z tego zadanie, czy przepuścić? (Drobne uwagi, 1)

### Akceptujesz przez scalenie

Scalenie akceptuje te pozycje; jeśli któraś Ci nie odpowiada, napisz która.

2. Instalator traktuje jako końcówkę linii, którą można pominąć, tylko dwuznakowe CRLF. Samotny znak powrotu karetki albo brak ostatniej końcówki linii liczy się jako prawdziwa różnica i plik jest podmieniany (i traci zbłąkany znak powrotu karetki). Plik o tej samej treści, ale z mieszanymi końcówkami (część CRLF, część LF), zostaje bez zmian. Drugi sposób, czyli traktowanie samotnego znaku powrotu karetki też jak końcówki linii, zachowywałby także pliki, które naprawdę się różnią; z tego powodu go nie wybrałem.
3. W fundamencie nie zapisano nowej reguły: reguła siedzi w testach dołączonych do zmiany, a pytanie autora, czy dopisać do niej niezmiennik, dostało odpowiedź „nie”, bo niezmiennik tylko powtórzyłby testy i wymagałby wpisu o ustawieniu Gita, którego nic innego jeszcze nie używa. Jeśli chcesz mieć ją jako niezmiennik, napisz, a stanie się zadaniem.

## Koszt

Cykl zajął około 42 minut pracy, z czego 25 to czekanie na narzędzia, i 22,3 mln tokenów razem: 7,5 mln na modelu autora (haiku), 7,4 mln na modelu orkiestratora (sonnet) i 7,4 mln na modelach recenzentów (opus, najmocniejszy dozwolony w tej sesji). Był jeden przegląd całej zmiany, jedna runda poprawek pięciu uwag drobnych i jeden przegląd tej poprawki; krok zwrotny niczego nie zmienił. Bramka na commicie bazowym trwała 14 minut na tym komputerze i przeszła. Tabela etapów jest w zatwierdzonym rekordzie: `docs/task-cycles/installer-preview-ignores-line-endings/stages.md` w commicie `<RECORD_SHA>`.

## Jak scalić

Scal commitem scalającym, który zachowuje commity, bo link do rekordu przetrwa tylko tak. Nic w tym requeście nie czeka na przegląd fundamentu.

</details>

## Technical changes

- `b2c31cc2` — `file_action` in `installation/install.py` now compares `path.read_bytes().replace(b"\r\n", b"\n")` with the new text's bytes, so a CRLF-only difference gives `KEEP`; a lone `\r`, a missing last line ending, an empty file and a file that is not UTF-8 stay `REPLACE`; the branch for the `foundations` directory is unchanged and `run()` gains no line. Tests in `installation/test_install.py`: a files-test class `FileActionTest` (nine cases) and two git tests on the existing fixture (a CRLF copy of every entry point and agent definition is `KEEP` with no diff, is not rewritten and gets "Already installed; no changes"; a CRLF file with a real change is `REPLACE` with only the real change shown and is written with LF). One sentence in `installation/README.md` and an addition to its list of tested cases.
- `ee4cbe35` — the fix of the five Minor findings of the review of the whole change: the README sentence narrowed, the "byte for byte" row made true beside it, the tested cases listed, and comments in the tests naming the source of the expected values and saying that two cases guard the comparison alone.

## Checks

- Final gate: the CI run on the request's last head — pending, written here when it ends.
- Gate on the base commit, on this computer (CI cannot stand for it, since no request existed yet): `python -B task-cycle/gate_times.py --output … -- python -B gate/run_tests.py` in a separate checkout of `9cc26f3e`, exit 0, 1653 tests in 11 directories, every directory passed, 859 s. No check failing on the base.
- Focused: `python -B gate/run_tests.py installation` — before the code change, with the new tests: exit 1, 3 failures (the new tests, as meant); after: exit 0, 73 tests OK (author at `b2c31cc2` and `ee4cbe35`, reviewer at `b2c31cc2`). New tests against the base code, reviewer: exit 1, the same 3 failures. Reviewer of the fix: `python -B -m unittest test_install.FileActionTest`, exit 0, 9 tests; that reviewer did not rerun the 73 tests, since the fix changes README text and test comments only.
- The pinned linter (`ruff` 0.17.1, `--ignore-noqa`) on `installation`: exit 1 on two old reports in `installation/install.py` (`:83`, `:467`), on lines this change does not touch and the same on the base; exit 0 on `installation/test_install.py`. The foundation already records the invariant of the linter as violated.
- Size invariant with its mark off, base and head: same 11 functions and 2 files over a threshold on both; `run()` stays at 120 lines; the change adds 3 lines to `installation/install.py`.
- Own-work check of the author: the requirement most likely missed (apply and rerun leave a CRLF file untouched and answer "Already installed; no changes") is checked by the git test above, red before and green after.
- `python -B elements/common/foundation_check.py`, no `--skip-test-citations`: exit 0, 0 errors, no `listed:` line.
- `python -B task-cycle/review_reminder.py origin/foundations`: exit 0, 17 merges, threshold 60, `reminder: no`.
- `python -B task-cycle/remarks_check.py` on the original record: run 1 exit 1 (10 items appended), run 2 exit 0; on the copy: pending.
- `python -B task-cycle/cycle_stages.py` and `cycle_measures.py`: exit 0 each.
- Form check, check of private paths on this file, and the checks on the record's copy (private paths, images, remarks): pending, filled in when the record's link is added.
- No working copy of an agent stays. No directory of an earlier task stays.

## Foundation entries

none

## Minor findings

1. `installation/README.md:60-61` — found new by the review of the fix: "the fix broke the agent-definitions row of the "Files in the product" table across two lines. On GitHub the row stops after "as git stores them," and the rest of the sentence shows up as a separate row under the "Path" column. Nothing is lost or false, but the table looks broken. The fix is to join line 61 back onto line 60." Not fixed (a Minor finding the review of a fix finds does not block). The five Minor findings of the review of the whole change were fixed in `ee4cbe35`.

## Findings outside the task's scope

none

## Course of the cycle

- **Task and sources:** an independent task: the installer's preview marks a file `REPLACE` where only the line endings differ; the task document of 2026-11-14 and the foundation of `foundations` at `9cc26f3e`.
- **Process pin:** not applicable; this is the-way itself.
- **Spec:** none: the task leaves no open design choice.
- **Route:** one author without a plan on a cheaper model (haiku), since the change is one short function and its tests; no discarded attempt.
- **Plan:** none.
- **Choices:** 3 other choices of the cycle, in the questions table of the committed record: how a line ending is folded (item 2 above), the class of the author, and no invariant (item 3 above).
- **Blocking findings left:** none.
- **Record:** `docs/task-cycles/installer-preview-ignores-line-endings/cycle.md` at commit `<RECORD_SHA>`.
