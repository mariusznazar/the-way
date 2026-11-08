# Report of the one author — task cycle `test-artifacts`

## Status

`done with concerns` (the concerns are listed under "Concerns"; none blocks).

## Commits

Base `f218b5542ae55b72a95832adde67591365abb72a`; branch `task/test-artifacts`; worktree clean.

- `dd84fba` — Record where the screenshots of a changed screen lie and how they reach the request
  (`foundations/decisions.md` +, `foundations/invariants.md` +10, `foundations/glossary.md` 1 line).
- `d0d3ce6` — Check a record's copy for image files and carry the screenshot rules into the skills
  (new `task-cycle/image_files_check.py` 97 lines, new `task-cycle/test_image_files_check.py` 160
  lines; edits to `task-cycle/skill/SKILL.md`, `task-cycle/skill/request_template.md`,
  `task-cycle/change/ui_check.md`, `task-cycle/record_template.md`, `task-cycle/review/SKILL.md`,
  `project-level/definition_template.md`, `project-level/technology/{list,research,running_product,start,task_run}.md`).

`git diff --stat f218b55..HEAD` has the exact counts. All paths are in the worktree.

## The choice about the check script

I made a script of its own, `task-cycle/image_files_check.py`, not an extension of
`task-cycle/private_paths_check.py`. Reasons: WAY-309 binds the existing script to "lists absolute
paths and note links, holds no list, rewrites nothing"; an image file is exactly the "binary file"
case it counts and skips (exit 0), so widening it would invert one of its tests and change its
contract; the private-paths check also runs on the request description, where the image check has no
place (the description embeds images by link). Cost if wrong: one more command in the record step
of `task-cycle/skill/SKILL.md` ("The record before it is committed", new step 5), and a second
script to keep.

How it recognizes an image: **by the end of the file name only**, case-insensitive, one of `.png`
`.jpg` `.jpeg` `.gif` `.webp` `.bmp` `.tif` `.tiff` `.ico` `.svg` `.avif` `.heic`. It never opens a
file. I chose not to add signature (content) recognition because the signatures are values from
outside standards, and the invariants template then asks for environment facts with sources read
now; that cost is not worth the case it adds. **What it does not catch:** an image saved under
another extension or none; an image inside a text (a `data:` URL, base64); an image inside an
archive; and it lists a text file merely named like an image (a false positive, stated in the
docstring). It takes a directory or one file; exit 0 nothing listed, 1 listed, 2 wrong argument.

## Checks (command and exit code)

- Invariant `record-copy-image-check`, failing run (script a stub that lists nothing, test file
  written first): `python -B -m unittest discover -s task-cycle -p "test_image_files_check.py"` ->
  exit 1 (13 tests, failures on every listing test and on the argument-error test, as expected);
  `python -B gate/run_tests.py task-cycle` -> exit 1 (`FAILED (failures=34)`, all in the new file).
- Same invariant, passing run after the script: `python -B -m unittest discover -s task-cycle -p
  "test_image_files_check.py"` -> exit 0 (13 tests OK).
- `python -B gate/run_tests.py task-cycle` -> exit 0 (200 tests OK).
- `python -B gate/run_tests.py elements/common` -> exit 0 (109 tests OK).
- `python -B gate/run_tests.py project-level` -> exit 0 (271 tests OK).
- `python -B gate/run_tests.py agent-instructions` -> exit 0 (18 tests OK).
- `python -B elements/common/foundation_check.py` -> `0 errors`, exit 0 (run after the entries and
  again after the commits).
- `python -B agent-instructions/skill_entry_points.py` -> `entry points are current`, exit 0 (no
  skill description changed).
