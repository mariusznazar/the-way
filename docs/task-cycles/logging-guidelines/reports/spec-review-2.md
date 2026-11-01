PASS

# Review of the revised spec — logging-guidelines

Reviewed: the revised `.runs/task-cycles/logging-guidelines/spec.md`, against the frozen `task.md`, the
first report `reports/spec-review.md` and the designer's `reports/designer-revision.md`. All four
findings are fixed, and the revision broke nothing else. Where the designer's report claims a change,
it was read in the spec itself. The spec is ignored by Git, so there is no diff: it was read whole
again and compared with the first version.

## Earlier findings

### 1. The exception widened to secrets: fixed

D3's row of `### Secrets and personal data` now reads "no secret in the logs, with no exception" and
"the identifiers `### Logging scope` lists being the one exception, to this ban alone". E6 reads "an
exception to the second ban alone". Both match To do 1 and row 6. The table of what goes with a
departure now says "the exception to the ban on personal data".

### 2. A departure from the ban on personal data alone: fixed, another way than recommended

The question now has one answer. The rule stays, and in its text the one line
`Personal data: none — <PREFIX-NN>` stands in place of the ban. The designer's reason for not taking
my recommendation holds, and my recommendation was the weaker one: row 6 lets a product depart from
the ban, and its exception covers only identifiers, so the list alone cannot carry that departure for
personal data that is no identifier. The list stays as the first step and is no departure.

Checked against the foundation and the rest of the spec:

- WAY-171 and `product-guidelines/template.md`. "Holds only `none —`" binds a rule the product drops,
  and this rule is not dropped. WAY-171 lets a discipline's template add what it names at its places,
  so the line needs no correction of an entry, and it keeps that entry's reason: a departure shows
  where the text would stand.
- WAY-173. The departure stands in a decision of the product's log, with its reason (D1, sentence 1
  and *Rationale*; E9).
- Row 6 and E6. E6 adds "the rest of the rule standing". That is the form of this departure, an open
  choice of the spec, and it takes nothing from the row. Dropping the rule whole stays open under
  WAY-173 (D3, item 3), so the two do not collide.
- Precedence. D3 and its table agree: it stays for a secret and goes as to personal data. An original
  error that quotes personal data is written as it stands. This follows from the ban having gone, so
  it invents nothing. E6's `narrows E2` stands at the template's level.
- D4. The heading stays, so a refresh meets no absence.
- D5. The warning about what goes with a departure stands under "What it settles", so the list of
  five weak points stays as To do 4 names it.
- `elements/common/foundation_check.py`. `FIELD` matches only `- **<name>:**`, so the line is not read
  as a field.

### 3. D3 against itself on `### Logging scope`: fixed

The sentence now excepts this case, "a rule whose subject has gone reads `none —` too, with the same
entry", and says that three headings hold the marker. The table, D1's log table and D5 agree, and the
human hears it before settling.

### 4. E2 and E5 on a last-resort line: fixed

E5's sentence carries the exception, "one from the last-resort handler apart". "How rows meet the
rest" and D9 say so, and neither entry names the other as `narrows`.

## What the revision broke besides

Nothing.

## Claims checked

The claims of the first report stand, and the revision changes none of the files, numbers or searches
they rest on. New in this round: the `FIELD` check above, and the units, which stay as they were: the
new form lies in `product-guidelines/coding/template.md` ("the departure") and in `settle.md`.

## Reaches beyond the handoff

- `elements/common/foundation_check.py:78-88` and `:220`, the patterns `FIELD` and `FINGERPRINTED`:
  to see whether the new line is read as a field.

No note of the author and no repository of any product was read in this round.

## Searches not found or unclear

- Unclear: whether the label `Personal data:` stays in English in a product that writes its guidelines
  in another language. WAY-171 and the *Language* bullet of `product-guidelines/template.md` keep the
  marker `none —` in English and name no such label, while D3 gives the line as a literal. No script
  reads it and either reading misleads no agent, so it is no finding; the maker can settle it in the
  template's bullet for this rule.
- Unclear, from the first report and unchanged: whether WAY-134's "ways not chosen that the row's
  source keeps" covers E7, whose *Rejected* stays `unknown`. The build does not go wrong either way;
  the whole-change reviewer may ask.
- Unclear, in the task and resolved by the spec: after a departure from the ban on personal data, an
  item that points to a person still takes the human's consent, since row 4 stands apart from row 6.
  The designer names this, and the spec's reading is sound.
