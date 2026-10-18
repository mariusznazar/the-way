# Task 1 review — the guidelines template and the styleguide template

Range `8ea4679..ddef02a` (one commit, `ddef02a`), two new files:
`product-guidelines/template.md` (174 lines) and `product-guidelines/styleguide/template.md`
(190 lines). Line numbers below are of the files at `ddef02a` (HEAD of the worktree, confirmed).

What I checked beyond the diff, one check per named risk:

- **Risk: the skeletons hold a fixture to more than it contains (the tests are read-only).** I read
  the fixtures `STYLEGUIDE`, `EACH_ROLE`, `BACKGROUND`, `DROPPED`, `TESTING` in
  `product-guidelines/test_form_check_invariants.py:146-223` against both fenced skeletons. The nine
  required headings at `product-guidelines/styleguide/template.md:38-46` equal the fixture's
  `EACH_ROLE` (`:160`), `BACKGROUND` (`:166`) and `DROPPED` (`:172-174`) in order; `## Roles` and its
  header row (`styleguide/template.md:31-34`) equal `:151-153`; the common skeleton
  (`product-guidelines/template.md:34-57`) is followed by `TESTING` (`:193-222`). No mismatch.
- **Risk: the invariant sentences are not those of the-way's entries.** Python compared
  `product-guidelines/template.md:144` with `foundations/invariants.md:2135` and `:156` with `:2145`:
  both `True` (byte-equal).
- **Risk: placeholders in backticks become dead paths once a skill points to the templates.**
  `instruction-files/check_instructions.py:371` skips any backticked text holding `*<>{}|$…`, so
  `guidelines/<discipline>.md`, `guidelines/**`, `{fork-point}` raise nothing.
- **Risk: the emphasis rule restates the principle wrongly.** `instruction-files/principles.md:171`
  and `check_instructions.py:535-537`: emphasis on one rule per file at most (see Minor M2).
- Trailing whitespace: none in either file. Both files stored `i/lf` with `eol=lf`.

## Spec Compliance

- ❌ Issues found:
  - Two rules of writing cite decisions of the-way that do not set them, against WAY-171's last
    sentence and the brief's "Each rule cites the decision that sets it" (Important I1,
    plan-mandated).
- ✅ Otherwise compliant with the brief, spec §3 and §4:
  - §3.1 skeleton verbatim (`product-guidelines/template.md:34-57`) with its rules (`:59-84`);
    §3.2 references in both forms (`:88-93`), bare identifiers and versioned package names
    (`:103-108`), code in backticks or fenced code (`:109-116`), language with its price
    (`:120-124`); §3.3 both sentences as given, not the product's to reword, with the-way's
    decisions they come from (`:126-139`), product copies (`:141-163`), the-way variant (`:170-171`),
    `unchecked` before a main branch (`:172-174`).
  - §4.1 merged form verbatim (`styleguide/template.md:23-56`) with its rules (`:58-71`); §4.2 part
    by part, each marked rule, example or table, each rule with the *Decision* and *Invariant* the
    skill proposes (`:73-153`); the pairs note, why meanings stand twice, translated meanings, role
    names (`:155-177`); §4.3 Writing the file (`:179-190`).
  - "A fault of one screen is fixed in its component" carries WAY-178 with WAY-172's clause that a
    value change keeping its meaning is no decision (`styleguide/template.md:127-134`).
  - No value, no package name, no glossary *Avoid* word (the glossary's only *Avoid* words are
    "checker" and "quality gate", `foundations/glossary.md:81`, `:102`; neither appears).
- ⚠️ Cannot verify from the diff:
  - Whether the interface the implementer chose — the form check reads the fenced block under
    `## Required form`, placeholders in `<…>` — is what slices 2–3 can parse without loss. The
    skeletons are consistent with that reading; the parser is not written yet.
  - File names `guidelines/<discipline>-<part>.md`: spec §5.3 5a
    (`.runs/task-cycles/product-guidelines-styleguide/spec.md:397-401`) accepts them, WAY-167
    (`foundations/decisions.md:5441-5445`) gives only `guidelines/<discipline>.md`, and the template
    follows WAY-167 (`product-guidelines/template.md:18-27`). The foundation and the spec disagree;
    this is for the whole-change review, not this slice (see Minor M6).

## Strengths

