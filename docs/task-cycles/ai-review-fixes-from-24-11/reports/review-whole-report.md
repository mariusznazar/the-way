PASS 225bf1c5eb30667afb8e5079f6d36d256aebd021

# Review of the whole change — ai-review-fixes-from-24-11

Range: `07aa55df565d5f10428176c89d20d2c6420a6dfd`..`225bf1c5` (one commit, one author, no plan, no slice). `git rev-parse HEAD` in the worktree is `225bf1c5eb30667afb8e5079f6d36d256aebd021`, the head given. Blocking findings: 0. Minor within the task: 1. Out of scope: 1.

## Verdict in short

Each of the five items of *To do*, both rows of *Settlements to record*, the four answers of *Questions to settle* and the acceptance criterion are met by the commit. The check does what item 3 and Questions 1-4 say, word by word. The fifteen links of item 4 are exactly the invariants whose *Derives from* names WAY-48, WAY-235 and WAY-368. I found no defect that blocks.

## Findings

### Blocking (Critical / Important)

none

### Minor

1. **Two wrapped lines in the new text run past the 100 columns of their paragraphs** (within the task; polish).
   - `README.md:94` is 105 characters (`whose sentence a change rewords while no file citing it changes. All of these compare the change with the`) and `agent-instructions/README.md:24` is 126 characters (`of the two entries as a whole, and lists any other such invariant. The script \`elements/common/migrate_foundation.py\` brings a`). Every other line of both paragraphs is 100 or fewer (README.md 86-93: 94-100; agent-instructions/README.md 17-23: 94-99), and on the base only one line of agent-instructions/README.md and none of the README paragraph passed 100.
   - Why it matters: nothing is wrong in meaning; the paragraphs were re-wrapped by hand and the joins left two long lines, which makes the next diff of the paragraph noisier.
   - Evidence: `awk '{print FNR": "length($0)}'` over the two ranges (output above). No script checks it.

### Out of scope (graded Minor, outside the task)

