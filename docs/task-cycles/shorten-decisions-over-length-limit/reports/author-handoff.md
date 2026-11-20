# Handoff — the one author of the change (`make-change`, "the whole change as the one author")

## Delegation

The person who requested this cycle has delegated intermediate choices to the orchestrator. Never label an answer of yours as that person's approval. You make the whole change below; you do not open the request, do not merge, do not run the product's full gate (its run is the orchestrator's or CI's, WAY-160). Focused runs of one directory are yours: `python -B gate/run_tests.py <directory>`.

## Where

- Worktree (the root of your work, on the branch `task/shorten-decisions-over-length-limit`, base `bafe3904a80f3f74e6a722dc3d8dc8be1ed882cc`): the root of the task's worktree. Work only there.
- The directory for your working copies: `.runs/author/` of the worktree.
- Report path: `.runs/task-cycles/shorten-decisions-over-length-limit/reports/author-report.md`. This file is the input of the cycle's scripts (`task-cycle/remarks_check.py` reads it); a subagent's write of a file whose name starts with `report` is refused by Claude Code, but this name begins with `author`, so the note that leaves that case open applies. Where the write is refused all the same, return the report whole as your answer.
- `cycle.md` and the other files of `.runs/task-cycles/shorten-decisions-over-length-limit/` — other agents' handoffs, reports and findings — are not yours to read, except those named here.

## Method and variant

Read `task-cycle/change/SKILL.md` whole. Your variant: **the whole change as the one author**. Read a file it names only when the step or variant that names it comes. You also do the foundation step: read `task-cycle/skill/foundation_step.md` whole and, for the new decision, `elements/decisions/skill/SKILL.md` whole (that is the path of the decisions element's skill; `elements/decisions/SKILL.md` does not exist) and the files it names when its step names them. No spec and no plan exist: the route is one author without a plan.

## The task

The frozen task document: `.runs/task-cycles/shorten-decisions-over-length-limit/task.md`. Read it whole — its *To do* 1–13 and *Acceptance criteria* are your requirement; *Questions to settle* hold the settlements with their sources; *Decisions in play* holds what each changed entry says to do and where; row 1 of *Settlements to record* is the new decision you write whole in its place (`Goes to: decision`), marked `row 1` in your report. *Human actions* is `none`; *Questions carried to cycle* is `none`.

The two questions of the start: it touches no trust boundary; it holds no operation that cannot be undone. No open design choice: if you meet one, return `returned` with no code, as `task-cycle/change/SKILL.md` gives.

The change rests on #152, merged at the base: the limit is 3 sentences and 300 words a paragraph and 600 words an entry, counted by `elements/common/foundation_check.py` (with `elements/common/foundation_text.py`), and WAY-05 and `elements/decisions/template.md` hold it. Read WAY-05 as it stands at the base, not the wording the task quotes as "before #152".

## Foundation to read, selected by the orchestrator

Decisions of `foundations/decisions.md`, each whole (the range from its heading to the next heading of any level, rationale and *Rejected* included): WAY-344 (the split), WAY-287, WAY-19, WAY-391, WAY-05, WAY-25, WAY-18, WAY-12, WAY-02, WAY-30, WAY-114, WAY-33 (the search of the whole foundation for the entries a change touches), WAY-150 and the nine other entries of the task's table "Podział na akapity" (WAY-256, WAY-148, WAY-339, WAY-289, WAY-405, WAY-136, WAY-154, WAY-139, WAY-134), the decisions WAY-386 to WAY-390 for how a *Scope* agrees with *Applies to*, and the decisions WAY-339 and WAY-405, whose sentences tests hold by `decision:` lines. For the new decision the decisions element's skill selects the rest of its reading.

Files whole: `elements/decisions/template.md` (sections "Binding sentences" and "Changing a decision" and "Decision entry"), `elements/common/foundation_check.py` for what the check reads as a sentence, a paragraph and a `decision:` line, `guidelines/coding.md` and `guidelines/testing.md` (you change test files and comments), `guidelines/coding-shared-module.md` (point 11), `agent-instructions/README.md` (point 12).

Every file you change, whole, before you change it; of `foundations/decisions.md`, the entries you change and the section the new entry goes into.

## What to produce

The whole of the task's *To do* 1–13 and its acceptance criteria, one change on this branch, committed by path (`git add <path>…`, never `git add -A`), in commits you name in the report; commit messages in English, in the form of the existing commits of the repository. Particular care where the task asks it:

- The sentences of the ten entries and of the kept and moved sentences of WAY-344 keep their words (the acceptance criterion compares the joined text word for word with the base, except one word in WAY-150, and in WAY-344 and WAY-287 the words the task names). Check it by a script of your own in `.runs/author/` that reads the log at the base (`git show bafe3904:foundations/decisions.md`) and at the head and compares, entry by entry; keep the script in `.runs/author/`, and say in the report what it compared and its exit code. Do not commit it.
- Find every reference to WAY-344 and to the sentences that move, by a search of the whole repository (docs of the cycles under `docs/task-cycles/` are records and stay as they are), by number and by the start of each moved sentence in a `decision:` line; the task names the files it knows of, and the search is yours. A reference to WAY-344 that does not concern a moved sentence stays; say in the report which references you left and why.
- The new decision's number is the next free number after the highest number the log holds, an entry or a withdrawn number (WAY-19); say it in the report.
- WAY-344's *Rationale*, *Rejected* and the clauses of *Verification* go to the decision whose sentence they concern, none lost, none in both (task, *To do* 5): give in your report, for each clause of *Verification*, each sentence of *Rationale* and each rejected way, the decision it went to and the sentence it concerns — the orchestrator copies the map into the request's description.
- Run `python -B elements/common/foundation_check.py` and the focused tests of every directory you changed (`elements/common`, `process-audit`, `task-cycle`, `agent-instructions`, `elements/decisions`, `elements/invariants` as they apply), each with its command and exit code in the report.
- Run the own-work check as the method gives: name the weakest point of your change and check it.

## Working copies

An agent of the cycle that makes a working copy to check something — a worktree of a commit, a clone, a script, a screenshot, a prepared input of a test — makes it in a directory of its own directly under the ignored `.runs/` of the task's worktree, the directory its handoff names; never in the system's temporary directory, in the scratch directory of a session or in the main checkout of the repository.

## Report

Write the full report to the report path as `task-cycle/change/SKILL.md` gives, with its **Unread material** and **Searches not found or unclear** sections (`none` is an answer). Return the status, the commits, a one-line check result naming what failed or did not run, and the report's path. Return before the review and before the return step; you do not start the next stage.
