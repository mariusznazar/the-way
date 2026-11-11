# Return step report, after the correction — cycle `cycle-remarks-batch-4`

**Status:** `done` — nothing no longer matches; **no commit** made. Head compared: `10d443f`
(range `e3825a8..10d443f`).

## Return step (fields of the record)

- **Foundation compared with code:** compared WAY-160, WAY-71 and WAY-287 (as the correction left
  them), WAY-27, WAY-17, WAY-163, WAY-294, WAY-58, the glossary entries `gate` and `return step` and the
  part-map entries `decisions`, `task-cycle` and `elements-common` with the files of the repository on
  this head and with the human's remarks (`reports/11-correction-remarks.md`). Result: all match.
  - WAY-71 binding sentence and `elements/common/rules.md` carry the same extended sentence (checked
    in the correction by whitespace-collapsed comparison); the decision template (*Based on* form, the
    bullet on *Relations*/*Origin*), the invariants template (*Rests on* and *Derives from* forms in the
    form lines and in the *Links* bullet), `foundation_check.py` (`missing_thing` for the three fields,
    `Relations`/`Origin` not taking `TODO`, docstring) and its tests say the same. WAY-71's
    *Verification* examples read true: `Based on: TODO — <what is missing, with its source>` is now a
    form the script accepts. The foundation of the-way holds no `TODO` in the five fields
    (`foundation_check.py .`: 0 errors).
  - WAY-287 (binding sentence, rationale, examples) and item 15 of `request_template.md` cover the same
    three fields, on the tree after the change, one item for each gap.
  - WAY-160's *violates* example names the gate failure whose fix the return step does not compare, and
    step 10 of `task-cycle/skill/SKILL.md` carries the rule; WAY-163 and `blocked_finding.md` agree.
  - WAY-27 and the *Origin* section of the decision template; WAY-17 and the invariants template; WAY-294
    and `remarks_check.py` — unchanged by the correction and still matching.
  - WAY-58 (*Derives from* when no decision carries the invariant): its two forms, a quoted source and
    `recovered from code`, are unchanged and do not claim to be the only forms; the `TODO — <the decision,
    and where it is expected>` form is the case of a decision not yet written, which the invariants
    template and WAY-71 already hold. No sentence of WAY-58 contradicts the new rule.
  - Glossary `gate` and `return step`: used in their meaning. Part map: no file added, removed or moved
    and no responsibility changed; the three entries need no edit.
- **Decisions written or changed:** none in this step.
- **Invariants:** none.
- **Environment facts:** none.
- **Glossary terms:** none.
- **Part-map changes:** none.
- **Projected entries:** none carried (projected-mode forms read in the correction; no conflict).
- **Rows of *Settlements to record*:** none.

## For the human, not changed here

- N-1 (the reviewer's remaining Minor finding): a mixed list such as `python-stdlib-modules · TODO` in
  *Rests on* is read as a list of facts with a `TODO` item, which the script does not report, against
  the rule that a bare `TODO` is an error; the docstring of `foundation_check.py` says so.
- A cosmetic leftover: the line ending "...while each remaining finding stands with its place in the
  code in the" in WAY-287 is longer than the 100 columns of its neighbours (the rewrap of the correction
  stopped one line early). Not a mismatch; not changed, since a commit would start a new review.
- M-5's remaining part (a *Relations* link from WAY-287 to WAY-71) as the first return step named it;
  M-4 is closed by route B.

## Checks (command and exit code)

- `python -B elements/common/foundation_check.py .` exit 0 ("0 errors").
- No commit, so no other check run.

## Unread material

none read in part beyond the compare: handoff, `return_step.md` and `foundation_step.md` read whole;
WAY-71 and WAY-287 read whole (current text), WAY-58 whole; the rest of the compare used the texts read
in the correction and the first return step, and WAY-160, WAY-27, WAY-17, WAY-163, WAY-294 and the
part-map entries and glossary entries were not re-read in this step (they are unchanged since the first
return step except WAY-160's *violates* line, seen in the correction).

## Searches not found or unclear

none
