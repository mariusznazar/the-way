# Findings of the review of the whole change for the fix (reviewer's words)

The review `reports/review-whole-report.md` returned `FAIL 55f1a24ddcece1ba8c48a5e27595a34072939359`. The blocking finding I1 and, after it, the Minor findings within the task that the review lists (m1–m5), word for word. m6 is outside the task's scope and is not to be fixed. The slice review's N1 is no finding.

## Blocking

**I1 — WAY-150 now leaves a decision that a selected entry links to unread beyond the index, while
its own example and the reading rule read it whole.** Comes from the plan's *Foundation entries*:
Fix 1, `dbdfdad` (F1, WAY-150), meeting slice 3, `3cec41a`, which kept step 3 of the reading rule as
it stood. It spans the foundation work and slice 3.

- Where:
  - `foundations/decisions.md:1474-1481` (WAY-150, first paragraph, second sentence): "Of the
    decisions it selects, whoever selects reads the index and opens whole only the decisions the
    work changes, goes against or proposes another answer to […] those whose sentence a test the
    work alters holds by a line `decision:` and those whose binding sentences leave open what the
    work has to do; each selected entry that is no decision — an invariant, an entry of the map of a
    touched part, or an entry other than a decision that these link to — it reads whole". The first
    sentence puts "the entries these link to as far as the work needs" into the selection, so a
    decision an invariant derives from, or a decision another selected decision names in
    *Relations*, is a selected decision: known from the index, opened whole only if it falls in one
    of the five kinds.
  - `foundations/decisions.md:1511-1516` (WAY-150's complying example): "reads whole the invariants
    naming `gate` or `every` and the entries they link to" — the entries an invariant links to are
    its *Derives from* decisions and *Rests on* facts, so the example reads those decisions whole.
  - `elements/common/way_of_working.md:113-117` (step 3, unchanged by slice 3): "and the entries
    these and the decisions of step 2 link to — *Relations*, *Based on*, *Verification*, *Derives
    from*, *Rests on* — as far as the work needs them, each whole." Step 2's switches add to the
    index only the decisions of *Decisions in play*, of the work's source and of `decision:` lines
    (`way_of_working.md:95-97`), so a linked decision never reaches the index; step 3 has it read
    whole instead. That contradicts step 2's own "Open whole only …" (`way_of_working.md:98-107`).
- Why it matters: WAY-150's binding sentence and the reading rule that restates it now say two
  things about the same decisions. An agent following `way_of_working.md` reads whole every
  decision that a selected decision or invariant links to — for this change, WAY-150 alone links
  WAY-21, WAY-33 and WAY-148 — which WAY-150's "opens whole only" forbids; an agent or reviewer
  comparing with WAY-150 holds such a decision to the index, which the rule never puts it in. That
  is the rule file restating the entry the change writes "differently, more broadly" (WAY-263), and
  a complying example that does what its sentence forbids, which no longer holds the sentence as
  WAY-12 asks of a pair of examples. Before `dbdfdad` WAY-150 read "it reads every other selected
  entry whole", which matched step 3 and the example; the fix report calls its change "wording
  only", but on linked decisions it changed the meaning.
- Evidence: the three passages above, at the head. `python -B elements/common/foundation_check.py`
  passes (exit 0), since no check reads this.
- What would fix it (one of two, the first smaller): (a) in WAY-150's second sentence, read whole
  the entries the selected entries link to as far as the work needs, decisions included, as step 3
  and the example say — for example "each selected entry that the index does not carry — an
  invariant, an entry of the map of a touched part, or an entry these link to as far as the work
  needs — it reads whole"; or (b) keep WAY-150, add the linked decisions to the index in step 2
  (`--decision`), drop "and the decisions of step 2 … each whole" for decisions in step 3, and
  rewrite the complying example. Variant (a) keeps the plan's sentence for slice 3 ("The
  invariants, the part map's entries, the glossary and the templates are read as before") true.


## Minor, within the task (fixed in the same round)

**m1 (within the task) — a line too large for memory ends `cycle_measures.py` with a traceback and
exit 1, not exit 2.** `task-cycle/cycle_measures.py:209-212`, `json_lines` catches `ValueError` and
`RecursionError` from `json.loads`, not `MemoryError`. Slice 5's *Goal* says "a huge text or a deeply
nested line end the reading with exit code 2 or are not counted, never with a traceback", and step 12
of `task-cycle/skill/SKILL.md:563-566` handles only an exit 2 with an `Error:` line. Minor: it needs
a single line that exhausts memory, and the transcript's writer is Claude Code or Codex. This is
review-5's M1, which I grade the same.

**m2 (within the task) — a subtest that asserts nothing.** `task-cycle/test_cycle_measures.py:1174-1177`,
`test_an_output_that_is_no_text_is_not_counted` loops over `(5, {"text": "a"}, None)` and, for
`None`, `continue`s before any assertion; the other two values assert. Drop `None` from the tuple
(its case is tested at `test_a_missing_field_of_a_call_or_an_output_ends_with_exit_2_naming_it`).
Review-5's M2; Minor, since the test as a whole still fails when the behaviour breaks.

**m3 (within the task) — step 12 describes the measures without the log and the index.**
`task-cycle/skill/SKILL.md:560-562`: "run `task-cycle/cycle_measures.py` … it counts the context
and the prompt cache of the cycle's agents." WAY-339's second paragraph (`foundations/decisions.md:7286-7291`)
now names, for each agent, the bytes and reads of the decision log and of the index, and *To do* 8
is about exactly that count. The sentence is not false, only short; an orchestrator reading it does
not learn that the file holds the measure the request's "before" figures come from. Slice 5's
executor reported it; the file is slice 4's.

**m4 (within the task) — a `--part` that no decision names gives an index silently empty of it.**
`elements/common/decision_index.py:109-128`: `python -B elements/common/decision_index.py --part
no-such-part --output …` exits 0 with "Listed in full: 0. Listed by heading alone: 0." With
`--section` given, a misspelled part drops, without a sign, the headings of the decisions outside
the sections — the safeguard F3 and WAY-21's rationale keep "so that a decision of another topic
that governs a touched part" is not lost. An error would be wrong (a new part may have no decision
yet), but a line in the index or on stderr naming each given part that no *Scope* names would show
the typo. Minor: a reasonable user's expectation the plan's list of exit codes does not cover.

**m5 (within the task) — lines past the files' width.** `project-level/lead/answering.md:9` (137
characters; slice 3 rewrapped the line before it and left this one long: "revisions checked. Expand
to the complete source units needed for each question. Unreadable sources are obstacles, not
negative evidence."); `project-level/lead/skill/SKILL.md:35-36` leaves "a large definition/plan by"
as a short line; `task-cycle/cycle_measures.py:83` (124 characters, review-5-fix's N2). Polish.

