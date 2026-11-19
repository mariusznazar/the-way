# Correction 1 — the human's remarks, word for word

Source: the comment https://github.com/mariusznazar/the-way/pull/150#issuecomment-7016261188 on the request, posted 2026-11-19T17:08:09Z from the owner's account; it opens "Uwagi doradcy dnia w imieniu Mariusza" (remarks of the coordinator of the day on behalf of the human). The text below is the comment as posted.

---

Uwagi doradcy dnia w imieniu Mariusza

Fix or let through:

1. **The closing step has never been run on a real project** — let through, no task. Nothing breaks: nothing is written before the human accepts the whole preview, so an unclear sentence or a missing case shows up as a question at the first real closing, where the human decides anyway.
2. **A closed plan passes the check although two of its tasks are each marked "delivered by the other"** — **fix in this request**: the check refuses a closed plan where following "delivered by another task" never reaches a task that is done (a loop of such rows, of any length), with a test for the pair and for a longer loop. It is a small addition to the check this request already changes, and the harm is the one the closing exists to prevent; a task for it would cost a whole cycle to read the same code again.
3. **No rule for the case where the existing task document stands** — let through, no task. The agent proposes in the preview and the human decides there; nothing is written before that.

This is the one round of remarks from the coordinator of the day on this request.

You accept by merging: items 4–12 accepted.

