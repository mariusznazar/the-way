# Report — the fix of the whole review's findings

**Status:** `done`

## Files and commits

| File | Added | Removed | Commit |
|---|---|---|---|
| `project-level/technology/task_run.md` | 8 | 5 | `58c0b7f` docs: list a new note at a task document that already has a technology list |
| `task-cycle/change/SKILL.md` | 10 | 11 | `d83067c` docs: point a stage agent to the reserved rule before it decides to stop |
| `task-cycle/change/fix.md` | 7 | 1 | `d83067c` |
| `foundations/decisions.md` | 32 | 29 | `9849f4b` docs: keep WAY-267 to what the files of the return do |

Range `e21d286..9849f4b`, on `task/unsettled-technology-returns`. Not pushed. The lines counted in
`foundations/decisions.md` are the edited sentences of WAY-267 and the reflow of the paragraphs they
stand in; no other entry changes.

## Each blocking finding

### 1. A second run's note lost at a document with a section *Technology* — fixed

`task_run.md`, *Start*: a new bullet stands before the bullets on a list. Where the section holds a
list and the run has a note the section does not yet hold, the run writes the note and follows *List*
for it first, whatever the items already there end with, and only then the rest applies. "Has a note"
covers both a note given and a choice taken as the note by a run refinement starts. The next bullet
gains "unless *List* has just shown it", so that the human is not asked the same list twice.

Check, the finding's example followed through the changed text (hand trace; see *Tests* below):

1. The section reads `— settled: ...`.
2. The cycle meets an error tracker and opens a blocked draft, which the human closes.
3. `draft.md:15-18` makes the named choice the note, and `resolve_gaps.md:29-30` runs the step.
4. `task_run.md` *Start*: the section holds a list and the note is not in it, so the new bullet
   fires. The note is written, *List* adds the item `— open`, shows the list, and the document reads
   `Status: waiting for human`.
5. The next bullet reads the notes and items, finds no question for the new item, does not show the
   list again and resumes "Settle the open choices" with that item.
6. "Where the list holds no open item" does not fire. *Close* comes only after the item ends
   `— settled: <question>`, and `final_review.md:7-8` sees no `— open` because the choice was settled.

The milder form in the finding, an open item already standing, takes the same bullet: the note's
choice stands beside it. A run with no new note, or resuming after the note is written, does not
fire the bullet and resumes as before.

### 2. The pointer fired only after the agent had decided to stop, and its *Also* — fixed

`task-cycle/change/SKILL.md` section 5 now opens with the paragraph on its own, "Where the work needs
a language, a framework, ...", before the two cases, in the form of `task-cycle/plan/SKILL.md:63` and
`task-cycle/spec/design.md:18`. It names the case the finding describes: "also where the need looks
like a choice of how to make the change. A reserved choice is no such choice". What it reports and
what it leaves for the cycle to reset are unchanged in substance.

*Also:* `task-cycle/change/fix.md` gains a section *A finding of a reserved choice*: the fix removes
the choice from the change, and an agent that cannot returns the status `reserved`, as section 5
gives. The table in section 1 of `SKILL.md` names this in the row of a fix. The file's first line
says so too.

Check, by reading the three pointers side by side and a search for the old gate:
`Before you return \`returned\`` no longer stands under `task-cycle/`, `project-level/` or
`foundations/`. Two traces:

- An executor about to add a new store of data, taking it for a choice of how to make the change,
  meets the opening of section 5 with no intent to return: the sentence fires on "needs ... a store
  of data", it reads the rule, and the rule's examples stop it.
- A fix's agent given a finding of a reserved choice reads `fix.md` by the table's row, and meets
  the sentence there without having read `reserved_return.md`.

### 3. WAY-267 said more than the files do — fixed

Through `the-way-record-decision`; the only file changed is `foundations/decisions.md`, and the only
entry WAY-267.

| Clause | Was | Now |
|---|---|---|
| name, binding | "under the same name and on a new branch", every task | "on a new branch and, for a task of a project plan, under the same name" |
| what the request says, binding | "says that nothing else ran and why" | "says what did not run and why" |
| the pair, binding (the finding's lesser clause) | "holding only the commit that adds its record and the commit that removes it" | "holding, above its base or the commit that moved the pin, only the commit ..." |
| *Verification*, complies | names the spec, the plan, the reviews, the return step, the reconciliation and the gate as not run | names as not run, with why, the gate and each of those stages that did not run |
| *Verification*, complies | "the new cycle keeps the task's name on a new branch" | "starts on a new branch, a task of a project plan keeping its name" |
| *Verification*, violates | "reuses the earlier branch or numbers its name" | reusing the branch, and, apart, "the new cycle of a task of a project plan numbers its name" |
| *Rationale* | "The new cycle keeps the name because a plan's task and its record meet through it" | "A plan's task keeps its name in the new cycle because the task and its record meet through it" |
| *Rejected* | "a numbered name for the new cycle" | "a numbered name for the new cycle of a plan's task" |

Check: an independent task's new cycle following step 5 (`task-cycle/skill/SKILL.md:121-122`) now
breaches no line of the entry; a stop after a reviewed spec or a slice, with the request naming only
the stages that did not run, as `reserved_return.md:73-74` gives, complies; `foundation_check.py`
exits 0.

Meaning for the request, in the task document's language (replaces the sentence in
`reports/foundation.md:23`): Gałąź trzyma ponad bazą albo commitem przesuwającym przypięcie tylko parę
commitów zapisu cyklu, zablokowany szkic nazywa wybór i mówi, czego nie uruchomiono i dlaczego; po
zamknięciu przez człowieka zadanie wraca do doprecyzowania, nowy cykl idzie na nowej gałęzi, a zadanie
z planu projektu zachowuje nazwę, zaś orkiestrator projektu, na słowo człowieka, usuwa po nazwie ślad
tego jednego cyklu i cofa wiersz planu.

