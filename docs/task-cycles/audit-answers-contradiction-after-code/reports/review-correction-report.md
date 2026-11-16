FAIL b3bd8f4e1b401ab38ccf6e22f2fa96847c508490

# Review of correction 1 — audit-answers-contradiction-after-code

- Range: base `428cc4553042992c6a9813e7dd0a9ef11f0e2ea1` to head
  `b3bd8f4e1b401ab38ccf6e22f2fa96847c508490` (`git rev-parse HEAD` in the reviewed worktree gives the
  head). `git log 428cc45..b3bd8f4`: `3d8d4ca` and `7101a44` add and remove the record's copy, `b3bd8f4`
  is the correction; the diff reviewed is `git diff 428cc45 b3bd8f4` (6 files, +81/-21).
- Method: `review-change` (`task-cycle/review/SKILL.md`) with `task-cycle/review/fix.md`, for a
  correction made for the human's remarks: the remarks take the findings file's place.
- Counts: 1 blocking (Important, within the task), 3 Minor (within the task), 1 out of scope.

## The remarks, as made

- **Remark 1 — fix I-2 as the finding says: made for the two records the finding names; the defect
  it names remains for one more shape (R-1 below).**
  - The record of the finding (an empty item, `reason: \`open design choice\`; 10:32, ...` on the line
    under it, `- reason: \`size\`; 14:05` as an entry) gives at the head `unknown` with "holds more than
    one reason in a form that is not read ..." (at `428cc45` it gave the false `no`). The one-attempt
    text with its details as a list gives `yes` again (at `428cc45` `unknown`, at `ab2c8c8` `yes`).
    Both are held by new tests through `read_contradiction`
    (`process-audit/test_record_items.py:129`, `:141`) and through the command
    (`process-audit/test_audit_count.py:3728-3731`).
  - **The author's choice** — read the whole item as the text of one attempt where a plain line stands
    beside the entries, rather than `unknown` for any plain line — I judge sound: it keeps every answer
    `ab2c8c8` gave right, the details-as-a-list form included, and a plain line that opens the item is
    then read by the one-attempt rule, which gives `unknown` for a second `reason: \`` anywhere in the
    text. Where an entry opens the item and a plain line stands at its indent, the whole text opens with
    `- ` and so gives `unknown` with the new reason "a plain line stands beside the entries ...". Its
    one cost is Minor M-2 below.
  - The earlier answers still stand: the six records of
    `test_audit_count.ProcessVersions.test_the_marker_of_a_discarded_attempt_gives_q1` keep their
    answers (`yes`, `no`, `no`, `no`, `yes`, `no`); no earlier test of `test_record_items.py` or
    `test_audit_count.py` was changed other than by addition; the four denials of review #100 give
    `unknown`. The answers that moved from `yes`/`no` to `unknown` between `428cc45` and the head
    (probe below: an entry beside a plain line, `none` on a plain line beside an entry) are items in
    no form the template gives, and `unknown` is what `ab2c8c8` gave for them; no answer moved from
    `unknown` to a wrong `yes` or `no`.
- **Remark 4 — N-1: made.** The four places that write a discard now say that the earlier attempt is
  rewritten as an entry too, as the template gives it: `task-cycle/skill/SKILL.md:375-377` (open design
  choice), `:384-386` (size), `task-cycle/skill/reserved_return.md:35-38`,
  `task-cycle/skill/correction.md:43-46`. A search of `task-cycle/**/*.md` for `discard` finds no other
  place that writes the item.
- **Remark 2** (the return step and the merge of the target branch with its review) is the cycle's,
  not in this range; not judged here.
- **Remark 3**: the section *The route of the narrowing of WAY-344* below.

## Findings

### Important

**R-1. An entry indented deeper than the next one, standing first under the item, is dropped: an
item whose first entry is `open design choice` gives Q1 `no`.** (Within the task; it counts as I-2
remaining, WAY-162.)

- Place: `process-audit/record_items.py:233-234`, the new predicate of the correction:
  ```python
  alone = lines[0][1] is not None and all(
      marker is not None or indent > base for indent, marker in lines)
  ```
  It asks that the first line be an entry, not that it stand at the entries' indent (`base`, the
  smallest indent of an entry). A first entry deeper than `base` passes, and `discarded_entries` then
  returns only the entries at `base` (`:235`), so the first entry is passed over in silence. The
  docstring's reason for letting deeper lines through — "A plain line deeper than the entries continues
  one of them" (`:225-226`) — does not hold for a line that comes before any entry at `base`: there is
  nothing for it to continue.
