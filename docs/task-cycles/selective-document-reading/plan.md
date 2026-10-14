# Plan — selective foundation and project-plan reading

- Task: `.runs/task-cycles/selective-document-reading/task.md`
- Spec: `.runs/task-cycles/selective-document-reading/spec.md`
- Base: `52b9d487efeafe37c46ad2b9f10d60c13a885e63`

## Foundation entries

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| Selective product-foundation reading default, preserving every touched-Scope decision, complete selected entries, required searches and whole-source duties | new decision; allocate its number when writing | Task settlement row 1; spec, Shared foundation-reading contract and Foundation changes item 1 | Slices 1 and 2 |
| Selective reading of large definitions and existing project plans, preserving complete coverage, whole-document checks and independent critique | new decision; allocate its number when writing | Task settlement row 2; spec, Selective definition and existing-plan reading and Foundation changes item 2 | Slice 2 |
| WAY-111/1: replace the whole-foundation obligation and its whole-reading rationale/examples; preserve conflict presentation to the human | decision edited in place | Task Context and Decisions in play; spec, Foundation changes item 3 | Slice 2 |
| WAY-115/1: replace only the whole-foundation obligation; preserve whole project-source reading, complete candidate table, human selection and recording | decision edited in place | Task Context and Decisions in play; spec, Foundation changes item 4 | Slices 1 and 2 |
| WAY-134/1: reread against changed WAY-115 and renew its actual incoming fingerprint without changing its binding meaning | decision relation renewal in place | WAY-31; spec, Foundation changes item 5 | Slices 1 and 2 |

The foundation step precedes both instruction slices; it is not an implementation slice. Write in
`foundations/decisions.md` through this worktree's `the-way-record-decision`, using the actual log
to allocate numbers and request-linked approval fields. Keep the accepted settlements whole. The
task expressly authorizes the WAY-111/115 meaning changes; provisional orchestration approval is
not human approval of the entries. Keep the other named decisions and invariant sentences intact
in meaning. No part-map responsibility or file assignment changes, new persisted index, selector,
manifest, parser interface or gate implementation is planned.

Before writing, search all five foundation elements for linked and unlinked effects, including
incoming dependents and meanings outside overlapping Scope; settle findings under WAY-31/33/37.
WAY-134 is the known direct dependent, not proof there are no others. Search again against the
current `foundations` integration tip before integration and retain both records. Assess possible
commit-level derivations under WAY-12/22 rather than automatically assigning existing invariants
to the new decisions. The designed reading behavior uses level-2 compliant/violating examples;
ordinary instruction changes need no string-matching test. A genuinely new unsettled foundation
choice returns to the orchestrator before dependent work.

Run `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none`,
`python -B gate/run_tests.py elements/decisions` and `python -B gate/run_tests.py gate` for the
foundation step. If its search actually changes invariants, also run
`python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none`
and their affected tests, with the required separate check author and deliberate-break duties.
Do not add an invariant or test merely to give this prose change a test. Keep warnings and
no-main comparison omissions explicit. The cycle still performs its one independent foundation
assessment and return step at their existing boundaries.

The Read ranges below are complete-entry locators at Base. After the foundation step changes the
log, the orchestrator refreshes touched parts, current Scope matches and the actual complete-entry
ranges before dispatch, includes the newly written entries, and reruns the size check if the Read
sets change. Do not use shifted line numbers as truncated entries or treat this plan's inventory
as limiting a receiving agent's required reading. Preserve current whole templates, rules and
examples wherever the invoked element skill requires them.

## Slices

### Slice 1 — share foundation selection across element workflows

