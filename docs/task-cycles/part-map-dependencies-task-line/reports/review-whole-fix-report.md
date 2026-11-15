PASS 1b5aba91fce0a23ee95d6bab2e107eb187b34d67

# Review of the fix of the whole-change review's findings

Range `af76148..1b5aba9` (`git rev-parse HEAD` is `1b5aba91fce0a23ee95d6bab2e107eb187b34d67`, one
commit). Method: `task-cycle/review/SKILL.md` and `fix.md`. Read: the findings file
`reports/whole-findings.md`, the fix report `reports/author-fix-report.md`, the handoff, the whole
fix diff. My earlier selection stands.

## Each finding

- **I-1 (blocking) — fixed.** `foundations/part_map.md:86-91`: the sentence of `project-level` now
  says the part answers "for the derivation of the identifier of a task of a plan, but not for the
  rest of how a line is made, which the rules of the task place say (WAY-107)". That agrees with
  WAY-107's second paragraph, `project-level/task_line.md` ("The identifier") and
  `project-level/backlog_place.md`. The part's text stays two sentences, as the task's item 7 asks.
  No new contradiction: the other clause, "when the line … is written, given its dependencies and
  moved to ready", is unchanged.
- **M-1 — fixed.** `elements/part-map/template.md:88-94` no longer lists the kinds of reach; it
  sends the reader to the glossary's definition ("what the glossary gives that term, any reach and
  not only an import"). One list of the kinds stands, in `foundations/glossary.md`.
- **M-2 — fixed.** `blocked-request-line` is split into `blocked-request-wording` (wording in
  backticks in the two skill files) and `blocked-request-label` (a line of
  `task-cycle/record_template.md` begins with the label), `foundations/invariants.md:378-396`; each
  one sentence, `Method: test`, `Derives from: WAY-153`, `Part: project-level · task-cycle`.
  WAY-153's *Verification* (`foundations/decisions.md:4794`) names both. `git grep
  "blocked-request-line"` outside `.runs` finds nothing left. Each test of
  `project-level/test_blocked_request_line.py` cites its own invariant. The break checks below show
  each side failing only its own test.
- **M-3 — fixed where it lay within the task; the rest contested with evidence and kept as a
  note.** The bare word is replaced by "dependency of a part" / "dependencies of a part" in
  `foundations/part_map.md:4`, in `elements/part-map/skill/SKILL.md` (description and the *Depends
  on* step), in `elements/part-map/template.md` (fields line, the paragraph on a dependency the
  code holds, "no list of such dependencies of a part"), and in the two entry points of the skill,
  rewritten by the generator; `python -B agent-instructions/skill_entry_points.py` prints `entry
  points are current`, exit 0, and the two copies are identical. The binding sentence of WAY-225 and
  its examples stay with the bare word: the frozen task lists WAY-225 under *Decisions in play* as
  "Bez zmiany", so I accept the author's contest. The finding itself said the sentence was kept
  unchanged by the task. What remains is a Minor note outside the fix diff and outside the task:
  WAY-225 (`foundations/decisions.md:2488-2491`, 2497-2503) and WAY-51's *Rejected* still say "a
  dependency the code holds that the part map does not allow" in the bare word. It blocks nothing.

## The fix diff itself

- No new Critical or Important finding. The edits to `elements/part-map/template.md` change no
  meaning: "dependency" qualified by "of a part" in four places, and the glossary pointer.
- Minor, new in the fix, blocks nothing: `foundations/part_map.md:4` is now one line of 106
  characters ("…The map says which dependencies of a part are allowed; the"), over the 100 columns
  the log's rewrap commits keep; no rule I found (`agent-instructions/README.md`, `AGENTS.md`)
  states a width for this file, so it is a polish note only.

## Checks I ran (worktree of `1b5aba9` under `.runs/review-whole-fix/wt`; command, exit code)

- `python -B elements/common/foundation_check.py` → exit 0, `0 errors`.
- `python -B agent-instructions/skill_entry_points.py` (no `--write`) → exit 0, `entry points are
  current`.
- `python -B -m unittest project-level/test_blocked_request_line.py` → exit 0 unbroken. Broken one
  side at a time (reset after each): wording in `task-cycle/skill/blocked_finding.md` reworded →
  exit 1, only the wording test (`test_each_writer_gives_the_wording_the_reader_takes`) fails;
  label in `task-cycle/record_template.md` renamed → exit 1, only
  `test_the_record_template_gives_the_label_the_reader_takes` fails; wording in `plan_state.py`
  `BLOCKED_DRAFT` reworded → exit 1, the wording test fails for both files.
- `python -B gate/run_tests.py project-level` (278 tests), `elements/part-map` (39),
  `elements/common` (235), `agent-instructions` (25) → exit 0 each. The whole gate not run.

## Unread material

none. (The task, the earlier report and the files the fix edits were read in this review; the
decisions of my earlier selection stand with the counts of the earlier report: 13 whole.)

## Searches not found or unclear

none.

## Working copies

`.runs/review-whole-fix/wt`, a detached worktree of `1b5aba9`, and the run outputs beside it: removed
(`git worktree remove --force`, `git worktree prune`, the directory deleted); `git worktree list`
no longer shows it. Nothing kept.
