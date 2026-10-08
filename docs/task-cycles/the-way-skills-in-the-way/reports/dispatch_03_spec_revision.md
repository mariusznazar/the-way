Spec revision request from the orchestrator (step 7 resolution). Same dispatch contract as before: you write only
`spec.md`; return your report as text; return before `writing-plans`.

The spec review is at `C:\Storage\repos\the-way-skills-self\.runs\task-cycles\the-way-skills-in-the-way\reports\report_02_spec_review.md`.
Read it in full. Revise `spec.md` under these orchestrator rulings (provisional, under Mariusz's delegation; none
of them is his approval):

R1 (finding 1, adopt). Entry point text stays tool-neutral and byte-identical in both copies. The product guard
runs `git -C <the directory that holds this entry point> rev-parse --show-superproject-working-tree`; the process
root is `git rev-parse --show-toplevel` run in the directory the session was started in (its project or working
directory), not the shell's current directory. Add the line telling the agent to skip any instruction in the skill
to resolve a link to find the-way. Rewrite §6. Use the same "session start directory" wording in §4.3. Decide
whether the guard's reliance on the agent knowing its entry point's own path needs a fact (WAY-90): if a page of
either tool states it, name the fact; if not, state the gap in the failure mode instead of inventing a fact.

R2 (finding 2, adopt with this route). Follow WAY-30 for point 5: the branch delivers the task as written — `## Backlog`
in `AGENTS.md` with the vault path of `_tasks_active.md` and the `_zadania/` folder linked from each task line — and
carries on the task branch a proposed new wording of WAY-27 (an exception written into its binding sentence for the
backlog place a root `AGENTS.md` names under WAY-107) and the matching sentence of `outbound-link-reach`, edited in
place (pre-main, WAY-07), with every fingerprint reference to WAY-27 renewed (WAY-31). Choose between that exception
and a `narrows` relation from WAY-107 (WAY-25 form) and give your reason; prefer the smaller change of meaning. The
request will be a blocked draft holding the question for Mariusz, with the alternative (no path in the section, or
no section, point 5 not met) and the orchestrator's recommendation. Remove the personal-instructions edit from §4.7
entirely (it goes to process remarks, not the request).

R3 (finding 3, adopt). Edit WAY-09 in place to name `.claude/skills/` and `.agents/skills/` as files of the
`agent-instructions` part (the entry points), renew its fingerprint in every reference (WAY-31). Same blocked draft,
second question. Drop the "root entry points" argument.

R4–R6 (findings 4, 5, 6, adopt). `Part: every`, `Derives from: WAY-127@<fingerprint>`, `Correction: none`; the
control test is a control of `problems()`, the deliberate break stays with the code reviewer (WAY-69); facts as
separate entries per WAY-76, shaped after `claude-code-path-rules`, checks called watches, sources with archived
copies where one exists (state where none could be found).

R7–R11 (minor findings, adopt). Criterion 2 reworded; §2 local-path sentence corrected; sibling-order parenthesis
dropped; §4.6 states the WAY-48 adversarial-input position for the installer sentence change (a string-only change
of generated text takes no new input — say so, and list the existing installer tests that still cover its inputs);
§4.7 adds a Codex check and replaces `-ErrorAction Stop` with a check-and-continue.

Also: list in §7 every foundation entry the task writes or changes after these rulings, each with one sentence of
meaning, and mark which ones change the meaning of an approved decision (these are the request's questions).
Return a short summary of the revision (under 300 words) and the list of changed sections.
