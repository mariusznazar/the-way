**State: ready** — the change is reviewed and every test passes; one item below waits for your answer, the rest only needs your merge.

## What you will see

The check for private paths and note links no longer reports a shell character class written in double square brackets, such as `[[:space:]]` or `[[:alpha:]]`, as a link to a note. These classes stand in shell commands that skill files and notes quote, and until now each one made a product's test of its tracked files fail, so a product had to retell the command in other words or mark its rule as violated.

The exception is exact. It covers the twelve class names the shell knows (`alnum`, `alpha`, `blank`, `cntrl`, `digit`, `graph`, `lower`, `print`, `punct`, `space`, `upper`, `xdigit`) in the form of `[[:space:]]`. Any other text between the colons, every real link to a note and every path on the same line are still reported. It applies in all three places where the check looks for a link: the copy of a cycle's record, the description of a request and the files a repository tracks.

The product that met the problem, loop2, still has to move its pin of the-way and lift its expected failure itself; that is outside this change.

### Underneath

One pattern in the check's script gains a lookahead for the twelve names, with tests for it and for the tracked-files check, and the decision that defines what the script takes for a note link says so.

## For you to decide

### Needed from you

none

### Fix or let through

1. The reviewer of the whole change read 7 of the 112 decisions that concern the process's cycle part in full and ran through the other 105 by title only. It named seven of those it did not open as bearing on this change: how reports and findings are graded, how an author edits a decision in place and searches the foundation, the form of a decision, and the author's own-work check. The change was judged on the other entries and the form check reports no error, so a miss is unlikely, but it is not excluded: if one of the seven said something the change breaks, you would find out in a later cycle, when its check or review reports it. Reading them now costs one more review by a fresh reviewer; merging costs nothing today. I recommend letting it through, since the change is one pattern and its decision, and the reviewer checked both against the rule they change. Have the unread decisions read in this request, make a task of it, or let it through?

### You accept by merging

Merging accepts these items; if one does not suit you, say which.

2. The exception is case-sensitive and needs the exact form: a name written with a capital letter, and a class without its closing colon, are still reported as links. The task asked for exactly the twelve names in the form of `[[:space:]]`, and a wider exception could hide a note with such a title. The price is a false report on a rare text of that shape.
3. The decision that defines the rule rests on no outside source: the twelve names come from the list you settled in the task, and no local document quotes the shell's list word for word. A source outside the repository was not fetched. The price is that a reader who asks why these twelve finds only the task's choice.

## Cost

About 20 minutes of working time. The orchestrator and the reviewer ran on Claude Sonnet 5.5, the author on Claude Haiku 5.5; 12.3 M tokens in all, of which 11.8 M were input read from cache and 0.09 M output. Review rounds: the whole change was reviewed once and passed; its one Minor finding within the task was fixed and that fix passed its review. The table of stages is in the committed record.

## How to merge

Use a merge commit, not squash or rebase: the link to the cycle's record points to a commit on this branch, and it survives only when the commits are kept.

<details>
<summary>W Twoim języku</summary>

**Stan: gotowe** — zmiana jest przejrzana i wszystkie testy przechodzą; jedna pozycja poniżej czeka na Twoją odpowiedź, reszta wymaga tylko scalenia.

**Co zobaczysz**

Kontrola ścieżek prywatnych i linków do notatek nie zgłasza już klasy znaków powłoki zapisanej w podwójnych nawiasach kwadratowych, jak `[[:space:]]` czy `[[:alpha:]]`, jako linku do notatki. Takie klasy stoją w poleceniach powłoki cytowanych w plikach skilli i notatek, a dotąd każda z nich czerwieniła produktowi test plików śledzonych, więc produkt musiał opowiadać polecenie innymi słowami albo oznaczać swój niezmiennik jako naruszony.