- **Goal:** One shared reading contract governs all foundation-element readers and the candidate finder, with complete Scope coverage, expandable context and the existing writing/search/source duties preserved.
- **Change:** `elements/common/way_of_working.md` · `elements/decisions/skill/SKILL.md` · `elements/part-map/skill/SKILL.md` · `elements/invariants/skill/SKILL.md` · `elements/environment-facts/skill/SKILL.md` · `elements/glossary/skill/SKILL.md` · `elements/common/skill/SKILL.md`
- **Read:** `.runs/task-cycles/selective-document-reading/task.md` · `.runs/task-cycles/selective-document-reading/spec.md` · `agent-instructions/README.md` · `foundations/part_map.md` · `foundations/glossary.md` · `elements/common/rules.md` · `elements/decisions/template.md` · `elements/part-map/template.md` · `elements/invariants/template.md` · `elements/environment-facts/template.md` · `elements/glossary/template.md` · `elements/decisions/examples.md` · `elements/part-map/examples.md` · `elements/invariants/examples.md` · `elements/glossary/examples.md`
  `foundations/decisions.md:6-413` · `foundations/decisions.md:459-2986` · `foundations/decisions.md:3117-3145` · `foundations/decisions.md:3176-3328` · `foundations/decisions.md:3363-3556` · `foundations/decisions.md:3648-3753` · `foundations/decisions.md:3967-4014` · `foundations/decisions.md:4120-4209` · `foundations/decisions.md:4494-4533` · `foundations/decisions.md:4647-4720`
  `foundations/invariants.md:6-165` · `foundations/invariants.md:176-586` · `foundations/invariants.md:597-856` · `foundations/invariants.md:867-1106` · `foundations/invariants.md:1117-1156` · `foundations/invariants.md:1187-1206` · `foundations/invariants.md:1227-1236` · `foundations/invariants.md:1257-1266` · `foundations/invariants.md:1277-1336` · `foundations/invariants.md:1347-1406` · `foundations/invariants.md:1417-1516` · `foundations/invariants.md:1547-1696` · `foundations/invariants.md:1707-1726` · `foundations/invariants.md:1737-1766` · `foundations/invariants.md:1777-1998` · `foundations/invariants.md:2065-2084`
- **Checks:** Run `python -B gate/run_tests.py elements/decisions`, `python -B gate/run_tests.py elements/part-map`, `python -B gate/run_tests.py elements/invariants`, `python -B gate/run_tests.py elements/glossary`, `python -B gate/run_tests.py elements/environment-facts`, `python -B gate/run_tests.py elements/common` and `python -B gate/run_tests.py gate`; run `git diff --check`. The common directory has no tests at Base: retain its no-tests result as unchecked. Compare the final instructions with the spec's complete reader table and shared contract, then record concrete walkthroughs for a wrapped Scope and entry-collecting file, no-diff project/ambiguous ownership, an incoming dependent plus Part every, and a collision outside selected parts/links. Check retained whole templates/examples, the candidate finder's whole source and table, numbering/version discovery, fact-method duties and glossary-use review. This changes Markdown instructions, so no production-code failing-test step or new instruction-string test is appropriate. Walkthroughs are inspection evidence, not executed agent runs.
- **Depends on:** all Foundation entries above

### Slice 2 — apply selective reading to projects and task cycles

