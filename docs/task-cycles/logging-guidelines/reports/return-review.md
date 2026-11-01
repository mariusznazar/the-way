PASS 70976ac

# Review of the return step's commit — logging-guidelines

Range `d78f148..70976ac`, one commit, two files: `foundations/decisions.md` and
`product-guidelines/coding/template.md`. `git rev-parse HEAD` is the head given. Counts: 0 blocking,
1 Minor, 2 out of scope (both lines of Declined to judge). No invariant test changed. Trust boundary
and operation that cannot be undone: no, as the handoff answers; neither file is named as a trust
boundary in `foundations/part_map.md`.

## Whether the commit stands

All three corrections stand.

### 1. WAY-276 gains its precedence over WAY-275: stands, though it acts on note A

`foundations/decisions.md:8182-8183` and `:8195`.

- **The collision is real.** WAY-275 (`:8142-8145`) has a line of a case flow carry the identifiers the
  list names, and WAY-274 does not keep a secret off the list, so WAY-275 asks for what WAY-276 bans,
  for one identifier. WAY-276's *Verification* treats that state as possible: "an access token that
  stands on the list as an identifier" (`:8198`).
- **The form is what WAY-25 asks.** The entry that prevails names the other as `narrows`, and its
  binding sentence states the area, an identifier on the list that is a secret. WAY-275 does not
  narrow WAY-276, so the two do not narrow each other. WAY-276 still has three binding sentences.
- **It settles nothing new.** To do 1 and row 6 make the list an exception to the ban on personal data
  alone, D3's row says "no secret in the logs, with no exception, so an identifier that is a secret
  stays out even where it stands on the list" (`spec.md:155`), and `template.md:203-204` already said
  so. The commit gives an outcome the accepted task carries the form WAY-25 requires. That is why it
  is no collision "with no precedence recorded" that an agent may not settle (WAY-25), and no meaning
  beyond the approved document (WAY-30, WAY-114). See *Searches not found or unclear*.
- **Acting on a Minor note.** WAY-161 and `task-cycle/skill/SKILL.md:351-354` leave a Minor finding
  unfixed, and `reports/return-handoff.md:14-15` has the step take up no finding as such. The commit
  stands on another ground, which the author names truly: the fix changed WAY-275's binding part, so
  WAY-33 owed the search, whose finding must become a link, a change or a question before the change
  is accepted, and `agent-instructions/README.md:30-31` says the same. A review's Minor grade does not
  release that duty; it says how much the defect matters, not that the foundation may keep it.
  WAY-161's rationale is a round spent on polish, and no round ran for this: the step was taken anyway
  and reviewed anyway. WAY-161's violating example, a fix run for Minor findings alone, does not
  describe it. The author also says what to revert should the orchestrator disagree.

**For the request.** Note A still goes to the request in the reviewer's words (WAY-161), but it no
longer describes the head: the relation it asks for is written. Its anchor `:8194` is now `:8195`. The
line the commit adds moves anchors in `foundations/decisions.md` below `:8182` by one; of those in the
reports, only note A's is affected. `reports/return-step.md` gives the shift for the template only,
where there is none.

### 2. `task-cycle` added to the *Scope* of WAY-168 and WAY-170: stands

`foundations/decisions.md:4622` and `:4702`.

- WAY-21 has a *Scope* name the parts a decision governs, so that the decisions of a change are found
  from its files. Both sentences say what the review of a change does, and `task-cycle/review/SKILL.md`
  now cites both, as To do 5 requires. `task-cycle/**` is that part in the map.
- The author's count holds. The file cites eleven entries, WAY-148, 150, 161, 168, 170, 213, 219, 220,
  221, 255 and 263. Each now has `task-cycle` in its *Scope*, and at `d78f148` only these two lacked it.
  WAY-150's stands on the *Scope*'s second line.
- The only entries the change newly cites in `task-cycle` or `project-level` are WAY-168, WAY-170 and
  WAY-277, and WAY-277 already names `project-level`.
