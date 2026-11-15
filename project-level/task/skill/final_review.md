# Review and hand off

When the draft is complete, before you show it, list the decisions it leaves to the executor
(WAY-377, WAY-378) where its *Decisions in play* is not `none` or the task changes a skill or an
instruction file. For any other task skip the step and say nothing of it. The step keeps one file in
the product's ignored `.runs/` directory, `.runs/decisions-list/<task-name>.md`, `<task-name>` being
the task document's name without its extension, with three parts: *List*, *Critique* and *Verdicts*.
No agent of the step writes it: you write what each returns, and in the refinement with a project
orchestrator `orchestrated_mode.md` gives who writes what.

1. **List.** Start one fresh agent on a class of model cheaper than yours, named in general terms
   and never by the name of a model. Give it the complete task document and the full text of each
   foundation entry that *Decisions in play* names, and nothing of the conversation of the
   refinement. It lists each decision an executor would have to take on its own that the document
   and those entries leave unanswered or answer in part, and marks where each answer is known:
   written, with the file and the sentence; visible only in a file the document names as a model; or
   guessed, with the answer the agent would take. A decision counts only where it follows from a
   sentence that stands in the document or in a named entry and where different answers give a
   different, observable result inside the task's scope (WAY-374); a case outside that scope counts
   for nothing, the list owes no decision and no number, and a matter that the check for a word read
   two ways has asked or that *Questions to settle* holds does not return.
2. **Critique.** Start one fresh agent on the same class, with read access to the repository the task
   changes, and give it the document, the entries and the list (WAY-120). For each guess it settles
   whether the repository or the document already settles the answer, with the quotation and the
   path; whether the answer the first agent took agrees with what the repository says; what would
   change in the files the task changes if the answer were another; and a verdict: most likely
   right, most likely wrong, or truly open. It writes in plain language and names what it did not
   check as not checked.
3. **Verdicts.** For each matter you will show, open the file the critique quotes from and check the
   quotation word for word, then write one explicit verdict under *Verdicts*: the critique's, or
   yours with its reason. A quotation that does not hold voids the critique's verdict on that
   matter; settle the matter from what the file says, or count it open.
4. **Show.** Show the human only the matters whose verdict is truly open and the gaps of the
   document itself — a guess the critique found most likely wrong is such a gap — at most about
   four, the most consequential first, each in plain language as "How a skill asks" gives for a
   decision: the ways, the cost of each and a recommendation (WAY-113). Give the path of the file.
   Where no matter is open, say nothing of the step.
5. **Answers.** Put the human's answer under *Questions to settle* with the human's words as its
   source and the ways not chosen, as for any question (WAY-134); what it changes in *Decisions in
   play* and *Settlements to record* enters the document as steps 4 and 5 of the skill give.

When the draft is complete, show it whole. Propose any block to move from Description to Context
or remove, with a short reason for each; apply the moves the human accepts. If there is nothing
worth moving, say so and continue.

Check that every blocking question has an answer, with its ways not chosen where the human chose
among ways shown (WAY-134), no item of the section *Technology* ends `— open`, the numbered work is
executable, the questions brought into this task are accounted for, every place to change in a file
is pointed at by a heading or a quotation, with a line number at most as a hint, the
decisions in play are present or `none` where the reading of the foundation found none, *Settlements
to record* opens with its `Candidates:` line and holds no row awaiting the human, and *Human
actions* reads `none` or has every human action placed and every human action before the cycle done
(WAY-124, WAY-140). For a plan member, check the assignment by `project_plan_task.md`; for any task
using approved project settlements, check the definition's approval and that every projected entry
its code makes true is marked with the part made true. Report an obstacle instead of declaring
readiness when a check fails.

Follow `guideline_findings.md` for a newly reached part, an unresolved classification or metadata,
or a missing-discipline question still awaiting its task's merge; a recorded dependency or an empty
reading does not answer it.

Once these checks pass, show the complete final document and explicitly ask the human to accept
that document, then wait. Acceptance of candidates, Human-action placement or an earlier draft is
not this acceptance. Keep `Status: waiting for human` until it is given, including a task with no
candidates. Apply requested changes and show the complete revised document again. In manual mode
mark `Status: ready for cycle` only after this acceptance and all applicable checks pass
(WAY-124), then move the task's line in the backlog to ready as `project-level/task_line.md`
gives, by the rules of the task place that the section `## Backlog` of the product root
`AGENTS.md` names, found as `project-level/backlog_place.md` gives. For the orchestrated handoff
and status, follow `orchestrated_mode.md`. No definition awaiting its gate permits readiness.
