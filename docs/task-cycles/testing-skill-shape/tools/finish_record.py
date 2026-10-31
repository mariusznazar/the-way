import sys
R = sys.argv[1]
p = R + '/cycle.md'
t = open(p, encoding='utf-8', newline='').read()


def sub(old, new):
    global t
    assert old in t, old
    t = t.replace(old, new, 1)


sub("- Status: running.", "- Status: request open.")
sub("- Whole-change review: pending.",
    "- Whole-change review: fresh reviewer, Opus 5.5, review-change; 00c0a74..5dc4b3b, FAIL with 5 Important and 5 Minor, 0 out of scope ([review.md](reports/review.md)); 14 Markdown files +326/-195; fix 5dc4b3b..c17f4f8, 5 files +17/-18, PASS c17f4f8 with 1 new Minor ([review-fix.md](reports/review-fix.md)). Coverage of every task item, acceptance criterion and settlement row and source fidelity reported; no projected entry. The reviewer read 40 of its 151 selected decisions whole and 111 by heading only, and says so.")
sub("- Review rounds: pending.",
    "- Review rounds: one whole-change round, one fix and its review. Blocking: stale word counts on all six routes; a mode the base and To do 3 do not have (\"tests at a level its cycle chooses\"); \"Extend what exists\" in the file of the first step, the layout WAY-256 names as violating; four binding sentences in WAY-256 against WAY-05; WAY-265's exemption not covering the styleguide skill. All closed at c17f4f8; no blocking finding remains.")
sub("- Weakest-point checks: pending.",
    "- Weakest-point checks: author named rule preservation (acceptance 1): base and rebuilt files compared sentence by sentence, each base fragment not verbatim accounted for ([author.md](reports/author.md), [fix.md](reports/fix.md)), 18 at the head; the reviewer repeated it with its own comparison in both directions, recomputed every count and walked the six routes by hand twice. The author's check took a mode's meaning as preserved, which the reviewer refuted (finding 2).")

ev = "| 2026-10-31 | return step dispatch |"
i = t.index(ev)
k = t.index("\n", i) + 1
t = t[:k] + (
    "| 2026-10-31 | return step returned | same author, Sonnet 5.5 | as above | [return.md](reports/return.md) | done; no change, no commit; head stays c17f4f8, so the return step has no review of its own |\n"
    "| 2026-10-31 | reconciliation | orchestrator | `git fetch origin foundations`: moved to 2dbf1e7 (PR #61); `git merge --no-ff origin/foundations` | b510f40 | clean merge; only task-cycle/skill/SKILL.md comes in, no file of the change, so no review of the merge (C7); tree 94bcd63 differs from the gated one |\n"
    "| 2026-10-31 | gate on the merged tree | orchestrator | `python -B gate/run_tests.py`, b510f40, task worktree | [merge-gate.log](merge-gate.log) | exit 0; result in *Verification* |\n"
    "| 2026-10-31 | draft publication | orchestrator, Opus 5.5 | `git push --set-upstream origin task/testing-skill-shape`; `gh pr create --draft --base foundations` | PR 62 | both exit 0; upstream matches the branch |\n"
    "| 2026-10-31 | assessment publication | orchestrator, Opus 5.5 | `gh pr comment 62 --body-file request-comments/assessment.md` | [comment](request-comments/index.md) | exit 0; whole table |\n"
    "| 2026-10-31 | stage accounting | orchestrator, Opus 5.5 | `python -B task-cycle/cycle_stages.py 2ccd66d4-d0c4-460a-9f99-587b25362648 --output .runs/task-cycles/testing-skill-shape/stages.md` | [stages.md](stages.md) | exit 0; snapshot before the record's commits |\n"
) + t[k:]