- No binding sentence moves, and `foundation_check.py` accepts the part. The cost is that a change to
  `task-cycle` now reads two more entries, which is the purpose. Both alterations are in the author's
  table with their sentence for the request, so the request must list them as entries the change
  alters (`agent-instructions/README.md:70`).

### 3. "never read off the code" removed from the template: stands

`product-guidelines/coding/template.md:311-313`.

- The clause contradicted `template.md:211`, WAY-274 and `settle.md:52`, all of which have the list
  written at adoption from what the product has in its code or its plan, and it used `read off`
  against `foundations/glossary.md:121-123`.
- Nothing is lost. What WAY-274's violating example forbids, a list regenerated from the code, is still
  carried by "the product's promise and no inventory of its code" (`template.md:211-212`), and WAY-225's
  ground stands.
- "Written from the task's settlements" is right for the section's reader, the author of coding
  guidelines in a task's cycle: `settle.md:52-54` makes the list a settled matter of that task. An item
  added later is governed by `template.md:212-215`, and `:314` does not reach it, since using a meaning
  a decision carries takes no approval (WAY-172).
- No use of `read off` remains in `product-guidelines/coding/`, searched with line breaks read as
  spaces. The task's To do 3 and its answers 1 and 12 are unaffected.

## Findings

### Critical

None.

### Important

None.

### Minor

#### 1. The departure table names one of the two rules that stop being narrowed

`product-guidelines/coding/template.md:273`, the row of `### Secrets and personal data`, the rule whole:
"`### Recording a failure` is no longer narrowed, so an original error may write what it quotes,
secrets included".

WAY-276 now narrows WAY-275 too (`foundations/decisions.md:8195`), so dropping the rule whole also frees
`### Identifiers in log lines`: an identifier on the list that is a secret would then go into every
line that carries it. The row, the place the skill sends a human to hear what goes
(`settle.md:42-44`), names only the first effect, and the commit made it incomplete without touching
it. The rule's own closing words, `template.md:207-208`, likewise name only `### Recording a failure`.

It is Minor, and WAY-263 does not make it Important. Nothing in the row is false, it does not say
"only", its first item already says the ban on secrets goes, and `template.md:203-204` carries the
outcome WAY-276 requires, so the template neither restates the entry differently nor fails to do what
it asks. Evidence: the two passages read together; `git grep` finds the wording in no other file.

Fix, if taken: "`### Recording a failure` and `### Identifiers in log lines` are no longer narrowed, so
an original error may write what it quotes, secrets included, and a line may carry a listed identifier
that is a secret".

## The author's own-work check

`reports/return-step.md` names no requirement for it, only that its script reported no problems. It
was weakest at the WAY-25 and WAY-161 question above, which a script cannot judge; the report raises
that question itself and gives the revert. See *Searches not found or unclear* for what was not read.

## Declined to judge

- `product-guidelines/styleguide/audit.md:18` ("A palette read off the code") and
  `product-guidelines/styleguide/starting_rules.md:15` ("never read off it") may use `read off` as the
  template did. They predate this change and belong to another discipline, so they lie outside the task.
- Whether other entries a part's files cite should name that part in *Scope*, the question the author
  raises of `product-guidelines`. WAY-21's reach beyond these two entries is outside the task.

## Checks run

| Command or method | Result |
|---|---|
| `git rev-parse HEAD` | `70976ac…`, the head given |
| `git log`, `git show --stat`, `git diff d78f148 70976ac` | one commit, two files, the three corrections and nothing else; matches the author's table |
| `python -B elements/common/foundation_check.py .` | exit 0, 0 errors |
| `git diff --check d78f148 70976ac` | exit 0 |
| `python -B gate/run_tests.py instruction-files` | exit 0, 104 tests, 5 skipped |
| `python -B gate/run_tests.py agent-instructions` | exit 0, 18 tests |
| `git grep` of the IDs in `task-cycle/review/SKILL.md`, with each entry's *Scope* | eleven entries, each with `task-cycle` |
| `git diff ea4694e 70976ac -- project-level task-cycle`, IDs on changed lines | WAY-168, WAY-170, WAY-277 |
| Multi-line search `read\s+off` in `product-guidelines/` | two hits, both in `styleguide/`, which also serve as the positive control; none in `coding/` |
| `git grep` of WAY-275 and WAY-276 outside and inside the log | no other text states a relation between them or goes stale, save the row of the Minor finding |
| Manual: the new sentence of WAY-276 against To do 1, row 6, answers 3 and 10, D3 and E6, WAY-25 and WAY-275 | as above |
| Manual: `reports/return-step.md` against the diff, including its sentences for the request | agrees, save the anchors noted under correction 1 |
| `git status --short` before and after | clean |

