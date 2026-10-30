# Orchestrated mode

When `refine-task` runs in orchestrated mode — a styleguide task of a project plan led by
`lead-project` (WAY-154, WAY-155) — this skill follows that mode's routing. Every question, the
proposal on accessibility and every choice shown through what the user sees go into the
conversation turn as `refine-task` routes them, and the skill ends the turn rather than asking the
human. The research agents and the critiques are requested from the project orchestrator, which
starts them, the turn naming the paths of their reports under `.runs/styleguide/<part>/`. The skill
starts no child agent and edits only the task document and its turn.
