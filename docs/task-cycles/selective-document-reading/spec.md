# Spec — selective foundation and project-plan reading

Status: independently reviewed; verification correction applied; provisionally accepted by the orchestrator

- Task: `.runs/task-cycles/selective-document-reading/task.md`
- Worktree: `C:/Storage/repos/the-way-wt/selective-document-reading`
- Base and source revision: `52b9d487efeafe37c46ad2b9f10d60c13a885e63`
- Method: Superpowers 6.4.1 `brainstorming`, architectural path, adapted by `task-cycle/skill/SKILL.md:172`.

## Purpose and boundaries

The task makes selective foundation reading the default throughout the-way and limits the material
`plan-project` loads from large definitions and existing plans. Selection must still find every
current decision whose Scope names a touched part. Project planning must still cover the whole
approved scope, every projected entry and every open question, run its existing script checks and
receive one independent critique under WAY-146.

The two accepted task settlements keep their meaning. The task expressly authorizes replacing the
whole-foundation obligations in WAY-111 and WAY-115. It does not authorize changing candidate
selection, task/project ownership, approval points, project-plan form, whole-source duties outside
the named document-reading change, or the independent assessor's filtered inputs.

This is a change to shared process interfaces, so the architectural path is appropriate. It needs
no new selector command, generated index, manifest, storage format or gate implementation.

## Chosen approach and costs

Add one shared `Reading the foundation` section to `elements/common/way_of_working.md` and make the
foundation-reading instructions use it. Put the additional definition/plan-reading method in
`project-level/plan/skill/SKILL.md`, where its readers and work already live.

| Approach | Result and cost |
|---|---|
| Shared instruction section — selected | One contract to maintain; existing skills name it and keep only their particular needs. Agents still have to establish relevance and retain evidence of completeness. |
| Local rules in every reader | Slightly easier first edits, but decisions, terms, incoming relations and no-diff work acquire different selection rules as the copies change. |
| Selector command or persistent index | A script can calculate Scope matches, but cannot decide unlinked semantic collisions or source meaning. It adds a public interface, parsing and test obligations without removing those judgments. |
| Leave the instructions unchanged | No implementation cost, but every invocation continues to load growing documents and the two accepted settlements remain unmet. |

The orchestrator provisionally accepted the selected direction under the user's delegation. This
is not human approval of a foundation entry or permission to skip independent spec review.

## Shared foundation-reading contract

The shared section owns the following method. Readers refer to it rather than copying it.

1. **Establish the work and version.** Use the task, source, proposed entry or project scope and the
   current foundation of the repository being worked on. Read the complete part map as the routing
   input: responsibilities, file assignments, dependencies, critical flows, surfaces, boundaries
   and the common rules/scales those entries use. This is one justified whole-file input, not a
   demand to read every foundation file whole.
2. **Name touched parts.** For a file change, use the map's assignment rules; for a file collecting
   entries about several parts, use the entries the work changes under WAY-44. Before a diff exists,
   map the proposed behavior, responsibilities, integrations, flows and surfaces to existing parts.
   Include any part whose responsibility or promise the work changes. A prospective new part is
   recorded as such; it is not fabricated as a current map entry. Uncertain ownership expands the
   candidate parts and reading, rather than treating an empty file diff as no affected parts.
3. **Find every applicable current decision.** Inspect the complete current decision log's Scope
   fields, including wrapped values, using the latest version of each decision and respecting
   repeals. Select every decision whose Scope names any touched part, together with decisions the
   task, project, proposed entry or source explicitly names. Read each selected entry whole,
   including fields, rationale and Rejected. A keyword hit or extracted binding sentence locates
   an entry; it does not replace reading the entry.
