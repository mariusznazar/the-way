# Foundation stage report

Status: complete at foundation-only boundary; dependent instructions remain unchanged.
Author: /root/author, inherited model.
Worktree: C:/Storage/repos/the-way-lean-cycle-orchestrator.
Branch: task/lean-cycle-orchestrator; no upstream is configured.
Input/base commit: 41cfbe55c17981500490ffddd24fc1fe0ec1c6ef.
Foundation commit: 18602fd699410b2906f04a4492bcdbdea743759e.

## Authority and inputs

Read the complete frozen task at `docs/task-cycles/lean-cycle-orchestrator/task.md` and
`reports/author-foundation-handoff.md`. The frozen task is ready, independent, has no human
actions, and carries five accepted settlements. Its predecessor is integrated in the base.
The named revisions are already authorized; this report does not claim an agent approved them.
No new design choice or size obstacle was found. No skill or code was changed in this stage.

Read the worktree's `AGENTS.md`, `agent-instructions/README.md`, complete
`task-cycle/skill/SKILL.md`, `.agents/skills/the-way-record-decision/SKILL.md`,
`elements/decisions/skill/SKILL.md`, `elements/decisions/template.md`,
`elements/decisions/examples.md`, `elements/common/rules.md` and
`elements/common/way_of_working.md`. WAY-03 was read whole as the required example.
These files and all selected entries were read from the named worktree at the base revision.
The skill-conventions file named in the handoff is for the later skill-edit stage and has not
been needed or read yet. No writes occurred outside this worktree.

## Selection and whole-foundation search

Touched part: task-cycle. WAY-44 assigns a collected entry's change by its scope, rather than
assigning every decision-log edit to the decisions part. Complete `foundations/part_map.md`
read, including dependencies, all failure modes, flows, surfaces, context, scales and exclusions.
Criticality remains high; there are no changed trust-boundary files or irreversible operations.

All current Scope fields were independently inspected, with wrapped values included. There
are 52 expected task-cycle matches at the input revision. Each was read whole from the
authoritative decision log, including rationale and rejected options:

WAY-01,03,09,10,11,13,16,21,25,26,27,28,30,33,34,36,37,38,44,45,46,47,48,51,55,57,
62,63,65,68,69,82,89,100,101,102,103,106,120,124,125,126,127,134,135,136,140,144,
147,148,149,150; all version 1. Expected minus read: empty. No repeal or later version was omitted.
The task explicitly names WAY-148,125,16,63,136; these are in that set.

Additional whole reads for governing rules or search findings:
WAY-02,05,07,12,14,17,18,19,22,31,32,61,80,83,112,113,114,118,146,151,152,153,154,
155,156; all version 1. Unrelated linked branches were not recursively loaded merely because
they existed. Current invariant Part fields were inspected with wrapped values included;
48 complete entries were read, selected through `every`, `task-cycle`, and the critical-flow
entries `decision-guard-stale-reference` and `skill-entry-points`. The glossary was read whole,
including all Avoid spellings. The distinction between a task-cycle orchestrator and the
glossary's `project orchestrator` is preserved.

Whole linked fact entries read: git-path-patterns, python-stdlib-modules,
impossiblebench-test-modification, llm-self-preference, llm-decision-violation-detection,
instruction-density-accuracy, visible-scoring-reward-hacking, oracle-in-loop-building,
python-314-bugfix-status, python-release-binaries, claude-code-project-skills,
claude-code-nested-skills, codex-repository-skills and codex-skill-paths. None was changed or
claimed newly observed. No new environment fact is required by a policy framed against the
available tool and active instructions, rather than a permanently assumed tool timeout.

WAY-33/WAY-37 search domain: all of `foundations/`, including decisions, invariants, glossary,
part map and environment facts, not just task-cycle scopes or existing links. Search expression:
`orchestrat|poll|waiting|wait for|full (report|diff|output)|focused checks|rerun|repeat.*(test|read)|reads? .*method|Superpowers|handoff`.
Incoming-reference search: `WAY-(125|148)@` across the entire foundation. Positive controls:
the task's WAY-125 and WAY-148 were both found; the glossary's separate project-orchestrator
entry and project-level decisions were also found outside the touched scope. Environment facts
were inspected for headings and these concepts; no waiting-capability fact exists.

Findings and disposition:

