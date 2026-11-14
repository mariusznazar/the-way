FAIL c76debc0598f468b9eaf6da263b750fee6484415

# Review of the whole change — own-measurement-in-decision

Range `3c572b95e86a1a4e6b0373b7fb11c3e7c6b00ead..c76debc` (one commit, `git rev-parse HEAD` =
`c76debc0598f468b9eaf6da263b750fee6484415`, the head given). Reviewed read-only from the worktree
`the root of the task's worktree`.

Counts: blocking 1, Minor 4 (all within the task), out of scope 0.

## Changed files (lines before, after, change; `task-cycle/change_file_sizes.py`)

| File | Before | After | Change |
|---|---|---|---|
| `foundations/decisions.md` | 12528 | 12582 | +54 (85 added, 31 removed) |
| `elements/decisions/template.md` | 242 | 248 | +6 |
| `elements/environment-facts/template.md` | 183 | 189 | +6 |

No code is changed, so the structure-of-code check of `whole_change.md` has nothing to measure; the
sizes above are the first numbers. The change adds no function and no test.

## What the change does, against the task

- Row 1 and *To do* item 1 (the rule in WAY-90): met. WAY-90's binding part gains one sentence, its
  *Verification* a third group (complies/violates), its *Rationale* the reason, its *Rejected* the
  ways the task's questions 1 and 2 give as not chosen (summary in a public file; the figure with a
  pointer to private notes; the rule without the sentence; no rule). The meaning matches the row;
  the extension to *Rejected* is discussed under the orchestrator's decision 3.
- Row 2 and *To do* item 3 (the sentence in the rationale of decisions that carry such a figure): met
  for 19 decisions, with two exceptions the author and the orchestrator decided (WAY-312, WAY-256).
- *To do* item 2 (the two templates say the same as WAY-90): met in meaning except one wording
  (Finding 1).
- WAY-27 and WAY-05 are unchanged, as question 1 says. `git diff` shows no change to a binding
  sentence, *Scope*, *Based on*, *Relations*, *Verification* or *Origin* of any decision but WAY-90:
  each of the other 19 hunks lies in a `*Rationale:*` or `*Rejected:*` paragraph (I mapped each hunk
  line to its entry and field by script; the result: WAY-136 *Rejected*, WAY-164 *Rejected*,
  WAY-229 *Rationale*, WAY-255 *Rationale* and *Rejected*, WAY-300, 308, 309, 316, 319, 320, 323,
  350, 352, 353, 362, 364, 368 (two hunks), 369, 371 all *Rationale*).

## Findings

### Important (blocking, within the task)

**1. `elements/decisions/template.md:54-55` restates WAY-90 differently from the other two texts.**
The new point ends "A measurement whose report a reader can open at an address is quoted like any
other source (WAY-90)." In that template the sentence before it (lines 44-49) separates two kinds of
source: a fact entry named by identifier for a citation whose change would call the decision into
question — "a finding about agents or models" — and "any other source" quoted with its address,
place, passage and date. Read in that frame, "quoted like any other source" puts a measurement with
an open report on the quoting side. WAY-90's own rationale says the opposite: such a measurement "is a
citation like any other, and follows the first sentence", that is, it becomes a fact entry where it
is a finding about agents or models. A decision's author reading only this template would quote a
public report of an experiment with agents, where WAY-90 asks for a fact. The real entry
`shorter-guidelines-trial` in `foundations/environment_facts.md:204` (an open report, a trial of agents) shows
which reading is the right one. `elements/environment-facts/template.md:59-60` words the same point
correctly ("is a citation, and a fact where this section asks for one"), so the two templates say
different things where the task asks for the same (*To do* item 2). Under WAY-263 a restatement that
differs from the entry is Important. Fix: in the decisions template say "is a citation like any
other and follows the point above (WAY-90)" (or the wording of the environment facts template).
Evidence: the three texts above; no other word of the change settles it.

### Minor (within the task)

