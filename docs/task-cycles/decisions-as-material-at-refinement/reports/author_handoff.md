# Handoff — the one author of the whole change

Stage: make the whole change as the one author (the row "the whole change as the one author" of
`task-cycle/change/SKILL.md`), including the foundation step.

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator, who
delegates to you the choices of how to make what the task and the foundation settle. Nothing you
decide is the human's approval. Ask no human anything: a question goes back to the orchestrator as
your status `questions`; an open design choice the task, the foundation and your reading leave open
goes back as `returned` with no code (WAY-135).

## Where you work

- Worktree (work from its root, change nothing elsewhere):
  `the root of the task's worktree`
- Branch `task/decisions-as-material-at-refinement`, base commit
  `354d37d56403b6f898155cb706efcb74f316c97a` (`foundations`). The-way is the product here: the
  pinned the-way is this worktree. Skills of the-way are read from the worktree (`task-cycle/...`,
  `elements/...`, `project-level/...`), never from another checkout.
- Report: write it to
  `docs/task-cycles/decisions-as-material-at-refinement/reports/author_report.md`
  as `task-cycle/change/SKILL.md` gives. Return the short result: status, commits, a one-line check
  result and the report's path.

## Method and what to read

- Method: `task-cycle/change/SKILL.md` (read whole), its row "the whole change as the one author".
  The foundation step: `task-cycle/skill/foundation_step.md` (read whole). The return step is a
  separate dispatch later; you do not take it.
- The frozen task, whole (the task is in Polish; write the files of the-way in English):
  `docs/task-cycles/decisions-as-material-at-refinement/task.md`, in the worktree. No spec, no plan:
  the orchestrator judged that the task leaves no open design choice and that one agent holds it.
- Answers of step 4 of the cycle: no trust boundary touched, no irreversible operation, no
  reserved choice.
- Foundation entries to read, each whole (a `###` heading of `foundations/decisions.md` to the next):
  - the task's *Decisions in play*: WAY-14, WAY-30, WAY-113, WAY-115, WAY-118, WAY-124, WAY-134,
    WAY-165, WAY-267;
  - cited by the files you change and bearing on them: WAY-33, WAY-114, WAY-121, WAY-123, WAY-126,
    WAY-139, WAY-140, WAY-154, WAY-166, WAY-270, WAY-25.
- Entries your foundation step writes go through the pinned element skill: `the-way-record-decision`
  (`elements/decisions/...`, found from the skill), for a decision it reads `elements/common/way_of_working.md`
  and `elements/common/rules.md` as that skill gives. Edit an existing decision in place (WAY-07,
  `agent-instructions/README.md`).
- There are no guidelines of the-way for coding or testing (no test in the-way checks the wording of
  these places, per the task's *Context*): the change is Markdown only.

## What to make

Make the six points of the task's *To do* and satisfy its *Acceptance criteria*, with the five
answers of *Questions to settle* as binding. The task's *Context* lists the places that carry the
binding at the commit `a3206c1`; `foundations` has moved to `354d37d`, so re-read each place on the
branch and edit what stands there now. Known drift (orchestrator's finding, row Q1 of its record):
the technology step now shows choices "in one message, one choice after another" (WAY-123), no
longer "in one table"; where the task says "tabela porównania" / "table" of the technology step,
the carrier is that message. Do not bring the "table" wording back.

Rows 1–5 of the task's *Settlements to record* are accepted and the foundation step writes each as a
decision of the-way's log through the element skill, marked `row <n>` in your report; the search of
the whole foundation (WAY-33) is yours: decide which of the rows already stand in an existing entry
(tie the row to it instead of a second entry) and correct every entry the change makes untrue in
the same change, the decisions of point 5 of *To do* included.

Places found by the orchestrator beyond the task's list, for you to judge in your WAY-33 search
(each may or may not need a change; name your ruling in the report):
- `project-level/task/skill/SKILL.md`, `project-level/task/template.md`,
  `project-level/lead/skill/SKILL.md`, `product-guidelines/audit_end.md` (all mention the question
  against an answer or "question against");
- `project-level/technology/start.md` and `project-level/technology/SKILL.md` (cite WAY-165 and the
  choice a decision holds);
- `project-level/task/skill/SKILL.md` and `project-level/task/skill/orchestrated_mode.md`
  (carry the same boundary for a task refined by an agent of a lead).

The task *Context* notes a sibling task, `the sibling task's note in the author's backlog`
(`ready for cycle`), whose point 17 rewords the same sentence of WAY-165; it is not merged on this
branch, so edit the wording as it stands on this branch.

## Boundaries

- Keep inside the task: nothing outside its six points, and nothing in the cycle (`task-cycle/`)
  beyond what point 6 needs to say "luźniejsze reguły obowiązują tylko przed startem cyklu".
  Point 6 requires the decisions and files of points 1–4 to say that their looser rules hold only
  before the cycle starts; the agent of the cycle still returns with a question as WAY-30 gives.
- Do not run the full gate (`python -B gate/run_tests.py` without an argument): the orchestrator
  runs it. Run `python -B elements/common/foundation_check.py` after your foundation edits, and the
  focused directories your edits can affect (for instance `python -B gate/run_tests.py
  project-level` and `elements/common`, and any directory whose tests read the files you change),
  and report each check with its command and exit code.
- A change that alters a skill's `description` runs `python -B agent-instructions/skill_entry_points.py
  --write`; none is expected here.
- Stage with `git add <path> ...` by path, never `-A`/`.`. Commit messages in English, imperative,
  like the history of the repository. Commit on the task branch; leave the worktree clean.
- Do not write the record `.runs/task-cycles/...` into a commit; it is ignored.
- Your report must hold the own-work check, the weakest-point check, **Searches not found or
  unclear** (each thing looked for and not found, or `none`), each reach beyond this handoff, one
  sentence of meaning in English and one in Polish for each foundation entry written, and for each
  entry its mark (`row <n>`, `projected`, `the cycle's`).
