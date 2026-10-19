# Slice 1 report — the common template names the coding files and gives test cases

**Status:** DONE_WITH_CONCERNS (one concern for S4, below). **Commit:** `7976b54` on
`claude/gallant-albattani-3k15lc` (parent `64344a3`), not pushed. Python 3.13.16 (`python3`; the
repository declares 3.14).

## What I implemented

`product-guidelines/template.md` only:

- **Where guidelines go.** The first bullet is split into three, each citing WAY-167: the
  `guidelines/<discipline>.md` rule "save the styleguide and coding disciplines"; the styleguide's
  `guidelines/styleguide-<part>.md`; and the coding discipline's `guidelines/coding.md` (standing
  checks, rules of the whole code, a table naming each other file of the discipline with when to
  read it) and `guidelines/coding-<kind>.md` (one per kind of code that has an exemplar, holding
  that exemplar and its rules, `<kind>` the identifier the designating decision gives), in WAY-167's
  current words.
- **Required form.** Only the *Good* and *Bad* placeholders changed:
  `<one line describing a use that follows the rule>` / `<one line describing a use that breaks it>`.
  Field names, headings and the fenced block are otherwise as they were.
- **A binding rule** bullet: *Good* "describes in one line" a use, *Bad* one that breaks it; a rule
  naming an invariant gives those uses as test cases (WAY-168); "the styleguide's template does
  (WAY-188), and so does the coding template (WAY-196)".