The search of the whole foundation (WAY-33), for the wording the entry changes: "same name",
"nothing else ran", "numbered name", "keeps the name", and "WAY-267" and "reserved choice" for the
entries that name it. Only WAY-135 (`foundations/decisions.md:3286-3288`), WAY-266 (`:7650`) and the
glossary's *reserved choice* touch it; each read, none restates a changed clause, and neither
*derives from* WAY-267, so none follows. No entry's binding part outside WAY-267 changes.

## Checks

Each run on head `9849f4b`, with no pipe, its exit code read from the shell.

| Command | Exit code |
|---|---|
| `python -B elements/common/foundation_check.py .` | 0 (`0 errors`) |
| `python -B instruction-files/check_instructions.py . --file project-level/technology/task_run.md --file task-cycle/change/SKILL.md --file task-cycle/change/fix.md` | 0 (0 errors, 2 warnings) |
| `python -B gate/run_tests.py task-cycle` | 0 (42 tests, `OK`) |
| `python -B gate/run_tests.py project-level` | 0 (268 tests, `OK`) |

The two warnings are `dead-path`: `AGENTS.md:21` `_zadania\`, a private folder, and
`task-cycle/change/SKILL.md:102` `.the-way/project-level/technology/reserved_choices.md`, a path that
exists only in a product. That second path stood in the same words before this fix, at the old
paragraph; it appears here because this run names the file with `--file`.

Not run: the gate, the orchestrator's by the handoff; the full suite, the cycle's by section 3 of the
method. Earlier runs on the uncommitted fix exited 0 for `foundation_check`, `check_instructions`,
`task-cycle` and `project-level`; `decisions.md` was reflowed after or during them, a change of line
breaks only, which is why each ran again on the commits and only those runs count here. The
`check_instructions` run on the commits also names the two other changed instruction files.

## Tests

No test was written first: all three changes are text that instructs agents, or a foundation entry.
The method tests such text by what an agent does with it, and it forbids dispatching a subagent, so
the evidence is the hand traces above, not an agent's run. No test named the behaviour, and no
invariant test changed.

## Own-work check

- **Requirement most likely not met:** To do 8, for the case the finding did not trace: a run whose
  note names a choice the section already lists, or that is interrupted after the note is written.
- **Check:** trace of `task_run.md` *Start* for each.
- **What it showed:** an interrupted run holds as far as the text goes: `list.md` writes the list
  before it asks, so, read that way, the note and its item land together and the resume finds the
  item `— open`; the text does not say "in one write" outright. A note whose choice already stands
  `— open` adds its note and no second item, the template giving one item per choice. A note that
  names a choice already `— settled` is not reopened by the text: *List* gives no step for it, and
  the human would change it through the list. The task does not ask for this case, so nothing is
  changed; see *Problems observed*.

## Reaches beyond the dispatch

- WAY-266 and WAY-135 in `foundations/decisions.md`, and the entry *reserved choice* in
  `foundations/glossary.md`: the search WAY-33 requires of a changed entry.
- `task-cycle/skill/SKILL.md:105-134`: to read step 5, which finding 3 cites.
- `elements/decisions/` (skill, `read.md`, `decide_entry.md`, `template.md`, `examples.md`),
  `elements/common/way_of_working.md` and `elements/common/rules.md`: named by
  `the-way-record-decision`. WAY-03, the form's example `examples.md` names, was not opened: the edit
  keeps the entry's fields and form, and `foundation_check.py` passes.
- `project-level/technology/start.md`, `list.md`, `SKILL.md`, `project-level/task/skill/draft.md`,
  `resolve_gaps.md`, `final_review.md`: to follow finding 1's trace.
- `reports/foundation.md:23`: to find the sentence of meaning the change replaces.

## Searches not found or unclear

- Whether the finding's lesser clause was to be fixed was unclear: its *Fix* line does not list it,
  while its *What is wrong* does. See *Choices*.

## Choices

| Choice | Way rejected | Cost if wrong |
|---|---|---|
| Fixed finding 3's lesser clause, on the pin, in the same sentence | Leaving it: the handoff bounds the edit to what the finding names, and the finding names it, so leaving it would keep a known overstatement in a sentence already being edited | One clause of the entry to take back |
| Edited *Rationale* and *Rejected* of WAY-267 as well, though the finding's *Fix* names only the binding sentence and *Verification* | Leaving them: the template has both describe the decision as it stands, and "a numbered name ... breaks WAY-147" would have read as a ban on an independent task, the clause the finding removes | Two phrases to take back |
| "unless *List* has just shown it" in the bullet that shows the list | Leaving that bullet as it was: the human would be asked about the same list twice in one run | One clause to take back |
| Three commits, one for each finding | One commit: the review of the fix reads each finding on its own | None |

## Problems observed

- `foundations/decisions.md:7706`, "ends with its attempt discarded", is not true of a choice the
  orchestrator finds at step 4, for which `reserved_return.md:38-40` gives "leaves nothing to
  discard". No finding names it, so it is not changed; it is the same kind of overstatement as
  finding 3's and may be worth the orchestrator's look.
- Spec decision 2 itself reads "that nothing else ran and why", and the spec's table of entries
  reads "the next cycle keeps the name" and "that nothing ran beyond it". The spec is frozen and was
  not changed; the entry now follows the spec's decision 5 and the file `reserved_return.md`, as the
  finding asks, not those short wordings.
- A note naming a choice that already stands `— settled` has no written way in `task_run.md`; the
  task's To do does not ask for one.
