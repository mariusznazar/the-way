PASS 03411a5d91724e1c9f90efa05fc88aea39d71108

# Review of a correction — task `rejected-from-refinement`, PR #53

Range `718c9dc9ad0f728761c7c9ce2eee0a69e6c05b48..03411a5d91724e1c9f90efa05fc88aea39d71108`, one
commit, 2 files (+3 −4). `git rev-parse HEAD` in the worktree is the head given. Method:
`task-cycle/review/SKILL.md` with `task-cycle/review/fix.md` (correction variant); the human's
remarks (`reports/09-correction-remarks.md`) take the findings file's place.

## Findings

- Critical: none.
- Important: none.
- Minor: none.

Blocking: 0. Minor: 0. Out of scope: 0 (one line under Declined to judge).

## Each remark, as made or not

1. **`elements/decisions/skill/SKILL.md:36` restates a rule the template holds — made.** The
   bullet "`none considered` in *Rejected* is the human's statement." is gone from step 3 (Draft);
   step 3 now holds only *Based on* and *Verification*. The rule stands once, in
   `elements/decisions/template.md:57–58` ("`none considered` in *Rejected* says the human weighed
   no other way; `unknown` says nobody knows what was weighed.") and, for rows of *Settlements to
   record*, `template.md:59–64`. The skill's opening (`SKILL.md:8–11`) still sends the writer to
   the template and `elements/common/rules.md` for every rule of an entry, so nothing the skill
   needs is lost. This now matches WAY-35 (rule in the template, never restated in the skill) and
   its *Rejected* ("rules restated in the skill next to the template — two copies that drift").
   `git grep "human's statement"` finds no other copy in the skill or the decisions element.
2. **`task-cycle/skill/foundation_step.md:22–24` paraphrased the exception with two outcomes —
   made, by the first of the two fixes offered (name all three).** It now reads "save a
   decision's *Rejected*, which takes the ways not chosen that the row's source keeps, `none
   considered` where the human said so, or `unknown`, as the decisions' template gives (WAY-134)".
   The three outcomes and their order match WAY-134 (`foundations/decisions.md:3201–3203`: "only
   the ways not chosen that the row's source keeps, `none considered` where the human said so, or
   `unknown`") and the template (`template.md:59–63`) word for word in the shared part; the pointer
   to the template stays. The rewrap of the following line ("two decisions colliding with no
   precedence recorded raise one too (WAY-25). The writer never writes …") moves words only; its
   text is unchanged.

"Nothing else is to change": the diff touches only these two passages. Confirmed from `git show
03411a5`.

## Review of the correction's diff (section 2)

- What would make it wrong: (a) the deleted skill line being the only place a writer of a decision
  meets the `none considered` meaning — it is not, the template holds it and the skill points
  there; (b) the new wording of the foundation step diverging from WAY-134 sentence 3 — it does
  not; (c) the edit giving the writer a reason to ask the human for `none considered` — the
  sentence still says the *Rejected* value is saved from the question rule, so no question arises,
  as WAY-134's *Verification* (violates: "blocks the request to ask the human for them") requires.
- No test asserts either changed passage (`git grep` over the tracked tests for "human's
  statement" and for the foundation step's sentence finds none); the edits are prose, so no test
  is expected.
- No foundation entry is changed by the correction; no invariant test changed.
- No trust boundary and no operation that cannot be undone.
- The author's return step names `project-level/definition_template.md:324` ("`none considered`
  being the human's statement") as left unchanged; I agree it lies outside the remarks, which bind
  "nothing else is to change" — see Declined to judge.

## Declined to judge

- `project-level/definition_template.md:324` still glosses `none considered` as "the human's
  statement" for projected decisions of a project definition — outside the two remarks and this
  correction; the remarks forbid other changes.
- `elements/decisions/skill/SKILL.md:31–32` (*Based on*: "what is not yet known, or the decider's
  own motive, is no source outside the product") restates `elements/decisions/template.md:50`, the
  same WAY-35 pattern as remark 1 — pre-existing on `foundations` (`c1fc8f4d`, 2026-10-21),
  outside this task and the remarks.

## Checks

| Check | Result |
|---|---|
| `git rev-parse HEAD` | `03411a5d91724e1c9f90efa05fc88aea39d71108`, the head given |
| `git diff --check 718c9dc..03411a5` | exit 0, no output |
| `python -B elements/common/foundation_check.py` | exit 0, "0 errors" |
| Added lines over 100 columns (`git diff -U0 … \| grep '^+' \| awk 'length>101'`) | none |
| Manual: `git grep -n "none considered"`, `git grep -n "human's statement"`, `git grep -n "ways not chosen that the row"` | the rule's only remaining copies are the template, WAY-134, the foundation step (pointer plus the three values) and the out-of-scope `definition_template.md:324` |
| Manual: compared the new foundation-step sentence with WAY-134 (`decisions.md:3188–3208`) and `template.md:57–64` | same three values, same order |

Not run: test directories (`gate/run_tests.py`) — the dispatch reserves them to the orchestrator's
gate running in this worktree.

## Reaches beyond the dispatch

- `task-cycle/review/fix.md` — named by the review skill for a correction.
- `agent-instructions/README.md` — named by the dispatch as governing the-way.
- `elements/decisions/skill/SKILL.md` lines 1–50 and `task-cycle/skill/foundation_step.md` lines
  10–27 — the context of each changed passage.
- `git blame` of `elements/decisions/skill/SKILL.md:31–32` and `template.md:50` — to tell whether
  the second Declined-to-judge line is pre-existing.
- `git grep` for "none considered", "human's statement" and "ways not chosen that the row" — to
  find other copies of the rule and tests on the changed text.