- The two invariant sentences are byte-equal to the-way's entries, and the paragraph at
  `product-guidelines/template.md:128-132` states exactly why they are not the product's to reword
  (C8's weak point), including what a rewording costs.
- The skeletons are faithful to the read-only F4 fixtures, and the implementer proved it with a
  script that imports the fixtures rather than retyping them
  (`.runs/task-cycles/product-guidelines-styleguide/reports/slice-1-weakest-point.py`).
- The `check_instructions.py` run on a temporary product carries a positive control
  (`reports/slice-1-check-instructions-control.txt`) that shows the instrument catches a backticked
  `/` and an `@` import outside code, so the clean run (`slice-1-check-instructions.txt`, 0 error,
  0 warn) is evidence, not silence.
- "Translated meanings" (`styleguide/template.md:166-173`) states plainly what no check catches, as
  the spec requires, rather than implying the fingerprint covers it.
- The implementer disclosed the citation gap itself (report, Issues 1) instead of papering over it.

## Issues

### Critical (Must Fix)

None.

### Important (Should Fix)

**I1 (plan-mandated). Two rules of writing cite decisions that do not set them.**
`product-guidelines/template.md:109-116` ("Code in backticks or in fenced code", citing WAY-129 and
WAY-192) and `product-guidelines/template.md:117-119` ("No emphasis words", citing WAY-192).

- What is wrong: WAY-129 (`foundations/decisions.md:3875-3880`) binds how the-way's own instruction
  files point to another file; WAY-192 (`:6336-6340`) binds how a product's `AGENTS.md` points to its
  styleguide and where the rule against values written in place of design tokens stands. Neither
  sets a rule on how the text of a file of guidelines writes code names, classes holding `/`, or
  emphasis. The rules follow from a reading — WAY-192's pointer makes the styleguide a repository
  instruction file, and `check_instructions.py` then reads it — but no decision of the-way says so.
  Spec §3.2 (`spec.md:176-182`) gives the rules with no decision, so the slice could not cite one.
- Why it matters: WAY-171's last binding sentence (`foundations/decisions.md:5616-5617`) has a
  rule of the-way's templates of guidelines change only with a decision of the-way and cite its
  number, and its *violates* case (`:5631`) is "a rule enters a template of guidelines with no
  decision of the-way". A citation that names a decision which does not set the rule looks like a
  carrier and hides the gap from the next reader, who will take WAY-129 as the rule's ground. The
  first is also not limited to the styleguide: "Once a product's root `AGENTS.md` names a file of
  guidelines" (`:109`) generalises WAY-192, which speaks only of styleguides, to every discipline.
- How to fix: not inside this slice's licence (the global constraints forbid editing
  `foundations/`). The root should rule: either a sentence in WAY-192 or WAY-171 that a file of
  guidelines an instruction file points to keeps the writing `instruction-files/check_instructions.py`
  reads (code with `/` in fenced code, no `@` import, emphasis on one rule at most), and the two
  items then cite it; or the two items are reworded as a note on how `check_instructions.py` reads a
  styleguide once WAY-192's pointer exists, standing outside the template's rules, with no
  citation dressed as a setting decision. Until then the task cannot claim the brief's "each rule
  cites the decision that sets it".

### Minor (Nice to Have)

