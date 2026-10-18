# Task 1 report — the guidelines template and the styleguide template

Status: DONE_WITH_CONCERNS. Commit range `8ea4679..ddef02a`, one commit:
`ddef02a feat(product-guidelines): add the template of guidelines and the template of the styleguide`.

## What I implemented

- `product-guidelines/template.md` (spec §3): what it binds (WAY-167, WAY-168, WAY-170, WAY-171,
  WAY-34); where guidelines go and file names (WAY-167); `## Required form` with the fenced
  skeleton of spec §3.1 verbatim, followed by its rules — *Discipline*, *Applies to*, `## When to
  read`, a binding rule's four fields, no rationale, examples, `## Where in code`, the `none —`
  departure; `## Rules of writing` — references (both forms of §3.2), fingerprint as
  `relation-model/fingerprint.py` computes it, stop-the-merge and no blind renewal (WAY-169), bare
  identifiers and versioned package names, code in backticks or fenced code with the reason
  (`check_instructions.py` dead-path and at-import), no emphasis words, language (WAY-171) with
  its price; `## The invariants of guidelines` — the sentences of `guidelines-form/1` and
  `guidelines-reference-current/1` byte-for-byte as `foundations/invariants.md:2135` and `:2145`
  hold them, as product copies (Method on `.the-way/product-guidelines/form_check.py`, `Derives
  from: none`, *Part* `every` and the three product parts), stated as given and not the product's
  to reword (C8 weak point), the-way's decisions they come from (WAY-170, WAY-171; WAY-169), the
  the-way variant, and the `unchecked` merge check before a main branch.
- `product-guidelines/styleguide/template.md` (spec §4): what it binds (WAY-167, WAY-183, WAY-173,
  WAY-171); `## Required form` with the merged form of spec §4.1 verbatim; its rules (an invariant
  in every rule WAY-188, order or `none —` WAY-171/WAY-173, unverifiable rule becomes an example,
  *Applies to*, `## When to read` condition WAY-192); `## What each part carries` — §4.2 part by
  part, each marked rule or example (Roles marked "a table"), each rule with the *Decision* and
  *Invariant* the skill proposes and its decision of the-way; "A fault of one screen is fixed in
  its component" carries WAY-178 with WAY-172's clause that a value change keeping its meaning is
  no decision; `## Pairs, meanings and role names` — the pairs note, why meanings stand twice
  (WAY-05 grouping), translated meanings (not caught by any check), role names (WAY-176, WAY-104);
  `## Writing the file` for the cycle's author (§4.3).

Interface for slices 2–3 (my choice, stated in both files): the form check reads the form from
the fenced block under `## Required form` — the only fenced block of that section. The
invariant-entry blocks in the common template are also ```` ```markdown ```` fences, but stand under
`## The invariants of guidelines`.

## Checks

All outputs under `C:/Storage/repos/the-way-wt/product-guidelines-styleguide/.runs/task-cycles/product-guidelines-styleguide/reports/`.

