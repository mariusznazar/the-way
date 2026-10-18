# Plan — wytyczne produktu: styleguide jako pierwsze wytyczne

- Task: `.runs/task-cycles/product-guidelines-styleguide/task.md`
- Spec: `.runs/task-cycles/product-guidelines-styleguide/spec.md`
- Base: `96623ed7710100fe6e11a0ce3c052fc44d4af52d` (`foundations`); foundation stage closed at
  `8ea4679` (F1a `2181273`, F1b `5fde846`, F2+F3 `eb9ff1e`, F4 `8ea4679`)

The frozen task binds over the reviewed spec; the spec binds where it settles more; the root's
rulings in `cycle.md` (C25–C28) bind the slices they name. This plan holds no code, no test body
and no wording of an entry: it names entries, files, commands and what each is to do.

The spec's working names G1–G26 are written as these decisions (root): G1 WAY-167, G2 WAY-168,
G3 WAY-169, G4 WAY-170, G26 WAY-171, G5 WAY-172, G6 WAY-173, G24 WAY-174, G25 WAY-175, and G7–G23
WAY-176–WAY-192 in order (G7 WAY-176, G8 WAY-177, G9 WAY-178, G10 WAY-179, G11 WAY-180, G12
WAY-181, G13 WAY-182, G14 WAY-183, G15 WAY-184, G16 WAY-185, G17 WAY-186, G18 WAY-187, G19
WAY-188, G20 WAY-189, G21 WAY-190, G22 WAY-191, G23 WAY-192). Below, WAY numbers stand for them.
"S1"–"S8" are the slices; "F1"–"F4" the foundation stages, now made.

Every `foundations/decisions.md` and `foundations/invariants.md` range below is a whole entry at
`8ea4679` (heading line to the line before the next heading). A slice that changes either file
does not exist in this plan, so the ranges hold until integration; each receiving agent still
checks and expands its selection by "Reading the foundation" (WAY-150).

## Foundation entries

