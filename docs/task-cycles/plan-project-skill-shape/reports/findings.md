# Blocking findings of the review of db3845c, in the reviewer's words

From [review.md](review.md). W and C are the worktree and the cycle's directory.

### 1. What the sentence that has `read.md` read does to step 1 is stated two opposite ways, and routes 3 and 6 are counted on the reading the task rejected

**Anchors:** `W/project-level/plan/skill/existing_plan.md:15-16`,
`W/project-level/plan/skill/SKILL.md:48-49`, `C/reports/assessment.md:81`,
`C/reports/word-counts.md:8`, `:18`, `:22`, `:33`, `:139`, `:322`. Slice: none (one author, no plan).

**To paste:** The assessment says that the last bullet of `existing_plan.md` "does not make step 1
run", while routes 4, 5a and 7 count step 1 as run although `SKILL.md` step 1 is switched off for
every session that passed that bullet. Say what the sentence does, and count routes 3 and 6 by that.

**Why I report it:**

What the sentence is for. The task's question 3 chose the pointer to `read.md` so that a session on
an existing plan keeps what all sessions do today. The way it turned down reads: "po cichu wyłącza
to, co dziś robią wszystkie sesje; agent zmienia plan bez fundamentu w głowie, a jedyną ochroną
zostaje `plan_check.py`". The same answer records `readiness_check.py` run in 14 of 14 sessions and
`foundations/` reached in 11 of 14.

The mechanism. The rebuilt files give one instruction, "reads it", and the materials give it two
effects:

- Routes 3 and 6: the session reads `read.md` and does none of it. `assessment.md:81`: "it does not
  make step 1 run (the readings of step 1 are done only where step 1 runs)".
  `word-counts.md:139`: "step 1 is not run (its file is read, as existing_plan.md has it, so the
  foundation and the guidelines are not read)". `:322` says the same of route 6.
- Routes 4, 5a and 7: step 1 runs, with the foundation and the guidelines counted. But on these
  routes too the session passed the same bullet at step 0, so `SKILL.md:48-49`, "Read `read.md` ...
  each unless step 0 had you read it", gives it nothing to do at step 1. That pointer is the whole
  of step 1 in `SKILL.md`. If reading `read.md` at step 0 does not carry it out, then nothing on
  these routes carries it out, and "the plan is checked against it from step 1"
  (`existing_plan.md:9`) has an empty step behind it. In the base, reaching step 1 meant its four
  bullets.

So the two claims cannot both hold:

- If "reads" means reads and carries out, as every other "Read `<file>`" pointer of `SKILL.md`
  means, the skill's text is consistent: step 0 carries `read.md` out and step 1 rightly skips it.
  Then `assessment.md:81` is false, and routes 3 and 6 reach the section "Reading the foundation"
  (492 words) and `product-guidelines/reading.md` (1141), which question 4 counts "tam, gdzie droga
  do nich dochodzi".
- If "reads" means sees and does not carry out, as the materials say of routes 3 and 6, those routes
  are the outcome question 3 turned down (a plan changed with no foundation in mind), and on routes
  4, 5a and 7 no pointer has the readiness check or the foundation run.

The figures, routes 3 and 6, totals with the files read beside the skill:

| Route | Stated before | Stated after | Stated change | After, step 1 counted | Before as stated | Before, step 1 counted too |
|---|---|---|---|---|---|---|
| 3 | 5264 | 4867 | -7.5% | 6500 | +23.5% | 6897, so -5.8% |
| 6 | 5852 | 5236 | -10.5% | 6869 | +17.4% | 7485, so -8.2% |

The absolute saving stays the same (397 and 616 words) only where both states count step 1, and the
recorded sessions argue for counting both: 14 of 14 ran the readiness check though the base's text
sent no resumed draft to step 1. Counted in the state "after" alone, the sign turns. Either way the
stated range "-10.5% to +9.4%" (`word-counts.md:33`, repeated in `author.md:51`) is not what the
request may carry as it stands, and the task's "ok. 170 słów na każdej drodze z istniejącym planem"
is the file alone, not what the sentence sets off.

The author raised this as concern 3 and kept the task's word "czyta". Grade and scope are mine: the
task requires each new sentence to be compared by what it selects and switches off, and this line
of the materials names an effect the text does not give. It is within To do 5, To do 8 and the
second acceptance criterion. A rationale in the report does not lower it.

Fix, recommended: keep the skill's text, which is consistent on the first reading; correct
`assessment.md:81` to say that the session carries `read.md` out; state in `word-counts.md` the rule
and routes 3 and 6 with step 1 counted, in both states, giving the figure for the literal base
beside it; correct the comparison paragraph and `author.md`'s route notes the request draws on.
Precedent for the plain wording, should the orchestrator want the sentence itself unmistakable: the
sentence WAY-266 has the guidelines skills carry says "goes through `refine-task` steps 1 and 2
first" (`W/product-guidelines/testing/SKILL.md:79-81`). If the orchestrator rules for the second
reading instead, `SKILL.md:48-49` has to change, so that a session that goes on from step 1 carries
out the file it already read.

Left as it is: the request tells the human that a resume and a hand-over turn get cheaper by 7.5%
and 10.5% and that step 1 does not run there, while agents will run it as they do today; the human
then reads the first real run (task question 5) against a wrong baseline.
