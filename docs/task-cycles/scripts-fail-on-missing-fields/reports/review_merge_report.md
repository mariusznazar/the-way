PASS c32cfe14ce85a2a8c81b54bdeff0f74a9b65550a

# Review of the reconciliation with the target branch — scripts-fail-on-missing-fields

Range: base `5922ffc` and `3bcad13` (the merge's parents), head `c32cfe1`. `git rev-parse HEAD` printed
`c32cfe14ce85a2a8c81b54bdeff0f74a9b65550a`; `git log -1 --format=%P` printed `5922ffc... 3bcad13...`.
Working tree clean; I changed nothing in the reviewed worktree.

## Findings

### Critical

none

### Important

none

### Minor

1. **WAY-344 has no clause for a field that a decision of the audit lets be absent**
   (`foundations/decisions.md:11307`, the sentence "ends the script with an error that names it, never
   guessing and never reading the absence as an empty value", with WAY-343 at `:11281`, WAY-337 at
   `:11112`, WAY-342 at `:11247`).
   What is wrong: three decisions of the audit make an absence a defined result: WAY-343 counts a cycle
   whose record names neither a pinned commit nor the line *Target branch and base* "under no version";
   WAY-337 leaves the fix-round share "unknown" where the record and the stages cannot tie a round;
   WAY-342 falls back to the checkout that runs the counting "where that entry [`repository` under
   `the-way`] is missing" and reads only the keys "that hold an entry `repository`". Each is a field
   the script looks for by name, so a later change that reworks the audit script's reading of the
   locations file or of a cycle record would be bound by WAY-344 to exit 2 at that field, and WAY-344's
   *Verification* "violates" list ("a script reads the absent key ... as no due date and gives its
   result with no error") would read as forbidding what WAY-343 and WAY-342 require.
   Why it is only Minor: WAY-344 binds a script that a change adds and the reworked reading of a file
   in a changed script, and says an existing script that no change touches stays as it is; this merge
   changes no script, so nothing is false today. WAY-344 also says the script checks the fields it
   "needs", which a reader can take to exclude an optional field. WAY-344 claims nothing about
   `process-audit/audit_count.py` or its tests (checked, see below), so the ask of point (3) is met;
   the gap is a latent ambiguity the merge created by putting the two sides together, not a
   contradiction in the files.
   Evidence: the three decisions above, read whole; `process-audit/audit_count.py` ends
   `return 1 if failed or register.errors else 0` (`:2170`) and returns 2 only at `:2161`, so a future
   rework of it would meet the rule at exactly these points.
   Resolution is not mine: adding a clause such as "except a field that a decision of the-way lets be
   absent and says what the script does then" changes the meaning of an approved decision beyond what
   the task settles (WAY-114), so it goes to the human, or is left for the first change that reworks
   the audit script. Not blocking.

2. none further. (The order of *Scope* is the part map's order with `process-audit` last, which is the
   order WAY-328's *Scope* uses; no finding.)

### Out of scope

The Minor finding above reaches the audit script, which the task puts out of scope ("przegląd i poprawa
istniejących skryptów"); it is listed as out of scope in that sense: it concerns a future change to that
script, not this change.

## Answers to the four points of the ask

1. **No loss or alteration of either side.** `git diff 3bcad13..HEAD --stat`: one file,
   `foundations/decisions.md`, 78 insertions, 0 deletions. The target's entries WAY-328 and
   WAY-330…WAY-343 and every other file are byte-identical to `3bcad13`. The task side: I extracted
   the entry of `5922ffc` (`### WAY-330` to the end of the decisions) and the entry of HEAD
   (`### WAY-344`) and diffed them: exactly two lines differ, the heading number (330 to 344) and the
   *Scope* line (`process-audit` appended). Title, body, *Relations*, *Verification*, *Rationale*,
   *Rejected* are unchanged. The task's own change before the merge was `e9a0f92..5922ffc`: one file,
   `foundations/decisions.md`, 78 insertions, so no file of the task is lost in the merge.
2. **Scope equals the 17 parts.** A script parsed `foundations/part_map.md` (sections that carry a
   `**Files:**` line, which excludes the five surfaces `test-runner-command`, `installation-command`,
   `foundation-check-command`, `project-plan-state-command`, `tracked-private-paths-command`): 17
   parts; WAY-344's *Scope* has 17 identifiers; the sets are equal, the symmetric difference is empty.
   The task asked for "all parts of the map" (it counted 16 when the map had 16), so 17 meets it.
3. **No contradiction with the target's entries, and no claim about the audit's script.** Read whole:
   WAY-328, WAY-330, WAY-331, WAY-332, WAY-337, WAY-338, WAY-339, WAY-341, WAY-342, WAY-343 and the
   `process-audit` entry of the part map. WAY-344 does not name `process-audit/audit_count.py`, its tests
   or the audit; it adds `process-audit` only to its *Scope*, as the sentence in WAY-328 and in itself
   requires. WAY-328 (departure from product guidelines) and WAY-344 (a requirement) are consistent with
   the *Rejected* and *Rationale* of WAY-344. The one tension is the Minor finding 1.
4. **Numbering.** `git grep -n -E 'WAY-330\b'`: every hit means the audit's WAY-330 (decisions.md
   `:11032`, `:11056`, `:11260` as *Relations* "derives from WAY-330" of audit entries; the comments and
   text of `process-audit/SKILL.md`, `audit_count.py`, `problem_register.md`, `test_audit_count.py` about
   the register of problems). No text means the task's decision under the old number. `git grep WAY-344`
   gives only the entry's own heading. `python -B elements/common/foundation_check.py`: `0 errors`, exit 0.
   No tracked file holds "16 parts", "sixteen" or "seventeen" (grep of `foundations`, `README.md`).

## Declined to judge

- Whether `audit_count.py` today meets WAY-344 (it is an existing script that no change of this task
  touches; WAY-344 and the task put such scripts out of scope).
- The contents of the target's changes outside the foundation (the audit's script, tests, skill entry
  points): not reviewed, only checked that the merge left them identical to `3bcad13`.

## Checks run

- `git rev-parse HEAD` — `c32cfe14...`, exit 0; `git status --short` — empty.
- `git diff 3bcad13..HEAD --stat` — one file, 78 insertions, exit 0; full `git diff 3bcad13..HEAD` read.
- `git diff e9a0f92..5922ffc --stat` — one file, 78 insertions, exit 0.
- Entry extraction with `awk` and `diff` of the `5922ffc` entry against the HEAD entry — two lines
  differ (heading and *Scope*); the `diff` exit code 1 is its answer "differs".
- `python -B -c` script parsing the part map and WAY-344's *Scope* — 17 parts, 17 identifiers, sets equal,
  exit 0.
- `git grep -n -E 'WAY-330\b'`, `git grep -n 'WAY-344'`, `git grep -n -i -E 'sixteen|16 parts|17 parts|seventeen'`
  — as in point 4, exit 0 (the last printed nothing).
- `python -B elements/common/foundation_check.py` — `0 errors`, exit 0.
- Not run, by the dispatch: `gate/run_tests.py` (the orchestrator runs it).

## Reaches beyond the dispatch

- `process-audit/audit_count.py` lines `2123-2174` and a grep of its exit codes — to see whether WAY-344
  claims anything about it and how it ends today (point 3 and the Minor finding).
- WAY-331, WAY-332, WAY-337, WAY-338, WAY-339, WAY-341, WAY-342, WAY-343 of `foundations/decisions.md` —
  the handoff named WAY-330 and WAY-343 and "any other whose title bears on scripts, exit codes or tests
  of the audit"; I read these because a grep of WAY-330…WAY-343 for "exit", "absent", "missing", "empty",
  "unknown", "script" and "command" pointed at them.
- `docs/task-cycles/scripts-fail-on-missing-fields/task_frozen.md` lines `40-52` and `100-115` — the
  accepted wording of the Scope requirement and the out-of-scope line.

## Unread material

- Read whole: WAY-328, WAY-330, WAY-331, WAY-332, WAY-337, WAY-338, WAY-339, WAY-341, WAY-342, WAY-343;
  WAY-344 whole; the `process-audit` part-map entry; `task-cycle/review/SKILL.md`;
  `agent-instructions/README.md`.
- Not read whole: WAY-333, WAY-334, WAY-335, WAY-336, WAY-340 (titles and a grep of their lines for
  "exit", "absent", "missing", "empty", "unknown", "script", "command" only; titles do not bear on
  scripts, exit codes or tests of the audit); `task_frozen.md` outside lines `40-52` and `100-115`;
  `review_whole_report.md` and `review_fix_report.md` (first lines only: `PASS 4905a56...` and
  `PASS 5922ffc...`, which confirm the entry was passed at `5922ffc`; I compared the entry itself
  with the entry of `5922ffc` instead); `process-audit/` files other than the lines of
  `audit_count.py` named above.

## Searches not found or unclear

- none
