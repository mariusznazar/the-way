# Design report — selective document reading

Stage status: spec ready for independent review; architectural design boundary reached.

## Inputs and authority

- Worktree: `C:/Storage/repos/the-way-wt/selective-document-reading`.
- Base/current HEAD: `52b9d487efeafe37c46ad2b9f10d60c13a885e63`.
- Frozen task: `.runs/task-cycles/selective-document-reading/task.md`, read whole;
  SHA-256 `dff4652dc2aa1b9a2b6dae1293f4cc5a8a3013983200da4c48e02ea1f2b852d6`.
- Handoff: `.runs/task-cycles/selective-document-reading/reports/design-handoff.md`.
- Product integration route: `agent-instructions/README.md`, especially start/check/integrate rules.
- Adapter: `task-cycle/skill/SKILL.md`, whole; design boundary at step 6 and review at step 7.
- Borrowed method: installed Superpowers 6.4.1 `skills/brainstorming/SKILL.md`, read whole. The
  adapter replaces its human stage approvals, output location, commit and planning transition.
- Actor: design subagent; model inherited from the orchestrator. Exact runtime model identifier,
  token cost and stage wall-time are not exposed to this agent.

The frozen task is independent and ready for cycle, with no human actions. Its two accepted
settlements are authoritative. The task explicitly authorizes revising the meaning of WAY-111
and WAY-115; no repeated human permission was requested. Intermediate workflow choices return to
the orchestrator, whose provisional rulings are not recorded as human approval.

## Classification and design choices

Architectural: the shared reading contract changes inputs used by foundation, project and task
workflows. The adapter requires the written-spec path for this design stage. Purpose and success
were already supplied, so no duplicate intent question was needed. No visual question arose.

The orchestrator accepted the following provisional direction before the spec was written:

| Choice | Evidence / reason | Rejected way and its cost |
|---|---|---|
| One section in the existing common way-of-working file | WAY-35 keeps shared work once; existing project skills already read sections of this file. | A separate helper or duplicate rules add another location or drift across readers. |
| Whole map as routing input, selective remaining foundation | WAY-21/WAY-44 need correct touched parts, while flows, surfaces and boundaries may reveal additional affected work. | Selecting map rows only from an initial keyword can miss the owner or a boundary; loading every foundation file preserves the task's cost. |
| Exhaustive current Scope inspection, whole selected entries | Acceptance criterion and `decisions-found-for-change/1`; Scope values can wrap and logs can have several versions. | Reading only explicit task links misses unlinked applicable decisions; excerpts discard Rejected and conditions. |
| Operational Scope-set comparison with visible method debt | Existing `latest_scopes(text)` at `elements/part-map/format_guard.py:1121` handles current versions and continuation lines. | A new selector/index interface costs parsing, testing and maintenance without proving semantic completeness or actual understanding. |
| Complete inventories and context expansion for plan-project | WAY-142/145/146 and existing plan-check implementation need the whole universe of scope, entries, tasks and questions. | An author-selected handful of plan rows can miss distant dependencies and assignments. |
| Whole plan and unrestricted authoritative sources for one critic | WAY-120 requires the full proposal; WAY-146 separates structural checks from semantic judgment. | Critique of only changed/selected rows does not judge the complete plan. |

The direction was approved provisionally in root's message: the common section and no new selector
were accepted; the whole map was justified as routing input; source paths must stay available to
the critic; batching must not omit semantic input; Method TODO must not be called implemented.
Root subsequently confirmed the existing Scope parser and the WAY-134 fingerprint dependency.

## Sources read and coverage

Read the whole part map, common way of working and common rules, project-planning skill and
template, define-project, settle-technology, refine-task, plan-task and implement-task skills,
the part-map skill and the glossary. Inspected the foundation reader clauses across all element
skills and the entry-finder, and read the entry-finder skill whole. Read existing plan/readiness
checker interfaces and the plan check's full-file input and coverage paths; read
`latest_scopes(text)` and its scope-name check.

Inspected every decision Scope against `elements-common`, `project-level`, `task-cycle`,
`part-map` and `decisions`; read all 117 matching complete entries, including rationale and
Rejected. All entries at this base have version 1. The applicable set was:

`WAY-01, 02, 03, 04, 05, 07, 09, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22,
24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44,
45, 46, 47, 48, 49, 51, 52, 53, 54, 55, 57, 60, 61, 62, 63, 64, 65, 68, 69, 71,
72, 73, 74, 79, 82, 83, 84, 85, 86, 89, 90, 93, 95, 97, 98, 99, 100, 101, 102,
103, 104, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119,
120, 121, 122, 123, 124, 125, 126, 127, 134, 135, 136, 137, 138, 139, 140, 142,
143, 144, 145, 146, 147, 148, 149`, all `/1`.

