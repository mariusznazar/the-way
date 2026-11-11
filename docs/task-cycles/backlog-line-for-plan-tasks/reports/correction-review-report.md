FAIL 047a9e7606e90dc164762bebb0c6bc48dcd46eeb

# Review of the correction for the human's remarks (range 7ca8642..047a9e7)

Range `7ca864236afac802d03ebb74d3fbe66bee1b755d..047a9e7606e90dc164762bebb0c6bc48dcd46eeb`, one commit,
confirmed by `git rev-parse HEAD`. Reviewed as a fix, the remarks standing in place of a findings file
(`correction-findings.md`, with the direction of `correction-handoff-2.md`). Paths are relative to
`the task's worktree root`.

Counts: 1 blocking, 3 Minor (within the task), 0 out of scope.

## The six remarks, each as made or remains

1. **Item 1, the rule of agreement of the lines at both ends of a dependency — made as the second
   direction gives, with one defect (B1 below).** The rule is in no skill and no decision: grep of the
   changed files and of `foundations/` finds no sentence about reading a line before a write, adding
   only a missing field, keeping one line to a task, or a clash of identifiers. `project-level/task_line.md:42-47`
   carries the one sentence (the refiner keeps its task's line and the lines of the tasks it waits on and
   that wait on it in agreement with the plan's dependencies as the rules of the task place give; where
   they do not say how, it asks the human once). The search bullet, the clash bullet and sentence, and
   "touches nothing else of the line" are removed from `task_line.md`; WAY-329 lost its clash clause and
   its *Violates* item; WAY-107 gained the third binding sentence. The defect is that four skill files
   now give refiners a write the entry does not.
2. **Item 3, finding 1 ("another line" without "of another task") — made, by removal.** WAY-329's clause is
   gone (word diff below), so no wording is left to correct.
3. **Item 3, finding 2 (the citation) — made.** `task_line.md:35-36`: `(WAY-329)` follows the derivation
   sentence; the sentence on a task of no plan (`:36-38`) carries none.
4. **Item 3, finding 3 (the long lines of the rewrap) — made for `foundations/decisions.md`.** I scanned
   every added line of `git diff 52f8164 047a9e7` for more than 100 characters (`python -I`, exit 0):
   none in `foundations/decisions.md`. Four other changed files have such lines (Minor 2), which the
   remark did not name.
5. **Item 3, finding 4 (binding sentences) — made.** WAY-154's first paragraph is three sentences
   (`foundations/decisions.md`, from "Project refinement resumes" to "its task is proposed again when the
   named prerequisite is done."); WAY-107's is three ("A product names ...", "A project definition stands
   ...", "How a task's line is handled ..."). Each is long and joined by semicolons, but within the form
   (`elements/decisions/template.md`, WAY-05).
6. **Item 3, finding 5 (vocabulary in `read_sources.md`) — made.** `project-level/task/skill/read_sources.md:17-19`:
   "short task lines only ... from that line". The wrapped line of WAY-107 is rewrapped.

## The rewrap, word by word

Method: for each entry whose text differs between `7ca8642` and `047a9e7`, I split both versions into words
(whitespace ignored) and compared them with `difflib` (`python -I`, exit 0). Entries that differ:
WAY-27, WAY-107, WAY-154, WAY-320, WAY-329 (and no other).

- **WAY-27 and WAY-320: no word differs.** Only line breaks moved. Nothing hides in them.
- **WAY-154: three changes, all joins of sentences.** "task's line" became "line of its task"; two full
  stops became semicolons, to hold three sentences. No qualification lost; the meaning is that of
  `7ca8642`. (The meaning of `7ca8642` itself is judged in B1.)
- **WAY-107:** the join of the two first sentences ("owns, a place ... standing there ..., and a directory
  of the repository or the address of a public tracker as it is": the old "stands there as it is" is
  kept in meaning); the added third sentence and its list (the human's remark, below); "the second line of
  *Verification*" gaining "how a line already there is handled"; *Violates* gaining "or a rule of how a
  line is found or changed"; *Rationale* "written" to "handled" and "the place can change them without a
  change of the-way". Each is the rule of the correction; no word of an old qualification is dropped.
- **WAY-329:** exactly the clash clause (binding sentence), the "a refiner that finds the first line
  already carrying it asks the human" part of the *Complies* example, the *Violates* item "a refiner that
  writes an identifier another line already carries", and the rationale's "the agent that meets a clash
  asks the human, and an identifier that is wrong is mended by editing the lines", replaced by "what is
  done with a clash is for the rules of the task place (WAY-107)". The derivation and its two conditions
  are intact.

## WAY-107's third binding sentence and the mark `the cycle's`

Judged against WAY-114 and WAY-263. The sentence says that how a task's line is handled (status, move to
ready, forms, how a line is found and kept one to a task, which fields may change, the agreement of the
lines at both ends of a dependency, a clash of identifiers) comes from the rules of the task place, never
from text at the product or in the-way's skills. No skill file of the-way holds such a rule now (grep
below), so the files do not do what the entry forbids or restate it differently. The mark is right: the
rule comes from the human's remark at the request, not from a row of the task, and by WAY-114 an entry no
row carries is accepted at the merge, where the request's section for the human's decisions must carry
it; the author gives the English and Polish meaning sentences and names the request as the place. No way
not chosen is added to *Rejected*, which is right (the remark keeps none, WAY-134). Not a finding. One
tension is noted in Minor 3.

