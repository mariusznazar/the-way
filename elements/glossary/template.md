# Glossary entry template

> **Draft.** Every rule below cites the decision that sets it, and every place that waits for a
> decision carries `TODO — decision pending: <question>`. The template reaches the main branch only
> together with the element's examples, skill and guard (WAY-06, WAY-09).

This file defines how a glossary entry is written. A glossary entry gives one word of the foundation
one meaning, so that the same word does not mean one thing in a decision, another in an invariant
and a third in the code (WAY-04). A mechanism keeps the words, never their meaning: a script finds
where a word stands and whether a word to avoid came back, while whether a word is used in its
meaning is judged by an agent, by the panel and by the search of WAY-33 (WAY-97, WAY-99).

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
  in lower case unless the word itself takes a capital. The term identifies the entry, and no other
  entry of the file holds it (WAY-93).
- Terms are a space of their own, apart from the identifiers of the part map, the invariants and the
  environment facts, which share one space (WAY-64, WAY-75). A change that makes a term and such an
  identifier read alike, its hyphens read as spaces — by adding or renaming either — is a warning
  for the panel: where both name the same thing the entry stays, and where they do not, one side is
  renamed. A part of the map whose files include the directory `elements/<identifier>/` answers for
  the element of that name, so a term naming that element, in any of its forms, is no such warning
  (WAY-93).
- Nothing cites a term by an identifier or a fingerprint: an entry of any element depends on a term
  by using its word, and the list of those uses is computed, never written in the entry (WAY-94).
- An entry holds only its current definition, carries no version and is changed in place; earlier
  definitions are read from git (WAY-97).
- The file keeps no list of withdrawn terms. A term renamed becomes a new entry, and the old word
  goes to the new entry's *Avoid* (WAY-93).
- An entry is written in English, whatever language the product shows the people who use it (WAY-72).
  How a word the product shows them in another language stands in an entry is
  `TODO — decision pending: set by the task that meets the first such word; the direction taken is the word quoted with its language, as "przejście"@pl, its definition in English, and its forms from the product's catalogue of strings`.

## Which words take an entry

- A word takes an entry when it stands in the binding part of an entry of the foundation, or in the
  rules of an element's template, and the foundation uses it in more than one meaning, in a meaning
  that is not its everyday English one, or in a meaning new to the product. A word used only in its
  everyday meaning takes none (WAY-95).
- A word the foundation uses both in its everyday meaning and in place of a term either becomes the
  term, its everyday uses rewritten, or keeps its everyday meaning alone, its other uses rewritten
  to the term. It never stands in *Avoid*, and never takes an entry for its everyday meaning alone
  (WAY-95).
- The definition of a word stands in the glossary, not in a decision or a template. A closed list of
  values that a guard reads — the kinds of change of a decision (WAY-20), the verdicts and results of
  a check (WAY-63, WAY-74), the words `none` and `TODO` (WAY-71), the values the gate fills in
  (WAY-61) — stays in its template together with what each value means, and its values take no
  entry (WAY-95).
- An agent finds the candidate words, and the human deciding the change decides which become entries
  and accepts each entry (WAY-95, WAY-10, WAY-14).
- On the main branch every term has a use; on a task branch an entry with no use is a warning, since a
  word may enter before its uses (WAY-95).
- When the process enters a product that already exists, no glossary is written in bulk: a word
  takes an entry with the entries written on entry that stand on it, and later with the return step
  of a task. Candidates an agent finds in the product's documents or in its rule files for agents
  become questions to a human at once, and no list of them is kept (WAY-28).
- The return step looks for words: a word of *Avoid* the change brings back is an error the guard
  reports; a new word in a sentence that binds or in a new identifier the product publishes, and an
  old word in a new meaning, are found by the agent's judgment and by the search of WAY-33 asked for
  them directly, until the task cycle is designed (WAY-11, WAY-33).

## Entry

```markdown
## <term>

<one sentence: the definition>

- **Avoid:** <word> — <what it is confused with> · … | none
- **Not:** <a meaning this word carries elsewhere in the foundation> — <what carries that meaning> | TODO · … | none
```

Every field of the form above appears in every entry, and holds `none` where nothing is there, or
`TODO` where the form gives it (WAY-71).

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
  the decision or the invariant that sets it. A definition carries a rule when, put in place of the
  word in the sentence that sets the rule, it makes part of that sentence say nothing new (WAY-96).
- The definition is the entry's binding part; *Avoid* and *Not* stay outside it. Nothing carries its
  fingerprint: the binding part is what the guard compares with `{fork-point}` to start the review
  of uses below (WAY-94).

## Avoid

- *Avoid* lists the other words for what the term names, each with what it is confused with. A word
  stands there only where every use of it in the foundation carries the term's meaning; a word that
  also has another correct meaning there goes to the *Not* of the entry for that meaning instead.
  The list of uses settles which, never the author's sense of the word (WAY-94, WAY-98).
- A word of *Avoid* is an error where a change, against `{fork-point}`, makes it stand more times in
  a file of `foundations/` or in an element's template, each read whole, than it stood there,
  counting neither text between quotation marks, nor text in backticks, nor a token that is an
  identifier of the part map, the invariants or the environment facts or holds a hyphen, nor the
  glossary's own entries, nor `examples.md`, nor text that a new version of a decision restates word
  for word from the version before it. Rewrapped lines therefore raise nothing (WAY-98).
