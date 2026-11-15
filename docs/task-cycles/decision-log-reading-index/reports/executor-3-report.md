# Report of executor 3, slice 3 (the reading rule and the template of the log)

**Status:** done with concerns (the concerns are about wording in `foundations/decisions.md`, which this slice does not change)

## Commits

- `3cec41a` Give the reading rule the index of the selected decisions and the selection by topic, and the decisions template the topical sections of the log

## Files changed (added / removed lines)

- `elements/common/way_of_working.md` +36 −12 — "Reading the foundation", step 2 rewritten
- `elements/decisions/template.md` +11 −6 — "Where entries go" (F4), "Withdrawn numbers", three rows of "Fields and their readers"
- `project-level/lead/skill/SKILL.md` +3 −2 — step 0 reads the index and the decisions the method opens whole
- `project-level/lead/answering.md` +2 −2 — same

## What each file now says

- `way_of_working.md` step 2: the agent that selects runs `decision_index.py --output PATH` into a file of its own working
  directory (in a cycle, its directory for working copies). Sectioned log: `--sections`, choose sections by heading and
  sentence, then `--section` for each and `--part` for each touched part (decisions outside the sections by heading alone,
  run through by their questions, opened whole where the question points to a bearing: F3). Log without sections: `--part`
  per touched part, the index stands in for the whole reading (F6). `--decision NUMBER` adds the decisions the task's
  *Decisions in play* or the work's source names and those whose sentence a test the work alters holds by a line
  `decision:`, as step 3 adds the invariants such a test cites (F5). Whole only: changed, gone against, answered otherwise
  (with *Rejected*), named, held by a test the work alters, left open by binding sentences (F1). An entry read whole runs to the
  next heading of any level. The reviewer of the whole change reads the index of its whole selection and states how many it read
  whole; "skims the rest by title" and "no other agent skims" are removed; only the run through the headings outside the
  sections stays. The search of `- **Scope:**` lines by hand is replaced by `--part`. Steps 3 and 4 and the closing paragraph
  (invariants, part map, glossary, templates read as before) are unchanged.
- `template.md`: the first point of "Where entries go" gives F4 (sections with one sentence, new entry at the end of its
  section, else a new section at the end of the log before the list of withdrawn numbers, named by the request; a log without
  sections takes it at its end). "Withdrawn numbers" keeps the list after the last entry and says that in a sectioned log it
  stands after the last section and is no section.
- `project-level/lead/skill/SKILL.md`, `answering.md`: "whole selected entries" is replaced by "the index of the selected
  decisions and the decisions that method opens whole".

## Checks (command and exit code)

- `python -B elements/common/foundation_check.py --skip-test-citations` — exit 0, `0 errors`.
- `python -B -m unittest discover -s elements/common -p "test_*.py"` — exit 0, 231 tests OK (199 s; it ran in the background
  after passing the foreground limit).
- `python -B instruction-files/check_instructions.py .` — exit 0, `0 error, 0 warn, 3 info`. It follows the files named from
  the root `AGENTS.md`/`CLAUDE.md` and the skill entry points; I did not verify that it reads my four files (the lead `SKILL.md`
  may be reached through `.claude/skills`), so its covering my files is unconfirmed.
