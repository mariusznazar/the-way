---
name: settle-technology
description: Use when a project definition of a product that uses the-way has to settle the technology and architecture choices its project needs before the readiness gate — a language, a framework, a library, a store of data, a way of logging in, a place to run — or to resume that step from the definition's Technology section.
---

# Settle a project's technology

Leads the step of the project level that settles the technology a project needs before the
readiness gate (WAY-121), after the step that finds the definition's foundation entries. It lists
the choices the project needs, finds the entry that already settles each, and settles every other
one with the human as a projected decision. The human weighs consequences for the product, not
technologies
(WAY-123). The form and rules of the Technology section — which choices it lists, its markers, the
weighing of options — stand in `definition_template.md`; how a skill asks stands in
`elements/common/way_of_working.md`; the critique stands in `elements/common/critique/SKILL.md`;
this skill holds the order of the work.

This skill lives in `project-level/technology/` of the-way. In the-way itself, the-way is the
checkout or worktree the session works in, the directory `git rev-parse --show-toplevel`
prints in the session's working directory; in a product, it is the product's pinned `.the-way`. The
project level's directory, `project-level/`, is there, and each skill named below is the project
skill of that name with the `the-way-` prefix.

The step writes into the definition only, never into the product's foundation
(WAY-106).

## 0. Start or resume

- Read the definition whole, `definition_template.md` in full, the section "How a skill asks" of
  `elements/common/way_of_working.md` and `elements/common/critique/SKILL.md`.
- Where "Projected foundation changes" reads `TODO` or holds its working table, the step that finds
  entries has not ended: return to `define-project` step 5.
- Read the product's `foundations/decisions.md` whole: the binding sentences, *Scope* and
  *Relations*.
- Where "Technology" reads `TODO`, begin with step 1.
- Where it holds an item ending `— open`, look first under "Projected foundation changes" for a
  decision written for that choice; where one stands, end the item `— projected: <its question>`.
  Then show the list, ask whether it still holds, and resume step 2 with the open items and the
  preferences written under them; a report of an open choice under `.runs/technology/` that reads
  `critique: passed` is reused, and the research of the others starts again.
- Where it holds a list with no open item, go to step 3.

## 1. List the choices

- From "In scope", "Deliverables", "Inputs and constraints", "Open questions" and the projected
  decisions, list the technology and architecture choices the project needs, by the rule of the
  template's Technology section: a choice whose later settling could change how the work is cut
  into tasks, or that adds something the product has to run, pay for or back up
  (WAY-121).
- Name each choice in the language of the definition by what the product needs it for — "where
  the accounts and saved games are kept" — never by a technology. A way of logging in is listed as
  its method; the library that implements it, where the code needs one and the rule takes it, is a
  choice of its own.
- For each, find what settles it: a decision of the product's foundation, `held by`; a projected
  decision of this definition, `projected`; nothing, `open`. A decision that settles the choice in
  a sentence about something else still holds it; name that decision. A decision of the foundation
  the project changes no longer holds the choice: where the definition projects its new version or
  edit, the item is `projected` with that heading's question; otherwise it is `open`.
- Write the list into "Technology" in the form the template gives, and set the status line to
  `definition — open: Technology`, before asking.
- Show the list, with one sentence for each item saying why the project needs it, and ask the
  human to confirm it, add to it or strike from it. In the same message ask, as one question of
  assessment for the whole list, whether the human has a preference or a constraint for any open
  choice; "I do not know" is an answer. Write the answers, a preference as a nested item under its
  choice.
- With no open item, say so in one sentence and go to step 3.

## 2. Settle the open choices

The research of every open choice that depends on no open choice starts as soon as the list is
confirmed, all at once, as one wave; a choice that depends on another — the library a server's code
calls for logging in, on the language of that server — starts in a later wave, once every choice it
depends on is settled (WAY-122). Write each dependency as a nested item under the choice that
waits, so that a resumed step finds it.

