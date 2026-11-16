# Author report — readiness-approval-rename

**Status:** done

**Commit:** `79c9bfb9` on `task/readiness-approval-rename` (one commit, 59 files, +395 −386 against base
`4758840f`; the move `project-level/skill/readiness_gate.md` → `readiness_approval.md` is a rename).

## What was changed

- **Readiness gate → readiness approval** (task *To do* 1–5, 11). Phrases `readiness gate`, `gate record`,
  `ready for gate`, `project-readiness-gate`, `readiness_gate` (also across a line break) were rewritten by a
  script over every tracked file (not `.claude/`, `.agents/`), and then the diff was read line by line for
  grammar. The bare uses (`the gate`, `its gate`, `definition gate`, `gated again`, `no gate returns`) were
  rewritten by hand, one by one, in `project-level/` (lead, plan, skill, task, technology), `elements/common/`,
  `task-cycle/skill/foundation_step.md`, `task-cycle/test_request_check.py` and `foundations/decisions.md`
  (WAY-118, WAY-126, WAY-145, WAY-121 and the other decisions that carried them). Code: `readiness_check.py`
  (section `Approval record`, status `awaiting approval`, names `APPROVAL_RECORD`, `APPROVAL_LINES`,
  `check_approval_record`, messages, help text, docstrings), `plan_check.py` (same names, messages), and the
  tests of both, `test_plan_state*.py`. Template `definition_template.md` has `## Approval record` and
  `awaiting approval`. The invariant is `project-readiness-check` in `foundations/invariants.md`, in
  `WAY-118`'s *Verification* and in every `invariant:` line of the tests. Glossary entry `gate` has
  *Not:* the human's approval of a project definition — "readiness approval".
- **Entry → key, backlog entry → line** (To do 9, 10). `AGENTS.md` (`## Backlog`), `project-level/backlog_place.md`
  (heading is now "Resolve a key of the locations file"), `definition_template.md`, `process-audit/SKILL.md`,
  `process-audit/problem_register.md`, `orchestrated_mode.md`, `read_sources.md`, `foundations/part_map.md`,
  decisions WAY-27, WAY-107, WAY-320 (binding sentence, *Verification*, *Rationale*, *Rejected*), WAY-330,
  WAY-344 and the row of WAY-342 in WAY-376; `audit_count.py` docstring, comments, messages and docstrings
  (`entry_path`, `REGISTER_ENTRY`, `RESULTS_ENTRY`, `REPOSITORY_ENTRY`, the local `entries` stay). Backlog line:
  WAY-140, `task-cycle/record_template.md` ("Writes to the task's line in the backlog:"),
  `task-cycle/skill/SKILL.md` (two places), `project-level/test_plan_state.py` (the copied line),
  `foundation-review/with_the_human.md`.
