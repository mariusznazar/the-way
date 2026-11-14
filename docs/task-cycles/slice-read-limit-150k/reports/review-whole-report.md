FAIL 888eb6150e13bee2337368114c4f1cd760b3d274

# Review of the whole change: slice reading limit to 150 000 tokens

Worktree `the task's worktree root`, branch `task/slice-read-limit-150k`. Range `f04f046d5220913a4ae399faf59683129e81c936..888eb61` (two commits: `92e7576`, `888eb61`). `git rev-parse HEAD` gave `888eb6150e13bee2337368114c4f1cd760b3d274`, the head of the handoff. No spec, no plan; one author. Read-only: no file of the worktree changed (`git status --short` empty).

Result: 1 blocking (Important), 4 Minor within the task, 1 Minor outside the task.

## Coverage of the task

| Item | Verdict | Where |
|---|---|---|
| To do 1: `READ_LIMIT_TOKENS` is 150 000 | met | `task-cycle/slice_size.py:63` (`READ_LIMIT_TOKENS = 150_000`) |
| To do 2: paragraph on limits explains the value by the measurement in words and numbers, replaces the "quarter" sentence, points to no source (WAY-27) | met in form; one number claim is worded differently from the task (finding 1) | `slice_size.py:35-40` |
| To do 3: WAY-136 *Rejected* gains the measure-of-size variant with the cost per changed line | met; numbers 1 500 to 3 000 lines, five cycles a route, 0.0182 and 0.0157 USD, medians 39 and 24 USD, and the three added costs all agree with the task | `foundations/decisions.md:3737-3743` |
| Settlements row 1 (WAY-136 edited in place) | met: *Rejected* only; binding sentences, fields, *Rationale* unchanged (diff shows one hunk) | same |
| Settlements row 2 (limit 150 000, with 175 000 and 125 000 rejected) | met as a new decision WAY-371; the search for an existing entry stating the limit found none (my grep for `250 000`, `quarter of`, `slice_size`, `READ_LIMIT` outside `.runs/` hits only the changed lines, `plan/SKILL.md` lines that state no value, and an unrelated audit test) | `decisions.md:12441-12469` |
| Questions to settle answers bind (150 000, not 175 000 or 125 000; variant recorded) | kept | as above |
| Decisions in play WAY-136, 229, 27, 328 | WAY-136 changed as the task says; WAY-229 untouched; WAY-27 kept (diff holds no path, note link or pointer to a private source); WAY-328 means no guidelines of the-way's own, so none were applied | |
| Test at the old boundary (`test_slice_size.py` ~line 83) | moved to 375 000 and 375 001 characters, expecting `150000 fits` and `150001 too large`, message `reads about 150001 tokens, more than 150000`; nothing weakened | `task-cycle/test_slice_size.py:77-85` |
| Orchestrator's binding choice 1 (report line no longer says "a quarter") | met: `slice_size.py:214-215` | |

## Findings

### Blocking

**1. Important, within the task. Source fidelity: the entry and the script's description attribute the 25% of input tokens and the "10 longest runs" differently from the task.**

Places: `foundations/decisions.md:12461-12463` (WAY-371 *Rationale*, also the *Rejected* text at `12465-12468`) and `task-cycle/slice_size.py:36-38`.

