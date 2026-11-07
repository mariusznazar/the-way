FAIL 02ca017cc5e7a6176f1f921f08d6eace43cd0ffd

# Review of the whole change — foundation-review-skill

Range `86cc21e876f27f5d7d3ffd811ba11b687ac04cc6..02ca017cc5e7a6176f1f921f08d6eace43cd0ffd`, five
commits, one author, no plan, no slices. `git rev-parse HEAD` printed
`02ca017cc5e7a6176f1f921f08d6eace43cd0ffd`, the head given. I read the diff, the frozen task whole, the
author's report, the skill and its four side files whole, the script and its tests, the decisions
changed or added, the part map entries, the request template and step 13 of the cycle skill. I
changed nothing in the worktree (`git status --short` printed nothing).

Counts: 1 blocking (Important), 7 Minor, 0 out-of-scope findings.

## Verdict in short

The change carries the task: the skill (`foundation-review/`), the count script with its test, the
reminder in step 13 and the request template, WAY-24 rewritten, WAY-300 to WAY-305 for the seven
settlement rows, the part and its installation. The sources are followed closely, and nothing private
is committed. One departure from a decision the change itself writes blocks it under WAY-263 (the tag
message). It is a one-word fix.

## Blocking findings

### Important 1 — the skill says the tag message counts "entries and remarks"; WAY-301 says "entries" (WAY-263)

- Place: `foundation-review/SKILL.md`, step 7, second bullet: "The message gives the number of
  entries and remarks checked, and no title of a task, of a note or of a person". Against
  `foundations/decisions.md`, WAY-301, binding sentence: "the tag's message gives the number of
  entries checked and no title of a task or of a private note"; and its *Verification* "violates" line
  "the message names the tasks the review made".
- What is wrong: the skill, a file of the change, restates an entry the change writes more broadly
  than the entry does: the entry names one count (entries); the skill names two (entries and
  remarks) and adds "of a person". The task's *Context* says "Opis tagu podaje tylko liczbę
  sprawdzonych pozycji", which fits either reading, so the source does not settle which of the two
  texts is right; they disagree with each other.
- Why it matters: WAY-263 grades a changed file that restates an entry differently, including more
  broadly, as Important. A later reviewer comparing a review's tag with WAY-301 and a review that
  follows the skill will find two rules for the same message. The consequence is small (a tag
  message), the fix is one word, but the grade is the rule's.