- **read off** (To do 8). `project-level/technology/research.md` ("take from its documentation … the page it was
  taken from"); the rationale of WAY-280 ("A weight taken from the effect"). The glossary entry
  `read off` is unchanged.
- **Glossary** (To do 7, rows 1–2): `projected entry` appended to `foundations/glossary.md`, written by following
  `elements/glossary/skill/SKILL.md`. Meaning in English: "A projected entry is the wording, under a project
  definition's 'Projected foundation changes', of an entry of a product's foundation — a decision, an invariant,
  a glossary term, an environment fact or a change to the part map — or of a change to one, that the foundation
  is to hold once a task's code makes it true." Po polsku: „Wpis projektowany to brzmienie wpisu fundamentu
  produktu albo zmiany wpisu — decyzji, niezmiennika, terminu, faktu o środowisku lub zmiany mapy części —
  zapisane w sekcji „Projected foundation changes" definicji projektu, które fundament ma przyjąć, gdy kod
  zadania uczyni je prawdziwym." Marked `row 2`. The change to `gate` is `row 1`. Rows 3–6: row 3 is the code and
  template (`awaiting approval`), row 4 is the invariant identifier, rows 5 and 6 are the sentences of WAY-320 /
  WAY-107 and WAY-140 — all written in place, none as a second entry.
- **Entry points** (To do 11): `python -B agent-instructions/skill_entry_points.py --write` changed the six copies of
  `define-project`, `plan-project`, `settle-technology` (`.claude/skills/`, `.agents/skills/`); committed.
  No definition in `task-cycle/agent-types/` changed.

## Checks (command, exit code)

- `python -B gate/run_tests.py project-level` — 0 (279 tests)
- `python -B gate/run_tests.py process-audit` — 0 (276 tests)
- `python -B gate/run_tests.py agent-instructions` — 0 (50 tests; includes the linter test and the entry-point test)
- `python -B gate/run_tests.py elements/common` — 0 (270 tests)
- `python -B gate/run_tests.py task-cycle` — 0 (534 tests, 2 skipped as before)
- `python -B gate/run_tests.py gate` — 0 (36 tests)
- `python -B elements/common/foundation_check.py` — 0, "0 errors" (run on the working tree and again after the commit)
- Not run: the full gate (`python -B gate/run_tests.py` without a directory), as the handoff says; no run of
  `installation/`, `instruction-files/`, `product-guidelines/`, `relation-model/` (no file there changed).

**The invariant's test seen failing once** (`project-readiness-check`, the tests of `readiness_check.py`): with
`APPROVAL_RECORD` set back to `"Gate record"` and the status value back to `ready for gate` in
`project-level/readiness_check.py`, `python -B -m unittest discover -s project-level -p test_readiness_check.py`
exit 1 (79 tests, 7 failures and 58 errors); with the edit restored, same command exit 0 (79 tests OK). The edit was
restored before the commit.

## Own-work check (section 3)

The requirement most likely not met: *every* use of a moved word in the English text of every tracked file is
rewritten, and none of an unmoved one. Check: a script over `git ls-files` that (a) finds the old phrases across line
breaks and (b) lists each paragraph holding `gate`/`gated`/`gating` together with `approv|definition|readiness|projected|human|plan`,
and (c) lists `entry`/`entries` within 90 characters of `locations|backlog|task-rules|tasks|projects|.json`. It showed:
(a) only `foundations/decisions.md:8335` ("the script that runs the gate records, at each run" — a line break splits
"gate" and "records"; it is the test-command meaning and stays; my script had first turned it into "approval records"
and I restored it); (b) only uses in the meaning of the test command (WAY-160, WAY-350, README, `task-cycle/skill/blocked_finding.md`);
(c) only foundation entries and the Python names `entry_path`/`entries`. A first version of the rename script also
touched the line at `decisions.md:8335`, caught by reading the diff before the checks.

## Choices I made (the orchestrator enters them in the questions table)

1. **File name** `project-level/skill/readiness_approval.md` (also the section heading "7. The readiness approval").
   Rejected: `approval.md` (loses the link to the skill step's name). Cost if wrong: one rename and the three references.
2. **Python names** of the readiness meaning follow: `GATE_RECORD` → `APPROVAL_RECORD`, `GATE_LINES` →
   `APPROVAL_LINES`, `check_gate_record` → `check_approval_record`, `GATE_FINGERPRINT` → `APPROVAL_FINGERPRINT`, test
   keyword `gate=` → `approval=`, test class `GateRecord` → `ApprovalRecord`. Rejected: leaving them (the word `gate`
   would still stand in the meaning that moved, WAY-97). Nothing outside `project-level/` imports them (searched).
3. **Wording of the bare uses**: "the readiness approval" where the moment is meant ("goes through the readiness
   approval again"), "its approval" for the state of an approved definition ("changed after its approval"), "the approval
   agent" for the agent that leads step 7 (`definition_change.md`), "a definition that has passed its readiness approval"
   where the old text said "the gate has approved". WAY-118's first clause "The readiness gate blocks a definition…"
   became "The readiness approval is blocked by a missing section, …" (the meaning is the one the clause had: the checkable
   conditions that hold the approval back). Rejected: "The readiness approval blocks a definition" (the approval is a
   human act and does not block; the check does).
4. **`audit_count.py` messages**: "the locations file holds no key `X` under `Y`", "the key `X` under `Y` of the locations
   file is …", "holds the key `X` twice" (was "key or entry"), "no repository named in the locations file holds a key
   `repository`". The message the old code wrote for an outer key (`holds no key`) is unchanged.
   **Changed tests of it** (rule of "Changing an existing test"): `test_audit_count.py` — three expected substrings
   (`no entry ... under` → `no key ... under`, line ~832 and ~880) and three test names; cause: the task's To do 9 names the
   messages of `audit_count.py` and WAY-99 renames the meaning; evidence: the frozen task, *To do* 9 and Question 7. The
   input handling (what is accepted or refused) is untouched; the tests of the refusal (`assert_refused`) are the same
   in every other respect. Two comments citing WAY-344 now quote "no key `repository` under `the-way`" as WAY-344 now reads.
5. **`intermediate human gates`** (*Rejected* of WAY-227)
   became "intermediate human approvals": a general-language use of "gate" for a stop awaiting a human, which the
   glossary of `gate` would make a reader take for the test command. Cost if wrong: one *Rejected* clause reworded back.
6. **`read off`**: only `research.md` (documentation) and the "weight read off the effect" in a decision rationale (a
   judgement; WAY-54 says a read-off value is a tool's) were moved. Left on purpose: `elements/common/rules.md:37` and
   WAY-54 (a tool reads a field off the product), `product-guidelines/styleguide/*` ("a palette read off the code",
   "read off what the product has"): the product as it stands, and WAY-204 ("the split is read off a trial run": a tool's run).
   Cost if wrong: a few lines to reword.
7. **Glossary form**: `gate` *Not:* "the human's approval of a project definition, given once a script has checked it —
   'readiness approval'", the quoted word form that WAY-99 allows; `projected entry` placed last in the file (the file has
   no order). No glossary entry for "readiness approval" (a reader who knows the field reads "approval" as it is meant, WAY-95).
8. **Context claim not found**: the task's *Context* lists `task-cycle/skill/foundation_step.md` and `project-level/definition_template.md`
   among files with the locations-key meaning of `entry`; `foundation_step.md` has none (its uses are the foundation's). I
   changed in it the one bare readiness use only.

## Reaches beyond the dispatch

- `elements/glossary/skill/{read,decide_entry,write,projected}.md` read for the steps of the glossary skill; `elements/common/way_of_working.md`
  (named by the handoff by section) read whole.
- `foundations/decisions.md` read by passages found by `grep` for `gate`, `entry`, `locations`, `backlog`, `read off`; the
  decisions the hits stand in are read in place, not whole each. No decision read whole beyond those
  the handoff named; the foundation search for the entries touched was by word, as WAY-97 asks.
- The worktree's `git ls-files` for the whole text search.

## Unread material

- The decisions the handoff names (WAY-99, WAY-95, WAY-97, WAY-34, WAY-114, WAY-117, WAY-118, WAY-126, WAY-27, WAY-107,
  WAY-140, WAY-320, WAY-330, WAY-106, WAY-116, WAY-124, WAY-134, WAY-142 to WAY-146, WAY-156, WAY-376): read whole were WAY-118,
  WAY-126, WAY-145, WAY-107 and WAY-320; WAY-99, WAY-95, WAY-97 and WAY-34 I took from the text the frozen task quotes; the
  others I read as the passages around my search hits and the changed lines, not each whole. The invariant
  `project-readiness-check` was read as its heading and sentence with its fields, other invariants only where a test cited them.
- `foundations/part_map.md`: read the parts `project-level` and `task-cycle` and the trust-boundary table, not every part.
- `guidelines/coding.md`, `guidelines/testing.md`, `agent-instructions/README.md`: read whole.
- Files I changed that I did not read whole before changing: `foundations/decisions.md`, `process-audit/audit_count.py`,
  `process-audit/test_audit_count.py`, `project-level/plan_check.py`, `task-cycle/skill/SKILL.md`, `project-level/test_plan_state*.py`,
  `project-level/test_plan_check.py` (read in the regions the edits touch).

## Searches not found or unclear

- `task-cycle/skill/foundation_step.md` is named in the task's *Context* as holding a locations-key use of `entry`; none found.
- The task says WAY-342's question is cited in WAY-376; the question stands only as a row of the table in WAY-376 (the
  decision WAY-342 has no heading in the log); I changed the row.
- The "Another change in flight" about WAY-27 and WAY-320 ("entry of the locations file"): not in this worktree; the cycle
  that merges second reconciles.
- Request description text for products (To do 6): not written, as the handoff says.

## Working copies

- `.runs/author/` held my scripts (`mech.py`, `edit_generic.py`, `reps_*.py`, `scan.py`, outputs of the runs, a backup of
  `readiness_check.py`). Removed before this return, with `.runs/author/` itself; nothing remains. No worktree or clone was made.

## Problems observed

- None beyond the line-break false hit of `gate record` at `decisions.md:8335`, mended.
