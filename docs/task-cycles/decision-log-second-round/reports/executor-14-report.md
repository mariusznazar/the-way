# Report of executor 14

**Status:** done

**Commits:** `5959aa9` — Remove the withdrawn decision numbers from the coding guidelines settle, task document, trial run and template files and give each rule its reason (4 files, +72 -63).

Files changed (added/removed lines):
- `product-guidelines/coding/settle.md` +20 -18
- `product-guidelines/coding/task_document.md` +2 -2
- `product-guidelines/coding/trial_run.md` +1 -1
- `product-guidelines/coding/template.md` +49 -42

## Checks

- `python -B elements/common/foundation_check.py | grep -E "product-guidelines/coding/(settle|task_document|trial_run|template)\.md"` — no line printed (grep exit 1). The check itself exits 1 from lines of files of slices not yet made, as the plan says.
- `grep -nE "WAY-(76|86|171|191|200|201|202|207|208|210|211|271|272|275|277|278|279|281|310)\b"` over the four files — no match (grep exit 1).
- I did not run `gate/run_tests.py`; the slice lists only the check above.

## Own-work check

Requirement most likely missed: "the sentence around each removed number reads as before, and no other change". Check: read the whole `git diff` of the four files hunk by hunk. Every hunk is either a removed number with its brackets (or one number out of a list), a rule sentence added, or a reason sentence added; the line breaks I moved are only on lines I touched (two long lines I produced were rewrapped to under 100 columns). The one place where the check found a risk: `template.md` line 196-197 says "A rule carries no reason: the reasons stand in the decisions it names (WAY-168)". It speaks of the rule text that a product writes, so I left it; the template's own reason sentences are not that text.

## Reasons added (file, sentence, entry read at base `ec7929d`)

- `settle.md` (library bullet), after the rule sentence "A cycle that needs such a library chooses none alone." (added first; from WAY-277's rule): "A library that writes log lines reaches every file that writes one, so its choice is met once, by the human who adopts the rules, beside the form of a line that shows the need for it." — WAY-277 *Rationale*, first sentence.
- `settle.md` (decision on the rules on failures and logs, before "A heading … `none —`"): "One entry gives the same shape whichever way the rules reach a product, and a product that adds them leaves its older decision alone." — WAY-279 *Rationale*, first sentence.
- `template.md` (three standing checks bullet): rule sentence added first, "The task that writes a product's coding guidelines is complete only once the product's log holds, for each of the three standing checks, a decision adopting it or departing from it with the reason." (WAY-202 binding text). Reason: "A product whose code no standing check reads changes its style and takes in a known vulnerability with no signal." — WAY-202 *Rationale*, first sentence.
- `template.md` (Linter bullet end): rule clause added first, "which the human approves" after "is a change of the adopting decision" (WAY-207 binding text, and `settle.md` already says it). Reason: "A rule of the linter reads every file of the parts it covers, so turning it off for one file's sake changes what binds all the others, unseen by the task that made the change." — WAY-207 *Rationale*, first sentence.
- `template.md` (end of first paragraph of "The rules on failures and logs"): "An agent that reaches a running product's logs finds there only what the code wrote, so what the code writes decides whether a failure can be diagnosed at all." — WAY-271 *Rationale*, first sentence.
- `template.md` ("Recording a failure" bullet end): "A line written once, where code handles the failure, keeps one failure from reading as several, the original error keeps the cause a string loses, and a failure no code handled would leave no trace at all without a last-resort handler." — WAY-272 *Rationale*, third and fourth sentences joined into one.
- `template.md` ("Business events" bullet end): "The events give what happened before a failure, which lines of failures alone do not." — WAY-275 *Rationale*, second sentence.

## Entries left under the "stay" rule

WAY-363 stays at `settle.md` (the "or a departure from the rule" bullet) and `template.md` (the "Size of a function and a file" bullet): untouched. None of the other nine stay-numbers (WAY-93, 94, 97, 263, 287, 294, 295, 297, 364) stands in the four files.

## Findings

- WAY-207's rule also says the exemplar is not changed for one file's sake. `template.md` has no sentence for it; I added only the approval clause and the reason, since the reason I gave concerns the linter's rule, and the plan names only the approval as missing. Not guessed further.
- WAY-279's reason covers why the decision is one entry apart from the template's adoption; the reason for "the task is not ready without it" is WAY-278's, which I removed without a reason (the slice asks none for it).
- The plan's remark for WAY-202 at `settle.md` says nothing of a reason there; I added none.

## Reaches beyond the dispatch

None.

## Choices

- Placed the WAY-279 reason sentence in `settle.md` directly after the rule sentence "the task is not ready without it." rather than after the `none —` sentence just before "It takes:"; the first is where the rule stands. Cost if wrong: one sentence moves.
- Joined two sentences of WAY-272's *Rationale* into one so the reason stays one sentence and covers both the single line and the last-resort handler. Cost if wrong: a longer sentence to cut.

## Unread material

none (the *Read* entries WAY-293 at its current place, and WAY-202, 207, 271, 272, 275, 277, 279 at the base, each whole; the four files whole).

## Searches not found or unclear

none.

## Working copies

`.runs/executor-14/` held `apply.py` (the replacement script) and `base.md` (the base log, `git show ec7929d:foundations/decisions.md`). Both files removed one by one before return.