4. **Expand from those entries and the work.** Read whole linked entries needed to understand or
   apply the selected rules and their verification: governing Relations, Based on facts,
   Verification invariants, invariants' Derives from and Rests on, and relevant map entries.
   Inspect invariant Part fields across the current file, including `every`, and select the
   invariants the work reaches under WAY-62; include methods naming a changed file and invariants
   of relevant critical flows. Search for incoming dependents when changing an entry or deciding
   its impact, since links are written at the dependent end. Follow these as far as their meaning
   or validity affects this work; unrelated branches of a relation graph need not all be loaded.
5. **Read vocabulary and required examples.** Inspect the product glossary and the pinned process
   glossary's terms and Avoid spellings; read complete entries for the terms used in the work and
   selected material, and meanings a draft may introduce or confuse. Preserve the element skill's
   mandatory whole templates, rules and examples, including complete entries named as examples.
   Selecting the product foundation does not make those required reads optional.
6. **Search beyond known links and parts.** A relevant topic, candidate duplicate, unclear meaning,
   changed dependency, unknown owner or search finding expands the selection. Search all five
   foundation elements for the behavior, rule, concepts and consequences the work concerns,
   including alternative vocabulary, not only identifiers or matching Scope. Where WAY-33,
   WAY-37 or the readiness gate requires a whole-foundation search, preserve that search's entire
   domain and timings; read each finding whole and settle it as its existing rule requires.
7. **Check the selection and refresh it.** Keep the foundation revision, touched parts and selected
   decision identifiers with source locations in the workflow's existing working record or
   handoff. Compare the selected identifiers against the expected matches from a complete current
   Scope inspection; resolve every missing match before relying on the selection. Distinguish
   entries loaded from entries merely discovered. Recheck after the work's scope or current
   foundation changes. Uncertain relevance calls for additional reading, up to a whole file where
   that is the smallest reliable way to resolve it.

Selection is not a token cap or a prohibition on reading small files whole. It changes the default
from unconditional whole-foundation loading to justified reading units. A handoff may name those
units, but each receiving stage still checks its inputs and reads whole entries it relies on.

### What the completeness evidence proves

`elements/part-map/format_guard.py:1121` already provides `latest_scopes(text)` for current versions
and wrapped Scope values. Existing scripts, a local read-only invocation of that parser, or an
exhaustive direct inspection can produce the expected decision set without a new supported tool.
Malformed or missing Scope data is a finding, not permission to silently omit the decision.

The operational comparison records the revision, touched parts, expected current Scope matches,
selected/read identifiers and resolved differences. It establishes the declared set and evidence
of reading; it does not prove the agent understood every entry or found every semantic collision.
`decisions-found-for-change/1` retains its current sentence and `Method: TODO`. Scope-name validation
and fingerprint guards remain partial checks; none is called a pass of that unimplemented method
or of the full gate. The WAY-33 search record remains separate evidence.

## Applying the contract to current readers

| Reader | Required adjustment |
|---|---|
| `elements/common/way_of_working.md:39` | Replace unconditional whole product element-file/glossary loading with the shared selection method; retain full templates, rules, examples and full found entries. Its search step retains the whole-foundation domain and timings. |
| `elements/decisions/skill/SKILL.md:20` | Read selected current log entries and the existing entry's versions needed for the operation; retain number/version discovery and log-empty behavior. |
| `elements/part-map/skill/SKILL.md:20` | Use the shared contract, retaining the whole map as routing input and the skill's identifier/dependency searches. |
| `elements/invariants/skill/SKILL.md:20` | Select invariant, map and decision entries through the shared contract; retain all current invariant-writing and check-author duties. |
| `elements/environment-facts/skill/SKILL.md:20` | Select facts and their actual decision/invariant dependents through the shared contract; preserve fact-method and verdict duties. |
| `elements/glossary/skill/SKILL.md:20` | Use shared selection for foundation context; preserve whole-foundation use/meaning searches and the glossary-change review. |
| `elements/common/skill/SKILL.md:39` | Select current foundation context and search for duplicates/collisions; keep the source read whole and the complete candidate table. |
| `project-level/skill/SKILL.md:54` | Select from the idea's affected responsibilities/flows before a diff exists; retain showing decision, invariant and boundary conflicts, and the readiness whole-foundation search. |
| `project-level/technology/SKILL.md:27` | Replace the whole current decision-log read with shared selection, including every current decision holding or constraining a listed choice; retain the whole definition read. |
| `project-level/task/skill/SKILL.md:16` | Replace generic foundation loading with shared selection; preserve its project-relation and source-reading rules. |
| `task-cycle/skill/SKILL.md:34` | Use shared selection and refresh it at the existing foundation/reconciliation steps; preserve frozen task reads, stage boundaries and the filtered assessment package. |
| `task-cycle/plan/SKILL.md:24` | Use the same selection method; any plan Read range identifying a foundation entry must contain that complete entry rather than a truncated paragraph. |
| `project-level/plan/skill/SKILL.md:35` | Use shared foundation selection, not only the decisions the definition already lists; add the document-reading method below. |

