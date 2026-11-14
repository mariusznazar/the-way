PASS 0364c08a6a9216899ab06bf13c61a1f6572bbd85

# Review of the fix of the whole-change findings — decision-log-second-round

Range `6a984c5..0364c08`: nine commits `26575cd` to `3849483` and the addition `0364c08`. `git
rev-parse HEAD` is `0364c08a6a9216899ab06bf13c61a1f6572bbd85`, the head given. The working tree is
clean. The findings file (`reports/review-whole-findings.md`, findings 1-5 and 7-10) bounds this
review (`task-cycle/review/fix.md`). Findings 6 and 11 belong to the orchestrator and 12 is out of
scope; they are not judged here.

Method: `git diff --word-diff -U0 6a984c5 0364c08`, split on whitespace, shows every change of
words. Apart from the hunks named below, each of the 35 files holds only rewrapped lines: the words
and their order are unchanged. That includes the 21 rewrapped lines of the log. Each touched rule
was read against its entry at the base, `git show ec7929d:foundations/decisions.md`.

## The findings

1. **WAY-207 exemplar clause — fixed.** `product-guidelines/coding/template.md:151-152` now reads
   "a fault of one file is fixed in that file, and the exemplar of its kind is not changed for that
   file's sake". Lines 157-158 give the entry's reason: "the exemplar is what every later file of
   its kind follows". With the approval clause already there, both halves of WAY-207's rule and of
   its *Rationale* now stand in the template.
2. **WAY-37 restated in an element skill — fixed.** `elements/environment-facts/skill/read.md` is
   back to the plan's text. The rule and its reason stand once, in
   `elements/common/way_of_working.md:114-118`.
3. **WAY-358 reason — fixed.** `task-cycle/record_template.md:225-228` now holds the first
   sentence of WAY-358's *Rationale* word for word.
4. **WAY-258 relation — fixed.** *Relations* now reads
   `derives from WAY-256 · derives from WAY-100`, and nothing else in the entry changed.
5. **WAY-09 inventory — fixed. The contest is accepted.** `foundations/part_map.md` now names:
   - for `installation`: the installer, its tests and the README;
   - for `gate`: its tests;
   - for `instruction-files`: the script's tests;
   - for `project-level`: the tests of its readiness check, plan check and reader of plan states.

   The wording comes from WAY-09 at the base. The fix agent is right that the `elements-common`
   sentence already names "the script that migrates a foundation from the earlier form of the-way"
   (`foundations/part_map.md:66-69`). That part of my finding was wrong. It is also right that the
   project-level sentence already named the checks, so only their tests were missing.
6. (Not in the file.)
7. **"held there" — fixed.** `elements/common/rules.md:52-55` reads "Splitting or merging entries
   gives each entry that comes out of it a new identifier", which is the base sentence. The reason
   from WAY-64 follows it. The bullet sits in the list about the three files, so its scope is as it
   was at the base.
8. **Projected-mode reason repeated — fixed.** The sentence is gone from the four element skills.
   It stands once, in `elements/common/projected_mode.md:4`.
9. **Duplicated rule sentences — fixed.** Each removed sentence still stands in the place it
   repeated:
   - `definition_change.md:10`;
   - "A new kind" in `product-guidelines/coding/SKILL.md`;
   - step 5 of `definition_variant.md` and `task_variant.md`;
   - the description of `product-guidelines/styleguide/SKILL.md`, beside "as before a first screen"
     in `recognize.md`.

   Removing them lost no rule of WAY-115, WAY-156, WAY-200 or WAY-184. The *Why* of those three
   withdrawn rows (WAY-115, WAY-156, WAY-184) now names those places (`0364c08`, `+3 -3`, rows only).
   I checked that each named file holds the rule.
10. **Long lines and the semicolon — fixed. The contest on WAY-288 is accepted.** The rewraps change
    no word (word diff). `process-audit/audit_count.py:54` ends with `;`. WAY-288 holds no added line
    over 100 characters: the one line my count showed at 101 is 99 characters of text once its dash
    is read as one character. A few lines now stand short in the middle of a paragraph, for example
    `gate/run_tests.py:17-18`. That is the fix agent's stated choice so that no line the change did
    not add is rewrapped. Acceptable.

## New findings in the fix

- **Minor.** `product-guidelines/styleguide/starting_rules.md:3` is a reason with no rule in its
  file. Since `d55625e` removed the timing sentence, the file opens with "A first screen built with
  no rules is the screen every later one copies." That is WAY-184's reason for the timing rule, which
  now stands only in the skill's description. A reader of `starting_rules.md` meets the reason
  without the rule it explains. Either drop the sentence or say that it is the reason the styleguide
  comes before the first screen. It blocks nothing.

No new Critical or Important finding: no rule was lost and no meaning changed, as the word diff and
the readings above show.

## Checks

| Command | Exit code / result |
|---|---|
| `git rev-parse HEAD`; `git status --short` | `0364c08…`; clean |
| `git diff --word-diff=plain --word-diff-regex='[^[:space:]]+' -U0 6a984c5 0364c08` | 0; word changes only in the hunks named above |
| `python -B elements/common/foundation_check.py` | 0; `0 errors`, and the one expected `listed:` line for `tracked-file-private-paths` |
| `python -B gate/run_tests.py elements/common` | 0; 201 tests OK |
| `python -B gate/run_tests.py elements/part-map` | 0; 39 tests OK |
| `python -B gate/run_tests.py gate` | 0; 36 tests OK |
| `python -B gate/run_tests.py instruction-files` | 0; 104 tests OK (5 skipped) |
| `python -B gate/run_tests.py project-level` | 0; 275 tests OK |
| `python -B gate/run_tests.py task-cycle` | 0; 440 tests OK |
| `python -B gate/run_tests.py process-audit` | 0; 182 tests OK |

## Unread material

- `reports/review-whole-findings.md`: I did not read it again. The dispatch says it holds findings
  1-5 and 7-10 of my report word for word, so I judged against my report's text of them.
- The touched files were read in their diff and at the fixed spots, not whole:
  - `part_map.md:60-75`;
  - `kinds.md:1-16`;
  - `coding/template.md:144-159`;
  - `starting_rules.md:1-8`;
  - WAY-288 at the head.
- `definition_variant.md`, `task_variant.md` and `product-guidelines/styleguide/SKILL.md`: I relied
  on the fix report's citations and checked only by my earlier readings in the review of the whole
  change.

## Searches not found or unclear

- WAY-288's long line: my earlier count was in the console's decoding, not in characters. Resolved
  as in finding 10.

## Working copies

None. I made no worktree or copy of the repository and created no `.runs/review-fix/`. My scripts'
outputs stood in the session scratchpad, outside every repository.
