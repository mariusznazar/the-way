# Report — the return step

**Status:** `done with concerns` — the comparison is finished and one commit corrects what no longer
matched. The commit changes the tree, so the gate on `9849f4b` no longer covers it, and three matters
go to the request (see *Concerns*).

## Files and commits

| File | Added | Removed |
|---|---|---|
| `foundations/environment_facts.md` | 6 | 0 |
| `foundations/decisions.md` | 3 | 5 |

Commit: `6f34b64` `docs: hold the GitHub source of WAY-267 as an environment fact`, on
`task/unsettled-technology-returns`, above reviewed head `9849f4b`. Not pushed.

## Return step

- **Foundation compared with code:** WAY-121, WAY-122, WAY-123, WAY-135, WAY-137, WAY-138, WAY-265,
  WAY-266, WAY-267 and the term `reserved choice`, against the files of the change; WAY-114 and
  WAY-160, which the search found; the task's *Decisions in play*; the part map of the touched parts.
  Two things no longer matched, both in WAY-267, both corrected:
  1. *Based on* quoted a page of GitHub's documentation that WAY-90 requires as a fact entry (see
     *The GitHub citation*).
  2. *Rationale* said "the tree equals the base the cycle started from". `reserved_return.md:45-47`
     also gives the commit that moved the pin, and `:85-86` gives the tree the request already holds
     after a correction. The sentence now says both. It explains the rule and changes no meaning.
- **Decisions written or changed:** WAY-267 changed (*Based on*, *Rationale*); its binding sentences
  and *Verification* are untouched.
- **Invariants written or changed:** none. No rule of the task, a decision or the human asks for one.
- **Environment facts:** `github-closed-pull-request-branch`, new.
- **Glossary terms:** none. `reserved choice` is used as its entry gives; `open design choice` still
  holds, a reserved choice being one such choice with the exception WAY-135 writes. "Note" and "run"
  keep their usual sense.
- **Part-map changes:** none (see *The part map*).
- **Projected entries written whole or in part:** none carried.
- **Rows of *Settlements to record* written:** none by this step; the foundation step wrote all three:
  row 1 → WAY-265; row 2 → WAY-266; row 3 → WAY-121, WAY-122, WAY-123, WAY-135, WAY-137, WAY-138.
  None was missed.

## Meaning of each entry written or changed, in the task document's language

| Entry | Meaning |
|---|---|
| `github-closed-pull-request-branch` (new) | Na GitHubie skasowaną gałąź źródłową zamkniętego pull requesta można przywrócić. |
| WAY-267 (changed, no change of meaning) | Znaczenie zostaje bez zmian: źródło GitHuba stoi teraz jako fakt środowiska, a uzasadnienie dopowiada commit przesuwający przypięcie i przypadek korekty. |

For the request's sentence on WAY-267 as a whole, use the one in `reports/fix.md:90-94`, which
replaces `reports/foundation.md:23`. This step leaves it valid.

## The GitHub citation

The handoff asks whether the source is held as the foundation requires. **It was not; it is now.**

- WAY-90 and the template of facts name a fact entry for a citation that "once it stopped being true,
  would call the decision into question — a finding about agents or models, the behaviour of a tool
  the process uses", and quote "every other citation with its source, as a precedent or a past
  event". What a host does with a closed request's branch is the behaviour of a tool, and neither a
  precedent nor a past event.
- WAY-267's own *Rationale* says the removal "relies on" this behaviour. Removing the branch on the
  host is the one step of the decision that git cannot bring back, so if the behaviour ended the
  decision would have to be weighed again. The same host has a fact for another of its behaviours,
  `github-private-repository-response`, named by WAY-84.
- `reports/foundation.md` chose the quotation because the spec's cost "falls short of calling the
  decision into question" and because "no such entry is planned". The first is a fair reading I do
  not share: that text says the next step survives, not that the removal stays sound. The second is
  no reason (WAY-01, WAY-11).

