# Author report — decisions-list-in-refinement

**Status:** done

## Commits and files

One commit on `task/decisions-list-in-refinement`, base `9cbc6b2`: `51f2590` "Add the step that lists the decisions a task document leaves to the executor to the refinement of a task".

| File | Added / removed |
|---|---|
| `project-level/task/skill/final_review.md` | +39 / -0 (new paragraph and five numbered steps before "When the draft is complete, show it whole.") |
| `project-level/task/skill/orchestrated_mode.md` | +10 / -0 (one new bullet after the bullet on `find-foundation-entries`) |
| `project-level/task/skill/SKILL.md` | +3 / -1 (section "## 6. Review and hand off", one sentence) |
| `foundations/decisions.md` | +103 / -0 (WAY-377 and WAY-378, at the end of the section "Task refinement and readiness") |

To do 1-8 are all made. Settlements rows 1 and 2 are each written as a decision.

## Foundation entries (foundation step)

| Entry | Marked | Meaning in English | Meaning in Polish |
|---|---|---|---|
| WAY-377 — Does the refinement of a task list the decisions its document leaves to the executor before the human sees the document, and who lists them? | `row 1` | Before the complete document is shown, two fresh agents of one cheaper class (named in general terms) list the decisions it leaves to the executor and settle the guesses against the repository, where the task has decisions in play or changes a skill or an instruction file. | Przed pokazaniem kompletnego dokumentu dwaj świeży agenci jednej, tańszej klasy (nazwanej ogólnie) wypisują decyzje, które dokument zostawia wykonawcy, i sprawdzają zgadnięcia w repozytorium — gdy zadanie ma decyzje w grze albo zmienia skill lub plik instrukcji. |
| WAY-378 — What does the human see after the decisions a task document leaves to the executor are listed and criticised? | `row 2` | The human sees only the open matters and the gaps of the document, at most about four, each with ways, cost and a recommendation; the full list and critique stay in a file, and the refining agent checks the critique's quotations, those behind the guesses kept from the human included, and gives each such matter one verdict (as of fix 1, commit b084a4a). | Człowiek widzi tylko sprawy otwarte i luki dokumentu, najwyżej około czterech, każdą z drogami, kosztem i rekomendacją; pełna lista i krytyka zostają w pliku, a agent doprecyzowania sprawdza cytaty krytyki, także te za zgadnięciami zatrzymanymi przed człowiekiem, i daje każdej takiej sprawie jeden werdykt (stan po poprawce 1, commit b084a4a). |

Form: WAY-377 `derives from WAY-100`, WAY-378 `derives from WAY-377`; *Scope* `project-level`; *Based on* `none`; *Verification* a pair of examples (no test holds a sentence of either; WAY-374, the neighbour, is held by none either, so I wrote no test); *Rejected* holds only the ways the rows' sources keep (questions 1, 2 and 3 of the task, *Not chosen*). WAY-33 search of the foundation: found WAY-374 (bounds, reused by name), WAY-120, WAY-113, WAY-229 (does not cover refinement agents, no collision, no `narrows`), WAY-154 (the orchestrator's dispatch is in the skill text, not in the decisions), WAY-100 (the adoption). No glossary term added: WAY-374's reading applies, no word of the new text takes a meaning a reader of the field would not give it.

## Checks (command, exit code)

- `python -B elements/common/foundation_check.py` — 0 errors, exit 0 (run before and after the commit).
- `python -B gate/run_tests.py project-level` — 278 tests OK, exit 0.
- `python -B gate/run_tests.py elements/common` — 242 tests OK, exit 0.
- `python -B gate/run_tests.py agent-instructions` — 27 tests OK, exit 0 (holds the skill-entry-point tests).
- `python -B gate/run_tests.py instruction-files` — 104 tests OK (5 skipped, POSIX-only link tests), exit 0.
- `python -B instruction-files/check_instructions.py .` — 0 error, 0 warn, exit 0.
- `python -B elements/common/decision_index.py --output … --decision WAY-377 --decision WAY-378` — exit 0, both entries listed in full (the index parses them).
- Grep of the added lines for absolute paths, `[[` and POSIX drive forms (WAY-309) — no hit.
- Not run: the whole gate (forbidden by the handoff); `skill_entry_points.py --write` (no skill added, renamed or moved, no description changed; its tests in `agent-instructions` pass); tests of `task-cycle/` (no file there changed).
- No failing-first run: no invariant's test was written or changed, and no test of behaviour exists for prose.

## Own-work check

Requirement most likely not met: To do 5 and the orchestrator's note, "who writes what file in `.runs/` of the product", and To do 7, "start no agent; the orchestrator runs both steps". I read the new text against the task item by item: `final_review.md` names the file `.runs/decisions-list/<task-name>.md` with the three parts *List*, *Critique*, *Verdicts*, says no agent of the step writes it, and that the refining agent writes what each returns (manual refinement); `orchestrated_mode.md` says the project orchestrator writes *List* and *Critique* from its two agents' returns and the refining agent writes *Verdicts* in the resumed turn. It showed: every To do 1-8 has its sentence; no step contradicts the other file; the condition appears the same in the three skill files and in WAY-377. This was a reading check, not a run.

## Choices (with the way rejected and the cost if wrong)

