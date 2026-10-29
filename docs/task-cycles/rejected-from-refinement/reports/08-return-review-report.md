PASS c6ee066e20eac62764dda9328cd04f93e826f7e5

# Review of the return step — task `rejected-from-refinement`

Range `1267e733e9d84581ce63d29d08da3744bd1bdadd..c6ee066e20eac62764dda9328cd04f93e826f7e5`, one
commit (`c6ee066`), four files, prose only. `git rev-parse HEAD` in the worktree
`C:\Storage\repos\the-way\.runs\worktrees\rejected-from-refinement` gave `c6ee066e…`, the head
dispatched. The worktree was left clean (`git status --short` empty after every check).

Blocking findings: 0. Minor: 2. Out of scope: 0 (2 lines under Declined to judge).

## What the range does, checked against the task and the entries

The commit closes the two restatements the whole-change review found (its Minors 3 and 4,
`reports/04-review-report.md`):

- `product-guidelines/coding/SKILL.md:78–79`, `product-guidelines/styleguide/SKILL.md:67–68`,
  `product-guidelines/testing/SKILL.md:71–72` — the *Questions to settle* item of "What reaches the
  task document" now adds "and the ways the human did not choose under it as the task template
  gives (WAY-134)". Matches WAY-134 sentence 1 as `1267e73` left it (the task keeps each way not
  chosen under the answer to its question) and To do 1. The clause reads unconditional, but "as the
  task template gives" carries the template's condition (`project-level/task/template.md:101–105`:
  only where the human chose among ways shown; an answer with no ways shown has no *Not chosen*),
  so no writer is told to invent ways. The same skills' "Write each answer under its question … as
  `refine-task` step 3 gives" (`coding/SKILL.md:263`, `styleguide/SKILL.md:223`,
  `testing/SKILL.md:245`) reaches the rule through `project-level/task/skill/SKILL.md:40` →
  `resolve_gaps.md:4–6`, which `1267e73` changed; I followed that chain, it holds.
- `project-level/lead/answering.md:43–46` and `:58–61` — refiners now copy "that answer, its source
  and the ways the human did not choose", and "transfer resolved answers with provenance and the ways
  the human did not choose into task documents (WAY-134)". Matches WAY-154 as `1267e73` left it
  ("transfers settled answers with their sources and the ways the human did not choose (WAY-134)",
  and the removal condition) and To do 4. The answering agent's own authority is unchanged: it
  still only stores the answer and provenance under the canonical ID; the ways are already in the
  canonical question it prepares ("available ways, what each costs", `answering.md:34–35`), so the
  refiners have them to copy. No conflict with WAY-155.
- WAY-29, WAY-113: untouched by the range; the added clauses do not concern recovered decisions or
  the form of a question. Consistent.
- WAY-35: the range adds no rule to an element's skill (the guideline skills are not element
  skills; they point at the task template rather than restate its rule). But see Minor 1 for the
  report's claim on WAY-35.
- Nothing added that the task did not ask for. No foundation entry is written or changed in the
  range; the record's field "Rows of *Settlements to record* written: row 1 — WAY-134" refers to
  `1267e73`, which is right.

Coverage: my own search of the repository outside `foundations/` for the ways answers are restated
(`words and date`, `with provenance`, `answer(s) and/with (original) source/provenance`,
`transfer… resolved/settled/every`, `settled answers`, `under its question`,
`Questions to settle:`) found no remaining passage that writes or transfers an answer without the
ways, other than `answering.md:43` "Store the answer and original provenance under the canonical
ID", which is the answering agent's storage in the conversation, where the ways stand in the
question itself — correct as is.

## Findings

### Critical

none

### Important

none

### Minor

