# Foundation selection — design stage

Method: "Reading the foundation", `elements/common/way_of_working.md` (WAY-150), applied by the
design agent of the task cycle.

## Revision

- Foundation read at `foundations` `96623ed7710100fe6e11a0ce3c052fc44d4af52d` (the task branch's
  base; worktree `C:/Storage/repos/the-way-wt/product-guidelines-styleguide`, clean when read).
- Files read whole: `foundations/part_map.md`, `foundations/glossary.md`; `foundations/decisions.md`,
  `foundations/invariants.md` and `foundations/environment_facts.md` read whole by a research
  subagent (see "Who read what"); `elements/common/way_of_working.md`, `elements/common/rules.md`
  read whole by the design agent.

## Touched parts

Existing parts the change touches or may touch:

- `decisions` — new decisions of the-way (26 decision rows, the WAY-100 adoption decision), the
  edit of WAY-09.
- `glossary` — the term "guidelines" (row 25).
- `part-map` — a new part, dependency changes, the flow `skills-reach-the-way-sessions`' list of parts.
- `invariants` — new invariants of the-way about the form check; renewed fingerprints where WAY-09's
  binding part changes (`repository-file-location` derives from WAY-09).
- `agent-instructions` — generated entry points of the new skill.
- `installation` — `SKILLS`, the product guidance block, the README table, the tests' `NAMES`.
- `instruction-files` — how its principles and check apply to a styleguide pointed to from a
  product's root `AGENTS.md`; read, not changed.
- `relation-model` — the form check uses `fingerprint.py`; read, not changed.
- `elements-common` — the form check loads `guard_shared.py`; the skill uses `way_of_working.md`,
  `critique`; read, not changed.
- `environment-facts` — the skill writes a product's facts through `record-environment-fact`; read.
- `project-level` — `technology/SKILL.md` as the model of the research discipline (WAY-122);
  `task/template.md` and `task/skill/SKILL.md` for the skill's place before a cycle; read.
- `task-cycle` — only as far as a styleguide task passes through `implement-task`; read, not changed
  (the cycle for view changes is out of scope).
- `gate` — test discovery and citation rules for the new tests; `gate/test_skills_reach_the_way_sessions.py`.

Prospective new part (not a map entry yet): the part answering for the guidelines template, the
styleguide template, the styleguide skill and the form check (identifier settled in the spec).

## Expected *Scope* matches

A script over the complete current log (latest version of every number; no repeal in the log)
listed each decision's *Scope*, wrapped values joined: 152 decisions, none with a missing or
malformed *Scope*. The touched parts above include `decisions`, which nearly every *Scope* names,
together with `project-level`, `task-cycle`, `elements-common`, `installation`,
`instruction-files`, `agent-instructions`, `relation-model` and `gate`: every one of the 152
decisions names at least one touched part. Expected matches: WAY-01 … WAY-166, all 152.

## Selected and read

Selected: all 152 decisions (by *Scope*), plus those the task names (WAY-02, 04, 09, 18, 22, 30, 31,
36, 38, 44, 51, 60, 62, 77, 86, 100, 114, 121, 122, 125, 127, 128, 129, 133, 136, 165 — all within
the *Scope* set). The selection equals the expected matches; nothing missing.

### Who read what

- Research subagent (same model, read-only, report
  [research-decision_map.md](research-decision_map.md)): all 152 decisions whole, all 210 invariants whole
  with *Part* fields, all 30 environment facts, keyword sweep of the five files. Its report
  rates each decision and quotes binding text; its causal readings were treated as hypotheses.
