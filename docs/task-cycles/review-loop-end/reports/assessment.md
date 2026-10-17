# Independent assessment — end of the whole-change review loop (e7f7c3a..6ed0e86)

Worktree: `C:/Storage/repos/the-way-wt/review-loop-end-assess` at `6ed0e86`. Read whole:
`elements/common/critique/SKILL.md`; the diff `e7f7c3a..6ed0e86` (five commits); WAY-125, WAY-161,
WAY-162, WAY-163, WAY-164 and the entries they relate to (WAY-10, WAY-11, WAY-13, WAY-69, WAY-100,
WAY-101, WAY-135, WAY-136, WAY-140, WAY-148, WAY-157, WAY-158, WAY-159, WAY-160);
`elements/decisions/template.md`; `elements/common/rules.md`; `foundations/glossary.md`; the
`task-cycle` part of `foundations/part_map.md`; `task-cycle/skill/SKILL.md` and
`task-cycle/record_template.md` at `6ed0e86`; `agent-instructions/README.md`; the Superpowers 6.4.1
files `requesting-code-review/SKILL.md`, `requesting-code-review/code-reviewer.md`,
`subagent-driven-development/SKILL.md`, `subagent-driven-development/re-review-prompt.md`,
`subagent-driven-development/implementer-prompt.md`. Line numbers below are of the files at
`6ed0e86` unless a Superpowers file is named.

Weights: **high** — the change should not merge as is; **medium** — the author should settle it
before the merge, by a change or a recorded reason; **low** — a reader's remark; the author may
leave it.

## Observations

### A1 — Parked slice findings and deferred minors of slice reviews have no settled path to the request (medium)

Checked: duplicated or missing settlements between WAY-161 and WAY-162; whether a finding can
still end in "a list nobody reads".

Evidence: WAY-162 keeps the fix loop of each slice as Superpowers gives it
(`foundations/decisions.md:5166-5167`, `task-cycle/skill/SKILL.md:305`, `:438`). In that loop the
orchestrator still parks findings at the cap with rulings, including findings it judges "Real, but
nothing downstream builds on it" (Superpowers `subagent-driven-development/SKILL.md:411-425`), and
records Minor findings of slice reviews as deferred (`:361-365`). Their only route onward is the
final reviewer's triage (`:454-456`). WAY-161 lists in the request only the unfixed Minor findings
and the out-of-scope findings *of the review of the whole change*
(`foundations/decisions.md:5097-5100`; `SKILL.md:478-482`). A parked Important finding or a deferred
minor that the final reviewer does not raise again therefore reaches the human only in the copied
ledger (`SKILL.md:308-310`), which is what WAY-161's *Rejected* names as the wrong place: "the
Minor findings kept only in the cycle's reports the request links to — nobody reads them"
(`:5148-5150`) and its rationale "a list the request only links to is a list nobody reads" (`:5138`).

What would have to change: the cheapest form is in the skill — the handoff of the final
whole-branch review asks the final reviewer to grade each deferred-minor and parked line of the
ledger in its own report, so that each becomes a finding of the review of the whole change and
flows by WAY-161; otherwise WAY-161's lists name the ledger's parked and deferred lines explicitly.

### A2 — Non-blocking findings of later code reviews stay in a linked report, which WAY-161 rejects, and no decision settles where they go (medium)

Checked: contradictions between the entries and the skill; missing settlements.

Evidence: `SKILL.md:416-420` — for the review of a settlement, of the reconciliation and of a
correction "the review's other findings cause no fix and stay in its report, which the record
links". WAY-161's *Verification* names as a violation "the Minor findings stand only in the cycle's
reports the request links to" (`decisions.md:5126-5127`), and its *Rejected* the same
(`:5148-5150`). WAY-161's binding sentences cover only the review of the whole change
(`:5086-5101`), and WAY-162, which extends the one-fix bound to the later reviews
(`:5157-5160`), says nothing of where their non-blocking findings go. So the skill settles, for the
later reviews, a question no decision settles, and settles it the way WAY-161 argues against.

