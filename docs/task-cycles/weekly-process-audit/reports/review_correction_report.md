PASS 9cf2633da6e40defa92ef121b221b47f7feda6bf

# Review of the correction for the human's decision (`5f2c155..9cf2633`)

`git rev-parse HEAD` = `9cf2633da6e40defa92ef121b221b47f7feda6bf`, confirmed. Two commits: `b43558a` (`task-cycle/cycle_stages.py`, its tests), `9cf2633`
(`process-audit/audit_count.py`, its tests, `task-cycle/record_template.md`, `task-cycle/skill/SKILL.md`, `foundations/decisions.md`).
Worktree read only: `git status --short` empty after every check. Method: `task-cycle/review/fix.md` (the human's remarks take the findings file's place) and section 2 of
`task-cycle/review/SKILL.md` for the diff; the remarks and the build list are in `correction_handoff.md`, the author's claims in `correction_report.md` (claims, not evidence).

Counts: 0 blocking, 4 Minor, 1 out of scope.

## The human's two points

1. **"A `0.0%` only where the record plainly says there was no round" — made.** The word rule (`report` and `fix` in a path; `fix`/`review` in a stage name) and the reading of *Events* are gone
   (`report_paths`, `record_rounds`, `stage_kind` removed; I grepped the file). The rounds are read from one place, the item `Review rounds`, in one form
   (`review_rounds`, `audit_count.py:655`). `0.0%` needs the item to read `none` (`remarks_check.reads_none`) and no turn given a findings file (`fix_rounds_share`, `:771`).
   The archive's form, prose in the item, now gives `unknown`: scratch S4 (`- Review rounds: none blocked. The review passed.` with a new-form `stages.md`) gives
   `Fix rounds` `unknown`, `Share` `unknown`, reason "names no findings file"; the executor's test for the prose form fails on `9392230` by the author's account.
2. **"Do it in this request, not as a task of its own" — made.** `cycle_stages.py` writes a column *Files named* per subagent turn; the audit reads it and gives a real figure
   (scratch S1, a conforming cycle: cost 0.011250, rounds 1, share 28.9 %; the executor's end-to-end test runs `cycle_stages.py` as a process on Claude Code transcripts, commits the
   output with a record and gets `15.8%`, hand-worked 2250 of 14250). I did not rerun that end-to-end test separately; the suite below ran it.

## The finding I left (the `0.0%` share silently wrong for the archive's form) — FIXED

