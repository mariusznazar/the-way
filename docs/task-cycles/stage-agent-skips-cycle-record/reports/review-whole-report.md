FAIL de24e5b8d03893f53cee4f8083b8f4ef2d102028

# Review of the whole change — stage-agent-skips-cycle-record

Range: `3cbaeb9ff188b77c8a96c4f3194db07e8a8a2898..de24e5b8d03893f53cee4f8083b8f4ef2d102028`. `git rev-parse HEAD` in the worktree gave `de24e5b8d03893f53cee4f8083b8f4ef2d102028`, the head given. One commit, `de24e5b8` "Tell each stage agent in its handoff that the cycle record directory is not its to read (WAY-148)", one author, no plan, no slice: there is no slice to name for any finding. Files: `foundations/decisions.md` (+27/-5, WAY-148) and `task-cycle/skill/SKILL.md` (+3/-1).

## Findings

### Critical

none

### Important

1. **`foundations/decisions.md:6096-6100` (WAY-148, *Rationale*): the rationale says the loop2 spec reviewer was influenced, but the source says the orchestrator had made no ruling and no harm was found.** Within the task.
   - The added text reads: "an agent that learns that reasoning before it gives its own assessment assesses under its influence, as a reviewer of a spec did in a cycle of a game product when it read the log to see whether the orchestrator had already ruled on the designer's points."
   - "as a reviewer of a spec did" claims that the reviewer learned the orchestrator's reasoning and assessed under its influence. The sources say otherwise:
     - The task's *Need* says "szkody nie stwierdzono" ("no harm was found").
     - The task's *Po co to* says "nie stwierdzono szkody ani błędnej oceny z tego powodu" ("no harm and no wrong assessment was found for this reason").
     - The evidence the task cites says the orchestrator had made no ruling. The loop2 report at `273446f:docs/task-cycles/ognisko-i-jedzenie/reports/02-spec-reviewer-report.md`, in the reach list near line 130, reads: "`.runs/task-cycles/ognisko-i-jedzenie/cycle.md` — to see whether the orchestrator had already ruled on the designer's five points (it had not)."
   - So the reviewer found no ruling to be influenced by. The task's *Decisions in play* cites the case only as an example in parentheses ("ocenia pod jego wpływem (recenzent specu w cyklu loop2 `ognisko-i-jedzenie`)"). The change turns that example into a statement that the influence happened.
   - Why it matters: the whole-change review checks fidelity to the task's sources, "with nothing the change takes from them altered or invented" (`task-cycle/review/whole_change.md`). WAY-134 also requires a decision written from a settlement row to keep the row's meaning. *Rationale* is what "a human considering a change" reads (decision template, "Fields and their readers"). A later reader weighing whether to keep or drop the rule would take this as an observed case of a review skewed by the log, which the evidence does not show.
   - Recommended fix: state the case as a risk shown, not as harm that happened. For example: "…assesses under its influence; a reviewer of a spec in a cycle of a game product read the log to see whether the orchestrator had already ruled on the designer's points, and found no ruling there."

### Minor

1. **`foundations/decisions.md:6043-6046` (WAY-148, binding sentence 2): the old premise "only the orchestrator reads the cycle record" now sits next to an exception it does not allow.** Within the task.
   - The sentence reads: "since only the orchestrator reads the cycle record, the handoff tells the agent that `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and findings — are not its to read unless its handoff names them".
   - Elsewhere in the log, "the cycle's record" also means the whole directory. WAY-403 calls the spec, plan, handoffs, reports and `cycle.md` "the original of the cycle's record". Read that way, the premise says that no agent reads any file of the record, while the same sentence lets an agent read a file its handoff names, as a reviewer reads the author's report.
   - The *Verification* pair settles the meaning, so this is polish. Naming `cycle.md` in the premise ("since only the orchestrator reads `cycle.md`") would remove the clash.
2. **`foundations/decisions.md:6100-6102` (WAY-148, *Rationale*): the rationale describes what one of the-way's own tools does today, which the template keeps out of the prose.** Within the task.
   - The added sentence reads: "…and the orchestrator's skill gives the sentence once for all the handoffs."
   - The decision template (`elements/decisions/template.md:80-85`) says *Rationale* prose names no file, script or count "nor what the process's own tools do or lack today" (WAY-05, WAY-29). Where the sentence lives is a fact about the skill, not a reason for the decision.
   - The reason for putting it in the handoff is already given: one text, read in every harness. Dropping this clause, or saying "the sentence stands in one place", loses nothing.
   - Graded Minor as a departure from the template's form whose content agrees with the code (WAY-364).

### Checked and found right

- **To do 1:** `task-cycle/skill/SKILL.md:213-215` holds the task's sentence word for word: "It tells the agent that `cycle.md` and the other files of the cycle's record directory — other agents' handoffs, reports and findings — are not its to read unless its handoff names them." I checked this against the task and the diff.
- **Where the sentence stands:** the task places it after the sentence that lists what every handoff carries, "ending 'and the report path.'". That list sentence has since grown and now ends "(WAY-148)." It is still the same sentence, so the new sentence right after it is the place the task means. "It" refers to "The handoff", the subject of the sentence before.
- **To do 2 and *Decisions in play*, WAY-148:**
  - The binding text now says the handoff tells the agent the ban, with the task's wording of its scope.
  - *Verification* "violates" covers both cases the task names: an agent that reads such a file not named in its handoff, and a handoff without the sentence.
  - *Rationale* adds the independence of the assessment and the loop2 case. Important 1 covers how it states the case.
  - *Rejected* holds the four ways the task did not choose (1 (b), 1 (c), 2 (a), 3 (b)), each with its cost as the task's *Not chosen* gives it.
  - The way set aside when the task was parked (the sentence in four stage skills) is rightly left out. The row's *Source* does not keep it, and WAY-134 and the decision template bar a way the writer derives.
