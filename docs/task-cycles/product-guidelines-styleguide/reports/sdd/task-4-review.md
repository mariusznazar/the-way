# Task 4 review — the skill `maintain-styleguide` and its entry points (10b5f4a..f248e42)

`S` = `product-guidelines/styleguide/SKILL.md`, `T` = `product-guidelines/styleguide/template.md`,
`G` = `product-guidelines/template.md`, all at `f248e42`. Line numbers in the implementer's report
were checked against the file and are accurate.

## Spec Compliance: ❌

- ✅ Frontmatter (S:1-4) is spec §6.1 verbatim, one line, no `": "` and no `" #"`.
- ✅ Opening paragraphs (S:8-24): where the-way lies, the `the-way-` prefix, no Superpowers
  (WAY-125), outside practice described through WAY-175 without naming a source (WAY-27). A grep
  for `10x`, `Mercato`, `om-ux`, `shadcn`, `tweakcn` finds nothing.
- ✅ The split table of §6.2 (S:33-36) and the hand-over points into `refine-task` (S:28-31) match
  `project-level/task/skill/SKILL.md`. Its step 3 is "Resolve the gaps" (:106), step 4 "Carry
  the foundation decisions" (:136), step 5 `find-foundation-entries` (:152), step 6 acceptance (:164).
- ✅ Orchestrated mode (S:75-83) matches §6.4. The lead side supports it:
  `project-level/lead/skill/SKILL.md:95` says the orchestrator performs "all child dispatches their
  borrowed workflows request", and `project-level/lead/conversation_template.md:97` gives the slot
  "Child-work requests".
- ✅ Steps 0–5 (S:85-207) cover §6.3, with the exceptions listed below.
- ✅ §6.6 instruction file (S:56-61): the pointer goes outside the installer's block, in backticks,
  with its condition; the rule stands where `instruction-files` places a rule for some files; the
  invariant is said to be what keeps it; no command of its own.
- ✅ Entry points. An in-process `produce(discover(ROOT))` gives the same bytes as both files on
  disk (`True`/`True`, read-only check rerun by this reviewer). The report of the dry run holds 0
  `would create` and 30 `would change` (`reports/slice-4-entry-points.txt`).
- ✅ README (README.md:71-73, :78-81) names `product-guidelines/` and the skill directory.
- ❌ **Missing:** §6.3 Accessibility says that a law or a contract binding the accessibility is
  "an environment fact **and a failure mode of the part**, not an adoption" (WAY-86's last
  sentence, WAY-46). S:173-174 keeps only the environment fact (Important 1).
- ⚠️ **Implementer's concern 1, part-map change.** The skill puts the change in *To do* (S:72-73)
  and not in *Settlements to record*, as spec §6.2 lists it. This is the correct reading:
  `project-level/task/template.md:132` says "a change of the part map is never a row", and
  `elements/common/skill/SKILL.md:77` says "never a change of the part map" for task mode. Spec
  §6.2:484-485 is the defect. It is not in spec §11, so the whole-change review should record it
  as a contradiction settled by the template.
- ⚠️ **Implementer's concern 2, no part for a new user interface.** S:102-105 makes the part's
  identifier a question of the task and adds a *To do* item for `update-part-map`. The spec is
  silent on this; the reading is needed (the form check rejects a part the map lacks) and adds no
  rule. Accepted. Minor 7 covers one leftover: `<part>` is used in a path before it is settled.
- ⚠️ **Implementer's concern 3, when research runs.** S:109-111 and S:117 run step 2 before the
  first screen and at refresh or extension, never in audit mode (screens and no styleguide). This
  follows spec §6.3 and *To do* 8 of the frozen task, which binds over the spec and frames the
  research for "a product that has no screens yet". WAY-186:6120-6127 and row 16, however, have no
  mode restriction. In audit mode the skill gives no source for the roles, states and focus rules
  the audit's charges call for beyond the code and the template, so new role names an audit
  proposes come from the agent's judgement. The diff cannot settle this. Carry it to the
  whole-change review as a reading of *To do* 8 against WAY-186.
