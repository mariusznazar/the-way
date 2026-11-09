# List the choices

The step "List the choices" of the skill `settle-technology`, whose `SKILL.md` lies beside this
file.

- From "In scope", "Deliverables", "Inputs and constraints", "Open questions" and the projected
  decisions, list the technology and architecture choices the project needs, by the rule of the
  template's Technology section: a choice whose later settling could change how the work is cut
  into tasks, or that adds something the product has to run, pay for or back up
  (WAY-121).
- Then, where the project brings behaviour a user sees in the running product, take the look at
  its logs, its interface, its development data and the place of its screenshots that
  `running_product.md` beside this file gives, and list each matter as it says.
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
  of what one of the four matters of `running_product.md` asks unanswered does not hold it: the
  item stands `— open`, with that decision nested under it as `running_product.md` gives. A decision
  of the foundation is material here, not a limit (WAY-313): where you see a reason to change the
  decision that holds a choice, the item stands `— open` with that decision nested under it as
  `Changes: <PREFIX>-<NN>`, and you ask no leave first. The decision's present answer enters the
  comparison as one option, and the option that changes the decision says in its line which decision
  it changes; the human's choice among the options is the one consent to the change (WAY-314). This
  holds only until the task's cycle starts (WAY-315). A decision of the foundation the project
  changes no longer holds the choice: where the definition projects its edit, the item is
  `projected` with that heading's question; otherwise it is `open`.
- Write the list into "Technology" in the form the template gives, and set the status line to
  `definition — open: Technology`, before asking.
- Show the list, with one sentence for each item saying why the project needs it, and for each item
  you opened over a decision, one sentence saying the reason to change that decision, and ask the
  human to confirm it, add to it or strike from it. The matters that `running_product.md` and
  `failure_notice.md` beside this file give, where the list holds them — the logs, the interface,
  the development data, the place of the screenshots and how a human learns of a failure — cannot
  be struck from it, and the message says so in one sentence. A human to whom such a matter does
  not apply answers it like any choice, "the tool prints to the console, an agent reads the
  terminal" for instance, and that answer settles the matter, so it does not come back open when
  the step is resumed (WAY-322). In the same message ask, as one question of
  assessment for the whole list, whether the human has a preference or a constraint for any open
  choice; "I do not know" is an answer. Write the answers, a preference as a nested item under its
  choice.
- With no open item, say so in one sentence and go to the step "Close" (`close.md` beside this file).
