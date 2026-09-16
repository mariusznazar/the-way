# Decisions

A decision is an active constraint, with its rationale and the options it rejected. Decisions
also carry what the product is for and who it is for, the principles for resolving trade-offs,
and what the product deliberately does not do.

Entries are written according to `template.md`; `examples.md` holds verbatim copies of real
entries.

`skill/` holds `record-decision`, a Claude Code skill that turns a decision into an entry of a
product's log. A product uses the skill from the commit of the-way it pins (WAY-34), linked into
the product's `.claude/skills/` from the pinned copy. For work on the-way itself, link its
directory into the user's skills directory; on Windows:

```powershell
New-Item -ItemType Junction -Path "$HOME\.claude\skills\record-decision" -Target "<the-way>\elements\decisions\skill"
```
