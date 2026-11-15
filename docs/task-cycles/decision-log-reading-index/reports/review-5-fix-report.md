PASS 55f1a24ddcece1ba8c48a5e27595a34072939359

# Review of the fix of slice 5's finding I1

Fix range `e1ab383..55f1a24` (one commit, `55f1a24`), files `task-cycle/cycle_measures.py` and
`task-cycle/test_cycle_measures.py`. `git rev-parse HEAD` printed `55f1a24ddcece1ba8c48a5e27595a34072939359`.
Bounded by the findings file `reports/slice-5-findings.md` (I1 alone), per `task-cycle/review/fix.md`.

Counts: blocking 0; findings of the file: I1 fixed; new Minor 2; out of scope 0.

## The finding of the findings file

### I1 — fixed

- Claude Code: `read_claude_blocks` (`task-cycle/cycle_measures.py:316-326`) now returns early only for a
  line whose `type` is neither `assistant` nor `user`, and reads `message` and `message.content` with
  `member`; a content present but not a list stays not counted. Codex: `read_codex_record`
  (`task-cycle/cycle_measures.py:440-447`) reads `payload` with `member`. `result_text`
  (`task-cycle/cycle_measures.py:268-283`) reads the `text` of each block of the counted kinds with `member`,
  naming `<label>[i].text`.
- Evidence, my own crafted inputs (each a separate process of the script at the fix head):
  `user_content_missing`, `user_content_null`, `assistant_content_missing`, `assistant_content_null` → exit 2,
  `no field message.content`; `user_message_missing` → exit 2, `no field message`; `text_missing`,
  `text_null` → exit 2, `no field message.content[0].content[0].text`; Codex `payload_missing`,
  `payload_null` → exit 2, `no field payload`; `input_text_missing`, `input_text_null` → exit 2,
  `no field payload.output[0].text`. Each: no traceback, no file written. Every one of these cases was exit 0
  with zeros at `e1ab383`.
- What stays not counted, as the plan allows and my finding asked: a content that is a number or a string, a
  text that is a number (the other blocks still count: `text_number` gave `2 | 1`), an image block, a Codex
  payload that is a list or a string, a line of another type without `message` (`system`, `attachment` with a
  null message), an `api-request-blob` line with a broken text block, a `<synthetic>` assistant line without
  content — each exit 0 with the expected figures.
- The `"DELETE"` subcase left `test_a_content_that_is_no_string_or_list_is_not_counted_and_ends_no_run`
  (`task-cycle/test_cycle_measures.py:438-445`), and so did `None`, which now ends with exit 2 (a `null` is a
  missing field for `member`; the docstring says so at `task-cycle/cycle_measures.py:80`). Four new tests
  assert exit 2 and the field's name (`task-cycle/test_cycle_measures.py:523-548`, `1183-1197`). I ran the
  fix head's tests against the code of `e1ab383` (copied beside them): 11 of 83 failed, all in the new tests,
  so they fail when the behaviour breaks.
- The stricter reading ends no real run: the script at the fix head on the 150 latest Claude Code sessions
  (with their subagents) and the 15 Codex orchestrator rollouts (with theirs) ended 150 of 150 and 15 of 15
  with exit 0, no `Error:`.

## New findings in the fix diff

### Minor

**N1. The `type` of a block or payload stays outside the check (the fixer's choice, which I was asked to
judge).**

