FAIL 2dca687367fb016839219488d08511ddf83e8e11

# Review of the whole change — ai-review-fixes-from-24-11

Range: `07aa55df565d5f10428176c89d20d2c6420a6dfd..2dca687367fb016839219488d08511ddf83e8e11`
(`225bf1c5` the change, `2dca6873` the re-wrap of two README lines). `git rev-parse HEAD` in the
reviewed worktree is `2dca687367fb016839219488d08511ddf83e8e11`, the head given. One author, no
plan, no slice: every finding below comes from no slice (`slice: none`).

Counts: blocking 2 (Important), Minor 2, out of scope 0.

## Findings

### Important

**I-1. The new check names a decision by its zero-padded label, so in a log whose headings write the
number otherwise a changed decision is never seen as changed and the error WAY-12 requires becomes a
listed line.** Slice: none.

- Place: `elements/common/foundation_check.py:813` (the heading pattern of `entry_texts` keys each
  decision by the text of its heading, `ABC-1`), `elements/common/foundation_check.py:833` (the
  label it is looked up by is `"%s-%02d" % (self.prefix, key)`, `ABC-01`) and
  `elements/common/foundation_check.py:844-846` (the comparison `before[path].get(entry) !=
  now[path].get(entry)` reads `None != None` for such a label on both sides).