Wyjątek jest dokładny. Obejmuje dwanaście nazw klas, które zna powłoka (`alnum`, `alpha`, `blank`, `cntrl`, `digit`, `graph`, `lower`, `print`, `punct`, `space`, `upper`, `xdigit`), w postaci `[[:space:]]`. Każdy inny tekst między dwukropkami, każdy prawdziwy link do notatki i każda ścieżka w tym samym wierszu dalej są zgłaszane. Wyjątek działa w trzech miejscach, w których kontrola szuka linku: w kopii zapisu cyklu, w opisie requestu i w plikach śledzonych przez repozytorium.

Produkt, który napotkał problem, loop2, sam musi jeszcze przesunąć przypięcie the way i zdjąć oczekiwane niepowodzenie testu; to jest poza tą zmianą.

*Pod spodem:* jeden wzorzec w skrypcie kontroli dostaje wyjątek na dwanaście nazw, razem z testami tego wyjątku i kontroli plików śledzonych, a decyzja, która określa, co skrypt uznaje za link do notatki, mówi to samo.

**Do Twojej decyzji**

*Wymaga Twojej odpowiedzi:* nic.

*Do poprawy albo przepuszczenia:*

1. Recenzent całej zmiany przeczytał w całości 7 ze 112 decyzji dotyczących części cyklu i resztę, 105, przejrzał po samych tytułach. Siedem z tych, których nie otworzył, nazwał jako mających związek z tą zmianą: ocenianie raportów i uwag, sposób, w jaki autor poprawia decyzję w miejscu i przeszukuje fundament, forma decyzji i sprawdzenie własnej pracy autora. Zmianę oceniono na podstawie pozostałych wpisów, a sprawdzenie formy fundamentu nie zgłasza błędu, więc pomyłka jest mało prawdopodobna, ale nie jest wykluczona: gdyby któraś z tych siedmiu mówiła coś, co zmiana łamie, dowiesz się w jednym z kolejnych cykli, gdy jego kontrola albo przegląd to zgłoszą. Przeczytanie ich teraz kosztuje jeszcze jeden przegląd świeżego recenzenta; scalenie nie kosztuje dziś nic. Polecam przepuścić, bo zmiana to jeden wzorzec i jego decyzja, a recenzent sprawdził oba względem reguły, którą zmieniają. Kazać przeczytać nieotwarte decyzje w tym requeście, zrobić z tego zadanie czy przepuścić?

*Akceptujesz przez scalenie:* scalenie oznacza zgodę na te pozycje; powiedz, która Ci nie odpowiada.

2. Wyjątek rozróżnia wielkość liter i wymaga dokładnej postaci: nazwa pisana wielką literą i klasa bez zamykającego dwukropka dalej są zgłaszane jako linki. Zadanie prosiło o dokładnie dwanaście nazw w postaci `[[:space:]]`, a szerszy wyjątek mógłby ukryć notatkę o takim tytule. Ceną jest fałszywe zgłoszenie rzadkiego tekstu tej postaci.
3. Decyzja, która określa regułę, nie opiera się na żadnym źródle spoza repozytorium: dwanaście nazw pochodzi z listy, którą ustaliłeś w zadaniu, a żaden lokalny dokument nie cytuje listy powłoki słowo w słowo. Źródła spoza repozytorium nie pobierano. Ceną jest to, że czytelnik pytający, czemu akurat te dwanaście, znajdzie tylko wybór z zadania.

**Koszt**

Około 20 minut pracy. Prowadzący cykl i recenzent pracowali na Claude Sonnet 5.5, autor na Claude Haiku 5.5; razem 12,3 mln tokenów, z tego 11,8 mln to wejście czytane z pamięci podręcznej, a 0,09 mln to wyjście. Rundy przeglądu: cała zmiana przejrzana raz i przeszła; jedna drobna uwaga w zakresie zadania została poprawiona, a poprawka przeszła swój przegląd. Tabela etapów jest w zatwierdzonym zapisie.

**Jak scalić**

Commitem scalającym, nie przez squash ani rebase: link do zapisu cyklu wskazuje commit na tej gałęzi i przetrwa tylko wtedy, gdy commity zostaną zachowane.

