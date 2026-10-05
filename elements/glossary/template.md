# Glossary entry template

This file defines how a glossary entry is written. A glossary entry gives one word of the foundation
one meaning, so that the same word does not mean one thing in a decision, another in an invariant
(WAY-94, WAY-99) and a third in the code (`TODO — decision pending: which decision sets that a
term of a product's glossary keeps its meaning in the product's code`); a word the glossary of
the-way holds keeps its domain meaning in a product's code (WAY-104). A mechanism keeps the words,
never their meaning: a script finds where a word stands and whether a word to avoid came back, while
whether a word is used in its meaning is judged by an agent, by the independent assessment and by the search of
WAY-33 (WAY-97, WAY-98, WAY-10, WAY-33).

The rules of form the elements share — the language of an entry, every field and the words `none`
and `TODO`, a sentence using a term rather than a paraphrase of its definition, and the marks of
where a value comes from — stand in `elements/common/rules.md`; this template holds what is
particular to a glossary entry (WAY-35).

## Two glossaries

- The glossary of the-way holds the words of the process — what its templates, decisions and
  entries name. A product's glossary holds the words of its domain. In the-way, whose product is
  the process, the two are one file (WAY-95).
- A product takes the words of the process from the-way at the commit it pins, and its glossary
  defines none of them again (WAY-95). That the glossary guard reports an entry of a product's
  glossary defining one of them or the last word of one, or listing either in its *Avoid*, answers
  to the invariant `glossary-process-terms`.
- A word of the product's domain that the glossary of the-way holds, or the last word of a term
  it holds, in any of its forms, is written in the product's foundation with a qualifier — "game
  clock" for "clock", or "assembly step" for "step", the last word of "return step". The bare word
  there keeps the meaning of the process. The qualified word takes an entry only as "Which words
  take an entry" says. The *Avoid* of an entry of the product's glossary holds such a word only
  with a qualifier: the entry "match timer" may list "match clock", never "clock", and the entry
  "lab result" may list "lab test", never "test", the last word of "invariant test". The
  product's code, its interface and talk about the product use the word of the domain unchanged
  (WAY-104).

## Where entries go

- A product's glossary entries stand in one file, `foundations/glossary.md`, which opens with a
  title and a paragraph saying what it holds (WAY-93).
- An entry is headed by its term: the word or words as the foundation writes them in running text
  (WAY-93), in lower case unless the word itself takes a capital, in its base form — a noun in the
  singular, a verb bare (`TODO — decision pending: which decision sets the letter case and the form
  of a term`). The term identifies the entry, and no other entry of the file holds it (WAY-93).
- Terms are a space of their own, apart from the identifiers of the part map, the invariants and the
  environment facts, which share one space (WAY-64, WAY-93). A change that makes a term read
  like such an identifier, by adding or renaming either, is a warning for the independent assessment: where both name
  the same thing the entry stays, and where they do not, one side is renamed (WAY-93, WAY-10). A
  term and an identifier read alike when they match with the hyphens of both read as spaces
  (`TODO — decision pending: which decision sets that hyphens read as spaces when a term is compared
  with an identifier or a carrier`).
- Nothing cites a term by an identifier or a fingerprint: a sentence depends on a term by using its
  word (WAY-94), and an entry carries no version and is edited in place (WAY-97); the file keeps no
  list of withdrawn terms (`TODO — decision pending: which decision sets that the glossary keeps no
  list of withdrawn terms`).
- A term renamed becomes a new entry. Its old word goes to the new entry's *Avoid* where no other
  meaning keeps it; where one does, the *Not* of that meaning's entry names the new term. Both are
  done wherever the foundation may still be edited (WAY-93, WAY-94, WAY-98, WAY-99).
- The language of an entry follows `elements/common/rules.md` (WAY-72). How a word the product
  shows the people who use it in another language stands in an entry is
  `TODO — decision pending: how does a word the product shows in another language stand in a
  glossary entry? (WAY-72)`.

## Which words take an entry

- A word takes an entry when it stands in the binding part of an entry of the foundation or in the
  rules of an element's template or of the part the elements share, and at least one of its uses
  carries a meaning a reader who knows the product's field would not give it. A word whose every
  meaning is one such a reader gives takes none, however many meanings it has — "run", for a
  command and for text running across lines (WAY-95).
- Two uses carry two meanings when a definition true of one is false of the other. A noun naming one
  occurrence of what its verb does, or what does it — a run, to run; a probe, to probe — carries the
  verb's meaning; any other noun and verb of one word are weighed by the same test
  (`TODO — decision pending: which decision sets when two uses of a word carry two meanings`).
- A word naming what a kind of foundation entry records names the entry that records it too, in one
  meaning (`TODO — decision pending: which decision sets that a word naming what a kind of entry
  records names the entry too, in one meaning`); a word naming what a rule computes keeps the
  meaning a reader of the field gives it (`TODO — decision pending: which decision sets that a word
  naming what a rule computes keeps the meaning a reader of the field gives it`). Either is defined
  by what the thing is; how the foundation records or computes it stays in the decision that sets
  it, and a definition holding it carries a rule, as the section on the definition tests (WAY-96).
