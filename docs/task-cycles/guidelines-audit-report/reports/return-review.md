FAIL aee18e4

# Review of the return step — guidelines-audit-report

Range `0ee0cd9..aee18e4`, one commit, one file, one sentence of WAY-281. `git rev-parse HEAD` in the
worktree is `aee18e47a0de3d49f5f85829d4a7b9460694b4b4`, the head given. Blocking findings: 1. Minor: 2.
Out of scope: 1 (the line of *Declined to judge*). No plan, so no finding comes from a slice.

**The correction itself is sound.** Adding "that block" keeps row 2's meaning: question 5 cites
`product-guidelines/coding/trial_run.md:17`, which at `2f51e6c` already reads "count the files that
break the rules that block", spec decision 11 says the same, WAY-203 says a rule among the examples
binds no code, and the wording is WAY-205's own ("the rules of its linter's set that block").
WAY-281 is new in this request, so WAY-30 does not arise, and `foundation_step.md` raises no question.
Acting on its own comparison despite the review's finding 4 is the return step's duty, as the
handoff told it. What fails is what the correction left behind: it gave the entry a qualification
that a file of the same request still lacks.

## Findings

### Critical

None.

### Important

**1. The correction gives WAY-281 a qualification that `audit_end.md` repeats the entry without.**
`product-guidelines/audit_end.md:13-16`, against `foundations/decisions.md:8371-8373`.

- What is wrong: `audit_end.md` says what each audit brings to the list: "coding's with the files
  marked `do not copy` and the trial run's reports, testing's with the trust boundaries at which a
  test of refusal is due and none exists." Those are the two things WAY-281 says the list "also
  holds", and the testing clause carries the entry's qualification nearly word for word. The coding
  clause does not: the trial run gives reports of every rule of the set, the blocking ones and those
  that go among the examples (`trial_run.md:11-16`). The next section then says "Merge every finding
  into a cause" and "each finding belongs to one cause" (`audit_end.md:21-22`), so read as it stands,
  every report of the trial run is a finding and belongs to a cause. That is the width the entry had
  before `aee18e4` and no longer has, and it contradicts `trial_run.md:23-24`, "yield no cause".
- Why it matters: this is the disagreement the return step set out to close, moved to another file.
  Its report's reason applies unchanged: an agent comparing work with the entry alone finds a file
  whose words reach reports the entry leaves out. Before this commit the line and the entry agreed;
  the commit made them disagree, and `return_step.md` has the step correct in the same change
  "whatever no longer matches".
- Why Important and not Minor: WAY-263 grades as Important a changed file that "repeats the entry
  while broadening it or dropping a qualification", and names grading it Minor "because the code or
  repeated account says something different" as its violation. The review's reason for leaving
  finding 4 Minor was that the file "drops no qualification of the entry"; after `aee18e4` this line
  drops one. What can be said against it: `coding/SKILL.md:114-115` has `trial_run.md` read first, so
  an agent on that path holds the narrower sentence when it arrives. That lowers the likelihood, not
  the grade: WAY-263's *Rationale* is about the second account standing for later work, and
  `audit_end.md` is the file that describes what enters the list.
- Evidence: the return step's table compares WAY-281 with `audit_end.md`, "Merge into causes", and
  the file's opening only against WAY-280 (`reports/return-step.md:13-14`), so its comparison did
  not reach this line. `git log 2f51e6c..aee18e4 -- product-guidelines/audit_end.md` shows the file
  last changed in `ac27d26`, before the correction.
- Fix: one clause, "the trial run's reports of the rules that block". No entry changes.

### Minor

**2. WAY-281 gains the qualification and none of the reasoning for it.**
`foundations/decisions.md:8372`, `foundations/decisions.md:8388-8396`.

- What is wrong: the *Rationale* speaks of "a wide debt a linter reports" and never says why the
  rules among the examples stay out. The reason stands in `trial_run.md:23-24`, in WAY-203, which the
  entry does not name, and in spec decision 11, under the ignored `.runs/` directory. WAY-27 has an
  entry carry its whole reasoning, and the decisions' template gives *Rationale* to "the agent in a
  borderline case".
- Why it matters: the borderline case is real. By `trial_run.md:13-14` a rule with one report that
  leads to no change goes among the examples, so its other, sound reports yield no cause. An agent
  or human meeting that has to reach WAY-203 unaided to see why. The entry's sentence is still right.
- Why Minor: nothing is done wrongly by the text, and WAY-263 does not reach a missing reason. The
  *Verification* pair is optional (`elements/decisions/template.md:172`), so its silence on the
  exclusion is no breach.
- Evidence: reading of the entry. One clause closes it: such a rule binds no code (WAY-203), so
  nothing breaks it.

**3. The fill of the top and the two facts of a fix bind every later audit and stand in no entry.**
`product-guidelines/audit_end.md:76-86`, `product-guidelines/audit_end.md:90-93`,
`reports/return-step.md:60-62`.

