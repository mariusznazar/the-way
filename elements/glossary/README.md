# Glossary

The glossary gives the words a product's rules stand on one meaning each, where they need one, so
that the same word does not mean one thing in a decision, another in an invariant and a third in the code. The glossary of
the-way holds the words of the process; a product's glossary holds the words of its domain and takes
the words of the process from the-way at the commit it pins (WAY-92).

An entry holds its term, one definition and two fields: *Avoid*, other words for what the term names,
and *Not*, other meanings the word carries in the foundation (WAY-94). Nothing cites a term by an
identifier or a fingerprint: a sentence depends on a term by using its word (WAY-94), and a changed
definition goes through a review of the term's uses (WAY-97).

This description grows into the element's template as the element goes through its steps.
`template.md` holds the rules of an entry; the guard that checks entries comes in the element's next
step.

`skill/` holds `record-glossary-term`, a Claude Code skill that writes the entries of a product's
glossary. A product uses the skill from the commit of the-way it pins (WAY-34), linked into the
product's `.claude/skills/` from the pinned copy. For work on the-way itself, link its directory into
the user's skills directory; on Windows:

```powershell
New-Item -ItemType Junction -Path "$HOME\.claude\skills\record-glossary-term" -Target "<the-way>\elements\glossary\skill"
```