- What is wrong: every other reading of the log in this script keys a decision by the value of its
  number — `read_decisions` accepts `[0-9]+` and keys `self.bodies` by `int`, `check_held` compares
  `before.get(key)` by `int`, and `decision_index.py` takes `7`, `WAY-7` and `D-07` as one decision.
  The new check alone keys the decision side of "changed" by a string re-formatted with two digits.
  For a heading `### ABC-1 — …` (or `ABC-007`), the decision side is always "unchanged", so an old
  gap stays a listed line even when the change rewrites that decision — the one case WAY-12's new
  paragraph, written by this change, makes an error ("where a change adds or alters either of the two
  entries as a whole"). The invariant side still works, so a newly added invariant is caught; what
  is lost is the case the task's Question 2 chose the whole entry for: "it leaves the gap where
  someone changes the decision and should see what stands on it".
- Why it matters: the gap is exactly the one the task sets out to stop, and it is lost silently — a
  listed line stops nothing, and nothing in the output says the decision side was not compared. The
  form is not exotic: the script and the index script accept it, and the template's `WAY-NN` is a
  placeholder that three-digit numbers such as `WAY-100` already exceed. The fix is local: key the decisions' texts by
  `int(number)` as `base_paragraphs` does, and add a test whose log writes a number without a
  leading zero.
- Evidence: probe `.runs/task-cycles/ai-review-fixes-from-24-11/reports/review-whole-2-probe-linked.py`
  (command: `PYTHONIOENCODING=utf-8 python -B review-whole-2-probe-linked.py <root of a worktree of
  the head>`; it subclasses the test class, so it also reruns the inherited tests and prints the
  three probe cases between them; output of the three cases kept in
  `.runs/task-cycles/ai-review-fixes-from-24-11/reports/review-whole-2-probe-linked-output.txt`). The
  same old gap with the decision's rationale changed gives, with the heading `ABC-01`:
  `foundations/decisions.md:10: `save-keeps-name` derives from `ABC-01`, … and this change adds or
  alters one of the two entries: …` / `1 error`; with the heading `ABC-1` and nothing else
  different: `foundations/decisions.md:10: listed: `save-keeps-name` derives from `ABC-01`, …` /
  `0 errors`.

Contradiction: yes — WAY-12, third paragraph ("The check of the foundation reports as an error an
invariant whose *Derives from* names a decision whose *Verification* does not name that invariant,
where a change adds or alters either of the two entries as a whole"), written by this change; and
the task's Question 2 answer ("cały wpis — każda zmiana niezmiennika albo decyzji").

**I-2. *Rejected* of WAY-12 and WAY-30 holds ways the rows' sources do not keep, one of them the
writer's own derivation, against WAY-134.** Slice: none.

- Place: `foundations/decisions.md:834-839` (WAY-12) and `foundations/decisions.md:1344-1345`
  (WAY-30).
- What is wrong: WAY-134 gives "a decision written from a row as its rejected options only the ways
  not chosen that the row's source keeps, `none considered` where the human said so, or `unknown`",
  and keeps out "a way that is itself a way of the process rather than of the product, such as how
  or when an answer is recorded"; `elements/decisions/template.md:93-101` repeats it: "A way the
  writer derives — from what the cycle would otherwise guess, from the cost of the way chosen, or
  from the foundation — never enters it (WAY-134)." Row 2's *Source* is "pytanie 2 (*Not chosen*
  tam)", whose *Not chosen* holds one way: "stroną jest pole z powiązaniem". WAY-12's *Rejected*
  gains three:
  - "an error only where the *Derives from* of the invariant or the *Verification* of the decision
    changes — it leaves the gap where someone changes the decision and should see what stands on it"
    — Question 2's way not chosen; it may stand;
  - "an error for every such invariant — no change passes until all the older gaps are closed" —
    stands nowhere in the task; the writer derived it from the foundation, by analogy with WAY-12's
    older "an error for every decision that nothing holds". This is the case WAY-134's *violates*
    names: "the cycle fills a decision's rejected options with ways it derives";
  - "the link of an invariant to its decision left to the skill that writes the invariant, with no
    check — a sentence an author can read past leaves the gap unseen until a reviewer finds it" —
    the task's *Context* keeps it ("AIR-718, sprawdzone i odrzucone: sam punkt 2, bez kontroli w
    skrypcie — sam tekst reguły już nie zadziałał"), but not row 2's *Source*, and its reason here is
    the writer's rewording of a reason that tells how the decision was reached.
  Row 1's *Source* is "pytanie 1 (*Not chosen* tam)". WAY-30's *Rejected* gains both of its ways;
  the second, "the approval left to the merge with no sentence saying so — cycles then stop or
  settle each in their own way", is Question 1's "zgoda przy scaleniu bez zmiany tekstu", a way
  that differs from the chosen one only in whether the answer is written into WAY-30 — as I read
  WAY-134, a way of how an answer is recorded, which stays out.
- Why it matters: WAY-134's rationale: "A rejected option the writer of an entry derives reads as
  one the human weighed, and an agent that proposes it later has to say what has changed for a way
  nobody turned down." The human merging does not read *Rejected*, so the derived option binds
  unseen; the request lists these entries as `row 1` and `row 2`, which tells the human there is
  nothing of the writer's to check in them.
- Evidence: the lines quoted above; the task's *Questions to settle* 1 and 2 and *Context*
  (`.runs/task-cycles/ai-review-fixes-from-24-11/task.md:50-60`, `:84`); WAY-134 at
  `foundations/decisions.md` (search `### WAY-134`), binding paragraph 2 and its *violates*.
- The fix: drop "an error for every such invariant …" and the skill-only option from WAY-12's
  *Rejected* (or carry the latter only if the orchestrator holds *Context* to be part of row 2's
  source, and then with the task's own reason); drop, or keep with the reason I read wrong named in
  the request, WAY-30's "the approval left to the merge with no sentence saying so …".

Contradiction: yes — WAY-134 (second paragraph: rejected options of a decision written from a row
only from the row's source; a way of how an answer is recorded stays out).

### Minor

**M-1. An invariant of the earlier form with a version in its heading is reported by the new check
beside the earlier-form error, though the docstring leaves such an entry to the reports above.**
Within the task (item 3).

- Place: `elements/common/foundation_check.py:824` skips only an entry whose fields are of the
  earlier form (`EARLIER & set(found)`), while `check_fields` (`:663`) also treats a heading with
  `/` as the earlier form; the docstring (`:100-102`) and the method's docstring say "an entry of the
  earlier form [is] left to the reports above".
- Evidence: the probe above, case `## save-keeps-name/2`: the earlier-form error and a `listed:`
  line for `save-keeps-name`. The listed line stops nothing and the earlier-form error already
  blocks, so the cost is a second, misleading line until the foundation is migrated; the fix is to
  skip the versioned heading as `invariant_entries` does (`"/" in heading`).

**M-2. WAY-30's new sentence "the agent making it asks that human no question" can be read as
forbidding any question by that agent, not only one about the line.** Within the task (row 1).

- Place: `foundations/decisions.md:1304-1307`.
- Row 1 says the line "nie wymaga zgody przed kodem"; the entry turns that into a prohibition
  without an object. An author that adds such a line and has an unrelated question for the human
  (no recommendation, WAY-114) reads a sentence that forbids it. "asks that human no question about
  it" keeps the meaning of the row. Minor: the surrounding paragraph makes the narrow reading the
  likely one.

## Judgments the dispatch asked for

1. **WAY-30's pair of examples, and the *Rationale* and *Rejected* of WAY-12 and WAY-30.** The pair
   (one *complies*, two *violates*, `foundations/decisions.md:1316-1326`) stays within the rules:
   WAY-12 allows a pair "only for the part of its sentences that no invariant and no test checks",
   and no test holds the new WAY-30 paragraph; WAY-114 and `task-cycle/skill/foundation_step.md:31-36`
   provide for a pair the writer adds — the entry becomes `the cycle's` and the request quotes the
   pair word for word under it. The author's report marks it so; the orchestrator must carry that
   into the request. The *violates* examples describe changes against the paragraph while WAY-30
   stays as it is, as WAY-12 requires. The *Rationale* additions of both decisions carry the meaning
   of the rows' sources (Question 1's and 2's answers and *Need*) and name no file, script or count
   (WAY-05); no finding. The *Rejected* additions: I-2.
2. **Root `README.md`, `elements/decisions/template.md`, `elements/invariants/template.md`.** The two
   templates and `agent-instructions/README.md` are named in the task's *Context* (line 88) as the
   places that describe what `foundation_check.py` reports; their "who reads it" rows are the
   readers WAY-05 keeps a field by, so the edit is a required correction, not a widening. The root
   `README.md` (`:83-95`) is not named, binds nothing (the part map leaves it out on purpose), and
   describes the same reports; the edit keeps it true and adds no meaning — within the change's
   reach, no finding.
3. **The rule of the check against item 3 and Questions 1-4; the fifteen links.** Item 3: error
   when the change adds or alters either whole entry, otherwise a `listed:` line; message gives the
   identifier, the decision and "after `invariants:`"; docstring bullet; tests of both cases — all
   present, apart from I-1. Two readings of the author's that the task does not settle and I accept:
   a change of spacing alone is no alteration (the convention of `check_held` and WAY-05's check);
   a file the base lacks counts as unchanged (the script's existing convention for an unknown base,
   announced by its own listed line). Question 1 → WAY-30 paragraph (I-2, M-2 aside, faithful);
   Question 2 → whole entry (met, I-1 aside); Question 3 → item 5, word for word; Question 4 →
   `task-cycle/skill/request_template.md:51-54`, after "(*Description*).", wording unchanged. Item 2
   (`elements/invariants/skill/write.md:5-7`) and item 5
   (`elements/invariants/skill/decide_entry.md:19-21`) are word for word. Item 4: each of the seven
   invariants' *Derives from* reads `WAY-48 · WAY-235`, and `installation-paths-through-links` also
   `WAY-368`; WAY-48 and WAY-235 now name the seven, WAY-368 names the one — fifteen, no more. The
   head's script run on the base lists exactly these fifteen and no other gap; on the head it lists
   none (acceptance criterion met).

## Declined to judge

- A product's first `foundations/invariants.md`, added by the change while the base lacks the file:
  its gaps are listed, not errors, because a file the base lacks counts as an unknown base — the
  script's convention before this change, which `check_held` shares; changing it is outside the task.
- Whether "no cost to the product known" (WAY-134) applies to a way of the-way's own whose only cost
  is a stop of a cycle (WAY-30's first new *Rejected* option): in the-way the process is the
  product, and the task gives no reading; not raised as a finding.
- The two gaps of the other product's log (D-13, D-22) — the task's *Out of scope*.

## Checks run

- `git rev-parse HEAD`, `git log --oneline 07aa55df..2dca6873`, `git diff --stat` and `git diff`
  of the range — exit 0; head matches the dispatch.
- `python -B elements/common/foundation_check.py` in the reviewed worktree — `0 errors`, no
  `listed:` line, exit 0.
- `python -B ../head/elements/common/foundation_check.py .` in a worktree of the base — 15 `listed:`
  lines (7 for WAY-48, 7 for WAY-235, 1 for WAY-368), `0 errors`, exit 0.
- `python -B instruction-files/check_instructions.py` in the reviewed worktree — `0 error, 0 warn,
  5 info`, exit 0 (no warning, no finding).
- `python -B task-cycle/change_file_sizes.py 07aa55df565d5f10428176c89d20d2c6420a6dfd 2dca6873` in
  the reviewed worktree — exit 0; `foundation_check.py` 1115 → 1193 lines (threshold 1200),
  `check_linked` 55 lines (threshold 110).
- `python -B -m unittest agent-instructions/test_size_invariant.py` in a worktree of the base and
  one of the head — `Ran 4 tests … OK`, exit 0 on both: nothing pushed over a threshold.
- `python -B gate/run_tests.py elements/common` in the head worktree — `Ran 314 tests … OK`, exit 0.
- `python -B gate/run_tests.py agent-instructions` in the head worktree — `Ran 53 tests … OK`,
  exit 0.
- `python -B gate/run_tests.py task-cycle` in the head worktree — `Ran 570 tests … OK (skipped=2)`,
  exit 0.
- `the pinned Ruff of the main checkout's quality virtual environment format --check --config ruff.toml
  elements/common` — `13 files already formatted`, exit 0; `… ruff.exe check --config ruff.toml
  --ignore-noqa elements/common` — `All checks passed!`, exit 0 (the pinned Ruff of the main
  checkout, the head worktree has none).
- Probe of the new check (I-1, M-1): `PYTHONIOENCODING=utf-8 python -B probe_linked.py <head
  worktree root>` from `.runs/review-whole-2/`, exit 0; the three printed cases are kept in
  `reports/review-whole-2-probe-linked-output.txt`, the probe in `reports/review-whole-2-probe-linked.py`.
- Searches: "level 1 verification" (case-insensitive) across the repository outside `.runs/` — none
  (positive control: the search for "Step 4.4" in `elements/invariants/` finds `write.md:5`); "WAY-30"
  across the repository, to find texts the new paragraph touches — `task-cycle/skill/foundation_step.md:36-43`
  reads consistently with it.
- The full gate was not run (the cycle's own run).

Changed invariant tests: none. The change adds tests only, to `elements/common/test_foundation_check.py`,
carrying lines `decision: WAY-12`.

## Reach beyond the dispatch

- WAY-134 whole (`foundations/decisions.md`, `### WAY-134`) and `elements/decisions/template.md:80-117`:
  the rules of *Rejected* for a decision written from a row, for the dispatch's point 1 (I-2).
- WAY-29 whole: what an agent may write of a human's decision's rationale, for point 1.
- `task-cycle/skill/foundation_step.md` whole: how a writer's pair of examples and the marks of an
  entry reach the request, for point 1.
- `elements/common/foundation_text.py` (`blocks`, `fields`, `located`): what an entry's text and a
  field's lines are, for the code of `check_linked`.
- `elements/common/test_foundation_check.py:1-280`: the fixtures and helpers the probe reuses.

## Working copies

- `.runs/review-whole-2/head` (worktree of
  `2dca6873`) and `…/.runs/review-whole-2/base` (worktree of `07aa55df`): removed with
  `git worktree remove --force` (exit 0 each), then `git worktree prune` (exit 0); `git worktree
  list` no longer shows them.
- `.runs/review-whole-2/` (the index of the
  selection, the probe, the test outputs): removed (exit 0). The probe and its output are kept in
  `reports/` as named above. No remainder.

## Unread material

13 decisions of the index of my selection read whole: WAY-05, WAY-07, WAY-12, WAY-14, WAY-17,
WAY-18, WAY-29, WAY-30, WAY-48, WAY-114, WAY-134, WAY-235, WAY-368. The index
(`decision_index.py` with the sections "Decision entries and the decision log", "Accepting and
applying decisions", "Invariants", "The request and the human", the parts decisions, invariants,
elements-common, task-cycle, agent-instructions, and the decisions of *Decisions in play* with
WAY-05, WAY-14, WAY-33) was read whole: 39 in full, 138 by heading. Decisions bearing on the change
read through the index's binding sentences only, not whole: WAY-33, WAY-150, WAY-263, WAY-385,
WAY-02, WAY-22, WAY-344, WAY-379, WAY-382, WAY-386, WAY-394 — none of them is changed or gone
against by the change. Guideline files: `guidelines/coding.md`, `guidelines/coding-check.md` and
`guidelines/testing.md` read whole. The part map read whole. Of the invariants whose *Part* names a
touched part or `every`, read whole: `own-foundation-check-report`, `foundation-change-merge-route`,
`skill-rule-source`, `test-method-citation` and the seven of item 4 by their *Derives from*; the
others (size, formatter, linter, imports and such, each held by a test of the gate) were not read
whole, their tests run as listed above. Glossary: `binding part`, `binding sentence`, `entry` read;
the other entries not.

## Searches not found or unclear

- WAY-134's "a way of the process rather than of the product" and "only a cost of the process": in
  the-way the process is the product, and no entry says how the distinction reads in the-way's own
  log (I-2's WAY-30 part and the second line of *Declined to judge*).
- Whether the task's *Context* line "AIR-718, sprawdzone i odrzucone: sam punkt 2, bez kontroli w
  skrypcie" counts as part of row 2's source for WAY-134: the row's *Source* names only Question 2.
