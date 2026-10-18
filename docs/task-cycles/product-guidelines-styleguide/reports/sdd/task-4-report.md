# Task 4 report — the skill `maintain-styleguide` and its entry points

Status: DONE_WITH_CONCERNS. Commit `f248e42` (BASE `10b5f4a`), author `mariusznn@gmail.com`.

## What was implemented

- `product-guidelines/styleguide/SKILL.md` (new, 207 lines):
  - frontmatter of spec §6.1 verbatim (one line, 287 characters, safe plain YAML — the generator
    accepted it; says "user interface");
  - opening paragraphs: what the skill does, where each rule it relies on stands (both templates,
    `way_of_working.md`, `critique`, element skills) and that it restates none of them (§6.5);
    where the-way lies (session checkout in the-way, `.the-way` in a product), every named skill
    being the `the-way-` project skill; no Superpowers (WAY-125); WAY-175 named as what is taken
    from outside practice, no outside source named or pointed to (WAY-27);
  - "Where the skill works" — the split of §6.2 as a table, the hand-over points into
    `refine-task` (steps 1–2 → this skill at step 3 → back to step 4), and the approval route of
    WAY-172 (meaning approved through the accepted task document; using an existing meaning needs
    none);
  - "What reaches the task document" — *To do* fixed items (styleguide file from the template;
    value and source per role; page of every state; checks; the instruction-file pointer and rule
    of §6.6/WAY-192; for the first guidelines the `guidelines/**` pattern and the two invariant
    copies; audit items), *Questions to settle*, *Context*, *Settlements to record*;
  - "Orchestrated mode" — §6.4;
  - steps 0 Read, 1 Recognize, 2 Starting rules, 3 Audit, 4 Settle with the human (how to show,
    what it settles, accessibility, invariants, critique), 5 Hand back — §6.3.
- `.claude/skills/the-way-maintain-styleguide/SKILL.md` and `.agents/skills/the-way-maintain-styleguide/SKILL.md`
  — written in process by `produce(discover(ROOT))` for these two paths only (script below), never
  by hand, never `--write`.
- `README.md` — "What else is here" gains `product-guidelines/` (naming the styleguide's skill
  directory); "Using the skills" names `product-guidelines/styleguide/` beside the other skill
  directories.

Script used for the entry points (scratchpad, not committed):

```python
import sys
from pathlib import Path
root = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(root / "agent-instructions"))
import skill_entry_points as g
assert g.ROOT == root, (g.ROOT, root)
produced = g.produce(g.discover(g.ROOT))
targets = [".claude/skills/the-way-maintain-styleguide/SKILL.md",
           ".agents/skills/the-way-maintain-styleguide/SKILL.md"]
for t in targets:
    p = g.ROOT / t
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(produced[t].encode("utf-8"))
```

## Checks

All outputs under `.runs/task-cycles/product-guidelines-styleguide/reports/`, run at `f248e42`.

| Command | Exit | Output | Result |
|---|---|---|---|
| in-process `produce(discover(ROOT))[path] == bytes on disk` for both paths | 0 | `slice-4-entry-points-equal.txt` | both `True`; the pair byte-identical (`cmp`) |
| `python -B agent-instructions/skill_entry_points.py` | 0 | `slice-4-entry-points.txt` | 0 `would create`, exactly 30 `would change`, no orphan; the 30 paths equal, sorted, the paths named in task-5/6/7 briefs (diff empty) |
| `python -B gate/run_tests.py agent-instructions` | 1 | `slice-4-tests-agent-instructions.txt` | 18 tests, 1 failure: `test_the_tracked_entry_points_are_what_the_generator_produces` on `.claude/skills/the-way-critique/SKILL.md` (sibling list lacks `maintain-styleguide`) — expected red until S7, not suppressed |
| `python -B gate/run_tests.py gate` | 1 | `slice-4-tests-gate.txt` | 98 tests, 1 failure: `test_every_skill_reaches_a_session_on_the_way`, 15 entry points not naming `maintain-styleguide` — expected red until S7, not suppressed |
| `git diff --check 10b5f4a HEAD` | 0 | `slice-4-diff-check.txt` | clean |
| weakest-point check (below) | 0 | `slice-4-weakest-point-overlap.txt` | 14 shared runs, 1 substantive, kept with reason |

## Row-to-text table (spec §10)

`S` = `product-guidelines/styleguide/SKILL.md`, `T` = `product-guidelines/styleguide/template.md`,
`G` = `product-guidelines/template.md`, at `f248e42`.

