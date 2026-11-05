# Designer report — pr-description-schema

Status: done
Spec: `docs/task-cycles/pr-description-schema/spec.md`

## Questions sent and their answers

None. Every choice of the handoff was settled from the task, the foundation, the code or by the
smallest reversible reading, each recorded in the spec with its rejected ways and cost. Three of
them the orchestrator may want to look at, since each resolves something the sources leave open:

- **Full text versus meanings of WAY-114, WAY-134 and WAY-10.** The handoff asks for "the full new
  text … their *Verification* and *Rejected* included". `task-cycle/spec/design.md` says a spec holds
  "no text a file will hold" and that "the foundation step or the return step words" the entries.
  WAY-114 also keeps an entry's wording the agent's.
  - What the spec gives: each binding sentence's meaning sentence by sentence, the replaced clause
    quoted where a clause changes in place, the complies and violates examples by content, and the
    *Rejected* options with their costs from the row's source.
  - Cost if the orchestrator wanted final text: the foundation step words them from these meanings,
    which it does anyway.
- **Where the block stands.** The task's "górna część stoi pod nim drugi raz" literally reads "under
  the description". The spec places the block directly after the top part, before the lower part.
  This follows the transcript's summary (MSG 22, item 6 of the top) and the human's reading habit.
  - Cost if wrong: moving one element and the script's slot.
- **An English task document.** The task says the block always repeats the top part in the task's
  language. The spec has the block read `none` when the task document is English, so that it does
  not hold an English copy of English text. This keeps To do 6 (the section stays, with `none`).

## Ways weighed

- **Template place.**
  - Chosen: `task-cycle/skill/request_template.md`, beside the skill, per WAY-256.
  - Rejected: `task-cycle/request_template.md` beside the record template, which matches an older
    file but goes against WAY-256's "beside the skill".
  - Rejected: inline in `SKILL.md`, which carries text only some steps consult through all of them.
- **Record section.**
  - Chosen: keep `## Request handoff` with URL, *Description* (new), backlog writes and *Process
    remarks on the-way* unchanged. The digest and the test fixtures need nothing.
  - Rejected: a heading of its own for the remarks, which buys nothing.
  - Rejected: keeping the copied fields, which makes two copies of one content.
- **Language measure.**
  - Chosen: (d), the English function-word share only. The description is English by rule, so
    English is the one language the script must know, and (d) catches the observed failures.
  - Rejected: (a), word lists per language, which fails other languages.
  - Rejected: (b), trigram profiles, which need tuning and are blurred by the English quotes in task
    documents.
  - Rejected: (c), a declared tag, which checks nothing.
- **Headings source for the script.**
  - Chosen: constants plus a test of agreement with the template's skeleton.
  - Rejected: reading the template at runtime, which makes a prose file a runtime format.
- **"Beyond the task" selection.**
  - Chosen: the orchestrator selects rows when it writes the request, by the criterion of D5.
  - Rejected: a new column in the questions table, which is more reliable but collides with the
    collective task's change of that section and with step 5.
- **Entries.**
  - Chosen: five new decisions (rows 1, 2, 3, 5, 6) and three changes in place (row 4).
  - Rejected: merging rows 1 and 2, which goes past three binding sentences.
  - Rejected: row 5 as a fourth sentence of WAY-161, which is past the limit, and a new rule beside
    a decision is a new question (WAY-19).
- **Step 12 order.**
  - Chosen: the stages run before the request opens, so *Cost* is real when the checked description
    opens it. The record's SHA link is added after the record pair, with a second check before the
    edit.
  - Rejected: the record pair before opening, as blocked requests do. It would drop the request URL
    from the committed record, which `plan_state.py` reads (`record_pointers`).
  - Rejected: opening with a provisional description. That breaks "before the request opens" of
    To do 9.

## The four checks

1. Placeholder, `TBD` or empty section: none. `<ready|draft|blocked>` and `<…>` are the settled
   forms, named as such.
2. Contradictions: none found.
   - The tie of a row to an entry already stated stands both in *Foundation entries* and in *For you
     to decide*. This is consistent with WAY-134's "naming both in the request", which stays.
   - Row 5 and WAY-161: the judgment adds a restatement and moves no finding. D5 and the row-5 entry
     say so.