- Evidence: the two quoted passages above, read in the worktree at the head.
- Fix: make the decision and the skill say the same (either "entries and remarks" in WAY-301, which
  matches the task's "pozycji", or "entries" in the skill).
- Slice: none (no plan; one author).

## Minor findings

1. `foundation-review/SKILL.md` step 1, `git rev-list --merges --first-parent <tag>..<main branch>`
   and the no-tag form `... <main branch>`: the task's *Context* says that in the-way the main branch
   is spelled `foundations --` because a directory has the same name. The skill drops that. Evidence:
   in this worktree `git rev-list --merges --first-parent --count foundations` printed "ambiguous
   argument ... Use '--' to separate paths from revisions" (exit 128), while
   `... origin/foundations` printed 86 and `... foundation-review/2026-11-06..foundations` printed 1.
   Only a bare name with no range is ambiguous, so in the-way (which has a tag) it bites only a
   review with no tag, but the skill is the one place a future agent reads. Say `origin/<main
   branch>` or add `--`. (`task-cycle/review_reminder.py` is not affected: the cycle passes
   `origin/<target branch>`.)
2. `task-cycle/test_review_reminder.py`,
   `test_a_branch_name_that_looks_like_an_option_is_an_error` does not reach the guard it names. The
   argument `--output=x` is rejected by argparse ("the following arguments are required: BRANCH"),
   so the `branch.startswith("-")` guard in `review_reminder.count` is never executed by the test:
   deleting the guard would leave the test green. Evidence: `python -B task-cycle/review_reminder.py
   --output=x` printed `Error: the following arguments are required: BRANCH`, exit 2; with `-- -x`
   it printed `Error: '-x' is no branch name`, exit 2 (the guard). The script's behaviour is right;
   the protection is untested. A test that passes `main`-less `["--", "-x"]` would cover it.
3. `task-cycle/review_reminder.py`, `last_review_tag`: any non-zero exit of `git describe` is read as
   "no tag", not only "No names found". The count then runs from the start of history and can read
   `reminder: yes` falsely (for instance in a clone where tags are not fetched). `rev-parse` before it
   covers a bad branch, so the exposure is a repository whose tags are missing; the cycle step 13
   says "after a fetch" but not "with tags". Say so in step 13 or tell the two cases apart.
4. `foundations/decisions.md`, WAY-300 *Rejected*: "running into the daily scan" names a routine of
   the human that no foundation entry defines, in a file a public repository can hold. A reader of
   the decision cannot read it; the other outside reference in that sentence ("an outside harness")
   is anonymised. Say "the human's existing daily review" with a clause, or drop the phrase.
5. `foundations/decisions.md`, WAY-24 *Verification* "violates": "the review is set as a task of the
   product's backlog with a date" is narrower than the binding sentence ("no task of the product's
   backlog"), so a task with no date reads as complying. And WAY-302 *Verification* "complies" says
   "the remarks about one guide gather into one collective task", where no guide is defined. Both
   are wording of a test line for a reviewer; neither changes what the entry binds.
6. `foundation-review/remarks.md`, "Which remarks": "A remark about the process itself, taken from a
   cycle's record, is not read: another review collects those." The task excludes these remarks
   (question 11, category B) because the human's nightly review of the AI layer collects them. In a
   generic skill for any product the sentence asserts a collector that a product may not have, and
   nothing in the foundation names it. Say the kind is out of this review's reading and leave it
   there.
7. Reminder in the cycle's other request variants: `task-cycle/skill/request_template.md` says "Where
   the count of `SKILL.md` step 13 reads `reminder: yes`" and step 13 says the request "the cycle
   writes or rewrites gets it while the count stands", but `task-cycle/skill/correction.md` (the
   rewrite for the human's remarks) does not tell the orchestrator to count again, and the variants
   table of the template for a blocked or reserved request gives *How to merge* as "do not merge,
   close" without saying whether the reminder still ends it. `reserved_return.md` and
   `blocked_finding.md` send the writer through "step 13", which includes the count, so a diligent
   orchestrator gets there; the correction path and the blocked variants are left to inference.
   WAY-300 says "each request the cycle writes". I judged it Minor because step 13 is named from
   each path but the correction path does not recount.

## Task coverage

- To do 1 (the skill): met by `foundation-review/SKILL.md`, `weak_points.md` (whole foundation, no
  list of conditions, facts against their sources, weak points of rationales against today's state,
  the cheap read-only check, run), `remarks.md` (every unfixed remark of the repository's own merged
  requests since the last tag, the question put at the merge included, an answered one not raised
  again), `proposals.md` (proposals, groups in three kinds and "leave", one data file), `SKILL.md`
  step 5 (the whole set to `critique` before the human), `with_the_human.md` (one by one, groups as
  groups), tasks from decisions, step 7 (tag, no change to the foundation).
- To do 2 (the reminder): met by `task-cycle/review_reminder.py` (counts with `--first-parent`, tag
  from the main branch, 30 for every product, no tag counts from the start), step 13 and the template.
  In the-way itself the target is `foundations`; `origin/<target branch>` works (I ran it).
- To do 3 (WAY-24): met; WAY-82's rationale and the facts template sentence that restated it are
  corrected (the task's *Decisions in play* names that sentence).
- Questions to settle that the change carries: 2 (reminder, tag, 30, the control question), 6, 10,
  11, 12, 13, 14, 15 are in the skill and WAY-300 to WAY-305; 1, 3, 4, 5, 7, 8, 9 need no code.
- *Settlements to record*, rows 1 to 7: row 1 is WAY-24 itself (the author ties it to WAY-24 and
  writes no second entry; WAY-24's text says what row 1 says); rows 2 to 7 are WAY-300 to WAY-305,
  one each, and each takes its *Rejected* from the ways the row's source keeps. No decision text
  carries a settlement the task did not take.
- *Decisions in play*: WAY-24, WAY-82 and the facts template changed; WAY-37, WAY-11, WAY-14, WAY-120,
  WAY-161, WAY-289 are cited and kept; WAY-140 and WAY-215 need nothing.
- Source fidelity: the numbers (30, 6 to 26 and 4 to 21 merges a week, 1 to 4 and 1.5 to 7 weeks), the
  commands and the tag convention follow the task's text. Where the change goes beyond the task it
  says so in the author's report and I judged each as a reasonable fill of silence, not a taken
  decision: the data file's place and name, the form of a task made in a backlog, the push of the tag
  on its own yes, no tag for an unfinished review, the checked commit being the remote tip of step 1,
  and the first-review start generalised from a date (question 14, for one product) to "after the
  request the human names" (WAY-304). Only the last widens a stated rule; the reading is sound (a
  date in a skill would become history) and consistent between WAY-304 and `SKILL.md`.
- Human action 2 (the "nośnik" of row L7): the number is WAY-300; the move is the human's, at the
  merge. The author names both WAY-300 and WAY-301.
- Nothing private is committed: I searched the added lines for names, vault paths, titles and
  tool names (patterns: mariusz, brain, vault, `C:\`, uwagi_z, gospodarczyk, limen, loop2, overment,
  ai-review, obsidian, notion); the one author line is the git author. WAY-300's rejected options
  name Limen's harness only as "an outside harness".

## Against the foundation and the guidelines

- Foundation read by "Reading the foundation": the parts touched are `foundation-review` (new),
  `task-cycle`, `decisions`, `part-map`, `environment-facts`, `installation`, `agent-instructions`,
  `repository`. Read whole: WAY-09 (the change's diff), WAY-24, WAY-82, WAY-256, WAY-263, WAY-286,
  WAY-287, WAY-300 to WAY-305; invariants `skill-rule-source`, `script-language`, `script-imports`,
  `script-subprocesses`, `repository-file-location`, `element-directory-contents`; the glossary's
  headings (no term of the change needs an entry, and none is written; the added words "review",
  "tag", "reminder" carry their ordinary meaning).
- No invariant is written or changed; no invariant test is changed.
- The script holds `script-language`, `script-imports` (standard library only) and
  `script-subprocesses` (only git).
- The skill's layout follows WAY-256: each side file is named at the step that needs it
  (`weak_points.md` step 2, `remarks.md` step 3, `proposals.md` step 4, `with_the_human.md` step 6);
  the passage "Sharing the reading" serves steps 2 and 3 and stays in `SKILL.md`.
- The-way has no guidelines of its own.
- No reserved choice is taken: no language, framework, library, store, login or place to run is
  settled.
- Tests: `test_review_reminder.py` builds histories with `commit-tree` and asserts counts, tags and
  exit codes; I ran it. It fails on the broken behaviours the author mutated (no `--first-parent`;
  `>=` to `>`) by the author's report; I did not repeat the mutations. See Minor 2 for the one guard
  it does not reach. The three installation tests moved from 40 to 42 entry points because the
  product now gets 21 skills; the assertion is kept, only its expected value changed to the new
  fact.
- Trust boundary: the part map names none for `foundation-review`; `installation/install.py` (a
  boundary of the map) gains one line, a skill name and its path in `SKILLS`, which the entry-point
  test and the installation README follow. No hostile input is added.
- Operation that cannot be undone: the skill puts a tag and pushes it only on the human's yes after
  showing name, commit and message; the cycle puts none. Fits the orchestrator's answers.
- Own-work check of the author: its named requirement ("every place that restates WAY-24 says the
  review is the skill's run") fits where the change is weakest, and its search catches an unfixed
  place. I repeated the search: `grep -rn -i "periodic review\|task of the product's backlog\|review of
  the foundation"` over `*.md` and `*.py` outside `.runs`, `.claude`, `.agents` and `foundation-review/`
  leaves only WAY-37 *Rejected* ("fixes left to the periodic review (WAY-24)"), the historic message at
  `elements/common/migrate_foundation.py:436`, and the corrected places; both leftovers are true as
  they stand (a review is still periodic; the message belongs to the migration of the old form).

## Declined to judge

- The skill has never been run on a repository; whether a human following it gets what the text
  describes cannot be settled by reading. Outside the task's reach to settle before a first run.
- A product that squashes or rebases its merges reads 0 merges and gets no reminder (the author's
  report, "Searches"). The task's *Context* fixes the two git commands and the request template
  already names the limitation for the merge; the skill tells such a product to read the host's list
  for the review itself. Outside the task.
- A change to the-way made under `agent-instructions/README.md` with no cycle gets no reminder, since
  WAY-300 and the task bind "the end of every cycle". The README sends that writer to the template
  but not to the count. Outside the task; a decision for the human whether the README should say so.
- The wording of WAY-300's rationale on the review intervals (the numbers come from the task's question
  2 and I did not recompute them from the history of git).
- The 42 regenerated entry points under `.claude/skills/` and `.agents/skills/` (44 files):
  generated; I checked the generator's `--check` mode and the new entry point whole, and read one
  regenerated sibling's diff (one added name in its list).

## Checks I ran

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `02ca017cc5e7a6176f1f921f08d6eace43cd0ffd` |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B agent-instructions/skill_entry_points.py` | 0 | `entry points are current` |
| `python -B -m unittest discover -s task-cycle -p "test_review_reminder.py"` | 0 | 9 tests OK |
| `python -B gate/run_tests.py task-cycle` | 0 | 151 tests OK |
| `python -B task-cycle/review_reminder.py origin/foundations` | 0 | `tag: foundation-review/2026-11-06`, `merges: 1`, `threshold: 30`, `reminder: no`; by hand `git rev-list --merges --first-parent --count foundation-review/2026-11-06..foundations` printed 1 and, for all history, `origin/foundations` printed 86 |
| `python -B task-cycle/review_reminder.py --output=x` | 2 | `Error: the following arguments are required: BRANCH` (Minor 2) |
| `python -B task-cycle/review_reminder.py -- -x` | 2 | `Error: '-x' is no branch name` |
| `python -B task-cycle/review_reminder.py nonexist` | 2 | `Error: 'nonexist' names no commit in .` |
| `git rev-list --merges --first-parent --count foundations` | 128 | ambiguous argument (Minor 1) |

Not run: `python -B gate/run_tests.py installation` (about 5.5 minutes; the orchestrator runs the
whole gate), the whole gate, and `task-cycle/request_check.py` on a description with the reminder
(the author reports it; I did not rebuild a sample). Unverified by me: that last claim.

## Reaches beyond the dispatch (section 1)

- `foundations/decisions.md` WAY-256, WAY-263, WAY-286, WAY-287: the placement of a skill's files, the
  grade rule for a restated entry, and the form of a request's description, which the reminder joins.
- `instruction-files/kind_skill.md`: where a skill's fragment stands (WAY-256).
- `foundations/invariants.md` ranges of `skill-rule-source`, `script-language`, `script-imports`,
  `script-subprocesses`, `repository-file-location`, `element-directory-contents`: for the new files.
- `task-cycle/skill/correction.md`, `blocked_finding.md`, `reserved_return.md`: the other paths that
  write a request's description (Minor 7).
- `agent-instructions/README.md` from line 80 to its end: the route for a change to the-way that
  runs no cycle (Declined to judge).
- `.claude/skills/the-way-review-foundation/SKILL.md` and its `.agents` twin: the new entry point;
  `.claude/skills/the-way-critique/SKILL.md` diff as a sample of the regenerated ones.

## Searches not found or unclear

- Not found: a rule saying whether a tag message may count remarks, or only entries (Important 1):
  the task says "pozycji" and no decision settles it beyond WAY-301's own "entries".
- Not found: any text in the-way that defines "the daily scan" (Minor 4).
- Unclear: whether question 14's first-review rule (given for one product, by date) was meant to be
  general; the change generalises it as "after the request the human names" (WAY-304). I read it as
  sound but it is the one widening of a stated rule.
- Unclear: whether the task wanted the reminder in changes to the-way made without a cycle
  (Declined to judge).
- Not found: the author's sample description for `request_check.py`; I did not re-run that check.
