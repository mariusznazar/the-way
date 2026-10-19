# Independent assessment (WAY-10) — coding guidelines, range `235b0b4..28b42a2`

Assessor: a fresh agent (Fable 5.1) following `elements/common/critique/SKILL.md`, given the
diff, its file list and the checkout at `28b42a2`; neither the task's chronicle nor the author's
reasoning was read. Read-only on the repository apart from this file; every command below wrote
its record into the assessor's scratchpad.

## The call

**Apply, with corrections.** The foundation entries are sound: every fingerprint the change
writes is current, every quotation of WAY-195 stands verbatim in its public source at the cited
line or page, the four format guards pass as the pre-`main` route runs them, and the
product-guidelines tests pass (138 tests, every `guidelines-check-*` invariant `pass`). Nothing of
the foundation change has to be cut. Two Important remarks ask for a wording and for the
styleguide skill and template to be brought under the obligation WAY-168 now puts on them; one
Important remark names clauses of a new invariant that no test breaks. What can be cut is small:
two *Avoid* words nobody has written, and the duplicated half of one installation test.

## What was checked, and the evidence

- **Fingerprints.** Every `WAY-NN@<fingerprint>` the diff holds (33 distinct) was recomputed with
  `relation-model/fingerprint.py` from the binding sentences of `foundations/decisions.md` at
  `28b42a2`: all current. The one mismatch is `WAY-168@47d9d53e`, which the diff only removes;
  no file at `28b42a2` still holds it. The fingerprints the invariants' *Derives from* carry
  (`WAY-167@052adf27`, `WAY-212@116bffdf`, `WAY-198@4dca82c6`, `WAY-199@9d0c758c`,
  `WAY-196@0e714a05`, `WAY-202@e0fb6a51`, `WAY-168@dc4a98a1`) are current. Six fingerprint
  constants of `test_form_check_invariants.py` were recomputed from their sentences: all match
  (`EXEMPLAR_DECISION`, `GUIDELINES_FORM`, `VALIDATES`, `LINT_DECISION`, `NO_AUDIT_DECISION`,
  `KIND_ONLY_DECISION`).
