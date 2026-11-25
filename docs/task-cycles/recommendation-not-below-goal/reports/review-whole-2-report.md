FAIL 42298f2a81d8d4600b7a3769ab5ab6795510f0f6

# Review of the whole change, second dispatch — recommendation-not-below-goal

Range: `301e4eae1111310ccd80e466f62ea01838b9ff88..42298f2a81d8d4600b7a3769ab5ab6795510f0f6`, two
commits (`7c2502a7`, the author's change; `42298f2a`, a fix of an earlier review's findings). `git
rev-parse HEAD` in the worktree gives `42298f2a81d8d4600b7a3769ab5ab6795510f0f6`, the head given. One
author, no plan, no slices: no blocking finding comes from a slice. Files changed:
`elements/common/critique/prepare.md`, `elements/common/way_of_working.md`, `foundations/decisions.md`
(WAY-113 only).

## Findings

### Important

**I1 — The new rule "where no way reaches the goal, the question recommends none" collides with
WAY-166, and the technology step that rests on a recommendation for every choice, with no precedence
recorded (WAY-25).**

Place: `foundations/decisions.md:1595-1597` (WAY-113, new third paragraph: "A way that gives less
stands among the ways [...] and is never recommended; where no way reaches the goal, the question
recommends none and says so") and its copy `elements/common/way_of_working.md:36-38`; against
`foundations/decisions.md:4847-4849` (WAY-166 binding: "Where no option can be used by an agent, the
recommendation goes by the other consequences and says in one sentence that no option lets an agent
check the running product this way"), `:4864-4866` (WAY-166 *violates*: "on a host where no option
can be used by an agent, the step recommends nothing"), `:4873-4875` (WAY-166 *Rationale*: "the human
is owed a recommendation (WAY-113)"), `:4886-4888` (WAY-166 *Rejected*: "the step recommending nothing
where no option can be used by an agent — an exception to WAY-113, and the human answers with no
hint"), and the copies of WAY-166 in `project-level/technology/settle.md:34-38` and
`project-level/definition_template.md:242-248`.

What is wrong: the human chose that the rule covers every goal the material sets (task, question 1:
"każdy cel, który materiał stawia pracy") — a task's need included. The step that settles technology
also runs at a task document (WAY-267), and a task's need can itself be that an agent checks the
running product, for example that an agent reads the product's logs (the deployment skill's item on
how to read the logs, WAY-139, sends such work to a task). In that run, where every option of the
logs is a panel only the human can read, WAY-166 and `settle.md` tell the agent to recommend by cost
and upkeep, and the new paragraph of WAY-113 tells it to recommend none, which WAY-166 names as its
own violation and its *Rejected* refuses by name as "an exception to WAY-113". Both decisions apply,
they pull opposite ways, and neither names the other `narrows` (WAY-113 *Relations*: none; WAY-166:
`derives from WAY-121 · narrows WAY-123`). WAY-166's *Rationale* also still says that WAY-113 owes the
human a recommendation, which the changed WAY-113 no longer says in this case.

The same new case reaches the rest of the technology step, which presumes a recommendation for every
choice: WAY-123 (`foundations/decisions.md:4171`, "each choice with its recommendation and the weak
point of the option recommended"), WAY-138 (index line: "tests the option it recommends for each
choice it settles"), `settle.md:39-41` (the risk tests run on "the option recommended for every
choice of the wave") and `settle.md:61-62` ("A human who answers "you choose" or "I do not know" takes
the recommendation"). Where no option of a choice reaches the definition's goal or measure of
success, or the task's need, the step's agent now has no recommendation to test and no answer for
"you choose", and no file says what it does instead. WAY-123 derives from WAY-113, so it may be read
under the new paragraph, but `settle.md` gives the agent no step for that case.

Why it matters: WAY-25 — "A collision between two decisions with no precedence recorded is never
settled silently by the agent that meets it"; the change must either record the precedence where what
the human accepted gives the outcome, or stop and ask. Merged as it stands, the head leaves every
agent of the technology step that meets this case with two binding decisions saying opposite things,
and each agent settles it its own way, which is the "case left unsaid" WAY-166's *Rejected* itself
refuses. WAY-33 requires each finding of the search to become a link, a change or a question before
the change is accepted; the author's first report judged "no collision", and the fix report asked
the human (author-fix-1-report.md, "I1 — not settled") but the head records nothing.

Evidence: the lines quoted above, read at head `42298f2a`; `grep -n "WAY-113" foundations/decisions.md`
finds the citation in WAY-166 at `:4875` and `:4887`.

Whether what the human accepted gives the outcome: the task's answers 1 and 2, read together
("każdy cel, który materiał stawia pracy"; "nigdy jako polecany"; not chosen: "polecany, gdy jego
słaby punkt mówi wprost, że schodzi poniżej celu"), point toward the goal rule prevailing where the
need is the agent's check, since WAY-166's one sentence "no option lets an agent check the running
product this way" beside a recommended option is exactly a way below the goal recommended with its
lack named. But WAY-166's *Rejected* refusing this very move was accepted by the human too, and no
passage of the task names WAY-166, the technology step or a goal that is an agent's check. I agree
with the author that the outcome is not given (WAY-25: "otherwise the agent stops and asks"), so the
fix needs the human's answer. My recommendation for that question, which differs from the author's
recommendation (a): the goal rule prevails only where the material's goal or need is itself that an
agent checks the running product, recorded as WAY-25 gives in the decision that prevails — WAY-113
names `narrows WAY-166` and its binding sentences state that area — with the copies in `settle.md`
and `definition_template.md` carrying the same area, and `settle.md` saying what the step does with a
choice that has no recommendation (the risk tests and "you choose"). Outside that area WAY-166 stays
as it is, since where the material sets no such goal no option falls below it. Weak point: it
overrides an approved refusal in WAY-166's *Rejected* ("the human answers with no hint") and costs
edits in four places (WAY-113, `settle.md` twice over, `definition_template.md`); the author's (a)
costs one relation, but in that one area it recommends a way below the goal with its lack named,
which is the way the human refused in question 2.

Contradiction: yes — WAY-166 (binding sentence, *Verification* "violates", *Rejected*), with no
precedence recorded under WAY-25.

### Minor

**M1 — `elements/common/critique/prepare.md:8-10`, within the task.** The added sentence leaves the
paragraph ragged: line 10 ("`elements/common/way_of_working.md`. Ask it to read the target in full")
is 70 characters between lines of 87–99. The fix re-wrapped the lines the change added in
`foundations/decisions.md` but not here. Polish only; the paragraph reads correctly.

**M2 — `foundations/decisions.md:1597-1600` and `elements/common/way_of_working.md:38-41`, within the
task, mandated by its *To do* 2.** The places where a goal held not worth its cost is settled name
"the goal of an independent task with the human in the same refinement". An agent that asks a
question of decision inside a task's cycle (for example in the foundation step, or an item of
*Needed from you* of a blocked request) has no refinement under way; the rule does not say that
there the question goes to the human through the cycle's own route (WAY-30, a blocked draft request).
The wording is the task's own ("cel zadania niezależnego u człowieka w tym samym doprecyzowaniu"), so
this is a gap the task mandates, named as such; the consequence is small, since WAY-30 and WAY-315
already stop a cycle that would change what the task settles.

## Against the task

- *To do* 1: met — `way_of_working.md:33-36` and WAY-113 `:1592-1595` name the three goals (a task's
  goal in a plan, the need in a task document, the goal and measure of success of a definition) and
  the model "feature by feature".
- *To do* 2: met in wording — a way below the goal stands with its lack on its own line and is never
  recommended; none recommended where no way reaches the goal, said so; the goal's cost asked as its
  own question of decision, also where no way reaches it, settled at the plan's owner, the
  definition's readiness approval (WAY-118) or with the human in the same refinement. Its reach into
  the technology step is I1.
- *To do* 3: met — `prepare.md:8-10`; `check.md` and `critique/SKILL.md` unchanged (`git diff --stat`
  names neither).
- Questions 1–4: answers 1, 2 and 4 carried into WAY-113's binding sentences, *Verification* and
  *Rationale*; their ways not chosen into *Rejected* (`:1704-1710`), faithful to the task's *Not
  chosen*. Answer 3 carried into `prepare.md`; its ways not chosen belong to row 2, which goes to an
  instruction file, so WAY-113's *Rejected* rightly does not take them (WAY-134).
- *Settlements to record*, row 1: written into WAY-113 (binding paragraph 3, *Verification*), the
  base's first two paragraphs unchanged in words (fix commit moved the new paragraph after them).
  Row 2: written into `prepare.md`, once, with no copy of the rule's content.
- *Out of scope*: no file of loop2 or its plan touched.
- *Decisions in play*: WAY-120 unchanged, as the task says.

## Structure the change leaves

`python -B task-cycle/change_file_sizes.py 301e4eae… 42298f2a…`: `prepare.md` 12→14, `way_of_working.md`
203→211, `decisions.md` 11891→11924. No code changed; the rule of size (`guidelines/coding.md`
"### Size of a function and a file", WAY-385, invariant `function-and-file-size`) covers the scripts
of the-way, so no test of it was run in worktrees and no structure finding follows. WAY-113's binding
part, counted from the file: paragraphs of 161, 154 and 162 words, 3, 2 and 3 sentences, 477 words in
all — within WAY-05's limits, as `foundation_check.py` reports.

## The author's own-work check

The first report named the coverage of every goal (question 1) and the goal's cost as its own
question (questions 2 and 4); its check, a reading of the paragraph against the answers, holds. The
change is weakest elsewhere — the decisions that already require a recommendation in a narrower area
(I1) — and that check would not catch it; the first report judged WAY-166 not to collide, the fix
report reversed that and asked the human. No walk through a running product applies: the change
alters no product behaviour.

## Declined to judge

- `product-guidelines/coding/new_tools.md:4`, `product-guidelines/styleguide/new_tools.md:4`,
  `product-guidelines/testing/new_tools.md:4` ("Give a recommendation and the weak point of the option
  recommended") restate WAY-123's form for tools of guidelines with no word on a question that
  recommends none — outside the task, which names only `way_of_working.md` and `prepare.md`, and its
  *Context* judged these rules of "the simplest and cheapest" not to collide; if the human's answer to
  I1 settles what a step does with a choice with no recommendation, these copies may follow it.
- `task-cycle/skill/request_template.md:380` (an item's recommendation "as "How a skill asks" gives
  it") — defers to the rule, so it takes the new case without change; nothing to judge in the task.

## Checks

| Command / method | Exit / result |
|---|---|
| `git rev-parse HEAD` | `42298f2a81d8d4600b7a3769ab5ab6795510f0f6`, the head given |
| `git diff 301e4eae..42298f2a`, `git log 301e4eae..42298f2a` | 0; 3 files, +49/−6, two commits |
| `python -B elements/common/foundation_check.py` | 0, `0 errors`; base resolved as `git merge-base HEAD origin/foundations` = `301e4eae`, so WAY-113 counts as changed and its limits were checked |
| `python -B instruction-files/check_instructions.py` (command of `installation/README.md`, from the root) | 0, `0 error, 0 warn, 5 info` |
| `python -B task-cycle/change_file_sizes.py 301e4eae… 42298f2a…` | 0 |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0, `checked: 344 files, 0 listed` |
| `python -B task-cycle/private_paths_check.py` (first without its argument) | 2, `the following arguments are required: TARGET` — wrong call of mine, not a check |
| `python -B task-cycle/private_paths_check.py .` | 1, lists fixtures of its own tests and of `tracked_private_paths_check.py`; none of the three changed files listed — not the invariant's check (the line above is), recorded for completeness |
| `python -B -c` count of words and sentences of WAY-113's binding paragraphs | 0; 161/3, 154/2, 162/3 words/sentences |
| `git diff 301e4eae..HEAD \| grep '^+' \| awk 'length($0)>101' \| wc -l` | 0 lines over 100 columns added |
| Manual: WAY-113 at head against the task's *To do*, questions, rows | as "Against the task" above |
| Manual: search of `WAY-113` and of "weak point" / "recommend" in `foundations/`, `project-level/`, `product-guidelines/`, `task-cycle/`, `elements/` | led to I1 and to Declined to judge |

Not run: the gate (WAY-160, the cycle's own run); no test file was changed and no test cites WAY-113
by a line `decision:` (`grep -rn "WAY-113" --include=test_*.py` — none found by the author; my search
of `WAY-113` over `*.md` and the foundation found no test either).

## Reaches beyond the dispatch

- `project-level/technology/settle.md:1-75` and `project-level/definition_template.md:234-263` — to
  quote the copies of WAY-166, WAY-123 and WAY-138 for I1.
- `elements/common/critique/SKILL.md`, `check.md`, `prepare.md` whole — the target of *To do* 3.
- `product-guidelines/coding/new_tools.md:1-7`, `task-cycle/skill/request_template.md:220-235,
  372-385` — restatements of the recommendation found by the search of "weak point".
- `elements/common/foundation_check.py:124-139` and its constants — to confirm which base it compares
  with.
- `installation/README.md:76-90` — the command of the instruction-file check.
- WAY-99 opened whole from its heading in the index — whether the new word "model" (`:1594`) needs a
  rename; the glossary's own entry "exemplar" uses "model" in the same sense, so no finding.

## Working copies

`.runs/review-whole-2/` in the worktree held only check outputs (`sections.txt`, `index.txt`, `fc.txt`,
`ci.txt`, `pp.txt`, `tpp.txt`); no worktree, clone or probe. Removed before returning. No probe is
needed for a finding: I1 rests on lines of the files at the head.

## Unread material

Decisions of the index of my selection read whole: 11 — WAY-113 (with *Rejected*), WAY-166, WAY-120,
WAY-123, WAY-174, WAY-25, WAY-33, WAY-35, WAY-118, WAY-134, WAY-99. Index: `decision_index.py` with
the sections "How skills write and read the foundation", "Accepting and applying decisions",
"Technology choices", "The running product", "Project definition", `--part elements-common`,
`--part decisions` and `--decision` 113, 166, 120, 35, 33, 123, 118, 25: 33 listed in full (the
other 22 read as index lines, binding sentences only), 69 by heading, run through.

- WAY-138, WAY-267, WAY-121: bear on I1 and were read as index lines (binding sentences) only, not
  whole; the binding sentence is what I1 cites.
- The derived decisions that name WAY-113 beyond those read whole (WAY-155 at `:5875`, WAY-374 at
  `:5991`, WAY-378 at `:6124`): read only the lines a search of `WAY-113` found; they cite "How a
  skill asks" for the form of a question and add no rule on what is recommended.
- Guidelines: none selected — the change writes no code and no test, so no file whose *Applies to*
  and *When to read* match (`guidelines/coding*.md`, `guidelines/testing.md` headers inspected).
- Invariants: read whole those whose *Part* names `every`, `elements-common` or `decisions` and bear
  on a Markdown change (`foundation-file-kinds`, `foundation-change-merge-route`,
  `repository-file-location`, `element-directory-contents`, `return-step-record`,
  `derived-file-content`, `ci-checking-commands`, `outbound-link-reach`, `tracked-file-private-paths`,
  `skill-rule-source`, `elements-pending-marker`, `own-foundation-check-report`, `generated-overview`,
  `skill-entry-points`, `guidelines-file-place`); the invariants of scripts and of other parts not
  read.
- Part map: entries `decisions`, `elements-common`, `project-level`, `task-cycle` and the tail
  (*External context*, *Files left out on purpose*) read; the other parts not read.

## Searches not found or unclear

- A passage of the task, its sources or *Context* that names WAY-166, the technology step, or a goal
  that is an agent's check of the running product: not found (read the task whole) — hence I1 goes to
  the human.
- A step of `project-level/technology/settle.md` for a choice with no option recommended (risk tests,
  the answer "you choose"): not found.
- A test that cites WAY-113 by a line `decision:`: not found.
