# Designer's report — revision of the spec, logging-guidelines

Status: `done`
Spec: `.runs/task-cycles/logging-guidelines/spec.md`
Review answered: `.runs/task-cycles/logging-guidelines/reports/spec-review.md`, `FAIL`, four findings.
No tracked file changed; no commit made. The two files written are the spec and this report. The
choices of the first spec stand: one entry, the words, the six headings, their place and their fields.

## The four findings

### Finding 1 — the exception widened to secrets: resolved

In D3's row of `### Secrets and personal data` and in E6, the exception now attaches to the ban on
personal data alone, as To do 1 and row 6 have it. D3 also says what follows for the reviewer's case:
no secret in the logs, with no exception, so an identifier that is a secret stays out even where it
stands on the list. D3's table of what goes with a departure now reads "the exception to the ban on
personal data".

### Finding 2 — a departure from the ban on personal data alone: settled, not as recommended

The question: what does a product write that departs from the ban on personal data and keeps the ban
on secrets? The spec's answer: the rule stays, with its heading and fields, *Decision* naming the entry
of D1, and in the rule's text, in place of the ban, the one line `Personal data: none — <PREFIX-NN>`.
The rule keeps the ban on secrets, the ban on whole objects and request bodies, and its precedence for
a secret; an original error that quotes personal data is written as it stands.

I did not take the recommended way as the whole answer. The list covers identifiers only, because
row 6's exception is "identyfikatory z listy". A product that wants to log personal data that is no
identifier could not do so by the list, yet row 6 says it may depart with a reason; and the fallback
the report offers, dropping the heading with a warning, costs the ban on secrets, which is exactly what
the handoff asks to keep. So the list stays as the first step and is no departure, and the chosen way
carries the real one.

| Way | Verdict | Why |
|---|---|---|
| the rule stays, one ban departed from, one line in its text | chosen | the only way that gives row 6's departure and keeps the ban on secrets within six rules |
| only the list | first step, not the whole answer | identifiers only, as above |
| the heading dropped, with a warning | rejected for this departure | takes the ban on secrets, the ban on whole objects and the precedence; stays the form of dropping the rule whole |
| two headings, `### Secrets` and `### Personal data` | rejected | the cleanest file, but seven rules where To do 1 holds one rule and D3 six, which reopens a settled form |

The line needs no correction of WAY-171: the rule is not dropped, so "holds only" does not reach it,
and WAY-171 lets a discipline's template add what it names at its places. It is limited to this ban
because row 6 names it alone. The cost is one line of form in one rule.

Changed: D1's first sentence, its log table (two new rows), D3 (a new passage, and two rows of its
table), D5's `settle.md`, and E6 and E9.

### Finding 3 — D3 against itself on `### Logging scope`: resolved

D3's sentence now says a rule whose subject has gone reads `none —` too, with the same entry, so a
departure from `### Logging scope` puts the marker on three headings; its table says the same. D1's log
table names the case. D5 has the skill say what goes with a departure before the human settles it, as
WAY-174 asks, and this applies equally to dropping `### Secrets and personal data` whole. That warning
stands under "What it settles" in `settle.md`, so D5's list of five *Weak points* stays as the task
names it.

### Finding 4 — E2 and E5 on a last-resort line: resolved

E5's sentence carries the exception, as the reviewer recommended and WAY-30 allows for one written in
advance. "How rows meet the rest" gains a line on the pair, and D9 says the two no longer collide.
Neither entry names the other as `narrows`.

## The four checks, on the revision

1. Placeholders, `TBD`, empty sections: none.
2. Contradictions: one corrected on rereading, a cell of the new table in D3 that said "against the
   question", which pointed at nothing in the spec. D1, D3, D5, D9, E5, E6 and E9 now agree on the
   exception, the three headings and the last-resort line.
3. Several independent changes: no, as before.
4. Two readings: the new one is whether an original error that quotes personal data keeps it after the
   departure. Picked: it does, since the precedence then holds only for a secret.

## Reaches beyond the handoff

None. `task-cycle/spec/design.md` and the entries were not read again; the revision rests on what the
first reading held and on the review report. WAY-171 and WAY-173 are cited from that reading.

## Searches not found or unclear

- `task-cycle/spec/design.md` gives no separate form for a revision. I took the same four checks and
  this report's form.
- Row 6 lets a product depart from the ban on personal data and says nothing of a departure from any
  other limb of the rule. The spec gives no partial form for those: another limb goes only with the
  rule whole. If a product reports wanting to drop the ban on whole objects alone, the spec's answer is
  that it drops the rule or keeps it.
- After a departure from the ban on personal data, the boundary of row 4 still has an item that points
  to a person take the human's consent. The task does not say this case. The spec keeps the boundary
  while `### Logging scope` stands, since row 4 stands apart from row 6.
- From the review report's "Weighed and not reported", E7's *Rejected* remains `unknown`. The handoff
  asks for nothing there, and the reviewer says the build does not go wrong either way; the
  whole-change reviewer may ask.