Read complete relevant invariant entries `decision-scope-names`, `decisions-found-for-change`,
`foundation-search-record`, `skill-rule-source`, `project-definition-form`,
`project-readiness-gate`, `project-technology-record`, `project-plan-form` and `project-plan-check`.
This stage does not modify any invariant or trust-boundary code.

The source anchors governing the design include:

- `foundations/decisions.md:623` — WAY-21 scope completeness; `:949` — WAY-33 unlinked search;
  `:1228` — WAY-44 entry-collecting files; `:1009` — WAY-35 shared work.
- `foundations/decisions.md:3117` — WAY-111 whole-foundation obligation;
  `:3237` — WAY-115 same obligation and unchanged candidate duties;
  `:3962` — WAY-134 task settlements and its WAY-115 fingerprint relation.
- `foundations/decisions.md:4489` — WAY-146 complete script checks and independent semantic
  critique; `:4560` — WAY-148 whole-source duties and filtered assessor input.
- `foundations/invariants.md:407` — `decisions-found-for-change/1`, Method TODO;
  `:527` — foundation-search record; `:2031` and `:2048` — current plan-check obligations.
- `project-level/plan/skill/SKILL.md:27` and `:37` — current whole-plan/definition reads;
  `:91` — critique; `project-level/plan_check.py:449` onward — complete coverage checks;
  `:634` onward — the CLI reads whole original input files.
- `elements/common/way_of_working.md:39` — full product files/glossaries;
  `:63` — separate whole-foundation search and full found entries.

## Foundation search and dependent effects

At the base revision, searched all files of `foundations/` for whole-foundation obligations,
whole-read instructions, WAY-111, WAY-115, `decisions-found-for-change` and WAY-146; inspected the
117 applicable entries and the relevant invariants. Searched all process Markdown for foundation
read clauses and whole definition/plan reads, then checked the resulting source clauses directly.
The reader coverage table in the spec names all 13 affected instruction locations.

Findings: WAY-111 and WAY-115 need the task-authorized meaning changes. WAY-134 carries
`derives from WAY-115@292bd21b` and needs rereading and fingerprint renewal without a meaning
change. No other direct WAY-111/115 fingerprint dependent was found. WAY-33 and WAY-118 still
require searching the whole foundation; selection cannot narrow their domain. WAY-40's rationale
mentions a whole map reading, which the design preserves. WAY-148 preserves other mandatory
whole-source reads; no change to its meaning is needed. There is no new part, surface, generated
entry point, dependency, environment fact or glossary meaning required by this design.

This is exploratory evidence for the design, not the foundation author's required first search
or the integration search. Those run under their own stage boundaries against current inputs.

## Check commands, results and limits

- `git rev-parse HEAD` — exit 0; base confirmed.
- `git status --short` — exit 0; no tracked/untracked visible changes (cycle record is ignored).
- `python -B elements/decisions/format_guard.py --help` — exit 0; planned no-main options exist.
- `python -B elements/invariants/format_guard.py --help` — exit 0; conditional guard command exists.
- Source searches/read commands — successful after correcting Windows wildcard arguments. One
  broad discovery output was truncated; the narrower complete search above replaced it. Two
  truncated decision outputs were reread at complete-entry scope (WAY-79 and WAY-122).

Root supplied baseline evidence: gate 98 tests pass, project-level 193 pass, task-cycle 41 pass,
elements/decisions 169 pass. The common-part runner exits 1 with 0 tests / NO TESTS RAN, recorded
as unchecked. This designer did not rerun those suites: no tracked behavior changed at this stage.
The spec names feasible later verification and workflow walkthroughs. None of those walkthroughs
has been executed on the future instructions yet. No full gate, automatic actual-read completeness
or measured token reduction is claimed.

## Result and self-review

Artifact: `.runs/task-cycles/selective-document-reading/spec.md`.

Self-review checked task coverage, accepted row meanings, WAY-111/115 authorized revisions,
WAY-134 propagation, full selected entries, glossary/examples, no-diff work, incoming/unlinked
discovery, source paths, exact question/entry inventories, complete WAY-146 verification, mandatory
whole-source reads, no new tool infrastructure and explicit unchecked debt. Existing Method TODO
is identified as debt, not an incomplete design field. No unresolved design question remains.

Changes made: the ignored spec and this ignored report only. No tracked files, code, foundation
entries, implementation plan or commits were written. A temporary source-reading bundle was
removed immediately; no copy of a git-held source remains in the record.

Next boundary: an agent other than this designer reviews the spec against the frozen task and
current foundation; root resolves findings, then dispatches `plan-task`. Planning must include all
13 instruction readers and the two new decisions, WAY-111/115 revisions and WAY-134 fingerprint
renewal. No further human permission is needed for the already authorized WAY-111/115 revisions.
