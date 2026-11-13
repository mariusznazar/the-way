# Return step for the correction — report

**Status:** done. **Commit:** none needed (head stays `2f9c200`; the worktree is clean).

## Check

`python -B elements/common/foundation_check.py` (the full check), run on the unchanged tree: exit 0, `0 errors`. I made no edit, so no run followed an edit. The product's gate was not run.

## What was compared

The correction's range, read by `git diff e00264a..2f9c200` for `foundations/decisions.md`, `task-cycle/gate_times.py`, `process-audit/audit_count.py`, `process-audit/SKILL.md` and `task-cycle/skill/SKILL.md` (tests not read, only listed by the stat), against WAY-350 as the correction edited it and against the entries a search of the foundation found. The search: `foundations/*.md` for "earlier form", "failed run", "run that failed", "exit code is unknown", "far future" and "registry", and the entries named in the handoff, read whole where they bear on the correction.

| Entry | Compared with | Result |
|---|---|---|
| WAY-350, binding sentences ("a run that has not ended counting for at most six hours, an ended one kept for a day and an entry whose times cannot be, such as an end in the far future, deleted and counted for nothing"; the audit compares "only over the runs that passed and during which no other such run was going") | `gate_times.py` `prepare` deletes at the start of a run an entry that is stale or `malformed` (a start or an end more than a minute after the present, or an end before its start); `count_others` skips a `malformed` entry, so it counts for nothing. `audit_count.py` `gate_values`: a run is on the compared side only when `run.others == 0 and run.code == 0`; every other run (company, unknown count, failed, unknown exit code) is on the side shown apart | matches |
| WAY-350 *Verification* (complies: the runs with company, the runs that failed and the runs of unknown exit code are listed apart; a version in which every run had company or failed gets no median and no comparison; violates: a run that failed enters the median) | `gate_values`, `gate_rows` (`median_of(alone)` is `None` then, so `Falls` is `unknown`); the header `Runs compared` and `Runs not compared`; the explanation printed in *Measure versions* | matches |
| WAY-350 *Rationale* and *Rejected* (a failed run says how soon it failed; the runs that failed taken into the median) | the line the count prints in *Measure versions* says the same ("a failed run's time says how soon it failed, not how long the gate takes") | matches |
| WAY-348 (the count shows each cycle's values and, per version, the median and whether it falls) | the new one-row form for a version in which no cycle gives a value or no run a time (`—` for the measure, `unknown` median, `unknown` falls, one line in *Unknown values*) | no clash. The entry says the count shows a median and its fall; a version with nothing to take a median of shows `unknown`, which the entry already allows for the gate ("gets no median and no comparison"). Not changed |
| WAY-349 (the script runs the gate and records times; no output of the gate in the file; the run is the orchestrator's alone) | `gate_times.py` changed only in what it does with registry entries; `task-cycle/skill/SKILL.md` step 10 now says that an exit code 2 with an `Error: gate_times.py:` line is the script's failure and the orchestrator does as step 12 gives, and step 12 says to record it as a check that did not run, fix the call and run again, and never write the file by hand | matches (WAY-160 asks that a check that did not run be named; the instruction does that; the "by hand" ban is what WAY-349's *Rejected* says) |
| WAY-344 (missing fields; earlier-form cases of the stage report) | the correction adds no reading of a field. `read_optional` now gives the reason "an earlier cycle, or a script that failed" for an absent `mechanism_measures.md` or `gate_times.md`; an absent file is no field of a file, gives unknown and no `Error:`, as before | no clash; not changed |
| WAY-339, WAY-352 | not touched by the correction | no clash |
| Part map `task-cycle` (trust boundary names `gate_times.py`) and the external-context row of the user's places (names the registry) | the correction only makes the script's handling of a damaged registry entry stricter; the script still lists, creates and deletes files in that directory | matches; the trust-boundary line fits better, not worse |
| `process-audit/SKILL.md` and `task-cycle/skill/SKILL.md` (instruction files of the change) | the sentences for the one-row form, the runs not compared, a missing file that may be a failed script, and a failing measuring script, against `audit_count.py` and the two entries | match |

## The known point: "an end in the far future"

WAY-350 says an entry "whose times cannot be, such as an end in the far future" is deleted. The code deletes, besides a far end, a start more than a minute after the present and an end before its start. The words "such as" keep the entry true for all three, and the entry's own phrase "whose times cannot be" is the rule; "an end in the far future" is an example. I left the wording as it is: naming the three cases, or the one-minute slack, would put the code's detail into a binding sentence, which is wider than the decision needs, and the slack is the script's own constant. Cost if wrong: a reader who takes the example for the whole rule would call the deletion of a reversed pair a violation; the *Verification* and the docstring of `gate_times.py` (which names the three cases) answer that reader.

## What no longer matched

None. No entry was written or changed.

- Decisions written or changed: none.
- Invariants: none.
- Environment facts: none.
- Glossary terms: none; "run", "compared", "failed" and "passed" are plain words in the sense the correction uses them.
- Part-map changes: none.
- Rows of *Settlements to record* and projected entries: nothing to write; the eight rows were written earlier and the task has no project definition.

## Choices

- **No edit to WAY-350's wording or line length.** Three lines of the entry run to 101-104 columns (lines 11601, 11606 and 11630 of `foundations/decisions.md`, the last two by the correction), and the log is wrapped near 100. Rejected: rewrap them in this step, since the handoff says to commit only if something needed correcting and a rewrap changes no meaning. Cost if wrong: a reviewer who counts columns finds the lines; the fix is a rewrap.
- **No change to WAY-348** for the one-row form (above). Rejected: add "or `unknown` where no cycle gives a value" to its binding sentence, which would be an entry the correction does not call for. Cost if wrong: a reader may take a version with no values, shown as one row, for a departure from "the median of each measure"; the entry's *Verification* does not say how such a version is shown, so no reading of it is violated.
- **The Minor findings of the review** (the stale comment at `process-audit/audit_count.py:371` and two overlong lines) were not touched; they are not mismatches of an entry with the code.

## Unread material

- The tests of the correction (`process-audit/test_audit_count.py`, `task-cycle/test_gate_times.py`): not read; the stat lists them.
- `reports/correction-report.md`, `reports/correction-review-report.md` and `reports/correction-remarks.md`: not read; the handoff and the diff were read instead.
- `process-audit/audit_count.py` and `task-cycle/gate_times.py`: read the hunks of the range, not the files whole again (read earlier in this task).
- WAY-348, WAY-349, WAY-344, WAY-339, WAY-352 and WAY-160: read in this task before the correction; the passages of them that the correction touches were re-read through the search, not each whole again.

## Searches not found or unclear

none
