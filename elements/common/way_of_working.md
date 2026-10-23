# The way of working the skills share

This file holds, once, the steps every element's skill takes to write an entry (WAY-35). Each rule
of an entry stands in its element's template or in `rules.md` beside this file; a skill holds only
the way of working particular to its element, and adds it to the steps below at the places it
names (WAY-35). A fix to a rule goes to the template or to `rules.md`.

Paths under `elements/` below are those of the-way at the commit the product pins (WAY-34); in
the-way itself, those of the checkout or worktree the session works in.

## Critique before collective review

When an agent has finished a set of proposals that the human will review together, one fresh
agent critiques the complete set before it is shown. This includes entries added as consequences
of earlier proposals. The agent follows `elements/common/critique/SKILL.md` for the critique and for
an independently requested critique (WAY-120).

## How a skill asks

Every skill of the-way that asks the human asks this way
(WAY-113):

- A question stands as plain text in the conversation, never in a tool that opens a separate panel
  for a question or its options.
- A question of decision — a choice that settles something in a file — gives the ways open, what
  each costs, and a recommendation; the question with a proposed answer and its reason of step 4.1
  is one such.
- Once the human has chosen, and the choice enters the binding part of an entry, ask one question
  against the answer given: its anchor quoted from a sentence of the human or of the material the
  work starts from, asking whether the choice still holds against it. A choice that ends with the
  work passes without one, and so does a way the human took as offered when the question of
  decision named its weak point, anchored in the material; an answer in the human's own words, or
  one that adds a condition to the way, still gets the question.
- A question of assessment — what something is worth, what may go wrong, what is done today — is
  open, with no ways offered.

## 1. Read

- Read in full the element's `template.md`, `elements/common/rules.md` and this file.
- Read the element's examples: its `examples.md` where it has one. Where `examples.md` names
  entries by identifier or number, read each of them in the-way's `foundations/`, at the commit the
  product pins; where it holds entries itself, read them there. An element with no `examples.md`
  names in its template the entries of the-way that serve as its examples, and those are read
  (WAY-09, WAY-34).
- Select and read the product's foundation as "Reading the foundation" below gives it; the
  element's skill adds the entries its operation needs (WAY-150).
- Where the product has no file of the element's entries, ask whether it starts that file here; if
  not, stop
  (`TODO — decision pending: which decision sets that a product starts an element's file only on
  the human's word`). If so, the same change gives the new file to a part of the map through
  `update-part-map` (WAY-44). Where the missing file is the part map itself, the current
  `update-part-map` invocation writes the first map directly, using its "The first map of a
  product" section. Where another element's file is missing and the product has no part map,
  `update-part-map` writes the map first (WAY-28, for a product the process enters;
  `TODO — decision pending: which decision sets that the part map is written before another
  element's first file`).

## Reading the foundation

Use this method for the current foundation of the repository being worked on (WAY-150). It
selects what the work reads and is no search of the whole foundation, which step 2 makes once the
entry is settled (WAY-33).

Who selects (WAY-150): outside the task cycle — refining a task, defining, planning or leading a
project — the agent doing the work selects for itself. In the task cycle, the orchestrator of
`implement-task` selects by this method for its own judgments and for what each handoff names; the
reviewer of the whole change selects for its own review; and an agent writing a foundation entry
through an element's skill, in the cycle's foundation step or return step included, selects as the
skill's step 1 gives. Every other agent of the cycle reads what its handoff names, as its method
gives.

1. Name the parts the work touches by the part map's rules for assigning files: the parts of the
   files the work changes or is to change, and, for a file collecting entries about several parts,
   the parts the entries it writes or changes name (WAY-44). Where the work names no file yet — an
   idea, a project's scope — name the parts whose responsibility it changes, and a new part as a
   prospective one. Where a part is uncertain, read each candidate.
2. Find the decisions whose *Scope* names a touched part (WAY-21) by a search of the decision log:
   take each `- **Scope:**` line with the indented lines that continue it, and keep the entries
   where the part's identifier stands as a whole item. *Scope* names parts by identifier alone, as
   `elements/common/foundation_check.py` holds it to. Add those the task's *Decisions in play* or
   the work's source names. Read each decision found whole, as the range of lines from its heading
   to the next heading, with its rationale and *Rejected*: a search hit or a binding sentence
   locates an entry, never replaces it. The whole log is not read.
3. Read the touched parts' entries of the part map; the invariants the work reaches (WAY-62) —
   those whose *Part* names a touched part or `every`, found by the same search of *Part*, and
   those a test the work alters cites by its line `invariant: <identifier>`; and the entries these
   and the decisions of step 2 link to — *Relations*, *Based on*, *Verification*, *Derives from*,
   *Rests on* — as far as the work needs them, each whole.
4. Read the glossary entries of the terms the work uses: of the product's glossary and, in a
   product other than the-way, of the-way's glossary at the pinned commit (WAY-226).

The selection is not recorded, nor compared with every *Scope* of the log (WAY-150). Where
relevance is uncertain, read more entries; read a file whole only where it is short, such as the
part map or the glossary. The templates, rules and examples of step 1 are read whole whatever the
selection.

