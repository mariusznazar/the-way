PASS 3023f604d5517ca157b3cb6bb9135a360d7e29f3

# Review of the whole change — cycle-remarks-batch-2

Range `61c72fb6347649a9bd61a71f0d2695f2e91e8b6a..3023f604d5517ca157b3cb6bb9135a360d7e29f3` (two commits, `b2a52f6` and `3023f60`). `git rev-parse HEAD` in the worktree is the given head. Worktree clean before and after my checks. One author, no spec, no plan: no slice reviews, so no Minor or out-of-scope findings inherited from slice reviews.

Counts: blocking 0, Minor 4, out of scope 1.

## Verdict in one paragraph

All thirteen sentences and fragments the task quotes stand word for word where the task places them (my own script, below). Every *To do* item (1-4) and rows 1-3 of *Settlements to record* are met by the commits. WAY-293 carries row 1's meaning, narrows WAY-22 and WAY-18 as WAY-25 requires and gives as *Rejected* only ways the task's source keeps (WAY-134). WAY-05 and WAY-148 are changed as the task approved (WAY-30). The findings below are polish or layout; none changes what a later cycle reads as a rule.

## Findings

### Critical

none

### Important

none

### Minor

**M1. WAY-05 *Verification*: the new pair is merged into the old pair instead of standing as "nowa para"** — `foundations/decisions.md:141-146`.
- What: To do 2, fourth bullet, asks for a new pair, `complies: …; violates: …`. The change appends the new example to the existing `complies:` line (after a `;`) and the new counter-example to the existing `violates:` line. The labels `complies:` and `violates:` therefore no longer open the task's two sentences, and the first line now lists two unrelated examples (a template field; a rationale with a measurement).
- Why it matters: the meaning is intact, but the entry no longer shows "a new pair" the task asked for, and each line now mixes two subjects, so a reader pairs the wrong examples more easily.
- The author's reason ("two lines of the same label would be a form the template does not give") does not hold: WAY-29 already holds two `complies:`/`violates:` pairs (`foundations/decisions.md:747-754`), and `foundation_check.py` accepts them. The cost of the choice, as the author states, is only a layout change; the fix is the same size.
- Evidence: `git diff 61c72fb..HEAD -- foundations/decisions.md` (hunk at WAY-05 *Verification*); my script reports the two task sentences with their labels as not present (the sentences without the labels are).

**M2. WAY-293 *Rationale* tells what the request does and lacks today** — `foundations/decisions.md:8818-8826` ("the request puts it before the human in the section for the human's decisions where it changes what the human meets when working with the process … the human sees, at the merge, the choice itself but no line saying it has no entry").
- What: WAY-05's binding sentence (as the same change words it) bars, in the entry author's own prose, "what the process's own tools do or lack today". The sentence describes what the request template does today and what it has no line for. The source is the task's *Context* bullet, but a *Context* bullet is not a quoted source of the entry, and the wording is the author's.
- Why it matters: the entry then states a fact about a tool that changes with the next edit of the request template, which the entry does not follow. Small, and borderline: the sentence is also the cost of the decision, which *Rationale* may state.
- Evidence: reading of WAY-05's binding sentence against the *Rationale*; `task.md` *Context*, the bullet for point 1.

**M3. WAY-293 *Rejected*: "no change, which withdraws the rule"** — `foundations/decisions.md:8830` (the second rejected way).
- What: the task keeps two ways here, "no change" (question 1, way C) and "withdraw point 1" (critique, way c); the entry folds them into one and words it as "no change, which withdraws the rule". Read cold, it says that making no change withdraws an existing rule; what is meant is that making no change leaves the return step without the precedence.
- Why it matters: the rejected way is the cost side of the decision; a reader who takes "withdraws" literally cannot tell what was weighed. Merging the two ways is a fair reading (WAY-134 asks for the ways the source keeps, not each by its letter); only the gloss misleads.
- Evidence: `task.md` question 1 ("Not chosen" C) and the critique paragraph (way c).

**M4. Rewrapped lines left uneven** — `foundations/decisions.md:3896-3899` (WAY-148 binding sentence: a short line "in its report. The handoff names what the agent reads, as the") and `elements/decisions/template.md:57` (110 characters, the longest of the added lines; the file already holds longer ones, so no rule is broken).
- Why it matters: polish only; the next edit of either paragraph produces a noisier diff.
- Evidence: `git diff 61c72fb..HEAD` for the two files.

### Out of scope

