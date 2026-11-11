# Fix report — Minor findings of the whole-change review (PASS 4905a56)

**Status:** done

Commit: see the return message. Changed: `foundations/decisions.md` only, +5 -6 lines, inside WAY-330.

## Findings

1. WAY-12 sentence in *Rationale*: no change, as the findings file says; the request carries it
   (named in its section for the human's decisions as the cycle's wording). A narrowing of WAY-12 is
   a separate change.
2. *Verification* "violates" example: fixed. The clause "a change adds a reading of a file with no
   test that gives the file without a field" now reads "a new script's reading of a file, or a
   changed script's reworked reading of a file, has no test that gives the file without a field",
   the wording the finding suggests, carrying the qualification of the binding sentence. Check:
   `python -B elements/common/foundation_check.py` — exit code 0, `0 errors`; the lines read back
   with `sed -n 10968,10976p foundations/decisions.md`.
3. The writer's own additions (relation `derives from WAY-38`, the pair of examples, the WAY-12
   sentence): no change, as the findings file says; the request names them as the cycle's choices.
4. *Rejected*, the clause on a new exit code: fixed. It now reads "a new exit code, such as 3 — each
   skill that reads exit codes would have to be extended." It ends at "extended", as the finding
   says. One adaptation, not contested: the suggestion names only the end of the clause, but the
   finding's complaint is the statement "the skills that read exit codes know only 0, 1 and 2", which
   would stay in the clause if only its tail were cut; I dropped that statement as well, so the clause
   no longer says what the skills do today. The dropped tail ("and until then each orchestrator would
   read an unknown code its own way, in exchange for a signal that exit code 2 already gives") is the
   part after "extended". Cost if wrong: the *Rejected* entry keeps a shorter reason; restore the
   source's sentence if Mariusz wants the task's wording whole.

## Checks

- `python -B elements/common/foundation_check.py` — exit code 0, `0 errors` (run after the edits).
- Gate: not run (the orchestrator's). No test written: the change is wording in one foundation entry.

## Unread material

none

## Searches not found or unclear

none