What is wrong:
- The task's *Need* says: "Limit 150 tys. objąłby 20 z 220 kawałków gry (9%), wśród nich 5 z 10 długich przebiegów wykonawców; te 20 kawałków zużyło 25% tokenów wejścia wszystkich wykonawców kawałków gry." The 25% belongs to the 20 slices.
- WAY-371 says: "the limit reaches 20 of the 220 slices (9%), among them 5 of the product's 10 longest agent runs, which took 25% of the input tokens of all its executors." The relative clause "which took" stands after "5 of the product's 10 longest agent runs", so its natural reading is that those 5 runs took 25% of the input tokens of all executors, a stronger claim than the task makes. The same entry's *Rejected* text for 175 000 ("among them 3 of the 10 longest runs, and 12% of the input tokens") attaches the share to the slices correctly, which shows the two sentences are not kept alike.
- The task says "długich przebiegów wykonawców" (long runs of executors). Both files say "the 10 longest agent runs" and, in WAY-371, "no added long run". "Longest" turns a set of long runs into a ranking, and "agent" widens "executor". Neither the task nor any foundation entry defines a long run (the task's *Need* gives more than 100 model calls only for slices, not for runs); the entry therefore says something the task did not.
- In the script (`slice_size.py:36-38`) the sentence "20 (9%) would reach that limit, among them 5 of its 10 longest agent runs and 25% of the input tokens of all its executors" repeats "longest agent runs" and puts the 25% in a list with the runs; the same wording issue.
- In the script the band "150 000 to 250 000" carries the 21 000 input tokens per changed line, where the task says "powyżej 150 tys."; the two are equal only because no slice of the 220 passed 250 000 (task *Need*, first line), which the script does not say. WAY-371 says "above 150 000", so the two files state the figure on different ranges.

Why it blocks: the task's *To do* 2 and the handoff require every number of the entries and the script to be the task's, with nothing altered (WAY-134, the whole-change method). This measurement is the whole reason the limit has its value, and a later agent will weigh a change of the limit against exactly these numbers (the *Rationale* says so). Reading "5 runs took 25% of all executors' tokens" would overstate the case for the limit. Under WAY-263 a restatement more broadly than its source is Important. The fix is small: attach the 25% to the 20 slices ("the 20 slices took 25% of ..."), say "5 of its 10 long runs of executors" (or say what a long run is, only if the task gives it), and put the same range on the 21 000 figure in both files.

Evidence: the task's *Need* lines 3 and 4 against `decisions.md:12461-12463` and `slice_size.py:36-40`, read side by side.

### Minor, within the task

**2. `task-cycle/slice_size.py:61` and `:30-34` — `CONTEXT_WINDOW_TOKENS` has no user after the change (WAY-362).** `grep -rn CONTEXT_WINDOW_TOKENS` finds the definition and the docstring bullet and nothing else, not even a test. The docstring still says the constant "comes from" the model overview page, as if a limit rested on it. The author kept it on the orchestrator's binding choice 4; the frozen task does not require keeping it (it has three *To do* items and no fourth point, though the author's report speaks of "the task's point 4"). A later task can remove the constant and its bullet together; keeping the constant leaves a reader to wonder what it limits.

**3. `slice_size.py:30` — the sentence "The limits start with a wide margin and are corrected as cycles bring data" is no longer true of `READ_LIMIT_TOKENS`.** It now holds a measured value, not a wide margin; it stays true of `CHANGE_LIMIT`, which the same list calls "a starting value with no source". The author flagged this; the task lets the sentence stay, so Minor.

**4. `decisions.md:12441-12445` — WAY-371's binding text restates the conversion "2.5 characters a token" and "never runs a tokenizer", which no row of the task settles.** The task settles only the value 150 000 and its alternatives. The conversion comes from a public page the script cites (a source outside the repository that *Based on* would have to name), yet WAY-371 has `Based on: none`; and by WAY-19 a new rule beside an existing one is a new question. The statement agrees with the code today, so it is polish, but it binds more than the human settled (WAY-114: the human accepted the row, not this).

**5. `decisions.md:12447-12452` — WAY-371's *Verification* "violates" names "a quarter of a context window" as a breach.** That is the old state of the script, written into a rule about the new state; a reader who meets the entry after the old wording is gone sees a violation no one will commit. Better: leave only "any value other than 150 000 tokens".

### Minor, outside the task

**6. WAY-371 has no derived invariant, though a commit can make its sentence false (WAY-22).** The test `test_read_at_the_limit_fits_and_one_character_more_is_too_large` checks exactly the boundary. Row 2 of the task asks for a decision only, and an invariant test would make a later move of the limit (which the *Rationale* expects) a change of an invariant test (WAY-03), so the task cycle's return step or a later task may judge it. No invariant test was changed by this change.

## Declined to judge

- Whether the report line of `slice_size.py` (`report()`) should be pinned by a test: none exists on the base either, and the task does not ask for it.
- Whether the first commit's message or the order of the commits is right: not part of the review.
- The unrelated number `250000` in `process-audit/test_audit_count.py:2576`: a price in an audit fixture.

## Other checks of section 2

