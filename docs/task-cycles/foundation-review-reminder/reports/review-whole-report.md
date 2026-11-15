PASS b7ec371207ad67d6378f323433f643e1703335e5

# Review of the whole change — foundation-review-reminder

Range `ff88ca3bc6beae07dbe1ee5adb1792773d28bcac..b7ec371` (`git rev-parse HEAD` = `b7ec371207ad67d6378f323433f643e1703335e5`, the head given). Commits: `f96ddd2`, `c0ba78b`, `b7ec371`. Route: one author, no plan, no spec, so this review is the only one the change gets. No commit made by me. Blocking findings: 0. Minor findings: 5 (4 within the task, 0 outside it as findings; the author's two additions are under *Declined to judge*). Out-of-scope findings: 0.

## Changed files (added / removed lines, `git diff --numstat`)

| File | + | - |
|---|---|---|
| `README.md` | 2 | 1 |
| `foundation-review/SKILL.md` | 15 | 7 |
| `foundation-review/proposals.md` | 18 | 0 |
| `foundation-review/weak_points.md` | 29 | 1 |
| `foundation-review/with_the_human.md` | 11 | 2 |
| `foundations/decisions.md` | 68 | 29 |
| `task-cycle/review_reminder.py` | 31 | 12 |
| `task-cycle/skill/SKILL.md` | 14 | 5 |
| `task-cycle/skill/request_template.md` | 17 | 7 |
| `task-cycle/test_review_reminder.py` | 47 | 9 |

Total 252 / 73, which agrees with the author's report. No changed invariant test: no file of `foundations/invariants.md` and no test that cites an invariant is touched. No screenshot among the commits.

## Findings

### Critical

none

### Important

none

### Minor

1. **`foundation-review/weak_points.md`, new section "Entries of the log that are no decisions", the sentence "A rule that ends with its own piece of work fails the plan test and belongs to the list of transitional states above, not to this one."** (within the task: point 2). The section "Decisions that describe a transitional state" of the same file, a few lines above and unchanged, says the opposite for what reads as the same class: "A rule that ends with its own change is no entry of the log (WAY-36) and gives none." The two sentences differ by "piece of work" against "change", and one sends the entry to the transitional list while the other gives it no line on that list. An agent that runs the review reads both and cannot tell where an entry that fails the plan test goes; the result is a human asked "is there a task that ends this state?" about an entry that has no state, or an entry that is dropped. Grade Minor: the review's output still goes to the human item by item, and the new section as a whole follows the task. Evidence: `git show c0ba78b:foundation-review/weak_points.md` lines about "gives none" and the added sentence. Not asked by the task: the task names only the questions of "Where it goes", and the plan test comes before them; the added sentence is the author's. Cheapest repair: delete the sentence, or state the boundary (the rule ends with a later piece of work: the transitional list; the rule that ended with its own change: none).

2. **`foundations/decisions.md`, WAY-24 *Rejected* and WAY-300 *Rejected*** (within the task: *Decisions in play* for WAY-24 and settlement row 2). Two readings that fall short of the entry's own rule (WAY-07 and the template's "Changing a decision": *Rationale* and *Rejected* describe the decision as it stands, never the change):
   - both entries reject "only the setup of one user, with the wording of this decision as it was" — "as it was" points at an earlier wording that the entry no longer holds, so a reader of the entry as it stands cannot tell what is rejected; the way rejected is "a sentence that asks for no line and says nothing of the backlog, with the human's own setup adding the line", which can be written without the history;
   - WAY-24 *Rejected* keeps "the review set as a task of the backlog, run by a cycle that ends in a request of corrections" and "a ready task of the review copied into the backlog — three steps where one command does", while the binding sentence now says a task of the backlog "may stand for that run, and a human adds it". The task's *Decisions in play* says of this very rejection that it "przestaje opisywać produkt". The first kept way is saved by "run by a cycle"; the second, read by itself, rejects what the reminder now asks the human to do (add a task of the review to the backlog). The author's choice 8 keeps both and names the cost. Grade Minor: WAY-364 — the content agrees with the code and no sentence of the files reads wrongly for it; I cite the second bullet as the one a reader could read wrongly, and it is still a *Rejected* line, which binds nothing. Evidence: the entries at `b7ec371`.

