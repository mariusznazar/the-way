PASS e82cbab6ea2d63939f85c9dcb6edbd74e6df517b

# Review of the fix of the whole-change review's findings — task `decision-log-reading-index`

- Range: `55f1a24..e82cbab` (`d6599c7` for I1, `e82cbab` for m1–m5); `git rev-parse HEAD` gave
  `e82cbab6ea2d63939f85c9dcb6edbd74e6df517b`, tree clean.
- Method: `task-cycle/review/SKILL.md` and `task-cycle/review/fix.md`, read whole. Bound: the findings
  file `reports/whole-findings.md` (I1, m1–m5), read whole; the fix report `reports/fix-whole-report.md`,
  read whole as claims; the diff of the range, read whole (9 files, +161 −46).

Each finding of the file: I1 fixed, m1 fixed, m2 fixed, m3 fixed, m4 fixed, m5 fixed. No new
Critical or Important finding in the fix. New Minor findings: 3 (n1–n3), none blocking.

## Each finding of the findings file

**I1 — fixed.** WAY-150's second sentence (`foundations/decisions.md:1474-1486`) now reads "Of the
decisions it finds by *Scope*, by a line `decision:` or as the task or the work's source names them,
whoever selects reads the index and opens whole only …; each other entry it selects — an invariant,
an entry of the map of a touched part, or an entry, a decision included, that these or the decisions
of the index link to as far as the work needs — it reads whole". Checked against each place the
finding named:
- the complying example (`:1513-1517`, "reads whole the invariants naming `gate` or `every` and the
  entries they link to") now does what the sentence says;
- step 3 of "Reading the foundation" (`elements/common/way_of_working.md:113-117`, "the entries these
  and the decisions of step 2 link to … as far as the work needs them, each whole") says the same;
- step 2 (`:98-107`) now opens "Read the index. Of its decisions, open whole only …" and ends "The log
  beyond the index, the entries opened and the decisions step 3 reaches by a link is not read", so it
  no longer contradicts step 3;
- in a sectioned log the third paragraph still has the sections' decisions "take the place of those
  found by *Scope*", so "the decisions it finds by *Scope*" reads as the index's decisions there too;
- rows 1, 2, 3, 5 and 6 still say what they said; the reading of linked entries is back to what it
  was at the base. `python -B elements/common/foundation_check.py` exits 0 (WAY-150's changed
  binding sentence stays held by its pair of examples, WAY-12).

**m1 — fixed.** `json_lines` (`task-cycle/cycle_measures.py:201-232`) now ends with exit 2 and
`Error: <file>:<line>: the line is too large to read into memory` for a `MemoryError` both in reading
a line and in parsing it; `read_subagent_name` (`:396`) and the Codex arguments (`:472`) catch it as
well. My own crafted runs (in process, `json.loads` or the file's iterator made to raise
`MemoryError`): a third line too large to parse → exit 2 naming line 3; the iterator failing at the
first line → exit 2 naming line 1; a meta file too large to parse → exit 2 naming the meta file; a
real result of 60 000 000 bytes → exit 0, counted whole. See n1 and n2 for what is left around it.

**m2 — fixed.** `task-cycle/test_cycle_measures.py`, `test_an_output_that_is_no_text_is_not_counted`
loops over `(5, {"text": "a"})`; both assert.

**m3 — fixed.** `task-cycle/skill/SKILL.md:560-564` now names, for each agent, the bytes and reads of
the decision log and of the index, with WAY-339.

**m4 — fixed; the choice of exit 0 is right.** `elements/common/decision_index.py:133-146` writes
`Parts that no Scope names: <part>, ….` after the counts line where a given part is named by no
*Scope*, and nothing where all are. On the real log, `--section "Review of a change" --part task-cycle
--part task-cycel --part task-cycle` gives exit 0 and "Parts that no Scope names: task-cycel." (each
part once, the duplicate collapsed); `--part task-cycle` alone gives no such line. An exit 2 would be
wrong: the work may touch a new part that no decision names yet, and the agent would get no index at
all; WAY-344 is about a missing field of a file, which a part absent from every *Scope* is not. The
line stands in the index, which the reading rule has the agent read, so the typo shows where it
matters. The new test asserts both the line and its absence.

**m5 — fixed.** `project-level/lead/answering.md:9-10` and `project-level/lead/skill/SKILL.md:35-38`
rewrapped with words unchanged; `task-cycle/cycle_measures.py:83-84` rewrapped. No added line of the
range is over 100 characters (one is 103 bytes with two em dashes, 100 characters).

## The fix agent's concern, judged

**n3 (Minor, within the task) — "the index of its whole selection" for the reviewer still takes in
linked decisions, which WAY-150 now reads whole and outside the index.** WAY-150's first sentence puts
"the entries these link to as far as the work needs" into the selection; its clause "the reviewer of
the whole change reads the index of its whole selection" (`foundations/decisions.md:1482-1483`), its
violating example "the reviewer of the whole change leaves decisions of its selection out of the index
it reads" (`:1537-1538`), the same words in `elements/common/way_of_working.md:108-110` and the count
"how many decisions of the index you read whole" in `task-cycle/review/SKILL.md:31-32` all read, taken
strictly, as if a linked decision had to be in the index too. Minor: a reviewer that reads such a
decision whole knows it better than from its index line, no check or reader acts on which decisions
the index held, and WAY-287's item turns on "did not read the index of its whole selection", which a
reviewer that ran the script on its selection and read linked decisions whole has not done in any
sense that loses a decision. The clean wording, for a later change or the same round: "the index of
the decisions of its whole selection that it finds by *Scope*, by section, by a line `decision:` or
by name", and the same in the violating example.

## New findings in the fix diff

**n1 (Minor, within the task) — a `MemoryError` after a line is parsed still ends with a traceback.**
`task-cycle/cycle_measures.py`: `json_lines` is a generator, and its `except MemoryError` covers only
the reading and parsing of a line; the work its callers do on the parsed line — `names_log`
(`text.replace`, the regular expression), `result_text` (`"".join`), `ReadCounter.result`
(`text.encode`) — runs outside it. My crafted run with `names_log` and with `result_text` made to raise
`MemoryError` ended with the exception raised out of `main` (a traceback, exit 1). Minor: once
`json.loads` has held the line, a further copy of its text running out of memory is rarer still than
m1's case; the plan's "never with a traceback" would be met wholly by catching `MemoryError` once in
`main` around the reading, with an `Error:` line and exit 2.

**n2 (Minor, within the task) — the error for a meta file too large to parse gives no reason.**
`task-cycle/cycle_measures.py:396-397`: `MemoryError` has an empty message, so the line reads
`Error: cannot read …\agent-a.meta.json: ` and stops there (my crafted run). The file is named, which
WAY-344 asks; the reason, as `json_lines` gives it ("too large to read into memory"), is missing.

## Checks

| Command (from the worktree's root) | Exit | Result |
|---|---|---|
| `git rev-parse HEAD`; `git status --short` | 0 | `e82cbab…`; clean |
| `python -B -m unittest -q task-cycle/test_cycle_measures.py` | 0 | 87 tests OK |
| `python -B -m unittest -q elements/common/test_decision_index.py` | 0 | 16 tests OK |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |
| `python -B elements/common/decision_index.py --output .runs/review-whole/i.md --section "Review of a change" --part task-cycle --part task-cycel --part task-cycle` | 0 | "Parts that no Scope names: task-cycel." |
| `python -B elements/common/decision_index.py --output .runs/review-whole/i2.md --part task-cycle` | 0 | 96 in full, no such line |
| `python -B .runs/review-whole/crafted_fix.py .runs/review-whole/crafted` — six crafted cases run in process against `cycle_measures.main` | 0 | parse `MemoryError` at line 3 → exit 2 naming line 3; iterator `MemoryError` at line 1 → exit 2 naming line 1; meta `MemoryError` → exit 2 naming the file (n2); 60 MB result → exit 0, counted; `MemoryError` in `names_log` and in `result_text` → raised out of `main` (n1) |
| a search of the added lines of the range for lines over 100 characters | 0 | one line of 103 bytes, 100 characters |

Not run: the full gate (the orchestrator's); the whole directories `task-cycle` and `elements/common`,
whose other tests the fix does not touch (the fix report gives 478 and 232 tests OK).

## Reaches beyond the dispatch

- `foundations/decisions.md` WAY-150 at the head, whole (`:1466-1590`), and `elements/common/way_of_working.md:58-124`,
  to judge I1 and the concern.
- `task-cycle/review/SKILL.md:28-33` and `foundations/decisions.md` WAY-287's binding sentence, for the
  concern (n3).

## Working copies

`.runs/review-whole/` held `crafted_fix.py`, its transcripts and results under `crafted/`, and the
two index files of the checks. The directory was removed before return; nothing kept in `reports/`,
since the results stand in this report.

## Unread material

- Decisions read whole for this review: 1, WAY-150. Of WAY-287 only its binding sentence was read
  again (it was read whole in the review of the whole change, and the fix does not touch it). No
  index was written for this review: a fix review reads what its findings file bounds, and the
  selection of the review of the whole change stands.
- `task-cycle/test_cycle_measures.py` and `elements/common/test_decision_index.py` beyond the hunks the
  diff changes were not read again.
- Otherwise `none`.

## Searches not found or unclear

- Whether "the index of its whole selection" (WAY-150, `way_of_working.md`) and the count "of the
  index" (`task-cycle/review/SKILL.md`) take in decisions reached by a link, which WAY-150 now reads
  whole outside the index: unclear (n3, the fix agent's concern).