The form: a page the publisher moves to newer text is no edition, so the source is a page without
editions, with its closest archived copy that already exists, found through the archive's index of
captures. No copy was made for the entry. The passage and its heading were compared with both pages.

## The part map

- `project-level`, `task-cycle`, `decisions`, `glossary`, `agent-instructions`: responsibilities, files
  and trust boundaries hold. `project-level/**` and `task-cycle/**` take the three new files; no
  trust-boundary file changed.
- `elements-common`: no file of it changed, so nothing to compare.
- Dependencies: `task-cycle` now names `project-level/technology/reserved_choices.md`, which it may
  depend on. The added lines of `project-level` name no `task-cycle` path, as at the base. The added
  lines of `elements/decisions/template.md` speak of the technology step by name and name no file.
- `environment-facts` is touched only by the new entry; its part entry holds.

## Entries compared and found true

- **WAY-265:** `task_run.md`, `SKILL.md` step 0, `project-level/task/template.md`.
- **WAY-266:** `reserved_choices.md`, `resolve_gaps.md`, the three stage pointers.
- **WAY-267:** `reserved_return.md`, `correction.md`, `draft.md`, `lead/skill/SKILL.md`; the
  plan-state test shows the conflict staying until the ref goes.
- **WAY-121, 122, 123, 137, 138:** `research.md`, `settle.md`, `task_run.md`, the decisions' template.
- **WAY-135:** `implement-task`'s design section and `reserved_return.md`.
- **WAY-114:** WAY-266 names it `narrows` and states the area, as WAY-25 gives.
- **WAY-160:** `reserved_return.md` names the gate as not run, and the entry's heading concerns the
  finished change.
- **Task's *Decisions in play*:** WAY-01, 30, 100, 106, 118, 124, 134, 154, 155, 156, 165, 166, 185,
  186, 210, 211, 219, 227, 248, 249 and `project-technology-record`, each read whole; plus WAY-142,
  147, 153, 162, 163 and 229, which the change bears on. No correction needed. `start.md`, `close.md`,
  `list.md`, `running_product.md` and the definition template's Technology section stay true of a run
  at a definition.

**Choices that bind after the merge (WAY-36):** the spec's five decisions and the record template
were read for one with no entry. None found: what binds at the level of a decision stands in WAY-265
to WAY-267, and the rest is method in the skills or a row of the questions table (Q3 to Q7, P1 to P9).

