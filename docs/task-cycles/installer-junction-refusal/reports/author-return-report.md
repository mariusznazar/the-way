# Author return report — installer-junction-refusal

## Status

`done`

## Commits

- `e899494` — State the junction fact for the call the installer makes (`foundations/environment_facts.md`, +2/-2)

Not pushed. Nothing else needed changing.

## Entries compared with the code

Read: `task-cycle/skill/return_step.md`, `foundation_step.md`, and the decisions WAY-36, WAY-95, WAY-11 (each whole), the decision template's "Decision or invariant". Code as it stands on `ee6126c`.

| Entry | Compared with | Result |
|---|---|---|
| invariant `installation-paths-through-links` (new, row 1) | `install.py`: `is_link` at `check_parents`, `stale_agent_definitions`, `stale_entry_points` (now also `.claude`/`.agents` themselves) and the `.the-way` check in `plan`; the junction tests; the two symlink tests that cite it | Matches. "refuses before it writes anything where such a link stands on the path of a file it is to write or is `.the-way`": `check_parents` runs for every written path before any write, and `.the-way` as a junction is refused with a pin ("not a submodule directory") and without one (`lexists`, run by hand in the first task). "neither writes nor deletes ... with its own code": removal skips instead of refusing, as the sentence says. Git's writes under `.git` stay outside, by the orchestrator's ruling. No change. |
| environment fact `python-junction-detection` (new) | the code calls `Path.is_junction()` (`install.py:308`), the fact quoted `os.path.isjunction` | **Did not match; corrected** (below). |
| decisions in play: WAY-48, WAY-13, WAY-38, WAY-328, WAY-235 | the change | Unchanged and still true: `installation/install.py` is the trust boundary and was checked for crafted input; the means is the standard library (`Path.is_junction`, `_winapi` in a test — `sys.stdlib_module_names` holds it); WAY-328/WAY-235 as the first report said. |
| decisions found by *Scope* `installation`: WAY-34, WAY-141, WAY-368 | the change | Unchanged and still true: the installer rewrites and deletes only its own files (WAY-368 verification) — the change only adds cases where it does not delete; WAY-141 concerns `CLAUDE.md` only. |
| row 1 of *Settlements to record* | the invariant | Written whole (first report), narrowed in the fix to "with its own code"; its meaning — the installer neither writes nor deletes through a link and refuses before writing — kept. |
| part map: `installation` (trust boundary `installation/install.py`), `invariants`, `environment-facts` | the files the change touched | All files stay under their parts' patterns (`installation/**`, `foundations/invariants.md`, `foundations/environment_facts.md`); `installation` still depends on nothing new (the test imports `install` and the standard library); no change. |
| part map: surface `installation-command` | the change | Not widened (the orchestrator's ruling): it promises that the installer "rewrites only its own ... and deletes only its own", which the change keeps true. No change. |
| search of the whole foundation (WAY-33) for `junction`, `symlink`, `symbolic link`, `.git/modules`, `os.path.isjunction` | all of `foundations/` | Only the new entries and one unrelated environment fact about `AGENTS.md`. No other entry states or contradicts the rule. |

## What was corrected

`python-junction-detection` (environment fact, `the cycle's`): the code and the invariant's meaning rest on `Path.is_junction`, which `install.py` calls, not on `os.path.isjunction` (the fix's choice, which the review's note B pointed out). The entry now reads: "In Python 3.14, `Path.is_junction` returns true if the path points to a junction and false for any other type of file, and only Windows supports junctions." Source: `https://docs.python.org/3.14/library/pathlib.html`, archived `http://web.archive.org/web/20261021035154/https://docs.python.org/3.14/library/pathlib.html` (2026-10-21, the latest existing capture by the archive's CDX index), § Path.is_junction — "Return True if the path points to a junction, and False for any other type of file. Currently only Windows supports junctions."; read 2026-11-14. I fetched the live page and the archived copy and both hold the passage word for word, in one paragraph. This also gives "Windows junction" in the invariant's sentence a source for the word "Windows" ("only Windows supports junctions"). The invariant's `Rests on: python-junction-detection` is unchanged (the identifier names what the fact is about). `foundation_check.py` after the change: exit 0, `0 errors`.

