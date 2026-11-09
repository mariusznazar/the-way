# Handoff — foundation entries (the foundation step of the plan)

The person who requested this cycle delegated its intermediate choices to the orchestrator; no
answer here is that person's approval. You never ask the human: a question goes back to the
orchestrator in your report.

- Worktree (work only from its root): `the task's worktree root`,
  branch `task/cycle-technology-decisions-batch`, base (and slice 1's base) `f238e4ffdfc2396ae0009fefa90b3af8d1e931e1`.
  This is the-way itself; no pinned process.
- Your method and variant: `make-change` — read `task-cycle/change/SKILL.md` whole. You are
  **the agent of the plan's *Foundation entries***: you take no row of its variants table. Read
  `task-cycle/skill/foundation_step.md` whole (it governs what you write and what your report keeps);
  each element's skill when you write an entry of that element (here the decisions element,
  `elements/decisions/skill/`), and `agent-instructions/README.md`.
- Stage and boundary: write only the foundation entries below, in `foundations/decisions.md`, in
  commits on the task branch. No other file is changed. Do not run `python -B gate/run_tests.py` (no
  full run); run `python -B elements/common/foundation_check.py --skip-test-citations` and the
  focused checks that the entries call for.
- Frozen task (read whole): `.runs/task-cycles/cycle-technology-decisions-batch/task.md` (Polish). Plan (read
  its *Foundation entries* section whole and the *Choices*): `.runs/task-cycles/cycle-technology-decisions-batch/plan.md`.
  No spec.
- Answers of step 4: trust boundary — yes (`project-level/plan_state.py`, not touched by you);
  irreversible operation — no.
- The entries to write (12): rows 1–5 of the task's *Settlements to record* and items 17–23 of *To do*
  (item 24 is row 4). Each is described, in the plan's table, by one sentence of the change; the
  words of the entry are yours (WAY-134). For rows 1–5, the settlement is the row's; whether a row
  becomes a new decision or an edit in place of WAY-121, WAY-139, WAY-148, WAY-165, WAY-166 or WAY-294
  is for you to judge by the search of the whole foundation (WAY-33, WAY-07) — a row whose settlement the
  search finds already stated becomes no second entry; tie it and say so. Items 17–23 are rewordings
  in place, accepted with the document (WAY-30).
- **Drift:** the task's line numbers come from `a3206c1`; the base is 46 commits later. Find each place
  by content. Where the current text of a decision already says what an item asks (the planner saw
  that the current WAY-165 may no longer carry "opens only on the human's word"), change nothing there
  and say so in your report.
- Foundation to read, by identifier, each whole from its heading to the next `###`: WAY-05, WAY-09,
  WAY-121, WAY-128, WAY-139, WAY-148, WAY-165, WAY-166, WAY-259, WAY-267, WAY-270, WAY-287, WAY-291,
  WAY-292, WAY-293, WAY-294, WAY-295, WAY-296, WAY-298, WAY-306, WAY-113, WAY-123, WAY-134, WAY-30, WAY-33,
  WAY-07; the glossary whole; the invariants whose *Part* names `task-cycle`, `project-level` or `every`
  — search `foundations/invariants.md` by `- **Part:**`; the part map whole; the decisions template
  `elements/decisions/template.md` and `elements/decisions/examples.md` whole. Name each reach beyond
  this list in your report.
- Writing rules to keep in mind: WAY-05 (rationale and rejected options in prose; for an entry you
  write yourself rather than quote, no file, script or count, and no description of what the process's
  tools do or lack today; no account of how the decision was reached), the template's fields, and
  `foundation_check.py` must exit 0. Item 21 changes WAY-05's *Verification* into two
  `complies`/`violates` pairs. Item 22 changes WAY-293's *Rationale* (no description of what the
  request template does or lacks today) and its rejected way "no change, which withdraws the rule" (no
  change leaves the return step without a precedence). Item 23: the WAY-287 list names also a listing of
  the remarks check held wrong (WAY-295) and an error of the form check held wrong (WAY-291).
- Commit each entry or a small group of entries as its own commit(s); commit messages in English.
  Mark each commit's files with `git add <path>`, not `git add -A`.
- Your report (write it in full to
  `.runs/task-cycles/cycle-technology-decisions-batch/reports/02-foundation-entries-report.md`): for each entry
  one sentence of its meaning in English and one in Polish, marked `row <n>`, `item <n>` (these are
  the plan's entries; mark an entry no row and no projected entry carries whole as `the cycle's` — items
  17–23 are accepted with the document, so mark them `item <n>`), the commits, the check commands and
  exit codes, your own-work check as `task-cycle/change/SKILL.md` gives, **Searches not found or
  unclear** (each thing looked for and not found or unclear, or `none`), and your reaches beyond this
  handoff.

Return: status (`done`, `done with concerns`, `questions`, `returned`, `reserved` or `blocked`), your
commits, a one-line check result naming what failed or did not run, and the report path.
