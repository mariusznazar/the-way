# Foundation stage — lead-project

Status: ready for the orchestrator's stage ruling. This stage writes no implementation or invariant check and launches no subagent.

Base and initial search revision: db77ba549cb9ece7d3e62bf29e1256973f62deab. Worktree: C:/Storage/repos/the-way-wt/lead-project. Source: complete frozen task, spec and approved plan in this cycle; source authority is its ten accepted settlement rows. Grouping and wording are stage recommendations under the root's delegation, not human approval. Existing versions remain /1 under the no-main integration route. The four amended choices and five new decisions use the prescribed `Mariusz, merge of <request link>` marker; the actual URL is substituted at task-cycle step 12 before request review.

## Changes and source mapping

| Entry | Accepted source | Meaning for the PR in Polish |
|---|---|---|
| WAY-152/1 | Rows 1 and 9; To do 1–4, 6, 19 | Prowadzący plan koordynuje potwierdzoną rundę i aktualizuje stany, a uruchomienie cykli, domknięcie projektu i ponowna ocena źródeł na starcie cyklu mają osobne miejsca. |
| WAY-153/1 | Row 2; To do 5; spec State-reader contract | Postęp w planie wymaga dowodu ze śladów cyklu; nierozstrzygnięte stany PR i sprzeczności trafiają do narzędzia produktu albo człowieka. |
| WAY-154/1 | Row 3; To do 7–8, 11–13, 16 | Agenci wymieniają treść przez tymczasowy plik, opis zadania pisze doprecyzowujący, a skasowanie rozmowy następuje dopiero po przyjęciu opisu i zachowaniu odpowiedzi ze źródłami. |
| WAY-155/1 | Row 4; To do 9–10 | Odpowiadający rozstrzyga tylko źródłem; kod opisuje stan obecny, dokument może określać wymaganie, a człowiek widzi także odpowiedzi udzielone cytatem. |
| WAY-124/1 amendment | Row 5; To do 17 | Każde zadanie uzyskuje gotowość dopiero po pokazaniu i przyjęciu przez człowieka całego dokumentu. |
| WAY-144/1 amendment | Row 6; To do 18 | Zależności blokują start cyklu, a doprecyzowanie czeka tylko na wynik potrzebny do wskazanego pytania. |
| WAY-156/1 | Row 7; To do 14–15 | Zmiana definicji przechodzi pełną bramkę u subagenta i nową kontrolę planu, a do tego czasu zadania nie otrzymują gotowości. |
| WAY-134/1 amendment | Row 8; To do 10, 16 | W trybie prowadzonym kandydatów i wymagane pytania przekorne przedstawia prowadzący plan w paczce rundy. |
| project orchestrator | Row 10 | Nazwa oznacza agenta prowadzącego oddany plan w rozmowie z człowiekiem; istniejące użycia samego orchestrator zachowują znaczenie związane z cyklem zadania. |
| WAY-09/1 amendment | To do 1 and 5 | Część project-level zawiera również prowadzenie planu i odczyt dowodów postępu. |
| project-plan-state-evidence/1 | WAY-153; spec invariant assignment | Czytnik proponuje postęp wyłącznie ze wskazanych dowodów, podaje oba przejścia dla zaległego stanu ready i nie zmienia dokumentów. |
| project-level map amendment | To do 1 and 5; spec Foundation changes | Odpowiedzialność obejmuje prowadzenie planu; błędny postęp ma wysoką wagę, a nowy czytnik przyjmuje niezaufane dane. |
| project-plan-state-command | Spec public CLI contract; WAY-49 | Polecenie odczytu zachowuje nazwę, argumenty, dowody, jawne niewiadome, kody wyjścia i brak zmian dokumentów. |
| WAY-135/1; six WAY-09 invariants; project-plan-form/1 | WAY-31 incoming links | Zależne wpisy zachowują znaczenie i otrzymują odciski ponownie ocenionych decyzji. |

