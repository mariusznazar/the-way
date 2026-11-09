# Handoff — planner

You are the planner of a the-way task cycle. The person who requested the cycle delegated its
intermediate choices to the orchestrator; no choice here is the human's approval, and you never ask
the human — questions go back to the orchestrator.

- Worktree (work only from its root): `the task's worktree root`
  (branch `task/cycle-technology-decisions-batch`, base `f238e4ffdfc2396ae0009fefa90b3af8d1e931e1`, target `foundations`). This is the-way itself; there is no pinned process.
- Your method: read `task-cycle/plan/SKILL.md` in full (the project skill `the-way-plan-task`). Read
  `task-cycle/plan/too_large.md` and any other file it names only when the step that names it comes.
- Stage and boundary: write the plan only. Write no code, no test, no foundation entry.
- Frozen task (read whole): `.runs/task-cycles/cycle-technology-decisions-batch/task.md` (written in Polish; its
  section *To do* holds 30 items; *Settlements to record* holds 5 rows; *Questions to settle* holds 6
  answered questions; *Decisions in play* quotes the decisions it touches). No spec exists.
- Plan path: `.runs/task-cycles/cycle-technology-decisions-batch/plan.md`; size report:
  `.runs/task-cycles/cycle-technology-decisions-batch/plan-size.md`.
- Report path: `.runs/task-cycles/cycle-technology-decisions-batch/reports/01-planner-report.md`.
- Answers of step 4 of the cycle (to carry into the plan's *Risk* marks): trust boundary — **yes**:
  `project-level/plan_state.py` is named as a trust boundary by `foundations/part_map.md` (part
  `project-level`) and task item 7 changes it, so the slice(s) that touch it are marked as touching a
  trust boundary and get a review of their own; irreversible operation — **no**. No other file the task
  touches is a trust boundary.
- No open design choice and no reserved choice were found at the start (cycle record). If you find
  one, write no plan and return it, as your method gives.
- Process rules that bind the plan:
  - The task's items cite line numbers from `foundations` `a3206c1` and `f218b55`; the worktree is at
    `f238e4f`. The task says "cykl szuka miejsca po treści" — find each place by its content and give
    current line ranges in the slices.
  - `agent-instructions/README.md` (read it): the whole test run is `python -B gate/run_tests.py`,
    about 16 minutes, run by the orchestrator only; slices name focused checks
    (`python -B gate/run_tests.py <directory>` or a single test file) and never the gate. A change to
    `gate/run_tests.py` is not planned here.
  - A change that adds, renames or moves a skill, or changes a skill's description, runs
    `python -B agent-instructions/skill_entry_points.py --write` and commits what it writes. Item 14
    renames one of two `settle.md` files — check whether any skill description or entry point is
    affected.
  - Once a foundation entry is written or reworded, the change searches the whole foundation once for
    entries it touches and corrects them (WAY-33); decisions are edited in place (WAY-07). The task's
    *Settlements to record* rows 1–5 are decisions the cycle writes (foundation entries): put them in
    the plan's *Foundation entries* section as `task-cycle/plan/SKILL.md` gives, and leave to the
    slices the rest. Items 17–24 reword accepted decisions; the task's *Context* says acceptance of the
    document accepts those changes (WAY-30).
  - Point 8 sub-point on `remarks_check.py` and point 7 on `plan_state.py` change scripts: their
    slices include the tests named in the task (`test_remarks_check.py`, a test for `plan_state`
    behaviour as it exists in the repository) and a focused check of that directory. Point 9 changes
    `installation/test_install.py`.
  - the-way has no `guidelines/` directory (task question 6): there are no product guidelines to
    read; say so in your report rather than treating it as a finding to resolve.
- What to read besides the frozen task, by identifier (read each decision whole, from its heading in
  `foundations/decisions.md` to the next `###`): all decisions of the task's *Decisions in play*
  (WAY-05, WAY-09, WAY-13, WAY-80, WAY-113, WAY-121, WAY-128, WAY-139, WAY-148, WAY-165, WAY-166,
  WAY-259, WAY-267, WAY-270, WAY-287, WAY-291, WAY-292, WAY-293, WAY-294, WAY-295, WAY-298, WAY-306),
  and WAY-135, WAY-136, WAY-150, WAY-229 for how the cycle slices; the part map `foundations/part_map.md`
  whole (to name the parts of each slice's files); `foundations/glossary.md` whole. For the invariants
  that a slice reaches, search `foundations/invariants.md` by the part's identifier on `- **Part:**`
  lines and by the line `invariant: <identifier>` in the tests the slices alter. Name each reach in
  your report.
- Grouping hint (yours to override): items fall into families — task-cycle skill/prose and scripts
  (1–9), technology step (10–16, including settlements 1–3), decision wording (17–24, settlement 4),
  task template / find-foundation-entries / README / instruction-files / part map (25–29), the
  refinement read-sources sentence (30). Settlement 5 (rule for report names) stands with item 8. A
  slice should not mix families that need different reading; cut to the size script's limits.

Return the status, the plan path, a one-line check result (naming what failed or did not run — the
size script is your only check), and the report path. The report must hold **Searches not found or
unclear** (each thing looked for and not found or unclear, or `none`), your reaches beyond this
handoff, and the size script's command and exit code.
