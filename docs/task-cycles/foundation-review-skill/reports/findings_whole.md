# Findings to fix — review of the whole change (blocking findings only, in the reviewer's words)

Source: `reports/review_whole.md`, first line `FAIL 02ca017cc5e7a6176f1f921f08d6eace43cd0ffd`. Fix range runs from that head. Minor findings are not yours to fix.

## Blocking findings

### Important 1 — the skill says the tag message counts "entries and remarks"; WAY-301 says "entries" (WAY-263)

- Place: `foundation-review/SKILL.md`, step 7, second bullet: "The message gives the number of
  entries and remarks checked, and no title of a task, of a note or of a person". Against
  `foundations/decisions.md`, WAY-301, binding sentence: "the tag's message gives the number of
  entries checked and no title of a task or of a private note"; and its *Verification* "violates" line
  "the message names the tasks the review made".
- What is wrong: the skill, a file of the change, restates an entry the change writes more broadly
  than the entry does: the entry names one count (entries); the skill names two (entries and
  remarks) and adds "of a person". The task's *Context* says "Opis tagu podaje tylko liczbę
  sprawdzonych pozycji", which fits either reading, so the source does not settle which of the two
  texts is right; they disagree with each other.
- Why it matters: WAY-263 grades a changed file that restates an entry differently, including more
  broadly, as Important. A later reviewer comparing a review's tag with WAY-301 and a review that
  follows the skill will find two rules for the same message. The consequence is small (a tag
  message), the fix is one word, but the grade is the rule's.
- Evidence: the two quoted passages above, read in the worktree at the head.
- Fix: make the decision and the skill say the same (either "entries and remarks" in WAY-301, which
  matches the task's "pozycji", or "entries" in the skill).
- Slice: none (no plan; one author).