- ⚠️ A deferred charge stands in *Context* (S:69-70, S:153-154), while spec §6.2:479 lists it
  under *To do*. *Context* is the right home: a deferred charge is not an executable change
  (`project-level/task/template.md:86-88`). This is a sound reading, not a finding.
- ⚠️ No trial on a product. The text is prose that no test asserts (spec §10:830-834).

## Strengths

- The skill keeps the order of the work and points to what it does not own. It points to the
  template's sections by name and checks that each exists ("Writing the file" T:179, "Pairs,
  meanings and role names" T:155, "What each part carries" T:73). It points to "How a skill asks",
  "Critique before collective review" and "Reading the foundation" by name rather than copying them.
- "What reaches the task document" (S:43-73) is written for the cycle's author, who was not in the
  conversation. It carries ruling C21: the value and its source per role, or the exact source
  address and entry.
- The audit (S:140-157) carries everything in WAY-187 and WAY-175: both directions, a file of
  design tokens nothing reads named as a charge, 3–5 charges with file, line and effect, the four
  categories, the standing question, the agent's way to the running product or the code with
  unchecked items marked (with focus as the example), a palette read off the code as a proposal,
  and `unknown` as a rationale.
- The research discipline (S:119-132) follows WAY-122's method in the skill's own words: one fresh
  agent per question, run all at once; each source a page with its version; a critique that
  refutes unsupported claims; `critique: passed`; a stop when no fresh agent can run.
- The WCAG proposal (S:175-180) carries the edition read on the W3C's page in the session and never
  from memory, level AA, every screen, nothing written without acceptance, and the criteria as
  environment facts with address and passage.
- The weakest-point check was real: it found and removed two restatements before the commit.

## Issues

### Critical

None.

### Important

1. **S:173-174 — a binding law or contract loses its failure mode.**
   - What: the skill says only "what one requires is an environment fact, and no adoption is
     needed (WAY-86)". Spec §6.3:539-541 also requires "a failure mode of the part". WAY-46:1304-1307
     says such an obligation "enters the part map as a failure mode of that part, whose detection
     names an invariant resting on the environment fact of that obligation".
   - Why: a product bound by law to accessibility gets the environment fact but no failure mode at
     its user-interface part. Its criticality is then computed without it, and nothing ties the
     detection to the contrast and focus invariants. A part-map change is never a row (template:132),
     so the cycle never learns of it unless *To do* names it.
   - Fix: after "no adoption is needed (WAY-86)", add: the obligation also enters *To do* as a
     failure mode of the user interface's part, recorded through `update-part-map`, with the human
     giving its damage and severity and its detection naming the invariant that rests on that fact
     (WAY-46). Add the same item to the *To do* list at S:48-65.

2. **S:28-31 and S:75-83 — nothing leads a `refine-task` agent to this skill (plan-mandated).**
   - What: the skill says `refine-task` "opens or resumes the task … this skill takes over at its
     step 3". But `project-level/task/skill/SKILL.md` never names `maintain-styleguide`, and the
     spec forbids changing it (§6.2:466-467, ruling C5). `lead-project` dispatches "one fresh
     `refine-task` agent per confirmed task" (`project-level/lead/skill/SKILL.md:91`) and names no
     skill for a styleguide task. A grep of the worktree finds `maintain-styleguide` only in the
     skill, its entry points, the template and the decisions; the slices 5–7 briefs add it to
     sibling lists only.
   - Why: in orchestrated mode, the paragraph S:75-83 takes effect only if the dispatched agent
     happens to match the skill by its description. In manual mode, an agent that starts in
     `refine-task` on a styleguide task has no pointer either. The skill's whole orchestrated
     design depends on a route that no file gives.
   - Fix (outside this slice): either `lead-project`'s dispatch names `maintain-styleguide` for a
     task whose outcome is a styleguide, or the plan item or the task document states it.
     Otherwise the whole-change review records explicitly that reaching the skill rests on its
     description. In this slice, the opening of "Where the skill works" can at least say that the
     human or the orchestrator invokes this skill for a styleguide task, and that it then runs
     `refine-task`'s steps itself.

