# Glossary entry template

> **Draft.** Every rule below cites the decision that sets it, and every place that waits for a
> decision carries `TODO — decision pending: <question>`. The template reaches the main branch only
> together with the element's examples, skill and guard (WAY-06, WAY-09).

This file defines how a glossary entry is written. A glossary entry gives one word of the foundation
one meaning, so that the same word does not mean one thing in a decision, another in an invariant
and a third in the code (WAY-04). A mechanism keeps the words, never their meaning: a script finds
where a word stands and whether a word to avoid came back, while whether a word is used in its
meaning is judged by an agent, by the panel and by the search of WAY-33 (WAY-33, WAY-98, WAY-100).

`{fork-point}` below is the commit the task branch left the main branch from, a value the gate fills
in (WAY-61).

## Two glossaries

- The glossary of the-way holds the words of the process — what its templates, decisions and entries
  name. A product's glossary holds the words of its domain. In the-way, whose product is the process,
  the two are one file (WAY-92).
- A product takes the words of the process from the-way at the commit it pins, and its glossary
  defines none of them again. Its guard does not read the-way's glossary yet; that comes with the
  first entry of a product's glossary (WAY-92).

## Where entries go

- A product's glossary entries stand in one file, `foundations/glossary.md`, which opens with a title
  and a paragraph saying what it holds (WAY-93).
- An entry is headed by its term: the word or words as the foundation writes them in running text,
  in lower case unless the word itself takes a capital, in its base form — a noun in the singular, a
  verb bare. The term identifies the entry, and no other entry of the file holds it (WAY-93).
- Terms are a space of their own, apart from the identifiers of the part map, the invariants and the
  environment facts, which share one space (WAY-64, WAY-75). A term and such an identifier read alike
  when they match with the hyphens of both read as spaces. A change that makes them read alike,
  by adding or renaming either, is a warning for the panel: where both name the same thing the entry
  stays, and where they do not, one side is renamed (WAY-93).
- A part of the map whose files include the directory `elements/<identifier>/` answers for the
  element of that name, so a term naming that element, in any of its forms, raises no such warning
  (WAY-93).
- Nothing cites a term by an identifier or a fingerprint: an entry of any element depends on a term
  by using its word, and the list of those uses is computed, never written in the entry (WAY-94).
- An entry holds only its current definition, carries no version and is changed in place; earlier
  definitions are read from git (WAY-97).
- The file keeps no list of withdrawn terms. A term renamed becomes a new entry. Its old word goes to
  the new entry's *Avoid* where no other meaning keeps it; where one does, the *Not* of that meaning's
  entry names the new term. Both are done wherever the foundation may still be edited (WAY-93,
  WAY-98, WAY-99).
- An entry is written in English, whatever language the product shows the people who use it and
  whatever language its team speaks (WAY-72). How a word the product shows them in another language
  stands in an entry is `TODO — decision pending: how does a word the product shows in another language stand in a glossary entry? (WAY-72)`.

## Which words take an entry

- A word takes an entry when it stands in the binding part of an entry of the foundation or in the
  rules of an element's template, and at least one of its uses carries a meaning a reader who knows
  the product's field would not give it. A word whose every meaning is one such a reader gives takes
  none, however many meanings it has — "run", for a command and for text running across lines
  (WAY-95).
- Two uses carry two meanings when a definition true of one is false of the other. A noun naming one
  occurrence of what its verb does, or what does it — a run, to run; a probe, to probe — carries the
  verb's meaning; any other noun and verb of one word are weighed by the same test (WAY-95, WAY-99).
- A word naming what a kind of foundation entry records names the entry or entries that record it
  too, and carries one meaning: its definition says what the thing is, and that the foundation holds
  an entry for it stays in the decision that sets it (WAY-95).
- A word the foundation uses both in its everyday meaning and in place of a term, or of the term the
  change writes, either becomes the term, its everyday uses rewritten, or keeps its everyday meaning
  alone, its other uses rewritten to the term — wherever the foundation may still be edited. It never
  stands in *Avoid*, and never takes an entry for its everyday meaning alone (WAY-95, WAY-99).
- The definition of a word stands in the glossary, not in a decision or a template. A closed list of
  values that a guard reads — the kinds of change of a decision (WAY-20), the verdicts and results of
  a check (WAY-63, WAY-74), the words `none` and `TODO` (WAY-71), the values the gate fills in
  (WAY-61) — stays in its template together with what each value means, and its values take no
  entry (WAY-95).
- Where a binding sentence says what a term is, the entry takes that, and the sentence keeps what is
  required of the thing, using the term. The change that writes the entry rewrites the sentence: a
  correction before the main branch, a new version after it (WAY-95, WAY-100).
- An agent finds the candidate words, and the human deciding the change decides which become entries
  and accepts each entry (WAY-95, WAY-10, WAY-14).
- On the main branch every term has a use outside the glossary; on a task branch an entry with no
  such use is a warning, since a word may enter before its uses (WAY-95).
- When the process enters a product that already exists, no glossary is written in bulk: a word
  takes an entry together with the entries written when the process enters it that stand on it, and
  later with the return step of a task. Candidates an agent finds in the product's documents or in
  its rule files for agents become questions to a human at once, and no list of them is kept
  (WAY-28).
