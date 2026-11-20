PASS 357965408b529da7d5965c6384c4883913ae1ddc

# Review of correction 1 and the reading of six decisions

Reviewed: the correction's range `2ffff547..35796540` (one commit, `35796540`, one file,
2 insertions and 1 deletion), and the six decisions of remark 2 read whole against WAY-05 and the
length check. `git rev-parse HEAD` gave `357965408b529da7d5965c6384c4883913ae1ddc`, the head I was
given. No blocking finding; three Minor findings, all outside the task's scope.

## The remarks

1. **Remark 1 — made, and no more.** `guidelines/coding-shared-module.md:4` now reads
   `- **Applies to:** relation-model · process-audit · task-cycle · elements-common`, and
   `guidelines/coding-shared-module.md:43` adds `` `elements/common/` `` as the last item of
   *Where in code*. Nothing else of the file changed (`git diff 2ffff547..35796540`): the table
   *Files of this kind*, the rule, the example and the index row in `guidelines/coding.md:21` stand
   as they were.
   - Form against the templates: `product-guidelines/template.md:74` asks for parts of the map joined
     by ` · `; `elements-common` is a part (`foundations/part_map.md:65`). The template of a kind
     (`product-guidelines/coding/template.md:123`) asks that *Applies to* name the parts the files of
     the kind lie in, and (`:275-277`) that *Where in code* give the directories its files lie in:
     `elements/common/` holds two modules other scripts import, `foundation_source.py` and
     `foundation_text.py`, the second added by this request. The new path is in backticks, relative
     to the root, and git tracks files under it (`product-guidelines/template.md:101-103`).
   - Does the guidance reach the agent: by `product-guidelines/reading.md:39-43` a file
     `guidelines/coding-<kind>.md` is read where its *Applies to* names an affected part and its index
     row's *When to read* matches the work. Both now hold for a change of a shared module in
     `elements/common/`. This stands on reading: no test checks the selection, as the author says.
   - The tests that read the file: only the check of the foundation reads a guidelines file's
     *Applies to* and a rule's *Invariant* (`elements/common/foundation_check.py:944-975`); it gives
     `0 errors`. No other test reads `guidelines/coding-shared-module.md` (search below).
   - The rule the guidance now hands to the part holds there today: a new interpreter that imports
     `foundation_text` and `foundation_source` with an empty input ended with exit code 0 and wrote
     nothing to either output (manual check below).
   - The author's report agrees with the diff in each claim I checked: the two lines, the commit, the
     clean worktree, the results of `product-guidelines`, `elements/common` and the check of the
     foundation. I did not rerun `agent-instructions` (see the checks).
2. **Remark 2 — made: each of the six decisions read whole**, from its heading to the next heading,
   with binding sentences, fields, *Rationale* and *Rejected*. The account of each is in the next
   section; the findings follow it.

## The six decisions read whole

Reference read for this: WAY-05 whole (`foundations/decisions.md:682-755`), `check_length`,
`excess`, `base_paragraphs`, `base_sentences` and `run` in `elements/common/foundation_check.py`,
its description (lines 1-134), and `elements/common/foundation_text.py` whole.

| Decision | Lines read | Measures by the check today | Collision |
|---|---|---|---|
| WAY-344 | `foundations/decisions.md:2947-3116` | paragraph 1: 8 sentences, 743 words (listed) | none found |
| WAY-134 | `foundations/decisions.md:5503-5645` | paragraph 1: 478 words (listed) | none found |
| WAY-18 | `foundations/decisions.md:814-866` | within both limits | none found |
| WAY-19 | `foundations/decisions.md:867-899` | within both limits | finding 1 (Minor, outside the scope) |
| WAY-150 | `foundations/decisions.md:1650-1777` | paragraph 1: 317 words (listed) | finding 2 (Minor, outside the scope) |
| WAY-321 | `foundations/decisions.md:2059-2095` | within both limits | none found |

