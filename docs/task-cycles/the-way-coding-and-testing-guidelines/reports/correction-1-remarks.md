# Remarks of the human for correction 1 (word for word)

Source: https://github.com/mariusznazar/the-way/pull/136#issuecomment-6901566614 (comment of 2026-11-15, written by the day advisor on behalf of the human).

Uwagi doradcy dnia w imieniu Mariusza

Answers to "Fix or let through":

1. Review of the whole change and of the return step on the same model — **let it through.** Mariusz accepted the Sonnet review for this one cycle (the strongest allowed class is opus; that rule goes into the collective task of small corrections after pull requests 93 and 117–121, item 20).

2. Small things found and not fixed (Minor findings 1–7) — **fix two of them in this request, let the rest through, no task:**
   - **Fix** Minor finding 4: WAY-395 says tests give time "as the option `--today` gives it", while `gate_times.py` has no such option and its tests replace the clock function. A decision that names an option the code does not have misleads the next agent who writes such a test; correct the wording to what the tests do.
   - **Fix** Minor finding 3: the pairs of examples in WAY-380 and WAY-388 to WAY-391 that repeat what an invariant holds — remove them, as the template allows a pair only for the part no invariant and no test checks.
   - **Let through** Minor findings 1, 2, 5, 6, 7: nothing breaks; each is rare, mention-only or already allowed by the narrowed invariant.

This is the one round of corrections from the day advisor on this request. After the fix: review of the fix, then wait for my start signal before the full gate.

