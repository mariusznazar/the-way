# Recognize

- Name the parts of the product's map that hold code, the scripts of its build included, however
  small (WAY-208). Before the first code, name the parts the product's plan gives that code; where
  the map holds no part for it yet, its identifier is a question of the task, and *To do* gains
  adding that part, with the files the task creates, through `update-part-map`.
- Read the product's root `AGENTS.md` whole, of which `refine-task` read only the section
  `## Backlog`, and every file under `guidelines/` that `refine-task` did not read at its step 1. Of
  the product's foundation, read — besides what `refine-task` selected at its step 1 — the
  decisions that settle the product's technology and every decision that already adopts a standing
  check, a set of rules or an exemplar, or departs from one (WAY-150).
- Find in the product's files what it has for that code — a linter, a formatter, an audit of
  dependencies, each with its configuration and version; kinds of code it already holds files of
  other than tests (WAY-231), such as endpoints, migrations or modules; or nothing — and whether it
  has coding guidelines. Say plainly when it has nothing (WAY-210).
- That gives the mode, and modes combine:
  - no code: the starting set of step 2, so that the general file with its standing checks comes
    into being before the first task that writes the product's code (WAY-209);
  - code and no coding guidelines: step 2, and the trial run and the audit of step 3;
  - a task that creates the first file of a kind of code: "A new kind" in step 3;
  - a kind of code whose files the product already has, with no row in the index of
    `guidelines/coding.md`, where that file stands, and the task neither refreshes nor extends the
    coding guidelines: "Kinds" of step 3 for that kind alone, with no step 2 and no trial run; where
    it combines with another mode, the wider mode governs (WAY-216);
  - existing coding guidelines, refreshed or extended: step 2, and step 3, which tries the set and
    audits each kind again.

A refresh updates or corrects accepted guidelines within the scope they already cover,
including adapting them to a new version of a tool the product uses. An extension covers something
new; its research checks whether to use what the product has or something else (WAY-251).
