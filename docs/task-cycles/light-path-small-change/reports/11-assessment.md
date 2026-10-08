# Independent assessment (WAY-10) of the light task cycle change

Range: c64a607..70f6bda. Changed files read in full: foundations/decisions.md (WAY-13/1 at 388-431,
WAY-125/1 at 3558-3624), foundations/invariants.md (foundation-change-path/1 at 259-265),
task-cycle/skill/SKILL.md, task-cycle/record_template.md. Also read: agent-instructions/README.md,
elements/decisions/template.md, elements/common/rules.md, elements/common/critique/SKILL.md,
foundations/glossary.md, foundations/part_map.md (task-cycle part, 122-137), and every decision that
cites WAY-13 or WAY-125 or holds task-cycle in its Scope (WAY-10, 11, 14, 100, 114, 126 read in full;
the rest by grep on Scope and citations). Paths below are relative to the assessed files.
I advise; I approve nothing.

## Observations

### O1. A light-cycle change to a high-risk part gets less than the decision says it must (main concern)

- Checked: the light-cycle criteria against WAY-13's own "violates" list and against step 4.
- Evidence:
  - foundations/decisions.md:412-413 lists as a violation "a small task skips a check that the parts
    it touches call for".
  - task-cycle/skill/SKILL.md:57-58 says "On the full cycle, use the full subagent review loop even
    for low criticality" - so the loop is the baseline check at every criticality.
  - SKILL.md:91-97 admits to the light cycle on three findings (foundation unchanged, about ten
    minutes, little context). None of them looks at criticality, trust-boundary files or
    reversibility. SKILL.md:113-116 then gives every light change one review and no spec review or
    plan review, whatever it touches.
  - WAY-13's own "complies" example (decisions.md:408-409) is "a one-line format change that breaks
    users' saved data gets the sharpest checks". That change is small, leaves the foundation
    unchanged and qualifies for the light cycle. The skill nowhere says what the sharpest checks are
    on the light cycle, beyond "if the sharpness inputs grew, add the resulting checks" (SKILL.md:189).
  - The new *Rejected* clause (decisions.md:428-431) dismisses keeping risky changes from the light
    preparation, because "a human's decision and checks kept whole already stop such a change".
    "Checks kept whole" is asserted, not shown. The spec review (step 7) and plan review (step 8)
    are independent readings of the design before any code exists. For a trust-boundary or
    irreversible change that is exactly what the light cycle removes.
- What would have to change: either add a fourth finding to the light-cycle test (parts touched not
  at the highest criticality, no trust-boundary file, change reversible), or state in the skill which
  additional check a high-criticality or trust-boundary light change gets (for example a second
  independent review, or the full loop). If the author keeps the explicit rejection, the request
  should put that rejection in front of Mariusz as the one place the new rule weakens preparation
  where harm is greatest. As written, the decision's "violates" clause and the skill contradict each
  other for that case.

### O2. The signal to abandon the light attempt is the executor's own judgement, with no measurable trigger

- Checked: how "outgrows a finding of step 4" is detected (SKILL.md:103-104, 121-123).
- Evidence: the three findings are "about ten minutes", "neither very large files nor very many
  files". Nothing is measured or bounded, and the record fields accept "estimate and reason". The
  agent that has written the code is the one that decides to throw it away, and the discard rule
  gives it a reason to under-report growth (the work is lost).
- Cost if it fails: a late switch costs the whole attempt plus the review. A missed switch means a
  large change gets one review and no spec.
- What would have to change: give one objective, recorded bound (elapsed time, number of files
  changed, or lines read) after which the executor must return, or let the orchestrator check the
  committed diff size against the recorded estimate before step 10.

### O3. WAY-125 now answers two questions

- Checked: elements/decisions/template.md:121-125 (a number stands for the question; a new rule next
  to an existing decision is a new question) and 132-134.