2. **`elements/common/foundation_check.py` now stands at 1193 lines, 7 under the 1200 of WAY-385.** Place: the file as a whole (`python -B task-cycle/change_file_sizes.py` gives 1115 -> 1193). The size test of the invariant `function-and-file-size` passes on the head, so the change breaks no threshold, and WAY-365 asks for a move out only for a change that adds to a file already over a threshold. But the next addition to this script will have to begin with a move of code out. The new code is in no way misplaced (`check_linked` stands beside `check_held`, as the task's *Context* says); this is a note for whoever changes the file next, not a defect of this change. Outside the task: a move of code out was not asked.

## Against the task, point by point

- **Item 1** (`task-cycle/skill/request_template.md`): the two accepted sentences stand at the end of point 6, after "(*Description*).", word for word (`Make each later edit as an edit of the part that changes, not a rewrite of the whole file. Where a script or a command has changed \`request.md\` since your harness last read it, read the file again before you edit it — your harness can refuse a write to a file changed outside it.`), only re-wrapped. Question 4 met.
- **Item 2** (`elements/invariants/skill/write.md`): step 4.4 reads exactly as the task gives.
- **Item 3** (`elements/common/foundation_check.py`, `check_linked`, called in `run` after `check_held`): for each invariant (earlier form skipped) the decision numbers are read from *Derives from* by `known_part` and `unquoted`, the same reading as the references check, so a `TODO` tail and a number inside a quoted source are no link. For each such decision of the log that has a *Verification*, the identifiers after `invariants:` are taken (the `@fingerprint` suffix dropped), and where the invariant is absent the report stands at the first line of that *Verification*. It is an error where the whole entry of the invariant, or of the decision (heading, every field, sentence, rationale, rejected, whitespace made one space), differs from the base or is absent from it — Question 2 "cały wpis, w dowolnym miejscu wpisu" — and otherwise a `listed:` line. The message names the invariant, the decision and "after `invariants:`". The docstring bullet is added. Where the base is unknown the entries count as unchanged and the gap is listed, the same convention as `check_held`; this keeps old gaps from becoming errors on every run without a history, and it follows from the settlement that every other gap is only listed. Tests of both cases and of the edges are in `elements/common/test_foundation_check.py` (10 tests, each expected message written out).
- **Item 4**: *Verification* of WAY-48 and WAY-235 gets the seven identifiers, WAY-368 gets `installation-paths-through-links`, in the form of the existing example (`invariants: a · b. For the rest, an agent compares …:` before the old pair). I checked it independently: a script over `foundations/invariants.md` lists exactly seven invariants deriving from WAY-48 and WAY-235 and one (`installation-paths-through-links`) from WAY-368, the same fifteen. No binding sentence of the three decisions changed.
- **Item 5** (`elements/invariants/skill/decide_entry.md`): the start of the sentence reads as the task gives; the rest is unchanged. A search for `level 1 verification` leaves only test fixtures (`test_foundation_check.py`, `test_migrate_foundation.py`), which are the earlier-form examples those tests need.
- **Acceptance criterion:** `python -B elements/common/foundation_check.py` on the head prints `0 errors`, no `listed:` line, exit 0 (run by me).
- **Row 1** (sentence of WAY-30) and **Row 2** (sentence of WAY-12): each stands as a new paragraph, as the *Context* asks (the earlier paragraphs are at the limit of three sentences). Row 1's paragraph says: a change to a decision's *Verification* that adds, removes or renames the identifier of a derived invariant and alters none of its binding sentences needs no approval before the code; the human accepts it at the merge with the request's entries (WAY-114); the agent asks no question. That is the row. Row 2's paragraph says: error where a change adds or alters either of the two entries as a whole, the message gives the identifier to add to which decision after `invariants:`, any other such invariant listed, the list stops no change. That is the row, with Question 2's "cały wpis" in the words "as a whole". Both paragraphs stay inside the limits of WAY-05 (the check passes, and it reports as error a decision over the limits that a change alters).

## The three points the orchestrator asked about

**(1) The additions to WAY-30 and WAY-12 beyond the sentence of the row.** Judged within the settlements; not a finding.

- WAY-30 *Verification*: one complies example and two violates examples were added to the pair the decision already carried. WAY-12 allows a pair "only for the part of its sentences that no invariant and no test checks"; no test or invariant can hold the new WAY-30 paragraph (it is a rule about approval), so a pair is allowed for it, and WAY-30 already had one. The two violates examples fit WAY-12's form: they describe a change that goes against the new paragraph while WAY-30's entry stays as it is — a cycle that stops with a question only to add an identifier, and a change that rewrites a binding sentence of some decision under cover of such a line (a change against WAY-30's first paragraph; the entry of WAY-30 is not what is rewritten). The pair does add a text that row 1 does not give, which WAY-114 already provides for: an entry marked as the cycle's because of a pair its writer added has that pair word for word in the request's list. The author's report names this for the request; the cycle must carry it there. No new meaning beyond the row is introduced by the examples.
- WAY-30 *Rationale* (one sentence) and *Rejected* (two options): the first rejected option is Question 1's "Not chosen" (b), the second is Question 1's "Not chosen" (a), in other words ("approval left to the merge with no sentence saying so — cycles then stop or settle each in their own way"). The rationale restates the same reasoning. Neither names a file, script or count, as WAY-05 requires of an author-written rationale.
- WAY-12 *Rationale* (the link written at both ends) and *Rejected* (three options): two are Question 2's "Not chosen" and the task's *Context* ("sam punkt 2, bez kontroli w skrypcie — sam tekst reguły już nie zadziałał"). The third, "an error for every such invariant — no change passes until all the older gaps are closed", is the author's, the mirror of WAY-12's existing "an error for every decision that nothing holds"; it is what row 2's "każdą inną taką lukę tylko wypisuje" already excludes, so it adds no meaning. WAY-12's *Verification* `tests:` clause names the new error and list in words, no path, no name, no number, as WAY-12 requires; its pair was not extended, which is right since tests hold the new paragraph (each carries `decision: WAY-12 "…"` lines that the script checks).
- WAY-05: the `Rationale` and `Rejected` of both entries name no file, script or count.

**(2) `README.md`, `elements/decisions/template.md`, `elements/invariants/template.md`.** Judged required corrections under WAY-33 and the task's own *Context*, not a widening.

- The task's *Context* (the line on what `foundation_check.py` reports) names three texts that also describe the reports: the paragraph of `agent-instructions/README.md`, the *Verification* row of "who reads it" in `elements/decisions/template.md`, and the *Derives from* row of `elements/invariants/template.md`. Each of the three now says what the check reports for an unnamed invariant; the template rows follow the WAY-05 rule "a field stays only while someone or something reads it" by naming the script as a reader.
- The root `README.md` paragraph is not in that list. It is an enumeration of everything the script "reports as an error" and "lists", written from the same list that would otherwise be left false by omission after the change. `README.md` is a file left out of the part map on purpose (it binds nothing, WAY-09), so no entry is changed by it and no test reads it; the edit is five lines of one paragraph, found by the author's search for "nothing holds" (WAY-33's search for the texts a change touches). I consider it a correction of the same class as the three the task names, not new scope. If the human prefers the paragraph untouched the cost is a stale list in a file that binds nothing.
- A search of my own for `nothing holds` and `held by nothing` finds the five files the change edits and the decisions file; no other text that describes the report was left.

**(3) The rule and the fifteen links.** Judged against item 3 and Questions 1-4 word by word above, and the fifteen against the invariants' *Derives from* (script over `foundations/invariants.md`; 7 + 7 + 1). I also ran a probe of the error path on a worktree of the head (below): with one identifier removed from WAY-368's *Verification* in the working tree, the script ends with exit 1 and the line `foundations/decisions.md:3676: \`installation-paths-through-links\` derives from \`WAY-368\`, whose *Verification* does not name it, and this change adds or alters one of the two entries: add \`installation-paths-through-links\` to the *Verification* of \`WAY-368\`, after \`invariants:\``.

## Against the foundation and the guidelines

- Entries the change writes or changes (WAY-12, WAY-30, *Verification* of WAY-48, WAY-235, WAY-368): each says what the code does and what the task settled; WAY-18's text ("one exception … a decision's invariants") and WAY-114 are read and unchanged and consistent with them. No glossary term is added or changed. The templates' rows and the two skill files say what the script does.
- Changed invariant tests: none changed or added in `foundations/invariants.md`; no invariant entry changed.
- The invariants of the touched parts that bear on the change (read whole; the 38 whose *Part* names `every`, `elements-common`, `decisions`, `invariants`, `task-cycle` or `agent-instructions`): `own-foundation-check-report` (the script on the head reports no error: met), `function-and-file-size` (test passes: met), `formatter-layout` and `ruff-blocking-rules` (ruff format and check pass on `elements/common`: met), `test-method-citation` (not changed). The others do not reach the change.
- `guidelines/coding.md` (whole), `guidelines/coding-check.md` (whole; `foundation_check.py` is a `copy` of the kind; its rules read `none — WAY-386`) and `guidelines/testing.md` (whole): "How a script starts and ends" is met by the docstring bullet; "Size of a function and a file" met (`check_linked` is about 55 lines against 110; the file is under 1200); "Test inputs and expected values" met — each test writes out the input and the expected message and the line numbers of the small log; "Where the expected value comes from" met — nothing is taken from the code under test; "Behaviour, not implementation" met — the tests assert the report lines and the count, and the one assertion on exact wording (the message with the identifier to add) is what item 3 requires the message to give. No reserved choice is taken.
- Code that passes a test without meeting the requirement: none found; the code has no branch or value made for a test input (the one special case, the unknown base, is the convention of `check_held` and stands in the task's rule for the listed line).
- The tests catch the break: the author reports seven of the ten failing with the call removed (and ten of ten having an input that decides them); my own probe above shows the error path on the real log. The ones that pass with or without the check (quoted source, no *Verification*, named in the same change) guard what the check must not report.
- Trust boundary: none; the change reads only the repository's own files. Irreversible operation: none.

## Structure of the code the change leaves

- `python -B task-cycle/change_file_sizes.py 07aa55df… 225bf1c5` (exit 0): `README.md` 246 -> 248; `agent-instructions/README.md` 136 -> 138; `elements/common/foundation_check.py` 1115 -> 1193 (+78); `elements/common/test_foundation_check.py` 2519 -> 2648 (+129); `elements/decisions/template.md` 354 -> 354; `elements/invariants/skill/decide_entry.md` 21 -> 21; `elements/invariants/skill/write.md` 9 -> 10; `elements/invariants/template.md` 188 -> 188; `foundations/decisions.md` 11851 -> 11895 (+44); `task-cycle/skill/request_template.md` 576 -> 579.
- Functions and files over a threshold: the test of the invariant (`agent-instructions/test_size_invariant.py`, 4 tests, OK) passes on the head; I ran it on the head only, since the base held no file over a threshold according to the merged request's green gate, and a pass on the head means no function or file is over. `foundation_check.py` stands 7 lines under its threshold (finding 2 above).
- Code with no user: `entry_texts` is used by `check_linked` only, and `check_linked` is called in `run`; no name stopped being true.

## Declined to judge

- The two gaps of loop2 (D-13, D-22): the task puts them out of scope (another repository); not judged.
- The script that writes the SHA of the cycle's record into `request.md`: the task's *Out of scope*; not judged.
- Whether Claude Code's refusal of a write to a changed file is as the added sentence describes: the sentence says "can refuse" on purpose, and the behaviour of a harness is outside the repository; not judged.
- The wording of the English sentences of the entries against the Polish of the task for meaning in the human's language: the Polish version belongs to the request's description (WAY-114, WAY-288), which this review does not see.

## Checks I ran (command and exit code)

- `git rev-parse HEAD`, `git log 07aa55df…..HEAD`, `git diff --stat` — 225bf1c5; one commit; 10 files, +282 −23. Exit 0.
- `python -B instruction-files/check_instructions.py` (the command `installation/README.md` gives, run from the root of the reviewed worktree) — `0 error, 0 warn, 5 info`. Exit 0. No warning.
- `python -B elements/common/foundation_check.py` — `0 errors`, no `listed:` line (counted with `grep -c listed`: 0). Exit 0.
- `python -B gate/run_tests.py elements/common` — 314 tests, OK. Exit 0.
- `python -B gate/run_tests.py task-cycle` — 570 tests, OK (skipped=2). Exit 0.
- `python -B -m unittest agent-instructions.test_size_invariant` — 4 tests, OK. Exit 0.
- `the pinned Ruff of the main checkout's quality virtual environment format --check --config ruff.toml elements/common` — 13 files already formatted. Exit 0. And `… check --config ruff.toml --ignore-noqa elements/common` — all checks passed. Exit 0.
- `python -B task-cycle/change_file_sizes.py 07aa55df565d5f10428176c89d20d2c6420a6dfd 225bf1c5` — table above. Exit 0.
- `python -B elements/common/decision_index.py --sections …` and `… --output .runs/review-whole/idx.md --section … --part … --decision …` — exit 0 each.
- A probe of the error path, in a worktree of `225bf1c5` at `.runs/review-whole/wt` (a one-line Python rewrite of `foundations/decisions.md` replacing `invariants: installation-paths-through-links. For the rest, an agent` by `invariants: cycle-stages-refuses-crafted-names. For the rest, an agent` in the *Verification* of WAY-368), then `python -B elements/common/foundation_check.py`: `1 error`, the line quoted under point (3) above. Exit 1 (as expected). No finding comes from it, so I keep no file of it in `reports/`.
- A script over `foundations/invariants.md` (regex over `## ` entries) listing the invariants whose *Derives from* names WAY-48, WAY-235 or WAY-368: 7, 7, 1 (the fifteen). Exit 0.
- Not run: the full gate (the cycle's own, not mine). The rest of the gate's directories (`agent-instructions`, `product-guidelines`, `instruction-files`, `project-level`) I did not rerun as a whole: the author ran them green and the change touches no code in them; I ran the size test of `agent-instructions` and the instruction-files check myself.

## Reaches beyond the dispatch

- `foundations/part_map.md` lines 1-82, 105-117, 154-192 (and a search for `README` in it): the entries of the parts `decisions`, `part-map`, `invariants`, `elements-common`, `task-cycle`, `agent-instructions` and the "Files left out on purpose" table, to name the parts the change touches and to learn that the root `README.md` binds nothing.
- `guidelines/coding.md`, `guidelines/coding-check.md`, `guidelines/testing.md` (each whole): the guidelines of the touched parts (`elements-common`, `agent-instructions`, `task-cycle`).
- `product-guidelines/reading.md` (whole), `elements/common/way_of_working.md` lines 60-140 ("Reading the foundation"): the method of my selection.
- `elements/decisions/template.md` lines 262-280 and `elements/invariants/skill/SKILL.md` (a search for step 4.4): to see whether other text describes step 4.4 or the *Verification* link; none does that the change left stale.
- A search of the whole repository for `level 1 verification`, `level 1 —`, `nothing holds` and `held by nothing`, to find stale text.
- `foundations/decisions.md` WAY-12 and WAY-30 whole entries, read at the lines 766-842 and 1290-1348 of the head.

## Working copies

- `.runs/review-whole/wt` — a worktree of `225bf1c5` for the probe; removed with `git worktree remove --force` and `git worktree prune`, by the full path.
- Files `idx.md`, `sections.md`, `inv.txt`, `ec.out` in `.runs/review-whole/` (the index of my selection, the list of sections, the invariants read, the output of the elements-common run): removed at the end of the review; nothing in them is needed by the report.

## Unread material

Decisions of the index of my selection read whole: **2** (WAY-12 and WAY-30, read as entries with *Verification*, *Rationale* and *Rejected*). The index listed 42 decisions in full and 135 by heading alone; the other 40 I read by their binding sentences and *Scope* in the index only, and those on the change I took further by their text in the task (WAY-18, WAY-114, WAY-48, WAY-235, WAY-368, WAY-385 are quoted whole in the task's *Decisions in play*, but I did not open their *Rationale* or *Rejected*; the rationale of WAY-48, WAY-235, WAY-368 and WAY-385 does not bear on a change of a *Verification* line or on the size of a file, which the size test checks; so none of them is "bears on the change and stayed unread" except as stated here). I did not run through the questions of the decisions outside the topical sections beyond the index's own list of headings (135 headings; none points to a bearing on the change). WAY-33, WAY-150, WAY-02 and WAY-05 I read by the index text only (WAY-05 and WAY-02 bear on the limits of binding sentences and on the reference form; the script's own checks of both pass).

Guideline files: each of the three I selected (`guidelines/coding.md`, `guidelines/coding-check.md`, `guidelines/testing.md`) I read whole. The other kind files of `coding.md` (`coding-measuring-report.md`, `-generator.md`, `-repository-changer.md`, `-command-runner.md`, `-shared-module.md`) I did not read: the change touches no file of those kinds.

Part-map entries: read whole for `decisions`, `part-map`, `invariants`, `elements-common`, `task-cycle`, `agent-instructions`. Not read: the glossary entries (the change adds or changes no term, and the foundation check, which reads the glossary, reports `0 errors`); `foundations/environment_facts.md` (no fact is named by the change).

## Searches not found or unclear

- Not found: a screenshot, a user interface or a trust boundary in the change; none was expected.
- Not found: any text outside the five edited files that still says what the check reports and is stale after the change (searched as listed above).
- Unclear: the author's note that the root `README.md` was edited "found by a search for nothing holds": the task's *Context* names three texts to correct, not four; I took the fourth as a correction of the same class (point 2). Unclear only in that the task does not say it; I raise it for the human.
