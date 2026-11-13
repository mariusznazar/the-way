# Findings of the review of the whole change — Minor findings within the task

Reviewer's words, cut from `reports/reviewer-report.md` (head `10c0f9eed88d05b2cff8145d2c58227e94346c6d`).
No blocking finding. The two Minor findings the reviewer marked outside the task's scope (4 and 5 of its
report) are not in this file and are not fixed.

1. `project-level/task/skill/draft.md:27-29` (and, in the same shape, `project-level/task/template.md:111` and
   WAY-354's last sentence, "has none"): "a document the refinement does not reopen keeps none, and its missing
   line means that it was not assessed". Written without backticks, "keeps none" can be read as "keeps the value
   `none`", the very reading the decision forbids; the next clause corrects it but a reader or an agent
   skimming the first clause may stop there. Suggest "keeps no line" in `draft.md` and "has no line" in the
   template and WAY-354. Within the task (it is the sentence of the task's own *Question settled*; the wording
   is the task's, so a change of it is a choice of the human). Grade Minor: the second clause states the
   meaning in the same sentence.
2. `task-cycle/skill/correction.md:56-57`: "as in item 8 above". The only mention of item 8 is below
   (`correction.md:65`); nothing above names it. A reader looks for an earlier passage that is not there.
   Suggest "as in item 8 below" or name `request_template.md` kind 8 in place. Within the task.
3. `project-level/task/template.md:112-113`: the sentence on `TODO` ("`TODO` marks a missing answer; never use
   it to make an unfinished task look ready.") was its own line before the change and is now joined at the end
   of the new paragraph's last line, a line longer than the rest of the paragraph. The sentence is unrelated to
   the new line and reads as part of it. Cosmetic; within the task (the author's edit made it).
