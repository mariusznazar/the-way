# Projected mode

A project definition projects entries of the foundation before the project is broken into tasks.
The skill `find-foundation-entries`, or `define-project` at the readiness gate, hands an entry to
the skill of its element in projected mode, naming the definition. The steps of `way_of_working.md` run with these
differences, and each element's skill adds its own
(WAY-117):

- Step 1: select and read the product's foundation where it exists by "Reading the foundation" in `way_of_working.md`;
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
