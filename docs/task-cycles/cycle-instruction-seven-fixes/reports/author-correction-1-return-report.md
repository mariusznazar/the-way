# Report of the return step after correction 1

**Status:** done. **Commits:** none (nothing found that no longer matches; head stays `8c97482a`, tree clean).

## Return step, as the record's *Return step* gives it

- **Foundation compared with code:** none needed correcting. Compared, for what the correction touches:
  - WAY-136 (sentence on reviews of groups of slices) with `task-cycle/skill/SKILL.md` step 9, sub-step 5: the skill now says "the orchestrator may dispatch a fresh reviewer … on groups of them in the plan's order, as for a slice with a review of its own, and records the grouping and its reason", which is the actor and the content of the decision's sentence; the earlier difference of word (review finding 5) is gone.
  - WAY-255, WAY-134 and `elements/decisions/template.md`: the correction touched none of the code or text they are compared with (it changed the word of one skill sentence and the count of one script), so the comparison of the earlier return step stands.
  - The part map: `task-cycle` (files `task-cycle/**`, trust boundary on `cycle_stages.py`, `stage_transcripts.py`, `cycle_measures.py`, `gate_times.py`) and `decisions`: the correction adds no file, changes no dependency (`slice_size.py` still imports the standard library only), touches no trust boundary. No change of the map needed.
  - Search of the foundation and the instructions for any entry or instruction that states how the measure counts a file of *Change* named by ranges: `grep -rn -i "slice_size|names by ranges|by ranges|ranges name"` over `*.md` of the worktree (outside `.runs`) found only references to the script, none of its counting rule: `task-cycle/plan/SKILL.md` lines 18, 210–211 (the script is there; run it; split what it reports), `guidelines/coding-measuring-report.md:20` (the file's status `do not copy`), and the withdrawn-numbers table of `foundations/decisions.md:11616` (WAY-371 withdrawn, "its rule … stands in `task-cycle/slice_size.py`"). The rule therefore stands in the script alone, as WAY-371's withdrawal says, and the script, its docstring and its tests agree. `task-cycle/plan/SKILL.md` point 4(b) (entries a slice changes and the section a new entry goes into named in *Read* by range) and `task-cycle/change/SKILL.md` point 4(c) (the entries and the section of a file of the foundation read by the ranges the dispatch names) say what the corrected measure counts; the plan skill's description of *Read* as "the whole reading of the slice's agent besides" the files of *Change* agrees with a code file counted whole.
  - Search for "the lead": `grep -rn -i "the lead\b"` over `*.md` and `*.py` of the worktree (outside `.runs`): no hit; the word stands nowhere in the repository.
- **Decisions written or changed:** none in this step (rows 1–3 were written in the foundation step and stand).
- **Invariants written or changed:** none.
- **Environment facts:** none.
- **Glossary terms:** none (no word used against its entry; "foundation" in the docstring of `slice_size.py` is used as the glossary entry `foundation` gives it, WAY-04).
- **Part-map changes:** none.
- **Projected entries:** none.
- **Rows of *Settlements to record* written, with the place:** unchanged since the first return step (rows 1, 2 → sentences of WAY-136 and WAY-255 in `foundations/decisions.md`; row 3 → sentence of WAY-134 in `foundations/decisions.md` and the bullet of `elements/decisions/template.md`); the correction rewrote none of them and the foundation step missed none.
- **Pair of examples and tests:** unchanged; no test holds a part of the sentences of the three decisions, so no part leaves a pair.

## The choice "a file of the foundation is a file under `foundations/` of the repository root" (WAY-36)

- It binds after the merge in one way only: the script counts by ranges a file of *Change* under `foundations/`, and a later change of the directory's name or of the rule would change what the measure reports. It therefore passes the plan test of the decisions template ("does the rule still bind once the change is merged?").
- It then goes through "Where it goes" in order: question 1 (an instruction for how an agent works) — no, it is how a script counts; question 2 (a rule only for how to write code, tests or the look) — no; question 3 ("a single text, number, list or location" → the product's data or code, with the test that holds it and a comment where the reason is not obvious) — yes: it is one constant, `FOUNDATION_DIRECTORY = "foundations"`, one condition, a docstring paragraph that names where the rule was taken from (the part map's five files and WAY-04), and the test `test_changed_code_file_that_read_names_by_ranges_counts_whole` with the log tests that hold it. So it is no entry of the log: it already stands where question 3 puts it, which is also where WAY-371's withdrawal says the rule of the reading limit stands. Written to the log, it would make a decision of a directory name that the code, the docstring and the tests already hold and that the part map and WAY-04 already state.
- It stays, then, a row of the cycle's questions table (the correction's choice, with the way rejected — a closed list of the five file names — and its cost, in the correction's report).

## Checks (command and exit code)

| Check | Command | Exit |
|---|---|---|
| Foundation check on the unchanged tree (head `8c97482a`, last run in the correction) | `python -B elements/common/foundation_check.py` | 0 (0 errors) |

No other check was run: this step changed no file. Not run: the full gate (handoff).

## Own-work check

- Requirement most likely unmet: that nothing in the foundation or the instructions states the old counting rule or the word "the lead". Check: the two greps above over the whole worktree. Showed: no instruction states the rule outside the script; no "the lead" anywhere.
- Behaviour a user sees in the running product: none; no walkthrough.

## Reaches beyond the handoff

- `grep -rn -i "slice_size|names by ranges|by ranges|ranges name" --include=*.md .` and `grep -rn -i "the lead\b" --include=*.md --include=*.py .` (outside `.runs`), the two searches the handoff asks for; `git log`/`git status` for the head and the clean tree.
- The handoff and `task-cycle/skill/return_step.md` were read whole in the earlier return step and the handoff now; `return_step.md` not read again this time (read whole in the first return step, unchanged since).

## Working copies

None made (`.runs/author-correction-1-return/` not created). The remainder named in the correction's report, `.runs/fc.txt`, is not mine and stays.

## Unread material

`task-cycle/skill/return_step.md`: read whole in the earlier return step of this session, not again; everything else the handoff names was read.

## Searches not found or unclear

none