- Run of the method on slice 3's parts (`elements-common`, `decisions`, `project-level`), working directory `.runs/executor-3/`:
  - `python -B elements/common/decision_index.py --sections --output .runs/executor-3/sections.md` — exit 0, 28 sections.
  - I chose from that list: "Decision entries and the decision log", "How skills write and read the foundation",
    "Review of a change", "Task refinement and readiness".
  - `python -B elements/common/decision_index.py --output .runs/executor-3/index.md --section "Decision entries and the decision log" --section "How skills write and read the foundation" --section "Review of a change" --section "Task refinement and readiness" --part elements-common --part decisions --part project-level --decision WAY-150 --decision WAY-18 --decision WAY-21`
    — exit 0, `Listed in full: 30. Listed by heading alone: 84.`, 38,686 bytes.
  - Run through the 84 headings; none was opened whole beyond what the handoff names (WAY-07 and WAY-02 came nearest; WAY-02 is
    in the handoff's list, WAY-07's rule of editing in place is not touched by this slice).
  - Decisions read whole by me: 9 — WAY-150, WAY-18, WAY-21, WAY-02, WAY-05, WAY-12, WAY-19, WAY-33, WAY-52 (the handoff's list).
  - A log without sections, a copy of the log with the `## ` headings other than the withdrawn list stripped:
    `--part decisions --decision WAY-150` — exit 0, 72 in full, 0 by heading; `--sections` — exit 0, `Sections: 0`. So the rule's
    two branches behave as it states. The copy was removed.

## Own-work check (WAY-164)

- Requirement most likely not met: "no file restates whole reading of every selected decision", and "the reading by title leaves
  the rule" — in the files this slice changes.
- Check: `grep -nE "whole selected|by title|skim|no topical sections"` on the four files — only the negation in
  `way_of_working.md:110` ("It reads no decision of its selection by title") remains; a repository-wide search for
  `decisions? (found|selected) … whole` and `selected entr` outside `foundations/decisions.md` finds only
  `way_of_working.md:94` (the sentence for a log without sections). Other places that still describe reading by title —
  `task-cycle/review/SKILL.md` lines 30–31 and 173–174, `task-cycle/skill/SKILL.md` line 275,
  `task-cycle/skill/request_template.md` lines 260–265, `task-cycle/test_remarks_check.py:204` — are outside this slice
  (the plan's Slice 4 or later, by the task's *Context*); I did not touch them.

## Choices (with the way rejected and its cost if wrong)

- I gave the template's "Fields and their readers" table the index as a reader of the question, binding sentences and *Scope*
  (WAY-05: a field stays only while someone reads it). Rejected: leave the table alone — the table would then say less than is
  true; the slice did not name it. Cost if wrong: three table cells to take out.
- "Withdrawn numbers" got a clause (after the last section, no section itself). Rejected: no edit, as the slice says only "keeps
  that list after the last entry" — in a sectioned log "after the last entry" is read as inside the last section.
- The sectioned-log branch of step 2 gives the commands and lets the word "section" mean a `## ` heading other than the list of
  withdrawn numbers, which is how the script reads it (docstring).
- In the lead `SKILL.md` and `answering.md` I wrote "the index of the selected decisions and the decisions that method opens
  whole" rather than restating the method (the files cite it).

## Reaches beyond the dispatch

- `elements/decisions/skill/read.md` (7 lines) — found by the search for what the decisions skill reads; it points to "Reading
  the foundation" and needs no change.
- `foundations/decisions.md` lines 1–30 and the last headings (to see the log's opening and the withdrawn list), and
  `.runs/.../reports/foundation-entries-report.md` lines 290–330 (concerns) — to see what the foundation step left to this slice.
- `instruction-files/SKILL.md` first 40 lines and the head of `check_instructions.py` — to run the check.

## Working copies

- `.runs/executor-3/`: files `fc.txt`, `ifc.txt`, `ut.txt` (outputs of the checks), `sections.md`, `index.md` (the run of the
  method). Kept in the ignored directory for the orchestrator to read; no worktree or clone was made. The copy of the log
  without sections was removed. Remainder: none.

## Concerns

1. `foundations/decisions.md` WAY-150, first paragraph, reads "opens whole only those … and it reads every other selected entry
   whole, reading more entries where relevance is uncertain and a whole file only where it is short". "Only" and "every other
   selected entry whole" contradict each other, and the second clause gives back the whole reading the entry replaces. I did not
   change the decision (the handoff forbids it) and wrote the method after the "only" clause and the Rationale. The phrase should
   be looked at in the review of the foundation entries; if it is meant for the entries of steps 3–4 (map, invariants, links),
   it should say so.
2. WAY-21's *Rationale* ("measured on 2026-11-15 …, about half of them name the part of the task cycle") is already named as a
   concern in the foundation-entries report; nothing in this slice depends on it.

## Unread material

- none of the files and passages the handoff names was left unread. Read whole: the handoff, `task-cycle/change/SKILL.md`,
  `slice.md`, WAY-150 (1465–1589), WAY-18, WAY-19, WAY-21 (713–825), WAY-02 (393–438), WAY-05, WAY-12 (604–712), WAY-33,
  WAY-52, `elements/decisions/skill/SKILL.md`, `decide_entry.md`, `elements/common/rules.md`, the four files I changed, and the
  first 120 lines (the docstring and the first functions) of `decision_index.py`. The passages of the task are copied in the
  handoff; I did not open `task.md` or `plan.md` themselves, and the line ranges of the decisions in `foundations/decisions.md`
  that the *Read* of the slice lists (for example 37–81 for WAY-02) differ from the handoff's current ones, which I followed.

## Searches not found or unclear

- The handoff's *Read* gives two sets of ranges for the same decisions (the plan's old ones, e.g. WAY-02 37–81, and the current
  ones, e.g. 393–438); I took the current ones, as `slice.md` says.
- Whether `instruction-files/check_instructions.py` covers the four changed files: unclear (see Checks).
- I found no sentence in the handoff or the task for what `PATH` of the index should be in a cycle; I took the agent's directory
  for working copies, as WAY-18's verification says "a file of its own working directory".