| Command | Exit | Output | Result |
|---|---|---|---|
| `python -B instruction-files/check_instructions.py <scratchpad>/slice1/product` (temp git repo built by `slice1/make_product.sh`; root `AGENTS.md` names `guidelines/styleguide-web.md` in backticks; the styleguide filled from the template: all 9 required rules, a role table with two background–text pairs, `bg-primary/90 w-1/2` in fenced code, `react@18`, `lucide-react@0`, `tailwindcss@4`, `@media` in backticks) | 0 | `slice-1-check-instructions.txt` | `0 error, 0 warn, 2 info`; the styleguide was read (its `size` line) — no `error`, no `dead-path`, no `at-import` |
| Positive control: same repo with `` `bg-primary/90` `` and `@src/tokens.css` appended outside fenced code | 0 | `slice-1-check-instructions-control.txt` | `WARN dead-path … bg-primary/90`, `WARN at-import … @src/tokens.css` — the instrument catches what the rule prevents; file restored after |
| `python -B elements/part-map/format_guard.py foundations/part_map.md --base none` | 1 | `slice-1-part-map-guard.txt` | `product-guidelines/**` matches files (no files error); the 2 remaining errors are the expected `form_check.py` trust boundary and `guidelines-form-check-command` declaration, until slice 2 |
| `git diff --cached --check` | 0 | `slice-1-diff-check.txt` | clean |
| `python -B gate/run_tests.py product-guidelines` | 1 | `slice-1-tests-product-guidelines.txt` | expected red: 25 tests, `failures=152`, each `can't open file …form_check.py` (exit 2 from a missing script) |
| `python -B gate/run_tests.py gate` / `agent-instructions` / `instruction-files` | 0 / 0 / 0 | `slice-1-tests-gate.txt`, `slice-1-tests-agent-instructions.txt`, `slice-1-tests-instruction-files.txt` | 98 OK; 18 OK; 104 OK (5 skipped) — nothing scanning `product-guidelines/` broke |
| `python -B elements/glossary/format_guard.py foundations/glossary.md --base none` | 0 | `slice-1-glossary-guard.txt` | 0 errors, 0 warnings |
| Weakest-point check (below) `python -B .runs/…/reports/slice-1-weakest-point.py .` | 0 | `slice-1-weakest-point.txt` (script: `slice-1-weakest-point.py`) | as below |

Manual check:

- Every `### ` of spec §4.1 is present verbatim and in order (`Each role in its meaning` …
  `The kitchen-sink page`, then the placeholder; `Mockups`, `Plan of a user-interface change`, then
  the placeholder); the nine required headings equal the fixture's `EACH_ROLE`, `BACKGROUND` and
  `DROPPED` headings in `product-guidelines/test_form_check_invariants.py` (scripted comparison).
- Each rule names its decision: every list item outside fenced code cites a `WAY-` number, except
  the five column sub-items of `## Roles`, whose parent item cites WAY-176.
- Each part of §4.2 marked: nine rules marked "rule", Mockups and Plan "example", `## Roles` "a
  table", `## Where in code` a section.
- No value, no package name, no *Avoid* word: grep over both files for hex colours, `px`, library
  names (react, tailwind, shadcn, lucide), course/skill names, `checker`, `quality gate`, bare
  `view`/`interface`/`token`/`domain`, and capitalised emphasis words — no hit (two bare "token"
  uses in the common template reworded to "run of characters" / "text"). A versioned package name
  is described as `<package>@<version>`, not by a real package.

## Files changed

| File | Added | Removed |
|---|---|---|
| `product-guidelines/template.md` | 174 | 0 |
| `product-guidelines/styleguide/template.md` | 190 | 0 |

## Sharpness inputs from the diff

- Part touched: `product-guidelines` only (two new Markdown files). No `foundations/` edit, no edit
  of the F4 test file.
- Trust-boundary files: none (`form_check.py` not touched).
- Irreversible: nothing. Process text with no behaviour; read later by the form check (S2–S3) and
  the skill (S4).

## Weakest-point check (WAY-164)

- Requirement most likely not met: the skeletons are the form the F4 fixtures follow, so a form
  check reading them holds the valid fixtures to exactly what they contain (a heading, header line
  or section in my skeleton that the fixtures lack, or a different order, would make S2 fail or
  force a test change — the tests are read-only), and the merged form is the common form with
  `## Roles` in its place.
- Check: `slice-1-weakest-point.py` reads the fenced block under `## Required form` of each
  template, takes its header lines, sections and non-placeholder `### ` headings, and checks them in
  order against the fixtures `TESTING` (common form) and `STYLEGUIDE` (merged form) imported from
  the F4 test file; it also checks the merged sections equal the common ones with `## Roles` after
  `## When to read`, the Roles table header, and lists items citing no decision.
- Shown: `TESTING follows the common form: True`, `STYLEGUIDE follows the merged form: True`,
  merged = common + Roles `True`, table header `True`; items with no decision: the 5 Roles column
  sub-items only (parent cites WAY-176); exit 0.

