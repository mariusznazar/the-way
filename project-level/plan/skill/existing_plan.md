# Work on an existing plan

Run `python -B <the-way>/project-level/plan_check.py <plan>` on the original whole file and read it
by `reading_definition_and_plan.md` beside this skill (WAY-151).

- A plan whose status reads `draft` goes on from the first step its sections leave unfinished; a
  plan handed over changes only as its change log records, and a finding that the definition's
  fingerprint no longer matches means the definition changed after its gate: it goes through
  `define-project` step 7 again, and the plan is checked against it from step 1.
- If the definition has already passed that new gate, verify its approval and proceed with that
  recheck rather than reopen the same gate.
- A finding that two tasks realize one entry with no order between them is settled as step 3 gives
  it (`assign_entries.md` beside this skill), each item letting them go side by side shown to the
  human as step 7 gives it (`hand_over.md` beside this skill) (WAY-230).
- Whichever step the plan goes on from, a session that has not read `read.md` beside this skill
  (step 1) yet reads it before it goes on.