- Evidence: WAY-125's question is "Which Superpowers methods does the cycle adopt?". The change adds
  "when is the cycle lighter, who makes the change, when is an attempt discarded", roughly doubling
  the first sentence (decisions.md:3560-3577, about 170 words in one sentence), the verification and
  the rationale. WAY-125's fingerprint (f4d471cc by my computation) will now move with every tweak of
  the light-cycle rule, and so will the Superpowers pin it also carries.
- What would have to change: consider a new decision for the light cycle, deriving from WAY-13 and
  WAY-125, and revert WAY-125 to its original adoption sentence. Cost of doing it: one more entry and
  relation. Cost of leaving it: a harder-to-read binding sentence and a pin decision entangled with a
  sizing rule. Not a defect; a form call for the author.

### O4. The foundation touch on the light cycle sits awkwardly with the glossary's "foundation step" and "return step"

- Checked: foundations/glossary.md:84-86 and 154-156 against SKILL.md:105-112.
- Evidence: the foundation step is where "the task writes the change of the foundation it sets out to
  make". The light cycle is chosen because the task sets out to make none (SKILL.md:91-92: "the
  foundation step below would not run for it"), then a touch found mid-implementation is written "as
  the foundation step below gives" (SKILL.md:109-110). By the glossary, what implementation finds is
  return-step material.
- Consequence: low. Both routes lead to an entry written and assessed once. But a reader following
  the glossary sees one process using two names for one act.
- What would have to change: say the touch is written in the manner of the foundation step, or
  treated as a return-step finding that is pulled forward because later code depends on it. Same
  point for "light cycle" and "full cycle": the skill and record template name them, WAY-13 and
  WAY-125 never do (they paraphrase), so a reader cannot map decision to skill by word.

### O5. Part map has no failure mode for the new path

- Checked: foundations/part_map.md:122-137 (task-cycle, three failure modes).
- Evidence: the part answers for "how sharply a change is checked along the steps" (part_map.md:124).
  The change adds a new way that part fails (a task is taken light that needed full; an attempt is
  mis-kept or mis-discarded) and the map gains no mode, although WAY-11 makes part-map changes a
  return-step item. The part is already high, so no computed criticality moves; the omission is only
  that the new failure is not recorded or marked "not detected".
- What would have to change: add one failure mode to task-cycle, or record in the return step that
  none is needed and why.

### O6. WAY-125 verification examples are narrower than the binding sentence

- Checked: decisions.md:3560-3568 against 3599-3602.
- Evidence: the binding sentence discards an attempt on five triggers (too large, a choice left open,
  changes the meaning of an approved decision, contradicts a current entry, writes or changes an
  invariant or invariant test). The "complies" example names only the first and the invariant case;
  no "violates" example covers keeping an attempt that should have been discarded except the one
  about spec and plan written around outgrown code. Low; a level 2 agent will compare against the
  example pair.
- What would have to change: one added clause in each example list, or leave it.

### O7. Residual ambiguity of the word "path" in foundation-change-path/1

- Checked: invariants.md:259-265 against the new WAY-13 and SKILL.md:105-112.
- Evidence: the invariant says no change that alters an entry "runs on the path for tasks that leave
  the foundation unchanged". A light-cycle change can alter an entry (after the ruling). It stays
  consistent only because the skill records the foundation route as changed at that moment
  (SKILL.md:108), so "path" means the foundation route and not the cycle. The invariant's *Method* is
  `TODO`, so nothing fails today, but whoever writes the method must read "path" as foundation route.
  The Derives-from fingerprint was updated, which is correct (below).
- What would have to change: nothing now; note the reading when the method is written.

## Checks that found no concern

- Fingerprints. I fed UTF-8 files (never console strings) to relation-model/fingerprint.py. WAY-13/1
  binding part (decisions.md:390-400) gives 97b17d59, equal to the value written at decisions.md:3594
  and invariants.md:262. WAY-100/1 binding part gives e7a74a18, equal to decisions.md:3594. The old
  value c6b33aa9 appears nowhere in the assessed files. No other entry cites WAY-13 or WAY-125 with a
  fingerprint (grep over foundations/ and elements/). WAY-125's own fingerprint f4d471cc is cited by
  nothing. All dependents were therefore updated.
