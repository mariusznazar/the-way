# Planner report — decision-log-reading-index

Status: done with concerns

- Plan: `.runs/task-cycles/decision-log-reading-index/plan.md`
- Size report: `.runs/task-cycles/decision-log-reading-index/plan-size.md` — five slices, every one
  `fits` (25 440 to 53 224 estimated tokens, 2 to 4 files to change); `python -B
  task-cycle/slice_size.py .runs/task-cycles/decision-log-reading-index/plan.md` exit 0.
- Commits: none. No code, test or foundation entry written.

## Open design choice and reserved choice

None. The change needs no language, library, store or place to run beyond what the foundation
settles (Python standard library, WAY-38), so `reserved_choices.md` was not opened. Every choice
the plan takes is a choice of how to make what the task settles and stands under *Choices*.

## The plan in short

- Foundation entries F1–F9 (WAY-150 for rows 1–3, 5, 6; WAY-18 for row 4; WAY-339 for row 7;
  WAY-287 and WAY-21 as consequences) and F10, the division of the log into 20–30 sections, all made
  by the agent of the foundation entries before Slice 1, the division as one commit of its own.
- Slice 1 — the index script `elements/common/decision_index.py` with tests, and the part map's
  sentence of `elements-common`.
- Slice 2 — the comparing script `elements/common/compare_log_entries.py` with tests, a test that
  the foundation check reads a log with sections, and the confirmation of F10 by the script.
- Slice 3 — "Reading the foundation", the decisions template, the two files of
  `project-level/lead/` that restate "whole selected entries".
- Slice 4 — the reviewer's instruction, **Unread material**, the paragraph of
  `task-cycle/skill/SKILL.md` that holds WAY-326's rule, the request template (item 14 and the new
  section in **Foundation entries**).
- Slice 5 — `task-cycle/cycle_measures.py` with tests; trust boundary, so a review of its own aimed
  at crafted transcript input.

Where the reading rule, the template and the other restating files are edited: Slice 3
(`elements/common/way_of_working.md`, `elements/decisions/template.md`,
`project-level/lead/skill/SKILL.md`, `project-level/lead/answering.md`) and Slice 4
(`task-cycle/review/SKILL.md`, `task-cycle/skill/SKILL.md`, `task-cycle/skill/request_template.md`).

## Concerns

