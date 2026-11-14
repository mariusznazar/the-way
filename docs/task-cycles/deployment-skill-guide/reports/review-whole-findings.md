# Findings for the fix — review of the whole change, head a900916 (task `deployment-skill-guide`)

Cut word for word from `reports/review-whole-report.md`: the blocking findings first, then the Minor findings of that review within the task (fixed before the request opens). The Minor finding outside the task (M5) is not part of this fix.

### Important (blocking, within the task)

**I1. The guide defines when a skill covers an item, against its own "it binds nothing" and WAY-139.**
Place: `project-level/task/deployment_skill_guide.md:31-33` (and, in the same vein, `:273-277`).

- What is wrong. "How to read a part" says of the questions of each part: "An answer that settles each
  question, or says in the skill that the human left it unsettled, covers the item." That is a rule for
  when an item is covered, and its measure is the guide's own questions. The same file says at `:15-17`
  that "Whether a skill covers an item is decided there [the list in WAY-139 and the check in
  `resolve_gaps.md`], not here." The two sentences contradict each other, and the first is the one a reader
  applies. The same reach shows in part 7 (`:273-277`): "A complete answer is one of two: a stated lifetime
  for each place, with what bounds it and what it misses; or the human's refusal". WAY-139 says only that a
  skill that records the refusal covers the item; WAY-165 says what the record asks; neither says that a
  lifetime "for each place, with what bounds it and what it misses" is the complete answer. (Part 8's "a
  complete answer is one of three" at `:309-311` restates WAY-270 and WAY-139 and is not part of this
  finding.)
- Why it matters. WAY-139 (its own *Verification*, `foundations/decisions.md:3918-3919`) names as a
  violation "the guide stands as a skill that a product applies as it is, or as a condition that a skill
  must meet to cover an item". A reviewer or the check, meeting a skill that answers the list but not every
  question of the guide, has a sentence in a the-way file that says it does not cover the item. Task item 6
  requires that the guide binds nothing; the explicit sentence at `:15` meets it, `:31-33` takes it back.
  Under WAY-263 a file that restates what the decision settles, broader or differently, is Important.
- Evidence. The two quotations above, read side by side; the decision's violation clause at
  `foundations/decisions.md:3918-3919`; `resolve_gaps.md:66-68` ("The guide binds nothing: the list and this
  check do").
- Fix direction. Say that the questions help to write an answer and that the list and the check decide
  coverage; drop "covers the item" from `:31-33`, and word part 7's two kinds as examples of an answer, not
  as the definition of a complete one.

**I2. A fragment cuts the qualifying clause of a sentence and so says what loop2's skill does not say.**
Place: `project-level/task/deployment_skill_guide.md:222`.

- What is wrong. The fragment reads "Every server or Cloudflare change is the human's, … The agent prepares
  the commands." The source sentence (`.claude/skills/loop2-deploy/SKILL.md:102-103` at
  `e54f23c0…`) is "Every server or Cloudflare change is the human's, except deployment started by the
  existing automation. The agent prepares the commands." The `…` marks a cut, but the cut takes the exception
  that makes the sentence true for loop2. The author's report names the cut (choice 3) and the reason: the
  exception would sit awkwardly beside WAY-140.
- Why it matters. (a) Task and WAY-139 require fidelity: "nothing the change takes from them altered". The
  cut changes the claim from "all but automated deployment" to "all". (b) The guide contradicts itself: part
  1 (`:64-66`) shows a push to `main` starting an SSH call that runs the installed deploy script, and part 5
  then says every server change is the human's. A reader who asks "what does the agent do, what does the
  human do, and what does the automation do" gets, from part 5, no third actor, though that third actor is
  the most common case of the item. (c) The reason given does not hold on its face: WAY-140
  (`foundations/decisions.md:3973-3976`) speaks of a task's effect outside the repository made through a human
  action the task names; code a human merged that an existing automation then deploys is not shown to
  contradict it, and the guide's own part 5 lead-in already states WAY-140 on its own. If the human holds
  that it does, that is a decision about WAY-140 for the human, not a cut in a quotation. The author's
  rationale does not lower the grade.
