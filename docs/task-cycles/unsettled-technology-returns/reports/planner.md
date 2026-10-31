# Report — planner

**Status:** done with concerns

- Plan: `.runs/task-cycles/unsettled-technology-returns/plan.md`
- Size report: `.runs/task-cycles/unsettled-technology-returns/plan-size.md`, final run; every slice
  fits, no slice unchecked
- Worktree: `C:/Storage/repos/the-way/.runs/worktrees/unsettled-technology-returns`, base `2dbf1e7`;
  no tracked file changed, no commit made (`git status --short` empty)

## The plan

| Slice | Goal | Files | Estimated tokens to read | Model |
|---|---|---|---|---|
| 1 | The technology step runs at a task document | 8 (two are path patterns) | 144670 | same |
| 2 | Refinement sends a reserved choice to the step | 7 | 98350 | cheaper |
| 3 | Orchestrated refinement carries a run | 4 | 94195 | cheaper |
| 4 | The stage agents return `reserved` | 5 | 104213 | cheaper |
| 5 | The orchestrator stops the cycle on a reserved choice | 5 | 112992 | same |
| 6 | A task comes back after the human closes the draft | 3 | 102141 | cheaper |

*Foundation entries* lists ten: three new decisions, one glossary term, six decisions changed in
place. No slice carries a risk, by the handoff's answers of step 4.

The division departs from the four seams the orchestrator saw: the cycle's seam is cut in two, stage
agents and orchestrator, and the return of a plan row stands as a slice of its own. The reasons stand
in the plan's *Choices*.

## Section 2: no open design choice

Reading the code and the tests showed none. Checked: each line the spec cites at the base
(`resolve_gaps.md:10-12` and `:17-18`, `find_settlements.md:21-22`, `carry_foundation.md:13-15`,
`design.md:15-16`, `task-cycle/skill/SKILL.md:186-188` and `:213-214`, `correction.md:15-17`,
`conversation_template.md:39-42`, `elements/decisions/template.md:59-67`,
`project-level/test_plan_state.py:297`, `plan_state.py:106-107`, `:409-410`, `:416-420`); that no test
reads a text the change alters except `project-level/test_plan_check.py:233`, which reads the table
headers of `project-level/plan/template.md`, which Slice 6 leaves alone; that `project-level/test_plan_state.py`
cites no invariant, so its new test alters no invariant test; that the new files fall under
`project-level/**` and `task-cycle/**` of the part map.

## Concerns

1. **A file beyond the spec's table.** Slice 5 changes `task-cycle/skill/planning.md`, which the
   spec's table of pointers does not list. Its sentence at lines 10–11 sends what a planner returns to
   step 6, and a reserved choice is also an open design choice by the glossary, so that sentence could
   take a planner's `reserved` to a spec. The change is therefore 29 files plus the entry points, not
   the handoff's "about 28". It is recorded under *Choices* as a way of making what is settled, not a
   new choice. Proposed answer if you disagree: take it out of Slice 5's *Change* and *Goal*; the
   status list of `task-cycle/skill/SKILL.md` then carries the route alone.
2. **The volume of *Read*.** Each slice names every decision whose *Scope* names a touched part, with
   the invariants of that part or of `every`, as "Reading the foundation" selects and WAY-150 requires;
   the handoff's sixteen identifiers are all included where they bear. That is 94k to 145k estimated
   tokens per slice, in line with the plan of `testing-guidelines` (commit `4b2cdb4`, 53k to 153k) and
   far above the plan of `task-cycle-skills-shape` (commit `eeb5b34`), which named few entries. The
   size script passes them; a cheaper agent still reads about 60k of decisions for a change of prose.
   You check *Read* at the plan's review and may decide otherwise.
3. **Files named without backticks in *Read*.** `task_run.md` and `reserved_choices.md` do not exist at
   the base, so Slices 2 to 5 name them as what the earlier slice makes, with no backticks, as the
   script would leave a missing path unchecked. Their size is not in the report, and you add their
   paths at the slice's handoff.
