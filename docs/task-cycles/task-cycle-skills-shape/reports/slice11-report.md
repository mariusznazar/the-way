# Slice 11 report — `implement-task` judged and rebuilt, with the change of WAY-125 in its handoffs

- **Status:** `done with concerns`. The concerns are listed under *Choices and doubts*: points 1–3
  (two fragments with several instructions that stay in `SKILL.md`, and the handoff sentence for
  the dispatches that fit no row of `make-change`'s table). None of them blocks the slice.
- **Commit:** `7369993885567d683ef7b7a8b08933318c21ed4d`, "Rebuild implement-task by its judgment: a
  file beside the skill for each route and stage that alone needs it (WAY-256, WAY-125)". It is on
  `task/task-cycle-skills-shape`, on top of the slice's base `a2456e5`. Not pushed. The worktree is
  clean.
- **Files changed** (`git diff --numstat a2456e5 HEAD`): `task-cycle/skill/SKILL.md` +47 / −109;
  new files `task-cycle/skill/plan_member.md` +11, `spec_review.md` +13, `planning.md` +36,
  `foundation_step.md` +25, `return_step.md` +16, `blocked_finding.md` +14, `correction.md` +18.
- **Method:** `make-change`, read whole from `.runs/the-way-base/task-cycle/change/SKILL.md`. I
  judged with the base copy's `maintain-instruction-files` (`SKILL.md`, `judging.md`,
  `kind_skill.md`, `tool_loading.md`), in the mode judge, for the kind skill. I applied the
  one-instruction exception of WAY-256 as changed in `40f0fd3` (plan, *Common*, point 1).

## Layout after the rebuild

The table of judgment has one row per fragment. Each file below is one level deep: no file beside
the skill names another file to read. `blocked_finding.md` names `task-cycle/cycle_stages.py`, but
only as a script to run. That is the same sentence as at the base, not a pointer to read.

```
task-cycle/skill/
  SKILL.md            frontmatter unchanged; the picture of the whole; steps 1–14 in order, each still
                      numbered; the rules that hold across the routes; the pointers
  plan_member.md      the plan member's check before its cycle starts      (step 1, a plan member)
  spec_review.md      the spec's review and the route judged again         (step 7, the spec route)
  planning.md         step 8 and what a slice's handoff carries             (the planning route)
  foundation_step.md  the foundation step                                   (its writer; the orchestrator on a question)
  return_step.md      what the return step compares and writes              (the return step's agent)
  blocked_finding.md  a blocking finding left after the review of its fix   (request blocked by a finding)
  correction.md       the correction after review                           (a correction session)
```

All paths in `SKILL.md` are root-relative (`task-cycle/skill/<file>.md`). Slices 7–10 used bare
file names instead. I chose root-relative paths because this skill names every other file of the-way
that way (`task-cycle/record_template.md`, `task-cycle/cycle_stages.py`,
`elements/common/way_of_working.md`). The entry point also tells the orchestrator to read "a file it
names under the same root", so a bare `planning.md` would be ambiguous there.

## (a) Table of judgment

Criterion in every row (WAY-257): when an agent needs the fragment, and whether it recognises that
moment when it comes. Lines are at `cf11541`. No session records were searched (plan, *Common*,
point 2). The ground is the decision or step of the cycle the fragment carries.

Readers of the skill:
- **The orchestrator.** It reads `SKILL.md` through its entry point. Its variants are the route
  (spec, one author or plan), with or without a move of the pin, a request that is ready or blocked,
  and the correction after review. Step 4 records the route. The task document says whether the pin
  moves and whether the task is a plan member. The status of a returning agent shows a blocked
  outcome. The input of the session shows a correction.
- **Stage agents that read a fragment of the skill:**
  - the writer of the foundation entries: the one author, or the agent of the plan's *Foundation
    entries*;
  - the agent of the return step.