- **Goal:** Project and task workflows consume the shared foundation method, and plan-project starts or resumes from complete inventories and selected source units while retaining all whole-document and independent semantic checks.
- **Change:** `project-level/skill/SKILL.md` · `project-level/technology/SKILL.md` · `project-level/task/skill/SKILL.md` · `task-cycle/skill/SKILL.md` · `task-cycle/plan/SKILL.md` · `project-level/plan/skill/SKILL.md`
- **Read:** `.runs/task-cycles/selective-document-reading/task.md` · `.runs/task-cycles/selective-document-reading/spec.md` · `agent-instructions/README.md` · `elements/common/way_of_working.md` · `elements/common/critique/SKILL.md` · `foundations/part_map.md` · `foundations/glossary.md` · `project-level/definition_template.md` · `project-level/plan/template.md` · `project-level/task/template.md` · `task-cycle/record_template.md` · `project-level/plan_check.py` · `project-level/readiness_check.py` · `project-level/test_plan_check.py` · `project-level/test_readiness_check.py`
  `foundations/decisions.md:6-37` · `foundations/decisions.md:71-94` · `foundations/decisions.md:234-458` · `foundations/decisions.md:480-530` · `foundations/decisions.md:623-644` · `foundations/decisions.md:708-825` · `foundations/decisions.md:857-922` · `foundations/decisions.md:949-1008` · `foundations/decisions.md:1043-1126` · `foundations/decisions.md:1228-1378` · `foundations/decisions.md:1423-1458` · `foundations/decisions.md:1541-1571` · `foundations/decisions.md:1602-1644` · `foundations/decisions.md:1782-1849` · `foundations/decisions.md:1890-1990` · `foundations/decisions.md:2315-2343` · `foundations/decisions.md:2471-2499` · `foundations/decisions.md:2783-2883` · `foundations/decisions.md:2987-3753` · `foundations/decisions.md:3967-4303` · `foundations/decisions.md:4328-4720`
  `foundations/invariants.md:36-45` · `foundations/invariants.md:86-95` · `foundations/invariants.md:126-155` · `foundations/invariants.md:206-225` · `foundations/invariants.md:236-265` · `foundations/invariants.md:287-296` · `foundations/invariants.md:307-346` · `foundations/invariants.md:397-416` · `foundations/invariants.md:467-476` · `foundations/invariants.md:527-536` · `foundations/invariants.md:547-576` · `foundations/invariants.md:617-626` · `foundations/invariants.md:647-656` · `foundations/invariants.md:697-716` · `foundations/invariants.md:747-756` · `foundations/invariants.md:817-826` · `foundations/invariants.md:867-886` · `foundations/invariants.md:897-906` · `foundations/invariants.md:917-926` · `foundations/invariants.md:937-946` · `foundations/invariants.md:987-996` · `foundations/invariants.md:1067-1076` · `foundations/invariants.md:1277-1286` · `foundations/invariants.md:1317-1336` · `foundations/invariants.md:1357-1366` · `foundations/invariants.md:1547-1556` · `foundations/invariants.md:1657-1666` · `foundations/invariants.md:1677-1696` · `foundations/invariants.md:1807-1816` · `foundations/invariants.md:1929-1938` · `foundations/invariants.md:1999-2084`
- **Checks:** Run `python -B gate/run_tests.py project-level`, `python -B gate/run_tests.py task-cycle` and `python -B gate/run_tests.py gate`; run `git diff --check`. Audit all six reader clauses against the spec, preserving whole definition/source duties outside plan-project, readiness collision-search timing, frozen tasks, approvals and the independent assessor's filtered input boundary. Walk through a resumed large plan whose distant task dependency, projected-entry writer and question alter the resumed work; a new breakdown processing every scope item, projected entry and exact question in batches; and a structurally valid plan with a layer-only goal, unexplained question move or inadequate quoted answer, which still requires complete independent semantic judgment. Verify that existing readiness_check.py and plan_check.py invocations use original authoritative whole files and retain findings/fingerprint handling, that the critic reads the complete plan and all needed source units independently of the author's inventory, and that plan-task ranges contain complete entries. No parser/interface or test-body change is needed for these instructions; do not call an inspection walkthrough an executed run.
- **Depends on:** Slice 1 · all Foundation entries above

## Independence and execution

Two slices provide separate useful reviews: shared selection plus its element-specific duties,
then the project/task consumers and complete project-planning application. Their write sets are
disjoint, but Slice 2 consumes Slice 1's final shared section and its source-reading semantics;
that is a real dependency, not independence inferred from different filenames. The foundation
stage also changes the decisions both rely on. Finish and review Slice 1 before Slice 2; there
is no useful parallel implementation opportunity in this two-slice cut. A separate slice for
each short referral would add handoffs without an independently meaningful goal.

Independently of that recommendation, adopted Superpowers 6.4.1
`subagent-driven-development` prohibits parallel implementation subagents. The orchestrator
records its execution ruling before implementation, including shared worktree/test state and
separate review ranges, and keeps one final review for this multi-slice change.

## Coverage

