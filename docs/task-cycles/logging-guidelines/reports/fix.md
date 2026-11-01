# Fix report — logging-guidelines

**Status:** `done`

The concern of `reports/author.md`, the three rule files of the vault, stays yours to judge. This fix
read nothing new of the author's and no repository of any product.

## Finding

**1. No rule tells a line of a case flow to carry the identifiers the list names: fixed.**

Read and confirmed before fixing. At `1740c02` the bullet of `### Identifiers in log lines` said
"carries the identifiers that join the events of that case flow" with no word of the list, so an id of
a request alone met the rule for an order's case flow while the list promised the order's number, and
the departure table's "nothing left to read" had nothing behind it.

The fix is the clause the finding gives, in both places, in the same words:

- `product-guidelines/coding/template.md:194-198`: a line of a case flow "carries those of the
  identifiers `### Logging scope` lists that join the events of that case flow, each under the same
  name in every line, the name the list gives it";
- `foundations/decisions.md:8141-8146`, WAY-275, second sentence: "carries those of the identifiers the
  logging scope lists that join the events of that case flow, each under the same name in every line,
  the name the list gives it".

The check that shows it: the two passages above read side by side, found by a search for "those of the
identifiers", so the template does not restate the entry differently (WAY-263). The case of the finding
now fails the rule: where the list names the order's number and an id of a request, and both join the
events of an order's case flow, a line carrying only the id of the request breaks it. The rule now
reads the list, so with the list gone it has nothing to read, as `template.md`'s departure table says.

No other line changed. A search of the repository for `WAY-275`, outside `.runs`, finds only the entry,
the template's two bullets and two citations in `settle.md`, whose text is about the form of a line and
the events; no entry restates the sentence, so the search of WAY-33 gives no further correction.
WAY-275's *Verification*, *Rationale* and *Rejected* stay true and are unchanged.

The review's Minor findings were not touched, as the handoff gives. `spec.md` stands as it passed its
review; its row of the heading at line 153 is narrower than this change, and the change binds.

## WAY-275's sentence for the request

The fix changes its meaning, so this replaces the sentence in `reports/author.md`:

Szablon wymaga linii dla zdarzeń biznesowych z listy, a każda linia przepływu sprawy (poza linią z
ostatniego miejsca) niesie te identyfikatory z listy zakresu logowania, które łączą zdarzenia tego
przepływu, pod tą samą nazwą w każdej linii, tą, którą podaje lista; linia spoza przepływu ich nie
niesie, a postać linii wybiera produkt w swojej decyzji.

## Files changed and commits

| File | Added | Removed |
|---|---|---|
| `foundations/decisions.md` | 4 | 4 |
| `product-guidelines/coding/template.md` | 4 | 3 |

- `d78f148` docs: WAY-275 and its rule have a line of a case flow carry the identifiers the logging
  scope lists

Tree clean, nothing pushed.

## Checks run

Each on `d78f148`, each exit code taken directly, its output going to a file.

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py .` | 0, 0 errors |
| `python -B gate/run_tests.py instruction-files` | 0, skipped 5 |
| `python -B gate/run_tests.py gate` | 0 |
| `python -B gate/run_tests.py agent-instructions` | 0 |
| own-work script, `C:/Users/Mariusz/AppData/Local/Temp/claude/C--Storage-repos-the-way/6e875913-ea61-4094-be96-22e216469b8d/scratchpad/own_check.py` | 0, 0 problems |

Not run: the full gate, as the handoff gives; `task-cycle` and `project-level`, none of whose files this
fix touches, and they passed on the reviewed text; a test of how an agent acts on the new text, as in
the author's report. The own-work script holds no phrase of the new clause, so it shows only that the
rest of the entries still stand; the search above shows the clause.

## Choices

- **"the logging scope" in WAY-275 where the template writes `### Logging scope`.** The entry names the
  scope its first sentence opens, as the rest of the log does. Rejected: the heading in the entry's
  sentence, which ties the entry's wording to a heading WAY-271 already names. Cost if wrong: one
  phrase.
- **The words "the same name in every line" stay**, with "the name the list gives it" added after them,
  so that the rule keeps its reason for a reader who does not open `### Logging scope`. Rejected: only
  "under the name the list gives", the finding's shorter wording, which row 5's "pod tą samą nazwą w
  każdej linii" would no longer stand in. Cost if wrong: a few words more.
- **An identifier the list does not name is neither required nor banned by this rule.** Whether it goes
  on the list is `### Logging scope`'s matter. The fix adds no ban, since no row and no finding asks
  for one. Row 5 said "niesie identyfikatory" with no word of the list, and this reading of it comes from
  D3's chosen way and row 4; the human sees the entry at the merge.
- **No violating example was added to WAY-275's *Verification***, though the finding's case would fit
  one: the handoff says to touch what the finding needs and nothing else.

## Reaches beyond the dispatch

None, beyond `task-cycle/change/fix.md`, which the method names, and the search for `WAY-275`.

## Searches not found or unclear

none
