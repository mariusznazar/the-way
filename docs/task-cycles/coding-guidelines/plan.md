# Plan — Wytyczne produktu: wytyczne kodowania jako druga dyscyplina

- Task: `docs/task-cycles/coding-guidelines/task-frozen.md`
- Spec: `docs/task-cycles/coding-guidelines/spec.md`
- Base: `235b0b4` (`foundations`, Merge pull request #25), branch `claude/gallant-albattani-3k15lc`;
  foundation stages closed at `64344a3` (F1a `a45956f`, F1b `b03c5da`, F2+F3 `05e44b1`, F4 `64344a3`)

The frozen task binds over the reviewed spec; the spec binds where it settles more; the
orchestrator's rulings C1–C21 (`reports/design-rulings.md`) are applied in the spec and bind the
slices that read it. This plan holds no code, no test body and no wording of an entry: it names
entries, files, commands and what each is to do. Rows of *Settlements to record* are "row N"; "F1a"
to "F4" are the foundation stages, "S1" to "S11" the slices.

**Ranges.** Every `foundations/…:<first>-<last>` range below is a whole entry, or a run of whole
entries, at `64344a3`, the commit that closes the foundation stages: heading line to the last line
before the next heading, recomputed there from the entries' headings (ruling C23). WAY-193–WAY-212
stand at `foundations/decisions.md:6460-7262`, the four new invariants at
`foundations/invariants.md:2213-2251`. No slice changes a foundation file, so the ranges hold until
integration. The reads that appear only with an earlier slice stay in the table "Reads that move or
appear with the foundation stages and earlier slices"; the orchestrator adds them before that
slice's dispatch and runs `python -B task-cycle/slice_size.py docs/task-cycles/coding-guidelines/plan.md`
again; a slice that no longer fits is split before dispatch, never dispatched. Each receiving agent
still checks and expands its selection by "Reading the foundation" (WAY-150).

## Foundation entries

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| WAY-167/1 edited in place — `guidelines/coding.md` for the standing checks, the whole product's rules and the table of kind files, each with when to read it; `guidelines/coding-<kind>.md` per kind with an exemplar, `<kind>` from its designating decision; *Verification* level 1 `guidelines-check-kind-index`, level 2 cases (no fingerprinted dependent: none carries `@681d47ff`, checked at `235b0b4`) | decision edit in place (WAY-07: shown for renewed acceptance) | row 1 (written whole, C20); spec §8.1 | S1, S2, S3, S6 |
| WAY-168/1 edited in place — a rule naming an invariant other than one checking the guidelines' own form gives, per named invariant, a good and a bad file at a product path that are cases on which that invariant's method passes and fails, read against the commit's own result for a listed invariant; checked only when the sentence or a case changes; at most three binding sentences; *Verification* level 1 `guidelines-check-example-files` · `gate-guidelines-example-evidence` | decision edit in place (WAY-07) | row 11; spec §8.1; C1, C11, C18, C19 | S1, S4, S5 |
| WAY-171/1, WAY-173/1, WAY-188/1 — relation `@47d9d53e` to WAY-168 read against its new binding part and renewed | relation renewal (WAY-31) | spec §8.1 | S1, S2 |
| WAY-193/1 — template and skill bind a product only through its adopting decision | new decision | row 16 | S2, S6 |
| WAY-194/1 — the skill asks every choice, a recommended one included, by its effect; decisions, not rules; `narrows` WAY-114 | new decision | row 14 | S6 |
| WAY-195/1 — what is taken from Open Mercato and Google's static-analysis lessons and what is left; *Based on* the public sources, each quotation re-read from the public source with path and line or page (spec §8.3; WAY-27, WAY-90) | new decision | row 17; Q16 B, Q18; WAY-100 | S6 |
| WAY-196/1 — every binding coding rule has an invariant (script, or agent with k of n, never a judge of following the exemplar); uncheckable → example; `narrows` WAY-168; level 1 `guidelines-check-carrier` | new decision | row 10 | S1, S2 |
| WAY-197/1 — the guidelines' author writes the bad use, an extra case beside the reviewer's break; the reviewer runs both until a gate does; *Review when* `check by: 2027-03-31` (C7) | new decision | row 12 | S1, S5 |
| WAY-198/1 — a product decision designates the exemplar by path for a kind; what a script checks of it are rules with invariants; the rest is example; level 1 `guidelines-check-exemplar` | new decision | row 2 | S2, S3, S6 |
| WAY-199/1 — another exemplar or a changed checked rule is a decision change; an edit keeping them is none; status beside each path in the kind file; level 1 `guidelines-check-exemplar` | new decision | row 4 (K3 in rationale) | S2, S3, S6 |
| WAY-200/1 — the task creating the first file of a kind designates it; with several, the audit judges every existing file and proposes from their comparison (C13) | new decision | row 3 | S2, S6 |
| WAY-201/1 — the audit ends with a proposed exemplar per kind, one sentence of gain, `do not copy` files with file and line | new decision | row 22 | S6 |
| WAY-202/1 — linter, formatter and dependency audit named in the binding sentence; departure only by a decision with reason; bind from the task writing the coding guidelines; level 1 `guidelines-check-form` | new decision | row 5 | S2, S6 |
| WAY-203/1 — only rules with no report leading to no change worth making block; such a rule is no rule (K1 in rationale; C2 plain words) | new decision | row 7 | S2, S6 |
| WAY-204/1 — split by a trial run judged by an agent that did not write the code; no-code product takes recommended rules (weak point); rationale on one fact per edition (spec §4.4); *Review when* as spec §8.2 | new decision | row 8 | S2, S6 |
| WAY-205/1 — linter: full invariant on the violated list plus the per-file fork-point invariant; formatter: one reformatting | new decision | row 9 | S1, S2, S4, S5, S6 |
| WAY-206/1 — the audit checks the change against `{fork-point}` from the named database read live, from the product's severity; two weak points named, WAY-68 unchanged (C10); *Review when* as spec §8.2 | new decision | row 6 | S2, S6 |
| WAY-207/1 — a fault of one file is fixed in that file; turning a rule off for the product is a decision change | new decision | row 23 | S2, S6 |
| WAY-208/1 — every part holding code gets coding guidelines; the general file names them in *Applies to* | new decision | row 18 | S2, S6 |
| WAY-209/1 — no-code product: general file before the first code; kind file with the first file of the kind; *Review when* as spec §8.2 | new decision | row 19 | S6 |
| WAY-210/1 — the skill looks first at what the product has, extends it, leaves a new tool to the human with the most-used tool as default recommendation (K2) | new decision | row 20 | S6 |
| WAY-211/1 — tools and rule sets from the human's preferences, else research with page and version and critique, again at refresh | new decision | row 21 | S2, S6 |
| WAY-212/1 — one line in root `AGENTS.md`, outside the installer's block, to `guidelines/coding.md` with "before you change code"; kind files through the general file's table; level 1 `guidelines-check-kind-index` | new decision | row 15 | S2, S3, S6 |
| glossary term "exemplar" — definition keeps that a product's decision designates the file for its kind (spec §2, review Minor 11) | glossary term | row 24 | S2, S6 |
| glossary term "standing check" | glossary term | row 25 | S2, S6 |
| glossary term for a report leading to no change worth making — only if the glossary skill's WAY-95 test on the final WAY-203/WAY-204 sentences requires it, listed as new in the request | glossary term, conditional (follows with no way open) | C2 | S2, S6 |
| part `product-guidelines` — two failure modes: a kind file whose exemplar no decision designates (high, detected by `guidelines-check-exemplar`); a blocking rule giving false alarms (high, not detected) | part-map change | spec §8.6; C6 | S3 |
| `guidelines-check-carrier/1` edited in place, version kept — "every such rule of a discipline whose template requires an invariant in every rule"; *Derives from* + WAY-196, WAY-168 renewed. Check: `product-guidelines/test_form_check_invariants.py` (F4). Covered: the form check (S2) | invariant edit in place (pre-`main`; request shows old and new sentence, WAY-57) | spec §8.5; row 10 | S2 |
| `guidelines-check-form/1` — *Derives from* gains WAY-202; sentence unchanged. Check: F4 file. Covered: S2 | invariant link change | spec §8.5 | S2 |
| `guidelines-check-kind-index/1` — derives from WAY-167, WAY-212; method `python -B gate/run_tests.py product-guidelines --record .runs/product-guidelines-tests.jsonl`; *Part* as the other `guidelines-check-*`. Check: F4 file. Covered: S3 | new invariant | spec §5.2 item 3, §8.5; rows 1, 15 | S3 |
| `guidelines-check-exemplar/1` — derives from WAY-198, WAY-199; method and *Part* as above. Check: F4 file. Covered: S3 | new invariant | spec §5.2 item 4, §8.5; rows 2, 4 | S3 |
| `guidelines-check-example-files/1` — derives from WAY-168; method and *Part* as above; a pair per named invariant, the exemption, the fence rule, the malformed test case. Check: F4 file. Covered: S4 | new invariant | spec §5.2 item 5, §8.5; row 11 | S1, S4 |
| `gate-guidelines-example-evidence/1` — derives from WAY-168; *Part* `gate · product-guidelines`; method `TODO` until a gate can (Q12). No check and no covered code in this task | new invariant | row 13; spec §8.5 | S5 |
| `product-guidelines/test_form_check_invariants.py` — the §9 cases; the valid styleguide fixture gains a good/bad pair for each rule naming an invariant other than `guidelines-form` | invariant tests (WAY-03, assessed under WAY-10) | spec §9 | S2, S3, S4 |
| `installation/test_install.py` — `NAMES` gains `("product-guidelines/coding/SKILL.md", "maintain-coding-guidelines")`; it holds tests citing `installation-claude-guidance/1`, so the change is an invariant-test change (WAY-03, WAY-65) | invariant tests | spec §6.6 | S11 |

Unchanged on purpose (spec §3.1, §8.1, §8.5): WAY-09, WAY-114, WAY-192, `guidelines-form/1`,
`guidelines-reference-current/1`, `invariant-test-break/1`, `gate-fork-point-evidence/1`. No
environment fact of the-way (spec §8.7). No projected entry: the task is independent.

### Foundation stages

All four run before S1, on the task branch, through the pinned element skills, each with a search
of the whole foundation (WAY-33) and its guards. Authors: F1a, F1b and the F2–F3 sentence author
write no check and no covered code; the F4 check author is neither the sentence author nor an
executor of S2, S3, S4 or S11 (WAY-69); each slice executor is a fresh agent.

- **F1a** — `the-way-record-decision`: WAY-167 and WAY-168 in place, the renewals of WAY-171,
  WAY-173, WAY-188, and WAY-193–WAY-202 with WAY-195's public sources re-read. Reachability
  checked by the planner on 2026-10-18 (HTTP status only, nothing quoted):
  `https://raw.githubusercontent.com/open-mercato/open-mercato/4374c48def1654927805c4b760f0e7f8648280f2/AGENTS.md`
  200; the paper's public copy linked from
  `https://research.google/pubs/lessons-from-building-static-analysis-tools-at-google/`,
  `https://storage.googleapis.com/gweb-research2023-media/pubtools/4365.pdf`, 200; `cacm.acm.org`
  and `dl.acm.org` 403. Where the author cannot read a quoted passage, it stops and asks through
  the orchestrator (spec §8.3).
- **F1b** — `the-way-record-decision`: WAY-203–WAY-212. Split from F1a because reading the whole
  log (431 463 characters at `235b0b4`) with the task, the spec and the skill comes to about
  227 000 estimated tokens of the 250 000 the size script allows; two dispatches keep each
  author's reading and its WAY-33 search apart.
- **F2** — `the-way-record-glossary-term` on the final sentences of F1a and F1b: "exemplar",
  "standing check", and the conditional term of C2; `the-way-update-part-map`: the two failure
  modes.
- **F3** — `the-way-record-invariant`, by the sentence author (may be F2's agent): the carrier
  edit, the check-form link, the four new invariants, each decision's level 1 identifier standing
  in that invariant's *Derives from* (`verification-invariant-derivation`).
- **F4** — the check author, given the F3 sentences and methods and the forms the checks read —
  spec §4.1, §4.2 (the two fenced forms and their verbatim headings and columns) and §5.1 — never
  §5.2 or any slice's reasoning: the §9 tests in `product-guidelines/test_form_check_invariants.py`
  and `NAMES` in `installation/test_install.py`. Its run is recorded RED for every new coding,
  index, exemplar and test-case test and for `NAMES`, each by name; the tests that passed at the base
  keep passing. Both files are read-only for every slice (WAY-03); a slice that needs either
  changed returns to the foundation step. Their line and message assertions are the contract S2,
  S3, S4 and S11 meet.

Checks of the stages, each with exit code and full output kept:
`python -B elements/decisions/format_guard.py foundations/decisions.md --base none --merge-onto none`,
`python -B elements/invariants/format_guard.py foundations/invariants.md --base none --merge-onto none`,
`python -B elements/glossary/format_guard.py foundations/glossary.md --base none --merge-onto none`,
`python -B elements/part-map/format_guard.py foundations/part_map.md --base none`,
`python -B gate/run_tests.py elements/decisions` and the same for `elements/invariants`,
`elements/glossary`, `elements/part-map`, `relation-model`, `gate`; after F4,
`python -B gate/run_tests.py product-guidelines` and `python -B gate/run_tests.py installation`
(expected RED as above). Expected until F3: the decisions guard reports the level 1 identifiers of
WAY-167, WAY-168, WAY-196, WAY-198, WAY-199, WAY-202, WAY-212 as missing invariants; rerun after F3.

Deliberate breaks (WAY-69), each written from the final sentence by the reviewer of the covering
slice, who wrote neither the check nor the code: S2's reviewer for `guidelines-check-form` (coding
cases) and `guidelines-check-carrier`; S3's for `guidelines-check-kind-index` and
`guidelines-check-exemplar`; S4's for `guidelines-check-example-files`; S11's for the changed
`NAMES` test of `installation-claude-guidance` (the new `SKILLS` entry removed). Code is restored
and the checks rerun clean.

## Slices

### Slice 1 — The common template names the coding files and gives test cases

- **Goal:** `product-guidelines/template.md` gives, each rule citing the decision that sets it
  (WAY-171): "Where guidelines go" with `guidelines/coding.md` and `guidelines/coding-<kind>.md` and
  the general file's table of kind files as WAY-167 now gives them; *Good* and *Bad* that describe a
  use in one line, the field names and the fenced required form otherwise unchanged so the form
  check reads it as before; the rule on test cases of spec §5.1 citing WAY-168 — one
  `good <identifier> <path>` and one `bad <identifier> <path>` block per invariant the rule names
  other than `guidelines-form`, after the four fields, each the whole text of a file at a product
  path, the relative reading for a listed invariant and the strict reading for its per-file
  companion (C19), every fenced block of such a rule a test case, illustration under `## Examples`,
  short files at paths that may not exist, the path limits and the 1 MiB limit, the three-backtick
  outer fence and no fence-opening line inside, the bare-fence consequence (C21), the exemption of
  a rule whose *Invariant* is `guidelines-form` (C11), every discipline (C1); "A discipline's
  template may require an invariant in every rule" names coding beside the styleguide (WAY-196);
  the note on `check_instructions.py` says the cases' paths and texts stay in fenced code. No value.
- **Change:** `product-guidelines/template.md`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `docs/task-cycles/coding-guidelines/spec.md`
  `docs/task-cycles/coding-guidelines/reports/design-rulings.md`
  `product-guidelines/styleguide/template.md` · `instruction-files/check_instructions.py`
  `product-guidelines/form_check.py:262-433` · `foundations/glossary.md`
  `foundations/decisions.md:1440-1474` · `foundations/decisions.md:1745-1797`
  `foundations/decisions.md:1972-2006` · `foundations/decisions.md:5439-5715`
  `foundations/decisions.md:6286-6315` · `foundations/decisions.md:6352-6386`
  `foundations/decisions.md:6633-6713` · `foundations/decisions.md:6974-7015`
  `foundations/invariants.md:2133-2251`
- **Checks:** text, no behaviour; no test of its own. `python -B gate/run_tests.py product-guidelines`:
  the same tests pass and fail as after F4 (the required form still parses), compared by name;
  `python -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` exits 0 with
  `pass` for `guidelines-form/1` on the-way. On a temporary git repository whose root `AGENTS.md`
  names in backticks a `guidelines/testing.md` holding one rule with a good/bad pair written as the
  template gives (info strings on opening fences, a path with `/`, an `@` inside a case),
  `python -B instruction-files/check_instructions.py <temporary repository>` reports no `error`, no
  dead path and no import — the check of the C12 assumption the design left unverified; output
  kept. `python -B gate/run_tests.py gate`. `git diff --check`. Manual, in the report: each bullet
  of spec §5.1 present; each rule names its decision; no glossary *Avoid* word.
- **Depends on:** F1a (WAY-167, WAY-168, WAY-196, WAY-197) · F1b (WAY-205) · F2 · F3
  (`guidelines-check-example-files`) · F4

### Slice 2 — The coding template, and the form check reads its two forms

- **Goal:** `product-guidelines/coding/template.md` holds spec §4 — its opening (WAY-193, WAY-171),
  `## Required form` and `## Required form of a kind` with the fenced forms of §4.1 and §4.2, their
  headings, columns and the *Status* list verbatim as the F4 fixtures use them, the sentence "its
  *Invariant* names at least one invariant" in each form section, what each section carries
  (§4.3, with C3, C4, C5, C13, C14 and the standing checks' test cases of C12, C18, C19), the rules
  for the tools (§4.4) and "Writing the files" (§4.5), each rule citing its decision, no value, no
  tool named as the-way's choice. `product-guidelines/form_check.py` does items 1, 2 and 6 of spec
  §5.2: an optional second form per discipline; `<discipline>-<kind>.md` names agreeing with
  *Discipline* `coding` and the names §5.2 item 1 refuses; `requires_invariant` read from each form
  section; role checks only on a table whose columns are the roles', every other table checked for
  its header and number of cells; the coding template's structural words read back from it,
  `TemplateError` where one is missing; its docstring lists the new findings, each an error of
  `guidelines-form/1`; the command, options and exit codes unchanged. `product-guidelines/test_form_check.py`:
  the fixtures using `coding` as a discipline with no template (`:142-145`, `:264-277`, `:288`,
  `:364`) move to `observability`; ordinary tests of §5.3 bullets 2 and 3 and of the template words.
  The F4 coding tests of `guidelines-check-form/1` and `guidelines-check-carrier/1` pass.
- **Change:** `product-guidelines/coding/template.md` · `product-guidelines/form_check.py`
  `product-guidelines/test_form_check.py`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `docs/task-cycles/coding-guidelines/spec.md`
  `docs/task-cycles/coding-guidelines/reports/design-rulings.md`
  `docs/task-cycles/coding-guidelines/reports/f4-check.md`
  `product-guidelines/template.md` · `product-guidelines/styleguide/template.md`
  `product-guidelines/test_form_check_invariants.py` · `elements/common/guard_shared.py`
  `foundations/part_map.md` · `foundations/glossary.md`
  `foundations/decisions.md:492-517` · `foundations/decisions.md:1114-1142`
  `foundations/decisions.md:1370-1394` · `foundations/decisions.md:1440-1474`
  `foundations/decisions.md:1709-1828` · `foundations/decisions.md:1972-2006`
  `foundations/decisions.md:2072-2167` · `foundations/decisions.md:2454-2486`
  `foundations/decisions.md:4011-4044` · `foundations/decisions.md:4315-4352`
  `foundations/decisions.md:5439-5921` · `foundations/decisions.md:6286-6386`
  `foundations/decisions.md:6460-7262` · `foundations/invariants.md:547-575`
  `foundations/invariants.md:1497-1525` · `foundations/invariants.md:2133-2251`
- **Checks:** The F4 RED list, by test name, is in `docs/task-cycles/coding-guidelines/reports/f4-check.md`; *File* cells of `## Kinds of code` and `## Files of this kind` hold paths in backticks, as spec §4.3 gives and the F4 fixtures write them (C32). Then: start from the F4 coding tests of `guidelines-check-form/1` and
  `guidelines-check-carrier/1`, RED at F4, and from a failing ordinary test (a
  `guidelines/coding-endpoint.md` named by the second form is refused). Ordinary tests: kind names
  `coding-.md`, `coding--a.md`, `coding-A.md`, `coding-a/b.md` (warned, not read), `coding-a.md.md`,
  `Coding-a.md`; a table row with `|` inside backticks, too few or too many cells, a separator row
  in the middle, a header off by one space; `read_templates` on a temporary copy of the templates
  missing each structural word raises `TemplateError`, and the command exits 2; the moved
  `observability` fixtures pass as before. Run `python -B gate/run_tests.py product-guidelines`
  (the F4 tests of kind-index, exemplar and test cases still RED, by name);
  `python -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` (exit 0, `pass`);
  `python -B product-guidelines/form_check.py --merge-onto none --record .runs/guidelines-reference.jsonl`
  (exit 0; merge `unchecked`); `python -B elements/part-map/format_guard.py foundations/part_map.md --base none`
  (`product-guidelines/coding/template.md` claimed by `product-guidelines`);
  `python -B gate/run_tests.py installation` after the commit (the styleguide installation test
  runs the form check of the committed `HEAD`; `NAMES` RED until S11); `python -B gate/run_tests.py gate`.
  WAY-48: the reviewer checks the crafted names and rows against §5.3 and that no new regular
  expression has nested repetition. Manual: every `### ` heading and column of §4.1–§4.2 verbatim.
- **Depends on:** Slice 1 · F1a (WAY-167, WAY-193, WAY-196, WAY-198–WAY-202) · F1b (WAY-203–WAY-208,
  WAY-211, WAY-212) · F2 · F3 (carrier, check-form) · F4

### Slice 3 — The form check: the index of kinds and the files of a kind

- **Goal:** `product-guidelines/form_check.py` does items 3 and 4 of spec §5.2: every
  `guidelines/coding-<kind>.md` git lists named by a row of `## Kinds of code` whose *File* is that
  path, every row naming a kind file git lists, a kind file with no `guidelines/coding.md` an error;
  in `## Files of this kind` exactly one `exemplar` row, every *Status* on the closed list, every
  *File* passing `refused()` and naming something git tracks (from the one list git gives), the
  exemplar row's *Decision* a decision of the log whose binding sentences hold `` `<path>` `` and
  `` `<kind>` `` after whitespace is collapsed, `—` on the other rows, its fingerprint checked as every
  reference is; no completeness asked (C13); `Foundation` keeps each decision's binding text; each
  finding an error of `guidelines-form/1`; docstring updated. The F4 tests of
  `guidelines-check-kind-index/1` and `guidelines-check-exemplar/1` pass.
- **Change:** `product-guidelines/form_check.py` · `product-guidelines/test_form_check.py`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `docs/task-cycles/coding-guidelines/spec.md`
  `docs/task-cycles/coding-guidelines/reports/design-rulings.md`
  `docs/task-cycles/coding-guidelines/reports/f4-check.md`
  `product-guidelines/template.md` · `product-guidelines/test_form_check_invariants.py`
  `elements/common/guard_shared.py` · `relation-model/fingerprint.py`
  `elements/decisions/format_guard.py:216-298` · `elements/decisions/format_guard.py:878-883`
  `foundations/decisions.md:38-69` · `foundations/decisions.md:1114-1142`
  `foundations/decisions.md:1370-1394` · `foundations/decisions.md:5439-5758`
  `foundations/decisions.md:6715-6815` · `foundations/decisions.md:7223-7262`
  `foundations/invariants.md:547-575` · `foundations/invariants.md:2133-2251`
- **Checks:** The F4 RED list, by test name, is in `docs/task-cycles/coding-guidelines/reports/f4-check.md`; *File* cells of `## Kinds of code` and `## Files of this kind` hold paths in backticks, as spec §4.3 gives and the F4 fixtures write them (C32). Then: start from the F4 tests of kind-index and exemplar, RED, and a failing ordinary test
  (a kind file missing from the index passes). Ordinary tests of spec §5.3: a *File* or index *File*
  absolute, UNC, holding `..`, `\`, `:`, a drive, a character not printable, a pathspec magic word,
  200 KiB long — refused before git sees it (the git calls captured), no socket opened, within a
  time bound; an index row differing from a file only by case or by a Unicode look-alike; two
  `exemplar` rows, none; a decision holding the path only outside backticks, `` `src/a.ts` `` where the
  row says `src/a.tsx`, a number with another log's prefix, a repealed decision; a line of 1 MiB of
  `|` or backticks. Run `python -B gate/run_tests.py product-guidelines` (test-case tests still RED,
  by name); both form-check runs of S2; `python -B gate/run_tests.py elements/decisions`,
  `relation-model`, `gate`. WAY-48: the reviewer checks those inputs and the bound on matching.
- **Depends on:** Slice 2 · F1a (WAY-167, WAY-198, WAY-199) · F1b (WAY-212) · F3 (kind-index,
  exemplar) · F4

### Slice 4 — The form check: test cases, and a filled product end to end

- **Goal:** `product-guidelines/form_check.py` does item 5 of spec §5.2: in every kept rule whose
  *Invariant* names an invariant other than `guidelines-form`, one `good <identifier> <path>` and one
  `bad <identifier> <path>` block per such invariant after the fields, each path passing `refused()`;
  a block naming an invariant the rule does not name is an error; the info string read only from an
  opening fence; a line inside a case that would open a fence is an error at that line; any other
  fenced block of such a rule's body a malformed test case at its opening line, a case left open an
  error at its opening line (C21); a rule naming only `guidelines-form` needs no blocks; no case path
  opened, given to git or written; each finding an error of `guidelines-form/1`; docstring updated.
  The F4 tests of `guidelines-check-example-files/1` pass, and with them the whole
  `product-guidelines` run.
- **Change:** `product-guidelines/form_check.py` · `product-guidelines/test_form_check.py`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `docs/task-cycles/coding-guidelines/spec.md`
  `docs/task-cycles/coding-guidelines/reports/design-rulings.md`
  `docs/task-cycles/coding-guidelines/reports/f4-check.md`
  `product-guidelines/template.md` · `product-guidelines/test_form_check_invariants.py`
  `elements/common/guard_shared.py` · `instruction-files/check_instructions.py`
  `foundations/part_map.md` · `foundations/decisions.md:1114-1142`
  `foundations/decisions.md:1370-1394` · `foundations/decisions.md:1440-1474`
  `foundations/decisions.md:1745-1797` · `foundations/decisions.md:1972-2006`
  `foundations/decisions.md:5439-5715` · `foundations/decisions.md:6352-6386`
  `foundations/decisions.md:6674-6713` · `foundations/decisions.md:6974-7015`
  `foundations/invariants.md:547-575` · `foundations/invariants.md:2133-2251`
- **Checks:** The F4 RED list, by test name, is in `docs/task-cycles/coding-guidelines/reports/f4-check.md`; *File* cells of `## Kinds of code` and `## Files of this kind` hold paths in backticks, as spec §4.3 gives and the F4 fixtures write them (C32). Then: start from the F4 test-case tests, RED, and a failing ordinary test (a rule naming an
  invariant with no blocks passes). Ordinary tests of spec §5.3 bullets 4, 5 and 7 with the expected
  reports C21 gives: a fence left open to the end, a tilde fence, a fence of four backticks closing
  three, a fence-opening line inside a case, `good` with no identifier or path,
  `good x  a.ts b.ts`, `GOOD x a.ts`, a block naming an invariant the rule does not name, a rule
  naming two invariants with a pair for one only, a 1 MiB info string, an info string on a closing
  fence, a bare three-backtick line inside a `good` case (malformed case at the former closing
  fence), a rule naming `guidelines-form` with and without blocks and with another invariant, a
  test-case path refused as in S3, a file just over 1048576 bytes refused unread; no case path
  reaches git or is opened. End to end: on a temporary product with a part map, decisions (one
  designating an exemplar by path and kind) and invariants, a `guidelines/coding.md` and a
  `guidelines/coding-endpoint.md` filled from the coding template, with a pair per named invariant,
  pass `python -B <the-way>/product-guidelines/form_check.py --record …` and `--merge-onto none`,
  and `python -B instruction-files/check_instructions.py <product>` with a root `AGENTS.md` naming
  `guidelines/coding.md` reports no `error`, dead path or import; outputs kept. Run
  `python -B gate/run_tests.py product-guidelines` (all pass); both form-check runs on the-way;
  `python -B gate/run_tests.py gate`. WAY-48: the reviewer checks the inputs above.
- **Depends on:** Slice 3 · Slice 1 · F1a (WAY-168, WAY-197) · F1b (WAY-205) · F3
  (`guidelines-check-example-files`) · F4

### Slice 5 — The task cycle: the reviewer runs the test cases

- **Goal:** `task-cycle/skill/SKILL.md` holds, at the code reviewer's deliberate break in step 10
  and at step 11's for return-step checks, the one sentence of spec §7 (C8, C18, C19): for an
  invariant a rule of the product's guidelines names with test cases, whose sentence the change adds
  or alters or one of whose cases it rewrites, the reviewer also runs the check in a scratch
  worktree of the commit with that invariant's good file and with its bad file in place, records
  that it passes and fails there — relatively for a listed invariant, strictly for its per-file
  companion — and does not accept the check otherwise; the bad file is a case beside the break,
  never the break; cases are applied only in the scratch worktree. Nothing else changes; the
  frontmatter stays as it is.
- **Change:** `task-cycle/skill/SKILL.md`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `docs/task-cycles/coding-guidelines/spec.md`
  `docs/task-cycles/coding-guidelines/reports/design-rulings.md`
  `product-guidelines/template.md` · `foundations/decisions.md:203-232`
  `foundations/decisions.md:1440-1474` · `foundations/decisions.md:1972-2006`
  `foundations/decisions.md:3665-3725` · `foundations/decisions.md:4723-4763`
  `foundations/decisions.md:5510-5578` · `foundations/decisions.md:6352-6386`
  `foundations/decisions.md:6674-6713` · `foundations/decisions.md:6974-7015`
  `foundations/invariants.md:136-144` · `foundations/invariants.md:1107-1115`
  `foundations/invariants.md:2243-2251`
- **Checks:** process prose; no test asserts it. `git diff --stat` shows this file alone, its
  frontmatter untouched; `python -B agent-instructions/skill_entry_points.py` prints
  `entry points are current` (no description changed); `python -B gate/run_tests.py task-cycle`
  and `python -B gate/run_tests.py gate` pass. Manual, in the report: the sentence in step 10 and
  in step 11, each element of spec §7 present, no review against guidelines added (Q5).
- **Depends on:** Slice 1 · F1a (WAY-168, WAY-197) · F1b (WAY-205) · F3
  (`gate-guidelines-example-evidence`)

### Slice 6 — The skill `maintain-coding-guidelines` and its entry points

- **Goal:** `product-guidelines/coding/SKILL.md` holds spec §6.1–§6.5: frontmatter
  `name: maintain-coding-guidelines` and a one-line, safe plain YAML description starting "Use
  when"; where the-way lies, `the-way-` names, no Superpowers method, the order of the work only and
  no rule restated; steps 0–5, orchestrated mode, what reaches the task document, writing only
  under `.runs/coding/`; it follows WAY-193–WAY-212 and describes what it takes from outside sources
  without naming them (WAY-27). Its two entry points exist exactly as the generator produces them.
  The root `README.md` names `product-guidelines/coding/` beside the styleguide's directory in its
  list of directories and of skill directories.
- **Change:** `product-guidelines/coding/SKILL.md`
  `.claude/skills/the-way-maintain-coding-guidelines/SKILL.md`
  `.agents/skills/the-way-maintain-coding-guidelines/SKILL.md` · `README.md`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `docs/task-cycles/coding-guidelines/spec.md`
  `docs/task-cycles/coding-guidelines/reports/design-rulings.md`
  `product-guidelines/styleguide/SKILL.md` · `product-guidelines/template.md`
  `project-level/task/skill/SKILL.md` · `project-level/task/template.md`
  `project-level/technology/SKILL.md` · `elements/common/way_of_working.md`
  `elements/common/critique/SKILL.md` · `instruction-files/SKILL.md`
  `agent-instructions/skill_entry_points.py` · `installation/README.md`
  `foundations/glossary.md` · `foundations/part_map.md`
  `foundations/decisions.md:775-804` · `foundations/decisions.md:838-867`
  `foundations/decisions.md:1024-1056` · `foundations/decisions.md:3193-3256`
  `foundations/decisions.md:3407-3437` · `foundations/decisions.md:3517-3613`
  `foundations/decisions.md:3665-3725` · `foundations/decisions.md:3774-3899`
  `foundations/decisions.md:4765-4801` · `foundations/decisions.md:5439-7262`
- **Checks:** process prose, no test asserts it. The two entry points are written with the
  generator's own `discover` and `produce`, in process, for these two paths only — never by hand,
  never by `--write`; their bytes equal `produce(discover(ROOT))` for those paths.
  `python -B agent-instructions/skill_entry_points.py` then prints no `would create` and exactly 32
  `would change` lines, the paths of S7–S10; output kept. `python -B gate/run_tests.py agent-instructions`
  and `python -B gate/run_tests.py gate` fail on the 32 stale entry points until S10 — recorded by
  test name, never suppressed. `python -B elements/part-map/format_guard.py foundations/part_map.md --base none`
  (the new files claimed). The report carries a table of rows 2, 3, 5, 8, 14, 18–22 and *To do* 2,
  3, 4, 7 against the sentence of the skill or of the coding template that carries each.
  `git diff --check`.
- **Depends on:** Slice 2 · Slice 1 · F1a (WAY-167, WAY-193–WAY-202) · F1b (WAY-203–WAY-212) · F2

### Slice 7 — Entry points, first batch

- **Goal:** the entry points of `critique`, `define-project`, `find-foundation-entries` and
  `implement-task`, in both tools, hold the sibling list with `maintain-coding-guidelines`, exactly
  as the generator produces them.
- **Change:** `.claude/skills/the-way-critique/SKILL.md` · `.agents/skills/the-way-critique/SKILL.md`
  `.claude/skills/the-way-define-project/SKILL.md` · `.agents/skills/the-way-define-project/SKILL.md`
  `.claude/skills/the-way-find-foundation-entries/SKILL.md`
  `.agents/skills/the-way-find-foundation-entries/SKILL.md`
  `.claude/skills/the-way-implement-task/SKILL.md` · `.agents/skills/the-way-implement-task/SKILL.md`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `agent-instructions/skill_entry_points.py` · `agent-instructions/test_skill_entry_points.py`
  `gate/test_skills_reach_the_way_sessions.py` · `foundations/decisions.md:3774-3831`
  `foundations/invariants.md:2065-2073`
- **Checks:** the eight paths written from `produce(discover(ROOT))` in process, nothing else; each
  pair byte-identical and equal to `produce`. `python -B agent-instructions/skill_entry_points.py`
  prints exactly the 24 `would change` lines of S8–S10. `python -B gate/run_tests.py agent-instructions`
  and `gate` still fail on those 24 — recorded.
- **Depends on:** Slice 6 · Slice 5 (`implement-task`'s skill file is final)

### Slice 8 — Entry points, second batch

- **Goal:** the entry points of `lead-project`, `maintain-instruction-files`, `maintain-styleguide`
  and `plan-project`, in both tools, as the generator produces them.
- **Change:** `.claude/skills/the-way-lead-project/SKILL.md` · `.agents/skills/the-way-lead-project/SKILL.md`
  `.claude/skills/the-way-maintain-instruction-files/SKILL.md`
  `.agents/skills/the-way-maintain-instruction-files/SKILL.md`
  `.claude/skills/the-way-maintain-styleguide/SKILL.md`
  `.agents/skills/the-way-maintain-styleguide/SKILL.md`
  `.claude/skills/the-way-plan-project/SKILL.md` · `.agents/skills/the-way-plan-project/SKILL.md`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `agent-instructions/skill_entry_points.py` · `agent-instructions/test_skill_entry_points.py`
  `gate/test_skills_reach_the_way_sessions.py` · `foundations/decisions.md:3774-3831`
  `foundations/invariants.md:2065-2073`
- **Checks:** as Slice 7, for these eight paths; the generator then prints exactly the 16
  `would change` lines of S9 and S10.
- **Depends on:** Slice 6 · Slice 7 (order of the batches only; no shared file)

### Slice 9 — Entry points, third batch

- **Goal:** the entry points of `plan-task`, `record-decision`, `record-environment-fact` and
  `record-glossary-term`, in both tools, as the generator produces them.
- **Change:** `.claude/skills/the-way-plan-task/SKILL.md` · `.agents/skills/the-way-plan-task/SKILL.md`
  `.claude/skills/the-way-record-decision/SKILL.md` · `.agents/skills/the-way-record-decision/SKILL.md`
  `.claude/skills/the-way-record-environment-fact/SKILL.md`
  `.agents/skills/the-way-record-environment-fact/SKILL.md`
  `.claude/skills/the-way-record-glossary-term/SKILL.md`
  `.agents/skills/the-way-record-glossary-term/SKILL.md`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `agent-instructions/skill_entry_points.py` · `agent-instructions/test_skill_entry_points.py`
  `gate/test_skills_reach_the_way_sessions.py` · `foundations/decisions.md:3774-3831`
  `foundations/invariants.md:2065-2073`
- **Checks:** as Slice 7, for these eight paths; the generator then prints exactly the 8
  `would change` lines of S10.
- **Depends on:** Slice 6 · Slice 8 (order of the batches only; no shared file)

### Slice 10 — Entry points, last batch and the whole inventory

- **Goal:** the entry points of `record-invariant`, `refine-task`, `settle-technology` and
  `update-part-map`, in both tools, as the generator produces them, and every entry point of
  the-way current.
- **Change:** `.claude/skills/the-way-record-invariant/SKILL.md`
  `.agents/skills/the-way-record-invariant/SKILL.md`
  `.claude/skills/the-way-refine-task/SKILL.md` · `.agents/skills/the-way-refine-task/SKILL.md`
  `.claude/skills/the-way-settle-technology/SKILL.md`
  `.agents/skills/the-way-settle-technology/SKILL.md`
  `.claude/skills/the-way-update-part-map/SKILL.md` · `.agents/skills/the-way-update-part-map/SKILL.md`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `agent-instructions/skill_entry_points.py` · `agent-instructions/test_skill_entry_points.py`
  `gate/test_skills_reach_the_way_sessions.py` · `foundations/decisions.md:3774-3831`
  `foundations/invariants.md:2065-2073`
- **Checks:** `python -B agent-instructions/skill_entry_points.py --write`; `git status --short`
  shows only these eight paths changed by it; then `python -B agent-instructions/skill_entry_points.py`
  prints `entry points are current` and no orphan. `python -B gate/run_tests.py agent-instructions`
  and `python -B gate/run_tests.py gate` pass; no stale-entry-point failure is acceptable here.
- **Depends on:** Slices 6, 7, 8 and 9

### Slice 11 — The installer gives products the skill

- **Goal:** `installation/install.py` `SKILLS` holds `"maintain-coding-guidelines":
  "product-guidelines/coding/SKILL.md"`, so a product gets both wrappers, every wrapper's sibling
  list and the `AGENTS.md` block name it, and no other text of the installer changes (the
  `installation-command` surface keeps its wording); `installation/README.md` names the skill in
  its table of installed files and in its list of what the tests check; a new ordinary test file,
  `installation/test_coding_guidelines_installation.py`, on the pattern of
  `installation/test_styleguide_installation.py`, shows the install and the refusals. The F4
  `NAMES` test passes.
- **Change:** `installation/install.py` · `installation/README.md`
  `installation/test_coding_guidelines_installation.py`
- **Read:** `docs/task-cycles/coding-guidelines/task-frozen.md`
  `docs/task-cycles/coding-guidelines/spec.md` · `installation/test_install.py`
  `installation/test_styleguide_installation.py` · `installation/test_installed_guidance.py`
  `foundations/part_map.md` · `foundations/decisions.md:995-1022`
  `foundations/decisions.md:1114-1142` · `foundations/decisions.md:1370-1394`
  `foundations/decisions.md:3030-3054` · `foundations/decisions.md:3774-3831`
  `foundations/decisions.md:4409-4431` · `foundations/decisions.md:5439-5508`
  `foundations/invariants.md:2065-2073` · `foundations/invariants.md:2095-2103`
- **Checks:** start from a failing test in the new file (a preview from the committed checkout lists
  no `the-way-maintain-coding-guidelines` wrapper) and the F4 `NAMES` test, RED. Then preview, apply
  and repeat from a committed checkout: both wrappers byte-identical, the pinned source path, the
  sibling sentence, the block naming `the-way-maintain-coding-guidelines`, product files preserved.
  WAY-48, crafted input: a conflicting file at the new wrapper's path in `.claude/skills/` and in
  `.agents/skills/`, a directory there, a non-UTF-8 file there — each stops the run before anything
  is written. Run `python -B gate/run_tests.py installation` (all pass) and
  `python -B gate/run_tests.py gate`. Final, by the executor, every exit code and unchecked line
  kept: `python -B gate/run_tests.py <directory>` for `gate`, `elements/decisions`,
  `elements/invariants`, `elements/glossary`, `elements/part-map`, `elements/environment-facts`,
  `relation-model`, `agent-instructions`, `installation`, `instruction-files` (3 platform failures
  expected, as at the base), `task-cycle`, `project-level`, `product-guidelines`; the five format
  guards with `--base none` and, where available, `--merge-onto none`; both form-check runs on
  the-way; `python -B agent-instructions/skill_entry_points.py`; `git diff --check 235b0b4..HEAD`.
- **Depends on:** Slice 6 (the skill committed) · Slice 10 (gate green) · F4 (`NAMES`)

## Reads that move or appear with the foundation stages and earlier slices

The size report measures what exists at `64344a3`: the foundation entries and F4's test files are
in the *Read* fields above, at their ranges there. These reads appear only with an earlier slice;
before the slice is dispatched the orchestrator adds them to its *Read* and runs the script again.

| Read | Written by | Added to |
|---|---|---|
| `product-guidelines/template.md` as S1 leaves it | S1 | S2, S3, S4, S5, S6 (already named; measured at `64344a3`) |
| `product-guidelines/coding/template.md` | S2 | S3, S4, S6 |
| `product-guidelines/coding/SKILL.md` (frontmatter) | S6 | S7, S8, S9, S10, S11 |

Margin, estimated until the files exist: S1's growth of the common template about 2 000 estimated
tokens; the coding template (spec §4) at most 25 000 characters, 10 000 tokens;
`product-guidelines/coding/SKILL.md` about 7 000 tokens. Added to the sizes of `plan-size.md`,
every slice stays under the limit of 250 000; the figures stand in `plan-size.md` and in the
planner's report. If a re-measured S2 exceeds the limit, its foundation ranges are narrowed first
(WAY-73–WAY-76 and WAY-139 are context, not inputs of its code), and only then is the template
split from the code into a slice of its own, which the moved fixtures then join.

## Independence and execution

The foundation stages come first and in order (F1a → F1b → F2 → F3 → F4): each needs the
fingerprints or sentences of the one before. Of the slices, after S1:

- **The form check** — S2 → S3 → S4 share `product-guidelines/form_check.py` and
  `product-guidelines/test_form_check.py`, so they are one line; each is reviewable alone against
  its items of spec §5.2 and its F4 tests.
- **The task cycle** — S5 changes only `task-cycle/skill/SKILL.md`, reads only S1's rule and the
  foundation, and is reviewable alone against spec §7; it could run beside S2–S4.
- **The skill** — S6 needs S2's template; then S7, S8 and S9 write disjoint entry points and could
  be made side by side; S10 must follow all three so that its `--write` changes only its own paths.
  S6–S9 could run beside S3–S4, whose files are disjoint.
- **The installer** — S11 needs S6's committed skill and S10's green gate.

Shared mutable state limits even that: the slices share one worktree and its index, the
installation tests install the committed `HEAD`, and the gate's entry-point test is red from S6 to
S10 for every slice that runs it. Parallel work would need separate worktrees and a merge order.

Recommendation: no parallel execution. The adopted Superpowers 6.4.1
`subagent-driven-development` forbids parallel implementation subagents, so the slices run one at
a time in the order S1 → S2 → S3 → S4 → S5 → S6 → S7 → S8 → S9 → S10 → S11, each by a fresh executor
with a fresh task reviewer, then the whole-branch review. This order puts S5 before S6, so the
generator check in S5 still reads `entry points are current`, keeps the gate's entry-point test red
only from S6 to S10, and runs S11 on a green gate.

## Coverage

| What the task requires | Slices or entries |
|---|---|
| Outcome (spec §1 Success): a product refines a coding-guidelines task with the skill, takes it through `implement-task`, and ends with guidelines the form check passes, adopting or departing decisions, invariants on its declared commands and the `AGENTS.md` pointer | WAY-167, WAY-168, WAY-193–WAY-212; S1–S4 (template and form check), S5 (cycle), S6 (skill), S7–S10 (entry points), S11 (installer) |
| To do 1 — template of the discipline; general file and a file per kind with an exemplar, changing WAY-167 and the name rule; every rule an invariant, uncheckable → example; binding only by adoption; names | WAY-167, WAY-193, WAY-196, WAY-208; "exemplar", "standing check"; `guidelines-check-form`, `guidelines-check-carrier`; S2 (template, name rule, two forms), S1 (common names) |
| To do 2 — skill `maintain-coding-guidelines`: recognize and extend, new tool a question with the most-used default, preferences or research with critique, propose for every part with code and before the first code, ask every choice by its effect | WAY-194, WAY-208–WAY-211; S6 |
| To do 3 — exemplar designated by a decision, approval rules, checkable parts rules with invariants, rest example, first file vs audit with statuses, audit end | WAY-198–WAY-201; `guidelines-check-exemplar`; S2 (kind form, `## Files of this kind`), S3 (checks), S6 (audit steps) |
| To do 4 — three standing checks required, departure by decision; recognition, research; rule set by adoption (WAY-86); audit on the change; blocking only without false alarms, split from a trial run; list of violations plus fork-point companion; one reformatting; fault fixed in the file; binding from the coding-guidelines task | WAY-202–WAY-207; S2 (§4.3, §4.4 rules), S6 (steps 2–4) |
| To do 5 — good and bad uses as test cases of the invariant for every discipline; checked only when the invariant or a case changes; gate invariant; author's bad use beside the reviewer's break | WAY-168 edit, WAY-197; `guidelines-check-example-files`, `gate-guidelines-example-evidence`; S1, S4, S5 |
| To do 6 — a decision of the-way on what is taken from Open Mercato and Google, with quotations, and the two blocking conditions not taken | WAY-195 (F1a, sources re-read); S6 (the skill follows it) |
| To do 7 — `AGENTS.md` pointer outside the installer's block; table of kind files with when to read each | WAY-212, WAY-167; `guidelines-check-kind-index`; S2 (`## Kinds of code`), S3 (check), S6 (*To do* of `maintain-instruction-files`) |
| To do 8 — form check and `guidelines-check-form`/`-carrier` take `coding`: two forms, names, an invariant in every rule; entry points; `SKILLS` | `guidelines-check-form` (link), `guidelines-check-carrier` (edit); S2–S4; S6–S10 (entry points); S11 (`SKILLS`) |
| CQ1 — how cases are extracted and run | spec §5.1 blocks: S1 (rule), S4 (form check), S5 (reviewer), `gate-guidelines-example-evidence` |
| CQ2 — part of the tools' configuration | C5: S2 (template *Part* bullet), S6 (*To do* through `update-part-map`) |
| CQ3 — a product with the-way installed | spec §6.5: S11 (`SKILLS` and README); the request's line on moving the pin |
| CQ4 — English words | F2: "exemplar", "standing check", conditional term (C2) |
| CQ5 — two forms in the form check | S2 |
| CQ6 — one fact per edition, pinned versions | WAY-204 rationale (F1b); S2 (§4.4) |
| CQ7 — tools' results as a verdict per invariant | S2 (§4.4 record of a run) |
| Spec: WAY-167/WAY-168 in place with dependents renewed (WAY-31) | F1a: WAY-171, WAY-173, WAY-188, `guidelines-check-carrier` (F3) |
| Spec: new invariants of the-way | F3; F4; S3, S4 (covered code) |
| Spec: part-map failure modes (C6) | F2 |
| Spec: the task-cycle sentence (C8) | S5 |
| WAY-48 — crafted input at both trust boundaries | `product-guidelines/form_check.py`: S2, S3, S4 (spec §5.3); `installation/install.py`: S11 |
| WAY-69 / WAY-10 — three authors; invariant tests assessed | foundation stages (authors), deliberate breaks by S2, S3, S4, S11 reviewers; assessment at step 11 of the cycle |
| Row 1 | WAY-167 edit |
| Row 2 | WAY-198 |
| Row 3 | WAY-200 |
| Row 4 | WAY-199 |
| Row 5 | WAY-202 |
| Row 6 | WAY-206 |
| Row 7 | WAY-203 |
| Row 8 | WAY-204 |
| Row 9 | WAY-205 |
| Row 10 | WAY-196 (with `guidelines-check-carrier`) |
| Row 11 | WAY-168 edit (with `guidelines-check-example-files`) |
| Row 12 | WAY-197 |
| Row 13 | `gate-guidelines-example-evidence/1` |
| Row 14 | WAY-194 |
| Row 15 | WAY-212 (with `guidelines-check-kind-index`) |
| Row 16 | WAY-193 |
| Row 17 | WAY-195 |
| Row 18 | WAY-208 |
| Row 19 | WAY-209 |
| Row 20 | WAY-210 |
| Row 21 | WAY-211 |
| Row 22 | WAY-201 |
| Row 23 | WAY-207 |
| Row 24 | glossary "exemplar" |
| Row 25 | glossary "standing check" |

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| Four foundation stages before any slice, F1 split into F1a (WAY-167, WAY-168, renewals, WAY-193–WAY-202) and F1b (WAY-203–WAY-212) | one F1 agent for all 22 decisions | one more dispatch; the rejected way leaves one author reading about 227 000 of 250 000 estimated tokens before writing |
| `installation/test_install.py` `NAMES` changed in F4 by the check author, as an invariant-test change (WAY-03, WAY-65), assessed with the rest | changed in S11 (spec §6.6's letter); left unchanged as in the styleguide cycle | `installation` tests RED from F4 to S11, recorded. The first rejected way has an executor change an invariant test; the second departs from the settled spec |
| The coding template lands with the form check's items 1, 2 and 6 in S2, with the move of the `coding` fixtures in `test_form_check.py` | template first, code after; code first, tested on temporary templates | a larger S2 (three files). `read_templates` refuses a table without role columns, and the moved fixtures break the moment the template exists |
| The form check in three slices: two forms and tables (S2), index and exemplar (S3), test cases (S4) | one slice for all of spec §5.2 | the F4 tests of later items stay RED between slices; one slice would join three reviews of a trust-boundary script |
| `product-guidelines/styleguide/template.md` and `product-guidelines/styleguide/SKILL.md` unchanged | add the test-case rule to the styleguide's files | the styleguide skill's *To do* does not mention test cases; the common template's rule binds every discipline (C1), the styleguide template defers rule fields to it, and the form check reports a missing pair; spec §3.1 names neither file |
| The root `README.md` gains `product-guidelines/coding/` in S6 | README left as it is (the spec does not name it) | one more file in S6; the README describes the repository's directories and would omit one |
| S6 writes the skill's own two entry points through `discover`/`produce`; the other 32 follow in four batches of eight, the last running `--write` | one slice changing 34 files; hand-written entry points | four more slices and reviews, and the gate's entry-point test red from S6 to S10; a 34-file slice exceeds the limit of ten files |
| Batches by skill name, four skills each | three batches of ten, ten and twelve | none beyond the count; twelve files exceed the limit |
| S5 before S6 | S5 at the end | none functional; S5 after S6 would run its gate check during the red window |
| The C12 assumption on `check_instructions.py` checked in S1 on a small case, and end to end on filled coding guidelines in S4 | one end-to-end check only, or none | two runs on temporary repositories; without them a fence handling the design left unverified reaches products |
| Crafted-input tests of the form check are ordinary tests in `test_form_check.py`, written by the executors; the invariant tests stay F4's | crafted inputs in the invariant-test file | none; the rejected way moves executors' work into a file WAY-03 closes to them |
| The F4 check author reads spec §4.1, §4.2 and §5.1 (the forms the checks read) besides the sentences and methods, never §5.2 | sentences and methods alone | the check author sees template structure, not code reasoning; with sentences alone its fixtures would guess headings and columns the template fixes |
| Ranges planned at `235b0b4`, recomputed at `64344a3` with the size report (C23) | ranges written after the foundation stages | one mechanical refresh before dispatch; ranges written now would otherwise point into moved text |
| Every check on Python 3.13.16, named in the reports (cycle choice O3) | install 3.14 | a 3.14-only behaviour stays unchecked; recorded as unchecked |
