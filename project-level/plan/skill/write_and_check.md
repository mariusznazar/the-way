# Write, check and ask

In a turn dispatched through a refinement conversation path, ask nothing of the human yourself:
each question below goes through the conversation, as `delegated_mode.md` beside this skill gives.

- Write the plan in the definition's directory with the status `draft`, the fingerprint
  `python -B <the-way>/project-level/readiness_check.py <definition> --fingerprint` prints, and the
  first line of its change log. Give its full path in the same message.
- Run `python -B <the-way>/project-level/plan_check.py <plan>` and fix each finding; it must report
  nothing before the critique.
- Ask the human, in one round, what steps 2–4 left for the human: questions that arose in the
  breakdown, moves that change which task writes an entry, a task or an entry the definition leaves
  unsettled. Write each answer into the plan, with its line in the change log where it changes the
  plan, before the next question. What steps 2–4 send here:
  - from step 2: something the definition leaves out that the cut seems to need, and questions
    or work beyond the approved definition that its guidelines tasks raise, which are never
    silently enlarged into the plan (WAY-145);
  - from step 3: an entry no task of the cut makes true, which shows a task missing or an entry
    the project does not need, never an entry left without a row;
  - from step 4: a move that changes which task writes a projected entry, and a question that
    arises only in the breakdown, which stands with `— definition: none` once answered or placed
    (WAY-145).