1. **Two decisions, not one.** The two rows answer questions that change independently (when and by whom; what the human sees), so WAY-19 gives two. Rejected: one decision with two paragraphs. Cost if wrong: a merge of the two in a later change.
2. **Who writes the file.** The refining agent (manual) or the project orchestrator (orchestrated) writes *List* and *Critique*; the refining agent writes *Verdicts*; the step's agents write nothing. Rejected: each agent writes its own part — `elements/common/critique/SKILL.md` says the critic writes no files, and one writer per part keeps the orchestrated mode's rule that only the refiner writes the task's files. Cost if wrong: copying the agents' returns into the file costs a few tokens more.
3. **Where the step stands in `final_review.md`.** A new opening paragraph, the paragraph "When the draft is complete, show it whole." left unchanged after it. Rejected: editing that paragraph. Cost if wrong: the two paragraphs both begin "When the draft is complete".
4. **A guess the critique finds "most likely wrong" is a gap of the document and is shown** (step 4 of the new text). The task says "only the open matters and the gaps of the document" and does not say what happens to a wrong guess; I read it as a gap, since an executor would guess it wrong. Rejected: leaving it out of the human's sight. Cost if wrong: one more matter shown, within the limit of about four.
5. **A quotation that does not hold voids the critique's verdict on that matter**; the refining agent settles it from the file or counts it open (the task says the agent checks quotations and gives a verdict, not what a failed check does). Rejected: showing the matter as the critique judged it.
6. **File name `.runs/decisions-list/<task-name>.md`.** The task fixes only "a file in the ignored `.runs/` of the product". Same naming habit as `.runs/technology/<choice>.md` and `.runs/project-refinement/<task-name>.md`.
7. **Orchestrated mode takes two turns** (request, then the resumed turn with checks and verdicts); `questions` carries the request, as the technology run's bullet gives.
8. **No test.** Prose for agents; no test holds a sentence of WAY-374 and the method asks for none (handoff note).

## Reaches beyond the dispatch

- `elements/decisions/skill/read.md`, `decide_entry.md`, `elements/decisions/template.md`, `elements/common/rules.md`, `elements/common/way_of_working.md`, `elements/decisions/examples.md` — the foundation step sends to them through the skill of decisions.
- `instruction-files/SKILL.md`, `kind_skill.md`, `placing.md` — the handoff names them.
- `elements/common/critique/SKILL.md` (only its head, not `prepare.md`, `check.md`, `settle_review.md`) — to see whether the critic writes files.
- `project-level/lead/skill/SKILL.md` (step 3, lines 90-140), `project-level/lead/conversation_template.md` (lines 95-120), `project-level/lead/answering.md` (lines 34-53), `project-level/task/template.md` (*Decisions in play*, lines 76-96 and 188-200), `project-level/task/skill/resolve_gaps.md` — to see how the orchestrator takes a *Child-work request* and how WAY-374 is worded in the skill. Why: the orchestrated bullet had to match what the orchestrator does.
- the user's rules for writing knowledge artefacts and for committing — the user's rules for writing artefacts and committing.
- A search of every local branch for `### WAY-377` to `### WAY-379` — none; the numbers 377 and 378 are free on every local ref (a parallel branch not yet fetched could still take them).

## Unread material

- WAY-113, WAY-134, WAY-124, WAY-154: read by their binding sentences in the index and the passages the task quotes; not whole, because the change goes against none of them and their sentences leave open nothing I had to do. WAY-120, WAY-100, WAY-229 and WAY-374: read whole.
- `foundations/part_map.md` entries of `project-level` and `decisions`: not read; the parts follow from the file paths and WAY-374's own *Scope* (`project-level`).
- The invariants whose *Part* is `project-level`, `decisions` or `every`: read as the grep output of their headings and sentences (the `foundations/invariants.md` entries listed above), not each linked entry; none constrains the change beyond the form checks that ran.
- `instruction-files/changing.md`, `writing.md`, `judging.md` and `tool_loading.md`: not read; the handoff sent me to `placing.md` and `kind_skill.md`, and the placement was fixed by the task.

## Searches not found or unclear

- WAY-100 asks that a decision which adopts an outside practice put in *Rejected* what it leaves out of the practice. The task's rows and *Not chosen* keep no such way, and the notes of the course are not open to me, so WAY-377's *Rationale* states what is taken (the list and the mark) and what is the-way's own, and its *Rejected* holds only the three ways the task keeps. Unclear whether this satisfies WAY-100 in the human's eyes.
- The project orchestrator's own files (`project-level/lead/…`) say nothing of this request type; its step 3.1 says it performs "all child dispatches their borrowed workflows request" and the conversation template's *Child-work requests* line says "needed critique or other delegated work and full paths of material", which covers it in general terms. I changed no lead file (outside the task's *To do*).
- Test holding WAY-374's sentences: none found (`decision: WAY-374` appears in no file).

## Working copies

One directory, `.runs/author/`, made for a check of the index script's output; removed before this report (`.runs/` now holds only `orchestrator/` and `task-cycles/`). The commit holds no file of `.runs/`.

## Problems observed

- `decision_index.py --decision 377` fails with "no decision 377"; the switch takes `WAY-377`. Observed, not a defect of this change; the handoff's wording of the switch in `way_of_working.md` ("`--decision NUMBER`") reads as the bare number.
