# Report 13 — task review of Task 3 with deliberate break (saved by the orchestrator from the returned text)

Range a7f42aa..c12d4dd, package `reports/sdd/review-a7f42aa..c12d4dd.diff`.

## Spec compliance

✅ The 22 entry points follow §4.2: name `the-way-<name>`; description ends with exactly ` Use this checkout's own
the-way.`; body names the right source path; sibling list sorted by source path, joined `, ` with ` or ` before the last,
no serial comma. Copies share blob hashes (e.g. `29b7f21` for both `the-way-critique`). `TrackedEntryPoints`
(`agent-instructions/test_skill_entry_points.py:510-522`) is the brief's code, placed before `if __name__`.
⚠️ Not verifiable from the diff: descriptions equal their sources byte for byte (break 5 shows the check catches a changed
start); part-map patterns (reported guard output only); the generator (Task 2).

## Strengths

One generated text per skill, identical in both directories; sibling sentence regenerated from discovery; the equality
test covers file set, bytes and orphans, cites no invariant (WAY-69); evidence complete (`reports/` files match: 22
generated, 12/98/16 OK, guard 0 errors 0 warnings 7 unchecked); all 13 deliberate breaks caught.

## Deliberate breaks (gate run with `--record .runs/gate-tests.jsonl` after each)

| # | Break | Test failed | `skill-entry-points/1` |
|---|---|---|---|
| 1 | delete `.agents/skills/the-way-refine-task/SKILL.md` | yes | fail |
| 2 | one byte changed in `.claude/skills/the-way-critique/SKILL.md` only | yes ("not byte-identical") | fail |
| 3 | `` `record-glossary-term` `` removed from the sibling sentence of `the-way-record-decision` (both) | yes | fail |
| 4 | add `.claude/skills/the-way-nothing/notes.txt` | yes ("no skill … named nothing") | fail |
| 5 | description start of `the-way-update-part-map` changed (both) | yes | fail |
| 6 | `` `critique` `` moved out of the sibling sentence (both) | yes | fail |
| 7 | frontmatter name → `the-way-settle-technologies` (both) | yes | fail |
| 8 | skip line removed from `the-way-define-project` (both) | yes | fail |
| 9 | `':/.the-way'` → `.the-way` in `the-way-implement-task` (both) | yes | fail |
| 10 | source path in `the-way-record-invariant` → `elements/invariants/SKILL.md` (both) | yes | fail |
| 11 | new untracked `elements/zz-break-probe/SKILL.md` without entry point | yes (every sibling sentence reported) | fail |
| 12 | words "with the `the-way-` prefix" changed in `the-way-record-environment-fact` (both) | yes | fail |
| 13 | sibling sentence split in two in `the-way-record-glossary-term` (both) | yes | fail |

Restored after each with `git restore --source=HEAD --staged --worktree -- .claude/skills .agents/skills`; deleted only what
`git clean -n -d` listed (`.claude/skills/the-way-nothing/`) and the probe directory `elements/zz-break-probe` by path;
status empty after every restore; final clean gate run exit 0, 98 OK, `skill-entry-points/1` pass. Nothing against the
check.

## Issues

Critical: none.

Important:
1. The root rule gives the wrong root after `/cd` (from the spec: §4.2 is binding, so it goes back to the design step).
   Every entry point, e.g. `.claude/skills/the-way-record-decision/SKILL.md:11` and `:8`: "The process root is the checkout
   or worktree the session was started in: the directory `git rev-parse --show-toplevel` prints when run in the session's
   start directory"; the product check also runs "in the directory the session was started in". Under the quoted Claude
   Code behaviour ("When you move the session with /cd on v2.1.246 or later, Claude Code adds the new directory’s project
   skills."): (a) started in `C:\Storage\repos\the-way`, `/cd` into a task worktree — the worktree's `the-way-*` skills are
   added; whichever copy runs, it sends the agent to the main checkout while it edits the worktree — the defect §4.2's own
   rationale rules out; (b) started in the-way, `/cd` into a product — both checks answer "not a product", the agent uses
   the-way's checkout instead of the product's `.the-way`, against WAY-34. Direction: root = "the directory the session works
   in — the one it was started in or, after `/cd`, the one it was last moved to — not the shell's current directory"; both
   checks there too.

Minor:
1. Line wrapping differs from the §4.2 block (`.claude/skills/*/SKILL.md:7,9-10,12,14`): one line per paragraph; renders the
   same; the cause is the Task 2 generator; the spec should say soft wraps are joined, or the generator keep them.
2. The test is wider than the generator (`test_skill_entry_points.py:514-519`): every tracked file under the skills
   directories must be generated, while the generator ignores other directories (`:502-505`, `someone-elses`); narrowing the
   listing to `the-way-*` would line them up.
3. The new flow's parts are not checked ("unchecked: the list of parts of `skills-reach-the-way-sessions` — its test leaves
   no coverage file"), the same known gap as `wording-reaches-dependants`.

## Assessment

Task quality: Approved — the entry points and the equality test meet the brief and §4.1–§4.2, all 13 breaks caught; the
important point is in the spec's text and goes back to the design step.
