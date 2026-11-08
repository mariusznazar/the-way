# Report of the fix of the review's findings — task cycle `test-artifacts`

Findings file: `reports/findings1.md` (review verdict FAIL d0d3ce6). Fix range starts at `d0d3ce6`.

## Status

`done`

## Commits

- One fix commit on `task/test-artifacts` (see `git log --oneline -1`; message "Fix the findings of
  the review of the whole change"), on top of `d0d3ce6`. Worktree clean after it; nothing pushed.
- Files changed: `foundations/decisions.md`, `foundations/glossary.md`, `foundations/invariants.md`,
  `project-level/definition_template.md`, `project-level/technology/{research,start,task_run}.md`,
  `task-cycle/review/SKILL.md`, `task-cycle/skill/SKILL.md`.

## Each finding

### I-1 — fixed (option: revert the glossary change)

Chosen: revert `foundations/glossary.md` to the definition of the base, "the means through which an
agent checks behaviour ... while it runs". Reason: it is the smaller fix (one line, no rewriting of
six uses in five files), it keeps WAY-219's "no such way" and WAY-317's "way settled, no place" as
two different cases whatever reading of the term an agent takes, and WAY-121 / WAY-165 already carry
the place as the fourth matter looked at with the way. Cost if wrong: the term's definition says
"means of checking" while WAY-121 lists the place of the screenshots as one of its four matters; a
reader may find the family not wholly fitting (the same objection WAY-270 once made to a further
matter). The other option would have moved six uses.
Check: `git diff f218b55 -- foundations/glossary.md` is empty (0 lines); `python -B
elements/common/foundation_check.py` -> `0 errors`, exit 0.

### I-2 — fixed (removal, as the reviewer says)

Removed: sentence 2 of WAY-319, the matching *Verification* clauses (the step comparing two options;
the option compared with no word), the half of the rationale ("a way that fails it is seen as a lack
in the comparison"), the *Relations* item `derives from WAY-166` (it existed only for sentence 2),
and the sentence of `project-level/technology/research.md` that said an interface option which
cannot let two cycles check at once "stays with the lack". Whether the technology step tests the
condition, and with what force, is left for the human; nothing in the files now says it does.
Check: `grep -rn "cannot check at once\|WAY-319"` over the tracked `.md` files shows only the entry
itself and `task-cycle/change/ui_check.md:18`; foundation check exit 0.

### I-3 — fixed (option: a second invariant, `Method: review`)

Chosen: keep `record-copy-image-check` (the script, `Method: test`) and add `record-copy-image-files`
(`Method: review`, `Part: every`, derives from WAY-316): "Where {merge-onto} exists, no commit of a
change against {fork-point} adds a file below `docs/task-cycles/` whose name ends in an image
extension that `record-copy-image-check` names." The extension list stays in one place. WAY-316's
*Verification* names both invariants. Reason against widening WAY-316 alone: row 7 is an invariant,
and an invariant is what a reviewer reads by `Part`; the template keeps a check and the data it reads
as two entries. I agree with the reviewer that my two earlier reasons did not hold: the-way's own
cycles do commit record copies (and remove them next), and `review` is a method the template gives.
Check: foundation check exit 0. I also checked the new sentence against the history it speaks of:
`git log --diff-filter=A --name-only f218b55 -- docs/task-cycles` lists no file ending in any
extension of the list (no output), so the invariant holds on the base.

### Minor 1 — fixed

WAY-267 *violates* now reads "a run adds the logs, the interface, the development data or the place
of the screenshots to its list though the note does not touch them". A grep for the four-matter
enumeration (`logs, the interface`, `development data`) over tracked `.md` files shows no other list
of three left.

### Minor 2 — fixed

Rewrapped to 100 columns the paragraphs holding the seven long lines, and nothing else in them:
`foundations/decisions.md` (WAY-121 binding sentence and *complies*), `project-level/definition_template.md`,
`project-level/technology/start.md`, `project-level/technology/task_run.md`,
`task-cycle/skill/SKILL.md` (intro of "The record before it is committed"). Check: `git diff
-U0 d0d3ce6` shows no added line over 100 characters in these files (the few that `awk` counts over
100 are measured in bytes and hold the dash `—`, 3 bytes) except the invariant sentence, which the
invariants file writes unwrapped.

### Minor 3 — fixed

WAY-316 *Rejected* now says the release attachments and the external file store were rejected "as
the place the-way would name", keeping the source and removing the reading that a product may not
settle them.

### Minor 4 — fixed

`task-cycle/review/SKILL.md`, the bullet on a user interface, gained: a screenshot the reviewer takes
to show the human lies in the place the foundation settles for screenshots, outside the product's
repository, the report names its address, and where the foundation settles none, the reviewer keeps
none (WAY-316, WAY-317). It writes outside the reviewed worktree, so the skill's read-only rule on the
worktree, index and branch holds.

### Minor 5 — acknowledged, no code

The earlier report's sentence "no record copy is committed there" (the-way) was wrong; I do not rely
on it. See I-3.

## Checks (command and exit code)

- `python -B elements/common/foundation_check.py` -> `0 errors`, exit 0.
- `python -B gate/run_tests.py task-cycle` -> exit 0, 200 tests OK.
- `python -B gate/run_tests.py elements/common` -> exit 0, 109 tests OK.
- `python -B gate/run_tests.py agent-instructions` -> exit 0, 18 tests OK.
- `python -B gate/run_tests.py project-level` -> exit 0, 271 tests OK.
- `python -B agent-instructions/skill_entry_points.py` -> `entry points are current`, exit 0.
- Not run: the full gate (the orchestrator's). The invariant `record-copy-image-check` and its test
  are unchanged; its test ran in the `task-cycle` run above.

## Own-work check (WAY-164)

- Requirement most likely missed by this fix: that removing the widened glossary meaning and sentence
  2 of WAY-319 leaves no use or reference of either behind, and that the new invariant is true on the
  history it speaks of.
- Checks: `git diff f218b55 -- foundations/glossary.md | wc -l` -> 0; the grep for WAY-319 and the
  removed lack wording (above) leaves only the entry and `ui_check.md`; the history query for image
  files under `docs/task-cycles/` prints nothing; foundation check exit 0. All showed the fix holds.

## Reaches beyond the dispatch

- `elements/invariants/template.md` ("Method and test", sentence rules on `{fork-point}` and
  `{merge-onto}`) and the existing invariant `return-step-record`, to word the new sentence.
- `git log` over the base history for files added under `docs/task-cycles/`, to check the invariant.
- `task-cycle/change/fix.md`, as the dispatch names.

## Searches not found or unclear

- Whether `record-copy-image-files` should have `Part: every` or `task-cycle`: the files it speaks of
  stand under `docs/task-cycles/`, which the part map does not give to a part of the-way; I took
  `every`, as `return-step-record` does.

## Changes of earlier choices (for the request)

- The glossary entry is back to its base wording, so it is no longer a foundation entry of this
  change; the earlier report's mark for it is void.
- WAY-319 is now only row 6's own two requirements (no shared browser, close the browser); its
  `the cycle's` second sentence is gone.
- A new invariant, `record-copy-image-files` (`Method: review`), is added for row 7's property —
  marked `row 7`. EN: A commit of a change adds no file below `docs/task-cycles/` whose name ends in
  an image extension of the list. PL: Commit zmiany nie dodaje poniżej `docs/task-cycles/` pliku,
  którego nazwa kończy się rozszerzeniem obrazu z listy.
