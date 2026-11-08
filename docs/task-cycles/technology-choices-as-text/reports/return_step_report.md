# Return step (step 11 of implement-task) — technology-choices-as-text

**Status:** done. **Commits:** none made by this step; the tree stays `f809953`. `git status --short` is empty.

Read whole: `task-cycle/skill/return_step.md`, `task-cycle/skill/foundation_step.md`, the *Return step* block of `task-cycle/record_template.md` (the labelled lines below follow it).

## The record lines

- **Foundation compared with code:** none of the entries compared needed a correction. Compared, each with the files of the repository as they stand at `f809953`:
  - *The entries the change writes or changes.* WAY-123 against `project-level/technology/settle.md` (item 5: one message, one choice after another, deciding options under their own names, one line for the others, the lines of options left out, recommendation and weak point; the critique agent receives the whole message and is asked for contradictions and for figures, features and unexplained words before "Then show") and against `project-level/definition_template.md` (the repetition of the sentence says "in one message, one choice after another and in plain text ... a fresh agent has checked that message"). WAY-165 against `task_run.md` (the list shown keeps the item `— held by` with one sentence on what the decision leaves unsaid) and `start.md` (the same sentence at a definition) and `list.md` (a silent decision stands `— open` at a definition). WAY-137, 138, 166, 267, 268: the changed word ("message") against `settle.md`, `task_run.md`, `orchestrated_mode.md`, `lead/skill/SKILL.md`.
  - *Those the task names.* WAY-113 (a decision question in plain conversation text, with ways, costs and a recommendation, a question against a choice taken as not offered) and WAY-120 (the critique of a set before presentation) against the same `settle.md` item 5 and item 6: no conflict; WAY-114, which WAY-123 prevails over, is unchanged and still says what WAY-123 narrows.
  - *Those the search found.* The decisions that cite WAY-123 for how a tool choice is shown (the ones the new-tools files of the coding, styleguide and testing guidelines carry) say "by their consequences, with a recommendation and the weak point of the option recommended" and name no table: compatible with the new WAY-123 and unchanged. Also WAY-121, WAY-122, WAY-270 and the invariant `project-technology-record` (about the readiness check of the Technology section): the change touches none of what they bind.
  - *The part map*, the entries `project-level` and `decisions` (responsibility, files, dependencies, trust boundary): the change adds, moves and removes no file, part or dependency, so the map still matches.
  - *The search for the old wording over the whole repository* (see Checks): the two hits left are the rejected way "the options in one table as before" in WAY-123's *Rejected* and the plan's "one table of tasks"; both are right.
- **Decisions written or changed:** WAY-123 and WAY-165 (rows 1, 2 and 3 of the foundation step, already in the commits `78c32c7` and `f809953`). Also changed by one word or one phrase, "table" to "message", with no change of meaning: WAY-137, WAY-138, WAY-166, WAY-267, WAY-268. This step changes none.
- **Invariants written or changed:** none. No rule of the task, a decision or the human asks for an invariant; the *Verification* of WAY-123 and WAY-165 keeps its pair of examples and names no invariant.
- **Environment facts:** none. The change rests on no source outside the product.
- **Glossary terms:** none. No word is used in a meaning for which WAY-95 gives it an entry; the glossary entry "reserved choice" (it cites WAY-268) is unaffected.
- **Part-map changes:** none.
- **Projected entries written whole or in part:** none. The task has no project definition (its *Project relation* is independent) and no projected entry.
- **Rows of *Settlements to record* written:** row 1 — WAY-123; row 2 — WAY-123; row 3 — WAY-165.

No entry is deferred, none proposed for later. The review's four Minor findings were fixed in `f809953` and are no foundation entries.

## Checks

| Check | Command | Exit |
|---|---|---|
| foundation form | `python -B elements/common/foundation_check.py` (worktree root, HEAD `f809953`) | 0 ("0 errors") |
| old wording over the repository | `git grep -n -E "one table\|separate tables\|table of choices\|table of consequences\|next table\|as the table gave\|the tables come\|in the table beside\|table for the human" -- .` | 0, with two hits, both right (WAY-123 *Rejected* "the options in one table as before"; the plan's "one row of one table of tasks") |
| worktree | `git status --short` | prints nothing |

No test was run: this step changed no file, and the gate passed on `f809953`.

## Own-work check (WAY-164)

- **The requirement most likely not met:** an entry or a file that still states the old rule (one table, `— held by` with no sentence at a task) and so no longer matches WAY-123 or WAY-165.
- **The check:** the `git grep` above over every tracked file, plus the reading of each decision that cites WAY-123 or WAY-165 (lines in `foundations/decisions.md` found by `grep -n -E "WAY-(123|165)"`), of the `project-level/technology/` files that apply them, and of the part-map entries of `project-level` and `decisions`.
- **What it showed:** the grep ran and found nothing stale. Seven decisions cite WAY-123 only to say that options are weighed by consequences and the simplest and cheapest is recommended; none states the form of the showing. One possible mismatch, in wording only: `definition_template.md` says "a fresh agent has checked that message" where WAY-123 says "in the first message, before it is shown"; "that message" is the one message of the same sentence, so the meaning is the same and I left it, which keeps the tree at `f809953` as asked.

## Reaches beyond the dispatch

`foundation-review/with_the_human.md:18` and `task-cycle/skill/reserved_return.md` were opened by the search for "table" beside "options" or "choice"; both speak of other tables (the group table of a foundation review, the cycle's questions table) and not of the technology step.

## Questions and concerns

None.

## Searches not found or unclear

none
