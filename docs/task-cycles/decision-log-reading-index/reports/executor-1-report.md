# Executor report, slice 1 — The index script

**Status:** `done`

**Commits (branch `task/decision-log-reading-index`, on top of `0023a28`):**
- `b34ed51` Add the failing tests of the decision index (test file and stub of the script)
- `30c5b1b` Add the script that writes the index of a product's decisions (script, tests made to pass, part map sentence)

**Files changed (against `0023a28`):**
- `elements/common/decision_index.py`: new, about 190 lines (the stub of `b34ed51` was 12 lines)
- `elements/common/test_decision_index.py`: new, 15 tests
- `foundations/part_map.md`: +2 / −1 (the sentence of `elements-common` now names the script among what the part answers for)

## Checks run

1. First failing run, before the implementation (stub in place):
   `python -B -m unittest discover -s elements/common -p test_decision_index.py -k test_section_lists_its_decisions_in_full`
   exit 1, `AssertionError: False is not true : no file written`. This is the two-section test, failing on its assertion.
   The full file at the stub stage gave exit 1 (8 failures, 7 errors). The errors come from reading the output file the stub never writes, not from a missing module.
2. `python -B -m unittest discover -s elements/common -p test_decision_index.py`: exit 0, `Ran 15 tests`, `OK`. One earlier run failed on a bug in my test (a leftover output file between two runs); I fixed the test by removing the file between the runs, without touching any assertion.
3. `python -B elements/common/decision_index.py --sections --output .runs/executor-1/sections.md`: exit 0. 28 sections (the handoff range is 20–30).
4. `python -B elements/common/decision_index.py --part task-cycle --output .runs/executor-1/index.md`: exit 0. 96 decisions listed in full. An independent count of decisions whose *Scope* names `task-cycle` as a whole item, written without the foundation_check helpers, also gives 96.
5. `python -B elements/common/foundation_check.py --skip-test-citations`: exit 0, `0 errors`, no listed lines. Output in `.runs/executor-1/foundation_check.txt`.
6. `python -B -m unittest discover -s elements/common -p "test_*.py"` (regression over the directory, 216 tests): exit 0, `OK`.
7. Own-work check (below), plus the error-path runs on the real log: `--section Nope` gives exit 2 with `Error: foundations/decisions.md: no section "Nope"`.

Not run: the product's full gate (the orchestrator runs it, per the handoff).

## Own-work check

- **Requirement:** the index must read a CRLF log with a byte-order mark the same as an LF log, since the handoff names both.
- **Check:** I wrote a copy of the real `foundations/decisions.md` with a BOM and CRLF endings (bytes, no newline translation), ran `--part task-cycle` on both copies and compared the files.
- **Result:** byte-identical (`cmp` silent; `SAME`). The copy was removed afterwards.

## Reaches beyond the handoff

- `foundations/decisions.md` lines 1–90, 150–350, 600–660, 700–770, 1085–1120, 1460–1600, 2505–2540, 2700–2830 and the section headings list (`grep "^## "`). Read to check the reading and the log's form.
- `elements/common/foundation_check.py` lines 160–236, not named in the handoff, read to see `read`, `git`, `at_commit` and the constants next to the reading functions I import.
- `foundations/invariants.md` lines 84–95, 114–145, 346–357 (named) — no extra reach.
- `task.md` lines 33–42 and 56–66, checked against the copies in the handoff; they matched in substance.
- `.ai\rules\scripts.md` and `.ai\rules\git.md`, read before writing a script and before committing, as the global instructions require.
- A grep over `elements/common` for importers of `foundation_check`, to see which tests import it.

## Choices made

