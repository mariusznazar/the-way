# Report: the agent of the plan's foundation entries (F1–F10), task `decision-log-reading-index`

- **Status:** done with concerns
- Worktree: `the task's worktree`, branch
  `task/decision-log-reading-index`, base `21ecb627f885de438e2209d7ff5c137b1e1b9d83`.

## Commits and files

| Commit | What | `foundations/decisions.md` |
|---|---|---|
| `dae85e1` | F1–F9: WAY-150, WAY-18, WAY-21, WAY-287, WAY-339 | +173 −85 |
| `104e126` | F10: the division into 28 topical sections, only order, headings and sentences | +7633 −7494 |
| `0023a28` | WAY-21's *Rationale*: the measurement's date and method (after the division) | +3 −3 |

No other file changed. **For Slice 2 and the request: the commit before the division is `dae85e1`, the
division's commit is `104e126`.** `0023a28` comes after the division and changes WAY-21's
*Rationale* only; Slice 2 compares `dae85e1` with `104e126`.

## Checks

- `python -B elements/common/foundation_check.py --skip-test-citations` at the base: `0 errors`,
  exit 0.
- The same after F1–F9 (before commit `dae85e1`): `0 errors`, exit 0.
- The same after F10 (before commit `104e126`): `0 errors`, exit 0.
- The same after the WAY-21 fix (before commit `0023a28`): `0 errors`, exit 0.
- The comparison of the entries before and after the division, by a throwaway script of my own in
  `.runs/foundation-entries/` (an entry from its `### WAY-NN` heading to the line before the next
  heading of any level, trailing blank lines dropped, keyed by identifier; the text before the first
  section and the `## Withdrawn identifiers` block compared the same way; bytes compared):
  - on the working tree before the commit: `entries before 198 after 198`, `sections before 0 after
    28`, `problems 0`, exit 0;
  - on the committed copies, `git show dae85e1:foundations/decisions.md` against
    `git show 104e126:foundations/decisions.md`: the same output, exit 0;
  - positive controls: a copy with one space doubled in WAY-150's *Rationale* gave
    `differs: WAY-150`, `problems 1`, exit 1; a copy with the heading of WAY-376 removed gave
    `problems 2` (WAY-376 only before, WAY-375 differs).
- The division script itself refused to write unless every one of the 198 entries was assigned
  exactly once and each section's numbers kept the log's order; it wrote 28 sections, 198 entries.
- No test ran: the change is prose of the foundation, and no test holds a sentence of the changed
  decisions (a search for `decision: WAY-(150|18|21|287|339)` found none).

## Own-work check

- Requirement most likely missed: the acceptance criterion and the plan's paragraph under its table —
  the entries' *Rejected* and rationale say which way earlier rejected each of WAY-150, WAY-18 and
  WAY-21 now takes in, without telling the change (WAY-07) — and with it *To do* 4's removal of the
  reading by title from the log.
- Check: a search of the log for `by title`, `title only`, `skims` and `in the order the entries
  were written`, and a reading of the three entries' *Rationale* and *Rejected*.
