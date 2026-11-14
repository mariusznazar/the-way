# Slice 6 report: the skill and the return step apply the questions

## Status

`done`

## Commits

- `64cd4ad` Point the decision skill and the return step to the questions of the template

Range: `c8dcc56..64cd4ad`, 4 files, 25 insertions and 5 deletions in total.

## Files changed

- `elements/decisions/skill/SKILL.md`: step 3 *Verification* bullet reworded (clause `tests:`, pair only for the part no test holds); a second bullet added for a decision whose test a later slice writes, carrying a pair for now. Frontmatter untouched.
- `elements/decisions/skill/decide_entry.md`: 4 lines added after "Apply the template's plan test", pointing to the template's "Where it goes" questions in order, with the routing of a first "yes" that is not the log and of question 5.
- `task-cycle/skill/return_step.md`: the clause "a choice that binds after the merge (WAY-36)" now names the place the questions give (WAY-11, WAY-134); a clause trims a pair of examples to the part no test holds, naming the test by `tests:`; a closing paragraph says the step's report names the place of each settlement. The exclusion sentence is kept.
- `task-cycle/record_template.md`: only the *Return step* item "Rows of *Settlements to record* written" changed, so a row that goes to a skill, a guidelines file or the code of the product names its place in place of the identifier. Label and the other items unchanged.

## Checks

| Check | Command | Exit code | Result |
|---|---|---|---|
| Foundation check | `python -B elements/common/foundation_check.py` | 0 | `0 errors`; one `listed:` line (`foundations/decisions.md:578`, WAY-17 held by nothing). Not checked against the base whether this listing predates the change. |
| Skill entry points | `python -B agent-instructions/skill_entry_points.py` (no `--write`) | 0 | `entry points are current` |
| Gate, agent-instructions | `python -B gate/run_tests.py agent-instructions` | 0 | Ran 25 tests, OK |
| Gate, task-cycle | `python -B gate/run_tests.py task-cycle` | 0 | Ran 394 tests, OK. Run twice: once before a line reflow in `return_step.md`, once after; both exit 0. |
| Gate, process-audit | `python -B gate/run_tests.py process-audit` | 0 | Ran 182 tests in 658.940s, OK. Run in the background; exit code 0 is that of the background command whose last step it was. |

Nothing the checks named failed or was left unrun.

## Own-work check (section 3)

- Requirement: the three files point to the questions of the decisions template and copy none of their words (WAY-35, D6).
- Check: `grep -n -i "instruction for how\|single text\|lack of a feature\|already answer"` over the four changed files.
- Showed: no copy of the question wording. The one hit, "A question the log already answers takes an edit", is text that already stood in `decide_entry.md` before this change.
- Second requirement, the pair-then-trim rule (D2): both halves are present, the bullet in `SKILL.md` step 3 and the clause in `return_step.md`.

## Choices made

- Wording of the `decide_entry.md` bullet: it names the template's "Where it goes" questions by label and gives the routing, without quoting the questions. Rejected: quoting the five questions (the handoff forbids copying them). Cost if wrong: a reader must open the template to see the questions; no check fails.
- The second `SKILL.md` bullet states the reason in one sentence (the foundation check's run after writing reports a changed decision with nothing holding it, and the switch does not skip that report). Rejected: a shorter bullet without the reason; the handoff asked for the reason.
- The clause in `return_step.md` also says "the log is one such place", so the reader does not take "the place the questions give" to exclude the log. Cost if wrong: none found.

## Reaches beyond the dispatch

- Read `foundations/invariants.md:96-104` (skill-rule-source) and `foundations/glossary.md` entries "foundation step" and "return step" (named by the plan): to confirm the skills still name the template and `elements/common/` as their rule sources (they do; no field list was restated).
- Confirmed `product-guidelines/template.md` exists before naming it.
- Read `foundations/decisions.md` WAY-11 (line 390), WAY-35 (1057), WAY-36 (1082), WAY-134 (3611), WAY-293 (around line 9649) and WAY-268 (line 8531), as the handoff's notes direct. These were read to confirm the return step's wording agrees with WAY-11 and WAY-134. No sentence of an entry contradicted the spec, so no `blocked`.
- Read `elements/common/way_of_working.md:140-161` (the steps of writing an entry).

## Unread material

- `.runs/task-cycles/co-trafia-do-dziennika-decyzji/spec.md:60-84` and `:129-141` (D2 and D6): read in full.
- `.runs/task-cycles/co-trafia-do-dziennika-decyzji/task.md:35-37`: read.
- `foundations/decisions.md` WAY-12 (383-411 in the plan's base, now around 435), WAY-22 (594-617 base, now 679), WAY-33 (886-917 base, now 987): not read in this session. Their content matters only for the sentences they bind; the changed text does not restate them.
- `foundations/part_map.md:7-15, 65-75, 93-103`: not read.
- `foundations/decisions.md:981-1005` (WAY-36 at the base) and `:9503-9542` (WAY-293 at the base): read at their current lines instead (WAY-36 at 1082, WAY-293 at 9649); the current text was read.
- `foundations/decisions.md:346-381` (WAY-11 at base) and `:3510-3604` (WAY-134 at base): read at current lines (390, 3611).
- `foundations/decisions.md:8385-8449` (WAY-268 at base): read at current line 8531, partly.
- `foundations/decisions.md` WAY-12 attached paragraph (D2 sentence on the report): not read; D2 in spec was read.

## Searches not found or unclear

- None found. The `foundation_check.py` `listed:` line at `foundations/decisions.md:578` (WAY-17 held by nothing) was not checked against the base; I did not establish whether it predates this change. It is not caused by the four files changed, as they contain no decision lines.
- The `CLAUDE.md` / `AGENTS.md` instruction files were read as given.

## Process

- Background processes started: the gate runs in the background (`bad14oiq1`, which completed exit 0), a monitor on the process-audit output (`bhtycy1zl`, stopped by TaskStop), and a waiter (`bzkv2e250`, completed). None remain running; `ps` shows no `run_tests` process.
- The commit hook on the first `git commit` asked for the git rules to be read before the commit; the commit was retried after that. The commit message is English, imperative, and staged by path.