1. **Scope read in selection mode, for every decision of the log.** A decision without *Scope* (or with an empty one) stops the run with exit 2 even if only `--section` is given, because `--part` needs every decision's *Scope*. The alternative was to read *Scope* only for printed decisions. Cost if wrong: a log with one bad entry blocks sections it would otherwise print; minor.
2. **Section sentence checked only in `--sections` mode.** A section with no sentence stops that listing with exit 2, naming the section (WAY-18 says one sentence). Selection mode prints no sentence, so it does not check. Cost if wrong: none for the current log (all 28 have one).
3. **`--sections` with any other switch is exit 2.** The spec says `--sections` writes "instead", so I read combination as an error rather than silently ignoring the other switches.
4. **Title line differs for `--sections`.** Selection output opens `# decision_index.py: index of the decisions of the log`; the sections list opens `# decision_index.py: list of the sections of the log`. Both hold the script's name. Slice 5 should match on `decision_index.py`, not on the full line.
5. **Argument errors use the same message form.** argparse's own errors are routed to `Error: <message>` with exit 2 (a subclass of `ArgumentParser` raises the failure), so every exit 2 has one shape.
6. **Heading-only extras go after the full list** under `## Listed by heading alone`, in log order.
7. **Heading form:** `^### (NUMBER) — (question)$` with `NUMBER` = letters, digits, hyphens and a final `-N`. The em dash is written as `\u2014` in the source.
8. **Section identity by heading line,** so a section name repeated in the log would not merge two sections in the counts. The log has no repeated names; the case is not tested.

## Concerns and open points

- **A decision with no binding sentence is not an error.** The index prints nothing for it. The spec does not ask for this check, and WAY-05 says one to three binding sentences, so an entry without any is a form problem that only the check would catch. I did not add it. The current log has none, I did not verify that exhaustively.
- **The first commit is a failing state.** At `b34ed51` the new tests fail (as the failing-test step requires); the commit passes again at `30c5b1b`. A reviewer reading history should not run the gate at `b34ed51`.
- **Output files kept in `.runs/executor-1/`:** `sections.md`, `index.md`, `index_crlf.md`, `section_part.md`, `way150.md`, `foundation_check.txt`, `nope.md` is not there (the error run wrote nothing). These are check outputs the handoff asked for or that the report cites, not working copies; they are in an ignored directory. The CRLF working copy is removed.
- **No `git worktree` was made**, so nothing needed a `git worktree remove`.

## Unread material

- `.runs/task-cycles/decision-log-reading-index/task.md` lines 123–135 (Settlements to record): taken from the handoff copy, not read from the file. The handoff copy is the one the orchestrator gave.
- `foundations/decisions.md` WAY-150 and WAY-18 were read in their rewritten form at the head; I did not compare them with the plan's F1–F6 text.
- `foundations/decisions.md` other sections, the rest of the log, not read (the handoff did not name them).
- `elements/common/foundation_check.py` lines 1–160 read in full; lines 236–345 read in full; 974–989 read. Nothing unread from the named ranges.
- `elements/common/test_foundation_check.py` lines 1–30 read. Lines beyond 30 not read.
- `elements/common/way_of_working.md` lines 58–100 read; the rest of the file not read.
- `foundations/part_map.md` only lines 60–80 read (the named range is 65–75 plus the sentence I changed). Other parts not read.
- `foundations/invariants.md`: the three named ranges read; nothing else.
- `foundations/decisions.md` WAY-150 index sentence and the reading rule: read.

## Searches not found or unclear

- The handoff's "Scope" reading rule says items are joined by `,` or ` · `. The existing `located` helper also splits on newline, so a continuation line without a comma joins the items as well. This is what I want, and the test for multi-line *Scope* passes, but the handoff text does not say it.
- Whether the log has a decision whose *Verification* or *Scope* contains a `·` inside an item: not searched; the independent count of 96 would have caught a systematic mismatch.
- `decision_index.py` numbers: the heading form I accept is letters-hyphen-digits. I did not search whether any product uses another prefix form; the-way's log uses `WAY-NN` only.

## Path

This report: `.runs/task-cycles/decision-log-reading-index/reports/executor-1-report.md`
