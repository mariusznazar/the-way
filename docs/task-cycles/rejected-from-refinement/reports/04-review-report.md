PASS 1267e733e9d84581ce63d29d08da3744bd1bdadd

# Review of the whole change — task `rejected-from-refinement`

Range `d7a205cb3ae8c49465cd66f4de2031b33fc7ff9d..1267e733e9d84581ce63d29d08da3744bd1bdadd`, one
commit (`1267e73`), one author, no spec, no plan, no slices. `git rev-parse HEAD` in the worktree
`C:\Storage\repos\the-way\.runs\worktrees\rejected-from-refinement` gave `1267e733…`, the head
dispatched. The worktree was left clean (`git status --short` empty after the checks).

Blocking findings: 0. Minor: 5. Out of scope: 0 (3 lines under Declined to judge).

## Against the task

Every item of *To do* and the one row of *Settlements to record* is met by the commit:

- **To do 1** — `project-level/task/template.md:36–37` adds `- Not chosen:` with one sub-line per
  way (`<way> — <cost the question gave it, or the human's reason>`); `:101–105` says when it
  appears, that a transferred or canonical answer brings it along, and that an answer with no ways
  shown has none; `:142–146` has the row's *Source* name the question, or hold the ways itself for a
  choice made outside *Questions to settle* (the question against a choice while candidates are
  cut, the task's Q1 example). Writers: `project-level/task/skill/resolve_gaps.md:4–6` (manual
  refinement), `elements/common/skill/SKILL.md:99–102` (question against a choice writes its ways
  into the row's *Source*); checker: `project-level/task/skill/final_review.md:7–8`. Wording keeps
  "one line each" and "cost the question gave it or the human's reason in the human's words" as
  To do 1 gives it.
- **To do 2** — `elements/decisions/template.md:59–64`: *Rejected* of a decision written from a row
  holds the ways the row's source keeps, `none considered` where the human said so, or `unknown`
  with no question; derived ways — from the guess column, the cost of the way chosen, the
  foundation — never enter it. These three exclusions match the task's list word for word.
- **To do 3** — `elements/decisions/template.md:37`: `*Rejected:* <…> | none considered | unknown`.
  `elements/common/foundation_check.py:432–433` checks only that a line starting `*Rejected:*`
  exists (read), so `unknown` passes without a script change, as the task's *Context* says.
- **To do 4** — refiner transfers the ways: `project-level/task/skill/orchestrated_mode.md:25–27`,
  `project-level/lead/conversation_template.md:21–22, 40–42, 107`, `project-level/lead/skill/SKILL.md:125–128`;
  check before deleting the conversation: `project-level/lead/skill/SKILL.md:157–159` and
  `project-level/lead/conversation_template.md:139–141`.
- **Row 1 (Q2)** — written into WAY-134 (`foundations/decisions.md:3188–3266`), still three binding
  sentences (WAY-05). Sentence 1 has the task keep each way not chosen under its answer, or in the
  row's source for a choice outside the questions (Q1); sentence 3 gives a decision written from a
  row only the kept ways, `none considered` or `unknown`, and narrows the blocked-request question
  to "any other value" — which answers the row's guess column ("czy przy braku wariantów blokować
  request pytaniem"): no. *Verification* gains a complies example (two kept ways → two rejected
  options; none → `unknown`, no question) and three violates examples matching the row. Meaning held.
- **WAY-134's own *Rejected*** applies the new rule to itself: the row's *Source* is Q1 and Q2, and
  the four added rejected options are exactly Q1's and Q2's *Not chosen* ways, translated with the
  costs those lines give (checked one by one against `task.md:37` and `:41`: the row's *Source*
  for every choice; templates alone; part of WAY-29 with WAY-19 and the precedence cost; a decision
  of its own). Nothing comes from the guess column. The step numbers "(krok 3)/(krok 5)" of Q1 are
  dropped, which WAY-05 asks of author-written prose; meaning unchanged.
- **WAY-154** (`foundations/decisions.md:4029–4038, 4048–4049`) is corrected in the same change so
  its deletion condition does not still allow removing the conversation while the ways live only
  there. This is within To do 4 and the task names WAY-154 in *Decisions in play* for exactly this,
  so the task document carries the change (WAY-30); not a finding. The request must list both
  WAY-134 and WAY-154 with a meaning sentence each (WAY-114); the author's report gives both.
