# Environment facts

An environment fact is something true about the world around the product: the platform,
licences, law, browser behaviour. Each fact has a method of checking it. A fact does not
describe the behaviour of the product itself — that is an invariant.

This description grows into the element's template as the element goes through its steps.

`skill/` holds `record-environment-fact`, a Claude Code skill that writes the entries of a
product's environment facts file. A product uses the skill from the commit of the-way it pins
(WAY-34), linked into the product's `.claude/skills/` from the pinned copy. For work on the-way
itself, link its directory into the user's skills directory; on Windows:

```powershell
New-Item -ItemType Junction -Path "$HOME\.claude\skills\record-environment-fact" -Target "<the-way>\elements\environment-facts\skill"
```