- **Format guards**, run as `agent-instructions/README.md` prescribes while the-way has no
  `main` (`--base none --merge-onto none`): decisions 0 errors (27 warnings, all the placeholder
  `merge of <request link>`, which the merge fills), invariants 0, glossary 0, part map 0 (with
  its standing `unchecked` lines). Run against `--base 235b0b4` instead, the decisions guard
  reports the in-place edit of WAY-167/1 (`decisions.md:5443`) and the invariants guard the
  in-place rewording of `guidelines-check-carrier/1` (`invariants.md:2163`, `3b699a99 →
  bde3cc86`); both are what the route allows before `main` ("edit an existing decision in place;
  do not manufacture a new decision version"), and WAY-167/1 and WAY-168/1 had their *Approved by*
  set back to the placeholder, so Mariusz accepts their changed meaning again (WAY-07). Not a
  remark; the human should know that two decisions approved at the merge of pull request 25 are
  re-accepted with new meaning, WAY-168 most of all (see I2).
- **Tests.** `python -B gate/run_tests.py product-guidelines` at `28b42a2`: `Ran 138 tests … OK`;
  the record gives `pass` to all nine `guidelines-check-*` invariants and no `fail`.
- **Source fidelity of WAY-195.** The seven Open Mercato files were fetched from
  `raw.githubusercontent.com/open-mercato/open-mercato/4374c48def1654927805c4b760f0e7f8648280f2/`
  and the paper from `storage.googleapis.com/gweb-research2023-media/pubtools/4365.pdf`
  (`pdftotext -layout`). Every quotation stands verbatim where cited: `AGENTS.md` lines 5, 16, 61,
  126, 144; `packages/core/src/modules/customers/AGENTS.md` lines 7, 16, 33;
  `apps/mercato/src/modules/example/README.md` lines 46–47; `.github/workflows/audit.yml` lines
  11 and 23–24; `.github/workflows/ci.yml` lines 436 and 503–506;
  `.ai/docs/agent-instructions.md` lines 22–24;
  `.ai/runs/2026-06-30-ts-morph-module-fact-sheets/PLAN.md` line 20. In the paper, the
  definition of an effective false positive and the sentence on a fix made anyway stand on
  printed page 59 (PDF page 2), the compiler-check criteria with "produce no effective false
  positives (the analysis should never stop the build for correct code)", "report issues
  affecting only correctness rather than style or best practices", "The primary goal of an
  analyzer …" and "up to 10% effective false positives" on page 62 (PDF page 5), and "tool
  writers take on the task of first fixing all the existing issues in the codebase" on page 66
  (PDF page 9). Authors, journal, volume 61 number 4, April 2018, pages 58–66: correct. The pieces
  the sentence says are left — the review skill, the lessons catalogue, the 32,768-byte limit
  with its chain ratchet, the generated fact sheets, the advisory DS lint, the daily audit of the
  unchanged graph, `--severity high` — are what those lines hold. No missing answer was completed
  from memory: every claim of the sentence has a cited line.
- **Code the invariants bind.** The three new sentences and the reworded carrier sentence were
  read against `product-guidelines/form_check.py` at `28b42a2` (`check_kind_index`,
  `check_exemplar`, `check_designation`, `check_cases`, `check_rule_cases`, `refused`,
  `fenced_blocks`): each clause of each sentence is a report the code makes, and the carrier
  sentence's "a file whose discipline's template requires an invariant in every rule" is read by
  the code from the template section itself (`form_check.py:428`), not hard-coded. Where the code
  reports more than a sentence says, see M1.
- **Contradictions and duplicates.** The twenty decisions were read against WAY-04, 07, 08, 19,
  22, 30, 51, 60, 62, 63, 68, 69, 76, 82, 86, 100, 114, 120, 122, 128, 129, 139, 161 and the
  styleguide family WAY-167 to WAY-192, and against both templates and the coding skill. Each
  coding decision mirrors a styleguide decision one to one (193↔173, 194↔174, 195↔175, 196↔188,
  201↔187, 205↔190, 207↔178, 208↔183, 209↔184, 210↔185, 211↔186, 212↔192), which is the pattern
  the approved styleguide family set; the alternative — widening those ten approved decisions to
  "a discipline's template" — would re-accept ten entries and cascade their fingerprints, so the
  mirror is the cheaper route and is not asked to be cut. Collisions found: I1 (WAY-203 against
  the template and WAY-204) and I2 (WAY-168 against the untouched styleguide skill and template).
  Overlaps that are not collisions: M3, M4.
- **Part map.** The new edge task-cycle → product-guidelines closes a cycle with the existing
  product-guidelines → task-cycle edge; the map at `235b0b4` already holds 236 such cycles among
  its fifteen parts (elements-common ↔ glossary, invariants ↔ environment-facts, …), so this adds
  no new condition. The two new failure modes name an existing invariant (the guard checks it).
- **Frequency of the problems.** None of the decisions rests on a claim about how often agents
  behaved some way; no session transcripts or run logs were given, and none were searched.
  WAY-209 and WAY-204 say themselves that their way of working is untried and set a review date.
- **Verification levels.** Every invariant a level-1 verification names derives from that
  decision (the invariants guard's `verification-invariant-derivation` passed): WAY-167 and
  WAY-212 → `guidelines-check-kind-index`; WAY-168 → `guidelines-check-carrier`,
  `guidelines-check-example-files`, `gate-guidelines-example-evidence`; WAY-196 →
  `guidelines-check-carrier`; WAY-198 and WAY-199 → `guidelines-check-exemplar`; WAY-202 →
  `guidelines-check-form`. `gate-guidelines-example-evidence/1` has *Method* `TODO`
  (`invariants.md:2247`), which the template allows, and WAY-197's "until a gate of the-way
  reports …" with its review date names the same debt once.

## Remarks by grade

### Critical

None.

### Important

**I1 — WAY-203's first sentence reads as one guidelines rule per linter rule.**
`foundations/decisions.md:6882`: "A rule of a linter's set stands as a rule of a product's coding
guidelines, checked by an invariant that blocks a change breaking it, only where …". Read alone,
it has each rule of the set stand as a `###` rule under `## Rules`. The coding template has one
rule `### Linter` whose adopting decision lists the rules that block
(`product-guidelines/coding/template.md:131-149`, `:231-233`), and WAY-204 says "the blocking
rules then stand in the adopting decision as the set less the rules it keeps among the examples".
The form check would accept a product that wrote a rule per linter rule, and a cycle's author
reading the log could. What would change: say where a blocking rule stands — e.g. "A rule of a
linter's set stands among the rules that block in the product's decision adopting the set, and is
checked by the invariant of the guidelines' `### Linter` rule, only where …". The rewording moves
WAY-203's fingerprint, carried by WAY-204's *Relations*; nothing else names it.

**I2 — WAY-168 now binds every discipline's guidelines, but the styleguide skill and template say
nothing of the test cases.**
`decisions.md:5510` (WAY-168's second sentence) and `product-guidelines/template.md:94-133`
("in the guidelines of every discipline") require, for each invariant a rule names other than
`guidelines-form`, a `good` and a `bad` file; `guidelines-check-example-files/1`
(`invariants.md:2233`) and the tests (`test_form_check_invariants.py:1302` ff., including "a
styleguide's rule with no case") enforce it on a styleguide. `product-guidelines/styleguide/SKILL.md`
and `product-guidelines/styleguide/template.md` were not touched: neither mentions a test case
(grep for "test case", "good", "```good": no match), the skill's *To do* sends the cycle's author
to the styleguide template's "Writing the file" alone (`styleguide/SKILL.md:50`), and no item
tells the author to write a case for each of the rules `### Each role in its meaning` (an agent's
k-of-n invariant, WAY-189), `### No value in place of a design token` (on the violated list under
WAY-190, so its cases take the violated-list reading) and the rest. A styleguide written as those
two files direct now fails the form check, and the author learns the obligation from the error.
This is a contradiction by omission between an edited approved decision and the files that apply
it, which the WAY-33 search of the whole foundation should have reached. What would change: the
styleguide template's "Writing the file" (and, as the coding skill does at `coding/SKILL.md:53-55`,
the styleguide skill's *To do*) point to "Test cases of a rule" of the common template, and say
which of the required rules' cases take the violated-list reading. No decision changes.

**I3 — Clauses of `guidelines-check-example-files/1` and `guidelines-check-kind-index/1` that no
invariant test breaks.**
`invariants.md:2233` says the check reports "every such block left open to the end of the file";
`test_form_check_invariants.py` holds no test that leaves a case open (grep "left open": none;
`:1384` closes a case early and asserts only that some error is reported in the file). The
ordinary tests (`test_form_check.py`) cite no invariant, so no deliberate break of that clause
backs the invariant's verdict. `invariants.md:2213` reports a row "whose *Kind* is not the
`<kind>` of the file its *File* names"; the code's separate report for a *File* that names a
tracked file of another form — `guidelines/testing.md`, `src/x.ts` — (`form_check.py`,
`check_kind_index`, "names no file `guidelines/coding-<kind>.md`") has no test
(`:1153` tests an untracked kind file, `:1168` a wrong *Kind*). What would change: one case each —
the file's last case with its closing fence removed, asserted at the opening line; a row naming
`guidelines/testing.md` with *Kind* `testing`, asserted at the row's line — both under the
existing `assert_reported_anew`.

### Minor

**M1 — Two new sentences say less than their check reports.** `invariants.md:2223` and `:2233`
report a path "absolute, holds a `..` segment, a drive or a UNC prefix"; `form_check.py` `refused`
also reports a backslash, a `:` and a character that is not printable, and the common template
says so (`template.md:119-120`); `check_rule_cases` also reports a case closed by anything but
three backticks (covered by the ordinary test `test_form_check.py:1129-1145`), which the sentence
does not say. This repeats the gap `guidelines-check-code-path/1` already has, so it is no new
kind of debt; the author may add "a backslash or a `:`" and "closed by anything but three
backticks" to the two sentences, or leave them as the minimum the check reports.

**M2 — *Avoid* words nobody has written.** `foundations/glossary.md:249` ("reference
implementation") and `:256` ("standing guard") appear nowhere in the repository outside the
glossary (grep over every `.md` and `.py`, `.runs/` excluded). The guard's search for a returning
word costs little, but the entries assert synonyms with no recorded use; whether either was seen
in a session cannot be measured from here. Can be cut to `none`; keep if the author saw them.

**M3 — WAY-212 restates the table WAY-167 gives.** `decisions.md:7223`'s second sentence ("Each
such file is named instead by a row of the table of `guidelines/coding.md`, by its path in
backticks with the condition under which to read it") repeats WAY-167's "a table naming each
other file of the discipline with when to read it" and adds only "path in backticks"; the entry
says so itself in its rationale. `guidelines-check-kind-index` derives from both. The sentence can
shrink to the `AGENTS.md` pointer and "no line of it names a file of a kind", leaving the table
to WAY-167; or stay, at the cost of two entries that say one thing.

**M4 — WAY-201 is one sentence on the audit WAY-200 settles.** `decisions.md:6817` could be the
second sentence of WAY-200 (`:6785`), as WAY-187 keeps the styleguide audit's ending in one
entry. One fewer entry to read and fingerprint; the author's split is defensible and is not asked
to change.

**M5 — The `NAMES` entry and the dedicated installation test cover the same ground.**
`installation/test_install.py:32` puts `maintain-coding-guidelines` under the loops of
`test_preview_apply_rerun_and_preserve_foundation` (the test that cites
`installation-claude-guidance/1`), which already check the wrapper's header, commit, `.the-way/`
path, every sibling's name, the guidance's naming of the skill and the ignored-path warning.
`installation/test_coding_guidelines_installation.py:58-125` asserts the same again (`:89`
header, `:97` sibling count, `:107` the block). `maintain-styleguide` never stood in `NAMES`
(`git log -S`: no commit), so the change departs from that precedent while keeping its dedicated
test. Keep the `NAMES` entry — it puts the new skill under the invariant-citing test — and the
dedicated test's unique parts: the refusal test (`:127`), the sibling count, the WAY-107 check
that the block names no product path (`:110`) and the preservation of a product's
`guidelines/coding.md`; the rest of its first test can be cut. Adding `maintain-styleguide` to
`NAMES` for the same reason lies outside this change.

**M6 — A fixture's cases could not decide the invariant they are cases of.**
`test_form_check_invariants.py:274`: the `good` and `bad` cases of `background-pair` are versions
of `src/tokens.css`, while that invariant's sentence is about the styleguide's table. The form
check never runs a method, so the test is sound; as an example an agent reads, it shows a pair
that could not make its invariant pass and fail. No change is needed; a short note in the
fixture's comment would do.

### Checked, no concern

- Every reference and relation fingerprint; the test fixtures' fingerprints.
- The quotations and page or line citations of WAY-195 (all verbatim), its *Based on* in the form
  the template asks (tools, date, commit, URLs), and its "left" items against the sources.
- `guidelines-check-carrier/1`'s new wording against the code that reads the template.
- The closed list of *Status* in WAY-199 against the template and the code; the "whitespace
  collapsed" clause of `guidelines-check-exemplar/1` against `names_in_backticks` and the test
  that wraps the exemplar decision over lines.
- The `"{fork-point}"` notation of `gate-guidelines-example-evidence/1`: the form the eleven
  existing sentences use.
- WAY-168's exemption of `guidelines-form`, WAY-188 and WAY-196 narrowing it, WAY-197 beside
  WAY-69, WAY-205 beside WAY-51 and WAY-60, WAY-206 beside WAY-68 and WAY-82, WAY-212 beside
  WAY-128, WAY-129 and WAY-107: no contradiction found.
- The new *Scope* values (`gate`, `task-cycle`, `instruction-files`, `decisions`) and *Part*
  values name parts of the map (the guards passed).
- The task-cycle skill's steps 10 and 11 against WAY-168 and WAY-197: consistent, including the
  violated-list reading and the scratch worktree.
- `README.md`, `installation/README.md`, `install.py`, the regenerated entry points: consistent
  with the new skill; the sibling count 32 is 16 skills in two directories.

## What can be cut

Nothing of the foundation entries or the invariant tests has to be cut. Cuttable: the two *Avoid*
words (M2); the duplicated half of the first test in
`installation/test_coding_guidelines_installation.py` (M5); at the author's choice, WAY-212's
restatement of the table (M3) and WAY-201 as a separate entry (M4).