</details>

## Technical changes

1. **The note-link pattern skips the twelve POSIX class names.** `8fa6bac`: in `task-cycle/private_paths_check.py` the pattern `NOTE_LINK` gains a negative lookahead on `POSIX_CLASS`, the alternation of the twelve names between colons and the closing `]]`; the module docstring says what is no link. The pattern list is shared, so the record copy, the request description and the tracked-files check (`task-cycle/tracked_private_paths_check.py`, which imports it) all take the exception.
2. **Tests were written first.** `8fa6bac`: `task-cycle/test_private_paths_check.py` (each of the twelve names unlisted, a class with another name listed, a real link and a path on the same line listed, a class in a shell command line unlisted, `[^[:space:]]` unlisted) and `task-cycle/test_tracked_private_paths_check.py` (a class in a Markdown file is no link). Three of them failed before the change.
3. **The decision is edited in place.** `8fa6bac`, reworded by `15c2062`: WAY-323 in `foundations/decisions.md` gains the exception in its statement, its *Verification* examples and its *Rationale*, with the two ways not chosen in *Rejected*. `15c2062` replaces a rationale clause that said the names are "not matched by a pattern" with "listed one by one, not matched by a general shape", which is what the code does.
4. **The return step changed nothing.** It compared WAY-323, WAY-328, the entries the search found, the invariant `tracked-file-private-paths` and the part map with the files, and made no commit.

## Checks

1. **The full test run passed on the base and on the final tree.** `python -B gate/run_tests.py`: on the base `e1726b7`, exit 0, 913 tests in 9 directories; on `15c2062`, the final tree, exit 0, 919 tests in 9 directories. No check failed or did not run.
2. **The author's own-work check showed the exception holds at the command level.** A scratch record directory run through `python -B task-cycle/private_paths_check.py` listed the real link and the path and not `[[:alpha:]]` (exit 1, 2 listed); the same run on a file holding only the class exited 0.
3. **The focused checks of author and reviewer exited 0.** `python -B gate/run_tests.py task-cycle` (263 tests), `python -B elements/common/foundation_check.py` (`0 errors`), `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` (275 files, 0 listed). The invariant's test was seen failing on a deliberate probe link and restored.
4. **The form check, the private-path checks and the remarks check on the record:** (filled in when the record is committed).

## Foundation entries

1. **WAY-323** (`row 1`): the script takes no `[[:space:]]`-style class for a note link when the name is one of the twelve POSIX classes, and every other `[[...]]` with a letter or digit stays listed. No invariant test, surface or *Violated* mark changed.

## Minor findings

none

## Findings outside the task's scope

1. **A class preceded by one more opening bracket is still reported as a link.** `task-cycle/private_paths_check.py:82`, reviewer's words, with the one listed text written out in words because the check for private paths would list it: "the text of three opening square brackets, a colon, `space`, a colon and two closing brackets (a bracket expression holding `[` and a class, which a shell regex can contain) is still listed as a note link: the first two brackets are followed by `[`, not by `:`, so the lookahead does not apply. The task defines the exception as exactly the two-bracket form, and the same text is listed by the old script, so this is not a regression; it is a different text from the one the task names, with no sign it occurs in the 12 hits of the source product. Mention only." Make a task of it only if it shows up in a product.

## Course of the cycle

- **Task and sources:** an independent task: the check for private paths does not report a POSIX class in double brackets as a note link; source revision `e1726b7` of `foundations`, the request https://github.com/mariusznazar/loop2/pull/76 and the record of the loop2 cycle that met the problem.
- **Process pin:** none (the-way itself).
- **Spec:** none; no open design choice, since the task settles the twelve names and the shared pattern list.
- **Route:** one author without a plan: one pattern, its tests and one decision in place.
- **Plan:** none.
- **Choices:** 2 other choices (case-sensitive exact form; `Based on` left `none`), in the questions table of the record.
- **Blocking findings left:** none.
- **Record:** (link added after the record is committed)
