"""Fill the rest of the cycle record once the request is open."""
import re

C = '.runs/task-cycles/plan-project-skill-shape/'
p = C + 'cycle.md'
s = open(p, encoding='utf-8', newline='').read()


def sub(a, b):
    global s
    assert s.count(a) == 1, a
    s = s.replace(a, b)


sub('- Status: running\n', '- Status: request open\n')
sub('- Whole-change review: pending\n', "- Whole-change review: fresh reviewer, Opus 5.5, review-change; 2f51e6c..db3845c, FAIL with 1 Important and 4 Minor, 3 lines out of scope ([review.md](reports/review.md)); 13 Markdown files +236/-156; fix db3845c..1fa823e, 1 file +2/-2, PASS 1fa823e with 2 new Minor and 2 lines out of scope ([review-fix.md](reports/review-fix.md)). Coverage of every task item and acceptance criterion and source fidelity reported; no settlement row and no projected entry. The reviewer read 70 decisions whole, every one of *Scope* `project-level`, of *Decisions in play* and those the moved text cites, and says the other 167 were not.\n")
sub('- Review rounds: pending\n', "- Review rounds: one whole-change round, one fix and its review. Blocking: the sentence of `existing_plan.md` that has `read.md` read was given two effects by the materials, and routes 3 and 6 were counted on the reading task question 3 turned down. Closed at 1fa823e; no blocking finding remains.\n")
sub('- Weakest-point checks: pending\n', "- Weakest-point checks: author named rule preservation: base and rebuilt files compared sentence by sentence, 3 base sentences not verbatim, all pointers, each accounted for ([author.md](reports/author.md)); the reviewer repeated it with its own comparison (144 clauses, the same 3, 36 new), read each new clause for what it switches off, recomputed every figure and walked routes 2, 3, 4, 5 and 7 by hand. The sentence comparison could not see what the new sentence does, which the author raised as a concern and the reviewer made finding 1.\n")
sub('| final-gate.log, final-gate.exit | running |\n', '| final-gate.log, final-gate.exit | running beside the review |\n')
tail = "task-cycle/skill/return_step.md and foundation_step.md; head 1fa823e | reports/return.md | sent |\n"
sub(tail, tail
    + "| 2026-11-01 | return step returned | same author, Sonnet 5.5 | as above | [return.md](reports/return.md) | done; no change, no commit; head stays 1fa823e, so the return step has no review of its own (C6) |\n"
    + "| 2026-11-01 | gate on the fix head complete | orchestrator, Opus 5.5 | as above | [final-gate.log](final-gate.log) | exit 0; 615 tests in 8 directories, every directory passed; 5 skipped |\n"
    + "| 2026-11-01 | reconciliation | orchestrator, Opus 5.5 | `git fetch origin foundations`: still 2f51e6c, an ancestor of the head | none | no merge needed; the final tree is the gated one (C6) |\n"
    + "| 2026-11-01 | draft publication | orchestrator, Opus 5.5 | `git push --set-upstream origin task/plan-project-skill-shape`; `gh pr create --draft --base foundations` | PR 69 | both exit 0; upstream matches the branch |\n"
    + "| 2026-11-01 | assessment publication | orchestrator, Opus 5.5 | `gh pr comment 69 --body-file request-comments/assessment.md` | [comment](request-comments/index.md) | exit 0; whole table |\n"
    + "| 2026-11-01 | stage accounting | orchestrator, Opus 5.5 | `python -B task-cycle/cycle_stages.py 33b4f246-0e6f-405f-af21-13bb33c778c4 --output .runs/task-cycles/plan-project-skill-shape/stages.md` | [stages.md](stages.md) | exit 0; snapshot before the record's commits |\n")
