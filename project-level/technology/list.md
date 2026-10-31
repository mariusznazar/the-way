# List the choices

The step "List the choices" of the skill `settle-technology`, whose `SKILL.md` lies beside this
file.

- From "In scope", "Deliverables", "Inputs and constraints", "Open questions" and the projected
  decisions, list the technology and architecture choices the project needs, by the rule of the
  template's Technology section: a choice whose later settling could change how the work is cut
  into tasks, or that adds something the product has to run, pay for or back up
  (WAY-121).
- Then, where the project brings behaviour a user sees in the running product, take the look at
  its logs, its interface and its development data that `running_product.md` beside this file
  gives, and list each matter as it says.
- Then, unless the definition, or a decision of the foundation, keeps the product on the machine on
  which it is made, take the look at how a human learns of a failure that `failure_notice.md`
  beside this file gives, and list the matter as it says.
- Name each choice in the language of the definition by what the product needs it for — "where
  the accounts and saved games are kept" — never by a technology. A way of logging in is listed as
  its method; the library that implements it, where the code needs one and the rule takes it, is a
  choice of its own.
- For each, find what settles it: a decision of the product's foundation, `held by`; a projected
  decision of this definition, `projected`; nothing, `open`. A decision that settles the choice in
  a sentence about something else still holds it; name that decision. A decision that leaves part
  of what one of the three matters of `running_product.md` asks unanswered does not hold it. A
  decision of the foundation
  the project changes no longer holds the choice: where the definition projects its edit, the item
  is `projected` with that heading's question; otherwise it is `open`.
- Write the list into "Technology" in the form the template gives, and set the status line to
  `definition — open: Technology`, before asking.
- Show the list, with one sentence for each item saying why the project needs it, and ask the
  human to confirm it, add to it or strike from it. In the same message ask, as one question of
  assessment for the whole list, whether the human has a preference or a constraint for any open
  choice; "I do not know" is an answer. Write the answers, a preference as a nested item under its
  choice.
- With no open item, say so in one sentence and go to the step "Close" (`close.md` beside this file).
