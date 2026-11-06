PASS 049e84e9fdea1784f348b29e7f20f33491e02ec5

# Review of the fix — task `glossary-three-questions`

Fix range `24e092ca8dd8ae2e7b6165133552e7590f73dc8c..049e84e9fdea1784f348b29e7f20f33491e02ec5` (one commit,
`049e84e`, one file: `C:\Storage\repos\the-way\.runs\worktrees\glossary-three-questions\foundations\decisions.md`).
`git rev-parse HEAD` in the worktree printed the head sha above. Counts: 0 blocking, 0 Minor, 0 out of scope.

## Findings of the findings file

- **F1 (WAY-104 had four binding sentences) — fixed.** The paragraph at `foundations/decisions.md:2251-2260` now
  reads: (1) "A word that ... takes a qualifier ... in a sentence ... that could otherwise be read in the other
  meaning: a sentence that uses the word for the product's domain and could be read as the process's, or one that
  uses it for the process and could be read as the domain's, and a bare use that no sentence of those files reads
  in the other meaning keeps the meaning it has there." (2) "A qualified word takes a glossary entry only where
  WAY-95 gives a word one, and where the bare word itself has an entry ... no *Not* for its domain meaning."
  (3) "The product's code, its interface and talk about the product use the word of the domain unchanged." Three
  sentences, within `elements/decisions/template.md:94`. The sentence-count script I used in the first review gives
  95 -> 2, 97 -> 2, 99 -> 3, 104 -> 3, 293 -> 2.
- **F2 (WAY-293 binding sentence used "should") — fixed.** `foundations/decisions.md:8840` now says "a finding that a
  word needs a glossary entry"; the same script finds neither "should" nor "will" in the binding paragraph of any of
  the five entries.

## What the fix itself did (diff read in full)

The diff has two hunks: the join of sentences 1 and 2 of WAY-104 (the words of the clauses are unchanged, only
"A bare use" became ", and a bare use" and the lines were rewrapped), and "should have" -> "needs" in WAY-293.
No meaning of WAY-104 moved: both directions of the test, the held-sentence limit, the bare-use clause, the
glossary-entry clause and the code/interface clause all stand as before; the join keeps the bare-use clause
attached to the same condition ("in a sentence of those files"). No meaning of WAY-293 moved: "needs" reads as
"should have" did, the Minor default, the cited-sentence exception, the WAY-99 and WAY-263 carve-outs are untouched.
No new Critical or Important finding in the fix.

## The "should" left in the skill sentence

`task-cycle/review/SKILL.md:113` still says "a word should have a glossary entry", WAY-293 now "needs". The template's
ban is on the binding sentences of a decision entry; a skill's prose is not one, and the two wordings mean the same
and bound the same findings, so the skill does not state WAY-293 more broadly or less qualified (WAY-263 not
engaged). Not a finding; if the author wants the same word in both places it is a one-word edit in the skill.

## Checks I ran

- In a separate detached worktree of `049e84e` under the system temp directory (removed afterwards; the reviewed
  worktree, its index and branch untouched, `git status --short` empty):
  - `python -B elements/common/foundation_check.py .` -> `0 errors`, exit 0.
  - `python -B gate/run_tests.py task-cycle` -> 92 tests OK, exit 0.
  - read-only Python script counting sentences and the words "should"/"will" in the binding paragraphs of WAY-95,
    WAY-97, WAY-99, WAY-104, WAY-293 -> counts above, exit 0.
- `git diff 24e092c..049e84e` and `git log 24e092c..049e84e` read in full.
- Not run: the full `gate/run_tests.py` (the orchestrator's run), `gate/run_tests.py elements/common` (the fix edits no
  code; the author reports exit 0).

## Declined to judge

none

## Reaches beyond the dispatch

none (the template `elements/decisions/template.md` lines 94-99 are the criteria of the findings file and were read in
the first review).

## Searches not found or unclear

none. The Minor findings M1-M6 and the out-of-scope finding O1 of `review-1.md` are not fixed by this commit, as WAY-161
provides for them; they are not reopened here.