- Evidence (my probe at the head, `read_contradiction` on the record):
  ```
  - Discarded attempt:
      - reason: `open design choice`
    - reason: `size`
  - Review rounds: none
  ```
  gives `('no', None)` at the head and at `428cc45`; at `ab2c8c8` it gave `unknown`. The same with a
  third entry `- reason: \`reserved choice\`` gives `('no', None)`. As Markdown, the two lines are two
  entries of one list under the item (the first is indented by 2 within the item's content, the second
  by 0, and the second is no continuation of the first), so the record holds two attempts, one of them
  an open design choice.
- Why it matters: a false `no` for a cycle that had an open design choice — the answer on which the
  human weighs whether a cycle needed a spec, and the kind of answer the remark says this task removes.
  The handoff asks that crafted input with deeper and shallower indents give no wrong `yes` or `no`;
  `record_items.py` reads lines from git history and calls them untrusted (`:4-5`). Writing the first
  entry at a different indent than the ones added later is an ordinary slip when a leader adds an
  entry to a list it wrote in an earlier turn.
- Fix, checked: add `lines[0][0] == base and` to the predicate. In a worktree of the head with that
  one change, the probe gives `unknown` for both records above, and
  `python -B -m unittest test_record_items` in `process-audit` passes, 29 tests (the test
  `deeper` at `test_record_items.py:183-185`, a sub-entry under an entry at `base`, still gives `no`).
  The reason it then gives, "a plain line stands beside the entries", is wrong for a line that is an
  entry; a reason that names lines at another indent than the entries fits both cases. A test with the
  record above.
- Contradiction: yes — WAY-405 (the reason stands "at the start of each entry under the item, one
  entry for each attempt", and its *Verification*: "an item of several entries gives yes where any of
  them has the marker `open design choice`") and the task's *To do* 3 (`yes` where *Discarded attempt*
  has the marker `open design choice`).

### Minor

**M-1 (within the task). In the entries form only the first line of an entry is read for a second
marker; in the one-attempt form the whole text is.** `process-audit/record_items.py:249-250` passes
each entry's first line to `discarded_reason`, which gives `SEVERAL` for a second `reason: \`` only in
the text it is given. An entry `- reason: \`size\`; 14:05` with a line under it `reason: \`open design
choice\`` (deeper, a continuation) or a sub-entry `- reason: \`open design choice\`` gives `no` (probe:
`size entry, deeper plain odc` and `size entry, deeper odc sub-entry`, both `('no', None)`), while the
same text as a single attempt (`reason: \`size\`; 14:05` on the item, the second line under it) gives
`unknown` for two reasons. The docstring at `:244-245` says "the reason of an entry that ... holds two
markers is None". The sub-entry case is held as intended by the test at `test_record_items.py:183-185`
(from `428cc45`), and WAY-405 reads only "the start of each entry", so this is no departure from the
decision; it is an inconsistency between the two forms that a leader would meet only by writing two
reasons into one attempt's details. Joining an entry's deeper lines into its text before
`discarded_reason` would give `unknown` there.

**M-2 (within the task). The chosen way reads a second attempt with a malformed marker as a detail of
the first.** In the shape of I-2 (first attempt plain under an empty item, second as an entry), where
the entry's marker is malformed so that it holds no `reason: \`` — `- reason: open design choice` with no
backticks, or `- open design choice found at 14:05` — the whole is read as one attempt with its
details as a list and gives the first attempt's marker: `no` where it is `size` or `reserved choice`.
The other way of the finding (`unknown` for any plain line beside entries) gives `unknown` here, at the
price of losing the details-as-a-list form. It takes two departures from the written form at once (the
first attempt not rewritten as an entry, which remark 4 now instructs, and a malformed marker), so I
keep the author's choice and note the trade.

