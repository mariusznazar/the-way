# Author report — the return step of correction 1, relations-todo-for-unwritten-decision

**Status:** done

**Commits:** none. The comparison found nothing that no longer matches, so nothing is committed; the head
stays `000a7639dc1b819dfa766d6690a7d00b1a3c551e`, the worktree is clean (`git status --short` empty).

## What was compared

Read: `task-cycle/skill/return_step.md`, the handoff, `reports/correction-1-remarks.md`,
`reports/author-correction-report.md`, the first part of `reports/review-correction-report.md` (`PASS`, and its
Minor findings m-a and m-b). `foundation_step.md` was read in the first stage of this cycle, not again; its
marking rule is applied in the correction's report.

Compared with the files of the repository: WAY-287 (its sentence, its *Verification* violates line and its
*Rationale*, now each naming a decision's *Based on* or *Relations*), the fact `foundations-branch-ruleset`
(`foundations/environment_facts.md`), WAY-16 (the decision whose *Based on* names the fact), WAY-71 (the rule
of the form the places stand on), item 16 of `task-cycle/skill/request_template.md`, `elements/common/rules.md`,
`elements/decisions/template.md`, `agent-instructions/README.md` ("Check the change"),
`installation/README.md` (the paragraph on the result of each job), `.github/workflows/tests.yml` (header) and
the part map.

## Items of the record's *Return step*

- **Foundation compared with code:** matches.
  - The four places of a described `TODO` agree across WAY-71, `rules.md`, the decision template, WAY-287 and
    item 16 of the request template (invariant's *Rests on* and *Derives from*; decision's *Based on* and
    *Relations*).
  - The fact says `tests` and `tests-windows`; `agent-instructions/README.md`, the header of `tests.yml` and
    `installation/README.md` ("the result of each job is a required check ... the rule names the check") say
    the same or no single check. WAY-16 names no single check (its sentence and *Verification* say "a check the
    repository requires" and "required check with a bypass for the owner"); the review read WAY-16 and WAY-287
    whole and found none either.
  - **Beyond that, the comparison finds nothing:** no invariant, no part-map entry and no glossary entry names
    the ruleset or a single required check (a search of `foundations/invariants.md`, `part_map.md` and
    `glossary.md` for `required`, `ruleset` and `branch rule` gave only unrelated lines on required sections).
- **Decisions:** none written or changed in this step.
- **Invariants:** none written; no rule set by the task, a decision or the human asks for one.
- **Environment facts:** none new; `foundations-branch-ruleset` was changed by the correction and stands as
  the correction's review passed it.
- **Glossary terms:** none.
- **Part-map changes:** none (no file added, removed or moved by the correction; the entries `decisions` and
  `environment-facts`/the parts that hold the files it touched are unchanged in what they claim).
- **Projected entries:** none.
- **Rows of *Settlements to record*:** none (the section reads `none`).

## Not done, by design

The review's two Minor findings go to the request's list, not fixed here: m-a (WAY-287's complies list gives no
example of a *Relations* `TODO`) and m-b (two reflowed lines of WAY-287 run wider than the paragraph).

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — 0, `0 errors`, on the head (run as a compare; nothing was
  committed, so no test directory was run).
- Not run: the full gate (CI is the final gate).

## Own-work check

Requirement most likely not met: no sentence resting on the old single required check remains. Check: a
search of the whole repository for `foundations_tests`, `tests-windows`, `required check`, `ruleset` and
`status check` (outside `.runs/`) found the fact, WAY-16, the two READMEs and the workflow header, each read
as above; none states one check as the rule.

## Reach beyond the dispatch

None.

## Unread material

`reports/review-correction-report.md` was read from its first lines (verdict, range and the Minor findings),
not through to its end; `reports/review-whole-report.md` was not read again. Nothing else the handoff names
was left unread.

## Searches not found or unclear

None.

## Working copies

None made in this step; `.runs/author/` does not exist (removed after the correction).
