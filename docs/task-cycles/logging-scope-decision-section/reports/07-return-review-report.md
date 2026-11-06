PASS 87377b210c5490fb6ef06cbd55a94c7063afb436

# Review of the return step — logging-scope-decision-section

Range `f604e93..87377b2` (one commit, `87377b2`, `task-cycle/skill/request_template.md`, +4/-2). `git rev-parse HEAD` is `87377b210c5490fb6ef06cbd55a94c7063afb436`, the head given. The worktree was not changed. Method: `task-cycle/review/SKILL.md`, dispatch "the return step's range".

Counts: blocking 0, Minor 1, out of scope 1.

## Findings

### Critical
none

### Important
none

### Minor

**M-1. `task-cycle/skill/request_template.md:48-49`: the parenthetical makes the exception sentence clumsy.**
"The one exception is the heading of the task's own sections, which is omitted where the task has none (the skeleton's `## <…>` heading)." The parenthetical points at the placeholder heading, but that heading is never written in either case: where the task has own sections each stands under its own heading, where it has none nothing is written. The sentence is right in substance and agrees with the skeleton note (`:104-105`), with `request_check.py` (`:353-358`, which rejects the literal `## <…>` and does not require the slot to be filled; `:372-377`, which accepts own headings between `Findings outside the task's scope` and `Course of the cycle`) and with task item 5. The reader may still take the sentence to say that `## <…>` is written when the task has sections. It costs at most one extra turn for an agent. Not blocking.

### Out of scope

**O-1. WAY-286 *Verification* (`foundations/decisions.md:8592-8593`) has no word for the omitted own-sections heading.**
Its *violates* bullet reads "a section with nothing in it is left out". My reading agrees with the return step's: the heading of the task's own sections stands for zero or more sections the task brings, WAY-286's binding text itself lists "the task's own sections under their own headings" as the task's own and never requires one, so a task with none leaves out no section. The task's item 5, which the human approved ("ready for cycle", question 3 answered "c - oba"), mandates the omission. So the return step needed no edit of the decision, and the template edit stays within the task. A narrower wording of WAY-286's *Verification* would change an approved decision's text and would be the human's choice; the return step rightly left it, but it is only a "judgment" in its report. If the orchestrator wants the reading visible, one line in *For you to decide* ("WAY-286 is read as allowing the omission; narrow its wording?") is the place. I do not grade it blocking: the template, the script and the task agree, and a reviewer comparing a request with WAY-286 would not fail a request for the omission.

## The three judgments asked for

1. **The two changed sentences.** Right against the skeleton (`:102-105` says "omit this heading altogether: it is not written with `none`"), against `request_check.py` (omission passes; the placeholder fails with a message saying to omit it or to write the task's own section heading) and against task item 5. Before the change the two sentences ("never disappears", "Every variant keeps every heading") contradicted the skeleton note; after it they do not. The edit is the smallest that closes the contradiction. Only Minor M-1 on wording.
2. **WAY-286 *Verification*.** Compatible, see O-1. It does not need a human decision before merge; it is a possible later narrowing of wording.
3. **Missed entries.** I found none. I read the return-step report's claims against: WAY-286 and WAY-287 (read whole, `foundations/decisions.md:8569-8626`; WAY-287 already holds the logging-scope kind in its binding sentence), the template item 10 (`:192-194`), `request_check.py` (docstring and `check()`), and the repository-wide search below. No new invariant (form behaviour is WAY-290's), no environment fact (the byte order mark is named in a code comment only; `utf-8-sig` is valid with or without the mark, and no entry rests on it), no glossary term, no part-map change. The template edit is the only unrelated text restating "every heading / never disappears" in the repository; `agent-instructions/README.md:70` mentions `none` only for *Cost*.

## Declined to judge

- The earlier range `61c72fb..f604e93` (item 1 to 4 of the task, `request_check.py`, WAY-287): reviewed by another agent, as the handoff says.
- WAY-287 itself (written in the earlier range): the handoff excludes it.
- The whole gate: the orchestrator's.

## Checks run

| Check | Command | Exit |
|---|---|---|
| Task-cycle tests | `python -B gate/run_tests.py task-cycle` | 0 (`Ran 94 tests`, `OK`) |
| Foundation check | `python -B elements/common/foundation_check.py` | 0 (`0 errors`) |
| Head | `git rev-parse HEAD` | `87377b2...`, the given head |
| Diff | `git diff f604e93..87377b2` and `git log f604e93..87377b2` | one commit, one file |
| Worktree state | `git status --short` | clean |

Not run: the whole gate (the orchestrator's); a scratch run of `request_check.py` on a description without the own-sections heading (the existing tests of the earlier range cover the placeholder; omission is the script's unrequired default, which I read in `check()` lines 346-383).

## Reaches beyond the dispatch

- `task-cycle/request_check.py:1-70` and `:325-395`: to compare the changed sentences with the script's behaviour, as the handoff asked.
- `foundations/decisions.md:8569-8626` (WAY-286 and WAY-287, each whole): to judge the *Verification* compatibility and the missed-entry question.
- Repository-wide grep for "never disappears", "every heading", "reads `none`", "left out", "own sections" (excluding `.runs` and `.git`): to find other text restating the rule the change qualifies.
- `task-cycle/test_request_check.py` (grep for omit/own-section tests, lines 310 and 408): to see whether omission and the placeholder are tested.

## Searches not found or unclear

- No test in `task-cycle/test_request_check.py` is named for "a description with no own sections passes" specifically (the grep found `test_the_tasks_own_sections_in_their_slot_pass` at `:310` and the placeholder test at `:408`); the passing case is probably the base good description, which I did not trace. Not needed for the template-only range.
- No other text in the repository restates the skeleton rule that needed the same exception (word search, not a reading of every file).
- The return-step report calls WAY-286 a "choice for Mariusz"; whether the cycle puts it into *For you to decide* is the orchestrator's call, and the handoff did not say.
