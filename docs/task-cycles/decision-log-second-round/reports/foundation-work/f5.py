p = 'foundations/decisions.md'
t = open(p, encoding='utf-8', newline='').read()


def rep(old, new):
    global t
    assert t.count(old) == 1, (t.count(old), old[:70])
    t = t.replace(old, new)


# ---- WAY-288 <- WAY-292
rep(r"""A request's description is written in English, and its top part stands a second time, in the
language of the task document, in a collapsed block of the description.

- **Scope:** task-cycle, agent-instructions
- **Based on:** github-collapsed-section
- **Relations:** derives from WAY-286
""", r"""A request's description is written in English, and its top part stands a second time, in the
language of the task document, in a collapsed block of the description.

Where the task document of a request is in English, the collapsed block of the request's description
holds `none` in place of a second English copy of the top part, and the form check, wherever it
reads the task document as English, holds the block to `none`.

- **Scope:** task-cycle, agent-instructions
- **Based on:** github-collapsed-section
- **Relations:** derives from WAY-286 · narrows WAY-114
""")
rep(r"""  - violates: a request opens in Polish; the human's decisions stand in English alone; the block
    holds the lower part as well, or a summary of the top part instead of the top part.
""", r"""  - violates: a request opens in Polish; the human's decisions stand in English alone; the block
    holds the lower part as well, or a summary of the top part instead of the top part.
  For the block where the task document is in English, an agent compares the request's description
  with the decision:
  - complies: a request of a task written in English keeps the block, its summary followed by
    `none`, and the form check passes it; wherever the form check reads the task document as
    English, it reports a block that repeats the top part;
  - violates: a request of an English task drops the block; its block repeats the top part in
    English; a request of a Polish task holds `none` in its block.
""")
rep(r"""time in the language the task was written in, and stays collapsed, so the request opens in English
for every other reader.
*Rejected:*""", r"""time in the language the task was written in, and stays collapsed, so the request opens in English
for every other reader. The block exists for a human who reads a long English text line by line;
where the task document is in English, that human reads the top part above it, so a second English
copy only doubles what the request shows. The block keeps its place with `none`, so the skeleton
stays the same for every request and the form check can tell a block left out from one that has
nothing to repeat.
*Rejected:*""")
rep(r"""a report in Polish in the human's notes — the cycle writes nothing outside the
repository, and the human would look in two places.
""", r"""a report in Polish in the human's notes — the cycle writes nothing outside the
repository, and the human would look in two places; the top part repeated in English in the block —
a copy that buys the reader nothing; the block left out for an English task — the skeleton would
differ by the task's language, and a missing block could not be told from one that was forgotten.
""")

# ---- WAY-316 <- WAY-317
rep(r"""clear its place after a long time, and the images of old requests then stop showing.

- **Scope:** task-cycle, project-level
- **Based on:** none
- **Relations:** derives from WAY-219 · derives from WAY-286 · derives from WAY-308
""", r"""clear its place after a long time, and the images of old requests then stop showing.

Where a change alters what a screen shows and the foundation of the product settles no place for
screenshots, the author inspects the screenshot as WAY-219 gives and the request shows none: the
section of its description for the human's decisions says that no screenshot is shown and why, and
the cycle does not stop. A screenshot left unchecked for want of a settled way to the running
product is reported as WAY-219 gives and needs no second item.

- **Scope:** task-cycle, project-level
- **Based on:** none
- **Relations:** derives from WAY-219 · derives from WAY-286 · derives from WAY-308 · derives from
  WAY-287
""")
rep(r"""    screenshots never to be cleared; a template of the-way names the place where the screenshots lie.
""", r"""    screenshots never to be cleared; a template of the-way names the place where the screenshots lie.
  For a product whose foundation settles no place for screenshots, an agent compares the cycle and
  its request with the decision:
  - complies: a product whose foundation settles a way to its running screens but no place for
    screenshots: the author inspects the screenshot, commits none and embeds none, and the request
    tells the human, in plain words, that the screen was looked at and is not shown, saying that the
    product has settled no place for screenshots, which the human accepts by merging; the cycle goes
    on to its review and its request; a product whose foundation settles no way to the running
    product: the screenshot stays unchecked for that reason in the report and the request, as
    WAY-219 gives, with no item about a place;
  - violates: the cycle stops or opens blocked for the missing place; the screenshot is committed to
    the record so that the request has something to show; the request says nothing of the missing
    screenshot, or only in its checks; the missing place is reported as the reason when the way to
    the running product is what fails.
""")
rep(r"""once its place is cleared; a product with no place settled shows no screenshot (WAY-317).
*Rejected:*""", r"""once its place is cleared; a product with no place settled shows no screenshot, and the human
accepts without seeing the screen or settles the place first. A request that shows no screenshot and
says nothing leaves the human to guess whether the screen was looked at; naming the lack in the
section for the human's decisions lets the human weigh it and make a task of settling the place.
WAY-219 refused to stop the cycle for an unsettled way to the interface, and the same holds here: a
stop comes after the change is made, when it can no longer be avoided. The case differs from that of
WAY-219: there the author cannot look at the screen, here it looks and has nowhere to put the result.
*Rejected:*""")
rep(r"""a place
never cleared, the matter returning when it grows — the evidence is looked at once, when the request
is accepted.
""", r"""a place
never cleared, the matter returning when it grows — the evidence is looked at once, when the request
is accepted; the lack of a place stopping the cycle — the stop comes after the change is made, which
WAY-219 refused for the way to the product.
""")