| Row | Carried by |
|---|---|
| 5 roles named by role, meaning for the user, values pointed to | T:79-91 (`## Roles`: "named by what it is for and never by a colour"; "The table holds no value"); S:167-168 "The roles of the table the styleguide template gives, each row settled with the human, its value and the value's source among them" |
| 6 background always with its text | T:85-86 (*Text on it*), T:98-102 (rule "Every background with its text"); S:167 (each row of the table settled, *Text on it* among its columns) |
| 7 shared components by path, states described, no inventory | T:119-126 ("States of shared controls"); S:168 "the states of the shared controls" |
| 8 a fault of one screen fixed in its component | T:127-134; S:184-185 proposes "for each rule the styleguide template requires, the invariant its entry under 'What each part carries' names" |
| 9 mockup a pattern, not a specification | T:144-147 (example "Mockups"); S:135-136 "A mockup shows what a screen holds; the meaning of a colour on it is settled with the human, never read off it (WAY-179)" |
| 10 kitchen-sink page, development only | T:139-143; S:54 "build the page of every state, or extend it"; S:168-169 "the page of every state" among what is settled |
| 11 plan order as example | T:148-150 (example "Plan of a user-interface change"); the skill adds nothing |
| 12 each value carries its source; the skill picks it | T:135-138, T:185-187; S:51-53 "naming for each role the value and its source as the human settled them, or the exact address of the source and the entry in it the value is read from (WAY-182)"; S:167-168 |
| 13 every user interface, admin panel included | S:99-102 "A product whose users reach it only through an API or a terminal has no user interface in this sense … Every other user interface gets a styleguide of its own, however simple, an admin panel added to a backend included" (WAY-183); T:5-8 |
| 14 recognize first, extend what exists | S:106-108 "Read off what the product has for it …"; S:112-113 "Extend what exists. A new library … is a technology choice: record it as an open question of the task, never settle it" |
| 15 before the first screen, wider than the first task | S:117 "Before the first screen …"; S:137-138 "so it is wider than the first task that uses it (WAY-184)" |
| 16 preferences, else research with sources and critique; announced meanings; research again | S:119-136 (preferences as a question of assessment; research with page and version per source; critique refuting unsupported claims, `critique: passed`; "proposed in step 4, never imposed"; announced screens from definition, plan, specs, mockups; "at every refresh or extension") |
| 17 two-way audit, 3–5 charges, four categories, standing question, agent's way or code | S:142-157 |
| 18 every binding rule has an invariant, else example | T:58-67 (required form); S:181-182 "Every binding rule gets an invariant of the kind the styleguide template's required form gives, and a rule no invariant can check goes among the examples (WAY-188)" |
| 19 first invariants: no hard-coded value, visible focus, contrast | S:184-187 "among them the first ones WAY-189 gives: by a script, no value written in place of a design token, visible focus on every control, and the contrast of every pair …"; T:103-118 |
| 20 companion invariant for gradual cleaning | S:191-194 "where the human chooses to clean the screens as tasks touch their styles … the second invariant WAY-190 gives, while the full one stands on the list of violated invariants …"; T:106-109 |
| 21 WCAG through an adopting decision, default AA, newest edition, facts | S:173-180 |
| 22 instruction file points to the styleguide and forbids hard-coded values | S:56-61 (*To do* item applying `maintain-instruction-files`, WAY-192) |
| 23 choices shown by what the user sees | S:161-166 "Show each choice by what someone using the product sees … never by the names or values of design tokens … say in plain words what it means (WAY-174, WAY-113)" |
| 24 new meaning a decision, approved in the task document before code; use needs none | S:38-41 "A meaning reaches the code only through the task document … Using a meaning that a decision of the product's log already carries takes no approval"; T:189-190 (blocked draft request in the cycle) |
| 26 template binds through the product's adopting decision; departure by a decision with reason | T:10-12; G:81-84; S:170-171 "the product's decision adopting the template, and each departure from it by a decision with its reason (WAY-173)" |
| 27 asks even with a recommendation; approval before code | S:163-164 "Put every choice to the human, a choice the skill recommends included"; S:38-41 |

## Files changed (`10b5f4a..f248e42`)

| File | Added | Removed |
|---|---|---|
| `product-guidelines/styleguide/SKILL.md` | 207 | 0 |
| `.claude/skills/the-way-maintain-styleguide/SKILL.md` | 15 | 0 |
| `.agents/skills/the-way-maintain-styleguide/SKILL.md` | 15 | 0 |
| `README.md` | 5 | 2 |

## Sharpness inputs

- Parts touched: `product-guidelines` (the skill), `agent-instructions` (`.claude/skills/**`,
  `.agents/skills/**`); `README.md` is claimed by no part (`foundations/part_map.md:413`). The
  critical flow `skills-reach-the-way-sessions` is red from this commit until S7, by plan.
- Trust-boundary files: none (`form_check.py` untouched).
- Irreversible: none.

## Weakest-point check (WAY-164)

- Requirement most likely not met: "restating no rule of the templates or element skills"
  (brief Goal; spec §6.5). A skill that leads the work naturally re-explains the templates.
