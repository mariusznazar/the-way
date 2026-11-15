PASS a3c97dff32f5341cee667eaa2619a18d96b1bdc3

# Review of the whole change — weak point in every decision question

Range `bfb2e109735b5fff98802b8be0ff3c43c799262a..a3c97df` (commits `a14b07f`, `a3c97df`); `git rev-parse HEAD`
in the worktree is `a3c97dff32f5341cee667eaa2619a18d96b1bdc3`, as dispatched. I read the full diff
(`git diff bfb2e10..a14b07f`, `git diff a14b07f..a3c97df`), the frozen task whole and the author's report whole.

Counts: blocking 0 · Minor 5 (all within the task) · out of scope 0.

## Against the task

*To do* 1–7, the rows of *Settlements to record* 1–8 and the answers to questions 1–9, each checked against the diff.

- *To do* 1 (WAY-113): met. First paragraph gives the ways, the cost of each with the cost of undoing in one word
  where nil, the recommendation and the weak point (anchored where the material gives one; for a shortcut it names
  the right way and why it is not recommended). The check-question exception is word for word as before. *Scope*
  gains `task-cycle`, `foundation-review`, `process-audit`, `product-guidelines`. *Verification*, *Rationale* and
  *Rejected* carry questions 2, 3, 7 (a, c) and 8 (a, c) with their kept costs. The Mega.DEV practice is named in
  *Rationale* with what was seen, as WAY-100 asks for a source a reader cannot open (row 3); `Based on: none` is
  right. The entry keeps three binding sentences in the first paragraph and two in the second, as
  `elements/decisions/template.md` gives.
