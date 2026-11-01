# Settle with the human

- **New tools.** For each new tool or library left as a technology question of the task, read
  `new_tools.md` beside this skill.
- **What it settles.** The roles of the table the styleguide template gives, each row settled with
  the human, its value and the value's source among them; the states of the shared controls; the
  page of every state; the meanings grouped into decisions as that template's section "Pairs and
  meanings" gives; the product's decision adopting the template, and each departure from it by a
  decision with its reason (WAY-173). Ask also what no reading of the code can tell: the names the
  team uses, the exceptions it keeps on purpose.
- **Accessibility.** First ask whether a law or a contract binds the accessibility of the user
  interface: what one requires is an environment fact, and no adoption is needed (WAY-86). Then
  propose the decision adopting WCAG, recommending the newest edition that is a W3C Recommendation
  when the decision is written, named by its number as read on the W3C's page in this session, never
  from memory, at level AA, for every screen of the user interface; propose another way only where
  the human chooses it, and write nothing the human has not accepted (WAY-191, WAY-80). Each success
  criterion an invariant takes a condition from — contrast and visible focus at least — becomes an
  environment fact, with its source as WAY-80 gives it (WAY-191).
- **Which criterion, which ratio.** Put to the human, as a question with a recommendation shown by
  what the user sees — "small text on any background stays readable for someone who sees less
  well" — the criterion of the adopted edition each invariant takes its condition from, and the one
  ratio the contrast test holds every pair of a background and its text to, read from that
  criterion's passage: the stricter one wherever the size of the text on a pair is not known.
  Record both with the facts of WCAG, so that the invariant's condition stands in a decision and
  its fact (WAY-60, WAY-191).
- **Invariants.** Propose an invariant only for a rule a cheap test of the product's suite checks on
  a convention of the product's code; the review compares each change with every other rule, each
  role in its meaning among them (WAY-168). Propose:
  - the three first invariants WAY-189 gives, each with its test in the product's suite: no value
    written in place of a design token, visible focus on every control, and the contrast of every
    pair of a background and its text;
  - the product's decision that the rule against values written in place of design tokens names,
    which says what counts as such a value, and the product's decision that the rule of visible
    focus names, which says which elements are controls and how the code marks them — a class, a
    component, an attribute — so that the condition of each invariant stands in a decision
    (WAY-60);
  - where the human chooses to clean the screens as tasks touch their styles rather than in one
    clean-up, read `staged_cleaning.md` beside this skill;
  - for any other rule, the template's or the product's, that such a test checks, its invariant.
- **The top of the audit's list.** Where step 3's audit ran, the proposal of which causes of the top
  the task takes joins the set, and the human decides on it, as "At step 4" in
  `product-guidelines/audit_end.md` gives (WAY-284).
- **Critique.** Once the set of proposals is complete, one fresh agent critiques it before it is
  shown together, as "Critique before collective review" gives (WAY-120): read that section of
  `elements/common/way_of_working.md` and, unless step 2 read it, `elements/common/critique/SKILL.md`.
