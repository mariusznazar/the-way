# Author return report — ai-review-fixes-from-24-11

**Status:** done. No correction was needed, so no commit was made; the head stays `2dca6873`.

## Return step (the record's form)

- **Foundation compared with code:** none of the entries compared no longer matches the code.
  - Entries the change writes or changes: WAY-12 (new third paragraph, `tests:` clause, rationale, rejected) matches `check_linked` — error where the change adds or alters the invariant's or the decision's whole entry, a listed line otherwise, the message giving the identifier and the decision "after `invariants:`". WAY-30 (new third paragraph, pair, rationale, rejected) matches the practice of this cycle: the *Verification* lines of WAY-48, WAY-235 and WAY-368 were written without a question before the code. *Verification* of WAY-48, WAY-235, WAY-368 names exactly the 15 invariants whose *Derives from* names them; the foundation check shows no `listed:` line.
  - Those the task names: WAY-18 ("the one exception … a decision's invariants, which its *Verification* names while each of them names the decision in *Derives from*") and WAY-114 (the merge is where the human accepts the line) are consistent with the new paragraphs and with the code; unchanged.
  - Those my search of the foundation found: WAY-17 ("an invariant derived from a decision names that decision", links written in the dependent entry) holds as it stands, WAY-18 being its recorded exception; WAY-03, WAY-61, WAY-71, WAY-344 (what the script lists or reports for invariants and for missing fields) are about other reports and match the code, which the change did not alter for them.
  - The search by the names and words the code adds (`check_linked`, `entry_texts`, "does not name it", "nothing holds", "held by nothing", "level 1 verification", "step 4.4"): the texts that say what the check reports are the docstring of the script, `agent-instructions/README.md`, the root `README.md` and the two templates' rows, all corrected in the change; no other text found, and the only remains of "level 1" are earlier-form fixtures of two tests.
  - Part map of the touched parts (`decisions`, `invariants`, `elements-common`, `task-cycle`, `agent-instructions`): the descriptions say the script checks a foundation's identifiers, references and assignment of files, which stays true; the change adds no file, and the foundation check reports no file unclaimed. Nothing to correct.
  - The pairs of examples: WAY-30's pair (one complies, two violates added by the cycle) holds nothing a test holds — the paragraph is a rule about approval that no test can check — so nothing is removed. WAY-12's pair was not extended; the existing pair stays for the part no test holds, since no `decision:` line cites the first paragraph's sentence on naming derived invariants (the tests cite the new paragraph). WAY-12's *Verification* names the tests that hold the new paragraph by the clause `tests:`.
  - The two reviews (`PASS 225bf1c5`, `PASS 2dca6873`) were read: neither holds a finding that bears on an entry. Their note on the file at 1193 lines (7 under the 1200 of WAY-385) is a note for the next change of the script, not an entry.
- **Decisions written or changed:** WAY-12 (new paragraph; row 2), WAY-30 (new paragraph; row 1), WAY-48, WAY-235, WAY-368 (*Verification* only; the cycle's, item 4 of *To do*).
- **Invariants written or changed:** none.
- **Environment facts:** none.
- **Glossary terms:** none.
- **Part-map changes:** none.
- **Projected entries written whole or in part:** none.
- **Rows of *Settlements to record* written:** row 1 — WAY-30 (a new paragraph); row 2 — WAY-12 (a new paragraph).

## For the request (not a correction)

WAY-30's added pair of examples is the writer's, so the entry stands as `the cycle's` in part and the request carries the pair word for word under it (the orchestrator's): complies — "a task that writes an invariant derived from a decision adds its identifier to that decision's *Verification* with no question, the line standing in the request's list of entries for the merge"; violates — "a cycle stops with a question for that human before the code only to add an invariant's identifier to a decision's *Verification*; a change rewrites a binding sentence of a decision under the cover of such a line".

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` → `0 errors`, exit 0, no switch, no `listed:` line.
- `git status --short` → empty; `git log --oneline -3` → `2dca6873`, `225bf1c5`, `07aa55df`.
- The full gate and the test directories were not run: nothing changed since the fix run of `agent-instructions` and `elements/common` (both exit 0).

## Unread material

Read in part: the part-map entries of the five parts (opening lines, with a search of their fields for what the check reports), not whole. The handoff, `task-cycle/skill/return_step.md`, the *Return step* of `task-cycle/record_template.md`, both review reports and WAY-17 were read whole.

## Searches not found or unclear

none.

## Working copies

None made; nothing to remove.
