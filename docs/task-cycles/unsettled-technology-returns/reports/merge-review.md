FAIL c69e35539aee2367bdda132b6d24cd1977d111b4

# Review of the reconciliation with the target branch

- Range: `b224a4f..c69e355` on `task/unsettled-technology-returns`, the head being `git rev-parse HEAD`.
- Task: `.runs/task-cycles/unsettled-technology-returns/task.md`.
- Answers of step 4 as the handoff gives them: trust boundary no, operation that cannot be undone no.
- No invariant test changed. The range changes no `.py` file.

## The two questions

1. **Is the renumbering whole and right? Yes.** Every one of the 36 references moved by the one
   simultaneous mapping, nothing else changed in either side's text, `foundations`' own WAY-265 and
   WAY-266 are untouched and still mean what they meant, and the three entries' *Relations* hold.
   Evidence under *Checks*.
2. **Does this change still hold against what the merge brought in? No.** WAY-265 reached this change
   after its reviews. Three skills this change altered now point to
   `project-level/technology/reserved_choices.md`, and one of them to `task_run.md`, only from a
   step's file, the layout WAY-265 calls a breach. WAY-256 as edited gives one Minor finding, and
   WAY-266 and `instruction-files/kind_skill.md` give nothing further.

## Findings

### Critical

none

### Important

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

### Minor

#### 4. `settle-technology` names `task_run.md` at step 0, not at the step whose file points to it

- **Place:** `project-level/technology/settle.md:61`; `project-level/technology/SKILL.md:37-38` and
  `:51-56`.
- **What is wrong:** `settle.md` is the file of step 2 and points to `task_run.md`, and WAY-265 wants it
  named in `SKILL.md` "at that step". Step 2 of `SKILL.md` does not name it; step 0 does, with its
  condition, saying it holds what a run at a task does "in place of what the steps below and their
  files give".
- **Why Minor:** the *violates* line is not met, since a reader of `SKILL.md` sees the file and its
  condition, and every run at a task reads it at step 0, resumed runs included. Only the words "at that
  step" are unmet. Naming it at step 2 without a second read would satisfy them, and WAY-256 forbids only
  a second read.

#### 5. Two later pointers have `reserved_return.md` read again with no "unless an earlier step did"

- **Place:** `task-cycle/skill/planning.md:12`, `task-cycle/skill/SKILL.md:218`.
- **What is wrong:** WAY-256 as edited gives "a step after the first having that file read unless an
  earlier step did", and its *violates* names "a step names a file and has it read again though an
  earlier step read it". Where an earlier question was checked and the rule did not take the choice, the
  cycle goes on, and a planner's `reserved` then has the file read again.
- **Why Minor:** this is a rare path and costs one more read of a 92-line file, against none of the task's
  behaviour. A session that lost the earlier read needs it anyway.

### Out of scope

#### 6. The request and the record still carry the old numbers, which now name other decisions

- **Place:** the description of https://github.com/mariusznazar/the-way/pull/63, lines 34, 35, 45, 46
  and 51-53 among others; `.runs/task-cycles/unsettled-technology-returns/cycle.md:126` and `:133`.
- **Beyond the task and beyond the range:** this is neither a file of the change nor in `b224a4f..HEAD`,
  so it blocks nothing here, and the remote head is still `b224a4f`, so the request is plainly not yet
  brought up to date.
- **Why it is worth saying:** the human accepts the entries by merging, reading that list. After this
  merge it would say WAY-265 is the technology run and WAY-266 the reserved rule, while the log gives
  those numbers to the variant file and the guidelines session. `cycle.md:83` keeps old numbers in
  earlier reports on purpose, which is sound for reports and not for the request's *What this request
  settles*. The task's Context also has a later session write the number of the decision from row 2 into
  `mapa_pakietu_10x.md`: that number is now WAY-268, and `cycle.md:126` still reads WAY-266.

## Declined to judge

- The range `2dbf1e7..b224a4f` other than against the target's entries: the handoff keeps it out, and
  `reports/whole-review.md` and `reports/whole-review-2.md` hold that review.
