# Report of the executor of slice 13

**Status:** done with concerns (two points for the orchestrator; see "Findings").

**Commit:** `ab75f6c` on `task/decision-log-second-round`.

**Files changed** (10, +84 / -52): `product-guidelines/audit_end.md` (+19/-11), `reading.md` (+7/-6), `template.md` (+20/-14), `coding/SKILL.md` (+7/-4), `coding/hand_back.md` (+3/-3), `coding/kinds.md` (+12/-5), `coding/new_tools.md` (1/1), `coding/recognize.md` (+10/-4), `coding/research.md` (1/1), `coding/starting_set.md` (+4/-3). Exact counts: `git show --stat ab75f6c`.

## Checks

- `python -B elements/common/foundation_check.py` — exit 1 (expected until the last slice). 263 lines printed, none for a file of this slice's *Change* (the lines stand for `agent-instructions/README.md`, `product-guidelines/coding/{settle,task_document,template,trial_run}.md`, and the styleguide and testing files). Output kept in `.runs/executor-13/fc.txt` while I worked, removed before return.
- `python -B agent-instructions/skill_entry_points.py` — exit 0, "entry points are current".
- Not run: `gate/run_tests.py` in any form (the method forbids the full suite; the slice lists no directory).

## Own-work check (make-change section 3)

Requirement most likely not met: "no file of the slice names a number that left the log" and "each rule has one sentence of reason, nothing invented". Check: a script-free loop over every `WAY-NN` in the ten files against the headings `### WAY-NN` of `foundations/decisions.md` as it stands; it printed no number that is absent from the log (exit 0, empty output). Second check: I read each added sentence against the *Rationale* of the entry at base `ec7929d` (see the list below); no sentence names a file, count or measurement the entry does not give.

## Sentences of reason added (file; entry the sentence comes from, read at the base)