- Meaning, English: Python 3.14's `Path.is_junction` recognises a junction, and only Windows has junctions. Po polsku: `Path.is_junction` w Pythonie 3.14 rozpoznaje junction, a junction istnieją tylko w Windows. Mark: `the cycle's`.

## What was decided, with reason

- **A choice that binds after the merge (WAY-36), for instance that the installer skips a stale entry through a link but refuses a write through one: no decision; it stays in the choices of the cycle record.** Reasons: (1) The behaviour is the installer's existing one for a symlink, kept by item 5 of the first handoff and held by an existing test; the task makes no new choice between ways about it, so there is nothing to put in *Rejected*, and the answer to question 1 of the task ("wherever it recognises a symlink today") is a scope, which the invariant states and a test holds. (2) The rule that binds after the merge, and is false on a commit that breaks it, is already an invariant with a test, as the decision template's test gives ("can you point to a commit on which the sentence is false? yes — an invariant"); a decision restating it would repeat its sentence without a rationale the foundation lacks. (3) A decision written here would have to carry a *Rejected* from the human; the task keeps only "only on the write path" as the way not chosen, in the task document, whose record leaves the final tree. If the human wants that rejected way in the log, it is a decision of its own, to be asked for.
- **A glossary term (WAY-95): none.** "Junction" means in the product what it means to a reader who knows the field (a Windows directory link), and "link" is used in the sentence for "a symbolic link or a Windows junction", which the sentence itself says; no sentence of the product's files would be read wrongly by a reader with the field's meaning, which WAY-95 requires for a narrower meaning.
- **Part-map change: none**, as the table above shows; the surface is not widened by ruling.
- **Review note A (a README clause that git's own writes under `.git` are outside what the installer checks): not made.** Nothing in the README says `.git` is checked: the added sentence names the paths where a junction stops the run, and "wherever the installer checks for one" is true as written. So it is no "what no longer matches"; a clause would be a new statement of a limitation, which is the invariant's and the human's at the merge.
- **Review note B: made**, as the correction above.
- Invariants written by the return step: none. Rows of *Settlements to record* written: none beyond row 1, already written whole (`installation-paths-through-links`); nothing was missed.

## Written or changed in this step

- Decisions: none. Invariants: none. Environment facts: `python-junction-detection` changed in place (`the cycle's`). Glossary terms: none. Part-map changes: none. Rows of *Settlements to record* written in this step: none.

## Own-work check (WAY-164)

Requirement most likely not met: that every entry the change writes matches the code it rests on — found one gap (the fact named a function the code does not call), corrected. The check: read `install.py` for the call (`grep is_junction|isjunction` → only `Path.is_junction()` at line 308), fetched the page, compared the passage word for word on the live page and the archived copy (both `True`), and ran `python -B elements/common/foundation_check.py` (exit 0, `0 errors`). A second gap I looked for and did not find: another entry naming `os.path.isjunction` (grep of `foundations/`: none left). I did not run the installer's tests again: nothing in code or tests changed in this step; the last run is the fix's, `python -B gate/run_tests.py installation` exit 0, 60 tests.

## Reaches beyond the handoff

- Network: the pathlib page and its archived copy, and the archive's CDX index (for the correction).
- `elements/decisions/template.md` section "Decision or invariant" (to weigh the WAY-36 question).

## Unread material

- `reports/review-whole-report.md`, `reports/review-fix-report.md`: not read (the handoff states their verdict `PASS ee6126c`, and the two notes it asks me to weigh).
- The `SKILL.md` of an element: not read again in this step, as I wrote no new entry by its skill; the change to the fact followed `elements/environment-facts/template.md`'s rules as read in the fix.
- Everything else the handoff names was read whole.

## Searches not found or unclear

- None.
