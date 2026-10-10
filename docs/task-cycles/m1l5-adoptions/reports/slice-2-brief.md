### Slice 2 — task refinement names human actions and checks the deployment skill

- **Goal:** `project-level/task/template.md` gives the task document a section, always present
  (`none` where the task has no effect outside the repository), that names each human action with
  its placement — before the cycle, with whether it is done, or in the cycle — and its rule under
  "What each section carries" (WAY-140, WAY-124), and says that a document written before the
  section existed names none; `refine-task` names each effect outside the repository as a human
  action, proposes its placement by WAY-140's rule and has the human place each; for a task whose
  outcome deploys the product or changes how and where it runs, checks the product's deployment
  skill against WAY-139's list and adds the item or offers the split; and its step 6 check requires
  every action placed and every action before the cycle done before `Status: ready for cycle`.
- **Change:** `project-level/task/template.md` · `project-level/task/skill/SKILL.md`
- **Read:** `foundations/decisions.md:3538-3622` · `foundations/decisions.md:3942-3989` ·
  `elements/common/way_of_working.md:1-60` · `.runs/task-cycles/m1l5-adoptions/frozen_task.md`,
  and the entries WAY-139 and WAY-140 the foundation step appends at the end of the decision log
- **Checks:** `python -B gate/run_tests.py project-level` · `python -B gate/run_tests.py gate` ·
  `python -B agent-instructions/skill_entry_points.py`; no script's behaviour changes, so no test
  is written first
- **Depends on:** WAY-139 · WAY-140 · WAY-124 edit

