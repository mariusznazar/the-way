# Author report — precedence-between-decisions

**Status:** done

## Files changed and commits

Added and removed lines (from `git diff --stat`, before the report was added):

| File | + / - |
|---|---|
| `foundations/decisions.md` | 33 / 7 |
| `elements/decisions/template.md` | 6 / 2 |
| `agent-instructions/README.md` | 6 / 3 |
| `task-cycle/skill/foundation_step.md` | 6 / 3 |
| `elements/decisions/skill/decide_entry.md` | 5 / 2 |
| `task-cycle/skill/request_template.md` | 5 / 3 |

Commits: one commit on `task/precedence-between-decisions` (hash is in the return message). The
report file under `.runs/` is not committed by the author.

## What was done, against the task's *To do*

1. WAY-25 binding paragraph: the second sentence now reads as the task gives, plus the closing
   sentence "Where what the human accepted gives the outcome ... otherwise the agent stops and
   asks." Compared as normalized text against the task's quoted sentence: identical.
2. WAY-25 *Verification*: *violates* gains "the change records a precedence that no passage of
   what the human accepted gives, or one its request does not name with those passages". *complies*
   now holds two members: the stop (what the human accepted does not give the outcome, or the
   change may not write the decision that prevails) and the record-and-name path (see Choices).
3. WAY-25 *Rationale* and *Rejected* describe the new decision. *Rejected* keeps the three old
   items and adds the not-chosen ways of questions 1 and 3 of the task: a human records every
   precedence; an exception only for a settlement that says which decision prevails; the wording
   "the change writes the `narrows` and its request names it"; recording with no passages in the
   request; "the passage" in the singular.
4. Copies kept in step: `elements/decisions/template.md` (Relations and precedence), 
   `agent-instructions/README.md` (Make the change), `task-cycle/skill/foundation_step.md`,
   `elements/decisions/skill/decide_entry.md`, `task-cycle/skill/request_template.md` (item 6 of
   *For you to decide*, at lines 190-198 now).
5. WAY-134 *Verification* complies example: reworded exactly as the task gives (compared as
   normalized text). The decisions template rule on *Rejected* is unchanged.

## Foundation entries written or changed (WAY-114, `foundation_step.md`)

