# Assign the projected entries

- Give every projected entry of the definition its row: the tasks whose work makes it true, and
  the one of them that writes it into the foundation (WAY-142, WAY-126).
- An entry no task of the cut makes true shows a task missing or an entry the project does not
  need; either is a question for the human in step 5, never an entry left without a row.
- Two tasks that realize the same entry go one after the other: make one depend on the other,
  unless one already does, directly or through other tasks. Where the two make parts of the entry
  true that do not touch, let them go side by side instead with a change log item
  `- YYYY-MM-DD — side by side: tasks <n>, <m> on "<entry>" — <why>`, the reason saying why their
  work does not collide; "neither depends on the other" is no reason. A pair with a task done,
  delivered or dropped needs neither (WAY-230).
- A finding of `plan_check.py` that two tasks realize one entry with no order between them is
  settled by the bullet above, each item letting them go side by side shown to the human as
  step 7 gives it (`hand_over.md` beside this skill) (WAY-230).