- Design agent, whole entries read directly in `foundations/decisions.md` at `96623ed` (line of the
  heading): WAY-02 (38), 03 (71), 04 (95), 05 (137), 07 (176), 08 (203), 09 (234), 17 (507), 18 (531),
  19 (563), 20 (596), 21 (623), 22 (645), 27 (763), 28 (794), 29 (826), 30 (857), 31 (891), 32 (926),
  33 (952), 34 (983), 35 (1012), 36 (1046), 37 (1075), 38 (1102), 44 (1233), 45 (1264), 46 (1290),
  47 (1331), 48 (1358), 51 (1428), 52 (1464), 53 (1490), 54 (1513), 60 (1697), 61 (1733), 62 (1787),
  63 (1818), 64 (1855), 65 (1895), 68 (1926), 69 (1960), 77 (2157), 86 (2442), 100 (2788), 101 (2814),
  102 (2837), 103 (2864), 104 (2889), 105 (2943), 113 (3181), 114 (3217), 121 (3427), 122 (3505),
  123 (3564), 127 (3762), 128 (3821), 129 (3863), 130 (3889), 131 (3929), 132 (3961), 133 (3999),
  141 (4397), 165 (5345).
- Design agent, binding sentences only (located, then relied on through the subagent's whole
  reading): WAY-26 (737), 84 (2377), 93 (2538), 107 (3018), 125 (3653), 134 (relation line 4055),
  166 (5392).
- Entries merely discovered (named by the subagent, not relied on): the remaining decisions rated
  `none` or `low` in `research-decision_map.md`.

### Invariants selected (WAY-62 reach, methods naming changed files, *Part* `every`)

Read whole (quoted by the subagent, checked against the file where relied on):
`repository-file-location/1` (invariants.md:146), `skill-entry-points/1` (:2065),
`instruction-file-imports/1` (:2075), `root-claude-md-import/1` (:2085),
`installation-claude-guidance/1` (:2095), `glossary-process-terms/1` (:1847),
`glossary-term-collision/1` (:1837), `decision-guard-stale-reference/1` (:6),
`relation-fingerprint-value/1` (:507), `fingerprint-definition/1` (:587),
`link-fingerprint-value/1`, `script-language/1`, `script-imports/1`, `script-subprocesses/1`,
`foundation-file-kinds/1`, `ci-checking-commands/1`. Every invariant whose *Part* is `every` is
reached by the change; the subagent listed them with their sentences.

### Glossary

Whole file read. Terms used or at risk of collision: "surface" (:203), "element", "part",
"entry", "result", "verdict", "gate", "format guard" (*Avoid*: "checker"), "foundation" (:86),
"repository instruction file" (:177), "agent's way to the running product" (:9). Words of the
change that the glossary does not hold and the foundation uses in another sense: "view"
(WAY-18's view of decisions in force), "token" (prose only: a secret in WAY-84's rationale, a
model's tokens in WAY-162), "guide" (WAY-128, WAY-130, WAY-133: the-way's integration guide).

### Environment facts

Whole file read by the subagent: 30 facts; no fact about WCAG, contrast, focus or any
accessibility catalogue. Facts on tools loading instruction files and skills listed in
`research-decision_map.md` §4.

## Search of the whole foundation for the topic (step 5)

Words searched in all five files: styleguide, guideline, guide, design system, token, UI, view,
screen, component, accessibility, WCAG, contrast, focus, hardcoded, hard-coded, literal, role,
kitchen, palette, colour, color. No entry speaks of styleguides, design tokens, components or
colour roles. Relevant hits: WAY-86's complying example (a decision adopting WCAG, naming its
edition, level AA and screens covered), WAY-08's accessibility example, WAY-121/WAY-165 on
screens and the interface, WAY-69 on literals in checks, WAY-18 "view". This is the design-stage
reading, not the WAY-33 search of the foundation step, which the cycle runs when entries are
written and again against the current `foundations` tip before integration.

## Comparison

The selected identifiers equal the expected *Scope* matches (152 of 152). The comparison records the
declared set and evidence of reading; it proves neither understanding nor completeness of semantic
collision discovery. Recheck when the spec's scope changes or `foundations` moves past `96623ed`.
