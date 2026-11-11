PASS 9d4bdcde27179325126d1431e6cb825df3290754

# Review of the fix of the four Minor findings — request-decision-groups

Range `ff7799473843608eb11cc2f4e162920d8f7681a7..9d4bdcde27179325126d1431e6cb825df3290754` (one commit, `9d4bdcd`; `git rev-parse HEAD` = the head given; `git status --short` empty). Files: `foundations/decisions.md`, `task-cycle/request_check.py`, `task-cycle/skill/correction.md`, `task-cycle/skill/request_template.md`. Findings file and fix report read. Read-only; no new Critical or Important finding. Beyond the fix I also judged the whole change `e3825a8..9d4bdcd` against the decisions named in the coordinator's message (below).

Counts: blocking 0; Minor remaining or new 2; out-of-scope 0.

## Each finding of the findings file

1. **"Let it through" against "only a task" after a correction — fixed.** The five places now say one thing: the `### Fix or let through` paragraph of the template ("Where the thing cannot be done in this request, and for whatever a correction left unfixed or undone, the item carries only the question 'Make a task of it?'; the human who makes no task lets it through by merging (WAY-289)"), kind 8 ("as anything else a correction left undone does"), the *A correction* row of the variants ("what a correction left unfixed or undone, whether it ran on an answer to item 8, 4, 9 or 14, carries only 'Make a task of it?'"), `task-cycle/skill/correction.md` (last paragraph, "and so is an item that cannot be done in this request at all ... lets such an item through by merging") and WAY-289's third binding sentence. Evidence: `grep -n "Make a task of it\|let it through\|let through"` on the template and a word-level diff (`git diff -w --word-diff`) show only the intended changes; the rest of the rewrap is whitespace. Note, not a finding: the frozen task's *To do* 5 says such an item "daje tylko odpowiedzi 'zadanie' albo 'przepuścić'"; the fix gives one question and lets the merge be the second answer. This is the second way my finding suggested and it means the same to the human, so I count it as meeting *To do* 5.
2. **Where the stages a blocked request did not run stand — fixed.** Kind 1 now names the return step, the reconciliation, the slices not made and the review of the whole change as standing under *Needed from you*; kind 4 says "The stages a blocked request did not run because it stopped are kind 1's, not these"; WAY-287's blocked-request sentence and its *Verification* say the same; the state line now reads "whether any item of *Needed from you* or *Fix or let through* below waits for the human's answer; what the human only accepts by merging waits for nothing". The variants rows for a blocked request (unchanged) agree with kind 1. Reading "waits" as waiting for the human's answer is right: WAY-287 says the accepting group "waits for no separate answer".
3. **WAY-289 title — fixed.** `foundations/decisions.md:9167`: "Which things the cycle left unfixed or undone does a request put before the human for a decision?". The number is unchanged. `grep -rn "Which unfixed findings"` over `*.md` and `*.py` outside `.runs` and `.git` finds nothing.
4. **Wrapping — fixed in the places named, with two new ragged lines.** `task-cycle/request_check.py:50` is rewrapped; `git diff ff77994..9d4bdcd -U0 | grep '^+' | awk 'length>101'` lists no line of `request_check.py`, and none of the template's kind entries. The template's step 5 and "two parts" bullet are rewrapped; WAY-327's *Rationale* is reflowed. See Minor A below for what the reflow left behind.

## Minor findings that remain or are new (do not block)

- **A. New ragged lines in `foundations/decisions.md`, made by the fix.** In WAY-287's *Verification* (`foundations/decisions.md:9091-9092`), the added clause ends in a line of about 190 characters ("run under *Needed from you*, while the finding's place and reason stand in the lower part; a request whose review of the whole change read 40 of 151 selected decisions whole and"); in WAY-289 the binding paragraph has two long lines (`:9181` "through by merging, or stays in the lower part, so that the loop ends after one correction. Every finding stays" about 113 characters) and the heading line of WAY-289 (about 110 characters, which a heading may be). The base already holds 536 lines above 100 characters in this file, so nothing breaks; it is the same cosmetic finding the fix set out to remove.
- **B. WAY-289's *Rationale* does not give the reason for the new rule.** `foundations/decisions.md` WAY-289, the binding sentence now says what "cannot be done in the request at all" carries, and the *Rationale* explains only the correction's leftovers ("what the correction leaves goes only with the question of a task, or stays below"). A reader will not find why a thing that cannot be done here carries a task question and no "let it through" answer. The binding sentence and the template carry the rule, so nothing is lost.

