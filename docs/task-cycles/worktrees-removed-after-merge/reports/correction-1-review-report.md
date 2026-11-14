PASS e802ec4668f7cb29d4f3f019265289afac5a3209

# Review of correction 1 (`review-change`, review of a correction)

Range `8c601d14eab5b08996744650c2a0431356ed298b..e802ec4`: one commit (`Say in WAY-375 that the script needs no act of a human and the first clearing is one`), one file, `foundations/decisions.md`, 3 lines added and 1 removed. `git rev-parse HEAD` = `e802ec4668f7cb29d4f3f019265289afac5a3209`, as given. Counts: blocking 0, Minor 2, out of scope 0.

## Each remark

- Item 3 (correct in this request): made. The last sentence of the second paragraph of WAY-375 (`foundations/decisions.md:12967-12970`) read "...so it needs no human action." and now reads "...no effect outside the repository in the sense of WAY-140, so the script that a cycle runs needs no act of a human; the first clearing of the directories that gathered before the script, which a task document places as a human action, is the human's act." It is the remark's own proposed shape ("skrypt uruchamiany przez cykl nie potrzebuje ruchu człowieka; jednorazowe pierwsze sprzątnięcie zaległości nim jest"). It does nothing else: the diff is those three lines; `git diff 8c601d1..HEAD --stat -- foundations/glossary.md` is empty and no other file changed (`git diff 8c601d1..HEAD -- . ':!foundations/decisions.md'` has 0 lines), so the glossary, WAY-140 and every other entry are untouched.
- Items 1 and 2: not for correction, as the remarks say; nothing was made for them.

## Does the corrected sentence agree with the rest of WAY-375, the task and WAY-140

- The conditions, *Verification*, *Rationale* and *Rejected* of WAY-375 still agree. The pair's *complies* (cycle goes on without a word to the human where the script removed a directory beside the repository's own) and *violates* (the cycle asks the human before such a removal) speak of the cycle's run, which the new first clause also says needs no act of a human; the *Rationale* ("asking the human for each directory would leave the directories where they are", the removal is state of the repository and no effect in the sense of WAY-140) says the same. Neither speaks of the first clearing, so neither contradicts the new clause.
- True to the task. Row 5 and the Answer to "Czy automat może usuwać katalogi leżące poza katalogiem repozytorium": the script removes only what git names, which is repository state and not an effect in the sense of WAY-140. Kept in the same sentence. *Human actions*: the one-time clearing is the human's act, in the cycle, run with the branch's script as a dry run and then `--apply`; the new clause says it is the human's act and that a task document places it as a human action. True of this task document (`task.md`, *Human actions*).
- True to WAY-140 (`foundations/decisions.md:4137-4175`): WAY-140 reserves for a human an effect on a server, DNS, keys or an external account and the human actions a task document names; the sentence keeps the first (not an effect of the script) and the second (the clearing the document names).
- The phrase "human action" elsewhere in the range: `git diff 835344f..HEAD` added lines matching "human action", "human's act", "act of a human" or "no human": one, this sentence. The files of the change (`SKILL.md`, `record_template.md`, `request_template.md`, the script's docstring) do not use the phrase in the changed lines. Nothing reads otherwise than the glossary.
- `python -B elements/common/foundation_check.py`: exit 0, `0 errors`.

## Findings

### Critical

none

### Important

none

### Minor

1. `foundations/decisions.md:12967-12970` (WAY-375, second paragraph, last sentence) — the sentence says the removal of a checkout git names, also one beside the repository's own directory, is "no effect outside the repository", and in the same sentence that the first clearing of the same kind of directories is "a human action", which the glossary (`foundations/glossary.md:81`) defines as "an act outside the product's repository". A reader meets the same removal as outside and not outside the repository. The two words differ (an effect in the sense of WAY-140 against an act that the glossary places outside), and the task document holds the same pairing (the Answer on row 5 against *Human actions*: "dotyczy katalogów poza repozytorium"), so the sentence is no worse than its source; the human's own remark asked for this shape. A reader still has to be told why the first clearing is the human's: the task's reason is that more than a hundred directories would go at once, with no sight of the list and no undo. Suggested repair, if the request takes it: add to the *Rationale* one sentence on that reason. Grade Minor: no sentence of the files is read wrongly by a reader who takes the two terms as the entry and WAY-140 define them.
2. `foundations/decisions.md:12968-12970` — "the first clearing of the directories that gathered before the script" is a single past event inside a standing decision; once the human has made it, the clause describes nothing that still holds, and a later reader will not know whether it is still owed. The vault's rule for knowledge artifacts (`.ai/rules/knowledge_artifacts.md`) keeps the way to a state out of an artifact. Grade Minor: it misleads no one now and the request's *Human actions* holds the same fact while the task is open. Repair: when the foundation is next reviewed, state the durable property instead (a run of the script that would remove directories gathered without it is first made by a human, as a dry run, with the list in front of them) or drop the clause with the task.

## Declined to judge

- The glossary's entry `human action` itself, whether it should carry the sense "an act outside the repository that a task places": the remarks say the glossary is not changed.
- Item 2 of the remarks (the unstable test of the number of directories at once): the remarks hand it to an open task.

## Checks (command, exit code)

| Command | Exit | Result |
|---|---|---|
| `git rev-parse HEAD` | 0 | `e802ec4668f7cb29d4f3f019265289afac5a3209` |
| `git diff 8c601d1..HEAD --stat` and `-- foundations/glossary.md` | 0 | one file, `foundations/decisions.md`; glossary untouched |
| `git diff 835344f..HEAD` searched for "human action", "human's act", "act of a human", "no human" in added lines | 0 | one hit, the corrected sentence |
| `python -B elements/common/foundation_check.py` | 0 | `0 errors` |

Not run: any test (no code or test changed), the full gate, any `--apply`.

## Reaches beyond the dispatch

- `foundations/glossary.md:75-83` (the entry `human action`), `foundations/decisions.md:4137-4175` (WAY-140): named by the handoff, read to compare.
- `a file of the author's private notes`: for Minor 2.

## Working copies

None made; `.runs/review-return/` was not created. Remainder: none.

## Unread material

none: the handoff, the remarks, the author's report, the task's *Human actions*, *Answer* of the row-5 question and WAY-375 (whole) read; WAY-140 read through its statement, *Verification* and the start of its *Rationale*.

## Searches not found or unclear

none