Only foundation-reading clauses and `plan-project`'s definition/plan-reading clauses change. Skill
names, locations and descriptions need no change. No part map entry or responsibility changes:
the existing shared-work and project-planning parts already own these files and actions.

## Selective definition and existing-plan reading in plan-project

### Start and resume

Keep the definition and existing plan as the authoritative files at their original paths. Run
`readiness_check.py <definition>` and, for an existing plan, `plan_check.py <plan>` on those whole
files, with the existing handling of findings and fingerprints. Never check a reduced copy.

First inspect the complete heading structure, status/header, gate record and document versions.
From the definition, inventory all top-level In scope items in their original order and numbering,
all projected-entry headings, and every open question with its exact wording and assigned place.
From an existing plan, inventory every task number/name/state and dependency, every projected-entry
realizing/writing assignment, every question and its placement or answer, and phases/change-log
locations. Read table rows and question items as complete units; wrapped text belongs to its unit.
The inventory may be accumulated in batches using ordinary file/search tools. It is temporary
working evidence, not a second plan, generated document or new persisted product format.

Use the status and unfinished sections to choose the work to resume. For that work, load complete
scope items, task rows, assigned projected entries and open questions, their dependency and
assignment context, and relevant Goal, Background, Out of scope, Inputs and constraints,
Deliverables, Success, Risks, Touched parts and decisions, and Technology content. A projected
entry is read whole before assigning what makes it true or what writes it. An answer quoted from
the definition or foundation is read at its original source with the context needed to judge its
meaning. Expand whenever a choice, boundary, dependency, source reference or ambiguity may change
the cut or the interpretation of a question. A summary cannot settle an unseen source's meaning.

For a new complete breakdown, all In scope items, projected entries and questions are processed;
selection is a way of bringing their context in when it is needed, not a way of planning only a
subset. For a resumed change, read affected rows and every other row/assignment/question their
dependency or meaning reaches before editing. Whole-plan checks still run after the change.

### Complete verification and critique

Preserve every WAY-146 script obligation: plan form, all projected entries with realizing tasks
and exactly one writer, all In scope items, dependency cycles, preparatory dependencies and all
exact open-question placements/answers. `plan_check.py` already reads the whole original plan and
the definition it names; its implementation and interface remain unchanged.

Give the one independent critic the exact authoritative plan, definition, map, relevant foundation
and existing rules. The critic reads the whole plan, in manageable batches if useful, and accesses
every source unit needed for every task, technical element, question move and quoted answer.
Neither the author's selection nor its inventory limits what the critic may inspect. Complete
the whole proposal's semantic judgment before reporting critique complete; batching cannot omit
any semantic input. Retain the existing handling of critic findings, second script run and human
handover. The plan remains one document with no duplicate task descriptions.

## Foundation changes required before dependent instruction changes

The foundation step writes, in English and under the element skills:

1. A new decision carrying task settlement 1 whole: the-way skills default to selective product
   foundation reading, choose through the part map and existing links, and expand to the work's
   needs. Its binding meaning includes the complete touched-Scope decision requirement, whole
   selected entries and preservation of required searches and whole-source reads.
2. A new decision carrying task settlement 2 whole: `plan-project` limits large definition and
   existing-plan reading to the material the work needs while preserving complete project
   coverage, existing whole-document script checks and independent critique.
3. WAY-111 edited in place: replace its whole-foundation obligation with selection under the
   shared default; preserve bringing affected parts, decisions, invariants and boundaries to the
   human and asking whether the project fits or changes the existing decision. Rewrite its
   whole-reading rationale and examples to match the current rule.
4. WAY-115 edited in place: replace only the current foundation-reading obligation with the
   shared default. Preserve full project-source reading, the complete candidate table, next-reader
   consequence test, human selection, row-by-row recording and final Candidates line.
5. WAY-134 reread against changed WAY-115 and renew its `derives from WAY-115` fingerprint. Its
   binding meaning and acceptance do not change. Search again for any additional direct or
   unlinked effects before writing and before integration; this list is not proof that none exist.

Allocate the two new decision numbers from the actual log when writing them. Keep WAY-21,
WAY-31, WAY-33, WAY-44, WAY-62, WAY-95/97, WAY-118, WAY-120, WAY-146 and WAY-148 intact in meaning.

The new decisions describe agent reading behavior. Use level-2 compliant/violating examples for
that behavior, rather than inventing a test that a particular string names the shared section.
The required commit-level obligations already have `decisions-found-for-change`,
`project-plan-form` and `project-plan-check`; their current methods and limitations remain visible.
Do not falsely list an existing invariant as deriving from a new decision without assessing and
recording that derivation. The foundation and return steps still derive any genuinely new
commit-level rule they find under WAY-12/WAY-22; this design waives none of those duties.

## Verification and limitations

Use the existing changed-part tests and mandatory critical-flow tests:

- `python -B gate/run_tests.py project-level`
- `python -B gate/run_tests.py task-cycle`
- `python -B gate/run_tests.py elements/decisions`
- `python -B gate/run_tests.py elements/part-map`
- `python -B gate/run_tests.py elements/invariants`
- `python -B gate/run_tests.py elements/glossary`
- `python -B gate/run_tests.py elements/environment-facts`
- `python -B gate/run_tests.py gate`
- `python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none`
- If an invariant file changes, its guard with `--base none --merge-onto none` and its affected tests.

`elements/common` has no tests at this base; its runner's `NO TESTS RAN` is unchecked, not a pass.
The decision guard's no-main comparison omissions and any warnings remain explicit. No standalone
instruction-string test or new gate is required by this prose change. Audit all foundation-reading
clauses and conduct concrete workflow walkthroughs:

- A current decision with a wrapped Scope is found even when the task never linked it; changing
  an entry-collecting file follows its entries' parts, not merely the file's owning part.
- A project with no diff still selects affected parts, surfaces and decisions from its proposed
  work; ambiguous ownership expands reading.
- A changed decision discovers an incoming dependent and a relevant `Part: every` invariant.
- A whole-foundation collision search finds a conflicting entry outside selected Scope/links.
- A resumed large plan discovers a distant task dependency, entry writer and question; a new
  breakdown processes every scope item, projected entry and question in batches.
- A structurally valid plan with a goal that is only a layer, an unexplained question move or an
  inadequate quoted answer still fails the independent semantic judgment.

Review these walkthroughs against the actual final instructions; do not report a designed example
as an executed agent run. The full gate, automatic actual-read completeness and a measured token
reduction on a real large project remain unchecked. The result promises a different reading
method, not a measured savings percentage.

## Design boundary

No tracked file, code, foundation entry or commit is written in this stage. The next authorized
stage is independent spec review by an agent other than the designer, then `plan-task` dispatched
by the orchestrator after findings are settled. No implementation plan or implementation is part
of this spec stage.