rows = [
    "| C5 | The reviewer lists Minor findings 2 to 7, some cheap to fix | not fixed; every Minor goes to the request, as \"The end of a code review\" gives | task-cycle/skill/SKILL.md, \"The end of a code review\" | fixing Minors in the round | a figure of the assessment reads 185 for 187; a reader loses nothing else | fix handoff, request |",
    "| C6 | Review of the return step and of a merge | neither ran: the return step committed nothing, and the target did not move | step 11, step 12; head 1fa823e, `git merge-base --is-ancestor` | a review with nothing to review | none | request |",
    "| A1 | One file per step 1-7 and four variant files | author's choice | [author.md](reports/author.md), choices | grouping steps 3-4; keeping steps 5-7 in `SKILL.md` | a little more upkeep | commit db3845c |",
    "| A2 | Step 0's reading of the template and \"Otherwise begin with step 1\" stay in `SKILL.md` | author's choice | as above; WAY-256 | moving them, one instruction for one pointer | none | commit db3845c |",
    "| A3 | Base lines 102-104 stand in the reading file, not in `SKILL.md` | author's choice; the reviewer confirmed the reach | as above; [review.md](reports/review.md) | keeping them in `SKILL.md` | about 55 words on every use the other way | commit db3845c |",
    "| A4 | Step 0 pointer: \"by the human or in a dispatched turn by its conversation file\" | author's choice; the reviewer confirmed what it selects and listed a third source as Minor 4 | as above | the literal base wording, which would leave a dispatched turn without the file | a rare route with a wrong start | commit db3845c |",
    "| A5 | A fragment needed in several places stays at its step and is restated where else it is needed | author's choice | as above | moving it to step 5 only | repeated text to change together | commit db3845c |",
    "| A6 | The delegated file reaches steps 5-7 by an opener in each file and a clause in `SKILL.md` | author's choice | as above | one sentence in the delegated file, unseen when the step files are read | three short sentences to keep in line | commit db3845c |",
    "| A7 | The condition of `guideline_tasks.md` carries \"missing or uncertain\" | author's choice; the reviewer found it widens only a read | as above | \"missing\" alone | an unneeded read of 176 words | commit db3845c |",
    "| A8 | No entry written, none found out of line | author's choice | as above; [return.md](reports/return.md) | none | a mismatch missed | commit db3845c |",
    "| A9 | Names of the eleven files | author's choice | as above | other names | none | commit db3845c |",
    "| A10 | The readings of the routes the task leaves open (which steps run on routes 3, 4, 6, 7) | author's choice, stated in `word-counts.md` | as above; C4 for routes 3 and 6 | counting step 4 on route 4 | words of `place_questions.md` come on top where a question moves | word-counts.md |",
]
c4 = "a resumed draft reads more than a literal base did, about the foundation and guidelines words a route already pays | fix handoff |\n"
sub(c4, c4 + '\n'.join(rows) + '\n')
sub("| Frozen task | [task.md](task.md) | orchestrator | n/a |\n",
    "| Frozen task | [task.md](task.md) | orchestrator | n/a |\n"
    "| Change | commits db3845c, 1fa823e | author, Sonnet 5.5 | FAIL, then PASS 1fa823e |\n"
    "| Assessment | [reports/assessment.md](reports/assessment.md), [published copy](request-comments/assessment.md) | author, Sonnet 5.5 | checked by the reviewer; Minor findings stand |\n"
    "| Word counts | [reports/word-counts.md](reports/word-counts.md), `tools/word_counts.py`, `tools/verify_counts.py` | author, Sonnet 5.5 | every figure recomputed by the reviewer, 0 differ |\n"
    "| Reports | [author](reports/author.md), [review](reports/review.md), [findings](reports/findings.md), [fix](reports/fix.md), [review of the fix](reports/review-fix.md), [return step](reports/return.md) | as named | n/a |\n"
    "| Request text | [request-draft.md](request-draft.md) | orchestrator, Opus 5.5 | n/a |\n")
