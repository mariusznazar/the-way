---
name: settle-technology
description: Use when a project definition of a product that uses the-way has to settle the technology and architecture choices its project needs before the readiness gate — a language, a framework, a library, a store of data, a way of logging in, a place to run — or to resume that step from the definition's Technology section.
---

# Settle a project's technology

Leads the step of the project level that settles the technology a project needs, between the step
that finds the definition's foundation entries and the readiness gate
(WAY-121). It lists the choices the project needs, finds the entry that already settles each, and
settles every other one with the human as a projected decision. The human weighs consequences for
the product, not technologies
(WAY-123). The form of the Technology section stands in `definition_template.md`; how a skill asks
stands in `elements/common/way_of_working.md`; the critique stands in
`elements/common/critique/SKILL.md`; this skill holds the order of the work.

This skill lives in `project-level/technology/` of the-way. Installed globally, its base directory
is a link, so resolve it first: `realpath <base>` in Bash, `(Get-Item <base>).Target` in
PowerShell. The project level's directory is the parent of the resolved one, and the-way the
directory above that. In a product, the-way is the product's pinned `.the-way`, and each skill
named below is the product's skill of that name with the `the-way-` prefix.

The step writes into the definition only, never into the product's foundation
(WAY-106).

## 0. Start or resume

- Read the definition whole, `definition_template.md` in full, the section "How a skill asks" of
  `elements/common/way_of_working.md` and `elements/common/critique/SKILL.md`.
- Read the product's `foundations/decisions.md` whole: the binding sentences, *Scope* and
  *Relations*.
- Where "Technology" holds an item ending `— open`, resume at the first such item in step 2. Where
  it reads `TODO`, begin with step 1. Where it holds a list with no open item, go to step 3.

## 1. List the choices

- From "In scope", "Deliverables", "Inputs and constraints", "Open questions" and the projected
  decisions, list the technology and architecture choices the project needs — a language, a
  framework, a library, a store of data, a way of logging in, a place to run, and others of that
  kind (WAY-121).
- Name each choice in the language of the definition by what the product needs it for — "where
  the accounts and saved games are kept" — never by a technology.
- For each, find what settles it: a decision of the product's foundation, `held by`; a projected
  decision of this definition, `projected`; nothing, `open`. A decision that settles the choice in
  a sentence about something else still holds it; name that decision.
- Write the list into "Technology" in the form the template gives, and set the status line to
  `definition — open: Technology`, before asking.
- Show the list, with one sentence for each item saying why the project needs it, and ask the
  human to confirm it, add to it or strike from it. Write the answer.
- With no open item, say so in one sentence and go to step 3.

## 2. Settle each open choice

One choice at a time, a choice that others depend on first — the language of a server before its
library for logging in (WAY-122). For each:

1. **Preferences.** Ask, as a question of assessment, whether the human has a preference or a
   constraint for this choice. "I do not know" is an answer. An option the human names enters the
   comparison and goes through the same filter and critique.
2. **Research.** Find the options in their documentation, starting from what the definition needs
   of the choice, never from a fixed list of stacks, not even as a hint
   (WAY-122). Give each option its source: a page of its documentation with its version.
3. **Filter.** An option the project's code is written in or against passes only where its
   documentation shows the four properties WAY-122 names; cite for each property the page it was
   read from. Keep one line for each option that fails, naming the property it fails
   (WAY-122).
4. **Consequences.** For each option that passed, say what it costs, where it runs, what keeping it
   running takes and what changing it later costs; every difference claimed between the options
   cites its source (WAY-123).
5. **Critique.** Give one fresh agent, following `critique`, the whole comparison of this choice,
   its sources and the definition, and ask it to refute every claimed difference no source
   supports. Verify each observation and give your verdict. Where no fresh agent can run, the
   comparison does not reach the human: stop and say so
   (WAY-122, WAY-120).
6. **Show.** Show the options by their consequences, with the lines of the options that failed,
   the cost of each way and a recommendation. A difference with no consequence for the product
   decides nothing; where none remains, recommend the simplest and cheapest option
   (WAY-123, WAY-113).
7. **Choose.** The human chooses; never choose alone (WAY-14). Ask one question against the
   choice, anchored in the human's words or the material (WAY-113).
8. **Write.** Hand the choice to `record-decision` in projected mode, naming the definition: its
   binding sentence states the choice, its *Rationale* the consequences that decided it, its
   *Rejected* the other options with their consequences. Then end the item with
   `— projected: <the decision's question>`, remove from "Open questions" the question the choice
   settles, and write both before the next choice.

## 3. Close

- No item of "Technology" ends `— open`.
- Run `python -B <the-way>/project-level/readiness_check.py <definition> --before-approval`. A
  finding of condition g goes back to step 1 or 2; any other finding goes back to `define-project`,
  which names where.
- Return to `define-project`, which sets the status line to `ready for gate` and leads the gate.

A definition approved before this step changes in the sections its fingerprint covers, and goes
through the gate again
(WAY-118).
