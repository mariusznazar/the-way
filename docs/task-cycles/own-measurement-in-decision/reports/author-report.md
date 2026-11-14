# Author report — own-measurement-in-decision

**Status:** done with concerns (two decisions the task or the search touches were left unchanged on purpose, see "Concerns")

**Commit:** `c76debc` on `task/own-measurement-in-decision` (one commit; worktree clean).

## Files changed

| File | Added | Removed |
|---|---|---|
| `foundations/decisions.md` | 85 | 31 |
| `elements/decisions/template.md` | 6 | 0 |
| `elements/environment-facts/template.md` | 6 | 0 |

## Checks run

| Command (from the worktree root) | Exit |
|---|---|
| `python -B elements/common/foundation_check.py --skip-test-citations` | 0 (`0 errors`) |
| `python -B gate/run_tests.py elements/common` | 0 (144 tests OK) |
| `python -B task-cycle/private_paths_check.py` on `foundations/decisions.md`, `elements/decisions/template.md`, `elements/environment-facts/template.md` | 0 each, `0 listed` |
| `python -B -m unittest task-cycle.test_tracked_files_private_paths` (the test of invariant `tracked-file-private-paths`) | 0 (1 test OK) |

Not run: the full gate (the cycle's run), by the handoff. No invariant is written or changed, so no
invariant test was seen failing.

## Own-work check (WAY-164)

- **Requirement most likely missed:** *To do* item 3 reaches "each decision whose rationale gives the
  result of such a measurement", so a decision with such a figure that I did not find would stay
  without the sentence.
- **Check:** a throwaway script (not committed) split `foundations/decisions.md` by entry and, for the
  prose after `*Rationale:*` (which includes *Rejected*), searched for figure signatures (`N of M`,
  `N%`, `measured`, `probe`, `counted`, `on 2026-..`, `median`, `N runs/cycles/slices/rows/errors`).
  It printed each entry with a signature, with or without the sentence "this product's own".
- **What it showed:** all 19 entries I edited carry the sentence. Entries with a signature and no
  sentence: WAY-52, 58, 60, 77, 85, 131, 304, 324, 329, 337, 338, 339, 344, 346, 348, 351, 354, 359,
  370 are figures of a rule's text or a counted rule, not a result (I read each hit); WAY-312 has a
  fact with an open source (below); WAY-256 is unclear (below). Earlier greps over `decisions.md` for
  `measur|trial|probe|2026|N of M|N%|session records|game|one product` found the other entries.
  The first run of the check was this one; it did not fail. A first version of it was not kept.

## Foundation entries (WAY-134)

Marks: `row 1`, `row 2`, `projected`, `the cycle's`. All carry the row meaning; the wording is mine.

| Entry | English | Polish | Mark |
|---|---|---|---|
| WAY-90 (edited in place; binding part, *Verification*, *Rationale*, *Rejected*) | A measurement the product's own people made, whose record a reader cannot open, is no *Based on* citation: its result stays in the decision's prose with what was measured and the conditions, the prose says the measurement is the product's own and its record is not open to a reader, and no fact entry is written for it. | Pomiar zrobiony przez ludzi produktu, którego zapisu czytelnik nie otworzy, nie jest cytatem *Based on*: jego wynik stoi w prozie decyzji z tym, co mierzono, i warunkami, proza mówi, że pomiar jest własny, a jego zapis niedostępny dla czytelnika, i nie zakłada się dla niego wpisu faktu. | row 1 + row 2 |
| `elements/decisions/template.md` (new point after the point on *Based on*) | Same as WAY-90, for a decision's author. | To samo co WAY-90, dla autora decyzji. | row 1 + row 2 |
| `elements/environment-facts/template.md` (new point in "Which facts are written", after the point on a finding of a study) | Same as WAY-90, for the writer of a fact: such a measurement is written as no fact. | To samo co WAY-90, dla piszącego fakt: taki pomiar nie jest zapisywany jako fakt. | row 1 + row 2 |
| WAY-229, WAY-164, WAY-364, WAY-136, WAY-371 (rationale / *Rejected* sentence only) | The reviewer-class, plan-versus-author and similar figures are this product's own measurement and their record is not open to a reader. | Liczby o klasie recenzenta, planie i autorze itd. to własny pomiar tego produktu, a jego zapis jest niedostępny dla czytelnika. | row 2 (carried by the cycle's item 3) |
| WAY-255, WAY-300, WAY-308, WAY-309, WAY-316, WAY-319, WAY-320, WAY-323, WAY-350, WAY-352, WAY-353, WAY-362, WAY-368, WAY-369 (same sentence) | Each says the figure it gives is this product's own and its record is not open to a reader. | Każda mówi, że podana liczba to własny pomiar tego produktu, a jego zapis jest niedostępny dla czytelnika. | row 2, found by the search of WAY-33 |