- Where a word carries two meanings in the files its uses are searched in, and one of them is a
  meaning a reader who knows the product's field would not give it, one of the two is renamed
  wherever those files may still be edited, never marked by a note beside the word, and the uses of
  the meaning that moves are rewritten to one word, the one *Not* names; a paraphrase is no
  renaming. Two meanings such a reader gives the word both need no renaming (WAY-99). So a word the
  foundation uses both in its everyday meaning and in place of a term, or of the term the change
  writes, either becomes the term, its everyday uses rewritten, or keeps its everyday meaning alone,
  its other uses rewritten to the term (WAY-99); it never stands in *Avoid* (WAY-98), and never
  takes an entry for its everyday meaning alone (WAY-95). In a product, none of this applies to a
  word of its domain that the glossary of the-way holds: the word is written as "Two glossaries"
  says, and the entry of the word in the glossary of the-way records no *Not* for its meaning of the
  domain (WAY-104).
- The definition of a word stands in the glossary, not in a decision or a template. A closed list of
  values that a guard reads stays in its template together with what each value means, and its
  values take no entry (WAY-95).
- Where a binding sentence says what a term is, the entry takes that, and the sentence keeps what is
  required of the thing, using the term. The change that writes the entry rewrites the sentence: an
  edit before the main branch, a new version after it (WAY-95, WAY-97, WAY-19).
- An agent finds the candidate words, and the human deciding the change decides which become entries
  and accepts each entry (WAY-95, WAY-10).
- On the main branch every term has a use outside the glossary (WAY-95); on a task branch an entry
  with no such use is a warning, since a word may enter before its uses
  (`TODO — decision pending: which decision lets a task branch hold a term with no use`).
- When the process enters a product that already exists (WAY-28), no glossary is written in bulk: a
  word takes an entry together with the entries written when the process enters it that stand on
  it, and later with the return step of a task. Candidates an agent finds in the product's documents
  or in its rule files for agents become questions to a human at once, and no list of them is kept
  (`TODO — decision pending: which decision sets how glossary entries are written when the process
  enters a product that already exists`).
- In the return step, a new word in a binding sentence or in a new identifier the product publishes
  is found by the agent's judgment, and an old word in a new meaning by the search of WAY-33 asked
  for it (WAY-11, WAY-33); a word of *Avoid* the change brings back is an error the guard reports
  (WAY-98). That the change holds, in one of its commits, the record of its task's return step
  answers to the invariant `return-step-record`.

## Entry

```markdown
## <term>

<one sentence: the definition>

- **Avoid:** <word> — <what a reader takes it for instead, or "same thing" for a synonym> · … | none
- **Not:** <meaning> — <what carries it, or TODO> · … | none
```

`none` stands for a whole field with nothing in it; `TODO` stands only in *Not*, in place of what
carries a meaning (WAY-71, WAY-99). The rest of the rule on `none` and `TODO`, every field in every
entry among it, stands in `elements/common/rules.md` (WAY-71).

## The definition

- The definition is one sentence in the present tense, with no normative word: neither *must* nor
  any word the decision template keeps out of binding sentences (WAY-96).
- A noun is defined as "<term> is <genus> that <difference>", with or without an article; a verb or
  an adjective as "<subject> is <term> when <condition>" (WAY-96).
- The genus is never a term of this glossary used in another meaning than its entry gives it. Where
  two terms name neighbouring things, the definition of one uses the other as its genus or in its
  difference — "A result is the value reported for an entry on one commit: the verdict that counts
  for it there, or …" — so that the uses of either find the relation (WAY-96).
- The definition says what the word means, never a rule about the thing it names: the rule stays in
  the decision or the invariant that sets it. A definition carries a rule when it holds something
  the decision or invariant setting it could change while the word went on naming the same thing
  (WAY-96).
- The definition is the entry's binding part; *Avoid* and *Not* stay outside it. Nothing carries its
  fingerprint (WAY-94).

## Avoid

- *Avoid* lists the other words for what the term names, each with what a reader takes it for
  (WAY-94). A word stands there only where every use of it in the files of `foundations/`, the
  elements' templates and the part the elements share carries the term's meaning; a word that also
  has another correct meaning there goes to the *Not* of the entry for that meaning instead. The
  list of uses settles which, never the author's sense of the word (WAY-98, WAY-99). Of the part
  the elements share, its Markdown files alone are read
  (`TODO — decision pending: which decision sets that only the Markdown files of the part the
  elements share are searched`).
- A word of *Avoid* is an error where a change makes it stand more times in such a file, each read
  whole, than on the commit the task branch left the main branch from; what WAY-98 does not count
  is left out, and the guard's code and tests hold how each of it is found (WAY-98). In a product, a
  file of the-way is counted by its path in the-way at two commits of the-way, the one pinned on
  the commit the task branch left the main branch from and the one the product pins now, both read
  from the history of the-way, never from its files on disk; where that commit pins none, the files
  of the-way are left `unchecked` and the product's own files are still counted (WAY-34, WAY-63,
  WAY-98).