- **The first paragraph** still has three sentences, within the template's limit of one to three.
- **Settlement row 1:** carried into WAY-148 with its reason; nothing goes to the agent-type definitions.
- **WAY-150, WAY-10, WAY-368, WAY-370:** unchanged, and the change does not contradict them:
  - WAY-150: "every other agent … reads what its handoff names".
  - WAY-368 and WAY-370: no definition of an agent type was touched.
- **Other files of the record directory:** a search of `task-cycle/**/*.md` found no method that tells a stage agent to read a file of the record directory its handoff does not name.
  - `plan.md` and the spec are named by path in every handoff, per the handoff list in `SKILL.md`.
  - The findings file and the fix report are named for the fix and its review.
  - The renumbering pass (`SKILL.md` "The renumbering of the task's decisions") and the reading of earlier tasks' records (step 4) are the orchestrator's own.
  - The orchestrator's own line, `SKILL.md:259-260` ("You alone read `cycle.md`…"), agrees.
- **Source fidelity of *Rejected*:** each cost matches the task's *Not chosen*.
- **The author's own-work check** (the skill sentence word for word, three binding sentences, the foundation check green) holds. It does not reach the weakest spot of this change, the rationale's fidelity to its evidence (Important 1), so it would not have caught that finding.
- **Structure of the code:** nothing to judge.
  - `task-cycle/change_file_sizes.py` gives `foundations/decisions.md` 10830 → 10852 (+22) and `task-cycle/skill/SKILL.md` 849 → 851 (+2).
  - Both are Markdown. No script or function changed, so the rule of size (WAY-385, invariant `function-and-file-size`) is not reached.

## Declined to judge

- The stage skills' paragraphs on reaching beyond the dispatch (`task-cycle/spec/SKILL.md`, `plan/SKILL.md`, `change/SKILL.md`, `review/SKILL.md`) still say nothing about the record directory. The task chose the handoff alone (question 1 (a)) and put the stage skills outside it, so this is outside the task.
- Many lines of `foundations/decisions.md` run past 100 characters, before this change as after it. This is not a rule the foundation check or the template holds, so it is outside the task.

## Checks

- `python -B elements/common/foundation_check.py` in the reviewed worktree: exit 0, "0 errors".
- `python -B task-cycle/change_file_sizes.py 3cbaeb9ff188b77c8a96c4f3194db07e8a8a2898 de24e5b8d03893f53cee4f8083b8f4ef2d102028`: exit 0 (sizes above).
- `python -B -m unittest discover -s task-cycle -p "test_*.py"`: exit 0, 534 tests, OK (2 skipped).
- `python -B elements/common/decision_index.py --output .runs/review-whole/sections.md --sections`: exit 0.
- `python -B elements/common/decision_index.py --output .runs/review-whole/index.md --section "The course of a task cycle" --section "The work of a cycle's agents" --section "Review of a change" --part task-cycle --decision WAY-148 --decision WAY-150 --decision WAY-10 --decision WAY-368 --decision WAY-370`: exit 0. A first run with `--decision 148` ended with exit 2, "no decision 148"; the switch takes the number with its prefix.
- Manual check: the loop2 evidence the task cites, at `273446f`, compared with the WAY-148 *Rationale* sentence. It shows "(it had not)" (Important 1).
- Not run: the test of the invariant `function-and-file-size` in worktrees of the base and the head. The change touches no script, so its result cannot differ between them. The product's gate was not run either: no handoff runs it.

## Reach beyond the dispatch

- The loop2 repository, `git show 273446f:docs/task-cycles/ognisko-i-jedzenie/reports/02-spec-reviewer-report.md`, lines 120-140, read in the loop2 checkout. The task's *Context* names it as the evidence of the case, and I read it to check the fidelity of the WAY-148 *Rationale*.
- `task-cycle/skill/planning.md` lines 1-38 and `task-cycle/skill/SKILL.md` lines 195-264 and 670-717: to check whether any method tells a stage agent to read a file of the record directory its handoff does not name.
- WAY-134 and WAY-213 opened from their index headings, as bearing on how a settlement row is carried and on what a handoff names.

## Working copies

- `.runs/review-whole/` held the index files (`sections.md`, `index.md`) and the outputs of the foundation check and the task-cycle tests. Removed before return. The report needs none of them.
- No worktree or clone was made.

## Unread material

- My selection's index lists 26 decisions in full and 89 by heading alone, 115 in all. I read 5 of them whole: WAY-148, WAY-150, WAY-10, WAY-368, WAY-370.
- Decisions that bear on the change and stayed unread whole: WAY-134 and WAY-213. I read their binding sentences and the start of their fields, not their *Rationale* and *Rejected*.
- Guideline files: none selected. The change touches no code, test or user interface of the `task-cycle` part, so `product-guidelines/reading.md` selects none.
- Invariants of `task-cycle` and `every`: read whole. Part-map entry `task-cycle` and the decisions template: read whole. `elements/decisions/examples.md`: read whole; it names only WAY-03, and I did not open WAY-03.

## Searches not found or unclear

- The task's reference to the skill sentence "ending 'and the report path.'" (*To do* 1, *Context*) no longer matches `task-cycle/skill/SKILL.md`. The list sentence now continues with the copy of "Working copies" and ends "(WAY-148).". Judged above as the same sentence, so the author's placement is right.
- `elements/common/decision_index.py --decision` does not take a bare number (`148`): it needs the prefix (`WAY-148`). `elements/common/way_of_working.md` "Reading the foundation" writes the switch as `--decision NUMBER`, which reads as a bare number.