- The change that puts a word into *Avoid* also searches the elements' skills and README files and
  the code for it, as it searches for the entries that wait for it (WAY-98, WAY-37).
- A word kept out of one kind of sentence only — "main branch" in an invariant's sentence (WAY-60) —
  stays in that element's template, never in *Avoid* (WAY-98).
- A word stands in the *Avoid* of one entry at most, and is no term of the glossary (WAY-98).

## Not

- *Not* names each other meaning the word carries in the foundation, with what carries it: the term
  of another entry of this glossary; the identifier in backticks of an entry of the part map, the
  invariants or the environment facts; a value of a template's closed list in backticks; or, between
  quotation marks, a word the foundation uses outside quotation marks and outside this glossary that
  holds neither the term nor any of its forms (WAY-99).
- Two meanings of one word are removed by renaming one of them wherever the foundation may still be
  edited, never by a note beside the word; *Not* shows the reader which word the other meaning took
  (WAY-99, WAY-04).
- Where a human has not yet chosen the word for the other meaning, *Not* reads `TODO` in place of what
  carries it. A task branch may hold it; the main branch never does (WAY-99, WAY-71).

## Uses and a changed definition

- The uses of a term are the places in the files of `foundations/` and in the elements' templates —
  every version of every entry included — where its word stands, bounded as a word, outside
  backticks, outside a token that holds a hyphen, and outside the span of a longer term of this
  glossary that contains it. Its forms are found by the endings `-s`, `-es`, `-ies`, `-'s`, `-d`,
  `-ed` and `-ing`; a form these endings miss, a short form ("the map" for "part map"), or a verb
  split by its object ("read the value off") is not found, and a field for such forms comes with the
  first term whose review needs it (WAY-97, WAY-94).
- A change to a definition goes, in the same change, through a review of the term's uses: an agent
  puts the new definition in place of the word in every use the guard lists and in every other form
  of it the agent finds, and reports each use whose meaning then moves to the human deciding the
  change (WAY-97).
- A term used by an entry on the main branch keeps its meaning: a new meaning takes a new word and a
  new entry, and whatever should carry it is rewritten (WAY-97).
- A sentence of another entry that speaks of what a term defines uses the term, never a paraphrase of
  its definition, so that the list of uses finds it. A term whose definition holds a word kept out of
  an invariant's sentence (WAY-60) enters such a sentence only where the human deciding the change
  accepts it (WAY-100).

## Fields and their readers

A field stays in this template only while someone or something reads it (WAY-05).

| Field | Who reads it, when | Where its value comes from |
|---|---|---|
| term (heading) | whoever writes an entry of any element; the guard, which finds its uses and compares it with the identifiers of other elements | judgment |
| definition | the agent reviewing the uses when it changes; whoever writes a sentence using the term | prose |
| Avoid | the guard, which counts the word in the files it reads; whoever writes a sentence | judgment for the word; the list of uses for whether it may stand there |
| Not | the agent and the panel judging a change; the guard, which checks that what it names exists | judgment for the meaning; read off for what carries it |

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
- Every term is held by one entry (WAY-93); no word stands in the *Avoid* of two entries, and no word
  of an *Avoid* is a term (WAY-98).
- Every entry carries both fields, `none` or `TODO` only where the form gives it, and no field the
  form does not hold, nor text outside its definition and fields (WAY-71, WAY-94). A `TODO` in *Not*
  is a warning, and, checking a merge onto the main branch, an error (WAY-99, WAY-71).
- Every definition is one sentence, counted as the decision guard counts binding sentences, and holds
  neither *must* nor a word the decision template keeps out of binding sentences (WAY-96).
- Everything *Not* names in backticks, and every term it names, exists; every word it names between
  quotation marks holds neither the term nor its forms and stands outside quotation marks and outside
  the glossary in a file the guard reads (WAY-99).
- No word of *Avoid* stands more times in a file of `foundations/` or in an element's template than
  on `{fork-point}`, outside the text the section on *Avoid* leaves out (WAY-98).
- A change that, against `{fork-point}`, adds or renames a term or an identifier of the part map, the
  invariants or the environment facts so that the two read alike is a warning, save a term naming
  the element that a part whose files include `elements/<identifier>/` answers for (WAY-93).
- A term with no use is a warning, and, checking a merge onto the main branch, an error. Since uses
  count every version of every entry, a term a version on the main branch uses always has one
  (WAY-95).
- For every entry whose definition differs from its definition on `{fork-point}`, the guard lists the
  term's uses: the input of the review above, never a verdict on it (WAY-97).
- No entry carries a version (WAY-97).
- Every example in `examples.md` matches its entry in the file word for word (WAY-05).
- The guard reports what it could not check and why, never agreement (WAY-38), and given the path of
  a record, writes the-way's own record of the run there (WAY-61, WAY-74).

## Examples

Examples live in `examples.md`: entries copied word for word from a real glossary. Until the first
entries are written, only the forms above stand (WAY-05).