4. **Weak checks on prose.** Slices 1 to 5 change text that instructs agents, which `make-change`
   does not test. Their *Checks* run the tests of the part and show that pointers stand and that
   unchanged files stayed unchanged; none shows that an agent acts on the text. The review of the whole
   change carries that judgment.
5. **`task-cycle/spec/SKILL.md`** stands in Slice 4's *Change* though the spec leaves to the maker
   whether it changes; a slice that leaves it alone is no mismatch, and its *Goal* says so.
6. **Forward references during the slices.** Slice 1's step 0 sends a note to `refine-task`, whose route
   for it exists only after Slice 2, and Slice 1 speaks of the rule through the glossary term because
   `reserved_choices.md` comes in Slice 2. Each is true once the change is whole.

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-03 and WAY-08, whole, to judge whether the new test of Slice 6 is an
  invariant test; WAY-142 and WAY-150, whole, for the states of a plan and for what *Read* has to name.
- `foundations/invariants.md`, the entries `return-step-record`, `derived-file-content`,
  `skill-rule-source`, `repository-file-location`, `element-directory-contents`, `generated-overview`,
  `project-technology-record`, `project-plan-form`, `project-plan-check`, `skill-entry-points`,
  `project-plan-state-evidence`, to see what the slices reach.
- `foundations/part_map.md`, the entries `decisions`, `glossary`, `project-level`, `task-cycle`,
  `agent-instructions`, and `foundations/glossary.md`, the entry `open design choice`, to place the new
  files and the term.
- `elements/decisions/skill/projected.md` and `project-level/definition_template.md:146-244`, for what
  stays true of a run at a definition.
- The history of `docs/task-cycles/*/plan.md` at `eeb5b34` and `4b2cdb4`, for how earlier plans name
  *Read*.

## Guidelines and the order of work

The-way has no directory `guidelines/`, so no guideline file applies and none is missing or uncertain.
No styleguide applies, so the order of the slices has no relation to its example.

## Checks

Each ran on the unchanged base, to show the command can actually run:

- `python -B task-cycle/slice_size.py .runs/task-cycles/unsettled-technology-returns/plan.md` — exit 0
- `python -B elements/common/foundation_check.py .` — exit 0, 0 errors
- `python -B agent-instructions/skill_entry_points.py` — exit 0, `entry points are current`
- `python -B instruction-files/check_instructions.py . --file project-level/technology/SKILL.md` —
  exit 0, 0 errors, 1 warning of the base
- `python -B gate/run_tests.py agent-instructions` — OK, about 6 s
- `python -B gate/run_tests.py gate` — OK, about 6 s
- `python -B gate/run_tests.py task-cycle` — OK, about 1 s
- `python -B gate/run_tests.py project-level` — exit 0, about 2 min
- `python -B -m unittest discover -s project-level -p "test_plan_state.py"` — OK, about 80 s
- `git grep -l -i "child-work request" -- project-level/task/skill/orchestrated_mode.md project-level/lead/conversation_template.md project-level/lead/answering.md`
  — lists two of the three at the base, as Slice 3's check expects before its change

Not run: the gate, which is yours (WAY-160); Slice 4's, Slice 5's and Slice 2's `git grep` checks and
the `--file` runs on files that do not exist yet; the `git diff --exit-code` checks, which need a
slice's base.

## Searches not found or unclear

- `git log --diff-filter=A -- 'docs/task-cycles/*/plan.md'` returned nothing, and so did the same
  search for `cycle.md`, a false "none": records added and removed on a merged branch are dropped by
  history simplification. With `--full-history` they appear. Noted for whoever searches records next.
- The handoff counts "about 28 files"; the plan counts 29 plus the entry points, for the reason of
  concern 1.
- `task.md:97` gives an act after the merge, moving a line of the private note `mapa_pakietu_10x.md`
  to the number of row 2's decision. It belongs to a later session, so no slice covers it; it stands
  here so it is not lost.

## Questions still open

None. Concern 1 holds the one decision you may want to reverse, with its proposed answer.
