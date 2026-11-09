# Return step report

**Status:** done. **Commits:** none (nothing no longer matched). Head stays `7c3161a`.

## Comparisons: what no longer matched, and the correction

| Compared | Against | Result |
|---|---|---|
| WAY-61 (binding sentences, examples, *Rationale*, *Rejected*) | `elements/invariants/template.md` "Method and test", `elements/invariants/skill/SKILL.md` (projected mode, step 3), `skill/write.md`, `foundation_check.py` | Matches. The skill's projected-mode sentence and WAY-117's example stay as the task's question 4 settles. `write.md` ("the test is written in the change that brings the entry") agrees with the new sentence. Correction: none. |
| WAY-321 | `foundation_check.py` (switch name, what is skipped, usage), `way_of_working.md` step 4.3, `installation/README.md`, the one command of the-way's gate | Matches: the switch skips only the citation report; the-way's own test and a product's one command run without it. Correction: none. |
| Invariant `test-method-citation` | `foundations/invariants.md` fields, its derivation from WAY-61 and WAY-321, the citing line in `test_the_way_foundation_passes`, the script's behaviour on the-way (19 `test` invariants, all cited) | Matches; `python -B elements/common/foundation_check.py` exit 0, `0 errors`. Correction: none. |
| WAY-16 | the one command of tests / gate | Matches (the check lives in the script the one command runs). none |
| WAY-65 | the script counts a comment line `invariant: <identifier>` in a tracked non-Markdown file, as WAY-65 gives the citation | Matches. none |
| WAY-63 | a `test` invariant without a citing test gets no result; the new check turns that silence into an error | Matches. none |
| WAY-160 | gate run by the orchestrator alone | Not touched; no statement of it changed. none |
| Other statements of the old rule ("reads `review` until the test is written") searched in `task-cycle/`, `project-level/`, `elements/`, `foundation-review/`, `product-guidelines/`, `foundations/` | | Only the places the task's question 4 leaves unchanged remain (`elements/invariants/skill/SKILL.md:57`, WAY-117's example, WAY-71's rationale about an invariant with no test at all). none |
| Part map: `decisions`, `invariants`, `elements-common`, `foundation-check-command`, `test-runner-command` | files and behaviour | `foundation-check-command` keeps its path, its argument and its exit codes; an optional switch is added and the codes keep their meaning. Descriptions of `elements-common` and `invariants` still match. none |
| `installation/install.py` generated guidance (`:168-176`) | the script | Still true (checks the foundation; before a merge, run without a switch). none |

## Entries written in the return step

- Decisions: none. Invariants: none beyond row 3 (written by the foundation step). Environment facts: none (the change rests on no source outside the product the foundation lacks). Glossary terms: none — "finished change" and "citing test" fail the WAY-95 test (a reader who knows the field reads them as they are used; WAY-160 already uses "finished change" with no entry; "invariant test" and "slice" have entries). Part-map changes: none.
- Rows of *Settlements to record*: rows 1–3 confirmed written: row 1 WAY-61 (edited), row 2 WAY-321 (new), row 3 `test-method-citation` (new). No row is missing; nothing written that no row set.

## Known open points (reported, nothing changed)

1. **WAY-61 *Scope* does not name `task-cycle`**, although the new sentence speaks of a later slice of a change (a thing of the task cycle). A change to the cycle's planning text would then not find WAY-61 by *Scope*. Outside the task's four items; left as is. Cost if left: that reading depends on the search of the foundation (WAY-33). Cost if changed: one word in *Scope* and a new reader for every change to `task-cycle`.
2. **The planned-slice gap** (`task-cycle/plan/SKILL.md:169-172`): a slice's *Checks* are its tests and those of the invariants it reaches. A slice that writes a `test` invariant before the slice that writes its test reaches `test_the_way_foundation_passes` (it reports the uncited entry, run without the switch), so that focused check fails between the two slices; the task's *Context* records this and carries no item for it. Left as is. In the one-author route of this task there is no such moment; it can appear on a planned route in the-way.

## Searches not found or unclear

- None beyond the two open points above.

## Check

`python -B elements/common/foundation_check.py` — exit 0, `0 errors`; the working tree is clean (`git status --short` prints nothing). No full gate run (the orchestrator's: exit 0, 834 tests on `7c3161a`).
