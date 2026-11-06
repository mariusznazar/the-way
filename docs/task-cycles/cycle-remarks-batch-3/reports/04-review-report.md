FAIL 7841f0031df8f9dfa9db69efeab3f70efc2ddf97

# Review of the whole change, range 3177e1090f6000ed97fbbbab70ec7c7e622aa2c9..7841f00

`git rev-parse HEAD` is `7841f0031df8f9dfa9db69efeab3f70efc2ddf97`; `git log` shows the three commits the handoff names. No spec, no plan, one author: no slice reviews, so no Minor or out-of-scope findings from slice reviews.

Verdict basis: To do 1 (the restart condition of the correction against WAY-298) has one blocking finding; To do 2, 3 and 4 and the source fidelity of the quoted sentences are met.

## Blocking findings

### 1. Important — `task-cycle/skill/correction.md:6-10` restarts only "where something came in"; WAY-298 (`foundations/decisions.md:9028-9037`, Verification at `:9042-9051`) requires the restart without that qualification (WAY-263)

- Place: `task-cycle/skill/correction.md:9-10`: "In both cases, where something came in, start again from the entry point that started the cycle." Against `foundations/decisions.md` WAY-298: "A correction after review begins the same way in the-way itself — it fast-forwards the checkout, or, where the session works in the request's worktree, merges the remote target branch into it, and starts again from the entry point"; its Verification "complies" line says a correction in the request's worktree "merges the remote target branch into it before it reads the request's record, and starts again from the entry point".
- What is wrong: the entry the change writes and the file the change writes say different things about when a correction restarts. The entry has no qualification, so a correction that fetched and found nothing new, as the entry reads, still starts again; the file restarts only when something came in. The author chose the conditional wording on purpose (report 02, *Choices*), reading the task's "in both cases" as a loop in its letter; that reasoning is sound for the file, but the entry was not brought into line with it. Row 1 of the task (the meaning WAY-134 binds the entry to) also says the correction "zaczyna od nowa" without the condition, so the choice is the author's, and it has to appear in the entry as well, or the file has to follow the entry.
- Why it matters: WAY-263 grades a departure of a change's files from a foundation entry it writes as Important when the files fail to do what the entry requires. The next reader of WAY-298 (an agent comparing a correction with the decision, per its Verification) will judge the file wrong, or will restart unconditionally and loop. The same ambiguity stands in step 4 (`task-cycle/skill/SKILL.md:116-120`, the task's sentence, kept word for word): "fetch, and where it stands behind, fast-forward it … then start again" reads as restart-after-fast-forward, and the entry's "fast-forwards … and then starts again" reads the same; only the correction paragraph says "where something came in". The three places do not say one thing.
- Evidence: the texts quoted above; `rg -n "start again|starts again" task-cycle/skill foundations/decisions.md` shows the conditional only in `correction.md:9`.
- Fix: write the condition into WAY-298's body and Verification ("and, where something came in, starts again from the entry point"), and make step 4's sentence unambiguous on that point if the task's sentence permits it; or make the file unconditional and let the entry stand. Either way one wording across the entry, step 4 and `correction.md`. The choice between them is the author's, to be recorded.
- Slice: not applicable (no plan).

## Minor findings

### 2. Minor — `task-cycle/skill/SKILL.md:68` still says "The cycle writes only in the task's worktree" while step 4 (`:116-117`) and WAY-298 (`foundations/decisions.md:9037`) say the cycle makes one change outside it

- The task (Context, AIR-602) says the clause "the one change the cycle makes outside the task's worktree" removes the contradiction with line 68, and Mariusz accepted it. The author left line 68 as it stands (report 02, *Concerns*). A reader of line 68, which comes before step 4, meets an unqualified "only"; the qualification stands 48 lines later and in the foundation. The effect is a sentence a careful agent will notice and then resolve by step 4; it does not change what the cycle does, so Minor. Within the task: the task decides on the wording of the sentence it adds and does not touch line 68. One clause on line 68 ("except the fast-forward of step 4") would settle it.

### 3. Minor — `task-cycle/record_template.md:181-182`: the rewritten sentence left a line of 181 characters

