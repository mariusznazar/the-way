# Invariants

An invariant is a rule the product has to keep. Each invariant carries its method of checking
and the current result of running it (WAY-08), and names the environment facts it rests on
(WAY-17).

This description grows into the element's template as the element goes through its steps.

`skill/` holds `record-invariant`, a Claude Code skill that writes the entries of a product's
invariants file. A product uses the skill from the commit of the-way it pins (WAY-34), linked into
the product's `.claude/skills/` from the pinned copy. For work on the-way itself, link its
directory into the user's skills directory; on Windows:

```powershell
New-Item -ItemType Junction -Path "$HOME\.claude\skills\record-invariant" -Target "<the-way>\elements\invariants\skill"
```
