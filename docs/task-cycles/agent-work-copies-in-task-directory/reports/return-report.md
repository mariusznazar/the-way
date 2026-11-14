# Return step report: agent-work-copies-in-task-directory

**Status:** done

**Commits:** none. The head stays `a300ee62676e5812141c86852357d32e54e3b068`; nothing no longer matched.

## What I compared, with the files as they now stand

- **WAY-373** (the entry the change wrote; row 1) against `task-cycle/skill/SKILL.md` (section "Working copies", step 2's clone in `.runs/pin/`, step 4's base checkout in `.runs/base/`, the handoff paragraph, the list of what is read in every report, step 14), `task-cycle/record_template.md` (item *Working copies left*), `task-cycle/skill/request_template.md` (*Cost* and *Checks*; no kind 18 left), `task-cycle/review/SKILL.md`, `task-cycle/review/whole_change.md`, `task-cycle/plan/SKILL.md`, `task-cycle/change/SKILL.md`, `task-cycle/change/ui_check.md`. They agree on: the directory of the agent under the ignored `.runs/` of the task's worktree, never the system's temporary directory, a session's scratch directory or the main checkout; removal before each return; the report states where the copy stood and that it was removed; a failed removal is named with its path, stops nothing and reaches the record and the description under *Cost* and *Checks*; the orchestrator's own checkouts are covered; the files that a product's own tools and tests make by themselves are no working copy of the agent (the same clause in the decision's third sentence and in the section's first paragraph); the sentence on tool-written files names only the screenshot of a screenshot tool. Binding sentences: three, as the template allows. No normative words in capitals, no *should*/*will*.
- **WAY-140** (the task's *Decisions in play*): an effect outside the repository is a human's; WAY-373 puts the agent's copies inside the task's worktree and leaves reading outside to the agent, so no conflict.
- **WAY-316**: no screenshot file is committed; a screenshot working copy stands under `.runs/<name>/`, outside the record directory `.runs/task-cycles/<task-slug>/` that the cleaned copy is made from, and the image check on the copy is untouched; the screenshot shown to the human keeps its route (`ui_check.md`). No conflict.
- **WAY-148** (the decision WAY-373 derives from) and **WAY-33**: the record is the cycle's only log, and the remainder goes into it as the item *Working copies left*; `Rationale` and *Rejected* name no file, script or count.
- **WAY-286 and WAY-287** (read in the fix): untouched, as they stand; the request's decisions section holds no item for a leftover copy.
- **Part map**: `task-cycle` (files `task-cycle/**`, which hold every file the change touched) and the decision log's part; no file added, moved or removed, no part added, so no line of the part map changes. The change adds a decision in `foundations/decisions.md`, which the part map already assigns.
- **The search** (WAY-33): one search of `foundations/` and `elements/` for `scratch`, `.runs`, `temporary director`, `working cop`, `leftover`, `separate worktree`, `separate checkout` in the first round, and `kind 18` and `Working copies left` in the fix round; and, now, `grep -n -i "playwright\|working copy\|remainder\|scratch"` over `foundations/environment_facts.md` and `foundations/glossary.md` (only an unrelated arXiv fact matched) and `grep -rn "WAY-373"` over the repository's Markdown and Python files (only the entry itself). Nothing found that WAY-373 touches.

## What I corrected

Nothing. I did not touch the reviewer's Minor note on `task-cycle/plan/SKILL.md:180-183`, as the handoff says.

## Entries written or changed in this step

- Decisions written or changed: none in this step (WAY-373 was written by the change, row 1).
- Invariants written or changed: none.
- Environment facts: none. The decision does not rest on a source outside the product; the section's mention of the Playwright server is an example in an instruction, not something an entry rests on.
- Glossary terms: none. "Working copy" is used in the plain sense of a copy made to check something; the glossary holds no entry for it and no entry is used against its meaning.
- Part-map changes: none.
- Projected entries: none.
- Rows of *Settlements to record*: row 1 went to the decision **WAY-373** (kind `decision`); no other row. No choice that binds after the merge was left as a row of the questions table that should be an entry.

## Checks (command and exit code)

| Command | Exit |
|---|---|
| `python -B elements/common/foundation_check.py` (on the head `a300ee6`, clean tree) | 0 (`0 errors`) |

Not run: the focused test commands of the earlier rounds (no file changed since the fix's run: `git status --short` prints nothing); the whole gate (the orchestrator's run).

## My working copies

I made none; `.runs/author/` was not created and `ls .runs` shows only `task-cycles/`. I wrote nothing to the system's temporary directory. Remainders: none.

## Unread material

- `task-cycle/skill/return_step.md`, `task-cycle/skill/foundation_step.md` (read in the first round), the return handoff: read whole.
- WAY-373: read whole. WAY-140, WAY-148, WAY-316, WAY-33, WAY-286, WAY-287: read whole in the earlier rounds, not again in this one beyond what the comparison above names.
- Not read: the part-map entry of `decisions` (I read the `task-cycle` entry whole and the rule that `task-cycle/**` holds the files); the invariants whose *Part* names `task-cycle` or `every`; the glossary beyond a `grep`. No invariant bears on where an agent's copy stands (the first-round search found none).

## Searches not found or unclear

none