**M1. "Nothing of this template is copied into a product" contradicts the invariants section.**
`product-guidelines/template.md:13-14` against `:136-137` ("A product that keeps guidelines holds
copies with the same identifiers and sentences"). An agent writing a product's first guidelines
reads first that nothing is copied, then that two blocks of this file are to be copied word for
word. The spec meant the form (`spec.md:100-101`, "the product's styleguide is an instance").
Fix: "The form of this template is not copied into a product: …".

**M2. The heading "No emphasis words" says the opposite of its body.**
`product-guidelines/template.md:117-118`: the heading forbids emphasis words, the body allows them on
one rule of a file, as `instruction-files/principles.md:171` and `check_instructions.py:535-537`
give it. The body is right; an agent reading the bold lead alone gets the wrong rule. Fix: lead
with "**Emphasis on one rule at most.**".

**M3. "Part" in a second meaning beside the part of the map.**
`product-guidelines/styleguide/template.md:4` ("what each part of a styleguide carries"), `:73`
(`## What each part carries`), `:75` ("Each part below"), while the same file uses "part" as the
glossary's part of a product's map at `:7`, `:68`, `:95-97`, `:106-107` and lists `part` at `:175`
as a word a role name avoids because the glossary holds it (`foundations/glossary.md:147-149`).
WAY-95 does not bind this file, but the template asks products to keep exactly this distinction,
and `:95-97` ("every file of the user interface's part … whose *Part* names that part") sits under
a heading that uses the other meaning. The spec's table header "Part" (`spec.md:273`) is the source
of the inherited word. Fix: "section" or "piece" for the styleguide's divisions.

**M4. The language rule does not name the column headings of `## Roles`.**
`product-guidelines/template.md:120-124` keeps in English "the headings of the required form, the
header lines, the field names, the values of closed lists, the headings of required rules and the
marker". The form check reads the header row `| Role | Kind | Meaning for the user | Text on it |
Decision |` (`styleguide/template.md:31-32`; spec §5.3 item 3, `spec.md:390-392`), and none of the
listed words clearly covers a table's column headings. A product writing in Polish could translate
"Meaning for the user" and fail the check with no rule having said not to. Fix: in
`styleguide/template.md:79-88` or `:58-71`, one clause that the table's header row stays as the
form gives it (WAY-171's "headings … field names" carries it).

**M5. The invariant proposed for "Every background with its text" does not speak of pairs.**
`product-guidelines/styleguide/template.md:98-102` names the product's copy of `guidelines-form`
as the invariant that checks the rule. The sentence of `guidelines-form`
(`foundations/invariants.md:2135`) speaks of header lines, sections, rules, rule fields, drops,
parts and paths — not of a background role's *Text on it*. The form check does report that fault
(spec §5.3 item 3) and records it under `guidelines-form`, so the fault is caught, but the method
then checks more than its sentence says (WAY-61, `foundations/decisions.md:1751-1752`), and WAY-188
asks for an invariant "that checks it". This follows spec §4.2 (`spec.md:277`) and is not this
slice's to change; flag it to the whole-change review.

**M6. Citation precision.**
- `product-guidelines/styleguide/template.md:95-97`: the *Part* of the role-meaning invariant
  (the user interface's part and the part holding `foundations/**`) is WAY-62's reaching, as spec
  §6.3 gives it (`spec.md:562-564`), but the item cites only WAY-189, which says nothing of *Part*.
  Add WAY-62.
- `product-guidelines/template.md:18-27` and `:26-27`: file names of non-styleguide guidelines
  follow WAY-167 alone, while spec §5.3 5a and slice 2's check will accept
  `guidelines/<discipline>-<part>.md`. Either the template is silent on a name the check accepts,
  or the check accepts a name the foundation does not give; for the whole-change review (also in
  the ⚠️ list).

## The implementer's weakest-point check (WAY-164)

- Named requirement: the skeletons are the form the F4 fixtures follow, so a form check reading them
  holds valid fixtures to exactly what they contain. This is a real weak point — the F4 tests are a
  read-only contract (C28.2), and a mismatch would surface only in slice 2 as a test that cannot be
  changed. The check (`reports/slice-1-weakest-point.py`) imports the fixtures rather than retyping
  them, which is the right instrument.
- Limits of the check: it tests one direction (every skeleton item appears in the fixture, in
  order), matches header lines by prefix, and does not exercise the failing fixtures whose expected
  line numbers depend on what the form check derives from the skeleton — acceptable for a text-only
  slice, since slice 2 runs them.
- What it misses: the slice's weakest point against the brief is citation fidelity — "each rule
  cites the decision that sets it". The script tests only that a `WAY-` number is present
  (`slice-1-weakest-point.py`, the `uncited` loop), so it passes I1. The implementer knew this
  (report, Issues 1) but did not make it the named requirement, and the check could not catch it.
  The choice is defensible, not the sharpest.

## Sharpness inputs (report, "Sharpness inputs from the diff")

Confirmed from the diff: part touched `product-guidelines` only, two new Markdown files (stat
`190 + 174`, `0` removed); no `foundations/` edit; no edit of
`product-guidelines/test_form_check_invariants.py`; no trust-boundary file (`form_check.py`
untouched); nothing irreversible. The part-map guard's two remaining errors
(`reports/slice-1-part-map-guard.txt`) are the expected ones, down from three as the global
constraints predict; the 152 failures of `gate/run_tests.py product-guidelines` are the recorded
red state (missing `form_check.py`). No unreported warning or noise in the outputs I read.

## Assessment

**Task quality:** Needs fixes

**Reasoning:** The templates are faithful to spec §3–§4 and to the read-only fixtures, and the
invariant sentences are exact, but two rules of writing cite decisions that do not set them, which
WAY-171 and the brief forbid; the fix needs a root ruling (a foundation sentence or a reframing),
plan-mandated by spec §3.2. The Minor items are wording that would mislead an agent at the margin
and can go with that fix.