What would have to change: either WAY-161's request lists take the Minor and out-of-scope findings
of every code review of the cycle (the request's description is updated after a correction in any
case, `SKILL.md:522-523`), or WAY-162 states, in a binding sentence, that the later reviews' other
findings stay in the record and why the argument of WAY-161 does not reach them.

### A3 — A behaviour the task requires that the reviewer declines to judge has no way back to review (medium)

Checked: error when the rule is applied too widely; whether it moves the problem elsewhere.

Evidence: WAY-161 makes every "Declined to judge" line an out-of-scope item of the request
"whatever its grade" and forbids the orchestrator to move it (`decisions.md:5090-5101`;
`SKILL.md:398-403`). The reviewer sets lines aside as "outside the plan or spec" by its own reading
(Superpowers `code-reviewer.md:45-48`). Where the reviewer misreads the frozen task and sets aside a
behaviour the task does require, the rule leaves that behaviour unreviewed and lists it as a
candidate for a new task; the only reader who can catch it is the human at the request. The
rationale guards against the orchestrator hiding an inconvenient finding (`:5140-5141`,
`:5151-5153`) but not against the reviewer's own exclusion error, which the borrowed step ("The
executor rules on each line") did cover.

Frequency, measured from the repository: of the five cycle records kept in git history
(`5ae2e65` shorten-task-cycle, `0f44d91` lead-project, `348169a` selective-document-reading,
`46060eb` one-author-small-change, `48df1dd` lean-cycle-orchestrator), one shows the orchestrator
ruling on declined lines — lean-cycle-orchestrator, choice C14 "Review's declined judgments: Accept
explicit limits" — and those lines were limits of evidence, not behaviours of the task; the rule
would have put them in the request, where that request already named them as limits.

What would have to change: WAY-161 could allow the orchestrator to return a declined line to the
reviewer with the requirement of the frozen task that covers it, for the reviewer to judge — the
reviewer still grades, so the move the rationale fears does not open. If the author prefers the
rule as it stands, the *Rejected* should name this option and the human's reading as the remedy.

### A4 — Three rationales rest on an unnamed source (low-medium)

Checked: source fidelity of every substantive claim; template rules for *Rationale*.

Evidence: "The rule takes from an agent harness's review practice …" in WAY-161
(`decisions.md:5143-5145`), WAY-162 (`:5206-5208`) and WAY-164 (`:5299-5301`). No *Based on* names
that practice, so the claim cannot be checked. WAY-164 moreover derives from WAY-100
(`:5275-5276`), whose binding sentence asks a borrowed practice to be named in the decision that
adopts it (`:2790-2792`). The template also asks that *Rationale* "does not tell how the decision
was reached" (`elements/decisions/template.md:51-53`).

What would have to change: name and quote the source in *Based on*, or cut the three sentences —
each rule stands on the argument its rationale already gives. Cutting is the cheaper of the two.

### A5 — The blocked request reverses step 12's order for no stated reason (low)

Checked: cheaper ways; consistency of the skill with itself.

Evidence: `SKILL.md:426-430` and `:442-444` commit the record pair and `stages.md` before the
request opens, then open the draft and swap `<request link>`. The ordinary path opens the draft
first, swaps the placeholders, then runs `cycle_stages.py`, commits the record pair and updates the
description with the record's SHA (`:455-469`). In the blocked order the committed record cannot
hold the request's URL (`record_template.md:141`), and nothing in WAY-162 or WAY-163 asks for the
reversal — WAY-163 says only that the record and `stages.md` are written (`decisions.md:5224`).
The commit `78df576` names the ordering as its purpose but the text gives no reason.

What would have to change: the blocked path follows step 12's order, skipping only the
reconciliation and the ready marking; the two sentences that reorder it can be cut.

### A6 — The blocked path is restated in six places (low)

Checked: cost of maintaining the skill text.

