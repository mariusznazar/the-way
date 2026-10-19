# Slice 1 review — common template names the coding files and gives test cases

Base 64344a3, head 18317a8 (7976b54 + the C33 fix). Diff: `product-guidelines/template.md` only
(61+/8-). Authority read: spec §5.1, cycle.md C1/C11/C12/C18/C19/C21/C33, progress.md C33 ruling,
WAY-167/168/170/190/196/197/205 in `foundations/decisions.md`.

### Spec Compliance

- ✅ Spec compliant. Every §5.1 bullet and the brief's list is in the head file:
  - Where guidelines go: three bullets, each citing WAY-167 (template.md diff lines 17-28); the wording
    follows WAY-167 as now edited (`save the styleguide and coding disciplines`, `coding.md` with
    standing checks, whole-code rules and the table of kind files; `coding-<kind>.md`, `<kind>` the
    identifier the designating decision gives).
  - Required form: only the *Good*/*Bad* placeholders changed to "one line describing …"; headings,
    field names and the fence are untouched. Executor's `same parse: True` (slice-1-fix-template-parse.txt)
    is consistent with the diff: no line in the fenced block other than those two changed.
  - Binding-rule bullet: *Good*/*Bad* described in one line; cases for a rule naming an invariant
    (WAY-168); "the styleguide's template does (WAY-188), and so does the coding template (WAY-196)".
  - `## Test cases of a rule` (every discipline, C1): pair per invariant other than `guidelines-form`
    after the four fields, `good|bad <identifier> <path>` (C18); whole file added or put in place, method
    passes good / fails bad; relative reading for a listed invariant, strict for the per-file companion
    (C19; WAY-190/205); every fenced block a case, illustration under `## Examples`; short file at a
    path that may not exist; path limits and the 1048576-byte limit; three-backtick outer fence and the
    no-fence-line rule; bare-fence consequence (C21); `guidelines-form` exemption (C11) naming
    `### Every background with its text`.
  - C33 (global constraint): the fence bullet says "no line that, after any leading whitespace, starts
    with three backticks or three tildes" — the constraint's wording; the form check reports it
    (WAY-168, WAY-170).
  - Note on `check_instructions.py`: new bullet says the cases' paths and texts stay in fenced code and
    gives the reason (the script toggles on every such line). The earlier indentation warning is gone,
    as C33 settles it.
  - No value copied; each new rule bullet ends with its decision(s); the note bullet cites none, as the
    note says it cites none. No glossary *Avoid* word added (`checker`, `quality gate`, `reference
    implementation`, `standing guard` absent; executor's `slice-1-manual-text.txt`).
- ⚠️ Cannot verify from this diff: the template promises behaviour of code that does not exist yet at
  this head (form check reporting a path outside the limits, a tilde fence or indented fence line in a
  case, a bare-fence malformed case, files over 1 MiB left unread). That is S4/S5 work; the controller
  should check at the S4 review that each reported item here has a matching check there.
  The `check_instructions.py` claim is verifiable and I verified it: `instruction-files/check_instructions.py:57`
  `FENCE = ^\s*(```|~~~)`, against `form_check.py:125` `OPEN_FENCE = ^ {0,3}…`, so the C33 widening is
  needed and the template's reason is accurate.

### Strengths

- Smallest possible footprint: one file, no code, and the form block untouched, so the form check's
  reading of the template is provably unchanged (parse compared by `read_templates`, test names compared
  88/88, same 23 F4 RED tests before and after, gate 98 OK, form check exit 0 with
  `guidelines-form/1` pass — all in the `slice-1-fix-*` outputs).
- The weakest point (indented fence vs `check_instructions.py`) was found by an actual run against a
  crafted variant (slice-1-fix-weakest.txt: the ≤3-space line `    ```` made the script toggle out of code
  and raise `ERROR at-import`), escalated rather than silently settled, and the final text matches
  the ruling exactly.
- Section placed after `## Required form` and before `## Rules of writing`, so `parse_form`'s
  fenced block stays first and alone in its section; every bullet carries its decision.
- Sharpness inputs check out against the diff: parts touched `product-guidelines` only; no trust-boundary
  file (`form_check.py`, `install.py`) in the diff, so no crafted-input tests (WAY-48) are owed by this
  slice. No invariant's code is covered, so no deliberate break (as the dispatch says).

### Issues

#### Critical (Must Fix)

None.

#### Important (Should Fix)

None in the diff.

#### Minor (Nice to Have)

1. Process, outside the task's scope: the report's own "Process slip" — the executor applied the C33
   edits through the Artifact tool's publish action, which created a private claude.ai artifact of
   `product-guidelines/template.md` (https://claude.ai/artifact/TF7fXTZmVWc59ASkjcDHFP). The file
   committed is correct, and the page is private, but it is an unrequested publication; the executor
   rightly did not delete it. The controller should tell Mariusz and delete only if he asks.
2. `template.md` (section `## Test cases of a rule`, bullet "A test case is a short file"): WAY-197 is
   cited for "the bad case teaches the agent reading the guidelines". WAY-197 sets who writes the bad
   use and that it stands beside the deliberate break; the teaching purpose is spec §5.1's Q7. The
   citation is defensible (the rule is about the author's bad use) but not exact; no change needed
   unless the human prefers citations to match one-to-one.
3. The exemption bullet and the pair bullet leave open a rule whose *Invariant* names `guidelines-form`
   together with another invariant (the pair bullet then applies to the other one). Spec §5.1 reads the
   same way; S4's form check should state the case in its tests rather than the template changing.
4. The fence bullet states the forbidden line and then the C21 bare-fence consequence; after C33 a bare
   fence line is already forbidden, so the consequence now describes how the form check reads a
   violation. Kept as the spec has it; fine.

### Assessment

**Task quality:** Approved

**Reasoning:** The template text matches spec §5.1 as amended by C33, WAY-167's current wording and the
form block is unchanged, with checks showing the same tests pass and fail as at 64344a3. Only the
executor's use of the Artifact tool (Minor 1, out of the task's scope) needs the controller's attention.
