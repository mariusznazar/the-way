# Correction report — human's remarks on PR #53, task `rejected-from-refinement`

**Status:** done

Worktree `C:\Storage\repos\the-way\.runs\worktrees\rejected-from-refinement`, branch
`task/rejected-from-refinement`, from head `718c9dc`. Variant: a correction for the human's remarks
(`reports/09-correction-remarks.md`, Mariusz, 2026-10-29, „popraw proszę”).

## Commits

- `03411a5` fix: leave the none considered rule to the decision template and name all three
  Rejected values in the foundation step — `elements/decisions/skill/SKILL.md` (+0 −1),
  `task-cycle/skill/foundation_step.md` (+3 −3).

## Each remark, as made, and how

1. **Remark:** "`elements/decisions/skill/SKILL.md:36` now restates a rule the template holds. …
   Fix: drop the skill's line 36 (the skill reads the rule from the template)."
   **How:** removed the bullet "`none considered` in *Rejected* is the human's statement." from step
   3 (Draft) of the skill. The rule now stands only in `elements/decisions/template.md` ("`none
   considered` in *Rejected* says the human weighed no other way; `unknown` says nobody knows what
   was weighed."). The skill's opening still names the template and `elements/common/` as the
   source of the rules of an entry.
2. **Remark:** "`task-cycle/skill/foundation_step.md:22–24` paraphrases the exception without
   `none considered`. … Fix: name all three or drop the paraphrase and keep only the pointer."
   **How:** named all three. The passage now reads: "— save a decision's *Rejected*, which takes the
   ways not chosen that the row's source keeps, `none considered` where the human said so, or
   `unknown`, as the decisions' template gives (WAY-134)". I kept the paraphrase rather than only
   the pointer, so that a writer reading only this step still sees why no question arises. I
   changed nothing else.

## Return step (limited to what the remarks touch)

- **WAY-35 vs `elements/decisions/skill/SKILL.md`:** matches. The skill no longer restates a rule
  of an entry that the template holds. The invariant `skill-rule-source` still holds: the skill
  names its template and `elements/common/` as the source.
- **WAY-134 vs `task-cycle/skill/foundation_step.md`:** matches. The step now gives the same three
  outcomes as sentence 3 of WAY-134: the ways the row's source keeps, `none considered` where the
  human said so, or `unknown`. It points to the decisions' template.
- **Not changed:** `project-level/definition_template.md:324` still says "`none considered` being
  the human's statement". It covers projected decisions of a project definition, which is outside
  this task and these remarks, and the remarks say nothing else is to change.

## Checks

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` | 0 (0 errors) |
| `python -B gate/run_tests.py agent-instructions` (a skill's `SKILL.md` changed) | 0 (OK) |
| check of added lines over 100 columns (`git diff -U0`) | none |

Not run: the full gate, which is the orchestrator's. No test written, because both edits are
prose.