sub("\n## Artifacts\n", (
    "| C7 | The target branch moved to 2dbf1e7 during the cycle; does the merge need a review? | No: the merge brings task-cycle/skill/SKILL.md alone, a file the change does not touch and the skill does not read; the gate runs again on the merged tree | `git diff 00c0a74 origin/foundations --stat`; identifiers WAY-265 and WAY-266 free on the target | A fresh review of a merge that leaves the reviewed code as it was | A collision the gate does not see; the reviewed files are unchanged by the merge | request |\n"
    "| A1 | File layout of the rebuilt skill (author) | Ten files beside the skill, one per step plus variants | author.md, choice 1 | One file for steps 2 and 3 | A file more or less | author, reviewer |\n"
    "| A2 | \"How to show\" and \"Write each answer\" (author) | Stay in `SKILL.md` as rules that hold across steps | author.md, choice 2; WAY-256 | `how_to_show.md` named by steps 2 and 4 | About 130 words carried through steps that do not ask | author, reviewer |\n"
    "| A3 | The new-level mode (author) | Reworded to what `product-guidelines/reading.md:77-78` says; its clause on a level the cycle chooses removed by the fix of finding 2 | author.md, choice 3; fix.md | Leaving the base's words | An agent on a level with no recipe skips step 2; guarded by the extension clause | author, reviewer |\n"
    "| A4 | Foundation additions and trust boundaries (author) | Read at step 1, after the parts are named | author.md, choice 4; WAY-248 | Boundaries at step 3 only | Step 4 lacks them on one route | author, reviewer |\n"
    "| A5 | When `product-guidelines/template.md` is read (author) | Step 4, as in the styleguide skill | author.md, choice 5 | Step 2 | A starting set drafted without the general form, caught at step 4 | author, reviewer |\n"
    "| A6 | Step 3's pointer (author) | Names `audit.md` and `new_level.md` directly and separately | author.md, choice 6 | `audit.md` pointing on to `new_level.md` | The new-level agent reads the audit first | author, reviewer |\n"
    "| A7 | Row 1 as a new entry (author) | Superseded by C6: written into WAY-256 in place | author.md, choice 7; author-repair.md | Kept as a new entry | See C6 | discarded in 5dc4b3b |\n"
    "| A8 | The exemption in the entry of row 3, now WAY-266 (author) | \"Skills of guidelines whose text stands unchanged are not bound by it until they are rebuilt\" | author.md, choice 8 | No clause: the coding skill breaches the entry on the day of the merge | The human wanted it to bind all three at once; drop the clause | author, reviewer, request |\n"
    "| A9 | *Rejected* of the entries (author) | The ways not chosen of questions 2, 3 and 4, without counts; \"two levels as in task 4\" rendered as the variant named only in the step's file | author.md, choice 9 | Copying the lines with their counts | One line of WAY-265's *Rejected* reads the question otherwise than the human meant | author, reviewer |\n"
    "| R1 | Place of the new sentence in WAY-256 (author) | Within the binding paragraph, joined to the closing sentence after finding 4 | author-repair.md, choice 1; findings.md, 4 | A separate paragraph | The paragraph reads densely | author, reviewer |\n"
    "| R2 | Wording of WAY-256's *Rationale* (author) | The author's own words from what the removed entry carried, no count or file name | author-repair.md, choice 2 | Copying that entry's text | None seen | author, reviewer |\n"
    "| F1 | Form of the moved cycle's-choice sentence (author) | Inside the exemplar item of `settle.md`, its full stop now a semicolon | fix.md, choice 1 | A bullet of its own | The reviewer declined to judge it | author, reviewer |\n"
    "| F2 | Order of \"Extend what exists\" in `SKILL.md` (author) | Last among the rules before \"Write each answer\" | fix.md, choice 2 | First | None | author, reviewer |\n"
    "\n## Artifacts\n"))

sub("| Frozen task | [task.md](task.md) | source copy | accepted 2026-10-31 |\n", (
    "| Frozen task | [task.md](task.md) | source copy | accepted 2026-10-31 |\n"
    "| Author handoff and report | [author-handoff.md](reports/author-handoff.md), [author.md](reports/author.md) | orchestrator, author | concerns read; own figures superseded by fix.md and word-counts.md |\n"
    "| Repair before review | [author-repair-handoff.md](reports/author-repair-handoff.md), [author-repair.md](reports/author-repair.md) | orchestrator, author | done |\n"
    "| Assessment and counts | [assessment.md](reports/assessment.md), [word-counts.md](reports/word-counts.md), [sentence-diff.txt](reports/sentence-diff.txt) | author | rechecked independently by the reviewer |\n"
    "| Change | 1c66173, d024d56, 5dc4b3b, c17f4f8; merge b510f40 | author; orchestrator for the merge | FAIL, then PASS c17f4f8 |\n"
    "| Whole-change review | [review-handoff.md](reports/review-handoff.md), [review.md](reports/review.md) | orchestrator, reviewer | FAIL: 5 Important, 5 Minor |\n"
    "| Fix | [fix-handoff.md](reports/fix-handoff.md), [findings.md](reports/findings.md), [fix.md](reports/fix.md) | orchestrator, author | done |\n"
    "| Review of the fix | [review-fix-handoff.md](reports/review-fix-handoff.md), [review-fix.md](reports/review-fix.md) | orchestrator, reviewer | PASS, 1 new Minor |\n"
    "| Return step | [return-handoff.md](reports/return-handoff.md), [return.md](reports/return.md) | orchestrator, author | no change, no commit |\n"))

a = "| `python -B gate/run_tests.py` | orchestrator, reviewed head c17f4f8"
i = t.index(a)
k = t.index("\n", i) + 1
t = t[:k] + "| `python -B gate/run_tests.py` | orchestrator, merged head b510f40, tree 94bcd63, task worktree, Windows | 0; 614 tests in 8 directories, every directory passed ([merge-gate.log](merge-gate.log)) | no failure; same 5 instruction-files checks skipped on Windows (unrun, not passed) |\n" + t[k:]

