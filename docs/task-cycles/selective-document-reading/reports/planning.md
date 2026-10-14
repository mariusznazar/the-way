# Planning report — selective document reading

Status: finished plan; all slices fit; no unresolved design choice.
Boundary: task-cycle step 8, before foundation writing and implementation.

## Inputs and result

- Worktree: `C:/Storage/repos/the-way-wt/selective-document-reading`.
- HEAD and base: `52b9d487efeafe37c46ad2b9f10d60c13a885e63`.
- Followed this worktree's `.agents/skills/the-way-plan-task/SKILL.md`, `task-cycle/plan/SKILL.md` and `agent-instructions/README.md`.
- Read the frozen `.runs/task-cycles/selective-document-reading/task.md` and reviewed `spec.md` whole, plus `reports/spec-review.md` and `reports/initial-scope-check.md`. The orchestrator accepted the review's sole verification finding; the spec now names the four formerly omitted element suites. This is a provisional stage go-ahead, not human foundation acceptance.
- Read the complete part map and glossary, all matching current decisions described below, the applicable complete invariant entries, all 13 reader files, common rules, the decision template and project-plan template. Inspected existing Scope parsing, slice-size behavior, runner/guard argument sources and test coverage references sufficiently to name the existing commands; no new interface is needed.
- Wrote `.runs/task-cycles/selective-document-reading/plan.md`, `.runs/task-cycles/selective-document-reading/plan-size.md` and this report only. No tracked file, foundation entry, code, test, commit or git state was changed; no subagent or human question was used.

The plan has a separate preceding foundation stage and two implementation slices. Slice 1 changes
the shared reading method and all element/common readers (7 files). Slice 2 changes project/task
workflow reading and plan-project document selection (6 files). Every spec reader appears exactly
once in the Change sets. Both accepted settlement rows, WAY-111/115 revisions and the WAY-134
dependent fingerprint renewal appear before dependent slices. Future decision numbers are left
to the foundation author, who uses the actual log.

## Scope and actual-read evidence

At Base the actual proposed changes touch `decisions`, `part-map`, `invariants`, `glossary`,
`environment-facts`, `elements-common`, `project-level` and `task-cycle`. This follows both the
reader paths and the foundation entries, rather than only the decision log's owning part.

A fresh read-only `python -B` invocation loaded the existing
`elements/part-map/format_guard.py:1121` helper and inspected the entire current log's Scope
fields, including wrapped values. It found 135 current decision entries with Scope fields and
128 matches for the eight parts. A separate heading count also found 135 current entries; no
repeal entry exists at this base. The selected set is every current decision in the following
complete-entry source ranges of `foundations/decisions.md`:

| Complete current entries selected and actually read | Source range at Base |
|---|---|
| All current entries through WAY-127 | 6–3748 |
| WAY-134, WAY-135, WAY-136, WAY-137, WAY-138, WAY-139, WAY-140 | 3962–4298 |
| WAY-142, WAY-143, WAY-144, WAY-145, WAY-146, WAY-147, WAY-148, WAY-149 | 4323–4640 |

Equivalently, the seven current entries outside the match set are WAY-128, WAY-129, WAY-130,
WAY-131, WAY-132, WAY-133 and WAY-141. The planner loaded all 128 matching entries whole in
batches; two truncated tool outputs were repaired by rereading the affected complete entries.
Expected: 128; selected: 128; actually loaded: 128; missing: 0. A comparison of the loaded-ID
inventory with the fresh expected set also reported no missing identifier. That comparison is
operational evidence, not a test proving actual understanding or an implementation of the
invariant's Method.

The eleven added matches from the earlier five-part scan were read in full: WAY-08, WAY-56,
WAY-58, WAY-76, WAY-77, WAY-78, WAY-80, WAY-81, WAY-94, WAY-96 and WAY-105. Their element-specific
duties reveal no new design blocker. The relevant Part-field selection, including `every`,
yielded 186 current invariant entries; those complete entries were also read in three batches.
The critical flows' decision stale-reference and skill-entry-point invariants are included.

The plan narrows its base Read sets to the actual slice parts: 105 current decisions for the six
Slice 1 parts and 74 for the two Slice 2 parts, with overlapping entries counted in each agent's
inputs. Their applicable invariant ranges are complete entries. These are locators at Base,
not a frozen future foundation: the foundation edits can shift line numbers, add decisions and
expand Scope. Refresh current selection and whole-entry ranges before dependent dispatch and
rerun size measurement where Read sets change. The orchestrator has explicitly accepted that
routine correction.