**O1. The planner's return still names a check result; WAY-148 now asks it only where the stage runs a check "of the product"** — `task-cycle/plan/SKILL.md:202-203` ("a one-line check result naming failed or unchecked work") against `foundations/decisions.md:3896` ("where the stage runs a test or another check of the product").
- The planner runs the size script over its plan's slices (`task-cycle/plan/SKILL.md:184-190`), a check of the plan, not of the product. After the approved wording it is unclear whether the planner returns a result. The task limits the change to the spec stage and the wording was approved with the document (WAY-30), so I do not grade it against the change; it is a gap the wording opens, for the human who accepts decisions to settle (a word in WAY-148, or a line in `plan/SKILL.md`).
- The author names the same place under **Searches not found or unclear** and says it did not verify what the planner's checks are; I read lines 184-203 and confirm they are the size check.

## Choices of the author, judged

- **New WAY-05 example inside the existing `complies:`/`violates:` lines:** not accepted as reasoned; see M1 (Minor).
- **WAY-293 scope `decisions, task-cycle`:** fine. It narrows WAY-22 (scope `decisions, invariants`) and WAY-18 (scope `decisions`), and a link is written at one end only (WAY-18), so a reader by part `decisions` finds it through *Scope*. `foundation_check.py` passes.
- **No `derives from WAY-36`:** fine. WAY-36 says what may enter the log, not that every choice must; the task and row 1 name only `narrows` of WAY-22 and WAY-18 (WAY-25 asks for exactly that, plus the area in the binding sentences, which the second sentence of WAY-293 gives).
- **Third binding sentence ("A candidate left out of a task's *Settlements to record* is no exclusion."):** acceptable. It is the last sentence of To do 1, approved with the document; the entry's allowance is three sentences. Two notes, neither a finding: the sentence is not in the two skill texts the task words (so only the decision carries it), and the *Verification* line "a candidate the human did not accept" says the same as the task's "wycięty" (the table's "Candidates: 5 shown, 3 accepted").
- **WAY-148 *Verification* and *Rationale* not changed:** fine. I read the whole entry; nothing in either says a stage that runs no check returns a result.

## Against the task, point by point

1. **To do 1.** `task-cycle/skill/return_step.md:13-15` has the sentence after "(WAY-36)."; the pronoun "It" of the next sentence still refers to the agent defined at the top of the file. `task-cycle/record_template.md:99-101` carries "(WAY-36), unless the task or its spec excludes the entry, as `task-cycle/skill/return_step.md` gives;". Foundation step (`task-cycle/skill/foundation_step.md`) writes entries "a reviewed spec names", so a spec that excludes an entry is not reached there; no further place found. Met.
2. **To do 2.** Binding sentence at `foundations/decisions.md:128-131` and `elements/decisions/template.md:53-57` carry the same fragment; *Rationale* sentence at `:149-152`; example pair at `:141-146` (see M1). The new sentences themselves stand word for word. No other file restates the ban (searched, see Searches). Invariant `skill-rule-source` (derives from WAY-35) is kept: the rule stands in the template as well. Met, with M1.
3. **To do 3.** `task-cycle/skill/SKILL.md:187-193` (general rule) and `:288-295` (mechanical check) in the task's wording; `questions` is excepted for **Searches not found or unclear**, and only `done`/`done with concerns` of `make-change` are held to the own-work check, as the task says. Met.
4. **To do 4.** `task-cycle/review/SKILL.md:140-141`, WAY-148 at `foundations/decisions.md:3894-3897`, `task-cycle/spec/SKILL.md:51-53`, the parenthetical at `task-cycle/skill/SKILL.md:177-179`, `task-cycle/spec/review.md:26` — all in the task's wording. The designer's `task-cycle/spec/design.md:60-73` "four checks" read the spec, not the product, so they do not contradict "neither runs a test or another check of the product". Met.
5. **Settlements, rows 1-3.** Row 1 is WAY-293 (new, `foundations/decisions.md:8794-8832`), row 2 is WAY-05 in place, row 3 is WAY-148 in place. Meaning of each matches the row; WAY-293's *Rejected* holds the ways the row's source keeps (the exception for every choice written in a skill or template; no change / withdrawing the rule; only the task excluding), without ways of the author's own.
6. **Out of scope of the task** (removing counts from the reviewer's message): not touched.

No test file changed, so no changed invariant test. No reserved choice is taken. Trust boundary and irreversible operation: none, as answered at the start.

**The author's own-work check:** the requirement it names ("copy it exactly") is where the change is weakest, and its check (look for each task sentence in its file with whitespace normalised; 14 of 14 `MISS` on the base commit, 0 `MISS` on the head) would catch a sentence left out or altered. It could not catch M1, because it looked for the sentences without their `complies:`/`violates:` labels; the author's report is open about the layout choice.

## Declined to judge

- The planner's check result against WAY-148's new clause — see O1; set aside as outside the task, reported once there.
- `task-cycle/test_request_check.py:60-62` quotes the old sentence of WAY-148 in a made-up task document used as a fixture; no test compares it with the log (outside the task; harmless).
- The wording of the new sentences themselves where the task dictates it (word for word) beyond what M2-M3 and O1 name — the human approved it with the document.

## Checks I ran

All from the worktree root `C:\Storage\repos\the-way\.runs\worktrees\cycle-remarks-batch-2`; none changed a tracked file (`git status --short` empty afterwards).

| Command | Exit |
|---|---|
| `git rev-parse HEAD` (= `3023f604d5517ca157b3cb6bb9135a360d7e29f3`) | 0 |
| `git log 61c72fb..HEAD`, `git diff 61c72fb..HEAD`, `git diff 61c72fb..HEAD --stat` | 0 |
| `python -B elements/common/foundation_check.py` (`0 errors`) | 0 |
| `python -B gate/run_tests.py task-cycle` (92 tests, OK) | 0 |
| `python -B gate/run_tests.py elements/common` (109 tests, OK) | 0 |
| `python -B gate/run_tests.py relation-model` (12 tests, OK) | 0 |
| `python -B gate/run_tests.py agent-instructions` (18 tests, OK) | 0 |
| `python -B gate/run_tests.py instruction-files` (104 tests, OK, 5 skipped by the tests) | 0 |
| `python -B C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\693489a7-cb0e-4eb7-9d76-91dc04059916\scratchpad\rev_check.py` — own script: 14 quoted sentences of the task searched in their target files, whitespace normalised, labels included; also checks the sentence is absent at the base | 0; 12 found, 2 reported missing = the `complies:`/`violates:` sentences with their labels (M1); with the labels removed both stand |

Not run: `python -B gate/run_tests.py` without a directory (the orchestrator's); `elements/decisions` and `foundations` hold no tests (the author's runs of them exit 1 with "no test found", not a failure of the change; I did not repeat them). No check was a pass-by-assertion of nothing: the changed files are instruction files, and the form of the foundation is the check that has teeth here (`foundation_check.py`), plus the instruction-file tests.

## Reaches beyond the dispatch

- Decisions read whole: WAY-05 (changed), WAY-148 (changed), WAY-18, WAY-22, WAY-25, WAY-36, WAY-114, WAY-134, WAY-293 (new) — the entries the change writes or collides with. Why: to judge precedence and *Rejected* (WAY-25, WAY-134) and the approval path (WAY-114). WAY-29 and WAY-168 read only at the lines I cite (the pairs of examples; the use of "choice that binds"). Not read whole: the other decisions scoped `decisions` or `task-cycle`; I selected by relevance to what the change reaches, and found the others by searching, not by reading each (the part's full list is in the hundreds).
- Invariants whose *Part* is `every` or names `decisions`: listed; read whole `skill-rule-source` and `return-step-record`. None cites WAY-05, WAY-148 or WAY-293.
- Files: `task-cycle/skill/foundation_step.md`, `task-cycle/spec/design.md` (lines 56-78), `task-cycle/plan/SKILL.md` (lines 184-210), `task-cycle/change/SKILL.md` (lines 140-152), `task-cycle/skill/SKILL.md` (lines 160-215 and 270-335), `task-cycle/test_request_check.py` (lines 56-64). Why: callers and neighbours of the changed sentences (a place that restates the old wording, the planner's and designer's return).
- `C:\Storage\The Brain\The Brain\.ai\rules\scripts.md` and `search.md` — instructions outside the repository, before writing the script and before reporting "not found".

## Searches not found or unclear

- Other places restating WAY-05's ban on counts, WAY-148's list of what a message carries, or the return step's rule for a choice that binds: searched with `names no`, `script or count`, `or count`, `check result`, `one-line`, `binds after`, `choice that binds` over `task-cycle`, `elements`, `project-level`, `foundations`, `agent-instructions` (Grep and `grep -rn`, no limit, positive control: each hit in the changed file itself). Found no further place to change besides O1 (the planner).
- A decision or invariant requiring that the reviewer's return be only the first line and the path: searched `counts`, `nothing more`, `first line` in `foundations/decisions.md` and `task-cycle`; none found.
- Whether the planner returns a check result under the new WAY-148 wording: unclear (O1).
- Whether `foundation_check.py` has any rule about the number of `complies:`/`violates:` pairs: not found by reading the check's output (it passes with the two pairs of WAY-29); I did not read the script whole.
- The full list of decisions of the parts `decisions` and `task-cycle` was not read entry by entry; see "Reaches".
