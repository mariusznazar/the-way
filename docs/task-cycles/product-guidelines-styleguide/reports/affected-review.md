# Affected review — `896071a..e549363`

Reviewer: the final whole-branch reviewer of this cycle (claude-opus-5-5); I wrote none of this
range. Method: Superpowers 6.4.1 `requesting-code-review`, template
`C:/Users/Mariusz/.claude/plugins/cache/claude-plugins-official/superpowers/6.4.1/skills/requesting-code-review/code-reviewer.md`.
Handoff: `reports/affected-review-handoff.md`.

**What the range holds.** Ten commits in nine files.
- The return step: `19d28f8`.
- Its settlement by ruling C32: `c355004` (WAY-167 reverted), `4a4f08e` (the F4 naming cases),
  `d1585d0` (the form check narrowed), `677ef7c` (the template's copy of the reworded sentence).
- The assessment settlement: `04f8754`, `8ff8966`, `35860df`, `3550497`, `e549363`.

**How I reviewed it.** I read the whole range in one pass from the diff, against the frozen task's
27 rows, `reports/assessment-settlement.md`, ruling C32 and the `cycle.md` entries for it. I checked
the new *Based on* of WAY-175 against its sources: every passage it quotes was found in
`loop2-10x` `e854fef5:.claude/skills/10x-ui/SKILL.md` and in `loop` `715026e:.agents/skills/om-ux-*`,
some of them across a line break. I ran one deliberate break in a detached worktree
(`C:/Storage/repos/the-way-wt/pg-affected-review`, restored and removed). I re-ran no whole suites;
the evidence for them is `return-*.txt`, `return-c32-*.txt` and `settlement-*.txt`.

## Strengths

- **C32 restores row 1's meaning and makes the code and its checks follow it.**
  - Row 1 is "jeden na dziedzinę" (one file per discipline). WAY-167 is back to one file for each
    discipline, and one for each user interface for the styleguide (`c355004`).
  - The form check now accepts a part in a file's name only for a discipline whose template is
    per part (`product-guidelines/form_check.py:863-878`). Before, it also accepted
    `guidelines/<discipline>-<part>.md` for any other discipline.
  - The F4 cases were narrowed by the check author, not by the executor (WAY-69). They now hold
    `testing-web.md` and `testing-mobile.md` as names that disagree with their *Discipline*
    (`product-guidelines/test_form_check_invariants.py:481-486`), with the controls adjusted
    (`:495-500`).
  - This closes ledger Task 1 M6 (the name part) and the `<discipline>-<part>` half of my earlier
    Recommendations.
- **WAY-170 now names its exception instead of contradicting it** (`8ff8966`, `04f8754`).
  - Until a gate of the-way runs a product's invariants, the installer's block names the script's
    two commands "to run before every merge". This agrees with the fix `896071a`.
  - The relation is `narrows WAY-16`. The *Review when* names the state that ends the exception.
  - *Violates* gains the stale case: the block still naming the commands once a gate exists.
- **WAY-186 now holds the scope of *To do* 8** (starting rules for a styleguide written before the
  first screen, research again at every refresh or extension). This closes my Task 4 note (b)
  without narrowing row 16: the repeated research stays.
- **WAY-175 stops restating what other decisions bind** (WAY-19). It names each piece by the
  decision that carries it.
  - Its *Based on* is an observation: repository, commit, path and passages. I re-read every
    passage at the stated commits.
  - The course's private lesson is said to be unquotable rather than paraphrased as a source.
- **The `guidelines-check-carrier/1` sentence now says exactly what the check decides** (see
  "Reworded sentences").
- **The other settled items keep their rows' meanings.**
  - Row 21's "wydanej" (published) is kept by "the newest edition that is a W3C Recommendation"
    (WAY-191, `SKILL.md:180-182`).
  - The new step "Which criterion, which ratio" (`SKILL.md:187-193`) asks even where it has a
    recommendation and shows the choice by what the user sees (rows 23 and 27).
  - The glossary's "user interface" (`foundations/glossary.md:217-222`) matches root C14.
- **Pointers to a "spec" the repository does not hold are replaced** in code and tests by the
  decision or invariant that holds the rule (WAY-27, A13).

## Issues

### Critical (Must Fix)

None.

### Important (Should Fix)

None.

### Minor (Nice to Have)

1. **"Each with the values and the links those templates give it" in `guidelines-form/1` is wider
   than the check.**
   - File: `foundations/invariants.md:2135` and its copy, `product-guidelines/template.md:150`.
   - What: for each required rule, the styleguide template's "What each section carries" names a
     *Decision* and an *Invariant*. For example, "Every background with its text" carries
     *Invariant*: the product's copy of `guidelines-form`, and "Visible focus" carries *Decision*:
     the WCAG adoption decision (`product-guidelines/styleguide/template.md:98-113`). A reader can
     take those for "the links those templates give". The form check never verifies them: a
     styleguide whose "Every background with its text" names `role-meaning` as its invariant
     passes. The links the check does verify — *Kind* from the closed list, a background's *Text on
     it* naming a text role, a decision in every row, and every role decision named by
     `### Each role in its meaning` (`form_check.py:774-834`) — are not named in the sentence.
   - Why: the sentence's verdict should cover exactly what it says (WAY-61). Read broadly, the
     product's method passes while the sentence is false. The defect is in the wording only; no
     behaviour is lost.
   - Fix: name what is checked: "its table of roles with each *Kind* from the template's list, each
     background's *Text on it* naming a text role of the table and each of its decisions named by
     `### Each role in its meaning`". The version stays 1 before `main`, and the template's copy
     follows byte for byte. That wording would also close ledger Task 1 M5, the pair rule naming
     `guidelines-form`, whose sentence said nothing of pairs. The rewording already half-closes it.
2. **"Section" now carries two meanings in the styleguide template.**
   - File: `product-guidelines/styleguide/template.md:4, 73, 75`; `product-guidelines/styleguide/SKILL.md:197`.
   - What: A7 replaced "part" with "section", so "What each section carries" now lists both
     `## ` sections and `### ` rules and examples ("Each section below is marked as a rule or an
     example"). The same file's required form and its rules use "section" for `## ` headings alone
     (`:19-21`, `:58-66`), as `product-guidelines/template.md` does.
   - Why: an agent writing a styleguide can read a rule as a section. It is less ambiguous than
     "part" was, but not apart from the template's own structural word.
   - Fix: "What each item carries" / "Each item below", matching A7's "item" and the skill's
     `:197`.
3. **Unwrapped lines in edited binding sentences.**
   - File: `foundations/decisions.md:6159` (WAY-186, about 160 characters) and `:6343` (WAY-191);
     the neighbouring lines keep about 100.
   - Why: cosmetic. No guard checks it, and a rewrap later changes no fingerprint (the binding text
     is the same words), but it adds to the diff.
   - Fix: rewrap while the entries are edited in place.

## Declined to judge

- **The four remarks of the assessment that were rejected (A4, A5, A12, A15, A16) and the cut of
  WAY-181.** Set aside: the root settled them against the rows (`assessment-settlement.md`). I
  checked only that no applied change contradicts a row. A16 carries the same point as my earlier
  Minors 1–3 (unchecked examples and rule order), which stay for the request.
- **Whether the new glossary entry "user interface" collides with earlier uses of the words in the
  foundation.** Set aside: `glossary-term-collision` and the glossary guard ran green in the
  settlement evidence. I did not search all 192 decisions again.
- **The new `guidelines-reference-current` *Part* in the-way
  (`… · agent-instructions · relation-model`).** Set aside: it applies A11 and only widens when the
  invariant runs, which in the-way holds trivially, since the-way has no guidelines.
- **Whether WAY-170's `narrows WAY-16` meets WAY-25's form for stating the area.** Set aside: the
  decision guard checks the relation form (0 errors in the evidence), and the area is stated in the
  added sentence.

## Deliberate break

- **Break:** in `product-guidelines/form_check.py:873` I changed `elif stem == discipline:` to
  `elif stem == discipline or stem.startswith(discipline + "-"):`. This accepts a part in the name
  of guidelines of any discipline, which is what the narrowing in `d1585d0` removed.
- **Command:** `python -B gate/run_tests.py product-guidelines --record .runs/product-guidelines-tests.jsonl`
- **Result: detected.** Exit 1, 61 tests, 3 failures:
  - `test_form_check_invariants.Form.test_a_file_whose_name_and_discipline_disagree_is_reported`,
    in subtests `guidelines/testing-web.md` and `guidelines/testing-mobile.md`. The record gives
    `guidelines-check-form/1` the verdict `fail`.
  - The ordinary test
    `test_form_check.Names.test_a_part_in_the_name_of_guidelines_other_than_a_styleguide_is_an_error`.
- The break was restored with `git checkout` and the worktree removed.
- Full command, diff, exit code and output:
  `.runs/task-cycles/product-guidelines-styleguide/reports/affected-break-naming.txt`.

## Reworded sentences

- **`guidelines-check-carrier/1`** (`foundations/invariants.md:2165`, `04f8754`): **holds exactly.**
  - The sentence now says: a rule whose *Decision* holds no decision number with the log's prefix
    followed by `@`, and in a styleguide whose *Invariant* holds no identifier of the invariants
    file followed by `@`. That is what `decisions_named` and `names_invariant` decide
    (`form_check.py:476-483`, through `Foundation.decision`/`.invariant` at `:445-458`). A
    number the log does not hold passes this check and is caught by
    `guidelines-check-reference-target`, as A10 intends.
  - The only difference is that the code requires at least one letter or digit after `@`, so
    `ABC-01@` with nothing after is still an error. The sentence says the check reports every such
    rule; it does not say it reports nothing else, so an extra error cannot make it false.
  - No test can pass while this sentence is false: the F4 carrier tests break the *Decision* and
    the *Invariant* fields and the coverage of role decisions, and the first deliberate break of
    this invariant was detected (`slice-2-break-guidelines-check-carrier.txt`).
- **`guidelines-form/1`** (`foundations/invariants.md:2135`, `19d28f8`; copy at
  `product-guidelines/template.md:150`, byte-equal): **holds for what the check records; wider in
  one phrase.**
  - Adding "tables" makes the sentence name what the check already recorded under it: the columns
    of the roles table, *Kind*, *Text on it*, the decision of each row, and their coverage. So the
    rewording narrows the gap of ledger Task 1 M5.
  - "Each with the values and the links those templates give it" can be read to cover each
    required rule's *Decision* and *Invariant* as the styleguide template proposes them, which no
    check verifies (Minor 1). Under that reading the product's method passes while the sentence
    is false.
  - In the-way, which has no guidelines, the invariant holds trivially, so no test of the-way
    passes falsely. The risk is for a product.
  - Required examples and the order of the product's further rules stay outside the sentence, as
    before (my earlier Minors 1 and 3, A16), so the sentence does not claim them.

## Assessment

**Ready to merge?** Yes

**Reasoning:** The range does what C32 and the assessment settlement say, and no row of *Settlements
to record* takes another meaning. The C32 narrowing is guarded: its deliberate break fails the tests
of `guidelines-check-form/1`. The three Minor findings are wording: one phrase of `guidelines-form/1`
claims more than its check gives, "section" now has two senses in the styleguide template, and two
lines are unwrapped. All three can go to the request.