- Tests: the boundary test fails if the constant moves in either direction or `>` becomes `>=` (150 000 must fit, 150 001 must not). It computes no expected value from the code. I did not run mutations in a separate worktree; I read the assertions.
- Foundation against code: WAY-371's limit, conversion, "never runs a tokenizer" and the `>` comparison agree with `slice_size.py` (`READ_LIMIT_TOKENS = 150_000`, `math.ceil(characters / 2.5)`, `self.tokens > READ_LIMIT_TOKENS`). WAY-136 changed in its *Rejected* only; its *Verification* and binding sentences need no change.
- Reserved choice: none settled. Trust boundary, irreversible operation: none touched (`task-cycle/slice_size.py` is not among the part map's trust-boundary files of `task-cycle`).
- Private paths and note links (WAY-27, `tracked-file-private-paths`, `outbound-link-reach`): the diff adds no path, link or note name. The foundation check and the gate's private-path test are not mine to repeat beyond the foundation check below.
- Glossary: `slice` has an entry; "estimated tokens" is not a glossary word and the entry uses it as the script does. No finding.
- The author's own-work check names the exact boundary and its check (boundary test, red before, green after) catches that requirement unmet; its second requirement (nothing private in the diff) holds.
- Structure of the code (WAY-362): `python -B task-cycle/change_file_sizes.py f04f046d5220913a4ae399faf59683129e81c936 888eb61` exit 0: `foundations/decisions.md` 12480 to 12515 (+35), `task-cycle/slice_size.py` 250 to 253 (+3), `task-cycle/test_slice_size.py` 171 to 171 (+0); total +38. The-way has no rule of size and no test of one (WAY-328), so structure findings are Minor (WAY-363); the only one is finding 2. I ran no second run in separate worktrees because no such test exists.

## Checks run

| Command (from the worktree root) | Exit code | Result |
|---|---|---|
| `python -B gate/run_tests.py task-cycle` | 0 | 394 tests, OK |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B task-cycle/change_file_sizes.py f04f046d5220913a4ae399faf59683129e81c936 888eb61` | 0 | sizes above |
| `git rev-parse HEAD`; `git diff`, `git log` of the range | 0 | head confirmed; 2 commits, 3 files |

Not run: the full gate (the cycle runs it), a mutation of the constant, a second worktree (no test of a rule of size exists).

## Reaches beyond the dispatch

- `elements/decisions/template.md`: the form of an entry, to judge WAY-371 and the WAY-136 addition (section 2, against the foundation the change writes).
- `task-cycle/plan/SKILL.md` lines 185-224: whether any text states the old limit (none does).
- `foundations/invariants.md`, listed by *Part* `every`, `task-cycle`, `decisions`: 22 invariants read by their sentence; none states the limit.
- `foundations/part_map.md` lines 1-16 and 90-104 (`decisions`, `task-cycle`) and `foundations/glossary.md` line 145 (`slice`).
- `git grep`-style search of the repository outside `.runs/` for `250 000`, `250000`, `quarter of`, `slice_size`, `READ_LIMIT`, `CONTEXT_WINDOW_TOKENS`, to find a text that states the old value or uses the constant.

## Unread material

Decisions of my selection (*Scope* naming `task-cycle` or `decisions`, matched by search of each `- **Scope:**` line with its continuations): 183. Read whole: 17 (WAY-05, 19, 22, 27, 33, 134, 135, 136, 229, 263, 328, 339, 362, 365, 369, 370, 371). Read by title only: 166.

Decisions that bear on the change and stayed unread whole: WAY-13 (what sets the weight of a task's process; the closest neighbour of the route variant WAY-136 now rejects), WAY-150 (how the-way's skills choose what to read; I took its method from `elements/common/way_of_working.md`), WAY-161, WAY-363 and WAY-364 (the grading rules; I took them from the method file `task-cycle/review/SKILL.md`), WAY-114 and WAY-07 (what a human accepts of an entry; entry changed in place), WAY-337 (the cost of a cycle). None of them was needed to reach the findings; they are listed so that the reader knows.

Guideline files: none exist for the-way (WAY-328), so none were read.

Other material: I read the handoff, the method `task-cycle/review/SKILL.md` and `task-cycle/review/whole_change.md`, the frozen task, the author's report and the author's handoff, whole. I read `task-cycle/slice_size.py` whole and the diff of the range whole. I read `elements/decisions/template.md` and `elements/common/way_of_working.md` lines 1-140 whole as far as the selection method; I did not read `elements/common/rules.md` or `elements/decisions/examples.md`. I read the part map's `decisions` and `task-cycle` entries and the glossary entry for `slice` only; the invariants were read by their sentence and *Part*, not whole. I did not read `foundations/environment_facts.md` (the change rests on no citation).

## Searches not found or unclear

- A definition of "long run" (of an executor, of an agent) in the task or the foundation: not found; the task's *Need* uses "długich przebiegów wykonawców" without saying what makes a run long, and the entry and the script call them "longest" (finding 1).
- The author's report speaks of "the task's point 4" about keeping `CONTEXT_WINDOW_TOKENS` and the first sentence of the paragraph; the frozen task has three *To do* items and no point 4. The orchestrator's binding choice 4 in the author's handoff carries the instruction instead. Unclear which of the two the report meant.
- An invariant covering the slice limit: not found (searched `foundations/invariants.md` for `slice_size`, the limit and tokens).
- A test of the report's header line: not found.