- *To do* 2: met (`elements/common/way_of_working.md:27-31`, the same content as WAY-113's first paragraph). The
  extra bullet at `way_of_working.md:46-50` on the project definition is needed: without it that section would
  contradict WAY-113 after the change. Not a defect.
- *To do* 3 and rows 4–5: met in `task-cycle/skill/request_template.md:358-363` (part 2 gets the cost of undoing in one
  word where nil; part 3 gets the weak point in one sentence by pointer to "How a skill asks") and in both examples
  (`:397-406`, `:420-430`). Kind 2 and the row "A question from the foundation step" now point to the item parts.
- *To do* 4: every file on the task's list changed; the pointers read correctly. The author's extra edits
  (`product-guidelines/{coding,styleguide}/settle.md`, `project-level/task/skill/final_review.md`, WAY-155, WAY-174,
  WAY-378 with the relation `derives from WAY-113`) each restated the rule or pointed to it with a list, and the
  rewording keeps their meaning; I judge them right, and the link for WAY-378 is correct (the entry already named
  WAY-113 with no written link, WAY-33). My own greps over tracked Markdown for "ways open", "what each costs",
  "their cost", "ways/costs", "and a recommendation", "options ... cost" and "recommend" found only the places the
  author lists as left: `project-level/skill/delegated_mode.md:11` and `project-level/task/skill/orchestrated_mode.md:17`
  (pointers "where/as required by How a skill asks", the same case as the one the task leaves alone),
  `project-level/technology/*`, `definition_template.md`, `product-guidelines/*/new_tools.md` (WAY-123's special case,
  out of scope), and the agents' own design choices in `task-cycle/{spec,plan,change}`. I agree with each. No other text
  of the-way restates what a decision question gives.
- *To do* 5 and row 6: met (`way_of_working.md:175-177`); the value-question rule stays in the step.
- *To do* 6 and row 7: met in WAY-113's second paragraph, in `way_of_working.md`, and in
  `project-level/skill/rounds.md:8-18`; `elements/common/skill/definition_variant.md` and `task_variant.md` untouched,
  and they agree with the new rule (the three moves of `definition_variant.md:40-48`; the task's refinement keeps the old
  rule). See the Minor findings 3 and 4.
- *To do* 7 and row 8: met in `process-audit/SKILL.md:158-169` (rule), `:11-14` and `:259-263` (*Decided* beside
  *Weighed* and *Set aside*). The two rules "How often an issue comes back is material, never a priority" and "The cost
  of an occurrence is material, never a priority" are untouched. See Minor finding 1.
- Questions 1–9: each answer is carried; question 1 (no dependency, no merge) is respected — no change to
  `orchestrated_mode.md` and `SKILL.md` of the refinement.

Consistency of the changed texts with each other: WAY-113 *Verification*, "How a skill asks", the request template's
item parts, the audit's step 3 and the pointers all read the same rule. The weak point and the cost of undoing are
stated in full in two places (WAY-113 and "How a skill asks", the second required by *To do* 2), in one sentence in the
request template's part 3, and everywhere else by pointer. The change contradicts no untouched decision I read
(WAY-114, 123, 134, 155, 174, 287, 289, 313–315, 372, 374, 377, 378): WAY-114's "question only where the agent has no
recommendation" and WAY-123's own weak point are consistent with the new first paragraph.

Strongest argument against the change, tried and judged: that the always-present weak point lets a doubtful
recommendation pass because the agent finds its own argument weak. WAY-113's *Rationale* names that price, and the
exception of the check question applies only where the weak point is anchored in the material, so a weak point with no
anchor leaves the check question in place. I did not find a way the change makes the rule fail silently.

## Findings

### Critical

none

### Important

none

### Minor (all within the task)

1. `process-audit/SKILL.md:155-156` — the step reads the newest earlier note "only to see which matters the human weighed or
   set aside; say so beside a matter that comes again". The change adds a third outcome and a field *Decided* to the
   note (`:11-14`, `:261-263`) but this sentence still names two. A matter decided in an earlier session therefore comes
   again with no remark beside it, which the sentence is there to prevent. Fix: add "decided on a step" there. Why it
   matters: the audit would put a decided matter before the human as new. Evidence: grep for "set aside" in
   `process-audit/SKILL.md` gives lines 13, 156, 169, 261-264; only 155-156 was not updated.
2. `task-cycle/skill/request_template.md:424` (and `:400-402`) — the example items say "undoing it, nothing" for
   every way, including "Letting it through accepts that risk; undoing it, nothing" in an item whose own first
   sentences say the user "loses the change on the first day". The rule's purpose is to name the choice that cannot be
   taken back cheaply; the example shows the word on every way and thereby teaches writing it by rote, and for that
   way it is arguably untrue. Fix: let one way in an example carry a real cost of undoing (for instance the way that
   accepts the risk: "undoing it, a correction after users lose data"). Examples carry no binding force; the
   consequence I name is the copying of the rote word. Within the task (*To do* 3: the examples show it).
3. `foundations/decisions.md` WAY-113 *Verification*, `complies` (the line on "the rounds of a project definition"): it
   gives only an example of the implication move. The binding sentence, *violates* and the task (*To do* 6: "Verification
   uznaje takie pytanie przy definicji za zgodne") name both moves, the implication and the reason of a decision costly
   to reverse. A reader comparing an exchange where the reason of a costly decision is asked in the rounds finds no
   `complies` case for it. Fix: add the reason move to that line.
4. `project-level/skill/rounds.md:8-18` — (a) the list is headed "Four moves", though its fourth item ("I do not know")
   is a rule for an answer, which the author notes; (b) that item's text changed from "to a question of decision, give a
   recommendation, with what each way costs" to "ask as 'How a skill asks' gives a question of decision". The old
   instruction was what to do when the human says "I do not know" — give a recommendation; the new one says "ask", which
   a reader can take as asking the same question again. Fix: "to a question of decision, answer with a recommendation put
   as 'How a skill asks' gives it" and a heading that says "Two moves ... and one rule" or similar.
5. Wrapping leftovers after the rewording, cosmetic: `foundations/decisions.md` WAY-378 binding sentence (line "plain language
   as WAY-113 asks a decision; the" is short, then "full list and the critique"), WAY-174 *Verification* ("as a question of
   decision (WAY-113); it asks" short lines), and `project-level/lead/skill/route_changes.md:17-19` (a line of 106 characters
   where the file wraps at 100). No reader is misled.

### Declined to judge

- `task-cycle/skill/request_template.md` examples hold "undoing it, nothing" in the form the task asked for; their
  realism is finding 2, the form itself is not set aside.
- Whether a pointer from a skill's text to a file of another part (the new references from `process-audit/SKILL.md` to
  `elements/common/way_of_working.md`) must appear in the part map's *Depends on* of `process-audit` — the invariant
  `cross-part-imports` and WAY-299 govern Python imports, not text pointers; outside the task and no rule found.

## Checks run

- `git rev-parse HEAD` in the worktree → `a3c97dff32f5341cee667eaa2619a18d96b1bdc3` (matches).
- `python -B elements/common/foundation_check.py` → exit 0, `0 errors`.
- `python -B task-cycle/change_file_sizes.py bfb2e10… a3c97df` → exit 0; 20 files, +88 lines in all, the largest growth
  `foundations/decisions.md` +53, `process-audit/SKILL.md` +12, `elements/common/way_of_working.md` +9,
  `task-cycle/skill/request_template.md` +8. No code file changed, so the structure test of the size rule has no
  function or file to show; no growth of a function.
- Greps over tracked Markdown (and other files) for the phrases above: results as given under *To do* 4. `git grep`
  for `decision: WAY-113/123/155/174/378` and `WAY-113` in `*.py` → no match: no test holds these decisions' sentences.
- Focused gate runs (in the reviewed worktree, which they change in nothing; logs in `.runs/review-whole/`):
  `python -B gate/run_tests.py <directory>` for `task-cycle`, `project-level`, `process-audit`, `product-guidelines`,
  `instruction-files`, `elements/common`, `agent-instructions` → all exit 0 (`summary.log`).
- Invariants whose *Part* names `every` or a touched part (33, extract by script into `.runs/review-whole/inv.txt`,
  first sentence read): the ones that bear on Markdown text — `tracked-file-private-paths`, `outbound-link-reach`,
  `skill-entry-points`, `skill-rule-source`, `instruction-file-imports` — are not violated by the diff (no absolute path, link
  or `@` was added; no `SKILL.md` frontmatter changed).
- Not run: `python -B gate/run_tests.py` with no directory (the orchestrator's); `elements` and `foundation-review` as
  directories (the runner exits 1 for a directory with no test, as the author's report notes).

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-114, WAY-314, WAY-315 whole, WAY-100 whole, WAY-123 and WAY-174 (from the verification
  to *Rejected*), WAY-155 and WAY-378 whole: each bears on the rule changed (acceptance, refinement rule, adoption of a
  practice, the technology and guidelines skills' questions).
- `elements/decisions/template.md` lines 1-125 (the form of binding sentences, *Rationale* and *Rejected*) to judge the
  entry written.
- `elements/common/skill/definition_variant.md` step 4, `task_variant.md` step 4: to check they agree with the new rule
  for the project definition and the task.
- `foundations/part_map.md` entries `decisions`, `elements-common`, `project-level`, `task-cycle`, `foundation-review`,
  `process-audit`, `product-guidelines` (read whole): the touched parts.
- `process-audit/SKILL.md` lines 150-275 whole (the step the change reaches) and `foundation-review/with_the_human.md` whole.

## Working copies

`.runs/review-whole/` of the worktree holds only my index of decisions (`index.md`, `sections.md`), the extract of
invariants (`inv.txt`) and the test logs and `summary.log`. No worktree, clone or screenshot was made. They are files
of the ignored `.runs/` and stay in place; nothing else remains.

## Unread material

- Decisions of the index of my selection (sections "How skills write and read the foundation", "Project definition",
  "Task refinement and readiness", "The request and the human", "Process audit", "Technology choices", "Writing and
  approving guidelines", the parts `decisions`, `elements-common`, `foundation-review`, `process-audit`,
  `project-level`, `task-cycle`, `product-guidelines`, and `--decision` for WAY-113, 123, 100, 155, 174, 378: 49 listed in
  full, 140 by heading alone): **9 decisions read whole** — WAY-113, WAY-100, WAY-114, WAY-314, WAY-315, WAY-123, WAY-174,
  WAY-155 and WAY-378. The other 40 of the full list I read as the index gives them (question, binding sentences, *Scope*); none
  of them is changed or contradicted by the change as far as that reading shows, but I did not open their
  *Verification*, *Rationale* or *Rejected*. Those that bear most: WAY-134, WAY-287, WAY-289, WAY-374 and WAY-377 (they name
  question or item forms) — read in the index only. The 140 by heading: run through the questions; none points to a
  bearing on the change except those opened.
- The invariants named above: only their first sentence (extract), not whole; none rests on the changed text.
- The glossary: not read (the change uses no term with a glossary entry that I found; "weak point" is no glossary term).
- Guidelines: the-way has no product guidelines for these files; none read.
- `process-audit/SKILL.md` lines 1-149 and 275-end read in part only (the changed passages and their surroundings).
- The task's vault sources (data file of the review, notes of the Mega.DEV course): not opened; the task's rows carry
  what the change needed.

## Searches not found or unclear

- A test that holds a sentence of WAY-113, 123, 155, 174 or 378 by a line `decision:` — searched, none.
- A template file for the audit's note — none exists; the note's list stands in `process-audit/SKILL.md` step 4, where
  *Decided* was added; taken as the template the task names.
- Whether the part map treats a text pointer between parts as a dependency — only code imports are governed; unclear,
  and not a finding.