head = "| Command or manual check | Actor, commit and environment | Exit code and result | Failed or unchecked |\n|---|---|---|---|\n"
sub(head, head
    + "| `python -B gate/run_tests.py` (base, before any change) | orchestrator, 2f51e6c, separate checkout `.runs/base-check` deleted after the run, Windows | exit 0; 615 tests in 8 directories, every directory passed ([base-gate.log](base-gate.log)) | none failed; 5 skipped by the platform, unchecked (log line 30 `OK (skipped=5)`) |\n"
    + "| `python -B gate/run_tests.py` | orchestrator, db3845c, task worktree, Windows | exit 0; 615 tests in 8 directories ([head-gate.log](head-gate.log)) | none failed; the same 5 skipped |\n"
    + "| `python -B gate/run_tests.py` (reviewed change, the tree of the request) | orchestrator, 1fa823e, task worktree, Windows | exit 0; 615 tests in 8 directories ([final-gate.log](final-gate.log)) | none failed; the same 5 skipped: test_a_dot_dot_after_a_directory_link_is_resolved_as_the_system_does, test_an_absolute_link_out_of_the_repository_is_not_read, test_a_link_loop_is_reported_as_unreadable_and_the_run_goes_on, test_every_directory_link_is_reported_wherever_it_points, test_a_fifo_named_like_an_instruction_file_does_not_stop_the_run |\n"
    + "| `python -B elements/common/foundation_check.py`, `python -B instruction-files/check_instructions.py .`, `python -B agent-instructions/skill_entry_points.py --write` | author, db3845c, 1fa823e and at the return step | exit 0 each; `check_instructions.py` output as on the base; entry points unchanged | see the reports |\n"
    + "| Manual: walk of routes 2, 3, 4, 5 and 7, each assessment row against its place | reviewer, Opus 5.5, db3845c; routes 3 and 4 again at 1fa823e | not applicable; one blocking finding, then held | [review.md](reports/review.md), [review-fix.md](reports/review-fix.md) |\n")
sub("- Foundation compared with code: pending\n- Decisions written or changed: pending\n- Invariants written or changed: pending\n- Environment facts: pending\n- Glossary terms: pending\n- Part-map changes: pending\n- Projected entries written whole or in part: pending\n",
    "- Foundation compared with code: every decision of *Decisions in play*, the decisions the moved text cites, the entries a search found and the part map entry `project-level` compared with the files at 1fa823e; nothing no longer matched ([return.md](reports/return.md))\n- Decisions written or changed: none\n- Invariants written or changed: none\n- Environment facts: none\n- Glossary terms: none\n- Part-map changes: none; `project-level/**` covers the new files\n- Projected entries written whole or in part: none\n")


def searches(f):
    t = open(C + 'reports/' + f, encoding='utf-8').read()
    m = re.search(r'## Searches not found or unclear\n\n(.*?)(?=\n## |\Z)', t, re.S)
    return m.group(1).rstrip()


items = [('author', 'author.md'), ('fix', 'fix.md'), ('review of the whole change', 'review.md'),
         ('review of the fix', 'review-fix.md'), ('return step', 'return.md')]
rem = ''
for n, f in items:
    body = '\n'.join(('  ' + l if l else '') for l in searches(f).split('\n'))
    rem += f'- {n} (`reports/{f}`):\n\n{body}\n'
sub("- Request URL and status: pending\n",
    "- Request URL and status: https://github.com/mariusznazar/the-way/pull/69, ready for review\n"
    "- Cycle and its reasons: no spec, one author; see \"Spec and execution route\"\n"
    "- Process pin: none; the-way works on itself\n"
    "- What this request settles: no foundation entry; To do 4 and 5 change one sentence of `lead-project` and add the sentence that has a session on an existing plan go through step 1\n"
    "- What the foundation puts in front of the human at the merge: none\n"
    "- Checks: `python -B gate/run_tests.py`, exit 0; none failed; 5 skipped by the platform, named under *Verification*\n"
    "- Human actions the request waits for: none\n"
    "- Questions: none\n"
    "- Review findings listed: Minor 2 to 5 of [review.md](reports/review.md), 6 and 7 of [review-fix.md](reports/review-fix.md), and the five lines of their *Declined to judge* as out of scope, in the request; no check failed and passed again\n"
    "- Blocked by review: none\n"
    "- Choices within the request: 16, in the questions table\n"
    "- Writes to the task's backlog entry: none\n"
    "- Process remarks on the-way, copied word for word from **Searches not found or unclear**:\n\n" + rem)
open(p, 'w', encoding='utf-8', newline='').write(s)
print(len(re.findall(r'^\| (?:C|A)\d+ \|', s, re.M)))
