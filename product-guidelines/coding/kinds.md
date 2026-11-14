# Kinds

Where the product has code:

- **Kinds.** Name the kinds of code the product already holds files of, each
  with its files; the audit covers every one of them. On the route of one kind (step 1's mode of
  one kind whose files the product already has), name that kind alone with its files: this is the
  comparison that judges every existing file of the kind, compares them and proposes the exemplar
  with `copy` or `do not copy` for each file, the human approving the decision that designates it,
  covering that kind and no other, and no audit. Who designates the exemplar follows from the state
  of the product: a first file built with no exemplar is the file every later one copies, and with
  several files a choice made without comparing them makes whichever file an agent finds into law.
  For each kind, judge every file of it the product holds,
  compare them, and propose:
  - its exemplar, with one sentence of what the product gains by it, such as "every new endpoint
    checks its input as this one does", since the human who approves the exemplar does not judge
    code and someone who is no developer can weigh what the product gains;
  - what a script can check of that exemplar — where a file of the kind lies, what it calls, how it
    validates its input — as the kind's rules, the rest of the exemplar standing as an example
    (WAY-198);
  - `do not copy` for each file that breaks a rule the product holds or the task settles, with the
    file and line of the place that breaks it, and `copy` for every other file of the kind.
- **Findings**, in the audit and not on the route of one kind. Each place marked
  `do not copy` is a finding, with one sentence of its effect, and a file with two breaks holds two
  findings. The `do not copy` list stays apart, whole, under no limit, and tells the next agent what
  not to copy; each of its places also stands in the `Places:` of its one cause, which says what to
  fix. In the task document each `do not copy` line gains the number of that cause, so that a reader
  sees one fact seen twice and not two problems; the mark stands there alone, and the table of a
  kind's files in the product's guidelines takes none.