**A source the change rests on, judged no fact:** the behaviour of `git fetch --prune` and
`git branch -dr` (WAY-267's *Verification*, `lead/skill/SKILL.md`). The change cites no page for it.
Were `--prune` to stop removing those refs, the ban would simply be unneeded and removal by name
would still stand, so nothing is called into question. The behaviour is also observed: the test in
`project-level/test_plan_state.py` runs real git, and the review's `--prune` mutation failed it.

## Checks

| Check | Exit code | What it showed |
|---|---|---|
| `python -B elements/common/foundation_check.py .` (edited tree, before commit) | 0 | 0 errors |
| same, with WAY-267's *Based on* set to `github-closed-pull-request-branch-x` for a moment (negative control) | 1 | `foundations/decisions.md:7720: ... names no fact`; 1 error |
| `cmp foundations/decisions.md <backup>` after restoring | 0 | restored byte for byte, before the commit |
| `python -B <scratchpad>/verify_fact.py` | 0 | the committed passage and its place stand in the live page and in the archived copy; a false passage is found in neither |
| `python -B gate/run_tests.py elements/common` | 0 | 109 tests OK |
| `git commit` | 0 | `6f34b64` |
| `python -B elements/common/foundation_check.py .` (on `6f34b64`) | 0 | 0 errors |

Not run: the gate, which is the orchestrator's. `installation` tests, which also name the foundation
files: left to the gate. The tree changed after the gate's run on `9849f4b`, so that run does not
cover `6f34b64`. No test was written: this step writes entries and no code. Nothing here was checked
by running an agent on the changed texts.

## Own-work check (section 3)

- **Requirement most likely unmet:** that the new fact is held as its template requires, the passage
  word for word in both addresses, and that WAY-267's name for it actually resolves.
- **Check:** the script above reads the passage out of the committed entry and compares it with both
  fetched pages, with a false passage as control; the identifier was broken for a moment to see the
  foundation check fail.
- **Showed:** both hold, and the check fails for the right reason, naming the identifier at
  WAY-267's *Based on*.

## Reaches beyond the dispatch

- `foundations/decisions.md`, whole: WAY-142, 147, 153, 162, 163, 229, for the change's plan-row and
  blocked-request rules. By their binding sentences only, not whole: WAY-27, 33, 36, 64, 73, 82, 84
  and 90, for what the fact requires; the template of facts gives the same rules in full.
- `foundations/invariants.md`: `project-technology-record`, `return-step-record`, `skill-rule-source`.
- `elements/environment-facts/` (template, `read.md`, `decide_entry.md`, `draft.md`, `write.md`),
  `elements/decisions/template.md` and skill, `elements/common/rules.md`, `way_of_working.md`, as
  writing an entry requires.
- `reports/whole-review.md`, `whole-review-2.md`, `fix.md`, so as not to turn a Minor finding into an
  entry.
- The GitHub page and the archive's index of captures, fetched to write the fact.

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| The GitHub source written as a fact entry | The quotation left in *Based on*, as `reports/foundation.md` chose: no new entry, but a tool's behaviour stays out of the facts WAY-33 searches | One fact too many; it goes as WAY-73 gives when nothing names it |
| *Rationale* of WAY-267 corrected for the pin and a correction | Left as it was: no edit, but the sentence says less than the file | One clause a reader may find needless |
| WAY-267's "ends with its attempt discarded" left unchanged | Rewording it for a choice found at step 4: the review's note calls it vacuous rather than false, and Minor findings are not fixed here | None seen |
| No fact for `git fetch --prune` | One more fact, for a citation no entry makes | A reader finds no source for the ban; the behaviour is observed in a test |

## Concerns

1. **The tree changed after the gate.** WAY-160 asks for the gate again after the return step changes
   the tree, and WAY-162 gives the return step's commits a code review of their own. The change is
   text in two foundation files.
2. **Row 1 is narrower in WAY-265 than in its wording, for the human to see at the merge.** Row 1 reads
   „człowiek może go uruchomić dla każdego wyboru”, while WAY-265 reads "any choice save one a
   projected decision of an approved definition settles". The narrowing comes from To do 6 („a
   zatwierdzona definicja zostaje nietknięta”) and Q5, and the whole-change review saw it, so this is
   no blocked question: the task itself carries both. It is named so that the request shows it.
3. **Two readings already raised stay for the request:** WAY-266's `narrows WAY-114`, a precedence
   neither the task nor the spec lists (WAY-25 has a human record one), and the reading that WAY-160
   does not reach a draft with no code.

The review's Minor findings stay in the request as the reviewer wrote them; none became an entry.

## Limits of this comparison

The comparison of the skills with the entries rests on reading, not on an agent run. Of the decisions
whose *Scope* names a touched part I read those listed above, not all of them; a collision with one
not read could stand unseen, the same limit the whole-change review states. This step did not repeat
the search of the whole foundation for the entries already written, only for the new fact (WAY-33).

## Searches not found or unclear

- **Other hosts.** WAY-267 speaks of "a host", and the fact covers GitHub alone. Whether another host
  restores a closed request's branch was not looked for; the decision's *Rationale* gives the cost
  where one does not.
- **A closed request's commits.** The page says the head branch can be restored; it does not say for
  how long, and it does not use the words "keeps the commits". WAY-267's "keeps a closed request's
  commits" is a reading of that sentence, and the fact's sentence does not go past the page.
- **A draft whose diff empties.** No host's documentation was found on whether it stays open, as the
  designer reported. `reserved_return.md:58-59` holds either way, so the change does not rest on it
  and no fact is due.
