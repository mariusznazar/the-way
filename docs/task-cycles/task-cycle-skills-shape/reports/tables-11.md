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

