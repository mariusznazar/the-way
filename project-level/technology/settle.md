# Settle the open choices

The step "Settle the open choices" of the skill `settle-technology`, whose `SKILL.md` lies beside
this file.

The research of every open choice that depends on no open choice starts as soon as the list is
confirmed, all at once, as one wave; a choice that depends on another — the library a server's code
calls for logging in, on the language of that server — starts in a later wave, once every choice it
depends on is settled (WAY-122). Write each dependency as a nested item under the choice that
waits, so that a resumed step finds it.

1. **Research.** Give each choice of the wave to a fresh agent of its own, all at once, with the
   document, the choice and the preferences under it, the template's Technology section, the
   binding sentences of every decision the Technology list names `held by`, and the path of the
   file `research.md`, beside this file, which holds the agent's work. The agent finds the options,
   weighs them, compares their consequences and writes the comparison to the choice's report.
2. **Weigh.** The research agent's work, in `research.md`.
3. **Consequences.** The research agent's work, in `research.md`; it ends with the comparison
   written to the choice's report, `.runs/technology/<choice>.md`.
4. **Critique.** Give one fresh agent, following `critique`, whose file is
   `elements/common/critique/SKILL.md`, the whole comparison of a choice, its sources and the
   document, as soon as that comparison is written, and ask it to refute every
   claimed difference no source supports. Verify each observation and give your verdict; correct the
   comparison by the verdicts, then end the report with the line `critique: passed`. Where no fresh
   agent can run, neither the research nor the comparison goes on: stop and say so (WAY-122,
   WAY-120).
5. **Show.** Once every comparison of the wave reads `critique: passed`, form the recommendation
   of each choice and the weak point of the option recommended, anchored in the document or a
   source of the comparison. A difference with no consequence for the product decides nothing;
   where none remains, recommend the simplest and cheapest option (WAY-123). For a place to run,
   where more than one option is the simplest and cheapest, recommend of those the one an agent
   works with best, by the template's rule (WAY-137). In a
   choice of an agent's way to the running product, the recommendation passes over an option an
   agent cannot use (WAY-166). Then give one
   fresh agent for the wave the option recommended for every choice of the wave, one a constraint
   of the document settles included, with the document and the comparisons, and ask it to run
   on each a devil's advocate, a pre-mortem and a search for unknown unknowns: what choosing that
   option could break. A choice the list names `held by` is never tested (WAY-138). Write the
   risks the tests give into the choice's report, `.runs/technology/<choice>.md`, so that a
   resumed step finds them, as sub-step 6, Choose, needs.
   Then give one fresh agent, following `critique`, whose file is
   `elements/common/critique/SKILL.md`, the whole table with the
   risks and the document, telling it that the risks are hypotheses with no source rather than
   differences claimed between options, so it does not strike them, and ask it for what one choice
   of the table contradicts in another; verify each observation (WAY-120, WAY-138). Then show the
   wave together, in one table: for each choice, the options by their consequences, the lines of
   the options left out, a recommendation, the weak point of the option recommended, and beside
   that option the risks the tests gave, each marked as a hypothesis
   (WAY-123, WAY-138, WAY-113).
6. **Choose.** The human chooses each; never choose alone (WAY-123). The human who chooses the
   option recommended takes the risks shown beside it (WAY-138). A human who answers "you
   choose" or "I do not know" takes the recommendation; write it as the human's choice. The
   recommended option taken as offered passes without a further question; any other answer — an
   option whose weak point the table did not name, an answer in the human's own words, one that
   adds a reason or a condition — gets one question against it, anchored in those words or the
   material, the question the section "How a skill asks" of `elements/common/way_of_working.md`
   asks after a choice, asked here and not again
   (WAY-113). A choice the human leaves unanswered goes into the next table with the risks
   already shown beside its option recommended, and is not tested again unless that option
   changes, when the new one is tested (WAY-138).
7. **Write.** In a run at a task, `task_run.md` beside this file holds this sub-step. Hand each
   choice to `record-decision` in projected mode, naming the definition, with
   the consequences that decided it, the other options with theirs, the source of each claimed
   difference for its *Based on*, the lacks of a chosen option and the risks taken with it for its
   *Rationale*, each risk marked as a hypothesis (WAY-138), and whether a question was asked
   against it; what its step 4.1 would still ask goes into the next table rather than a round of
   its own. The `Candidates:` line stays as it is. Then end the item with
   `— projected: <the decision's question>`, narrow under "Open questions" the question the choice
   settles to what it still asks, removing it once nothing remains, and write both before the next
   table. Start the next wave: every choice whose every dependency is now settled.
