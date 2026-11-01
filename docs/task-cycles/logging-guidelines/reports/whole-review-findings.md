# Blocking findings — whole-change review `FAIL 1740c02`

From `reports/whole-review.md`, in the reviewer's words.

## 1. No rule tells a line of a case flow to carry the identifiers the list names

Place: `product-guidelines/coding/template.md:194-197`, the bullet **Identifiers in log lines**, from
commit `aa4a41c`, and `foundations/decisions.md:8143`, WAY-275, from `8b563cd`.

What is wrong. The spec's chosen way for the six rules reads, at D3: "a sixth rule holding both lists;
the identifiers, events and personal-data rules name it" (`spec.md:142`). Two of the three do:

- `template.md:200`: "Each business event `### Logging scope` lists leaves a log line";
- `template.md:204`: "the identifiers `### Logging scope` lists being the one exception";
- `template.md:194-197`: "carries the identifiers that join the events of that case flow, each under
  the same name in every line", with no word of the list.

The departure table rests on the missing link. `template.md:269` says that `### Identifiers in log
lines` goes with `### Logging scope` because it has "nothing left to read". As written it reads
nothing of the list, and it would stand unchanged with the list gone.

Why it matters. The list is the product's promise of which identifiers it logs (To do 3, row 4), and
the rule is the one a change is compared with (WAY-168, To do 5). As written, a change whose lines
carry only an id of a request meets the rule for an order's case flow, since that id joins the events,
while the list promises the number of the order. No rule then requires what the list promises, so a
reviewer has nothing to hold the change to, and a reviewer reading `### Logging scope` alone finds "a
promise and no inventory". Events have a rule of their own for this reason: question 8 turned down
"bez reguły, tylko decyzja produktu" because the promise would act only when someone happened on it.
Identifiers get that outcome by omission. Nothing also ties the name a line uses to "the name it takes
in every line" that the list gives, so the sameness of names rests on each agent happening to read the
later rule for it.

Evidence: the three lines above and `spec.md:142`, `:216`. The table at `spec.md:153` is silent on the
list, so the spec's own row of the heading is narrower than its chosen way, which is where the omission
comes from. The author's own-work check could not see this: it checks that phrases stand, and all of
them do.

The fix is one clause: the bullet says the line carries those of the identifiers `### Logging scope`
lists that join the events of the case flow, under the name the list gives. WAY-275's second sentence
takes the same clause, so that the template does not restate it differently (WAY-263).
