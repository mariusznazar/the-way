# Slice 10 report — the instruction-files skill: names and emphasis

**Status:** done
**Commit:** `fcb701e` Name the readers' words as a rule and word the emphasis point as the Claude docs give it
**Files changed:** `instruction-files/SKILL.md` (+5, −1)

## What changed

In `instruction-files/SKILL.md`, section "How to write a single rule":

1. **New bullet (item 28a):** "A rule names things in the words its readers use for the product." The bullet gives the same wording as `instruction-files/writing.md` step 4 ("in the words its readers use for the product", with the same examples `Where things are`, `Before you release`), so the two files give one account, not two.
2. **Emphasis bullet (item 28b):** the sentence "piled-on emphasis makes a current model over-apply the rule" now reads "the Claude Code documentation says piled-on emphasis mostly makes Claude over-apply the rule, and that older models sometimes needed the emphasis". The citation stays.

## Source passage (item 28b)

Read from https://code.claude.com/docs/en/best-practices, section "What you can stop doing", table row "Add IMPORTANT or ALL CAPS to instructions Claude keeps missing":

> Older models sometimes needed the emphasis. Current ones follow a plainly worded line, and piling on emphasis mostly makes Claude over-apply the rule. If it's a rule that can't bend, turn it into a hook or a deny rule. If the line is getting lost in a long file, the file needs to be shorter.

The page speaks of Claude, uses "mostly", and does not claim anything about every model. The new sentence says no more than that. The page was readable, so no question was raised on this item.

## Other places the handoff named

- `instruction-files/kind_main_file.md:10-22` (emphasis): this range has no emphasis sentence. Its citation of the same page is at line 18, and it supports a different claim: that a repository overview does not help agents and the agent reads the repository itself. The page's matching row is "Describe your architecture and file layout in `CLAUDE.md` — Claude reads the repo itself. Only write down what isn't in there." Changed nothing in `kind_main_file.md`, as the handoff asks.
- `instruction-files/writing.md:14` — confirmed: step 4 holds the names rule. Not changed (outside the slice's *Change* line).
- `foundations/decisions.md` WAY-130 (`:3317-3353`) and WAY-133 (`:3418-3448`): read; the current texts are the ones the slice cites. Nothing in them requires a change for item 28. The skill's citations of WAY-130/WAY-133 are untouched.
- `foundations/environment_facts.md:162-166` (single-rule-compliance) and `foundations/invariants.md:86-94` (tracked-file-private-paths): read; no change needed by this slice.
- WAY-322 (`foundations/decisions.md:10370`): read only to see whether it touches the instruction-files skill. It concerns the technology step's list of matters, so it has no bearing on this slice.

## Own-work check (section 3)

- Requirement: the new names rule must not contradict `writing.md` step 4, and the emphasis sentence must not state more than the page. Check: compared the new bullet word for word with step 4; compared the emphasis sentence with the page's row (quoted above). Result: wording matches step 4's key phrase; the emphasis sentence keeps the page's hedges ("sometimes", "mostly") and its subject ("Claude"). The `check_instructions` test suite (checks 1 below) passed, so the skill's own check still runs.
- The new bullet's code span `Where things are` wraps over a line break in the Markdown. It renders as one code span in Markdown, and the check suite does not flag it. Noted, not changed.

## Checks (command — exit code)

1. `python -B gate/run_tests.py instruction-files` — exit 0 (104 tests, OK, skipped=5; the skips are link tests that need POSIX links on Windows)
2. `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0 (0 errors)
3. `python -B -m unittest discover -s task-cycle -p "test_tracked_files_private_paths.py"` — exit 0 (9 tests, OK)
4. `git diff --check` — exit 0

No check failed, so no re-run pair was needed. The failing run of a test written first does not apply: this slice writes prose, not a test.

## Reaches beyond the handoff

- `task-cycle/change/SKILL.md`, `task-cycle/change/slice.md`, `agent-instructions/README.md` — read for the method (named in the handoff).
- `instruction-files/writing.md` — read whole; a named file.
- `instruction-files/kind_main_file.md` lines 1-40 — read to check the emphasis claim.
- `foundations/decisions.md` lines 10370-10400 (WAY-322) — read to check for bearing on this slice; none.
- https://code.claude.com/docs/en/best-practices — fetched with WebFetch; the full page was saved to `a saved tool result outside the repository`, and the table row is at its line 617.

## Searches not found or unclear

- `kind_main_file.md:10-22` does not contain an emphasis sentence (see above). The handoff's range label "emphasis" points to the citation at line 18, which is about a different claim.
- None else.

## Choices, and questions for the orchestrator

- **Choice:** the names rule is placed in SKILL.md's section and worded to match `writing.md` step 4, not moved out of `writing.md`. Rejected: deleting step 4 and pointing to the SKILL bullet — it would be the one-place fix, but `writing.md` is outside this slice's *Change* line. Cost if wrong: two files now hold the same rule, which the "one place" bullet forbids. Recorded as a question below.
- **Question 1 (recommended answer: yes, in a later slice or a small follow-up):** should `instruction-files/writing.md` step 4 be reduced to a pointer to the new SKILL.md bullet, so the rule has one place? Recommended: yes — the SKILL rule is the one place, and step 4 becomes "Name the file's sections as the rule 'How to write a single rule' gives". Rejected: leaving both — works today because the wording matches, but drifts on the next edit.
- **Question 2:** none beyond the above.

## Problems observed

- None in the code. The gate's `instruction-files` run reports 5 skipped link tests on Windows; this is the existing state, not caused by this slice.