## Open-choice assessment and autonomous choices

No unresolved open design choice was found. The reviewed spec settles the shared section, the
selection/expansion contract, the large-document method and its boundaries. The task explicitly
authorizes changing WAY-111/115; their current whole-reading wording does not block the accepted
revision. The actual incoming WAY-115 fingerprint appears in WAY-134's Relations at Base line
3980. Further incoming or unlinked effects still require the foundation author's actual search;
the known dependent is not an exhaustive search verdict.

| Choice made in the plan | Alternative rejected | Cost if wrong |
|---|---|---|
| Two coherent reviewed slices after foundation writing | A 13-file slice or separate mechanical referral slices | Each reviewer still reads several workflows; split only if an executor demonstrates that the goal is too large |
| Slice 2 consumes the reviewed Slice 1 contract | Concurrent consumers against an unsettled shared method | Sequential work costs elapsed time; it prevents independently drafted contracts from diverging |
| Existing suites/guards and concrete instruction walkthroughs | New selector, parser, persistent inventory or string tests | Semantic execution remains only partly checkable; extra literal checks would not prove completeness |
| Original documents remain authoritative, with temporary inventories in existing evidence | Reduced check copies or another maintained plan | Selection still requires judgment; whole-file checks and complete independent semantic review remain mandatory |
| Refresh base complete-entry ranges after foundation edits | A whole log in every Read field or stale fixed line numbers | A read-only refresh and possible size rerun cost work, but prevent cut entries and missing newly applicable decisions |

The two write sets are disjoint but their semantics are dependent: the six project/task readers
consume Slice 1's finalized shared reading section. No useful parallel implementation opportunity
remains in this proportionate cut. Separately, adopted Superpowers 6.4.1
`subagent-driven-development` prohibits parallel implementation subagents. The orchestrator
records its ruling, including shared mutable worktree/test state and separate review ranges,
before execution. A single final review remains required after both slice reviews.

## Checks executed

| Check | Result |
|---|---|
| Fresh current-Scope/heading/repeal inspection with existing helper | Exit 0; 128 expected matches across eight parts; no missing current Scope field or repeal at Base |
| Loaded-ID versus expected-ID comparison | Exit 0; 128 loaded, 128 expected, no missing identifier |
| `python -B task-cycle/slice_size.py .runs/task-cycles/selective-document-reading/plan.md` | Exit 0; both slices fit; actual unmodified output saved as plan-size.md |
| Tracked status before writing the ignored artifacts | Clean at Base |
| Artifact/range inspection and final tracked status | Exit 0; no unwanted control character in the three outputs; no foundation range starts or ends inside an entry; tracked tree remains clean |

Actual size results:

| Slice | Changed files | Characters to read | Estimated tokens | Verdict |
|---|---|---|---|---|
| 1 | 7 | 503552 | 201421 | fits |
| 2 | 6 | 502207 | 200883 | fits |

The size tool's token estimate is rough and measures declared input and changed-file counts,
not execution steps. Its limits are 250000 estimated tokens and 10 changed files. No slice is
too large or unchecked. Each source range includes the complete entries it selects at Base.

No suite, guard, agent walkthrough or benchmark was run by this planning stage. The plan names
future commands for every changed part and both current critical flows, plus the actual changed
foundation guards. It does not introduce a production-code test-first step for Markdown changes.

## Remaining concerns for the next dispatch

No blocking question or design concern remains. The foundation author must allocate the two
numbers, write both whole settlements and authorized revisions, reread WAY-134 before its
fingerprint renewal, and perform the required linked/unlinked searches. Refresh the plan's
current-entry ranges and expected Scope set after those writes before execution.

Keep these limitations explicit in future evidence: `elements/common` has no tests; the full
gate and automatic actual-read completeness are unimplemented; no-main guard comparisons leave
unchecked work and existing warnings may remain; `decisions-found-for-change/1` keeps Method
TODO; and no real large-project token savings were measured. Inspection walkthroughs are not
executed agent runs. None of these is represented as a successful full-gate result.

Return paths:

- Plan: `C:/Storage/repos/the-way-wt/selective-document-reading/.runs/task-cycles/selective-document-reading/plan.md`
- Size report: `C:/Storage/repos/the-way-wt/selective-document-reading/.runs/task-cycles/selective-document-reading/plan-size.md`
- Planning report: `C:/Storage/repos/the-way-wt/selective-document-reading/.runs/task-cycles/selective-document-reading/reports/planning.md`