- **New section `## Test cases of a rule`**, between `## Required form` and `## Rules of writing`,
  each bullet citing WAY-168 (plus WAY-170 where the form check reports, WAY-197 for the teaching
  bad case, WAY-190/WAY-205 naming the companion): every discipline (C1); one `good <identifier>
  <path>` and one `bad <identifier> <path>` block per invariant named other than `guidelines-form`,
  after the four fields (C18); each the whole text of a file at a product path, added or put in
  place on the commit checked, method passes good / fails bad; the relative reading for a listed
  invariant and the strict reading for its per-file companion (C19); every fenced block of such a
  rule a test case, illustration under `## Examples`; short files at paths that may not exist
  (C12); path limits (relative, no `..`, drive, `\`, `:`, leading `/`) and the 1048576-byte limit;
  three-backtick outer fence and no fence-opening line inside, the form check reporting a tilde
  fence or backticks-with-text inside; the bare-fence consequence (C21); the `guidelines-form`
  exemption with its reason (C11), naming the styleguide's `### Every background with its text`.
- **Note on `check_instructions.py`**: a new bullet — the cases' paths and texts stay in fenced
  code, where that script reads no path or import; the script toggles on a line beginning with
  three backticks or tildes after *any* spaces or tabs, so a case keeping it quiet holds no such
  line at any indentation (see Weakest point).

No value is copied. No illustration block was added (a fenced example of a fenced case would need
nested fences in the template, which `template_section`/`parse_form` and the rule itself make
fragile); the prose gives the form exactly.

TDD: text only, no behaviour change; no test of its own (as the brief says). No RED/GREEN.

## Checks (outputs beside this report, in `reports/sdd/`)

| Check | Command | Exit | Output |
|---|---|---|---|
| Baseline at `64344a3` | `python3 -B gate/run_tests.py product-guidelines --record …/slice-1-baseline-product-guidelines.jsonl` | 1 (88 tests, failures=89) | `slice-1-baseline-product-guidelines.txt`, `.jsonl` |
| Baseline per name | `python3 -B -m unittest discover -v -s product-guidelines -p "test_*.py"` | 1 | `slice-1-baseline-unittest-v.txt` |
| After | `python3 -B gate/run_tests.py product-guidelines --record …/slice-1-product-guidelines.jsonl` | 1 (88 tests, failures=89) | `slice-1-product-guidelines.txt`, `.jsonl`, `.exit` |
| After per name | same unittest -v command | 1 | `slice-1-unittest-v.txt` |
| Compared by name | script in this session | — | `slice-1-compare.txt`: 88/88 test ids identical outcomes; 89/89 FAIL headers (with subtests) identical; 64/64 record lines identical. The 23 not-ok tests are exactly F4's RED list (`f4-check.md`) |
| Template parse | `form_check.read_templates` on the `64344a3` templates vs the working tree | 0 | `slice-1-template-parse.txt`: `same parse: True` |
| Form check on the-way | `python3 -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` | 0 | `slice-1-form-check.txt`; record: `read_guidelines` `pass` for `guidelines-form/1` |
| C12 assumption | temporary git repo: root `AGENTS.md` names `` `guidelines/testing.md` ``, holding one rule with a good/bad pair as the template gives (info strings, paths `tests/api/orders/…`, `@` in `ops@example.com` and `@docs/setup.md.` inside the bad case); `python3 -B instruction-files/check_instructions.py <repo>` | 0 | `slice-1-check-instructions.txt`: `0 error, 0 warn, 2 info` (size lines only; the file was followed), no dead path, no import |
| Gate tests | `python3 -B gate/run_tests.py gate --record …/slice-1-gate.jsonl` | 0 (98 tests OK) | `slice-1-gate.txt`, `.jsonl`, `.exit` |
| Whitespace | `git diff --check 64344a3` | 0 | — |
| Manual text | glossary *Avoid* words (`checker`, `quality gate`, `reference implementation`, `standing guard`) grep; added lines listed | grep 1 (no match) | `slice-1-manual-text.txt` |

Failed checks: none beyond the expected RED. Unchecked: none of the brief's.

### Manual (spec §5.1 bullets, decisions, Avoid words)

- §5.1 bullet 1 (pair per invariant, whole file, method passes/fails): bullets "A pair for each
  invariant", "A test case is a whole file" — present.
- §5.1 bullet 2 (relative reading; companion strict, C19): "An invariant on the list of violated
  invariants" — present.
- §5.1 bullet 3 (every fenced block a case; illustration under `## Examples`) — present.
- §5.1 bullet 4 (short file, may not exist; path limits; 1 MiB) — two bullets, present.
- §5.1 bullet 5 (three-backtick outer fence; no fence-opening line; check_instructions reason;
  paths/texts in fenced code; bare fence → malformed test case, C21) — fence bullet plus the note
  bullet, present.
- §5.1 exemption (C11) and "every discipline" (C1) — present (section intro and last bullet).
- Every added rule bullet ends with its decision(s); the note stays without a citation, as the
  existing note says it cites none. No *Avoid* word in the file.

## Weakest point (WAY-164)

Requirement: a file of guidelines written as the template gives keeps
`instruction-files/check_instructions.py` quiet once a product's `AGENTS.md` names it (spec §5.1
bullet 5, the C12 assumption). The spec's rule forbids a fence-opening line "after at most three
spaces", as the form check reads fences, but `check_instructions.py`'s `FENCE` is `^\s*(```|~~~)`
(any whitespace).

Check (manual, by me, the executor): a copy of the temporary repository whose good case holds a
Python docstring with a line of four spaces and three backticks — allowed by the ≤3-space rule,
read by the form check as case text. Observed: `ERROR at-import guidelines/testing.md:38
@docs/setup.md. — a punctuation mark right after the path…`, exit 1
(`slice-1-weakest-indented-fence.txt`): the script toggled out of code inside the case and read the
bad case's text as prose. The plain template-conformant file gives no error
(`slice-1-check-instructions.txt`).

What I did: kept the binding rule as the spec gives it (≤3 spaces, what the form check reports) and
put the fact in the note on `check_instructions.py`, which tells an author a case keeping that
script quiet holds no such line at any indentation. This is a description of an existing script,
not a new rule, so I settled it rather than stopping.

## Changed files (`git diff --numstat 64344a3..HEAD`)

```
63	8	product-guidelines/template.md
```

## Sharpness inputs