3. **`task-cycle/skill/SKILL.md` step 13 against WAY-300 and the task's point 1: the source of "the name of the repository"** (within the task). The task and WAY-300 say "the name of the repository". Step 13 says "the name of the repository, as the `## Backlog` section of the root `AGENTS.md` names the product" (the author's question to the orchestrator, kept by record row Q4). For the-way the section names it (`the-way`, the key of the locations-file entry), so the wording works here. For a product whose `## Backlog` section names a directory of the repository or a public tracker, the section gives no name, and step 13 then holds no rule for it; `request_template.md` and WAY-300 repeat "the name of the repository" with no pointer to that source. The check is self-consistent, because the orchestrator writes the name it later looks for, so the harm is a different name for the same product in two cycles, which makes a reminder ask again for a line that stands. Judged against point 1 and question 3: the author's qualifier is narrower than what the task says and is unneeded for the examples of question 3 ("Przegląd fundamentu loop2 (`review-foundation`)"). Minor.

4. **`task-cycle/skill/SKILL.md` step 13, the clause "where the script ends with exit code 2, record its message under *Verification* and write no reminder, since the count is unknown"** (author's choice 6; the task makes git errors exit 2 and is silent on what the cycle does). The behaviour is reasonable and I do not ask for its removal. Minor: a count that fails is a check that did not run, and WAY-287 puts the steps skipped and the checks not run in the section of the request for the human's decisions; step 13 sends the failure to *Verification* only, so the human who merges sees no reminder and no sign in the part they read, in the one case where the task's purpose is that the reminder cannot be missed. Where the cycle treats it as WAY-287 gives, the repair is one clause in step 13. Within the task (point 4 reaches what the cycle does with the new exit code).

5. **Two lines over the width the files keep**: `foundation-review/proposals.md` ("that the run found, and its count stands beside its place. The human decides on whole groups, never on part of one: the groups chosen", 137 columns) and `foundation-review/weak_points.md` line 4 ("transitional states and the entries that are no decisions. An entry that holds takes no line beyond the number of items", 120 columns); the other lines of those files wrap at 100. No check reads this. Polish, within the task.

## Declined to judge

- Author's addition 6 (exit 2 of the script in step 13): judged only as Minor 4 above; that the cycle should react to the error at all lies outside the task's text.
- Author's addition 7 (`foundation-review/SKILL.md` step 7, "Where an open line of this review stands in the backlog, tell the human to mark it done …"): beyond the task. I checked it does no harm: it writes nothing to the backlog, it takes the meaning of "done" from the task place's rules (WAY-107), it does not touch what the task puts out of scope (the daily advisor's reaction), and it closes a real gap — a line left open silences the next reminder for good. The cycle may keep it or cut it.
- The upper pace of 26 merges a week in the `THRESHOLD` comment: the task's own *Context* says week 46 (36 merges) lies above the range; the comment keeps the range the task prescribes. Not a finding (see the judgment below).
- Whether the new text for the human's session with the review (`with_the_human.md`) should ask for a task of the log's tidying as a form of its own: the task leaves the form open.

## Judgments the orchestrator asked for

- **The rhythm in the `THRESHOLD` comment, "every 2 to 10 weeks in the-way".** 60 / 26 = 2.3 and 60 / 6 = 10 weeks; "2,5" in the task's *Context* is a rounding that the arithmetic does not give, and "2 to 10" holds for both ends; the product's "3 to 15" is 60 / 21 = 2.9 to 60 / 4 = 15; "about every 10 days" is 60 / (49 / 8 days) = 9.8 days; "at 30 about once a week" is 30 / (49 / 8) = 4.9 days. The author's reckoning is right; no finding. The task's point 3 asks for "the rhythm computed for 60 from the pace in *Context*", which the comment gives, with the price taken, beside the value.
- **The name the line must hold**: Minor 3 above.
- **The four entries the author read in part**: opened whole by me were WAY-161, WAY-107 (both bear on the change and were read to the end), WAY-150 (opened whole, as it names the reviewer's duties), and WAY-344 (opened whole; it does not bear: `review_reminder.py` reads the output of git, no file an agent or a human writes, and no other script is added or reworked).

## Coverage of the task

### To do

1. Met. Step 13 (`task-cycle/skill/SKILL.md`) has the orchestrator, from the threshold, read the backlog as `project-level/backlog_place.md` gives and look for an open line whose name holds `review-foundation` and the repository's name, with "open" taken from the task place's rules (WAY-107); `request_template.md` gives the two forms (asks, with what the name holds, the number of merges, the tag, the skill; or points to the line and does not urge) and the unreadable backlog as the form for a missing line that also says it could not be read; the cycle adds and changes no line (WAY-140). WAY-300 carries the same. See Minor 3 for the name.
2. Met. `weak_points.md` (new section, applying the five questions of "Where it goes" with WAY-293's reading for the-way's log), `proposals.md` (groups by place with a count, whole groups, no batch chosen by the review, the data-file section), `with_the_human.md` (the groups as step 3, one at a time, the human decides which whole groups go into the task this time, the rest wait; renumbering of the later steps; no other file of the repository refers to those step numbers), `SKILL.md` steps 2, 4, 6, 7. See Minor 1 for one sentence.
3. Met. `THRESHOLD = 60` in `task-cycle/review_reminder.py` with a comment holding the rhythm and the price; `test_the_reminder_starts_at_sixty_merges_and_not_at_fifty_nine` holds 59 and 60 and the printed `threshold: 60`; WAY-300 says "from the threshold of the reminder script on" and keeps "one number for every product, which no product sets for itself"; its *Verification* lost "31 merges", its *Rationale* the rhythm for 30, its *Rejected* the "50 merges" way; `foundation-review/SKILL.md` and `README.md` no longer give 30 (`grep` of the tree for "30 merges", "after 30", "from 30", "thirty", "50 merges" finds nothing left, apart from an unrelated example in the log).
4. Met. `last_review_tag` lists the tags first (`git tag --list --merged BRANCH 'foundation-review/*'`): non-zero is exit 2 with `Error:`, empty with 0 is no tag, a failed `git describe` where the list names a tag is exit 2. I ran the script on the real history (exit 0, `tag: foundation-review/2026-11-15`, `merges: 1`, `threshold: 60`, `reminder: no`) and on the tests. The two error tests replace one git command by a stub answering in Polish, so no English wording can pass them; the no-tag case still runs on real git. Step 13 says "after a fetch that brings the tags".
5. Met. WAY-300's *Verification* says the reminder ends *How to merge*; its *Rationale* has no "the history of the first product is not open to a reader of this repository"; step 13 says that below the threshold the description says nothing about a review of the foundation; `request_template.md` says the same ("nothing is written about a review of the foundation").

### Settlements to record

| Row | Where it goes | Met by |
|---|---|---|
| 1 | sentence of WAY-300 | WAY-300 second paragraph, in the code of the cycle step 13 and the template; checked against the row's three conditions (no line, line stands, backlog unreadable). Met. |
| 2 | sentence of WAY-24 | WAY-24 binding sentences 2–3 ("A task of the product's backlog may stand for that run, and a human adds it, never a cycle."); "and no task of the product's backlog" is gone; the review stays a run of the skill in a session with a human. Met. See Minor 2 for *Rejected*. |
| 3 | skill files of `foundation-review/` | `weak_points.md`, `proposals.md`, `with_the_human.md`, `SKILL.md`. Met. |
| 4 | `task-cycle/review_reminder.py` | `THRESHOLD = 60`, the test, the comment with the reason. Met. |
| 5 | sentence of WAY-300 | "from the threshold of the reminder script on", with the rule of one number for every product kept. Met. |

*Projected entries*: none carried. *Out of scope* respected: no change to loop2's pin, none to the daily advisor.

## Against the foundation the change writes

- WAY-24 and WAY-300 (written by the change). Binding sentences: WAY-05 allows one to three sentences per paragraph; WAY-24 has 3, WAY-300 has 2 and 3. WAY-12: each is held by its pair of examples, and `python -B elements/common/foundation_check.py` reports `0 errors` (run by me). WAY-22: the number stands in the script with its test and a comment at the value, as WAY-22 and the task's question 6 give; WAY-300 no longer states a number. WAY-107/WAY-140/WAY-161: the cycle only reads the backlog and writes no line; the entries and the skill say so; consistent. The *Relations* added to WAY-300 (`derives from WAY-107 · derives from WAY-140`) match what the entry now rests on. WAY-263: the files do what the entries require; no departure that changes what is done. The wording points are Minor 2 and 3.
- The entry the change should write for the review's groups of entries is not a decision (row 3 goes to skill files), correctly so: it is an instruction for how an agent works, WAY-293's second paragraph (a rule of a skill stands in one skill with its reason) — the new section of `weak_points.md` gives the reasons for its own rule in one place and `proposals.md` / `with_the_human.md` do not repeat them.
- Invariants of the touched parts read (`.runs` selection of all with *Part* `every`, `decisions`, `task-cycle`, `foundation-review`): `script-subprocesses` (the script starts only git), `script-imports` (standard library only: `unittest.mock` is in the standard library), `script-language`, `tracked-file-private-paths` (no absolute path or note link in the added lines, which I searched), `return-step-record` (the cycle's, not the author's). None departed from.
- Tests: do they fail when the behaviour breaks? Yes. The boundary test fails for a threshold of 59 or 61. `test_a_git_that_cannot_list_the_review_tags_is_an_error` fails if a list failure is read as no tag, and `test_a_git_that_cannot_describe_a_tag_that_exists_is_an_error` fails if a describe failure is read as no tag; both assert exit 2, empty stdout and an `Error:` prefix. The restart test patches `THRESHOLD` to 3 to avoid building 61 merges and asserts `reminder: yes` before the tag and `merges: 2` / `reminder: no` after it, so it fails if the tag is ignored (6 merges would read `yes`). The test of the case "list names a tag, describe returns empty with exit 0" has no test; git cannot produce it. The prose of the skill files has no test, as for the other skills of the-way.

## The structure of the code the change leaves

`python -B task-cycle/change_file_sizes.py ff88ca3… b7ec371` (exit 0): `review_reminder.py` 102 → 121 lines; `test_review_reminder.py` 153 → 191; `task-cycle/skill/SKILL.md` 734 → 743 (step 13 grew by 9 lines); `request_template.md` 528 → 538; `foundations/decisions.md` 9421 → 9460; the others under 120. The-way departs from a product's coding guidelines (WAY-328) and holds no rule of size or test of it, so the per-function numbers rest on the diff: the function `last_review_tag` grew from 2 to 9 lines of code and holds one decision path each; no function of the change reaches a length that calls for a move. No code has no user after the change: the old branch that took every failure of `git describe` for "no tag" is gone, and its callers (`count`) are unchanged. No name stopped being true: `last_review_tag` still returns the nearest tag or none; the docstring of the module was updated. Nothing to grade above Minor (WAY-363).

## Checks I ran

| Check | Command (from the worktree root) | Result |
|---|---|---|
| Range and head | `git rev-parse HEAD`; `git log ff88ca3..b7ec371`; `git diff ff88ca3..b7ec371` | head `b7ec371207ad67d6378f323433f643e1703335e5`; 3 commits |
| Whitespace of the range | `git diff --check ff88ca3..b7ec371` | exit 0 |
| Tests of the script | `python -B task-cycle/test_review_reminder.py` | exit 0, 11 tests OK |
| Foundation entries | `python -B elements/common/foundation_check.py` | exit 0, `0 errors` |
| Script on the real history | `python -B task-cycle/review_reminder.py b7ec371` | exit 0; `tag: foundation-review/2026-11-15`, `merges: 1`, `threshold: 60`, `reminder: no` |
| Sizes | `python -B task-cycle/change_file_sizes.py ff88ca3bc6beae07dbe1ee5adb1792773d28bcac b7ec371` | exit 0 (table above) |
| Instruction/skill entry points | `python -B gate/run_tests.py agent-instructions` | exit 0, 25 tests OK |
| Searches of the tree | `grep` of the tree (outside `.runs/`, `.git/`) for the old number and the old wording; for absolute paths and links in the added lines; for any other reference to the step numbers of `with_the_human.md` | nothing left of the old number; no path or link; no reference to the step numbers |
| Long lines | awk over the added lines of the range, over 101 columns | 7 lines; the two in Minor 5 are in new text of the skill files; the others in `decisions.md` and the template stay within the 102–103 columns of their neighbours or are template lines |

Not run: the full gate (as the handoff says); `python -B gate/run_tests.py task-cycle` (the author ran it, 480 tests, and the change in `task-cycle` outside the script is Markdown only; I ran the script's own file and the two checks above); the skill-entry-point writer (`agent-instructions/skill_entry_points.py --write`), since no `description:` line of a skill changed (confirmed in the diff); `request_check.py` against a real request (it reads a request, not the template). Unverified therefore: that a real cycle that follows the new step 13 produces a request that passes `request_check.py`; the template's new bullets add no heading and no item of *For you to decide*, so I expect it does.

## Reaches beyond the dispatch

- `foundations/part_map.md` — the entries `decisions`, `task-cycle`, `foundation-review`, `repository`, and the list of files left out (README): to name the parts the change touches.
- `foundations/invariants.md` — a search by *Part* for `every`, `decisions`, `task-cycle`, `foundation-review` (21 invariants read whole): to compare the change with the invariants of the touched parts.
- `foundations/glossary.md` — a search of the headings for "remind", "review", "backlog", "task place", "threshold", "merge": no entry; nothing to read.
- `elements/decisions/template.md` lines 125–200 ("Decision or invariant", "Changing a decision"): to check the five questions "Where it goes" against `weak_points.md` and the rule that *Rationale* and *Rejected* describe the entry as it stands.
- `task-cycle/skill/SKILL.md` steps 12–14 and the other lines the diff does not show (step 13 whole), `foundation-review/SKILL.md` whole, `with_the_human.md` whole, the first 35 lines of `proposals.md`, `weak_points.md` lines 1–45: to read each changed passage in its context.
- `elements/common/way_of_working.md` "Reading the foundation" and `elements/common/decision_index.py` (docstring): the method for my selection.
- `AGENTS.md` (`## Backlog`): the source of "the name of the repository" for Minor 3.
- WAY-07, WAY-02, WAY-33, WAY-344, WAY-365, WAY-05, WAY-12, WAY-11, WAY-134, WAY-150 — opened whole beyond the decisions the task names (WAY-05, WAY-12 for the form of the entries the change writes; WAY-07 for Minor 2; WAY-11 and WAY-134 for the settlements and the return step; WAY-02 and WAY-33 for the references and the search; WAY-365 for the rule on a change that adds to a large file; WAY-344 and WAY-150 as named in the handoff).

## Unread material

**Decisions read whole: 19** of the 58 the index lists in full (and 79 by heading alone): WAY-24, WAY-300, WAY-140, WAY-161, WAY-107, WAY-36, WAY-22, WAY-293, WAY-328, WAY-344 (the ten of *Decisions in play*, each opened whole), and WAY-05, WAY-12, WAY-11, WAY-134, WAY-150, WAY-07, WAY-365, WAY-33, WAY-02. My selection: parts `decisions`, `task-cycle`, `foundation-review`; sections "Decision entries and the decision log", "Accepting and applying decisions", "The course of a task cycle", "The request and the human", "Review of a change", "Scripts and the gate", "The-way and how a product takes it"; the ten decisions of *Decisions in play* by `--decision`. The index is at `docs/task-cycles/foundation-review-reminder/reports/review-whole-index.md` (written by `elements/common/decision_index.py` into `.runs/review-whole/`, which I removed); I read it whole. The run through the headings of the decisions outside my sections: I read the 79 headings of the index; none bears on the change beyond what I opened.

Decisions of the index that bear on the change and I read through their binding sentences in the index only: WAY-18 and WAY-19 (the log's in-place edits and numbering; I relied on the template's "Changing a decision", which cites both), WAY-27 (no reference outside the repository; I searched the added lines for paths and links), WAY-101 (the backlog tool; unaffected), WAY-125, WAY-136, WAY-148, WAY-160, WAY-162, WAY-227, WAY-287, WAY-289 (the course of the cycle, the request and its sections; the change touches the *How to merge* part and I read the template's section whole), WAY-263, WAY-297, WAY-363, WAY-364 (grading, applied in this report). Of the four the author read in part: WAY-161, WAY-107 read whole by me; WAY-150 and WAY-344 read whole by me, the last without bearing.

**Guideline files:** none read, because the-way departs from a product's coding and testing guidelines (WAY-328) and holds no guidelines of its own; no styleguide applies. `elements/decisions/template.md` was read from line 125 to line 200, not whole, for the questions it holds; `elements/common/way_of_working.md` was read from line 40 to line 160.

**Parts of the dispatch not read whole:** `task-cycle/skill/SKILL.md` (743 lines) and `task-cycle/skill/request_template.md` (538 lines) — I read the changed step 13 and its neighbours, steps 12–14, and the section of the template on *How to merge* and the reminder; `foundations/invariants.md` — the 21 invariants of my selection whole, no other; `foundations/part_map.md` — the entries named above whole, the rest by heading; the root `README.md` — lines 100–140 and the changed lines, not the whole file (the part map leaves it out on purpose).

## Searches not found or unclear

- Where "open" is defined for a line of the task place: `project-level/backlog_place.md` says nowhere what open means (the author found the same); step 13 and WAY-300 refer to the task place's rules and to WAY-107, as the task does; for the-way's own backlog the file named by the `task-rules` entry lies on the author's disk and I did not open it, so I could not check that its definition of an open line agrees with what step 13 assumes ("open" as opposed to done). Unverified.
- Which source gives "the name of the repository" for a product whose `## Backlog` section names a directory or a public tracker: not found; see Minor 3.
- A test that holds a sentence of WAY-300 or WAY-24 by a line `decision:`: none exists (the entries are held by their pairs of examples, which WAY-12 allows).
- The text of the daily advisor's reaction to the reminder (out of scope of the task): not looked for.

## Working copies

None made outside the directory the handoff names. In `.runs/review-whole/` I wrote the index, the list of sections, three extracts of decisions, the invariants I selected and one helper script for the extracts; the directory is removed, and the index is kept as `docs/task-cycles/foundation-review-reminder/reports/review-whole-index.md`. No worktree, no clone. The reviewed worktree is unchanged (`git status --short` clean at the end).