Evidence: step 10 (`SKILL.md:342-344`), step 11 (`:376-377`), the section (`:422-432`), step 12
(`:442-444`), step 13 (`:494-499`) and the correction (`:518-521`), with twelve references to
"The end of a code review". Step 10's last sentence and step 12's first sentence repeat the section's
third paragraph in full.

What would have to change: those two sentences become a reference to the section, or are cut.
Can be cut.

### A7 — WAY-161's binding sentence and the skill differ on whether a Minor finding may be fixed (low)

Checked: contradictions between the entries and the skill.

Evidence: the binding sentence lists "the unfixed Minor findings" (`decisions.md:5098`), which
implies some may be fixed; the skill says a Minor finding is never fixed (`SKILL.md:400`). The
rationale argues only against "a minor finding fixed in a round of its own" (`:5136-5137`), not
against taking one into a fix round that runs for blocking findings anyway.

What would have to change: the binding sentence says Minor findings are not fixed, or the skill
allows a Minor fix inside a fix round that runs anyway — the second widens the fix diff the
re-review reads, so the first is cheaper.

### A8 — A new blocking finding in the fix stops the cycle without any attempt at its repair (low)

Checked: error when applied too widely; would it act in the case that prompted it.

Evidence: `decisions.md:5160-5161`, `SKILL.md:413-414`. The case the rule targets is a finding that
survived its own fix; a finding the fix introduced has had no fix tried, yet it opens a blocked
request with the cycle's cost. The rationale gives the reason ("keeps a fix from trading one
blocking finding for another", `:5201-5203`) and *Review when* measures excess stops
(`:5191-5192`).

What would have to change: nothing is required; the author may note the choice as deliberate in the
*Rejected* ("one more round for findings the fix introduced") so a later reader does not reopen it.

### A9 — WAY-164 on a change with no runnable behaviour, and its overlap with the borrowed self-review (low)

Checked: purpose; cheaper existing practice; error when applied too widely.

Evidence: the binding sentence asks every author and executor to write "a check that would catch
that" (`decisions.md:5266-5269`); the complies example speaks of "a test" (`:5279-5280`). For a
change of text only — foundation entries, a skill — no test runs; the skill's report contract allows
a manual check with its method and observed result (`SKILL.md:142-144`), but neither the entry nor
step 9 says that this check may be one. The borrowed implementer prompt already asks the executor
"Did I miss any requirements? Are there edge cases I didn't handle?" (Superpowers
`implementer-prompt.md:92-117`); WAY-164 sharpens that to one named requirement, one check and a
reported outcome, which is a real difference, and its *Review when* (`:5286-5288`) measures whether
the check ever catches anything.

What would have to change: one clause in the binding sentence or in step 9 that the check may be a
manual check recorded as the report contract gives. Otherwise no concern.

### A10 — What WAY-164 forces on the deliberate break stands in prose and verification, not in a binding sentence (low)

Checked: template conformance — "What a decision forces on later work stands in a binding sentence
or a field, never in prose" (`template.md:53-54`).

Evidence: "it is never that check, which an agent other than the code's author writes" is in the
rationale (`decisions.md:5297-5299`) and the violates example (`:5284-5285`) only.

What would have to change: a clause in the binding sentences, or nothing if the author reads the
rule as already following from WAY-69.

### A11 — The orchestrator may not overrule the reviewer, but nothing bars steering the reviewer through the handoff on the one-author route (low)

Checked: whether the rule moves the problem elsewhere.

Evidence: `SKILL.md:300-301`, `:405-406`, `:411-413` bar overruling and ask the fix-review handoff
to put contested findings to the reviewer. Superpowers forbids its controller to pre-judge findings
in a reviewer's prompt (`subagent-driven-development/SKILL.md:339-344`), which the planned route
inherits; `requesting-code-review` carries no such rule, so the one-author route has none.

What would have to change: one sentence in "The end of a code review" that the handoff of a review
or a fix review names no finding as wrong, at most Minor or outside scope. Low, because the
reviewer's report and the handoff both go into `reports/` where the human can read them.

### A12 — `correction` is used in a meaning the glossary does not give; inherited, not introduced (low)