- **WAY-344** (a field missing from a file a script reads). The length check reads the log of the
  working tree and its copy at the commit the branch left. It looks for no named field there beyond
  what the check already read before this request: the heading of an unversioned entry and the first
  field line or `*Rationale:*`, which ends the binding sentences. The fields of an entry of the
  working tree stay reported by the check of fields as findings with exit code 1, as WAY-344 gives
  for a check of form. A base that is unknown, or a copy of the log the base lacks, makes no decision
  added or changed and is listed, never read as an empty file, which agrees with the sentence of
  WAY-344 on a copy from the commit the branch left and with its *Rationale* ("a gap in what the
  check compares with, never a fault of the change"). `foundation_text.py` is a new file, but it
  holds readers moved word for word out of `foundation_check.py` and reads no file, so I do not take
  it for a script a change adds whose readings each need a new test. The change adds no part to the
  part map (`foundations/part_map.md` changes the description of `elements-common` only), so the
  clause on the *Scope* of WAY-344 is untouched. No collision.
- **WAY-134** (how a task carries what its refinement settles). The cycle writes a kept row "keeping
  its meaning and choosing its wording", so the cycle keeps the freedom the limits need. A row that
  goes to a sentence of an entry already over a limit makes that entry changed, and the check then
  stops the change until the old paragraph is within the limits: that is the consequence the task
  settles on purpose (the answer under "Błąd czy linia `listed:`", on trial), not a collision. The
  rejected options this request gave WAY-05 are the ways not chosen under the task's questions, and
  the question of where the twelve entries are mended, a way of the process, stays out of them, as
  WAY-134 gives. No collision.
- **WAY-18** (how the log is kept). The check finds a decision at the base by its number, not by its
  place, so an entry moved to another section, its words and paragraphs as they were, is not changed:
  probe `moved` below kept WAY-256 a listed line at its new place, with 0 errors. The list the check
  prints is written nowhere, so it is no view kept in the log's place. A section's heading and
  sentence are not read as binding sentences of the entry before them. No collision.
- **WAY-19** (how decisions are numbered). No collision with the limits or the check: a decision is
  found by its number, which WAY-19 keeps for good; a new answer rewrites the entry and so counts as
  a change; and an older entry that loses a sentence to a new decision counts as changed too, so the
  change that moves the sentence must bring that older entry within the limits (probe
  `lost_sentence` below), which WAY-05 chooses in its *Rejected* ("an error only where a change adds
  an entry over a limit or lengthens one already over it"). What I found is that WAY-19 does not give
  the rule the remark takes it to give, and names the part in other words than WAY-05: finding 1.
- **WAY-150** (which foundation material is read). The index gives each paragraph of the binding
  sentences apart (`elements/common/decision_index.py:158-159`), so a reader of the index sees the
  division the limits count. Nothing in its sentences, fields, *Rationale* or *Rejected* goes against
  the limits or the error. One sentence names the entry's own first paragraph by its place:
  finding 2.
- **WAY-321** (the report of an invariant with no citing test). Its sentence says the switch
  `--skip-test-citations` "skips this report and no other". `run` calls `check_length` whatever the
  switch (`elements/common/foundation_check.py:1081-1085`), and probe `switch` below gave the error
  of the length with the switch passed. The report of an uncited invariant stays in
  `foundation_check.py`, the file WAY-321 names. No collision.

## Findings

### Critical

none

### Important

none

### Minor, within the task's scope

none

### Minor, outside the task's scope

1. **WAY-19 gives no rule of a paragraph, and it names the part in other words than WAY-05.**
   Place: `foundations/decisions.md:871-872` (WAY-19), `foundations/decisions.md:685-686` and
   `:730-732` (WAY-05), `elements/decisions/template.md:133-134`.
   - What the files say. WAY-19, binding: "a part of the question an existing entry answers is a
     sentence of that entry where it cannot change without changing that entry". The entry holds the
     word "paragraph" nowhere, in its sentences, fields, *Rationale* or *Rejected*. The rule of a
     paragraph is WAY-05's alone: "one paragraph of one to three binding sentences for each part of
     another question that it answers". The template joins the two: "A part of another question that
     the entry answers (WAY-19) has its own paragraph after that one".
   - What is wrong. The same thing has two names that read as opposites: for WAY-19 it is a part of
     *the question the entry answers*, for WAY-05's binding sentence and the template a part of
     *another question*; WAY-05's own *Rationale* uses the first ("A part of a question that an entry
     already answers is a paragraph of its own"). And WAY-19 gives the part one sentence, WAY-05 a
     paragraph of one to three.
   - Why it matters now. Before this request nothing stopped a change at a fourth sentence. Now the
     place of such a part decides whether a change passes: in the first paragraph it counts toward
     that paragraph's limits, in a paragraph of its own it does not, and the check does not limit the
     number of paragraphs. Whether a part earns a paragraph of its own is left to the reviewer, who
     has these two wordings to judge by. A reader who takes WAY-19's words puts the part into the
     first paragraph, meets the error and joins sentences; a reviewer who takes WAY-05's words
     literally may refuse a paragraph for a part of the entry's own question. The next task meets
     this at once: the eight sentences of WAY-344 are cases and exceptions of its one question, and
     WAY-19 forbids them a number of their own, so they fit the limits only as paragraphs of their
     own.
   - Grade and scope. Minor: the words of both entries predate this request, the check works as
     WAY-05 says whichever reading is taken, and WAY-05's *Rationale* with the template's citation
     carry the intended reading. Outside the task's scope: the task changes WAY-05 in the five ways
     its *Decisions in play* list and leaves WAY-19 alone; aligning the words changes an approved
     binding sentence, which is the human's to approve. I recommend the human settles, before the
     task that shortens the twelve entries, whether a part of an entry's own question that cannot
     change apart from it has a paragraph of its own; one phrase of WAY-05 or of WAY-19 then says so.
2. **WAY-150 names its own first paragraph by its place.** Place: `foundations/decisions.md:1682`:
   "the decisions the first paragraph names being opened whole as it gives".
   - Why it matters. The first paragraph of WAY-150 has 317 words, so the next change of WAY-150 has
     to cut or divide it, and WAY-05 now counts a new division as a change. If the passage that names
     the decisions opened whole lands in another paragraph, this sentence points to the wrong one,
     and no check reports it.
   - Grade and scope. Minor, a hazard for the task that changes WAY-150 and no fault of this
     request's files. Outside the task's scope: the task shortens no entry.
3. **WAY-391 does not name `elements-common` in its *Scope*, while the guidance that names it now
   applies there.** Place: `foundations/decisions.md:11171` (`- **Scope:** relation-model`) against
   `guidelines/coding-shared-module.md:4`.
   - What is wrong. For the five other kinds the *Scope* of the decision that designates the exemplar
     is the same list as the *Applies to* of the kind's guidance (WAY-386 to WAY-390). For
     `shared-module` the *Scope* names `relation-model` alone, while WAY-391 also says "importing a
     file of the kind runs nothing" and the guidance applies to four parts. The gap stood for
     `process-audit` and `task-cycle` before; the correction adds a third part to it.
   - Why it matters. An agent that changes a shared module in `elements/common/` and finds its
     decisions by *Scope* (WAY-21, WAY-150) does not find WAY-391; it reaches it only through the
     guidance, which names it.
   - Grade and scope. Minor. Outside the task's scope: remark 1 asks for the two lines of the
     guidance and nothing else, and a change of a decision's *Scope* is not what it carries.

## Declined to judge

- Rows of *Files of this kind* for `elements/common/foundation_source.py` and
  `elements/common/foundation_text.py`: the status of each (`copy` or `do not copy`) is a judgment
  the remark does not carry, and the template lets a file take no row until the guidelines are
  refreshed (`product-guidelines/coding/template.md:266-269`).
- Other parts of the-way that hold a module other scripts import and that *Applies to* does not
  name: the remark names one part, and I surveyed no other.
- The test of `shared-module-import-runs-nothing` reads the exemplar only, not the modules of
  `elements/common/`: it predates the request and the correction changes no rule and no invariant.
- A change that brings a product's first decision log, or one whose base holds the log in the
  earlier form: the length check then takes no decision, or every decision, for added, as the check
  of what holds a decision already did. That is the whole change, reviewed earlier, and no collision
  of the six decisions.
- The shortening of the twelve entries over a limit, WAY-134, WAY-150 and WAY-344 among them:
  another task, by the handoff.

## Checks

- `git rev-parse HEAD` — exit 0, `357965408b529da7d5965c6384c4883913ae1ddc`.
- `git diff 2ffff547..35796540`, `git log --oneline 2ffff547..35796540` — exit 0; one commit, one
  file, 2 insertions, 1 deletion.
- `git diff --check 2ffff547..35796540` — exit 0, no whitespace fault.
- `python -B elements/common/foundation_check.py` — exit 0, `0 errors`, 12 lines `listed:`, all of
  the length of a paragraph.
- `python -B gate/run_tests.py elements/common` — exit 0, 283 tests, OK.
- `python -B gate/run_tests.py product-guidelines` — exit 0, 14 tests, OK.
- `python -B gate/run_tests.py relation-model` — exit 0, 13 tests, OK (the test of the invariant the
  guidance names).
- Manual: from `elements/common/`, `python -B -c "import foundation_text"` and the same for
  `foundation_source`, each with an empty input — exit 0, nothing on either output.
- Probe in a scratch worktree of `35796540` (`python -B .runs/review-correction-1/probe.py`, exit 0),
  three variants of `foundations/decisions.md`, each run through that worktree's
  `elements/common/foundation_check.py`:
  - `moved` — the entry of WAY-256 moved word for word to stand before WAY-12: exit 0, `0 errors`,
    `foundations/decisions.md:756: listed: `WAY-256`: paragraph 1 of its binding sentences has 301
    words (at most 300)`;
  - `switch` — one word added to WAY-256, run with `--skip-test-citations`: exit 1,
    `foundations/decisions.md:3454: `WAY-256` is added or changed by this change: paragraph 1 of its
    binding sentences has 302 words (at most 300)`;
  - `lost_sentence` — WAY-344 without its last binding sentence: exit 1, `` `WAY-344` is added or
    changed by this change: paragraph 1 of its binding sentences has 7 sentences (at most 3) and 718
    words (at most 300)``, with two errors of lines `decision:` in `process-audit/test_audit_count.py`
    whose quotation was the removed sentence.
- Not run: the product's full gate (as handed); `python -B gate/run_tests.py agent-instructions`
  (the author ran it; no test of that directory reads the changed lines, and the range changes no
  Python file); the linter and the formatter (no Python file changed).

## Reaches beyond the dispatch

- `guidelines/coding.md` and `guidelines/coding-shared-module.md`, each whole: the file the
  correction changes and its index.
- `product-guidelines/template.md`, `product-guidelines/coding/template.md` and
  `product-guidelines/reading.md`, each whole: the form of a guidelines file and how one is selected.
- WAY-391 whole (`foundations/decisions.md:11166-11184`) and the invariant
  `shared-module-import-runs-nothing` whole (`foundations/invariants.md:501-509`): the decision and
  the invariant the changed file names.
- WAY-21 whole (`foundations/decisions.md:900-927`): what a *Scope* names, for finding 3; the
  *Scope* lines and headings of WAY-386 to WAY-390, by a search, for the same finding.
- WAY-12 whole (`foundations/decisions.md:756-812`): the pattern the length check follows.
- The entry `elements-common` of `foundations/part_map.md:65-80` whole: that the part exists and
  what it holds.
- `elements/common/decision_index.py:158-159` and `elements/common/test_guidelines_place.py:1-80`,
  by a search: how the index gives paragraphs, and what that test reads of the guidelines.
- `task-cycle/remarks_check.py:1-70`: how this report's sections are read.

## Working copies

- `.runs/review-correction-1/` in the task's worktree held the outputs of the checks, the probe
  script and a detached worktree of `35796540` at `.runs/review-correction-1/wt`. The worktree was
  removed with `git worktree remove --force` and `git worktree prune`, and the directory was removed
  after this report was written.
- One file went outside that directory by my mistake: `.runs/review-correction-1-headings.txt`,
  written directly under the ignored `.runs/` by the first search of headings. I removed it in the
  next command. No tracked file, index or branch of the reviewed worktree changed
  (`git status --short` empty after the checks).
- `.runs/fc_final.txt` stands directly under the ignored `.runs/` and is not mine: it was written at
  12:13:14 on 2026-11-20, before my first command, and I left it in place.

## Unread material

- The six decisions of remark 2: each read whole; nothing of them stayed unread.
- WAY-05: read whole.
- `elements/common/foundation_check.py`: not whole. Read: lines 1-155, 300-402, 685-805 and
  1048-1112, and its diff over `1b6fe1c1..35796540`. `elements/common/foundation_text.py`: whole.
- `elements/common/test_foundation_check.py`: not read, but for a search of the messages of a
  missing field.
- `elements/decisions/template.md`: only its diff over `1b6fe1c1..35796540` and lines 133-134.
- The task document, the remarks, the author's report, `task-cycle/review/SKILL.md` and
  `task-cycle/review/fix.md`: each whole.

## Searches not found or unclear

- Remark 2 says WAY-19 "gives the rule of a paragraph for a part of another question"; WAY-19 read whole holds no rule of a paragraph, which is WAY-05's, and the template `elements/decisions/template.md:133` cites WAY-19 only for what such a part is.
- Looked for a test that reads `guidelines/coding-shared-module.md` or the *Applies to* of a real guidelines file other than through `elements/common/foundation_check.py`, by a search of `Applies to`, `Where in code` and `shared-module` in the Python files; found none.
