# The way of working the skills share

This file holds, once, the steps every element's skill takes to write an entry (WAY-35). Each rule
of an entry stands in its element's template or in `rules.md` beside this file; a skill holds only
the way of working particular to its element, and adds it to the steps below at the places it
names (WAY-35). A fix to a rule goes to the template or to `rules.md`, with the decision that sets
it; in the decisions element, a rule changes only with a decision in the log (WAY-35, WAY-05).

Paths under `elements/` below are those of the-way at the commit the product pins (WAY-34); in
the-way itself, those of the checkout or worktree the session works in.

## Critique before collective review

When an agent has finished a set of proposals that the human will review together, one fresh
agent critiques the complete set before it is shown. This includes entries added as consequences
of earlier proposals. The agent follows `elements/common/critique/SKILL.md` for the critique and for
an independently requested critique (WAY-120). A change to an invariant test
or to the foundation is assessed by the same skill (WAY-10, WAY-120).

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

Use this method for the current foundation of the repository being worked on (WAY-150). Start
from the task, source, proposed entry or project scope, and read the complete part map: its
responsibilities, file assignments, dependencies, critical flows, surfaces, boundaries and the
common rules and scales its entries use.

1. Name the touched parts. For changed files, use the map's assignment rules; for a file
   collecting entries about several parts, use the entries the work changes (WAY-44). Before a
   diff exists, map proposed behaviour, responsibilities, integrations, flows and surfaces to
   existing parts, including any responsibility or promise the work changes. Record a prospective
   new part as such, not as an existing map entry. Uncertain ownership expands the candidate parts
   and reading; an empty diff does not mean no affected parts.
2. Inspect the complete decision log's current *Scope* fields, wrapped values included, using
   the latest version of each decision and respecting repeals. Select every decision whose
   *Scope* names any touched part, and every decision the work or its source explicitly names
   (WAY-21). Read each selected entry whole, with all fields, rationale and *Rejected*: a search
   hit or binding sentence locates an entry, never replaces it. Missing or malformed *Scope*
   data is a finding to resolve, never a reason to silently omit an entry.
3. Expand to whole linked entries needed to understand, apply or verify those rules: governing
   *Relations*, *Based on* facts, *Verification* invariants, invariants' *Derives from* and
   *Rests on*, and relevant map entries. Inspect current invariant *Part* fields across the
   file, including `every`; select the invariants the work reaches under WAY-62, methods naming
   a changed file and invariants of relevant critical flows. When changing an entry or deciding
   its impact, search for incoming dependents: links stand at the dependent end (WAY-17,
   WAY-31). Follow them as far as their meaning or validity affects the work; unrelated branches
   need not all be loaded.
4. Inspect the terms and *Avoid* spellings of the product's glossary where it exists and, in a
   product other than the-way, of the-way's glossary at the pinned commit. Read whole entries for
   terms used in the work and selected material, and meanings a draft may introduce or confuse
   (WAY-95, WAY-97). Keep the mandatory whole templates, rules and examples of step 1, complete
   entries named as examples included.
5. Search all five foundation elements for the behaviour, rules, concepts and consequences the
   work concerns, using alternative vocabulary as well as identifiers. A relevant topic,
   candidate duplicate, unclear meaning, changed dependency, unknown owner or search finding
   expands the selection. A required whole-foundation search keeps its entire domain and timing
   under WAY-33, WAY-37 or the readiness gate, beyond known links and selected parts. Read every
   finding whole and settle it as that search's rule requires.
6. In the workflow's existing working record or handoff, keep the foundation revision, touched
   parts, expected current *Scope* matches and selected decision identifiers with source
   locations. Distinguish entries read from entries merely discovered. Compare the selected
   identifiers with the expected matches from the complete current *Scope* inspection and
   resolve every missing match before relying on the selection. Use existing scripts or an
   exhaustive direct inspection; no new index is needed. Recheck when the work's scope or current
   foundation changes. Uncertain relevance calls for additional reading, up to a whole file
   where that is the smallest reliable way to resolve it.

Selection is no token cap and does not forbid reading a small file whole. A handoff can name
reading units, but each receiving stage checks its inputs and reads whole entries it relies on.
The comparison records the declared set and evidence of reading; it proves neither understanding
nor completeness of semantic collision discovery. `decisions-found-for-change` still has
`Method: TODO`; Scope-name and fingerprint guards are partial checks, not a pass of that method
or of the full gate. Keep the WAY-33 search record as separate evidence.

