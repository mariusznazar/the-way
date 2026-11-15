# Handoff: the agent of the plan's foundation entries, task `decision-log-reading-index`

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator, which
answers your questions from the task, its sources, the foundation and the code; no answer is the
human's approval. You never ask the human. The cycle has one human contact, the request.

## Where you work, and your stage

- Worktree (your working directory): `the task's worktree`, branch
  `task/decision-log-reading-index`, base of this stage `21ecb627f885de438e2209d7ff5c137b1e1b9d83`.
  Nobody else writes in this worktree while you work.
- Your stage: the foundation entries of the plan, F1–F10, before any slice. Read
  `task-cycle/skill/foundation_step.md` whole (it is your stage's rule) and `task-cycle/change/SKILL.md`
  whole (how a change is made, checked, committed and reported; your dispatch takes none of its variant
  rows). For each decision you write or change follow `elements/decisions/skill/SKILL.md` (a skill the
  cycle's types cannot call: read it as a file, and the files it names when its steps come), `record-decision`
  being its name.
- Boundary: F1–F10 as the plan's *Foundation entries* below give them; no code, no test, no change of
  `elements/`, `task-cycle/`, `project-level/` or the part map (the slices make those). Commit your work
  in the commits below, by `git add <paths>` and never `git add -A`; commit messages in English in the
  imperative, in the manner of `git log`. Return before any review.
- Report: `.runs/task-cycles/decision-log-reading-index/reports/foundation-entries-report.md`, as your
  method gives the report, with the own-work check, the **Unread material** and **Searches not found or
  unclear** sections, and for each entry one sentence of its meaning in English and one in Polish (the
  task document's language), marked `row <n>`, `projected` or `the cycle's`.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a
clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own
directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never
in the system's temporary directory, in the scratch directory of a session or in the main checkout
of the repository. The screenshot that a screenshot tool, such as the Playwright server, saves by
itself under its session's directory is moved into the agent's directory and the original removed.
The files that a product's own tools and tests make by themselves are no working copy of the agent
and stay outside this rule. Before the agent returns, each time it returns, it removes its copy — a
worktree with `git worktree remove --force`, then `git worktree prune` — keeps in `reports/` beside
its report what the report needs, and states in the report where each copy stood and that it was
removed. Where a removal fails, the agent finishes all the same and names in the report the
remainder, with its full path and the reason it stayed.

Your directory for working copies: `.runs/foundation-entries/`.

## The task, the plan and the answers of step 4

- Frozen task (Polish; read whole): `.runs/task-cycles/decision-log-reading-index/task.md`. Its *To do*
  1–8, *Acceptance criteria*, questions 0–4 and the 7 rows of *Settlements to record* carry the meaning
  of F1–F9.
- The plan (read whole): `.runs/task-cycles/decision-log-reading-index/plan.md`. The section below is
  copied from it word for word; the file is its address.
- Trust boundary: yes (`task-cycle/cycle_measures.py`, a slice's concern, not yours). Irreversible
  operation: no. No spec; no reserved choice.
- Two facts the orchestrator checked in the log at your base: it holds 198 decisions (the task counted
  331 on an earlier commit); WAY-326 and WAY-347 are withdrawn, the rule of WAY-347 now being the second
  paragraph of WAY-339, so *Settlements to record* row 7 goes to WAY-339, as the plan's F7 gives; and
  WAY-287's binding sentence words the reviewer's reading "by title", which F8 brings into line.

## Foundation entries to read

Decisions by identifier, each whole (each entry runs to the next `###` heading): WAY-150, WAY-18,
WAY-21, WAY-339, WAY-287, WAY-05, WAY-12, WAY-02, WAY-07, WAY-19, WAY-33, WAY-52, WAY-134, WAY-344 — the
task's *Decisions in play* and the entries your own skill sends you to. For F10 read the heading and the
`- **Scope:**` lines of every entry of the log (the log is large; read the entries whole only where your
assignment of an entry to a section needs it). The invariants whose *Part* names `decisions` or `every`
and cite the log (the check `elements/common/foundation_check.py` holds the form), the part map's entry of
`decisions`, and `elements/decisions/template.md` whole.

## Two things the plan leaves to you

1. The sections of F10: choose 20–30 topics by what the entries are about — read off each entry's own
   question and *Scope*, never guessed from its number. A heading is a short noun phrase of the topic; its
   one sentence says what the section covers, so that a reader choosing sections for a piece of work can
   pick by the heading and the sentence alone. A topic that fits one section only should not be split;
   an entry that fits two stands where its question points most. Numbers are not renumbered; inside a
   section the entries keep their relative order; the section of withdrawn identifiers is not a topic and
   stays last and unchanged.
2. Verify the division yourself in your own directory before you commit it: compare each entry of the
   log at the commit before F10 with the same entry after it (its identifier, then its bytes), and run
   `python -B elements/common/foundation_check.py --skip-test-citations` after F1–F9 and after F10. The
   committed comparing script comes in Slice 2; do not write it.

## The plan's *Foundation entries* (copied word for word from `plan.md`)

## Foundation entries

| Entry | Kind | From | What depends on it |
|---|---|---|---|
| F1 — WAY-150: an agent that selects reads the index of its selection of decisions and opens whole only the decisions the work changes, goes against or proposes another answer to (that one with its rejected options), those the task or the work's source names and those whose binding sentences leave open what the work has to do; the reviewer of the whole change reads the index of its whole selection and states how many decisions it read whole | change of a decision's binding sentences, *Verification* examples, rationale and *Rejected* (the rejected "a separate maintained index" is taken in the form of an index made on demand, which does not drift; the maintained file stays rejected, as question 1 gives) | Settlements row 1; question 0 | Slices 3, 4 |
| F2 — WAY-150: the index is no file of the repository; a script of the-way writes on demand the index of the selected decisions — number, question, binding sentences, *Scope* | change of a decision (a paragraph of WAY-150) | Settlements row 2; question 1 | Slices 1, 3 |
| F3 — WAY-150: in a log with topical sections the agent picks the sections of the work's topics and reads the index of their decisions, runs through the questions of the decisions outside those sections whose *Scope* names a touched part, and opens those that point to a bearing on the work | change of a decision (a paragraph of WAY-150) | Settlements row 3; question 2 | Slices 1, 3, 4 |
| F4 — WAY-18: the log has topical sections, with the numbers unchanged; a new entry stands at the end of the section of its topic, and where none fits, in a new section at the end of the log, which the request names; "with no view generated from it" stays true, since the index is no file | change of a decision's binding sentences, examples, rationale and *Rejected* | Settlements row 4; question 3 | F10; Slices 2, 3, 4 |
| F5 — WAY-150: a decision whose sentence a test the work alters holds by a line `decision:` joins the selection and is read whole | change of a decision (a sentence of WAY-150) | Settlements row 5; *To do* 3 | Slice 3 |
| F6 — WAY-150: in a log without topical sections the selection stays by the product's parts, and the index takes the place of reading the decisions whole | change of a decision (a sentence of WAY-150) | Settlements row 6; *To do* 7 | Slices 1, 3 |
| F7 — WAY-339, its second paragraph (the successor of the withdrawn WAY-347): the measures of context use count, for each agent of the cycle, the bytes of the decision log and of the index that entered its context and how many times | change of a decision's paragraph and its examples | Settlements row 7; question 4 | Slice 5 |
| F8 — WAY-287: the item of the incomplete reading of the review of the whole change follows the reading F1 gives — a reviewer that did not read the index of its whole selection, or named a decision bearing on the change as unread — in place of the reading by title | change of a decision's binding sentence, examples and rationale, which follows from F1 | *To do* 4 ("from every place of the-way that describes it today"); consequence of F1 | Slice 4 |
| F9 — WAY-21: its rationale and *Rejected*, which refuse topics ("Topics cannot be derived from changed files"; "topics — cannot be derived from a change"), give the selection by topic beside the selection by *Scope*, which stays as the safeguard; the binding sentence does not change | change of a decision's rationale and *Rejected* only | *Decisions in play* (WAY-21); *To do* 7; question 2; *Acceptance criteria* | Slice 3 |
| F10 — the division of the-way's decision log into 20–30 topical sections, each with a heading and one sentence of what it covers, the entries' numbers and text unchanged | edit of the log's form; no entry's text changes | *To do* 5; question 3; F4 | Slices 1, 2 |

The agent of the foundation entries writes F1–F9 through `record-decision`, as the task's rows and
its *Decisions in play* give them, and F1, F2, F3, F5 and F6 in one change of WAY-150, each part
of another question a paragraph of its own as WAY-05 gives; it brings each changed decision's
*Verification* examples into line with its new sentences — WAY-150's "reports "40 read whole, 111
by title only"" and WAY-287's "ran through none of the other 111 by title" among them — so that
each stays held as WAY-12 gives, and runs `elements/common/foundation_check.py --skip-test-citations`
after them. The acceptance criterion names the rejected options of WAY-150, WAY-18 and WAY-21 that
the change takes in: the entries' *Rejected* and rationale say it, and the request names it.

Then it makes F10 as one commit of its own that changes only the order of the entries, the section
headings with their sentences and, where it has to, the log's opening paragraph; the list of
withdrawn identifiers stays last and unchanged. Each section is a heading `## <topic>` followed by
its one sentence; no section is named "Withdrawn identifiers". The assignment of each entry is read
off the entry's own question and *Scope* — its heading and its `- **Scope:**` lines — and never
guessed from its number; inside a section the entries keep their relative order. 20–30 sections
over 198 entries gives some 7–10 entries each. It checks its own division, in its directory for
working copies, by comparing each entry of the log before the commit with the same entry after it,
and runs the foundation check again. Its report gives the list of sections — heading, sentence,
number of entries and the numbers it holds — the commit of the division and the commit before it,
for Slice 2 and the request.

The edits of the files that restate the rules come after: the reading rule
(`elements/common/way_of_working.md`, "Reading the foundation"), the decisions template ("Where
entries go") and the two files of `project-level/lead/` that restate "whole selected entries" in
Slice 3; the reviewer's instruction (`task-cycle/review/SKILL.md`), the stage reports' paragraph of
`task-cycle/skill/SKILL.md` that holds WAY-326's rule, and the request template
(`task-cycle/skill/request_template.md`, item 14 and the lower part's **Foundation entries**) in
Slice 4; WAY-339's measure in `task-cycle/cycle_measures.py` in Slice 5.
