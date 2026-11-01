# Cut the tasks

- Cut the definition's In scope into tasks, each ending with something that can be checked in the
  running product, never with a layer put in place (WAY-143). A large task is split; its size
  chooses nothing else (WAY-13).
- Bring a technical element in with the first task that uses it. Write a preparatory task only for
  work that task cannot start without, and make that task depend on it (WAY-143).
- Where the reading of the product's guidelines in step 1 found a styleguide, general coding file
  or testing guidelines missing or uncertain, or the approved scope has a task create the first
  file of a kind of code, work on a kind that has files but no entry in the guidelines index,
  make the first test of a level, or extend existing guidelines, read `guideline_tasks.md` beside
  this skill before the next bullet.
- Give each task its number, its name and its goal in the definition's language, the tasks it
  depends on and the items of In scope it delivers, as the template gives them (WAY-147, WAY-144).
  Every task of a new plan reads `to refine`.
- `Depends on` constrains cycle starts, not refinement: a cycle starts only when its dependencies
  are done, and cycles run beside one another only when neither depends on the other directly or
  transitively. Dependent tasks may be refined together; a refinement waits only for a named
  question needing another task's result (WAY-144).
- Something the definition leaves out that the cut seems to need is a question for the human in
  step 5 (WAY-145).