Not run: the full suite, the cycle's own run; `gate` and `task-cycle`, which the author reports at exit 0
and I did not repeat, since the diff changes one sentence, one relation, two *Scope* lines and one
clause; a test of how an agent acts on the text, as in the earlier reviews.

## Reaches beyond the dispatch

- WAY-11, `foundations/decisions.md:320`: what the return step is bound to correct.
- WAY-114, `:2450`: whether a question to the human was owed.
- WAY-161, `:4266`: what a Minor finding's being left unfixed means.
- WAY-272, `:8017`: the entry WAY-276 already narrowed, for the parallel form.
- The *Scope* lines of WAY-148, 150, 161, 210, 213, 219, 220, 221, 255, 263, 268 and 277: to check the
  author's count and the entries the change newly cites.
- `foundations/glossary.md:13-23`, `binding part` and `binding sentence`: the author's "no binding part
  moves".
- `elements/decisions/template.md:40-169`: fields, binding sentences, relations and precedence.
- `elements/glossary/skill/decide_entry.md`: the route `return_step.md` names for a term used against
  its entry.
- `foundations/part_map.md`: `relation-model`, `project-level`, `task-cycle`, `product-guidelines`.
- `task-cycle/skill/SKILL.md:335-354`, `reports/return-handoff.md`, and `product-guidelines/coding/settle.md:30-59`:
  the step's dispatch, the end of a review, and what the human is told at a departure.

No note and no repository of any product was read.

## Searches not found or unclear

- Unclear: whether an agent may write a precedence at all. WAY-25 has "a human" record one and
  `agent-instructions/README.md:32-34` sends "two decisions colliding with no precedence written" to
  Mariusz. I read the outcome here as already written, in substance, in row 6 and WAY-276, and the
  commit as supplying the form, for Mariusz to accept at the merge through the sentence for the request
  (WAY-114). The other reading would have had the step ask first. The result is the same text, so I do
  not grade it, but the sentence for the request should stay as the author wrote it, naming WAY-275.
- Unclear: whether a collision over a state the rules forbid needs a relation, as `whole-review-2.md`
  and the author both ask. I read it as yes, since WAY-274 does not keep a secret off the list.
- Unclear: WAY-161 speaks of the review of the whole change, and nothing says what a return step's own
  duty does when it lands on a Minor finding's matter. I judged by the ground, not the coincidence.
- Unclear: whether *Scope* is in an entry's binding part; the glossary's definition does not settle it
  field by field. The author's "no binding part moves" holds for what a decision requires. If *Scope*
  did count, no rule of guidelines would have anything to bring in line (WAY-169).
- Unclear: `task-cycle/skill/return_step.md:10-11` sends "a term used against its entry" through
  `record-glossary-term`, whose `decide_entry.md` has no such case: it starts from a word with another
  meaning or two meanings. The author corrected the use and wrote no entry, which fits the outcome. The
  report does not show that it listed the word's uses, and it calls `read off` "the one term used
  against its entry", true of this change's text; see *Declined to judge* for the rest.
- Not read: the author's `own_check.py` and `scope_check.py` in the session's scratchpad, since the
  handoff keeps me to this worktree's tracked files and the cycle's directory. The scope check is
  reproduced above; the own-work script is unverified.
- Not checked: the author's "25 of its 65 cited entries" for `product-guidelines`. Nothing in the
  verdict rests on it.
