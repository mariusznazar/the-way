# Recognize

- Name the parts of the product's map that have tests: the parts whose code its tests check and the
  parts that hold its test files (WAY-246, WAY-248). Before the first test, name the parts the
  product's plan gives tests; where the map holds no part for them yet, its identifier is a question
  of the task, and *To do* gains adding that part, with the files the task creates, through
  `update-part-map`.
- Read the product's root `AGENTS.md` whole, of which `refine-task` read only the section
  `## Backlog`, and every file under `guidelines/` that `refine-task` did not read at its step 1. Of
  the product's foundation, read — besides what `refine-task` selected at its step 1 — the
  decisions that settle the product's technology, every decision that already adopts a test tool, a
  level, an exemplar test or an exclusion, or departs from the testing template, and the trust
  boundaries its part map records (WAY-150, WAY-48).
- Find in the product's files what it has for those tests — a test tool, with its configuration and
  version; levels; directories of tests; doubles; tests of invariants; or nothing — and whether it
  has testing guidelines. Say plainly when it has nothing (WAY-248).
- That gives the mode, and modes combine:
  - no tests: the starting set of step 2, so that the testing guidelines come into being before the
    first task that writes the product's tests (WAY-244);
  - tests and no testing guidelines: step 2, and the audit of step 3;
  - a task whose required outcome is the first test of a level whose recipe already stands in
    `guidelines/testing.md` with an empty *Exemplar*: the new-level case of step 3, and no step 2;
    a level with no recipe yet is an extension (WAY-251), which takes step 2 as well;
  - existing testing guidelines, refreshed or extended: step 2, and step 3, which audits each level
    again.

A refresh updates or corrects accepted guidelines within the scope they already cover,
including adapting them to a new version of a tool the product uses. An extension covers something
new; its research checks whether to use what the product has or something else (WAY-251).