1. **Research.** Give each choice of the wave to a fresh agent of its own, all at once, with the
   definition, the choice and the preferences under it, the template's Technology section, and the
   binding sentences of every decision the Technology list names `held by`. Each finds the options
   in their documentation, starting from what the definition needs of the choice, never from a fixed
   list of stacks, not even as a hint, and gives each option its source: a page of its documentation
   with its version (WAY-122). An option the human named enters the comparison. Where the definition
   already settles the choice in the human's words — a constraint under "Inputs and constraints" —
   that settlement is the only option sought, and it is weighed like any other.
2. **Weigh.** For each option the project's code is written in or against, the agent reads off
   its documentation and its public record of use the properties the template's Technology section
   lists, citing for each the page it was read from. An option lacking one stays in the comparison,
   each lack said as what it means for the product; an option with no documentation or with a
   project no longer maintained is left out with one line saying which, unless the human named it
   or the definition holds it as a constraint — then it stays, with that line said as a lack
   (WAY-122).
3. **Consequences.** For each option kept, the agent says what it costs, where it runs, what
   keeping it running takes and what changing it later costs; every difference claimed between the
   options cites its source (WAY-123). It writes the comparison to
   `.runs/technology/<choice>.md`, the choice's name in lower case with hyphens for spaces, which
   the product's Git ignores, and ends.
4. **Critique.** Give one fresh agent, following `critique`, the whole comparison of a choice, its
   sources and the definition, as soon as that comparison is written, and ask it to refute every
   claimed difference no source supports. Verify each observation and give your verdict; correct the
   comparison by the verdicts, then end the report with the line `critique: passed`. Where no fresh
   agent can run, neither the research nor the comparison goes on: stop and say so (WAY-122,
   WAY-120).
5. **Show.** Once every comparison of the wave reads `critique: passed`, give one fresh agent,
   following `critique`, the whole table with the definition, and ask it for what one choice of
   the table contradicts in another; verify each observation (WAY-120). Then show the wave
   together, in one table: for each choice, the options by their consequences, the lines of the
   options left out, a recommendation and the weak point of the option recommended, anchored in the
   definition or a source of the comparison. A difference with no consequence for the product
   decides nothing; where none remains, recommend the simplest and cheapest option
   (WAY-123, WAY-113).
6. **Choose.** The human chooses each; never choose alone (WAY-123). A human who answers "you
   choose" or "I do not know" takes the recommendation; write it as the human's choice. The
   recommended option taken as offered passes without a further question; any other answer — an
   option whose weak point the table did not name, an answer in the human's own words, one that
   adds a reason or a condition — gets one question against it, anchored in those words or the
   material, the question `way_of_working.md` asks after a choice, asked here and not again
   (WAY-113). A choice the human leaves unanswered goes into the next table.
7. **Write.** Hand each choice to `record-decision` in projected mode, naming the definition, with
   the consequences that decided it, the other options with theirs, the source of each claimed
   difference for its *Based on*, the lacks of a chosen option, and whether a question was asked
   against it; what its step 4.1 would still ask goes into the next table rather than a round of
   its own. The `Candidates:` line stays as it is. Then end the item with
   `— projected: <the decision's question>`, narrow under "Open questions" the question the choice
   settles to what it still asks, removing it once nothing remains, and write both before the next
   table. Start the next wave: every choice whose every dependency is now settled.

## 3. Close

- No item of "Technology" ends `— open`.
- Run `python -B <the-way>/project-level/readiness_check.py <definition> --before-approval`. A
  finding of condition g on an item still open goes back to step 2, any other finding of
  condition g to step 1; any other finding goes back to `define-project`, which names where.
- Return to `define-project`, which sets the status line to `ready for gate` and leads the gate.

A definition approved before this step changes in the sections its fingerprint covers, and goes
through the gate again
(WAY-118).