## 2. Search the foundation

Once the skill has settled what the entry is, search the whole foundation once for the entries it
touches: those that name it or that it names, and those no written link joins to it — not only
those a link, a shared *Scope* or a shared *Part* leads to (WAY-33). Read each entry the search
finds whole (WAY-150): a decision's *Rejected* holds an option already weighed and refused, and
nowhere else says so. The search also asks:

- whether the entry uses a glossary term in another meaning than its entry gives, or a word in a
  meaning a reader who knows the product's field would not give it, which the glossary does not
  yet hold: such a word goes through `record-glossary-term` (WAY-95, WAY-99);
- whether the change brings what entries of the foundation wait for — an element's template, the
  part map, a script; each such entry is fixed in the same change (WAY-37).

Each finding becomes a link the element's template gives, a change to one of the entries, or a
question in step 4, before the entry is accepted (WAY-33). The skill names what else the search
looks for in its element. The search is not repeated before the merge and leaves no record
(WAY-33).

## 3. Draft

- Fill every field as the element's template and `rules.md` give it.
- Take every value from its source — the conversation, a document the human names, the product's
  files, the output of a command run for it — never from memory. A value the source does not give
  is a question in step 4 that proposes where to look for it, never the value itself, and the draft
  takes it only as read there (WAY-80 for the source of a fact and of a citation;
  `TODO — decision pending: which decision sets that any other value the source does not give is
  asked for, never taken from memory`).
- A field its source is silent on is a question in step 4, never a `none` the agent writes
  (`TODO — decision pending: which decision sets that a field its source is silent on is asked
  about before anything is written in it`); what stays open after step 4 is written as `rules.md`
  gives it (WAY-71).
- A value that a closed list of the template does not hold is a question in step 4, never the
  nearest value on the list with a reason why it will do (WAY-54); the list grows as the template
  says.

## 4. Ask, show, write

1. Ask in one round about everything still open, each question with a proposed answer and the
   reason for it
   (`TODO — decision pending: which decision sets that the questions of one entry are asked in one
   round, each with a proposed answer`).
2. Show the whole entry with what the skill adds beside it, and one sentence of its meaning in the
   human's language. Write it on your recommendation; ask before writing only where you have no
   recommendation or the entry would change the meaning of an approved decision beyond what the
   approved task document or plan carries (WAY-30). The human accepts the meaning at the merge,
   or at the readiness gate for a projected entry (WAY-114).
3. Write the entry in its place in the file and run `elements/common/foundation_check.py` with
   `python -B` from the product's repository root. Fix what the entry broke and run it again; an
   error the entry did not cause goes to the human.
4. What follows from the entry goes through these steps one at a time, each through the skill of
   its element
   (`TODO — decision pending: which decision sets that the entries following from one entry are
   written one at a time`): every entry that names this one, when its binding part changes
   (WAY-02, WAY-33); every link the entry names that the foundation does not
   hold yet (WAY-17); and each finding of step 2. The skill names what follows in its element.

## Projected mode

A project definition projects entries of the foundation before the project is broken into tasks.
The skill `find-foundation-entries`, or `define-project` at the readiness gate, hands an entry to
the skill of its element in projected mode, naming the definition. The steps above run with these
differences, and each element's skill adds its own
(WAY-117):

- Step 1: select and read the product's foundation where it exists by "Reading the foundation";
  ask about no file to start and write no part map first — nothing is written into `foundations/`.
- Step 2: no search of the whole foundation runs for the entry: `define-project` searches it once
  for the whole definition at the readiness gate (WAY-118). What the element's skill adds within its
  own file — a search of that file for the same question, entry or part — still applies; what it
  adds to the search of the whole foundation runs in the search at the gate.
- Step 4.2: prepare the whole entry and one sentence of its meaning, but do not ask for acceptance
  before writing the proposal into the definition. Candidate selection accepts what is worth
  projecting, not the proposal's meaning. The readiness gate shows each projected entry's meaning
  sentence with the entry beside it and approves the meaning (WAY-114).
- Step 4.3: write the entry under "Projected foundation changes" of the definition, in the
  subsection of its kind and with the heading `project-level/definition_template.md` gives,
  followed by its meaning sentence; write nothing into `foundations/`. Run no foundation check, and
  tell the human that no script checked the entry: the check runs in the task that writes the entry
  into the foundation.
- Step 4.4: what follows from the entry is another projected entry, or, where it cannot be written
  before the code exists, an open question of the definition with its place of resolution. Where
  `find-foundation-entries` called the skill, report what follows to it, which adds it to its
  table, and write nothing; otherwise write it through the skill of its element in projected
  mode. What a skill hands to other agents after step 4.4, such as a check, waits for the task that
  writes the entry.
- In every step, a skill this one hands to runs in projected mode on the same definition, and no
  step writes into `foundations/`: neither an entry nor a row of a list or a scale the element's
  file holds. Such a row is an open question of the definition, `— resolved in: breakdown`.