The sentence is the same everywhere in meaning: "this product's own, and its record is not open to a
reader of this repository"; the form changes to fit each entry's sentence.

## Search of the whole foundation (WAY-33)

Searched: all of `foundations/decisions.md` (patterns above, plus entries whose *Scope* names
`decisions` or `environment-facts`, listed by a script, the ones bearing on the form of an entry read
whole: WAY-05, 17, 24, 27, 29, 33, 73, 80, 84, 85), `foundations/invariants.md`, `glossary.md`,
`part_map.md` (no figure of a measurement; `outbound-link-reach` and `tracked-file-private-paths`
are the invariants that bear, checked), `environment_facts.md` (no fact of an own measurement;
`shorter-guidelines-trial` is the only one near the subject and has an open source), and every
mention of WAY-90 in the repository.

Findings and what I did:

- **WAY-229, 164, 364, 312 (named by the task); WAY-136, 371 (named by the orchestrator).**
  Sentence added to 229, 164, 364, 136, 371. WAY-312: see Concerns.
- **Further decisions with a figure of an own measurement:** WAY-255 (cache probes; a count over
  session records of one game product and of the-way), WAY-300 (history of merges of the-way and of
  one product), WAY-308 and WAY-309 (search of the commits of record copies, 2026-11-07), WAY-316
  (size of screenshots in the history of one product), WAY-319 (errors in conversation files),
  WAY-320 and WAY-323 (runs of the check on one public product), WAY-350 (durations of gate runs),
  WAY-352 (count of cycles with a cost), WAY-353 (register of problems), WAY-362 (function sizes in
  one product), WAY-368 (counts, probes, estimates), WAY-369 (a start of about eleven thousand
  tokens, whose conditions the entry says are not recorded). Each got the sentence, in the field
  where the figure stands. Judgement calls: WAY-362 (two line counts of one function each, an
  observation more than a measurement) and WAY-323/WAY-320 (the product run on is public, but the
  result of the run is not kept anywhere a reader can open); I took them as measurements whose
  record is not open. If the orchestrator holds either not to be one, the sentence comes out.
- **WAY-90's neighbours:** WAY-05, WAY-27, WAY-80 unchanged (rows 1, 2). WAY-17 says a decision names
  the facts it rests on; it holds with the new rule, since a measurement of the product's people is no
  fact about the world around the product, so I left it. WAY-85 (a decision says in its rationale it
  takes a finding across publishers) is the model I followed for putting a statement about the
  status of a figure in the rationale.
- **Links, questions to the human:** none arose.

## Concerns (orchestrator to decide)

1. **WAY-312 is left unchanged.** The task and the handoff list it among the decisions that get the
   sentence. Its *Based on* names the fact `shorter-guidelines-trial`, whose source is a report at a
   fixed commit of a public repository; I confirmed that the repository is public and that the file at
   that commit opens (`gh repo view` reports `PUBLIC`; `gh api` returns the file). So its measurement
   has a record a reader can open, the sentence "its record is not open to a reader" would be false
   there, and WAY-90 as written (the first sentence governs a measurement with an open report)
   leaves it as a citation with a fact. Cost if wrong: one sentence to add in WAY-312's rationale;
   cost if I had added it: a decision that says its record is closed beside a fact that opens it.
2. **WAY-256 is left unchanged, unclear.** Its rationale and *Rejected* give an estimate "from the
   word counts of the files of one skill" (five to fifteen percent). The entry does not say whose skill
   or whether its files are in this repository; if they are, a reader can recompute and the sentence
   does not apply. I did not guess. Recommended: leave it, or the orchestrator names the skill.