### Minor

1. **S:38 — "A meaning reaches the code only through the task document"** overstates WAY-172.
   WAY-172:5661-5663 also allows "a blocked draft request on whose branch the cycle proposes the
   decision", and T:189-190 gives that route. Fix: "In this skill's work, a meaning reaches the code
   through the task document: …", or add the second route in a clause that points to T:189-190.
2. **S:66-70 and S:175-180 — the WCAG edition's address and the passages are not named among what
   reaches the task document.** S:180 asks for "the edition's address and the passage word for
   word". But *Context* (S:69-70) carries only "the research's sources", and a row of *Settlements
   to record* is one sentence in the human's words. The cycle's author, who was not in the
   conversation, then has the edition's number but not where it was read. Fix: add to *Context*
   "the WCAG edition as read — its number, its address and the date read — and the address of each
   success criterion taken".
3. **S:191-194 — row 20 is carried only in part.** "The second is withdrawn once the full one
   holds" stands in neither the skill nor T:106-109. Only WAY-190 says it, by number. The human
   accepts a proposal without its end condition, and the cycle may write the invariant without it.
   Fix: add "withdrawn once the full one holds" to the bullet.
4. **S:170-171 — row 26 is carried only in part.** WAY-173:5703-5705 says that what the skill
   proposes binds a product only through an adopting decision; that covers every user interface
   getting a styleguide (WAY-183) and the styleguide coming before the first screen (WAY-184). The
   skill proposes only "the product's decision adopting the template". Fix: "the product's decision
   adopting the template and what this skill proposes".
5. **S:85-95 — the steps never tell the agent to run `refine-task` steps 1–2 first.** Only the
   description at S:29-30 says it. An agent following the numbered steps reaches step 4's "Write
   each answer … in the task document" (S:198) with no document yet. Fix: open step 0 with "Have
   `refine-task` steps 1 and 2 open or resume the task document, then read: …".
6. **S:119-127 — no stop where the foundation settles no technology of the user interface.** Before
   a first screen this is likely in an independent task, and the research has nothing to research
   "for that technology". S:112-113 covers a *new* library, not the absence of any. Fix: "Where the
   foundation settles no such technology, record it as an open question of the task (WAY-121) and
   run no research until it is settled."
7. **S:82, S:126-127 — `<part>` is used in the paths of the reports while S:103-104 may leave the
   part's identifier an open question.** Fix: settle the identifier before the research starts, or
   name a provisional directory.
8. **S:147 — "Ask every time what someone sees …"** reads as a question to the human. WAY-187:6164
   means the audit checks it on every screen. Fix: "For every screen, check what someone sees
   without data, straight from a link, after a refresh."
9. **README.md:71-73 — "the template of each discipline of guidelines with the skill that leads
   the work on them"** suggests that every discipline has a template and a skill. Only the
   styleguide has either. Fix: "the styleguide's template and the skill that leads the work on it,
   in `product-guidelines/styleguide/`".
10. **S:128 — "Give one fresh agent … each report"** leaves open whether one critic takes all
    reports or one critic takes each. `project-level/technology/SKILL.md:112` gives one critic per
    comparison. Fix: "Give each report, with its sources, to a fresh agent following `critique`".

## Row-to-text check

