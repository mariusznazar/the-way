# Slice 5 review — task reviewer (spec compliance and quality)

Reviewer: Sonnet 5.5, read-only. Diff read once (`slice-5-review-package.diff`, one file, +12 lines;
both hunks end with their full paragraph, no cut-off). Checks I ran: `python3 -B
agent-instructions/skill_entry_points.py` -> `entry points are current`; the added lines are at
most 100 columns (`awk length` over the `+` lines, the `+` prefix included). I did not re-run the
suites (prose only, no test asserts it). Outside the diff I read: spec §7 and §5 tail
(`spec.md:516-526`, `:365-376`), C18/C19 in `cycle.md`, WAY-197 (`foundations/decisions.md:6674-6713`),
and `task-cycle/skill/SKILL.md:63` and a grep for "scratch" in that file — each for the named risk
below.

### Spec Compliance

- Spec compliant. `task-cycle/skill/SKILL.md` alone; frontmatter untouched (first hunk at line 329
  of the old file, the second at 373); `entry points are current`.
- Step 10 (`SKILL.md:337-347`): one sentence carrying every element of §7 as amended by C18/C19:
  invariant named with test cases by a guidelines rule; trigger (sentence added or altered, or a case
  rewritten); "that reviewer" = the break's writer (WAY-197); scratch worktree of the commit; `good`
  file once, `bad` file once; "the pair whose info string names that invariant" (C18); records pass /
  fail; listed-invariant relative reading with the per-file companion strict (C19); "not accepted
  otherwise"; bad file beside the deliberate break and never the break; cases only in the scratch
  worktree; citations WAY-168, WAY-197, WAY-69. Nothing extra. No review of code against guidelines
  added (Q5): the only added lines are those twelve, none mentions a checklist or review of code.
- Step 11 (`SKILL.md:391-393`): one sentence for the return-step check, taking the readings, the pair
  and the worktree rule from step 10 by reference. Settled by C8 ("one sentence in steps 10 and 11")
  and by §7's own "(step 10, and step 11 for return-step checks)"; see the judgement of concern 1.
- Cannot verify from the diff: nothing outstanding.

### Strengths

- The step 10 sentence follows §7 and WAY-197 closely, including the easy-to-drop parts: the pair is
  selected by info string, the listed-invariant reading is stated with both halves (good adds no failure,
  bad adds one) and the strict companion, and "never the break" is kept.
- "never in the task's worktree" is the skill's own name for the working tree (line 63, step 1), so
  the sentence uses the file's vocabulary.
- Placement is right (directly after each existing deliberate-break sentence), citation form matches
  the file, no other line touched, nothing else added to the cycle.
- The report's element table is honest about which elements step 11 carries only by reference.

### Issues

#### Critical (Must Fix)
None.

#### Important (Should Fix)
None.

#### Minor (Nice to Have)

1. `SKILL.md:391-393` (step 11) leaves out the trigger. Step 10 limits the run to a change that adds
   or alters the invariant's sentence or rewrites a case; step 11 says "Where a rule ... names that
   check's invariant with test cases", then "as step 10 gives". A return-step check can be written for
   an invariant whose sentence the change leaves alone (a check added to an existing invariant); read
   without "as step 10 gives" reaching the trigger, step 11 would require the run there too. The
   reference most naturally covers the trigger as well, and a return-step check normally follows a new
   or altered sentence, so this is a reading ambiguity, not a gap. Optional fix: "...with test cases,
   and the change meets step 10's trigger, the reviewer also runs...". Not worth a round alone.
2. Executor concern 3 (line 63 against the scratch worktree), judged on its merits: line 63 says "The
   cycle writes only in the task's worktree and changes nothing outside the product repository". A
   scratch worktree is a separate checkout (in the reviewer's scratchpad) and `git worktree add` also
   writes the repository's worktree metadata, so read literally line 63 forbids what step 10 now
   requires. WAY-140, which line 63 rests on, concerns effects outside the product's repository and its
   task record, and a scratch worktree of the product's own commit is not one; the new sentence itself
   says where cases may be applied. This is a real wording tension but not a defect of this slice:
   §7 calls the sentence "the whole change to the cycle" and the brief says "Nothing else changes", so
   adding a clause at line 63 is outside this slice's scope. Recommend the controller note it as a
   process remark for the human (a later one-clause edit of line 63, e.g. "and, for the reviewer's
   scratch worktrees, in those"), not a fix here. Outside the task's scope.

### Judgement of the other flagged concerns

- Concern 1 (step 11 refers to step 10): accepted. Writing the sentence twice would give two
  wordings that can drift; the file already uses such cross-references ("follow step 11's order", "as
  'The end of a code review' gives"). Only the trigger ambiguity above is worth noting (Minor 1).
- Concern 2 (what "not accepted otherwise" withholds when a change only rewrites a case): not a defect.
  WAY-197 reads "the check is accepted only where both that use ... and the deliberate break ... make it
  fail", and §7 says "the check is not accepted otherwise"; the sentence repeats them word for word.
  In a change that rewrites a case and leaves the sentence alone, the check being run is the existing
  one and the withheld item is the acceptance of that check's coverage of the rewritten case (an unrun
  or wrongly-reading case is a finding via step 11 / "An undetected break is a finding to resolve").
  Making that explicit would widen the spec's sentence; the spec and the decision do not.
- Concern 3: see Minor 2.

### Deliberate break
None: no invariant's code is covered by this slice (brief and constraints).

### Assessment

**Task quality:** Approved

**Reasoning:** The one sentence of §7 sits in step 10 with every element, step 11 carries the
acceptance and takes the rest by reference, nothing else changes and the frontmatter and entry points
are intact. Two Minor notes (step 11's trigger by reference; line 63's wording beside the scratch
worktree, outside this slice) need no fix before the slice is accepted.
