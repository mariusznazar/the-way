# Foundation selection — agent-path-to-running-product, foundation step

Method: "Reading the foundation" in `elements/common/way_of_working.md` (WAY-150), at base
`77c8a8bb98d4a093c9a4c9891ac4e9ad86f4f988` (= `origin/foundations`), worktree
`C:/Storage/repos/the-way-wt/agent-path-to-running-product`, branch
`task/agent-path-to-running-product`.

## 1. Touched parts

- Part map read whole (`foundations/part_map.md`, 391 lines).
- Proposed behaviour: the project definition's Technology list always holds three choices of how an
  agent reaches the running product (logs, interface, development data); what each asks and how an
  agent's use of an option weighs; the readiness gate stops a definition lacking one, approved
  definitions included. All of it is the responsibility of `project-level` ("the form and writing
  of a project definition, its readiness gate, ... the refinement of a task").
- Files this step changes: `foundations/decisions.md` (file of part `decisions`). It collects
  entries about many parts, so the touched parts follow from the entries changed (WAY-44): WAY-121,
  WAY-122, WAY-123 and the new WAY-165 all have *Scope* `project-level, decisions`. Touched parts:
  **project-level**, **decisions** (the latter through the entries' *Scope*: these decisions bind
  the projected decisions a definition writes).
- Files the later code step is expected to touch (from the cycle record): `project-level/**`
  (template, `technology/SKILL.md`, `skill/SKILL.md`, `task/skill/SKILL.md`, `readiness_check.py`
  and its tests) and `foundations/invariants.md` (invariant `project-technology-record`, *Part*
  `project-level`). No prospective new part. Trust boundary of `project-level`:
  `project-level/readiness_check.py`, `plan_check.py`, `plan_state.py`.
- Failure modes of `project-level` relevant here: "a definition reaches the breakdown with a listed
  technology choice still open or naming no entry — detected by project-technology-record"; "a
  technology choice the project needs is missing from the definition's list — not detected".

## 2. Expected *Scope* matches (complete inspection)

Inspected all 150 current decision versions at base (all version 1, no repeals, no review
records, every *Scope* present) with wrapped *Scope* values joined (scratch script, output not kept
in git). 96 decisions name `project-level` or `decisions`, with their heading line at base:

WAY-01 (L6) · WAY-02 (L38) · WAY-04 (L95) · WAY-05 (L137) · WAY-07 (L176) · WAY-09 (L234) ·
WAY-10 (L305) · WAY-11 (L343) · WAY-12 (L384) · WAY-14 (L459) · WAY-17 (L507) · WAY-18 (L531) ·
WAY-19 (L563) · WAY-20 (L596) · WAY-21 (L623) · WAY-22 (L645) · WAY-24 (L673) · WAY-25 (L708) ·
WAY-26 (L737) · WAY-27 (L763) · WAY-28 (L794) · WAY-29 (L826) · WAY-30 (L857) · WAY-31 (L891) ·
WAY-32 (L926) · WAY-33 (L952) · WAY-34 (L983) · WAY-35 (L1012) · WAY-36 (L1046) · WAY-37 (L1075) ·
WAY-38 (L1102) · WAY-52 (L1464) · WAY-53 (L1490) · WAY-54 (L1513) · WAY-55 (L1546) ·
WAY-60 (L1697) · WAY-61 (L1733) · WAY-65 (L1895) · WAY-69 (L1960) · WAY-71 (L1996) ·
WAY-72 (L2034) · WAY-73 (L2060) · WAY-74 (L2093) · WAY-84 (L2377) · WAY-85 (L2410) ·
WAY-86 (L2442) · WAY-89 (L2476) · WAY-90 (L2505) · WAY-95 (L2606) · WAY-97 (L2686) ·
WAY-98 (L2722) · WAY-99 (L2756) · WAY-100 (L2788) · WAY-101 (L2814) · WAY-102 (L2837) ·
WAY-103 (L2864) · WAY-104 (L2889) · WAY-106 (L2992) · WAY-107 (L3018) · WAY-108 (L3044) ·
WAY-109 (L3075) · WAY-110 (L3098) · WAY-111 (L3122) · WAY-112 (L3151) · WAY-113 (L3181) ·
WAY-114 (L3217) · WAY-115 (L3246) · WAY-116 (L3277) · WAY-117 (L3305) · WAY-118 (L3334) ·
WAY-119 (L3368) · WAY-120 (L3395) · WAY-121 (L3427) · WAY-122 (L3464) · WAY-123 (L3523) ·
WAY-124 (L3562) · WAY-126 (L3674) · WAY-127 (L3721) · WAY-134 (L3993) · WAY-137 (L4172) ·
WAY-138 (L4212) · WAY-139 (L4262) · WAY-140 (L4301) · WAY-142 (L4380) · WAY-143 (L4432) ·
WAY-144 (L4470) · WAY-145 (L4507) · WAY-146 (L4553) · WAY-147 (L4593) · WAY-150 (L4712) ·
WAY-151 (L4750) · WAY-152 (L4787) · WAY-153 (L4818) · WAY-154 (L4860) · WAY-155 (L4898) ·
WAY-156 (L4933)

Of these, 40 name `project-level`. Explicitly named by the task and handoff: WAY-121, WAY-122,
WAY-123, WAY-137, WAY-138, WAY-118, WAY-139, WAY-140, WAY-143, WAY-100, WAY-04 — all inside the 96.
Also named by the task's answers: WAY-102 (answer 4), WAY-134 (*Settlements to record*), WAY-31
(fingerprints) — inside the 96. Missing matches: none.

After this step the selection also holds the new WAY-165 (*Scope* `project-level, decisions`).
On the branch, line numbers after L3427 shift (WAY-121 grew by 46 lines, WAY-165 is appended at the
end of the log).

## 3. Read vs discovered

- **Decisions: read whole** — the complete log `foundations/decisions.md` (5302 lines at base) was
  read whole, so every one of the 96 selected entries and every linked entry (WAY-08, WAY-13,
  WAY-125, WAY-135, WAY-136 and the rest) was read with all fields, rationale and *Rejected*.
  Nothing in the log was merely discovered.
- **Invariants:** five name *Part* `project-level`; read whole: project-definition-form,
  project-readiness-gate, project-technology-record, project-plan-form, project-plan-check,
  project-plan-state-evidence and project-plan-state-subprocesses (headings, sentences, links).
  `every` invariants read whole where relevant to a decision change: level-one-decision-invariants,
  verification-invariant-derivation, foundation-search-record, foundation-change-path,
  link-fingerprint-value, decision-scope-names, decisions-found-for-change. Discovered only
  (headings and *Part* lines): the other `every` invariants (scripts, map, facts, glossary,
  surfaces, skill entry points) — none concerns the Technology section or the readiness gate.
  Incoming dependents of WAY-121: only `project-technology-record` (*Derives from*
  WAY-121@740c254e); invariant tests citing it: `project-level/test_readiness_check.py`
  (17 tests, lines 404–495).
- **Glossary:** read whole (31 terms). Terms the entries touch: surface (not used — the task
  forbids it for the interface), gate (the entries say "readiness gate" and "readiness check" as
  the log already does), entry, task, human action (used in its meaning in WAY-165's example),
  preparatory task (not used). "running product", "logs", "interface", "development data" are used
  as the field uses them and take no entry (WAY-95); the binding sentences of WAY-165 say what each
  choice asks.
- **Environment facts:** headings of all 30 inspected; none holds logging, test data, interfaces,
  test environments or an agent's access to a product; none is named by the new entries.
- **Templates, rules, examples (mandatory, whole):** `elements/decisions/template.md`,
  `elements/common/rules.md`, `elements/common/way_of_working.md`,
  `elements/decisions/examples.md` (example WAY-03 read whole in the log),
  `elements/decisions/skill/SKILL.md`, `.claude/skills/the-way-record-decision/SKILL.md`.
- **Files the change will touch, read whole:** `project-level/definition_template.md`,
  `project-level/technology/SKILL.md`, `project-level/readiness_check.py`; read in part:
  `project-level/skill/SKILL.md` (lines 50–183), `project-level/task/skill/SKILL.md` (60–99),
  `project-level/plan/skill/SKILL.md` (60–70), `project-level/lead/skill/SKILL.md` (28–40),
  `project-level/plan_state.py` (370–395), `project-level/test_readiness_check.py` (395–500),
  Technology fixtures of `test_plan_state.py`, `test_plan_state_invariant.py`, `test_plan_check.py`.

## 4. Incoming dependents of the entries changed

- WAY-121 (binding part changed, `740c254e` → `d0b060e5`): `derives from WAY-121@740c254e` in
  WAY-122 and WAY-123 — each checked against the new binding part, still valid, renewed to
  `d0b060e5`. Invariant `project-technology-record` carries `WAY-121@740c254e` — **left stale on
  purpose**: `foundations/invariants.md` is not edited in this turn (WAY-69; the sentence agent
  rewrites it and renews the link). No test or other file carries `740c254e`.
- WAY-137 (unchanged, `86b2a30d`): newly named by WAY-165 as `narrows`.
- WAY-123 (unchanged, `f3b45293`): newly named by WAY-165 as `derives from`; its other dependents
  WAY-137, WAY-138 keep `f3b45293`.

## 5. Recheck

Refresh this selection when the scope of the code step or the target branch changes (return step
and the reconciliation with `foundations`).
