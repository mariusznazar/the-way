# Handoff — designer of the spec

## Delegation

The person who requested this cycle (Mariusz) delegated every intermediate choice to the cycle's
orchestrator. You answer to the orchestrator, never to the human, and you ask no human.

## Where you work

- Worktree, your working directory for every command and read:
  `C:/Storage/repos/the-way/.runs/worktrees/pr-description-schema`
- This is the-way working on itself, at the checkout above; there is no `.the-way`, and the-way's
  files are read from this worktree, never from another checkout. Skills named below are this
  repository's files, listed here by path.
- Target branch `foundations`, base `f45ca40`, task branch `task/pr-description-schema`. You make
  no commit and change no file of the repository. You write two files only, both ignored by Git:
  - the spec: `docs/task-cycles/pr-description-schema/spec.md`
  - your report: `docs/task-cycles/pr-description-schema/reports/designer.md`
- The full test run of the base is running in this worktree in the background: touch no tracked
  file.

## Your method and stage

Read `task-cycle/spec/SKILL.md` whole and follow it as the **designer**. Read each file it names
when the step that names it comes. Your boundary: you return with `questions`, `done` or
`reserved`, before any plan or code; you start no later stage.

## The task

Frozen task, read it whole: `docs/task-cycles/pr-description-schema/task.md`. It was copied from
the author's private notes on 2026-11-05, accepted there with `Status: ready for cycle`,
`Project relation: independent`. Its citations stand at `foundations` `f45ca40`, the base. It is
written in Polish; the request's collapsed block is therefore in Polish.

The task's *To do* 1–9, its answers under *Questions to settle* and its six rows of *Settlements to
record* are settled. They bind you; your spec does not reopen them. *Out of scope* holds: where
screenshots and other test artifacts live, and the weekly review of the archives' findings.

## Answers of step 4

- Trust boundary: no at the start. Where your design changes a file the part map names as one, say
  so in the spec, by file.
- Operation that cannot be undone: no.
- Open design choice: yes, the choices below.
- Reserved choice: none expected; the script is Python like every script of the-way. Return
  `reserved` only if your design would need a language, framework, library, store, login or place
  to run nothing settles.

## The choices this spec settles