Evidence. (a) The `0.0%` branch now needs the item `Review rounds` to read exactly `none`; every archived record I looked at last time (`reports/fix.md`, `reports/review-fix.md`, prose "one fix and its review")
has prose or paths in another form, so it gives `unknown` (S4). (b) A record of the archive's old form cannot reach the `0.0%` line with an old `stages.md`: the share needs the column *Files named*, and all
archived `stages.md` lack it (the stages section itself is missing in 67 of them, as the executor's run on this repository shows: 70 of 71 cycles `unknown`). The one remaining way to a wrong `0.0%` is a new-form
`stages.md` beside a record that reads exactly `none` although a round ran; the cross-check (a turn given a file with `findings` in its name that the record does not name makes the share `unknown`) catches the
ordinary case, and the rest is the record's own word (Minor 1).

## Findings

### Minor 1 — the count of turns named by a findings file has a lower bound only; a stray mention counts as fix cost, and unreadable turns blind the `0.0%` cross-check

Place: `process-audit/audit_count.py:771-806` (`fix_rounds_share`).
A round needs at least two turns naming its findings file; no upper bound exists. Scratch S2: a conforming round plus one more stage ("Whole-change review of the later change") whose message names the
same findings file: share `97.2%`, no unknown, against `28.9%` without it. The rule that no other message names the file is in `task-cycle/skill/SKILL.md` and WAY-336, but nothing in the audit holds it. A cheap upper
bound the stages do carry: the turns naming one findings file belong to at most two distinct subagents (the fix agent and the reviewer; the turn suffix ` — turn n` stripped); a third makes the share `unknown`.
Second part: with the item `none`, a turn whose cell is `unknown` is skipped, so the "no turn names a findings file" test is blind there; S3b (all subagent turns `unknown`, item `none`) gives `0.0%`. S3 (item `none`, fix turns naming only `reports/h.md`,
`reports/fix_input.md`) gives `0.0%` too, since only a name holding `findings` trips the cross-check. Both rest on the record's own word, as the human accepted ("the record plainly says"), so Minor; the
consequence is a figure that looks measured where a stray mention or an unread turn hides a round. A cost of `unknown` in the unread case is cheap.

### Minor 2 — a tokenless parallel row of the orchestrator still makes the cost of the whole cycle `unknown`

Place: `audit_count.py:716-722` (`priced`): `row.name == ORCHESTRATOR` only; `is_orchestrator_row` (`:700`) also covers `orchestrator while in parallel: ...`.
`cycle_stages.py` makes a parallel row for a tool call too (`orchestrator_row(call.start)`), so such a row can have time and calls and no usage, written with the model `—`. In the archived (old form) `stages.md`
all 30 zero-token rows of 1,762 are plain `orchestrator` rows, so the case is rare, but the docstring promises "an orchestrator stretch with no token usage costs nothing" and the helper that tells the orchestrator's rows exists.
Direction: use `is_orchestrator_row` there. Effect today: `unknown` (the safe direction), not a wrong number.

### Minor 3 — the Codex reader takes the first user message of a turn, which a real rollout fills with injected context

Place: `task-cycle/cycle_stages.py` `codex_message_text` and `read_codex_agent` (`messages[owner]` set once, first wins).
A real rollout of this machine (`~/.codex/sessions/2026/10/26/rollout-...01a1797b....jsonl`) starts the turn with `response_item message developer ...`, then `message user # AGENTS.md instructions for ...`, and only then
the user's prompt. The reader would take the AGENTS.md text as the turn's starting message, and the prompt's file names would not be read. The tests use synthetic rollouts. Effect: an empty cell instead of the prompt's files, so a round is
named by fewer than two turns and the share is `unknown` (safe), or `0.0%` under a `none` item (Minor 1). The executor also found that today's Codex encrypts agent-to-agent messages, so the path is dormant; I could not check a plain-text subagent rollout,
which is unverified. Direction: skip the injected context messages (the instructions block and the environment block) or take the last user message before the first response.

### Minor 4 — rows with one `#` are merged with the first row's files, and nothing says when two rows of one stage disagree

Place: `audit_count.py:780-788`. A stage's model rows are grouped by `#`; the first row's cell is kept, the costs are summed. A `stages.md` with two different stages under one number (hand-edited, since the writer numbers them apart) or two rows
of one stage with different cells (scratch S6: first row names the findings file, second is empty) is read without a note. The writer gives each stage's rows the same cell, so this concerns a malformed section only; the old pin/remarks lines treat a doubled item as `unknown`.
Direction: `unknown` where rows of one `#` differ in stage name or in the cell.

## Out of scope

### Out of scope — `task-cycle/cycle_stages.py` is not recorded as a trust boundary of its part

`foundations/part_map.md` (grep `cycle_stages`: no match) names no trust boundary for it, though it reads session transcripts from the user's disk, now including the text of messages (WAY-48: "files that come from outside the product, such as one on the user's disk").
The correction's concern 2 asks the same; it is a part-map decision for the orchestrator (the part map is a separate entry the change did not touch). Not graded as a defect of the correction.

## Review of the diff, by the points the dispatch names

- **`cycle_stages.py` — untrusted text.** `FILE_NAMED = (?<![A-Za-z0-9_.-])reports[\\/]+([A-Za-z0-9_.-]+)` takes the name run whole; scratch timings on 2 MB inputs: `reports` + 2,000,000 slashes 0.10 s, `reports/` x 500,000 0.18 s,
  a 3 MB name 0.01 s, 200,000 names 0.0 s (cut at 20, flag set), 2 MB of dots 0.01 s: linear, no backtracking blow-up. Names are kept only if at most 120 characters, ending `.md`, no `..`, first character a letter, digit or `_`
  (`x reports/..md`, `reports/.md` rejected; `xreports/a.md` not matched). Written through `cell()`; the charset leaves no bar or control character. A cap of 20 per turn with a warning. A turn naming nothing is an empty cell, an unreadable message `unknown`.
  No path is followed. Claude Code: the user line starting the turn (`message_text`), a meta line only after an answer, as before. Codex: Minor 3.
- **`audit_count.py` — reading the new forms.** `files_cell` splits on `,` and requires every part to fullmatch `reports/<name>.md` of at most 120 characters and no `..` (`REPORT_FILE` is bounded, no nested repetition); `reports/../x.md` and a name with ESC give
  `unknown` for the share with the cost kept (S8, S9; the reason passes through `cell()`). `review_rounds`: item missing, doubled (S7), prose, text beside entries, entry not opening with `findings` and a backticked path, the same file twice: each `unknown` with its reason;
  `ROUND_ENTRY` is bounded to 200 characters between backticks; one pass over the lines; fenced lines excluded. Token counts keep their 15-digit guard; the new share arithmetic is `Decimal` division by a nonzero total (zero total is `unknown`) and cannot raise on the inputs tried.
  A failure of one cycle stays that cycle's `unknown`. Size caps are the existing ones (4 MiB copy cap).
- **The orchestrator's extra rule (a findings file must be named by at least two turns).** Sound as a lower bound and in the safe direction: a conforming round always has a fix turn and the review of that fix, so it never produces an `unknown` for a conforming cycle, and a fix whose message
  named the file only in its handoff (this very cycle, as the author's run on the real transcripts showed) gives `unknown`, not a share that leaves the fix out. It is not in WAY-336's text, but "unknown wherever the record and the stages cannot tie each round to the turns that served it"
  covers it. What it does not do is bound the count from above (Minor 1).
- **The orchestrator's rows** are excluded from the share by name (`orchestrator`, `orchestrator while in parallel: ...`), so their tokens while a fix runs are in the cost and not in the share (the share understates the orchestrator's own work on fixes, as the earlier fix report said); stated in the docstring.
- **Record template and skill.** `record_template.md`: the item reads `none` or one entry per round opening with `findings` and the path; slice rounds are entries too. `task-cycle/skill/SKILL.md`: one sentence added after the fix gets its findings file; the rest of the passage is unchanged
  (the line wraps differently, which the diff shows). I found no other sentence in `task-cycle` that still says a slice's rounds stand only in the Slices table (grep of `Review rounds` and "stand in its row"). `gate/run_tests.py task-cycle`, which holds the template test, was reported 0 by the author; I did not rerun it (the cycle's own run).
