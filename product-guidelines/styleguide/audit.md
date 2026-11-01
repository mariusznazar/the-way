# Audit

Where the user interface has screens (WAY-187):

- Read the decisions of the product's log that settle the agent's way to the running product
  (WAY-165), where `refine-task` did not select them.
- Audit in both directions: from the source of values to the screens that read it — a file of
  design tokens nothing reads is a finding — and from each value on a screen to the design token or
  shared component meant to cover it.
- Ask every time what someone sees without data, straight from a link, after a refresh.
- Where the product's foundation settles the agent's way to the running product, open the screens
  that way; otherwise audit from the code and mark as unchecked what cannot be seen without the
  running product, such as whether focus shows.
- Give each finding its file and line and one sentence of its effect on the user. Each cause takes
  one category: a missing design token, a missing shared component, accidental architecture, or a
  meaning — one colour carrying several.
- A palette read off the code is a proposal, never a rule, until the human settles it (WAY-185). An
  existing choice the human keeps becomes a decision whose rationale is the human's words or
  `unknown`, never one the agent infers (WAY-29).
- The audit ends as `product-guidelines/audit_end.md` gives.