## 2. Search the foundation

Once the skill has settled what the entry is, search the whole foundation for entries it touches
that no written link joins to it — not only those a link, a shared *Scope* or a shared *Part*
leads to (WAY-33). Read each entry whole: a decision's *Rejected* holds an option already weighed
and refused, and nowhere else says so
(`TODO — decision pending: which decision sets that the search reads a decision's *Rejected*`).
The search also asks:

- whether the entry uses a glossary term in another meaning than its entry gives, or spells out a
  term's definition instead of using the term: a paraphrase is rewritten to the term, and another
  meaning, or a word the glossary does not yet settle, goes through `record-glossary-term`
  (WAY-33, WAY-97, WAY-99);
- whether the change brings what entries of the foundation wait for — an element's template, the
  part map, a script; each such entry is fixed in the same change (WAY-37).

Each finding becomes a link the element's template gives, a change to one of the entries, or a
question in step 4, before the entry is accepted (WAY-33). The skill names what else the search
looks for in its element. Repeat the search against the current main branch before merging the
task branch, and keep the records of both searches with the change (WAY-33).

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
   recommendation or the entry would change the meaning of an approved decision. The human accepts
   the meaning at the merge, or at the readiness gate for a projected entry (WAY-114).
3. Write the entry in its place in the file and run the element's format guard (WAY-09) from the
   product's repository root, `python -B <the element's directory>/format_guard.py`, with the
   arguments its `--help` gives for this file and for the commit the task branch left the main
   branch from, or for no main branch
   (`TODO — decision pending: which decision sets that the skill runs the format guard on the file
   it writes`). Fix what the entry broke and run it again; an error or a warning elsewhere in the
   file goes to the human. Of the report's `unchecked:` lines, those that a `none` given to an
   option leaves — the text after the dash begins with that option and `none` — go to the human
   once per run of the guard, as their number, and every other `unchecked:` line goes to the human
   on its own
   (`TODO — decision pending: which decision sets how the unchecked lines of a guard's report reach
   the human`).
4. What follows from the entry goes through these steps one at a time, each through the skill of
   its element
   (`TODO — decision pending: which decision sets that the entries following from one entry are
   written one at a time`): every entry that names this one with its fingerprint, when its binding
   part changes (WAY-31, WAY-90); every link the entry names that the foundation does not
   hold yet (WAY-17); and each finding of step 2. The skill names what follows in its element.

## Projected mode

A project definition projects entries of the foundation before the project is broken into tasks.
The skill `find-foundation-entries`, or `define-project` at the readiness gate, hands an entry to
the skill of its element in projected mode, naming the definition. The steps above run with these
differences, and each element's skill adds its own
(WAY-117):

- Step 1: select and read the product's foundation where it exists by "Reading the foundation";
  ask about no file to start and write no part map first — nothing is written into `foundations/`.
- Step 4.2: prepare the whole entry and one sentence of its meaning, but do not ask for acceptance
  before writing the proposal into the definition. Candidate selection accepts what is worth
  projecting, not the proposal's meaning. The readiness gate shows each projected entry's meaning
  sentence with the entry beside it and approves the meaning (WAY-114).
- Step 4.3: write the entry under "Projected foundation changes" of the definition, in the
  subsection of its kind and with the heading `project-level/definition_template.md` gives,
  followed by its meaning sentence; write nothing into `foundations/`. Run no format guard, and tell
  the human that no script checked the entry's form: the guard checks it in the task that writes
  the entry into the foundation.
- Step 4.4: what follows from the entry is another projected entry, or, where it cannot be written
  before the code exists, an open question of the definition with its place of resolution. Where
  `find-foundation-entries` called the skill, report what follows to it, which adds it to its
  table, and write nothing; otherwise write it through the skill of its element in projected
  mode. What a skill hands to other agents after step 4.4 — a check, a deliberate break, a review
  of uses — waits for the task that writes the entry.
- In every step, a skill this one hands to runs in projected mode on the same definition, and no
  step writes into `foundations/`: neither an entry nor a row of a list or a scale the element's
  file holds. Such a row is an open question of the definition, `— resolved in: breakdown`.