No environment-fact entry is needed: the new rule defines evidence the product's reader accepts rather than asserting an outside fact about Git or a private product. Its controlled-repository method checks the reader, not whether a real product is done. Rests on therefore reads none. The map retains its existing external-context rows and pinned change path.

## Reading and initial whole-foundation search

Read the complete current part map, four source element skills, common rules and way_of_working, four templates and their example lists and complete named example entries. Selected behavioral parts are project-level, task-cycle, agent-instructions and installation. Initial current Scope inventory has 83 matches, the same identifiers as design/spec review; none has a missing Scope or a version/repeal ambiguity. The selection was read as whole entries, including rationale and rejected options. Additional whole decisions read for explicit rules and links: WAY-07, 08, 12, 17, 31, 35, 49, 56, 60, 61, 73 and 95–99. Relevant invariant Part entries include all 56 naming a touched part or every, plus the six WAY-09 dependants and named examples; the complete glossary and environment-fact file were read. No found relevant entry remained merely a search hit.

Initial complete-Scope matches and source heading locations at the base (foundations/decisions.md):

WAY-01/1:6, WAY-03/1:71, WAY-09/1:234, WAY-10/1:305, WAY-11/1:343, WAY-13/1:414, WAY-16/1:480, WAY-21/1:623, WAY-25/1:708, WAY-26/1:737, WAY-27/1:763, WAY-28/1:794, WAY-30/1:857, WAY-33/1:949, WAY-34/1:980, WAY-36/1:1043, WAY-37/1:1070, WAY-38/1:1097, WAY-44/1:1228, WAY-45/1:1259, WAY-46/1:1285, WAY-47/1:1326, WAY-48/1:1353, WAY-51/1:1423, WAY-55/1:1541, WAY-57/1:1602, WAY-62/1:1782, WAY-63/1:1813, WAY-65/1:1890, WAY-68/1:1921, WAY-69/1:1955, WAY-82/1:2315, WAY-89/1:2471, WAY-100/1:2783, WAY-101/1:2809, WAY-102/1:2832, WAY-103/1:2859, WAY-106/1:2987, WAY-107/1:3013, WAY-108/1:3039, WAY-109/1:3070, WAY-110/1:3093, WAY-111/1:3117, WAY-112/1:3146, WAY-113/1:3176, WAY-114/1:3212, WAY-115/1:3241, WAY-116/1:3272, WAY-117/1:3300, WAY-118/1:3329, WAY-119/1:3363, WAY-120/1:3390, WAY-121/1:3422, WAY-122/1:3459, WAY-123/1:3518, WAY-124/1:3557, WAY-125/1:3603, WAY-126/1:3648, WAY-127/1:3695, WAY-128/1:3754, WAY-129/1:3796, WAY-130/1:3822, WAY-131/1:3862, WAY-132/1:3894, WAY-133/1:3932, WAY-134/1:3967, WAY-135/1:4015, WAY-136/1:4063, WAY-137/1:4120, WAY-138/1:4160, WAY-139/1:4210, WAY-140/1:4249, WAY-141/1:4304, WAY-142/1:4328, WAY-143/1:4380, WAY-144/1:4418, WAY-145/1:4448, WAY-146/1:4494, WAY-147/1:4534, WAY-148/1:4565, WAY-149/1:4605, WAY-150/1:4647, WAY-151/1:4685.

Refreshed inventory after writing: 88 matches = the same 83 plus WAY-152–156. WAY-144 also names task-cycle now because its accepted rule governs cycle starts; this changes routing coverage rather than the settlement. Every selected existing match was read, and all five new entries were read again as complete current entries.

Exact initial whole-foundation search (expanded during drafting, before the foundation commit):

