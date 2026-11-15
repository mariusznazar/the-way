PASS 31f7507bce088ecf6ee825889bfada949076db68

# Review of the fix of the five Minor findings — foundation-review-reminder

Range `b7ec371207ad67d6378f323433f643e1703335e5..31f7507` (`git rev-parse HEAD` = `31f7507bce088ecf6ee825889bfada949076db68`, the head given); commits `9638c91`, `31f7507`. Files changed: `foundation-review/proposals.md` (+4/-4), `foundation-review/weak_points.md` (+4/-4), `foundations/decisions.md` (+14/-13), `task-cycle/skill/SKILL.md` (+13/-9), `task-cycle/skill/request_template.md` (+2/-2). My commits: none. Blocking findings: 0. New Minor findings of the fix: 1. Findings remaining: 0 of the 5.

## The five findings

1. **`weak_points.md`, the contradiction about a rule that ends with its own change — fixed.** The sentence now reads "A rule that ends with its own change fails the plan test and gets no line here, as it gets none above (WAY-36)." It uses the words of the unchanged transitional section ("A rule that ends with its own change is no entry of the log (WAY-36) and gives none"), so the two sections no longer send the same class of entry to different places. Evidence: both passages read side by side at `31f7507`.
2. **WAY-24 and WAY-300 *Rejected* — fixed.** Both entries now reject "a sentence that asks for no line and says nothing of the backlog, the human's own setup adding the line"; "as it was" is gone from both. WAY-24's second kept way now reads "a task of the review made ready for a cycle and copied into the backlog — three steps where one command does", which no longer rejects the line a human adds as a mark. The first kept way ("run by a cycle that ends in a request of corrections") stays; I found it saved by those words in the first review and it still is. `python -B elements/common/foundation_check.py`: exit 0, `0 errors`.
3. **The source of "the name of the repository" — fixed.** Step 13 now gives the name as the last segment of the address of the remote `origin` of the repository the request merges into, without `.git`, or, where there is no such remote, the name of the directory of its main checkout, the same in every cycle and every worktree "whatever the `## Backlog` section names". The qualifier I found narrower than the task is gone. The template points to step 13 ("taken as `SKILL.md` step 13 gives it") and WAY-300's second paragraph says the name "is the same in every cycle", so the three texts agree and none restates another's rule differently. Judged against point 1 and question 3: the task says "nazwa repozytorium" with the example "Przegląd fundamentu loop2 (`review-foundation`)"; the last segment of the remote's address is the repository's own name on its host, which is what the example shows, and it holds for a product whose section names a directory or a public tracker. For this repository it gives `the-way` (the author's check: origin `…/the-way.git`). The ways the author rejected stand: the checkout directory alone would differ per worktree (this worktree's directory is `foundation-review-reminder`), the name the section gives fails where the section names none, and the bare phrase gives no source. Residual, not a finding: the rule leaves a few details to the orchestrator (an address with a trailing slash or an `scp`-style address, a product with a `.the-way` submodule, where the remote meant is the product's — the sentence says "the repository the request merges into"); the same name comes out of every cycle whichever way it is cut, and the sentence the cycle writes states the name it expects, so a mismatch shows to the human. WAY-300 names no source of its own for the name, only that it is the same in every cycle; the rule itself stands in a skill step, which is where WAY-293 puts a rule of how an agent works.
4. **The failed count among the checks not run — fixed.** Step 13 now says: where the script ends with exit code 2, "record its message under *Verification*, write no reminder, since the count is unknown, and put the count among the checks not run in the section for the human's decisions (WAY-287)". WAY-287 lists "the steps skipped and the checks not run" in that section; the two now agree.
5. **The two long lines — fixed.** The paragraph of `foundation-review/proposals.md` and line 4 of `foundation-review/weak_points.md` are rewrapped; `awk 'length>100'` over `proposals.md`, `weak_points.md` and `with_the_human.md` prints nothing.

## New findings in the fix diff

### Critical / Important

none

### Minor

1. **`foundations/decisions.md`, WAY-300 *Rejected*, the line "later review needs a new one, since the old stays on a done line; no reading of the backlog, the sentence always asking for the"** — 127 columns, left over by the author's rewrap commit `31f7507` (the report claims the lines of WAY-24 and WAY-300 were rewrapped); the line "identifier the-way computes for the review's line, in the field of identifier …" is 101 columns. Besides this, the second paragraph of WAY-300 now has a short ragged line ("(WAY-107). Where no such line stands, or") after the edit. Polish; no check reads it; the finding 5 repair was for the other two files and holds. Within the task.

## Declined to judge

- That the decision log's remaining lines over 100 columns that were already there stand: outside the fix diff.
- Whether the exit-2 clause of step 13 (the author's earlier addition) should exist at all: not the fix's subject.

## Checks I ran

| Check | Command (from the worktree root) | Result |
|---|---|---|
| Head | `git rev-parse HEAD` | `31f7507bce088ecf6ee825889bfada949076db68` |
| Diff of the range | `git diff b7ec371..31f7507`, `git log --oneline b7ec371..31f7507` | read whole |
| Foundation entries | `python -B elements/common/foundation_check.py` | exit 0, `0 errors` |
| Whitespace | `git diff --check b7ec371..31f7507` | exit 0 |
| Width of the lines the fix added | awk over the added lines of the range, over 100 columns | 2 lines, both in WAY-300 *Rejected* (Minor 1) |
| Width of the three skill files of the review | `awk 'length>100'` over `foundation-review/proposals.md`, `weak_points.md`, `with_the_human.md` | none |

Not run: the full gate (as asked); `task-cycle` tests (the author ran them at 480 OK; the fix changed Markdown only, and the script and its test are untouched); a trial of the name rule on a real product (the only repository available is this one, where the author's check gave `the-way`, which I take as stated and did not repeat). The rule's behaviour for a `.the-way` submodule is unverified.

## Reaches beyond the handoff

- The three passages of `weak_points.md` (the transitional section and the new section, whole): to compare the two sentences of finding 1.
- WAY-287 (in `foundations/decisions.md`, read whole in my first review): to compare it with step 13 for finding 4.
- WAY-293 (read whole in the first review): to place the name rule in a skill step and not in an entry.

## Unread material

The decisions I selected in my first review (index kept at `reports/review-whole-index.md`) were read as that report counts (19 whole); this review adds none and relies on that reading. In this review: the findings file, the fix handoff, the author's fix report, the fix method and the whole diff of the range were read whole; `task-cycle/skill/SKILL.md` and `request_template.md` were read only at the changed passages and their neighbours in the diff (step 13 and the *How to merge* bullets), as in the first review.

## Searches not found or unclear

- A source in the foundation for how the-way names "the repository" for a request in a product with a `.the-way` submodule: not found; step 13's sentence "the repository the request merges into" is the only statement, and it is clear enough for the case.
- Nothing else new.

## Working copies

None made. I did not create `.runs/review-whole-fix/`; the reviewed worktree is unchanged (`git status --short` clean).