- Place: `task-cycle/cycle_measures.py:82-83` (docstring: "The `type` that tells one kind of block or record
  from another is not checked"), `:331-338` and `:445-447` (a block or payload without `type` is passed over),
  `:276-278` (a result block without `type` is not text).
- Judgement by WAY-344: the letter covers it — `type` is a named thing the script looks for data by, and a
  block without it is read as "another kind", so a rename of `type` would give the four figures as `0` with
  exit 0, the quiet pass of I1 (crafted `block_type_missing`: a result list `[{"text": "ab"}]` counted as a
  read of 0 bytes; `result_block_no_type`: a result without `type` not counted). I grade it Minor, not
  Important, and do not reopen I1, for three reasons: (1) the plan's sentence that "a list of blocks that are
  no objects" is not counted and its test of junk blocks (`{}` among them) treat a block of an unknown kind as
  not counted, and a block with no `type` is not distinguishable in kind from one with an unknown `type`; the
  unchanged line-level `type` is read the same way, so checking only the block's would be uneven; (2) the
  docstring now states the choice, so no reader takes the figures for checked where they are not; (3) `type`
  is the key on which every block of both formats is dispatched, the least likely key to be renamed alone. I
  said in the first round I did not require it; nothing new changes that.

**N2. One docstring line is 124 characters long.**

- Place: `task-cycle/cycle_measures.py:83`. The rest of the file wraps near 100 (the longest elsewhere is
  104, already there before). Polish only.

## Considered and not a finding

- A Claude Code `user` line whose `message` is a list or a string now ends with `no field message.content`
  (crafted `user_message_list`, `user_message_str`): the wording says "no field" where the field's holder has
  the wrong type. Exit 2 with the file, the line and the field named is what the plan allows for such content;
  no real line has that form (150 sessions ran clean).
- A result for an id no call names, with a text block lacking `text`, now ends the run (crafted
  `text_missing_unknown_id`): the field is missing in a line the reading reads, so WAY-344 asks exactly this.
- `process-audit/` is unchanged in the range (`git diff --quiet e1ab383..55f1a24 -- process-audit`, exit 0).

## Declined to judge

- M1 and M2 of the first round: outside the findings file (not to be fixed).

## Checks

| Check | Command or method | Exit code / result |
|---|---|---|
| Head | `git rev-parse HEAD` | 0, `55f1a24ddcece1ba8c48a5e27595a34072939359` |
| Range | `git log --oneline e1ab383..55f1a24`, `git diff --stat e1ab383..55f1a24`, `git diff e1ab383..55f1a24` | 0; one commit, two files |
| The slice's check 1 | `python -B -m unittest discover -s task-cycle -p test_cycle_measures.py` | 0, 83 tests OK |
| New tests against the old code | the fix head's `test_cycle_measures.py` beside `git show e1ab383:task-cycle/cycle_measures.py` in `.runs/review-5/old/`, `python -B -m unittest discover -s .runs/review-5/old -p test_cycle_measures.py` | 1, 11 failures, all in the four new tests |
| Private paths | `python -B task-cycle/private_paths_check.py <file>` for each of the two files | 0 and 0, 0 listed |
| `process-audit` untouched | `git diff --quiet e1ab383..55f1a24 -- process-audit` | 0 |
| Crafted input | `python -B -I .runs/review-5/crafted.py <worktree> task-cycle/cycle_measures.py <out>` (30 cases, each a subprocess) | 0; results above |
| Real sessions | `python -B -I .runs/review-5/real.py <worktree>`: the 150 latest Claude Code sessions and 15 Codex orchestrator rollouts | 0; 150/150 and 15/15 exit 0, no traceback |
| Line lengths | a count of lines over 100 characters at both heads | line 83 new at 124 (N2) |
| Worktree untouched | `git status --short` | 0, empty |

Not run: `python -B -m unittest discover -s process-audit -p test_audit_count.py` — the fix range changes no
file under `process-audit/` and not the file's labels it reads, so it cannot tell this fix from a broken one
(it passed at `e1ab383` in the first round, 182 tests). The gate: the cycle's own run.

## Reaches beyond the dispatch

- Real Claude Code transcripts and Codex rollouts on this machine, run through the script for exit codes and
  summed figures only, to check that the stricter reading ends no real run.

## Working copies

- `.runs/review-5/` in the worktree held `crafted.py`, `real.py`, `crafted.txt`, the folder `old/` (the old
  script beside the new tests) and `work/` (crafted transcripts and outputs). I removed the whole directory
  before returning (`Test-Path` then printed `False`); nothing remains. No worktree or clone was made.

## Unread material

none. Read whole: `task-cycle/review/fix.md`, the findings file, the fix report, the diff of the fix range;
the changed functions at the fix head through the diff and the crafted runs (the rest of the two files I read
in the first round and the range does not change).

## Searches not found or unclear

none.