- The change that puts a word into *Avoid* also searches the elements' skills, the root
  `README.md` and the code for it, as it searches for the entries that wait for it
  (`TODO — decision pending: which decision sets that a change putting a word into Avoid searches
  the skills, the root README.md, the code and the entries that wait for the word`).
- A word kept out of one kind of sentence only — "main branch" in an invariant's sentence (WAY-60) —
  stays in that element's template, never in *Avoid*, which holds other words for what a term names
  (WAY-94).
- A word stands in the *Avoid* of one entry at most, and is no term of the glossary
  (`TODO — decision pending: which decision sets that a word stands in one Avoid at most and is no
  term`).

## Not

- *Not* names each meaning the word carried or carries in the files of `foundations/`, the elements'
  templates and the part the elements share — of which its Markdown files alone are read
  (`TODO — decision pending: which decision sets that only the Markdown files of the part the
  elements share are searched`) — besides its definition and a meaning a reader who knows the
  product's field gives it, with what carries it now: the term of
  another entry of this glossary; the identifier in backticks of an entry of the part map, the
  invariants or the environment facts; in backticks, a value of a template's closed list as that
  template writes it; or, between quotation marks, a word used, as WAY-98 counts a use, outside
  quotation marks and outside this glossary. No carrier holds the term or any of its forms (WAY-94,
  WAY-99), the hyphens of both read as spaces (`TODO — decision pending: which decision sets that
  hyphens read as spaces when a term is compared with an identifier or a carrier`).
- Where a human has not yet chosen the word for the other meaning, *Not* reads `TODO` in place of
  what carries it. A task branch may hold it; the main branch never does (WAY-99, WAY-71).

## Uses and a changed definition

- The uses of a term are the places in the files of `foundations/`, the elements' templates and the
  Markdown files of the part the elements share — every version the files hold included, and of the
  glossary only the definitions of other entries — where its word stands as a word (WAY-97,
  WAY-98); the shared part's code is not searched
  (`TODO — decision pending: which decision sets that only the Markdown files of the part the
  elements share are searched`). The guard lists them, `--uses` given a word lists that word's uses
  alone, and the guard's code and tests hold what a use leaves out (WAY-97).
- The guard finds a term's forms by regular endings, which its code and tests hold; an irregular
  form, a short form ("the map" for "part map") or a verb split by its object ("read the value off")
  is found by the review of uses, never by the guard (WAY-97).
- A term's last word standing for the whole term — "fact" for "environment fact", "the map" for
  "part map" — is a use of the term that the list of uses does not show and the review of uses looks
  for; it stands in no *Avoid* (WAY-94, WAY-97). Where the files also use that word in another
  meaning, the rule for a word with two meanings applies: its other uses are rewritten, or its uses
  for the term are written as the whole term (WAY-99).
- A change to a definition goes, in the same change, through a review of the term's uses: an agent
  puts the new definition in place of the word in every use the guard lists and in every other form
  of it the agent finds, and reports each use whose meaning then moves to the human deciding the
  change (WAY-97).
- A term used by an entry on the main branch keeps its meaning: a new meaning takes a new word and a
  new entry, and whatever should carry it is rewritten (WAY-97).

## Fields and their readers

A field stays in this template only while someone or something reads it
(`TODO — decision pending: which decision keeps a field in an element's template only while it is
read`). Each field carries the mark of where its value comes from (`elements/common/rules.md`).

| Field | Who reads it, when | Where its value comes from |
|---|---|---|
| term (heading) | whoever writes a sentence of any element, which depends on the term by using its word; the format guard (`glossary-term-holder`, `glossary-term-collision`, `glossary-term-use`, `glossary-process-terms`) | judgment |
| definition | the agent reviewing the uses when it changes; whoever writes a sentence using the term; the format guard (`glossary-definition-count`, `glossary-definition-words`, `glossary-definition-uses`) | judgment |
| Avoid | whoever writes a sentence; the format guard (`glossary-avoid-growth`, `glossary-avoid-single`, `glossary-avoid-term`, `glossary-avoid-carrier`, `glossary-process-terms`) | judgment for the word; read off, from the list of uses, for whether it may stand there |
| Not | the independent assessment judging a change, which sees the foundation; the search of WAY-33; the format guard (`glossary-not-target`, `glossary-not-quoted-word`, `glossary-entry-merge-todo`) | judgment for the meaning and the word chosen; read off for whether it exists |

## Examples

`examples.md` names, by term, the entries of this repository's own glossary
(`foundations/glossary.md`) that show the form of an entry; they are read there, in the commit of
the-way a product pins, instead of being copied (WAY-09, WAY-34). The format guard checks that each
term it names is the term of an entry of that glossary (`glossary-example-target`).