## New defect in the correction

### B1 (Important, within the task). Four skill files give a refiner a write that WAY-154 does not give it

- Place: `project-level/task/skill/orchestrated_mode.md:41-43` ("bring it and the lines of the tasks tied
  to it into agreement"), `project-level/lead/conversation_template.md:22-24`, `project-level/lead/skill/SKILL.md:105-106`
  ("each makes its task's line and brings the lines of the tasks tied to it into agreement"),
  `project-level/plan/skill/delegated_mode.md:9-10` ("refiners write only separate task documents/conversations
  and the backlog lines of their tasks and of the tasks tied to them (WAY-154)"), and
  `project-level/task_line.md:42-47`; against WAY-154's binding sentence in `foundations/decisions.md`
  ("...the line of its task in the backlog the product names (WAY-107), where none stands, with the
  dependencies the plan gives the task ...").
- What is wrong: WAY-154 lists what a refiner may write besides what the order asks, and the list holds
  the refiner's own line, made in its first turn or the first later one, where none stands. The skills now
  have the refiner also write the lines of the tasks it waits on and that wait on it (a different task's
  line, one that already exists). That is a broader write than the entry gives, in the files and in
  `delegated_mode.md`, which cites WAY-154 for it (WAY-263: files that restate an entry more broadly than
  it says are an Important departure). WAY-107's new sentence names "the agreement of the lines at both
  ends of a dependency" only as a matter of the place's rules; it says nothing of who writes. `grep -rn
  "tied to" foundations project-level product-guidelines` finds the phrase in the four skill files and in
  no entry. WAY-154's *Verification* (complies and violates), its *Rationale* (the accepted cost covers
  "two writes to the one backlog file in the same instant can lose a line", of lines being made, not of
  several refiners editing one task's existing line) and WAY-329's relation to it are likewise silent.
  The second direction says the-way keeps what only it knows, and who writes what is the-way's own: the
  same direction keeps "a refiner never moves a line to ready" in WAY-154.
- Why it matters: a later agent reads WAY-154 as the authority for what a refiner may write and the
  four skill files as what to do; one of them tells refiners to edit other tasks' lines, the other does
  not allow it. A reviewer or a refiner that follows the entry will not touch a tied task's line, and
  the human's rule of item 1 is then not carried out, or is carried out against the entry.
- Fix (either is enough, the first is the smaller): add to WAY-154's second binding sentence that the
  refiner also brings the lines of the tasks tied to it into agreement with the plan's dependencies as
  the rules of the task place give, mark it as the human's remark at the request, and add the same to the
  *Verification* examples and to the *Rationale*'s accepted risk; or take "and of the tasks tied to
  them" out of the four skill files and leave the write only in the one sentence of `task_line.md`,
  which would still need the entry to say it. I recommend the first.
- Evidence: the texts side by side; the word diff above shows WAY-154's text in `047a9e7` differs from
  `7ca8642` only in the three joins, so the entry was not given the tied-line write.

## Minor findings (within the task, not blocking)

1. **The report's claim about line length is not accurate.** `project-level/lead/skill/SKILL.md:105-106`
   (the last line of the item is 158 characters, new in this commit), `project-level/lead/conversation_template.md:23`
   (102), `project-level/task_line.md:56` (101), and `product-guidelines/coding/orchestrated_mode.md:9` (111,
   from the earlier fix), against the correction report's "No line of the diff against `52f8164` is now
   longer than 100 characters". The remark named the entries of `decisions.md`, which are clean; the
   skills' lines are cosmetic.
2. **The part map says the part answers for "how the line of a task ... is made".**
   `foundations/part_map.md` (the `project-level` entry, from the return step, not in this range) and
   `project-level/backlog_place.md:15-20` ("`project-level/task_line.md` says how a line is written by
   them") now read broader than the-way's side after the correction, which moved how a line is
   handled to the rules of the task place. What the part answers for is when and by whom a line is made,
   the derivation of its identifier, where its dependencies come from, who moves it to ready. Still true
   enough to read, and the author compared it; reword "how ... is made" to "when and by whom ..." at
   the next touch. The unchanged-here entries WAY-144, WAY-147, WAY-328, WAY-329's links and the
   invariants stand as I left them.
3. **Two small leftovers of the removal.** `project-level/task_line.md:10` still says "where the rules
   give none of the three forms", after the opening list grew to six matters (`:3-9`), so "three" has no
   referent; and `task_line.md:22-23` ("A new line links the task's document") and `:55-56` say what a
   line carries, which WAY-107's new sentence leaves to the place's rules only for "how a line is found
   and which fields may change", so no breach, but the boundary is not drawn in the file. Reword "the
   three forms" to "the forms".

## Declined to judge

- The Ready line a task returned to refinement keeps: it stands on the request's list (handoff).
- The rules of the task place: private notes outside the repository, not reviewed, nothing quoted.
- Whether the Tasks plugin treats a `⛔` naming an absent identifier as no dependency (the earlier
  finding's recollection): not checked, outside the correction.

## Checks run

All read-only, from the reviewed worktree, `python -B`; `git status --short` empty.

| Check | Command | Exit |
|---|---|---|
| Foundation identifiers and references | `python -B elements/common/foundation_check.py` | 0 ("0 errors") |
| Instruction files | `python -B instruction-files/check_instructions.py .` | 0 ("0 error, 0 warn, 3 info") |
| Private paths and note links | `python -B task-cycle/test_tracked_files_private_paths.py` | 0 (OK) |
| Word-by-word comparison of rewrapped entries, `7ca8642` against `047a9e7` | one-off `python -I` with `difflib` over the five changed entries | 0 (result above) |
| Lines over 100 characters added since `52f8164` | one-off `python -I` over `git diff 52f8164 047a9e7 -U0` | 0; hits listed in Minor 1 (none in `decisions.md`) |
| The refiner's write of tied lines in entries and skills | `grep -rn "tied to" project-level foundations product-guidelines --include=*.md` | 0; four skill hits, no entry (B1) |
| The remaining "three forms" | `grep -rn "three forms" project-level` | 0; `task_line.md:10` |
| Diff, log, head | `git diff --stat 7ca8642..047a9e7`, `git log 7ca8642..HEAD`, `git rev-parse HEAD` | 0; seven files, one commit, head confirmed; `docs/task-cycles/` untouched |

Not run: the `project-level` directory and the full suite (the orchestrator's).

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-329 and WAY-154 read whole on the new head, WAY-107 whole; the entries'
  old text from `7ca8642` through `git show`, for the word comparison.
- `foundations/part_map.md`, the `project-level` entry, and `project-level/backlog_place.md`, `AGENTS.md`
  (read in the `52f8164..047a9e7` diff), to judge whether they stay true.
- `project-level/task_line.md` whole; the earlier reports of mine as background, not re-graded.

## Unread material

Decisions: WAY-107, WAY-154 and WAY-329 read whole on the new head; WAY-27 and WAY-320 compared by words
with `7ca8642` (no word differs) and not re-read whole. The earlier selection (28 whole, 114 by title) is
unchanged and not re-read. WAY-114 and WAY-263 I used as read in the first review and as quoted in the
method. The correction report and handoffs read whole; `correction-handoff.md` (the first direction,
replaced) read only through the second and the findings file.

## Searches not found or unclear

- A sentence in WAY-107, WAY-154 or WAY-329 that says the refiner writes the lines of tied tasks: looked
  for by `grep "tied to"` and by reading the three entries; not found (B1).
- Whether the second direction meant WAY-154 to stay silent on the tied-line write: unclear. It says "a
  skill and a decision only point to those rules"; but it also keeps who writes what in the-way, and the
  skill pointers it asks to keep "pointing" were reworded to carry the write. If the orchestrator wants
  the entry silent, the four skill files and `task_line.md:42-47` must not give the write to the refiner
  either, and that is the second fix above.