- Result: `by title` stands only in WAY-150's *Rejected* (the way "the rule of whole reading kept,
  with the reviewer ... running through the rest of its selection by title", from question 0's *Not
  chosen*); `in the order the entries were written` no longer stands (WAY-18 now says "in the order
  they were written" for a log without sections only). WAY-150: *Rationale* says the index is
  written on demand, holds exactly the selection and cannot go stale; *Rejected* keeps "a separate
  maintained index, kept as a file of the repository and refreshed after each change of the log".
  WAY-18: *Rationale* says why entries are ordered by topic and not by the order of writing. WAY-21:
  *Rationale* gives topics beside scope; *Rejected* now reads "topics in place of scope".

## Entries

### F1, F2, F3, F5, F6 — WAY-150 (one change, `dae85e1`)

Paragraph 1 (main question): selection, with the decisions whose sentence an altered test holds by
a line `decision:` added (F5); the agent that selects reads the index of the decisions it selects
and opens whole only those F1 names; the reviewer of the whole change reads the index of its whole
selection and states how many decisions it read whole (F1). Paragraph 2: the index (F2). Paragraph
3: a log with topical sections (F3) and without them (F6). Paragraph 4: who selects, the sentence of
paragraph 1 at the base moved unchanged into a paragraph of its own (see Choices). *Verification*
examples, *Rationale* and *Rejected* rewritten; *Scope*, *Based on*, *Relations* unchanged.

- F1 — `row 1`.
  - EN: Whoever selects reads the index of its selection of decisions and opens whole only those the
    work changes, goes against or answers otherwise (with their rejected options), those the task or
    the source names, those a test the work alters holds, and those whose binding sentences leave
    the work open; the reviewer of the whole change reads the index of its whole selection and
    reports how many decisions it read whole.
  - PL: Kto wybiera lekturę, czyta spis swojego wyboru decyzji i w całości otwiera tylko te, które
    praca zmienia, którym przeczy albo na których pytanie daje inną odpowiedź (z wariantami
    odrzuconymi), te nazwane w zadaniu lub w źródle pracy, te pilnowane przez zmieniany test oraz
    te, których zdania wiążące zostawiają otwarte, co praca ma zrobić; recenzent całej zmiany czyta
    spis całego wyboru i podaje, ile decyzji przeczytał w całości.
- F2 — `row 2`.
  - EN: The index is no file of the repository: a script of the-way writes it on demand into a file
    the agent names, with each selected decision's number, question, binding sentences and *Scope*.
  - PL: Spis nie jest plikiem repozytorium: skrypt the way wypisuje go na żądanie do pliku
    wskazanego przez agenta — dla każdej wybranej decyzji numer, pytanie, zdania wiążące i *Scope*.
- F3 — `row 3`.
  - EN: In a log with topical sections, whoever selects picks the sections of the work's topics and
    reads the index of their decisions, runs through the questions of the decisions outside them
    whose *Scope* names a touched part, and opens whole those that point to a bearing on the work.
  - PL: W dzienniku z sekcjami tematycznymi wybierający bierze sekcje tematów pracy i czyta spis ich
    decyzji, przegląda pytania decyzji spoza tych sekcji, których *Scope* nazywa dotkniętą część, i
    otwiera w całości te, które wskazują na związek z pracą.
- F5 — `row 5`.
  - EN: A decision whose sentence a test the work alters holds by a line `decision:` joins the
    selection and is read whole.
  - PL: Decyzja, której zdanie zmieniany test pilnuje linią `decision:`, wchodzi do wyboru i jest
    czytana w całości.
- F6 — `row 6`.
  - EN: In a log without topical sections the decisions are selected by the parts the work touches,
    and their index takes the place of reading them whole.
  - PL: W dzienniku bez sekcji tematycznych decyzje wybiera się po dotkniętych częściach produktu, a
    spis zastępuje ich lekturę w całości.
- The price sentence of WAY-150's *Rationale* — `the cycle's` (the orchestrator's addition 1).
  - EN: The price of the reading is the round of fix it can still need: a reviewer of the whole
    change may name decisions of its index as bearing on the change and leave them unopened, and
    only a round of fix with a fresh reviewer closes that gap.
  - PL: Ceną tej lektury jest runda poprawki, której może wciąż wymagać: recenzent całej zmiany może
    nazwać decyzje ze spisu jako związane ze zmianą i ich nie otworzyć, a lukę zamyka dopiero runda
    poprawki ze świeżym recenzentem.

WAY-150's *Rejected* now holds, from the rows' sources: the maintained index file (question 1's *Not
chosen*, merged with the item that stood); "the rule of whole reading kept, with the reviewer ...
by title" and "the log split into two files" (question 0's *Not chosen*); "the sections of the
work's topics alone" and "the sections ... for every agent but the reviewer of the whole change"
(question 2's *Not chosen*). Rows 5 and 6 have sources that keep no way not chosen, so they add
none. The items that stood and concern the rest of the decision stay.

### F4 — WAY-18 (`dae85e1`) — `row 4`

First paragraph keeps "with no view generated from it"; "in the order the entries were written"
leaves it. A second paragraph: a log may be divided into topical sections, each a heading with one
sentence, its entries keeping their numbers; a new entry at the end of the section of its topic, or,
where none fits, in a new section at the end of the log, which the request adding it names; a log
without sections keeps the order of writing, a new entry at its end. A second pair of examples for
where an entry stands; one example each added to the first pair (the index in a working file, not a
file of the repository). *Rationale* says the index is no view and why entries are ordered by topic.
*Rejected* unchanged (row 4's source, question 3, keeps ways not chosen only for how fine the
sections are and who accepts their list — another part of the question).

- EN: A decision log may have topical sections with the numbers unchanged; a new entry goes to the
  end of its topic's section or, where none fits, to a new section at the end of the log, which the
  request names; a log without sections keeps the order of writing; the index is no view kept beside
  the log.
- PL: Dziennik decyzji może mieć sekcje tematyczne bez zmiany numerów; nowy wpis staje na końcu
  sekcji swojego tematu, a gdy żadna nie pasuje, w nowej sekcji na końcu dziennika, którą wymienia
  opis prośby; dziennik bez sekcji zachowuje kolejność zapisania; spis nie jest widokiem
  przechowywanym obok dziennika.

### F7 — WAY-339, second paragraph (`dae85e1`) — `row 7`

The list of the measures of context use gains "for each agent of the cycle, the bytes of the decision
log and of the index of decisions that entered its context and how many times each entered it". One
example added to each side of the pair on where those measures are counted; a sentence of
*Rationale*; *Rejected* gains question 4's *Not chosen* (a one-off measure by a separate agent). The
first paragraph is unchanged: a change of the counting script starts a new series of these measures.
WAY-326 and WAY-347 stay withdrawn; nothing in the table of withdrawn identifiers changed.

- EN: The measures of context use count, for each agent of the cycle, the bytes of the decision log
  and of the index that entered its context and how many times, in the file of those measures.
- PL: Pomiary użycia kontekstu liczą dla każdego agenta cyklu, ile bajtów dziennika decyzji i spisu
  weszło do jego kontekstu i ile razy, w pliku tych pomiarów.

### F8 — WAY-287 (`dae85e1`) — `the cycle's`

The item of the incomplete reading now reads "where its reviewer did not read the index of its whole
selection or itself named a decision concerning the change as unread"; the example pair rewritten
(40 of 151 read whole and the index of the other 111 not read → an item; index of all 151 read, two
bearing decisions named unread → an item; index of all 151 read, 40 opened, none named unread → no
item); the *Rationale* sentence on the reading by title replaced.

- EN: The request puts the incomplete reading of the review of the whole change before the human
  where the reviewer did not read the index of its whole selection or named a decision bearing on the
  change as unread.
- PL: Prośba stawia przed człowiekiem niepełną lekturę przeglądu całej zmiany, gdy recenzent nie
  przeczytał spisu całego swojego wyboru albo sam nazwał decyzję związaną ze zmianą jako
  nieprzeczytaną.

### F9 — WAY-21, *Rationale* and *Rejected* only (`dae85e1`, `0023a28`) — `the cycle's`

Binding sentence and examples unchanged. *Rationale*: topics beside scope, scope as the safeguard;
and the price of scope alone (the orchestrator's addition 2): "measured on 2026-11-15 on the-way's
own log, by a search of the *Scope* lines of all its decisions, about half of them name the part of
the task cycle". My count: 96 of 198 decisions name `task-cycle` (a `- **Scope:**` line with its
indented continuation, items split at `,` and `·`). *Rejected*: "topics — cannot be derived from a
change" became "topics in place of scope — they cannot be derived from a change, and a decision of
another topic that governs a touched part would be lost without a trace".

- EN: A decision's scope stays the safeguard that finds, from the touched files, the governing
  decisions outside the work's topical sections; topics narrow the reading beside it, never in its
  place.
- PL: *Scope* decyzji zostaje zabezpieczeniem, które z dotkniętych plików znajduje decyzje
  rządzące spoza sekcji tematów pracy; tematy zawężają lekturę obok niego, nigdy zamiast niego.
- The sentence of the price of scope alone — `the cycle's` (the orchestrator's addition 2).
  - EN: Selecting by scope alone takes in about half of the-way's log for a change to the task
    cycle, as measured by a search of the log's scope lines.
  - PL: Wybór po samym *Scope* obejmuje przy zmianie cyklu zadania mniej więcej połowę dziennika the
    way, jak pokazało przeszukanie linii *Scope*.

### F10 — the division of the log (`104e126`) — `the cycle's`

28 sections; numbers and text of every entry unchanged; the log's opening paragraph unchanged; the
list of withdrawn identifiers last and unchanged. Each section is `## <heading>`, a blank line, its
one sentence. Each entry was assigned by its heading and *Scope* lines; for WAY-10, 11, 24, 28, 63,
107, 113, 120, 126, 139, 140, 145, 270, 319 and 355 I also read the binding sentences.

- EN: The-way's decision log is divided into 28 topical sections, each with a heading and one
  sentence of what it covers, every entry keeping its number and its text.
- PL: Dziennik decyzji the way dzieli się na 28 sekcji tematycznych, każda z nagłówkiem i jednym
  zdaniem o tym, co obejmuje; każdy wpis zachowuje numer i treść.

| # | Heading | Sentence | Entries | Numbers |
|---|---|---|---|---|
| 1 | The-way and how a product takes it | What the-way is for and for whom, what its repository holds and points to, and how a product takes up its process, its version and its backlog. | 9 | 09, 27, 28, 34, 100, 101, 102, 103, 107 |
| 2 | The foundation and its entries | What a product's foundation is made of and what state it describes, and the rules every entry shares: no version, references by identifier, mandatory links and the values of fields. | 7 | 01, 02, 04, 07, 17, 54, 71 |
| 3 | Decision entries and the decision log | How a decision is written, numbered, scoped, checked and kept in the log, and what is a decision rather than an invariant, a rule of a plan or a rule of a skill. | 10 | 05, 12, 18, 19, 21, 22, 26, 29, 36, 293 |
| 4 | Accepting and applying decisions | Who accepts a decision and from when it binds, what a decision is to refinement, what settles a collision or a contradiction with one, and how one that rests on a prediction is reviewed. | 8 | 14, 24, 25, 30, 114, 313, 314, 315 |
| 5 | How skills write and read the foundation | How an agent selects the foundation it reads, searches the whole foundation for what an entry touches, asks the human and has a proposal critiqued, and what an element's skill holds. | 5 | 33, 35, 113, 120, 150 |
| 6 | Invariants | How an invariant is written, checked by a test or by review, given a result, marked violated and changed together with its test. | 8 | 03, 08, 51, 60, 61, 62, 69, 321 |
| 7 | Environment facts | Which sources and settings become environment facts, how a fact is written and named, and how it keeps up with its source. | 5 | 73, 82, 84, 85, 90 |
| 8 | Glossary | Which words take a glossary entry, what an entry holds, and how a sentence and a product's own words rely on a term. | 6 | 93, 94, 95, 97, 99, 104 |
| 9 | The part map and derived files | How files are assigned to parts, how a trust boundary is recorded, and what is generated or derived rather than written by hand and how it is compared with its generator. | 5 | 44, 48, 52, 53, 225 |
| 10 | Scripts and the gate | The language, the version of Python and the handling of a missing field of the-way's scripts, the rules the-way's own code keeps, and the one command that runs every test, with how a cycle runs it. | 8 | 16, 38, 55, 63, 89, 160, 328, 344 |
| 11 | Instruction files | What an instruction file that a tool loads holds, how it points to other files, when a rule enters or leaves it, how its rules are kept and judged, and how it is shared and installed. | 8 | 128, 129, 130, 131, 132, 133, 141, 258 |
| 12 | Skills and agent types in sessions | How a session reaches the-way's skills and agent types, and where the fragments and variants of a skill stand. | 5 | 127, 256, 265, 368, 370 |
| 13 | Project definition | What a project writes before tasks exist, when its definition is ready for breakdown, and how its projected entries and open questions move on. | 4 | 106, 118, 126, 145 |
| 14 | Technology choices | Where and by whom a technology choice is settled, how its options are found, tested and shown to a human, and what a reserved choice does to a task. | 9 | 121, 122, 123, 137, 138, 267, 268, 269, 270 |
| 15 | The running product | A product's deployment skill, an agent's way to the running product, and how a product shows its failures and what its logs hold. | 7 | 139, 165, 166, 273, 274, 276, 319 |
| 16 | Project plan | What the breakdown of a project writes, how the plan's tasks are named, ordered and run side by side, how the plan is checked, and how a task's state in it is proven. | 7 | 142, 143, 144, 146, 147, 153, 230 |
| 17 | Task refinement and readiness | When a task is ready for its cycle, split or the fix of a defect, how its refinement is exchanged and carries what it settles, and how it places the human's actions outside the repository. | 8 | 124, 134, 140, 154, 155, 355, 372, 374 |
| 18 | The course of a task cycle | The weight of a task's process, the methods of the cycle, when it writes a spec or a plan, on which models it runs, how its stages pass their work, and how a task ends. | 7 | 11, 13, 125, 135, 136, 148, 229 |
| 19 | The work of a cycle's agents | What an agent of the cycle checks of its own work and reports, how it waits for a long command, and where its working copies and working directories go. | 8 | 164, 255, 260, 261, 365, 373, 375, 376 |
| 20 | Review of a change | Who reviews a change, which findings are fixed or block, and how a reviewer grades a finding on the foundation, the glossary or the structure of code. | 7 | 10, 161, 162, 263, 297, 363, 364 |
| 21 | The request and the human | Where the human meets a cycle's work, what a request's description puts before the human and in what language, the screenshots it shows, and the process remarks of the cycle. | 8 | 227, 287, 288, 289, 294, 295, 300, 316 |
| 22 | Private paths and notes | Where a user keeps the places outside every repository that the-way's files name, and how a cycle and a product keep private paths and notes out of what they publish. | 4 | 308, 309, 320, 324 |
| 23 | Process audit | How the cost and the measures of cycles are counted and compared across versions of the process, and where the audit gets the cost of a problem. | 4 | 330, 337, 339, 350 |
| 24 | Product guidelines and their rules | Where a product's guidelines stand, what a rule of them holds and does not, whether the-way's templates bind a product, and how instruction files and the agents of a cycle reach them. | 6 | 167, 168, 173, 212, 213, 312 |
| 25 | Writing and approving guidelines | How guidelines are written, refreshed, extended and approved, what a task that needs missing guidelines gets, and how an audit of the skills of guidelines weighs its findings and chooses its causes. | 8 | 172, 174, 215, 216, 247, 251, 280, 284 |
| 26 | Coding guidelines | A product's exemplar, its standing checks, its linters and formatters, the audit of its dependencies, and the rule of the size of functions and files. | 9 | 198, 199, 202, 203, 204, 205, 206, 360, 361 |
| 27 | Rules of a product's tests | Where the rules of a product's tests stand, where a test takes its input and expected value, what an assertion and a change of a test may do, and how tests keep trust boundaries, take in AI and leave things untested. | 8 | 228, 231, 232, 233, 234, 235, 236, 237 |
| 28 | Test levels, flaky tests and mutation | The levels of a product's tests with their recipes and exemplars, when testing guidelines come into being, what a bug caught late gets, how a flaky test is treated and how a mutation tool checks the tests. | 10 | 238, 239, 240, 241, 242, 243, 244, 252, 253, 254 |

Total: 198 entries in 28 sections, 4–10 each (all numbers written with `WAY-` in the log).

## Choices, with the way rejected and the cost if wrong

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| WAY-150's sentence on who selects (paragraph 1 at the base) moved unchanged into a paragraph of its own, as the part of the question "who selects in the task cycle", so the main paragraph keeps three sentences (WAY-05) | four sentences in the first paragraph; or the sentence merged into another by a semicolon | a reviewer may hold that "who selects" is the main question, not a part of another; the wording is unchanged, so only the layout moves |
| F3 and F6 in one paragraph of WAY-150, F2 in another, F5 inside the main paragraph's selection and reading | a paragraph for each row | none beyond readability |
| In a sectioned log the sections' decisions "take the place of those found by *Scope*" in the selection whose index is read; the named decisions (*Decisions in play*, source, `decision:` lines) stay added | the decisions found by *Scope* kept in the index beside the sections — that is question 2's rejected way for the reviewer | Slice 1's `--section` with `--part` follows this already (headings alone for the decisions outside) |
| Three items dropped from WAY-150's *Rejected* that weighed ways against the screening by title, which the decision no longer holds ("a separate task for the screening after a measure", "a narrower selection for the reviewer ... with no measure", "no screening at all"); question 2's "the sections of the work's topics alone" stands in place of the second | keeping them — they reject alternatives of a practice the entry no longer has, and would read as live options | an option once weighed leaves the entry; git keeps it |
| WAY-18's "with no view generated from it" kept word for word; *Rationale* says the index is no such view | rewording it to "no view kept beside it" | a reviewer may read the on-demand index as a "view generated"; the *Rationale* and the new complying example answer it |
| WAY-18's new paragraph says a log *may* be divided, and a log without sections keeps the order of writing | "the log has topical sections" for every product — the game's log is not divided until its own task (*To do* 7, F6) | none |
| WAY-18's *Rejected* left unchanged | adding question 3's ways not chosen — they answer how fine the sections are and who accepts the list, another part of the question (WAY-134's `unknown` case does not arise, since *Rejected* already holds weighed ways) | the request names the acceptance criterion's reversal from the *Rationale* |
| No glossary entry for "index" or "topical section" | an entry through `record-glossary-term` — WAY-150's second paragraph defines the index in place, and both words keep their ordinary meaning | a reader might take "index" for a maintained file; the binding sentence says it is none |
| WAY-287's examples count unread decisions of the index ("named two decisions bearing on the change as unread") as an item, as F8 gives | — | none |
| 28 sections; scripts and the gate share one section (8 entries) | 30 sections, with "The-way's own scripts" (4) and "The gate" (4) apart, and "Failures and logs" (3) apart from "The running product" | the human may ask for another division at the merge; Slice 2's script makes a second one cheap to confirm |
| WAY-24 (review of a decision resting on a prediction) in "Accepting and applying decisions"; WAY-270 (the technology step asking how a human learns of a failure) in "Technology choices"; WAY-140 and WAY-355 in "Task refinement and readiness"; WAY-63 in "Scripts and the gate"; WAY-10 in "Review of a change"; WAY-320 in "Private paths and notes" | the sections their *Scope* alone suggested | an agent picking sections may miss one; the run through the questions of the decisions outside the sections whose *Scope* names a touched part (F3) is the safeguard |
| The measurement in WAY-21's *Rationale* written with its date and method (2026-11-15, a search of the *Scope* lines of all the log's decisions) and as a share, "about half", not as a count of entries | the raw count "96 of 198" — WAY-05 forbids a count of the foundation's entries in prose save as a measurement with its conditions | see Concerns 1 |

## Reaches beyond the dispatch

- The search of the whole foundation (WAY-33, step 2 of `elements/common/way_of_working.md`): a
  search of `foundations/` for `WAY-150`, `WAY-18`, `WAY-21`, `WAY-287`, `WAY-339` and for `by title`,
  `title only`, `titles`, `topical`, `topic`, `index`, `order the entries`, `at its end`, `end of the
  log`, `skims`; read whole the entries found that name a changed decision: WAY-148, WAY-168, WAY-213,
  WAY-289, WAY-293, WAY-316 — none needs a change (WAY-168 and WAY-293 stand on "one log", which
  stays; WAY-289's fresh reviewer for an incomplete reading stays true). Also WAY-225 (derived files,
  for whether the index is one; it is not in the foundation). WAY-19's *Rejected* "numbering by
  topic" and WAY-18's "a field for an entry's topic" stay true: numbers do not move and a section is
  no field.
- `foundations/glossary.md` headings and entries 1–60, for whether "index" needs an entry.
- `foundations/invariants.md` whole (377 lines): no invariant derives from WAY-150, 18, 21, 287 or
  339, so step 4.4 of `record-decision` has no invariant to bring into line.
- `elements/decisions/examples.md` (names WAY-03, read); `elements/decisions/skill/read.md`,
  `decide_entry.md`; `elements/common/way_of_working.md` and `elements/common/rules.md` whole, as
  `record-decision` step 1 gives.
- `elements/common/foundation_check.py:236-265` and a search of it for `binding` and `sentence`, to
  confirm that it closes an entry at a heading of any level and does not count sentences.
- For F10's assignment, the binding sentences of WAY-10, 11, 24, 28, 63, 107, 113, 120, 126, 139,
  140, 145, 270, 319, 355.
- `the user's private rule file on git` and `scripts.md` (the user's rules before a
  commit and a script).

## Working copies

`.runs/foundation-entries/` in the worktree held: `scope_count.py` (the count of *Scope* items),
`headings.py` and `headings.txt` (every entry's heading and *Scope*), `binding.py` and
`binding.txt`, `divide.py` (the division), `compare.py` (the comparison), `before.md`, `after.md`,
`mutated.md`, `dropped.md`. All removed before return (`Test-Path` gave `False`). Nothing kept in
`reports/`; the comparison's output stands above.

## Unread material

- The `- **Scope:**` lines and headings of every entry were read, as the handoff gives; the entries
  themselves were read whole only where named above, not all 198.
- `elements/decisions/skill/projected.md` and `elements/common/projected_mode.md` not read: no
  projected mode here.
- Otherwise `none`.

## Searches not found or unclear

- "The invariants whose *Part* names `decisions` or `every` and cite the log" (handoff): which of them
  "cite the log" was unclear; I read the whole invariants file instead.
- The handoff and the plan say F8 and F9 come from no row; I marked them `the cycle's`, as the
  foundation step gives for an entry no row carries whole.
- Otherwise `none`.

## Concerns

1. WAY-21's *Rationale* now holds a measurement of the-way's own log ("about half of them name the
   part of the task cycle"), added at the orchestrator's request. WAY-05 lets a measurement stand in
   prose "with what was measured and under which conditions, never as a general bound", and forbids a
   count of the foundation's entries; I wrote it with its date and method and as a share. A reviewer
   may still read it as a count of entries, and it will age as the log grows. The way out, if the
   review holds it so: drop the measured share and keep "scope alone selects widely, since a part is
   governed by many decisions".
2. Between `dae85e1` and Slice 3 the template's "Where entries go" still says "the log has no topical
   sections" while WAY-18 allows them and the log is divided; the plan gives that edit to Slice 3.
   The same holds for "Reading the foundation" against WAY-150 (Slice 3) and the reviewer's
   instruction against WAY-287 (Slice 4).
3. The log's opening paragraph is unchanged and does not mention the sections; the plan allowed an
   edit "where it has to", and nothing required it.

## Fix 1

- **Status:** done
- **Commit:** `dbdfdad` on top of `3cec41a`; `foundations/decisions.md` only, +30 −27. Entries
  changed: WAY-150, WAY-18, WAY-21 (rewrap only), WAY-287 (rewrap only); no other entry's lines.
- **The finding:** WAY-150's first paragraph said whoever selects "opens whole only those the work
  changes …, and it reads every other selected entry whole", which, read at face value, brings back
  the whole reading of every selected decision.
- **What changed (meaning of F1 unchanged, wording only):**
  - WAY-150, paragraph 1, second sentence now reads: "Of the decisions it selects, whoever selects
    reads the index and opens whole only the decisions the work changes, goes against or proposes
    another answer to — that one with its rejected options — those the task or the work's source
    names, those whose sentence a test the work alters holds by a line `decision:` and those whose
    binding sentences leave open what the work has to do; each selected entry that is no decision —
    an invariant, an entry of the map of a touched part, or an entry other than a decision that these
    link to — it reads whole, and it reads more entries where relevance is uncertain and a whole file
    only where it is short; the reviewer of the whole change reads the index of its whole selection
    and states in its report how many decisions it read whole." Rewrapped to the file's width.
  - The same ambiguity elsewhere: WAY-150's third paragraph said, for a log without sections, "their
    index takes the place of reading them whole", which can be read as opening none; it now ends
    "takes the place of reading each of them whole, the decisions the first paragraph names being
    opened whole as it gives". WAY-18's "says what binds today with no view generated from it" could
    be read against WAY-150's index written on demand; it now reads "itself says what binds today,
    with no view generated from it kept in its place; the index of a selection of decisions that an
    agent writes on demand (WAY-150) is no such view" (still three sentences in that paragraph).
    WAY-21, WAY-287 and WAY-339: no such ambiguity found in the sentences I wrote or changed.
  - Long lines: my earlier edits had joined lines past the file's width in WAY-18, WAY-21's
    *Rationale*, WAY-150's *Rejected* and WAY-287's example; each rewrapped, words unchanged. Lines
    over 100 characters that stood at the base `21ecb62` were left as they were.
- **Verification examples:** WAY-150's pair already gives, for a log without sections, an index read
  and the named decisions opened whole, and the invariants and linked entries read whole; WAY-18's
  pair already gives the index in a working file as complying and an index kept as a file of the
  repository as violating. Both still hold the reworded sentences as WAY-12 gives; no example
  changed. No test holds a sentence of these decisions (a search for
  `decision: WAY-(150|18|21|287|339)` found none).
- **Checks:** `python -B elements/common/foundation_check.py --skip-test-citations`: `0 errors`,
  exit 0. A script run from the worktree listed, for WAY-18, 21, 150, 287 and 339, every line over
  100 characters that the base `21ecb62` does not hold: none after the fix. A comparison of every
  entry of `HEAD` (`3cec41a`) and the working tree before the commit listed exactly WAY-150, WAY-18,
  WAY-21 and WAY-287 as changed.
- **Own-work check:** the requirement most likely missed was "touch no lines of any other entry";
  the per-entry comparison above showed only the four entries.
- **Working copies:** none; the checks ran as one-line scripts on stdin. A redirect to `/tmp/x`
  wrote nothing, since `/tmp/x` is a directory there, and was not mine to remove.
- **Concerns:** WAY-18's first paragraph changed in wording past what the fix named, to remove the
  same kind of face-value conflict; its meaning is unchanged, and the human accepts it with the rest
  at the merge.
- **Unread material:** `none` beyond what stands in the sections above.
- **Searches not found or unclear:** `none`.