- The line "cycles and `task-cycle/remarks_check.py` cut the block as that item and the lines under it. Before the record is committed, `task-cycle/skill/SKILL.md` ("The process remarks check")" was not re-wrapped after the replacement. The file has other lines over 100 (up to 123) and no script enforces the width, so no check fails; only the diff reads untidily (the wording equals the task's replacement word for word). The words are right.
- Evidence: `awk 'length>100{print FNR": "length}' task-cycle/record_template.md` lists `182: 181`.

## Out-of-scope findings

### 4. Minor, outside the task — `task-cycle/skill/SKILL.md:389` (step 12) says "merge the current target branch into the task branch", while the correction now merges the remote target branch

- The task changed only `correction.md:20` and the start of step 4, so step 12 is not among its items. The effect: in a cycle on the-way, the reconciliation before the request merges the local target branch, which step 4 brought up to date at the start of the cycle but which may have fallen behind the remote since; the correction merges the remote branch. The two merges of the same cycle name different branches. The author noted it (report 02, *Concerns*). A later task can say "the remote target branch" there, as it did for the correction.

## Checked and found met

- To do 1: the sentence in step 4 (`SKILL.md:116-120`) is the task's sentence word for word; step 5 holds "in the task's worktree" (`:129-130`); `correction.md` new first paragraph precedes the *Reserved choice* paragraph, which keeps its text ("Then read the field *Reserved choice* …"); `correction.md:26` reads "the remote target branch". The restart condition is finding 1.
- To do 2: the sentence stands after "(WAY-120)." in `elements/common/way_of_working.md:16-18`, word for word as the task quotes it (re-wrapped only).
- To do 3: all four replacements in `record_template.md` and `remarks_check.py` (docstring lines 31-35 and the comment at line 70) read as the task gives; `grep cycle_remarks_digest` in the repository's tracked md/py outside `.runs` finds nothing outside what the task leaves (the private script itself is not in the repository).
- To do 4: `QUOTED` and `BLOCK_QUOTE` in `request_check.py:104-107` do what the task says (the three quotation forms, within one line, lines starting with `>`); the measure's description (`:31-43`) names quoted text; the tests cover the Polish task with English quotations (`not English`), the block wholly in quotation marks (`not judged`, the known gap named in the test) and the unpaired mark. The WAY-291 *Verification* example is changed word for word as the task gives (`decisions.md:8810`), re-wrapped.
- Row 1 of *Settlements to record*: WAY-298 carries the meaning of the row (fetch and fast-forward before the task branch, the one change outside the worktree, the restart, the stop where it cannot fast-forward, the correction's merge into the request's worktree, the remote branch in products). Its *Rejected* holds all six ways of the task's *Not chosen* (questions 1, 2 and 3) with the cost beside each; question 4 is rightly absent. The count "15 times" and the hash `8e5115a` are left out and the fact "may have changed the entry point" stays; acceptable, they are history and not a way. Form follows WAY-297 (Scope, Based on, Relations, Verification, Origin, Rationale, Rejected).

## Declined to judge

- The second, no-op merge of the remote target branch in a correction in the request's worktree (the new first paragraph merges it, `correction.md:26` merges it again): harmless and the task gives the sentence as it is.
- "step 4 of `implement-task`" in `correction.md:7` against the project skill name `the-way-implement-task`: the skill's text uses `implement-task` throughout.
- The wording of WAY-298's Verification lines, beyond their agreement with the files (finding 1): the log's form does not set a number of lines.
- Whether the fast-forward belongs in a hook or a script: not the task's matter (its *Not chosen* rejects the hook).

## Checks I ran

- `git rev-parse HEAD` -> `7841f0031df8f9dfa9db69efeab3f70efc2ddf97`; `git log 3177e10..HEAD` -> the three commits.
- `git diff 3177e1090f6000ed97fbbbab70ec7c7e622aa2c9..HEAD` read whole for every file (decisions.md and the test file included).
- `python -B elements/common/foundation_check.py` (from the worktree root) -> exit 0, `0 errors`.
- `python -B gate/run_tests.py task-cycle` -> exit 0 (142 tests, OK).
- `awk 'length>100'` over the changed md/py files -> only finding 3 is new (other long lines pre-exist).
- `git status --short` after my runs -> empty; no tracked file, index or branch changed.
- Not run: the full gate (the orchestrator's). Not repeated: the author's mutation runs of `test_request_check.py`; I read the three new tests and their fixtures and they assert on the measured share, the words and the verdict, not on a value the code computes for itself (the unpaired-mark test holds a hand-counted 33 words and 9/33).

## Reaches beyond the dispatch

- `task-cycle/review/whole_change.md` (the variant file `SKILL.md` names), read whole.
- `foundations/decisions.md:8990-9025` (WAY-297, as the form example for the entry WAY-298 follows) and the passage of WAY-298 and WAY-291 in the diff; a search for `current target branch|remote target branch` and `outside the task's worktree` over md and py files outside `.runs` to find the places that say the same thing (SKILL.md:68 and :389).
- WAY-263 and WAY-297 as quoted in `task-cycle/review/SKILL.md` section 3, for the grade of finding 1; the decisions named in the task's *Decisions in play* (WAY-10, 27, 114, 120, 127, 140, 290-292, 296) I read as the task quotes them, not in the log.

## Searches not found or unclear

- none
