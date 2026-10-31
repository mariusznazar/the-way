# Findings of the review of the reconciliation

Copied word for word from `reports/merge-review.md`, whose first line is `FAIL c69e355`. The reviewer's
grades and scope stand. Minor findings and those outside the scope are not fixed.

The three findings below have one cause and are kept apart because each is fixed in a different
`SKILL.md`. None comes from a slice in particular: the pointers were correct when reviewed, and WAY-265
did not stand on their base. No earlier review could have found them.

**Why these are Important.** WAY-263 is not the ground: this change neither writes nor changes
WAY-265. The ground is the general grade, a missed requirement, and the consequence for the change:

- WAY-265 binds a skill "rebuilt or changed according to WAY-256", and exempts only "a step's file
  that stands unchanged, with the variant file it points to". WAY-256 binds every fragment "a change
  to a skill of the-way adds or rewords", and each step file below is altered by this change, the
  pointer being its own line. So the exemption does not reach them. This change's own pointers are
  within the task: To do 5 and 7.
- Its *Verification* names the case as a breach: "the research file is named only in the second
  step's file, so an agent that read the skill's `SKILL.md` cannot see that the file exists." Its
  *Rejected* refuses this layout by name: "the variant named only in the step's file, as in a layout
  with two levels — the layout stays at odds with the rule of references one level deep, and the rule
  has to change or a reviewer reports it in every later skill".
- Merged as it stands, the request puts onto `foundations` files that breach a decision already there,
  and no check catches it: `foundation_check.py` passes and the entry's test is an agent's reading.
- What it protects here matters more than in most skills. The rule in `reserved_choices.md` is what
  tells a reserved choice from any other. An agent that does not reach it settles the choice silently,
  the failure this task exists to end, and the same consequence was graded Important in
  `reports/whole-review.md`, finding 2 ("does not reach the pointer and never reads
  `reserved_choices.md`").

The limit of that consequence, stated plainly: `reserved_choices.md` is 40 lines, so the partial read
of the fact `claude-skill-nested-references` (`head -100`) would still show it whole, and an agent
that reads the step's file whole does reach the pointer. What is missing is what WAY-265 requires:
that `SKILL.md` shows the file and its condition, so the step's file is not the only way to it.

#### 1. `refine-task` does not name the reserved rule or the run's file at the step that needs them

- **Place:** `project-level/task/skill/SKILL.md:38-42` (step 3) and `:16-20` (orchestrated mode), which
  this change left unchanged; the pointers stand at `project-level/task/skill/resolve_gaps.md:23-26`
  and `project-level/task/skill/orchestrated_mode.md:21-23`.
- **What is wrong:** `resolve_gaps.md:24-26` says `project-level/technology/reserved_choices.md` is one
  "which you read when the task's outcome needs a language, a framework, a library, a store of data, a
  way of logging in or a place to run that no decision, approved definition or accepted answer
  settles". That is the sentence shape of WAY-265's complying example, a step's file saying a file is
  read when something runs. But `SKILL.md` step 3 names only `resolve_gaps.md` and
  `guideline_findings.md`. Likewise, in orchestrated refinement, `orchestrated_mode.md:21-23` has the
  run "led through this file by `project-level/technology/task_run.md`", and the refiner runs no
  `settle-technology` of its own whose `SKILL.md` would name that file, while `SKILL.md:16-20` names only
  `orchestrated_mode.md`.
- **Why it matters:** refinement is the first place a reserved choice can be caught; the cycle is the
  later and dearer one (WAY-268). A session that read `SKILL.md` cannot see that the rule exists.
- **Evidence:** `git grep -n "reserved_choices\|task_run" HEAD -- project-level/task/skill/SKILL.md`
  finds nothing; `git diff --stat 2dbf1e7 HEAD -- project-level/task/skill/SKILL.md` is empty. The same
  skill's step 1, `SKILL.md:29-32`, shows the required form, naming `project_plan_task.md` and
  `source_only_task.md`, which `read_sources.md` points to, each with its condition.
- **What would close it:** step 3 names `project-level/technology/reserved_choices.md` with the
  condition `resolve_gaps.md` gives, and the orchestrated-mode section names `task_run.md` with its
  condition, a run of `settle-technology` in orchestrated refinement. The condition has to read the
  same in both places (WAY-265, *Rationale*: "a file named in two places that must be kept equal").

#### 2. `write-spec` does not name the reserved rule at its design step

- **Place:** `task-cycle/spec/SKILL.md:37-39` (step 2), which this change left unchanged; the pointer
  stands at `task-cycle/spec/design.md:18-21`.
- **What is wrong:** `design.md:18-21` reads "Where the design needs a language, a framework, a library,
  a store of data, a way of logging in or a place to run that the task and the foundation do not
  settle, read `project-level/technology/reserved_choices.md`". `SKILL.md` step 2 lists what `design.md`
  holds and names no such file. A skill in which `SKILL.md` names a file only by what a step's file does
  is the layout WAY-265 refuses.
- **Why it matters:** the designer is the agent that may otherwise settle the choice by a spec, against
  WAY-135. The three sister methods this change touched are right: `task-cycle/change/SKILL.md:101-102`,
  `task-cycle/plan/SKILL.md:65-66` and `task-cycle/review/SKILL.md:68-69` name the file in `SKILL.md`
  itself. `write-spec` is the one stage method that does not.
- **Evidence:** `git grep -n "reserved" HEAD -- task-cycle/spec/SKILL.md` finds nothing;
  `git diff --stat 2dbf1e7 HEAD -- task-cycle/spec/SKILL.md` is empty.
- **What would close it:** step 2 names the file with `design.md`'s condition, in the same two-path
  form the sister methods use.

#### 3. `implement-task` names the file that reads the rule, not the rule

- **Place:** `task-cycle/skill/SKILL.md:214-218`; the pointer stands at
  `task-cycle/skill/reserved_return.md:14`.
- **What is wrong:** `SKILL.md:218` has the orchestrator read `reserved_return.md`, whose line 14 has it
  read `project-level/technology/reserved_choices.md` and check the choice "before any answer". That is
  a file reached only through another file, two levels from `SKILL.md`. `git grep` finds
  `reserved_choices` nowhere in `task-cycle/skill/SKILL.md`.
- **Why it matters:** this check is what stops an agent's claim of `reserved`, or a smallest reversible
  reading, from settling the matter; the file says itself "an agent's claim is no evidence". WAY-265's
  *Rationale* wants every file a use may reach visible from `SKILL.md`.
- **A reading to weigh:** this is the least literal of the three. `reserved_return.md` is itself a
  variant's file, read on every path of that variant, and WAY-265's sentence speaks of "a step's file".
  I read it as reaching this case, since its *Rationale* says "every file its use may reach" and its
  *Rejected* refuses two levels; see *Searches not found or unclear*.
- **What would close it:** `SKILL.md:214-218` names `reserved_choices.md` beside `reserved_return.md`,
  under the same condition. Nothing else changes: WAY-256 keeps the check itself in `reserved_return.md`.
