PASS faee0f877d899070ba090c4e4d546f6ab5af713c

# Review of the whole change, gap closed — range `fca8491`..`faee0f8`

`git rev-parse HEAD` in the worktree is `faee0f877d899070ba090c4e4d546f6ab5af713c`. The range holds the change (`2c27260`) and its fix of the three Minor findings (`faee0f8`); seven `elements/` files, no file of `foundations/`.

Result: no new blocking finding. Two new Minor findings, both outside the task (the task prescribes the text they concern). Nothing I read breaks, contradicts or leaves stale by the change.

## Counts of the reading (WAY-150)

- Decisions read whole: 80. 22 in the first review (WAY-02, 05, 17, 22, 28, 29, 40, 41, 44, 48, 61, 62, 64, 71, 72, 73, 76, 82, 90, 99, 113, 321) and 58 now (WAY-01, 04, 07, 08, 09, 10, 11, 12, 16, 18, 21, 24, 30, 33, 35, 36, 37, 42, 45, 49, 51, 54, 56, 58, 60, 63, 65, 68, 69, 77, 78, 80, 84, 85, 86, 89, 93, 94, 95, 96, 97, 104, 114, 117, 120, 126, 134, 150, 174, 225, 226, 263, 313, 314, 315, 344, 354, 364).
- Decisions read by title only: 242, of 323 in `foundations/decisions.md`. I ran through all 323 titles with their line numbers (`grep -n "^### WAY-"`) and opened every one whose title points to a bearing on the change: the named eight, the entries of the elements and their rules of form, the ones about asking, about `TODO`/`none`, about citations, about the glossary and about what a foundation describes. WAY-34 stands apart: I read its binding sentences and *Verification* in the first review, and its heading to *Origin* again now, not its *Rationale* or *Rejected*.
- Titles I judged to have no bearing and did not open (so by title only), the ones nearest to the change: WAY-03, WAY-25, WAY-26, WAY-27, WAY-32, WAY-38, WAY-53, WAY-55, WAY-161, WAY-162, WAY-164, WAY-297, WAY-300 to WAY-305, WAY-308, WAY-309, WAY-323 and WAY-324. For WAY-03 (invariant tests), WAY-27, WAY-308, WAY-309, WAY-323 and WAY-324 (links and private paths) and WAY-38 (scripts) I checked the diff instead: the change adds no test, no script, no link, no absolute path and no `@` (`git diff fca8491..faee0f8 | grep '^+'` for `http`, drive-letter paths, `[[`, `~/`, `@` gave no hit). WAY-161, 162, 164 and 297 are the rules by which I grade and by which the author checks; they do not reach the sentences changed.

## What I read besides decisions

- Invariants: `foundations/invariants.md` read whole this time, all 33 entries. The ones that reach the changed files are `foundation-file-kinds`, `repository-file-location`, `element-directory-contents`, `return-step-record`, `derived-file-content`, `ci-checking-commands`, `outbound-link-reach`, `tracked-file-private-paths`, `skill-rule-source`, `map-reference-target`, `test-method-citation`, `skill-entry-points` and `instruction-file-imports`; none of them is broken or made stale (checks: no SKILL.md and no test touched; no file outside `elements/`; every `Part`/`Derives from` identifier those templates name still exists).
- Part map: the entries `invariants` and `glossary` read whole now, with `decisions`, `part-map`, `environment-facts` and `elements-common` from the first review. The files the change touches all match a *Files* pattern of those parts, and `foundation_check.py` reports no unmatched file.
- Glossary: `foundations/glossary.md` read whole. The words the changed sentences use are `entry`, `foundation`, `environment fact`, `invariant`, `part map`, `part`, `binding part`, `read off`, `transitional state`; each is used in the meaning its entry gives. The removed Draft header describes a `transitional state` in the glossary's sense; WAY-36 and WAY-354 say a rule that ends with a piece of work stays out of the log and its files, which agrees with removing it.
- `elements/common/rules.md` read whole. Its rule on `none` and `TODO` (lines 17-23) is what item 5 and S12 rest on and says the same as the fixed sentence in `elements/environment-facts/template.md`.
- `elements/decisions/template.md`: the *Based on* rule (lines 44-58), the closing rule on `none` and `TODO` and "Fields and their readers" read; they use the same wording as the four templates that now end with `(WAY-05)`.
- Pointers to the changed text elsewhere: `git grep` for `How a skill asks`, `step 4.1`, `proposed answer`, `one round` over `elements`, `project-level`, `product-guidelines`, `foundation-review`, `task-cycle`, `agent-instructions`. The other mentions of "step 4.1" are the element skills' own steps and `project-level/technology/settle.md:77`, a step of that skill; the `elements/common/projected_mode.md` steps 4.2-4.4 stay as they were. No file still says that step 4.1 gives every question a proposed answer. `task-cycle/plan/SKILL.md:214` ("proposed answers and evidence") is a stage report, not step 4.1.

## Judgement against what I read

