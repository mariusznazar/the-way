# Findings of the review of correction 2 — for the fix

Reviewer's report: `reports/review-correction-2-report.md`, first line `FAIL fa5d349e`. Cut word for word from it: the blocking finding. The two Minor findings of the report (2 and 3) are findings of a correction: they are not fixed and go to the request's list.

## Blocking

**1. The three statements of item 2 do not say the same thing.**

- WAY-05, `foundations/decisions.md:686-687`: an entry "may carry a further such paragraph for a
  part of its own question". On its words that is one further paragraph. The clause before it says
  "one paragraph … for each part of another question", so the change from "for each part" to "a
  further … for a part" reads as meant.
- The template, "Binding sentences", `elements/decisions/template.md:135-137`: "A part of the
  entry's own question, the question of its heading, may also have a paragraph of its own after the
  first." Any part may have one, so several paragraphs.
- The template, the entry form, `elements/decisions/template.md:31-32`: "for a part of another
  question this entry answers or for a part of the question of the heading, one paragraph for each
  such part". One paragraph for each part, several, and with no "may": it gives a part of the
  heading's question the same rule as a part of another question.

What the remark says: "A further paragraph may also carry a part of the entry's own question … each
such paragraph stands within the limits of a paragraph". "Each such paragraph" allows several, and
WAY-05 does not carry those words.

Why it matters. The entry is what binds, and its words are the narrowest of the three. The two
tasks that follow this request divide entries at parts of their own question: WAY-344, with 8
sentences and 743 words, needs at least three paragraphs to meet the limit of three sentences, so
two further ones. A reviewer of that task who reads WAY-05 as it stands can object to the second,
which is the state item 2 was to end ("the rule and the entries then say different things and a
reviewer can rightly object"). Read that way, WAY-05 is also a limit on the number of paragraphs
for an entry's own question, a kind of limit the human did not choose under item 1. And the
template, a file of the same change, says more than the entry it restates, which WAY-263 grades
Important.

The sentence of WAY-05 can be read the other way too, as "for any part, a further paragraph"; I
block because the entry form beside it is plainly broader and the next task rests on the
difference. The fix is one wording in the three places: that an entry may carry a further such
paragraph for each part of its own question it sets apart, and an entry form that keeps "may" for
that kind.

Contradiction: yes — item 2 of the remarks ("each such paragraph"), the way not chosen under
item 1 ("a limit on the number of paragraphs of an entry"), and WAY-05 as the correction writes it,
which the template's entry form restates more broadly.
