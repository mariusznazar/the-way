# Fix report: task `resolve-gaps-two-meanings`

**Status:** done

## Commits

- `187bbde` Bring WAY-374 and the check of the skill to one wording and re-wrap them (on `9c66ee1`)

Files: `foundations/decisions.md`, `project-level/task/skill/resolve_gaps.md`, `project-level/task/skill/SKILL.md`.

## Findings

- **I-1 fixed.** WAY-374's second paragraph now reads "an ambiguity in the approved project definition whose resolution changes the definition goes back to the definition and its readiness gate (WAY-118)". The skill (`resolve_gaps.md`, third paragraph of the check) reads "An ambiguity in the approved project definition whose resolution changes the definition goes the way the paragraph below on that definition gives (WAY-118)". Same condition in both, and it matches the paragraph "If the answer changes the approved project definition ..." it points to. Check: reading the two passages side by side; `foundation_check.py` exit 0.
- **M-1 fixed.** The paragraph of section 3 in `SKILL.md` is re-wrapped; no line of it is over 100 characters (line 3 is the frontmatter `description`, unchanged).
- **M-2 fixed.** The entry's paragraphs, *Rationale* and *Rejected* are re-wrapped at 100 characters; a count of characters of every line of the entry shows none over 100 (the heading included). The check was a script count over `foundations/decisions.md` lines 12879-12944, no output.
- **M-3 fixed.** *Rationale* now says "after the model of WAY-99 for a word of the foundation".
- **M-4 fixed.** The entry says the candidate glossary term is one "which WAY-95 judges there"; the skill says "which step 5 finds and WAY-95 judges there". The reader-of-the-field wording stays as the task's Q4 gives it.
- **M-5 fixed.** The check's paragraph is split into three (what to search and what settles it; what counts and what to show and ask; the glossary candidate, the definition, the no-duty rule), and the question is named "as a question of decision according to "How a skill asks" (WAY-113)".

No finding is contested.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- `python -B gate/run_tests.py project-level` — exit 0 (OK).
- `python -B gate/run_tests.py instruction-files` — exit 0 (OK, 5 skipped).
- Not run: other test directories (no file of theirs touched), the whole gate (the cycle's).

## Own-work check

- Requirement most likely not met after a fix of Minor findings: a fix that grows beyond its findings, or that changes the meaning of WAY-95, WAY-99, WAY-113 or WAY-118.
- Check: `git diff 9c66ee1 HEAD` read: the edits are the condition in I-1, the clause on WAY-95, "after the model of", the naming of "How a skill asks", the split of one paragraph and re-wrapping; no sentence added to the meaning of a decision other than WAY-374.
- Result: within the findings.

## Reaches beyond the handoff

None. I did not re-read the decisions already read in the author's report.

## Working copies

None made. A temporary test-output file under `.runs/` was removed.

## Unread material

`task-cycle/change/fix.md` read whole; the handoff and the findings file read whole. `whole-change-review-report.md` (the full review) not read: the findings file holds the reviewer's words for each finding.

## Searches not found or unclear

None.