```text
rg -n -i 'lead|orchestrat|refin|ready for|in cycle|done|depend|plan.state|plan check|questions|gate|wait|project-level|WAY-(09|124|134|144)@' foundations/decisions.md foundations/invariants.md foundations/glossary.md foundations/environment_facts.md foundations/part_map.md
rg -n 'WAY-(09|124|134|144)@' foundations
rg -n -U -i -w 'project\s+orchestrators?|orchestrators?|plan\s+lead(er|ing)?' foundations elements/common -g '*.md'
rg -n -U -i -w 'project\s+orchestrators?|orchestrators?|plan\s+lead(er|ing)?' elements -g template.md
rg -n -i 'state|progress|refin|depend|lead|orchestrat|wait|cycle|plan' foundations/environment_facts.md
```

Raw initial matches: reports/foundation-search-initial.txt and reports/foundation-term-uses-initial.txt. Search domain is all five elements, not only selected scopes. Heading/field inspection supplies whole-entry context beyond matches. Positive controls include WAY-124's readiness rule, WAY-142's task states and plan log, and WAY-125's task-cycle orchestrator. Environment-fact hits concern model evaluation or Python lifecycle, not project-state authority; no Git state fact waits for this change. Template term search returned no occurrences, while the foundation/common search returned the existing task-cycle uses, so the zero is not treated as an unchecked search instrument.