1. **The English headings of the template** (the task's one *Questions carried to cycle*), in their
   fixed order and level, for the top part (To do 2, 3) and the archive (To do 5). *Checks* stays
   as a heading, since WAY-261 names it. Give the heading of the decision section, of the collapsed
   block, and of each archive section, the task's own sections' place included.
2. **Where the template stands and how it is pointed to.** To do 1 names step 13 of
   `task-cycle/skill/SKILL.md` (lines 390–425), the *Request handoff* section of
   `task-cycle/record_template.md` (163–191), `task-cycle/skill/correction.md:31`,
   `task-cycle/skill/foundation_step.md:15`, `task-cycle/skill/reserved_return.md:76` and `:90`, and
   the list in `agent-instructions/README.md:66-74`. Settle the template's path, and for each of
   these what it keeps, what moves into the template and what it points to instead; check
   `task-cycle/skill/blocked_finding.md` and every other file of `task-cycle/` that names what the
   request states, by a search, and say what each becomes. Under WAY-256 a template the cycle's
   step 13 reads stands in a file beside the skill or in a place WAY-35 gives; say which.
3. **The record's *Request handoff* section.** Say what it keeps once the template holds the
   request's content. It must not lose the "Process remarks" block: the nightly digest
   `C:\Storage\The Brain\The Brain\Notes\Areas\(A) Claude code\scripts\cycle_remarks_digest.py`
   cuts out every block of a committed record that starts with "Process remarks" (read its
   `extract_remark_blocks`, around line 240, for what counts as a block); and the test
   `project-level/test_plan_state_invariant.py:186` holds `## Request handoff` in its data — say
   whether that heading stays and what the test needs.
4. **The script of To do 9.** Its path and part, command and arguments, inputs (the description
   file; the task document or its language, if needed), what it reports as an error — the order of
   the headings, content or `none` in every section, the collapsed block in the task document's
   language — how it recognizes that block and that language mechanically and what it does not try
   to judge, its exit codes, its output, and its tests so that `python -B gate/run_tests.py` runs
   them (a test file in a directory of its own runs only once git tracks it). Say where the cycle
   runs it — before the request opens and again after a correction — and how the cycle "corrects
   the description while the script reports errors". Look at `task-cycle/cycle_stages.py` and
   `task-cycle/test_cycle_stages.py` for the house style of a cycle script. Say whether the script
   or the template is a surface under WAY-49; the part map's surfaces are at the end of
   `foundations/part_map.md`.
5. **What fills the decision section** (To do 3, 7, row 2, row 5). Each item To do 3 names comes
   from a place in the record or the reports; say from which, so that the orchestrator can fill the
   section and nothing waiting for a yes stays below it. In particular: what of the questions table
   counts as "a choice of the cycle beyond the task's content" — the table holds every micro choice,
   most of which settle only how to make what the task settles (see `SKILL.md:234-237`); which
   skipped steps and unrun checks; and how row 5's judgment by the orchestrator stands beside
   WAY-161, whose rationale warns against an orchestrator sorting findings — the findings stay in
   their lists in the archive with the reviewer's words, and none moves between kinds.
6. **The foundation entries.** Whether rows 1–6 enter as new decisions or as changes of existing
   ones, given that a decision holds one to three binding sentences
   (`elements/decisions/template.md`); which row each entry carries; and the full new text of
   WAY-114, WAY-134 and WAY-10 under row 4, their *Verification* and *Rejected* included (WAY-114's
   *Verification* today says "the request lists each entry it writes with one sentence of its
   meaning in Polish"). Say what the search of the whole foundation (WAY-33) is to look for: every
   entry that says what "the request lists", "names in its request" or "states" — WAY-03, WAY-49,
   WAY-51, WAY-140, WAY-161, WAY-162, WAY-163, WAY-164, WAY-219, WAY-261, WAY-269 among them — and
   whether each still holds once its item stands in the decision section or the archive.
7. **A blocked request, a request a reserved choice blocks, and a correction**, each on the same
   skeleton (the task's answer on blocked requests; `reserved_return.md`, `blocked_finding.md`,
   `correction.md`): what the first sentence and the decision section hold in each.
8. **The-way's own requests.** `agent-instructions/README.md` "Integrate into `foundations`" lists
   what a request to `foundations` holds, for every change of the-way, a cycle's or not. Say what
   that section becomes.

## What the design has to fit, for you to check, not a design

- The task's *Decisions in play* quotes the binding sentences of WAY-03, WAY-10, WAY-49, WAY-51,
  WAY-114, WAY-134, WAY-140, WAY-161, WAY-162, WAY-219, WAY-227, WAY-256, WAY-261 and WAY-269. Read
  each of them whole in `foundations/decisions.md`, from its `###` heading to the next, with its
  rationale and *Rejected*: a quoted sentence locates an entry, never replaces it.
- Read also, whole: WAY-14, WAY-35, WAY-36, WAY-107, WAY-126, WAY-135, WAY-148, WAY-158, WAY-160,
  WAY-163, WAY-164, WAY-260, WAY-268. Follow their *Relations* where your design needs them.
- The part map, `foundations/part_map.md`, whole (it is short): the parts `task-cycle`,
  `agent-instructions` and `decisions`, and the surfaces.
- The glossary, `foundations/glossary.md`, whole (short), for the words your headings use.
- The examples of today's descriptions: `gh pr view 66 --repo mariusznazar/the-way`, `gh pr view
  69 --repo mariusznazar/the-way`, `gh pr view 70 --repo mariusznazar/the-way`; loop2 is
  `mariusznazar/loop2`, private: `gh pr view 52 --repo mariusznazar/loop2` and `gh pr view 55
  --repo mariusznazar/loop2`. Read them for what goes wrong today (the task's *Need*), not as a
  pattern.
- The draft of the top part for loop2 #55 that Mariusz judged ("taki opis byłby dużo lepszy"), and
  the seven choices of the-way #66 rewritten in plain words, stand in the transcript of the
  refinement conversation, `C:\Users\Mariusz\.claude\projects\C--Storage-repos-the-way\d1b0591c-1681-4be5-8324-5e7e1fa1d4e3.jsonl`
  (about 2.5 MB of JSON lines). Search it for "#55" and "taki opis" rather than reading it whole;
  quote what you take from it in the spec, and treat it as the source of the rows' meaning, never
  as a wording the template must copy.

## Your report

Write `reports/designer.md` as your method gives it, with **Searches not found or unclear** — each
thing looked for and not found or unclear, or `none`. Return your status, the spec's path, a
one-line check result and the report's path.