3. **Where the sentence stands.** The handoff says only the rationale gets the sentence. In WAY-136,
   WAY-164 and WAY-364 the figures stand in *Rejected* (and in WAY-229 and others in both), so I put the
   sentence next to the figures, in the field where they stand, and WAY-90 says "*Rationale*, or
   *Rejected* where it weighs a way not chosen". *Rationale* and *Rejected* are both prose of the
   entry; no binding sentence, *Scope*, *Based on* or other field of those entries changed. Cost if the
   orchestrator wants it in *Rationale* only: a move of the sentence in four entries.
4. The handoff says WAY-136's rationale gained the measurement; it stands in its *Rejected*.

## Choices (with the way rejected)

- **Standard sentence** "this product's own, and its record is not open to a reader of this repository"
  against a pointer such as "the author's private notes": the pointer is what WAY-27 forbids.
- **WAY-90 binding part** got a second sentence (the rule) and not a separate decision, because it
  answers the same question (which citations of *Based on* become facts and how a source outside them
  is written); rejected: a new decision, which would split one question in two.
- **WAY-90 *Rejected*** holds the ways the task's questions 1 and 2 give as not chosen (the summary kept
  in a public file, the figure with a pointer to the notes, the rule without the sentence, no change),
  each with its cost, as the task keeps them.
- **WAY-90 wording "product's own people — its author and its agents"** in the rule and the two
  templates (generic for any product), "this product's own" inside the-way's own log.

## Reaches beyond the dispatch

- `elements/decisions/skill/read.md`, `decide_entry.md` (the decisions skill's step 1 and 2 files):
  named by the skill I was told to follow; read. `elements/environment-facts/skill/SKILL.md`: read to
  see whether it restates the rule (it does not; it points to the template).
- Invariants whose *Part* names `decisions`, `environment-facts` or `every`: listed by a script and I
  read `outbound-link-reach` and `tracked-file-private-paths` as the ones that bear on a sentence in a
  decision.
- A script run over `decisions.md` listing entries by *Scope* (not committed).
- Entries read whole beyond the handoff: WAY-17, 24, 29, 73, 84, 85, 255, 256, 300, 308, 309, 316,
  319, 320, 323, 350, 352, 353, 362, 368, 369, 370 (at the passages of the figures, each with its
  whole *Rationale* and *Rejected* where I edited), `shorter-guidelines-trial` in
  `environment_facts.md`. Why: the search of WAY-33 for the rest of the entries that carry such figures.

## Unread material

- `elements/environment-facts/skill/read.md`, `decide_entry.md`, `draft.md`, `write.md`: not read; the
  change edits that element's template (a point of a rule), not an entry of it.
- `elements/decisions/skill/projected.md`, `elements/common/projected_mode.md`: not read; no projected
  entry.
- Decisions found by the *Scope* search that do not bear on the form of an entry's *Based on* or
  prose (WAY-01, 02, 04, 07, 09, 10, 11, 12, 14, 18, 19, 21, 22, 25, 26, 28, 30, 32, 34–37, 52–55, 60,
  61, 64, 65, 71, 72, 76–78, 82, 86, 95–104, 113–150 and later): read by title only, and by figure
  signature through the greps; none read whole except those listed above.
- The glossary: only the entries `environment fact` and `foundation` read; the terms used in my
  sentences ("measurement", "record", "reader") are not entries of it.
- `elements/decisions/examples.md`: not read; names entries by number and none I changed form.

## Searches not found or unclear

- The glossary holds no entry for "product"; I used the word as the decisions already use it.
- The handoff asks the invariants "whose *Part* names `decisions`, `environment-facts` or `every`" to
  be read; I read two of seventeen whole and listed the rest by name only.
- Whose skill the estimate of WAY-256 is (Concern 2).
- Whether the record of the trial in WAY-323 and WAY-320 is kept somewhere a reader can open: I found
  nothing in the repository; taken as not open.

## Weakest point and how I checked it

The weakest point is the set of decisions that got the sentence: the line between "a measurement of
the product's people with a record a reader cannot open" and an observation, an estimate or a count a
reader could redo from the open history is a judgement for WAY-362, WAY-323, WAY-320, WAY-256 and
WAY-300 (the history of the-way is open, that of the first product is not). I checked it by reading
each entry whole where it stands, by the figure-signature script above (no entry with a figure of
this kind without the sentence apart from the two Concerns), and by confirming the one case where the
source is open (WAY-312) with `gh`. The wording of the sentence in each entry also sits where a
reviewer may read it as history of how the decision was reached (WAY-05); I kept it to the one clause
that says whose the measurement is and that its record is closed.