- `task_run.md`'s references to `project-level/task/skill/draft.md`, `resolve_gaps.md` and
  `orchestrated_mode.md`: these are steps of another skill, `refine-task`, whose own `SKILL.md` names
  them, so I did not count them under WAY-265.
- The styleguide skill's two-level layout (`starting_rules.md` to `research.md` and the like): the
  target's own, its files standing unchanged, and not touched by this change.

## Checks

| Check | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `c69e35539aee2367bdda132b6d24cd1977d111b4`; the handoff names `HEAD` and gives no SHA |
| `git diff b224a4f c2683b7`, read whole | 0 | 16 files, each change one number |
| `git grep -E 'WAY-26[567]\b' b224a4f`, `git grep -E 'WAY-26[789]\b' c2683b7` | 0, 0 | 36 occurrences in 16 files before, 36 after |
| `git grep -E 'WAY-26[56]\b' c2683b7` | 1, no match | no WAY-265 or WAY-266 left at `c2683b7` |
| `git grep -n -E 'WAY-26[56789]\b'` at `2dbf1e7`, `87286f6`, `HEAD` | 1, 0, 0 | none at the base; the six at `87286f6` stand unchanged at `HEAD`: the two headings, `styleguide/SKILL.md:70`, `testing/SKILL.md:81,92,107` |
| `git grep -n -E '\b26[5-9]\b' HEAD -- '*.md' '*.py' ':!foundations/decisions.md'` | 0 | every match is a `WAY-26x` reference; no bare number |
| `git grep -P 'WAY[\x{2010}-\x{2015} ]26[5-9]' HEAD` | 1, no match | no reference with another dash or a space |
| `python -B <scratchpad>/check_merge.py <tree>`, the scratchpad being `C:\Users\Mariusz\AppData\Local\Temp\claude\C--Storage-repos-the-way\3f495b8a-5898-44db-bd97-8c76e67b3513\scratchpad` | 0 | each of the 16 files at `b224a4f`, under the simultaneous map 265 to 267, 266 to 268, 267 to 269, equals its blob at `c2683b7` byte for byte, 36 substitutions, 0 mismatches |
| `git merge-tree --write-tree --name-only c2683b7 87286f6` | 1, the conflict | one conflicted file, `foundations/decisions.md`, tree `9188b44`, one hunk at lines 7599-7846 |
| `git diff --stat <that tree> HEAD` | 0 | only `foundations/decisions.md` differs, so the merge commit holds no change outside the conflict |
| same script, the resolution | 0 | `HEAD`'s log equals prefix + the target's block + this change's block + suffix, except one blank line between the blocks, the separator the entries need; each block is found whole in its own side |
| `git diff --stat 87286f6 HEAD -- product-guidelines instruction-files` | 0 | empty: the target's files stand as the target has them |
| `python -B elements/common/foundation_check.py .` | 0 | `0 errors` |
| `python -B agent-instructions/skill_entry_points.py` | 0 | `entry points are current`; run without `--write` |
| `python -B instruction-files/check_instructions.py . --file <f>` for `project-level/task/skill/SKILL.md`, `task-cycle/spec/SKILL.md`, `task-cycle/skill/SKILL.md` | 0 each | 0 errors; it does not test what findings 1 to 3 name, so this clears nothing of them |
| Scan of the backticked `.md` paths each file of this change adds, `git diff 2dbf1e7 c2683b7` | 0 | the list findings 1 to 5 rest on |
| `git grep` of `settle-technology`, `reserved choice`, `task_run`, `reserved_choices` in `product-guidelines` and `instruction-files` at `HEAD` | 1, no match | the target's files lean on nothing this change altered |
| `git status --short`, before and after | 0 | empty; the reviewed worktree, index and branch are as they were |

Manual checks:

- **Meaning of each reference:** read each changed line in `git diff b224a4f c2683b7` with the entries
  at `foundations/decisions.md:7654`, `:7715` and `:7781`. Each reference keeps its meaning: a run at a
  task, 267; who settles, 268; how a task leaves, 269.
- **Relations of the three entries:** WAY-267 at `:7670-7671` and WAY-268 at `:7734-7735` name none of the
  moved numbers. WAY-269 at `:7798-7799` derives from WAY-268, and WAY-135 at `:3292-3293` derives from
  WAY-268, each what it derived from under the old number 266. The entries stand in ascending order
  after the target's two.
