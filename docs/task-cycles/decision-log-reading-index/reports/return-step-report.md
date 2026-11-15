# Report: the return step, task `decision-log-reading-index`

- **Status:** done
- Worktree `the task's worktree`, branch `task/decision-log-reading-index`, head
  `e82cbab6ea2d63939f85c9dcb6edbd74e6df517b`, base `21ecb627f885de438e2209d7ff5c137b1e1b9d83`.
- **Commits:** none. Nothing needed to change; the tree is as the earlier stages left it.

## Checks

| Command | Exit code | Result |
|---|---|---|
| `python -B elements/common/foundation_check.py` (full, test citations included) | 0 | `0 errors` |
| `python -B elements/common/compare_log_entries.py <log at 104e126> foundations/decisions.md` | 1 | differs in WAY-18, WAY-21, WAY-150, WAY-287 only: the entries the two fix rounds reworded (commits `0023a28`, `dbdfdad`, `d6599c7`); expected |
| `python -B elements/common/compare_log_entries.py <log at 21ecb62> foundations/decisions.md` | 1 | differs in WAY-18, WAY-21, WAY-150, WAY-287, WAY-339 only; the other 193 entries stand byte for byte as at the base |
| `python -B elements/common/decision_index.py --sections --output ...` | 0 | lists 28 sections |
| `python -B elements/common/decision_index.py --part elements-common --part decisions --part task-cycle --section "How skills write and read the foundation" --decision WAY-150 --output ...` | 0 | 5 decisions in full, 132 by heading alone |

The full gate was not run (the orchestrator runs it).

## Foundation compared with code

Compared, each whole where it is an entry: WAY-150, WAY-18, WAY-21, WAY-287, WAY-339 as they stand; WAY-05, WAY-12, WAY-02, WAY-52,
WAY-33 (no change needed: the index takes the paragraphs before the first field, as WAY-05 gives them; WAY-12 and WAY-02 give the line
`decision:` that step 2 of the reading rule now adds from; WAY-52 concerns the part map only; WAY-33's search stays in step 2 of the way
of working); WAY-326 and WAY-347, withdrawn, with their rules at their places (`task-cycle/skill/SKILL.md:274-276`, the
`task-cycle/skill/SKILL.md` paragraph on the measures, and the second paragraph of WAY-339); the `Withdrawn identifiers` table of the
log and of the part map; the entries of `decisions`, `elements-common` and `task-cycle` in `foundations/part_map.md` with their files;
`foundations/glossary.md` (headings and the entries of "binding part", "binding sentence", "entry", "return step"); `foundations/invariants.md`
and `foundations/environment_facts.md` by search for the log, a section, an index.

What I found matches the code:

- WAY-150 against `elements/common/decision_index.py` and "Reading the foundation" (`elements/common/way_of_working.md:73-112`): the
  switches `--sections`, `--section`, `--part`, `--decision`, the full and by-heading listing, the opening range "to the next heading
  of any level" and the reviewer's count agree; step 3's whole reading of the entries the index links to agrees with WAY-150's first
  paragraph.
- WAY-18 and the template's "Where entries go" and "Withdrawn numbers" (`elements/decisions/template.md:11-18, 190-195`) say the same of
  sections, the new section at the end before the list of withdrawn numbers, and a log without sections.
- WAY-339 against `task-cycle/cycle_measures.py` (docstring, lines 33-71): the bytes and the reads of the log and of the index, for each
  agent, in the table of agents; `process-audit/audit_count.py` reads the cycle-level lines of the file by label, which this change does not
  alter, so the audit starts a new series by the change of the script (WAY-339, WAY-350) and shows no new figure, as the cycle's choice Q5 says.
- WAY-287 against `task-cycle/skill/request_template.md:258-268` (item 14) and the **Foundation entries** paragraph (new sections named).
- WAY-326's rule against `task-cycle/skill/SKILL.md:274-276` and `task-cycle/review/SKILL.md:169-176`: a decision the reviewer knows from the
  index and did not open is no gap.
