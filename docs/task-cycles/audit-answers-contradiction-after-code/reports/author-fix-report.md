# Author report — the fix of the review of the whole change

**Status:** done

**Commit:** `428cc45` (one commit, by path). Range of the fix: `ab2c8c801b2ba9170a00ed6056b8b7c56b062868..428cc45`.
The worktree is clean.

Files changed (added / removed): `foundations/decisions.md` 24/10, `process-audit/record_items.py` 57/17,
`process-audit/test_audit_count.py` 35/3, `process-audit/test_record_items.py` 63/4,
`process-audit/SKILL.md` 4/1, `task-cycle/record_template.md` 3/1, `task-cycle/skill/SKILL.md` 4/2,
`task-cycle/skill/reserved_return.md` 2/2, `task-cycle/skill/correction.md` 3/1.

## The findings

- **I-1 (blocking, WAY-344): fixed by a proposed narrowing, no change of the behaviour.** WAY-344 is edited
  in place with one new binding sentence: "Where the command that counts the audit reads a cycle's record that
  lacks a line or an item it reads of it — the line `Process pin` or `Target branch and base`, or the item
  `Process remarks on the-way`, `Discarded attempt`, `Review rounds`, `Plan` or `Slices returned too large` —
  the record is of an earlier form and no field is missing: the command gives the values that need it as
  unknown, with a reason that names the line or the item, no line `Error:` and no change of the exit code."
  The list is from the code: `process_pin` reads `Process pin` and, for the-way's own cycles, `Target branch
  and base`; `remarks_count`, `read_contradiction`, `read_rounds`, `read_plan` and `read_too_large` read the
  five items. Its *Verification* gained a `tests:` clause for it; its *Rationale* gained one sentence (a record
  lacks what the template gained after it was written and carries no sign of its form). *Rejected* and the
  pair of examples are as they were. The test that holds it is
  `test_audit_count.ProcessPin.test_a_record_that_lacks_every_line_and_item_the_count_reads_is_of_an_earlier_form`
  (cites the sentence by a line `decision: WAY-344`): a product's record with no pin and none of the items, and
  a the-way cycle with neither the pin nor the target line, run through the command, assert exit code 0, no
  `Error:` on stderr and, for each line or item, a reason that names it. `process-audit/SKILL.md` (matter 1) says
  the same for the session. WAY-33 search: the entries that name WAY-344 (the guidelines `coding.md`,
  `coding-measuring-report.md`, `coding-generator.md`, the template of invariants, WAY-294 which narrows it,
  decisions at 7137, 7871, 10035, 10135) point to it or narrow it for other files; none restates the part
  narrowed, so none needed a change. I did not change the code to give `Error:` and exit 1.
  **This entry change is `the cycle's`** (no row carries it; it narrows an approved decision, WAY-30). Meaning,
  EN: A cycle's record that lacks a line or an item the audit's count reads of it is of an earlier form, so the
  count gives the values that need it as unknown with a reason that names it, with no `Error:` line and no change
  of the exit code. PL: Zapis cyklu, w którym brakuje linii albo pozycji, które czyta liczenie audytu, jest
  zapisem starszej formy, więc liczenie daje wartości, które jej potrzebują, jako nieznane z powodem
  nazywającym tę linię albo pozycję, bez linii `Error:` i bez zmiany kodu wyjścia. No pair of examples added.
