FAIL e8b76178

# Review of the whole change — decision-length-check

Range `1b6fe1c1..e8b76178`, four commits (`0f738707`, `58f9937d`, `9dc811af`, `e8b76178`);
`git rev-parse HEAD` gave `e8b7617893c512fa20850545d65a766d9c5df679`. One author, no plan and no
slices, so no finding names a slice. One blocking finding, four Minor findings within the task, one
Minor finding outside the task's scope.

The check itself does what the task asks. Every point of *To do*, both rows of *Settlements to
record*, the five changes of WAY-05 in *Decisions in play* and *Out of scope* are met by the
commits, and no rejected variant is restored. The one thing that blocks is how two summaries of the
new report word it.

## Findings

### Important

**1. Two summaries of the new report restate the second paragraph of WAY-05 differently.**
Slice: none.

- `README.md:86-88` reads: "It reports as an error each decision that a change adds or whose
  binding sentences it alters and that nothing holds, and each paragraph of such a decision's
  binding sentences over three sentences or 300 words". "Such a decision" points back to the whole
  description before it, "that a change adds or whose binding sentences it alters and that nothing
  holds". Read that way, the sentence says a paragraph over a limit is an error only in a decision
  that nothing holds, and the next clause, "the other decisions with a paragraph over those
  limits", then puts an added decision that is held among the listed ones. At best the sentence
  can be read both ways.
