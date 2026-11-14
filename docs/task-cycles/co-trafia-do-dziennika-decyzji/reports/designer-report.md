# Designer report — revision of the spec of "co trafia do dziennika decyzji"

Status: done. Revised spec: `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md` (the reviewed one is
`spec-reviewed.md`). Reviewer's report: `reports/spec-reviewer-report.md`; rulings: `reports/designer-revision-handoff.md`.

## The four findings and where the revision settles each

1. The line for an unknown base broke `installation/test_install.py::test_empty_foundations_have_valid_form`
   (ruling: the reviewer's way (a)). Settled in D1: the line is written only where the working tree's
   `foundations/decisions.md` holds at least one decision. Constraints now says every other existing test that
   runs the script or reads its report, the installation tests included, passes as it stands, names that test,
   says the change edits no installation test, and says `test_cross_part_imports.py` keeps its imported names.
   D9 adds the test for a repository with no commit and an empty log, which reads no such line.
2. The pair of examples written at the foundation step and trimmed later had no file (ruling: the first way).
   Settled in D2 ("Where the two halves of the rule below stand") and in the list of D6: a bullet in
   `elements/decisions/skill/SKILL.md` step 3 (a decision whose test a later slice writes carries a pair for
   now) and a clause in `task-cycle/skill/return_step.md` (it removes from the pair the part a test then holds
   and names the test by `tests:`). The line for the human, with the open alternative (the switch also skipping
   the error, WAY-321 changed), stays as it was.
3. "Rationale and rejected options stay whole" was missing from WAY-12. Added to the WAY-12 line of
   *Foundation entries* and to D3.
4. A file missing at the base. Settled in D1 by one more bullet: a base that lacks `foundations/decisions.md` or
   `foundations/invariants.md` makes the base unknown for that file, never an empty file (no decision changed,
   no invariant listed, the line of finding 1 written under the same rule, naming the file). D9 adds the
   cases for both files.

Also taken in, as the handoff asks:

- WAY-241, WAY-237, WAY-235 and WAY-268 are named under "Other decisions of the log the change reaches", each
  with the way it is met (read in their binding sentences from the log for this revision). WAY-17's consequence
  is stated: the one decision of the real log that nothing holds; if the search edits its sentences it needs a
  pair.
- D9 adds the test for an invariant with no *Method* at the base or now.
- The word: the script compares the "binding sentences" of an entry (the glossary's word), not the "binding part",
  which may include fields; the spec says so in D2 and uses the one word, and WAY-12 and its attached paragraph
  are to say "binding sentences".

The task is not widened: no new file, argument, switch or exit code is added; WAY-321 stays as it is.

## Ways weighed (unchanged from the first report, with the two the review put to a choice)

- Unknown-base line: only where the log holds a decision (chosen) against naming the installation test among the
  tests the change edits (rejected: it would alter an installer test for a line nothing needs).
- Temporary pair: two halves in two files (chosen, as the orchestrator's answer to the switch requires) against
  letting the switch also skip the error (kept as the open alternative in the line for the human).

## The four checks

1. Placeholder, `TBD`, empty section: none found.
2. Contradiction: none found after the revision; the "binding part" and "binding sentences" uses were made one
   word, and D1, Constraints and D9 agree on the unknown-base line and the empty log.
3. Scope: still two independent changes in one spec (process texts; the script with its tests and request
   wording); point 8 alone could be its own task, as the task says. Left as one.
4. Two readings: a file missing at the base and an empty log were the two found by the review; each now has one
   reading in D1.

## Reaches beyond the dispatch

- This revision: the binding sentences and *Verification* of WAY-241, WAY-237, WAY-235 and WAY-268 (a search for
  their numbers in `foundations/decisions.md` and a read of their first lines).
- Earlier, kept from the first report: `foundation_step.md`, the decision skill's `SKILL.md` and `projected.md`,
  `change/SKILL.md` and `review/SKILL.md` (a few lines), `installation/README.md` (parts), `agent-instructions/README.md`
  (top), `foundations/part_map.md`, `project-level/readiness_check.py` (grep), `foundations/invariants.md`
  (grep), the 91-entry sweep of *Scope* lines for `decisions` and `elements-common`.

## Unread material

- WAY-241, WAY-237, WAY-235 and WAY-268: read only to the end of their first paragraph and the start of *Based on*
  (about fifteen lines each); their *Verification*, *Rationale* and *Rejected* not read. WAY-135 and WAY-136, which the
  reviewer names beside WAY-268, not read.
- The reviewer's report: read whole. The handoff: read whole.
- Decisions of the 91-entry sweep read by title only: WAY-41, 52, 53, 84, 85, 89, 101, 102, 103, 104, 121, 122, 123,
  137, 138, 165, 166, 267, 270, 322. Entries whose *Scope* names `project-level`, `task-cycle` or
  `product-guidelines` and not `decisions` or `elements-common` were not swept (the reviewer searched them; WAY-241,
  237 and 235 came from that search).
- `foundations/invariants.md`: by grep only. `task-cycle/request_check.py`: lines 1–120 only.
- The revised spec itself was edited by string replacement and not read through again whole after the last edit; its
  sections were checked by search for the terms changed.

## Searches not found or unclear

- Whether the guidelines rule found by the cycle has a kind of its own in `request_template.md`: the spec extends
  kind 6 and leaves a new kind number to the maker as equivalent (unchanged).
- WAY-344 and the base file: the text does not say whether the new reading of the base commit's file is a "reading of a
  file the rule covers"; the spec takes the safe reading and has D9 test it (unchanged).
- No decision of the log says how a script finds the main branch, or whether the surface `foundation-check-command`
  allows new `listed:` lines; the spec reads "path, argument and exit codes" as not covering added report lines
  (unchanged).
- The task text calls the column's neighbours by *Kind* only in `project-level/task/template.md`; no script reads that
  column (found by the reviewer, confirmed by my grep earlier).