| # | Fragment (`SKILL.md` at `cf11541`) | Needed when / recognised? | Verdict | Reason | Ground |
|---|---|---|---|---|---|
| 1 | `:1-4` frontmatter | every use / no moment | keep (unchanged) | the description is the trigger and the source of the entry point | WAY-127 |
| 2 | `:6-14` the picture of the whole | every use / no moment | keep | the picture of the whole stays in `SKILL.md` | WAY-256, WAY-125 |
| 3 | `:16-23` one human contact; when to stop early | every route, at any step / no moment | keep | rule of working across the steps | WAY-227 |
| 4 | `:27-35` step 1: the task document, its relation, a changed source | every cycle, at the start / no moment | keep | common to the routes | WAY-124, WAY-134 |
| 5 | `:36-41` step 1: a plan member's check before its cycle starts (about 4 instructions) | only for a plan member / yes — the task's `Project relation:` names it at step 1 | move → `plan_member.md`; pointer "Before a plan member's cycle starts, read `task-cycle/skill/plan_member.md` and follow it." | several instructions of one variant | WAY-144 |
| 6 | `:42-43` step 2: the product's `AGENTS.md`, pin against the gitlink, git and test rules | every cycle / no moment | keep | common | WAY-34 |
| 7 | `:43-60` step 2: the move of the pin (287 words) | only where the task moves the pin; later also at each reset and at the whole-change review / yes — the task names the commit | **keep** (departure from the rule's default — see *Choices*, point 1) | moving it would put `installation/README.md`, which the fragment tells the orchestrator to read twice, two levels deep. Plan *Common* point 5 does not allow that, and Slice 10 kept a fragment for the same reason. `installation/README.md:82` cites step 2 either way | WAY-34; WAY-129 (one level deep) |
| 8 | `:61-65` step 2: reading the foundation and guidelines | every cycle / no moment | keep | common; the selection of every handoff rests on it | WAY-150, WAY-213 |
| 9 | `:66-70` step 3: harness, methods, who reads what | every cycle / no moment | keep; its second sentence is **changed by the Goal** (WAY-125 as changed in `40f0fd3`) | the only change of meaning; see (d), lines 21–22 | WAY-125 |
| 10 | `:72-76` the cycle writes only in its worktree; the backlog exception | every route, at any step / no moment | keep | common | WAY-140, WAY-107 |
| 11 | `:80-94` step 4: the two questions | every cycle / no moment | keep | common | WAY-13, WAY-48 |
| 12 | `:95-106` step 4: an open design choice; one author or planning; the author's class | every cycle, at step 4 / no moment | keep | the route judgment is common to every route | WAY-135, WAY-136, WAY-229 |
| 13 | `:107-111` an effect outside the repository | when the task places human actions in the cycle, or when the cycle finds such an effect / partly — the found effect can come at any step | keep | a moment that comes anywhere cannot hang on a pointer at one step | WAY-140 |
| 14 | `:112-117` the branch, base, failing checks, frozen copy; "Where step 2 moved the pin, … already stand" | every cycle; the last sentence only with a pin move / yes | keep | the pin sentence is one instruction (WAY-256 exception) | WAY-34 |
| 15 | `:118-126` step 5: the record, `record_template.md`, reports, events | every cycle / no moment | keep | common | WAY-148, WAY-147 |
| 16 | `:128-137` the handoff paragraph | every dispatch / no moment | keep; **changed by the Goal**: the method by its path; reading the `SKILL.md` whole and a file when its step comes; the variant in the words of `make-change`'s table; the files of the foundation step and the return step in place of "the paragraph or step of this skill" | the Goal's change; see (d) | WAY-125, WAY-148 |
| 17 | `:139-144` what each agent reads; who reads the whole task | every dispatch / no moment | keep | common | WAY-150, WAY-213 |
| 18 | `:145-153` a slice's executor and reviewer: the selection; building a slice's handoff; current ranges (3 sentences, about 170 words) | only on the planning route, at step 8 (reviewing *Read*) and step 9 sub-step 2 / yes — the route is set at step 4 | move → `planning.md` (section "A slice's handoff"); pointer sentence in place; sub-step 2 now names `planning.md` beside "the handoff paragraph above" | several instructions of one route | WAY-148, WAY-150 |
| 19 | `:153-159` copy word for word; the whole-change reviewer selects; only you read `cycle.md` | every dispatch / no moment | keep | common | WAY-148, WAY-150 |
| 20 | `:161-168` waiting for an agent (one clause each for Codex and Claude Code) | every dispatch / no moment | keep | common; each harness clause is one instruction | WAY-148 |
| 21 | `:170-188` the return contract, statuses per method, `questions`, `blocked` | every return / no moment | keep | common; each method's status clause is one instruction | WAY-148, WAY-159 |
| 22 | `:190-196` advance on the short return; questions to you; go-aheads provisional | every route / no moment | keep | common | WAY-148, WAY-114 |
| 23 | `:200-203` only a design choice calls for a spec; both routes | every cycle / no moment | keep | the picture of the routes | WAY-135, WAY-136 |
| 24 | `:205-211` step 6: the designer and how its questions are answered | step 6 on the spec route; **and** every agent's `questions` on every route, which `:181-183` answers "as step 6 answers the designer's" / yes | keep | the way of answering questions is used by every route; moving it would hide "note the ways and the price of being wrong" and "Never widen the task" from routes without a spec | WAY-135, WAY-227 |
| 25 | `:212-220` step 7: the spec's review, its finding, the route again (about 10 instructions) | only on the spec route, after the designer returns `done` / yes — step 6 ends with that return | move → `spec_review.md`; step 7 stays numbered with the pointer "When the designer returns `done` with the spec, read `task-cycle/skill/spec_review.md` and follow it: …" | several instructions of one route | WAY-135, WAY-30, WAY-136 |
| 26 | `:221-236` step 8: the planner and the plan's review | only on the planning route / yes — chosen at step 4, or entered from a return for size | move → `planning.md`; step 8 stays numbered with its pointer | several instructions of one route | WAY-136, WAY-229, WAY-160, WAY-62 |
| 27 | `:238-245` an agent that returns an open design choice | when an agent returns `returned` with a choice / yes — but its sentence "A choice of how to make … you enter it in the questions table" serves every agent's choice on every route | keep | a common sentence stands mid-paragraph; `correction` cites "the recovery" as a whole | WAY-135 |
| 28 | `:247-251` a one-author change that proves too large | only on the one-author route, on a return for size / yes | keep | `:253` says "returns the same way", so the paragraph is the referent of the next one; moving either breaks the chain | WAY-136 |
| 29 | `:253-255` a slice that proves too large (3 instructions) | only on the planning route / yes | keep (doubt, *Choices* point 2) | "the same way" refers to row 28; in `planning.md` it would dangle | WAY-136 |
| 30 | `:259-277` the foundation step | its writer, at the start of the writing — the one author with its code, the agent of the plan's *Foundation entries*, and the return step's agent, which "writes as the foundation step writes" / yes, the handoff names it. The orchestrator: only when a writer returns `blocked` with a question, and at step 7 for a finding that the spec contradicts a decision / yes — both are events it meets | move → `foundation_step.md` (the carried question: in a file the handoff names); pointer at its place naming both kinds of reader. Two rewordings with no change of meaning: "you open" → "the orchestrator opens", and "step 13" → "step 13 of `implement-task`", since the reader is now the writer agent | its writer needs nothing else of the skill. Base: a ~320-word paragraph inside a 6 605-word file, whose "you" addressed the orchestrator. The orchestrator's handling of a `blocked` return stays in `:184-188` | WAY-134, WAY-126, WAY-30, WAY-25, WAY-125 |
| 31 | `:279-287` step 9: one author | the one-author route / yes | keep | it cites sub-step 2 of the planned route for the class rules (row 32); a several-instruction fragment of one route, kept with row 32 | WAY-136, WAY-229 |
| 32 | `:288-330` step 9: the planned route, sub-steps 1–5 (616 words) | only on the planning route / yes | **keep** (doubt, *Choices* point 1; proposal (b) 1) | the one-author bullet takes from its sub-step 2 the rules common to both routes: the harness's closest model, `same` and `strongest` as one class, a harness that cannot choose. Moving the bullet would take those rules from the one-author route | WAY-136, WAY-229, WAY-159 |
| 33 | `:332-343` the review of the whole change | every route / no moment | keep | common; the plan insets are clauses inside its sentences | WAY-136, WAY-164, WAY-158 |
| 34 | `:344-348` step 10, the gate | every route / no moment | keep | common | WAY-160, WAY-159 |
| 35 | `:349-350` and `:361-364` step 11: who takes the return step; its review; the record | every route / no moment | keep; pointer "What it compares and writes stands in `task-cycle/skill/return_step.md`, which its handoff names." | the orchestrator's part of the step | WAY-229, WAY-11 |
| 36 | `:350-361` step 11: what the return step compares and writes (198 words) | only the agent of the return step / yes, the handoff names it (the carried question: in a file). The orchestrator does not apply it | move → `return_step.md`, with a one-line note saying that "It" is that agent | the content is the agent's; the orchestrator builds no handoff from it | WAY-11, WAY-36 |
| 37 | `:368-373` who reviews; the reviewer alone grades | every review / no moment | keep | common | WAY-161, WAY-220, WAY-221 |
| 38 | `:375-378` `PASS`; Minor and out-of-scope findings | every review / no moment | keep | common | WAY-161 |
| 39 | `:380-389` `FAIL`: one fix, one review of it, classes | every `FAIL` on every route / yes | keep | common to every review's failure | WAY-162, WAY-229 |
| 40 | `:391-398` a blocking finding remains after its fix (about 8 instructions) | only when the review of a fix fails again / yes — the review's first line | move → `blocked_finding.md`; pointer keeps "When a blocking finding remains after the review of its fix — in any of these reviews, a slice's included —". Rewording in the file with no change of meaning: "in any of these reviews" → "in any of the cycle's code reviews" | several instructions of one variant (a request blocked by a finding) | WAY-162, WAY-163 |
| 41 | `:402-419` step 12 | every route / no moment | keep | common; the blocked and human-action clauses are one instruction each | WAY-148 |
| 42 | `:420-445` step 13, the request | every route / no moment | keep | common; its blocked sentences are also named by step 9 sub-step 4 for a failed retry, so they stay where both reach them | WAY-134, WAY-161, WAY-162, WAY-163 |
| 43 | `:446-448` step 14 | every route / no moment | keep | common | WAY-148 |
| 44 | `:452-464` the correction after review | only in a correction session / yes — its input is a link to the request or to a comment of remarks | move → `correction.md`; the heading stays, with "When your input is a link to a request, or to a comment holding the human's remarks, read `task-cycle/skill/correction.md` and follow it." Rewording with no change of meaning: "the recovery above" → "the recovery "Design and execution choice" gives" | one variant; several instructions | WAY-162, WAY-163 |
| 45 | `task-cycle/record_template.md` (1 901 words; its **place** only) | the orchestrator, at step 5 and while it fills the record / yes — step 5 names it | keep where it stands, named at step 5 | it is read at the one step that names it, one level deep. Its **content was not judged** (plan, *Goal*). It lies outside `task-cycle/skill/`, which this slice does not change | WAY-148 |

## (b) "Remove" and "reword" proposals (no edit)

No session records were searched, so neither proposal rests on a mistake that was seen. Neither
proposal is a condition of "When to remove a rule". By "When to add a rule", each is listed as **not
recommended** unless the orchestrator takes the cost of the kept fragment as its ground.

1. **Reword step 9** so that the planned route can leave `SKILL.md` (row 32, 616 words that the
   one-author route reads without need). State the class rules once, in the one-author bullet or in
   a sentence common to step 9: the harness's closest model, `same` and `strongest` as one class
   where yours is the strongest, and a harness that cannot choose a model. Then move the Plan bullet
   with its sub-steps into `planning.md`. Recommended wording of the common sentence: "Each author
   and executor runs on the harness's model closest to its class, recorded in its row; where yours
   is the strongest, `same` and `strongest` are one class; where the harness cannot choose a model,
   dispatch as it allows and record that the class was not applied." Ground: a cost, about 616 words
   per one-author cycle. Carried decision: WAY-229.
2. **Let the pin move leave `SKILL.md`** (row 7, 287 words read by every cycle that does not move
   the pin). This needs one of two changes:
   - the step 2 pointer names `installation/README.md` beside `pin_move.md`, so that neither file
     beside the skill points further; or
   - the series settles that a beside-file naming a file of the-way outside the skill is not a
     second level.

   Ground: a cost. Both are changes of text this slice cannot make (plan, *Common*, point 5).

## (c) Words read before and after

Commands (in the worktree):
- `git show cf11541:task-cycle/skill/SKILL.md | wc -w` → 6605
- `wc -w task-cycle/record_template.md` → 1901
- `git show cf11541:task-cycle/skill/SKILL.md | sed -n '259,277p' | wc -w` → 318 (the foundation
  paragraph)
- `git show cf11541:task-cycle/skill/SKILL.md | sed -n '349,364p' | wc -w` → 254 (step 11)
- `cd task-cycle/skill && wc -w SKILL.md plan_member.md spec_review.md planning.md foundation_step.md return_step.md blocked_finding.md correction.md`
  → 5498, 113, 169, 454, 376, 217, 175, 235

**The orchestrator.** Every row below adds `record_template.md` (1 901 words, read at step 5), both
before and after.

| Variant | Before | After |
|---|---|---|
| one author, no move of the pin or with one, request ready | 6605 | 5498 |
| spec, then one author | 6605 | 5498 + 169 = 5667 |
| planning (with or without a spec before it) | 6605 | 5498 + 454 = 5952 (+169 after a spec = 6121) |
| the task is a plan member | as its route | + 113 |
| a writer returns `blocked` with a question, or step 7 meets a finding that the spec contradicts a decision | as its route | + 376 |
| request blocked by a finding left after its fix | as its route | + 175 |
| correction session | 6605 | 5498 + 235 = 5733, plus the route files its repeated work names |

A move of the pin adds nothing to the "after" figures: it stays in `SKILL.md` (row 7).

**Stage agents that read a fragment of the skill.**

| Agent | Before | After |
|---|---|---|
| writer of the foundation entries (one author's start, the plan's *Foundation entries*) | the paragraph, 318 words, found inside a 6 605-word file its handoff pointed into | `foundation_step.md`, 376 |
| agent of the return step | step 11, 254 words, inside the same file; its "as the foundation step writes" sent it to the paragraph too (318) | `return_step.md` 217 + `foundation_step.md` 376 = 593 |

The two stage files carry more words than the bare paragraphs because each adds a heading and a note
on who reads it. They spare their agent the opening of `SKILL.md`, with every instruction addressed
to the orchestrator.

## (d) Sentence comparison

Commands, all exit code 0:

```text
git show cf11541:task-cycle/skill/SKILL.md | tr -d '\r' | tr '\n' ' ' | tr -s ' ' | sed 's/\([.!?]\) /\1\n/g' | sort > .runs/task-cycles/task-cycle-skills-shape/reports/slice11-before.txt
cat task-cycle/skill/*.md | tr -d '\r' | tr '\n' ' ' | tr -s ' ' | sed 's/\([.!?]\) /\1\n/g' | sort > .runs/task-cycles/task-cycle-skills-shape/reports/slice11-after.txt
comm -3 .runs/task-cycles/task-cycle-skills-shape/reports/slice11-before.txt .runs/task-cycles/task-cycle-skills-shape/reports/slice11-after.txt > .runs/task-cycles/task-cycle-skills-shape/reports/slice11-comm.txt
```

The output has 42 lines (`reports/slice11-comm.txt`). Lines with a leading tab are found only after
the rebuild. Every moved sentence that does not appear below stands word for word in its new file.

- **Headings and notes of the new files** — added text, no rule:
  - "It" below is that agent. — row 36;
  - `# A blocking finding that remains Read under …` — row 40;
  - `# A plan member's cycle Read at step 1 …` — row 5;
  - `# Correction after review Read when the input …` — row 44;
  - `# The foundation step Read by the agent …` — row 30;
  - `# The planning route Step 8 …` — row 26;
  - `# The return step Read by the agent …` — row 36;
  - `# The review of the spec Step 7 …` — row 25.
- **Moved sentences merged with a heading by the pipeline** — the same sentence in a new file:
  - after `## A slice's handoff A slice's executor gets …`, before `A slice's executor gets …` — row 18;
  - after `## The planner and the review of the plan Only on the planning route, dispatch …`, before
    `Only on the planning route, dispatch …` — row 26;
  - after `The foundation step writes the entries … names.`, before
    `## Execute, verify and review The foundation step writes …` — row 30;
  - after `Take a link to the request …`, before `## Correction after review Take a link …` — row 44;
  - before `When a blocking finding remains … do not rule on the finding.`, after the same sentence with
    "in any of the cycle's code reviews" — row 40, a rewording with no change of meaning.
- **Pointer sentences:**
  - `## Correction after review When your input is a link …` — row 44;
  - `## Execute, verify and review The foundation step writes …, as task-cycle/skill/foundation_step.md gives: …` — row 30;
  - `Read it yourself when an agent returns blocked …` — row 30;
  - `Before a plan member's cycle starts, read …plan_member.md…` — row 5;
  - `Only on the planning route, read …planning.md…` — row 26;
  - `When the designer returns done with the spec, read …spec_review.md…` — row 25;
  - `What a slice's executor and the reviewer of a slice get stands in …planning.md…` — row 18;
  - `What it compares and writes stands in …return_step.md…` — row 35;
  - `When a blocking finding remains … read …blocked_finding.md…` — row 40;
  - sub-step 2: "as the handoff paragraph above gives" → "as the handoff paragraph above and
    `task-cycle/skill/planning.md` give" — row 18.
- **Rewordings with no change of meaning:**
  - "follows the recovery above" → "follows the recovery "Design and execution choice" gives" — row 44;
  - "and you open the blocked draft request …, as step 13 gives" → "and the orchestrator opens …, as
    step 13 of `implement-task` gives" — row 30.
- **The Goal's change of meaning**, in step 3 and the handoff paragraph and nothing else:
  - step 3: "Each stage agent reads the method of its stage, and what it names, whole; …" became
    "Each stage agent reads the `SKILL.md` of its stage's method whole, and a file the method names,
    one beside that `SKILL.md` included, only when the step or variant that names the file comes; …";
  - the handoff: "The handoff gives …, the method, …" became "…, the method of the stage by the path
    of its `SKILL.md` in the pinned the-way, …";
  - the handoff, new: "The agent reads that `SKILL.md` whole, and a file it names … only when the step
    or variant that names the file comes (WAY-125); no handoff tells it to read at the start every
    file its method names.";
  - the handoff, new: "Where that `SKILL.md` opens with a table of variants, the handoff names the
    agent's variant in the words of its row: …", and "The agent of the plan's *Foundation entries*
    and a fresh agent of the return step take none of its rows, and their handoff names their stage
    instead." (*Choices* point 3);
  - the handoff: "For the foundation step and the return step, it names the paragraph or step of
    this skill that holds that stage, which the agent reads whole, with the element skills it names."
    became "For the foundation step, the handoff names `task-cycle/skill/foundation_step.md`, and for
    the return step `task-cycle/skill/return_step.md` with it, …; the agent reads each whole, and the
    skill of an element when it writes an entry of that element." (*Choices* point 4).

Nothing printed is left unaccounted for, and no rule sentence was dropped.

## (e) Contradictions

I compared the rebuilt skill with the four stage skills in the worktree: their `SKILL.md` and the
files beside them where the dispatches meet them. I also used the reports of Slices 7–10.

- **None new.** Statuses (`:170-188` at the base) match all four. The designer's `done` (step 6),
  which opens `spec_review.md`, matches `write-spec` section 4. The planner's return of a design
  choice ("continue at step 6") matches `plan-task` step 2. The fix gets the findings file and the
  correction gets "the remarks in place of a findings file", which matches `review-change/fix.md`.
- **Carried, not mine to change:** `review-change`'s return names no one-line check result against
  `:170-172` and WAY-148 (Slice 10, (e)). `implement-task`'s text is kept as it is.
- **The gap Slice 7 found, now named in `implement-task`:** the dispatch of the plan's *Foundation
  entries*, and a fresh agent of the return step, fit no row of `make-change`'s table ("Your
  dispatch says which of these you make"). The handoff paragraph now says that their handoff names
  their stage instead. `make-change`'s table is unchanged (outside this slice). The one author
  resumed for the return step stays in "the whole change as the one author".
- **Stage skills with no table of variants.** Only `make-change` opens step 1 with a table of
  variants. `write-spec`, `plan-task` and `review-change` name their files beside the skill at steps
  (`design.md` and `review.md`; `too_large.md`; `whole_change.md` and `fix.md`), with conditions
  the agent meets from its dispatch: designer or reviewer, a return for size, the review of the whole
  change or of a fix. So the handoffs need no variant words for them.

## Checks (command and exit code)

- **Sentence comparison** (above): exit 0 for each command; 42 lines, all accounted for.
- **Each file named in `SKILL.md`:** `for f in plan_member spec_review planning foundation_step return_step blocked_finding correction; do grep -n "$f.md" task-cycle/skill/SKILL.md; done`
  → exit 0 for each:
  - `plan_member.md` at step 1, line 36;
  - `spec_review.md` at step 7, line 212;
  - `planning.md` at the selection paragraph line 154, step 8 line 214 and step 9 sub-step 2 line 264;
  - `foundation_step.md` in the handoff paragraph line 138 and at the foundation step line 238;
  - `return_step.md` in the handoff paragraph line 139 and at step 11 line 316;
  - `blocked_finding.md` at "The end of a code review", line 347;
  - `correction.md` at "Correction after review", line 402.

  The line numbers are those of the commit.
- **`ls task-cycle/skill/`:** exactly `SKILL.md` and the seven files it names.
- **Frontmatter:** `git diff cf11541 -- task-cycle/skill/SKILL.md` — the first hunk starts at line
  33, so lines 1–4 are unchanged.
- **`python -B agent-instructions/skill_entry_points.py`:** "entry points are current", exit 0
  (run again after the last edit).
- **No private links:** `grep -rn -E "Storage|The Brain|_zadania|Notes/" task-cycle/skill/` printed
  nothing, exit 1 (no match).
- **Tests:** `python -B gate/run_tests.py task-cycle` → 41 tests OK, exit 0. Output in
  `reports/slice11-gate-task-cycle.log`.
- **Whitespace:** `git diff --check` printed nothing, exit 0.
- **"whole":** `grep -n -i "whole" task-cycle/skill/*.md` → exit 0. Every hit about reading:
  - `:64` (step 3) and `:128` (handoff) say the `SKILL.md` is read whole and a file "only when the
    step or variant that names the file comes";
  - `:140` is "the agent reads each whole", about the two files of this skill its handoff names;
  - the rest are "the whole change", "the whole frozen task", "the whole foundation" (search) and
    "each whole" (guideline files).

  No sentence tells a stage agent to read at the start everything its method names.
- **Variant words:** `grep -rn "<variant>" task-cycle/skill/` for each of the four rows of
  `make-change`'s table → exit 0 each, at `SKILL.md:132-135`, the handoff paragraph:
  - "the whole change as the one author";
  - "a slice, or the retry of a slice";
  - "the fix of a review's findings";
  - "a correction for the human's remarks".
- **Steps:** `grep -n -E "^[0-9]+\. " task-cycle/skill/SKILL.md` → steps 1–14 in order, exit 0.
- **Not run:** the whole `gate/run_tests.py` (the orchestrator's run). No test was written: the
  slice holds no code (plan, *Common*, point 6).

## Own-work check

- **Requirement most likely missed:** acceptance criterion 2 — every fragment stands after the
  rebuild in `SKILL.md`, or in a file beside it that the step or variant needing it names.
- **Check:** the sentence comparison, plus the pointer greps above, plus a read of each moved
  fragment's references. Do "step 6", "step 13", "the same way", "above", "these reviews" and "you"
  still resolve for the reader of the new file?
- **What it showed:**
  - three references would have dangled ("the recovery above", "these reviews", "you open"); each
    is reworded with no change of meaning (rows 30, 40, 44);
  - one would have dangled and made me keep a fragment instead ("the same way", rows 28–29);
  - one would have taken a common rule from another route and made me keep a fragment ("as step 6
    answers the designer's", row 24; "as sub-step 2 of the planned route gives", rows 31–32).

## Reaches beyond the dispatch

- `git show --stat 40f0fd3` — to see which entries the foundation commit changed.
- `instruction-files/kind_skill.md:1-30` in the worktree — to read the one-instruction exception as
  Slice 1 wrote it. I applied it from the plan and WAY-256, not from that file.
- `.claude/skills/the-way-implement-task/SKILL.md` — to see how the entry point says when the
  orchestrator reads a file the skill names. That led to root-relative paths.
- `grep -rn record_template` — to confirm that only step 5 names `record_template.md`.

I did not open the cycle record.

## Choices and doubts

1. **Two fragments with several instructions of one variant stay in `SKILL.md`** (rows 7 and 32).
   - **Row 7, the pin move.** It names `installation/README.md`, and a file beside the skill would
     make that a second level.
   - **Row 32, the planned sub-steps of step 9.** The one-author bullet takes the class rules from
     its sub-step 2.
   - **Way rejected:** move them and leave the cross-references dangling, or reword. Rewording is a
     proposal, (b) 1–2.
   - **Cost if wrong:** about 900 words that a one-author cycle without a pin move reads without
     need. That is why "after" for that route is 5 498 and not about 4 600.
2. **Row 29, a slice too large** (3 instructions, planning route only), stays because "returns the
   same way" refers to the paragraph before it. Cost: about 45 words on the other routes.
3. **The handoff for the plan's *Foundation entries* and for a fresh agent of the return step.**
   Neither fits a row of `make-change`'s table, and the paragraph now says "their handoff names
   their stage instead". This is a new sentence, within the handoff paragraph the Goal changes.
   - **Way rejected:** silence, which leaves the orchestrator to guess a row and the agent to read
     "Your dispatch says which of these you make" against a dispatch that names none.
   - **Cost if wrong:** one sentence. The lasting fix is a row in `make-change`'s table, which is
     outside this slice.
   - **Recommended answer:** keep it until `make-change` gets a row for these dispatches.
4. **"With the element skills it names" became "and the skill of an element when it writes an entry
   of that element".** The base sentence told the agent to read the element skills with the
   paragraph. The Goal's change (no reading at the start of everything named) reaches it, and WAY-150
   says the writer of an entry "reads as the element's skill gives". I took it as part of the Goal's
   change in the handoff paragraph. Way rejected: keep the base clause. Cost if wrong: the writer
   loads the element skills at the start, as before.
5. **The foundation step leaves `SKILL.md`, although the orchestrator meets it at two moments**
   (row 30). The pointer names both moments: a `blocked` return with a question, and step 7's
   finding. Its handling of the `blocked` return also stays word for word in `:184-188`.
   - **Way rejected:** keep the paragraph in `SKILL.md`. Its writer would then read a 6 605-word
     file in which "you" means the orchestrator.
   - **Cost if wrong:** the orchestrator passes by the conditions of a question for the human at
     step 7. `spec_review.md` names "the foundation step" by name at that moment, and the pointer in
     `SKILL.md` says to read it there.
6. **Root-relative paths** (`task-cycle/skill/<file>.md`), unlike Slices 7–10's bare names; reason
   under *Layout*. Cost: longer pointer lines.
7. **Pointer phrasing.** Each pointer carries the moment as the orchestrator meets it: a plan member
   before its cycle starts; the designer returning `done`; the planning route; a `blocked` return; a
   blocking finding left after its fix; an input that is a link to the request. This follows
   WAY-257's second question.

No adaptation of `make-change` section 4 was needed. No invariant test changed.

## Questions

None that stop the work. Points 1, 3 and 4 above are the orchestrator's to accept or settle.
