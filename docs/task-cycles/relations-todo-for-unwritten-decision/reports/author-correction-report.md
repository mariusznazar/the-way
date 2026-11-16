# Author correction report — correction 1, relations-todo-for-unwritten-decision

**Status:** done

**Commit:** one, on top of `f496f05`: "Add a decision's Relations to the descriptive TODO places of WAY-287
and the second required check to the ruleset fact" (hash in `git log -1` of the branch). Files:
`foundations/decisions.md` (WAY-287 only), `foundations/environment_facts.md` (`foundations-branch-ruleset`
only). Not pushed.

## Each remark, as made, and how

**Remark 1 — fixed.** WAY-287 now names the fourth place where it lists the places of a described `TODO`:
- binding sentence: "…or in a decision's *Based on* or *Relations* that stands on the main branch after the
  change (WAY-71)";
- *Verification*, the violating line: "…or *Derives from* or a decision's *Based on* or *Relations* holds a
  descriptive `TODO` on the merged tree…";
- *Rationale*: "…or in a decision's *Based on* or *Relations* once the change is merged is a gap…".
Nothing else of WAY-287 changed (its *Rejected* too, as the remark says the reviewer reads it); the three
places are the ones review finding M4 names. I read the whole entry first, *Rejected* included. The
identifier stays, no version (WAY-07). The entry now agrees with item 16 of
`task-cycle/skill/request_template.md`; I searched the repository once for other restatements of the list of
places (`decision's *Based on*` beside `TODO`/`gap`) and found only `elements/common/rules.md:27` (the rule of
form WAY-71 states, already with *Relations* in the sentence before it) and WAY-287's own lines.

**Remark 2 — no change from me** (a reviewer of the correction reads the rest of WAY-287).

**Remarks 3–5 — no change** (accepted; M5 let through, no task).

**Remark 6 — fixed.** I read the rule again with the two `gh api` read commands the fact holds (gh 2.88.1,
GET only; I wrote nothing to the host and changed no setting). The answer: `foundations_tests`, enforcement
active, target `refs/heads/foundations`, required checks `tests` and `tests-windows`, each of the integration
15368, no up-to-date requirement, rules `deletion` and `non_fast_forward`, one bypass actor (repository role
5, `always`), `current_user_can_bypass` `always`; the account holds `admin`. I changed the fact
`foundations-branch-ruleset` in place: the sentence now says it "requires the status checks `tests` and
`tests-windows`, each of the integration 15368", and the *Source* quotes the new output word for word and reads
"run 2026-11-16" (I compared the quoted outputs with a fresh run: both match). The rest of the sentence is the
same.
- **The CI decision:** WAY-16 (the decision whose *Based on* names the fact) says "The result of each such run
  is a check the repository requires before a merge" and, in its *Verification*, "required check with a bypass
  for the owner"; neither names one check, so no sentence of it rests on the old single check, and I left it
  unchanged. No other invariant or decision names the fact (search of the whole foundation, WAY-33).
- **Files outside the foundation:** `agent-instructions/README.md` ("Check the change") already says the two
  jobs are two checks, `tests` and `tests-windows`, both required; `.github/workflows/tests.yml` says the same
  in its header; `installation/README.md` says "the result of each job is a required check". None states a
  single check as the rule, so no file outside the foundation changed.

## Foundation step: entries

Both entries are marked `the cycle's` (no row carries them; the section reads `none`; the remarks are the
human's, through the adviser, and they set the meaning):
- **WAY-287** (changed): the request's section for the human's decisions also lists a descriptive `TODO` in a
  decision's *Relations* among the gaps the merge leaves.
- **`foundations-branch-ruleset`** (changed fact): the rule `foundations_tests` on `foundations` requires two
  checks, `tests` and `tests-windows`, as read on 2026-11-16.

(In Polish, for the human: WAY-287 — sekcja próśb o decyzje w opisie żądania wymienia też opisowe `TODO`
w *Relations* decyzji wśród luk, które scalenie zostawia; fakt `foundations-branch-ruleset` — reguła
`foundations_tests` wymaga dwóch sprawdzeń, `tests` i `tests-windows`, odczyt z 2026-11-16.)

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — 0, `0 errors`.
- `python -B gate/run_tests.py elements/common` — 0, 257 tests OK.
- `python -B gate/run_tests.py task-cycle` — 0, 534 tests OK (2 skipped).
- Not run: the full gate (CI is the final gate on the request).

## Own-work check

Requirement most likely not met: the entry must agree with item 16 in all the places it lists the
fields. Check: a search of the repository for the old three-field wording shows no remaining list of three
(only the two lines above, already four-place or about the form); the foundation check passes. For the
fact: the quoted outputs equal a fresh run of the two commands (a script compared them with the file's
text: both found).

## Reach beyond the dispatch

`task-cycle/skill/foundation_step.md` was not re-read (read in the first stage; its marking rule is applied
above). I read WAY-16 (selectively: its sentence, *Verification* and the start of *Rationale*) to see
whether it names one check. `elements/environment-facts/template.md` and the files of its skill
(`read.md`, `decide_entry.md`, `draft.md`, `write.md`) were read whole for the fact.

## Unread material

`reports/review-whole-report.md` (the findings file of M4 is quoted in the handoff; not read again). WAY-16's
*Rejected* was read only to its first lines. Nothing else the handoff names was left unread.

## Searches not found or unclear

None. (A search for other sentences resting on the ruleset fact found only WAY-16's *Based on* line.)

## Working copies

`.runs/author/` held my edit script, the two saved command outputs for the comparison; it stood at
`.runs/author/` and was removed before the
report. No worktree or clone was made.
