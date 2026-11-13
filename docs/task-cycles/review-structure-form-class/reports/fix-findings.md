# Findings for the fix — review of the whole change `FAIL 5353268`

Cut from `reports/review-whole-change-report.md` in the reviewer's words (WAY-161): the blocking finding, then the Minor findings within the task. M6 of that report lies outside the task's scope and is not here.

### Important

**I1. The condition for marking the rule of size violated leaves out the exceptions, so a product whose only code over a
threshold is excepted is told to mark a met invariant violated.** Within the task (To do 3, row 3, question 4). From the
one author, commit `c7a6733`.

- Places:
  - `foundations/decisions.md:11797-11798` (WAY-355, binding): "Where the product's code is over a threshold, the rule's
    invariant is marked violated until the code is cleaned (WAY-51)."
  - `product-guidelines/coding/template.md:241-242`: "Where the product's code is over a threshold when the rule enters, the
    invariant is marked violated until the code is cleaned (WAY-51)".
  - `product-guidelines/coding/settle.md:113-114`: "where the trial run found code over a threshold, it is marked violated by a
    change of the foundation the human accepts".
  - `product-guidelines/coding/trial_run.md:30-31`: "where the code is over a threshold, step 4 proposes the rule's invariant
    marked violated (WAY-51)".
- What is wrong: the rule's own invariant (template.md, same bullet) is "that no function and no file of the parts named
  is longer than its threshold, other than those the decision's exceptions name". A function the human keeps whole as an
  exception is still code over a threshold, so all four sentences, read as written, mark the invariant violated where it
  holds. WAY-355's own *Verification* shows the intended meaning — "lists that function as an exception … and marks the
  rule's invariant violated where **other** code stands over" (`foundations/decisions.md:11808-11809`) — and question 4's
  answer says "gdy kod **już** przekracza próg" alongside "funkcje, których dzielić nie warto, dostają wyjątek"; the binding
  sentence drops both qualifications.
- Why it matters: the trial run happens before the exceptions are settled (settle.md asks thresholds, then exceptions,
  then invariants), so an agent following settle.md and trial_run.md proposes the violated mark from the trial run's count
  alone. Where every function over the threshold becomes an exception, the invariant's test is then marked as an expected
  failure and passes; under WAY-51 that test is to be unmarked when it passes, and a test runner fails on an unexpected
  success (the-way's own `gate-exit-code`: "exits non-zero when … a test marked as an expected failure passes"). The
  product's guidelines task would reach its gate with a foundation mark the human accepted and that the code
  contradicts — a blocked request for a wording slip. The binding sentence of WAY-355 is also what a later reader of the
  product's adoption checks against.
- Evidence: the four quoted sentences against the template's invariant sentence and WAY-355's *Verification*; nothing in
  the change says what happens where all over-threshold code is excepted.
- Fix in kind: "over a threshold, other than the exceptions of the decision" (or "where code other than the exceptions
  stands over a threshold") in WAY-355's binding sentence, template.md, settle.md and trial_run.md; trial_run.md and
  settle.md can say the mark is proposed once the exceptions are settled.

### Minor

Each within the task unless marked otherwise.

**M1. `foundations/decisions.md:11968-11970` (WAY-359, *Rationale*)** — "the same remark on the form of an entry was graded
blocking in 9 runs of an experiment with reviewers and Minor in 8, and 6 of its 32 runs rejected the change for its form
alone". The measurement stands with no conditions, while WAY-05 and the decisions template
(`elements/decisions/template.md:61-65`) let a measurement stand only "with what was measured and under which conditions".
The author's report says the task does not tie this experiment to WAY-229's; it does: the task's *Context* names cards D2
(the grade of the form) and D3 (the class of the reviewer) of one and the same "raport o eksperymencie z recenzentami",
and 32 runs is four variants of WAY-229's "8 runs a variant". Fix: one sentence pointing to WAY-229 for the conditions,
as WAY-164 does (`foundations/decisions.md:4918`). Minor: no sentence of the entry is read wrongly for lack of it, only
weighed without its population.

**M2. `product-guidelines/coding/template.md:75` and `:223`** — "It is no standing check, and the linter's set holds no rule
of it" / "It is no standing check and no rule of the linter's set." The glossary defines a standing check as "a check that a
tool makes of every change to a product's code for the whole of the product, rather than for one kind of code"
(`foundations/glossary.md`, `## standing check`), which is what the rule's test is: a tool run over the whole of the code on
every change. The sentence gives the term a second, narrower meaning ("one of the three checks WAY-202 requires"). Fix:
"It is none of the three standing checks the template requires (WAY-202)", or drop the clause; the next clause about the
linter's set already carries the point. Minor: the template spells out the rule's whole machinery, so no step goes wrong
by it; it is a word used against its glossary entry (WAY-99), with no behaviour that follows from it.

**M3. `product-guidelines/audit_end.md:52-55`** (not changed by the range) — "take from it its mode alone: the check of the
required headings of the rules on failures and logs, with the question to the human it brings at a refresh, waits for the
turn of the skill whose step it is." The change adds to `recognize.md:37-41` a second refresh check, of
`### Size of a function and a file`, with its own question to the human, and the sentence that defers the first check in a
task joining coding and testing does not name it. An agent running coding's step 1 from the testing skill may ask the
human about the rule of size out of turn. Fix: name both checks, as `product-guidelines/coding/SKILL.md:105` now does.

**M4. `task-cycle/review/whole_change.md:33`** — "Take your numbers from two runs of your own, none in the reviewed
worktree". The first run is `change_file_sizes.py`, which writes nothing (its test
`test_the_command_changes_nothing_in_the_repository`, and my run on this range left `git status --porcelain` empty), and
section 2 of the skill asks for a separate worktree only "when they need files changed". In a product the instruction
also misleads: `python -B .the-way/task-cycle/change_file_sizes.py` is to be run "from the root of the repository", and a
fresh `git worktree add` leaves the `.the-way` submodule unpopulated, so in a separate worktree the path does not exist.
Fix: "the second in separate worktrees" — let the script run in the reviewed worktree.

**M5. `task-cycle/test_change_file_sizes.py`** — two behaviours of the script are untested: the status `T` and its note
`type changed` (`task-cycle/change_file_sizes.py:165-166`; `grep -c "type changed"` on the test file gives 0), and the
escaping of `|` in a file name (`change_file_sizes.py:205`; no test name holds `|`). A change that drops either passes
every test. Separately, a name holding a backtick breaks the Markdown code span of its row (scratch run: the row
`` | `back`tick.md` | 1 | 2 | +1 | modified | ``). Polish; the numbers are right in every case tried.