| Finding | Disposition |
|---|---|
| WAY-125 adopts methods and defines the orchestrator's boundary | Revise in place to assign complete method reads to the conducting agent; preserve adopted methods, version and approval boundary. |
| WAY-148 already distinguishes routine progression from a ruling needing evidence | Revise in place to make non-duplication explicit and preserve whole reads by their responsible agent; no relaxed evidence requirement for questions. |
| WAY-140 and WAY-148 depend on WAY-125 | Read whole and confirm meaning remains valid; update both incoming fingerprints. WAY-140 binding sentences and approval remain unchanged. |
| No entry answers how the task-cycle orchestrator waits | New WAY-157. |
| WAY-136 assigns independent review but does not assign the orchestrator's full-diff reading | New WAY-158 derives from WAY-136 and WAY-148; WAY-136 stays unchanged. |
| WAY-13/149 preserve checks and affected verification; WAY-68 forbids a green rerun concealing unresolved failure | New WAY-159 removes only routine duplication, retaining affected verification after change, failure or disputed evidence. No collision. |
| WAY-16/63 define gate execution/result semantics, not where output enters coordination | New WAY-160 preserves the full required gate and all actionable results; no change to WAY-16 or WAY-63. |
| WAY-61 distinguishes a command exit code from an invariant verdict | Reports keep full execution output; this change neither turns exit zero into per-entry pass nor changes verdict aggregation. |
| WAY-47 already reuses coverage from one run | Compatible; no new coverage run or format change. |
| WAY-152–156 and project-orchestrator glossary term concern project leading/refinement | Keep unchanged; the new rules explicitly name task-cycle coordination. |
| WAY-150 retains mandatory complete inputs and foundation search | Reading duties remain with the agent using the material, not waived by short handoffs. |
| No waited-for template, script or foundation element is brought by this change | No WAY-37 repair required. |

After the edit, the expected task-cycle Scope set is the same 52 plus WAY-157–160. The author
read the complete new entries and changed entries while checking the written diff. No other
scope or part was introduced. Before integration, the orchestrator still owes the second
whole-foundation search against the then-current target, as well as the independent assessment.

## Entries and accepted-settlement mapping

Only `foundations/decisions.md` changed: 143 added and 15 removed lines. Existing entries keep
version 1 because the repository has no main branch. There is no invariant or invariant-test edit.

| Accepted task row | Entry | Meaning in Polish |
|---|---|---|
| 1 | WAY-157/1 | Orkiestrator cyklu czeka jednym najdłuższym dozwolonym oczekiwaniem, bez odpytywania i usypiania między sprawdzeniami; ponawia je tylko po rzeczywistym limicie czasu lub przerwaniu, gdy praca nadal trwa. |
| 2 | WAY-158/1 | Pełną różnicę zmiany jednego autora lub plasterka czyta niezależny recenzent, a orkiestrator przy zwykłym przejściu korzysta z listy plików, liczby dodanych i usuniętych linii oraz werdyktu. |
| 3 | WAY-159/1 | Orkiestrator nie powtarza wykonanych testów tylko z powodu zakończenia etapu, lecz korzysta z zapisanego polecenia, kodu wyjścia i pełnego wyniku; brak dowodu wraca do autora, a zmiana lub problem wymaga odpowiedniej weryfikacji. |
| 4 | WAY-160/1 | Orkiestrator sam uruchamia pełną wymaganą bramkę gotowej zmiany, zachowuje pełny wynik w pliku i czyta kod wyjścia, podsumowanie, błędy, niepowodzenia, ostrzeżenia i wyniki unchecked. |
| 5 | WAY-125/1 | Całą metodę i wskazane przez nią materiały czyta agent, który ją prowadzi; orkiestrator czyta własne metody i zna granice etapów delegowanych z cyklu. |
| To do 2 and common evidence contract | WAY-148/1 | Przy zwykłym przejściu orkiestrator nie wczytuje ponownie materiałów ani pełnego raportu etapu, ale przed rozstrzygnięciem pytania, uwagi lub niepełnego dowodu czyta potrzebne źródła. |
| Incoming dependent, no meaning change | WAY-140/1 | Zasada czynności wykonywanych przez człowieka poza repozytorium pozostaje bez zmiany; odwołanie otrzymuje aktualny odcisk WAY-125. |

Changed decisions whose meaning is accepted at this request use
`Approved by: Mariusz, merge of <request link>`. WAY-140's unchanged meaning retains its existing
approval while its relation is refreshed. No private task path is added to the foundation.

## Choices and costs

1. Keep four independent new questions separate, and place method-reading ownership in
   WAY-125 and routine handoff reading in WAY-148. An omnibus decision would be shorter but
   conflate independent choices; the chosen form costs more entries while keeping each question
   independently revisable under WAY-19. No separate decision duplicates an existing answer.