- **WAY-336 against the code.** The text (a fix round is the fix and the review of it; a turn serves it when its starting message names the round's findings file by its path in `reports/`; the record names each round by that path; `0.0%` only where the record says no round;
  unknown where record and stages cannot tie) matches `fix_rounds_share`. *Verification* names the violations the earlier reviews found (words in names, `0.0%` for a named round, the resuming message naming the file only in its handoff). *Scope* gains `task-cycle`, which the skill sentence and the template justify.
  The text does not say the share is the cost of the subagent turns over the cycle's cost, nor that the orchestrator's own rows stay out of it, nor the at-least-two rule; none contradicts the code, and the code's docstring holds them. **WAY-338** says a change of the form of a stage report starts a new series: still true, and now exercised
  (the column is such a change; `cycle_stages.py`'s docstring says so). `python -B elements/common/foundation_check.py`: 0 errors.
- **A record of the archive's old form giving a silently wrong figure:** no. Old `stages.md` (no section, or no column) gives `unknown` for cost or share; an old record's prose item gives `unknown`; the one residue is an exact `none` that was written while a round ran, with a new-form `stages.md`, which both parts of
  the old process could not produce together (the template and the script of one pin change together) and which the findings-word cross-check usually catches (Minor 1).

## Declined to judge

- The figures of the price list and the pricing (settled in the first review).
- Slices 5-7, and what the per-version medians do with the new series.
- Whether the orchestrator will keep naming the findings file by its path in every dispatch (the rule is in the skill; its use is the cycle's).
- `remarks_check.HEADING` (the author's concern 4): outside the range; one probe (`#` + 80,000 spaces + `x`) ran in 0.0 s, so I could not confirm a quadratic case.

## Checks run

| Command | Exit |
|---|---|
| `git rev-parse HEAD`; `git log 5f2c155..9cf2633`; `git diff 5f2c155..9cf2633` for `cycle_stages.py`, `record_template.md`, `SKILL.md`, `decisions.md`, `audit_count.py` (read whole where changed) | 0 |
| `python -B gate/run_tests.py process-audit` | 0 — 72 tests OK, 312 s |
| `python -B -m unittest discover -s task-cycle -p test_cycle_stages.py` | 0 — 41 tests OK |
| `python -B elements/common/foundation_check.py` | 0 — 0 errors |
| `python -B task-cycle/tracked_private_paths_check.py tracked-file-private-paths` | 0 |
| scratch `scratchpad\scratch5.py` (outside the worktree; temporary repositories through the tests' helpers): S1 baseline, S2 third turn, S3/S3b `none` cases, S4 prose, S6 merged `#`, S7 doubled item, S8 `..`, S9 control character; timings of `files_named` on 2 MB crafted texts | 0; results as above |
| a probe of a real Codex rollout's first items (`~/.codex/sessions/2026/10/26/...`) | 0; injected AGENTS.md message precedes the prompt |
| `git status --short` after the checks | empty |

Not run: the full suite and `gate/run_tests.py task-cycle` (the cycle's own runs; the author reports 0); a run of `cycle_stages.py` on the live session (the author's; the transcripts are not mine to reread).
Unverified: the Codex reading on a plain-text subagent rollout; that the conforming dispatches of a later cycle will name the findings file in both messages (a convention).

## Reaches beyond the dispatch

- `process-audit/audit_count.py` lines 1-200 (docstring and constants) and 496-810, read; `task-cycle/remarks_check.py` `reads_none`, `HEADING` (grep and a probe).
- `foundations/decisions.md` WAY-338 (whole) — to check the sentence on series.
- `task-cycle/skill/SKILL.md`, `task-cycle/review/whole_change.md`, `task-cycle/skill/correction.md`, `task-cycle/change/SKILL.md` (grep of "findings file" only) — to see which messages may name a findings file.
- `foundations/part_map.md` (grep of `cycle_stages`) — the out-of-scope note.
- One local Codex rollout, first 17 items — Minor 3.

## Unread material

- `task-cycle/test_cycle_stages.py` and `process-audit/test_audit_count.py`: read by test names and the helpers I used; not every new test body (I ran them).
- `task-cycle/cycle_stages.py`: read the diff and the Codex/Claude reading code around it, not the whole file again.
- `task-cycle/skill/SKILL.md`: the changed sentence and its passage only.
- WAY-336's neighbours and the rest of the decisions of scope `task-cycle`: not read.

## Searches not found or unclear

- A part-map entry naming `cycle_stages.py` as a trust boundary: not found.
- A plain-text agent-to-agent message in a Codex rollout: not found on this machine (the author's search agrees), so Minor 3 is shown from the injected context only.
- Whether a real later cycle's whole-change review message names an earlier round's findings file: not found in what I read; Minor 1 shows the effect, not the likelihood.
