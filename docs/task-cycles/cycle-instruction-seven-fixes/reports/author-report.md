# Report of the one author — cycle-instruction-seven-fixes

**Status:** done with concerns (the concerns are the choices and the open points below; none blocks).

## Commits (branch `task/cycle-instruction-seven-fixes`, base `0b43a27d`)

- `2a0df03c` — Count a changed file that Read names by ranges by those ranges in the slice size (point 4(a): `task-cycle/slice_size.py`, `task-cycle/test_slice_size.py`)
- `fc88ee2c` — Settle seven gaps of the cycle's instructions (points 1, 2, 3, 4(b), 4(c), 6, 7: `task-cycle/skill/SKILL.md`, `task-cycle/plan/SKILL.md`, `task-cycle/change/SKILL.md`, `task-cycle/review/SKILL.md`)
- `bcaddc2b` — Record the settlements of the seven fixes in WAY-136, WAY-255, WAY-134 and the decision template (point 5 and rows 1–3: `elements/decisions/template.md`, `foundations/decisions.md`)

## Files changed (added / removed lines, `git diff --numstat 0b43a27d..HEAD`)

| File | + | − |
|---|---|---|
| `elements/decisions/template.md` | 5 | 2 |
| `foundations/decisions.md` | 55 | 23 |
| `task-cycle/change/SKILL.md` | 4 | 2 |
| `task-cycle/plan/SKILL.md` | 3 | 1 |
| `task-cycle/review/SKILL.md` | 2 | 1 |
| `task-cycle/skill/SKILL.md` | 20 | 7 |
| `task-cycle/slice_size.py` | 17 | 11 |
| `task-cycle/test_slice_size.py` | 31 | 0 |

## Points, one by one

1. `task-cycle/skill/SKILL.md`, the paragraph "The cycle writes only in the task's worktree": the clause is in the list after "the account of the request named below", joined by a comma, so the list reads "…named below, the screenshot shown to the human, which goes to the place the product's foundation settles for screenshots ("Working copies" below), and the registry…".
2. Same file, sub-step 5 of step 9: the sentence of the task follows "…the review of the whole change judges it (WAY-136)." in the quoted words.
3. Same file, after "…answering that subagents should return findings as text.": the two sentences in the quoted words. `task-cycle/remarks_check.py` exists (checked).
4(a). `task-cycle/slice_size.py`: docstring paragraph and code, with tests (below). 4(b). `task-cycle/plan/SKILL.md`: the sentence follows the bullet on foundation entries in *Read*; the bullet's closing `;` after "only when written" became a full stop and the new sentence ends with the `;`, so the list keeps its form. 4(c). `task-cycle/change/SKILL.md`: the list item reads as the task gives it.
5. `elements/decisions/template.md`: the replacement in the quoted words, in the bullet on the *Rejected* of a decision written from a row.
6. `task-cycle/change/SKILL.md` and `task-cycle/review/SKILL.md`: the replacement in the quoted words in both.
7(a). `task-cycle/skill/SKILL.md`, section "Working copies", end of the first paragraph: the new sentence, in the quoted words. 7(b). Step 2 of "The record before it is committed": "Remove an earlier copy, by its path written out in full, then copy the whole record directory to `docs/task-cycles/<task-slug>/` on the task branch and rewrite its links to the committed copies."

### Quotation versus file (the checkout stands at a later commit than the one the task was checked on)

The places were all found as quoted, at lines near the hints (shifted a few lines). No place failed to match.

## Point 4(a): what the code does