| Row | Verdict | Carrying text (checked) |
|---|---|---|
| 5 | ✅ | T:79-91 — role named by purpose, never a colour; meaning for the user; "The table holds no value". |
| 6 | ✅ | T:85-86 (*Text on it*), T:98-102. |
| 7 | ✅ | T:119-126 — path to the shared components, states listed, "never copies the list of components". |
| 8 | ✅ | T:127-134. S:184-185 only proposes its invariant; the meaning stands in the template. |
| 9 | ✅ | T:144-147; S:135-136 (meaning of a colour never read off a mockup); T:187 (values never from a mockup). |
| 10 | ✅ | T:139-143 ("served in development alone and never in production", code of the product). |
| 11 | ✅ | T:148-150 ("an example, never a rule"). |
| 12 | ✅ | T:135-138, T:185-187; S:51-53; S:167-168. The skill holds no list of tools. |
| 13 | ✅ | S:99-102; T:5-8. |
| 14 | ✅ | S:106-108, S:112-113. |
| 15 | ✅ | S:117, S:137-138. |
| 16 | ✅ | S:119-138. Audit-mode scope is a ⚠️ above. |
| 17 | ✅ | S:142-157. Every element of the row is present. |
| 18 | ✅ | T:58-67; S:181-182. |
| 19 | ✅ | S:184-187; T:103-118. |
| 20 | ⚠️ partial | S:191-194; T:106-109. "Not proposed under a single clean-up" is carried; withdrawal is not (Minor 3). |
| 21 | ✅ | S:175-178 — default recommendation, newest edition named by number, AA, every screen. Law branch incomplete (Important 1, spec-level). |
| 22 | ✅ | S:56-61. |
| 23 | ✅ | S:161-166. |
| 24 | ✅ | S:38-41; T:189-190. S:38 overstates (Minor 1). |
| 26 | ⚠️ partial | T:10-12; G:81-84; S:170-171. Adoption of the skill's proposals is missing (Minor 4). |
| 27 | ✅ | S:163-164; S:38-41. |

No row's carrying sentence brings in another meaning. The two partial rows lack part of their
meaning; neither contradicts it.

## Weakest-point check (WAY-164) and sharpness inputs

- Choice: "restating no rule" is a fair choice of weakest point, and the check (runs of seven or
  more words against eight files, each judged by hand) did catch two restatements. It sees only
  verbatim overlap. Paraphrased restatements pass it, for example S:181-182 against T:58-67 and
  S:163 ("the ways open, their cost and a recommendation") against `way_of_working.md:27-28`. Both
  are short, point to their source and are acceptable. The kept overlap S:51-53 against T:185-187
  is justified by ruling C21, which puts it on both sides.
- What the check missed: a requirement of spec §6.3 that was simply left out, the failure mode in
  Important 1. A sentence-by-sentence pass of §6.3 against the skill, not only rows 5–27, would
  have caught it. The row-to-text table cannot, because §6.3's sentence comes from WAY-46, not
  from a row.
- Sharpness inputs, verified:
  - Parts touched: `product-guidelines` (`foundations/part_map.md:266`) and `agent-instructions`
    (`.claude/skills/**`, :194). `README.md` belongs to no part on purpose (:413).
  - Trust-boundary files: none. Nothing irreversible.
  - The red state of `skills-reach-the-way-sessions` until slice 7 is planned and recorded, not
    suppressed.

## Assessment

**Task quality:** Needs fixes.

The skill is a good instruction to an agent. Its steps can be followed in a product without its
author; it stops where it should (no user interface, no fresh agent); it shows choices through
what the user sees and asks even where it recommends; its orchestrated routing matches what
`lead-project` can serve; and it restates almost nothing. The entry points are exactly what the
generator produces.

One requirement of spec §6.3 is missing: the failure mode of a binding law (Important 1). It is a
two-sentence fix in this slice.

Important 2 is plan-mandated. No file routes a `refine-task` agent, manual or dispatched, to this
skill, so it is reached only through its description. It cannot be fixed inside this slice's
change list without breaking "refine-task unchanged", and has to be settled at the plan or
whole-change level.

The ten Minor issues are sharpening: two rows carried only in part, one overstated sentence, a
missing stop, ambiguous phrasing, and README wording.

Counts: Critical 0 · Important 2 (1 plan-mandated) · Minor 10.
