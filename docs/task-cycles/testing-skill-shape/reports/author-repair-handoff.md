# Repair before review — the author's foundation step

Same worktree, branch, method and rules as `reports/author-handoff.md`. This is not a review's fix:
no review has run. It answers one point your report left unclear and supplies one step your report
does not show. Head at dispatch: `d024d56`.

## 1. Row 1 is written in WAY-256, in place

Your report names as unclear whether row 1 should extend WAY-256 itself. The answer, from the
sources:

- `elements/decisions/skill/decide_entry.md:9-10`: a question the log already answers takes an edit
  of that entry in place. WAY-256 asks "Where does a fragment of a skill stand?"; your WAY-265 asks
  the same question for one more case.
- Row 1 calls itself "Rozszerzenie WAY-256"; *Decisions in play* marks every decision "nie zmienia
  się" except WAY-256.
- WAY-30: the approval of a task document, "including a change carried by a row of *Settlements to
  record*", answers the question WAY-114 requires. Your choice 7 gave WAY-30 as the reason against
  the edit; it is the permission for it.
- Question 8's "WAY-256 się nie zmienia" rejects a first-step exception and rules nothing on row 1.

So: withdraw the entry WAY-265 before the merge by removing it, never by listing it among the
withdrawn identifiers, since no merged text carries it. Write row 1's meaning into WAY-256 by
"Changing a decision" in `elements/decisions/template.md`: its binding sentences with the sentence
on a fragment some steps need, its *Verification* with a complying and a violating case, its
*Rationale* and *Rejected* with what WAY-265 carried for them. Keep the sentence "Fragments that
stand unchanged are not bound by it." as one sentence covering both cases, and keep the row's
wording of the rule. `instruction-files/kind_skill.md` then cites WAY-256 for the third answer and
in its question.

Rows 2 and 3 answer other questions and stay entries of their own. Give them the next free numbers
in order, WAY-265 and WAY-266, and correct every citation of them: the step 0 sentence in both
skills, `assessment.md`, your report's figures of identifiers, and any file beside the skill.

## 2. The search of the foundation

`elements/common/way_of_working.md`, "2. Search the foundation", binds you for each entry you write
or change, WAY-256 included, and `task-cycle/skill/foundation_step.md` names it. Your report does
not show it. Make it now, once, over the whole of `foundations/`: the entries that name the entry or
that it names, and those no written link joins to it, not only those a link or a shared *Scope*
leads to. Read each entry the search finds whole, its *Rationale* and *Rejected* included. Answer
also its two questions, on glossary terms and on what entries wait for, and what
`elements/decisions/skill/decide_entry.md:11-13` adds. Each finding becomes a link, a change to an
entry, or, where you cannot settle it, a question in your return. In your report name what you
searched for and what it found.

## 3. Your reading

Read whole every decision your rebuilt files cite beside a sentence you moved and reworded, and each
of the five kinds of base fragment your report counts as reworded. The other reading your report
names as partial stays as you reported it; the reviewer selects its own foundation.

## Checks and report

Run again `python -B elements/common/foundation_check.py`,
`python -B instruction-files/check_instructions.py .` and your `verify_reports.py`. Do not rewrite
history: new commits on the branch, by `git add <paths>`. Do not run the whole gate.

Report: `.runs/task-cycles/testing-skill-shape/reports/author-repair.md`, with each check's command
and exit code, every choice with the way not taken, reaches, concerns and **Searches not found or
unclear**. Return: your status, your commits, a one-line check result naming what failed or did not
run, and the report's path.
