# Decide entry

- Find the rule and where it is said: the conversation, a decision's verification, the list a
  task's return step made, a ticket or a requirement of the product, or the product's code when
  the process enters an existing product.
- Recovering from what a product does: list what the part does, each item as a candidate
  sentence with the place in the code that shows it, and let the human choose; only what the
  human chooses becomes an entry (WAY-28).
- Apply the test in the decision template's section "Decision or invariant": a rule that records
  a choice goes through `record-decision` first, and the invariant is written as derived from it.
  A reason found behind recovered behaviour is not recovered as a decision in this change (WAY-28);
  one the human gives is (`TODO — decision pending: which decision sets that a reason the human
  gives for recovered behaviour is written as a decision`).
- When the rule holds more than one sentence can state, propose one entry per sentence; the
  template says what one sentence may join.
- Search the file, including its withdrawn identifiers, for an entry this rule would change:
  found — a change, split, merge or withdrawal, or an entry of its own where the template's "Where
  entries go" gives one; not found — a new identifier.
- The search of the foundation also looks for a decision whose level 1 verification calls for this
  rule, and an entry it names whose binding part has changed, to check it against that part again
  (WAY-33).
