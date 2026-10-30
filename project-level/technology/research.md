# Research the options of one technology choice

This is your work as a fresh research agent of the skill `settle-technology` of the-way: the
research of one technology choice of a project definition, for the agent that leads the step, the
leader. This file lies in `project-level/technology/` of the-way — the checkout or worktree the
leader works in or, in a product, its pinned `.the-way` — and `definition_template.md` lies in
`project-level/`, one directory above it.

The leader gives you the definition, the choice and the preferences under it, the template's
Technology section — the section "Technology" of `definition_template.md` — and the binding
sentences of every decision that the list in the definition's section "Technology" names `held by`.
The step writes into the definition only, never into the product's foundation (WAY-106); your own
output is the one report below. A reference such as (WAY-122) names the decision of the-way that sets
the rule beside it; you need not open it.

1. **Research.** Find the options in their documentation, starting from what the definition needs
   of the choice, never from a fixed list of stacks, not even as a hint, and give each option its
   source: a page of its documentation with its version (WAY-122). An option the human named enters
   the comparison. Where the definition already settles the choice in the human's words — a
   constraint under "Inputs and constraints" — that settlement is the only option sought, and it is
   weighed like any other.
2. **Weigh.** For each option the project's code is written in or against, read off its
   documentation and its public record of use the properties the template's Technology section
   lists, citing for each the page it was read from. An option lacking one stays in the comparison,
   each lack said as what it means for the product; an option with no documentation or with a
   project no longer maintained is left out with one line saying which, unless the human named it
   or the definition holds it as a constraint — then it stays, with that line said as a lack
   (WAY-122).
3. **Consequences.** For each option kept, say what it costs, where it runs, what keeping it
   running takes and what changing it later costs; every difference claimed between the options
   cites its source (WAY-123). In a choice of an agent's way to the running product — the logs, the
   interface or the development data, the three matters the template's Technology section names —
   also say for each option whether an agent can use it, and an option an agent cannot use stays in
   the comparison with the lack "an agent does not check the running product this way" (WAY-166).
   Write the comparison to
   `.runs/technology/<choice>.md`, the choice's name in lower case with hyphens for spaces, which
   the product's Git ignores, and end.