**M-3 (within the task, outside the correction's diff). The docstring of `audit_count.py` still says
only the start of the item is read.** `process-audit/audit_count.py:149-151`: "the item *Discarded
attempt* opens with `reason: ` and the marker `open design choice` ... and only the start of the item is
read" — since `428cc45` the marker also stands at the start of each entry under the item (WAY-405). A
reader of the command's help would not learn the entries form. Not reopened by fix.md.

### Out of scope

**O-1. A line at the margin ends an item, so a lazy continuation of an entry is not read.**
`process-audit/record_items.py:185-186` (`item_texts`, unchanged since before the task) ends an item at
the first line with indent 0; `remarks_check.split_lines` also splits at a bare CR. An entry
`- reason: \`size\`` followed by a CR or newline and `reason: \`open design choice\`` at the margin gives
`no` (probe: `CR inside entry`). Markdown would show the second line as part of the entry. It is the
reading of every item of the record, older than this task, and low in likelihood.

## Declined to judge

none

## The route of the narrowing of WAY-344 (remark 3)

**Judgment: the route holds**, on the condition that the narrowing binds only at Mariusz's own merge of
the request (WAY-14). No finding.

Read whole at the head: WAY-14, WAY-30, WAY-114, WAY-314, WAY-315; WAY-344 whole; the narrowing by
`git show 428cc45 -- foundations/decisions.md` (the new sentence at `foundations/decisions.md:2877-2882`,
the *Verification* clause at `:2901-2904`, the *Rationale* sentence at `:2945-2948`).

1. **The narrowing is beyond the task document, and needed there.** No row of *Settlements to record*
   and no entry of *Decisions in play* names WAY-344, so the task document carries no change of it.
   The contradiction showed during implementation: the change reworked the reading of `cycle.md`, so
   WAY-344's clause "the whole reading of each file whose way of reading the change reworks — every
   field of that file" brought every line and item of `cycle.md` the count reads under the rule, and
   the code read their absence as `unknown` with no `Error:` (I-1 of the review of the whole change).
   The narrowing names exactly those seven lines and items and no other file, so it is no wider than
   the contradiction.
2. **WAY-30 gives the route.** "When a contradiction shows only during implementation, the agent stops,
   quotes the decision by its number, and either brings the change into line, drops the change, or
   proposes on the task branch an edit of the decision, a new wording or a narrowing, and the code that
   needs it waits for that human." Its *complies*: "a task branch whose code goes against a decision
   carries a proposed narrowing, and the merge waits for the human who accepts it". The branch carries
   the narrowing in the entry itself, not in a task document, plan or record ("no exception lives only
   in a task document, plan or cycle record").
3. **WAY-315 sends an agent in a cycle to that route.** "In the cycle no agent departs from a decision
   on its own and returns with the question, as WAY-30 gives." The author first departed on its own
   (I-1); the fix turned the departure into WAY-30's proposal, and the question now stands before the
   human in the request. WAY-315 also says that the looser rules of refinement hold only before the
   cycle, so **WAY-314** (the human's choice of an option at refinement as consent) gives this narrowing
   no route of its own and takes nothing away from WAY-30's.
4. **WAY-14 and WAY-114: who accepts and by which act.** WAY-14: "A decision, and every change to it,
   binds once a human accepts it, never an agent. In the-way, that human is Mariusz", and its
   *complies*: "a decision written on a task branch binds once Mariusz merges its request". WAY-114: the
   meaning of an entry no row or projected entry carries is accepted "at the merge of the change that
   holds it", with a plain sentence in the section for the human's decisions; "before that, a question
   goes to the human only where ... the entry would change the meaning of an approved decision". The
   narrowing does change the meaning of approved WAY-344 (a record that lacks an item went from a
   missing field with `Error:` and exit code 1 to no missing field), so it is such a question, and
   `task-cycle/skill/foundation_step.md:35-37` says the same ("an entry would change the meaning of an
   approved decision beyond what the accepted task document or plan carries (WAY-30)").
5. **Where the route was bent, and why it still holds.** The remarks show the narrowing stood as item 5
   under *You accept by merging*, the group for "what the cycle did within its authority"
   (`task-cycle/skill/request_template.md:206`), while by point 4 it was a question for the human, which
   the foundation step returns as `blocked` for *Needed from you* (`foundation_step.md:46-48`,
   `request_template.md:222-226`). The human's answer cures that placement: remark 3 names it ("item 5
   changes a standing rule") and the closing paragraph accepts items 5–7 on the condition of this
   reading. So the question was put and answered by the human's own reading, and asking it again in
   *Needed from you* would ask twice. That answer is written by the day advisor on Mariusz's behalf;
   under WAY-14 it is the merge, by Mariusz, that makes the narrowing bind — the route as the handoff
   states it ("accepted by the human's merge").
6. Recommendation for the request after this correction: keep the narrowing as the cycle's, with its
   plain sentence saying that it changes a standing rule (WAY-344) and that the human accepted it in
   the answer to the request on the condition of this reading, which holds; nothing for the human to
   leave aside.

## Checks run

All in a worktree of the head, `.runs/review-correction/head`:

- `python -B gate/run_tests.py process-audit` — exit 0, 267 tests, OK.
- `python -B gate/run_tests.py task-cycle` — exit 0, 534 tests, OK (1 skipped: Windows gives a killed
  process no signal number).
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`.
- Manual: a probe script running `record_items.read_contradiction` on 32 crafted records at the head, at
  `428cc45` and at `ab2c8c8` (worktrees of each): the two records of the finding; deeper and shallower
  entries and plain lines; `none` beside entries; numbered and `*` entries; tab-indented entries (tabs
  are expanded to 4 by `split_lines`, so they behave as deeper lines); fenced lines before entries; NUL,
  ESC and a bare CR; 100,000 entries with a plain line (0.19 s), 100,000 plain lines then an entry
  (0.13 s), 100,000 deeper lines (0.12 s), one 2,000,000-character line (0.01 s), a 2,000,000-space
  indent (0.09 s), 50,000 markers on one line (0.01 s). No hang, no crash, every reason a fixed string;
  wrong answers: R-1 (`no`), M-1 (`no`), O-1 (`no`).
- Manual: R-1's fix (`lines[0][0] == base` added to the predicate) in a fourth worktree of the head:
  the probe gives `unknown` for R-1's records; `python -B -m unittest test_record_items` in
  `process-audit` — exit 0, 29 tests, OK.
- Not run: the product's full gate, by the handoff.

## Reaches beyond the dispatch

- `task-cycle/remarks_check.py` (`MARKER`, `indent_of`, `split_lines`, `fenced_flags`) — how the lines
  under the item are cut, for the probes of indents, tabs and CR.
- `process-audit/record_items.py` at `ab2c8c8` — the answers before the fix of M-1.
- `reports/review-whole-findings.md` I-1 — what contradiction the narrowing of WAY-344 answers.
- `task-cycle/skill/foundation_step.md` (whole) and `task-cycle/skill/request_template.md:186-315` —
  where a change of an approved decision goes in the request, for remark 3.
- `task-cycle/record_template.md:38-44` — the form of the item.
- `process-audit/audit_count.py:144-160`, `process-audit/SKILL.md:218-232` — whether the descriptions
  of the reading still agree (M-3).

## Working copies

Four detached worktrees under
`.runs/review-correction/` — `head`
(b3bd8f4), `base` (428cc45), `old` (ab2c8c8) and `mut` (b3bd8f4 with R-1's one-line fix) — and the
probe script, its outputs and the check outputs in the same directory. Each worktree removed with
`git worktree remove --force` (exit 0 for each), then `git worktree prune`, and the directory
`.runs/review-correction/` deleted; `git worktree list` names none of them and the reviewed worktree is
clean. No remainder. Nothing kept in `reports/`: the
probe inputs and outputs that the findings need stand in them.

## Unread material

- WAY-14, WAY-314 and WAY-315 read whole, and WAY-30, WAY-114, WAY-344 and WAY-405 whole, at the head.
- `process-audit/test_audit_count.py` and `process-audit/test_record_items.py`: the diff and the
  tests of the item *Discarded attempt* around it, not whole.
- The request's description itself is not in the worktree; item 5's placement is read from the
  remarks.
- Nothing else of the dispatch left unread.

## Searches not found or unclear

- The request's description (to see item 5's wording and group directly): not found under
  `.runs/task-cycles/audit-answers-contradiction-after-code/reports/`; its placement is taken from the
  remarks' words "Items 5–7 in \"You accept by merging\"".
- Whether the day advisor who writes on Mariusz's behalf is a human: unclear from the files; it does not
  change the judgment, since the merge is the act that binds (WAY-14).
