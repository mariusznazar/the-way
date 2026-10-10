### Slice 3 — task cycle never makes an effect outside the repository itself

- **Goal:** `implement-task` states WAY-140: lines 15–21 add the human action in the cycle beside
  the decision reserved to a human; step 1 requires every human action the task document places
  before the cycle to be done (WAY-124); the paragraph at line 46 keeps writes to the repository
  and allows reads outside it; step 4 (lines 63–69) replaces "when the product's rules reserve its
  authorization" with WAY-140's rule — the cycle prepares what the repository allows and returns a
  blocked draft request listing the actions in the cycle, and an effect the document does not name
  goes into that list for the human to place; steps 12–13 keep that request a draft and list the
  actions in it; `task-cycle/record_template.md`'s *Request handoff* gains the line for the human
  actions the request waits for.
- **Change:** `task-cycle/skill/SKILL.md` · `task-cycle/record_template.md`
- **Read:** `project-level/task/template.md` · `foundations/decisions.md:3538-3622` ·
  `foundations/decisions.md:3942-3989`, and the entry WAY-140 the foundation step appends at the
  end of the decision log
- **Checks:** `python -B gate/run_tests.py task-cycle` · `python -B gate/run_tests.py gate` ·
  `python -B agent-instructions/skill_entry_points.py`; no script's behaviour changes, so no test
  is written first
- **Depends on:** Slice 2 · WAY-140 · WAY-124 edit