- Check: a script compares every run of seven or more words of the skill with eight files it must
  not restate (both templates, `way_of_working.md`, `refine-task`'s skill and template,
  `find-foundation-entries`, `critique`, `instruction-files`), and each shared run is judged by
  hand. Actor: this executor; scratchpad script `overlap.py`; output
  `reports/slice-4-weakest-point-overlap.txt`.
- First run showed two restatements, fixed before the commit: the WAY-188 kind of invariant
  ("a script where a script can decide it and otherwise an agent whose method sets k of n runs")
  and the role-meaning invariant's *Part*, both now pointed to in the template.
- Final run: 14 runs. 13 are names, paths or the location paragraph every skill shares
  (`elements/common/skill/SKILL.md`). One is substantive: S:51-53 repeats the wording of T:185-187
  on what *To do* names per role. Kept on purpose: spec §6.2 (root finding 12) places it on both
  sides — the refiner writes *To do* that way, the author reads it that way — and the template's
  rule is addressed to the author, the skill's to the refiner.

## Self-review

- Spec §6.1–§6.6 each has its place; rows 5–24, 26, 27 map as above.
- Words: "user interface" and "screen" only (no bare "interface"/"view"), "design token" only,
  "discipline", "form check"; no glossary word in another meaning (`surface`, `slice`, `gate`).
- No outside source named (grep for `10x`, `Mercato`, `om-ux`, `shadcn`, `tweakcn`: none).
- No `@` in the skill; lines ≤ 100 characters outside the table and frontmatter.
- Template sections the skill names exist: "Writing the file", "Pairs, meanings and role names",
  "What each part carries" (T:179, T:155, T:73).

## Concerns

1. **Spec §6.2 vs `find-foundation-entries`.** The spec lists "the part-map change" among
   *Settlements to record*; `elements/common/skill/SKILL.md` (task mode) and
   `project-level/task/template.md` say a part-map change is never a row. The skill follows the
   element skill and template: the part-map change stands in *To do* (S:71-73). The whole-change
   review should confirm the reading.
2. **A user interface with no part in the map yet** (before the first screen): the styleguide's
   file name and *Applies to* need a part of the map, and the form check reports one the map lacks.
   The spec does not say what happens then. The skill makes the part's identifier a question of
   the task and adds a *To do* item putting that part, with the files the task creates, on the map
   through `update-part-map` (S:102-105). Autonomous reading; its price: a part whose first files
   are the design-tokens file and the page of every state.
3. **Step 2 scope.** Following spec §6.3, starting-rules research runs before the first screen and
   at every refresh or extension, not for a product with screens and no styleguide (audit mode).
   WAY-186 does not restrict it to those modes; the spec does. The skill follows the spec.
4. **Research questions** are illustrated by three examples (naming and pairing colour roles, focus,
   states of controls), not a fixed list, to keep WAY-186's "never a fixed list".
5. Expected red: agent-instructions and gate tests fail on the 30 stale entry points until S7.
6. The skill text is prose that no test asserts; it has had no trial on a product (spec §10; the
   `loop2` task after the merge).

## Fix round 1

Commit `784284c` (`product-guidelines/styleguide/SKILL.md` +7/−1), on `f248e42`.

- **I1 addressed.** Where a law or contract binds the user interface's accessibility, the skill now
  records two things beside the environment fact. First, at S:177-179, the obligation also stands
  as a failure mode of the user interface's part: the human gives its kind of damage and its
  severity, its detection names the invariant that rests on that fact, and it reaches the map
  through *To do* (WAY-46). Second, at S:65-67, a matching *To do* item records it at the part
  through `update-part-map`. This keeps the rule that a part-map change is never a row of
  *Settlements to record*. Row 21 of the row-to-text table now also cites S:65-67 and S:176-179.
- **I2** was ruled by the controller: no change. Minors are deferred to the final review.
- The frontmatter is unchanged, so the entry points are unchanged.

| Command | Exit | Output (`.runs/task-cycles/product-guidelines-styleguide/reports/`) | Result |
|---|---|---|---|
| in-process `produce(discover(ROOT))` equality, both paths | 0 | `slice-4-fix-1-entry-points-equal.txt` | both `True` |
| `python -B agent-instructions/skill_entry_points.py` | 0 | `slice-4-fix-1-entry-points.txt` | 0 `would create`, 30 `would change`, same paths as S5–S7 |
| `python -B gate/run_tests.py agent-instructions` | 1 | `slice-4-fix-1-tests-agent-instructions.txt` | 1/18 fails, the same stale-entry-point test as before (expected until S7) |
| `python -B gate/run_tests.py gate` | 1 | `slice-4-fix-1-tests-gate.txt` | 1/98 fails, the same critical-flow test as before (expected until S7) |
| `git diff --check 10b5f4a HEAD` | 0 | `slice-4-fix-1-diff-check.txt` | clean |