2. Apply diff and focused-check ownership equally to the one-author route and planned slices.
   The base's WAY-136 and cycle step 10 already unify those paths. Restricting the change to
   planned slices would leave the same redundant work on the intended small-task route; this
   interpretation preserves task outcome and review weight, not a new process route.
3. Express waiting against both the tool and active instructions, and permit renewal after an
   actual timeout or interruption. An absolute single call cannot complete work that outlasts
   a bounded tool call. Choosing repeated short polls would contradict the settlement. The
   cost is multiple legitimate waits when an external limit is short; it adds no polling or sleep.
4. Use level 2 verification for the changed and new runtime coordination policies. They govern
   which agent reads, runs or waits during a cycle; the same repository commit can be used by
   compliant and noncompliant sessions. Asserting that prose contains prescribed words would
   verify prose presence, not those actions. No new sentence true or false on every commit was
   found under WAY-12/22; an unknown checking method was not used as an excuse to omit an
   invariant. Existing record, assessment and source invariants remain intact.
5. New policy entries use `Based on: none`, `Origin: none`, `Review when: none`: these are
   accepted standing choices, with the complete trade-off in the entries, not empirical claims
   that depend on a tool version or predictions awaiting observation. Existing review triggers
   were not changed.

## Verification

Environment: Windows PowerShell, Python 3.14.3. Full raw command output is retained in the files
below; exact argument arrays and exit codes also stand in `foundation-checks.json`.
The helper `check_foundation.py` invokes these commands and performs the additional current-tree
decision-reference comparison; it is working verification material, not a product check.

| Command | Exit | Raw output | Result |
|---|---|---|---|
| `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none` | 0 | foundation-decisions.txt | 0 errors, 11 warnings, 5 unchecked. |
| `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none` | 0 | foundation-invariants.txt | 0 errors, 0 warnings, 3 unchecked. |
| `python -B elements/part-map/format_guard.py foundations/part_map.md --base none` | 0 | foundation-part-map.txt | 0 errors, 0 warnings, 7 unchecked. |
| `python -B gate/run_tests.py task-cycle` | 0 | foundation-task-cycle-tests.txt | 41 tests passed. |
| `python -B gate/run_tests.py elements/decisions` | 0 | foundation-decisions-tests.txt | 169 tests passed. |
| `python -B gate/run_tests.py gate` | 0 | foundation-critical-flow-tests.txt | 98 tests passed; existing critical flows included. |
| `python -B docs/task-cycles/lean-cycle-orchestrator/reports/check_foundation.py` | 0 | foundation-checks.json and foundation-current-fingerprints.json, plus raw logs above | All six invocations succeeded; 432 current decision references across foundations compared, 0 mismatches. |
| `git diff --check` | 0 | no output | No whitespace error. |

Current binding fingerprints: WAY-125 `7362c7ab`, WAY-148 `4c7fab3a`; full new-entry values
are in `foundation-current-fingerprints.json`. The explicit current-tree comparison supplements
the no-main guard but is not a simulated merge or proof of semantic validity of every reference.

Warnings: five unchanged overdue review conditions, WAY-03/21/52/55/69, all check-by 2026-10-02;
six expected request-link placeholders, WAY-125/148/157/158/159/160. Replace these placeholders
with the request URL at the prescribed later point.

Unchecked due to the explicit no-main options: decisions guard 5, invariants guard 3, part-map
guard 3. The other four unchecked results are:

- `wording-reaches-dependants` has no coverage file to verify its parts.
- `skills-reach-the-way-sessions` has no coverage file to verify its parts.
- No product command reports promise levels at their declarations for checking change paths.
- No product command reports the dependency graph for dependency/violation comparison.

These are partial tests and format guards, not a pass of the unavailable full gate. No method of
unchanged environment facts was run; none of those entries or their probe files changed. There
is no new invariant check requiring a deliberate break. The final independent review, return
step, independent foundation assessment, current-target search and final required verification
are later cycle duties and have not been represented as completed here.

## Boundary and next step

Resume this author for implementation only after the orchestrator records this result and gives
the next-stage handoff. Read skill conventions before changing the cycle skill. Verify Claude
Code's actual waiting mechanism from installed source or official documentation, not memory;
the foundation does not fix a numeric limit. The live Codex tool permits a longer call than this
session's active 60-second responsiveness instruction, so the effective maximum remains 60 seconds.

No blocking question, scope expansion, invariant author request or unresolved meaning collision.
No backlog, original checkout, vault, other repository or external application was changed.