# ---- WAY-309 <- WAY-323
rep(r"""item it lists is made to read the same in the report and in the remarks, not appended again.

- **Scope:** task-cycle, agent-instructions, project-level""", r"""item it lists is made to read the same in the report and in the remarks, not appended again.

The script takes no `a note of the author's vault` for a note link when its first bracket stands against a letter, a
digit, a dot or an underscore on its left, when it is a character class of the shell in double
brackets, `a note of the author's vault`, with one of the twelve POSIX names between the colons (`alnum`, `alpha`,
`blank`, `cntrl`, `digit`, `graph`, `lower`, `print`, `punct`, `space`, `upper`, `xdigit`), and no
letter for the start of a drive when a backslash stands before it. It takes no text for an absolute
path when all that follows the drive letter and its colon is escape sequences of a newline, a tab or
a carriage return (`\n`, `\t`, `\r`), so a message ending in a letter, a colon and such a sequence is
not listed; a path written with a real name, a Git Bash path, a link after a space or a mark and a
text stuck to such a sequence stay listed.

- **Scope:** task-cycle, agent-instructions, project-level""")
rep(r"""    WAY-294 lists only on the cleaned copy.
- **Origin:** none
""", r"""    WAY-294 lists only on the cleaned copy.
  For what the script takes for an absolute path and for a note link, an agent compares the change
  with the decision:
  - complies: the script lists a path through a directory named `new`, written after a drive letter
    in a string of code, and a note link that follows a space; it lists nothing for a slot of a
    specification written with a dot before its brackets, for an array inside an array in code, for
    the end of a message in a string of code that ends in a letter, a colon and a newline sequence,
    or for the letters of a regular expression that stand after a backslash; it lists nothing for a
    character class of the shell in double brackets with one of the twelve names, such as
    `a note of the author's vault` in a command, and lists a note link on the same line as one;
  - violates: the script lists the slot of a specification; the script lists the end of a message
    that ends in a newline sequence; the script lists nothing for a path through a directory named
    `new` written in a string of code; the script lists nothing for a link to a note after a space;
    the script lists `a note of the author's vault`; the script lists nothing for a double-bracketed text between
    colons whose name is none of the twelve, such as the name `other`.
- **Origin:** none
""")
rep(r"""one more check in every cycle.
*Rejected:* patterns and a list of private words""", r"""one more check in every cycle. The patterns were written for the prose a cycle publishes, and code
holds shapes that look like their targets and are not. A trial on every tracked file of one public
product on 2026-11-09, with these rules and the rule of WAY-320 that a note link counts only in a
Markdown file, listed exactly the nine real paths and the one example of a Git Bash path written on
purpose, where the patterns without them had also listed 78 texts that were neither: 73 of them
`a note of the author's vault`, among them an array inside an array in code, a character class of the shell and slots
of a specification quoted word for word, and 5 the end of a message or a regular expression. Each
rule is narrow, so that what a real path or link can look like stays listed. The price taken: a
directory of the root of a disk with a one-letter name, written `n`, `t` or `r` and standing alone
after the colon, is not listed; a link stuck to a word, which Obsidian renders as a link, is not
listed; and a text stuck to an escape sequence still gives a false hit, which the product removes
by rewriting the string. A character class of the shell in double brackets is code too, though a
command quoted in a Markdown file holds it: a run of the check on 2026-11-11 over the commands in
the Markdown files of one product listed twelve such texts, all of them one of the twelve classes.
Both runs are this product's own, and their record is not open to a reader of this repository. The
twelve names are listed one by one, not matched by a general shape, so a text with another name
between the colons stays listed, since it may be a note. The price taken: a note whose title is one
of these names between colons is not listed, and a name a shell adds later needs the list changed.
*Rejected:* patterns and a list of private words""")
rep(r"""the names of a public and of a private repository look alike in text.
""", r"""the names of a public and of a private repository look alike in text; the product lists the Markdown
file holding the quoted specification among the skipped files — every real path later written in
that file of its foundation passes; no change to the rule for a link — the check of that product
fails while the quoted fact stands in its foundation, and the quote cannot be reworded, since an
environment fact quotes its source word for word; a small letter for a drive in code starts no path
— it passes every path written with a small letter, the home directory of a user in the form some
tools print it included; recognising strings and regular expressions for each language — a parser
for each language a product adds, out of proportion to the few texts it frees; no change to the
rule for a drive — the product rewrites each such string and every later message of that form hits
again, or lists its files and a real path in them passes; no exception for every double-bracketed
text between colons — a note whose title is written between colons, in double brackets, passes, a
cost the check cannot see; no exception for every `[[` that a parenthesis or another mark follows —
it cuts real links whose titles begin with a parenthesis, as a vault holds them; the exception only
in the check of tracked files — two sets of rules to keep and to describe apart, and a cycle copy
that quotes such a command still gives the false hit, which the cycle removes by rewriting it in
words.
""")

