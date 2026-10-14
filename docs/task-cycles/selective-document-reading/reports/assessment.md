# Independent foundation assessment — selective document reading

Assessed source range: `52b9d487efeafe37c46ad2b9f10d60c13a885e63..1de9e1aa8e91134131d2e5c6d07c0f0ebf359186`.
Assessor: independent agent, GPT-6 Astra; the dispatch identifies the source authors as GPT-6.1 Sol and GPT-6 Luna.
Assessment date: 2026-10-14.
Source root: `C:/Storage/repos/the-way-wt/selective-document-reading`.

The change has one minor consistency finding below. I found no material contradiction in the proposed selection rules, their preservation of required searches and checks, or the independent plan critique. This is an assessment for author settlement, not approval of the foundation change or verification of its task-cycle execution.

## Boundary and material examined

I used the supplied source-only diff and file list, the full contents of all 14 changed source files at the assessed head, relevant foundation entries, the complete part map and glossary, the decision template and examples, the common rules, the project-plan template, and relevant readiness/plan-check implementation. I inspected source history without commit-message rationale. `HEAD` was the assessed head, and `git diff --name-only <assessed-head> --` returned no tracked working-tree differences.

The supplied `assessment-files.json` lists paths and the two commits; it contains no per-file hashes. I therefore checked the actual Git range (14 source files) and computed SHA-256 values from the assessed head's Git objects. The full changed targets were:

- `elements/common/skill/SKILL.md`, `elements/common/way_of_working.md`;
- `elements/decisions/skill/SKILL.md`, `elements/environment-facts/skill/SKILL.md`, `elements/glossary/skill/SKILL.md`, `elements/invariants/skill/SKILL.md`, `elements/part-map/skill/SKILL.md`;
- `foundations/decisions.md`;
- `project-level/plan/skill/SKILL.md`, `project-level/skill/SKILL.md`, `project-level/task/skill/SKILL.md`, `project-level/technology/SKILL.md`;
- `task-cycle/plan/SKILL.md`, `task-cycle/skill/SKILL.md`.

I did not read the frozen task, spec, cycle plan, chronology, operational handoffs, reports other than the two supplied assessment inputs, prompts, session transcripts, or the authors' reasoning outside assessed source. Source entries' Rationale and Rejected fields were read as source. I changed no source, branch, HEAD or index and started no subagent. This report is the only file written.

## F1 — remove the pending-decision marker now answered by WAY-150

**Finding: minor source consistency issue; a concrete cut is available.**