## What the fix itself could have broken

- The tests: `python -B gate/run_tests.py task-cycle` exit 0 (254 tests, including the template-example test). No test file changed; the change to `request_check.py` is a docstring rewrap (`git diff` shows the three lines only).
- The template example still passes the form check (the test above).
- Kind numbers: `grep -c '^- \*\*[0-9]*\.\*\*'` over the template finds 15 kinds; the word diff shows no kind's content changed beyond the sentences above, so "item 8" (`correction.md`), "item 12" (`SKILL.md:563`) and "item 4" (kind 13) still point at the same kinds.
- WAY-287 holds three binding sentences (the decisions template allows one to three, `elements/decisions/template.md:96`); WAY-289 holds three. `foundation_check.py`: exit 0.
- No stale statement of the old wording in the other foundation files: `grep` of `foundations/*.md` (except `decisions.md`), `agent-instructions`, `task-cycle`, `elements` for "For you to decide", "Merge as it stands", "Fix it in this request" finds none outside the edited files.

## The whole change `e3825a8..9d4bdcd` against the decisions I had read by title

Each read whole now (they follow the statement of what I found, in the order of the coordinator's list):

- **WAY-33** (search of the whole foundation): the author's search found WAY-317 and edited its *Verification* example in the same change; the search found nothing else that I could add (grep of the whole foundation for the old question wording, above). Met.
- **WAY-150** (reading, counts): this report's counts follow it; the author's lacks (WAY-150 not opened) did not change the content of the change. Met.
- **WAY-316, WAY-318** (screenshots and artifacts in the description): the template's passages on them are unchanged except kind 13, which now states the fact for the human to accept by merging; WAY-316's rule (no screenshot in the product's repository, a place the product settles) is untouched. Met.
- **WAY-308, WAY-309** (private paths): `private_paths_check.py` on the six files of the first range and the four of the fix: exit 0 each; the template's example holds no path or note link. Met.
- **WAY-134** (rows kept, rejected options the source keeps): WAY-287 carries all four ways not chosen from the task's *Not chosen* (the three-with-one, bold lines, three sections, only groups that hold an item); WAY-327 the two of its row; WAY-290 the template-alone way. Met.
- **WAY-126** (projected entries): no projected entry in this task. Not reached.
- **WAY-164** (own-work check): the author's report names the requirement, the check and what it showed; I repeated it. Met.
- **WAY-168, WAY-213** (guidelines): the-way has no `guidelines/` directory (task *Context*), so no guideline rule is reached. Not reached.
- **WAY-287, WAY-289, WAY-290 whole:** the groups, the answers for items 4, 9 and 14, and the form check's headings agree between the entries, the template, `correction.md` and the script. The one place I found where two of them disagree in detail is WAY-289's *Verification* *violates* ("a skipped step is offered only the answers of a task or a let-through while it can still be run in the request"), which speaks of the case before a correction and agrees with the template. No finding.
- **WAY-288, WAY-295, WAY-317, WAY-10** (read whole now too): the block translates the headings (WAY-288, kept by the template); WAY-295's item sits in the accepting group (kind 10, no question), consistent with the entry; WAY-317's *Verification* and the template's kind 13 agree; WAY-10 holds.

No new finding from these reads.

## Checks I ran

| Check | Command | Exit |
|---|---|---|
| Focused: task-cycle | `python -B gate/run_tests.py task-cycle` | 0 (254 tests) |
| Foundation check | `python -B elements/common/foundation_check.py` | 0, `0 errors` |
| Instruction files | `python -B instruction-files/check_instructions.py .` | 0, `0 error, 0 warn, 3 info` |
| Private paths on each of the four changed files | `python -B task-cycle/private_paths_check.py <file>` | 0 each |
| Long lines added by the fix | `git diff ff77994..9d4bdcd -U0 \| grep '^+' \| awk 'length>101'` | lists the lines of Minor A (none from `request_check.py`) |
| Whitespace-blind diff of the fix | `git diff ff77994..9d4bdcd -w`, and `-w --word-diff` for the template | read in full; only the changes listed above |

Not run: the whole gate (the orchestrator's).

## Declined to judge

- The wording of any real request written under the fixed rules: no real description is in the range.
- Whether WAY-289 should have a *Rejected* entry for "a let-through answer for what cannot be done in the request" (Minor B touches its *Rationale* only): the task did not ask for one.

## Reach beyond the dispatch

- `task-cycle/review/fix.md` (whole): the method of this variant.
- `foundations/decisions.md` WAY-33, 150, 316, 318, 308, 309, 134, 126, 164, 168, 213, 288, 295, 317, 10 (whole), WAY-287, 289, 290 (whole): at the coordinator's direction, with the earlier reads of the whole-change review.

## Unread material

Counts for the whole change (my selection: parts `task-cycle` and `decisions` by *Scope*, 157 decisions): **31 read whole** and **126 by title only**. Read whole: WAY-05, 07, 10, 33, 114, 126, 134, 150, 161, 162, 164, 168, 213, 227, 263, 286, 287, 288, 289, 290, 291, 292, 295, 300, 308, 309, 316, 317, 318, 326, 327. The first review's count was 14 whole, 143 by title; the coordinator's message added WAY-33, 150, 316, 318, 308, 309, 134, 126, 164, 168, 213 (11), and I read whole WAY-289, 290, 288, 295, 317, 10 which I had read in part (6).

Still unread whole: the remaining 126 decisions, read by title only (every title read). Decisions with a title that bears on the change, still unread whole: WAY-294 and WAY-296 (the remarks check and the form of the remarks: the request's kind 10 cites WAY-295 only; the change does not touch the check), WAY-219 and WAY-220/221 (user-interface checks; no screen in this change), WAY-306 (merge of the target branch; `correction.md` is touched only in its last paragraphs, not in the paragraph on the merge), WAY-300's neighbours WAY-301 (review tag). Invariants: `foundations/invariants.md` not read whole (the entries naming `task-cycle` were read by the author and checked by their tests, which pass). Part map: the `task-cycle` and `decisions` entries were read in the first review as the author's report names them; not re-read. Glossary: not read. `task-cycle/skill/SKILL.md`: passages only. Guideline files: none exist.

## Searches not found or unclear

- A quote of the old WAY-289 title: searched, none.
- A rationale in WAY-289 for the new "cannot be done at all" rule: looked for, not found (Minor B).
- Whether the frozen task's *To do* 5 ("odpowiedzi 'zadanie' albo 'przepuścić'") asks for two printed answers or two outcomes: unclear; the fix gives one question and a merge as the second outcome. I read it as the outcomes.

## Addendum: seven decisions read

Read whole in `foundations/decisions.md` at head `9d4bdcde27179325126d1431e6cb825df3290754` (unchanged; `git rev-parse HEAD` confirmed), and the whole range `e3825a8..9d4bdcd` judged against each. The first line of this report stands: no Critical or Important finding appeared.

- **WAY-294** (process remarks check): no finding. The change adds nothing to the reports or to the remarks; kind 10 of the template still points at the remarks check as `SKILL.md` gives it, and the form check's script does not read `reports/`.
- **WAY-296** (form of the process remarks): no finding. The change writes no process remarks into a section or file of its own.
- **WAY-219** (user-interface check before review): no finding. The template keeps "a screenshot unchecked (WAY-219)" as a kind 4 item in *Fix or let through* and kind 13 still sends a screenshot unchecked for want of a settled way to kind 4; for such an item that cannot be done in this request, the fixed group paragraph gives the task question only, which agrees with WAY-219 (it asks that the gap be shown to the human, not that a screenshot be forced).
- **WAY-220** (grading of appearance findings): no finding. The change has no screen; my four Minor findings of the first review were graded by their effect on the writer and the reader of the template, as it asks.
- **WAY-221** (departure from a guideline example): no finding. The-way has no product guidelines, so no example was in play; none of my findings rested on a departure from an example.
- **WAY-306** (review of the merge of the target branch): no finding. The fix touches only the last paragraphs of `task-cycle/skill/correction.md` (items to do in the request), not the paragraph on the merge of the target branch, which is unchanged.
- **WAY-301** (mark of the last foundation review): no finding. The template's reminder in *How to merge* (WAY-300) is unchanged and still not an item of *For you to decide*.

Counts for the whole change, selection of 157 decisions (parts `task-cycle` and `decisions` by *Scope*): **38 read whole, 119 by title only** (31 before this addendum plus the seven above).

Still unread whole: the 119 other decisions, every title read; no title among them points to a bearing on the change that I did not open, as far as I can tell from the titles (a decision with an unremarkable title that bears on the change can pass unopened, as WAY-150 says). `foundations/invariants.md` not read whole (the entries naming `task-cycle` were read by the author and their tests pass); the part-map entries of `task-cycle` and `decisions` and `foundations/glossary.md` not re-read; `task-cycle/skill/SKILL.md` read in passages only; no guideline files exist.
