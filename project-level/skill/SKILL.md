---
name: define-project
description: Use when a project of a product that uses the-way has to be defined before it is broken into tasks — an idea, a concept or a note to turn into a project definition, a definition to resume from its status line, or a definition to take through the readiness gate.
---

# Define a project

Leads the first two steps of the project level: the definition, written with a human, and the
readiness gate; the settling of the project's technology, between them, it hands to
`settle-technology`. A definition records what is settled about the product before the project is
broken into tasks — as projected entries of the foundation — so that the breakdown and the tasks
guess as little as they can. The form of a definition and the rule of each section stand in
`definition_template.md`; how a skill asks stands in `elements/common/way_of_working.md`; this
skill holds the order of the work. The decisions that set its rules are cited below.

This skill lives in `project-level/skill/` of the-way. Installed globally, its base directory is a
link, so resolve it first: `realpath <base>` in Bash, `(Get-Item <base>).Target` in PowerShell. The
project level's directory is the parent of the resolved one, and the-way the directory above that.
In a product, the-way is the product's pinned `.the-way`, and each skill named below is the
product's skill of that name with the `the-way-` prefix.

The project level reads the product's foundation and writes nothing in it
(WAY-106).

## 0. Start or resume

- Read `definition_template.md` in full, and the section "How a skill asks" of
  `elements/common/way_of_working.md`.
- When the human names an existing definition, read it whole and go on from where its status line
  says; a working table under "Projected foundation changes" means step 5 is under way, and an
  item of "Technology" ending `— open` that step 6 is. A definition whose status reads `approved`
  is checked first:
  `python -B <the-way>/project-level/readiness_check.py <definition>`. A finding that its
  fingerprint no longer matches means the definition changed after the gate, and it goes through
  step 7 again.
- A definition with no `## Technology` section was written before the step that settles the
  technology. Say so, and ask whether the project is reopened, with the cost of each way:
  reopening settles the technology at step 6 and takes the definition through the gate again
  (WAY-118); leaving it leaves the choices to the breakdown, and the check keeps reporting the
  missing section. On reopening, add `## Technology` reading `TODO` before "Projected foundation
  changes", set the status line to `definition — open: Technology`, and go on at step 6
  (WAY-121).
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
  the decisions the binding sentences, *Scope* and *Relations*; in the invariants the sentence and
  *Part*; the glossary; the environment facts
  (WAY-111).
- Bring what you find into the conversation as material: a decision the project would change, an
  invariant it may break, a trust boundary it crosses, a surface it changes. For a decision, ask
  whether the decision changes or the project fits it (WAY-30).
- When the foundation holds no entries, say so in one sentence and go on.

## 3. The first write

- Find where the product keeps its projects: the `## Backlog` section of the product's root
  `AGENTS.md`. Where it does not name the place, ask once, and offer to add the answer as the
  template gives it.
- Once the human has confirmed the goal, write the definition there without asking: the confirmed
  goal, `TODO` in every other section but the gate record, which the template gives, and the
  status line. Give the definition's full path in the same message
  (WAY-112).

## 4. Rounds through the sections

- Ask about the largest unknowns first: what is in and out of scope, what success looks like and
  what would show it false, the risks, the inputs and constraints.
- Write each answer into the definition, with its status line, before the next question, so that a
  fresh agent reading only the file knows where the work stands
  (WAY-112).
- Background, Success and Risks hold what the human answered: ask for them, as the template gives.
- Three moves run through the rounds
  (WAY-112):
  - where two sentences of the human contradict each other, quote both and ask which holds; both
    are quoted from the human's words or material, never invented as a risk;
  - "I do not know" to a question of assessment is a result, written as an open question with its
    place of resolution; to a question of decision, give a recommendation, with what each way
    costs;
  - what the files can answer, read yourself instead of asking.
- Never ask for a deadline; the template says how one enters.
- A settlement that binds beyond the project stays in the text of its section for now; step 5 makes
  it an entry. "Projected foundation changes" reads `TODO` until then.
- A technology choice the human cannot settle stays in the text or as an open question for now;
  step 6 settles it. "Technology" reads `TODO` until then.
- What is not yet known goes to one of the three places the template names.
- Once no section but "Technology" and "Projected foundation changes" holds `TODO`, step 5
  begins.

## 5. Find the entries

- Run `find-foundation-entries` with this definition, the conversation and the material it started
  from as the source, the breakdown of the project as the next reader, and projected entries into
  "Projected foundation changes" as the mode.
- A new projected decision needs no number and no prefix: ask for none. Keep the identifiers that
  other projected headings require.
- A technology choice the human has not settled is no candidate: step 6 settles it.
- Once the step ends, set the status line to `definition — open: Technology`; step 6 begins.

## 6. Settle the technology

- Run `settle-technology` with this definition
  (WAY-121).
- Once `python -B <the-way>/project-level/readiness_check.py <definition> --before-approval`
  reports nothing — a `TODO` in a projected field awaiting code or the world is no machine gap —
  set the status line to `ready for gate`, as the template gives it; step 7 begins.

## 7. The readiness gate

1. Run `python -B <the-way>/project-level/readiness_check.py <definition> --before-approval`. A
   finding of condition f goes back to step 5; a finding of condition g, or of condition a in
   "Technology", goes back to step 6; a finding of condition a inside a projected entry goes to the
   skill of its element in projected mode, which completes that entry's wording; any other finding
   goes back to step 4.
2. Search the whole foundation for what the definition collides with that no written link joins
   (WAY-33): a decision whose binding sentences the project would break, an invariant, a glossary
   term the definition uses in another meaning, a fact the project contradicts. Settle each before
   the gate: a projected change to the entry through the skill of its element in projected mode
   (an edit in place before main, otherwise a new version), or the definition brought into line
   with it. Note the commit of the product's foundation you searched, as `git rev-parse HEAD` in
   the product prints it.
3. Offer the human a review of the projected entries one by one or as a complete set, with the
   cost of each way. Candidate selection chose which entries to project; their wording has not yet
   been approved (WAY-114, WAY-115). For a complete set, first run `critique` once on all finished
   entries, the definition and its sources. Verify its observations, correct proposals through the
   skills of their elements and bring any conflict with a human settlement back to the human. If
   an independent critic cannot run, stop the collective route and offer one-by-one human review
   or wait; the author's self-check does not meet this condition. After the critique, show all
   projected entries whole, with their translations, for collective approval. For review one by
   one, show each entry whole with its translation and ask whether its wording is approved; the
   human supplies the critical second reading. A wording the human changes goes through the skill
   of its element in projected mode again; where it changes the question of a decision an item of
   "Technology" names, the item takes the new question.
4. After the final review changes, run the check of 7.1 again; a finding goes where 7.1 sends it.
   Then, for each projected decision whose *Review when* reads `TODO`,
   confirm that the human expressly deferred it and that a related item under "Open questions"
   names the breakdown or task that will settle it. The readiness script does not establish this
   relation. On the human's approval, write `<who>, YYYY-MM-DD` into *Approved by* of every projected
   decision; the other kinds have no field of approval, and the gate record approves them. Then
   print the fingerprint with
   `python -B <the-way>/project-level/readiness_check.py <definition> --fingerprint`, write the
   gate record, and set the status line to `approved YYYY-MM-DD`.
5. Run the check with no option; it must report nothing found. Tell the human what it reported,
   and that conditions b and c rest on the approval and on the search, which no script checks.

A change of the definition after the gate goes through the gate again
(WAY-118).
