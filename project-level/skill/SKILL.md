---
name: define-project
description: Use when a project of a product that uses the-way has to be defined before it is broken into tasks — an idea, a concept or a note to turn into a project definition, a definition to resume from its status line, or a definition to take through the readiness gate.
---

# Define a project

Leads the first two steps of the project level: the definition, written with a human, and the
readiness gate. The form of a definition and the rule of each section stand in
`definition_template.md`; this skill holds the order of the work and what to ask. The project
level has no decision in the log of the-way yet, so a rule below ends with the decision it waits
for.

This skill lives in `project-level/skill/` of the-way. Installed globally, its base directory is a
link, so resolve it first: `realpath <base>` in Bash, `(Get-Item <base>).Target` in PowerShell. The
project level's directory is the parent of the resolved one, and the-way the directory above that.
In a product, the-way is the product's pinned `.the-way`, and the decisions skill named below is
the product's `the-way-record-decision`.

The project level reads the product's foundation and writes nothing in it
(`TODO — decision pending: which decision sets that the project level writes nothing in the
foundation`).

## 0. Start or resume

- Read `definition_template.md` in full.
- When the human names an existing definition, read it whole and go on from where its status line
  says. A definition whose status reads `approved` is checked first:
  `python -B <the-way>/project-level/readiness_check.py <definition>`. A finding that its
  fingerprint no longer matches means the definition changed after the gate, and it goes through
  step 5 again.
- Otherwise begin with step 1.

## 1. The idea

- Read in full what the human brings: an idea, a note, a concept, a link.
- Settle four things with the human: what the project is to achieve; what is done today without it
  and where that hurts; what changes once it succeeds; why now.
- Give back your understanding in two or three sentences, and wait for the human to confirm or
  correct it.
- Speak the language the human opened in; the definition is written in it, as the template gives.

## 2. Read the foundation for the idea

- Read the product's `foundations/`: in the part map *Files*, *Trust boundary* and *Surface*; in
  the decisions the binding sentences, *Scope* and *Outranks*; in the invariants the sentence and
  *Part*; the glossary; the environment facts
  (`TODO — decision pending: which decision sets what the definition reads from the
  foundation`).
- Bring what you find into the conversation as material: a decision the project would change, an
  invariant it may break, a trust boundary it crosses, a surface it changes. For a decision, ask
  whether the decision changes or the project fits it (WAY-30).
- When the foundation holds no entries, say so in one sentence and go on.

## 3. The first write

- Find where the product keeps its projects: the `## Backlog` section of the product's root
  `AGENTS.md` or `CLAUDE.md`. Where neither names it, ask once, and offer to add the answer as the
  template gives it.
- Propose the definition's file name and path there, and on the human's word write the definition:
  the confirmed goal, `TODO` in every other section, and the status line.

## 4. Rounds through the sections

- Ask a few questions at a time, about the largest unknowns first: what is in and out of scope,
  what success looks like and what would show it false, the risks, the inputs and constraints.
  After each round update the definition and its status line, so that a fresh agent reading only
  the file knows where the work stands.
- Three moves run through the rounds
  (`TODO — decision pending: which decision sets how the definition questions the human's
  frames`):
  - where two sentences of the human contradict each other, quote both and ask which holds; both
    are quoted from the human's words or material, never invented as a risk;
  - "I do not know" to a question of assessment is a result, written as an open question with its
    place of resolution; to a question of decision, give a recommendation, with what each way
    costs;
  - what the files can answer, read yourself instead of asking.
- Never ask for a deadline; the template says how one enters.
- A choice that binds beyond the project — an exclusion for good (WAY-26), a constraint that
  outlives the project, a change to a current decision — goes to the decisions skill in its
  projected mode, naming this definition.
- What is not yet known goes to one of the three places the template names.
- Once no section holds `TODO`, the status line reads `ready for gate`, and step 5 begins.

## 5. The readiness gate

1. Run `python -B <the-way>/project-level/readiness_check.py <definition> --before-approval`. Each
   finding goes back to step 4.
2. Search the whole foundation for what the definition collides with that no written link joins
   (WAY-33): a decision whose binding sentences the project would break, an invariant, a glossary
   term the definition uses in another meaning. Settle each before the gate: a projected new
   version of the decision through the decisions skill, or the definition brought into line with
   it. Note the commit of the product's foundation you searched, as `git rev-parse HEAD` in the
   product prints it.
3. Show the human each projected decision whole, with its translation, and ask whether its wording
   is approved. A wording the human changes goes through the decisions skill's projected mode
   again.
4. On the human's approval, write `<who>, YYYY-MM-DD` into *Approved by* of every projected
   decision; then print the fingerprint with
   `python -B <the-way>/project-level/readiness_check.py <definition> --fingerprint`, write the
   gate record, and set the status line to `approved YYYY-MM-DD`.
5. Run the check with no option; it must report nothing found. Tell the human what it reported,
   and that conditions b and c rest on the approval and on the search, which no script checks.

A change of the definition after the gate goes through the gate again
(`TODO — decision pending: which decision sets the readiness gate of a project`).
