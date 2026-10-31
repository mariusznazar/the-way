# Orchestrated mode

When `refine-task` runs in orchestrated mode — a testing-guidelines task of a project plan led by
`lead-project` (WAY-154, WAY-155) — this skill follows that mode's routing. Every question and
every choice shown by its effect go into the conversation turn as `refine-task` routes them, and
the skill ends the turn rather than asking the human. The research agents and the critiques are
requested from the project orchestrator, which starts them, the turn naming the paths of their
reports under `.runs/testing/`. The skill starts no child agent and edits only the task document
and its turn.