1. **The task's numbers and two of its decisions are older than the base.** The task was written on
   `f4af75d` (331 decisions); at the base `21ecb62` the log holds 198 decisions, and WAY-326 and
   WAY-347 are withdrawn (`foundations/decisions.md`, the list "Withdrawn identifiers": WAY-326's
   rule "stands in `task-cycle/skill/SKILL.md`", WAY-347's "is a paragraph of WAY-339"). The plan
   sends row 7 to WAY-339 and *To do* 4's "WAY-326" to its paragraph in `task-cycle/skill/SKILL.md`.
   Proposed answer: keep that mapping; the request says it.
2. **"20–30 sections po kilkanaście wpisów" cannot both hold over 198 entries.** 20–30 sections give
   some 7–10 entries each; "kilkanaście" gives 11–18 sections. The plan keeps 20–30, which both
   *To do* 5 and the answer to question 3 give, and records the departure from "kilkanaście" under
   *Choices*. Proposed answer: keep 20–30; the human accepts the list at the merge anyway.
3. **WAY-287 is changed, though no row of *Settlements to record* names it.** Its binding sentence
   names "the incomplete reading of the review of the whole change where its reviewer did not run
   through the rest of its selection by title" (`foundations/decisions.md:6994-6998`), and its
   examples and rationale do the same. *To do* 4 has the reading by title leave "every place of
   the-way that describes it today", so I hold this a consequence of F1 settled by the task (F8),
   not an open design choice. Proposed answer: confirm F8 as a consequence entry.
4. **The division of the log is foundation work, not a slice.** `task-cycle/slice_size.py` counts a
   file of *Change* as read whole, and the log is 721 002 characters (about 288 000 tokens), over the
   limit of 150 000 for any slice that changes it; the same was done in the plan of the cycle
   `decision-log-second-round` (its plan, line 7, at commit `cfd275c`). This leaves the agent of the
   foundation entries with five decisions to rewrite and 198 entries to assign. Proposed answer: the
   orchestrator may dispatch F10 to a second agent of the foundation entries after F1–F9; the plan
   allows it.
5. **The handoff's hint about `blocks` does not hold.** `blocks(lines, "### ")` in
   `elements/common/foundation_check.py:240-250` closes the open block at any line that starts with
   `#`, so a `## ` section heading and its sentence fall into no entry; the check needs no change for
   sections. Slice 2 pins this with a test. `migrate_foundation.py`'s `segments` cuts at headings up
   to level 3 and keeps a section's lines; `installation/install.py` writes a log with no entry. The
   reading rule's "to the next heading (`###` in the decision log …)" (`way_of_working.md:81-82`)
   is the one consumer that changes, in Slice 3.
6. **The measures' consumer.** `process-audit/audit_count.py` reads the cycle-level lines of
   `mechanism_measures.md` by label (`read_measures`, `header_fields` at 644-665, where a label
   followed by " and " counts as that label). The new measures go into four columns of the table of
   agents and no cycle-level line is added; the series of these measures restarts by itself when
   `cycle_measures.py` changes (audit_count.py docstring, 129-145), so nothing is recorded in
   `process-audit/`. The audit will not show the new measure; that is a later task if wanted.
7. **The Codex form of a tool call is unverified.** I read no Codex rollout; Slice 5 confirms the
   form from a real rollout or gives a Codex agent's four figures as `unknown`.

## Questions

None that hold the plan. Each concern above carries its proposed answer.

## Order of work

The-way has no guideline files of its own, so there is no styleguide example of an order of work
and no rule of size (WAY-365 asks nothing). The order follows dependencies: the entries and the
division first, the index script before every slice that names it, the comparing script after the
division it confirms, the rule before the reviewer's instruction that follows it.

## Guidelines found missing or uncertain

None for this change: the-way departs from a product's coding and testing guidelines by WAY-328;
`product-guidelines/reading.md` was not opened, as the dispatch allowed.

## Reaches beyond the dispatch

- `foundations/decisions.md`, WAY-287 (6992-7103) — found by a search for "by title"; it restates the
  reviewer's reading by title, so it enters the plan as F8.
- `foundations/decisions.md`, WAY-339 (8172-8243) — the successor of the withdrawn WAY-347, named in
  the withdrawn list.
- `foundations/decisions.md`, WAY-07, WAY-09, WAY-19, WAY-38, WAY-48, WAY-260, WAY-328, WAY-344 — for
  the slices' *Read* and the rules on scripts, trust boundaries and missing fields.
- `foundations/invariants.md` whole (376 lines) — for the invariants with *Part* `every` and of the
  touched parts.
- `process-audit/audit_count.py` (95-160, 176-187, 644-665, 1478-1512) and
  `process-audit/test_audit_count.py` (1430-1437) — the reader of the measures file; found by a search
  for `mechanism_measures`.
- `task-cycle/review/whole_change.md` whole, `task-cycle/skill/request_template.md` (250-270,
  465-489), `task-cycle/skill/SKILL.md` (58-66, 234-280, 548-566) — the places that restate the
  reading.
- `project-level/lead/skill/SKILL.md` (30-37), `project-level/lead/answering.md` (5-10),
  `project-level/task/skill/carry_foundation.md`, `project-level/task/skill/read_sources.md`,
  `project-level/technology/start.md` (5-14), `project-level/skill/read_foundation.md`,
  `elements/part-map/skill/SKILL.md` (20-25) — the files that cite "Reading the foundation", found by
  a search for that phrase and for WAY-150.
- `task-cycle/slice_size.py` (1-62) — the limits.
- The plan and size report of the cycle `decision-log-second-round` at commit `cfd275c` — how a plan
  handled a slice that changes the log.

## Working copies

- `.runs/planner/heads.txt` and `.runs/planner/scopes.txt` — the heading lines of the log and the list
  of decisions by *Scope* for the parts `decisions`, `elements-common`, `process-audit`, `gate`,
  `installation` and `task-cycle`. Both removed, and the directory `.runs/planner/` with them.

## Unread material

- `foundations/decisions.md`: of the decisions whose *Scope* names `decisions` (72), `elements-common`
  (27), `task-cycle` (96), `process-audit` (11) and `gate` (19), I read whole the entries the
  dispatch names (WAY-150, WAY-18, WAY-21, WAY-05, WAY-12, WAY-02, WAY-52, WAY-33, WAY-135, WAY-136,
  WAY-229, WAY-160, WAY-243, WAY-161, WAY-162) and those named under reaches; the rest by heading
  only, as the dispatch allowed ("read whole what bears on your cut"). WAY-326 and WAY-347 do not
  stand in the log (withdrawn).
- `elements/common/foundation_check.py`: 1-30, 96-160, 236-345, 410-459, 925-989 and a search of its
  headings; not whole.
- `elements/common/test_foundation_check.py`: 1-30, 150-260 and a list of its tests; not whole.
- `elements/common/migrate_foundation.py`: 1-70, 133-153, 355-424, 872-877 and a search; not whole.
- `elements/common/test_migrate_foundation.py`: a search for the log only; not read.
- `task-cycle/test_cycle_measures.py`: the list of its helpers and tests only; not read.
- `task-cycle/review/SKILL.md`: 18-60 and 160-185; not whole.
- `task-cycle/skill/SKILL.md`: 58-66, 234-280, 548-566; not whole.
- `task-cycle/skill/request_template.md`: 250-270, 465-489 and its headings; not whole.
- `elements/decisions/template.md`: 1-40, 168-203 and its headings; not whole.
- `installation/install.py` and its tests: the lines that name the log, found by a search; not read
  further.
- `process-audit/SKILL.md`: a search for "series" and "measures" only.

## Searches not found or unclear

- WAY-326 and WAY-347 as entries of the log — not found; both are withdrawn, their rules standing in
  `task-cycle/skill/SKILL.md` and WAY-339.
- The task's counts (331 decisions; 191 for this task's parts) — unclear at the base, which holds 198.
- "20–30 sekcji … po kilkanaście wpisów" — unclear over 198 entries (concern 2).
- The handoff's hint that a `## ` heading would join the body of the entry before it — not so in
  `foundation_check.py` (concern 5).
- The form of a tool call and its output in a Codex rollout — not found in the repository's tests,
  which hold only `session_meta` and `token_usage_record`; no real rollout read.
