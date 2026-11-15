# What the review looks for in the foundation

Read at step 2 of `SKILL.md`. For each file of the foundation, judge every entry whole and write one
of these results: it holds, a proposal, or a line of one of the two lists of decisions below, the
transitional states and the entries that are no decisions. An entry that holds takes no line beyond
the number of items checked that the tag message gives.

## Decisions

Read each decision's binding sentences, *Rationale* and *Rejected* as a claim about the product and
about how agents and humans work with it, and ask whether the claim still holds against what the
repository shows today: its code and texts, its merged requests since the last review, and what
the remarks of step 3 show. A decision whose reasoning stopped being true needs a proposal, and so
does one that two requests since have applied against each other.

Then list the **weak points** the entries name themselves: every weak point, price, gap, lack and
accepted risk that a *Rationale* or *Rejected* states or a *Based on* quote implies, such as "no
signal while no change brings in a version of it", "costs a review round for each blocked change",
"the sources are private". For each, write one line: the entry, the weak point in the entry's own
words, the product's state today with the place or the command that shows it, and what it means
for the decision — still accepted at this cost, the cost has grown, or the cause is gone.

Run the check a weak point lacks, where it is cheap and by reading alone: it reads files, the
history, a published page or the output of a command that only reports, changes nothing in the
repository, acts on no account or server and costs nothing beyond the reading. Three different
ones: an audit of the lock file for known vulnerabilities, a search of the code for a pattern the
entry says is absent, a read of the published table a fact quotes. A check that needs a running
server, an account, money or a long run is not run: the line names the check that would settle the
weak point and says it was not run, and the proposal for the human says what the check would cost. A
check that only reads is cheap enough to run at every review, where a check that acts would cost
more than the review.

## Decisions that describe a transitional state

Beside the weak points, read each decision's binding sentences for a transitional state of the
product: a state that holds until work later than the change that brought the decision ends it,
such as two forms of one control until the last screen moves to a new library. List each
decision that describes one. The words "until" and kindred ones stand mostly in ordinary rules, so
no search by a word gives the list; it is made by reading. A rule that ends with its own change is
no entry of the log (WAY-36) and gives none. For each, write one line: the decision, the sentence
that describes the state, and what the decision says ends it. Step 6 asks the human at each whether
a task exists that ends the state.

## Entries of the log that are no decisions

Beside the weak points, find at every run all the entries of the decision log that are no decisions,
whole and not a batch of the cheapest ones: the groups of `proposals.md` count them all, and the
human decides which groups go forward. Put each entry through the plan test and the questions of
"Where it goes" in `elements/decisions/template.md`, in the order the template gives them and as it
reads for this repository's log (WAY-293). The first "yes" names the place the entry goes to; an
entry that gets no "yes" is a decision and takes no line. The places:

- a skill or an instruction file — an instruction for how an agent works (question 1);
- the guidelines of a discipline — a rule only for how to write code, tests or the look of the
  product, which carries no choice with a real cost (question 2);
- the product's data or code, with the test that holds it and a comment at the value — a single
  text, number, list or location (question 3);
- no entry — the description of the lack of a feature that no other entry stands on (question 4);
- a sentence of the entry that already answers the question — a part of one question that stands
  under a number of its own (question 5).

A rule that ends with its own change fails the plan test and gets no line here, as it gets none
above (WAY-36). The list is made by reading, as that one is: no search
by a word finds these entries. An entry stands in the log only where someone who does not know the
decision would do otherwise and a test that stops them would not tell them why, so an entry that
carries a choice with a real cost stays a decision whatever it is about. For each entry write one
line: its number, the question that gave the first "yes", the place it goes to and, for question 5,
the entry that takes it; where a test holds a sentence of it by a line `decision:`, say so, since
that line moves with the sentence.

## Environment facts

For each fact, open its source at the address it gives and compare the passage with the fact's
sentence and with its quoted passage (WAY-82): the source that moved, changed or says otherwise
makes a proposal to rewrite or withdraw the fact, and so does a fact no entry rests on any more.
A source that cannot be opened is reported as not checked, never as holding. The date a fact was
read is a date of reading, not a due date, and a fact is not proposed for change for being old.

## Invariants, glossary and the part map

Read each entry against the decisions and against the repository. An invariant marked `Violated:
yes`, whose test still stands as an expected failure, is looked at once: does the violation still
exist, is it cheaper or dearer than the entry says. A glossary entry whose word the repository now
uses in another meaning, a part whose files or dependencies the code no longer follows, and two
entries that collide are proposals. Tests are not run here: the gate runs them.

## What a proposal about the foundation says

Each proposal names the entry, quotes the words that no longer hold, gives the evidence with its
place, and says what to do — change the entry, withdraw it, add the entry that is missing, or
check something that was not run. `proposals.md` gives its form.
