# Findings of the review of the whole change, to fix

Reviewer's words, cut from `reports/review-whole-report.md` (first line `FAIL 888eb6150e13bee2337368114c4f1cd760b3d274`), range `f04f046..888eb61`. Finding 1 blocks; findings 2 to 5 are the Minor findings within the task, which the cycle has fixed too (WAY-161). The Minor finding outside the task (6) is not fixed and is not here.

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