| Finding | Whole-entry assessment and result |
|---|---|
| WAY-09 incoming links | Exactly repository-file-location, element-directory-contents, relation-model-directory-contents, invariant-example-target, map-example-target and glossary-example-target. The inventory addition changes none of their sentences: directory locations, required element contents, fingerprint code and example targets still hold. Renew only their WAY-09 links. |
| WAY-134 incoming links | WAY-124 and WAY-135. Candidate acceptance stays required for readiness; who presents the table changes only in orchestrated mode, and WAY-124 gains its separately accepted full-document requirement. WAY-135 still treats an invariant sentence already settled in the task as leaving no open design choice; presentation routing changes none of that. Renew both links; preserve WAY-135's entire binding part. |
| WAY-144 incoming link | project-plan-form: its table grammar and allowed states remain unchanged; absence of an extra parallel-work field still follows from WAY-144. Renew only the link, keeping version and sentence. |
| WAY-124 incoming links before writing | No fingerprinted incoming dependent. New WAY-152 and WAY-154 carry the amended fingerprint. |
| WAY-106 project-level foundation boundary | Leading writes no foundation entries; new WAY-152 derives from the existing boundary. No revision to WAY-106. |
| WAY-113/120/134/140 human choice, critique and actions | Existing collective critique and human-action placement still apply. New WAY-155 and amended WAY-134 route human material without granting agents human authority; new WAY-156 preserves full independent critique at the gate. No new exception. |
| WAY-118/145/146 definition and plan boundary | Gate approval and plan recheck survive; question moves without a definition change remain plan work. WAY-156 links to 118, 120 and 145 rather than inventing a lighter gate. |
| WAY-125/136/148 orchestrator | Every existing bare use refers to task-cycle coordination, including part-map failure modes; none moves meaning. New leading uses the qualified project orchestrator term. No old definition exists to change and no use-review dispatch is needed. |
| WAY-142/147 states and stable name | Ordinary state writes retain the plan log and stable task identity; new conversation/result states do not become task-document statuses. New 153/154 link to these rules. |
| WAY-38/89 and script invariants | Python and product-declared command bounds remain. New reader's stronger Git-only policy is explicit in WAY-153 and its level-2 assessment; no PR-host command is authorized in that reader. |
| Map and identifiers | No existing state-reader surface or identifier duplicates the new invariant or surface. project-level/** already owns planned files; installation and generated wrappers keep their existing owners. No part dependency is added. |

These are the first WAY-33 search and its assessed results. The second search against the then-current integration tip and the independent WAY-10 assessment have NOT occurred; the root carries them with the final foundation return commit before PR. This report is not either of those later records.

## Glossary uses

The new definition uses agent as ordinary genus and the leading project plan as its distinguishing subject. It contains no dispatch, approval, storage or execution rule. All existing orchestrator uses were inspected in WAY-125, WAY-136, WAY-148 and the task-cycle part; they keep the task-cycle meaning. No synonyms were found that justify Avoid, and no other meaning of the full qualified term was found that needs Not. Both fields read none on that inspection, not from an empty source. Template/common inspection found no competing definition. The new term does not read like an invariant, map or environment-fact identifier. Existing glossary definitions remain byte-identical.

The uses command was first called incorrectly with --base/--merge-onto (exit 1: --uses forbids these options); corrected `python -B elements/glossary/format_guard.py foundations/glossary.md --uses "project orchestrator"` returned exit 0, 20 occurrences before final formatting. Each was inspected; one wrapped line contains two distinct occurrences, rather than duplicate semantic objects. The compliant example was corrected to say the project orchestrator coordinates refinement, making ownership explicit.

## Drafting choices and costs

The five questions A–E remain the provisional grouping in the approved slice plan; the source settlement meanings are unchanged. Splitting by every procedural clause would duplicate the ownership and resumption contract, while one all-purpose leading entry would couple independent future changes. New decision rationale/rejected options express the tradeoffs already settled in the task and spec, with no invented external facts or private Origin. Each new Review when is none: these are chosen workflow boundaries and authority rules, not predictions awaiting a state of the world or measured pilot outcome. Operational costs remain in the rationale (host lookup, human inspection of quotations, serialized ownership and a full gate) rather than invented review dates or arbitrary trial counts.

Semantic agent conduct is level 2 with concrete complies/violates pairs. The state-reader's evidence behavior is level 1 through the new invariant; its stronger Git-only execution policy and human application/host resolution stay explicitly within level 2, with the existing script invariants still applicable. No string match over skill prose is claimed to establish agent compliance. The new invariant's one sentence constrains the reader's evidence-bearing proposal as a whole, including composed transitions and nonmutating conservative output; its method uses controlled repositories because its subject is the reader. Its Part is project-level: that part owns both its reading code and parser; changes to workflow prose elsewhere do not alter the executable reader. No source private-product state becomes an invariant.

The executable method uses the project-level directory, not a test filename: gate/run_tests.py accepts DIRECTORY and rejects a file at its isdir check. The independent check still belongs in the assigned project-level/test_plan_state_invariant.py. Initial draft mistakenly supplied the file as Method; root inspection caught it before commit and it is corrected without changing the sentence or runner interface. Root also confirmed task-cycle Scope for WAY-144, the heading separator and line wrapping; those corrections are present.

## Checks, warnings and work not yet checked

Four guards were run with the prescribed no-main flags; their full outputs and exit statuses stand in reports/foundation-guard-{decisions,invariants,glossary,part-map}.txt. They were rerun after formatting and Method/Scope corrections before this commit.

- Decision guard: exit 0, 0 errors, 14 warnings, 5 unchecked. Nine warnings are the prescribed request-link placeholders; five pre-existing overdue reviews are WAY-03, 21, 52, 55 and 69. They are not silently moved or claimed reviewed.
- Invariant guard: exit 0, 0 errors, 0 warnings, 3 unchecked; no human_verdicts.md exists, so no human verdict was given.
- Glossary guard: exit 0, 0 errors, 0 warnings, 5 unchecked; own glossary is not compared with itself as if this were a product.
- Map guard: exit 1, 2 errors, 0 warnings, 7 unchecked. The two transitional errors are the trust-boundary path and surface declaration for missing project-level/plan_state.py. No stub was written. They must disappear after Slice 1 creates and tracks the real reader; surface declaration still needs main and pinned policy there.
- Critical-flow suite `python -B gate/run_tests.py gate`: exit 0, 98 tests passed. No full gate exists or is claimed passed.
- Existing Method command `python -B gate/run_tests.py project-level --record .runs/project-plan-state-evidence.jsonl`: exit 0, 193 tests passed. Its record has no verdict for the newly added invariant because its independent check has not been written. That invariant remains unverified, not passed.
- `git diff --check`: final exit 0 after removing one excess trailing blank line; no product code/check was written.

The five decision-guard unchecked results all come from none options: --base (existing log lines/version growth; template versioning) and --merge-onto (TODO at merge; repeated version copies; relation fingerprints). Three invariant-guard unchecked results likewise concern --base (identifiers/versions/corrections/violations) and --merge-onto (TODO and fingerprints). Five glossary-guard unchecked results concern --base (Avoid growth; term/identifier collisions; changed-definition uses) and --merge-onto (TODO; term use after merge). Map has three none-option unchecked results (known-violation list; identifiers; criticality lowering), plus these four separate limitations: wording-reaches-dependants coverage absent; skills-reach-the-way-sessions coverage absent; no command reports promise levels/change paths; no command reports the dependency graph or new/stale violations. The none-option counts per run are therefore 5, 3, 5 and 3; every other unchecked line is listed individually here. Independent assessment, deliberate break, real acceptance and the later integration-tip search remain with the root and subsequent stages.

## Git-held source quotations

The report originally repeated complete changed foundation entries here. Those redundant source quotations are represented by the exact source commits 87d1dc460a4b1e6d1773ee0b46a7eaa2887dd0a5 and 7b070c1b5697c42d416903fbfbf62f09dc8a5c62, paths foundations/decisions.md, foundations/invariants.md, foundations/glossary.md and foundations/part_map.md. All stage findings, choices, checks and corrections are retained above and below; no Git-held file is duplicated in this archive.

## Fingerprints and pending boundary

- WAY-09: 60c8a936 → 909e9c5c.
- WAY-124: 9eaf23e6 → 4fbad55c.
- WAY-134: b858b34f → 2fc974a9.
- WAY-144: 6cdf8d49 → d5802c22.

Pending input: no unresolved source choice or blocker. The actual request URL, implementation-dependent map declarations and independent checks/review are deliberately later work. Stop at the foundation boundary; the check author receives reports/invariant-check-contract.md independently from this report and implementation rationale. Commit identity is returned separately and can be added by the orchestrator to its cycle record.

## Root inspection correction after 87d1dc4

Range: foundations/decisions.md:240–241 and 250–251 only. Automatic text wrapping had split `the-way` into `the-` plus `way` and `handed-over` into `handed-` plus `over`. Restore both full words with a line break before the word. The full WAY-09 excerpt and fingerprint above now show the corrected current text; no other entry's wording changes. This is a correction of the intended wording, keeping version /1 on the no-main route, not a new settlement.

Recomputed WAY-09 fingerprint: `909e9c5c`. All six incoming links already carry `909e9c5c`, computed from the intended wording before the faulty reflow. Their whole-entry meaning assessment remains the one above. Explicit comparison of all six references against the recomputed corrected fingerprint returns `909e9c5c refs 6 all_match True`; no artificial invariant-file diff is needed. The old malformed actual binding paragraph would instead have disagreed with those references, a check hidden by the prescribed no-main guard's unchecked fingerprint comparison.

Correction checks: decision guard exit 0 (0 errors, unchanged 14 warnings and 5 none-option unchecked); invariant guard exit 0 (0 errors, 0 warnings and unchanged 3 none-option unchecked); `python -B gate/run_tests.py gate` exit 0, 98 tests passed; `git diff --check` exit 0. `rg -n '\w-$' foundations/decisions.md` returns exit 1 with no matches, confirming no remaining line-terminal word hyphens in the log. Existing meaningful hyphenated names serve as a positive control in the corrected excerpt. No map or surface declaration changed, so its previously recorded two transitional missing-reader errors remain pending Slice 1. No independent assessment or integration-tip search is claimed by this correction. Commit scope is only foundations/decisions.md, followed by a separate commit without amend.
