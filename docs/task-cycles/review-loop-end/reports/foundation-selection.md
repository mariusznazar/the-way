# Foundation selection — review-loop-end, foundation step

Method: "Reading the foundation" in `elements/common/way_of_working.md` (WAY-150), at base
`e7f7c3a15c3f80143f9ad582ec785c993cff3779` (= `origin/foundations`), worktree
`C:/Storage/repos/the-way-wt/review-loop-end`, branch `task/review-loop-end`.

## 1. Touched parts

- Part map read whole (`foundations/part_map.md`, 391 lines).
- Proposed behaviour: how the review of the whole change ends, which findings block, where Minor
  and out-of-scope findings go, what runs before a blocked request, the author's weakest-point
  check. All of it is the responsibility of `task-cycle` ("the steps a task runs through and how
  sharply a change is checked along them").
- Files this step changes: `foundations/decisions.md` (file of part `decisions`). It collects
  entries about many parts, so the touched parts follow from the entries changed (WAY-44): every
  entry written or edited has *Scope* `task-cycle`. Touched parts: **task-cycle**. The part
  `decisions` is not touched as a responsibility (the form of the log does not change).
- Prospective new part: none. Failure modes of `task-cycle`: three, all high, not detected
  (orchestrator stops for a settleable choice; omitted micro decision; unlisted entry).

## 2. Expected *Scope* matches (complete inspection)

Inspected all 146 current decision versions (all version 1, no repeals, no review records) with
wrapped *Scope* values joined (script in the author's scratchpad, output not kept in git).
56 decisions name `task-cycle`, with their heading line at base `e7f7c3a`:

WAY-01 (L6) · WAY-03 (L71) · WAY-09 (L234) · WAY-10 (L305) · WAY-11 (L343) · WAY-13 (L414) ·
WAY-16 (L480) · WAY-21 (L623) · WAY-25 (L708) · WAY-26 (L737) · WAY-27 (L763) · WAY-28 (L794) ·
WAY-30 (L857) · WAY-33 (L952) · WAY-34 (L983) · WAY-36 (L1046) · WAY-37 (L1075) · WAY-38 (L1102) ·
WAY-44 (L1233) · WAY-45 (L1264) · WAY-46 (L1290) · WAY-47 (L1331) · WAY-48 (L1358) · WAY-51 (L1428) ·
WAY-55 (L1546) · WAY-57 (L1607) · WAY-62 (L1787) · WAY-63 (L1818) · WAY-65 (L1895) · WAY-68 (L1926) ·
WAY-69 (L1960) · WAY-82 (L2320) · WAY-89 (L2476) · WAY-100 (L2788) · WAY-101 (L2814) ·
WAY-102 (L2837) · WAY-103 (L2864) · WAY-106 (L2992) · WAY-120 (L3395) · WAY-124 (L3562) ·
WAY-125 (L3612) · WAY-126 (L3665) · WAY-127 (L3712) · WAY-134 (L3984) · WAY-135 (L4038) ·
WAY-136 (L4089) · WAY-140 (L4292) · WAY-144 (L4461) · WAY-147 (L4584) · WAY-148 (L4615) ·
WAY-149 (L4661) · WAY-150 (L4703) · WAY-157 (L4959) · WAY-158 (L4988) · WAY-159 (L5015) ·
WAY-160 (L5045)

Explicitly named by the task and handoff: WAY-125, WAY-136, WAY-11, WAY-10, WAY-148, WAY-13,
WAY-69, WAY-101, WAY-140, WAY-134 — all inside the 56. Missing matches: none.

After this step the selection also holds the new WAY-161, WAY-162, WAY-163, WAY-164 (*Scope*
`task-cycle`).

## 3. Read vs discovered

- **Decisions: read whole** — the complete log `foundations/decisions.md` (5073 lines at base) was
  read whole, so every one of the 56 selected entries and every linked entry (WAY-07, WAY-14,
  WAY-19, WAY-20, WAY-31, WAY-32, WAY-107, WAY-114 and the rest) was read with all fields,
  rationale and *Rejected*. Nothing in the log was merely discovered.
- **Invariants:** no entry's *Part* names `task-cycle`; 47 name `every`. Read whole (relevant to
  the cycle's review, merge and foundation route): foundation-change-merge-route,
  foundation-change-assessment-record, return-step-record, foundation-change-path,
  foundation-search-record, decisions-found-for-change, level-one-decision-invariants,
  verification-invariant-derivation, decision-approval-record, decision-approver,
  decision-guard-stale-reference, log-reference-target, log-existing-lines,
  log-versions-added-per-number, log-merge-copies, decision-verification-level. Discovered only (headings and *Part* lines): the other `every` invariants (scripts,
  map, facts, glossary, surfaces, skill entry points) — none concerns review, findings or requests.
  No invariant derives from WAY-125 or WAY-136 (searched their fingerprints across the repository).
- **Glossary:** read whole (31 terms). Terms the entries touch: verdict, correction, result (all
  avoided in the new wording — a reviewer's call is a "grade", the repair a "fix", a check's
  outcome "what the check showed"), gate, slice, return step, foundation step, entry, open design
  choice, human action (used in their glossary meanings or not used).
- **Environment facts:** headings of all 30 inspected; study facts lines 62–133 read whole; none
  holds Superpowers or review behaviour, none is named by the new entries.
- **Templates, rules, examples (mandatory, whole):** `elements/decisions/template.md`,
  `elements/common/rules.md`, `elements/common/way_of_working.md`,
  `elements/decisions/examples.md` (example WAY-03 read whole in the log),
  `elements/decisions/skill/SKILL.md`, `.claude/skills/the-way-record-decision/SKILL.md`.

## 4. Incoming dependents of the entries changed

- WAY-125 (binding part changed): `derives from WAY-125@7362c7ab` in WAY-140, WAY-148, WAY-157 —
  each checked against the new binding part, still valid, fingerprint renewed to `18d08c16`.
  No invariant, test or other file carries `7362c7ab`.
- WAY-136 (unchanged): dependent WAY-158 keeps `986ff0ac`.

## 5. Recheck

Refresh this selection when the scope of the code step or the target branch changes (step 11 and
step 12 of the cycle).
