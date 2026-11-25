# Findings of the second review of the whole change — for the fix

Review: `reports/review-whole-2-report.md`, `FAIL 2dca687367fb016839219488d08511ddf83e8e11`, range `07aa55df..2dca6873`. Two blocking findings (both marked `Contradiction: yes`) and two Minor findings within the task, copied in the reviewer's words. The probe behind I-1 and M-1: `reports/review-whole-2-probe-linked.py` and `reports/review-whole-2-probe-linked-output.txt`.

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