## Self-review findings (fixed)

- Two bare "token" uses (glossary of spec §9.1: "design token", never bare "token") reworded.
- One the-way-specific item had no citation; added (WAY-62).

## Issues or concerns

1. **Thin citations for two writing rules.** "Code in backticks or in fenced code" cites WAY-129
   and WAY-192, and "No emphasis words" cites WAY-192 and points to
   `instruction-files/principles.md`; no decision of the-way sets either for guidelines directly —
   they follow from a guidelines file becoming a repository instruction file once `AGENTS.md`
   names it (glossary term, WAY-192 for the styleguide). Spec §3.2 (root, finding 16) gives the
   rules with no decision. The whole-change review may want a sentence in a decision, or accept the
   reading.
2. **File names of non-styleguide guidelines.** Spec §5.3 5a and the F4 tests accept
   `guidelines/<discipline>-<part>.md` (e.g. `testing-web.md`); WAY-167 gives only
   `guidelines/<discipline>.md`. The template follows WAY-167 and says only that a name agrees with
   its *Discipline*; it does not offer `<discipline>-<part>.md`. Slice 2 will accept it per the
   tests; the foundation does not state it.
3. **Package-name examples.** Spec §3.2 names `react@18`, `tailwindcss@4`, `lucide-react@0`; the
   brief's manual check asks for no package name, so the template writes `<package>@<version>`.
4. Interface for S2: the form check should read the fenced block under `## Required form` (stated
   in both templates).

## Fix report — round 1 (finding I1)

Commit: `e62ca49 fix(product-guidelines): move the instruction-file reading of guidelines into a note citing its source files`
(`product-guidelines/template.md`, +17 −11).

What changed, per the controller's ruling:
- Removed from `## Rules of writing` the items "Code in backticks or in fenced code" (cited
  WAY-129, WAY-192) and "No emphasis words" (cited WAY-192).
- Added, after `## Rules of writing` and before `## The invariants of guidelines`, the section
  `## Note: a file of guidelines read as an instruction file`. It says it is no rule of the
  template and cites no decision as setting it. It explains that once a product's root `AGENTS.md`
  or `CLAUDE.md` names a file of guidelines by its path, the file is a repository instruction file
  (glossary of the-way). It then gives, citing the two files as the source:
  `instruction-files/check_instructions.py` takes backticked text holding `/` for a path (dead path
  when nothing lies there) and an `@` word holding `.` or `/` outside code for an import, so code
  names, at-rules and selectors go in backticks and a class or value holding `/` goes in fenced
  code; `instruction-files/principles.md` puts emphasis on one rule per file at most, and the
  script warns where more than one line carries it (`principles.md:171`, `check_instructions.py:533-537`).
  The note writes no capitalised emphasis words itself.
- No `foundations/` edit; the fenced skeleton and every heading of the required forms unchanged
  (the diff touches neither fenced block).

Checks (outputs under `.runs/task-cycles/product-guidelines-styleguide/reports/`):

| Command | Exit | Output | Result |
|---|---|---|---|
| `python -B instruction-files/check_instructions.py <scratchpad>/slice1/product` | 0 | `slice-1-fix1-check-instructions.txt` | `0 error, 0 warn, 2 info` — no `error`, `dead-path`, `at-import` |
| `git diff --cached --check` | 0 | `slice-1-fix1-diff-check.txt` | clean |
| `python -B .runs/task-cycles/product-guidelines-styleguide/reports/slice-1-weakest-point.py .` | 0 | `slice-1-fix1-weakest-point.txt` | skeleton headings unchanged: TESTING follows the common form `True`, STYLEGUIDE follows the merged form `True`, merged = common + Roles `True`; items citing no decision: the 5 Roles column sub-items and the 2 items of the new note, which by the ruling cite no decision |

Concern 1 of the report is resolved by this fix; concerns 2–4 stand.
