# Author's report — logging-guidelines

**Status:** `done with concerns`

The one concern is the first item of *Reaches beyond the dispatch*: three files of the author's vault
were read, as the global instructions demand, while the handoff says to read no note of the author.
The orchestrator judges whether that touches the measurement. Nothing else stands open.

## Files changed and commits

Base `ea4694e`, branch `task/logging-guidelines`, four commits, nothing pushed, tree clean.

| File | Added | Removed |
|---|---|---|
| `foundations/decisions.md` | 340 | 0 |
| `product-guidelines/coding/template.md` | 105 | 5 |
| `product-guidelines/coding/settle.md` | 52 | 3 |
| `product-guidelines/coding/recognize.md` | 9 | 3 |
| `product-guidelines/coding/task_document.md` | 9 | 2 |
| `product-guidelines/coding/SKILL.md` | 7 | 4 |
| `product-guidelines/coding/hand_back.md` | 6 | 2 |
| `task-cycle/review/SKILL.md` | 8 | 0 |
| `project-level/technology/reserved_choices.md` | 2 | 0 |

The counts were taken at `aa4a41c`; `1740c02` changes one line of `settle.md` in place.

- `8b563cd` docs: WAY-271 to WAY-279 settle the rules on failures and logs of the coding template
- `fa85fa5` docs: the review compares a change with rules without an invariant and guidelines with their templates
- `aa4a41c` docs: the coding template requires the rules on failures and logs and its skill leads a product to a decision on them
- `1740c02` docs: settle cites only the entries behind a departure from the rules on failures and logs

No skill's *description* changed, so `skill_entry_points.py --write` was not run, as the spec gives.

## What each entry means, for the request

The nine entries, with the row each carries. E9 is the spec's own and carries no row.

| Entry | Spec | Row | Sentence for the request |
|---|---|---|---|
| WAY-271 | E1 | 1 | Szablon wytycznych kodu wymaga w pliku ogólnym sześciu reguł o awariach i logach, każdej pod własnym nagłówkiem, po stałych sprawdzeniach; żadna nie jest stałym sprawdzeniem, a niezmiennik dostaje tylko wtedy, gdy tani test sprawdza całą regułę. |
| WAY-272 | E2 | 2 | Szablon mówi, czym jest awaria (także gdy zawiodła usługa z zewnątrz) i że przewidziana odmowa jest zwykłą odpowiedzią; awaria zapisuje się zawsze z oryginalnym błędem, raz, tam, gdzie kod ją obsługuje, a każdy osobno działający program ma jedno ostatnie miejsce zapisu, którego linia może nie nieść identyfikatorów. |
| WAY-273 | E3 | 3 | Szablon zakazuje chowania awarii w odpowiedzi „wszystko w porządku” albo w pustej liście, a tryb awaryjny dopuszcza tylko wtedy, gdy ustali go zadanie jako decyzję produktu, i zawsze z linią w logu; regułę przejmuje z lekcji m3l5 kursu 10xDEVS. |
| WAY-274 | E4 | 4 | Zasada zakresu logowania stoi w decyzji produktu, a lista na dziś w regule jego wytycznych, jako obietnica, nie spis kodu; agent dopisuje sam pozycję zgodną z zasadą, a wszystko, co wskazuje osobę, wymaga zgody człowieka, przy czym numer użytkownika ustala człowiek przy przyjęciu listy. |
| WAY-275 | E5 | 5 | Szablon wymaga linii dla zdarzeń biznesowych z listy i identyfikatorów pod tą samą nazwą w każdej linii przepływu sprawy (poza linią z ostatniego miejsca), a linia spoza przepływu ich nie niesie; postać linii wybiera produkt w swojej decyzji. |
| WAY-276 | E6 | 6 | Szablon zakazuje w logach sekretów, danych osobowych (wyjątkiem są tylko identyfikatory z listy) oraz całych obiektów i treści żądań; gdy oryginalny błąd cytuje takie wartości, zakaz ma pierwszeństwo nad WAY-272, a od zakazu danych osobowych produkt może odstąpić z powodem, bo to wybór szablonu, nie prawo. |
| WAY-277 | E7 | 7 | Bibliotekę, która zapisuje linie logu, wybiera człowiek na drodze skilla wytycznych, w zadaniu przyjmującym reguły, jako osobną decyzję produktu; krok technologii wchodzi tylko przy wyborze zastrzeżonym, a cykl sam żadnej nie wybiera. |
| WAY-278 | E8 | 8 | Reguły wchodzą do produktu z wytycznymi zwykłym rozszerzeniem, bez własnej drogi; odświeżenie, które zauważy ich brak, proponuje je, „tak” zmienia zadanie w rozszerzenie, a „nie” jest odstępstwem z powodem. |
| WAY-279 | E9 | — | Decyzja produktu o tych regułach jest jednym osobnym wpisem, poza decyzją przyjmującą szablon, mówi, co przyjmuje i od czego odstępuje, jaka jest postać linii, zasada zakresu i granica z WAY-274, a zadanie pierwszych wytycznych, rozszerzenia albo odświeżenia, które zauważyło brak, nie jest bez niej skończone. |