- Before: a file of *Change* that exists was counted whole whatever *Read* named of it.
- After: a file of *Change* that exists and that *Read* names by ranges counts the lines of those ranges; a file of *Change* that *Read* does not name counts whole; a file that *Read* names whole counts whole.
- Choice (named): where *Read* names the same file both whole and by ranges, the file counts whole. The task's sentence ("A file of *Change* that *Read* names by ranges counts the lines those ranges name; any other file counts whole where either field names it whole…") can be read both ways for that case. I kept the existing behaviour (whole wins, as `test_changed_file_named_again_in_read_counts_once` already had it) and added one sentence to the docstring after the quoted one: "a file that *Read* names whole counts whole, whatever ranges of it *Read* names beside." Way rejected: ranges win over a whole entry of *Read* — it would make an explicit whole reading count less than it is. Cost if wrong: one condition in `measure` and one sentence plus one test.
- Internal change: `whole` is now a `set[Path]` (its values were never read).
- The size rule (WAY-385: a function at most 110 lines, a file at most 1200): `slice_size.py` is 253 lines and `measure` about 50, so no move-out commit was needed (WAY-365 does not apply).

## Tests

Three tests added to `task-cycle/test_slice_size.py`, expected values written out in the test with their derivation in a comment:

- `test_changed_file_that_read_names_by_ranges_counts_only_those_lines` — a log with a first line of 400 000 characters, *Change* and *Read* `:2-3`: expects 8 characters, 4 tokens, `fits`. It catches the old behaviour (counting the whole file, 160 004 tokens, `too large`) — a bug, not a decision. Seen failing first: `python -B -m unittest task-cycle/test_slice_size.py` → `AssertionError: 1 != 0` in this test, 1 failure of 19 (the shell pipeline hid the exit code in that run; the failure itself is the run's FAILED line; exit code of the non-piped rerun after the code is 0).
- `test_changed_file_that_read_names_whole_and_by_ranges_counts_whole` — 14 characters, not the 4 of the range; protects the choice above (a mutation making ranges win fails it).
- `test_changed_file_that_read_does_not_name_counts_whole` — *Change* `log.md` (8 characters) and *Read* a range of another file (2 characters): expects 10; protects the case of a changed file untouched by any range (a mutation that drops such a file fails it).

## Checks (command and exit code)

| Check | Command | Exit |
|---|---|---|
| New test red, before the code | `python -B -m unittest task-cycle/test_slice_size.py` | non-zero (1 failure, 19 tests; shown through a pipe, so the shell printed the pipe's code) |
| New tests green, after the code | `python -B -m unittest task-cycle/test_slice_size.py` | 0 (19 tests OK) |
| Directory of the code | `python -B gate/run_tests.py task-cycle` | 0 (537 tests, 2 skipped on Windows) |
| Foundation check | `python -B elements/common/foundation_check.py` | 0 (0 errors) |
| Tests of the elements | `python -B gate/run_tests.py elements/common` | 0 (271 tests) |
| Entry points and copies | `python -B gate/run_tests.py agent-instructions` | 0 (52 tests); no description changed, so `skill_entry_points.py --write` and `agent_type_copies.py --write` were not needed and not run |
| Instruction files | `python -B gate/run_tests.py instruction-files` | 0 (105 tests, 5 skipped) |
| Guidelines | `python -B gate/run_tests.py product-guidelines` | 0 (14 tests) |

Not run: the full gate (`python -B gate/run_tests.py` with no directory) — by the handoff and the user's rule for this cycle. `ruff` is not installed in this session (`ruff: command not found`, `No module named ruff`), so I ran no linter or formatter by hand; the invariant tests of the linter and formatter sit in `agent-instructions` and passed there.

## Own-work check (WAY-164)

- The requirement my work most likely does not meet: point 4 as a whole — that a slice which changes a large decision log and names a range of it in *Read* is measured by the range and no longer comes out "too large" (the need in the task: every slice that changes one decision came out too large), while a slice that names no range still counts the whole file.
- The check: a plan of two slices against the real `foundations/decisions.md` (916 K characters) in this worktree, run with `python -B task-cycle/slice_size.py <plan> --root` default from the worktree root: slice 1 (*Change* the log, *Read* `foundations/decisions.md:6243-6338`) and slice 2 (*Change* the log, *Read* only `task-cycle/slice_size.py`).
- What it showed: with my change, slice 1 = 8 521 characters, 3 409 tokens, `fits`; slice 2 = 916 646 characters, 366 659 tokens, `too large`. On the stashed base (before my code), slice 1 = 902 521 characters, 361 009 tokens, `too large`; slice 2 = 913 213 characters, `too large`. So the range narrows the measure and the gap for a slice with no range is kept, as the task wants.
- Mutation in the head (no tool adopted, WAY-402): wrong branch order (ranges beating a whole *Read*) — caught by the second test; a changed file dropped when *Read* names a different file's ranges — caught by the third; counting the whole file as before — caught by the first; a range beyond the file in *Read* of a changed file still gives `unchecked` — not retested by me (unchanged code path; `test_range_beyond_the_file_leaves_the_slice_unchecked` covers it for a file not in *Change*).
- Behaviour the user sees in the running product: none (a script of the process and texts of skills; no screen, API answer, terminal command of a product or data of a product). No walkthrough (`walkthrough.md` not read, for that reason).

## Foundation step (rows 1–3; `task-cycle/skill/foundation_step.md` read whole)

All three rows were written into the place their column names. Corrected after the review of the whole change (finding 1): each of the three entries carries examples that its row does not give, so each is marked **`the cycle's`** (`foundation_step.md`: a part the writer adds that its row does not give — a pair of examples — makes the entry `the cycle's`), and each row's meaning also stands in it (`row 1`, `row 2`, `row 3`). No `decision:` line cites WAY-136, WAY-255 or WAY-134 (grep), so no test holds the pairs. The added clauses of *Verification*, word for word (they were added to the existing `complies:` / `violates:` clauses of each entry):

- WAY-136, complies: "a change that rewrites many entries of the foundation from many notes has the slices without a review of their own reviewed in groups, in the plan's order, the grouping and its reason recorded"; violates: "reviews of groups of slices are dispatched with no grouping and reason recorded, or by a measure in place of the orchestrator's judgment".
- WAY-255, complies: "and returns its report after reading the result"; violates: "an agent ends its turn with a note that it still waits for the tests it started in the background, in place of their result".
- WAY-134, complies: "a decision row whose source keeps a way with only the cost of a gate to reopen gives that way `no cost to the product known` in the decision's rejected options, and leaves out the way that only chose when the answer is recorded"; violates: "the cycle puts in the rejected options a way of the process, such as when an answer is recorded, or leaves a way whose source keeps no cost without the words `no cost to the product known`".

**Row 1 — sentence of WAY-136** (`foundations/decisions.md`, entry WAY-136, first paragraph; also *Verification*, *Rationale*, *Rejected*).
- English: Where the slices that have no review of their own are more than one reviewer of the whole change can compare with their sources, the orchestrator may, by its own judgment and not by a measure, dispatch reviews of groups of them in the plan's order, as for a slice with a review of its own, and it records the grouping and its reason.
- Polski: Gdy kawałków bez własnego przeglądu jest więcej, niż jeden recenzent całości porówna ze źródłami, prowadzący może z własnego osądu, a nie z miary, zlecić przeglądy ich grup w kolejności planu, tak jak dla kawałka z własnym przeglądem, i zapisuje podział z powodem.
- *Rejected* reconciled as *Decisions in play* asks: "a review of every slice" became "a review of every slice as a rule … while the review of the whole change still reads every slice that one reviewer can compare with its sources"; and one way kept by the row's source was added — a criterion for the reviews of groups taken from a measure of the slices' size, with its cost beside it (off in two directions: a file read by several slices counts several times, the diff a reviewer reads counts not at all, a slice left unchecked has no size). The way "only the skill, the decision unchanged" stays out as a way of where the answer is recorded (see Choices). *Rationale* got the reason of the groups' reviews.

**Row 2 — sentence of WAY-255** (entry WAY-255; also *Verification*, *Rationale*).
- English: An agent that waits for a command that runs long by running it in the background ends its turn only after the command has ended and it has read its result.
- Polski: Agent, który czeka na długie polecenie, puszczając je w tle, kończy turę dopiero, gdy polecenie się skończyło i przeczytał jego wynik.
- Form: the entry's first paragraph already has three sentences (template: one to three), so I put the rule into its first sentence as a clause ("…never in one wait past it, and ending its turn only after the command has ended and it has read its result; …") instead of a fourth sentence. *Rejected* of WAY-255 is unchanged (see Choices).

**Row 3 — sentence of WAY-134** (entry WAY-134, first paragraph; also *Verification*, *Rationale*) and `elements/decisions/template.md` (point 5).
- English: A way not chosen that the row's source keeps with no cost, or with only a cost of the process such as a gate to reopen or a step to repeat, stands in the rejected options with `no cost to the product known`, and a way that is itself a way of the process rather than of the product, such as how or when an answer is recorded, stays out of them.
- Polski: Wariant, który źródło wiersza zachowuje bez kosztu albo tylko z kosztem procesu, np. bramką do ponownego otwarcia albo krokiem do powtórzenia, wchodzi do odrzuconych wariantów z `no cost to the product known`, a wariant będący sposobem procesu, a nie produktu, np. jak albo kiedy zapisać odpowiedź, do nich nie wchodzi.
- *Rejected* of WAY-134 unchanged: the source of row 3 (point 5 and the first question) keeps no way not chosen for point 5.

Search of the whole foundation (WAY-33), done once: entries that name WAY-136, WAY-255 or WAY-134 (grep of `foundations/*.md` for the numbers) — WAY-100 and the decision at line ~254 (which cite WAY-134 for where the left-out parts come from) are unchanged in meaning; no decision found that derives from or narrows one of the three and states a sentence now false. Instruction files that cite WAY-134 (`project-level/task/template.md`, `find_settlements.md`, `elements/common/skill/task_variant.md` and others) say that the *Rejected* is "taken from" the ways the source keeps and none restates the `none considered` / `unknown` rule against the new sentence. `task-cycle/skill/foundation_step.md` states the *Rejected* rule shortly "as the decisions' template gives" and so now says less than the template; I left it, since it points to the template (see open points).

## Choices (with the way rejected and the cost if wrong)

1. **Whole beats ranges where *Read* names a file both ways** (point 4(a)) — described above.
2. **Row 2 and row 1: ways of the source that stay out of *Rejected*.** The source of row 2 keeps two ways ("only the two skills, the reference (WAY-255) stays"; "only the two skills, the reference moved to the part on waiting"); the source of row 1 keeps "only the skill, the decision unchanged". I judged all three to be ways of where the answer is recorded, hence ways of the process, which the sentence of row 3 (point 5) keeps out. Way rejected: write them into *Rejected* with the cost the source gives beside each (the reference claims what the decision does not say; the rule living in two skills may drift). Cost if wrong: a reviewer reads WAY-255 as having dropped ways the source kept; the fix is two clauses in its *Rejected* and one in WAY-136's.
3. **Row 2 as a clause, not a fourth sentence** — above. Way rejected: a second paragraph (the template allows one only for a part of another question). Cost if wrong: a template-form finding (Minor under WAY-364 unless a sentence is read wrongly).
4. **Point 4(b)**: the `;` at the end of the bullet became a full stop and the new sentence ends in `;`. Way rejected: appending after the `;` with a capital letter. Cost: none beyond form.
5. **Verification and Rationale of the three decisions were extended** with the new sentence's case (the task names only the sentences and *Rejected*). Way rejected: leave them as they were, so that the decisions' pair of examples would not cover the new sentence. Cost if wrong: a few lines removed.
6. Point 2 in the decision names the actor as "the orchestrator" (the decision's own word), the skill says "the lead" (the task's word for the skill).

## Reaches beyond the handoff

- `instruction-files/SKILL.md` and `instruction-files/kind_skill.md`, whole, as the handoff says "also read `instruction-files/` if its skill applies" — to judge the form of a sentence in the four skills (they give no change to the wording).
- `elements/decisions/skill/read.md`, `decide_entry.md`, `elements/common/way_of_working.md` and `elements/common/rules.md`, whole, and `elements/decisions/examples.md` (it names WAY-03 only; WAY-03 itself I did not open) — the files `elements/decisions/skill/SKILL.md` and `foundation_step.md` send a writer of a decision to read.
- `foundations/decisions.md:6230–6313` (WAY-136), `6657–6696` (WAY-255, then the *Rejected* at the end of the entry), `5480–5610` (WAY-134), `5612–5656` (WAY-140), `6314–…` (WAY-148), `6827–6864` (WAY-373), `8073–…` (WAY-316), `10957–…` (WAY-385, the thresholds for the size rule) — the entries named by the handoff, and WAY-385 as an addition to decide whether `slice_size.py` was over its threshold.
- Greps: `decision:\s*WAY-(255|136|134)` (no test cites these decisions); `reading its output between them|Every file you change, whole|…` and `that makes a working copy to check something` (the sentence of the "Working copies" paragraph that handoffs copy word for word stands only in `task-cycle/skill/SKILL.md` and in WAY-373); `none considered`; `WAY-(136|255|134)` across the repository; `ls task-cycle/remarks_check.py`; `Events` in `task-cycle/record_template.md` (the table the point 3 sentence names exists, line 102).
- `the author's own rule on commits (a file outside the repository)` (user's rule before a commit).

## Working copies

- `.runs/author/` of the worktree held the outputs of the test runs and one test plan for the own-work check. Removed (`rm -rf` with the path written out in full); `.runs/` now holds `task-cycles/` only. A temporary stash of my own uncommitted change (for the check on the base) was popped at once; no stash remains.

## Unread material

- `foundations/decisions.md`: read by the entries and ranges named above, not whole (as the handoff says); `WAY-140`, `WAY-148`, `WAY-316`, `WAY-373` read whole except that the output of WAY-316 ended at its *Rationale* (lines 8123–8132 read; the rest of that entry's *Rationale* and *Rejected*, after line ~8132, was not read) and WAY-148's *Rationale* ended at its first paragraph (lines up to ~6373); `WAY-140`'s *Rejected* — the entry has none at the end of the range I read (lines 5612–5656) and I did not check further. These four are decisions the change does not touch.
- Examples: `WAY-03`, named by `elements/decisions/examples.md`, not opened.
- `orch_index.md`: read whole.
- Everything else the handoff names was read whole: the task, `foundation_step.md`, the three guidelines, the element's skill and template, the files of the change.

## Searches not found or unclear

- `ruff` not available in the session (`ruff: command not found`): the linter and the formatter were not run by me directly.
- The task's sentence for point 4(a) is unclear for a file that *Read* names both whole and by ranges (see Choices 1).
- The task's point 5 leaves open whether a way such as "only the skill, the decision unchanged" is a way of the process (see Choices 2); the template sentence names "how or when an answer is recorded" as an example, and where the rule is recorded is the nearest case.
- Whether `task-cycle/skill/foundation_step.md` (the sentence "a decision's *Rejected*, which takes the ways not chosen that the row's source keeps, `none considered` where the human said so, or `unknown`, as the decisions' template gives") should carry the new words: unclear, since the task does not name that file; I left it.

## Questions for the orchestrator

None blocking. For a decision, with the answer I recommend: (a) point 4(a), both-ways case — keep whole (recommended); (b) the ways of Choices 2 — keep them out of *Rejected* as ways of the process (recommended; the reviewer of the whole change may judge otherwise and the cost is two or three clauses).

## Problems as observed

None found in the code or tests. One observation: the task's *Decisions in play* says the *Rejected* of WAY-136 is to be reconciled with the new sentence; I did it by narrowing "a review of every slice" to "as a rule" and adding the reading condition, which is an edit of a sentence of *Rejected* the task asked for, not one it quoted.