- **WAY-256 as edited, rule of working against text to consult:** the rule "No stage of the cycle settles
  a reserved choice" stands in `task-cycle/skill/SKILL.md:214`, and what the agent consults stands in
  `reserved_return.md`, as the entry gives. The only departure is finding 5.
- **WAY-266 and the guidelines skills:** this change touches no skill of guidelines. A run of
  `settle-technology` called from `refine-task` is not such a skill, and `task_run.md:13-15` lists its own
  reading. `reserved_choices.md:34` keeps a test tool "on that skill's route", and the route stands at
  `product-guidelines/testing/new_tools.md`, whose last sentence leaves the choice to the human.
- **`refine-task` step numbers:** `project-level/task/skill/SKILL.md` is unchanged, so "steps 1 and 2" of
  WAY-266 and of `styleguide/SKILL.md:70` and `testing/SKILL.md:81` still point right.

Not run: `python -B gate/run_tests.py`, the orchestrator's run on this head, by the handoff. No focused
test: the range changes no code, and the two checks above cover what a broken merge of these files would
break. `git merge-tree` left an unreferenced tree object in the shared object store and changed nothing
else.

## Reaches beyond the dispatch

- `foundations/decisions.md`, WAY-161 and WAY-263: for what blocks and whether WAY-263 is the ground of
  the grade. It is not.
- `foundations/decisions.md`, WAY-162, passage found by the word "reconciliation": how the end of this
  review goes.
- `foundations/environment_facts.md:186-190`, `claude-skill-nested-references`: WAY-265's *Based on*, to
  size the consequence.
- `task-cycle/skill/SKILL.md:14-243`, `:280-389`: what a variant is called there and step 12's rule.
- `docs/task-cycles/testing-skill-shape/reports/review.md` at `15b041a`, line 72: how the review that
  shaped WAY-265 read "variant file", which counts a step's file naming `research.md` as the case.
- `reports/whole-review.md:48-65` and a search of the two whole-review reports for nested references:
  to see this was not already judged, and how the same consequence was graded.
- `.runs/task-cycles/unsettled-technology-returns/cycle.md`, by search only, for WAY-26x. The record is
  the orchestrator's to read (`task-cycle/skill/SKILL.md:165`). I searched it to see whether the old
  numbers were accounted for, and nothing in the findings above rests on it save finding 6.
- `gh pr view 63`, read only, for the same reason.

## Searches not found or unclear

- **"The file of a variant" in WAY-265.** The entry does not say whether it reaches a file outside the
  skill's directory, such as `project-level/technology/reserved_choices.md` read from `task-cycle/`, or a
  file read on every path of a variant rather than on a further condition. I read both as reached, by its
  *Rationale* ("every file its use may reach") and its *Rejected*. A narrower reading would keep findings
  1 and 2 and drop finding 3.
- **"Changed according to WAY-256" in WAY-265.** Not defined. I read it as any change WAY-256's first
  sentence binds, a fragment "a change to a skill of the-way adds or rewords", with the entry's last
  sentence as the only exemption.
- **"As your method's reconciliation gives" in the handoff.** `task-cycle/review/SKILL.md` has no section
  for the reconciliation: it names it at lines 11, 21 and 29, and line 29 has the orchestrator select the
  foundation and guidelines, while the handoff has me select my own. I followed the handoff and its two
  questions.
- **Grade of a departure from an entry the change neither writes nor changes.** WAY-263 covers only
  entries a change writes or changes, and neither `task-cycle/review/SKILL.md` nor the log gives a rule
  for an entry that reached the change by a merge. I used the general grade and say so above.
- **A mechanical check of WAY-265.** Looked for a check that would catch a file named only in a step's
  file, by the words `nested`, `variant` and `variants` in `elements/common/foundation_check.py`,
  `instruction-files/check_instructions.py`, `gate/run_tests.py` and
  `agent-instructions/skill_entry_points.py`. Found none. The one near miss, `nested-pointer` at
  `instruction-files/check_instructions.py:635`, concerns a nested `AGENTS.md`, not a skill's files.