No row's settlement was found already stated, so no row is tied to an earlier entry.

## Checks run

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py .` (after the entries, and again at `1740c02`) | 0, 0 errors |
| `python -B gate/run_tests.py instruction-files` | 0, 104 tests, 5 skipped |
| `python -B gate/run_tests.py gate` | 0, 18 tests |
| `python -B gate/run_tests.py agent-instructions` | 0, 18 tests |
| `python -B gate/run_tests.py task-cycle` | 0, 42 tests |
| `python -B gate/run_tests.py project-level` | 0, 268 tests |
| `python -B -m unittest installation.test_coding_guidelines_installation` | 0, 2 tests |
| own-work script, below | 0, 0 problems |

The five directory runs each wrote to a file and their exit codes were read from that, not through a
pipe. The installation test ran through `tail`, with the exit code taken from `PIPESTATUS`.

The five directory runs and the own-work script ran on `aa4a41c`, before `1740c02`. That commit drops
one identifier from a parenthesis of `settle.md`; `foundation_check.py` ran after it, the others did
not.

Not run:

- `python -B gate/run_tests.py`, the full gate: the handoff keeps it for the orchestrator.
- The rest of `installation`, `elements/common` and `relation-model`: the change touches no code, and
  `foundation_check.py` itself is unchanged.
- A test of how an agent acts on the new text. The method says a text that instructs agents is tested
  by what an agent does with it, and it forbids dispatching a subagent, so the skill's route was only
  read through by hand. No test was written, as the spec gives: no invariant comes and nothing that
  runs changes.

## Own-work check

**Requirement most likely unmet:** that the eight rows stand in the log each whole, each *Rejected*
holding every way its row's source keeps and no other, with the template and the skill saying the same.

**Check:** a scratch script,
`C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/6e875913-ea61-4094-be96-22e216469b8d/scratchpad/own_check.py`.
It looks up each row's key phrases in its entry, each kept way in that entry's *Rejected*, the headings
of the required form in order, a bullet for each of the six, the five weak points, and private words in
the new text. Its phrases were written by hand from the task and the spec.

**What it showed:** 0 problems, exit 0. It proves presence of phrases, not meaning, and it cannot show
that a *Rejected* holds no extra way; that was read by hand against questions 1–5, 8–10 and 12.

Reading the text against To do 3 before the commits found one gap: the template's and `settle.md`'s
text on the number the product gives a user did not say that adding it later takes consent. Both now
say so; the script checks that only in WAY-274, so the two texts rest on my reading. A later reading
found a stray `WAY-273` in a citation of `settle.md`, fixed by `1740c02`.

A scan of the added lines found no bare `flow`, no `part` or `section` used for these rules, and
`the product's log` used only for the decision log, as D2 asks.

## Reaches beyond the dispatch

- **Three files of the author's vault:** `C:/Storage/The Brain/The Brain/.ai/rules/git.md`,
  `scripts.md` and `knowledge_artifacts.md`. The user's global instructions demand them before a commit,
  a script and a change of a skill. They are rules for agents on commit form, line endings and
  knowledge artifacts, and they say nothing of logs or of any product. The handoff says "read no note
  of the author"; the task's Context says "notatek ani repozytoriów żadnego produktu". I weighed this
  before reading and judged them rules for agents, not notes, which is my reading of the handoff's
  wider sentence and not a clearance, so it is reported. No text of the change draws on them, beyond
  commits made by path.
