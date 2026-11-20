# Handoff — correction 2, for the human's remarks (a change of scope)

You are the one author, resumed for a second correction after the human's remarks on the open request.
The remarks bind. The person who requested this cycle delegated intermediate choices to the orchestrator;
no answer here is that person's approval.

- Worktree and branch: the task's worktree, `task/decision-length-check`; the head you start from is
  the commit that removes the record's copy after correction 1 (`b0bba24d`); the code and the entries are as
  correction 1 (`35796540`) left them. Work from the worktree's root. The target branch has no new commit,
  so nothing was merged or renumbered.
- Your method: `task-cycle/change/SKILL.md`, variant **"a correction for the human's remarks"**; read the file
  the variant's row names. The change writes a decision (WAY-05) again, so you do the foundation step with it:
  read `task-cycle/skill/foundation_step.md` whole and the `SKILL.md` of the decisions element at the path it
  gives. Return before review; the return step is another dispatch.
- The remarks, word for word: `.runs/task-cycles/decision-length-check/reports/correction-2-remarks.md`. Read
  it whole; it is what you make: item 1, a limit of 600 words for the binding sentences of one decision, all
  their paragraphs together, in the check, WAY-05, the template, the descriptions of the check and the tests;
  item 2, a further paragraph that may carry a part of the entry's own question, in WAY-05 and in the section
  "Binding sentences" of the template, with `WAY-19` or any other entry that says the opposite changed with
  them. Do not widen it: the entries over a limit today stay as they are and are only listed.
- Answers of the orchestrator:
  - The 600 words are counted as the check already counts the words of a paragraph (a run of characters between
    spaces), over all the paragraphs of the binding sentences of one decision together; the error names the
    decision and the measure that is over, with its value, as the error of a paragraph does; the entry is
    added or changed by the same test as for the limits of a paragraph, a different division into paragraphs
    included, and any other decision over the limit is only listed with a line `listed:`.
  - Where WAY-05 needs a new sentence, the limit stands in its binding sentences and WAY-05 itself stays within
    all three limits afterwards (count it with the script). *Rejected* gets the two ways not chosen of each
    item of the remarks (under "Not chosen"), written as the rule of WAY-05 on counts and on the process asks
    (no count of entries in prose), with their reasons; the pair of examples of WAY-05 is brought to what the
    two items say (the part of the entry's own question may have a paragraph of its own).
  - The review of correction 1 reported, outside the task's scope, that WAY-19 gives a part of the question an
    entry answers "one sentence" and calls it by other words than WAY-05, which says "a part of another
    question". Your item 2 touches the same words: read WAY-19, WAY-05 and
    `elements/decisions/template.md` lines about it (the section "Binding sentences", and the bullet that cites
    WAY-19 near "Fields and their readers"), settle what each says after your change so that they do not
    contradict, change the entries that say the opposite, and name each such entry and what you changed in your
    report, so that the request can name it (the remarks ask for that).
  - The two follow-up tasks of the human, which shorten the entries over a limit, are outside this change.
- What you read: the foundation of the parts you touch, by the selection of "Reading the foundation" in
  `elements/common/way_of_working.md` (the index of the orchestrator's earlier selection is
  `.runs/task-cycles/decision-length-check/orch_index.md`, a start, not the whole selection; you run the
  selection and the search of the foundation of step 2 there, WAY-33): WAY-05 whole with its *Rejected*, WAY-19,
  WAY-12, WAY-02, WAY-22, WAY-385 whole; the guidelines `guidelines/coding.md`, `guidelines/coding-check.md`,
  `guidelines/testing.md` whole; the code and tests `elements/common/foundation_check.py`,
  `elements/common/foundation_text.py` and `elements/common/test_foundation_check.py` (the tests of the check
  of length and the tests the new one stands beside), the template and the three places that describe what the
  check reports (the head of the script, `agent-instructions/README.md`, `README.md`). Note that
  `foundation_check.py` stands at 1111 lines against the 1200 of WAY-385 and a function at most 110.
- Tests: each new test holds a sentence of WAY-05 by a line `decision:` quoting the start of that sentence as
  you leave it, as WAY-12 and WAY-02 give; record its failing run before the code and its passing run, each
  with command and exit code (do not take the exit code through a pipe).
- Checks to run again, each with command and exit code: `python -B gate/run_tests.py elements/common`,
  `elements/part-map`, `agent-instructions`, `product-guidelines`, `installation`;
  `python -B elements/common/foundation_check.py` (exit 0, `0 errors`); `ruff check .` and
  `ruff format --check .` with the environment under `.runs/quality-venv`. Do not run the product's full gate:
  CI is its final gate and a local run is the orchestrator's.
- Commit on the task branch by path, in English, in the form of the commits of this repository; leave the worktree
  clean. Do not touch the files of `.runs/task-cycles/`, and make no file outside the worktree. Your directory
  for working copies: `.runs/author-correction-2/`; remove it before you return.
- Your report: `.runs/task-cycles/decision-length-check/reports/author-correction-2-report.md`, with its status,
  commits, checks, your own-work check (the weakest point of the change and how you checked it), the entries you
  wrote or changed with the marks the foundation step gives, **Unread material**, **Searches not found or
  unclear** and working copies, as before.
