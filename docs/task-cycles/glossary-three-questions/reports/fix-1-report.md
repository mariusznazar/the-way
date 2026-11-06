# Fix 1 — task `glossary-three-questions`

**Status:** done

Reviewed head: `24e092ca8dd8ae2e7b6165133552e7590f73dc8c`. Fix commit: see `git log` (message "docs: WAY-104 binding paragraph back to three sentences, WAY-293 without \"should\""), one file: `foundations/decisions.md`.

## F1 — fixed
WAY-104's binding paragraph had four sentences. Sentence 2 ("A bare use that no sentence of those files reads in the other meaning keeps the meaning it has there.") is joined to sentence 1 with ", and a bare use ... keeps the meaning it has there". The paragraph is now three sentences: (1) qualifier rule with the bare-use clause, (2) the qualified word's entry and the *Not* clause, (3) the product's code, interface and talk. No meaning moved; no word of the clauses changed except the joining. Check: the paragraph read at `foundations/decisions.md:2251-2260` shows three sentence ends; `foundation_check.py` exit 0 (it does not count sentences).

## F2 — fixed
WAY-293's binding sentence: "a finding that a word should have a glossary entry" -> "a finding that a word needs a glossary entry". Check: the word "should" no longer occurs in WAY-293's heading-to-*Scope* paragraph (read at `foundations/decisions.md:8840`). The same phrase in `task-cycle/review/SKILL.md:113` is not an entry's binding sentence and, per the findings file, was left as it is.

## Checks
- `python -B elements/common/foundation_check.py .` -> `0 errors`, exit 0.
- `python -B gate/run_tests.py elements/common` -> exit 0.
- `python -B gate/run_tests.py task-cycle` -> exit 0.
- Not run: the full gate (the orchestrator's run).

## Searches not found or unclear
- My own script to count sentences of binding paragraphs gave 0 for every entry (the regex was wrong); I counted by reading the paragraphs instead. The reviewer's script was not available to me.
- The skill sentence at `task-cycle/review/SKILL.md:113` still says "should"; the fix is not asked to touch it, so its wording differs by one word from WAY-293. Whether to align it is for the reviewer or the orchestrator.
