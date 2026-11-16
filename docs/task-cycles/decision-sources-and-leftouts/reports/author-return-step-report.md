# Author return-step report — decision-sources-and-leftouts

**Status:** done. The step commits nothing; head stays `01ab269`.

## Return step

- **Foundation compared with code:** the change writes no code. I compared WAY-100 and the other
  changed decisions with the files that describe what they bind:
  - `elements/decisions/template.md:47-49` points to WAY-100 by number for how a decision that
    adopts a practice names it; its rules on *Based on* (`:51-71`) and on a measurement a reader
    cannot open (`:57-62`) agree with the new WAY-100 sentence. No change.
  - `elements/common/rules.md` (the `TODO` form of a decision's *Based on*) agrees: no `TODO` is
    left in any *Based on*, and every source found is cited or described. No change.
  - `elements/environment-facts/template.md:43-60` ("Which facts are written") agrees. No change.
  - Skills and other files citing WAY-100's wording: a search of every tracked `*.md` for `WAY-100`,
    "from outside", "method or practice", "borrow", "likeness", "what it leaves out" finds WAY-100
    named only in the decision log and at `elements/decisions/template.md:49`; no skill restates
    its second paragraph. No change.
  - `agent-instructions/README.md`: no mention of WAY-100 or of outside sources. No change.
  - Tests with a line `decision:` for any of the changed decisions: none found (search of the whole
    repository for `decision: WAY-<n> ` for each of the 26 numbers). Nothing to update; no pair of
    examples loses a part to a test.
  - Part map, part `decisions` (`foundations/part_map.md:7-15`): its files and dependencies are
    untouched by the change and still match. No change.
  - WAY-136 unchanged, as the foundation step judged (evidence only).
- **Decisions written or changed in this step:** none.
- **Invariants:** none (the handoff and the step write none for this change).
- **Environment facts:** none written. The two citations the change added fail WAY-90's test, as
  `elements/environment-facts/template.md:45-48` gives it:
  - WAY-164, Limen `templates/worker.md` line 25: the place the-way took a practice from. Were Limen
    to change or drop that line, the practice would stay the-way's and WAY-164 would not be called
    into question; it is no finding about agents or models and no behaviour of a tool the process
    uses. It is quoted "as a precedent".
  - WAY-199, Open Mercato `customers/AGENTS.md` line 7: the origin of the status `exemplar`. A change
    in Open Mercato would leave WAY-199 as true; Open Mercato is no tool the process uses. Quoted as
    a precedent, like the Open Mercato and Google citations already in those decisions.
- **Glossary terms:** none. The change uses "trace", "source", "practice" in their ordinary meaning;
  no term is used against its entry.
- **Part-map changes:** none.
- **Projected entries:** none — the task carries none.
- **Rows of *Settlements to record*:** rows 1 and 2 are written in WAY-100's second binding paragraph
  (foundation step, commit `05b4648`). No row was missed.
- **Choices that bind after the merge (WAY-36):** none found that is no row. The *Based on* `none`
  with the source described in *Rationale* for a closed course source applies WAY-100 and the form of
  WAY-121 and five other decisions already in the log; it is no new rule. The other choices of the
  change (where the description of the roadmap practice stands, which leftovers to list) end with the
  work and stay as choices of the report, for the orchestrator's questions table.
- The review-of-fix finding N1 is not mine to fix and is not touched.

## Checks

| Command | Exit | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` (run after the fix, on `01ab269`; no file changed since) |

Searches above were made with the search tool, not commands. Not run: the full gate (the
orchestrator's). No test changed or written.

## Working copies

None made in this step; `.runs/author/` does not exist (`.runs/` holds only `task-cycles/`).

## Unread material

- `elements/environment-facts/skill/SKILL.md`: not read — no entry was written, and the template's
  section "Which facts are written" (read, lines 1-70) gives the test.
- `reports/review-fix-report.md`: not read; the handoff states its result and N1.

## Searches not found or unclear

none
