# Report of the fix of C1

**Status:** done. C1 fixed, not contested.

## How
`foundations/decisions.md`, WAY-165 only (still three binding sentences):
- the clause on an entry that leaves part of a matter unanswered now reads: it does not settle the matter at a project definition, while in a run at a task (WAY-267) it holds the choice like any decision, which opens only on the human's word. This agrees with `task_run.md`.
- *Verification*: a complying example added (at a run at a task the item over a silent logs decision stays `— held by` until the human's word opens it); the violating example "a logs item stays `— held by` or `— projected`..." is limited to a definition's list, and a violation added (an agent opens, in a run at a task, a silent logs decision with no word of the human).
- *Rationale*: the sentence on a partial entry is limited to a definition, with a clause that at a task no gate follows and opening a decision stays the human's (WAY-267).
WAY-267, WAY-270, WAY-139 and the files unchanged; a definition's behaviour unchanged. I read WAY-270 and WAY-139: neither states how a silent decision opens at a task.

## New meaning sentence, WAY-165 (Polish)
Pytanie o logi obejmuje też to, jak długo zapis żyje, także między wdrożeniami; wpis, który zostawia część tego, o co pyta sprawa, bez odpowiedzi, nie rozstrzyga jej przy definicji projektu, a w przebiegu przy zadaniu (WAY-267) trzyma wybór jak każda decyzja, więc otwiera się tylko na słowo człowieka.

## Checks (command, exit code)
- `python -B elements/common/foundation_check.py .` : 0
- `python -B gate/run_tests.py project-level` : 0
- Full gate: not run (the orchestrator's).

## Searches not found or unclear
none new.