# ---- WAY-339 <- WAY-347
rep(r"""judges a version of the process by the cycles that ran on it, never one week against another.

- **Scope:** process-audit, task-cycle, gate""", r"""judges a version of the process by the cycles that ran on it, never one week against another.

The measures of how a cycle's agents use the context and the prompt cache of the model — the number
of model calls, the size of each call's context, the tokens written to the cache and the tokens
written to it again — are counted by a script of their own into a file of their own in the cycle's
record, and are never columns of the stage report.

- **Scope:** process-audit, task-cycle, gate""")
rep(r"""    a new series of the cost.
- **Origin:** none

*Rationale:* a change of the form of a stage report changes how many remarks""", r"""    a new series of the cost.
  For where the measures of context and cache use are counted, an agent compares a change with the
  decision:
  - complies: a later change that adds one more measure of context or cache use adds it to the
    script and the file of those measures, and the stage report keeps the columns it has;
  - violates: a change adds a column of context or cache use to the stage report; the script of
    those measures writes its numbers into the stage report.
- **Origin:** none

*Rationale:* a change of the form of a stage report changes how many remarks""")
rep(r"""output is what those times are read from.
*Rejected:*""", r"""output is what those times are read from. A change of the form of the stage report starts a
new series of measures, so a column added to the report for the measures of context and cache use
would end the comparison of the cost of cycles across the change, while a file of its own changes no
form of the report. The price: a second file in each cycle's record, and a second reading of the
record for the audit.
*Rejected:*""")
rep(r"""whoever reads the audit must remember it until the new runs outnumber
the old.
""", r"""whoever reads the audit must remember it until the new runs outnumber
the old. New columns of context and cache use in the stage report — a change of the form of the
stage report starts a new series of measures; a sentence added to the first paragraph saying that
adding columns starts no series — a file of its own avoids the dispute with no change to that
paragraph.
""")

# ---- WAY-368 <- WAY-369
rep(r"""the installer writes the definitions of the
pinned commit into a product, replacing and deleting only its own files, and the copies a session on
the-way itself loads are generated from them and tracked.

- **Scope:** task-cycle, installation, agent-instructions
- **Based on:** claude-code-subagent-skills-denied · claude-code-subagent-cache-ttl ·
  claude-code-subagent-agent-directories
""", r"""the installer writes the definitions of the
pinned commit into a product, replacing and deleting only its own files, and the copies a session on
the-way itself loads are generated from them and tracked.

The agent types of a task cycle start with the instruction files that Claude Code loads into an
agent of the session, the user's and the product's; no definition of a type sets the field that
starts an agent without them.

- **Scope:** task-cycle, installation, agent-instructions
- **Based on:** claude-code-subagent-skills-denied · claude-code-subagent-cache-ttl ·
  claude-code-subagent-agent-directories · claude-code-subagent-instruction-files
""")
rep(r"""    the one author's sets the hour lifetime; the installer overwrites a file of a product that is
    not its own.
""", r"""    the one author's sets the hour lifetime; the installer overwrites a file of a product that is
    not its own.
  For the start with the instruction files, an agent compares a change with the decision:
  - complies: a definition of a type holds the fields `name`, `description`, the denied tools and,
    for the one author, the cache lifetime;
  - violates: a definition sets the field that starts the agent without the instruction files.
""")
rep(r"""dispatches as before (WAY-370).
*Rejected:*""", r"""dispatches as before (WAY-370). The instruction files are the part of the start that the types keep.
The field that drops them drops the user's file, which holds the rules of git, of scripts and of
privacy, and the product's file together, and the product's file alone cannot be kept; starting
without them lowers the start by about eleven thousand tokens, to 10.5 thousand, a figure whose
conditions — version, model, tools — are not recorded. A later decision may reverse this where the
handoffs of the stages begin to name the product's instruction file themselves. The figure is this
product's own measurement, and its record is not open to a reader of this repository.
*Rejected:*""")
rep(r"""and the orchestrator chooses the type for each stage anyway.
""", r"""and the orchestrator chooses the type for each stage anyway; start without the instruction files —
the start falls to 10.5 thousand tokens, but the agent loses at once the user's global instruction
file (the rules of git, of scripts and of privacy) and the product's instruction file, and the
product's file alone cannot be kept.
""")
open(p, 'w', encoding='utf-8', newline='').write(t)
print('ok')