- In the return step, a new word in a binding sentence or in a new identifier the product publishes
  is found by the agent's judgment, and an old word in a new meaning by the search of WAY-33 asked for
  it, until the task cycle is designed; a word of *Avoid* the change brings back is an error the
  guard reports (WAY-11, WAY-98).

## Entry

```markdown
## <term>

<one sentence: the definition>

- **Avoid:** <word> — <what a reader takes it for instead, or "same thing" for a synonym> · … | none
- **Not:** <meaning> — <what carries it, or TODO> · … | none
```

Every field of the form above appears in every entry. `none` stands for a whole field with nothing
in it; `TODO` stands only in *Not*, in place of what carries a meaning (WAY-71, WAY-99).

## The definition

- The definition is one sentence in the present tense, with no normative word: neither *must* nor
  any word the decision template keeps out of binding sentences (WAY-96).
- A noun is defined as "<term> is <genus> that <difference>", with or without an article; a verb or
  an adjective as "<subject> is <term> when <condition>" (WAY-96).
- The genus is never a term of this glossary used in another meaning than its entry gives it. Where
  two terms name neighbouring things, the definition of one uses the other as its genus or in its
  difference — "A result is a verdict, or `error` where …" — so that the uses of either find the
  relation (WAY-96).
- The definition says what the word means, never a rule about the thing it names: the rule stays in
  the decision or the invariant that sets it. A definition carries a rule when it holds something
  the decision or invariant setting it could change while the word went on naming the same thing
  (WAY-96).
- The definition is the entry's binding part; *Avoid* and *Not* stay outside it. Nothing carries its
  fingerprint (WAY-94).

## Avoid

- *Avoid* lists the other words for what the term names, each with what a reader takes it for. A
  word stands there only where every use of it in the files of `foundations/` and the elements'
  templates carries the term's meaning; a word
  that also has another correct meaning there goes to the *Not* of the entry for that meaning
  instead. The list of uses settles which, never the author's sense of the word (WAY-94, WAY-98).
- A word of *Avoid* is an error where a change makes it stand more times in a file of `foundations/`
  or in an element's template, each read whole, than it stood there on `{fork-point}`. The word is
  counted in any letter case, with the endings the section on uses gives. Rewrapped lines therefore
  raise nothing (WAY-98).
- The count leaves out what a use of a term leaves out (the section on uses), text between quotation
  marks, an identifier of the part map, the invariants or the environment facts standing in a field's
  value, the glossary's own entries, and text that a new version of a decision restates word for word
  from the version before it, compared sentence by sentence, each item of a list read as a paragraph
  of its own (WAY-98).
- The change that puts a word into *Avoid* also searches the elements' skills and README files and
  the code for it, as it searches for the entries that wait for it (WAY-98, WAY-37).
- A word kept out of one kind of sentence only — "main branch" in an invariant's sentence (WAY-60) —
  stays in that element's template, never in *Avoid* (WAY-98).
- A word stands in the *Avoid* of one entry at most, and is no term of the glossary (WAY-98).

## Not

- *Not* names each meaning the word carried or carries in the files of `foundations/` and the
  elements' templates, besides its definition and a meaning a reader who knows the product's field
  gives it, with what carries it now: the term of another entry of this glossary; the identifier in backticks
  of an entry of the part map, the invariants or the environment facts; in backticks, a value of a
  template's closed list as that template writes it; or, between quotation marks, a word the
  foundation uses, as the section on uses bounds a use, outside quotation marks and outside this
  glossary. No carrier holds the term or any of its forms, the hyphens of both read as spaces
  (WAY-99).
- Where a word carries two meanings and one of them is a meaning a reader who knows the product's
  field would not give it, one of the two is renamed wherever the text may still be edited, never
  marked by a note beside the word; *Not* shows the reader which word the other meaning took. Two
  meanings such a reader gives the word both need no renaming (WAY-99, WAY-04).
- The uses of a meaning such a reader would not give the word are rewritten, when it moves, to one
  word, the one *Not* names; a paraphrase is no renaming (WAY-99).
- Where a human has not yet chosen the word for the other meaning, *Not* reads `TODO` in place of what
  carries it. A task branch may hold it; the main branch never does (WAY-99, WAY-71).

## Uses and a changed definition

- The uses of a term are the places in the files of `foundations/` and in the elements' templates —
  every version the files hold included, and of the glossary only the definitions of other entries —
  where its word stands, bounded as a word. Left out are text in backticks or a fenced block, a token holding a hyphen the term does not
  hold, a token holding `/`, the span of a longer term of this glossary that contains it, a field's
  name, and the values of *Scope*, *Part* and *Change* (WAY-97).
- Its forms are found by the endings `-s`, `-es`, `-ies` in place of a final `y`, `-'s`, `-d`, `-ed`
  and `-ing`, a final consonant doubled before the last two; a multi-word term takes the ending on its
  last word. A form these endings miss, a short form ("the map" for "part map"), or a verb split by
  its object ("read the value off") is not found, and a field for such forms comes with the first
  term whose review needs it (WAY-97, WAY-94).