i = t.index("## Return step")
j = t.index("The return step corrects in the same change")
t = t[:i] + (
    "## Return step\n\n"
    "- Foundation compared with code: WAY-256, WAY-265, WAY-266, each decision of *Decisions in play*, each entry the search found and the part-map entries of product-guidelines, instruction-files and decisions, compared with the files at c17f4f8; nothing no longer matches ([return.md](reports/return.md)).\n"
    "- Decisions written or changed: WAY-256 changed in place; WAY-265 and WAY-266 new (foundation step).\n"
    "- Invariants written or changed: none.\n"
    "- Environment facts: none.\n"
    "- Glossary terms: none.\n"
    "- Part-map changes: none.\n"
    "- Projected entries written whole or in part: none.\n"
    "- Rows of *Settlements to record* written: 1 — WAY-256; 2 — WAY-265; 3 — WAY-266.\n\n"
) + t[j:]

i = t.index("## Request handoff")
t = t[:i] + (
    "## Request handoff\n\n"
    "- Request URL and status: https://github.com/mariusznazar/the-way/pull/62; opened as a draft, marked ready after the record's commits. Not merged.\n"
    "- Cycle and its reasons: no spec, no open design choice; one author without a plan; one repair before review, one whole-change review with one fix and its review.\n"
    "- Process pin: none; the-way works on itself, base 00c0a74, foundations 2dbf1e7 merged at b510f40.\n"
    "- What this request settles: WAY-256 changed, row 1; WAY-265 new, row 2; WAY-266 new, row 3; meaning sentences in the request.\n"
    "- What the foundation puts in front of the human at the merge: none.\n"
    "- Checks: `python -B gate/run_tests.py`, exit 0 on b510f40, 614 tests in 8 directories; 5 instruction-files checks skipped on Windows, named in the request; none failed. No agent session was run on the rebuilt skill.\n"
    "- Human actions the request waits for: none.\n"
    "- Questions: none.\n"
    "- Review findings listed: Minor findings 6 to 10 of [review.md](reports/review.md) and 11 of [review-fix.md](reports/review-fix.md) in the reviewer's words, in the request; findings outside the task's scope: none.\n"
    "- Blocked by review: none.\n"
    "- Choices within the request: 20, in the questions table.\n"
    "- Writes to the task's backlog entry: none.\n"
    "- Process remark of the orchestrator: the report of the author did not show the search of the foundation, and the foundation's text says the search leaves no record, so a report that omits it cannot be told from a search not made; the orchestrator asked for it in a repair. The base gate ran in the unchanged main checkout at 00c0a74, as the cycle's text stood when it started; PR #61, merged during the cycle, now names a separate checkout under `.runs/` or a run before anything changes.\n"
    "- Process remarks of the stages, copied word for word:\n\n"
    "- Stage author, report .runs/task-cycles/testing-skill-shape/reports/author.md, **Searches not found or unclear**:\n"
    "  - No remark of PRs #50, #51, #52, #59 or #60 (their comments, reviews and inline comments, read by `gh pr view <n> --comments` and `gh api`) mentions this skill; #51 has no comment. No mistake that a fragment of this skill was added for was found in the five commits of its history (judged from their messages and the PRs; I did not read the five diffs line by line).\n"
    "  - `rg`-style search for incoming references to sections of this skill (`What reaches the task document`, `A new level`, `Starting set`, `Orchestrated mode`) found them only inside this skill and in `product-guidelines/coding/SKILL.md`, which has its own sections of the same names (not touched). `product-guidelines/reading.md:79`, `testing/template.md:7`/`:105`, `project-level/task/skill/guideline_findings.md`, `project-level/plan/skill/SKILL.md:122` and `installation/*` name the skill, not a section.\n"
    "  - The task text \"`product-guidelines/testing/SKILL.md:53-54`\" (the name \"Writing the file\") is the template's section; it stands in `task_document.md` unchanged and the template's `## Writing the file` exists (`template.md:264`).\n"
    "  - Unclear: whether row 1 should extend WAY-256 itself (choice 7); what \"two levels as in task 4\" in Question 3 means exactly (concern 2).\n"
    "  - Nothing else was looked for and not found.\n"
    "- Stage whole-change review, report .runs/task-cycles/testing-skill-shape/reports/review.md, **Searches not found or unclear**:\n"
    "  - Unclear: `author.md` describes choices 7 and 8 in the old form; its repair note says so, and I judged the tree.\n"
    "  - Unclear: whether row 2's \"pliki\" means a skill's every file or the step and variant files. I took the second, which the row's own example requires.\n"
    "  - Otherwise none.\n"
)
open(p, 'w', encoding='utf-8', newline='').write(t)
print('ok', t.count('pending'))