1. **The record says "WAY-35: matches" while `elements/decisions/skill/SKILL.md:36` still restates
   a rule the template now holds.** `1267e73` added to `elements/decisions/template.md:57` "`none
   considered` in *Rejected* says the human weighed no other way" and at `:62` "`none considered`
   where the human said so"; the skill keeps "`none considered` in *Rejected* is the human's
   statement" (`SKILL.md:36`). WAY-35 binds that "a skill reads the rules … from there instead of
   restating them", and its *Rejected* names exactly "rules restated in the skill next to the
   template — two copies that drift". The return step's job is to compare the entries the task names
   with the files and correct what no longer matches (`task-cycle/skill/return_step.md`, WAY-11);
   WAY-35 is named in the task's *Decisions in play*. The report
   (`reports/06-return-step-report.md`, "WAY-35: matches — the rule of the *Rejected* field stands
   in the decision template; the record-decision skill was not given it") does not mention the
   duplicate the whole-change review had raised as its Minor 1. Why only Minor: the two sentences
   agree today, and the skill's line sits in "3. Draft" where it can be read as a drafting
   instruction (who supplies the value) rather than a rule of the entry; the cost is drift later and
   a cycle record that states a full match. Fix: drop `SKILL.md:36`, or keep it and say in the
   record why it is the skill's way of working rather than a restated rule. Evidence:
   `grep -n "none considered" elements/decisions/skill/SKILL.md elements/decisions/template.md` →
   skill `:36`, template `:37`, `:57`, `:62`.

2. **The record says WAY-134 matches `task-cycle/skill/foundation_step.md`, whose paraphrase still
   gives two outcomes where WAY-134 gives three.** `foundation_step.md:22–24`: "save a decision's
   *Rejected*, which takes the ways not chosen that the row's source keeps, or `unknown`, as the
   decisions' template gives (WAY-134)". WAY-134 sentence 3 (at `1267e73`): "only the ways not chosen
   that the row's source keeps, `none considered` where the human said so, or `unknown`". The
   pointer to the template makes a careful writer correct, so no step goes wrong; a writer reading
   only this step could write `unknown` where the human said "none considered". This is the
   whole-change review's Minor 2, left as it was and counted as a match. Fix: name `none considered`
   or keep only the pointer.

No own-work check is named in the return step report; for this step the weakest point is coverage
of restatements, which I checked by my own search above (it found nothing further).

## Declined to judge

- `project-level/definition_template.md:323` — projected decisions' *Rejected* and whether project
  definitions need the same rule: projects are outside this task (the whole-change review and the
  author set it aside too).
- `elements/decisions/skill/SKILL.md:54–55` — the projected-mode line between two step bullets:
  pre-existing at `d7a205c`, not touched by `1267e73` or this range.

## Checks run

| Check | Result |
|---|---|
| `git rev-parse HEAD` in the worktree | `c6ee066e20eac62764dda9328cd04f93e826f7e5` = dispatched head |
| `git log 1267e73..c6ee066`, `git diff 1267e73..c6ee066` (whole diff read) | 1 commit, 4 files |
| `git diff --check 1267e73..c6ee066` | exit 0 |
| width of added lines (`git diff -U0`, added lines over 100 columns) | none |
| `python -B elements/common/foundation_check.py` | exit 0 |
| `python -B -m unittest test_coding_guidelines_installation test_styleguide_installation test_testing_guidelines_installation` (in `installation/`, the tests that read the three changed guideline skills at the head commit) | first run under `timeout 230` killed at 230 s (exit 124) after printing `....F`; its failure detail was lost with the kill. Rerun verbosely without a limit: exit 0, `Ran 6 tests in 227.663s`, `OK`, all six including the fifth (`test_crafted_entry_at_the_new_wrapper_path_stops_the_run_before_writing` of testing) passing. The tests assert on the skills' installation and wrappers, not on the changed prose; the change gate on `1267e73` (cycle record) passed `installation` too. The single `F` is unreproduced and not attributable to this range |
| manual: WAY-134, WAY-154, WAY-29, WAY-35, WAY-113 read whole from `git show 1267e73:foundations/decisions.md`; each corrected passage compared with them | consistent (see above) |
| manual: repository search for restatements of how answers are written or transferred (patterns above) | no remaining passage without the ways |
| manual: pointer chain guideline skills → `refine-task` step 3 → `resolve_gaps.md:4–6` | holds |
| `git status --short` after the checks | empty |

Not run: the full gate (the orchestrator's, per the handoff); `gate/run_tests.py project-level` —
no test reads `answering.md` (search of `*.py` for `answering.md` found none).

## Reaches beyond the dispatch

- `reports/04-review-report.md` (whole) — the handoff names it; it lists the Minors the return step
  was to close.
- `reports/05-return-step-handoff.md` and `cycle.md` — what the return step was asked to do.
- `task-cycle/skill/return_step.md` (whole) — what the return step owes, to judge its record.
- `elements/decisions/skill/SKILL.md:26–45`, `elements/decisions/template.md:30–66`,
  `task-cycle/skill/foundation_step.md:14–30` — to check the report's "matches" claims for WAY-35
  and WAY-134 (Minors 1, 2).
- `foundations/invariants.md` entry `skill-rule-source` (whole) — WAY-35's verification names it;
  method `review`, no script check; not changed by the range.
- `project-level/task/skill/SKILL.md:38–40` — to follow the guideline skills' pointer to step 3.
- `installation/test_coding_guidelines_installation.py:13–98` — to see what the installation tests
  read from the changed skills.