All written before the slices, at the commits above (`reports/foundation.md` holds their meaning
sentences, searches and checks; `reports/check-author.md` the F4 check).

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| WAY-167 (G1) — what a product's guidelines are and where they lie | new decision | Settlements row 1; spec §2.2, §9.1; root C7 | S1, S2, S4, S8 |
| WAY-168 (G2) — what a guideline holds beside the entries that carry it | new decision | row 2; spec §3.1 | S1, S2; `guidelines-check-carrier` |
| WAY-169 (G3) — a reference whose entry changed wording stops the merge | new decision | row 3; spec §3.2, §5.3 item 7 | S1, S3; `guidelines-reference-current`, `-check-reference-target`, `-check-stale-reference` |
| WAY-170 (G4) — the form check checks the form before a merge | new decision | row 4; spec §5 | S1, S2; `guidelines-form`, `-check-form`, `-check-code-path` |
| WAY-171 (G26) — the common form, the language rule, templates cite their decisions (C27) | new decision | spec §3.1, §3.2; root C22, C27 | S1, S2; `guidelines-form`, `-check-form` |
| WAY-172 (G5) — a new or changed meaning approved before code; a value kept with its meaning is no decision (C27); `narrows` WAY-114 | new decision | rows 24, 27; spec §7; root C19, C23, C27 | S1, S4 |
| WAY-173 (G6) — the styleguide template binds through the product's adopting decision | new decision | row 26 | S1, S4; parent of WAY-176–WAY-184 |
| WAY-174 (G24) — the skill asks even with a recommendation, shows through what the user sees; `narrows` WAY-114 | new decision | rows 23, 27 | S4 |
| WAY-175 (G25) — what the-way takes from `10x-ui` and the Open Mercato skills | new decision | task *Decisions in play* (WAY-100) | S1, S4 |
| WAY-176 (G7) — roles by role, background–text pairs, *Kind*, words role names avoid | new decision | rows 5, 6 | S1, S2; `guidelines-check-colour-pair` |
| WAY-177 (G8) — states of shared controls | new decision | row 7 | S1, S4 |
| WAY-178 (G9) — a fault of one screen is fixed in its component (refers to WAY-172's clause) | new decision | row 8; root C23, C27 | S1, S4 |
| WAY-179 (G10) — a mockup is a pattern to compare against | new decision | row 9 | S1 |
| WAY-180 (G11) — the kitchen-sink page | new decision | row 10 | S1, S4 |
| WAY-181 (G12) — the plan order of a user-interface change as an example | new decision | row 11 | S1 |
| WAY-182 (G13) — each value carries its source; the skill picks it | new decision | row 12 | S1, S4 |
| WAY-183 (G14) — every user interface gets a styleguide | new decision | row 13 | S1, S4, S8 |
| WAY-184 (G15) — a styleguide before the first screen, wider than the first task | new decision | row 15 | S4 |
| WAY-185 (G16) — the skill first recognizes what the product has | new decision | row 14 | S4 |
| WAY-186 (G17) — where the starting rules come from | new decision | row 16 | S4 |
| WAY-187 (G18) — the two-way audit | new decision | row 17 | S4 |
| WAY-188 (G19) — every binding rule of a styleguide has an invariant; `narrows` WAY-168 | new decision | row 18 | S1, S2; `guidelines-check-carrier` |
| WAY-189 (G20) — the starting invariants | new decision | row 19; root C16 | S1, S2, S4; `guidelines-check-carrier` |
| WAY-190 (G21) — the companion invariant for gradual cleaning | new decision | row 20 | S1, S4 |
| WAY-191 (G22) — thresholds of contrast and focus through a decision adopting WCAG | new decision | row 21 | S1, S4 |
| WAY-192 (G23) — the instruction file points to the styleguide and forbids hard-coded values | new decision | row 22 | S1, S4 |
| WAY-09/1 — `product-guidelines/` added, fingerprint `909e9c5c` → `ce6bd9c0` | decision edit in place | spec §2.1; root C10 | every slice |
| WAY-38/1, WAY-27/1 — *Scope* gains `product-guidelines` | field edit | spec §2.1; finding 21 | S2, S3, S4 |
| six WAY-09 invariants (`foundations/invariants.md:146-205`) — *Derives from* renewed | invariant link renewal | WAY-31, WAY-57 | every slice |
| "guidelines" (`foundations/glossary.md:105-110`) | glossary term | row 25; spec §9.2 | S1, S4, S8 |
| part `product-guidelines` (`foundations/part_map.md:261-279`), `installation` and `agent-instructions` *Depends on*, flow `skills-reach-the-way-sessions` | part-map part and changes | spec §9.4 | every slice |
| surface `guidelines-form-check-command` (`foundations/part_map.md:355-360`), declared at `product-guidelines/form_check.py · main` | part-map surface | glossary "surface", WAY-49 (root accepted, C25) | S2, S3, S8 |
| `guidelines-form/1` (`foundations/invariants.md:2133-2142`). Check: the form checks of `product-guidelines/form_check.py` (S2). Covered: a product's `guidelines/` files, none in the-way | new invariant | spec §3.3 | S1 (template gives the sentence), S2 |
| `guidelines-reference-current/1` (`:2143-2152`). Check: the reference checks of `form_check.py` (S3). Covered: as above | new invariant | spec §3.3 | S1, S3 |
| `guidelines-check-form/1`, `-carrier/1`, `-colour-pair/1`, `-code-path/1` (`:2153-2182`, `:2203-2212`). Check: `product-guidelines/test_form_check_invariants.py` (F4). Covered: the form checks of `form_check.py` (S2) | new invariants | spec §9.3 | S2 |
| `guidelines-check-reference-target/1`, `-stale-reference/1` (`:2183-2202`). Check: the F4 file. Covered: the reference checks of `form_check.py` (S3) | new invariants | spec §9.3 | S3 |

No environment fact of the-way (spec §9.5). No projected entry: the task is independent.

### Foundation stages (made)

- **F1** — `2181273` (WAY-167–WAY-175, WAY-09 in place, *Scope* of WAY-27 and WAY-38) and
  `5fde846` (WAY-176–WAY-192), through `the-way-record-decision`.
- **F2 + F3** — `eb9ff1e`: the glossary term, the part, the *Depends on* and flow changes, the
  surface, the eight invariant sentences and the six renewals, by the sentence author.
- **F4** — `8ea4679`: `product-guidelines/test_form_check_invariants.py`, 25 tests over the six
  `guidelines-check-*`, by a check author who is neither the sentence author nor an executor of
  S2 or S3; its run fails because `form_check.py` does not exist (recorded RED). The file is
  read-only for every slice (WAY-03); a slice that needs it changed returns to the foundation step.
  Its line and message assertions are the contract S2 and S3 meet (C28 (2)).

Expected until code exists: the part-map guard reports the trust boundary and the surface naming a
missing file until S2; rerun there. The whole-foundation search (WAY-33) is repeated against the
`foundations` tip before integration; the independent assessment (WAY-10) covers the foundation
change and the F4 check together.

Deliberate breaks (WAY-69), each from the sentence by a reviewer who wrote neither the check nor
the covered code: the reviewer of S2 for `guidelines-form` (a crafted guidelines file run through
`form_check.py`) and for `guidelines-check-form`, `-carrier`, `-colour-pair`, `-code-path` (a
guard line of `form_check.py` removed); the reviewer of S3 for `guidelines-reference-current`,
`guidelines-check-reference-target` and `-stale-reference`. Code and file are restored and the
checks rerun clean.

## Slices

### Slice 1 — The guidelines template and the styleguide template

- **Goal:** `product-guidelines/template.md` gives the common form of spec §3 — what it binds, the
  fenced skeleton the form check reads, the rules of writing (references, code in backticks or
  fenced code, language), the sentences of `guidelines-form` and `guidelines-reference-current`
  as given, not the product's to reword, with the-way's decisions they come from — and
  `product-guidelines/styleguide/template.md` gives the merged form of spec §4.1, what each part
  carries (§4.2, each rule with the decision and invariant the skill proposes, each example under
  `## Examples`), the pairs and translated-meanings notes, role names (WAY-176) and "Writing the
  file" for the cycle's author (§4.3). The required-rule headings are written verbatim as §4.1
  gives them — `### Each role in its meaning` exactly, since `guidelines-check-carrier` and the F4
  tests name it. Each rule cites the decision that sets it (WAY-171, C27); the rule "A fault of
  one screen is fixed in its component" follows WAY-178 with WAY-172's clause that a value kept
  with its meaning is no decision; no value is written.
- **Change:** `product-guidelines/template.md` · `product-guidelines/styleguide/template.md`
- **Read:** `.runs/task-cycles/product-guidelines-styleguide/task.md`
  `.runs/task-cycles/product-guidelines-styleguide/spec.md`
  `.runs/task-cycles/product-guidelines-styleguide/cycle.md:89-92`
  `elements/common/rules.md` · `elements/invariants/template.md` · `foundations/glossary.md`
  `foundations/part_map.md` · `instruction-files/check_instructions.py`
  `product-guidelines/test_form_check_invariants.py`
  `foundations/decisions.md:38-69` · `foundations/decisions.md:95-135`
  `foundations/decisions.md:234-315` · `foundations/decisions.md:543-573`
  `foundations/decisions.md:657-683` · `foundations/decisions.md:775-804`
  `foundations/decisions.md:995-1056` · `foundations/decisions.md:1525-1556`
  `foundations/decisions.md:1709-1743` · `foundations/decisions.md:2008-2070`
  `foundations/decisions.md:2454-2486` · `foundations/decisions.md:2550-2798`
  `foundations/decisions.md:2901-2953` · `foundations/decisions.md:3056-3085`
  `foundations/decisions.md:3833-4044` · `foundations/decisions.md:5439-6368`
  `foundations/invariants.md:2133-2212`
- **Checks:** text, no behaviour: no test of its own. After it, the F4 tests can reach the
  templates; `python -B gate/run_tests.py product-guidelines` still fails for want of
  `form_check.py` — recorded. On a temporary git repository whose root `AGENTS.md` names in
  backticks a `guidelines/styleguide-web.md` filled from the template (every required rule, a role
  table, a class with `/` in fenced code, a versioned package name), run
  `python -B instruction-files/check_instructions.py <temp repository>`: no `error`, no
  `dead-path`, no `at-import`; output kept. `python -B elements/part-map/format_guard.py foundations/part_map.md --base none`
  shows `product-guidelines/**` matching files. `git diff --check`. Manual check in the report:
  every `### ` of spec §4.1 present, verbatim and in order, matching the headings the F4 fixtures
  use; each rule names its decision; each part of §4.2 marked rule or example; no value, no
  package name, no glossary *Avoid* word.
- **Depends on:** F1 (WAY-167–WAY-192) · F2 (the term, the part) · F3 (the two sentences the
  template gives) · F4 (the headings its fixtures use)

### Slice 2 — The form check: form, carriers, parts and paths

- **Goal:** `product-guidelines/form_check.py` runs as spec §5.1 gives it — `ROOT`,
  `--merge-onto` (accepted and recorded as selecting the reference checks, which S3 adds),
  `--record`, exit codes 0/1/2, one report per guidelines file and one for the run — reads the
  templates from the-way checkout it lies in (C28 (1)), reads what §5.2 gives except the
  foundation's decisions and invariants, treats `~~~` fences as fenced code (C28 (4)), reports
  errors 1–6 and 5a of §5.3 under `guidelines-form/1` with the lines and message fragments the F4
  tests assert (C28 (2), (6)), holds the trust boundary of §5.4, cites
  `# invariant: guidelines-form/1` where it records it, loads the part-map guard's parser by path
  with a discarded report of its own, and passes the F4 tests of `guidelines-check-form`,
  `-carrier`, `-colour-pair` and `-code-path`; run on the-way (no `guidelines/`) it records `pass`
  for `guidelines-form/1`.
- **Change:** `product-guidelines/form_check.py` · `product-guidelines/test_form_check.py`
- **Read:** `.runs/task-cycles/product-guidelines-styleguide/task.md`
  `.runs/task-cycles/product-guidelines-styleguide/spec.md`
  `.runs/task-cycles/product-guidelines-styleguide/cycle.md:92-92`
  `.runs/task-cycles/product-guidelines-styleguide/reports/check-author.md`
  `product-guidelines/test_form_check_invariants.py` · `foundations/part_map.md`
  `elements/common/guard_shared.py` · `elements/part-map/format_guard.py:1-330`
  `elements/part-map/format_guard.py:704-777` · `elements/invariants/format_guard.py:1122-1191`
  `elements/decisions/format_guard.py:1-80` · `instruction-files/check_instructions.py`
  `gate/run_tests.py:1-80` · `foundations/decisions.md:38-69` · `foundations/decisions.md:95-135`
  `foundations/decisions.md:1114-1142` · `foundations/decisions.md:1370-1438`
  `foundations/decisions.md:1745-1936` · `foundations/decisions.md:1972-2006`
  `foundations/decisions.md:2105-2138` · `foundations/decisions.md:2488-2515`
  `foundations/decisions.md:5487-5527` · `foundations/decisions.md:5571-5655`
  `foundations/decisions.md:5835-5873` · `foundations/decisions.md:6227-6296`
  `foundations/invariants.md:547-576` · `foundations/invariants.md:877-886`
  `foundations/invariants.md:1317-1326` · `foundations/invariants.md:1497-1516`
  `foundations/invariants.md:2133-2142` · `foundations/invariants.md:2153-2182`
  `foundations/invariants.md:2203-2212`
- **Checks:** start from the F4 tests, failing without the script (recorded), and from a failing
  ordinary test in `product-guidelines/test_form_check.py` (a repository with no `guidelines/`
  exits 0 with a `note:`). Ordinary tests cover what no invariant's sentence holds: records with no
  option (`guidelines-form/1` lines only), findings of two files under their own paths, `warning:`
  for `guidelines/styleguide/web.md` and `guidelines/x.MD`, the trust boundary (a symlink —
  skipped where the platform cannot create one — a directory `x.md`, `guidelines` as a file,
  non-UTF-8 bytes, a file over 1 MiB refused unread, a file just under 1 MiB of one line of
  backticks, `@` and hex runs finished within a bound, the git subprocess calls captured to show
  no refused path reaches git, a patched `socket` failing if called), a non-`.jsonl` record path
  exiting 2, and each report's count line. The report states what a no-option run does on a
  reference error (C28 (5)). Run `python -B gate/run_tests.py product-guidelines` (the F4
  reference tests still fail until S3 — recorded);
  `python -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` (exit 0,
  `pass` for `guidelines-form/1`);
  `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none`
  (no `invariant-citation-target` error); `python -B elements/part-map/format_guard.py foundations/part_map.md --base none`
  (trust boundary and surface name existing items); `python -B gate/run_tests.py gate`. WAY-48:
  the reviewer checks the crafted inputs above against §5.4.
- **Depends on:** Slice 1 · F3 (`guidelines-form`, four `guidelines-check-*`) · F4 · WAY-168,
  WAY-170, WAY-171, WAY-176, WAY-188, WAY-189 · F2 (part, trust boundary, surface)

### Slice 3 — The form check: references and the merge

- **Goal:** `product-guidelines/form_check.py` finds every reference of the two forms of spec §3.2
  outside fenced code (`~~~` fences included, C28 (4)), whatever its section, withdrawn
  identifiers counting (C28 (3)), and reports error 7 of §5.3 under
  `guidelines-reference-current/1` with the lines and fragments the F4 tests assert — malformed
  fingerprint, a decision absent or repealed, an invariant absent or withdrawn, a fingerprint
  other than the current one on the same commit and, with `--merge-onto`, after the merge
  (decisions from the decisions guard's merged log; an invariant as on the branch where its
  sentence differs from the fork point, else as on the onto commit) — computing every fingerprint
  through `relation-model/fingerprint.py`, borrowing the decisions and invariants guards' parsers
  with discarded reports, never offering to renew a fingerprint; `--merge-onto none` records the
  same-commit `pass` or `fail` and the merge `unchecked` with the shared reason; without the
  option the merge check does not run and a `note:` says so; the F4 tests of
  `guidelines-check-reference-target` and `-stale-reference` pass.
- **Change:** `product-guidelines/form_check.py` · `product-guidelines/test_form_check.py`
- **Read:** `.runs/task-cycles/product-guidelines-styleguide/task.md`
  `.runs/task-cycles/product-guidelines-styleguide/spec.md`
  `.runs/task-cycles/product-guidelines-styleguide/cycle.md:92-92`
  `.runs/task-cycles/product-guidelines-styleguide/reports/check-author.md`
  `product-guidelines/test_form_check_invariants.py` · `elements/common/guard_shared.py`
  `relation-model/fingerprint.py` · `elements/decisions/format_guard.py:1-300`
  `elements/decisions/format_guard.py:805-965` · `elements/invariants/format_guard.py:1-461`
  `elements/invariants/format_guard.py:1403-1525` · `gate/test_wording_reaches_dependants.py`
  `foundations/decisions.md:38-69` · `foundations/decisions.md:519-541`
  `foundations/decisions.md:575-633` · `foundations/decisions.md:903-962`
  `foundations/decisions.md:1619-1660` · `foundations/decisions.md:1907-1936`
  `foundations/decisions.md:1972-2006` · `foundations/decisions.md:2105-2138`
  `foundations/decisions.md:5529-5569` · `foundations/invariants.md:6-15`
  `foundations/invariants.md:507-516` · `foundations/invariants.md:587-596`
  `foundations/invariants.md:1357-1366` · `foundations/invariants.md:2143-2152`
  `foundations/invariants.md:2183-2202`
- **Checks:** start from the failing F4 reference tests and a failing ordinary test (a run with
  `--merge-onto` records `guidelines-reference-current/1` lines only). Ordinary tests:
  `react@18`, `tailwindcss@4`, `lucide-react@0` and a bare identifier in prose pass; a token in
  fenced code is ignored; a decision log whose copies conflict with the onto commit gives no
  `log-merge-copies` line and no exit 1; without `--merge-onto` a `note:`. Run
  `python -B gate/run_tests.py product-guidelines` (all pass);
  `python -B product-guidelines/form_check.py --merge-onto none --record .runs/guidelines-reference.jsonl`
  (exit 0; same-commit `pass`, merge `unchecked`);
  `python -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` (still `pass`);
  `python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none`;
  `python -B gate/run_tests.py elements/decisions`, `elements/invariants`, `relation-model`, `gate`.
  End to end: on a temporary product with a part map, decisions and invariants, a
  `guidelines/styleguide-web.md` filled from the template passes the form check, and after a
  decision it names is reworded fails it with both fingerprints in the message. WAY-48: the
  reviewer checks the reference pattern for runaway matching on the long-line input of S2.
- **Depends on:** Slice 2 · F3 (`guidelines-reference-current`, two `guidelines-check-*`) · F4 ·
  WAY-169

### Slice 4 — The skill `maintain-styleguide` and its entry points

- **Goal:** `product-guidelines/styleguide/SKILL.md` holds the frontmatter of spec §6.1 (one-line,
  safe plain YAML description saying "user interface") and steps 0–5 of §6.3, the split of §6.2,
  the orchestrated mode of §6.4, §6.5 and the instruction-file guidance of §6.6, describing what it
  takes from outside sources without naming them (WAY-27) and restating no rule of the templates
  or element skills; it follows WAY-172–WAY-175 and WAY-182–WAY-192; its two entry points exist
  exactly as the generator produces them; the root `README.md` names `product-guidelines/` and
  the skill directory beside the others.
- **Change:** `product-guidelines/styleguide/SKILL.md`
  `.claude/skills/the-way-maintain-styleguide/SKILL.md`
  `.agents/skills/the-way-maintain-styleguide/SKILL.md` · `README.md`
- **Read:** `.runs/task-cycles/product-guidelines-styleguide/task.md`
  `.runs/task-cycles/product-guidelines-styleguide/spec.md`
  `.runs/task-cycles/product-guidelines-styleguide/cycle.md:91-91`
  `.runs/task-cycles/product-guidelines-styleguide/reports/research-outside_sources.md`
  `project-level/task/skill/SKILL.md` · `project-level/task/template.md`
  `project-level/technology/SKILL.md` · `elements/common/way_of_working.md`
  `elements/common/critique/SKILL.md` · `elements/common/skill/SKILL.md`
  `instruction-files/SKILL.md` · `agent-instructions/skill_entry_points.py`
  `foundations/glossary.md` · `foundations/part_map.md` · `foundations/decisions.md:6-36`
  `foundations/decisions.md:806-901` · `foundations/decisions.md:1024-1085`
  `foundations/decisions.md:1709-1743` · `foundations/decisions.md:1799-1828`
  `foundations/decisions.md:1938-1970` · `foundations/decisions.md:2072-2103`
  `foundations/decisions.md:2140-2285` · `foundations/decisions.md:2454-2486`
  `foundations/decisions.md:2800-2824` · `foundations/decisions.md:3030-3054`
  `foundations/decisions.md:3193-3256` · `foundations/decisions.md:3407-3725`
  `foundations/decisions.md:3774-4098` · `foundations/decisions.md:4765-4801`
  `foundations/decisions.md:4913-4984` · `foundations/decisions.md:5357-5485`
  `foundations/decisions.md:5657-6368` · `foundations/invariants.md:2133-2152`
- **Checks:** process prose, no test asserts it. The two entry points are written with the
  generator's own `discover` and `produce`, in process, for these two paths only — never by
  hand, never by `--write` here; their bytes equal `produce(discover(ROOT))` for those paths.
  `python -B agent-instructions/skill_entry_points.py` then prints no `would create` and
  exactly 30 `would change` lines, the paths of S5–S7; output kept. `python -B gate/run_tests.py agent-instructions`
  and `python -B gate/run_tests.py gate` fail on the 30 stale entry points until S7 — recorded,
  never suppressed. The report carries the row-to-text table of spec §10: each of rows 5–24, 26
  and 27 against the sentence of the skill or a template that carries it. `git diff --check`.
- **Depends on:** Slice 1 · F1 (WAY-167, WAY-172–WAY-175, WAY-182–WAY-192) · F2

### Slice 5 — Entry points, first batch

- **Goal:** the entry points of `critique`, `define-project`, `find-foundation-entries`,
  `implement-task` and `lead-project`, in both tools, hold the sibling list with
  `maintain-styleguide`, exactly as the generator produces them.
- **Change:** `.claude/skills/the-way-critique/SKILL.md` · `.agents/skills/the-way-critique/SKILL.md`
  `.claude/skills/the-way-define-project/SKILL.md` · `.agents/skills/the-way-define-project/SKILL.md`
  `.claude/skills/the-way-find-foundation-entries/SKILL.md`
  `.agents/skills/the-way-find-foundation-entries/SKILL.md`
  `.claude/skills/the-way-implement-task/SKILL.md` · `.agents/skills/the-way-implement-task/SKILL.md`
  `.claude/skills/the-way-lead-project/SKILL.md` · `.agents/skills/the-way-lead-project/SKILL.md`
- **Read:** `.runs/task-cycles/product-guidelines-styleguide/task.md`
  `agent-instructions/skill_entry_points.py` · `agent-instructions/test_skill_entry_points.py`
  `gate/test_skills_reach_the_way_sessions.py` · `foundations/decisions.md:3774-3831`
  `foundations/invariants.md:2065-2074`
- **Checks:** write the ten paths from `produce(discover(ROOT))` in process, nothing else; each
  pair byte-identical and equal to `produce`. `python -B agent-instructions/skill_entry_points.py`
  prints exactly the 20 `would change` lines of S6 and S7. `python -B gate/run_tests.py agent-instructions`
  and `gate` still fail on those 20 — recorded.
- **Depends on:** Slice 4

### Slice 6 — Entry points, second batch

- **Goal:** the entry points of `maintain-instruction-files`, `plan-project`, `plan-task`,
  `record-decision` and `record-environment-fact`, in both tools, as the generator produces them.
- **Change:** `.claude/skills/the-way-maintain-instruction-files/SKILL.md`
  `.agents/skills/the-way-maintain-instruction-files/SKILL.md`
  `.claude/skills/the-way-plan-project/SKILL.md` · `.agents/skills/the-way-plan-project/SKILL.md`
  `.claude/skills/the-way-plan-task/SKILL.md` · `.agents/skills/the-way-plan-task/SKILL.md`
  `.claude/skills/the-way-record-decision/SKILL.md` · `.agents/skills/the-way-record-decision/SKILL.md`
  `.claude/skills/the-way-record-environment-fact/SKILL.md`
  `.agents/skills/the-way-record-environment-fact/SKILL.md`
- **Read:** `.runs/task-cycles/product-guidelines-styleguide/task.md`
  `agent-instructions/skill_entry_points.py` · `agent-instructions/test_skill_entry_points.py`
  `gate/test_skills_reach_the_way_sessions.py` · `foundations/decisions.md:3774-3831`
  `foundations/invariants.md:2065-2074`
- **Checks:** as Slice 5, for these ten paths; the generator then prints exactly the 10
  `would change` lines of S7.
- **Depends on:** Slice 4 · Slice 5 (order of the batches only; no shared file)

### Slice 7 — Entry points, last batch and the whole inventory

- **Goal:** the entry points of `record-glossary-term`, `record-invariant`, `refine-task`,
  `settle-technology` and `update-part-map`, in both tools, as the generator produces them, and
  every entry point of the-way current.
- **Change:** `.claude/skills/the-way-record-glossary-term/SKILL.md`
  `.agents/skills/the-way-record-glossary-term/SKILL.md`
  `.claude/skills/the-way-record-invariant/SKILL.md` · `.agents/skills/the-way-record-invariant/SKILL.md`
  `.claude/skills/the-way-refine-task/SKILL.md` · `.agents/skills/the-way-refine-task/SKILL.md`
  `.claude/skills/the-way-settle-technology/SKILL.md`
  `.agents/skills/the-way-settle-technology/SKILL.md`
  `.claude/skills/the-way-update-part-map/SKILL.md` · `.agents/skills/the-way-update-part-map/SKILL.md`
- **Read:** `.runs/task-cycles/product-guidelines-styleguide/task.md`
  `agent-instructions/skill_entry_points.py` · `agent-instructions/test_skill_entry_points.py`
  `gate/test_skills_reach_the_way_sessions.py` · `foundations/decisions.md:3774-3831`
  `foundations/invariants.md:2065-2074`
- **Checks:** `python -B agent-instructions/skill_entry_points.py --write`; `git status --short`
  shows only these ten paths changed by it; then `python -B agent-instructions/skill_entry_points.py`
  prints `entry points are current` and no orphan. `python -B gate/run_tests.py agent-instructions`
  and `python -B gate/run_tests.py gate` pass; no stale-entry-point failure is acceptable here.
- **Depends on:** Slices 4, 5 and 6

### Slice 8 — The installer gives products the skill and names the form check

- **Goal:** `installation/install.py` `SKILLS` holds `maintain-styleguide` →
  `product-guidelines/styleguide/SKILL.md`, so a product gets both wrappers and every wrapper's
  sibling list names it; `product_guidance()` gains the one sentence of spec §8 naming both
  form-check commands, run before a merge in which a file of `guidelines/` or `foundations/`
  changed; `installation/README.md` names the skill in its table; a new ordinary test file
  shows both.
- **Change:** `installation/install.py` · `installation/README.md`
  `installation/test_styleguide_installation.py`
- **Read:** `.runs/task-cycles/product-guidelines-styleguide/task.md`
  `.runs/task-cycles/product-guidelines-styleguide/spec.md` · `installation/test_install.py`
  `installation/test_lead_installation.py` · `installation/test_installed_guidance.py`
  `foundations/part_map.md` · `foundations/decisions.md:995-1022`
  `foundations/decisions.md:1114-1142` · `foundations/decisions.md:1370-1394`
  `foundations/decisions.md:3030-3054` · `foundations/decisions.md:3774-3831`
  `foundations/decisions.md:4409-4431` · `foundations/decisions.md:5439-5485`
  `foundations/decisions.md:6035-6057` · `foundations/invariants.md:2095-2104`
- **Checks:** start from a failing test in `installation/test_styleguide_installation.py`
  (preview of an install from the committed checkout lists no `the-way-maintain-styleguide`
  wrapper; the guidance lacks the form-check sentence); then preview, apply and repeat from a
  committed checkout: both wrappers byte-identical, the pinned source path, the sibling sentence,
  the guidance sentence with `python -B .the-way/product-guidelines/form_check.py` and its
  `--merge-onto <main commit>` form, product files preserved. `installation/test_install.py` and
  `installation/test_installed_guidance.py` stay unchanged (they hold tests citing
  `installation-claude-guidance/1`; WAY-03). Run `python -B gate/run_tests.py installation`
  and `python -B gate/run_tests.py gate`. WAY-48: the reviewer checks the changed installer
  against crafted product files as the existing tests do (an existing `AGENTS.md` block, a CRLF
  file), and that no product-chosen path enters the block (WAY-107). Final: the baseline set —
  `python -B gate/run_tests.py <directory>` for `gate`, `elements/decisions`, `elements/invariants`,
  `elements/glossary`, `elements/part-map`, `elements/environment-facts`, `relation-model`,
  `agent-instructions`, `installation`, `instruction-files`, `task-cycle`, `project-level` and
  `product-guidelines`, the five format guards with the no-main options of
  `agent-instructions/README.md`, `python -B agent-instructions/skill_entry_points.py` and
  `git diff --check 96623ed..HEAD` — every exit code and unchecked line kept.
  (`reports/run_checks.py all` also runs `elements/common`, which holds no test and exits 1 at the
  base as well.)
- **Depends on:** Slice 4 (the skill committed) · Slice 3 (the commands it names exist) · Slice 7
  (gate green before the installer's run) · F2 (`installation` *Depends on*)

## Reads that exist only after an earlier slice

The size report measures what exists at `8ea4679`. These reads exist only later; before the slice
is dispatched they are added to its *Read* and
`python -B task-cycle/slice_size.py .runs/task-cycles/product-guidelines-styleguide/plan.md` is
run again. A slice that no longer fits is split before dispatch, never dispatched.

| Read | Written by | Added to |
|---|---|---|
| `product-guidelines/template.md`, `product-guidelines/styleguide/template.md` | S1 | S2, S3, S4 |
| `product-guidelines/form_check.py` (its usage) | S2, S3 | S8 |
| `product-guidelines/styleguide/SKILL.md` (frontmatter) | S4 | S5, S6, S7, S8 |

## Independence and execution

The foundation stages are made. Of the slices, two lines of work are independent once S1 is made:
the form check (S2, then S3, which share both files) and the skill (S4, then its entry-point
batches S5–S7). They change disjoint files, read nothing the other writes, and each can be
reviewed alone: the form check against spec §5 and the F4 checks, the skill against spec §6 and
the row-to-text table. S5 and S6 write disjoint files and could be made side by side; S7 must come
after both, so that its whole `--write` changes only its own ten paths. S8 needs S4's committed
skill and S3's commands.

Possible parallel work: S2–S3 beside S4–S7. Recommendation: none in practice — the adopted
Superpowers 6.4.1 `subagent-driven-development` forbids parallel implementation subagents, so the
slices run one at a time in the order S1 → S2 → S3 → S4 → S5 → S6 → S7 → S8, each by a fresh
executor with a fresh reviewer, then the whole-branch review (root ruling C26). The order keeps
the gate's critical-flow test red only from S4 to S7, and S8 runs on a green gate.

## Coverage

| What the task requires | Slices or entries |
|---|---|
| Outcome (spec §1 Success): a product refines a styleguide task with the skill, takes it through `implement-task`, ends with a styleguide the form check passes, entries carrying its rules and a pointer from its instructions | WAY-167–WAY-192; S1–S4, S8; reached through S5–S7 |
| To do 1 — guidelines outside the foundation, in the agent-directing part, WAY-04 unchanged, "guidelines" | WAY-167; WAY-09 edit; "guidelines"; part `product-guidelines`; S1 |
| To do 2 — guidelines essentialize entries: decision and invariant by identifier, how to apply, good and bad use, values in the tokens file, the rest an example | WAY-168, WAY-171; S1; S2 (carrier checks) |
| To do 3 — form script; references carry fingerprints; a changed entry reported before merge and fixed in the same change | WAY-169, WAY-170; `guidelines-form`, `guidelines-reference-current`, six `guidelines-check-*`; F4; S2, S3; S8 (guidance) |
| To do 4 — a new or changed meaning is a decision on WAY-30's route; using a meaning needs no approval | WAY-172; S1 (§4.3); S4 (§6.2, §7) |
| To do 5 — what the styleguide template carries; values, pairs and components pointed to; product adopts by its own decision | WAY-173, WAY-176–WAY-181, WAY-171; S1; S2 (roles table) |
| To do 6 — every value carries its source, chosen by the skill | WAY-182; S1 (rule); S4 |
| To do 7 — the skill creates and keeps the styleguide of every user interface, recognizes and extends, talks, asks with a recommendation, shows through what the user sees | WAY-183, WAY-185, WAY-174, WAY-172; S4; S5–S7 (entry points); S8 (installer) |
| To do 8 — before the first screen, starting set wider than the first task, preferences or research, announced screens; research again on refresh | WAY-184, WAY-186; S4 |
| To do 9 — two-way audit, 3–5 charges, four categories, the standing question, the agent's way or code with unchecked marked | WAY-187; S4 |
| To do 10 — an invariant for every binding rule; first invariants; companion; WCAG adoption with facts | WAY-188, WAY-189, WAY-190, WAY-191; S1 (rules with *Invariant*); S2 (form requires it); S4 (proposals) |
| To do 11 — instruction file points to the styleguide and forbids hard-coded values | WAY-192; S1 (writing rules for `check_instructions.py`); S4 (§6.6) |
| Questions carried to cycle 1 — part, directory, skill name | WAY-09 edit; part `product-guidelines`; S4 (`maintain-styleguide`) |
| Questions carried to cycle 2 — product path; how an installed product gets the skill | WAY-167; S8 (`SKILLS`, guidance, README's moving the pin) |
| Questions carried to cycle 3 — computing a reference's fingerprint with the standard library | S3 (`relation-model/fingerprint.py`, borrowed parsers) |
| Questions carried to cycle 4 — `instruction-files` on a styleguide named from `AGENTS.md` | S1 (writing rules); S1 and S3 checks with `check_instructions.py`; S4 (§6.6) |
| Questions carried to cycle 5 — role names against "surface", "view", "token" | WAY-176; S1 |
| WAY-100 adoption from `10x-ui` and the Open Mercato skills | WAY-175; S4 |
| Settlement 1 | WAY-167 |
| Settlement 2 | WAY-168 (with WAY-171 for the common form) |
| Settlement 3 | WAY-169; `guidelines-reference-current`; `guidelines-check-stale-reference` |
| Settlement 4 | WAY-170; `guidelines-form`; `guidelines-check-form`, `guidelines-check-code-path` |
| Settlement 5 | WAY-176 |
| Settlement 6 | WAY-176; `guidelines-check-colour-pair` |
| Settlement 7 | WAY-177 |
| Settlement 8 | WAY-178 |
| Settlement 9 | WAY-179 |
| Settlement 10 | WAY-180 |
| Settlement 11 | WAY-181 |
| Settlement 12 | WAY-182 |
| Settlement 13 | WAY-183 |
| Settlement 14 | WAY-185 |
| Settlement 15 | WAY-184 |
| Settlement 16 | WAY-186 |
| Settlement 17 | WAY-187 |
| Settlement 18 | WAY-188; `guidelines-check-carrier` |
| Settlement 19 | WAY-189; `guidelines-check-carrier` |
| Settlement 20 | WAY-190 |
| Settlement 21 | WAY-191 |
| Settlement 22 | WAY-192 |
| Settlement 23 | WAY-174 |
| Settlement 24 | WAY-172 |
| Settlement 25 | glossary term "guidelines" |
| Settlement 26 | WAY-173 |
| Settlement 27 | WAY-172 (approval before code) · WAY-174 (asking with a recommendation) |

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| The six `guidelines-check-*` checks stand in their own file, `product-guidelines/test_form_check_invariants.py`, written in F4; the executors' ordinary tests stand in `product-guidelines/test_form_check.py` | every test in `test_form_check.py` (spec §10's letter) | One more test file. The rejected way makes the executors of S2 and S3 edit a file of invariant tests, which WAY-03 sends back to the foundation step |
| The form check in two slices: form, carriers, parts, paths and the trust boundary (S2), then references and the merge (S3) | one slice for the whole script | S3 may need to reshape what S2 built; the F4 reference tests stay red between S2 and S3, recorded. One slice would join two reviews of a trust-boundary script into one large one |
| The installer's tests in a new file, `installation/test_styleguide_installation.py`; `installation/test_install.py` and its `NAMES` unchanged | `NAMES` gains the skill (spec §8, §10) | `NAMES` stays incomplete, as it already is for `lead-project`; the new file repeats some set-up. The rejected way changes a test citing `installation-claude-guidance/1` (WAY-03), so it would need the foundation step and its assessment |
| S4 writes the skill's own two entry points through the generator's `discover`/`produce`; the other 30 follow in three batches of ten, the last running `--write` | one slice changing 32 files; hand-written entry points | Three more slices and reviews, and the gate's critical-flow test red from S4 to S7. A 32-file slice exceeds the limit of ten files |
| The surface `guidelines-form-check-command` in F2 (made) | no surface (the spec names none) | Products' invariant methods and the installer's guidance name the command, which makes it "something … someone outside the product relies on" (glossary "surface"), as every guard's command is |
| The root `README.md` gains `product-guidelines/` and its skill directory in S4 | the README left as it is (the spec names only `installation/README.md:56`) | One more file in S4. The README describes the repository (WAY-09) and would otherwise omit a directory |
| S1 (templates) before S2 (form check) | form check first | The form check reads the templates' fenced skeleton at run time (C28 (1)), so it cannot pass without them |
| S8 last, after S7 | S8 right after S4 | Later delivery of the installer change; S8 earlier would run its gate check while the critical-flow test is red |
| One end-to-end check on a temporary product (styleguide filled from the template, form check and `check_instructions.py`) split across S1 and S3 | its own slice | A check in a slice that changes no file. The rejected way adds a dispatch for a run |
| S2 and S3 read `reports/check-author.md` and the F4 file, the check's contract (C28 (2)), and no other record of the check author's reasoning | executors given the sentences only | The executors fit the code to the assertions they can see — which C28 makes the contract; the deliberate breaks by the reviewers still test the sentences |
