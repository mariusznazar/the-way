# Correction report: the human's remarks on the request

**Status:** done. One commit, `047a9e7`, on top of `7ca8642`. Tree clean. `docs/task-cycles/` untouched.

Direction followed: `reports/correction-handoff-2.md`, which replaces item 1 of
`reports/correction-handoff.md`. An earlier uncommitted draft that wrote the agreement rule into
`task_line.md`, WAY-154 and WAY-329 was dropped before the commit; none of it is in the commit.

## Remarks, one by one

- **Item 1 (the rule of agreement of lines at both ends of a dependency), made as the second
  handoff says.** The rule is in no skill and no decision. `project-level/task_line.md`, "The
  dependencies", carries the one sentence: the refiner keeps the task's line, and the lines of the
  tasks it waits on and that wait on it, in agreement with the plan's dependencies as the rules of
  the task place give; where those rules do not say how, it asks the human once. The opening
  paragraph of the file lists, as the rules' own matter, how a line is found, which fields may change
  and what to do where an identifier is already carried.
- **What left the-way (removed, not moved to another repository file):**
  1. How a line is found and that a task gets no second one: the search bullet of "Make the line".
  2. The clash step (the bullet of "Make the line", the clash sentence of "The identifier") and
     WAY-329's clause and *Verification* example on it. **This also settles Minor 1 of item 3**
     ("another line" without "of another task"): the clause is gone, so there is nothing to word.
  3. How an existing line is changed and the check before a write: "touches nothing else of the
     line" and the read-before-write sentence of "The dependencies".
  4. The agreement rule itself, as above.
- **What stays in the-way:** the turn in which a refiner makes a line, in parallel with no queue, and
  the late line (`task_line.md` "Make the line", **When**; the only place of the moment in the
  skills); that a refiner never moves a line to ready and the orchestrator does it with `Status:` and
  the plan's row, making a line already ready where none stands ("Move to ready"); the dependencies
  from the plan's `Depends on` column; the derivation of the identifier and its two conditions
  (`task_line.md` "The identifier"; WAY-329).
- **WAY-107 (`foundations/decisions.md`)**: gains the third binding sentence — how a task's line is
  handled (status of a new line, move to ready, form of dependencies and identifier, how a line is
  found and kept one to a task, which fields may change, the agreement of the lines at both ends of a
  dependency, a clash of identifiers) is taken from the rules of the task place itself, never from
  text of the product or of the-way's skills. *Verification*, *Rationale* (the place can change the
  rules without a change of the-way) adjusted. WAY-107 now has three binding sentences.
- **WAY-154**: back to three binding sentences, with what the committed text held about the line (made
  in the first turn that creates the document or the first later turn that can; the orchestrator
  moves it to ready, already ready where none stands; dependencies in step when the plan's
  dependencies change). It names nothing of the agreement rule. Its *Verification* and *Rejected*
  hold no addition of the first, dropped draft.
- **WAY-329**: keeps the derivation and its two conditions; loses the clash clause, its example and
  its *Violates* item; the sentence "writes it in the dependency of another task's line before that
  task's line exists" is as committed.
- **Item 3, finding 1** — see item 1 above (settled by removal).
- **Item 3, finding 2 (the citation)** — made: `(WAY-329)` now follows the derivation sentence in
  `task_line.md` "The identifier", and the sentence on a task of no plan has none.
- **Item 3, finding 3 (long lines)** — made. Width used: **100 columns**, the width of the
  neighbouring lines of the file (wrapped with `textwrap`, `width=100`, no breaking of hyphenated
  words). Rewrapped whole paragraphs: WAY-154 binding sentences, *Verification*, *Rationale*,
  *Rejected*; the whole of WAY-329; WAY-107's binding paragraph, *Verification*, *Rationale*,
  *Rejected*; WAY-320's binding paragraph and the run of its *Rejected* from "careful review; one
  entry for the rules of the task place" to "the script harder to read,"; WAY-27's binding paragraph.
  No line of the diff against `52f8164` is now longer than 100 characters (character count, checked
  with a one-off `python -I` run over `git diff 52f8164`; first checked with `awk` by bytes, which
  counts a dash as three and gave false hits). Rewrapping whole paragraphs also moved some old words
  to other lines of those paragraphs, so the diff shows them.
- **Item 3, finding 4 (binding sentences)** — made: WAY-154 and WAY-107 are three sentences each.
  Nothing that bound is dropped; WAY-154's second sentence is long, joined by semicolons.
- **Item 3, finding 5 (vocabulary, `read_sources.md`)** — made: "short task entries only ... link it
  from that entry" is now "lines ... that line". The long wrapped line of WAY-107 is rewrapped (above).
- Pointers brought into line with the one sentence: `project-level/task/skill/orchestrated_mode.md`,
  `project-level/lead/conversation_template.md`, `project-level/lead/skill/SKILL.md` and
  `project-level/plan/skill/delegated_mode.md` say the refiner makes its task's line and brings the
  lines of tied tasks into agreement "as `project-level/task_line.md` gives" (the delegated-mode line:
  "the backlog lines of their tasks and of the tasks tied to them").

## Return step again (compared with the files)

Read whole: `task-cycle/skill/return_step.md`, `task-cycle/skill/foundation_step.md` (read earlier in
this session and read again in the first part of this correction; the text did not change).