Checked: use of glossary terms in another meaning (`verdict`, `correction`, `result`, `gate`,
`return step`, `foundation step`, `slice`, `human action`).

Evidence: the glossary defines a correction as a change to an entry's binding part that leaves its
meaning unchanged (`foundations/glossary.md:28-30`). The new skill text uses "correction after
review" for the work done on a request after the human's remarks (`SKILL.md:418`, `:426`, `:430`,
`:518-519`) and the record template likewise (`record_template.md:47`). The usage comes from the
pre-existing section "Correction after review" (`SKILL.md:506`); the new binding sentences of
WAY-163 avoid the word (`decisions.md:5222-5228`). `verdict` appears only in pre-existing skill text
(`SKILL.md:146`, `:299`, `:447`), not in the new entries. `result` is avoided in the new text ("what
the check showed"). The other terms are used as the glossary gives them.

What would have to change: nothing in this change; renaming the section is a separate decision.

### A13 — The exception is written into WAY-125 rather than carried by `narrows` (low)

Checked: cheaper ways within the template.

Evidence: the edit of WAY-125's binding sentences (`decisions.md:3624-3627`) renews its fingerprint
and so touches WAY-140, WAY-148 and WAY-157 (`:4320`, `:4642`, `:4979`). The template gives both
forms: an exception written into the decision itself, or `narrows` from the more specific decision
(`template.md:159-160`). `narrows WAY-125` in WAY-161 and WAY-162 would have left WAY-125 and the
three dependants untouched; the chosen form has the merit of telling a reader of WAY-125 which steps
no longer apply.

What would have to change: nothing is required; a judgment the author may keep.

### A14 — Cosmetic (low)

`decisions.md:5239-5241`: the complies example of WAY-163 wraps at "a cycle blocked by the" with a
short line, unlike every other field of the log.

### A15 — The case WAY-162 answers has not occurred in the repository's records (low)

Checked: how often the problem occurred, from available records.

Evidence: the five cycle records named under A3 (kept only in git history; no `docs/task-cycles/`
exists in the tree). Whole-change reviews: three returned no finding (shorten-task-cycle,
one-author-small-change, lean-cycle-orchestrator); two returned one Important finding each, fixed
in one round and marked ADDRESSED by the scoped re-review (lead-project `84cdc87`,
selective-document-reading `1de9e1a`). No record shows a finding surviving its fix review, a
tripped breaker, or a parked finding. The one-fix-one-review bound on the one-author route entered
the skill on 2026-10-08 (`3bf1452`) and the records since show no recurrence of a second round.
Session transcripts were not searched (outside the worktree). The decision therefore rests on a
prediction, which its *Review when* (`decisions.md:5191-5192`) measures; this is the form the
template asks for, so no change is required — the author should know the rule is ahead of its
evidence.

## Checks that found no concern

- **Quotations.** Every quotation in *Based on* of WAY-161 and WAY-162 is verbatim in the named
  Superpowers 6.4.1 file: `code-reviewer.md:45-48` (declined-to-judge sentence), `:113`, `:116`,
  `:119` (the three grades); `requesting-code-review/SKILL.md:45` ("Note Minor issues for later");
  `subagent-driven-development/SKILL.md:454-456` (triage line), `:465-466` (adjudicate residuals),
  `:467-469` (no second fix wave), `:401-402` (new breakage joins the open list). The environment
  named in *Based on* matches the machine (`bash --version` → 5.3.15, `uname` →
  MINGW64_NT-10.0-26300); the `cat -n` method cannot be verified after the fact and is plausible.
- **Paraphrases of the borrowed methods** in WAY-125's new sentence (`:3624-3627`) and in the
  skill's last paragraph of "The end of a code review" (`SKILL.md:434-438`) describe steps the
  sources hold: adjudicate and park residuals (`SDD:465-466`), the final fix wave taking in
  triaged deferred minors (`SDD:454-459`), the executor ruling on declined lines
  (`code-reviewer.md:47`). "NOT ADDRESSED alone does not settle a contested finding"
  (`SKILL.md:412-413`) is true of `re-review-prompt.md:80-85`, which has no verdict for a contested
  finding.
- **Fingerprints.** `elements/decisions/format_guard.py` run with `--merge-onto e7f7c3a` reports
  no fingerprint error: WAY-125@f3e6afcf is carried by all five references (`:4320`, `:4642`,
  `:4979`, `:5107`, `:5173`), WAY-161@d6d3137b and WAY-162@ce2e41f0 match their binding parts, and
  the other fingerprints the new entries carry (WAY-136, WAY-140, WAY-100, WAY-11, WAY-10,
  WAY-148) are current. The guard's only errors under that option are the in-place edits of
  WAY-125, WAY-140, WAY-148 and WAY-157 and the `<request link>` placeholders, both of which the
  pre-main route prescribes (`agent-instructions/README.md:21-25`, WAY-14); under the README's
  `--base none --merge-onto none` the guard reports 0 errors.
- **Template conformance.** All fields present in WAY-161–164; binding sentences count 3, 3, 2, 2;
  *Change* `new decision`; *Scope* names a part; *Relations* use `derives from` with fingerprints;
  *Verification* level 2 with a complies/violates pair; *Review when* holds an observable state and
  a date or `none`; *Origin* `none`; *Approved by* in the merge form. No `should`, `will` or
  capitalised RFC word in a binding sentence (the one `must` is inside a quotation in *Based on*).
  No rationale names a file, script or count. WAY-125 keeps *Rationale* and *Rejected* consistent
  with its new sentence.
- **Tests.** `python -B gate/run_tests.py task-cycle` → 41 pass; `gate` → 98 pass;
  `agent-instructions/skill_entry_points.py` → entry points current.
- **Contradictions with current entries.** None found against WAY-10 (settlements stay part of the
  one assessment; a blocked finding is kept out of them), WAY-11 (return step still precedes the
  merge — WAY-163 moves it, does not drop it), WAY-13 (checks are not lightened: the gate still
  runs before a blocked request), WAY-69, WAY-100, WAY-101 and WAY-140 (the human creates the new
  task), WAY-136 (whole-change review of each route unchanged), WAY-148 and WAY-158 (the
  orchestrator still reads evidence before ruling on a question; the skill narrows "settling a
  finding" consistently at `SKILL.md:158-159`), WAY-159, WAY-160. The part map's failure modes of
  `task-cycle` (`part_map.md:144-150`) are not contradicted; the new human stop is not "a choice it
  can settle from the task and foundation".
- **Entries against one another.** WAY-161 (what blocks, where the rest goes), WAY-162 (how the
  loop ends), WAY-163 (what runs before a blocked request), WAY-164 (the author's own check) answer
  four distinct questions; apart from A1 and A2 no settlement is duplicated or missing between them.
  WAY-163's complies example for a block in the settlement review ("names only what has not run on
  the code it holds", `:5239-5241`) agrees with the skill (`:376-377`).
- **Record template.** The four new fields (`record_template.md:46-51`, `:151-157`) match what the
  skill asks the record and the request to hold (`SKILL.md:478-482`, `:494-499`, `:503`).
- **Purpose and moment.** Each entry names the moment it acts (the review of the whole change and
  the reviews after it; before a blocked request; before review) and would act in its case: a
  finding surviving its fix now produces a blocked request instead of an orchestrator ruling; a
  declined line now reaches the request; the gate runs and the return step waits before a blocked
  request; every author and executor reports one weakest-point check.

## What can be cut

- The reordering of the blocked request (A5): the two sentences at `SKILL.md:426-430` and
  `:442-444` that commit the record before the draft opens.
- The restatements of the blocked path in step 10 (`SKILL.md:342-344`) and step 12 (`:442-444`)
  (A6).
- The three "takes from an agent harness's review practice" sentences (A4), unless the source is
  named.

None of the four decisions can be cut: each answers a question no current entry answers, and the
edit of WAY-125 is needed for the borrowed steps to give way. The record template's four fields are
each read by the request or the correction.
