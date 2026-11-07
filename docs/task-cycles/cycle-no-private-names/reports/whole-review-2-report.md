FAIL 4deb195b32c33ef12d8e8fcf2b609dd69e550722

# Review of the fix of the review of the whole change (range b6d93e8..4deb195)

`git rev-parse HEAD` is `4deb195b32c33ef12d8e8fcf2b609dd69e550722`; commits `d745246` and `4deb195`.
Method: `task-cycle/review/SKILL.md` and `task-cycle/review/fix.md`. Bounds: the findings file
`reports/whole-review-findings.md` (1 blocking, 7 Minor), the fix report `reports/fix.md`, the
orchestrator's ruling in `reports/fix-handoff.md` (way (c); `plan_state.py` and the invariant
unchanged; a test pins the reader on a cleaned copy). Counts: findings of the first review remaining 0;
new blocking finding in the fix diff 1; new Minor 3. The new finding is Important, so the review fails
(WAY-162).

## Each finding of the findings file

1. Blocking (reader cannot anchor the cleaned copy; WAY-308 said it could): **fixed**.
   - WAY-308 *Rationale* (`foundations/decisions.md`) now says three readers go on as before and the
     plan-state reader reads the copy with one loss: before the plan row's document link names the frozen
     copy it anchors by the absolute path of `Task source:`, which the cleaning replaces; for a plan task
     it reports the copy unchecked and proposes no move to done until a human links the frozen copy; it
     fails closed; a task of no plan is not read this way. The "price taken" lists the loss. This is what I
     found in the first review.
   - `task-cycle/record_template.md` (`Task source:`) and SKILL.md step 3 (new bullet for `Task source:`)
     say the same.
   - Tests in `project-level/test_plan_state.py`: `test_cleaned_copy_of_an_unfinished_plan_item_is_unchecked_until_the_copy_is_linked`,
     `test_cleaned_copy_anchors_a_done_task_once_the_document_links_the_frozen_copy`,
     `test_task_relation_naming_the_plan_by_a_description_conflicts_when_the_copy_is_linked`. They assert
     the reader's actual output (`unchecked 1 reports:`, `original Task source or Document cannot be
     anchored`, no ` -> done`, no `conflict`; the `cycle record ... commit <sha>` line and no `unchecked`
     once linked; `conflict 1 reports:` and `human reconciliation required` with exit 1). They match what I
     saw in my own fixtures; the first one would fail if the absolute path stayed (it would then propose
     done), as the author's mutation shows. `plan_state.py` and the invariant are untouched
     (`git diff b6d93e8..4deb195 --stat` lists neither).
   - The second form (the `Task relation:` line): the cleaning now leaves that line; test 3 pins why. But
     see new finding N1: the way the rule handles a listing of that line is not sound.
2. WAY-294 against step 5: **fixed**. WAY-309 gets a third sentence, `narrows WAY-294`, and complies and
   violates lines; SKILL.md step 5 points to WAY-309. `foundation_check.py` exit 0.
3. Scope: **fixed** (`project-level` in both entries).
4. *Checks* line for the copy's run: **fixed** (SKILL.md step 12, `request_template.md` step 5).
5. `record_template.md` line 93: **fixed** (the copy is cleaned and checked as the section gives).
6. Truncated listing and the real directory name in a test: **fixed** by the rule (replace the whole path
   to the end of the phrase, SKILL.md step 4 and `request_template.md` step 4) and the docstring; the
   sample is now a made-up path on a drive, with a space in a directory name. The author chose not to make the script print more; I accept it.
7. Files not read: **fixed**. UTF-16 with a byte order mark is read (test
   `test_a_utf16_file_with_a_byte_order_mark_is_read`; I confirmed `\xfe\xff` UTF-16-BE listed, UTF-16-LE
   without a mark still counted as `1 binary files not read`, as the docstring says), and step 4 says what
   to do with the count.
8. Edges: **fixed**. a web address with a drive-like segment is no longer listed; file addresses that name a drive and a Linux home directory are listed (checked by hand, and by the new tests).

## New findings in the fix diff

### N1. Important — the rule for a listed `Task relation:` / `Project relation:` line has the cycle commit and push what the check listed, against WAY-308 and WAY-309, and the remedy comes after the publication

Place: `task-cycle/skill/SKILL.md` section "The record before it is committed", step 4 (last sentences of
the exit-1 paragraph), against `foundations/decisions.md` WAY-309 (binding sentence "corrects what it
lists until it lists nothing"; *Verification* violates: "the orchestrator stops after a run that listed
something") and WAY-308 (*Verification* violates: "a copy of the record is committed with the path of the
author's notes or of a directory on the author's disk").

What is wrong. Step 4 now says: if the check lists a `Task relation:` or `Project relation:` line, do not
rewrite it, "commit the copy with that line as it is", and put it to the human in the request as a draft.
A line the check lists holds an absolute path or a note link by definition, so this is the one case in
which the cycle commits and pushes (step 12 pushes before the description is written) a copy that still
holds the path, which is what WAY-308 and WAY-309 name as violations. The author changed WAY-308's
binding sentence to leave those two lines unchanged but did not write the exception into WAY-309's
sentence or either *Verification*, and the loop in steps 4 and 5 still says "until both exit 0" while step
6 records an exit code. By WAY-263 this is Important: the files do what the entry forbids.
The remedy does not undo the leak: the human decides "merge as it stands?" after the branch with the path
is on the remote; merging or not does not take the path out of the pushed history. The draft is not
`blocked` as the handoff said; the author disclosed this, and I do not grade it, but with a listed path
in a pushed copy `blocked` is no better.
Why it matters: the task exists to stop exactly this publication; the new exception reopens it for a case
the rule itself says is rare, with a safety net that comes too late, and leaves the foundation saying the
opposite of the rule.
Evidence: SKILL.md step 4 text above; WAY-309 text (`git show 4deb195:foundations/decisions.md`, section
WAY-309) has no exception; the order of commit and push in step 12.
Not decided here, ways out: (a) drop the exception: rewrite the line like any other (a reader conflict
is then possible and visible, but nothing private is published), and have the request tell the human; or
(b) keep it and write it into WAY-308/WAY-309 (binding sentence, *Verification*, the price taken), and make
the cycle stop before the commit and ask the human instead of committing the path. Either way the
decision, the section and the template must agree.
Comes from: the orchestrator's ruling on the second form of finding 1 (handoff), carried out as written;
the finding is about the files, not the author's following of the ruling.

## New Minor findings

- N2. `task-cycle/private_paths_check.py` (`WINDOWS_DRIVE`): a drive letter after any slash is now
  excluded, so `/C:/Work/x` (a Windows path in a URL path, as some tools print it) is no longer listed as
  a drive path; only a home directory behind it is still caught. Not listed in my checks: `/C:/Work/x`
  alone. Narrow; within the task.
- N3. `task-cycle/private_paths_check.py` (`check_file`): a UTF-16 file that fails to decode raises an
  error that says "as UTF-8". Cosmetic. Within the task.
- N4. `foundations/decisions.md` WAY-308: the edited sentences are not re-wrapped (some lines run past the
  file's 100-column wrap), e.g. the binding paragraph and the *Verification* lines. Cosmetic. Within the
  task.

## Declined to judge

- A reader that anchors a cleaned `Task source:` (a change of `plan_state.py`): the orchestrator's ruling
  names it a task of its own; the author lists it under concerns.
- UTF-16 without a byte order mark: the docstring and the rule say it is counted and read by hand.
- A private name in plain words, commit messages, history: unchanged from the first review.

## Checks I ran (focused only; the full gate is the orchestrator's)

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `4deb195b32c33ef12d8e8fcf2b609dd69e550722` |
| `git diff --stat b6d93e8..4deb195` | 0 | 7 files, 162 insertions, 53 deletions; `plan_state.py` and `invariants.md` not in it |
| `python -B gate/run_tests.py task-cycle` | 0 | 187 tests OK |
| `python -B -m unittest project-level/test_plan_state.py -k cleaned -k description_conflicts` | 0 | 3 tests OK |
| `python -B gate/run_tests.py project-level` | 0 | 271 tests OK |
| `python -B gate/run_tests.py agent-instructions` | 0 | 18 tests OK |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B task-cycle/private_paths_check.py` on three scratch files (file URLs, UTF-16-BE with a mark, UTF-16-LE without) | 1, 1, 0 | as in findings 7 and 8 and N2 |

Not run: the author's mutations, the full gate.

## Reach beyond the dispatch

None beyond the files the dispatch names; I re-read `foundations/decisions.md` WAY-309/WAY-308 from the
head commit and `task-cycle/skill/SKILL.md` steps 4-6 and 12 for N1.

## Searches not found or unclear

- Unclear: whether the `blocked` state the handoff asked for on a listed relation line was meant to be
  reachable through the existing request template; the template's row "A draft for another reason" gives
  a plain draft (the author's choice, disclosed in `fix.md`). Not decided here.
- Not found: any text in WAY-309 or the section that says what happens to the exit code and step 6's
  record of it when a relation line stays listed.