- Evidence. `git -C the local checkout of loop2 show e54f23c0ea3bd1db13d2635333417eb50412d6a0:.claude/skills/loop2-deploy/SKILL.md`
  lines 102-103; the guide lines `:64-66` and `:222`.
- Fix direction. Quote the whole sentence, mark the exception as loop2's (`[loop2: …]`) and, if the human
  wants it, say in one sentence in the guide that an automated deployment on merge is the third case a skill
  names beside the agent's reads and the human's changes.

### Minor, within the task

**M1. Unmarked loop2 parameters in fragments, against the guide's own marking rule.**
Place: `deployment_skill_guide.md:320` ("At most one message per kind in six hours and six in all in 24
hours"), `:322-324` (the scheduled check's "Every five minutes … up to six attempts 20 seconds apart"), `:281`
("not above about 100 MB"), `:145-146` ("players stay signed in"), `:315-316` ("both containers").
The guide says (`:34-38`) that loop2's own — "commands, paths, names and deployment parameters" — stands
inside `[loop2: …]`, and task item 4 and WAY-139's *Verification* (`:3909-3910`) require loop2's own parts to
be marked. The commands, paths, server and Cloudflare settings are marked throughout; these numbers and
intervals are values loop2 chose, and a reader who keeps "the shape outside the brackets" would copy them.
Effect is small (no command and no address is involved), hence Minor. Fix: put each in a marker.

**M2. Fragments join sentences from different places of the source, or reorder them, under one quotation;
a few statements about the source are not true as written.**
Place and evidence:
- `:187-191` (part 4): the guide puts "This is **script installation, one deployment and four Cloudflare
  changes**; public traffic can be unavailable…" before item "3. Restore the Origin Rule…". In
  `references/troubleshooting.md:162-170` the four items come first and "This is…" follows them.
- `:222-223` (part 5): "Treat service logs as potentially sensitive; report selected, redacted diagnosis,
  not raw logs." comes from `SKILL.md:115-116` ("Seeing deployments"), joined by `…` to `SKILL.md:102-103`.
- `:287-289` (part 7): "The file holds the game's lines for those weeks, with `accountId` values …" comes
  from `SKILL.md:279-281` ("How an agent reads it"), joined by `…` to the paragraph "How long each lives"
  (`SKILL.md:268-274`).
- `:152`: "A list of rotations ends the file" — in `references/setup_and_secrets.md` a "Sources" section follows
  the rotation list (`:615` onward). `:259`: "The table is loop2's own, from its deploy script" — `SKILL.md`
  carries the table and does not say it is copied from the script.
Why it matters: the `…` shows that something is missing but not that the pieces lie elsewhere or in another
order; a reader opening the source to see the context does not find it where the fragment implies.
No number, command or meaning is changed by these. Fix: keep the source order, name the section a spliced
sentence comes from or take it as a separate fragment, correct the two statements.

**M3. The binding sentence of WAY-139 reads as if the guide were an eighth item of the list.**
Place: `foundations/decisions.md:3868-3873`. The list is introduced by "the list of what a product's
deployment skill covers:" and runs on with semicolons to "…how a human learns of a failure; and, beside the
list, a guide to writing such a skill…". A reader reads the guide as one more thing a skill covers; "beside
the list" is the only sign it is not. The sentence at `:3873-3878` has also irregular line breaks ("When" at
the end of line 3873; line 3878 much longer than the rest) from the in-place edit. Task item 7 asks for the
guide beside the list. Fix: close the sentence of the list at "failure" and open a new one for the guide.
Minor because the *Verification* and *Rationale* of the same entry say the guide is beside the list and binds
nothing; the foundation check (`foundation_check.py`) passes.

**M4. "A preview of deployments" is read as if the list defined it.**
Place: `deployment_skill_guide.md:77-79`. WAY-139 does not define the item and nor does the task; the guide
writes "The skill of loop2 answers it in two places", which presents the author's reading (choice 1 of the
report) as the item's meaning. The reading is reasonable and part 2's questions cover the other likely
reading too (a change deployed to look at before it reaches the main line, `:83-84`), so a product with
per-branch preview environments is not left without a question. Fix: one clause saying the list does not
define it and the guide reads it as both. Minor.