- WAY-01, 36, 09, 354 and the glossary: removing the Draft header and the `decision pending` lines leaves the templates describing the process as it is, as WAY-01 asks. WAY-09 requires an element to hold its template and rules when it reaches the main branch; the header said the template did not.
- WAY-113, 114, 30, 174, 313-315: the rewritten step 4.1 (ask in one round, a choice with its ways, costs and a recommendation, a question of assessment open) and the bullet in "How a skill asks" no longer contradict WAY-113 or WAY-114; "write it on your recommendation" in step 4.2 stays as WAY-30 and WAY-114 give it.
- WAY-71, 54, 80 and `rules.md`: S12, S13 and item 5 say what they say; the fixed item 5 gives the two forms of `TODO` that WAY-71 gives.
- WAY-64, 76, 77, 78, 80, 82, 84, 85, 89, 90: S2, S6, S7, S16-S19, items 4 and 6 are in line with them. WAY-85 gives a study's finding as a fact saying what it found, so dropping "in the present tense" (item 4) agrees with it, and WAY-82 is silent on a move to a newer release, so item 6 contradicts none. S7 is carried by WAY-90 alone (checked again against WAY-73, whose *Rests on* rule does not speak of outside partners).
- WAY-41, 44, 45, 48, 49, 62: S8, S9, S11, S24 and the surviving `Files: none` rule agree with them; WAY-44 says every tracked file has a part, which `Files: none` keeps.
- WAY-72, 93-99, 104, 226: item 9 (S27) agrees with them; WAY-104 says a product's interface and talk about the product keep the word of its domain, which fits "a word the product shows its users in another language stays in the product's files".
- WAY-22, 56, 58, 61, 62, 321: S3 now cites WAY-61 and WAY-321, S5 rests on WAY-22 and WAY-62; the sentences say what those decisions say.
- `foundation_check.py --skip-test-citations`: 0 errors on `faee0f8`, so no identifier, reference or part pattern the change touches is broken.

## Findings

No Critical or Important finding. Each of the three Minor findings of the first report stays fixed (see `fix-review-report.md`).

### Minor, outside the task (new)

1. `elements/invariants/template.md:165`, `elements/environment-facts/template.md:170`, `elements/glossary/template.md:102`, `elements/part-map/template.md:168` — S1. Each ends "A field stays in this template only while someone or something reads it (WAY-05)". WAY-05's *Scope* is `decisions`, and its sentence speaks of "the template" of a decision entry; WAY-71 *Rejected* names "a wider scope for WAY-05" as refused because WAY-05 "answers how a decision entry is written". The same sentence is already cited to WAY-05 for templates in general by WAY-54, WAY-18 and WAY-86 (*Rejected*), and the decisions template says it the same way, so a reader meets no contradiction; but no decision states the rule for the other four elements. The task prescribes WAY-05 here and forbids a change of the log, so I do not count it against the change; a fix would be a decision or a widened WAY-05, a separate task. Out of scope.
2. `elements/common/way_of_working.md:138-140` — item 2. Step 4.1 reads "as »How a skill asks« gives it (WAY-113): a value the source does not give, with where to look for it and never the value itself; a choice ...; a question of assessment, open". The section "How a skill asks" and WAY-113 give two kinds of question, a decision and an assessment; the kind "a value the source does not give" is in step 3 (line 127) and in WAY-54, not in what the sentence points to. The sentence is the task's own, word for word, so the change is faithful to it. Out of scope: reword or add the kind to "How a skill asks" in a later task.

## Declined to judge

The same as in `whole-review-report.md`, and nothing new. In particular the removal of the S5 ending, the task's own choice, stays set aside.

## Checks run

| Command (from the worktree root) | Exit |
|---|---|
| `git rev-parse HEAD` | 0, `faee0f877d89...` |
| `git diff --name-only fca8491..faee0f8` | 0, seven `elements/` files |
| `python -B elements/common/foundation_check.py --skip-test-citations` | 0, "0 errors" |
| `git grep -c "^### WAY-" faee0f8 -- foundations/decisions.md` | 0, 323 |
| `git grep -n -i "proposed answer\|proposes where to look\|reason for it\|4\.1" faee0f8 -- elements project-level product-guidelines foundation-review task-cycle agent-instructions` | 0, five hits, none stale |
| `git diff fca8491..faee0f8 \| grep '^+'` for links, paths and `@` | no hit |
| a script of my own printing whole decision entries by number from `foundations/decisions.md` | 0, run in the first review and again now |

Not run: `gate/run_tests.py` whole (the orchestrator's); the earlier runs of `elements/common` (144 OK) and `elements/part-map` (39 OK) stand, since no file of those parts' code or tests changed after them.

## Unread material

- Of the 323 decisions, 80 read whole and WAY-34 in part (above); 242 by title only, of which none points to a bearing on the change except those listed above as judged without bearing, each checked against the diff where it could matter.
- Invariants: all 33 read whole; the long sentences of the `project-*` and `installation-claude-guidance` entries were cut at about 260 characters in my printout, so I read those few lines in part. None of them concerns the changed files.
- Part map: the entries of the parts the change touches read whole; the entries of the other parts and the three command entries were not read.
- Glossary: read whole.
- Guidelines: the-way has none for these files; `product-guidelines/*` not read.
- `elements/decisions/template.md` read in the parts that bear on `TODO`, `none` and the fields; not whole. `elements/common/projected_mode.md` read to its step 4.4; the `examples.md` files of the elements not read, since the change touches no example.

## Searches not found or unclear

- A decision or invariant that states "a field stays in a template only while read" for the elements other than decisions: not found (see Minor 1).
- A place that gives "a value the source does not give" as a kind of question besides step 3 and WAY-54: not found (see Minor 2).
- A guideline of the-way's own files setting a rule of size: not found; no structure test applies to Markdown.
