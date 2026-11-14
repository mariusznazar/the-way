# Report of the executor of slice 15 (Guidelines: the styleguide)

**Status:** done

**Commits:** `93f1989` — "Remove the withdrawn decision numbers from the styleguide skill files and give each rule its reason" (9 files, +81 -61): `SKILL.md`, `audit.md`, `new_tools.md`, `recognize.md`, `research.md`, `settle.md`, `starting_rules.md`, `task_document.md`, `template.md`, all in `product-guidelines/styleguide/`.

## Checks

- `python -B elements/common/foundation_check.py` — exit 1 (as expected until the last slice); it prints no line for any file of `product-guidelines/styleguide/` (`| grep -c styleguide` gave 0; before the change it listed 63 lines).
- `python -B agent-instructions/skill_entry_points.py` — exit 0, "entry points are current".
- Not run: the product's gate and `gate/run_tests.py`, per the handoff.

## Own-work check (make-change section 3)

Requirement most likely unmet: "no file of the slice names a number that left, and each reason sentence says only what the entry's *Rationale* gives". Check: grep of the nine files for every withdrawn number of the slice (266, 187, 185, 186, 183, 184, 182, 192, 169, 170, 171, 176, 177, 178, 180, 189, 191, 80, 86) found none; then each reason sentence compared with the *Rationale* of its entry at the base `ec7929d`. They name no file, count or measurement. I also checked no added line is longer than the files' 100-column wrap (two lines I had made long were rewrapped).

## Reasons added (file, sentence, entry)

- `audit.md`, bullet "Audit in both directions" — "Each direction finds what the other misses: a file of design tokens nothing reads shows only from the source, and a value no token covers only from the screen." (WAY-187, *Rationale*, first sentence).
- `audit.md`, fallback bullet — "A product with no decided way to the running product is audited from its code rather than left waiting for a task that settles it." (WAY-187, *Rationale*, last sentence).
- `recognize.md`, first bullet, after "...this task covers." — "A small or helper user interface left without one is styled in each task its own way, and a screen nobody outside the team sees still needs one meaning for each colour." (WAY-183, *Rationale* and *Rejected*).
- `recognize.md`, "Extend what exists." — "An existing system, even a worse one, beats a better one brought in, since the screens already read it and a second one splits them in two." (WAY-185, *Rationale*).
- `settle.md`, "Accessibility" bullet — "A threshold written into an invariant with no adopted catalogue is a number from WCAG without its source, and no reader can tell which edition it follows." (WAY-191, *Rationale*).
- `starting_rules.md`, opening — the missing rule sentence added first, "The styleguide of a user interface comes into being before that user interface's first screen." (WAY-184 binding sentence), then its reason "A first screen built with no rules is the screen every later one copies." (WAY-184, *Rationale*). The file had no sentence of the timing rule (SKILL.md's description and `recognize.md` only touch it).
- `starting_rules.md`, research bullet — "Research with sources keeps the quality of the rules where a fixed list in the-way would fit no technology well, and a refresh needs none, since correcting accepted rules within their scope needs no new comparison." (WAY-186, *Rationale*).
- `task_document.md`, `maintain-instruction-files` bullet — "A styleguide no instruction leads to is not found by an agent in a new session, and a path with its condition costs one line and is read when the condition comes;" (WAY-192, *Rationale*).
- `template.md`, "Every background with its text" — "A background never stands alone: its text decides whether anything on it can be read, so the two are written together." (WAY-176, *Rationale*).
- `template.md`, "States of shared controls" — "The states other than the default are the ones that drift first and that a screenshot of a screen with data never shows." (WAY-177, *Rationale*).
- `template.md`, "A fault of one screen is fixed in its component" — "A global design token is read by every screen, so changing it for one screen changes what all the others show, unseen by the task that made the change." (WAY-178, *Rationale*).
- `template.md`, "Every value with its source" — "Values that live only in a conversation are values the next session invents again, so each keeps its source where it stands." (WAY-182, *Rationale*).
- `template.md`, "The kitchen-sink page" — "The page shows in one place what the text says of every state, for an agent checking its work and for a reviewer, while a screen with data shows only one state." (WAY-180, *Rationale*).

## Rewrites named by the plan

- `settle.md`: "with its source as WAY-80 gives it (WAY-191)" is now "with its source in the form the environment-facts template gives (section Source)" (section `## Source` exists in `elements/environment-facts/template.md:98`). "the three first invariants WAY-189 gives, each with..." is now "the three first invariants, each with...".

## Entries left under the "stay" rule

None of the ten (WAY-93, 94, 97, 263, 287, 294, 295, 297, 363, 364) is named in the nine files, so none was touched. References to numbers outside the slice's list (WAY-165, 29, 123, 121, 120, 251, 173, 150, 174, 134, 167, 60, 168, 284, 172, 225, 51, 213, 05, 107, 265) are left as they were; the foundation check raises none of them.

## Choices and mismatches

- **Plan contradiction:** the section says "remove WAY-191 (line 16, 18, 25)" and, for line 18, "keep (WAY-191)". WAY-191 has left the log, so I read "keep" as "keep the parenthesis position during the rewrite" and removed it too (the goal says no file names a number that left; the check lists it). Cost if wrong: one reference to restore.
- **Placement in `template.md`:** the plan says "end of bullet" for WAY-177, 178, 180, 182. The end of those bullets is the *Invariant* field, and a trailing sentence there would read as part of the invariant. I put each reason directly after the rule text, before *Decision*. WAY-176's reason sits in the "Every background with its text" bullet (the plan's second option). Cost if wrong: move one sentence per bullet.
- **WAY-187 two places:** I read "line 9 ... and after line 15" as one sentence at each of the two places.
- **One reason per rule where the plan said "or":** WAY-184 (timing, no separate sentence for the width bullet), WAY-186 (the research bullet, not the preferences bullet).
- For the numbers the plan only asks to remove (WAY-169, 170, 171, 266, 86 and the rest not listed above) no sentence was added.

## Reach beyond the dispatch

`elements/environment-facts/template.md`, headings only (grep of `^#`), to confirm the section name "Source" for the rewrite in `settle.md`. Also `the task's note in the author's backlog` (the author's script rules, read before an editing script).

## Unread material

- The plan and the whole task: not opened, as `slice.md` gives (read the task lines 1-70 only, which hold To do 1-6).
- WAY-293: read whole at its current place (`foundations/decisions.md:7171`).
- WAY-176, 177, 178, 180, 182, 183, 184, 185, 186, 187, 189, 191, 192 and WAY-80: read whole at the base `ec7929d` (`git show ec7929d:foundations/decisions.md`, lines 5682-6075 and 1994-2054). WAY-169, 170, 171, 266 and 86: not read, since the slice only removes their numbers.
- All nine files changed were read whole before the change, except `SKILL.md`, which I read in lines 1-30 and 60-90 and then, after the commit, in lines 30-60 and 90 to the end (a bare count of lines, not the text); the only change there is the one number at base line 74. Partial read, named.

## Searches not found or unclear

- None unclear except the plan contradiction on WAY-191 line 18 above. The plan's line numbers (base lines) matched by search of each number.

## Working copies

`.runs/executor-15/` held `edit.py` (the editing script), `base.md` (a copy of the base decision log) and `fc.txt` (output of the foundation check). All three removed before return.