| What the task requires | Slices or entries |
|---|---|
| To do 1: limit complete loading of large definitions and existing project plans to material needed for the work | Selective definition/plan decision; Slice 2 start/resume inventory, complete source units and expansion |
| To do 2: default selective product-foundation reading across every instruction requiring full loading | Selective foundation decision; Slice 1 shared contract and all seven element/common readers; Slice 2 all six project/task readers |
| Settlement row 1, whole accepted meaning | First Foundation entry; Slices 1 and 2 |
| Settlement row 2, whole accepted meaning | Second Foundation entry; Slice 2 |
| WAY-111/115 whole-reading obligations and affected WAY-134 fingerprint | Foundation entries 3–5, before Slices 1 and 2 |
| All 13 spec readers accounted for, with current paths | Seven Slice 1 Change paths and six Slice 2 Change paths |
| Acceptance: complete project scope, projected-entry and open-question coverage, existing scripts and independent assessment under WAY-146 | Slice 2 inventories, whole-original checks, complete independent semantic judgment and retained handover |
| Acceptance: every current decision whose Scope names a touched part | Shared contract in Slice 1; both slices' refreshed complete Scope selection and evidence; decisions-found-for-change sentence retained with Method TODO |
| Carried question: parts/relations and expansion without a diff | Slice 1 shared routing, complete map, proposed behavior/flows/surfaces and uncertain-owner expansion; Slice 2 callers |
| Carried question: reduce document loading while retaining task/question/answer meaning | Slice 2 global inventories, complete projected entries/rows/questions, original quoted sources, dependency/meaning expansion and whole-plan critic |
| Carried question: check Scope completeness while Method remains TODO | Slice 1 operational expected-versus-read comparison from complete current Scope inspection, revision and source locations; no automatic invariant-method/full-gate claim |
| WAY-33 search of unlinked entries across all foundation elements, at writing and before integration | Foundation step; Slice 1 shared search section; Slice 2 readiness/reconciliation duties |
| Linked/incoming effects, Part every, relevant methods/flows, glossary meanings and required examples | Slice 1 shared expansion and preserved element duties; both slices' actual reads |
| Existing authority, candidate selection, task/project ownership and mandatory whole sources outside the named change | Foundation entry boundaries and both slices' retention audits |
| Changed-part suites, critical flows, warnings and unchecked work | Each slice's Checks and final verification below |
| Out of scope: other implement-task organization changes | Slice 2 changes only reading/refresh clauses; preserves every stage and filtered assessment boundary |

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| Two reviewed instruction slices after the separate foundation stage | One 13-file slice; one slice per referral; extra slices solely to expose nominal parallelism | Each review reads several element-specific duties or six workflow consumers; split again only if an executor actually cannot hold its coherent goal |
| Slice 2 follows the reviewed shared contract | Concurrent drafting of its consumers against an unsettled section | Sequential handoffs cost elapsed time; concurrent wording could duplicate the contract or silently narrow it |
| Existing checks plus semantic instruction walkthroughs; no new literal-text tests | A selector/parser, persisted inventory or tests asserting a section name appears | Human/agent execution remains only partly checkable; future evidence may justify a separately designed tool, but these additions would not prove semantic completeness |
| Original definition/plan files stay authoritative; temporary inventories live in existing working evidence | Reduced copies as check input or a second maintained task/entry inventory | Batch selection can still miss needed context; complete inventories, expansion, whole checks and independent review address different parts of that risk |
| Base complete-entry ranges refreshed after foundation writing and any write-set expansion | Whole decision log in every slice; fixed line numbers reused after edits | Refresh costs a read-only selection/range update and possible size rerun; stale ranges could cut an entry or omit a new decision |

Final verification reruns every changed-part suite: `elements/decisions`, `elements/part-map`,
`elements/invariants`, `elements/glossary`, `elements/environment-facts`, `elements/common`,
`project-level` and `task-cycle`, each through `python -B gate/run_tests.py <directory>`, plus
`python -B gate/run_tests.py gate`, the actual changed foundation guards, `git diff --check`,
the complete reader audit and the recorded final-instruction walkthroughs. Skill names,
locations and descriptions stay unchanged; if execution changes one, refresh entry points with
the existing generator and refresh this plan's write sets and touched-part selection first.

Keep common's absent tests, all guard warnings/no-main omissions, the unimplemented full gate,
automatic actual-read completeness, `decisions-found-for-change/1` Method TODO and the lack of a
real large-project token-reduction measurement visible. The plan makes no savings percentage
claim. All listed implementation verification is future work at this plan boundary.