- Not run: the full gate `python -B gate/run_tests.py` (the orchestrator's, by the handoff); other
  directories with tests (`gate`, `installation`, `product-guidelines`, `instruction-files`,
  `relation-model`, `foundation-review`) because I changed nothing they test and the handoff asks for
  the directories I change only.

The test file cites `invariant: record-copy-image-check` at the three tests that check the sentence
(an image listed with exit 1, a clean copy with exit 0, every extension of the list in either case)
and at the one test that runs the command as a process. Mutations I considered: an extension missing
from the list (caught by the per-extension test, which writes its own literal list), the comparison
case-sensitive (caught), a directory named like an image listed (caught), reading content (caught by
the cp1250 file and the text named `.png`), unsorted output (caught), exit code not propagated by the
command (caught by the process test), `rglob` replaced by a one-level listing (caught by the deep
file). Not caught and by design: the list's contents beyond what the test writes out.

## Own-work check (WAY-164)

- Requirement most likely missed: "before every commit that adds a record copy, the script checks
  the copy for image files" (item 8) holding on a realistic record, not only on made-up files, and
  "everything that repeats 'three matters' is corrected" (row 4).
- Check: `python -B task-cycle/image_files_check.py <temp record with cycle.md and a real photo copied
  from the machine as reports/real.JPG>` -> listed `…/reports/real.JPG: image file`, `checked: 2
  files, 1 listed`, exit 1; the same record with the photo removed -> `checked: 1 files, 0 listed`,
  exit 0; a missing directory -> `Error: …`, exit 2. A grep of every `.md` for `three matters`, `the
  three`, `three further choices` and the lists "logs, interface, development data" found the ten
  places the handoff pointed to plus WAY-267 (`up to three further choices`), WAY-270 (`the three
  matters`), `project-level/technology/{task_run,start,list}.md`; all corrected; the remaining hit
  (`product-guidelines/coding/template.md:64`, "three standing checks") is unrelated.
- It showed the first check passes and the grep leaves no repeat of "three matters".

## Reaches beyond the handoff

- `elements/invariants/skill/{SKILL,decide_entry,draft,write}.md`, `elements/invariants/template.md`,
  `elements/decisions/skill/{SKILL,read,decide_entry}.md`, `elements/decisions/template.md`,
  `elements/glossary/skill/{SKILL,decide_entry,write,read}.md` and `elements/glossary/template.md`,
  `elements/common/way_of_working.md`: to write the entries as their skills give.
- Decisions WAY-165, WAY-267, WAY-33, WAY-134, WAY-287 and the start of WAY-122: WAY-165 because it
  defines what each matter of the way asks, so the fourth matter had to be written there; WAY-267 and
  WAY-270 (in the list) for the counts; WAY-33/134 as the handoff names.
- `task-cycle/review/SKILL.md` (changed, read whole): the reviewer has to know a screenshot file in
  the range is a finding.
- `agent-instructions/README.md`: to check whether the image check belongs to the-way's own change
  flow (it does not; no record copy is committed there).
- `the author's global rule for writing scripts` (the author's global rule before writing a
  script).

## Searches not found or unclear

- How an image file is to be recognized (extension or content) — the task and the row say nothing;
  I chose the end of the name (see above).
- Who puts a reviewer's screenshot in the place, and what a read-only reviewer does about the place:
  the task says "autor albo recenzent pokazuje"; `task-cycle/review/SKILL.md` has no step for a
  reviewer taking a screenshot, so I added only the finding "a screenshot file among the commits".
- Whether WAY-166 ("an option an agent cannot use stays in the comparison with a lack") binds the
  fourth matter: the task is silent; I took it as binding all four (see `task_run.md`).
- Whether the step that settles technology must test row 6's condition on a way (the task only says
  the-way "sets a condition"); I added the sentence to WAY-319 and one sentence to
  `project-level/technology/research.md`, marked below.
- A glossary or part-map entry that the new script needs: none (the file stays in `task-cycle/**`;
  no new word needed an entry, only the definition of an existing one changed).
- The item order of *For you to decide* for the "no place settled" case: not given by the task; I
  appended it as item 13 so as not to renumber items other files cite (items 8 and 12).

## Concerns

1. The WAY-121 binding sentence is edited in place as the task commands (three -> four matters), and
   I added one dependent change the task does not name: WAY-165 now also says what the fourth matter
   asks (where the screenshot files lie outside the product's repository, and how the description
   shows each as an image). If the human wants the matter's question put otherwise, that sentence and
   the matching one in `project-level/definition_template.md` are the two places.
2. WAY-319's second sentence (an option for the interface that cannot let two cycles check at once
   "stays in the comparison with that lack said, as WAY-166 gives") and the matching sentence in
   `project-level/technology/research.md` go beyond the literal row 6; without them the condition has
   no hook in the step that settles technology. Removing both leaves the row's meaning intact.
3. `task-cycle/skill/SKILL.md` "The record before it is committed" gained a step: the old steps 5
   and 6 are now 6 and 7. I found no reference to those numbers elsewhere (grep of
   `task-cycle`, `agent-instructions`, `installation`, `project-level`).
4. WAY-270's *Rejected* said "a fourth matter in the family of an agent's way"; with a real fourth
   matter that wording became misleading, so I changed it to "a further matter" (no meaning change).
5. No `guidelines/` exists in the-way; the script and its test were made without coding or testing
   guidelines, as task question 9 accepts.

## Foundation entries

Each entry: one sentence of its meaning in English and in Polish, with its mark.

- **WAY-316** (new decision) — `row 1` and `row 2`. EN: Screenshots that the author or reviewer shows
  the human go into the request's description as images from a place the product's foundation
  settles outside the product's repository, never into the repository's history (the record's copy
  included), and they are evidence for acceptance time, so the product may clear the place later.
  PL: Zrzuty, które autor albo recenzent pokazuje człowiekowi, trafiają do opisu PR-a jako obrazki z
  miejsca ustalonego przez fundament produktu poza jego repozytorium, nigdy do historii repozytorium
  (także w kopii zapisu cyklu), a są dowodem na czas akceptacji, więc produkt może to miejsce po
  czasie wyczyścić.