- Format guards. elements/decisions/format_guard.py on the log with --base none --merge-onto none:
  0 errors, 7 warnings (5 are old overdue check-by dates; 2 are the `merge of <request link>`
  placeholders of WAY-13 and WAY-125, which are expected before the request exists and are swapped at
  SKILL.md step 12). The invariants guard could only report an environment error because the
  assessed files are not in a git repository; I did not rely on it.
- Template form of WAY-13 and WAY-125: every field present, 1-3 binding sentences (WAY-13 has two,
  WAY-125 three), no `should`/`will`, Rationale and Rejected name no file or script. *Approved by* uses
  the template's merge form and no date (template 273-281). *Review when*/*Origin* `none` allowed.
  The Verification pairs of both are present.
- Edit in place and acceptance: both decisions had meaning changed and had an approval; their
  *Approved by* was reset to the merge of the new request, which is what agent-instructions/README.md
  asks (decisions edited in place, a change of meaning accepted at the merge). No new version was
  fabricated.
- Simple-and-obvious test in SKILL.md:106-109 matches WAY-125's list of discard triggers
  (decisions.md:3566-3569): same four touch conditions, plus "outgrows".
- WAY-14 (human approver), WAY-114 (human accepts at merge, question only without a recommendation or
  on a changed meaning), WAY-10 (one assessment, settlement does not reopen it), WAY-11 (return step),
  WAY-69 (invariant sentence, check and break from different agents): no contradiction. A touch that
  needs a choice, changes an approved meaning or writes an invariant leaves the light cycle, which
  lands it in the routes those decisions already govern.
- The light cycle keeps step 10, step 11 (return step and independent assessment) and steps 12-14 as
  written, so the outcome and the checks on the finished change are the same as on the full cycle
  (WAY-13's own new clause, decisions.md:396-398). Consistent with that clause, not with O1's
  criticality case.
- record_template.md fields are used by the skill: Foundation route, Cycle section (choice, touch,
  switch), Artifacts line for the discarded report, Request handoff. Nothing is read by no one.
- Glossary use in the changed sentences: "invariant test", "foundation", "return step" are used
  as the glossary has them; no paraphrase of a defined term found.
- Frequency (critique question 2): the material has no records of how many tasks were small, so the
  need cannot be measured here. The rule is new, so no recurrence-after-rule question arises.
  The cost-of-delay (spec and plan costing more than a small change) is argued in WAY-13's
  Rationale but not measured.
- Cheaper alternative (question 4): SKILL.md:136-138 says brainstorming "classifies the task" and the
  cycle then "follows its architectural path because the full cycle requires a written spec and plan".
  If that Superpowers skill has a lighter path for small work, dropping the override would be cheaper
  than a second cycle with its discard machinery. I could not verify the skill's content from the
  material given, so I report it as unverified.

## What can be cut

- record_template.md: the new tail of the *Foundation route* line ("on the light cycle, the time a
  touch changed it") repeats the *Foundation touched on the light cycle* row of the Cycle section.
- record_template.md and SKILL.md step 13: the *Cycle and its reasons* row of Request handoff
  repeats the Cycle section; keep one.
- decisions.md WAY-125 *Rationale*, last sentence ("a change that outgrows that finding starts
  again ... without the shape of its code"): repeats the two last *Rejected* items. Keep it in one
  place.
- Everything else is load-bearing for the new rule. Cutting the light cycle itself is only an option
  if the cheaper alternative in the checks above proves real.

## Overall call

The change is coherent and its mechanical parts (fingerprints, form, approvals, cross-decision
consistency) are correct. The one finding I would not let pass unaddressed is O1: the rule that
sharper checks follow risk (WAY-13 "violates" clause, SKILL.md:57) is not carried into the light
cycle's admission test, and the new *Rejected* clause asserts rather than shows that the checks stay
whole. Settle O1 and O2 before the merge; O3-O7 are form calls for the author.