- What is wrong: the handoff asks for a judgment of *Choices that bind after the merge*. Spec
  decisions 2 and 9 pass the plan test of WAY-36, since neither ends with this work. Each was a
  choice among named options (hours, points, a ratio; always five, the agent's judgement), and
  `task-cycle/record_template.md:98-100` knows only two places for a choice: the foundation, or a row
  of the questions table. A later change could turn "the next cause while it weighs as much as the
  one before it" into "always five" and contradict no entry, since WAY-283 holds only the bounds,
  and the reasons for rejecting that stand only in the spec under `.runs/`.
- Why Minor and not a missed requirement: the spec's "No other entry" is a reviewed instruction, the
  rules stand in the one file every audit reads, they lie inside what WAY-282 and WAY-283 state, and
  WAY-282's *Verification* already uses `one file` and `several parts`. Decision 2 is the weaker
  case; decision 9 is the one I would write, as it decides how a requirement of the human's To do 6
  is read. Nothing is wrong today, the cost of a wrong rule is one sentence, and the report says the
  matter openly instead of passing it over.
- Evidence: reading of the passages named; the spec's *Foundation entries* lists no glossary term,
  invariant, environment fact or change of the part map, and does not weigh these two choices as
  decisions.

## Declined to judge

- A rule among the examples whose other reports are worth a change leaves those reports out of the
  list: spec decision 11 and WAY-203 settle it, this range did not bring it, and question 5 does not
  reach it.

## Checks

| Check | Result |
|---|---|
| `git rev-parse HEAD` | `aee18e47a0de3d49f5f85829d4a7b9460694b4b4`, the head given |
| `git diff 0ee0cd9..aee18e4`, `git show --stat aee18e4`, `git log --oneline -5` | one commit on `0ee0cd9`, `foundations/decisions.md`, 2 insertions, 2 deletions, read whole |
| `git diff --check 0ee0cd9 aee18e4` | exit 0 |
| `python -B elements/common/foundation_check.py .` | exit 0, 0 errors |
| `python -B gate/run_tests.py elements/common` | exit 0, 109 tests |
| `git grep -l -E "WAY-281|rules of a linter" -- "*.py"` | no hits: no test reads the sentence, and no invariant test changes |
| `git show 2f51e6c:product-guidelines/coding/trial_run.md` | line 17 reads "the rules that block", the citation of question 5 |
| `git grep -i -E "linter|trial run|reports"` over `audit_end.md`, the coding skill's files and `guideline_findings.md`; `git grep -i "linter's set"` over `product-guidelines`, `project-level`, `task-cycle`, `elements` and the part map and invariants | finding 1, and no other restatement of what enters the list |
| `git log 2f51e6c..aee18e4 -- product-guidelines/audit_end.md` | last changed in `ac27d26` |
| `git status --short` | clean before this report; no tracked file changed |
| Report's claims on the review's finding 5, `elements/glossary/template.md:42-45` and `foundations/part_map.md:157-159`, by reading | each as the report states it |

Not run, each with its reason:

- `python -B gate/run_tests.py`, the full suite: the cycle's own run.
- A trial of an agent following this text: no such tool exists in this cycle.

## Reaches beyond the dispatch

- `foundations/decisions.md`: WAY-263, for the grade; WAY-36 and WAY-27, for the duty and for finding
  2; WAY-201, WAY-280, WAY-282 and WAY-283, each whole, for what stands beside WAY-281.
- `task-cycle/skill/foundation_step.md`, `task-cycle/skill/SKILL.md:335-340` and
  `task-cycle/record_template.md:98-100`: how the return step writes and what a choice becomes.
- `elements/decisions/template.md`, whole, and `elements/common/skill/SKILL.md:50-84`: what makes an
  entry, and the reader of each field.
- `agent-instructions/README.md`, as `AGENTS.md` asks.
- `product-guidelines/audit_end.md`, `coding/kinds.md`, `coding/SKILL.md:108-142`,
  `coding/settle.md:58-68`, `coding/task_document.md:30-54`, `testing/audit.md:12-19`: what restates
  the entry.
- `foundations/glossary.md:31-35`, `elements/glossary/template.md:38-46`,
  `foundations/part_map.md:155-160`: the report's claims.
- `spec.md`, decisions 2, 9, 11 to 14, *Foundation entries*, *Left to the maker*;
  `reports/author.md`, `reports/return-handoff.md`, `reports/spec-review-2.md:40-59`: what the choices
  of finding 3 rest on and what the step was told.

## Searches not found or unclear

- **What "a choice that binds after the merge" covers** where the choice stands in the text of a
  skill: `return_step.md`, `record_template.md:98-100` and WAY-36 do not say, and read literally they
  reach every sentence of a skill. I judged the two choices one by one, in finding 3.
- **`debt` where a set is only proposed.** The report says the rules that block "are rules the
  product's foundation holds". That is so once step 4 adopts the split; at the audit, on a first
  adoption, they are a proposal. WAY-281 keeps "debt" for what it reports then. No agent would act
  otherwise, so no finding.
- **`audit_end.md:131`, "for a linter's rules the number of files",** also lacks "that block". I read
  it as the label of a kind of cause and not as saying what enters the list, so it stands outside
  finding 1.
- **The Glob and Grep tools** were not used for any claim that something is absent; those rest on
  `git grep`.
