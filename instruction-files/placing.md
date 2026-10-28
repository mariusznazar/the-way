# Placing a single rule

How the skill places one rule, in the mode place.

1. Name what lets the rule in, as "When to add a rule" gives it — the mistake it removes, with the
   records where it was found, or the decision or step it carries — and whether the rule applies
   with a human present or without one. A rule with neither is not placed.
2. Answer the two questions of "Where a rule stands" for the rule. When it must happen every
   time, propose the mechanism first — a CI check, a linter, a check of a step's output, or a
   local git hook where the rule guards against slips rather than against an agent that can turn
   the hook off — and an instruction only for what the mechanism cannot do.
3. Search the instruction files for a rule on the same subject; when one stands, the new wording
   replaces it.
4. Word the rule by "How to write a single rule", with the command or file that leaves its trace.
5. Show the place, the wording and what happens if it is left out, and write only after approval.
