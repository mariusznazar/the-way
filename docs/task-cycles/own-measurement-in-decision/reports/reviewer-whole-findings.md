# Findings of the review of the whole change (c76debc), in the reviewer's words

Source: reports/reviewer-whole-report.md, lines 42-99. Finding 1 blocks; findings 2-5 are Minor, within the task, and are fixed with it (WAY-161).

### Important (blocking, within the task)

**1. `elements/decisions/template.md:54-55` restates WAY-90 differently from the other two texts.**
The new point ends "A measurement whose report a reader can open at an address is quoted like any
other source (WAY-90)." In that template the sentence before it (lines 44-49) separates two kinds of
source: a fact entry named by identifier for a citation whose change would call the decision into
question — "a finding about agents or models" — and "any other source" quoted with its address,
place, passage and date. Read in that frame, "quoted like any other source" puts a measurement with
an open report on the quoting side. WAY-90's own rationale says the opposite: such a measurement "is a
citation like any other, and follows the first sentence", that is, it becomes a fact entry where it
is a finding about agents or models. A decision's author reading only this template would quote a
public report of an experiment with agents, where WAY-90 asks for a fact. The real entry
`shorter-guidelines-trial` in `foundations/environment_facts.md:204` (an open report, a trial of agents) shows
which reading is the right one. `elements/environment-facts/template.md:59-60` words the same point
correctly ("is a citation, and a fact where this section asks for one"), so the two templates say
different things where the task asks for the same (*To do* item 2). Under WAY-263 a restatement that
differs from the entry is Important. Fix: in the decisions template say "is a citation like any
other and follows the point above (WAY-90)" (or the wording of the environment facts template).
Evidence: the three texts above; no other word of the change settles it.

### Minor (within the task)

**2. `foundations/decisions.md` WAY-256 (rationale, near the sentence "estimated before any rebuild
from the word counts of the files of one skill", and *Rejected*, "an estimate of five to fifteen
percent more words read in a typical session, made before any rebuild from the word counts of that
skill's files").** The figure is the product's own estimate from files of a skill the entry does not
name, so a reader cannot recompute or open its record; by WAY-90's rule (a result stays in the prose
and says that it is the product's own and its record is not open) it either carries the sentence or
names the skill. The orchestrator left it unchanged (decision 2); that follows the author's doubt
whether the files are in this repository, but the entry as it stands is the case WAY-90's third
*Verification* group calls a violation ("the same figures stand in the rationale with no word that
the figure is the product's own"). Minor because it is an estimate, not a measurement, and the entry
says it was made before any rebuild. It lies within the task (*To do* item 3: "each decision whose
rationale gives the result of such a measurement"). Fix: add the sentence to the two places, or name
the skill so that a reader can count.

**3. `foundations/decisions.md`, WAY-90 *Rationale* (the new sentences, around line 2092-2102) names no
price and does not meet WAY-17's *Rejected*.** Other entries of the log state the price taken (WAY-229,
255, 320 and others: "The price: …"). This rule has one: a measurement of the product's own agents is
found by no fact search (WAY-33), so when the model it measured is replaced, no entry flags the
decision that rests on it; and WAY-17's *Rejected* turns down "research findings outside the environment
facts" for just that reason. A reader weighing the rule would find the cost named nowhere. Not a
contradiction (WAY-17 speaks of findings of others, which still get a fact), so Minor; one sentence in
the rationale would close it. Within the task.

**4. `foundations/decisions.md` WAY-229 *Rejected* (about line 6951-6954).** Figures of the same
experiment ("5 of the 14 reference errors", "5 and 6 in two such runs", the verdict of a PASS in both
runs) stand in *Rejected* with the sentence only in *Rationale* above. WAY-164 and WAY-364 make the
same measurement say it in the field where the figure stands. I read the *Rationale* sentence ("The
measurement is this product's own…") as covering the whole entry, so I do not block, but a reader of
*Rejected* alone does not see it, and WAY-90 itself says "in the *Rejected* where it weighs a way not
chosen". Minor, within the task; either repeat a short clause in *Rejected* or leave as is.

**5. Formatting of the inserted sentences in `foundations/decisions.md`.** Several inserted clauses
break the wrap of the file and leave one very long line (WAY-353 about line 11836, 145 bytes; WAY-364
about 12255, 135; WAY-350 about 11747, 112; WAY-368 about 12417, 111; WAY-255 about 7956, 110) or a
short orphan line (WAY-368 about 12426-12428: "definition with no body"). No check reads it; it
makes the next diff of those paragraphs noisy. Minor, within the task.