Both are marked `the cycle's`: no row of *Settlements to record* and no projected entry carries them
(the task's *Settlements to record* is `none`). The meaning of each was settled by the human in the
task document (questions 1, 3, 5 and 2); the wording is the author's.

- WAY-25 (edited in place, WAY-07), `the cycle's`.
  - EN: A collision between two decisions with no recorded precedence is never settled silently by
    the agent; where what the human accepted gives the outcome and the change may write the
    prevailing decision, the change records the precedence there and its request quotes the
    passages that give the outcome for the human to accept at the merge, otherwise the agent stops
    and asks.
  - PL: Zderzenie dwóch decyzji bez zapisanego pierwszeństwa agent nigdy nie rozstrzyga po cichu;
    gdy to, co człowiek przyjął, daje wynik, a zmiana może zapisać decyzję, która wygrywa, zmiana
    zapisuje pierwszeństwo w tej decyzji, a jej PR cytuje fragmenty dające wynik do przyjęcia przy
    scaleniu, w przeciwnym razie agent staje i pyta.
- WAY-134 (edited in place), `the cycle's`.
  - EN: A decision row whose source keeps only ways that answer another part of the question gives
    `unknown` as the decision's rejected options, with no question to the human.
  - PL: Wiersz decyzji, którego źródło zachowuje tylko warianty odpowiadające na inną część
    pytania, daje w odrzuconych wariantach decyzji `unknown`, bez pytania do człowieka.

## Search of the whole foundation (WAY-33)

Searched by the identifier `WAY-25` across the repository (not only the foundation) and by the
words collid*, collision, precedence, narrows, "stops the work".

- Places that say a collision stops the work and were changed: the five copies of *To do* 4, and
  `elements/decisions/template.md:168`.
- Entries that cite WAY-25 and were read whole: WAY-26 (`foundations/decisions.md`, rationale),
  WAY-32 (rationale), WAY-172, WAY-268, WAY-293. Each says why a precedence was written there, or
  that without it the agent would face two decisions with nothing to choose between; the new text
  does not contradict any of them. No change. Judgment on WAY-293's rationale ("the agent that meets
  the collision may not settle it (WAY-25)"): it describes a collision between a task or spec that
  excludes an entry and a rule, where the spec is not something the human accepted, so the agent
  still may not settle it; left as is.
- WAY-30 and WAY-114, the task's *Decisions in play*, read whole. WAY-25 now cites WAY-114 in its
  binding sentence; I judged that no `derives from WAY-114` is needed (that relation means "a
  higher decision this one serves", WAY-32) and added no relation. No other invariant or glossary
  entry states the old rule.
- `project-level/**` skills mention "collision" for candidates or projected entries colliding with
  current decisions at a readiness gate; that is another process, not a collision between two
  decisions of the log, and the task does not name it. Not changed.

## Checks

| Command | Exit code |
|---|---|
| `python -B elements/common/foundation_check.py` (from the worktree root) | 0 (`0 errors`) |
| `python -B gate/run_tests.py agent-instructions` | 0 (18 tests) |
| `python -B gate/run_tests.py elements/common` | 0 (109 tests) |
| `python -B gate/run_tests.py task-cycle` | 0 (187 tests) |
| `python -B task-cycle/private_paths_check.py <file>` for each of the six changed files | 0 each (`0 listed`) |

Not run: the whole gate `python -B gate/run_tests.py` (the orchestrator's run); `installation`,
`project-level`, `instruction-files`, `gate`, `relation-model` and `elements/part-map` tests (none
reads a file changed here by name; `installation` tests that copy a skill do not read the changed
passages — I did not verify this by running them). No test written: the change is prose and a
foundation entry, which gets no test (`SKILL.md` section 2); no invariant is changed.

## Own-work check (section 3)

- Requirement most likely not met: the two quoted wordings of the task (WAY-25 binding sentences,
  WAY-134 example) copied exactly, wrapped across lines in the file.
- Check: a script reading `foundations/decisions.md`, collapsing whitespace, and testing that each
  quoted text is a substring. Showed: both True. No failing run beforehand (not a test written
  first; prose).

## Reaches beyond the dispatch (section 1)

- `foundations/decisions.md` WAY-26, WAY-293, WAY-172, WAY-268 passages found by the grep for
  `WAY-25`: read (rationale text and neighbouring lines of each), not whole entries for WAY-26. 
  Reason: WAY-33 search.
- `elements/common/foundation_check.py` head (usage), `gate/run_tests.py` use as the handoff gives;
  `task-cycle/private_paths_check.py` as the handoff's README names.
- `git ls-files` for test files, to choose the focused directories.

## Choices

- *complies* of WAY-25 holds the record-and-name path as well as the stop. The task asks only that
  the complies example say the agent stops when what the human accepted gives no outcome; with
  only that, the pair would show no complying case of the main new behaviour. Rejected: stop-only
  complies. Cost if wrong: the reviewer sees one more member than the task names; strike it.
- *Rejected* of WAY-25: the task's "not chosen" for question 1 ("exception for the settlement that
  says which decision prevails") is worded without the task-internal detail ("did not even cover
  the case that started it"); it gives the reason as "the outcome often follows from settlements
  that do not say so".
- `foundation_step.md`: the recording writer marks the entry `the cycle's` and keeps the passages in
  its report; the task names only the request's item for the passages, and the report is where the
  request gets them from. Cost if wrong: one clause to strike.
- `README.md`: "what he accepted" (Mariusz) in the same register as the file's other sentences.

## Task values that do not pass my reckoning

- The task gives `request_template.md:174-180` for the item; the item is at `190-196` in the
  worktree (the handoff says so). Same item.
- *To do* 3 says the rejected variants come from "questions 1 and 3"; question 5's not-chosen
  variant concerns the example, not *Rejected*, so it is not carried there. Not a contradiction.

## Searches not found or unclear

- none found missing. Unclear: whether the `project-level` readiness-gate collision handling
  (`project-level/skill/SKILL.md:155`, WAY-118 area) should follow the new rule; I read it as a
  different process and left it.