- `elements/decisions/template.md`, `examples.md`, `skill/read.md`, `skill/decide_entry.md`, WAY-03,
  `elements/common/rules.md`, `elements/common/way_of_working.md`: the skill of the element sends there.
- WAY-139, WAY-169, WAY-207, WAY-208, WAY-209, WAY-212, WAY-216: found by the search of WAY-33, read
  whole. None needs a change.
- `product-guidelines/testing/template.md:100-129`: the form of a rule's bullet, as D3 refers to it.
- `product-guidelines/coding/new_tools.md`: the route of D6.
- `reports/spec-review-2.md`: the point on the label the review left open.

## Searches not found or unclear

- The search of WAY-33, over all five files of the foundation for failure, swallow, secret, personal
  data, degraded, fallback, the logs, library, and the coding template and its skill, found no row
  already stated, no collision and no entry to correct. WAY-165, WAY-167, WAY-202, WAY-270 stay true,
  as the spec foretold. The return step found nothing to correct in the part map or in those entries.
- Unclear, settled by me: an extension of a product that already holds these rules. See the choices.
- Unclear, from the spec review and left as it stands: whether WAY-134's "ways not chosen that the row's
  source keeps" covers WAY-277, whose *Rejected* stays `unknown`, as the handoff binds.
- WAY-273's *Rejected* holds both ways of question 5, as the spec gives, though the second, each
  product defining a failure, bears on it less than on WAY-272.

## Choices, each with the way rejected and its cost if wrong

- **The label `Personal data: none — <PREFIX-NN>` stays in English** in a product that writes its
  guidelines in another language, settled in the template, in item 2 of "Departing from the rules on
  failures and logs". Reason: the template names the line and a reviewer compares the file with it, the
  reason the marker keeps. Rejected: a translated label, which fits the product's text but leaves a
  reviewer comparing two languages. Cost if wrong: one word, and no script reads it.
- **`hand_back.md` and `settle.md` ask for the decision only where `guidelines/coding.md` does not yet
  hold the rules.** D5 reads "not ready without the decision of D1 among the choices settled" for any
  extension, while D4 proposes the rules only where they are missing. Read literally, a later extension
  would have to settle again what the log holds. WAY-279 therefore reads "complete only once the
  product's log holds that entry". Rejected: asking at every extension. Cost if wrong: a reader finds
  the wording looser than D5's, with no case that goes differently.
- **WAY-277 carries a third clause, "a cycle that needs such a library chooses none alone"**, from D6
  and row 7's guess. Row 7's sentence does not state it. Rejected: leaving it to the skill's text alone,
  where a cycle's agent reading the log would not meet it. Cost if wrong: one clause more in an entry.
- **Departures stand in a new section, `## Departing from the rules on failures and logs`**, because a
  table does not sit in a bullet. It splits D3's third step into "from one rule" and "from all of them".
  Rejected: nesting them under the bullet of the rules. Cost if wrong: one heading moved.
- **The six stated once in a seventh bullet, "The rules on failures and logs"**, for the fields they
  share, then a bullet each. Rejected: repeating the fields six times, against the file's size.
- **`*Writing the files*` gains two words**: "library" in the first bullet, and a sentence that the list
  of `### Logging scope` is no copied value, without which WAY-171's "copy no value" reads against it.
- **`reserved_choices.md` gains two rows, not one,** as the icons do, one for each outcome.
- **The review's two lines stand right after "Against the foundation".** The bullet on a refresh in
  `recognize.md` stands after the list of modes, since it can turn the mode; the addition "what writes
  its log lines" stands in the bullet that lists what the product has.
- **Commits:** the foundation first, so that the template's citations stand on existing entries.

No section 4 adaptation, and no invariant test changed.

## Problems as observed

- A `Read` of `foundations/decisions.md` with an offset and no limit failed on the file's size. The
  named entries were read from a scratch extract by their ranges, as the handoff asks.
- No value in the task, spec or handoff failed my reckoning. The spec's "the next free number, WAY-271"
  held: the log ended at WAY-270 and no withdrawn number reaches it.