- Parts touched (`foundations/part_map.md`): `product-guidelines` only.
- Trust-boundary files touched: none (`product-guidelines/form_check.py` is the part's trust
  boundary; it reads the template, whose parsed form is unchanged — `same parse: True`).
- Irreversible operations: none.

## Questions and choices

- No open design choice met.
- Choices of how to make what is settled: a section of its own for test cases (keeps the `## Required
  form` section's fenced block first and alone, which `parse_form` needs); no fenced illustration;
  the indentation fact in the note rather than in the rule (above).

## Self-review

- The template's form block, header lines, fields and sections parse identically; the styleguide's
  merged form and `requires_invariant`/`per_part` are unchanged.
- WAY-167 wording followed closely; `<kind>`'s identifier pattern is left to the coding template
  and form check (S2/S5), as WAY-167 does not state it.
- No line over 100 characters added; no capitals emphasis.

## Concerns

1. **For S4 (form check of test cases) and the orchestrator:** the spec's fence rule (≤3 spaces)
   and `check_instructions.py`'s toggle (any indentation, tabs included) differ. A case with a line
   indented four or more spaces that starts with three backticks or tildes passes the form check
   as S4 is specified, yet makes `check_instructions.py` read the rest of the case as prose (an
   `error` is possible). The template's note now warns authors; whether S4 should also report such
   a line (stricter than the spec's §5.2 item 5) is the orchestrator's ruling.

## Fix after ruling C33

**Commit:** `18317a8` (parent `7976b54`), not pushed. Ruling C33: a test case's text holds no line
that, after any leading whitespace, starts with three backticks or three tildes; S4's form check
reports such a line.

What changed in `product-guidelines/template.md`:

- The fence bullet of `## Test cases of a rule` now says: "the text of a case holds no line that,
  after any leading whitespace, starts with three backticks or three tildes; the form check reports
  such a line (WAY-168, WAY-170)". The bare-fence consequence (C21) is unchanged.
- The note's warning about indentation is gone. Its bullet keeps "the paths and texts of a rule's
  test cases stay in fenced code, where that script reads no path and no import", and adds that
  the script switches on every such line, "which is why the text of a case holds no such line".

The concern of the first report is settled by C33.

Checks (Python 3.13.16; outputs in `reports/sdd/`):

| Check | Command | Exit | Output |
|---|---|---|---|
| product-guidelines | `python3 -B gate/run_tests.py product-guidelines --record …/slice-1-fix-product-guidelines.jsonl` | 1 (88 tests, failures=89) | `slice-1-fix-product-guidelines.txt`, `.jsonl`, `.exit` |
| per name | `python3 -B -m unittest discover -v -s product-guidelines -p "test_*.py"` | 1 | `slice-1-fix-unittest-v.txt` |
| compared with `64344a3` | comparison script | — | `slice-1-fix-compare.txt`: 88/88 ids same outcome, 89/89 FAIL headers, 64/64 record lines identical; the 23 failing tests are F4's RED list |
| template parse | `read_templates` at `64344a3` vs now | 0 | `slice-1-fix-template-parse.txt`: `same parse: True` |
| form check | `python3 -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` | 0 | `slice-1-fix-form-check.txt`: `guidelines-form/1` pass |
| gate | `python3 -B gate/run_tests.py gate --record …/slice-1-fix-gate.jsonl` | 0 (98 OK) | `slice-1-fix-gate.txt`, `.jsonl`, `.exit` |
| whitespace | `git diff --check 64344a3` | 0 | — |
| weakest point | the indented variant's case lines matched against the rule as the template now words it (`^\s*(```|~~~)`) and against check_instructions' `FENCE`; check_instructions on the variant and on the conformant repository | variant 1, conformant 0 | `slice-1-fix-weakest.txt` |

**Weakest-point result:** the variant's line 26 (`'    ```'`) is now forbidden by the template's
rule, and it is exactly the line check_instructions toggles on (`FENCE toggles: True`). That is 1
forbidden line, and it is what caused the variant's `ERROR at-import`. The conformant file still
gives 0 errors. So a file that follows the template now keeps check_instructions quiet. It is S4
that will make the form check report the line.

Changed files (`git diff --numstat 64344a3..HEAD`): `61	8	product-guidelines/template.md`.
Parts touched: `product-guidelines`. Trust-boundary files: none. Irreversible operations: none.

**Process slip, for the orchestrator:** I applied the two edits with the Artifact tool's publish
action (its `edits` option) instead of Edit. The edits did land in the file, which is what was
committed. But the call also published `product-guidelines/template.md` as a private claude.ai
artifact: https://claude.ai/artifact/TF7fXTZmVWc59ASkjcDHFP. Only the owner can open it. I have not
deleted it, because deleting needs the user's request. If the user does not want it, they can ask
for it to be deleted.

## Assessment I2 settlement — the styleguide template and skill point to test cases

**Commit:** `8242720` (parent `a677bc4`), not pushed. Only the Edit tool was used,
as the updated contract requires (no Artifact tool).

What changed:

- `product-guidelines/styleguide/template.md`:
  - The opening's list of the rules of form every file of guidelines keeps now includes "the test
    cases of a rule that names an invariant", kept in `product-guidelines/template.md`.
  - A new bullet in "Writing the file" says to write each rule's test cases as "Test cases of a
    rule" of `product-guidelines/template.md` gives them (WAY-168). It says
    `### Every background with its text`, whose invariant is the product's copy of
    `guidelines-form`, carries none. It also says that, where the product cleans its screens
    gradually, the full invariant of `### No value in place of a design token` stands on the list
    of violated invariants: its cases are read against the commit's own result, while its per-file
    companion's cases take the strict reading (WAY-168, WAY-190).
- `product-guidelines/styleguide/SKILL.md`, *To do*: the item that writes the styleguide now also
  points to "Test cases of a rule" of `.the-way/product-guidelines/template.md` (WAY-168). It says
  the cases of `### No value in place of a design token` take the reading that section gives for a
  violated invariant and for the invariant beside it (WAY-190). The frontmatter is unchanged.

The form section is unchanged. No rule is restated and no value is added.

Checks (Python 3.13.16; outputs in `reports/sdd/`):

| Check | Command | Exit | Output |
|---|---|---|---|
| template parse | `read_templates` on the three templates at `a677bc4` vs now | 0 | `slice-1-i2-template-parse.txt`: `same parse: True` |
| product-guidelines | `python3 -B gate/run_tests.py product-guidelines --record …` | 0 (138 OK) | `slice-1-i2-product-guidelines.txt`, `.jsonl`, `.exit` |
| form check | `python3 -B product-guidelines/form_check.py --record .runs/guidelines-form.jsonl` | 0 | `slice-1-i2-form-check.txt`: `guidelines-form/1` pass |
| entry points | `python3 -B agent-instructions/skill_entry_points.py --write` | 0 | "entry points are current"; nothing written |
| agent-instructions | `python3 -B gate/run_tests.py agent-instructions --record …` | 0 (18 OK) | `slice-1-i2-agent-instructions.*` |
| gate | `python3 -B gate/run_tests.py gate --record …` | 0 (98 OK) | `slice-1-i2-gate.*` |
| installation (it installs the skill) | `python3 -B gate/run_tests.py installation --record …` | 0 (35 OK) | `slice-1-i2-installation.*` |
| whitespace | `git diff --check a677bc4` | 0 | — |

**Weakest point:** the requirement most likely missed was naming *every* required styleguide rule
that takes the relative reading. Check: I searched the styleguide decisions WAY-173 to WAY-192 for
"violated invariants", and confirmed that both headings named in the new text exist verbatim in the
form block (`slice-1-i2-weakest.txt`). Result: only WAY-190 places an invariant on the list, and it
is the invariant of `### No value in place of a design token`. Both headings match (1 each). No
other required rule takes the relative reading.

Parts touched: `product-guidelines`. Trust-boundary files: none. Irreversible operations: none.