- **M-1 (Minor): fixed.** The smallest form I chose: one entry for each discarded attempt. A cycle that discarded
  one attempt writes the item as before (`reason: `<marker>`; ...` in its text). A cycle that discarded more
  writes nothing after the colon and, under the line, one list entry for each attempt, each opening with its own
  `reason: ` and marker; the template, the two paragraphs of `task-cycle/skill/SKILL.md`, the section "Discard
  the attempt" of `reserved_return.md` and `task-cycle/skill/correction.md` say so ("an entry of its own where
  the cycle discarded an attempt before"). The count (`discarded_entries`, `discarded_reasons` in
  `process-audit/record_items.py`) reads each entry's marker and gives `yes` where any is `open design choice`;
  an entry that opens with no marker, or reads `none`, or holds two markers, gives `unknown` with "an entry of the
  item `Discarded attempt` opens with no marker of its reason" (unless another entry is an open design choice);
  a text with two markers in the one-attempt form, or text beside entries, gives the reason of its own "holds more
  than one reason in a form that is not read: write nothing beside its colon and one entry for each attempt";
  the reason "opens with no marker of its reason" (reworded from "holds no marker", which was false for some
  texts) stays for a text that opens with none. WAY-405 states the form. The three markers and the place of
  *To do* 6 are kept. Way rejected: a second marker inline in the one text — it brings back a search of the text
  for markers, which question 5 refused. Tests: `test_record_items.py` (two markers give the reason of their own
  and not the false one; entries in either order give yes; an entry with no marker, with `none` or with two
  markers gives unknown; text beside entries; nested and fenced entries not read; entries with the rounds) and
  `test_audit_count.ProcessVersions.test_the_marker_of_a_discarded_attempt_gives_q1` (two entries through the
  command: `yes` and `no`). Cost if wrong: one form of the template and one function change.
  Found while testing: an entry of two markers was first read as a reason; the new test caught it, fixed.
- **M-2 (Minor): fixed.** WAY-405 now reads "an item that reads neither `none` nor a marker, written in any
  earlier form, gives the answer unknown".

Foundation entries written in this fix: WAY-344 (the narrowing, `the cycle's`, meaning above) and WAY-405
(edited for M-1 and M-2; it stays `row 4`, its sentences give the form the row names and the entries form is its
smallest extension, which is why I name it here: it is the one part beyond the row's text, and the human sees it
in the diff of WAY-405 — mark it `the cycle's` in the request if the orchestrator reads it so).

## Checks (command, exit code)

- `python -B gate/run_tests.py process-audit` — 0 (262 tests).
- `python -B gate/run_tests.py task-cycle` — 0 (534 tests, 1 skipped).
- `python -B gate/run_tests.py elements/common` — 0 (246 tests).
- `python -B elements/common/foundation_check.py` (no `--skip-test-citations`) — 0, `0 errors`.
- Ruff `check --config ruff.toml --no-cache --ignore-noqa process-audit`, the pinned executable of the main
  checkout's `quality-venv`, written to a file — exit 1 with the same 4 reports as before the fix, all on lines this
  change did not write (`audit_count.py` 2126, 2339, 2413 `UP037`; `test_audit_count.py` 2451 `F541`, the line of
  commit `b6f800c`, moved by my added lines).
- Mutations of the new reading (an entry of two markers read as a reason, entries read beside text, `none` read as a
  reason, the unknown of a marker-less entry dropped, only the first entry read, nested entries read): six, all
  caught by `test_record_items`.
- Not run: the product's full gate (by the handoff); `elements/part-map` and `agent-instructions` (no code or
  part-map change of mine in this fix; the first fix commit left them as they ran before).

## The own-work check

- **Requirement most likely unmet:** I-1 — that no behaviour changes while the decision now says what the code does.
- **Check:** the test above, run on the code of `ab2c8c8` unchanged in this respect (exit code 0, no `Error:`) and on
  the head; and the grep for other restatements. Result: exit code 0 and no `Error:` on both; the narrowing's list of
  seven lines and items matches the readers in the code.

## Reaches beyond the handoff

None beyond the findings file, the handoff and `task-cycle/change/fix.md`. I re-read WAY-344 whole (the entry, as
the finding asks) and the code the finding names.

## Working copies

`.runs/author-fix/` held the scripts and outputs of the checks; it stood at
`.runs/author-fix/` and was removed before this
return.

## Unread material

none (everything the handoff names was read whole; the only entries of the foundation I searched for by word were the
WAY-33 hits above, read at their lines).

## Searches not found or unclear

- None found missing. Unclear: the handoff says "one blocking, two Minor"; the findings file's I-1 *Recommended fix*
  also names `Process remarks on the-way` among the items; the list in WAY-344 follows the code, which includes the
  lines `Process pin` and `Target branch and base` beside the five items.
