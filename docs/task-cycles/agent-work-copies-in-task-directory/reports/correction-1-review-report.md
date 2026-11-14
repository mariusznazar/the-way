PASS 463076e0dac9bad96e008766b48565759cfd25bc

# Review of correction 1 — the six decisions read whole against WAY-373 and the changed files

Head confirmed: `git rev-parse HEAD` = 463076e0dac9bad96e008766b48565759cfd25bc (exit 0); `git status --short` empty. Range reviewed: `git diff 671f470 a300ee6` (9 files), read whole for `task-cycle/` and `foundations/decisions.md`.

## Findings

None. No finding of any grade. For each of the six: what it holds and why it does not meet the change.

- **WAY-33** (`foundations/decisions.md:1002`): when a change writes a foundation entry, its author searches the whole foundation once, at the time the entry is settled, for entries it touches, and turns each hit into a link, a change or a question. It speaks of an author's search and of no working copy, no report line and no place for files; WAY-373 and the changed files add nothing to that search and do not restate it. The new entry WAY-373 is itself linked to WAY-148 and sits among task-cycle entries with no entry it contradicts (see the other entries below).
- **WAY-114** (`:2877`): what the human accepts of an entry and when; the request's section for the human's decisions gives one plain sentence per entry the cycle wrote, and the lower part lists every entry by identifier. The change touches the description only in *Cost* and *Checks* (a remainder of a working copy, `task-cycle/skill/request_template.md`), not in the section for decisions or the list of entries; WAY-373 itself falls under "every other entry, at the merge", which the template already carries.
- **WAY-127** (`:3428`): a session on the-way reaches each skill through the entry points of the checkout or worktree it works in, the files a skill names are read when their step comes, and no global link reaches the-way's skills. The change keeps "each handoff has the agent work from the worktree's root" and names the stage's method by its path in the worktree; copies made in `.runs/<name>/` are no session's working place, and a worktree there offering its own entry points beside the session's was already so before the change (`.runs/` held the step 2 clone and the step 4 checkout; WAY-127 rationale accepts "gains that directory's entry points beside"). The added paragraphs of the handoff and of the skills name no file for an agent to read at the start.
- **WAY-150** (`:4503`): selection of the foundation to read — the orchestrator selects for handoffs, the reviewer of the whole change for itself, every other agent reads what its handoff names and names each reach in its report. The change adds to the handoff the name of the agent's directory and a word-for-word paragraph (not a foundation entry, so no selection), and adds a line to the report; it leaves the screening of the whole-change reviewer, its count and the "no gap for a title-only decision" sentence of step 6 unchanged.
- **WAY-161** (`:4927`): which findings of the whole-change review are fixed, and how the request lists those that stay. A remainder of a working copy is not a finding of a review; the request places it in *Cost* and *Checks*, which is not one of the lists WAY-161 gives, and the orchestrator is not told to move any finding between lists.
- **WAY-255** (`:8139`): an agent waits for a command that may outlast its prompt cache by running it in the background and reading between waits under about four minutes. The change leaves the bullet in `task-cycle/review/SKILL.md` as it was (and the whole-change method's runs); removal of a copy "before the agent returns" is later than any wait and asks no wait of its own.

Entries read to judge them against, whole: WAY-373 (new, `:12841`), WAY-148 (`:4435`), WAY-140 (`:4137`), WAY-316 (`:10702`).

- WAY-148: the new rule keeps full material in reports, a line per report read by the orchestrator when the agent returns (as it reads checks, reaches, unread material and searches in every report), the record as the only log (record item *Working copies left*), and the handoff carrying the first paragraph "word for word" as it permits. No contradiction.
- WAY-140: the change's rule moves agents' copies from outside the repository (system temporary directory, session scratch) into the task's ignored `.runs/`, which narrows writes outside the repository; the sentence "The cycle writes only in the task's worktree, the working copies of its agents included" does not claim more. No contradiction.
- WAY-316: the screenshot that a tool writes itself is a working copy removed before return; `task-cycle/change/ui_check.md` sends a shown screenshot to the place the foundation settles, and "where none, into your directory for working copies, original removed, goes before you return" agrees with "keep none". No contradiction. An observation, not a finding: the first paragraph of "Working copies", copied into every handoff, says the tool's file "is moved into the agent's directory and the original removed" without the exception for a settled place that `ui_check.md` and `review/SKILL.md` give; each of those two files says the shown copy lies in the settled place, so a reader of them reads it right. I name it only because the paragraph in the handoff is read alone by an agent that takes no screenshot to show; I grade it no finding for lack of a sentence a reader would read wrongly.

## Correction's remarks

1. Made: the six read whole by a reviewer that did not write the earlier review; no contradiction found; this report is the place the description's statement rests on ("no contradiction with WAY-33, WAY-114, WAY-127, WAY-150, WAY-161, WAY-255; nothing to correct in the request").
2–3. Accepted; ask nothing.

## Declined to judge

- Whether the paragraph copied into every handoff should carry the settled-place exception for shown screenshots: set aside as the observation above, not a defect I can cite.
- The wider tree against decisions other than the six, WAY-373, WAY-148, WAY-140 and WAY-316: outside what the correction asks.

## Checks

- `git rev-parse HEAD` — exit 0, 463076e0dac9bad96e008766b48565759cfd25bc.
- `git status --short` — exit 0, empty.
- `git diff 671f470 a300ee6 --stat` and `git diff 671f470 a300ee6 -- task-cycle` — exit 0, read whole.
- `grep -rnE "separate (worktree|checkout)|system's temporary|scratch dir|temporary dir|\.runs/" task-cycle foundations --include=*.md` filtered of WAY-373 and `task-cycle/skill/SKILL.md` — exit 0: no remaining old "separate worktree" wording of the unchanged files; the other `.runs/` hits are the task cycle's record directory and `.runs/project-refinement/` (not a working copy).
- `grep -nE "WAY-373" -r task-cycle foundations agent-instructions instruction-files` — exit 0: no reference beyond the entry (the changed files give the rule by the paragraph "Working copies" without naming WAY-373 other than through the handoff's WAY-148 mention).
- The product's gate was not run (the tree did not change); not in the ask.

## Reaches beyond the dispatch

- `foundations/decisions.md` — WAY-140, WAY-148, WAY-316 were named by the dispatch; WAY-373 too. Nothing else outside the dispatch read, except the grep results above, the end of WAY-127 and WAY-150, and the *Rejected* paragraphs of WAY-161, WAY-255 (same entries, read through their end).

## Working copies

None made. `.runs/correction-review/` was not created; no worktree, clone, script or screenshot of mine stood anywhere; no remainder.

## Unread material

none. The six were read whole from heading to the next heading with *Rationale* and *Rejected*; WAY-373, WAY-148, WAY-140, WAY-316 whole. The changed files of `task-cycle/` were read as the diff `671f470..a300ee6` (with its surrounding lines the diff shows), not each file whole; `task-cycle/review/SKILL.md` and `fix.md` whole.

## Searches not found or unclear

none