- **WAY-154**: compared with `task_line.md` ("Make the line", "The dependencies", "Move to ready"),
  `orchestrated_mode.md`, `conversation_template.md`, `lead/skill/SKILL.md`: match. None to correct.
- **WAY-329**: compared with `task_line.md` "The identifier" (derivation, two conditions): match.
  The example in the skill and the examples in the entry agree. None.
- **WAY-107**: compared with `project-level/backlog_place.md`, `AGENTS.md` (`## Backlog`), `task_line.md`
  opening paragraph: match; `backlog_place.md` and `AGENTS.md` were not changed (they name the entry
  `task-rules` and add no form). None.
- **WAY-320, WAY-27**: only rewrapped; their meaning matches `AGENTS.md` and `backlog_place.md`.
  None.
- **Part map**: `project-level` still says it answers for how a task's line is made, given its
  dependencies and moved to ready; `decisions`, `agent-instructions`, `product-guidelines` — no
  change of responsibility. None.
- **WAY-144, WAY-147, WAY-328** (compare only): unchanged and still consistent.
- Foundation step marks of entries written or changed: WAY-154 `row 1`, `row 2`, `row 5`; WAY-107
  `row 3`, `row 4`, and **`the cycle's`** for the added rule on how a line is handled (the human's
  remark at the request, not a row of the task: "no row carries it whole" is the step's
  description of `the cycle's`, and the request puts it before the human); WAY-329 `the cycle's`;
  WAY-320 `row 4`; WAY-27 `the cycle's`. WAY-107's *Rejected* gains nothing: the remark keeps no way
  not chosen, and the step forbids a way the writer derives.
- **EN / PL meaning of the one entry the correction adds meaning to (WAY-107's added rule):**
  - EN: How a task's line is handled — finding it, one to a task, which fields may change, the
    agreement of lines at both ends of a dependency, a clash of identifiers — comes from the rules of
    the task place, never from text of the product or of the-way's skills.
  - PL: Sposób obchodzenia się z linią zadania — znalezienie jej, jedna linia na zadanie, które
    pola wolno zmienić, zgodność linii na obu końcach zależności, zderzenie identyfikatorów — bierze
    się z zasad miejsca zadań, nie z treści przy produkcie ani ze skilli the way.
- No invariant, environment fact, glossary term or part-map change written.

## Checks (command, exit code)

All from the worktree root, run on the tree that was committed.

- `python -B elements/common/foundation_check.py` — exit 0, "0 errors".
- `python -B instruction-files/check_instructions.py .` — exit 0, "0 error, 0 warn, 3 info".
- `python -B task-cycle/test_tracked_files_private_paths.py` — exit 0, "OK".
- Not run, as the handoff says: the `project-level` directory and the full gate.

## Own-work check

- Requirement most likely unmet: that no tracked file of the-way holds a rule of handling a line that
  the rules of the task place now hold (finding, one line to a task, which fields to change, read
  before writing, agreement of lines, clash of identifiers).
- Check: `grep -rniE "no second|second line|read each line|read .* before (it is )?writ|only a
  field|field (it|that) (is )?missing|touches nothing|another line|already carr|carrying the
  identifier|names the task|kept one to a task|nothing else of the line|agreement" project-level
  product-guidelines AGENTS.md foundations/decisions.md foundations/part_map.md --include=*.md`, exit 0.
  Read every hit: none states a rule of handling a line. The hits that touch the subject are pointers
  or lists of the rules' topics (`task_line.md:7`, `:9`, `:50`; `conversation_template.md:23`;
  `lead/skill/SKILL.md:105`; `orchestrated_mode.md:42`; `decisions.md:2445`), and the others are
  unrelated uses of "agreement", "second" and "carries". No rule found.
- Check that the one-place sentence of "Make the line" is still the only place of the moment of
  making a line: `grep -rn "first creat" project-level product-guidelines foundations --include=*.md`,
  exit 0: two lines, `project-level/task_line.md:17` (the skill rule) and `foundations/decisions.md:4446`
  (WAY-154's binding sentence, which states the same rule as the decision). No other skill file holds
  the moment.
- Not checked by a test: no test reaches these files; the checks are reading and `grep`.

## Unread material

none beyond what the earlier reports name. I read both handoffs, `correction-findings.md`,
`return_step.md`, `foundation_step.md`, and every file I changed. I did not read the reviewers'
reports (the findings file carried them in their words).

## Searches not found or unclear

- What "mark it as that step's mark for a change the human's remark makes" means (handoff 2): the
  foundation step has three marks, `row n`, `projected`, `the cycle's`. I took the last for the added
  rule in WAY-107 and named the human's remark as its source in this report; the entry itself holds no
  history of how it was reached (the decision template forbids it in *Rationale*). If another mark
  was meant, say so.
- Whether the agreement sentence's "asks the human once" in `task_line.md` should stay where the rules
  of the task place do hold the agreement rule: unclear; I followed the handoff, which asks for it.

## Reach beyond the handoff

- `project-level/plan/skill/delegated_mode.md` and `project-level/lead/conversation_template.md` /
  `lead/skill/SKILL.md` / `task/skill/orchestrated_mode.md` pointers reworded (they named only the
  refiner's own line; the one sentence now has the refiner touch the lines of tied tasks).
- `foundations/decisions.md` WAY-27 and WAY-320: rewrapped only.