- Nothing was added that the task did not ask for, except the template bullet on the meaning of
  `none considered` and `unknown` (`elements/decisions/template.md:57–58`), which supports To do 3
  (defines the new word) — see Minor 1 for its side effect.

## Against the foundation

- WAY-05: three binding sentences kept; new *Rationale* and *Rejected* name no file, script or
  count and do not tell how the decision was reached.
- WAY-19: the rule extends WAY-134's question rather than opening a new one, as Q2 settled; no
  sentence of it now answers the same question in another entry. WAY-154 refers to WAY-134 inline
  rather than restating its rule.
- WAY-29: consistent — same family (`unknown`, no inferred rejected options); untouched.
- WAY-30 / WAY-114: WAY-134 and WAY-154 meaning changes are carried by the accepted task document
  (row 1, To do 4); no further question was due.
- WAY-35: the rule of the *Rejected* field stands in the decision template, the record-decision
  skill is not given it. But see Minor 1.
- WAY-113: the ways kept are those "a question of decision showed (WAY-113)"; consistent.
- WAY-154 / WAY-155: refiner alone transfers; answering agent unchanged in authority; consistent.
- WAY-118, WAY-140, WAY-168, WAY-172, WAY-215, WAY-22, WAY-227, WAY-242 (found by the search below):
  no collision. WAY-168 (a guideline rule's rejected options stand in its decision alone) is served
  by the change.
- No invariant test changed. The invariant `skill-rule-source` (WAY-35) is method `review`; see
  Minor 1.

## Findings

### Critical

none

### Important

none

### Minor

1. **`elements/decisions/skill/SKILL.md:36` now restates a rule the template holds.** The change
   adds to `elements/decisions/template.md:57–58` "`none considered` in *Rejected* says the human
   weighed no other way", while the skill keeps "`none considered` in *Rejected* is the human's
   statement." Before the change the rule stood only in the skill; after it, it stands in both —
   the very case WAY-35 rejects ("rules restated in the skill next to the template — two copies
   that drift"). The two agree today, so nothing breaks; the cost is drift later. Fix: drop the
   skill's line 36 (the skill reads the rule from the template). The author's report names this
   ("Choices" 5) and left it as not its question; since the change creates the second copy, it is
   this change's to remove. Evidence: `grep -n "none considered" elements/decisions/template.md
   elements/decisions/skill/SKILL.md` → template `:57`, skill `:36`.

2. **`task-cycle/skill/foundation_step.md:22–24` paraphrases the exception without
   `none considered`.** It says a decision's *Rejected* "takes the ways not chosen that the row's
   source keeps, or `unknown`, as the decisions' template gives". The pointer to the template makes
   it correct, but a writer reading only this step sees two outcomes where WAY-134 sentence 3 and
   the template give three. Fix: name all three or drop the paraphrase and keep only the pointer.

3. **`project-level/lead/answering.md:43–45` and `:58–59` restate the transfer without the ways.**
   They say fresh refiners "copy that answer and source into each of their documents" and "transfer
   resolved answers with provenance into task documents". The conversation template and the lead
   skill, which say the same, were updated to include the ways not chosen; these two passages were
   not. The answering agent does not transfer, so no step goes wrong today; the passages now
   disagree with their siblings. Fix: add "and its ways not chosen" or replace the restatements
   with a pointer.

4. **The guideline skills' lists of what goes into *Questions to settle* do not mention the ways.**
   `product-guidelines/coding/SKILL.md:73–78`, `product-guidelines/styleguide/SKILL.md:66–68`,
   `product-guidelines/testing/SKILL.md:65–…` each list the choices step 4 settles "each with the
   human's words and date as its source". These refinements are where a human most often chooses
   among shown ways (adopt or depart from a template, a tool, an exemplar), and WAY-168 puts a
   guideline rule's rejected options in its decision alone. The task template's rule
   (`project-level/task/template.md:101–105`) binds these documents and `final_review.md:7–8`
   checks it, so the ways should still reach the document; the skill a writer follows at the moment
   of writing is silent. Fix: one clause in each list, or a pointer to the template's rule.

5. **The own-work check aimed at the strongest point, not the weakest.** The author checked that a
   decision with `*Rejected:* unknown` passes `foundation_check.py` — something the task's
   *Context* already established and the script's presence-only check makes near-certain. The
   weaker points of this change are coverage (every place that writes, transfers or checks an
   answer carries the ways — Minors 3 and 4 show two it missed) and the fidelity of WAY-134's
   extended sentences to row 1. The author's report does list a search of writers, so this is
   noted, not graded higher.

## Declined to judge

- `project-level/definition_template.md:323` — projected decisions' *Rejected* (`none considered`
  as the human's statement) and whether projects need the same rule: projects are outside this
  task (the author also left it).
- *Rejected* of D-121–D-126 in loop2 and decisions written before this change: the task's
  *Out of scope*.
- `elements/decisions/skill/SKILL.md:54–55` — the projected-mode line placed between two step
  bullets (pre-existing at `d7a205c`, reported by the author, not touched by the change).

## Checks run

| Check | Result |
|---|---|
| `git rev-parse HEAD` in the worktree | `1267e733e9d84581ce63d29d08da3744bd1bdadd` = dispatched head |
| `git log d7a205c..1267e73` / `git diff d7a205c..1267e73` (whole diff read) | 1 commit, 10 files, +97/−43 |
| `python -B elements/common/foundation_check.py` | exit 0, "0 errors" |
| `python -B gate/run_tests.py task-cycle` | exit 0, 41 tests OK |
| `python -B gate/run_tests.py elements/common` | exit 0, 109 tests OK |
| `git diff d7a205c..1267e73 --check` | exit 0 (no whitespace errors) |
| width of added lines (`git diff -U0`, added lines > 100 columns) | none |
| search of `.py` files for parsers of task documents (`Answer:`, `Questions to settle`, `Not chosen`) | none — the new sub-list cannot break a script |
| search of `test_*.py` for the changed files' names / `none considered` | only fixtures in `project-level/test_plan_check.py:52`, `test_readiness_check.py:36,250` and `elements/common` tests; none reads the changed passages |
| manual: each added WAY-134 rejected option compared with Q1/Q2 *Not chosen* in `task.md` | faithful (see "Against the task") |
| manual: reading of `foundation_check.py:425–434` | *Rejected* checked for presence only; `unknown` passes |
| `git status --short` after the checks | empty |

Not run: `python -B gate/run_tests.py project-level` — no test there reads the changed passages
(only `*Rejected:* none considered` fixtures), and the full gate is the orchestrator's; the full
gate itself, per the handoff. Not repeated: the author's temporary edit of WAY-154's *Rejected* to
`unknown` — replaced by reading the check's code, which shows the same without changing a file.

## Foundation reading and reaches beyond the dispatch

- Parts touched (by `foundations/part_map.md`): decisions, elements-common, project-level,
  task-cycle. Decisions whose *Scope* names one of them: 143 by a search of the `- **Scope:**`
  lines. **Not all 143 were read whole** — reading most of the log would have cost more than this
  prose change warrants. Read whole: the task's *Decisions in play* WAY-134, WAY-29, WAY-35,
  WAY-113, WAY-154; and WAY-05, WAY-19, WAY-30, WAY-114, WAY-115, WAY-155 (linked by the entries in
  play or governing entry form and acceptance). Read binding sentences only, located by a search of
  the log for "rejected option", "*Rejected*", "none considered", "Questions to settle",
  "conversation file", "removes only" and "blocked draft request": WAY-118, WAY-140, WAY-168,
  WAY-172, WAY-215, WAY-22, WAY-227, WAY-242. The remaining scoped decisions were not read; a
  collision with one that uses none of those words would be missed.
- Invariant `skill-rule-source` (`foundations/invariants.md:86`), whole — WAY-35's verification
  names it, and Minor 1 touches it.
- `agent-instructions/README.md` — governs changes to the-way (handoff).
- `elements/common/way_of_working.md` "Reading the foundation" — the selection method.
- `elements/decisions/skill/SKILL.md:20–60`, `elements/common/skill/SKILL.md:70–125` — what the
  record-decision and find-entries skills say about *Rejected* and the question against a choice.
- `project-level/lead/answering.md`, `project-level/task/skill/draft.md`, `guideline_findings.md`,
  `product-guidelines/{coding,styleguide,testing}/SKILL.md` — found by a search for
  "Questions to settle" / "answer", to check every place that writes or transfers answers.
- `task-cycle/skill/return_step.md` — whether the return step restates the question rule (it does
  not).
- `elements/common/foundation_check.py:425–440` — to confirm `unknown` passes.