- **WAY-317** (new decision) — `row 3`. EN: When the foundation settles no place for screenshots,
  the author inspects the screenshot but the request shows none and says so, with the reason, in the
  section for the human's decisions, and the cycle does not stop; this is a different case from
  WAY-219 (no settled way to the running product). PL: Gdy fundament nie ustala miejsca na zrzuty,
  autor ogląda zrzut, ale opis PR-a go nie pokazuje i podaje człowiekowi do decyzji, że go nie ma i
  dlaczego, a cykl się nie zatrzymuje; to inny przypadek niż WAY-219 (brak ustalonej drogi do
  działającego produktu).
- **WAY-318** (new decision) — `row 5`. EN: Of the artifacts of a change's check only screenshots
  reach the request's description; motion is described in words and text traces stay in the cycle's
  reports. PL: Z artefaktów sprawdzenia do opisu PR-a trafiają tylko zrzuty ekranu; ruch opisuje
  agent słowami, a ślady tekstowe zostają w raportach zapisu cyklu.
- **WAY-319** (new decision) — `row 6` (its second sentence, the comparison hook, is `the cycle's`).
  EN: The way to the running product that a product's foundation settles for its interface lets two
  cycles in separate worktrees check at once without a shared browser, and an agent closes the
  browser it opened. PL: Droga do działającego produktu, którą ustala fundament produktu, pozwala
  dwóm cyklom w osobnych worktree sprawdzać naraz bez wspólnej przeglądarki, a agent zamyka
  przeglądarkę, którą otworzył (drugie zdanie, o porównaniu opcji, jest od cyklu).
- **WAY-121** (edited in place) — `row 4`. EN: The step that settles technology looks at four matters
  of an agent's way to the running product — logs, interface, development data and the place of the
  screenshots — and lists each that no decision settles. PL: Krok technologii patrzy na cztery
  sprawy drogi agenta do działającego produktu — logi, interfejs, dane deweloperskie i miejsce na
  zrzuty — i wypisuje każdą, której żadna decyzja nie ustala.
- **WAY-165** (edited in place) — `the cycle's`. EN: The place of the screenshots, as the fourth
  matter, asks where the screenshot files lie outside the product's repository and how the request's
  description shows each as an image. PL: Miejsce na zrzuty jako czwarta sprawa pyta, gdzie leżą
  pliki zrzutów poza repozytorium produktu i jak opis PR-a pokazuje każdy jako obrazek.
- **WAY-267** and **WAY-270** (wording only, "three" to "four" and "fourth" to "further") — `the
  cycle's`. EN: counts and a word kept consistent with the four matters. PL: liczby i słowo
  dopasowane do czterech spraw.
- **record-copy-image-check** (new invariant, `Method: test`, `Part: task-cycle`, derives from
  WAY-316) — `row 7`. EN: The script that checks a cycle record's copy lists each file below the
  directory whose name ends in an image extension of the list and exits 1 when it lists any, 0 when
  none. PL: Skrypt sprawdzający kopię zapisu cyklu wypisuje każdy plik poniżej katalogu, którego
  nazwa kończy się rozszerzeniem obrazu z listy, i kończy kodem 1, gdy cokolwiek wypisał, a 0, gdy
  nic. Row 7's other half (the copy holds no image file) is carried by WAY-316's binding sentence and
  its verification; I did not write it as a second invariant because no commit of the-way's own
  history keeps such a copy for a test to read, so its method would be `review` only.
- **Glossary entry "agent's way to the running product"** (definition widened by the place of the
  screenshots) — `the cycle's`. EN: the way is the means of checking plus the place where the check's
  screenshots lie for the human. PL: droga to środek sprawdzania razem z miejscem, gdzie leżą zrzuty
  tego sprawdzenia dla człowieka.

Rows tied to existing entries: none (the search of the foundation found no entry stating any row;
`grep -i screenshot` over the decisions found only WAY-219, WAY-286/287 and styleguide mentions,
none stating where screenshots lie). WAY-219 is untouched: its case (no settled way to the running
product) and the new one (way settled, no place) are kept apart in WAY-317 and in item 13 of the
request template.

## Other changes in the skills (for the review)

- `task-cycle/skill/SKILL.md`: new step 5 of "The record before it is committed" calls
  `python -B task-cycle/image_files_check.py docs/task-cycles/<task-slug>` on the copy (delete the
  listed files from the copy only, rewrite the mentions, run again); "the two checks" became "the
  three checks" in step 12 and step 7; the step about files not read says an image is step 5's
  business.
- `task-cycle/skill/request_template.md`: *What you will see* now says screenshots stand there as
  images from the product's place, none is shown when no place is settled, only screenshots reach
  the description; new item 13 of *For you to decide* for the "no place settled" case; *Checks* gains
  the image check's last run on the copy; "two checks on the copy" became "three".
- `task-cycle/change/ui_check.md`: where the screenshot lies, no place settled, only screenshots
  shown, no shared browser and closing the browser.
- `task-cycle/record_template.md`: evidence of a screenshot is its address, never the file.
- Names of no concrete place appear in any normative text; the rejected ways (a release attachment,
  an external file store, the human's disk) appear only as ways not chosen in WAY-316's *Rejected*,
  without product names.