- A search of the whole tree (without the log, without `.runs`, without tests) for `by title`, `title only`, `skim`, `titles` and
  `no topical sections` finds only `elements/common/way_of_working.md:110`, which says the reviewer reads nothing by title. A search of the
  log for them finds only WAY-150's *Rejected* and *Rationale* (the way weighed and refused, and the contrast with the index), and
  entries on other subjects. A search for "in the order they were written", "at its end", "end of the log" finds WAY-18 and the template,
  both worded for a log with and without sections. No file still says that a reader reads by title or that the log has no sections.
- Files that name the reading method without restating it (`project-level/lead/*`, `project-level/*/read*.md`, `elements/*/skill/read.md`,
  `task-cycle/plan/SKILL.md`, `task-cycle/spec/SKILL.md`, `task-cycle/change/SKILL.md`, `task-cycle/skill/SKILL.md` on the handoff) say that
  the orchestrator's handoff names the entries by identifier, each read whole; that agrees with the method, since the entries
  the orchestrator names are those the method opens whole.
- The part map's three entries: `elements-common` names the two new scripts in its sentence and holds `elements/common/**`; `decisions`
  holds the template and the log; `task-cycle` holds `task-cycle/**`, `cycle_measures.py` among its trust boundaries already. The new
  scripts import only the standard library and `foundation_check` of the same part, so no dependency of the map is crossed.

## Written or changed by the return step

- **Decisions:** none by me. The change's own: WAY-150, WAY-18, WAY-21, WAY-287, WAY-339 edited in place and the log divided into 28
  sections, by the foundation step (`foundation-entries-report.md`) and the fixes.
- **Invariants:** none. No task, decision or human sets a rule that a commit can break and no test holds as an invariant; the cycle's
  other choices stay rows of the questions table.
- **Environment facts:** none. The change rests on the shapes of the Claude Code transcript and the Codex rollout (`tool_use` and
  `tool_result`; `function_call`, `custom_tool_call` and their outputs), read by the slice from rollouts on the author's disk. The
  template gives a fact only where a decision's *Based on* or an invariant's *Rests on* would name it and no page or reading of a host
  the product's people run is its source; WAY-339's *Based on* stays `none` and no decision of this change cites that shape, and the
  scripts `task-cycle/cycle_measures.py` and `task-cycle/cycle_stages.py` stood on the same shapes before the change with no fact. See Concern 1.
- **Glossary terms:** none. "index" (WAY-150 defines the index of a selection in place; the word keeps its ordinary meaning), "topical
  section" and "selection" are used in no meaning the glossary entries or WAY-95 contradict; the foundation step decided the same.
- **Part-map changes:** none by me. The change's own: the sentence of `elements-common` names the script that writes the index and the
  script that compares the entries of two copies (`foundations/part_map.md:67-73`); correct and complete. No surface entry is added: the
  scripts of `task-cycle` that products run from the pin (`cycle_measures.py`, `cycle_stages.py`) have none either.
- **Projected entries written whole or in part:** none; the task has no projected entries.
- **Pair of examples and `tests:`:** no decision of the change carries a part held by a test (a search for `decision: WAY-(150|18|21|287|339)`
  finds no test), so no pair was reduced.

## Rows of *Settlements to record* written

Each row compared with the entry as it stands in `foundations/decisions.md`:

| Row | Where | Result |
|---|---|---|
| 1 | WAY-150, first paragraph (`foundations/decisions.md:1472-1488`): index of the selection; whole only the decisions the work changes, goes against or proposes another answer to (with the rejected options), those the task or the source names and those whose binding sentences leave open what the work has to do; the reviewer of the whole change reads the index of its whole selection and states how many it read whole | written, same meaning |
| 2 | WAY-150, second paragraph: no file of the repository; a script of the-way writes it on demand into a file the agent names; number, question, binding sentences, *Scope* | written, same meaning |
| 3 | WAY-150, third paragraph: the sections of the work's topics chosen by heading and sentence; the questions of the decisions outside them whose *Scope* names a touched part run through, those that point to a bearing opened whole | written, same meaning |
| 4 | WAY-18, second paragraph: sections with unchanged numbers; a new entry at the end of the section of its topic or, where none fits, in a new section at the end of the log which the request names; a log without sections keeps the order of writing | written, same meaning |
| 5 | WAY-150, first paragraph: the decisions whose sentence a test the work alters holds by a line `decision:` join the selection and are opened whole | written, same meaning |
| 6 | WAY-150, third paragraph: a log without sections selects by the parts and its index replaces reading each decision whole, the decisions the first paragraph names opened whole | written, same meaning |
| 7 | WAY-339, second paragraph (WAY-347 withdrawn, its successor): for each agent the bytes of the decision log and of the index that entered its context and how many times each entered it | written, same meaning |

Entries beyond the rows, marked `the cycle's` by the foundation step: the price sentences of WAY-150 and WAY-21 (the orchestrator's additions), WAY-287's
reading of the index, the division into 28 sections. Their meaning stands in `foundation-entries-report.md`.

## Concerns

1. Environment fact for the transcript shapes. I wrote none (reasons above). The alternative is a fact with a reading of a real transcript as
   its source, which would hold private session content and need a decision's *Based on* to name it, a change of WAY-339 the task does not
   carry. If the human holds that the return step must write it, it is a separate decision on the form of its source.
2. The comparison script `elements/common/compare_log_entries.py` is named only in the part map and in its own docstring. A product that
   later divides its log learns of it by searching, not from the template or WAY-18. The plan assigned it to the cycle's request only; I did not
   add it to the template, since no entry and no plan item says that a division of a log needs it (the foundation step's "no entry is deferred"
   applies to entries this request writes, and this is a possible addition, not a mismatch).
3. WAY-21's *Rationale* holds a measured share ("about half", dated 2026-11-15) of the-way's log; the foundation step's Concern 1 stands. It will
   age as the log grows, and WAY-05 allows it only as a measurement with its conditions; the entry gives its date and method.

## Working copies

`.runs/return-step/` in the worktree held `div.md` and `base.md` (the log at `104e126` and at `21ecb62`, from `git show`), `sections.md`
and `index.md` (output of the index script). Removed; `ls .runs` shows `executor-1`, `executor-2`, `executor-3`, `executor-5`, `task-cycles`
(none mine). No worktree or clone made.

## Unread material

- `task-cycles/decision-log-reading-index/plan.md` read in part (lines 120-200: slices 1-3 and their *Checks*), not whole.
- The executor and review reports, `fix-whole-report.md`, `planner-report.md`: not read; `foundation-entries-report.md` read whole.
- `task-cycle/cycle_measures.py` read in part (lines 1-130 and the diff's label lines); `elements/common/compare_log_entries.py` read in
  part (lines 1-60); the tests of the new scripts not read.
- The entries of the log not named above (the other 193 of 198) were checked only by the byte comparison with the base, not read.
- `elements/environment-facts/template.md` read to the end of "Source"; the rest of its sections not read.
- Everything else the handoff names: read whole.

## Searches not found or unclear

- The task says WAY-326's rule stands in `task-cycle/skill/SKILL.md`; the sentence changed there is at lines 274-276 and in `task-cycle/review/SKILL.md`
  (the counts); I found no other place that restates WAY-326's section of the report. Not unclear, noted.
- A search of `foundations/invariants.md` and `foundations/environment_facts.md` for a rule or fact on the form of the decision log, a section or an
  index: not found (no invariant or fact depends on the change).
- Where a product that divides its log should learn of `compare_log_entries.py`: not found (Concern 2).
