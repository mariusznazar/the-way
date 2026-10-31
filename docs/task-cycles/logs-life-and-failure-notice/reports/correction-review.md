FAIL 94d20f3

# Review of the correction — logs-life-and-failure-notice

Range `5eb89cf..94d20f3`, one commit. `git rev-parse HEAD` is the head given. `5eb89cf` holds the tree of
`63fa039`: `git rev-parse` gives the same tree for both. The remark in place of a findings file is the
human's decision in `reports/correction-handoff.md`. No file the part map names as a trust boundary
changes, no invariant test changes, and no operation cannot be undone.

Counts: 1 blocking, 2 Minor, 0 out-of-scope.

## The remark: made

The human's decision: a decision silent on part of a matter opens at a task only on the human's word, as a
decision that answers the matter does, and WAY-267 stays as it is.

- `project-level/technology/task_run.md:50-57` now says so: such a decision "holds the choice too", and "the
  item opens only on the human's word and then stands `— open`, with that decision nested under it".
- The diff touches no file of `foundations/`, so WAY-267 stands word for word.

## N1: gone

The condition is now the human's word, no longer that the note touches the matter. An agent's run on a
reserved choice opens nothing by itself: "A note that refinement derived from a reserved choice is not that
word". The sentence no longer qualifies "An agent never opens one" and now extends it.

## Finding 4 of the first review: stays fixed

Read as a run at a task, on the human's word: the exception fires, the decision is nested, `settle.md`
sub-step 1 and `research.md` step 1 give it, and *Write* says which decision the choice changes, since this
is now a choice the human opened, which closes the seam N1 named at `task_run.md`, *Write*. A human's note, and
the human's yes at `resolve_gaps.md:65-66`, both reach this path; `resolve_gaps.md` needed no change.
`list.md:23-26` with `task_run.md:52-57` read together do not contradict one another as text of the step's
files. The new-list path at a definition is untouched.

## Important (blocking)

### C1. The correction keeps an item `— held by` on a silent decision, which WAY-165 names as a violation with no limit to a definition

- **Place:** `project-level/technology/task_run.md:52-57` ("the list shown to the human keeps the item
  `— held by`") against `foundations/decisions.md:4480-4481` and `:4459-4461`.
- **What is wrong:** WAY-165, an entry this change writes, says with no qualification that an entry leaving
  part of a matter unanswered "does not settle that matter", and gives as a violation "a logs item stays
  `— held by` or `— projected` on a decision silent on the record's life". The new text has a run at a task
  do exactly that, and says the silent decision "holds the choice too". `— held by` means settles, by both
  marker tables: "a decision of the product's foundation settles the choice"
  (`project-level/definition_template.md:204`, `project-level/task/template.md:148`). The file and the entry
  therefore say opposite things of the same item at a task.
- **Why it matters:** WAY-263 grades this Important: the change's files do what the entry forbids. The
  human's decision is right and the file carries it; the entry is what no longer agrees. An agent or a
  reviewer who compares a run at a task with WAY-165 finds the run's correct behaviour listed as a violation,
  and it meets two rules, WAY-165 and WAY-267, with no precedence between them, which WAY-25 says no agent
  settles. The author's report says WAY-165 says "nothing of opening a decision at a task beyond what the file
  now says"; the violating example and the binding clause do, since neither is limited. The handoff asked for
  this check: "WAY-165, WAY-270 and WAY-139, where one of them states or implies what you correct, say the same
  as the file; change one only where it departs."
- **Evidence:** the passages above. `foundation_check` cannot see it, and no test pins this text.
- **Fix in one line:** limit WAY-165's own clause and its violating example to a list of a project definition,
  or say in the clause that at a run at a task such a decision opens only on the human's word (WAY-267); then
  WAY-267 stays as it is, no `narrows` is needed, and WAY-165's meaning sentence for the request changes.

## Minor

1. `project-level/technology/task_run.md:55-57` and `list.md:31`: a human who is to give the word is not told
   there is anything to give it on. For a note refinement derived, the list shows `— held by: <X>`, and
   `list.md` asks for one sentence on why the project needs the item; nothing has the run say what `<X>` leaves
   unsaid, as `start.md` has a definition say. The handoff's "the list shows the human the silent decision" and
   the correction report's "the human sees the decision silent" hold only of the marker, which reads as settled.
   The default is the safe one, nothing opens and the deployment check still asks at a task that deploys, so I
   grade it Minor. The same case meets `reserved_choices.md`, where a choice no decision settles is reserved: with
   a silent decision, the run can close with the item held while WAY-165 says the choice is unsettled, and C1's
   fix does not remove that. One clause, saying what the decision leaves unsaid when the list is shown, closes both.
2. `project-level/technology/task_run.md:53-54`: "whatever `list.md` says of the matter it settles" calls the
   matter one the silent decision settles, the reverse of `list.md`'s sentence. "whatever `list.md` says" reads
   clean.

## Declined to judge

- `list.md`'s line break after "A decision of the foundation" keeps a short line the change left: form, already
  named in the first review's Minor 6.

## Checks

- `python -B elements/common/foundation_check.py .`: exit 0, "0 errors".
- `python -B agent-instructions/skill_entry_points.py`: exit 0, "entry points are current".
- `python -B gate/run_tests.py project-level`: exit 0, 268 tests OK.
- `git diff --check 5eb89cf..94d20f3`: exit 0.
- `git rev-parse 63fa039^{tree} 5eb89cf^{tree}`: the same tree.
- Manual: read the three cases of a run at a task on the new head (the human's note, a note refinement
  derived, the human's yes at a deployment task), and the entries WAY-165, WAY-267, WAY-270 and WAY-139 against
  them. WAY-139 and WAY-270 do not depart: neither speaks of a marker at a task. Only WAY-165 does.
- Not run: the full gate, the cycle's own; an agent following the texts, which no test exercises.

## Reaches beyond the dispatch

`foundations/decisions.md`, WAY-165, WAY-267, WAY-268, WAY-263, WAY-25; `project-level/definition_template.md` and
`project-level/task/template.md`, the marker tables; `project-level/technology/reserved_choices.md`, "The rule";
`project-level/task/skill/resolve_gaps.md`: all to judge the correction against what it meets, as the handoff's
"What to check" names most of them.

## Searches not found or unclear

- Not found: any sentence that has a run at a task say what a held decision leaves unsaid (Minor 1).
- Unclear: whether a reserved choice with a silent decision, the human leaving the list unchanged, ends settled or
  not. The correction report names the case as outside the finding; `reserved_choices.md` and WAY-268 make it
  "not ready until the human has settled it", and `task_run.md` *Close* asks only that no item ends `— open`.
