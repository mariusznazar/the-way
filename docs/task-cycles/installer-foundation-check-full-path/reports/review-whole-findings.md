# Findings of the review of the whole change (`reports/review-whole-report.md`, FAIL 1c222ce238c2194900ec246de5f8cc6cfa7faa5b)

Copied from the reviewer's report in its words. Blocking finding first, then the Minor findings of the review of the whole change within the task, which the same fix covers (none is marked outside the task's scope).

## Blocking

**1. WAY-418's *Verification* does not name the invariant the change derives from it**
(`foundations/decisions.md:3349`, the entry WAY-418, against `foundations/invariants.md:334-342`).

The change adds the invariant `installation-agents-md-warnings` with `**Derives from:** WAY-418`.
WAY-418's *Verification* still holds only its pair of examples ("an agent compares a change with the
decision: complies … violates …") and has no `invariants:` clause. The foundation requires that link
in three places:
- WAY-12 (`foundations/decisions.md:768-770`), binding: "A decision names in *Verification* the
  invariants derived from it, by the identifiers of their entries, where such invariants exist".
- The decision template's section "Verification" (`elements/decisions/template.md:270-272`):
  "*Verification* names, after `invariants:`, the invariants of the product's invariants file that
  derive from the decision, each by its identifier, and only where such invariants exist; each of
  them names the decision in *Derives from*".
- The step of the invariants skill that the author's entry went through
  (`elements/invariants/skill/write.md:5-6`): "Step 4.4: what follows from this entry is a decision
  whose level 1 verification gains, loses or renames it, through `record-decision`."

The author's report reads step 4.4 as applying only to a decision whose verification "calls for"
the entry. That wording belongs to `decide_entry.md:19`, which governs the search for a decision
that asks for a rule. `write.md` says that the decision's verification *gains* the new entry. The
orchestrator left the decision unchanged because no row of *Settlements to record* asks for the
edit. Row 2, though, settles an invariant that derives from WAY-418, and WAY-12 makes the link a
part of writing such an invariant. It is no further change of meaning.

Why it matters: by the template's table of fields (`elements/decisions/template.md:130`),
*Verification* is where "whoever looks for the checks of the decision" finds its invariants. Someone
reading WAY-418 sees only an agent's comparison and does not learn that a test now holds part of it.
A later change of WAY-418 would then miss the invariant and its test. `elements/common/foundation_check.py`
does not check this link, so it passes with 0 errors and nothing else would catch the gap.

Evidence: the probe `reports/review-whole-probe-derived-links.py` lists, for each invariant, every
decision in its *Derives from* whose *Verification* does not name it.
- On the head: "16 of 75 links not named" (`reports/review-whole-probe-derived-links-head.txt`).
- On the base: "15 of 74" (`reports/review-whole-probe-derived-links-base.txt`).
- The one new gap is `installation-agents-md-warnings <- WAY-418`. The other 15 are older
  trust-boundary invariants (see **Declined to judge**). Elsewhere in the-way 59 of 75 links follow
  the rule, `installation-claude-guidance` in WAY-141 among them.

Fix: through `record-decision`, WAY-418's *Verification* gains
`invariants: installation-agents-md-warnings.` in the form the template gives at
`elements/decisions/template.md:42-44`. Its pair of examples stays and is introduced as covering the
part no invariant holds ("An agent compares a change with the part no invariant and no test
holds:"). The invariant covers only the installer's block in a fresh product. The examples cover
every change that names a path and the grading done by the review. The binding sentences do not
change.

Contradiction: yes — WAY-12 (and the rule of `elements/decisions/template.md` § Verification that
carries it).

## Minor findings within the task

**2. The new test lets an error on the root `AGENTS.md` pass** (`installation/test_install.py:454`).

The assertion keeps only lines that match `WARN +\S+ AGENTS\.md:`. A sentence of the block that the
checker reports at the level `error` passes the test. The checker exits 1 on that error, and the
test does not assert the exit code. In a product such an error stops the one command, which is worse
than the warning this test guards against. No test of the-way runs the checker on the block, so the
first sign would be every product's gate going red after the next pin move.

Evidence:
- `reports/review-whole-probe-mutations.py error-line` inserts "See @docs/rules.md." into the
  block's sentence about the part map. The new test then passes, exit 0
  (`reports/review-whole-probe-error-line.txt`).
- On a file holding that same line (`reports/review-whole-probe-error-line-AGENTS.md`), the checker
  reports `ERROR at-import AGENTS.md:3 @docs/rules.md. — a punctuation mark right after the path
  stops Claude Code from loading it` and exits 1.

Suggested fix: match `(ERROR|WARN) +\S+ AGENTS\.md:` too. This lies within the task, since it
concerns the test that To do item 2 asks for, but it goes beyond the warnings that item names.

**3. The invariant's sentence can be read to cover the product's own lines of `AGENTS.md`**
(`foundations/invariants.md:336`).

The sentence: "In a product made by a full run of the installation command, before any skill of
the-way has run in it, the script that checks instruction files, run on the product's root,
reports no warning on the root `AGENTS.md`." The installer also runs on products that already
exist, which keep their own text in `AGENTS.md` outside the marked block (WAY-28, the part-map
entry `installation-command`). For such a product, a path that the product's own lines name and
that does not exist makes the sentence false, and no change of the installer can prevent it. The
test builds only an empty product (`test_install.py:442`), so it checks the narrower reading.

My reading of "made by" is a product the run creates, and on that reading the code meets the
sentence, so this is a matter of form (WAY-364), not of content. A reader weighing a change to how
the installer treats an existing `AGENTS.md` could still read it as a rule the installer cannot
keep. A wording that removes the doubt: "…reports no warning on the root `AGENTS.md` the installation
command created". This lies within the task: row 2 of *Settlements to record* carries the same
breadth.