3. Scope: one change. The script depends on the template's skeleton, and the entries describe the
   same shape. It spans three kinds of work, which a planner may cut into slices:
   - the template and the pointers in `task-cycle/` and `agent-instructions/`;
   - the script and its tests;
   - the foundation entries and the search of D9.
4. Two readings, each settled in the spec:
   - the block's place: after the top part (D1);
   - the block for an English task: it reads `none`.

## Reaches beyond the handoff

- `task-cycle/spec/review.md` and `task-cycle/skill/spec_review.md`: to see what the reviewer
  checks, so that the spec meets it.
- `foundations/decisions.md`: WAY-01 to WAY-07 headings only; WAY-19 via the decisions template;
  WAY-113, WAY-125, WAY-126, WAY-135 and WAY-150 whole or in part. They are needed for whether
  rows are new questions, for the projected-part case of WAY-114, and for the question rule.
- `foundations/invariants.md`: `foundation-change-merge-route`, `repository-file-location`,
  `return-step-record`, `script-language`, `script-imports` and `script-subprocesses`. These are
  constraints on the new script.
- `elements/decisions/template.md:20-170`: the binding-sentence limit, the *Rejected* rule for
  rows, and changing in place.
- `project-level/task/template.md:1-40`: where the task document's human-language text stands, for
  the language measure.
- `project-level/plan_state.py:15-160` and
  `project-level/test_plan_state_subprocesses_invariant.py:90-130`: how the record's request link
  is found, and the second fixture holding `## Request handoff`.
- `task-cycle/slice_size.py` and `task-cycle/test_slice_size.py` (heads), and `gate/run_tests.py`
  (discovery lines): house style and how the gate finds the tests.
- `elements/common/way_of_working.md:125-140`: it restates WAY-114's acceptance at the merge, and
  changes with row 4.
- A search of the whole tree outside `.runs/` for request-content wording (listed in D2), and of
  `foundations/decisions.md` for every entry mentioning the request (D9).
- `gh pr view 66` and `gh pr view 55 --repo mariusznazar/loop2`: read as the handoff names.
- The refinement transcript, read through a dump of its text messages. The dump is at
  `C:\Users\Mariusz\AppData\Local\Temp\claude\6b84451ec494cdda\7a4fe94e-3148-4011-bad6-7d83342c594a\scratchpad\transcript.txt`.
  Messages read: MSG 5–25 and 31–57, holding the #55 draft, the #66 rewrite, the language ways and
  the control questions. Nothing from it is copied as template wording.
- `git fetch -q origin` in the worktree, to see whether `foundations` had moved. It changed refs
  only, no tracked file. `origin/foundations` is still `f45ca40`.

## Searches not found or unclear

- `gh pr view 69` and `gh pr view 70 --repo mariusznazar/the-way` and `gh pr view 52 --repo
  mariusznazar/loop2` were not read. #69's own sections and #52's first sentence are quoted in the
  transcript (MSG 5, 18), which sufficed. #70 was not seen in any form.
- The transcript's text has no English heading proposal for the template. Its headings are Polish
  ("Do Twojej decyzji", "Co zobaczysz po wdrożeniu"), so the English headings are the spec's own.
- How a request is "marked `blocked`" today is not settled anywhere in `task-cycle/` (title, label
  or body). The spec makes the first line's `**State: blocked**` that mark. It does not say whether
  a host label is also set.
- `foundations/decisions.md` WAY-134 *Relations* reads `narrows WAY-114`. It is unclear what it
  narrows once WAY-114 states the row case itself. This is left to the search (D9).
- The task's "pod nim" (To do 4) can be read as under the description or under the top part.
  Settled in D1.
- `task-cycle/spec/design.md` ("no text a file will hold") and the handoff's "full new text" of
  WAY-114, WAY-134 and WAY-10 conflict. Resolved as above.
- No decision or file says why step 12 opens the request before committing the record. The reason
  inferred is that the committed record must hold the request URL for `plan_state.py`.