**2. `foundations/decisions.md` WAY-256 (rationale, near the sentence "estimated before any rebuild
from the word counts of the files of one skill", and *Rejected*, "an estimate of five to fifteen
percent more words read in a typical session, made before any rebuild from the word counts of that
skill's files").** The figure is the product's own estimate from files of a skill the entry does not
name, so a reader cannot recompute or open its record; by WAY-90's rule (a result stays in the prose
and says that it is the product's own and its record is not open) it either carries the sentence or
names the skill. The orchestrator left it unchanged (decision 2); that follows the author's doubt
whether the files are in this repository, but the entry as it stands is the case WAY-90's third
*Verification* group calls a violation ("the same figures stand in the rationale with no word that
the figure is the product's own"). Minor because it is an estimate, not a measurement, and the entry
says it was made before any rebuild. It lies within the task (*To do* item 3: "each decision whose
rationale gives the result of such a measurement"). Fix: add the sentence to the two places, or name
the skill so that a reader can count.

**3. `foundations/decisions.md`, WAY-90 *Rationale* (the new sentences, around line 2092-2102) names no
price and does not meet WAY-17's *Rejected*.** Other entries of the log state the price taken (WAY-229,
255, 320 and others: "The price: …"). This rule has one: a measurement of the product's own agents is
found by no fact search (WAY-33), so when the model it measured is replaced, no entry flags the
decision that rests on it; and WAY-17's *Rejected* turns down "research findings outside the environment
facts" for just that reason. A reader weighing the rule would find the cost named nowhere. Not a
contradiction (WAY-17 speaks of findings of others, which still get a fact), so Minor; one sentence in
the rationale would close it. Within the task.

**4. `foundations/decisions.md` WAY-229 *Rejected* (about line 6951-6954).** Figures of the same
experiment ("5 of the 14 reference errors", "5 and 6 in two such runs", the verdict of a PASS in both
runs) stand in *Rejected* with the sentence only in *Rationale* above. WAY-164 and WAY-364 make the
same measurement say it in the field where the figure stands. I read the *Rationale* sentence ("The
measurement is this product's own…") as covering the whole entry, so I do not block, but a reader of
*Rejected* alone does not see it, and WAY-90 itself says "in the *Rejected* where it weighs a way not
chosen". Minor, within the task; either repeat a short clause in *Rejected* or leave as is.

**5. Formatting of the inserted sentences in `foundations/decisions.md`.** Several inserted clauses
break the wrap of the file and leave one very long line (WAY-353 about line 11836, 145 bytes; WAY-364
about 12255, 135; WAY-350 about 11747, 112; WAY-368 about 12417, 111; WAY-255 about 7956, 110) or a
short orphan line (WAY-368 about 12426-12428: "definition with no body"). No check reads it; it
makes the next diff of those paragraphs noisy. Minor, within the task.

### Out of scope

None.

## The orchestrator's decisions (judged)

1. **WAY-312 left unchanged: correct.** Its *Based on* is the fact `shorter-guidelines-trial`, whose
   source is a report at a fixed commit of `mariusznazar/loop2` (`gh repo view mariusznazar/loop2
   --json visibility` returned `PUBLIC`; the file's address is in `environment_facts.md:204-207`). The
   record opens, so WAY-90's first sentence (the exception needs a record a reader cannot open) does
   not reach it and "its record is not open" would be false. The task text lists WAY-312 by name;
   the request must say that it left it, with this reason.
2. **WAY-256 left unchanged:** see Finding 2 (Minor).
3. **The sentence in *Rejected* where the figures stand (WAY-136, 164, 364): correct.** WAY-05 treats
   "rationale and rejected options" as the prose of the entry, WAY-90 now says so, and a sentence in
   *Rationale* alone would leave the figure in *Rejected* without it. Row 2 says "uzasadnienie"; I
   read *Rejected* as part of the same prose, and no binding sentence changed. The cost the author
   names (a move in four entries if the human wants it in *Rationale* only) is right.
4. **The 14 further decisions (WAY-255 … 369).** Each against WAY-90's rule (a measurement of the
   product's own people, whose record a reader of this repository cannot open), by the passage I read:
   - WAY-255 (cache probes; counts over session records of one game product and of the-way): yes.
   - WAY-300 (merges of the-way and of the first product, weeks 40-45): the history of the-way is
     public and could be recounted; the history of the first product cannot. The inserted sentence
     says exactly that ("the history of the first product is not open"), so it is true. Borderline,
     accepted.
   - WAY-308, WAY-309 (a search of commits of record copies on 2026-11-07 in repositories where cycles
     had run; WAY-309 points back to WAY-308's sentence): yes.
   - WAY-316 (objects of one product's repository, 2026-11-08): yes.
   - WAY-319 (errors in conversation files of two products): yes.
   - WAY-320, WAY-323 (a run on "one public product" on 2026-11-09 and 2026-11-11, 71 of 88 findings;
     twelve texts): the product is public but is not named and the result is kept nowhere a reader can
     open, so the sentence is true. Borderline, accepted.
   - WAY-350 (gate durations), WAY-352 (7 of 138 cycles with a cost), WAY-353 (register of problems;
     the register lives in the author's notes, the repository holds its template only, `process-audit/problem_register.md`):
     yes.
   - WAY-362 (a function of 456 lines, another of 781, in one product's game): an observation of
     two counts more than a measurement; the sentence is true and harmless. Borderline, accepted.
   - WAY-368 (72 of 625 and 4 of 252 subagents; probe at 36,711 and 21,759 tokens; estimates), WAY-369
     ("about eleven thousand tokens", conditions not recorded), WAY-371 (220 slices of one game
     product): yes. In WAY-371 the sentence replaced "described here because its source is not
     reachable from this repository" with "The measurement is this product's own, and its record is not
     open to a reader of this repository, so it is described here"; the earlier meaning is kept.
   None of the 14 is a case where the sentence is false or the figure has an open record. No entry
   among them needs the sentence taken out.
5. **No field but WAY-90's changed:** confirmed (above).

## Other checks asked

- **WAY-90, the two templates and the rationale sentences say the same thing:** yes except Finding 1.
  The wording "the product's own people — its author and its agents" matches the task's "ludzie produktu
  (autor procesu i jego agenci)". The inserted sentences say the same in meaning ("this product's own,
  and its record is not open to a reader of this repository") with the form fitted to each entry.
- **Collisions with WAY-27, WAY-05, WAY-80, WAY-17, WAY-85:** none. WAY-27 (no pointer to a source
  the reader cannot open; describe what is seen there) holds: the new sentences point to nothing,
  they say a figure's record is closed, and the `*Rejected*` of WAY-90 repeats WAY-27's own rejection of
  a note pointing to private notes. WAY-05 lets a measurement stand with what was measured and its
  conditions; the sentences add the status of the figure, not how the decision was reached, so they
  add no history. WAY-80 (a fact needs an edition, an archived page or a reading) is not touched: no
  such fact is written. WAY-17 and WAY-85: see Finding 3 and the third *Verification* group, which
  keeps a fact for a measurement whose report opens.
- **No entry now points to a source a reader cannot open:** the inserted sentences name none; the
  phrase "private notes" stands only in WAY-90's *Rejected* and *Verification* as the described
  rejected way and the example of a violation. `private_paths_check` lists nothing.
- **No history of how a decision was reached (WAY-05):** the sentences say whose the measurement is and
  that its record is closed; WAY-308/309's "the search of WAY-308: this product's own" is a
  cross-reference, not a story.

## Checks run (read-only, from the worktree root)

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `c76debc0598f468b9eaf6da263b750fee6484415`, the given head |
| `git diff 3c572b9..HEAD` (also `-U0`) and `git log 3c572b9..HEAD` | 0 | one commit, three files |
| `python -B elements/common/foundation_check.py --skip-test-citations` | 0 | `0 errors` |
| `python -B task-cycle/private_paths_check.py foundations/decisions.md` (and the same for `elements/decisions/template.md`, `elements/environment-facts/template.md`, one run each; the script takes one target) | 0, 0, 0 | `checked: 1 files, 0 listed` each |
| `python -B task-cycle/change_file_sizes.py 3c572b95e86a1a4e6b0373b7fb11c3e7c6b00ead c76debc` | 0 | table above |
| A throwaway script (scratchpad, not committed) mapping each hunk line to its entry and field | 0 | the list under "What the change does" |
| A throwaway script listing the entries whose *Rationale*/*Rejected* has a figure signature (measure, trial, probe, `N of M`, `N%`, dates, counted, runs of) and lacks the sentence, then reading the hits | 0 | residual hits are rules, counts of a rule's text, or open-source figures (WAY-312); WAY-256 is Finding 2; WAY-354 ("a search of the log by 'until' on 2026-11-12") is a search of this repository's own open file, which a reader can redo, so needs none |
| `gh repo view mariusznazar/loop2 --json visibility` | 0 | `PUBLIC` |

Not run: the full gate (the orchestrator's), the invariant tests (no invariant written or changed,
none named as changed), the tests of `elements/common` (the author ran them).

## Reaches beyond the dispatch

- `foundations/environment_facts.md` entry `shorter-guidelines-trial` (lines 204-207): to confirm
  that WAY-312's source opens.
- `process-audit/problem_register.md` (listed by `git ls-files`) and `foundations/decisions.md` lines
  around the register of problems (250, 11067, 11401): to learn whether WAY-353's register is in the
  repository (it is a template; the register itself is not).
- WAY-85 and WAY-17: read whole for the collision check.
- `git grep WAY-90` over the repository: the places that cite WAY-90 are the two templates, the skill
  files `elements/environment-facts/skill/SKILL.md:44` and `read.md:6` (both point to WAY-90 by
  number and do not restate its rule) and entries of the log (line 1444 cites it as a model).

## Unread material

- **Counts (WAY-150):** decisions of my selection read **whole: 11** (WAY-05, 07, 17, 27, 33, 80, 85,
  90, 134, 256, 312). **At the passage of the change only: 19** (the 19 changed entries other than
  WAY-90 minus WAY-256 and 312 above: WAY-136, 164, 229, 255, 300, 308, 309, 316, 319, 320, 323, 350,
  352, 353, 362, 364, 368, 369, 371; for each I read its *Rationale*/*Rejected* paragraph around the
  inserted sentence, and for WAY-229 the entry from *Based on* to the end, not its binding sentence).
  WAY-150 read in its first part only (the binding sentence and the beginning of *Verification*).
  **By title only:** the rest of the log, screened by a script for figure signatures and not by
  reading; I opened every entry that script named and found to bear (list under "Checks run").
- The guidelines of `product-guidelines/reading.md` and the files it selects: not read; the change
  is to foundation text and two templates, the-way holds no product guidelines of code for it, and I
  judged the files not to bear.
- `elements/common/way_of_working.md` "Reading the foundation": not read whole; I selected by the
  parts the three files belong to (decisions, environment-facts, elements) and read the entries named
  in the handoff, `foundations/invariants.md`, `foundations/part_map.md` and `foundations/glossary.md`
  I did not read whole; the invariants that bear (`outbound-link-reach`, `tracked-file-private-paths`)
  I covered by running `private_paths_check.py`, not by reading their entries or tests.
- WAY-364's, WAY-136's and WAY-164's whole entries: read at the inserted sentence only.
- The author's report: read whole. The task: read whole.

## Searches not found or unclear

- The handoff names the rationale only for the sentence; it did not say what to do for an entry whose
  figures stand in two fields with the sentence in one (WAY-229 *Rejected*, Finding 4) — I took the
  sentence in one field as covering the entry and listed the doubt as a Minor.
- Whether the estimate of WAY-256 comes from files in this repository: the entry does not say
  (Finding 2); I did not find the skill it means.
- Whether the glossary has "measurement" or "record" as a term: not searched in the glossary (the
  author's report says the terms are not entries).