- The same sentence, and `agent-instructions/README.md:14-17` ("the paragraphs of binding sentences
  over three sentences or 300 words in a decision a change adds or whose binding sentences it
  alters"), leave out that a different division into paragraphs counts as an alteration. In both
  files the phrase "whose binding sentences it alters" also stands for the check of what holds a
  decision, where a different division does not count, so a reader takes one meaning for both.

What WAY-05 says, as the change writes it (`foundations/decisions.md:697-700`): "in a decision that
a change adds or whose binding sentences it alters, a different division of them into paragraphs
included". What the code does: a held decision over a limit is an error
(`test_a_new_decision_with_four_sentences_in_a_paragraph_is_an_error` uses an entry held by an
invariant; my probe P3 added a fourth sentence to WAY-05, which a pair and tests hold, and got exit
1), and a new division alone is an error (`test_a_different_division_into_paragraphs_counts_as_a_change`;
my probe P6 joined the two paragraphs of WAY-18 with no word changed and got exit 1).

Why it matters: both files are changed by this change and repeat an entry the change writes, one
with a qualification the entry does not have and both without one it has. By WAY-263 that is
Important. The answer "a different division counts" is also one the human gave to a question of
its own in the task. The cost of the fix is one sentence in each file.

Contradiction: yes — WAY-05, second paragraph (row 2 of *Settlements to record*, and the answer
under "Czy inny podział zdań wiążących na akapity…").

### Minor, within the task

**2. The row "binding sentences" of the template's table narrows what the script counts.**
`elements/decisions/template.md:121` says `foundation_check.py` "counts the sentences and the words
of each of their paragraphs in a decision a change adds or alters (WAY-05)". The script counts them
in every decision and lists the others, and the row does not name the division. I grade it Minor
and not as finding 1 because the full account, with the list and the division, stands in the same
file fifteen lines below (`template.md:136-141`), so a reader of the template is not led wrong.

**3. One replacement in a new test changes nothing.**
`elements/common/test_foundation_check.py:2191`, in
`test_a_decision_over_a_limit_whose_spacing_alone_changed_is_listed`:
`long.replace(" ", "  ", 2).replace("e. ", "e.\n")`. The paragraph is
`word well-known, end. word well-known, end. …`; it holds no `e. ` (the sentences end in `d. `), so
the second `replace` matches nothing and the test checks two doubled spaces only, never a line
break. Checked by running the two expressions: equal strings, no line break, zero occurrences. The
test still passes for the right reason, and the shared normalisation of a line break is held by the
older `test_decision_with_only_its_spacing_changed_is_listed`; the line reads as if it tested more
than it does. `"d. "` in place of `"e. "` makes it do what it says.

**4. The move changed how one pattern is written.**
`elements/common/foundation_text.py:17` writes `QUOTED` with the three typographic quotation marks
as characters, where the base wrote them as escapes
(`r"\"[^\"]*\"|[\u201c\u201e][^\u201d]*\u201d"`, `foundation_check.py:169` at `1b6fe1c1`). The
pattern matches the same text: I read the code points of the new pattern as U+201C, U+201E, U+201D,
U+201D, and the older test of the three kinds of marks passes. But the commit message of `0f738707`
and the author's report say the patterns "move unchanged", and it is the one line of the move that
did not (a sorted comparison of the lines removed with the lines of the new module shows no other
difference). The opening and closing marks are hard to tell apart on a screen, which the escapes
avoided.

**5. The part map names one module of the script and the change adds a second.**
`foundations/part_map.md:67-70` says the part `elements-common` answers for "the script that checks
a whole foundation's identifiers, references and assignment of files to parts, … with the module
that reads the files and git for it". After the change the script also has
`elements/common/foundation_text.py`. The sentence is still true and the file is claimed by
`elements/common/**`, so nothing breaks; the return step of an earlier cycle (`4066ae5d`) added the
first module to this sentence, and the return step of this cycle is the place to add the second.

### Minor, outside the task's scope

**6. The guidelines of the kind `shared-module` do not name `elements-common`.**
`guidelines/coding-shared-module.md:4` gives *Applies to* as `relation-model · process-audit ·
task-cycle`, and its *Where in code* (lines 40-42) the same three directories. `elements/common/`
held a shared module before this change (`foundation_source.py`) and holds two after it. By
`product-guidelines/reading.md` an agent is given a guideline file whose *Applies to* names a part
its work touches, so an agent changing these modules is not given the file of their kind. The gap
stood at the base; the change adds one more file to it. The author did read the file, on the
handoff's word, and the new module keeps its one rule: its top level only imports, sets
`sys.dont_write_bytecode`, and defines three patterns and seven functions.

## What I judged and found sound

- **The move into `foundation_text.py`.** `foundation_check.py` stood at 1141 lines against the 1200
  of WAY-385 and stands at 1111 after the change; the addition without the move would have crossed
  the threshold. The move is the first commit that changes code, as WAY-365 asks of a change that
  adds to a file over the threshold, and apart from finding 4 the moved lines are the same. Every
  moved name that another file imports from `foundation_check` is still imported there and used
  there (`decision_index.py:46`, `elements/part-map/test_cross_part_imports.py:66`), the same way
  `foundation_source.py` was split out in `ac3c96f4`. The focused runs of `elements/common`,
  `elements/part-map` and `agent-instructions` pass, the test of allowed imports among them.
- **The three texts left unchanged.** `product-guidelines/styleguide/template.md:168`,
  `product-guidelines/testing/template.md:196` and `foundations/decisions.md:10303` say a decision
  holds one to three binding sentences, each to explain why something is split over several
  decisions or kept out of one. The limit of 300 words does not make any of them false and does not
  change their point. I agree with the author: none needs a change.
  `product-guidelines/coding/template.md:184` ("at most three binding sentences") is of the same
  kind.
- **Other places that describe what the check reports.** I searched every Markdown file for
  `foundation_check`, `listed:`, `nothing holds` and the wording of the limits. Beside the four
  places the task names, no file gives the list of what the script reports about a decision's
  binding sentences: `installation/README.md` (lines 61, 79, 167, 266), `elements/common/rules.md:31`,
  `elements/common/way_of_working.md:95` and `:186`, `task-cycle/skill/request_template.md:322-329`,
  `task-cycle/plan/SKILL.md:181`, `task-cycle/skill/SKILL.md:769` and the tables of readers of the
  other four elements each speak of another report. None needs the new one.
- **WAY-05 against the task.** The first sentence carries the limit of 300 words; the second
  paragraph carries the error and the list in one sentence; *Verification* opens with `tests:` and
  the pair that was "For the binding sentences" keeps only whether a part of another question has
  its own paragraph; *Rejected* holds the six ways not chosen under the three questions, each with
  the reason the task keeps, and "a higher fixed limit" now says "of sentences". The script counts
  WAY-05 itself within both limits (it is altered by this change and gives no error). The entry
  names no date or condition of the trial the human spoke of, which is what WAY-24 asks.
- **The *Rejected* of WAY-05 against its source.** The author left out the counts the task quotes
  (30 and 45 paragraphs, 478 words in WAY-134) and wrote the reasons without them. WAY-05 itself
  keeps counts of entries out of prose, and the reason of each way is kept, so I raise nothing.
- **The tests.** Twelve tests, eleven with a line `decision:` that quotes the start of a sentence
  of WAY-05 as it stands; the script accepts each. The twelfth, on an unknown base, takes its value
  from the description at the head of the script, as WAY-394 allows. I ran twelve mutations of the new code in a copy
  of the head and each was caught (below). I found no branch, value or comparison in the script
  made for an input of a test.
- **The author's own-work check and walk.** The requirement it names, an altered decision being an
  error on the real foundation while the others stay listed, is where a check tested only on small
  products would be weakest, and its check would catch it unmet; I repeated it another way (probes
  P1 to P6). Its judgment that the change alters nothing a user sees in a running product agrees
  with the change.
- **Sizes.** `foundation_check.py` 1141 to 1111 lines, `foundation_text.py` new with 112,
  `test_foundation_check.py` 2294 to 2452 (a test file, outside the rule). The test of the invariant
  `function-and-file-size` names nothing at the base and nothing at the head. The new functions are
  `excess` (11 lines) and `check_length` (25 lines). No code is left without a user and no name
  stopped being true: `base_sentences` still gives the joined text that the check of WAY-12 uses.
- **Reserved choices.** The change brings no language, library, store of data, way of logging in or
  place to run: the new module imports `re` and `sys` only.
- **No invariant test is changed**, and no invariant, part-map entry or glossary entry is changed.

## Declined to judge

- The twelve entries of the-way that stand over a limit today (WAY-134, 136, 139, 148, 150, 154,
  256, 287, 289, 339, 344, 405): the task puts their shortening in a task of its own.
- The entries of loop2 over a limit: outside this repository and outside the task.
- Whether three sentences, 300 words and an error rather than a list are the right limits: the
  human settled each under *Questions to settle*.
- That `guidelines/coding-shared-module.md` lists only its exemplar under "Files of this kind"
  while other shared modules stand unlisted: it stood so at the base and the task does not touch it.
- That two templates of product guidelines say "a decision holds one to three binding sentences"
  where WAY-05 gives that number for each paragraph: unchanged files, the same at the base.

## Checks I ran

All from the root of the reviewed worktree unless a directory is named.

| Check | Command | Exit code | Result |
|---|---|---|---|
| The check of the foundation | `python -B elements/common/foundation_check.py` | 0 | `0 errors`, twelve `listed:` lines, for the twelve entries and with the figures the task gives (WAY-344: 8 sentences, 743 words; WAY-405: 5 and 343; WAY-256: 301 words) |
| Tests of `elements/common` | `python -B gate/run_tests.py elements/common` | 0 | 283 tests, OK |
| Tests of `elements/part-map` | `python -B gate/run_tests.py elements/part-map` | 0 | 40 tests, OK |
| Tests of `agent-instructions` | `python -B gate/run_tests.py agent-instructions` | 0 | 52 tests, OK, none skipped (linter, formatter, size) |
| Tests of `installation` | `python -B gate/run_tests.py installation` | 0 | 73 tests, OK |
| Tests of `product-guidelines` | `python -B gate/run_tests.py product-guidelines` | 0 | 14 tests, OK |
| Sizes of the changed files | `python -B task-cycle/change_file_sizes.py 1b6fe1c1 e8b76178` | 0 | the figures under "Sizes" above |
| Size invariant at the base | in a worktree of `1b6fe1c1`, from `agent-instructions/`: `python -B -m unittest test_size_invariant` | 0 | 4 tests, OK |
| Size invariant at the head | the same in a worktree of `e8b76178` | 0 | 4 tests, OK |
| Whitespace errors of the range | `git diff --check 1b6fe1c1..e8b76178` | 0 | none |

Manual checks, each in a worktree of the head under `.runs/review-whole/`, never in the reviewed
worktree:

- **Twelve mutations of `foundation_check.py`**, each run against the new tests
  (`python -B -m unittest test_foundation_check -k …` from `elements/common/`), each ending with
  exit code 1: `>=` for `>` (3 tests fail); the joined text compared in place of the list of
  paragraphs (1); every full stop and space counted as the end of a sentence (1); an unknown base
  counted as a change (1); only the first paragraph counted (1); always an error (4); never an error
  (7); words counted as runs of letters (3); a limit of 4 sentences (9); a limit of 301 words (1);
  the check not called (10); the error placed at no line (3).
- **Probes on the real foundation**, each an edit of `foundations/decisions.md` in the copy, then
  the script; output kept in `reports/review-whole-probes.txt`:
  - P0, nothing changed: exit 0, twelve listed lines.
  - P1, the paragraph of WAY-344 cut in two with no word changed: exit 1, an error for its
    paragraph 2 (7 sentences, 658 words), eleven listed lines left.
  - P2, the rationale of WAY-405 alone changed: exit 0, WAY-405 still listed.
  - P3, a fourth sentence added to WAY-05: exit 1, "4 sentences (at most 3)".
  - P4 and P4b, a sentence added to WAY-12 with three full stops inside `“…”` and inside `„…”`:
    exit 1 with 4 sentences, not 7, so a full stop inside either pair ends no sentence.
  - P5, one space of WAY-256 doubled: exit 0, still listed.
  - P6, the two paragraphs of WAY-18 joined with no word changed: exit 1, 5 sentences.
- **The move**: the lines `0f738707` removes from `foundation_check.py` compared, sorted, with the
  lines of `foundation_text.py` at that commit: the only moved line that differs is `QUOTED`
  (finding 4).

Not run: the product's full gate (`python -B gate/run_tests.py` with no directory), which is the
orchestrator's or CI's (WAY-160).

## Reaches beyond my selection

- `foundations/decisions.md`, WAY-263 whole (the grade of finding 1) and WAY-365 in part (whether
  the move had to be the first commit of code): neither is in the index of my selection.
- `git show` of `ac3c96f4` and `4066ae5d`: how the first module was split out of the script and
  where the part map came to name it, for the judgment of the move and for finding 5.
- `installation/README.md` lines 58-82, 163-170 and 262-268, `elements/common/rules.md` lines 25-36,
  `task-cycle/skill/request_template.md` lines 300-344, `task-cycle/plan/SKILL.md` lines 176-184,
  `task-cycle/skill/SKILL.md` lines 764-774: the search for another place that describes what the
  check reports.
- `product-guidelines/styleguide/template.md` lines 164-170, `product-guidelines/testing/template.md`
  lines 193-198, `product-guidelines/coding/template.md` lines 181-186: the texts the author left
  unchanged.
- `elements/common/foundation_source.py` lines 1-30, `elements/common/decision_index.py` lines 1-80,
  `agent-instructions/test_size_invariant.py` lines 1-60, `task-cycle/remarks_check.py` lines 1-90:
  the module beside the new one, the script that writes the index, the test of sizes, and the form
  this report has to keep.
- `foundations/invariants.md`, the entry `shared-module-import-runs-nothing` whole: whether its test
  names the modules it covers (it names the exemplar alone).

## Working copies

All stood under `.runs/review-whole/` and all are
removed; `git worktree list` shows no worktree of mine and `git status --short` of the reviewed
worktree is empty.

- `base\` — a worktree of `1b6fe1c1`, removed with `git worktree remove --force`, then
  `git worktree prune`.
- `head\` — a worktree of `e8b76178`, in which the mutations and the probes ran, each restoring the
  file it changed; removed the same way.
- The diff of the range, the list of sections and the index of my selection, the invariants
  selected, three scripts (the selection of invariants, the mutations, the probes) and the outputs
  of the runs: removed with the directory.
- Kept beside this report: `reports/review-whole-probes.txt`, the output of the probes.

## Unread material

Of the 118 decisions of the index of my selection (48 listed in full, 70 by heading alone) I read
14 whole: WAY-02, WAY-04, WAY-05, WAY-07, WAY-12, WAY-22, WAY-24, WAY-33, WAY-385, WAY-386,
WAY-391, WAY-392, WAY-393 and WAY-394. I read the binding sentences of all 48 listed in full, in
the index, and ran through the 70 headings.

Decisions that bear on the change and stayed unread or read in part:

- WAY-344 (a field missing from a file a script reads): its binding sentences in the index only.
  The new check takes no named field from the copy at the base, so I judged from them.
- WAY-134 (how a task carries what refinement settles): its binding sentences, its fields and most
  of its *Verification*; not its *Rationale* or *Rejected*.
- WAY-18 and WAY-19: binding sentences in the index only.
- WAY-150 and WAY-321: headings only; I took the method of selection from
  `elements/common/way_of_working.md` and the switch from the head of the script.

Guideline files: `guidelines/coding.md`, `guidelines/coding-check.md`,
`guidelines/coding-shared-module.md` and `guidelines/testing.md`, each read whole; none left unread.

Other material:

- `elements/common/test_foundation_check.py`: lines 1-290, 1750-2226 (the base, the decisions that
  nothing holds, and all twelve new tests) and 2395-2452; the rest, which the change does not touch,
  unread.
- `foundations/glossary.md`: the entries `binding part`, `binding sentence`, `files test` and
  `git test`; the other entries by their headings.
- `project-level/technology/reserved_choices.md`: not opened, since the change makes no choice of
  that kind.
- `elements/decisions/skill/` and `elements/common/rules.md`: searched, not read whole.

Read whole: the task document, the author's report, `task-cycle/review/SKILL.md`,
`task-cycle/review/whole_change.md`, `elements/common/way_of_working.md`,
`product-guidelines/reading.md`, `foundations/part_map.md`, `elements/decisions/template.md`,
`elements/common/foundation_check.py`, `elements/common/foundation_text.py`, the diff of the range,
and the 29 invariants whose *Part* names `decisions`, `elements-common`, `agent-instructions` or
`every`.

## Searches not found or unclear

- The index script refused `--decision 5` with `Error: foundations/decisions.md: no decision 5` and exit code 2. Its description and `elements/common/way_of_working.md` both write the switch as `--decision NUMBER` and neither says that the number is given as the log writes it, `WAY-05`.
- `guidelines/coding-shared-module.md` has no *Applies to* for `elements-common`, though the handoff names the file for the new module there; I read it on the handoff's word (finding 6).
