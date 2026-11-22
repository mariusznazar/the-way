# Author fix 1 report — installer-foundation-check-full-path

**Status:** done

**Commit:** `674c93fe` (on `task/installer-foundation-check-full-path`, after the reviewed head
`1c222ce2`). Files: `foundations/decisions.md` +2 / -1, `foundations/invariants.md` +1 / -1,
`installation/test_install.py` +6 / -2.

## Findings

### 1. WAY-418's *Verification* does not name the invariant — fixed

Through `record-decision` (`elements/decisions/skill/SKILL.md`, read whole, with `read.md` and
`decide_entry.md` at steps 1 and 2, and the template's sections "Changing a decision" and "Verification").
The entry is edited in place; its binding sentences, *Scope*, *Based on*, *Relations*, *Origin*,
*Rationale* and *Rejected* are untouched. The *Verification* now reads:

    - **Verification:** invariants: installation-agents-md-warnings. An agent compares a change with the
      part no invariant and no test holds:
      - complies: … (unchanged)
      - violates: … (unchanged)

The pair of examples stays word for word; only its introduction changed, as the template's form gives
(`invariants: <identifier>. An agent compares a change with the part no invariant and no test holds:`).
There is no `tests:` clause: the new test cites the invariant, not a sentence of the decision, and carries no
`decision:` line.

WAY-30 (a question for the human): I hold no question here. The edit adds the link WAY-12 requires and changes
no binding sentence, so it changes no meaning of an approved decision. My earlier reading of step 4.4 as
applying only where the verification "calls for" the entry was wrong: `write.md` says the verification
*gains* the entry, and `decide_entry.md:19` is a different step.

Check: `python -B elements/common/foundation_check.py` — exit 0, `0 errors` (run before the commit and the
files added to git).

### 2. The new test lets an error on the root `AGENTS.md` pass — fixed

The match is now `(?:ERROR|WARN) +\S+ AGENTS\.md:`, with a comment saying why an error counts (the same
break in a worse form: it stops a product's one command). The invariant's sentence still says "warning"
(the row's words, and WAY-418's); the test guards the worse level as well. I judged this the smallest fix
and a stricter test than the sentence is a cost-free direction; say if the sentence should name errors too.

The reviewer's mutation, shown failing after the change: the sentence about the part map in `product_guidance`
made to end with " See @docs/rules.md." (an edit of `installation/install.py` in the worktree, restored with
`git checkout installation/install.py` before the commit):

- `python -B -m unittest installation.test_install.InstallTest.test_a_fresh_installation_leaves_the_main_agents_md_without_a_warning`
  with the mutation: exit 1, `['ERROR at-import AGENTS.md:10 @docs/rules.md. — a punctuation mark right after
  the path stops Claude Code from loading it, without a warning'] != []`.
- Same command on the committed code: exit 0.

### 3. The sentence of the invariant can be read to cover the product's own lines — fixed

The sentence now ends "… reports no warning on the root `AGENTS.md` that the run created." (the wording the
reviewer gave). The test already builds an empty product, so a file the run creates; nothing in the test
changes for it. The entry's *Method*, *Rests on*, *Derives from*, *Part* and *Violated* are unchanged.

## Checks

- `python -B -m unittest installation.test_install.InstallTest.test_a_fresh_installation_leaves_the_main_agents_md_without_a_warning`:
  exit 0 on the committed code; exit 1 with the reviewer's mutation (above).
- `python -B gate/run_tests.py installation`: exit 0 (74 tests, OK, 676 s; run in the background and waited for).
- `python -B elements/common/foundation_check.py`: exit 0, `0 errors`.
- `python -B instruction-files/check_instructions.py .`: `0 error, 0 warn, 5 info`.
- Pinned Ruff of the main checkout (`the main checkout's .runs/quality-venv/Scripts/ruff.exe`):
  `format --check installation/test_install.py` exit 0; `check` exit 0, `All checks passed!`. The test line
  I wrote came out in the formatter's layout at once.
- Not run: the full gate, as the handoff says.

## Reaches beyond the dispatch

- `elements/decisions/template.md` ("Changing a decision", "Verification", the form of an entry) and
  `elements/decisions/skill/read.md`, `decide_entry.md`: named by `SKILL.md` at the steps; read for the edit.
- `elements/common/way_of_working.md`, step 4 (read from its heading to the end of the step): for the order
  of writing the entry and running the foundation check.

## Unread material

- `reports/review-whole-report.md` and the review's probe files: not mine, as the handoff says; the findings
  file I read whole.
- `elements/decisions/skill/projected.md` (projected mode): not read, as the mode does not apply.
- `elements/decisions/template.md`: read the sections named above and the form of an entry, not the whole
  file.

## Searches not found or unclear

none

## Working copies

None made in this fix beyond `.runs/author/installation.out` (the output of the long run, the last line its
exit code), removed; `.runs/author/` is empty.