- `audit_end.md`, Merge into causes (WAY-281): "A reformatting of the code is no finding." (rule, first) then "One fix removes a source and not a place, so violations of one source listed one by one would read as many problems and hide what to repair."
- `audit_end.md`, Order (WAY-282): "The weight says what is at stake, so it comes first, and within one weight what is left to ask is where the work goes furthest." Placed inside the first paragraph, before "Beside its fix...", because the paragraph ends with a colon that opens a list.
- `audit_end.md`, The top of the list (WAY-283): rule sentence "The list of files marked `do not copy` stands apart from this limit." (first, from the log text at base), then one reason sentence "A few causes with a place and an effect can be weighed by a human who is no specialist and a whole list cannot, so the limit reaches only what the human gets, and the files marked `do not copy` tell the next agent what not to copy."
- `audit_end.md`, Go back (WAY-285): "The human spends attention on the top and a repair may follow it, so each of its causes is read again with one aim, to see whether its effect occurs, which listing it did not ask." Placed inside the first paragraph, before "This is your own check".
- `reading.md` (WAY-217): "A product can knowingly decline guidance through its own decision, and forcing its creation afterwards would cancel that choice."
- `template.md` (WAY-170, end of the opening paragraph): "The form of a file of guidelines misleads no agent that reads it, while what a rule says can and only a reading judges that, but a reference that names no entry does mislead and a check of references finds it in every file at once."
- `template.md` (WAY-169, bullet "A changed entry brings its rules along"): "Guidelines that say something other than their decision are worse than weak ones, since agents go on following the old rule, and the author of the change that moved the entry knows what moved." (the entry's "say in silence other than" I wrote as "say something other than", the same meaning in plain words.)
- `template.md` (WAY-312, bullet "A rule lists no state and repeats no decision or value"): "A sentence that lists what the code or the product is today goes stale when the code changes, and a sentence that repeats a decision or a value of a configuration file is a second copy that drifts from the first." (the orchestrator's addition and the *Rationale* of WAY-312, which stays in the log.)
- `coding/SKILL.md`, Recognize/Extend bullet (WAY-210): "An existing tool, even a worse one, beats a better one brought in, since the code and the people working on it already follow it and two linters over one code disagree."
- `coding/SKILL.md`, section 0 (WAY-266): "A skill of guidelines takes over inside the refinement of a task, whose template and sources `refine-task` has read, and a session that did not pass through that refinement lacks them."
- `coding/kinds.md`, bullet Kinds (WAY-200): first the missing half of the rule, "Where the product holds no file of a kind, the exemplar of that kind is designated by the task that creates its first file." (from the log text at base), then the reason "Who designates the exemplar follows from the state of the product: a first file built with no exemplar is the file every later one copies, and with several files a choice made without comparing them makes whichever file an agent finds into law."
- `coding/kinds.md`, exemplar sub-bullet (WAY-201): "since the human who approves the exemplar does not judge code and someone who is no developer can weigh what the product gains" (clause inside the bullet, so one sentence).
- `coding/recognize.md` first bullet (WAY-208): "An agent left free does something different in every task, and a small part of code drifts as surely as a large one."
- `coding/recognize.md` mode "no code" (WAY-209): the missing second half added first ("and the file of a kind of code comes into being with the task that creates the first file of that kind", from the log text at base), then the reason as a clause: "since the first code written with no standing check is the code every later change copies and checks brought to it afterwards find code to clean".
- `coding/recognize.md` refresh bullet (WAY-278): "Adding these rules covers something new, so it is an extension, and a refresh, which stays within what the guidelines cover, can only notice the absence and put it to the human."
- `coding/starting_set.md` (WAY-211): "since new scope needs a check of whether the existing tools fit it, while updating or correcting accepted rules within their scope needs no new comparison" (clause at the end of the research bullet).

## Rewrites the plan asked for

- `audit_end.md` line 6: "(WAY-280 to WAY-285)" now "(WAY-280, WAY-284)": both stay in the log.
- `reading.md`: "under WAY-200" dropped; the sentence now says `maintain-coding-guidelines` "judges each file, compares them and proposes the exemplar".
- `kinds.md`: the route-of-one-kind sentence says what the comparison is (judges every existing file of the kind, compares them, proposes the exemplar with `copy` or `do not copy` for each file, the human approving the designating decision), and "under WAY-201" is gone; it ends "and no audit".

## Entries left under the "stay" rule

None of the ten numbers (WAY-93, 94, 97, 263, 287, 294, 295, 297, 363, 364) stands in any file of this slice; nothing to leave or to keep. References to numbers that stay (WAY-02, 33, 34, 36, 120, 121, 123, 167, 168, 172, 173, 174, 205, 213, 215, 216, 235, 247, 251, 265, 274, 280, 284, 312 and others) are untouched. WAY-312 and WAY-274 references in `template.md` kept as asked.

## Findings and choices (for the orchestrator)

1. **The first sentence of the former WAY-312 already stood in `template.md`**, almost word for word, in the bullet "A rule lists no state and repeats no decision or value" ("It does not list the state of the product's code or of the product ... it repeats neither a decision of the product's log nor a value taken from a configuration file ...; it says what the author of the code is to do"). I did not add the orchestrator's sentence a second time, since two copies in one bullet would be a drifting duplicate; I added only the missing reason. Cost if wrong: one more sentence is a one-line edit. The bullet lacked "so that what remains is what the author of the code is to do", which the bullet states in the form "it says what the author of the code is to do".
2. **The plan's text for the missing half of WAY-200 and WAY-209 is truncated** ("Missing in kinds.md: 'the exem…'", "the file of a kind of code comes into being wit…"). I took the missing half from the log text of the entries at the base (WAY-200: "Where a product holds no file of a kind of code, the exemplar of that kind is designated by the task that creates its first file"; WAY-209: "the file of a kind of code comes into being with the task that creates the first file of that kind"). `kinds.md` got the WAY-200 half (the plan's primary place) and `recognize.md` the WAY-209 half in the "no code" mode. The "A new kind" bullet in `SKILL.md` keeps stating the first-file half too, so the half stands in two files; the plan's alternative (reason in `SKILL.md`) was not used. Cost if wrong: a sentence moves.
3. The plan says "the human approving the designating decision" for WAY-200 in `kinds.md`; I put it in the rewritten sentence at the route-of-one-kind, which is the one place where the comparison is said, and not in the later "For each kind, judge..." list.
4. WAY-171 and WAY-183, 187, 202, 214, 218, 277, 279 were only removed as the slice says (no reason sentence asked), plus WAY-277 and WAY-210 from the SKILL.md technology-choice sentence (WAY-121 stays).
5. Line-length: two edited lines (`audit_end.md` Order paragraph, `template.md` opening paragraph and the Logging scope bullet) run longer than the 100-character wrap of the neighbours; not rewrapped, to keep the diff to the slice's changes.

## Reaches beyond the dispatch

- Read the slice's section of `plan.md` (only the lines of "Slice 13") to see the full text of the truncated lines in the handoff; the plan itself is truncated at the same points ("add that first"). Why: to find out which half of WAY-200 and WAY-209 the plan meant.
- Read the base `ec7929d` of `foundations/decisions.md` through `git show` into `.runs/executor-13/base.md` and read entries WAY-169, 170, 171, 200, 201, 208, 209, 210, 211, 217, 266, 277, 278, 281, 282, 283, 285 whole there. WAY-312 read whole at the current log.
- Checked by `grep` which WAY numbers stay in the log (headings `### WAY-NN`).

## Working copies

`.runs/executor-13/` held `base.md` (the log at `ec7929d`) and `fc.txt` (the foundation check's output); both deleted one by one before I returned. No worktree or clone made.

## Unread material

- WAY-293 (`foundations/decisions.md`, in the dispatch's *Read*) and the task's *To do* lines 33-40: read the To do lines; WAY-293 not opened (it is the question-form of the decision-log evaluation, with no bearing on the text changed here).
- WAY-171, WAY-183, WAY-187, WAY-202, WAY-214, WAY-218, WAY-279: not read as entries (only removal asked; WAY-171 read at the base anyway).
- The audit_end sections of "Go back" etc. were read whole as part of the file; the other `product-guidelines` files not in the slice were not read.

## Searches not found or unclear

- The plan's text of the "missing part of the rule" for WAY-200 (kinds.md) and WAY-209 (recognize.md), and of the merge rule of WAY-281, is cut off in the plan itself ("..."). Resolved from the base text of the entries as above.
- The orchestrator's additional instruction for `template.md` and the template's own bullet disagree about whether the sentence is absent (it was already there); see finding 1.