At [elements/common/way_of_working.md:118](https://github.com/mariusznazar/the-way/blob/1de9e1aa8e91134131d2e5c6d07c0f0ebf359186/elements/common/way_of_working.md#L118), the search section still says:

> Read each entry whole: a decision's *Rejected* holds an option already weighed and refused, and nowhere else says so
> (`TODO — decision pending: which decision sets that the search reads a decision's *Rejected*`).

The change supplies that decision: [WAY-150, foundations/decisions.md:4649](https://github.com/mariusznazar/the-way/blob/1de9e1aa8e91134131d2e5c6d07c0f0ebf359186/foundations/decisions.md#L4649) requires reading selected entries whole and expanding selection, while the new method explicitly includes all fields and Rejected at [elements/common/way_of_working.md:76](https://github.com/mariusznazar/the-way/blob/1de9e1aa8e91134131d2e5c6d07c0f0ebf359186/elements/common/way_of_working.md#L76) and whole search findings at line 97. Leaving the TODO says this obligation still lacks its governing decision after that decision has been written. WAY-37 requires resolving what the change supplies to waiting entries; its same-change principle also makes this adjacent instruction debt needless.

Proposed local wording, for the author to settle:

> Read each entry selected or found by the search whole (WAY-150): a decision's *Rejected* holds an option already weighed and refused, and nowhere else says so.

This cuts the obsolete pending marker and makes clear that “each entry” means a selected entry or search finding, rather than silently reinstating whole-foundation reading. It does not cut the search domain or weaken the requirement to read complete entries. Leaving it costs misleading debt and an avoidable interpretation; changing it costs one local wording correction. This is not evidence that the new selection method fails in use.

## O2 — beneficiary, point of use and source-level need

**No concern about the stated beneficiary or placement; realized savings are unverified.**

The immediate beneficiary is the agent starting or resuming work under a skill, and the human paying for or waiting on that work. The new rule acts before drafting, planning or implementing, where the old rules explicitly loaded complete files. The common method is reached by each changed entry-writing skill and the changed project/task workflows. The unchanged requirement to read the complete part map provides a basis before any changed-file list exists.

The source itself demonstrates a real opportunity: at the base, the decision log has 135 decision entries and 4,640 lines; at the head it has 137 entries and 4,720 lines. As a bounded illustration, direct current Scope matching for `project-level` selects 35 of the head's 137 entries; `task-cycle` selects 51, and `decisions` 72. These are **initial direct matches only**, not final reading counts: explicitly named decisions, relations, invariants, facts, terms and search findings expand them. I checked an actual matching entry, WAY-111, against its Scope and meaning; the count is of real decision entries, not textual mentions. This establishes that the proposed mechanism can avoid unrelated initial reads, not that it saves any particular number of tokens or improves an agent's judgment.

For a fresh breakdown, WAY-151 still processes every scope item, projected entry and question. Its strongest potential saving is on resumed, local work, not a claim that a complete initial breakdown need read only a small fraction of its source. The changed source says this accurately at [project-level/plan/skill/SKILL.md:70](https://github.com/mariusznazar/the-way/blob/1de9e1aa8e91134131d2e5c6d07c0f0ebf359186/project-level/plan/skill/SKILL.md#L70).

## O3 — history and frequency

**Source frequency is measurable; agent-run frequency and recurrence after the earlier rules are unavailable to this assessment.**

I used `git log -S` restricted to source paths and inspected the historical source, with commit identifiers and dates but without commit messages. The common requirement to read the element's entries and the glossary in full entered in `e1d54e3` on 2026-09-29. The pending marker discussed in F1 entered in `6fa7510` on 2026-09-29. WAY-111 and WAY-115 entered in `56a88e5` on 2026-10-04. The plan skill's whole-definition and whole-existing-plan reads entered in `ffa9aa6` on 2026-10-11. WAY-21 and WAY-33 already existed in `4685365` and `7b21b80`, respectively, on 2026-09-16. I compared those rules with the base and assessed-head source, rather than treating each later mention as an occurrence of a problem.

Thus older selection and collision-search principles coexist with later unconditional-read instructions. Merely telling agents again to follow Scope would leave explicit whole-file obligations in place; this change replaces those obligations rather than adding an unrelated retry rule. The plan's unconditional-read instruction is recent. Its age is a reason not to claim repeated observed failures without run evidence.

Eligible source inspection spans these introductions through the assessed head. The examined agent-run population is **zero**: no session transcript or operational run log is permitted by the independent-assessment input boundary. I did not search such records to circumvent that boundary. Neither the number of real over-reading incidents, the number after an earlier rule took effect, repeated omissions, nor latency/token savings can be measured from the eligible material. Dates above are dates of source rules, not dates of agent failures. The existing environment facts on instruction density and context-file effects concern their named studies and models; they do not measure this proposal's effect. The new rationales appropriately avoid presenting a local measured gain.

## O4 — completeness of foundation selection and its failure modes

**No material concern found in the declared selection contract; semantic discovery remains a human/agent judgment.**

I compared the new method with WAY-21, WAY-44, WAY-17, WAY-31, WAY-33, WAY-37, WAY-62, WAY-95 and WAY-97. [elements/common/way_of_working.md:59](https://github.com/mariusznazar/the-way/blob/1de9e1aa8e91134131d2e5c6d07c0f0ebf359186/elements/common/way_of_working.md#L59) retains the complete map, all current Scope fields including wrapped values, every matched decision, whole selected entries, relevant forward and incoming links, invariant Part fields including `every`, methods naming changed files, and glossary terms and Avoid spellings. Unknown ownership expands the search instead of narrowing it to an empty diff. An unlinked search finding expands selection outside the initial part set.

The risk moves from unconditional material volume to the agent's judgment of relevance. A sound Scope inventory cannot prove an unlinked semantic collision absent, and reading an identifier does not prove reading its entry. The new method explicitly distinguishes discovered/read entries, compares expected and selected identifiers, retains the all-five-element search, and states those limits. Those qualifications are necessary, not candidates to cut.

The selective method does not remove element-specific searches for duplicates, withdrawn identifiers, dependents or glossary uses. The first-map and no-foundation routes remain in the relevant skills. I found no introduced new foundation format or maintained index.

## O5 — authoritative project sources and independent critique

**No concern found about a reduced copy passing as the source or about limiting the critic to the author's excerpts.**

[project-level/plan/skill/SKILL.md:49](https://github.com/mariusznazar/the-way/blob/1de9e1aa8e91134131d2e5c6d07c0f0ebf359186/project-level/plan/skill/SKILL.md#L49) requires whole-original checks, complete initial inventories, exact open questions, complete source units, refresh after source changes and expansion through distant dependencies. At line 124, the independent critique reads the complete authoritative plan and every source unit needed for its whole semantic judgment, independently of the author's inventory. This preserves WAY-142, WAY-145 and WAY-146 rather than outsourcing semantic judgment to a structural check.

I verified the relevant implementation: [project-level/plan_check.py:634](https://github.com/mariusznazar/the-way/blob/1de9e1aa8e91134131d2e5c6d07c0f0ebf359186/project-level/plan_check.py#L634) reads the original plan and resolves its definition relative to that plan; its header check compares the definition fingerprint, and its check routine checks assignments, scope coverage, dependencies and questions. [project-level/readiness_check.py:278](https://github.com/mariusznazar/the-way/blob/1de9e1aa8e91134131d2e5c6d07c0f0ebf359186/project-level/readiness_check.py#L278) fingerprints the definition's sections from Goal to before Gate record; its read function reads the whole file. The patch changes neither command nor parser. Original paths matter because a copied plan could resolve its definition differently.

The new plan rule is limited to `plan-project`: the other source-consuming skills still require their specified whole sources. It does not silently authorize selective reading of the frozen task, the source from which candidate settlements are extracted, or the technology step's definition.

## O6 — fidelity of the changed foundation entries and relationships

**No concern found in fidelity to eligible governing sources. Human authorization and task conformance are outside this filtered assessment.**

WAY-150 states the common selection policy; WAY-151 states the distinct policy for project definitions/plans and retains the independent whole-plan critique. WAY-111 and WAY-115 now delegate foundation reading to WAY-150 while preserving, respectively, the project conversation about changed constraints and the source/candidate process. This is a change of their meaning, visibly requiring renewed human acceptance; their pending merge approval fields do not falsely retain the old approval dates. The integration guide expressly permits in-place decision edits before main.

The changed WAY-134 relation correctly carries the new WAY-115 fingerprint without changing WAY-134's settlement-carrying meaning. Independent normalized-binding SHA-256 calculations gave WAY-115 `eb7ba15c`, WAY-150 `3bd9e695`, and unchanged WAY-134 `b858b34f`, matching the affected references. Searching the source foundation found no further fingerprinted dependent of WAY-111 or WAY-115 requiring an update. The new decisions' form includes the required fields, no unsupported quantitative claim, and rationale/rejected options consistent with the binding rule. The relevant glossary meanings remain intact.

I cannot establish fidelity to the human's task wording or settlements because those materials are expressly excluded. I do not infer their contents from the implemented change, from pending approval fields, or from the source rationale. The author must settle this report against that authority without giving it retroactively to the independent assessor.

## O7 — verification boundaries

**No concern found about falsely claiming a full gate; no runtime or agent-behavior result is supplied by this assessment.**

[foundations/invariants.md:407](https://github.com/mariusznazar/the-way/blob/1de9e1aa8e91134131d2e5c6d07c0f0ebf359186/foundations/invariants.md#L407) still gives `decisions-found-for-change` Method `TODO`; [foundations/invariants.md:527](https://github.com/mariusznazar/the-way/blob/1de9e1aa8e91134131d2e5c6d07c0f0ebf359186/foundations/invariants.md#L527) does the same for `foundation-search-record`. The new shared method explicitly acknowledges the first gap and keeps WAY-33 evidence separate. Scope-name validity and fresh fingerprints cannot establish semantic completeness or prove a reader understood the sources. Project guard tests protect their declared structural checks, not actual selective reading by an agent.

I ran `git diff --check` on the exact assessed range: exit 0, no findings. Source/hash checks were read-only. I did not run tests, alter fixtures, generate run logs or inspect the authors' test reports: the only permitted mutation was this report. Consequently this assessment makes no assertion that implementation checks ran or passed, no full-gate claim and no inference from an unrun deliberate break.

## O8 — costs, cheaper alternatives and cut conclusion

**Keep the mechanism; cut the obsolete pending marker in F1. No additional substantive cut is supported by the source.**

Keeping the old behavior costs repeated unrelated source context but offers simpler reading instructions and fewer selection judgments. The proposed behavior reduces potentially unnecessary complete-entry loading but adds a complete map/field inventory, all-element searches, selection evidence and refresh work. Narrow changes may still read many entries, and a broadly scoped foundation change may approach a whole read. Small files may be read whole, so there is no need for a size threshold, token cap, separate path or new maintained index.

The cheaper existing ingredients are already used: Scope routing from WAY-21, map ownership from WAY-44, written links and incoming-dependent review from WAY-17/WAY-31, and whole-foundation collision search from WAY-33. Using only known links or keyword matches is cheaper but fails the governing-decision lower bound and unlinked-conflict requirement. Leaving plan checks or the critic on excerpts would save work by changing what they check, not by achieving the same effect more cheaply. A maintained index adds synchronization cost without solving semantic relevance.

Centralizing the common method and using short skill references avoids copying its rules into every consumer. The entry-specific additions (version/number inspection, actual fact dependents, term-use searches) still serve distinct operations. The separate WAY-151 rule serves source documents with tasks/questions rather than foundation entries, so merging it into WAY-150 would join different contracts. I recommend no extra tooling, permanent inventories, invariants claiming agent understanding, benchmark requirements or instruction layers on the strength of this assessment alone.

The author should settle F1 and explicitly retain the limitation that observed savings and agent-run failure frequency were not measured here. No other correction or substantive deletion is requested.