- A term's last word standing for the whole term — "fact" for "environment fact", "the map" for
  "part map" — is a use of the term that the list of uses does not show and the review of uses looks
  for; it stands in no *Avoid*. Where the files also use that word in another meaning, the choice for
  a word used both in its everyday meaning and in place of a term applies: its other uses are
  rewritten, or its uses for the term are written as the whole term (WAY-94, WAY-95).
- A change to a definition goes, in the same change, through a review of the term's uses: an agent
  puts the new definition in place of the word in every use the guard lists and in every other form
  of it the agent finds, and reports each use whose meaning then moves to the human deciding the
  change (WAY-97).
- A term used by an entry on the main branch keeps its meaning: a new meaning takes a new word and a
  new entry, and whatever should carry it is rewritten (WAY-97).
- Any sentence of another entry, its rationale included, that speaks of what a term defines uses the
  term, never a paraphrase of its definition, so that the list of uses finds it. A term whose
  definition holds a word an invariant's sentence may not hold (WAY-60) enters such a sentence only
  where the human deciding the change accepts it (WAY-100).

## Fields and their readers

A field stays in this template only while someone or something reads it (WAY-05).

| Field | Who reads it, when | Where its value comes from |
|---|---|---|
| term (heading) | whoever writes an entry of any element; the guard, which finds its uses and compares it with the identifiers of other elements | judgment |
| definition | the agent reviewing the uses when it changes; whoever writes a sentence using the term; the guard, which counts its sentences and words and compares it with `{fork-point}` | prose |
| Avoid | the guard, which counts the word in the files it reads; whoever writes a sentence | judgment for the word; the list of uses for whether it may stand there |
| Not | the agent and the panel judging a change; the guard, which checks that what it names exists | judgment for the meaning and the word chosen; read off for whether it exists |

A field marked *judgment* holds someone's call: no tool reads its value off the product, and no
question about a fact settles it. A reader takes such a value as a call, not as a reading (WAY-54).
A field marked *prose* carries text rather than a value.

## What the format guard checks

- The product has exactly one file of glossary entries: the file checked stands in
  `foundations/glossary.md` from the root of its repository, letter case included, as git lists it,
  and no other Markdown file git tracks holds an entry — a section `## <term>` carrying an *Avoid*
  field, outside a fenced block — save `examples.md` beside this template, which holds copies
  (WAY-93).
- The file holds a title, the paragraph under it and its entries in the form above, and no other
  heading (WAY-93).
- No term heads two entries (WAY-93); no word stands in the *Avoid* of two entries, and no word of an
  *Avoid* is a term, or a word a *Not* names (WAY-98).
- Every entry carries both fields, `none` or `TODO` only where the form gives it, and no field the
  form does not hold, nor text outside its definition and fields (WAY-71, WAY-94). A `TODO` in *Not*
  is a warning, and, checking a merge onto the main branch, an error (WAY-99, WAY-71).
- Every definition is one sentence, counted as the decision guard counts binding sentences: text in
  backticks counts as one word beginning with a capital, and a sentence ends at `.`, `!` or `?`
  followed by white space and a capital letter, `"`, `'` or `(`, or at the end of the text. Outside
  backticks it holds neither *must* nor a word the decision template keeps out of binding sentences
  (WAY-96).
- Everything *Not* names in backticks, and every term it names, exists; nothing it names holds the
  term or its forms; every word it names between quotation marks is used, as the section on uses
  bounds a use, outside quotation marks and outside the glossary in a file of `foundations/` or in an
  element's template (WAY-99).
- No word of *Avoid* stands more times in a file of `foundations/` or in an element's template than
  on `{fork-point}`, outside the text the section on *Avoid* leaves out (WAY-98).
- A change that, against `{fork-point}`, adds or renames a term or an identifier of the part map, the
  invariants or the environment facts so that the two read alike is a warning, save a term naming
  the element that a part whose files include `elements/<identifier>/` answers for (WAY-93).
- A term with no use outside the glossary is a warning, and, checking a merge onto the main branch,
  an error (WAY-95).
- No entry carries a version (WAY-97).
- Every example in `examples.md` matches its entry in the file word for word (WAY-05).
- The guard's report lists, for every entry whose definition differs from its definition on
  `{fork-point}`, the term's uses: the input of the review of uses, never a verdict on it (WAY-97).
- The guard reports what it could not check and why, never agreement (WAY-38).
- Given the path of a record, the guard writes the-way's own record of the run there, with a
  verdict for each invariant its checks cite (WAY-61, WAY-74); given `none` as either commit, it
  records the checks that need that commit as `unchecked`; a call to git that fails, the file
  standing outside a git repository included, is a failure of the run, never an unchecked check
  (WAY-61, WAY-63).
- Given a word in place of the options, the guard lists its uses as the section on uses bounds them
  and checks nothing: the list that settles whether a word may stand in *Avoid* (WAY-98).

## Examples

Examples live in `examples.md`: entries copied word for word from a real glossary. Until the first
entries are written, only the forms above stand (WAY-05).
